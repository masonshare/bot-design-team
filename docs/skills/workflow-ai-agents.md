# workflow-ai-agents

## What it does

Guides a user through four steps (identify, research, blueprint, build and verify) that turn one repeatable business task into a single-purpose AI agent. It ends with an eight-part blueprint document and a reusable draft of the agent's instructions (a soul draft), plus a failure plan and tests. Two helper files hold the blueprint template and the soul draft. Body in Vietnamese, description bilingual.

Many people want to "make an agent" but pick the wrong job, skip researching how the work is really done, or have no failure plan or tests. The skill forces four gated steps and adds a Go or No-go check at the identification step. It overlaps in part with `bot-shape` and `bot-design`, the bot architecture skills of Dried Plum; use this one when the job is a single repeatable task, and those when you are designing a bot or a team. In testing it treated gate 1 as approved instead of waiting for the user, so make sure it stops. Reference points: the task repeats a few times a month or more, otherwise the build effort rarely pays back; at least 3 test cases (normal, missing data, out of scope); run it by hand twice before turning on a schedule; review 2 weeks after switching on, then every quarter. Every number in this skill is a labelled reference point; adjust it to your kind of work.

Source: [`packs/starter/dried-plum/skills/workflow-ai-agents/SKILL.md`](../../packs/starter/dried-plum/skills/workflow-ai-agents/SKILL.md)

## When to reach for it

Someone asks to build an agent for a task, automate a repeated job with AI, turn a chat routine into an agent, or get an agent blueprint. For a whole bot or several bots use `bot-design`.

## Common questions

**What do I get at the end?** A blueprint document and a draft of the agent's instructions you can reuse.

**When will it say No-go?** When the job is not repeated often enough, has no clear scope, or cannot be checked.

**Does it wait for my approval at each gate?** It should; if it ever skips one, say so and it must return to that gate.

## It's working if

- The identify step ends with an explicit Go or No-go that you approved.
- The blueprint has all eight parts and the soul draft is reusable.
- There is a failure plan and at least 3 test cases (normal, missing data, out of scope).
