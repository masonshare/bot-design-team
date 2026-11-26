# Workflow template

Read this when step 3 of skill-write starts from raw notes, a transcript or an SOP. Adapted from Masonshare's distill-to-skill templates.

Draft the workflow before writing SKILL.md. Each step has Input, Action, Output, and the Output is checkable.

```markdown
---
title: "<Workflow name>"
topic: "<topic>"
target_user: "<who runs it>"
date: YYYY-MM-DD
---

# <Workflow name>

## Summary
<1-2 sentences: what it does, for whom, what problem it removes>

## Use when
<the situation the user is in>

## Steps

### Step 1. <short name>
- **Input:** <data, files or conditions needed>
- **Action:** <the concrete tool or method>
- **Output:** <a result you can check>
- **Gate:** auto | confirm | stop

### Step N. <short name>
- **Input / Action / Output / Gate:** ...

## Done when
- [ ] <criterion 1>
- [ ] <criterion 2>

## Edge cases
- When <situation>: <action>

## Worked example
**Sample input:** ...
**Sample output:** ...
```

Quality checklist before moving to SKILL.md:

- [ ] 5-10 steps (fewer is too thin, more should be split into two skills or a reference)
- [ ] Every step has Input, Action and Output
- [ ] Every Action names a concrete tool or method
- [ ] Every Output can be checked as right or wrong
- [ ] A Done when list exists
- [ ] At least one edge case and one worked example
- [ ] A clarify step sits right after the first user message when the request is usually vague (ask in one batch, at most 2 rounds, then proceed on stated assumptions)

Gate types, choosing per step:

| Gate | Use when | Behaviour |
|---|---|---|
| auto | low risk, easy to undo | run without asking |
| confirm | the choice affects later steps | show a one-line summary, ask to proceed |
| stop | hard to reverse (publishing, sending, deleting, spending, installing, giving write access, enabling a schedule) | halt until the user approves |

Default to auto and raise a step only when the cost of a wrong guess justifies the interruption.
