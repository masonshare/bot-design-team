# For developers

The README is for shop owners. This page is for people who build, test or change the bots. Nothing here is needed to use a bot.

## What this repo is

Bots Factory is a production line for AI bots: describe the job, design it, test it, hand over a ready bot. The bots run in [Orca](https://github.com/stablyai/orca) on the user's own machine and subscription, on top of Claude Code or Codex. Orca shares a bot with its bot share link.

Terms used in these docs:

- **Harness**: everything around the model that makes it an agent: the loop, tools, permissions, steering files. Claude Code and Codex are harnesses.
- **Soul**: a bot's standing instructions (`SOUL.md`), loaded at the start of every chat.
- **Skill**: a folder with a `SKILL.md` that teaches an agent one job. Written to be neutral, so it runs on Claude Code and Codex.
- **Pack**: a set of bots, skills and sample data you can install together.

## Layout

```
packs/starter/              the mandatory first pack: 4 bots
  <bot>/SOUL.md             soul (English, the one that is used)
  <bot>/SOUL.vi.md          Vietnamese reading copy
  <bot>/skills/<name>/      the bot's skills, most with references/vi.md
packs/ecommerce-cskh/       use-case pack: Editor and Staff bots, FAKE data, scenarios
docs/skills/                one page per pack skill (what it does, when, questions, how to tell it works)
docs/adr/                   decisions (pack layout: ADR 0005 and 0006)
docs/agents/                notes for coding agents (issue tracker, labels, domain docs)
scripts/                    repo checks (run `sh scripts/ci.sh`)
```

The map with every path is in [`repo-map.md`](repo-map.md).

## Install the skills with npx

Needs Node.js. The installer copies skills into your coding agent (Claude Code, Codex, Cursor and others). It finds skills in nested folders, so the pack layout works:

```bash
npx skills add masonshare/bots-factory            # pick skills and agents interactively
npx skills add masonshare/bots-factory --list     # preview what is inside
npx skills add masonshare/bots-factory --skill prompt-design
npx skills add masonshare/bots-factory -g         # install for your user, not one project
```

Installing the skills does not create the bots. A bot is its soul plus its skills.

## Set the bots up in Orca

Create each bot in Orca, paste its soul from `packs/starter/<bot>/SOUL.md` and enable the skills in that bot's folder. Disable every visible skill that none of the bot's jobs uses, and pick a model for each bot. Start a new chat after any change: an open chat does not reload the soul or the skills. The `bot-package` skill walks through the steps and the rollout order. How Orca loads skills and bots: [`orca-skill-loading.md`](orca-skill-loading.md).

## CI and tests

`sh scripts/ci.sh` runs every static check (frontmatter, layout, no leftovers, scenarios, no real data, glossary, repo map). `sh scripts/tests/run.sh` breaks one rule at a time and checks CI goes red. Scenarios that replay a pack against a real agent: [`scenario-testing.md`](scenario-testing.md), including the Windows quirks. The merge gate is in [`../CONTRIBUTING.md`](../CONTRIBUTING.md).

## No real data

This repo is public. No real company, customer, staff, price or chat data goes into it. Only fake examples (sample files are marked FAKE). `scripts/check-no-real-data.py` enforces it in CI.

## Earlier platforms

Bots Factory targets Orca only. Material for the earlier platforms, OpenMausBot and Grok, was removed from the main branch; the full text stays at the git tag `v0-openmausbot`.

## Credits and license

Ideas from other people's work are rewritten and credited in [`../CREDITS.md`](../CREDITS.md). MIT License: [`../LICENSE`](../LICENSE).
