---
name: bot-design
description: Design one AI bot or a small team of bots for any platform (OpenMausBot, Grok Bot, or others) and package it - interview, go/no-go, shape (one bot, or one coordinator plus 2-3 specialists), bot profile, least-privilege permissions, soul, scorecard, then an OpenMausBot team.md or manual setup steps. Use when the user wants to create, plan, split, review or package a bot or bot team, asks whether a task needs a bot at all, or wants an existing bot profile scored. Vietnamese triggers - thiết kế bot, tạo bot, đội bot, hồ sơ bot, chấm điểm bot, đóng gói team bot, có cần bot không.
license: MIT
metadata:
  author: Masonshare
  version: "1.0.0"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot design

Turn a bot idea into a profile that a person can set up and trust, and score it before it ships. Platform-neutral; OpenMausBot packaging is step 8.

Reply in the user's language. Vietnamese users get Vietnamese output (full edition: `references/vi.md`).

Work loop: clarify, research, plan, build, verify. Steps 1-2 clarify, 3-4 plan, 5-6 build, 7 verify, 8 package. Stop at a **gate** (the user approves before work continues) before anything hard to reverse: publishing, sending, deleting, spending, installing, giving a bot write access, enabling a schedule.

## Handoff format

Bots pass work to each other, and to you, in one message with exactly these 5 fields, in this order:

1. Goal: one sentence.
2. Inputs: what is attached or linked.
3. Deliverable: what this bot produced (file names or inline).
4. Done when: the checkable acceptance criteria.
5. Open items: questions, risks, anything not done.

Your inputs may arrive as handoffs from a prompt designer (a soul or prompt plus test cases) and a skill designer (skill folders plus trigger tests). Your own handoff carries the profile, the scorecard result and the package.

## Steps

### 1. Interview (one batch)

For an existing bot, before changing its role, inventory its current instructions, skills and enabled states, permissions and connections, model, and all accessible automations (including enabled state, purpose, destination and schedule or event). Read saved state directly where permitted; identify activities that conflict with the proposed role. Report unresolved conflicts before any completion report and mark the redesign incomplete until resolved or the user explicitly accepts the remaining risk. Do not modify or pause them without authorization. Record each item, source and time, intended change, saved readback and outstanding conflict. If access is missing or a list cannot be confirmed complete, mark it `unverified`; a teammate's report is not a direct readback.

If a configuration request has multiple plausible interpretations and broad impact, present those interpretations and their affected scope, then clarify the decisive choice before writing changes.

Ask all of these in a single message, offering a default for each so the user can answer fast:

- Job: what the bot does, with 3 real examples, and what it must not do.
- User: who talks to it, their expertise, their language.
- Inputs: data, apps, files and accounts available.
- Outputs: format, destination, who reviews it.
- Frequency: on request, on a schedule, or on an event.
- Risks: what a wrong action costs (money, reputation, data).
- Budget: model cost tolerance, time to set up, who maintains it.
- Platform: OpenMausBot, Grok Bot or other.

Done when: each field has an answer or an agreed assumption written in the brief.

### 2. Go/no-go

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

### 3. Shape: one bot or a team

Default to 1 bot with 1 job. Split into a team only when the work has distinct specialties that would overload one context, and each specialist already works alone.

A team is 1 coordinator plus 2-3 specialists. The coordinator receives requests, routes each to the right specialist, merges the results into one answer, and reports real progress. It does no specialist work and holds no specialist tools. Every message between bots uses the handoff format above. Specialists report at three moments: start, done, stuck.

Describe each bot's behaviour with seven answers: trigger, inputs, steps, outputs, human checkpoints, success criteria, stop-and-ask rules (the exceptions where the bot halts and asks instead of guessing).

Done when: the user has approved the shape (gate) and every bot has a one-line job and a seven-answer spec.

### 4. Fill the bot profile

