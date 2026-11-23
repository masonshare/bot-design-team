---
name: skill-review
description: Reviews a skill that already exists. Scores it against four packaging criteria, finds overlap with other skills, decides whether to split a big skill or merge small ones, and plans a fix from a real failure. Use when the user points to a SKILL.md and asks what is wrong with it, whether it is too long or does two jobs, how to split or merge skills, or reports that a skill misbehaved. Vietnamese triggers - rà soát skill, chấm skill, skill quá dài, chia skill, gộp skill, sửa skill bị lỗi.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Skill review

Judge an existing skill, or a family of skills, and say what to change. Takes a SKILL.md or folder (and its neighbours when overlap matters). Hands out a scored review and an ordered fix list.

Reply in the user's language. Vietnamese users get Vietnamese output, with the English term in parentheses on first use (full edition: [references/vi.md](references/vi.md)).

A **gate** is a stop where the user approves before work continues. Gate here: before overwriting or deleting an existing skill.

## Route

| The user wants | Use |
|---|---|
| An existing skill scored, split, merged or fixed from a failure | this skill |
| The rewrite itself, once the verdict is known | skill-write |
| Tests that prove the fix | skill-test |
| Validation, version, publishing | skill-package |
| A brand-new skill | skill-design |

When the matching skill is not installed, say so in one line and finish the part you can do here.

## Steps

### 1. Read

Read the SKILL.md, its references and any tests. List the descriptions of installed neighbouring skills. For a failure report, ask for the prompt and what the agent did.

Done when: the skill, its neighbours and (if any) the failing prompt are in front of you.

### 2. Score

A skill ships when it is:

1. **Minimal**: one coherent job; every line changes behaviour.
2. **Accurate**: steps match how the work really goes, checked against a real run.
3. **Modular**: depth in `references/`, deterministic work in `scripts/`, one source of truth per fact.
4. **Clear input and output**: it states what it takes in and hands out, so another skill or bot can chain it.

Add three checks: the description names one job a user would type; SKILL.md runs without its references; no credential or personal path sits in the folder. Mark each pass or fail with a quoted line as evidence.

Done when: every criterion has a mark and a quote.

### 3. Overlap

For each neighbour, take three sentences a user would type for this skill and three for the neighbour. If a description could plausibly claim a sentence of the other, they overlap. Fix by narrowing the description to the job, adding a `Not for` clause, or merging.

Done when: each pair is marked clear or overlapping, with the sentence that shows it.

### 4. Split or merge

Split when: SKILL.md passes about 300 lines, two jobs have different trigger sentences, or one part is used far less than the rest and bloats every run. Merge when: two skills always load together, or their descriptions cannot be told apart.

Weigh the cost: descriptions are always in context, so each extra skill adds its description length every turn, while a smaller body saves tokens on each run. Split only when the saved body per run is larger than the added description, over the runs you expect. Keep a short router skill so the family still has one front door. Keep small repeated lines (language rule, gate, 5-field handoff) in every skill, because each SKILL.md must run alone; list them so an edit reaches every copy. Detail and a cost formula: [references/split-merge.md](references/split-merge.md).

Done when: a verdict (keep, split, merge or rewrite) with the numbers behind it.

### 5. Fix from a real failure

1. Reproduce the failure as a trigger or task test and run it without the fix to confirm it fails.
2. Edit the smallest part that explains it: the description for a trigger miss, the step or its completion criterion for wrong behaviour.
3. Rerun the full test set and the validator; confirm no earlier case regressed (use skill-test and skill-package).
4. Bump the version and add a changelog entry that names the driver.

Done when: the failing case passes, no old case regressed, and the changelog states the driver.

### 6. Report

Send the score table, the overlap marks, the verdict and the fix list in priority order, using the handoff below.

## Handoff

When passing work to another bot or the user, send 5 fields in order: Goal (one sentence), Inputs (attached or linked), Deliverable (file names or inline), Done when (checkable criteria), Open items (questions, risks, anything not done).

## Reference files

- [references/split-merge.md](references/split-merge.md): cost formula, split and merge examples, how to keep repeated lines in step. Read when step 4 decides a split or merge.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user works in Vietnamese.

## Sources

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Anthropic, "Agent Skills overview" (loading levels): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
