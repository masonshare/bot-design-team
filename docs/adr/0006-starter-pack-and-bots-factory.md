# 0006. Starter pack replaces top-level bots/ and skills/

Status: Accepted. Amends 0001 and 0005 (rule 5 and the skill buckets).

## Context

The repo is renamed Bots Factory: a production line for AI bots for small businesses. The four design bots and their skills lived in two top-level folders (`bots/`, `skills/`), apart from the packs. Two places for the same thing, and a reader could not tell which bots to install first.

## Decision

- The four design bots become one pack, `packs/starter/`, the mandatory first install. Every other pack needs Starter first.
- Layout: `packs/starter/<bot>/SOUL.md` (English), `SOUL.vi.md` (Vietnamese), `skills/<name>/SKILL.md` (bot-home form, as in 0005). Bots: `dried-plum` (bot architecture), `mango-spring-roll` (skills), `pink-pepper-coated-lotus-seeds` (souls and prompts), `ask-masonshare` (Chief of Staff).
- No top-level `skills/` or `bots/`. The buckets `design`, `in-progress`, `deprecated` are gone; a skill under work lives in its pack.
- Docs pages stay flat at `docs/skills/<name>.md` (0005 rule 3 unchanged).
- Dried Plum does bot architecture only; routing and handoff belong to Ask Masonshare.

## Consequences

- `scripts/check-layout.sh` fails if `skills/` or `bots/` reappears; `scripts/check-frontmatter.py` scans `packs/` only.
- `npx skills add` finds the skills by recursive search (checked in `docs/for-developers.md`). Orca delivers bots by share link, not by scanning.
- Rule 5 of 0005 is void: there are no repo-level skills outside packs.