Use the 13 sections as suggestions, not a mandatory gate: overview, identity, soul, skills, memory, library, routines, access, model, permissions, voice/alerts, history, usage. Fill only the sections this bot needs. Mark each other section `not needed` with a one-line reason. Fill-in template with a fill/avoid/example hint per section: `references/profile-template.md`.

Layer the content by how often it is needed:
- Soul: what is true on every run, short.
- Skills: procedures that run only when relevant.
- Library: long reference documents, split by topic with dates.
- Memory: stable facts about the user, one line each.

Section essentials:

| Section | Fill with | Avoid |
|---|---|---|
| Overview | One sentence: helps [who] do [what] to get [result]; 3-5 in-scope jobs; 2-3 out-of-scope; one success metric | "General assistant" |
| Identity | Short name that hints at the job; title; 1-2 line description saying what it does and when to use it; language and form of address | Generic or duplicate names |
| Skills | 3-7 skills, each with a trigger description, numbered steps, a verify step, an output template | One giant skill; mechanical work left to the model instead of a script |
| Memory | Stable preferences, settled decisions with reasons, user corrections, naming | Anything expiring within a week, secrets, long text (point to Library) |
| Library | Small files by topic, update date, owner | One 50-page file; stale copies beside new ones |
| Routines | Repeatable work with predictable output; instructions that run without chat context; event triggers over frequent polling; draft-only output | Schedules every few minutes without need; routines that act irreversibly |
| Access | Only the apps the bot truly uses; read before write; who it may call and who may call it | Connecting everything for convenience |
| Model | The smallest model that passes the test cases; cheaper for high-volume routines | Strongest model everywhere |
| Voice/alerts | Notify only when action is needed: approval, error, deadline; short message saying what, what to do, where; quiet hours | Alerting every step |
| History | One thread per job; on a heavy thread, start a new one with a handoff | One endless thread |
| Usage | Token or cost per task tracked weekly; a limit and a warning | No measurement |

Done when: every section is either filled or marked `not needed` with a reason, and no filled section contains secrets.

### 5. Permissions

Apply least privilege. Grant read and search freely, drafts and writes inside a working folder within scope, and put a gate before every outward or irreversible action.

| Risk tier | Examples | Control |
|---|---|---|
| Low | Read, search, summarise | Autonomous, logged |
| Medium | Drafts, files in a working folder | Reviewed before leaving the workspace |
| High | Logins, payments, bulk changes | Gate every time; the human enters passwords, codes and CAPTCHAs |
| Critical | Delete data, sign, change policy | Do not automate |

- Read before write: start every connection read-only; add write access per tool when a test case needs it.
- Gate before sending, publishing, deleting, spending, installing, committing or pushing code, enabling a schedule.
- Money limits live in the platform's settings, not in prompt text.
- Credentials go only in the platform's secret or connection store. Keep secrets, webhook URLs and auth notes out of prompts, skills, memory, chat and files. Ask the user to add them through the secret store.
- Several labelled accounts for one app beat duplicate bots.

Done when: the permission table shows the worst case if the bot is wrong, and every irreversible action has a gate.

### 6. Write the soul and workflows

Delegate prompt craft to the `prompt-design` skill when it is available, passing a brief (goal, audience, inputs, constraints, definition of done) and receiving the soul plus test cases. Delegate workflows to the `skill-design` skill the same way. When they are missing, write inline:

Soul, 150-400 words, in this order: role in 1-2 sentences; the user and their expertise; voice; working principles, each with its reason; hard limits (ask first before sending, deleting, spending, committing); honest reporting (what was done, not done, what failed; never claim done before checking); when stuck, say so and name how to get the data. Prefer reasons over capital-letter bans. Keep procedures out of the soul and put them in skills. Keep time-bound facts out.

Skill (inline fallback): a folder with `SKILL.md` carrying `name`, a one-line `description` saying what it does and when to trigger, numbered steps each ending on a checkable criterion, and an output template.

