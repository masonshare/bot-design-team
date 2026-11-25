# Pilot rollout checklist: owner, then one staff member, then the whole team

Manual seam of spec #14 (issue #27, T13). An agent only prepared this list; the owner and the pilot do the steps. Pack: `packs/ecommerce-cskh/`.

Who: **owner** (shop owner), **pilot** (one staff member), **agent** (a coding agent such as Claude Code or Codex, only where a step is a repo or file task).

Rules for every stage:

- Move to the next stage only when every exit criterion of the current one is met and the owner has signed the confirmation line at the end of the stage.
- No real company, customer or staff data goes into this repo, ever (ADR 0003). Real data lives only in the owner's own Google Sheet, loaded at runtime.
- If an observation differs from "Expected", stop, write it down in the owner's notes, and do not continue the stage.

## Stage 0: ship gate (before the owner touches Orca)

The gate has two levels (decision D on PR #28). See `docs/scenario-testing.md`.

- Owner pilot (stage 1) may proceed with the Claude-based owner bot (Claude passes every scenario).
- BEFORE the bot is handed to ONE staff member (stage 2; staff run Codex), the Codex scenario suite must pass 17/17 stably: at least 3 consecutive full runs, each with 0 fail and 0 error. Status: MET on 2026-11-25 (issue #29): Codex 51/51 (17 scenarios x 3) with `gpt-6.1-terra`, Claude 17/17; evidence in `docs/scenario-testing.md` (Latest status). Gate model: the gate was proven on `gpt-6.1-terra` only (pinned with `--codex-model`). It holds only while staff run Codex with that model; if a staff member's default model differs, or Codex's default changes, run the gate again with `--codex-model <that model>` first. "3 consecutive full runs" means `--full --repeat 3`: every scenario 3 times in a row (51 runs), not three whole-suite passes.

| # | Who | Step | Expected observation |
|---|---|---|---|
| 0.1 | agent | `sh scripts/ci.sh` | Exits 0 |
| 0.2 | owner | Log in to Claude Code (`claude auth status`) and Codex (`codex login status`) | Both report logged in |
| 0.3 | agent | `python scripts/run-scenarios.py --agent claude` (smoke subset), then `python scripts/run-scenarios.py --agent claude --full` | Results file for `claude` shows 0 fail, 0 error |
| 0.4 | agent | Same for `--agent codex` (smoke, then `--full`). Not required to start stage 1; required before stage 2 (see 0.6) | Results file for `codex` shows 0 fail, 0 error |
| 0.5 | owner | Open both results files in `packs/ecommerce-cskh/scenarios/results/` | No recorded gap; counts match 0.3 and 0.4 |
| 0.6 | agent | Staff handoff gate: run `python scripts/run-scenarios.py --agent codex --codex-model gpt-6.1-terra --full --repeat 3 --gate 1.0 --timeout 480` (every Codex scenario 3 times in a row; the model is recorded in the results file; exit code 0 = gate met; repeat more if any run fails; the count restarts after a failure or after any change to a bot instruction or skill) | Exit 0; results file for `codex` shows 17/17 scenarios at 3/3 (100%), 0 fail, 0 error (issue #29) |

Exit criteria for the owner pilot (stage 1): `sh scripts/ci.sh` green and Claude passes every scenario (a missing results file or a recorded gap means not met); the Codex gate is not needed for this stage.

Exit criteria before stage 2: additionally the 0.6 Codex gate is met (17/17 on at least 3 consecutive full runs, meaning `--full --repeat 3`, with the model the staff will use; it is met for `gpt-6.1-terra`). Do not hand the bot to a staff member before that. Do not edit results by hand. Owner confirms: ____ (name, date)

## Stage 1: owner

| # | Who | Step | Expected observation |
|---|---|---|---|
| 1.1 | owner | Install Orca and open it | App starts, shows the home screen |
| 1.2 | owner | Log in to Codex (ChatGPT account) and to Claude Code if used for the Editor bot | Orca can start a chat on each agent |
| 1.3 | owner | `orca --version`; note it | Version printed (V6); compare with 1.4.271 in `docs/orca-skill-loading.md` |
| 1.4 | owner | Add this repo and the pack as described in `docs/orca-skill-loading.md` (sections 4a and 5), then run owner verification steps V1 to V6 in section 6 of that file | Each V1 to V6 has a recorded result; any difference from the doc is reported back so the doc can be fixed |
| 1.5 | owner | Create the Editor bot from `packs/ecommerce-cskh/editor/` and the Staff bot from `packs/ecommerce-cskh/staff/`; enable only the skills each bot needs | Two separate bots; each lists its own skills in a new chat |
| 1.6 | owner | Create the Google Sheet from `packs/ecommerce-cskh/sheet-template.md` in the owner's own Google account (tab `Kịch bản`, exact name) and, separately, the `Đề xuất CSKH` file (tab `Đề xuất`) as in step 1.13 | Scripts Sheet opens with tab `Kịch bản` and the exact headers |
| 1.7 | owner | Connect the Google connector for each bot (kind `google`), signed in as the owner | Each bot can read tab `Kịch bản` when asked |
| 1.8 | owner | Load the owner's REAL scripts and Q&A into the owner's own Sheet only, through the Editor bot or by hand. Never copy them into the repo or a bot's files | Rows appear in the Sheet as `Nháp`; `git status` in the repo shows nothing new |
| 1.9 | owner | Review the drafts and approve the first batch: set `Đã duyệt` and fill column I (approver, date) | Approved rows have status and column I filled; the rest stay `Nháp` |
| 1.10 | owner | Publish the Staff bot with its Share dialog (tick skills, leave memory unticked); copy the link | Link produced; publishing is not blocked by a secret warning |
| 1.11 | owner | Open the link on the same Orca as a new bot (or a second profile) and read the review dialog | Soul and ticked skills listed; no sheet ID, token or header value appears |
| 1.12 | owner | Ask the Staff bot a question that an approved script answers, then one that none answers | First: answers from the approved script. Second: says there is no script and logs a row in the `Đề xuất CSKH` file (needs 1.13) |
| 1.13 | owner | Set up the separate `Đề xuất CSKH` file (see "Staff bot write access (decided)" below): create it, add tab `Đề xuất` with the 8 headers, share it as editor with staff, keep the scripts file view-only | `Đề xuất CSKH` exists with tab `Đề xuất` and exact headers; the Staff bot (signed in as the owner for this test) appends a row there; scripts file is shared view-only only |

Exit criteria:

- V1 to V6 recorded, and `docs/orca-skill-loading.md` corrected if reality differed.
- Editor bot writes only `Nháp`; Staff bot never edits `Kịch bản`.
- The share link opens and installs a working Staff bot on the owner's side.
- A no-script question lands in the `Đề xuất CSKH` file.
- No real data in the repo.

Owner confirms: ____ (name, date)

## Staff bot write access (decided, set up in step 1.13)

Decision C on PR #28: `Đề xuất` is its own Google Sheet file, `Đề xuất CSKH`. Google shares per file, never per tab, and the bot signs in as the staff member, so this is the only way staff stay view-only on scripts while the bot can append.

How to set it up (owner, in the owner's own Google account):

1. Create a new Google Sheet named exactly `Đề xuất CSKH`. Rename its single tab to `Đề xuất` and add the 8 headers from `packs/ecommerce-cskh/sheet-template.md` (Ngày, Kênh, Câu hỏi của khách, Câu đã trả lời, Mã gần nhất, Người hỏi, Trạng thái xử lý, Số lần hỏi).
2. Share `Đề xuất CSKH` with each staff member as **Editor** (this file only).
3. Share the main scripts Sheet (tab `Kịch bản`) with each staff member as **Viewer** (view-only). Never give staff editor access there.
4. The Staff bot reads the scripts file read-only and appends or increments only in `Đề xuất CSKH`.
5. The owner reviews `Đề xuất CSKH` daily during the pilot and turns useful rows into `Nháp` scripts.

Accepted cost: a staff editor could edit or delete rows in `Đề xuất CSKH`. Review daily, or protect the header row. Real file links and IDs stay in the owner's Google account, never in this repo.

## Stage 2: pilot (one staff member)

| # | Who | Step | Expected observation |
|---|---|---|---|
| 2.0 | owner | Confirm the staff handoff gate (step 0.6): Codex 17/17 on at least 3 consecutive full runs (`--full --repeat 3`) and the staff member's Codex model is the gated one | One results file with 17 scenarios at 3/3 and the model name in its header (`codex-2026-11-25-gate4.md` for `gpt-6.1-terra`); otherwise stop, do not hand over the bot |
| 2.1 | pilot | Install Orca; log in to Codex with the pilot's own ChatGPT account | Orca can start a Codex chat |
| 2.2 | owner | Share the main scripts Sheet with the pilot as view-only, and the `Đề xuất CSKH` file as editor | Pilot opens the scripts Sheet and cannot edit `Kịch bản` ("Chỉ xem"); can edit `Đề xuất CSKH` |
| 2.3 | owner | Send the Staff bot share link to the pilot | Pilot receives the link |
| 2.4 | pilot | Open the link, review the dialog, choose Codex, create the bot (V5 in `docs/orca-skill-loading.md`) | Bot created; it shows its skills; no owner sign-in or sheet ID included |
| 2.5 | pilot | Connect the Google connector signed in as the pilot | Bot can read tab `Kịch bản` |
| 2.6 | pilot | Ask a question covered by an approved script, on its channel (Shopee, Zalo or hotline) | Reply uses the approved script, matching the channel; no `Nháp` or `Hết hạn` script used |
| 2.7 | pilot | Ask a question no script covers | Bot says so honestly (for example "chưa có kịch bản") and logs a row in the `Đề xuất CSKH` file, with no customer name or phone number |
| 2.8 | pilot | Ask the same unanswered question again | Count in column H goes up by 1, no duplicate row |
| 2.9 | pilot | Try to make the bot edit `Kịch bản` | Refused; the Sheet is unchanged |
| 2.10 | pilot | Use the bot for real work for about one week | Daily notes of wrong, missing or confusing answers |
| 2.11 | owner | Review the `Đề xuất CSKH` file daily; fix wrong answers, add missing scripts (as `Nháp`, then approve) | Fewer repeated unanswered questions over the week |

Feedback path (story 34): the pilot reports problems to the owner the same day, in one place the owner picks (a shared chat message or a note), with the date, channel and what the bot said, never customer names or phone numbers. The owner turns each report into a script fix, a bot instruction change, or a repo issue (only without real data). Rows in `Đề xuất CSKH` are the standing feedback channel for missing scripts.

Exit criteria:

- Steps 2.4 to 2.9 behaved as expected.
- About one week of use with no wrong answer left unfixed; the pilot says the answers are acceptable.
- Scenario suite re-run on both agents if any bot instruction or skill changed during the pilot.

Owner confirms: ____ (name, date)

## Stage 3: whole team

Tet season: do not start this stage in the Tet peak (high order volume, short staffing, many new questions). Finish the pilot well before the peak, roll out in a quiet week, and avoid changing scripts or bot instructions during the busiest days. If the pilot is not clean in time, wait until after Tet rather than rolling out under pressure. Check the lunar calendar for the real dates.

| # | Who | Step | Expected observation |
|---|---|---|---|
| 3.1 | owner | Go/no-go decision (see below) | Decision written down with date |
| 3.2 | owner | Share the main scripts Sheet with each staff member as view-only and the `Đề xuất CSKH` file as editor | Each person can read but not edit scripts, and can edit `Đề xuất CSKH` |
| 3.3 | owner | Send the Staff bot link and a short setup note to the team | Everyone has the link |
| 3.4 | each staff member | Install Orca, log in to Codex, open the link, create the bot, connect Google | Same observations as 2.1 to 2.5 |
| 3.5 | owner | Watch `Đề xuất CSKH` and staff feedback for the first week | Rows arrive with channel and question; no personal data in them |
| 3.6 | owner | After any change to scripts or bot text, re-run the scenario suite on both agents before telling staff | 0 fail, 0 error on both |

Exit criteria: every staff member completed 3.4; no one can edit `Kịch bản`; the owner reviewed the first week's `Đề xuất CSKH`. Owner confirms: ____ (name, date)

## Go/no-go (owner decides)

Go to stage 3 only if all are true: ship gate met on both agents (Codex 17/17 on at least 3 consecutive full runs, issue #29); stage 2 exit met; no open question from V1 to V6 that blocks staff; the separate `Đề xuất CSKH` file (step 1.13) is set up and works; it is not the Tet peak. Otherwise no-go: list the blockers, fix them, and repeat the failed stage. The owner alone makes the call.

Decision: GO / NO-GO. Owner: ____ Date: ____
