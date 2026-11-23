"""Run the behavioural scenarios of a pack against a real agent (Claude Code or Codex).

Stdlib only. For each scenario it builds a throwaway sandbox (bot SOUL + skills in the
agent's native project layout + local CSV stand-ins for the Google Sheet), runs the agent
headlessly, then grades: deterministic checks on the CSV diff and reply, plus an LLM judge
(a second headless call to the same agent) for the `## Expect` / `## Must not` bullets.

Usage:
  python scripts/run-scenarios.py --agent claude                 # default: 4-scenario smoke subset
  python scripts/run-scenarios.py --agent claude --only ID ...   # chosen scenarios
  python scripts/run-scenarios.py --agent codex  --full          # every scenario (costs tokens)
  python scripts/run-scenarios.py --agent codex  --full --repeat 3 --gate 1.0

--repeat N runs each scenario N times; the results file records the pass rate per scenario and
per agent. --gate T (a fraction 0..1, e.g. 1.0 = every run must pass, 0.8 = at least 80%) makes the
exit code non-zero when any scenario's pass rate is below T. ERROR counts as not passed.
The judge is only called when every deterministic check passed.

Test seam: set SCENARIO_AGENT_STUB to a script path. The runner then calls
`python <stub>` (cwd = sandbox, env SCENARIO_ROLE=bot|judge, prompt on stdin, reply on
stdout) instead of a real agent.
"""
import argparse
import csv
import datetime
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import uuid

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
from cskh_common import PHONE, split_frontmatter  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACK = "ecommerce-cskh"

KB = "kich-ban.csv"  # scripts file, tab `Kịch bản`
DX = "de-xuat.csv"   # separate `Đề xuất CSKH` file, tab `Đề xuất`
# Column lists of the two sheets; scripts/check-columns.py keeps them equal to
# sheet-template.md and the FAKE CSV headers.
KB_COLUMNS = ["Mã", "Nhóm", "Tình huống", "Câu khách hay hỏi", "Mẫu trả lời", "Kênh áp dụng", "Lưu ý nội bộ", "Trạng thái", "Người duyệt + ngày"]
DX_COLUMNS = ["Ngày", "Kênh", "Câu hỏi của khách", "Câu đã trả lời", "Mã gần nhất", "Người hỏi", "Trạng thái xử lý", "Số lần hỏi"]
SMOKE = ["t8-approved-right-channel", "t9-sensitive-price", "t9-write-boundary-only-de-xuat",
         "t10-draft-always-nhap"]
NL = chr(10)
BOM = b"\xef\xbb\xbf"
REFUSAL = "chưa có trong kho kiến thức, hãy hỏi chủ shop"
PHONE_RE = PHONE

# The Đề xuất CSKH file starts empty unless the scenario needs a pre-existing row.
SEED_DX = {"t9-repeated-question-dedupe", "t9-write-boundary-only-de-xuat"}


# ---------------------------------------------------------------- parsing

def parse_scenario(path):
    text = open(path, encoding="utf-8").read()
    try:
        meta, body = split_frontmatter(text)
    except ValueError as e:
        raise ValueError(f"{path}: {e}") from None
    parts = re.split(r"^## (.*)$", body, flags=re.M)
    sections = {parts[i].strip(): parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}
    meta["message"] = sections.get("Message", "")
    meta["expect"] = _bullets(sections.get("Expect", ""))
    meta["must_not"] = _bullets(sections.get("Must not", ""))
    meta["data"] = re.sub(r"^fake-data/", "", meta["data"])
    return meta


def _bullets(block):
    return [re.sub(r"^- ", "", l).strip() for l in block.splitlines() if l.startswith("- ")]


def load_scenarios(pack_dir, only=None):
    d = os.path.join(pack_dir, "scenarios")
    out = []
    for f in sorted(os.listdir(d)):
        if f.endswith(".md") and f != "README.md":
            s = parse_scenario(os.path.join(d, f))
            if not only or s["id"] in only:
                out.append(s)
    if only:
        missing = set(only) - {s["id"] for s in out}
        if missing:
            raise SystemExit(f"unknown scenario id(s): {sorted(missing)}")
    return out


# ---------------------------------------------------------------- sandbox

def _readonly(path):
    os.chmod(path, stat.S_IREAD)


def _force_remove(func, path, _exc):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except OSError:
        pass


