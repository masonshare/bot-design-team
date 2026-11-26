# Testing a skill with subagents

Read this when running the tests from skill-test, or when a skill keeps failing. The idea, test first and watch it fail before writing the fix, comes from the "writing-skills" skill in obra/superpowers (https://github.com/obra/superpowers). The procedure is written fresh.

## The idea

A skill is code for an agent, so test it like code. Run the task without the skill, record what goes wrong, write the skill to fix exactly those failures, then run again. A skill never seen failing may fix nothing.

## Setup

Use a fresh subagent or a fresh process per run, so the result reflects the skill and the prompt only.

- Without-skill run: the prompt and nothing else.
- With-skill run: the same prompt, plus the skill folder installed where the agent loads skills, or the SKILL.md text pasted in front when the platform imports only SKILL.md.
- When the platform cannot spawn subagents, open a new chat per run and paste results into a table.

## Reading which skill fired (Claude Code CLI)

Run `claude -p "<prompt>" --output-format stream-json --verbose --max-turns 2`, with the skill under test and its siblings placed in `.claude/skills/` of an empty project folder, and with file-writing and shell tools disallowed so the run stays short. Each loaded skill appears as a `tool_use` event named `Skill`; its `input.skill` is the skill name. No such event means no skill fired.

Limits to state in the report:

- This is the Claude Code picker. Another platform mounts skills by its own rules, so a pass here is indicative, not proof.
- User-level skills on the machine also load, which is useful: they are the real rivals.
- A short run shows the first decision only, not whether the skill was then followed.

## Baseline

1. Take the task cases from `evals/evals.json`.
2. Run each case without the skill.
3. Record the output and, for each failure, the exact wording and the shortcut taken.
4. Group failures: wrong format, skipped step, invented fact, ignored constraint, wrong tool, never started the skill.

## Write to the failures

Each failure becomes one instruction, placed where it applies, with its reason. Generic advice ("be careful") adds length and changes nothing.

## Retest

1. Run the same cases with the skill, each in a fresh context.
2. Grade every assertion PASS or FAIL with a quoted line as evidence.
3. Compare three columns per case: baseline, with skill, expected.
4. After each fix, rerun the failed cases and a few passed ones to catch regressions.

## Trigger testing details

- Include prompts that never name the skill's domain, and near-misses for the negatives.
- Run each prompt at least 3 times with the skill installed alongside unrelated skills. A prompt fires when the skill loads in at least 2 of 3 runs.
- Agents may skip a skill for a simple one-step request they can do alone. Test with tasks big enough to need the skill.
- Check sibling routing by running a sentence that belongs to a sibling and confirming only the sibling fires. Check the missing-sibling case by installing one skill alone and giving it a sentence that belongs to a sibling: it should say so in one line and do the part it can.

## Report

A table: case, baseline result, with-skill result, verdict, change made, real or simulated. Pass bar: at least 80% of should-fire prompts fire, at most 10% of should-not-fire prompts fire, every task case meets its expected behaviour.

## Source

- obra/superpowers, "writing-skills": https://github.com/obra/superpowers
- Agent Skills, evaluating skills and optimizing descriptions: https://agentskills.io