Done when: the soul passes 5 varied questions with a consistent voice and boundaries.

### 7. Score and test

Report four separate states with evidence: **designed** (proposal exists), **applied** (change applied), **read back** (saved state independently read), and **behaviour tested** (actual test and evidence). Each can be pending or `unverified`; a teammate's claim is labelled teammate-reported and does not substitute for a direct readback. No profile score proves a saved setting or operational performance.

For coordinators include these safe cases; for each record input, expected result, actual result, evidence and pass/fail or `unverified` when not run:

| Input | Expected result |
|---|---|
| A newly available bot appears within accessible scope | Discover it using permitted current listings; route only after checking its fit. |
| No accessible specialist fits | Say so and offer an authorized alternative; do not invent a specialist. |
| A teammate claims completion without evidence | Mark teammate-reported; seek evidence or read back directly, otherwise `unverified`. |
| A request to send externally | Prepare a draft and seek the user's approval before sending; no real send during the test. |

If a teammate hits a usage limit, record the model before and after any authorized change, whether temporary or permanent, and the reason. Reassign the exact work and verify that the recipient acknowledged it; otherwise report it as pending. Call a fallback automatic only after testing that it actually occurs automatically.

Run 5-10 test cases and record results: 3 normal, 2 ambiguous, 2 out of scope, 2 asking for a risky action. Run a baseline first (a plain chat without the new profile), then the retest (with it), and compare. Fix failures and re-run.

Then score with the scorecard. Each item is 0 or 1, and only applicable items count; aim for at least 80%.

- [ ] Overview: one-sentence goal, in scope and out of scope
- [ ] Identity: name and description say what and when
- [ ] Soul: under 400 words, voice, limits, honest reporting, stuck handling
- [ ] Skills: 3-7, descriptions trigger correctly, each has a verify step and output template
- [ ] Memory: only stable facts, no secrets, nothing expiring
- [ ] Library: small dated files, no duplicates
- [ ] Routines: run alone, event-first, draft-only
- [ ] Access: only used connections, read before write
- [ ] Model: smallest that passes the test cases
- [ ] Permissions: every irreversible action has a gate
- [ ] Voice/alerts: notify only when action is needed
- [ ] History: one job per thread, handoff template
- [ ] Usage: cost measure and limit
- [ ] Test cases run and results recorded (always applicable)

`scripts/score_bot.py profile.md` measures **profile completeness** by content presence under the 13 headings (optional; shipped with the skill). It marks sections filled, empty or `not needed` and computes the ratio over applicable sections. It does not assess content quality, applied settings or behaviour. Evaluate quality with the checklist and behaviour with recorded tests separately.

Done when: the quality checklist and test results are reported separately, including shortfalls and unverified items with fixes; no completeness threshold alone establishes readiness.

### 8. Package and roll out

Choose by platform:

- OpenMausBot: write a team file `team.md` (BotMRR Markdown v1) the user imports through Teams, Import by pasting the public repo link. Essentials below; the full guide is `references/team-file.md`.
- Other platforms, or a single bot: write manual setup steps, one numbered list per bot: create the bot, paste identity and soul, add skills, connect apps read-only, set model, set permissions, add library files, create routines paused.

Roll out in this order, with a gate between stages:
1. One bot, proven alone on the test cases.
2. Routines, starting paused; run each by hand twice, then enable.
3. The team, last; add a bot to a group only after it works alone.

Review after 1-2 weeks using usage and history; trim any soul that grew, move procedures into skills.

Done when: the user has the package or the setup steps, the rollout order, and a 10-line summary: what the bot does, does not do, which permissions, approximate cost.

## OpenMausBot team file essentials

