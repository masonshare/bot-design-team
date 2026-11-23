---
name: bot-interview
description: Interviews the user about a bot idea in one batch of questions and decides whether a bot is the right tool at all. Use when the user describes a task and asks whether it needs a bot, a skill, a prompt or a plain automation, or whether it is worth building a bot at all versus doing it by hand, wants the requirements for a bot gathered, or wants an existing bot's current setup inventoried before its role changes. Produces a brief (job, anti-job, user, inputs, outputs, frequency, risks, budget, platform) and a go/no-go verdict. Not for splitting work across several bots, filling a profile, routines, permissions, scoring or packaging. Vietnamese triggers - có cần bot không, có đáng làm bot không, làm tay hay làm bot, phỏng vấn yêu cầu bot, bot hay skill hay prompt, kiểm kê bot hiện có, go/no-go.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot interview and go/no-go

Learn what the bot must do, then pick the lightest tool that does the job. Stages 1-2 of the bot design flow; the next stage is bot-shape.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Stop at a **gate** (the user approves before work continues) before anything hard to reverse. This skill only reads and asks; it changes nothing.

## Steps

### 1. Inventory (only for an existing bot)

Before changing the role of a bot that already exists, list its current instructions, skills and enabled states, permissions and connections, model, and every automation you can access (enabled state, purpose, destination, schedule or event). Read saved state directly where permitted and find activities that conflict with the proposed role. Do not modify or pause anything without authorization.

Record per item: source and time, intended change, saved readback, outstanding conflict. If access is missing or a list cannot be confirmed complete, mark it `unverified`; a teammate's report is not a direct readback. Report open conflicts before any completion report, and mark the redesign incomplete until they are resolved or the user accepts the remaining risk.

If a configuration request has several plausible readings and a broad impact, show the readings and what each would affect, and get the deciding choice before writing any change.

Done when: the inventory is written with sources, or the bot is new and this step is skipped.

### 2. Ask, in one message

Ask all of these in one message, each with a default so the user can answer fast:

- Job: what the bot does, with 3 real examples.
- Anti-job (required): 2-4 lines on what the bot must never do, even when asked.
- User: who talks to it, their expertise, their language.
- Inputs: data, apps, files and accounts available.
- Outputs: format, destination, who reviews it.
- Frequency: on request, on a schedule, or on an event.
- Risks: what a wrong action costs (money, reputation, data).
- Budget: model cost tolerance, time to set up, who maintains it.
- Platform: Orca (this repo targets Orca only).

Done when: each field has an answer or an agreed assumption written in the brief.

### 3. Go/no-go

Pick the lightest tool that does the job:

| Situation | Use |
|---|---|
| One-off or rare, no memory or tools needed | A prompt |
| A repeatable procedure the user already drives in chat | A skill |
| Fixed steps, fixed inputs, no judgment | A plain automation (cron, n8n, Make) |
| Recurring work with judgment, context that must persist, tools or a schedule | A bot |
| Heavy human judgment on every step, or irreversible stakes | No bot; give a checklist |

Start from the most boring task the user knows step by step. Say the verdict and the reason in two sentences.

Done when: the user has seen the verdict. If it is not "bot", stop and deliver the lighter option.

## Next stage

On "bot", hand off to bot-shape with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. Deliverable is the brief. If bot-shape is not installed, tell the user the next stage is to decide one bot or a team (default one bot, one job) and offer to do it from the brief.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.

## Sources

- Masonshare, bot design process (original).
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
