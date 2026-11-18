# Testing a skill with subagents

Read this when running the baseline and retest from Step 7, or when a skill keeps failing. The core idea, test first and watch it fail before you write the fix, comes from the "writing-skills" skill in obra/superpowers (https://github.com/obra/superpowers). The procedure below is written fresh for this skill.

## The idea

A skill is code for an agent, so test it like code. Run the task without the skill, record what goes wrong, write the skill to fix exactly those failures, then run again. A skill never seen failing may fix nothing.

## Setup

Use a fresh subagent per run. A subagent starts with no memory of earlier runs, so the result reflects the skill and the prompt only.

- Without-skill run: the subagent gets the test prompt and nothing else.
- With-skill run: the subagent gets the same prompt, plus the skill folder installed where the agent loads skills, or the SKILL.md text pasted in front when the platform imports only SKILL.md.
- Run the two versions side by side, with identical prompts and files.
- When the platform cannot spawn subagents, open a new chat per run and paste results into a table.

## Baseline

1. Take the task cases from `evals/evals.json`.
2. Run each case without the skill.
3. Record the output and, for each failure, the exact wording the agent used and the shortcut it took. Real quotes show the cause; paraphrases hide it.
4. Group failures: wrong format, skipped step, invented fact, ignored constraint, wrong tool, never started the skill.

## Write to the failures

Each failure becomes one instruction, placed where it applies, with its reason. Write to the failures you saw. Generic advice ("be careful") adds length and changes nothing.

## Retest

1. Run the same cases with the skill, each in a fresh context.
2. Grade every assertion PASS or FAIL with a quoted line as evidence.
3. Compare three columns per case: baseline, with skill, expected.
4. A case that fails with the skill goes back to the failure grouping: a skipped step means a weak completion criterion, a wrong result means a missing instruction, a skill that never loaded means a weak description.
5. After each fix, rerun the failed cases and a few passed ones to catch regressions. Five rounds or fewer usually settles it.

## Test style by skill type

| Type | Test with | Passes when |
|---|---|---|
| technique | a new scenario, a variation, a prompt missing some information | the agent applies the steps correctly and asks for the missing input |
| reference | questions whose answers sit in the references, plus a gap question | the agent finds the right fact and says when it is absent |
| discipline | the rule under pressure: deadline, "just skip it", a tired user | the agent keeps the rule and explains it briefly |
| pattern | a case where the pattern fits and one where it does not | the agent recognizes both |

For discipline skills, combine two or three pressures in one prompt, and write each observed excuse's counter into the skill as a reason.

## Trigger testing

1. Write 8-10 should-fire and 8-10 should-not-fire prompts. Include prompts that never name the skill's domain, and near-misses for the negatives.
2. Run each prompt 3 times with the skill installed alongside a few unrelated skills. Count how often the skill loads.
3. A prompt counts as firing when it loads in at least 2 of 3 runs.
4. Split the prompts roughly 60/40 into a tuning set and a held-out set. Edit the description against the tuning set, then check the held-out set. Fixing a miss by pasting its words in the description overfits; add the user situation behind it.
5. Agents may skip a skill for a simple one-step request they can do alone. Test with tasks big enough to need the skill.

## Report

End the run with a table: case, baseline result, with-skill result, verdict, and the change made. Pass bar: at least 80% of should-fire prompts fire, at most 10% of should-not-fire prompts fire, every task case meets its expected behaviour. List anything still failing as open items in the handoff.

## Source

- obra/superpowers, "writing-skills": https://github.com/obra/superpowers
- Agent Skills, evaluating skills and optimizing descriptions: https://agentskills.io
