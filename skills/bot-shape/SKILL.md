---
name: bot-shape
description: Decides whether work belongs in one bot or a team of bots and specifies each bot's behaviour. Use when the user asks how many bots they need, wants one bot split into several, wants two bots merged, asks who should coordinate, or has a bot that does too many jobs. Produces the shape (one bot, or one coordinator plus 2-3 specialists), a one-line job and a seven-answer spec per bot, and a gate for the user's approval. Not for deciding whether a bot is needed at all, filling profile sections, routines, permissions, scoring or packaging. Vietnamese triggers - tách bot, gộp bot, cần mấy bot, đội bot, bot điều phối, chia việc giữa các bot.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot shape

Choose the smallest structure that works: one bot with one job, or a coordinator with a few specialists. Stage 2 of the bot design flow.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Changing the shape is a **gate**: the user approves it before anything is built or changed.

## Steps

### 1. Read the brief

Take the interview brief (job, anti-job, inputs, outputs, frequency, risks). If none exists, ask for the job with 3 examples and the anti-job first; without them any shape is a guess, so mark it as one.

Done when: the jobs to place are listed, one line each.

### 2. Choose the shape

Default to 1 bot with 1 job. Split into a team only when the work has distinct specialties that would overload one context, and each specialist already works alone.

Merge two bots when they never work apart: same inputs, same user, always run together. Say which test decided it.

A team is 1 coordinator plus 2-3 specialists. The coordinator receives requests, routes each to the right specialist, merges the results into one answer and reports real progress. It does no specialist work and holds no specialist tools. Specialists report at three moments: start, done, stuck. Every message between bots uses the 5-field handoff (see Next stage).

The number of skills a bot owns is not a reason to split it. A split that comes from a bloat warning (a soul or description past about 600 words) is proposed here and needs the same approval.

Done when: the shape and the reason for it are written in two sentences.

### 3. Specify each bot

Describe each bot's behaviour with seven answers: trigger, inputs, steps, outputs, human checkpoints, success criteria, stop-and-ask rules (the exceptions where the bot halts and asks instead of guessing).

Output template:

```
Shape: <one bot | coordinator + N specialists>. Why: <test that decided it>
Bot: <name> - <one-line job>
 Trigger / Inputs / Steps / Outputs / Human checkpoints / Success criteria / Stop-and-ask
```

Done when: the user has approved the shape (gate) and every bot has a one-line job and a seven-answer spec.

## Next stage

Hand off to bot-profile, one bot at a time, with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. If bot-profile is not installed, tell the user the next stage is to fill the 13-section profile for each bot (unneeded sections marked with a reason) and offer to start.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.

## Sources

- Masonshare, bot design process (original).
- OpenMausBot documentation, https://docs.openmausbot.com/docs/features/chat-and-teams (teams, Chief of Staff).