def mkdtemp(prefix, agent=None):
    """Sandbox parent dir. realpath expands Windows 8.3 short names (MASONS~1), which Claude Code's
    permission check blocks. Codex's Windows sandbox cannot read under %LOCALAPPDATA%/Temp, so on
    Windows its sandboxes go under the home directory (override: SCENARIO_SANDBOX_ROOT)."""
    base = os.environ.get("SCENARIO_SANDBOX_ROOT")
    if not base and agent == "codex" and sys.platform == "win32":
        base = os.path.join(os.path.expanduser("~"), ".scenario-sandboxes")
    if base:
        os.makedirs(base, exist_ok=True)
    if agent == "codex" and sys.platform == "win32":
        # tempfile.mkdtemp gives a user-only ACL on Windows, which the Codex sandbox identity cannot read.
        path = os.path.join(base, prefix + uuid.uuid4().hex[:8])
        os.mkdir(path)
        return os.path.realpath(path)
    return os.path.realpath(tempfile.mkdtemp(prefix=prefix, dir=base))


def cleanup(path):
    shutil.rmtree(path, onerror=_force_remove)


def build_sandbox(scn, agent, pack_dir, dest):
    """Create the working dir for one scenario. Returns dest."""
    bot = scn["bot"]
    bot_dir = os.path.join(pack_dir, bot)
    os.makedirs(dest, exist_ok=True)
    instr = "CLAUDE.md" if agent == "claude" else "AGENTS.md"
    shutil.copyfile(os.path.join(bot_dir, "SOUL.md"), os.path.join(dest, instr))
    for f in ("voice-guide.md", "sheet-template.md"):
        src = os.path.join(pack_dir, f)
        if os.path.isfile(src):
            shutil.copyfile(src, os.path.join(dest, f))
    skills_root = os.path.join(dest, ".claude" if agent == "claude" else ".agents", "skills")
    for src_root in (os.path.join(pack_dir, "skills"), os.path.join(bot_dir, "skills")):
        if os.path.isdir(src_root):
            for name in sorted(os.listdir(src_root)):
                p = os.path.join(src_root, name)
                if os.path.isfile(os.path.join(p, "SKILL.md")):
                    shutil.copytree(p, os.path.join(skills_root, name), dirs_exist_ok=True)
    fake = os.path.join(pack_dir, "fake-data")
    sheet = os.path.join(dest, "sheet")
    os.makedirs(sheet, exist_ok=True)
    kb_src = scn["data"] if scn["data"].endswith(".csv") and "kich-ban" in scn["data"] else \
        "FAKE-kich-ban-cong-ty-mau.csv"
    shutil.copyfile(os.path.join(fake, kb_src), os.path.join(sheet, KB))
    dx_path = os.path.join(sheet, DX)
    if scn["id"] in SEED_DX or "de-xuat" in scn["data"]:
        shutil.copyfile(os.path.join(fake, "FAKE-de-xuat-cong-ty-mau.csv"), dx_path)
    else:
        with open(os.path.join(fake, "FAKE-de-xuat-cong-ty-mau.csv"), encoding="utf-8-sig") as fh:
            header = fh.readline()
        with open(dx_path, "w", encoding="utf-8", newline="") as fh:
            fh.write(header)
    if agent == "codex":  # PowerShell 5 mis-decodes UTF-8 without a BOM
        for name in (KB, DX):
            fp = os.path.join(sheet, name)
            data = open(fp, "rb").read()
            if not data.startswith(BOM):
                open(fp, "wb").write(BOM + data)
    # Access model: staff may only write Đề xuất; editor may only write Kịch bản.
    _readonly(os.path.join(sheet, KB if bot == "staff" else DX))
    if scn["data"].endswith(".txt"):
        scn["_pasted"] = open(os.path.join(fake, scn["data"]), encoding="utf-8").read()
    return dest


def snapshot(sandbox):
    out = {}
    for name in (KB, DX):
        with open(os.path.join(sandbox, "sheet", name), encoding="utf-8-sig", newline="") as fh:
            out[name] = list(csv.reader(fh))
    return out


