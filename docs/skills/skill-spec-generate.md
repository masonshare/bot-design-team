# skill-spec-generate

## What it does

Writes a design-notes file for a finished skill: why it exists, architecture decisions, threshold values, trade-offs, when to revisit, related skills and sources. The notes are kept outside the skill folder, so they never load when the skill runs and cost no context. It uses a bundled template.

A SKILL.md is for the AI and the reason behind it is for people; mixing them wastes context. The two judgement sections (trade-offs, when to revisit) are always asked of the person, never guessed. A sources section feeds `docs/credits.md`. Reference point: keep the notes to about 150 lines. Every number in this skill is a labelled reference point, not a fact about your market; the skill asks for your own figures. In this repo, the content of such notes goes into the skill's page under `docs/skills/` instead of a separate file.

Source: [`packs/starter/mango-spring-roll/skills/skill-spec-generate/SKILL.md`](../../packs/starter/mango-spring-roll/skills/skill-spec-generate/SKILL.md)

## When to reach for it

Right after finishing a skill, or when asked to record the design reasons of a skill, write design notes for skill X, or backfill notes for an older skill. It is separate from reviewing a project instruction file (CLAUDE.md or AGENTS.md), which is another layer.

## Common questions

**Where does the file go?** Outside the skill folder, so it is never loaded at runtime.

**Does it guess the trade-offs?** No. It asks the person for trade-offs and when to revisit.

**Will it overwrite an existing note?** No. It never overwrites a file without asking.

## It's working if

- The notes file sits outside the skill folder.
- Trade-offs and when to revisit came from the person, not from a guess.
- No private details (machine paths, customer names, access keys) are in the notes.