- Repo root holds `team.md` (or `botmrr.md`) on the main or master branch; the repo is public.
- YAML frontmatter keys: `botmrr: 1`, `id`, `release`, `name`, `tagline`, `summary`, `category`, `author` {name, url}, `license`, `tags`, `outcomes`, `setupMinutes`, `requirements` {apps, capabilities}, `agents` (each: key, name, title, description, soul, appearance {color, mascotExpression}, skills), `chiefOfStaff`, `rooms`, `routines` (each with `enabledAfterInstall: false`), `playbooks`, `skills` {version: 1, entries (each: name, description, license, instructions)}.
- `instructions` holds the full SKILL.md text and starts with `---`; its name, description and license match the SKILL.md frontmatter exactly.
- Body headings, all 7 required: Activation, Mission, Outcomes, Connections, Team, Chief of Staff, Completion rule.
- Colors: green, blue, red, orange, purple, cyan, pink, yellow, teal, coral, silver, chrome.
- Limits: soul up to 24000 bytes, description up to 4000 characters, at most 20 skills per v1 package.

## Platform note

Import carries bots' souls, skills text, rooms, the Chief of Staff and paused routines. It does not carry models, credentials, connections, memory, or the `references/` and `scripts/` of a skill (only the `SKILL.md` text travels). Imported skills arrive switched off. After import: pick a model per bot, switch skills on, connect apps yourself, and enable routines by hand. So keep each skill self-sufficient in its `SKILL.md`.

This repository's three-bot team defaults to exactly one assigned enabled skill per bot; inspect and read back all visible skill states. This is a package-specific setup target, not a rule for every redesigned bot: inventory existing skills and agree the appropriate set for its new role.

## Bot-type starter frames

Pick the nearest row as the starting point, then adjust.

| Type | Soul emphasis | Typical skills | Library | Permissions | Model |
|---|---|---|---|---|---|
| Marketplace operations | Exact numbers, never invent prices | Write listings, analyse orders, draft customer replies | Price list, marketplace policy, brand | Read and draft; never change prices alone | Mid |
| Content and image prompts | Brand voice; wait for approval of the direction before writing the full set | Brief, ideas, prompts, save .md by project structure | Brand guide, good prompt examples | Write the project folder; ask before spending credits | Strong for ideas, cheap for variants |
| Coding | Small scope; ask before adding a dependency; no commit or push unless told | Spec, issue, PR, review, handoff | Repo conventions | Read and write the repo; git needs approval | Strong |
| Research and analysis | Cite source and date; separate fact from inference | Look-up, compare, report | Trusted sources | Read only | Mid or strong |
| Secretary, calendar, email | Brief; list only what needs action | Filter important mail, prepare meetings, draft replies | Contacts, priority rules | Read and draft; never send alone | Small or mid |
| Coordinator (Chief) | Route to the right bot, merge into one answer, report real progress | Assign work, review errors, report overall | List of bots and roles | Manage bots, not exceed their rights | Strong |
| Data and reporting | Check the numbers before concluding | Clean, SQL, charts | Data dictionary | Read data, export files | Mid |

## References

- `references/profile-template.md`: read when filling step 4; it has the 13 sections with fill / avoid / example hints.
- `references/team-file.md`: read when packaging for OpenMausBot in step 8; full frontmatter, body, limits and an example.
- `references/sample-profile.md`: read to see a small scored profile; it is the input for `scripts/score_bot.py`.
- `references/vi.md`: read when the user writes in Vietnamese; full Vietnamese edition of this skill.

## Sources

- Masonshare, bot profile 13-criteria checklist, bot-type starter frames and scorecard (original).
- OpenMausBot documentation, https://docs.openmausbot.com/docs/features/skills and https://docs.openmausbot.com/docs/features/chat-and-teams (skills, teams, Chief of Staff).
- OpenMausBot repository docs, team-sharing and presets, https://github.com/milind-soni/OpenMausBot (what travels in a shared team).
- openmausbot-teams, FORMAT.md, https://github.com/milind-soni/openmausbot-teams (BotMRR Markdown v1).
- Agent Skills specification, https://agentskills.io/specification.
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