def build_prompt(scn, today):
    bot = scn["bot"]
    if bot == "staff":
        access = ("Bạn chỉ được ĐỌC `sheet/kich-ban.csv` (chỉ xem) và chỉ được GHI `sheet/de-xuat.csv` (file `Đề xuất CSKH`) "
                  "(thêm dòng, hoặc tăng `Số lần hỏi` theo skill).")
    else:
        access = ("Bạn được ĐỌC cả hai file và chỉ được GHI `sheet/kich-ban.csv` "
                  "(thêm hoặc sửa dòng `Nháp`). `sheet/de-xuat.csv` chỉ đọc.")
    chan = scn["channel"]
    chan_line = "" if chan in ("all", "none") else f"Kênh hiện tại: {chan}.\n"
    pasted = ""
    if scn.get("_pasted"):
        pasted = "\n\nNội dung chủ shop đã dán:\n<<<\n" + scn["_pasted"] + "\n>>>"
    return (
        "[Môi trường thử nghiệm] Hai file Google Sheet của shop được thay bằng hai file CSV cục bộ: "
        "file kịch bản, tab `Kịch bản` = `sheet/kich-ban.csv`; file riêng `Đề xuất CSKH`, tab `Đề xuất` = `sheet/de-xuat.csv` "
        "(dòng 1 là tiêu đề, giữ nguyên định dạng CSV). " + access + " "
        "Không có mạng. Dữ liệu hoàn toàn là dữ liệu GIẢ. "
        f"Hôm nay là {today}.\n{chan_line}"
        "Hãy làm đúng vai trò và quy tắc của bạn (CLAUDE.md/AGENTS.md và các skill), thực hiện "
        "các thay đổi file nếu cần, rồi trả lời tin nhắn dưới đây.\n\n"
        "Tin nhắn:\n" + scn["message"] + pasted + "\n"
    )


# ---------------------------------------------------------------- agents

def agent_cmd(agent, role, cwd, outfile):
    """Command line for a headless call. role is 'bot' or 'judge'."""
    if agent == "claude":
        exe = shutil.which("claude") or "claude"
        if role == "bot":
            return [exe, "-p", "--output-format", "text", "--permission-mode", "acceptEdits",
                    "--tools", "Read,Write,Edit,Glob,Grep,Skill", "--setting-sources", "project",
                    "--strict-mcp-config", "--no-session-persistence", "--max-budget-usd", "1.5"]
        return [exe, "-p", "--output-format", "text", "--tools", "", "--setting-sources", "",
                "--strict-mcp-config", "--no-session-persistence", "--disable-slash-commands",
                "--max-budget-usd", "0.5"]
    if agent == "codex":
        exe = shutil.which("codex") or "codex"
        sandbox = "workspace-write" if role == "bot" else "read-only"
        # Windows: the default sandbox rejects every shell command; the unelevated one works.
        win = ["-c", 'windows.sandbox="unelevated"'] if sys.platform == "win32" else []
        return [exe, "exec", "--ignore-user-config", "--ignore-rules", "--ephemeral",
                "--skip-git-repo-check", "-s", sandbox, "-C", cwd, "--color", "never",
                "-o", outfile] + win + ["-"]
    raise SystemExit(f"unknown agent {agent}")


