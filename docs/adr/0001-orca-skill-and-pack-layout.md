# 0001. Follow Orca's skill loading and share model

Status: Accepted. Owner checks V1 to V3 and V6 are confirmed (Orca 1.4.274, Windows); V4 and V5 stay pending until the pilot-staff phase. See `docs/orca-skill-loading.md` section 6.

## Context

The repo ships skills and a bot pack that run in Orca. Public Orca docs do not say which directories Orca reads or what a bot share link carries. Reading the installed Orca 1.4.271 shows:

- A bot's own skills live at `skills/<name>/SKILL.md` in its home. Orca links them into `.claude/skills` and `.agents/skills` itself at chat start.
- Project skills are discovered under `<repo>/.agents/skills`, `<repo>/.claude/skills` and other per-agent folders. A bare top-level `skills/` is not scanned.
- A bot share link ("anyone with the link can make a copy") carries `bot.json`, `SOUL.md`, ticked skills and memory, tool URLs without secrets, connector kinds, and schedules that arrive disabled.

Evidence and the list of unverified items are in `docs/orca-skill-loading.md`.

## Decision

1. Author skills as `skills/<name>/SKILL.md` (lowercase-dash names, self-contained, agent-neutral). Distribute them to projects with `npx skills add`, which fills `.agents/skills`.
2. Deliver the pack through a bot share link. Pack skills use the bot-home form `skills/<name>/`. Nothing is hand-placed into `.claude/skills` or `.agents/skills` in a bot home.
3. Share links carry no real data. Real scripts, prices and chats stay in the owner's Google Sheet.
4. Editor bot and Staff bot are separate shared bots. The agent in the package is a hint only.

## Consequences

- The repo layout keeps `skills/<name>/SKILL.md` as the unit and groups skills in buckets (`skills/design/`, `skills/in-progress/`, `skills/deprecated/`); `npx skills add` was checked to find nested skills. It documents the install path into `.agents/skills`. The layout must not assume Orca reads `skills/` at the repo root.
- The pack is built as a bot package (SOUL.md, skills, optional memory, short setup note) and must not rely on schedules being enabled.
- This rests on Orca internals, not a documented API. A new Orca version may change it, so the docs page records the versions (code read on 1.4.271, owner checks on 1.4.274) and the owner verification steps V1 to V6. V1 and V2 passed, so this ADR stands. If V4 or V5 fail at the pilot-staff phase, revise it.
