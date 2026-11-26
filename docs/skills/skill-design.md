# skill-design

## What it does

Runs the whole job of building an Agent Skill from a first idea to a published folder, taking the intake and handing each stage to the matching skill-* sibling.

Source: [`packs/starter/mango-spring-roll/skills/skill-design/SKILL.md`](../../packs/starter/mango-spring-roll/skills/skill-design/SKILL.md)

## When to reach for it

You want to create a skill from a workflow, SOP or knowledge, or do not know which skill step comes next.

## Common questions

**Do I need it for one step?** No. Use the stage skill, for example skill-write.

**What are the stages?** Search, write, test, review, package.

**Where does the result go?** A skill folder ready to install.

## It's working if

- A named stage was handed to the right sibling skill.
- The finished folder passes scripts/validate_skill.py (in skill-package).
- A go or no-go on the idea was recorded first.
