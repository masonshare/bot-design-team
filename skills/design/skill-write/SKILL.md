---
name: skill-write
description: Writes the description and the SKILL.md body of one skill, choosing its size tier and the split between SKILL.md, references and scripts. Use when the user has decided what the skill does and wants SKILL.md drafted, holds raw notes, a transcript or an SOP to turn into a SKILL.md, wants a description that triggers reliably, or has a bloated skill to restructure. Vietnamese triggers - viết SKILL.md, viết description cho skill, soạn mô tả skill, chuyển quy trình thành các bước skill.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Skill write

Draft one skill folder: description first, then body. Takes the intake summary and a go verdict (see skill-search). Hands out a folder ready for skill-test.

Reply in the user's language. Vietnamese users get Vietnamese output, with the English term in parentheses on first use (full edition: [references/vi.md](references/vi.md)).

A **gate** is a stop where the user approves before work continues. Gate here: before overwriting an existing skill folder.

## Route

| The user wants | Use |
|---|---|
| A description or SKILL.md written or restructured | this skill |
| To find out first if a skill exists or is worth it | skill-search |
| Tests, a baseline against a retest | skill-test |
| An existing skill scored, split or merged | skill-review |
| Validation, version, publishing | skill-package |

When the matching skill is not installed, say so in one line and finish the part you can do here.

## Steps

### 1. Size tier and type

| Tier | Use when | Layout |
|---|---|---|
| simple | one idea, about 200 lines or fewer | `SKILL.md` only |
| expanded | several sub-topics, templates, long examples | `SKILL.md` plus `references/` |
| platform | one domain with many separate areas | `SKILL.md` as a router, one `references/<area>.md` per area, `scripts/` for deterministic work |

Start at the smallest tier that holds the workflow. Name the skill type too, since it decides the test style: technique (how-to), reference (facts to look up), discipline (rules under pressure), pattern (a way of thinking).

One skill covers one job a user would actually type. When the draft holds two jobs with different trigger sentences, write two skills (see skill-review).

Done when: tier, type and the one job are recorded.

### 2. Description first

The description is the only skill text loaded all the time, so it alone triggers the skill. Draft it before the body.

- One line, at most 1024 characters, no double quotes, no `: ` sequence (it breaks plain YAML).
- Open with what the skill does (verb first), then `Use when` plus 3-6 distinct user situations, with the words a user would type, including cases where the user does not name the domain.
- State the outcome and the triggers. Keep the step list in the body: an agent that reads a step summary in the description tends to follow it and skip the body.
- When a neighbouring skill is close, add a short `Not for` clause naming what belongs to the neighbour. Two descriptions must never claim the same sentence.
- End with 4-8 trigger words in the user's language (Vietnamese with diacritics).
- Leave out generic words ("help", "task"): they fire on everything.

Done when: the description reads right to someone who has not seen the body, and skill-test can run against it.

### 3. Workflow draft (when starting from an SOP or notes)

Draft the steps before writing SKILL.md. Each step has Input, Action, Output (checkable) and a Gate: `auto` (low risk, easy to undo), `confirm` (the choice affects later steps), `stop` (hard to reverse: publishing, sending, deleting, spending, installing). Default to auto. Aim for 5-10 steps; more means two skills or a reference file. Add one edge case and one worked example. Full template: [references/workflow-template.md](references/workflow-template.md).

Done when: every step has an Input, an Action naming a concrete tool or method, and a checkable Output.

### 4. Body

1. **Steps first.** Numbered, each ending on a checkable "Done when" line. Reference material (tables, rules) follows the steps.
2. **Add what the agent lacks.** For each line ask: would the agent get this wrong without it? If not, cut it. Put gotchas and unwritten conventions in SKILL.md.
3. **One default**, with a short escape hatch, in place of a menu of options.
4. **Positive instructions.** State the target behaviour. Keep a prohibition only as a hard guardrail, paired with the action to take instead. Give the reason for fragile steps.
5. **Self-sufficient SKILL.md.** Some platforms import only SKILL.md, without `references/` or `scripts/`. Every step a run needs lives in SKILL.md; `references/` holds optional depth, each file named with the condition for reading it, and SKILL.md keeps a short summary that works when the file is missing.
6. **One level deep.** SKILL.md links to files; those files link onward to nothing. Use relative paths from the skill root.
7. **Scripts only for deterministic work** (validation, parsing, conversion). Standard library, no prompts, `--help`, clear errors, non-zero exit on failure. The skill states a by-hand way when the script is missing.
8. **Credentials never live in a skill folder.** API keys, tokens, webhook URLs, passwords and auth notes belong in the platform's secret or connection store. The skill names the connection ("use the stored connection called X") and stores nothing else.
9. **Route and handoff lines.** When the skill has siblings, add a short route table that says what to do when a sibling is missing. End with the 5-field handoff (below).
10. Plain Markdown. Aim for under 300 lines in SKILL.md; stay under 500.

Done when: every step has a completion criterion, every link resolves, and a reader could run the skill from SKILL.md alone.

### 5. Self-check, then hand on

Check by hand: `name` is lowercase with single hyphens and equals the folder name; the description is one line, non-empty, at most 1024 characters; SKILL.md is under 500 lines; links resolve; no absolute local paths. Then hand on to skill-test, and to skill-package for the full validator.

Done when: the folder exists, the self-check passes and the handoff is sent.

## Handoff

When passing work to another bot or the user, send 5 fields in order: Goal (one sentence), Inputs (attached or linked), Deliverable (file names or inline), Done when (checkable criteria), Open items (questions, risks, anything not done).

## Reference files

- [references/workflow-template.md](references/workflow-template.md): the full workflow template and quality checklist. Read when step 3 starts from raw notes.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user works in Vietnamese.

## Sources

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Agent Skills specification: https://agentskills.io/specification
- Adapted from Masonshare's distill-to-skill templates.
