# Pilot rollout checklist: owner, then one staff member, then the whole team

Manual seam of spec #14 (issue #27, T13). An agent only prepared this list; the owner and the pilot do the steps. Pack: `packs/ecommerce-cskh/`.

Who: **owner** (shop owner), **pilot** (one staff member), **agent** (a coding agent such as Claude Code or Codex, only where a step is a repo or file task).

Rules for every stage:

- Move to the next stage only when every exit criterion of the current one is met and the owner has signed the confirmation line at the end of the stage.
- No real company, customer or staff data goes into this repo, ever (ADR 0003). Real data lives only in the owner's own Google Sheet, loaded at runtime.
- If an observation differs from "Expected", stop, write it down in the owner's notes, and do not continue the stage.

## Stage 0: ship gate (before the owner touches Orca)

Scenarios must pass on both agents first. See `docs/scenario-testing.md`.

| # | Who | Step | Expected observation |
|---|---|---|---|
| 0.1 | agent | `sh scripts/ci.sh` | Exits 0 |
| 0.2 | owner | Log in to Claude Code (`claude auth status`) and Codex (`codex login status`) | Both report logged in |
| 0.3 | agent | `python scripts/run-scenarios.py --agent claude --smoke`, then without `--smoke` | Results file for `claude` shows 0 fail, 0 error |
| 0.4 | agent | Same for `--agent codex` | Results file for `codex` shows 0 fail, 0 error |
| 0.5 | owner | Open both results files in `packs/ecommerce-cskh/scenarios/results/` | No recorded gap; counts match 0.3 and 0.4 |

Exit criteria: both agents pass every scenario (a missing results file or a recorded gap means the gate is not met). Do not edit results by hand. Owner confirms: ____ (name, date)

## Stage 1: owner

| # | Who | Step | Expected observation |
|---|---|---|---|
| 1.1 | owner | Install Orca and open it | App starts, shows the home screen |
| 1.2 | owner | Log in to Codex (ChatGPT account) and to Claude Code if used for the Editor bot | Orca can start a chat on each agent |
| 1.3 | owner | `orca --version`; note it | Version printed (V6); compare with 1.4.271 in `docs/orca-skill-loading.md` |
| 1.4 | owner | Add this repo and the pack as described in `docs/orca-skill-loading.md` (sections 4a and 5), then run owner verification steps V1 to V6 in section 6 of that file | Each V1 to V6 has a recorded result; any difference from the doc is reported back so the doc can be fixed |
| 1.5 | owner | Create the Editor bot from `packs/ecommerce-cskh/editor/` and the Staff bot from `packs/ecommerce-cskh/staff/`; enable only the skills each bot needs | Two separate bots; each lists its own skills in a new chat |
| 1.6 | owner | Create the Google Sheet from `packs/ecommerce-cskh/sheet-template.md` in the owner's own Google account (tabs `Kịch bản` and `Đề xuất`, exact names) | Sheet opens with both tabs and the exact headers |
| 1.7 | owner | Connect the Google connector for each bot (kind `google`), signed in as the owner | Each bot can read tab `Kịch bản` when asked |
| 1.8 | owner | Load the owner's REAL scripts and Q&A into the owner's own Sheet only, through the Editor bot or by hand. Never copy them into the repo or a bot's files | Rows appear in the Sheet as `Nháp`; `git status` in the repo shows nothing new |
| 1.9 | owner | Review the drafts and approve the first batch: set `Đã duyệt` and fill column I (approver, date) | Approved rows have status and column I filled; the rest stay `Nháp` |
| 1.10 | owner | Publish the Staff bot with its Share dialog (tick skills, leave memory unticked); copy the link | Link produced; publishing is not blocked by a secret warning |
| 1.11 | owner | Open the link on the same Orca as a new bot (or a second profile) and read the review dialog | Soul and ticked skills listed; no sheet ID, token or header value appears |
| 1.12 | owner | Ask the Staff bot a question that an approved script answers, then one that none answers | First: answers from the approved script. Second: says there is no script and logs a row in `Đề xuất` (needs 1.13) |
| 1.13 | owner | Decide and test the Staff bot write access (see "Staff bot write access" below) | Decision recorded: how the Staff bot appends to `Đề xuất` while staff stay view-only on scripts |

Exit criteria:

- V1 to V6 recorded, and `docs/orca-skill-loading.md` corrected if reality differed.
- Editor bot writes only `Nháp`; Staff bot never edits `Kịch bản`.
- The share link opens and installs a working Staff bot on the owner's side.
- A no-script question lands in `Đề xuất` through the chosen access method.
- No real data in the repo.

