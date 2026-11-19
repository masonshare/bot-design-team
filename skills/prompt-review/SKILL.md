---
name: prompt-review
description: Diagnoses a prompt the user already has and rewrites it. Use when the user pastes a prompt and says it is vague, too long, ignored, gives wrong or inconsistent output, or asks for a review of it. Finds the cause against four errors (vague, greedy, unbounded, trapping) and a six-element checklist, quotes the line behind each finding and returns a marked rewrite. Not for writing a prompt from scratch, a bot soul or a multi-step chain. Vietnamese triggers - sửa prompt, gỡ lỗi prompt, đánh giá prompt, review prompt, prompt bị sai, prompt chạy không đúng, tối ưu prompt.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Prompt Review

Find why an existing prompt fails, fix the top causes, show the evidence. Process credit: the Prompt Architect method by Masonshare.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Scope: one existing prompt. A bot soul or system prompt that a bot carries on every turn goes to bot-soul. A task that needs several linked calls goes to prompt-chain. A writing job from scratch goes to prompt-design. Full test loops go to prompt-test; when it is not installed, use the quick check in step 5.

## Steps

### 1. Read the prompt and the symptom

Take the prompt and what goes wrong (or no symptom). Ask for one failing output when none is given; a diagnosis without an output is a guess, so mark it as one.

Done when: the prompt, the symptom and at least one example output (or a note that none exists) are in hand.

### 2. Diagnose

Check the prompt against both tables. Quote the exact line behind each finding.

| Error | Sign | Fix |
|---|---|---|
| Vague | Words like better, professional, optimise with no yardstick | Replace each with a measurable criterion: tone, length, vocabulary, count |
| Greedy | One prompt asks the model to judge and to act | Split into an evaluate prompt and an act prompt that consumes the evaluation |
| Unbounded | No limit on format, length, style, scope | Add the fence: length, structure, audience, must-include, out-of-scope |
| Trapping | The question assumes an answer ("explain why A is best") | Ask neutrally ("compare A, B, C against the goal") or assign a critic role |

| Element | Check |
|---|---|
| Context | Does the model know the situation, audience and purpose? |
| Role | Is the persona specific (field, experience, stance)? |
| Task | One strong verb per job, compound tasks split? |
| Example | 2-5 consistent, varied examples, input and output separated? None for simple tasks. |
| Tone | Voice given as a pair of adjectives or a sample? |
| Format | Shape given: table, JSON, bullets, length? |

Not every prompt needs all six elements: flag a missing one only when adding it would change the output. Also look for instructions that conflict, a variable input placed above stable rules, and a "never" with no replacement action.

Done when: every finding has a quoted line, an error or element name and a one-line effect.

### 3. Rank

Order the findings by impact on the symptom. Fix the top 3 first and list the rest as optional.

### 4. Rewrite

Rewrite the prompt. Mark each change with the finding it answers, for example `[F1]`. Keep what works. Write positively and keep a "never" only as a hard guardrail with the action to take instead.

Show the result in this shape:

```
| # | Quoted line | Error / element | Effect | Fix |
|---|-------------|-----------------|--------|-----|

Rewritten prompt (changes marked [F1], [F2] ...):
<prompt>
```

Done when: every finding is answered by a marked change or listed as deliberately skipped.

### 5. Verify

Run the old and the new prompt on the failing input plus 2 other inputs (one edge, one typical). Record pass or fail with a one-line reason each. The symptom must be gone in the new run. For 5-10 cases, a score sheet and a changelog, hand over to prompt-test.

Hand off with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. Mark untested claims as untested.

Done when: the failing input passes on the rewrite and the handoff is sent.

## Reference files

- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese and wants the process in Vietnamese.

## Sources

- Masonshare, Prompt Architect process, 4 errors and 6-element checklist (original work).
- Anthropic, "Prompt engineering overview": https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
