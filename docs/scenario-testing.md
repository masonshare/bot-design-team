# Scenario testing (ecommerce-cskh)

Behavioural tests for the two bots (staff, editor) against FAKE data, run on both Claude Code and Codex. This is testing seam 2 of spec #14. Scenarios live in `packs/ecommerce-cskh/scenarios/` (format in its `README.md`); the runner is `scripts/run-scenarios.py` (Python standard library only).

## Ship gate

The gate has two levels. A missing results file, or one that records a gap, means the level is not met.

- Owner pilot: may proceed with the Claude-based owner bot (every scenario passes on `claude`: 0 fail, 0 error) while Codex is at 14/17.
- Staff handoff: BEFORE the bot is handed to ONE staff member (staff run Codex), the Codex suite must pass 17/17 stably, meaning at least 3 consecutive full runs each with 0 fail, 0 error. Tracked in issue #29 (Tighten the 3 Codex-failing scenarios). Any change to a bot instruction or skill restarts the count.

## What the runner does

For each scenario it:

1. Builds a throwaway sandbox: the bot's `SOUL.md` as `CLAUDE.md` (Claude Code) or `AGENTS.md` (Codex), its skills in `.claude/skills/<name>` or `.agents/skills/<name>`, `voice-guide.md`, `sheet-template.md`, and CSV stand-ins for the Google Sheet (`sheet/kich-ban.csv` = tab `Kịch bản` of the scripts file, `sheet/de-xuat.csv` = the separate `Đề xuất CSKH` file) copied from `fake-data/`.
2. Enforces the access model: staff may write only `de-xuat.csv` (the `Đề xuất CSKH` file) and the scripts file `kich-ban.csv` is read-only for them; editor may write only `kich-ban.csv`. The other file is read-only, and the CSVs are diffed after the run anyway.
3. Runs the agent headlessly (no network, only file tools for Claude Code, workspace-write sandbox for Codex) with the scenario message.
4. Grades twice: deterministic checks on the CSV diff and reply (for example `Kịch bản` unchanged for staff, new editor rows are `Nháp` with no approver, `Đề xuất` row appended or count +1, no phone/name in new rows), then a second headless call to the same agent as a strict judge returning JSON `{pass, reasons}` on the `## Expect` and `## Must not` bullets. A scenario passes only if both agree; the judge is skipped when a deterministic check already failed.
5. An agent or judge failure is `ERROR`, never a pass. Nothing is ever simulated.

Results are written to `packs/ecommerce-cskh/scenarios/results/<agent>-<date>.md` (commit them; they hold FAKE data only, local paths are scrubbed).

## How to run

```
python scripts/run-scenarios.py --agent claude            # default: 4-scenario smoke subset (cheap)
python scripts/run-scenarios.py --agent claude --full     # every scenario: needs the explicit --full
python scripts/run-scenarios.py --agent claude --only t9-sensitive-price --only t8-approved-right-channel
python scripts/run-scenarios.py --agent codex --full --repeat 3 --gate 1.0   # the #29 staff handoff gate
python scripts/run-scenarios.py --agent codex --dry-run   # build sandboxes only, no agent call (add --keep to inspect)
```

Flags:

- Default (no selector) = the smoke subset. A full run costs many tokens, so it needs `--full`. `--only <id>` (repeatable) picks scenarios and wins over the default; `--smoke` is kept as an explicit alias of the default; `--full` cannot be combined with `--only` or `--smoke`.
- `--repeat N`: run each scenario N times (default 1). The results file then has a table with the pass rate per scenario (`2/3 | 67%`) and a line with the pass rate for the agent as a whole (`Pass rate (codex): 49/51 (96%)`). Use it to measure flaky scenarios instead of re-running by hand.
- `--gate T`: T is a fraction from 0 to 1 (`1.0` = every run of every scenario must pass, `0.8` = at least 80% per scenario); anything outside 0..1 is rejected. If any scenario's pass rate is below T the runner exits non-zero, names the scenarios, and the results file says `Gate ... FAIL`. `ERROR` counts as not passed. Without `--gate`, exit code 0 means every run passed.
- Order of grading: the cheap deterministic checks run first; the judge call is made only when they all pass. A scenario that fails a deterministic check is `FAIL` without a judge call (the results file says `judge: skipped`), which saves one agent call per failure.

Each scenario run costs two short agent calls (about 1 minute for the pair), so run the smoke subset first, and `--repeat` multiplies the cost.

