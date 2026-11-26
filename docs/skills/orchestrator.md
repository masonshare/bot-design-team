# orchestrator

## What it does

Navigator and router for the marketing-ecommerce pack. It picks the right skill for a request (router), sequences several skills into a phased plan for a project (planner), and checks which skills a project is missing and what to do first (diagnoser). It coordinates; the other skills do the work, and it always ends with a concrete next step. Say a keyword to choose the depth: express (match now, almost no questions), guided (the default, a short intake first) or deep (a multi-skill project with gates and handoff blocks). Body in English, description bilingual. Two reference files hold an ecosystem map (what each skill is for, what it needs, where it hands off, and close calls) and ten sample project paths.

The pack has more than twenty skills, and new users do not know where to start or pick a neighbouring skill by mistake. The skill lists only the skills that ship in the pack and never recommends another name as if it were installed. Skills from the strategy-advisor pack and a skill-design skill appear only as soft suggestions "if installed", with a plain-answer fallback when they are not. The order rules are explicit so plans stay consistent: brand voice before copy, a lead magnet before email, a landing page check before buying traffic. When a request needs a handoff, it passes a short block (goal, audience, voice rules, decisions made, open questions) that any agent or person can read. When no skill fits, it says so and offers to do the task in place instead of forcing a match. Reference points: at most 5 skills in a first plan for a newcomer; 5 intake questions (3 for the diagnoser), each with a default; sample paths run from 1 to 8 weeks, to compare with your team's capacity. Every number is a reference point. Trade-off: the skill lists in `SKILL.md` and `references/ecosystem-map.md` must be updated whenever the pack adds or drops a skill; `scripts/check-orchestrator-skills.py` fails CI when they drift from the folder.

Source: [`packs/marketing-ecommerce/skills/orchestrator/SKILL.md`](../../packs/marketing-ecommerce/skills/orchestrator/SKILL.md)

## When to reach for it

Someone asks which skill to use, where to start, to plan a launch, a campaign, shop growth or a content month, what to do next, or describes a marketing, brand, copy, content, funnel, ads or e-commerce goal without naming a skill. If the user already names a skill, go straight to that skill.

## Common questions

**Does it do the work itself?** No. It routes and plans, then hands off to the specialist skill.

**What if a skill it names is not installed?** It says so in one line and finishes the part it can do. Strategy-advisor skills are always offered only as "if installed".

**How is the list kept correct?** A CI check compares the lists in the skill with the pack folder, so a renamed or missing skill turns CI red.

## It's working if

- The answer names a skill that exists in the pack, with the reason, and ends with a concrete next step.
- A multi-skill plan is in a sensible order (brand voice before copy, lead magnet before email) with a decision gate per phase.
- When nothing fits, it says so instead of forcing an approximate match.
