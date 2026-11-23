# prompt-review

## What it does

Diagnoses a prompt you already have against four errors (vague, greedy, unbounded, trapping) and a six-element checklist, quotes the line behind each finding and returns a marked rewrite.

Source: [`skills/design/prompt-review/SKILL.md`](../../skills/design/prompt-review/SKILL.md)

## When to reach for it

You paste a prompt that is vague, too long, ignored or gives inconsistent output.

## Common questions

**Does it rewrite everything?** It returns a marked rewrite with each change tied to a finding.

**Can it write from scratch?** No. Use prompt-design.

**Does it test the result?** Use prompt-test for that.

## It's working if

- Every finding quotes the offending line.
- The rewrite is marked so you see what changed.
- The rewritten prompt fixes the failure you reported.
