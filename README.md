# Bot Design Team

[Tiếng Việt](README.vi.md)

Three AI bots and Agent Skills for designing prompts, skills and bots, built for [Orca](https://github.com/stablyai/orca) only.

| Bot | Role | Skills |
|---|---|---|
| Pink Pepper Coated Lotus Seeds | Prompt Designer: prompts, system prompts, prompt chains, bot souls | [`prompt-design`](skills/design/prompt-design/SKILL.md) and the other `prompt-*` skills |
| Mango Spring Roll | Skill Designer: turns workflows into tested Agent Skills | [`skill-design`](skills/design/skill-design/SKILL.md) and the other `skill-*` skills |
| Dried Plum | Bot Architect and Chief of Staff: bot profiles, teams, packaging | [`bot-design`](skills/design/bot-design/SKILL.md) and the other `bot-*` skills |

Each skill also works on its own, without the team.

## Pack: ecommerce-cskh

A ready-made two-bot pack for a Vietnamese e-commerce shop (Shopee, Zalo, hotline), in [`packs/ecommerce-cskh/`](packs/ecommerce-cskh/README.md). The owner keeps approved reply scripts in a Google Sheet.

| Bot | Role | Skills |
|---|---|---|
| Editor | Helps the owner draft and clean up scripts; drafts are always `Nháp` and only the owner approves | [`cskh-draft`](docs/skills/cskh-draft.md) |
| Staff | Helps staff answer customers from approved scripts only; read-only on scripts | [`cskh-lookup`](docs/skills/cskh-lookup.md), [`cskh-no-script`](docs/skills/cskh-no-script.md) |

The pack ships with FAKE sample data and replayable behaviour scenarios, no real data. See the pack README for the Sheet layout, Google permissions and rollout.

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
skills/        Agent Skills in buckets: design/ (promoted), in-progress/, deprecated/; each with references/vi.md (Vietnamese edition)
packs/         ready-made bot packs (ecommerce-cskh: Editor and Staff bots, FAKE data, scenarios)
docs/skills/   one page per promoted skill and per pack skill (what it does, when, questions, how to tell it works)
docs/agents/   notes for coding agents (issue tracker, labels, domain docs)
scripts/       repo checks (run `sh scripts/ci.sh`)
```

## No real data

This repo is public. Hard rule: no real company, customer or staff data goes into it, ever. Only fake examples (the pack's sample files are marked FAKE).

## Credits and license

The skills and souls are written by Masonshare. The ideas they draw from other people's work are rewritten and credited in [CREDITS.md](CREDITS.md). The repo is released under the MIT License: see [LICENSE](LICENSE).
