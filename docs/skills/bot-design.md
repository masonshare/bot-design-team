# bot-design

## What it does

Front door for designing one bot or a small team. It holds the shared rules (work loop, approval gates, 5-field handoff) and routes each stage to the matching bot-* skill.

Source: [`skills/design/bot-design/SKILL.md`](../../skills/design/bot-design/SKILL.md)

## When to reach for it

You want to create a bot or plan a bot team and the stage is unclear, or the request covers the whole job from idea to setup.

## Common questions

**Do I need it if I know my stage?** No. Go straight to the stage skill, for example bot-profile or bot-access.

**What are the stages?** Interview, shape, profile, routine, access, score, package, each with its own skill.

**Does it write files?** It plans and hands off between stages; the stage skills produce the artifacts.

## It's working if

- You leave with a named next stage and a 5-field handoff, not a vague plan.
- Each approval gate was shown to you before any outward action.
- The stage skills were used one at a time rather than everything at once.