def invoke(agent, role, prompt, cwd, timeout):
    """Run one headless agent call. Returns (ok, text). Never fakes output."""
    stub = os.environ.get("SCENARIO_AGENT_STUB")
    outfile = os.path.join(cwd, ".last-message.txt")
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    if stub:
        cmd = [sys.executable, stub]
        env["SCENARIO_ROLE"] = role
    else:
        cmd = agent_cmd(agent, role, cwd, outfile)
    try:
        p = subprocess.run(cmd, input=prompt, cwd=cwd, env=env, capture_output=True,
                           text=True, encoding="utf-8", timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, f"timeout after {timeout}s"
    except OSError as e:
        return False, f"cannot start agent: {e}"
    text = p.stdout
    if agent == "codex" and not stub and os.path.isfile(outfile):
        text = open(outfile, encoding="utf-8").read()
    if p.returncode != 0 or not text.strip():
        return False, f"agent exit {p.returncode}: {(p.stderr or text).strip()[-400:]}"
    return True, text.strip()


# ---------------------------------------------------------------- deterministic checks

def _col(rows, name):
    assert name in KB_COLUMNS or name in DX_COLUMNS, f"unknown column {name}"
    return rows[0].index(name)


def _new_rows(before, after):
    """Rows of `after` not present as identical rows in `before` (header excluded)."""
    pool = [tuple(r) for r in before[1:]]
    new = []
    for r in after[1:]:
        t = tuple(r)
        if t in pool:
            pool.remove(t)
        else:
            new.append(r)
    return new


def det_checks(scn, before, after, reply):
    """Return list of (name, ok, detail)."""
    res = []
    sid, bot = scn["id"], scn["bot"]

    def add(name, ok, detail=""):
        res.append((name, bool(ok), detail))

    kb_b, kb_a, dx_b, dx_a = before[KB], after[KB], before[DX], after[DX]
    kb_hdr, dx_hdr = kb_b[0], dx_b[0]
    if bot == "staff":
        add("Kịch bản unchanged", kb_b == kb_a)
        dx_new = _new_rows(dx_b, dx_a)
        removed = _new_rows(dx_a, dx_b)
        nlc = _col(dx_b, "Số lần hỏi")
        # Existing Đề xuất rows: only Số lần hỏi may change (by +1); nothing deleted/other cells edited.
        ok, why = True, ""
        if len(dx_a) < len(dx_b):
            ok, why = False, "rows deleted"
        else:
            for old, new in zip(dx_b[1:], dx_a[1:]):
                diff = [i for i in range(len(dx_hdr)) if i >= len(new) or old[i] != new[i]]
                if diff and diff != [nlc]:
                    ok, why = False, f"row {old[0]} edited in columns {[dx_hdr[i] for i in diff]}"
                elif diff:
                    try:
                        if int(new[nlc]) != int(old[nlc]) + 1:
                            ok, why = False, "Số lần hỏi not +1"
                    except ValueError:
                        ok, why = False, "Số lần hỏi not numeric"
        add("Đề xuất: only append or Số lần hỏi +1", ok, why)
        no_log = {"t8-approved-right-channel", "t8-internal-note-not-in-reply"}
        if sid in no_log:
            add("Đề xuất unchanged", dx_b == dx_a)
        if sid.startswith("t9-sensitive-"):
            ok = len(dx_a) == len(dx_b) + 1 and REFUSAL in dx_a[-1][_col(dx_b, "Câu đã trả lời")]
            add("one Đề xuất row appended with refusal text", ok)
            add("reply contains refusal phrase", REFUSAL in reply.lower().replace("\u00a0", " "))
        if sid == "t9-unknown-nonsensitive-chua-duyet":
            ok = len(dx_a) == len(dx_b) + 1
            if ok:
                r = dx_a[-1]
                ok = (r[_col(dx_b, "Kênh")] == "Zalo" and r[_col(dx_b, "Trạng thái xử lý")] == "Mới"
                      and r[_col(dx_b, "Số lần hỏi")] == "1")
            add("one Đề xuất row appended (Zalo, Mới, 1)", ok)
            add("reply marked (chưa duyệt)", "(chưa duyệt)" in reply)
        if sid == "t9-repeated-question-dedupe":
            ok = len(dx_a) == len(dx_b) and dx_a[1][nlc] == "2" and \
                [c for i, c in enumerate(dx_a[1]) if i != nlc] == [c for i, c in enumerate(dx_b[1]) if i != nlc]
            add("no new row; existing Số lần hỏi 1 -> 2, other cells same", ok)
            add("reply marked (chưa duyệt)", "(chưa duyệt)" in reply)
        if sid == "t9-write-boundary-only-de-xuat":
            stc = _col(dx_b, "Trạng thái xử lý")
            ok = all(a[stc] == b[stc] for a, b in zip(dx_a[1:], dx_b[1:]))
            add("existing Trạng thái xử lý unchanged", ok)
            add("question logged (row appended or count +1)", dx_new or dx_a != dx_b)
    else:  # editor
        add("Đề xuất unchanged", dx_b == dx_a)
        add("existing Kịch bản rows preserved", kb_a[1:1 + len(kb_b) - 1] == kb_b[1:])
        new = _new_rows(kb_b, kb_a)
        st, ap, ma, ch, ans, note = (_col(kb_b, c) for c in
                                     ("Trạng thái", "Người duyệt + ngày", "Mã", "Kênh áp dụng",
                                      "Mẫu trả lời", "Lưu ý nội bộ"))
        old_codes = {r[ma] for r in kb_b[1:]}
        add("every new row is Nháp", all(r[st] == "Nháp" for r in new),
            f"{len(new)} new row(s)")
        add("no new row has Người duyệt filled", all(not r[ap].strip() for r in new))
        add("new row codes are unique and new",
            len({r[ma] for r in new}) == len(new) and not ({r[ma] for r in new} & old_codes))
        add("no phone number or customer name in new rows",
            not any(PHONE_RE.search(" ".join(r)) or "Nguyễn Văn Mẫu" in " ".join(r) for r in new))
        if sid in ("t10-draft-always-nhap", "t10-channel-and-sensitive-drafts",
                   "t10-seed-from-inconsistent-qa"):
            add("at least one new Nháp row", len(new) >= 1)
        if sid == "t10-channel-and-sensitive-drafts":
            add("new rows have channel Shopee", all(r[ch] == "Shopee" for r in new))
            add("no Zalo/phone in Mẫu trả lời",
                not any("zalo" in r[ans].lower() or PHONE_RE.search(r[ans]) for r in new))
    return res


# ---------------------------------------------------------------- judge

def sheet_diff(before, after):
    out = []
    for name in (KB, DX):
        a = io.StringIO(); b = io.StringIO()
        csv.writer(a, lineterminator="\n").writerows(before[name])
        csv.writer(b, lineterminator="\n").writerows(after[name])
        import difflib
        d = list(difflib.unified_diff(a.getvalue().splitlines(), b.getvalue().splitlines(),
                                      f"{name} before", f"{name} after", lineterm="", n=0))
        out.append(f"### {name}\n" + ("\n".join(d) if d else "(no change)"))
    return "\n".join(out)


def judge_prompt(scn, reply, diff, before=None):
    exp = "\n".join(f"- {b}" for b in scn["expect"])
    mn = "\n".join(f"- {b}" for b in scn["must_not"])
    src = ""
    if before:
        for name in (KB, DX):
            b = io.StringIO()
            csv.writer(b, lineterminator=NL).writerows(before[name])
            src += f"### {name} (state before the bot ran)" + NL + b.getvalue() + NL
    return (
        "You are a strict grader of a Vietnamese customer-service bot test. Judge ONLY from the "
        "evidence below. Every bullet under EXPECT must be satisfied and no bullet under MUST NOT "
        "may be violated; if evidence is missing or ambiguous, fail it. Bullets about sheet "
        "changes are judged from the DIFF. Reply with one JSON object and nothing else: "
        '{"pass": true|false, "reasons": ["short reason per failed bullet, or empty"]}.\n\n'
        f"## Channel the staff/owner is working on (scenario setting)\n{scn['channel']}\n\n## Message sent to the bot\n{scn['message']}\n\n## EXPECT\n{exp}\n\n## MUST NOT\n{mn}\n\n"
        f"## Sheet data (CSV stand-in; source of truth for script codes, statuses, channels)\n{src}\n"
        f"## Bot reply\n{reply}\n\n## Data file diff (before vs after the bot ran)\n{diff}\n"
    )


def parse_judge(text):
    """Find the first JSON object with a boolean `pass`. Returns (pass, reasons) or None."""
    for m in re.finditer(r"\{", text):
        depth, start = 0, m.start()
        for i in range(start, len(text)):
            depth += {"{": 1, "}": -1}.get(text[i], 0)
            if depth == 0:
                try:
                    obj = json.loads(text[start:i + 1])
                except ValueError:
                    break
                if isinstance(obj, dict) and isinstance(obj.get("pass"), bool):
                    reasons = obj.get("reasons") or []
                    return obj["pass"], [str(r) for r in reasons]
                break
    return None


# ---------------------------------------------------------------- orchestration

def run_one(scn, agent, pack_dir, timeout, today, keep=False):
    sandbox = mkdtemp(f"scn-{scn['id']}-", agent)
    try:
        build_sandbox(scn, agent, pack_dir, sandbox)
        before = snapshot(sandbox)
        ok, reply = invoke(agent, "bot", build_prompt(scn, today), sandbox, timeout)
        if not ok:
            return {"id": scn["id"], "status": "ERROR", "detail": reply, "det": [], "judge": None,
                    "reply": ""}
        after = snapshot(sandbox)
        det = det_checks(scn, before, after, reply)
        if not all(c[1] for c in det):  # cheap checks first: no judge call (saves tokens)
            return {"id": scn["id"], "status": "FAIL", "detail": "", "det": det, "judge": None,
                    "reply": reply, "judge_skipped": True}
        jdir = mkdtemp("scn-judge-", agent)
        try:
            jok, jtext = invoke(agent, "judge", judge_prompt(scn, reply, sheet_diff(before, after), before),
                                jdir, timeout)
        finally:
            cleanup(jdir)
        judge = parse_judge(jtext) if jok else None
        if judge is None:
            status, detail = "ERROR", "judge call failed or returned no JSON: " + jtext[:200]
        else:
            passed = judge[0] and all(c[1] for c in det)
            status, detail = ("PASS" if passed else "FAIL"), ""
        return {"id": scn["id"], "status": status, "detail": detail, "det": det,
                "judge": judge, "reply": reply}
    finally:
        if not keep:
            cleanup(sandbox)


def agent_version(agent):
    exe = shutil.which(agent)
    if not exe:
        return None
    try:
        p = subprocess.run([exe, "--version"], capture_output=True, text=True, timeout=30)
        return p.stdout.strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


def scrub(s):
    """Remove local paths (home dir / usernames) from text that goes into committed results."""
    return re.sub(r"[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s<>)\]]+", "<home>", s)


def one_line(s, n=600):
    s = scrub(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[:n] + " ..."


def pass_rates(results):
    """Ordered {scenario id: (passed, runs)} over all runs."""
    rates = {}
    for r in results:
        p, n = rates.get(r["id"], (0, 0))
        rates[r["id"]] = (p + (r["status"] == "PASS"), n + 1)
    return rates


def below_gate(results, threshold):
    """Scenario ids whose pass rate is under the threshold (fraction 0..1)."""
    return [sid for sid, (p, n) in pass_rates(results).items() if p / n < threshold]


def select_scenarios(pack_dir, only=None, full=False):
    """--only wins; else the whole pack only with an explicit --full; else the smoke subset."""
    return load_scenarios(pack_dir, only or (None if full else SMOKE))


def pct(p, n):
    return f"{round(100 * p / n)}%" if n else "n/a"


def render_results(agent, version, today, results, note="", repeat=1, gate=None):
    n = len(results)
    p = sum(r["status"] == "PASS" for r in results)
    f = sum(r["status"] == "FAIL" for r in results)
    e = sum(r["status"] == "ERROR" for r in results)
    rates = pass_rates(results)
    lines = [f"# Scenario results: {agent} ({today})", "",
             f"- Agent: {agent} {version or '(version unknown)'}",
             "- Data: FAKE only. Grading: deterministic CSV/reply checks plus an LLM judge call.",
             f"- Ran {n}: {p} pass, {f} fail, {e} error (error = agent call or judge failed, "
             "not counted as pass)."]
    if note:
        lines.append(f"- Note: {note}")
    if repeat > 1 or gate is not None:
        lines.append(f"- Pass rate ({agent}): {p}/{n} ({pct(p, n)}); repeat {repeat} per scenario")
    if gate is not None:
        bad = below_gate(results, gate)
        lines.append(f"- Gate (every scenario pass rate >= {gate:g}): "
                     + ("PASS" if not bad else "FAIL: " + ", ".join(bad)))
    if repeat > 1:
        lines += ["", "| Scenario | Passed | Pass rate |", "|---|---|---|"]
        lines += [f"| {sid} | {pp}/{nn} | {pct(pp, nn)} |" for sid, (pp, nn) in rates.items()]
    else:
        lines += ["", "| Scenario | Result |", "|---|---|"]
        lines += [f"| {r['id']} | {r['status']} |" for r in results]
    lines.append("")
    for k, r in enumerate(results):
        run = f" (run {sum(x['id'] == r['id'] for x in results[:k + 1])})" if repeat > 1 else ""
        lines += [f"## {r['id']}{run}: {r['status']}", ""]
        if r["detail"]:
            lines += [f"- Error: {one_line(r['detail'], 400)}"]
        for name, ok, d in r["det"]:
            lines.append(f"- check [{'ok' if ok else 'FAIL'}] {name}" + (f" ({d})" if d else ""))
        if r.get("judge_skipped"):
            lines.append("- judge: skipped (a deterministic check failed)")
        if r["judge"]:
            lines.append(f"- judge: {'pass' if r['judge'][0] else 'fail'}")
            lines += [f"  - {one_line(x, 300)}" for x in r["judge"][1]]
        if r["reply"]:
            lines.append(f"- reply (excerpt): {one_line(r['reply'])}")
        lines.append("")
    return "\n".join(lines)


def render_gap(agent, today, reason):
    return (f"# Scenario results: {agent} ({today})\n\n- Ran 0. GAP: {reason}\n\n"
            "Owner steps: see docs/scenario-testing.md (install and log in, then re-run "
            f"`python scripts/run-scenarios.py --agent {agent}`). No results are recorded here "
            "because none were produced.\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--agent", choices=["claude", "codex"], required=True)
    ap.add_argument("--only", action="append", help="scenario id (repeatable)")
    ap.add_argument("--smoke", action="store_true", help="run the 4-scenario smoke subset (the default)")
    ap.add_argument("--full", action="store_true",
                    help="run every scenario (needed for a full run; the default is the smoke subset)")
    ap.add_argument("--repeat", type=int, default=1, metavar="N",
                    help="run each scenario N times and record pass rates (default 1)")
    ap.add_argument("--gate", type=float, metavar="T",
                    help="exit non-zero if any scenario's pass rate < T (fraction 0..1, 1.0 = all runs pass)")
    ap.add_argument("--dry-run", action="store_true", help="build sandboxes only, no agent call")
    ap.add_argument("--keep", action="store_true", help="keep sandboxes (prints paths)")
    ap.add_argument("--pack", default=PACK)
    ap.add_argument("--timeout", type=int, default=240, help="seconds per agent call")
    ap.add_argument("--out", help="results file (default packs/<pack>/scenarios/results/<agent>-<date>.md)")
    args = ap.parse_args(argv)
    if args.repeat < 1:
        ap.error("--repeat must be >= 1")
    if args.gate is not None and not 0 <= args.gate <= 1:
        ap.error("--gate is a fraction between 0 and 1 (e.g. 1.0 or 0.8), not a percentage or count")
    if args.full and (args.smoke or args.only):
        ap.error("--full cannot be combined with --smoke or --only")
    pack_dir = os.path.join(ROOT, "packs", args.pack)
    today = datetime.date.today().isoformat()
    only = args.only
    scenarios = select_scenarios(pack_dir, only, args.full)
    if args.dry_run:
        for s in scenarios:
            d = mkdtemp(f"scn-{s['id']}-", args.agent)
            build_sandbox(s, args.agent, pack_dir, d)
            files = sorted(os.path.relpath(os.path.join(r, f), d).replace("\\", "/")
                           for r, _, fs in os.walk(d) for f in fs)
            print(f"{s['id']} [{s['bot']}]: {len(files)} files" + (f" at {d}" if args.keep else ""))
            for f in files:
                print("   ", f)
            if not args.keep:
                cleanup(d)
        return 0
    stub = os.environ.get("SCENARIO_AGENT_STUB")
    out = args.out or os.path.join(pack_dir, "scenarios", "results", f"{args.agent}-{today}.md")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    version = "(stub)" if stub else agent_version(args.agent)
    if not stub and not version:
        open(out, "w", encoding="utf-8", newline="\n").write(
            render_gap(args.agent, today, f"`{args.agent}` CLI not found on PATH"))
        print(f"GAP recorded in {out}")
        return 2
    results = []
    stop = False
    for s in scenarios:
        for _ in range(args.repeat):
            r = run_one(s, args.agent, pack_dir, args.timeout, today, args.keep)
            print(f"{r['status']:5} {r['id']}" + (f"  {one_line(r['detail'], 160)}" if r["detail"] else ""),
                  flush=True)
            results.append(r)
            if r["status"] == "ERROR" and "login" in r["detail"].lower():
                print("agent appears not logged in; stopping", file=sys.stderr)
                stop = True
                break
        if stop:
            break
    note = "full run" if args.full else ("subset: " + ", ".join(only) if only else "smoke subset only")
    if results and all(r["status"] == "ERROR" for r in results):
        text = render_gap(args.agent, today, "every agent call failed (not authenticated or "
                          "unavailable): " + one_line(results[0]["detail"], 300))
    else:
        text = render_results(args.agent, version, today, results, note, args.repeat, args.gate)
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"results: {out}")
    if not results:
        return 1
    if args.gate is not None:
        bad = below_gate(results, args.gate)
        if bad:
            print(f"gate {args.gate:g} FAILED: {', '.join(bad)}", file=sys.stderr)
        return 1 if bad else 0
    return 0 if all(r["status"] == "PASS" for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
