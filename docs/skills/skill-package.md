# skill-package

## What it does

Validates a skill folder against the Agent Skills spec and packages it for sharing, with a version bump, a changelog entry and the right layout for npx skills add.

Source: [`skills/design/skill-package/SKILL.md`](../../skills/design/skill-package/SKILL.md)

## When to reach for it

You want a skill checked before shipping, or ask how to publish it or where it goes on Claude Code or Orca.

## Common questions

**How do I validate?** `python scripts/validate_skill.py <skill-folder>` from this skill's folder.

**Do nested buckets work?** Yes. `npx skills add` finds skills/design/<name>/SKILL.md; see docs/orca-skill-loading.md.

**Which version number?** The skill explains how to pick one.

## It's working if

- validate_skill.py reports all checks passed.
- The changelog entry and version bump exist.
- `npx skills add <repo> --list` shows the skill.
