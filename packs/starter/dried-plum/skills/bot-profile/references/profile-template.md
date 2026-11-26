# Bot profile: [bot name]

Fill what this bot needs. For any section it does not need, write `not needed` and a one-line reason. The 13 sections are suggestions, not a mandatory gate. Lines starting with `>` are hints; `scripts/score_bot.py` ignores them.

Adapted from the 13-criteria checklist by Masonshare.

## 1. Overview
> Fill: one sentence "The bot helps [who] do [what] to get [result]"; 3-5 in-scope jobs; 2-3 out-of-scope jobs; one success metric.
> Avoid: "general assistant"; a list of 20 jobs; no way to measure success.
> Example: Helps a shop owner clear the inbox in 10 minutes. Out of scope: sending mail.

**Anti-job (required, 2-4 lines):** what this bot must never do, even when asked.
> Fill: concrete refusals tied to the real risk, one per line.
> Avoid: "be careful"; a line that only repeats the out-of-scope list.
> Example: Never send mail without the owner's approval. Never guess a price.

## 2. Identity
> Fill: short name that hints at the job; title; 1-2 line description (what it does plus when to use it); main language and form of address.
> Avoid: "Bot 1"; a name another bot already uses; a description so long that a coordinator cannot route by it.
> Example: Inbox Triage, email secretary, replies in Vietnamese.

## 3. Soul
> Fill: 150-400 words. Role; user and expertise; voice; working principles with reasons; hard limits (ask before send, delete, spend, commit); the Anti-job; honest reporting; the missing-data labels: `Unknown` (not found, never guess), `UNVERIFIED` (held but not checked against the source), `BLOCKED` (cannot go on without access, approval or input; say who can unblock).
> Avoid: capital-letter bans without reasons; pasting long procedures (move them to Skills); facts that go stale; a soul or description past about 600 words (warn and propose a split).
> Example: "Draft, never send, because the owner signs every outgoing message." "If a price is not in the price list, write Unknown and ask; never estimate."

## 4. Skills
> Fill: a bot may own as many skills as its role needs, one per procedure (no fixed cap); each ties to one job in the Job and has a trigger description, numbered steps, a verify step, an output template and one good example. Remove skills no job uses. Give mechanical work to a script.
> Avoid: one giant skill; a skill with no job; vague descriptions that never trigger; overlapping skill descriptions.
> Example: triage-inbox, draft-reply, daily-summary.

## 5. Memory
> Fill: stable preferences, settled decisions with reasons, user corrections, naming. One fact per line, dated.
> Avoid: anything that expires within a week; secrets; long text (point to Library).
> Example: Reply in Vietnamese. Sign with the shop name (2026-11-01).

## 6. Library
> Fill: stable reference documents in small files by topic, with an update date and an owner. Add a ledger or file for any state the bot must trust across runs (sent, pending, decided, current numbers): the file is the source of truth, not the chat; the bot reads it at the start of a run and appends at the end.
> Avoid: a whole data dump; one 50-page file; old and new versions side by side; state that lives only in chat history.
> Example: price-list.md (updated 2026-10-15, owner: shop owner). orders-ledger.md (one dated line per order handled, appended by the bot).

## 7. Routines
> Fill: repeatable work with predictable output; instructions that run without chat context; event triggers over frequent polling; draft-only output; start paused. Give each routine five parts: Owner (a named person), Trigger (schedule with time zone, or event), Allowed actions (an exact list), Escalation path (who is told, how, with what), Stop condition (when a run ends, and how many failed or empty runs lead to a proposed pause).
> Avoid: a 5-minute schedule without need; routines that send, delete or spend; "do what you did yesterday"; a routine with no named owner or no stop condition.
> Example: Owner: the shop owner. Trigger: weekdays 08:00 in the owner's time zone. Allowed: read inbox, draft summary. Escalation: message the owner when a supplier mail is urgent. Stop: after the summary, or 2 empty runs in a row propose a pause. Paused until tested twice.

## 8. Access
> Fill: only the apps the bot truly uses, each tied to a job in the Job (otherwise remove it); read before write; which bots it may call and who may call it.
> Avoid: connecting everything for convenience; two bots handing work to each other in a circle.
> Example: Gmail read plus draft; Calendar read.

## 9. Model
> Fill: the smallest model that passes the test cases; a cheaper model for high-volume routines.
> Avoid: the strongest model for classification or formatting.
> Example: small model first; upgrade only on failed cases.

## 10. Permissions
> Fill: a table of what is free (read, search, analyse), what is free inside scope (drafts, files in a working folder), what always needs approval (send, pay, delete, commit or push, spend credits), and what the bot may not do (computer control, login) unless the job requires it.
> Avoid: write access when read is enough; money limits stated only in prompt text.
> Example: sending mail needs approval; no payment tools.

## 11. Voice and alerts
> Fill: notify only when action is needed (approval, error, deadline, long job finished); a short message saying what, what to do, where; quiet hours in the user's time zone.
> Avoid: alerting every step; generic "there is an update".
> Example: "Deadline in 20h: reply to supplier X. Draft ready in Gmail."

## 12. History
> Fill: one thread per job with a clear name; a handoff template for a new thread (done, open, decisions, key files); close finished threads.
> Avoid: one long thread for everything; dragging the full history into a new thread.
> Example: Handoff: Goal / Inputs / Deliverable / Done when / Open items.

## 13. Usage
> Fill: a way to track tokens or cost per task weekly; a limit and a warning; a check that routines are not running without useful results.
> Avoid: no measurement; a routine whose runs rarely produce anything.
> Example: weekly cost per task; warn at 80% of the limit.

## Test cases
> Fill: 5-10 cases: 3 normal, 2 ambiguous, 2 out of scope, 2 asking for a risky action; baseline result, retest result. For each result: input, expected, actual, the evidence and its source tier (direct, primary, teammate-reported or UNVERIFIED, inference).
