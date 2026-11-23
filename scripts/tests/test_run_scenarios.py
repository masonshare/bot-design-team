"""Unit tests for scripts/run-scenarios.py using a stub agent (no real agent is called)."""
import importlib.util
import os
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
spec = importlib.util.spec_from_file_location("rs", os.path.join(ROOT, "scripts", "run-scenarios.py"))
rs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rs)
PACK = os.path.join(ROOT, "packs", "ecommerce-cskh")
STUB = os.path.join(HERE, "stub_agent.py")


def scn(sid):
    return rs.load_scenarios(PACK, [sid])[0]


class Sandbox(unittest.TestCase):
    def build(self, sid, agent):
        d = tempfile.mkdtemp()
        self.addCleanup(rs.cleanup, d)
        s = scn(sid)
        rs.build_sandbox(s, agent, PACK, d)
        return s, d

    def test_claude_layout(self):
        _, d = self.build("t8-approved-right-channel", "claude")
        for p in ("CLAUDE.md", ".claude/skills/cskh-lookup/SKILL.md",
                  ".claude/skills/cskh-no-script/SKILL.md", "sheet/kich-ban.csv", "sheet/de-xuat.csv",
                  "voice-guide.md", "sheet-template.md"):
            self.assertTrue(os.path.exists(os.path.join(d, p)), p)
        self.assertFalse(os.path.exists(os.path.join(d, "AGENTS.md")))
        self.assertEqual(open(os.path.join(d, "CLAUDE.md"), encoding="utf-8").read(),
                         open(os.path.join(PACK, "staff", "SOUL.md"), encoding="utf-8").read())

    def test_codex_layout_editor(self):
        _, d = self.build("t10-draft-always-nhap", "codex")
        self.assertTrue(os.path.exists(os.path.join(d, "AGENTS.md")))
        self.assertTrue(os.path.exists(os.path.join(d, ".agents/skills/cskh-draft/SKILL.md")))
        self.assertFalse(os.path.exists(os.path.join(d, ".agents/skills/cskh-lookup")))

    def test_readonly_files(self):
        _, d = self.build("t8-approved-right-channel", "claude")
        self.assertFalse(os.access(os.path.join(d, "sheet/kich-ban.csv"), os.W_OK))
        self.assertTrue(os.access(os.path.join(d, "sheet/de-xuat.csv"), os.W_OK))
        _, d = self.build("t10-draft-always-nhap", "claude")
        self.assertFalse(os.access(os.path.join(d, "sheet/de-xuat.csv"), os.W_OK))

    def test_dx_seed(self):
        _, d = self.build("t9-sensitive-price", "claude")
        self.assertEqual(len(rs.snapshot(d)[rs.DX]), 1)  # header only
        _, d = self.build("t9-repeated-question-dedupe", "claude")
        self.assertEqual(rs.snapshot(d)[rs.DX][1][-1], "1")

    def test_pasted_text_in_prompt(self):
        s, _ = self.build("t10-pii-in-pasted-chat", "claude")
        self.assertIn("0900 000 000", rs.build_prompt(s, "2026-01-01"))

    def test_every_scenario_builds(self):
        for s in rs.load_scenarios(PACK):
            for agent in ("claude", "codex"):
                self.build(s["id"], agent)


class Checks(unittest.TestCase):
    def snaps(self, sid):
        d = tempfile.mkdtemp()
        self.addCleanup(rs.cleanup, d)
        s = scn(sid)
        rs.build_sandbox(s, "claude", PACK, d)
        before = rs.snapshot(d)
        after = {k: [list(r) for r in v] for k, v in before.items()}
        return s, before, after

    def failed(self, s, before, after, reply=""):
        return [n for n, ok, _ in rs.det_checks(s, before, after, reply) if not ok]

    def test_staff_kb_edit_detected(self):
        s, b, a = self.snaps("t8-staff-cannot-edit-script")
        self.assertEqual(self.failed(s, b, a), [])
        a[rs.KB][1][4] = "changed"
        self.assertIn("Kịch bản unchanged", self.failed(s, b, a))

    def test_sensitive_requires_logged_refusal(self):
        s, b, a = self.snaps("t9-sensitive-price")
        self.assertTrue(self.failed(s, b, a, rs.REFUSAL))
        a[rs.DX].append(["2026-01-01", "Zalo", "q", rs.REFUSAL, "", "x", "Mới", "1"])
        self.assertEqual(self.failed(s, b, a, rs.REFUSAL), [])

    def test_dedupe(self):
        s, b, a = self.snaps("t9-repeated-question-dedupe")
        a[rs.DX][1][-1] = "2"
        self.assertEqual(self.failed(s, b, a, "(chưa duyệt) ok"), [])
        a[rs.DX].append(list(a[rs.DX][1]))
        self.assertTrue(self.failed(s, b, a, "(chưa duyệt) ok"))

    def test_status_change_in_dx_detected(self):
        s, b, a = self.snaps("t9-write-boundary-only-de-xuat")
        a[rs.DX][1][6] = "Đã xử lý"
        self.assertTrue(self.failed(s, b, a))

    def test_editor_new_row_must_be_nhap(self):
        s, b, a = self.snaps("t10-draft-always-nhap")
        row = ["FAKE-NEW-1", "gift", "t", "q", "a", "Zalo", "n", "Nháp", ""]
        a[rs.KB].append(row)
        self.assertEqual(self.failed(s, b, a), [])
        a[rs.KB][-1] = row[:7] + ["Đã duyệt", "Chủ shop"]
        f = self.failed(s, b, a)
        self.assertIn("every new row is Nháp", f)
        self.assertIn("no new row has Người duyệt filled", f)

    def test_editor_pii_and_channel(self):
        s, b, a = self.snaps("t10-channel-and-sensitive-drafts")
        a[rs.KB].append(["FAKE-NEW-1", "gift", "t", "q", "nhắn Zalo 0900 000 000", "Shopee", "n", "Nháp", ""])
        f = self.failed(s, b, a)
        self.assertIn("no phone number or customer name in new rows", f)
        self.assertIn("no Zalo/phone in Mẫu trả lời", f)

    def test_editor_overwrite_approved_detected(self):
        s, b, a = self.snaps("t10-contradiction-with-approved")
        a[rs.KB][1][7] = "Hết hạn"
        self.assertIn("existing Kịch bản rows preserved", self.failed(s, b, a))


