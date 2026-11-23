---
name: skill-design
description: Runs the whole job of building an Agent Skill from a first idea to a published folder, by taking the intake and handing each stage to the matching skill-* sibling. Use when the user wants to create a new skill, turn a workflow, SOP or body of knowledge into a skill, or does not know which skill step comes next. Not for only searching existing skills, only writing the description or SKILL.md, only testing, reviewing or splitting a skill, or only validating and packaging one. Vietnamese triggers - tạo skill mới, biến quy trình thành skill, đóng gói kiến thức thành skill, làm skill từ SOP.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Skill design (router)

Turn a workflow, SOP or body of knowledge into a skill an agent loads on the right prompt and follows the same way every run. This skill takes the intake, routes each stage to a sibling skill and keeps the order. Work loop: clarify, research, plan, build, verify.

Reply in the user's language. Vietnamese users get Vietnamese output, with the English term in parentheses on first use (full edition: [references/vi.md](references/vi.md)).

A **gate** is a stop where the user approves before work continues. Gates in this family: before installing anything found online, before overwriting an existing skill, before publishing.

## What a skill is

An **Agent Skill** is a folder with a `SKILL.md` (YAML frontmatter with `name` and `description`, then Markdown steps) and optional `scripts/`, `references/`, `assets/`. Agents load it in levels: the `description` is always in context, the `SKILL.md` body loads when a prompt matches, other files load only when read or run.

| Thing | Loads | Use it for |
|---|---|---|
| Prompt | That turn only | A one-off task |
| Soul (a bot's standing instructions) | Every turn, ranks above skills | Who the bot is and what it never does |
| AGENTS.md / CLAUDE.md | Every session | Short project facts and rules |
| Skill | Description always, body on a match | A repeating workflow done the same way each run |

## Route first

| The user wants | Use |
|---|---|
| A whole new skill, or is unsure where to start | this skill |
| To know if a skill already exists, or if the idea deserves one | skill-search |
| The description or SKILL.md written or restructured | skill-write |
| Trigger tests, a baseline against a retest, a skill that never fires | skill-test |
| An existing skill judged, split, merged or fixed from a failure | skill-review |
| A skill validated, versioned, published or shared | skill-package |

When a sibling is not installed, say so in one line and do its part with the fallback in step 3. Never stop the whole job for a missing sibling.

## Steps

### 1. Intake (clarify)

Ask every missing field in one batch. Fill defaults for the rest and state them.

| Field | Question | Default |
|---|---|---|
| topic | What workflow, SOP or knowledge becomes the skill? | required |
| target user | Who runs it, and in which agent? | required |
| inputs available | Documents, transcripts, examples, a past run? | none |
| detail level | high, medium or low | medium |
| language | Language of the skill body | English, plus a Vietnamese edition for Vietnamese users |
| execution mode | `coach` (asks at each step), `auto` (end to end, stops at gates) or `hybrid` | hybrid |
| deployment target | Global install, project folder or a public repo | project folder |
| definition of done | What a correct run looks like | one sample task |

Done when: every field has an answer or a stated default, and the user confirmed the summary.

### 2. Run the stages in order

| Stage | Skill | Output that feeds the next stage |
|---|---|---|
| Search and go/no-go | skill-search | verdict (use, customize, build new, or no-go) with candidates |
| Description and body | skill-write | one skill folder |
| Trigger and task tests | skill-test | test table, baseline against retest |
| Review (optional, for a big or crowded skill) | skill-review | score and split or merge verdict |
| Validate and package | skill-package | passing folder, version, changelog, user approval |

After each stage, show the user one line of result and continue. Stop at a gate. In `coach` mode, ask before every stage.

Done when: the user holds a skill folder that passed skill-test and skill-package, or knows which stage is still open.

### 3. Fallback when a sibling is missing

Do the smallest honest version, mark it "minimal, sibling not installed":

- skill-search: run `npx skills find <need in 2-4 words>`, read the top candidates, ask use, customize or build new. Go only if the task repeats, the agent errs without guidance, the steps can be written and checked, and the knowledge lasts over a week.
- skill-write: write the description first (one line, at most 1024 characters, no double quotes, no `: `, verb first, `Use when` plus 3-6 user situations, 4-8 trigger words in the user's language). Then numbered steps, each ending in a checkable "Done when". SKILL.md must run alone, without references or scripts.
- skill-test: write 3 prompts that should fire and 2 that should not, run each without and with the skill in a fresh context, and record the result in a table.
- skill-review: check the skill is one job, every line changes behaviour, and it runs from SKILL.md alone.
- skill-package: check `name` equals the folder name and is lowercase with single hyphens, the description is non-empty and at most 1024 characters, SKILL.md is under 500 lines, every relative link resolves, no absolute local paths. Ask before publishing.

## Handoff

When passing work to another bot or the user, send 5 fields in order: Goal (one sentence), Inputs (attached or linked), Deliverable (file names or inline), Done when (checkable criteria), Open items (questions, risks, anything not done).

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user works in Vietnamese.

## Sources

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Agent Skills specification: https://agentskills.io/specification
- Skills directory: https://skills.sh
