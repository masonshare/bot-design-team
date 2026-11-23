---
name: bot-profile
description: Fills the profile of one AI bot, the 13 sections from overview and identity to model, history and usage, marking unneeded sections with a reason, and prepares the brief for the bot's soul and skills. Use when the user wants a bot profile written or reviewed, a bot's overview, anti-job, identity, memory, library or model choice decided, or a starter frame for a type of bot such as support, coding or research. Not for writing the soul text itself, routines, permissions, scoring or packaging. Vietnamese triggers - hồ sơ bot, điền hồ sơ bot, mô tả bot, anti-job, trí nhớ và thư viện của bot, chọn model cho bot.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot profile

Fill the profile that a person can use to set up one bot. Stage 3 of the bot design flow.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Gate: giving the bot write access, installing or enabling anything waits for the user's approval. Writing the profile does none of that.

## Steps

### 1. Take the shape and pick a frame

Take one bot's one-line job and seven-answer spec from bot-shape (or the interview brief). Pick the nearest starter frame and adjust: marketplace operations, content and image prompts, coding, research and analysis, secretary or email, coordinator, data and reporting. The frame table is in `references/starter-frames.md`; without it, start from the bot's own job.

Done when: the job, the anti-job and the nearest frame are written at the top of the profile.

### 2. Fill the 13 sections

The 13 sections are suggestions, not a mandatory gate: overview, identity, soul, skills, memory, library, routines, access, model, permissions, voice/alerts, history, usage. Fill only what this bot needs and mark each other section `not needed` with a one-line reason. Fill-in template with hints: `references/profile-template.md`.

Layer content by how often it is needed: soul = true on every run, short; skills = procedures that run only when relevant; library = long reference documents and ledgers, split by topic with dates; memory = stable facts about the user, one line each.

| Section | Fill with | Avoid |
|---|---|---|
| Overview | One sentence: helps [who] do [what] to get [result]; 3-5 in-scope jobs; 2-3 out-of-scope; one success metric; an Anti-job of 2-4 lines (required) | "General assistant"; an Anti-job that only says "be careful" |
| Identity | Short name that hints at the job; title; 1-2 line description saying what it does and when to use it; language and form of address | Generic or duplicate names |
| Skills | As many as the role needs, one per procedure (no fixed cap); each ties to one job in the Job and has a trigger description, numbered steps, a verify step, an output template; remove skills no job uses | One giant skill; a skill with no job; mechanical work left to the model instead of a script |
| Memory | Stable preferences, settled decisions with reasons, user corrections, naming | Anything expiring within a week, secrets, long text (point to Library) |
| Library | Small files by topic, update date, owner; a ledger or file for any state the bot must trust across runs (what was sent, what is pending, what was decided) | One 50-page file; stale copies beside new ones; state that exists only in chat |
| Routines | Only if the bot runs alone: the five-part spec from bot-routine (owner, trigger, allowed actions, escalation path, stop condition) | Schedules every few minutes without need |
| Access, Permissions | Fill from bot-access: apps tied to a job, read before write, a gate before every irreversible action | Connecting everything for convenience |
| Model | The smallest model that passes the test cases; cheaper for high-volume routines | Strongest model everywhere |
| Voice/alerts | Notify only when action is needed: approval, error, deadline; short message saying what, what to do, where; quiet hours | Alerting every step |
| History | One thread per job; on a heavy thread, start a new one with a handoff | One endless thread |
| Usage | Token or cost per task tracked weekly; a limit and a warning | No measurement |

Source of truth: a ledger or file in the Library, not the chat. A routine runs without chat context and a new thread starts empty, so anything the bot must trust later (sent items, pending items, decisions, current numbers) goes in one named file with an owner and a date. The bot reads it at the start of a run and appends to it at the end. Where ledger and chat disagree the ledger wins, and a fact a human owns is changed only by that human.

Done when: every section is filled or marked `not needed` with a reason, and no filled section contains a secret.

### 3. Brief the soul and the skills

Hand the soul to the `bot-soul` skill (or `prompt-design`) when installed, and each procedure to `skill-design`, with a brief: goal, audience, inputs, constraints, definition of done. They return the soul and the skills with test cases. Do not redo their work.

When they are missing, write inline. Soul, 150-400 words, in this order: role in 1-2 sentences; the user and their expertise; voice; working principles, each with its reason; hard limits (ask first before sending, deleting, spending, committing); the Anti-job; honest reporting (what was done, not done, what failed; never claim done before checking); the three missing-data labels, in every soul so each output says the same thing in the same words:

- `Unknown`: the fact is not in the inputs and could not be found. Say what is missing and where it might come from; never guess.
- `UNVERIFIED`: the claim is held but not checked against the source (secondhand, summarised, teammate-reported). Keep it, label it, say what check would settle it.
- `BLOCKED`: the step cannot go on without something the bot cannot supply (access, an approval, an input). Say what blocks it and who can unblock it, then stop.

Prefer reasons over capital-letter bans. Keep procedures out of the soul and time-bound facts out of everything. Inline skill: a folder with `SKILL.md` carrying `name`, a one-line `description` saying what it does and when to trigger, numbered steps each ending on a checkable criterion, and an output template.

Done when: the soul passes 5 varied questions with a consistent voice and boundaries, and answers `Unknown`, `UNVERIFIED` or `BLOCKED` instead of guessing when data is missing.

## Next stage

If the bot runs alone, bot-routine; then bot-access; then bot-score. Hand off with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. If a sibling is not installed, tell the user the next stage by name (routines get five parts, access gets least privilege, then a scorecard) and offer to do it.

## Reference files

- [references/profile-template.md](references/profile-template.md): read when filling step 2; the 13 sections with fill, avoid and example hints.
- [references/starter-frames.md](references/starter-frames.md): read in step 1 to pick a starter frame.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.

## Sources

- Masonshare, bot profile 13-criteria checklist and bot-type starter frames (original).
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
