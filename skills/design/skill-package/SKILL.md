---
name: skill-package
description: Validates a skill folder against the Agent Skills spec and packages it for sharing, with a version bump, a changelog entry and the right layout for npx skills add, GitHub or a zip upload. Use when the user wants a skill checked before shipping, asks how to publish or share a skill, how to pick the version number, or where a skill goes on Claude Code, Claude.ai, the API or Orca. Vietnamese triggers - kiểm tra skill theo chuẩn, đóng gói skill, xuất bản skill, ghi changelog, npx skills add.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Skill package

Make a finished skill valid and shippable. Takes a skill folder that passed skill-test. Hands out a passing folder, a version, a changelog entry and an install command, after the user approves.

Reply in the user's language. Vietnamese users get Vietnamese output, with the English term in parentheses on first use (full edition: [references/vi.md](references/vi.md)).

A **gate** is a stop where the user approves before work continues. Gates here: before overwriting an existing skill, before publishing.

## Route

| The user wants | Use |
|---|---|
| A skill validated, versioned, published or shared | this skill |
| The description or body fixed | skill-write |
| Tests run | skill-test |
| A skill judged, split or merged | skill-review |
| The whole build | skill-design |

When the matching skill is not installed, say so in one line and finish the part you can do here.

## Steps

### 1. Validate

Run `python scripts/validate_skill.py <skill-folder>` (path from this skill's root; the script needs only the Python standard library and exits 1 on failure). When the script is missing, check by hand against these rules (Agent Skills specification):

- `SKILL.md` exists with YAML frontmatter.
- `name`: required, 1-64 characters, lowercase `a-z`, `0-9` and hyphens, no leading, trailing or double hyphen, equal to the folder name.
- `description`: required, non-empty, at most 1024 characters, one line, no double quotes and no `: `.
- Optional fields: `license`, `compatibility` (at most 500 characters), `metadata` (string-to-string map for author, version, language), `allowed-tools` (experimental). Spec-strict validators reject other top-level keys, so custom keys go under `metadata`.
- SKILL.md under 500 lines; body under roughly 5000 tokens.
- Every relative link resolves; no absolute local paths (drive letters, user home folders).

Fix each failure at its cause and rerun until clean.

Done when: every check passes, and the output is saved for the user.

### 2. Scrub

Remove credentials, personal paths, private names and copied third-party text from the folder. Keys, tokens and webhook URLs belong in the platform's secret or connection store, never in a skill folder. List each source under a Sources heading at the bottom of the file that uses it.

Done when: a search of the folder for keys, tokens, URLs with secrets and home paths finds nothing.

### 3. Layout and where it runs

Repo layout: `skills/<name>/SKILL.md`, plus `references/`, `scripts/`, `evals/`. The installer finds `skills/<name>/SKILL.md` on its own, also inside a bucket folder such as `skills/design/<name>/SKILL.md`. Preview with `npx skills add <owner>/<repo> --list`.

| Platform | How the skill gets in |
|---|---|
| Claude Code | Folder `~/.claude/skills/<name>/SKILL.md` (personal), `.claude/skills/<name>/SKILL.md` (project) or a plugin. No upload. |
| Claude.ai | Zip upload in settings. Custom skills need Pro, Max, Ultra, Team or Enterprise with code execution on. |
| Claude API | Upload through `/v1/skills`, then list `skill_ids` in the `container` parameter with the code execution tool. Workspace-wide; the container has no network. |
| Agent SDK | Files on disk under `.claude/skills/`, found through `settingSources` and the `skills` option. |

Custom skills do not sync across Claude surfaces: upload or copy to each one. Checked against the official docs on 2026-11-18.

What an import carries (unverified, from the owner's experience): a share may bring only SKILL.md; an install from GitHub brings `references/` and `scripts/` too. Treat both as unproven until one import is checked. Because of the first case, every SKILL.md must run alone; tell the user which files will be lost if only SKILL.md travels.

Done when: the layout is listed and the target platform's route is stated with its limits.

### 4. Version and changelog

PATCH: wording or typo fixes with no behaviour change. MINOR: added sections, scripts or references; old use keeps working. MAJOR: renamed steps, changed output format, removed fields, or a split of one skill into several. Between two levels, take the higher. Write one entry per bump:

```markdown
## v<X.Y.Z> - <YYYY-MM-DD>

**Bump:** PATCH | MINOR | MAJOR
**Backward compatible:** yes | no
**Driver:** <one line: the failure or request that caused the change>

### Changes
- Added / Changed / Removed / Fixed: <what>

### Migration
<"none" for PATCH and MINOR; for MAJOR, exact instructions>

### Rollback
<the tag or commit to return to>
```

Keep the history in `CHANGELOG.md` at the repo root or in release notes. SKILL.md carries only the current `metadata.version`. The long template: [references/changelog-template.md](references/changelog-template.md).

Done when: the version is set in `metadata.version` and the entry exists.

### 5. Gate and publish

Show the user the file list, the version, the validator output and the install command. Publish only after approval; installing for the user is a separate yes. Users install with `npx skills add <owner>/<repo>` (`--skill <name>` for one skill, `-g` for global).

Done when: the user approved, and the `--list` preview shows the skill.

## Handoff

When passing work to another bot or the user, send 5 fields in order: Goal (one sentence), Inputs (attached or linked), Deliverable (file names or inline), Done when (checkable criteria), Open items (questions, risks, anything not done).

## Reference files

- [references/changelog-template.md](references/changelog-template.md): full changelog template with a worked entry. Read when writing a MAJOR entry.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user works in Vietnamese.
- `scripts/validate_skill.py`: the step 1 checker. By-hand rules above replace it when it is missing.

## Sources

- Agent Skills specification: https://agentskills.io/specification
- Anthropic, "Agent Skills overview" (platforms, sharing scope): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Claude Code, "Extend Claude with skills": https://code.claude.com/docs/en/skills
- Claude Agent SDK, "Extend agents with skills": https://code.claude.com/docs/en/agent-sdk/skills
- vercel-labs/skills (`npx skills`): https://github.com/vercel-labs/skills
