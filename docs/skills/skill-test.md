# skill-test

## What it does

Tests one skill: trigger tests check the description fires on the right prompts and no others; task tests compare a baseline without the skill to a retest with it.

Source: [`skills/design/skill-test/SKILL.md`](../../skills/design/skill-test/SKILL.md)

## When to reach for it

You want to know whether a skill triggers reliably, or need test prompts or an evals.json.

## Common questions

**What is a trigger test?** Prompts that should and should not fire the skill.

**Where is the method?** references/testing.md.

**Does it fix the skill?** No. Use skill-review or skill-write.

## It's working if

- Both should-fire and should-not-fire prompts were run.
- A baseline and a retest are recorded.
- Failures are listed with the prompt that caused them.
