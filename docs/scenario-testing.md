# Scenario testing (ecommerce-cskh)

Behavioural tests for the two bots (staff, editor) against FAKE data, run on both Claude Code and Codex. This is testing seam 2 of spec #14. Scenarios live in `packs/ecommerce-cskh/scenarios/` (format in its `README.md`); the runner is `scripts/run-scenarios.py` (Python standard library only).

## Ship gate

The pack is not shippable to staff until every scenario passes on BOTH agents (results files for `claude` and `codex` show 0 fail, 0 error). A missing results file, or one that records a gap, means the gate is not met.

## What the runner does

For each scenario it:

1. Builds a throwaway sandbox: the bot's `SOUL.md` as `CLAUDE.md` (Claude Code) or `AGENTS.md` (Codex), its skills in `.claude/skills/<name>` or `.agents/skills/<name>`, `voice-guide.md`, `sheet-template.md`, and CSV stand-ins for the Google Sheet (`sheet/kich-ban.csv` = tab `Kịch bản`, `sheet/de-xuat.csv` = tab `Đề xuất`) copied from `fake-data/`.
2. Enforces the access model: staff may write only `de-xuat.csv`; editor may write only `kich-ban.csv`. The other file is read-only, and the CSVs are diffed after the run anyway.
3. Runs the agent headlessly (no network, only file tools for Claude Code, workspace-write sandbox for Codex) with the scenario message.
4. Grades twice: deterministic checks on the CSV diff and reply (for example `Kịch bản` unchanged for staff, new editor rows are `Nháp` with no approver, `Đề xuất` row appended or count +1, no phone/name in new rows), then a second headless call to the same agent as a strict judge returning JSON `{pass, reasons}` on the `## Expect` and `## Must not` bullets. A scenario passes only if both agree.
5. An agent or judge failure is `ERROR`, never a pass. Nothing is ever simulated.

Results are written to `packs/ecommerce-cskh/scenarios/results/<agent>-<date>.md` (commit them; they hold FAKE data only, local paths are scrubbed).

## How to run

```
python scripts/run-scenarios.py --agent claude            # all scenarios
python scripts/run-scenarios.py --agent codex --smoke     # 4-scenario smoke subset
python scripts/run-scenarios.py --agent claude --only t9-sensitive-price --only t8-approved-right-channel
python scripts/run-scenarios.py --agent codex --dry-run   # build sandboxes only, no agent call (add --keep to inspect)
```

Exit code 0 only if every scenario ran and passed. Each scenario costs two short agent calls (about 1 minute for the pair), so run the smoke subset first.

## Owner steps per agent

Claude Code: install the CLI, run `claude` once and log in (`claude auth status` must show `loggedIn: true`). Needs a subscription or API key; nothing else.

Codex: install the CLI (`codex --version`), run `codex login` (`codex login status`). On Windows the runner passes `-c windows.sandbox="unelevated"` (the default sandbox rejects every shell command) and puts sandboxes under `~/.scenario-sandboxes` because Codex's sandbox cannot read the user Temp directory; override with `SCENARIO_SANDBOX_ROOT`.

If an agent is not installed or not logged in, the runner writes a results file that records the gap and exits nonzero. Fix the cause and re-run; do not edit results by hand.

## Reading results

The top of a results file gives the agent version and counts (pass, fail, error). Then one section per scenario with each deterministic check (`ok` or `FAIL`), the judge verdict with reasons, and a short excerpt of the reply. A deterministic `FAIL` is a hard fact about the files. A judge-only `FAIL` is a judgement: read the reasons and the reply, and decide whether the bot, the skill text or the scenario wording needs fixing. LLM runs vary between runs, so re-run a failing scenario with `--only <id>` before changing anything.

## Tests of the runner itself

`scripts/tests/test_run_scenarios.py` tests the sandbox builder, the checks and the judge parser with a stub agent (`SCENARIO_AGENT_STUB` points at a script that stands in for the agent). It runs from `scripts/tests/run.sh`. CI never calls a real agent.

## Latest status

Results files `*-2026-11-23-review-fixes.md`: claude 17/17 pass, codex 14/17 pass. The gate is NOT met for codex: `t10-pii-in-pasted-chat`, `t9-repeated-question-dedupe` and `t9-write-boundary-only-de-xuat` failed on judge strictness (see reasons in the file; the last two passed in the earlier run, so they vary between runs). The earlier `claude-2026-11-23.md` and `codex-2026-11-23.md` are the pre-fix baseline (16/17 and 5/17).
