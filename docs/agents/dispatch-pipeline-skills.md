# Dispatching pipeline skills to a worker

The pipeline skills (`to-spec`, `to-tickets`, `implement-spec`, `retro`, and helpers such as `tdd`, `code-review`) keep `disable-model-invocation` on. A dispatched worker therefore cannot start them with the Skill tool, and a worker has no one to ask mid-run.

## Decision (issue #31, from retro #30)

Option A: keep `disable-model-invocation` on. The dispatching bot writes the owner's durable authorization into the worker task. With it, the worker reads the skill files and follows them by hand. No skill frontmatter changes, and no per-skill owner round trip.

Why: the flag stays a guard against a model starting a skill by itself. The authorization comes from the owner, is explicit, and is scoped to one task.

## Before dispatching implementers

Push the integration branch to the remote first (`git push -u origin <branch>`). A branch that exists only locally leaves workers with nothing to base on or merge into. After every merge into it, run `sh scripts/ci.sh` (see the merge gate in `CONTRIBUTING.md`).

## Where the skills live

`~/.claude/skills/<name>/SKILL.md`, plus sibling files in the same folder (templates, references). Read the siblings the SKILL.md points to, not only SKILL.md.

## Pre-authorization paragraph (paste into the worker spec)

```text
Owner pre-authorization (durable, covers this whole task): the skills to-spec,
to-tickets, implement-spec, tdd, code-review and retro are set to
disable-model-invocation, so do not call them with the Skill tool. Instead read
~/.claude/skills/<name>/SKILL.md and every sibling file it references, then
follow it manually, step by step, as if it were invoked. Do this for each skill
in the chain without asking the owner per skill. Ask the owner at most once, in
one message, and only if a skill file is truly missing or unreadable; that
message must name every missing skill. Use FAKE data only. Never put real
company data or machine-specific paths in the repo. In your worker_done
report, give red-then-green evidence per ticket: the test name, that it
failed before the change, and that it passes after.
```

Add other skills (for example `diagnosing-bugs`) to the list when the task needs them.

## Dry-run checklist (to-spec through retro, at most one owner question)

1. Spec carries the paragraph above and names the whole chain.
2. Worker reads `to-spec/SKILL.md` and siblings, writes the spec. No question.
3. Reads `to-tickets`, splits into tickets with `gh` (see `issue-tracker.md`). No question.
4. Reads `implement-spec` and `tdd`, builds test-first. No question. The report carries red-then-green evidence per ticket.
5. Reads `code-review`, reviews the branch. No question.
6. Reads `retro`, files follow-ups. No question.
7. If any file is missing, one message to the owner naming all missing skills; otherwise zero questions.