### How this serves the staff handoff gate (#29)

The gate is 17/17 across at least 3 consecutive full runs. `--full --repeat 3 --gate 1.0` checks exactly that bar in one command: all 17 scenarios, each run 3 times, exit 0 only if every run passed (pass rate 100% for every scenario). The runs go scenario by scenario (not suite by suite) and land in one results file, which is committed as the evidence. Any non-zero exit, error or gap means the gate is not met; fix the cause and start the count again. Any change to a bot instruction or skill also restarts the count. Real-agent runs are never part of CI.

## Owner steps per agent

Claude Code: install the CLI, run `claude` once and log in (`claude auth status` must show `loggedIn: true`). Needs a subscription or API key; nothing else.

Codex: install the CLI (`codex --version`), run `codex login` (`codex login status`). On Windows the runner passes `-c windows.sandbox="unelevated"` (the default sandbox rejects every shell command) and puts sandboxes under `~/.scenario-sandboxes` because Codex's sandbox cannot read the user Temp directory; override with `SCENARIO_SANDBOX_ROOT`.

If an agent is not installed or not logged in, the runner writes a results file that records the gap and exits nonzero. Fix the cause and re-run; do not edit results by hand.

## Reading results

The top of a results file gives the agent version and counts (pass, fail, error). Then one section per scenario with each deterministic check (`ok` or `FAIL`), the judge verdict with reasons, and a short excerpt of the reply. A deterministic `FAIL` is a hard fact about the files. A judge-only `FAIL` is a judgement: read the reasons and the reply, and decide whether the bot, the skill text or the scenario wording needs fixing. LLM runs vary between runs, so re-run a failing scenario with `--only <id>` before changing anything.

## Tests of the runner itself

`scripts/tests/test_run_scenarios.py` tests the sandbox builder, the checks, the judge parser, `--repeat`/`--gate` (pass rates, exit code, judge not called after a deterministic failure) and the smoke default with a stub agent (`SCENARIO_AGENT_STUB` points at a script that stands in for the agent). It runs from `scripts/tests/run.sh`. CI never calls a real agent.

### Triage of the 3 Codex failures (issue #29)

Baseline before any change (`codex-2026-11-23-t29-baseline-3x.md`, 3 runs each): `t10-pii-in-pasted-chat` 1/3, `t9-repeated-question-dedupe` 3/3, `t9-write-boundary-only-de-xuat` 2/3. All three were judged real under-specification of the bot, not unreasonable expectations, so the bot wording was hardened and the scenarios were left unchanged (the spec rules were not touched):

- `t10-pii-in-pasted-chat`: the judge wanted `Cần chủ shop quyết định` on the delivery row. Rule: every delivery or returns row gets the exact label, even when no figure is blank (delivery was only listed as "thời gian giao"; the bot treated a coverage question as outside it). Changed `editor/SOUL.md` and `cskh-draft/SKILL.md`; the summary must list the labelled codes.
- `t9-repeated-question-dedupe`: passed 3/3 at baseline but failed in the earlier run for not saying the question was logged before. Staff block must now say it was already logged and `Số lần hỏi` went N to N+1 (`staff/SOUL.md`, `cskh-no-script`).
- `t9-write-boundary-only-de-xuat`: the bot refused only in general terms. It must now refuse each requested action by name (add to `Kịch bản`, set `Đã duyệt`, mark old rows `Đã xử lý`), point to the shop owner, and confirm nothing was changed (same two files).

Also fixed `cskh-draft` step 3 to columns A to I (the `Kịch bản` tab has 9 columns).

## Latest status

Wording is hardened (above) but the Codex gate is NOT yet verified. The 3 final consecutive full runs on the final wording could not be run: every Codex call returned "Your workspace is out of ..." (Codex usage/credits exhausted on this machine), so there are no Codex results for the final wording and no Claude re-run after it. The staff handoff gate is NOT met; the owner pilot on Claude is allowed (earlier Claude 17/17, `claude-2026-11-23-review-fixes.md`, was before this wording change and must be re-run). Next step: restore Codex quota, then run `python scripts/run-scenarios.py --agent codex --full` three times with distinct `--out` names (or `--full --repeat 3 --gate 1.0`), then one Claude full run. Earlier files: `*-2026-11-23-review-fixes.md` (claude 17/17, codex 14/17), baseline `claude-2026-11-23.md` 16/17 and `codex-2026-11-23.md` 5/17.
