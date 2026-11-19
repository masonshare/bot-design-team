---
name: bot-package
description: Packages a designed bot or bot team for rollout, as an OpenMausBot team file (team.md, BotMRR Markdown v1) or as numbered manual setup steps for Grok Bot and other platforms, with the rollout order and a 10-line summary. Use when the user wants to export, share or publish a team, make a team.md, import a team into OpenMausBot, set a bot up by hand on another platform, or learn what an import carries and what it drops. Not for deciding whether a bot is needed, designing the profile, routines, permissions or scoring. Vietnamese triggers - đóng gói team bot, tạo team.md, chia sẻ đội bot, nhập team vào OpenMausBot, cài đặt bot thủ công, import mang theo gì.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Bot package and rollout

Hand over something a person can install, in an order that stays safe. Stage 7 of the bot design flow.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Publishing, pushing to a repository, installing and enabling a schedule are **gates**: the user approves each first. Writing the package is not publishing it.

## Steps

### 1. Choose by platform

- OpenMausBot: write a team file `team.md` (BotMRR Markdown v1). The user imports it through Teams, Import, by pasting the public repo link.
- Other platforms, or a single bot: write manual setup steps, one numbered list per bot: create the bot, paste identity and soul, add skills, connect apps read-only, set the model, set permissions, add library files, create routines paused.

Done when: the platform is named and the route chosen.

### 2. Write the team file (OpenMausBot)

Essentials; the full guide with an example is `references/team-file.md`. When it disagrees with the openmausbot-teams FORMAT.md or the app, those win; check before publishing.

- Repo root holds `team.md` (or `botmrr.md`) on the main or master branch; the repo is public.
- YAML frontmatter keys: `botmrr: 1`, `id`, `release`, `name`, `tagline`, `summary`, `category`, `author` {name, url}, `license`, `tags`, `outcomes`, `setupMinutes`, `requirements` {apps, capabilities}, `agents` (each: key, name, title, description, soul, appearance {color, mascotExpression}, skills), `chiefOfStaff`, `rooms`, `routines` (each with `enabledAfterInstall: false`), `playbooks`, `skills` {version: 1, entries (each: name, description, license, instructions)}. Unknown keys are rejected.
- `instructions` holds the full SKILL.md text, starts with `---`, and its name, description and license match the SKILL.md frontmatter exactly.
- Body headings, all 7 required, in order: Activation, Mission, Outcomes, Connections, Team, Chief of Staff, Completion rule.
- Colors: green, blue, red, orange, purple, cyan, pink, yellow, teal, coral, silver, chrome.
- Limits: soul up to 24000 bytes, description up to 4000 characters, at most 20 skills per v1 package, file up to 1,000,000 bytes.

Check before publishing: seven headings present; every agent complete; `chiefOfStaff` matches an agent key; every listed skill exists in `skills.entries`; all routines paused; no secret, token or webhook URL anywhere.

Done when: the checks pass and the file is shown to the user (not yet published).

### 3. Tell the user what the import carries

Import carries the bots' souls, skill text, rooms and the Chief of Staff. It usually carries routines too, paused, but that is not guaranteed: re-read the automation list after import. It does not carry models, credentials, connections, memory, or the `references/` and `scripts/` of a skill; only the `SKILL.md` text travels, so each skill must work from its SKILL.md alone. Imported skills arrive switched off. After import: pick a model per bot, switch skills on, connect apps yourself, enable routines by hand, and compare the routines declared in `team.md` with the real automation list, adding what is missing (paused) and reporting any difference.

Assign skills by role: each enabled skill ties to one job in its bot's Job, and skills no job uses are disabled or removed, including inherited ones. A bot can own many skills.

### 4. Set the rollout order

Roll out in this order, with a gate between stages:
1. One bot, proven alone on the test cases.
2. Routines, starting paused; check each has its five parts, run each by hand twice, then enable.
3. The team, last; add a bot to a group only after it works alone.

Review after 1-2 weeks using usage and history; trim any soul that grew and move procedures into skills.

### 5. Summarise

Done when: the user has the package or the setup steps, the rollout order, and a 10-line summary: what the bot does, does not do, which permissions, approximate cost.

## Reference files

- [references/team-file.md](references/team-file.md): read in step 2; full frontmatter, body, limits and an example.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese.

## Sources

- openmausbot-teams, FORMAT.md, https://github.com/milind-soni/openmausbot-teams (BotMRR Markdown v1).
- OpenMausBot documentation, https://docs.openmausbot.com/docs/features/skills and https://docs.openmausbot.com/docs/features/chat-and-teams; repository docs team-sharing and presets, https://github.com/milind-soni/OpenMausBot (what travels in a shared team).
- Grok Bot, templates guide (what a template carries), https://x.ai/bot/guides/templates-for-grok-bot.
