# skill-review

## What it does

Reviews an existing skill: scores it on four packaging criteria, finds overlap with other skills, decides on a split or merge, and plans a fix from a real failure.

Source: [`skills/design/skill-review/SKILL.md`](../../skills/design/skill-review/SKILL.md)

## When to reach for it

You point at a SKILL.md and ask what is wrong, whether it is too long or does two jobs.

## Common questions

**When to split?** When a skill does two jobs; see references/split-merge.md.

**Does it edit the skill?** It plans the fix; you apply it with skill-write.

**What if it misbehaved?** Give the real failure; the plan starts there.

## It's working if

- Each score cites a line of the skill.
- Overlap with named sibling skills is checked.
- The fix plan addresses the failure you reported.