Owner confirms: ____ (name, date)

## Staff bot write access (open question, decide in step 1.13)

`packs/ecommerce-cskh/sheet-template.md` and ADR 0002 say two things that conflict in practice: staff get a view-only share of the Sheet, and the Staff bot appends to tab `Đề xuất`. Neither names a mechanism. The bot signs in to Google as the staff member (sign-ins are never shared), so a view-only share means the append would be refused. Google also cannot grant edit on one tab only; sharing is per file.

Candidate fix, not yet decided or in the template: keep `Kịch bản` in the main Sheet (staff: view-only) and move `Đề xuất` into a separate file, for example `Đề xuất CSKH`, shared with staff as editor. The staff bot appends there only. The owner reads that file and turns useful rows into `Nháp` scripts. Cost: staff could edit or delete rows in `Đề xuất`; accept and review daily, or protect the header row. If the owner chooses this, a follow-up issue must update `sheet-template.md`, the Staff `cskh-no-script` skill and the pack README. Until then the pilot can use an interim choice recorded by the owner: (a) separate edit-shared `Đề xuất` file, or (b) staff paste the proposed row by hand and the bot only drafts it.

## Stage 2: pilot (one staff member)

| # | Who | Step | Expected observation |
|---|---|---|---|
| 2.1 | pilot | Install Orca; log in to Codex with the pilot's own ChatGPT account | Orca can start a Codex chat |
| 2.2 | owner | Share the main Sheet with the pilot as view-only (and the `Đề xuất` file as editor, if 1.13 chose that) | Pilot opens the Sheet and cannot edit `Kịch bản` ("Chỉ xem") |
| 2.3 | owner | Send the Staff bot share link to the pilot | Pilot receives the link |
| 2.4 | pilot | Open the link, review the dialog, choose Codex, create the bot (V5 in `docs/orca-skill-loading.md`) | Bot created; it shows its skills; no owner sign-in or sheet ID included |
| 2.5 | pilot | Connect the Google connector signed in as the pilot | Bot can read tab `Kịch bản` |
| 2.6 | pilot | Ask a question covered by an approved script, on its channel (Shopee, Zalo or hotline) | Reply uses the approved script, matching the channel; no `Nháp` or `Hết hạn` script used |
| 2.7 | pilot | Ask a question no script covers | Bot says so honestly (for example "chưa có kịch bản") and logs a row in `Đề xuất` per the 1.13 decision, with no customer name or phone number |
| 2.8 | pilot | Ask the same unanswered question again | Count in column H goes up by 1, no duplicate row |
| 2.9 | pilot | Try to make the bot edit `Kịch bản` | Refused; the Sheet is unchanged |
| 2.10 | pilot | Use the bot for real work for about one week | Daily notes of wrong, missing or confusing answers |
| 2.11 | owner | Review `Đề xuất` daily; fix wrong answers, add missing scripts (as `Nháp`, then approve) | Fewer repeated unanswered questions over the week |

Feedback path (story 34): the pilot reports problems to the owner the same day, in one place the owner picks (a shared chat message or a note), with the date, channel and what the bot said, never customer names or phone numbers. The owner turns each report into a script fix, a bot instruction change, or a repo issue (only without real data). Rows in `Đề xuất` are the standing feedback channel for missing scripts.

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
| 3.2 | owner | Share the main Sheet with each staff member as view-only (and the `Đề xuất` file per 1.13) | Each person can read but not edit scripts |
| 3.3 | owner | Send the Staff bot link and a short setup note to the team | Everyone has the link |
| 3.4 | each staff member | Install Orca, log in to Codex, open the link, create the bot, connect Google | Same observations as 2.1 to 2.5 |
| 3.5 | owner | Watch `Đề xuất` and staff feedback for the first week | Rows arrive with channel and question; no personal data in them |
| 3.6 | owner | After any change to scripts or bot text, re-run the scenario suite on both agents before telling staff | 0 fail, 0 error on both |

Exit criteria: every staff member completed 3.4; no one can edit `Kịch bản`; the owner reviewed the first week's `Đề xuất`. Owner confirms: ____ (name, date)

## Go/no-go (owner decides)

Go to stage 3 only if all are true: ship gate met on both agents; stage 2 exit met; no open question from V1 to V6 that blocks staff; the `Đề xuất` write method (step 1.13) is decided and works; it is not the Tet peak. Otherwise no-go: list the blockers, fix them, and repeat the failed stage. The owner alone makes the call.

Decision: GO / NO-GO. Owner: ____ Date: ____
