---
name: bot-routine
description: Writes or audits the routines of a bot, meaning scheduled or event-triggered runs that happen without a person in the chat, using a five-part spec (owner, trigger, allowed actions, escalation path, stop condition), and sets up the optional weekly healthcheck routine. Use when the user wants a bot to run on its own every morning or week or when an event happens, asks for a routine or automation spec for a bot, wants a routine made safe to enable, or wants a bot's existing routines reviewed. Not for deciding whether a bot or a plain automation is the right tool, permissions in general, profile sections, scoring or packaging. Vietnamese triggers - routine cho bot, bot tự chạy mỗi sáng, lịch chạy của bot, đặc tả routine, kiểm tra routine, bot chạy theo sự kiện.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot routine

Make an unattended run safe, bounded and answerable to a named person. Stage 4 of the bot design flow.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Enabling a schedule is a **gate**: the user approves before it is switched on. Every routine starts paused.

## Steps

### 1. Check a routine is warranted

A routine fits repeatable work with a predictable output. If the steps are fixed and need no judgment, a plain automation (cron, n8n, Make) is lighter; say so. Prefer an event trigger over frequent polling, and a schedule no more often than the output needs.

Done when: the user has the reason a routine fits, in one sentence.

### 2. Write the five-part spec

Write every routine with five parts and do not enable one that lacks any of them.

| Part | Say |
|---|---|
| Owner | The named person who answers for the routine and receives its escalations; never "the bot" |
| Trigger | The schedule (time and time zone) or the event, and why that one |
| Allowed actions | The exact list a run may do (read, draft, write to a working folder); anything not listed is not allowed, and send, delete and spend always sit behind a gate |
| Escalation path | Who is told, how, and with what (what happened, what is needed, where to approve) when a run cannot finish or needs something outside the list; an approval nobody answers means nothing happens |
| Stop condition | When a run ends (done criterion, nothing to report, a cap on time or cost) and how many failed or empty runs make it propose a pause to the owner |

Done when: all five parts are written for each routine, with a named owner.

### 3. Write the run instructions

The routine text must work with no chat context: say what to read, what to produce, where to write it, and what to leave alone. Output is a draft; the routine sends, deletes and spends nothing. State that must be trusted across runs (what was sent, what is pending) lives in a named ledger file with an owner and a date: read it at the start, append at the end; where it and the chat disagree, the ledger wins. Approval cards can expire: a run that waits for approval must not depend on a late answer, and an expired card means nothing happens.

Done when: someone who never saw the chat could run the text and get the intended output.

### 4. Create paused, test, then enable

Create it paused. Run it by hand twice and read both results. Then ask the user to approve enabling it (gate). After a share or setup, compare the routines you declared with the automations that actually exist; add what is missing (paused) and report any difference.

Done when: two manual runs are read and recorded, and the user decided whether to enable.

### 5. Optional: healthcheck routine

Only when the bot owns unattended routines and the user wants a periodic audit. Weekly, in the user's time zone, outside quiet hours, created paused and read-only: it reads the bot's automations and their last 4 runs and checks that each ran on schedule with a useful result, is not enabled yet idle or failing, does not fire more often than needed, and does not duplicate another. It stays silent when everything passes and otherwise sends one short message with the proposed change and where to approve; it changes nothing itself. Ready-made text: `references/healthcheck-routine.md`.

Done when: the healthcheck exists paused, one manual run produced no message and one produced a real finding, and the user decided.

## Next stage

bot-access for permissions, or bot-score when access is done. Hand off with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. If a sibling is not installed, tell the user the next stage by name and offer to do it.

## Reference files

- [references/healthcheck-routine.md](references/healthcheck-routine.md): read in step 5; the ready-made healthcheck routine text, English and Vietnamese.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.

## Sources

