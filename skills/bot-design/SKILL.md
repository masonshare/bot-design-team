---
name: bot-design
description: Front door for designing one AI bot or a small team of bots on any platform (Orca). Use when the request covers the whole job or the stage is unclear, for example create a bot, plan a bot team, turn an idea into a bot someone can set up. Holds the shared rules (work loop, approval gates, 5-field handoff) and routes each stage to its own skill (bot-interview, bot-shape, bot-profile, bot-routine, bot-access, bot-score, bot-package). Not for a single stage the user already names, which goes straight to that stage skill. Vietnamese triggers - thiết kế bot, tạo bot mới, lên kế hoạch đội bot, tôi muốn có một bot, từ ý tưởng thành bot.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot design

Turn a bot idea into a bot that a person can set up and trust. This skill is the front door: it keeps the shared rules and sends each stage to the skill that owns it.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use (full edition: `references/vi.md`).

Work loop: clarify, research, plan, build, verify. Stop at a **gate** (the user approves before work continues) before anything hard to reverse: publishing, sending, deleting, spending, installing, giving a bot write access, enabling a schedule.

## Stages

| # | Stage | Skill | Result |
|---|---|---|---|
| 1 | Interview and go/no-go | bot-interview | A brief and a verdict: prompt, skill, automation, bot, or no bot |
| 2 | Shape | bot-shape | One bot, or one coordinator plus 2-3 specialists; a spec per bot |
| 3 | Profile | bot-profile | The 13-section profile, plus the brief for the soul and skills |
| 4 | Routines | bot-routine | A five-part spec per unattended run (only when the bot runs alone) |
| 5 | Access | bot-access | Permissions, connections and secret handling at least privilege |
| 6 | Score and test | bot-score | Scorecard, test cases, evidence per conclusion |
| 7 | Package | bot-package | Manual setup steps or an Orca share link, rollout order, summary |

Run one stage at a time, in order, starting at the first stage whose output the user has not approved. Pass each result on in the handoff format below. Skip stage 4 when the bot has no unattended runs. For a single stage the user names ("score this profile"), run only that stage's skill.

## When a stage skill is not installed

Run the stage yourself from this summary, then tell the user which skill would do it in depth.

1. Interview: ask everything in one message, each question with a default: job with 3 real examples, anti-job (2-4 lines of what it must never do), user, inputs, outputs, frequency, risks, budget, platform. Then pick the lightest tool: a prompt (one-off), a skill (repeatable procedure driven in chat), a plain automation (fixed steps, no judgment), a bot (recurring work with judgment, memory, tools or schedule), or no bot with a checklist (heavy judgment or irreversible stakes). State the verdict and reason in two sentences.
2. Shape: default to 1 bot with 1 job. A team is 1 coordinator plus 2-3 specialists, only when distinct specialties overload one context and each specialist already works alone. The coordinator routes, merges and reports; it holds no specialist tools. Write a one-line job per bot. Gate: the user approves the shape.
3. Profile: fill the 13 sections the bot needs (overview, identity, soul, skills, memory, library, routines, access, model, permissions, voice/alerts, history, usage) and mark each other one `not needed` with a reason. Keep the soul short (150-400 words) and procedures in skills.
4. Routines: every routine has an owner (a named person), a trigger, allowed actions, an escalation path and a stop condition; start it paused.
5. Access: least privilege. Read before write. A gate before every send, publish, delete, spend, install, commit or push. Credentials only in the platform's secret store.
6. Score: report designed, applied, read back and behaviour tested as four separate states, each conclusion with its evidence; run 5-10 test cases, baseline first then retest; score the 14 checklist items 0 or 1 each (13 profile items plus the always-applicable test item), counting only applicable items; aim for 80%.
7. Package: write numbered manual steps for Orca, or share the bot with Orca's bot share link; note that only each skill's SKILL.md may travel. Roll out one bot first, routines paused, the team last.

## Shared rules

- Existing bot: inventory its instructions, skills, permissions, connections and automations before changing its role. A teammate's report is not a readback; mark what you could not read `unverified`.
- Credentials, tokens and webhook URLs never go in a prompt, skill, memory, chat or file. Ask the user to add them through the platform's secret or connection store.
- A bot may own as many skills as its role needs, one per procedure; the count is not a warning sign, overlapping descriptions are.
- When a prompt designer or skill designer exists, delegate soul and skill writing to them with a brief; do not redo their work here.

## Handoff format

Bots pass work to each other, and to you, in one message with exactly these 5 fields, in this order:

1. Goal: one sentence.
2. Inputs: what is attached or linked.
3. Deliverable: what this bot produced (file names or inline).
4. Done when: the checkable acceptance criteria.
5. Open items: questions, risks, anything not done.

Your inputs may arrive as handoffs from a prompt designer (a soul or prompt plus test cases) and a skill designer (skill folders plus trigger tests). Your own handoff carries the profile, the scorecard result and the package.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.

## Sources

- Masonshare, bot profile 13-criteria checklist and scorecard (original).
- Agent Skills specification, https://agentskills.io/specification.
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
