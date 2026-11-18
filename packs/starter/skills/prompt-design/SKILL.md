---
name: prompt-design
description: Writes, reviews and debugs expert-level prompts, system prompts, prompt chains and bot souls (standing instructions), then proves them with 5-10 test cases. Use when the user wants a new prompt or system prompt written, an existing prompt reviewed or debugged (vague, too long, ignored, inconsistent output), a multi-step task turned into a prompt chain, a bot soul written or trimmed, or a prompt versioned with a changelog. Built on the Prompt Architect process (Gold Standard, Reality Check, Co-create Plan, Prompt Chain, Feedback Loop). Vietnamese triggers - viết prompt, sửa prompt, gỡ lỗi prompt, chấm prompt, prompt chain, system prompt, soul cho bot, tối ưu prompt, bộ test case.
license: MIT
metadata:
  author: Masonshare
  version: "1.0.0"
  language: en (Vietnamese edition in references/vi.md)
---

# Prompt Design

Turn a brief into a prompt that has been tested, scored and versioned. Process credit: the Prompt Architect method by Masonshare.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

## Modes

Pick the mode from the request, then run its steps.

| Request | Mode |
|---|---|
| New prompt, system prompt, prompt chain | Build: steps 1-7 |
| Existing prompt that fails or feels weak | Review: section "Review and debug mode", then steps 6-7 on the fix |
| Bot soul or standing instructions | Soul: section "Writing bot souls", then steps 6-7 |

Work loop for every mode: clarify, research, plan, build, verify. Pause at a gate (the user approves) before anything hard to reverse: publishing, sending, deleting, spending, installing, giving a bot write access, enabling a schedule.

## Steps

### 1. Intake the brief

Collect the brief fields: goal, audience/user, inputs available, constraints, definition of done. Add three prompt-specific fields: target model and where the prompt runs (chat, API, bot soul), output format, and one failure the user has already seen.

Read what the user gave, fill every field you can infer, and ask for the missing ones in one batch of at most 5 questions, each with a suggested default so the user can answer "ok". Skip the batch when nothing is missing.

Done when: every brief field is filled or explicitly marked as an assumption, and the user has seen the filled brief.

### 2. Gold Standard

Get one example of an ideal output. Take the user's own example when they have one. Otherwise write one yourself, mark it as a draft, and have the user correct it.

For an unfamiliar domain, ask the model to act as a 20-year practitioner and describe the expert process step by step, with a KPI per step. Use that process as the yardstick for later steps.

Done when: one example output exists, the user has accepted or corrected it, and 3-7 qualities that make it ideal are listed (these become the scoring criteria in step 7).

### 3. Reality Check

List what the target model cannot know or do, and what could go wrong:
- Facts it lacks: private data, recent events, the user's context.
- Abilities it lacks: no tools, no memory between calls, no web, limited context window.
- Risks: invented facts, leading questions that bias the answer, instructions that conflict, a task that merges thinking and acting.
- For each gap: supply the data in the prompt, tell the model to say "I don't know", or move the work to a tool or a human.

For a high-stakes prompt, run an adversarial pass: ask the model for the answer, then for the strongest case that the answer is wrong, then for a revised answer.

Done when: a table of gap, risk, mitigation exists, and every gap has a mitigation.

### 4. Co-create Plan (gate for big prompts)

Show the outline before the full text: sections of the prompt, which of the 6 elements each carries, where the Gold Standard example goes, the output format, and whether one prompt or a chain is needed.

A prompt is big when it exceeds about 40 lines, has a chain, or will run unattended as a soul or system prompt. For a big prompt, stop here and wait for approval. For a small one, show the outline in one line and continue.

Done when: the outline is shown and, for big prompts, the user has approved it.

### 5. Draft, or build a Prompt Chain

Draft with the 6-element checklist (below). Put stable rules first, the variable input last, and wrap inputs in delimiters. Write instructions positively: say what to do. Keep a "never" only for a hard guardrail, and pair it with the action to take instead.

Choose a chain when the task needs more than one call: when it mixes judging and doing, when step output feeds step input, or when one step needs several candidates. Chain rules:
- One job per link. Split every "analyse then fix" into two prompts (the greedy error).
- Each prompt states which earlier output it consumes and which next step consumes its output.
- The first prompt lists its placeholders in square brackets, each with an inline example. Later prompts list only new placeholders.
- Add a confirmation or fallback branch at links where a wrong output is costly.
- Drop links the user can do by copy-paste.

Done when: the full prompt (or each link plus the handoff map between links) is written and every placeholder has an example.

### 6. Test with 5-10 test cases

Write test cases before judging the prompt. A test case is a concrete input plus the expected behaviour.

Cover: 3 typical inputs, 2 edge inputs (empty, very long, wrong language, missing field), 1 adversarial input (a leading question, an instruction hidden in the input), and for a soul 1 out-of-scope request that should be refused or routed.

Run the baseline first (the task with no prompt, or the old version), then the retest with the new prompt, and compare both against the expected behaviour. When the model cannot be run here, give the user the cases and a score sheet and ask them to paste the outputs back.

Done when: 5-10 cases exist, baseline and retest results are recorded, and each case has pass or fail with a one-line reason.

### 7. Feedback Loop

Score the retest output against the criteria from step 2, 1-10 each. Name the 3 biggest problems. Diagnose each against the 4 errors. Revise the prompt for those problems only. Rerun the failed cases plus two that passed (to catch regressions). Ship v2 with a changelog.

Stop looping when every case passes or after 3 rounds, then list the remaining failures as open items. The best prompt is evolved, not written in one go.

