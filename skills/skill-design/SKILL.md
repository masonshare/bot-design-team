---
name: skill-design
description: Turns a workflow, SOP or body of knowledge into a valid Agent Skills skill folder, then tests and publishes it. Use when the user wants to create, package, distill, test, validate, improve or publish a skill, asks whether something deserves to be a skill, or wants a skill description that triggers reliably. Covers existing-skill search first, go/no-go, size tier, description, body, trigger tests, baseline vs retest, spec validation, npx skills add layout and changelog. Vietnamese triggers - tạo skill, đóng gói quy trình thành skill, viết SKILL.md, kiểm thử skill, xuất bản skill, sửa skill.
license: MIT
metadata:
  author: Masonshare
  version: "1.0.0"
  language: en (Vietnamese edition in references/vi.md)
---

# Skill design

Turn a workflow, SOP or body of knowledge into a skill that an agent loads on the right prompt and follows the same way every run. Work loop: clarify, research, plan, build, verify. Reply in the user's language; Vietnamese users get Vietnamese output (full edition in [references/vi.md](references/vi.md)).

A **gate** is a stop where the user approves before work continues. Gates in this skill: before installing anything found online, before overwriting an existing skill, before publishing.

## Step 1. Intake (clarify)

Ask every missing field in one batch. Fill defaults for the rest and state them.

| Field | Question | Default |
|---|---|---|
| topic | What workflow, SOP or knowledge becomes the skill? | required |
| target user | Who runs it, and in which agent? | required |
| inputs available | Documents, transcripts, examples, a past run? | none |
| detail level | high, medium or low | medium |
| language | Language of the skill body | English, plus a Vietnamese edition for Vietnamese users |
| execution mode | `coach` (asks at each step), `auto` (runs end to end, stops at gates) or `hybrid` | hybrid |
| deployment target | Global install, project folder, or a public repo | project folder |
| definition of done | What a correct run looks like | one sample task |

Done when: every field has an answer or a stated default, and the user confirmed the summary.

## Step 2. Search for an existing skill

1. Run `npx skills find <need in 2-4 words>` and search https://skills.sh with the same words. Try a second query on the problem domain.
2. Open each candidate's SKILL.md and read what it contains. Judge it on four points: it covers the user's task, it works in the user's agent, it asks before acting externally, and it makes no hidden network calls.
3. Present a short table: skill, source, what it covers, what it lacks. Ask the user: use it as is, customize it, or build new. Show the exact install command and install only after the user says yes (gate).
4. When customizing, treat the found skill as a reference and build from the user's workflow.

Done when: the user chose use, customize or build new, with the candidates listed (or "none found").

## Step 3. Go/no-go

A skill earns its place when all four answers are yes:

1. The task repeats, or will repeat, with the same shape.
2. The agent is inconsistent or wrong without written guidance (run one baseline prompt to see).
3. The steps can be written down and success can be checked.
4. The knowledge stays valid for longer than a week.

A one-off task, a plain fact lookup, or a rule that fits in one line of the user's AGENTS.md or CLAUDE.md is not a skill: say so and name the better home.

Done when: a verdict (go or no-go) with one reason per answer.

## Step 4. Choose the size tier

| Tier | Use when | Layout |
|---|---|---|
| simple | one idea, about 200 lines or fewer | `SKILL.md` only |
| expanded | several sub-topics, templates, long examples | `SKILL.md` plus `references/` |
| platform | one product or domain with many separate areas | `SKILL.md` as a router, one `references/<area>.md` per area, `scripts/` for deterministic work |

Start at the smallest tier that holds the workflow. Also name the skill type, which decides the test style: technique (how-to), reference (facts to look up), discipline (rules to follow under pressure), pattern (a way of thinking).

Done when: tier and type are recorded.

## Step 5. Write the description first

The description is the only skill text loaded all the time, so it alone triggers the skill. Draft it before the body.

- One line, at most 1024 characters, no double quotes, no `: ` sequence (it breaks plain YAML).
- Open with what the skill does (verb first), then `Use when` plus 3-6 distinct user situations, with the keywords a user would type, including cases where the user does not name the domain.
- State the outcome and the triggers. Keep the step list in the body: an agent that reads a step summary in the description tends to follow it and skip the body.
- End with 4-8 trigger words in the user's language (Vietnamese with diacritics).
- Leave out generic words ("help", "task"): they fire on everything.

Done when: the description passes Step 8 and reads right to someone who has not seen the body.

## Step 6. Write the body

1. **Steps first.** Numbered, each ending on a checkable "Done when" line. Reference material (tables, rules, definitions) follows the steps.
2. **Add what the agent lacks.** For each line ask: would the agent get this wrong without it? If not, cut it. Put gotchas and unwritten conventions in SKILL.md.
3. **One default**, with a short escape hatch, in place of a menu of options.
4. **Positive instructions.** State the target behaviour. Keep a prohibition only as a hard guardrail, paired with the action to take instead. Give the reason for fragile steps.
5. **Self-sufficient SKILL.md.** Some platforms import only SKILL.md, without `references/` or `scripts/`. Every step a run needs lives in SKILL.md; `references/` holds optional depth, each file named with the condition for reading it.
6. **One level deep.** SKILL.md links to files; those files link onward to nothing. Use relative paths from the skill root.
7. **Scripts only for deterministic work** (validation, parsing, conversion). Standard library, no prompts, `--help`, clear errors, non-zero exit on failure. The skill still works when the platform skips scripts.
8. **Credentials never live in a skill folder.** API keys, tokens, webhook URLs, passwords and auth notes belong in the platform's secret or connection store. The skill names the connection ("use the stored connection called X") and stores nothing else.
9. Plain Markdown. Aim for under 300 lines in SKILL.md; stay under 500.

