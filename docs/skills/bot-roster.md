# bot-roster

## What it does

Helps the Coordinator bot decide who should do a job and run the delegation safely: read the live bot list and the bot's own roster file, pick the bot or code worker, ask the user for approval first, choose `question` or `handoff`, write the 5-field brief (Goal, Inputs, Deliverable, Done when, Open items), merge results and report real progress. It also carries the pre-authorization paragraph that lets a code worker read pipeline skills by hand.

Source: [`skills/design/bot-roster/SKILL.md`](../../skills/design/bot-roster/SKILL.md)

## When to reach for it

The Coordinator is about to give any job to another bot or to a code worker, register a new bot in the roster, or report delegated progress.

## Common questions

**Does it write the soul, skill or code itself?** No. It only routes the job; specialist bots and workers do the work.

**When does the user approve?** Before every handoff to a bot, with the bot named in the question, even if the user already named it. For a code worker, once before it starts, naming the repo; the worker then begins by grilling the user and writes code only after the spec is settled.

**Where does the worker paragraph come from?** From [`docs/agents/dispatch-pipeline-skills.md`](../agents/dispatch-pipeline-skills.md); re-copy it if that doc changes.

## It's working if

- No bot gets a job before the user said yes to a question that named it.
- Every brief has all five fields and a checkable Done when.
- Status reports use Đã giao, Đã về and Còn mở, and never claim a merge the user did not do.
