# prompt-test

## What it does

Proves a prompt, chain or soul with 5 to 10 test cases, a baseline run, a retest, a score sheet and a v2 changelog.

Source: [`packs/starter/pink-pepper-coated-lotus-seeds/skills/prompt-test/SKILL.md`](../../packs/starter/pink-pepper-coated-lotus-seeds/skills/prompt-test/SKILL.md)

## When to reach for it

You want test cases, an old and new version compared, or outputs scored.

## Common questions

**How many cases?** 5 to 10, including at least one that should fail.

**What is a baseline?** The run before the change, for comparison.

**Is a changelog required?** Yes for v2, so the change is traceable.

## It's working if

- A baseline and a retest exist for the same cases.
- The score sheet shows the difference.
- The v2 changelog names what changed and why.
