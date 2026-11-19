---
name: skill-test
description: Tests one skill. Trigger tests check that its description fires on the right prompts and on no others, and task tests compare a baseline run without the skill against a retest with it. Use when the user wants to know whether a skill triggers reliably, asks for a set of test prompts for a skill or an evals.json, wants a baseline against a retest, or says a skill fires on the wrong request or never fires. Vietnamese triggers - kiểm thử skill, test kích hoạt skill, skill không kích hoạt, chạy baseline cho skill, viết evals.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Skill test

Prove a skill fires on the right prompts and changes behaviour for the better. Takes a skill folder. Hands out a result table and a pass or fail verdict.

Reply in the user's language. Vietnamese users get Vietnamese output, with the English term in parentheses on first use (full edition: [references/vi.md](references/vi.md)).

A **gate** is a stop where the user approves before work continues. Gate here: before overwriting an existing evals file.

## Route

| The user wants | Use |
|---|---|
| Trigger tests, task tests, baseline against retest | this skill |
| The description or body rewritten after a failure | skill-write |
| A skill judged, split or merged | skill-review |
| Validation, version, publishing | skill-package |
| The whole build | skill-design |

When the matching skill is not installed, say so in one line and finish the part you can do here.

## Steps

### 1. Trigger tests

1. Write 8-10 prompts that should fire the skill and 8-10 that should not. Make the negatives near-misses that share keywords, and include at least 2 that belong to a sibling skill. Vary wording, formality, length and whether the domain is named. Write them in the languages the users type.
2. Install the skill next to a few unrelated skills and next to every installed skill whose description is close (for example a general skill-writing guide). Record any rival that wins a should-fire prompt.
3. Run each prompt 3 times, each in a fresh context. A prompt counts as firing when the skill loads in at least 2 of 3 runs.
4. Split the prompts about 60/40 into a tuning set and a held-out set. Tune the description on the first, then check the second. Fixing a miss by pasting its words into the description overfits; add the user situation behind it. Never reuse held-out prompts when writing the description.

Done when: a table lists every prompt, its expected result, the skill that fired in each run and how the test was run (real or simulated).

### 2. Task tests

Write 3-5 realistic prompts with the expected behaviour, plus one vague prompt and one edge case. Save them as `evals/evals.json`:

```json
{
  "skill_name": "<name>",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic message, worded the way a user would type it.",
      "expected_output": "The behaviour a correct run shows.",
      "files": [],
      "assertions": ["A checkable statement, such as: asks which output format before drafting"]
    }
  ]
}
```

Each assertion can be graded PASS or FAIL from the transcript with a quoted line as evidence. Assertions describe behaviour, not internal step numbers. Trigger prompts go in `evals/triggers.json` as `{ "query": "...", "should_trigger": true }` entries.

Done when: each case has a prompt, an expected behaviour and assertions.

### 3. Baseline

Run each task case in a fresh context without the skill. Record the output and, for each failure, the agent's exact words and the shortcut it took. Real quotes show the cause; paraphrases hide it.

Done when: every case has a recorded baseline.

### 4. Retest

Run the same cases with the skill, each in a fresh context. When the platform imports only SKILL.md, test with the SKILL.md alone, since that is what some users get. Grade each assertion PASS or FAIL with a quoted line. Compare three columns per case: baseline, with skill, expected.

Done when: every assertion is graded.

### 5. Fix and rerun

Close each failure at its cause: the skill never loaded means a weak description; a skipped step means a weak completion criterion; a wrong result means a missing instruction. Rerun the failed cases plus a sample of the passed ones. Five rounds or fewer usually settles it.

Done when: the failed cases pass and no earlier case regressed.

### 6. Pass bar and report

At least 80% of should-fire prompts fire, at most 10% of should-not-fire prompts fire, and every task case meets its expected behaviour. End with a table: case, baseline, with skill, verdict, change made. Mark each row real (an actual run) or simulated (reasoned, not run), and list what still fails as open items.

Done when: baseline and retest sit side by side and the bar is met, or the failures are listed as open items.

## Test style by skill type

| Type | Test with | Passes when |
|---|---|---|
| technique | a new scenario, a variation, a prompt missing information | applies the steps and asks for the missing input |
| reference | questions answered in the references, plus a gap question | finds the right fact and says when it is absent |
| discipline | the rule under pressure: deadline, "just skip it" | keeps the rule and explains it briefly |
| pattern | one case where it fits and one where it does not | recognizes both |

## Handoff

When passing work to another bot or the user, send 5 fields in order: Goal (one sentence), Inputs (attached or linked), Deliverable (file names or inline), Done when (checkable criteria), Open items (questions, risks, anything not done).

## Reference files

- [references/testing.md](references/testing.md): subagent setup, a command-line way to read which skill fired, and limits of each method. Read when running the tests, or when a skill keeps failing.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user works in Vietnamese.

## Sources

- obra/superpowers, "writing-skills" (test-first idea for skills): https://github.com/obra/superpowers
- Agent Skills, evaluating skills and optimizing descriptions: https://agentskills.io