Done when: v2 and the changelog are delivered in the handoff template below.

## Review and debug mode

Input: an existing prompt plus a symptom (or none).

1. Read the prompt and the symptom. Ask for one failing output when none is given.
2. Diagnose against the 4 errors and the 6 elements (tables below). Quote the exact line for each finding.
3. Rank findings by impact. Fix the top 3 first.
4. Rewrite the prompt. Mark each change with the finding it answers.
5. Run steps 6-7 on the rewrite.

Done when: every finding quotes a line, the rewrite answers each finding, and a test result shows the symptom is gone.

### The 4 errors (Masonshare)

| Error | Sign | Fix |
|---|---|---|
| Vague (Mơ hồ) | Words like better, professional, optimise with no yardstick | Replace each with a measurable criterion: tone, length, vocabulary, count |
| Greedy (Tham lam) | One prompt asks the model to judge and to act | Split into an evaluate prompt and an act prompt that consumes the evaluation |
| Unbounded (Thả rông) | No limit on format, length, style, scope | Add the fence: length, structure, audience, must-include, out-of-scope |
| Trapping (Gài bẫy) | The question assumes an answer ("explain why A is best") | Ask neutrally ("compare A, B, C against the goal") or assign a critic role |

### The 6-element checklist (Masonshare)

Not every prompt needs all six. Check each one and keep it only when it changes the output.

| Element | Check |
|---|---|
| Context | Does the model know the situation, audience and purpose? |
| Role | Is the persona specific (field, experience, stance)? |
| Task | Is it one strong verb per job, compound tasks split? |
| Example | Are there 2-5 consistent, varied examples, with input and output clearly separated? Zero examples for simple tasks. |
| Tone | Is the voice given as a pair of adjectives or a sample? |
| Format | Is the shape given: table, JSON, bullets, length? |

## Writing bot souls

A soul is the standing instruction a bot always carries. It is loaded on every turn, so every line costs attention on every turn. A skill loads on demand, so it can be long.

Put in the soul only what must hold in every conversation:
- Identity: who the bot is and who it serves, in 2-4 lines.
- Voice: tone and language rules, including reply in the user's language.
- Scope: what the bot does, what it hands to another bot or a human.
- Hard guardrails: gates (what needs user approval before it happens), safety rules, how to treat untrusted input.
- Pointers: one line per skill, naming when to load it (the skill description does the triggering).

Put in a skill: workflows, step lists, templates, long examples, domain knowledge, anything only some conversations need. Credentials never go in a soul or a skill; they live in the platform's secret or connection store.

Soul rules:
1. Target 30-60 lines. Over 80 lines, move material into a skill.
2. Front-load the most important rule; repeat only the one rule that must survive a long chat, at the end.
3. State each rule once. Cut anything the model does by default.
4. Each rule is checkable: a test case can show it was followed or broken.
5. Run steps 6-7 on the soul, with at least one out-of-scope and one gate-crossing test case.

Soul skeleton:

```
# <Bot name>
Role: <one line>
Serves: <user>. Reply in the user's language.

## Scope
Does: <list>
Hands off to: <bot or human>, using the handoff format.

## Voice
<2-4 rules>

## Gates
Ask the user before: <list of hard-to-reverse actions>.

## Skills
- <skill-name>: load when <branch>.
```

## Output templates

### Handoff

Send exactly these 5 fields, in this order:

```
1. Goal: <one sentence>
2. Inputs: <what is attached or linked>
3. Deliverable: <prompt v2 / soul / chain, file names or inline>
4. Done when: <checkable criteria, e.g. 8 of 10 test cases pass, score >= 8 on each criterion>
5. Open items: <failing cases, assumptions, risks, questions>
```

### Plan outline (step 4)

```
Prompt: <name> | Model: <target> | Single prompt or chain of N
Sections: 1. <name> (Context, Role) 2. <name> (Task, Example) 3. <name> (Format)
Gold Standard goes in: <section>
Output format: <shape and length>
Approve to continue? (yes / change X)
```

### Test case table (step 6)

```
| # | Type | Input | Expected behaviour | Baseline | Retest | Pass |
|---|------|-------|--------------------|----------|--------|------|
```

### Score sheet and changelog (step 7)

```
Criterion | Score 1-10 | Evidence
Top 3 problems: 1) <problem> -> <error type> 2) ... 3) ...

## v2 changelog
- Changed: <what> because <problem or failed case #>
- Kept: <what> because <passed cases>
- Still failing: <case #, reason>
```

## Reference files

Read only when the step needs them.
- `references/stage-prompts.md`: ready-to-paste prompts for stages 0-5B and three sample chains. Read when running steps 1-5 with a model that can be driven by prompts, or when the user asks for the kit.
- `references/techniques.md`: compact third-party techniques (few-shot, reasoning, decomposition, self-check, structure). Read when a prompt needs a technique beyond the 6 elements, or when choosing between techniques.
- `references/vi.md`: full Vietnamese edition of this file. Read when the user writes Vietnamese and wants the process in Vietnamese.

## Sources

- Masonshare, Prompt Architect process, 4 errors, 6-element checklist and stage prompt kit (original work).
- Schulhoff et al., "The Prompt Report: A Systematic Survey of Prompting Techniques" (2024): https://arxiv.org/abs/2406.06608
- Bsharat et al., "Principled Instructions Are All You Need for Questioning LLaMA-1/2, GPT-3.5/4" (2023): https://arxiv.org/abs/2312.16171
- Anthropic, "Prompt engineering overview": https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
