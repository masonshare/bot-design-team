# Templates

Read this when drafting the workflow behind a skill, writing a changelog entry, or creating `evals/evals.json`. Adapted from Masonshare's distill-to-skill templates.

## 1. Workflow template

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
- **Gate:** auto | confirm | stop (see below)

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

## 2. Changelog entry template

One entry per version bump. A reader should see what changed, why, and how to go back.

```markdown
## v<X.Y.Z> - <YYYY-MM-DD>

**Bump:** PATCH | MINOR | MAJOR
**Backward compatible:** yes | no
**Driver:** <one line: the failure or request that caused the change>

### Changes
- Added: <new section, field or file>
- Changed: <what was altered>
- Removed: <what was deleted; MAJOR only>
- Fixed: <bug or typo>

### Migration
<"none" for PATCH and MINOR; for MAJOR, exact instructions, such as "field X is now Y">

### Rollback
<the git tag or commit to return to, for example: git checkout v<previous> -- skills/<name>>
```

Bump rules: PATCH for wording, typos and description tightening with no behaviour change. MINOR for new sections, scripts or references where old use still works. MAJOR for renamed steps, changed output format, changed defaults or removed fields. Torn between two levels: take the higher.

Keep the history in a `CHANGELOG.md` at the repo root or in the release notes. SKILL.md carries only the current `metadata.version`.

## 3. evals.json format

Store task test cases at `evals/evals.json` inside the skill folder. Start with 3-5 cases.

```json
{
  "skill_name": "<name>",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic message, worded the way a user would type it.",
      "expected_output": "The behaviour or result a correct run shows.",
      "files": [],
      "assertions": [
        "A checkable statement, such as: asks which output format before drafting",
        "Another checkable statement, such as: ends with a Done when check"
      ]
    }
  ]
}
```

Rules for good cases:

- Prompts read like real messages: some precise, some vague, one with an edge case.
- Each assertion can be graded PASS or FAIL from the transcript or output, with a quoted line as evidence.
- Assertions describe behaviour. They name no internal step numbers a user would never see.

Trigger tests go in a second file, `evals/triggers.json`:

```json
[
  { "query": "turn our onboarding checklist into a reusable skill", "should_trigger": true },
  { "query": "summarize this meeting transcript", "should_trigger": false }
]
```

Aim for 8-10 `true` and 8-10 `false` entries. Write the `false` entries as near-misses that share words with the skill's domain.
