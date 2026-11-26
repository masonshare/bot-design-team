# bot-routine

## What it does

Writes or audits a bot's routines (scheduled or event-triggered runs) with a five-part spec: owner, trigger, allowed actions, escalation path, stop condition. Also sets up the optional weekly healthcheck.

Source: [`packs/starter/dried-plum/skills/bot-routine/SKILL.md`](../../packs/starter/dried-plum/skills/bot-routine/SKILL.md)

## When to reach for it

You want a bot to run on its own every morning or week, or when an event happens, or want existing routines reviewed.

## Common questions

**Is a routine always right?** No. First check a plain automation would not do.

**What is the healthcheck?** An optional weekly routine, described in references/healthcheck-routine.md.

**Can routines act outward?** Only inside allowed actions and with the escalation path defined.

## It's working if

- Each routine has all five parts filled.
- It can be switched off and has a stop condition.
- A dry run produced the expected result before it was enabled.
