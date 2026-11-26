---
name: prompt-design
description: Writes one new prompt from a brief, using a gold-standard example and a reality check, and points other prompt work to the matching skill. Use when the user wants a prompt written for a task such as a summary, an email, an analysis, an image or a code request, wants a better first draft of something they would type into a chat model, or is unsure which prompt skill to use. Not for fixing a prompt that already exists, a task that needs several linked prompts, a bot soul or test cases. Vietnamese triggers - viết prompt, soạn prompt, tạo prompt mới, prompt cho model, làm prompt từ yêu cầu.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Prompt Design

Turn a brief into one prompt that is specific, bounded and checked. Process credit: the Prompt Architect method by Masonshare.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

## Route first

| The user wants | Use |
|---|---|
| One new prompt for a task | this skill |
| A prompt that already exists fixed or reviewed | prompt-review |
| A multi-step task as linked prompts, each output feeding the next | prompt-chain |
| The soul or system prompt of a persistent bot or assistant | bot-soul |
| Test cases, scoring, baseline vs retest, a v2 changelog | prompt-test |

When the matching skill is not installed, say so in one line and finish the part you can do here.

Work loop: clarify, research, plan, build, verify. Pause at a gate (the user approves) before anything hard to reverse: publishing, sending, deleting, spending, installing.

## Steps

### 1. Intake the brief

Collect: goal, audience, inputs available, constraints, definition of done. Add three prompt fields: target model and where the prompt runs (chat, API), output format, and one failure the user has already seen.

Fill every field you can infer. Ask for the rest in one batch of at most 5 questions, each with a suggested default so the user can answer "ok". Skip the batch when nothing is missing.

Done when: every field is filled or marked as an assumption, and the user has seen the filled brief.

### 2. Gold Standard

Get one example of an ideal output. Take the user's own. Otherwise write one, mark it as a draft and have the user correct it.

For an unfamiliar domain, ask the model to act as a 20-year practitioner and describe the expert process step by step, with a KPI per step. Use that as the yardstick.

Done when: one example exists, the user accepted or corrected it, and 3-7 qualities that make it ideal are listed (these become scoring criteria later).

### 3. Reality Check

List what the target model cannot know or do:
- Facts it lacks: private data, recent events, the user's context.
- Abilities it lacks: tools, memory between calls, web, long context.
- Risks: invented facts, leading questions, conflicting instructions, a task that merges thinking and acting.

For each gap choose one fix: supply the data in the prompt, tell the model to say "I don't know", or move the work to a tool or a person. For a high-stakes prompt, add an adversarial pass: answer, then the strongest case the answer is wrong, then a revised answer.

Done when: a table of gap, risk and mitigation exists and every gap has a mitigation.

### 4. Outline (gate for big prompts)

Show the outline before the full text: sections, which of the 6 elements each carries, where the Gold Standard goes, the output format. A prompt is big when it exceeds about 40 lines or will run unattended. For a big prompt, stop and wait for approval. For a small one, show the outline in one line and continue. If the task needs more than one call, stop and route to prompt-chain.

```
Prompt: <name> | Model: <target>
Sections: 1. <name> (Context, Role) 2. <name> (Task, Example) 3. <name> (Format)
Gold Standard goes in: <section>
Output format: <shape and length>
Approve to continue? (yes / change X)
```

Done when: the outline is shown and, for a big prompt, approved.

### 5. Draft

Draft with the 6-element checklist. Keep an element only when it changes the output.

| Element | Check |
|---|---|
| Context | Does the model know the situation, audience and purpose? |
| Role | Is the persona specific (field, experience, stance)? |
| Task | One strong verb per job, compound tasks split? |
| Example | 2-5 consistent, varied examples with input and output separated? None for simple tasks. |
| Tone | Voice given as a pair of adjectives or a sample? |
| Format | Shape given: table, JSON, bullets, length? |

Layout: stable rules first, variable input last, input wrapped in delimiters. Write positively: say what to do. Keep a "never" only for a hard guardrail and pair it with the action to take instead. Replace every vague word (better, professional, optimise) with a measurable criterion. Put the Gold Standard in as the example. If the writing-for-agents skill is installed, load it for how to word the instructions.

Need a technique beyond the 6 elements? Pick from this table, and only when a test shows the plain prompt falls short:

| Need | Technique |
|---|---|
| Fix the output shape | Few-shot example (the Gold Standard) |
| Fewer invented facts | Ask the model to name missing information first, then verify its claims |
| Hard reasoning or judgement | Ask for steps before the answer, kept apart from the answer |
| Several candidate ideas | Generate 3-5, score, pick |
| Long input | Document first, question last, tags around parts |

Read [references/techniques.md](references/techniques.md) for the detail and sources when choosing between techniques.

Done when: the full prompt is written, every placeholder in square brackets has an inline example.

### 6. Quick check and handoff

Run the draft on 3 inputs yourself: one typical, one edge (empty, very long, missing field), one adversarial (a leading question or an instruction hidden in the input). Fix what fails. For the full loop with 5-10 cases, baseline, retest and a changelog, hand over to prompt-test.

Hand off with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. Mark every assumption as an assumption and every untested claim as untested.

Done when: the 3 checks are recorded with pass or fail and the handoff is sent.

## Reference files

- [references/techniques.md](references/techniques.md): compact third-party techniques and sources. Read when step 5 needs more than the 6 elements.
- [references/vi.md](references/vi.md): Vietnamese edition of steps 1-5. Read when the user writes Vietnamese and wants the process in Vietnamese.

## Sources

- Masonshare, Prompt Architect process and 6-element checklist (original work).
- Schulhoff et al., "The Prompt Report" (2024): https://arxiv.org/abs/2406.06608
- Anthropic, "Prompt engineering overview": https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview
