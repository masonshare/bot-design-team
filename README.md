# Bot Design Team

[Tiếng Việt](README.vi.md)

Three AI bots and Agent Skills for designing prompts, skills and bots, built for [Orca](https://github.com/stablyai/orca) only.

| Bot | Role | Skills |
|---|---|---|
| Pink Pepper Coated Lotus Seeds | Prompt Designer: prompts, system prompts, prompt chains, bot souls | [`prompt-design`](skills/prompt-design/SKILL.md) and the other `prompt-*` skills |
| Mango Spring Roll | Skill Designer: turns workflows into tested Agent Skills | [`skill-design`](skills/skill-design/SKILL.md) and the other `skill-*` skills |
| Dried Plum | Bot Architect and Chief of Staff: bot profiles, teams, packaging | [`bot-design`](skills/bot-design/SKILL.md) and the other `bot-*` skills |

Each skill also works on its own, without the team.

## Direction

This repo is Orca-only. Bots run inside Orca on the user's own machine and subscription, and are shared with Orca's bot share link. The earlier platform-specific material was removed; it stays available at the git tag `v0-openmausbot`.

## Install the skills

Requires Node.js. The installer copies the skills into your coding agent (Claude Code, Codex, Cursor and others):

```bash
npx skills add masonshare/bot-design-team            # pick skills and agents interactively
npx skills add masonshare/bot-design-team --list     # preview what is inside
npx skills add masonshare/bot-design-team --skill prompt-design
npx skills add masonshare/bot-design-team -g         # install for your user, not one project
```

## Set the bots up in Orca

Create each bot in Orca, paste its soul from [`bots/`](bots/) and enable the skills from the table above. Disable every visible skill that none of the bot's jobs uses, and pick a model for each bot. The `bot-package` skill walks through the steps and the rollout order.

## Layout

```
bots/          the three souls (standing instructions), English and Vietnamese
skills/        Agent Skills, each with references/vi.md (Vietnamese edition)
docs/agents/   notes for coding agents (issue tracker, labels, domain docs)
scripts/       repo checks
```

## No real data

This repo is public. No real company, customer or staff data goes into it: only fake examples.

## Credits and license

The skills and souls are written by Masonshare. The ideas they draw from other people's work are rewritten and credited in [CREDITS.md](CREDITS.md). The repo is released under the MIT License: see [LICENSE](LICENSE).
