# skill-search

## What it does

Searches for an existing Agent Skill before building, reads the candidates, and gives a go or no-go verdict on whether the idea deserves a skill.

Source: [`skills/design/skill-search/SKILL.md`](../../skills/design/skill-search/SKILL.md)

## When to reach for it

You ask whether a skill for X exists, or whether something is worth a skill rather than a prompt or an AGENTS.md rule.

## Common questions

**Where does it search?** `npx skills find` and skills.sh.

**Can the verdict be no?** Yes. Reuse or a prompt may be better.

**Does it install anything?** No.

## It's working if

- Candidates were read, not just listed.
- The verdict names reuse, build or skip with a reason.
- You did not build something that already existed.
