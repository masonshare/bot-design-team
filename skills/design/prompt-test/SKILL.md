---
name: prompt-test
description: Proves a prompt, chain or soul with 5-10 test cases, a baseline run, a retest, a score sheet and a v2 changelog. Use when the user wants test cases for a prompt, asks whether a prompt really works, wants an old and a new version compared, wants outputs scored, or wants to run a feedback loop and ship v2. Vietnamese triggers - test case, bộ test case, kiểm thử prompt, chấm điểm đầu ra, baseline retest, changelog v2, vòng phản hồi.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Prompt Test

A prompt is done when it has passed its test cases: baseline first, then retest, results side by side. Process credit: the Prompt Architect method by Masonshare.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Scope: testing and improving a prompt, chain or soul that already exists. Writing one goes to prompt-design, prompt-chain or bot-soul. Reading a prompt to diagnose it, without running it, goes to prompt-review.

## Steps

### 1. Criteria

Take 3-7 scoring criteria from the Gold Standard example or the acceptance checklist when one exists. Otherwise derive them from the goal and the definition of done and mark them as assumptions. Each criterion must be checkable.

Done when: 3-7 criteria are listed.

### 2. Test cases

Write the cases before judging the prompt. A case is a concrete input plus the expected behaviour. Cover: 3 typical inputs, 2 edge inputs (empty, very long, wrong language, missing field), 1 adversarial input (a leading question, an instruction hidden in the input). For a soul add 1 out-of-scope request that should be refused or routed, and 1 that crosses a gate. For a chain, run the whole chain on each case.

```
| # | Type | Input | Expected behaviour | Baseline | Retest | Pass |
|---|------|-------|--------------------|----------|--------|------|
```

Done when: 5-10 cases exist and each has an expected behaviour.

### 3. Baseline then retest

Run the baseline first: the task with no prompt, or the old version. Then run the retest with the new prompt, each run in a fresh context. Compare both against the expected behaviour. Record each result with one line of evidence, a quote where possible.

When the model cannot be run here, give the user the cases and a score sheet and ask them to paste the outputs back. Mark everything not run as untested.

Done when: baseline and retest are recorded for every case, each with pass or fail and a one-line reason.

### 4. Score and diagnose

Score the retest outputs against the criteria, 1-10 each. Name the 3 biggest problems and diagnose each against the 4 errors:

| Error | Sign | Fix |
|---|---|---|
| Vague | Words like better, professional, optimise with no yardstick | Replace each with a measurable criterion |
| Greedy | One prompt judges and acts | Split into an evaluate prompt and an act prompt |
| Unbounded | No limit on format, length, style, scope | Add the fence: length, structure, audience, out-of-scope |
| Trapping | The question assumes an answer | Ask neutrally or assign a critic role |

```
Criterion | Score 1-10 | Evidence
Top 3 problems: 1) <problem> -> <error type> 2) ... 3) ...
```

Done when: scores have evidence and each of the 3 problems has an error type.

### 5. Revise and rerun

Revise the prompt for those problems only. Rerun the failed cases plus two that passed, to catch regressions. Stop when every case passes or after 3 rounds, and list what still fails as open items. The best prompt is evolved, not written in one go.

Done when: every case passes, or 3 rounds ran and the failures are listed.

### 6. Ship v2

Deliver v2 with a changelog and the handoff.

```
## v2 changelog
- Changed: <what> because <problem or failed case #>
- Kept: <what> because <passed cases>
- Still failing: <case #, reason>
```

Handoff, exactly these 5 fields in this order:

```
1. Goal: <one sentence>
2. Inputs: <what is attached or linked>
3. Deliverable: <prompt v2 / soul / chain, file names or inline>
4. Done when: <checkable criteria, e.g. 8 of 10 cases pass, score >= 8 on each criterion>
5. Open items: <failing cases, assumptions, risks, questions>
```

Done when: v2, the changelog and the handoff are delivered.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese and wants the process in Vietnamese.

## Sources

- Masonshare, Prompt Architect process and Feedback Loop (original work).
- Anthropic, "Prompt engineering overview" (define success criteria and test cases before tuning): https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