Done when: every step has a completion criterion, every link resolves, and a reader could run the skill from SKILL.md alone.

## Step 7. Test

Write tests before calling the skill done. Subagent setup: [references/testing.md](references/testing.md). File formats: [references/templates.md](references/templates.md).

1. **Trigger tests.** 8-10 prompts that should fire the skill and 8-10 that should not. Make the negatives near-misses that share keywords. Vary wording, formality, length, and whether the domain is named.
2. **Task test cases.** 3-5 realistic prompts with expected behaviour, plus one vague prompt and one edge case. Save as `evals/evals.json`.
3. **Baseline.** Run each case in a fresh context without the skill. Record what went wrong, in the agent's exact words.
4. **Retest.** Run the same cases with the skill. Compare against the baseline and the expected behaviour.
5. **Fix and rerun.** Close each failure at its cause (usually a missing instruction or a weak description). Rerun the failed cases plus a sample of the passed ones. Revise from the failing cases' cause, and keep a failed prompt's own words out of the description.
6. **Pass bar.** At least 80% of should-fire prompts fire, at most 10% of should-not-fire prompts fire, and every task case meets its expected behaviour.

Done when: baseline and retest results sit side by side and the bar is met, or the remaining failures are listed as open items.

## Step 8. Validate against the spec

Run `python scripts/validate_skill.py <skill-folder>` when scripts are available; otherwise check by hand against these rules (Agent Skills specification):

- `SKILL.md` exists with YAML frontmatter.
- `name`: required, 1-64 characters, lowercase `a-z` and `0-9` and hyphens, no leading, trailing or double hyphen, equal to the folder name.
- `description`: required, non-empty, at most 1024 characters, one line.
- Optional fields: `license` (short name), `compatibility` (at most 500 characters, only for real environment needs), `metadata` (string-to-string map for author, version, language), `allowed-tools` (experimental, space-separated).
- Spec-strict validators reject other top-level keys, so custom keys go under `metadata`.
- SKILL.md under 500 lines; body under roughly 5000 tokens.
- Every relative link resolves; no absolute local paths (drive letters, user home folders).
- `scripts/`, `references/`, `assets/` are conventions; `evals/` holds tests.

Done when: all checks pass.

## Step 9. Package and publish

1. Layout in the repo: `skills/<name>/SKILL.md`, plus `references/`, `scripts/`, `evals/`. The installer finds `skills/<name>/SKILL.md` on its own. Preview with `npx skills add <owner>/<repo> --list`.
2. Scrub the folder of credentials, personal paths, private names and copied third-party text. List each source under a Sources heading at the bottom of the file that uses it.
3. Pick the version and write the changelog entry from [references/templates.md](references/templates.md). PATCH: wording or typo fixes with no behaviour change. MINOR: added sections, scripts or references; old use keeps working. MAJOR: renamed steps, changed output format, removed fields. Between two levels, take the higher.
4. Gate: show the user the file list, the version and the install command. Publish after approval.
5. Users install with `npx skills add <owner>/<repo>` (`--skill <name>` for one skill, `-g` for global).

Done when: the user approved, the changelog entry exists, and the `--list` preview shows the skill.

## Updating an existing skill

1. Read the current SKILL.md and its tests. Ask for a real failure: the prompt and what the agent did.
2. Reproduce the failure as a trigger or task test and run it without the fix to confirm it fails.
3. Edit the smallest part that explains the failure: the description for trigger misses, the step or its completion criterion for wrong behaviour.
4. Rerun the full test set and the validator; confirm no earlier case regressed.
5. Bump the version, add a changelog entry (driver, changes, migration, rollback), and pass Step 9's gate.

Done when: the failing case passes, no old case regressed, and the changelog states the driver.

## The 4 packaging criteria

A skill ships when it is:

1. **Minimal**: one coherent job; every line changes behaviour.
2. **Accurate**: steps match how the work really goes, checked against a real run.
3. **Modular**: depth in `references/`, deterministic work in `scripts/`, one source of truth per fact.
4. **Clear input and output**: it states what it takes in and what it hands out, so another skill or bot can chain it.

## Handoff

When passing work to another bot or the user, send 5 fields in order: Goal (one sentence), Inputs (attached or linked), Deliverable (file names or inline), Done when (checkable criteria), Open items (questions, risks, anything not done).

## Read these when needed

- [references/templates.md](references/templates.md): when writing the workflow draft, a changelog entry or `evals/evals.json`.
- [references/testing.md](references/testing.md): when running baseline and retest with subagents, or when a skill keeps failing.
- [references/vi.md](references/vi.md): when the user works in Vietnamese.
- `scripts/validate_skill.py`: the Step 8 checker.

## Sources

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Agent Skills specification: https://agentskills.io/specification
- obra/superpowers, "writing-skills" (test-first idea for skills): https://github.com/obra/superpowers
- vercel-labs/skills (`npx skills`, find-skills): https://github.com/vercel-labs/skills
- Skills directory: https://skills.sh