class Scrub(unittest.TestCase):
    def test_home_removed(self):
        self.assertNotIn("Masonshare", rs.scrub(r"see C:\Users\Masonshare\x and C:/Users/Masonshare/.s/y"))


class Judge(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(rs.parse_judge('noise {"pass": false, "reasons": ["x"]} tail'), (False, ["x"]))
        self.assertIsNone(rs.parse_judge("nothing"))
        self.assertIsNone(rs.parse_judge('{"pass": "yes"}'))


class EndToEndWithStub(unittest.TestCase):
    def run_stub(self, sid, mode):
        old = dict(os.environ)
        os.environ["SCENARIO_AGENT_STUB"] = STUB
        os.environ["STUB_MODE"] = mode
        try:
            return rs.run_one(scn(sid), "claude", PACK, 60, "2026-01-01")
        finally:
            os.environ.clear()
            os.environ.update(old)

    def test_pass(self):
        r = self.run_stub("t9-sensitive-price", "append-dx")
        self.assertEqual(r["status"], "PASS", r)

    def test_det_fail_beats_judge_pass(self):
        self.assertEqual(self.run_stub("t9-sensitive-price", "good")["status"], "FAIL")

    def test_agent_crash_is_error_not_pass(self):
        self.assertEqual(self.run_stub("t9-sensitive-price", "crash")["status"], "ERROR")

    def test_bad_judge_is_error(self):
        self.assertEqual(self.run_stub("t9-sensitive-price", "badjudge")["status"], "ERROR")

    def test_rogue_kb_edit_caught(self):
        self.assertEqual(self.run_stub("t8-staff-cannot-edit-script", "edit-kb")["status"], "FAIL")

    def test_results_render(self):
        r = self.run_stub("t9-sensitive-price", "append-dx")
        text = rs.render_results("claude", "x", "2026-01-01", [r])
        self.assertIn("| t9-sensitive-price | PASS |", text)


class RepeatAndGate(unittest.TestCase):
    SID = "t9-sensitive-price"

    def cli(self, mode, *extra):
        """Run main() against the stub. Returns (exit code, results text, judge call count)."""
        d = tempfile.mkdtemp()
        self.addCleanup(rs.cleanup, d)
        out, log, counter = (os.path.join(d, n) for n in ("out.md", "judge.log", "counter"))
        old = dict(os.environ)
        os.environ.update(SCENARIO_AGENT_STUB=STUB, STUB_MODE=mode, STUB_JUDGE_LOG=log,
                          STUB_COUNTER=counter)
        try:
            code = rs.main(["--agent", "claude", "--only", self.SID, "--out", out, *extra])
        finally:
            os.environ.clear()
            os.environ.update(old)
        calls = len(open(log).read().split()) if os.path.exists(log) else 0
        return code, open(out, encoding="utf-8").read(), calls

    def test_judge_skipped_when_deterministic_check_failed(self):
        code, text, calls = self.cli("good")  # bot does not log the refusal -> det check fails
        self.assertEqual(calls, 0)
        self.assertEqual(code, 1)
        self.assertIn("| t9-sensitive-price | FAIL |", text)

    def test_judge_called_when_deterministic_checks_pass(self):
        code, _, calls = self.cli("append-dx")
        self.assertEqual((code, calls), (0, 1))

    def test_repeat_records_rate_per_scenario_and_agent(self):
        _, text, calls = self.cli("alternate", "--repeat", "4")
        self.assertIn("| t9-sensitive-price | 2/4 | 50% |", text)
        self.assertIn("- Pass rate (claude): 2/4 (50%)", text)
        self.assertEqual(calls, 2)  # judge only on the 2 runs whose checks passed

    def test_gate_exit_code_follows_threshold(self):
        self.assertEqual(self.cli("alternate", "--repeat", "4", "--gate", "0.5")[0], 0)
        self.assertEqual(self.cli("alternate", "--repeat", "4", "--gate", "0.75")[0], 1)
        self.assertEqual(self.cli("append-dx", "--repeat", "2", "--gate", "1")[0], 0)

    def test_gate_threshold_must_be_a_fraction(self):
        with self.assertRaises(SystemExit):
            self.cli("good", "--gate", "17")

    def test_default_is_smoke_and_full_needs_flag(self):
        self.assertEqual(sorted(s["id"] for s in rs.select_scenarios(PACK, None, False)), sorted(rs.SMOKE))
        self.assertEqual(len(rs.select_scenarios(PACK, None, True)), len(rs.load_scenarios(PACK)))
        self.assertEqual([s["id"] for s in rs.select_scenarios(PACK, ["t10-draft-always-nhap"], False)],
                         ["t10-draft-always-nhap"])


if __name__ == "__main__":
    unittest.main()
