# Bot Design Team

[Tiếng Việt](README.vi.md)

Three AI bots and three Agent Skills for designing prompts, skills and bots.

| Bot | Role | Skill |
|---|---|---|
| Pink Pepper Coated Lotus Seeds | Prompt Designer: prompts, system prompts, prompt chains, bot souls | [`prompt-design`](skills/prompt-design/SKILL.md) |
| Mango Spring Roll | Skill Designer: turns workflows into tested Agent Skills | [`skill-design`](skills/skill-design/SKILL.md) |
| Dried Plum | Bot Architect and Chief of Staff: bot profiles, teams, packaging | [`bot-design`](skills/bot-design/SKILL.md) |

Each skill also works on its own, without the team.

## Install the skills

Requires Node.js. The installer copies the skills into your coding agent (Claude Code, Codex, Cursor and others):

```bash
npx skills add masonshare/bot-design-team            # pick skills and agents interactively
npx skills add masonshare/bot-design-team --list     # preview what is inside
npx skills add masonshare/bot-design-team --skill prompt-design
npx skills add masonshare/bot-design-team -g         # install for your user, not one project
```

## Create the team in OpenMausBot

1. Open **Teams → Import** and paste `https://github.com/masonshare/bot-design-team`.
2. Review and import. OpenMausBot creates the 3 bots with their souls and skills.
3. After the import:
   - Switch the 3 skills on, because imported skills arrive switched off.
   - Pick a model for each bot, because models do not travel with the file.

The team file is [`team.md`](team.md). It is plain Markdown, so you can also give it to any agent that can act as a Chief of Staff.

## Set the bots up by hand

To build the bots by hand in OpenMausBot or Grok Bot, see [guides/en](guides/en/README.md). The readable souls are in [`bots/`](bots/).

## Layout

```
team.md        OpenMausBot team file (generated from bots/ and skills/)
bots/          the three souls (standing instructions), English and Vietnamese
skills/        three Agent Skills, each with references/vi.md (Vietnamese edition)
guides/        manual setup for OpenMausBot and Grok Bot, English and Vietnamese
```

## Credits and license

The skills and souls are written by Masonshare. The ideas they draw from other people's work are rewritten and credited in [CREDITS.md](CREDITS.md). The repo is released under the MIT License: see [LICENSE](LICENSE).
