---
name: prompt-chain
description: Turns a multi-step task into a prompt chain, a numbered series of prompts where each output feeds the next, with placeholders, a handoff map and approval points. Use when one prompt is too much because the task mixes research, planning, drafting and checking, when the output of one step must feed another, or when the user wants a step-by-step workflow to run in a chat model, such as a launch plan, an insight report or a content calendar. Vietnamese triggers - prompt chain, chuỗi prompt, chia việc nhiều bước, quy trình nhiều prompt, bộ prompt theo giai đoạn, kế hoạch nhiều bước.
license: MIT
metadata:
  author: Masonshare
  version: "2.0.0-draft"
  language: en (Vietnamese edition in references/vi.md)
---

# Prompt Chain

Split a task that is too big for one prompt into linked prompts, each with one job. Process credit: the Prompt Architect method by Masonshare.

Reply in the user's language. Vietnamese users get Vietnamese output; keep the English term in parentheses on first use.

Scope: a task that needs more than one model call. A single prompt goes to prompt-design, a prompt that fails goes to prompt-review, a bot soul goes to bot-soul, test loops go to prompt-test.

Work loop: clarify, research, plan, build, verify. A chain is always a big prompt: stop at the outline in step 4 and wait for approval. Pause at a gate before anything hard to reverse: publishing, sending, deleting, spending, scheduling.

## Steps

### 1. Start the project

Collect in one batch, each with a suggested default: final goal, context (field), reader or user, channel, constraints (time, budget, legal, brand voice, length), data the user has, success criteria (measurable). Ask at most 5 questions.

Done when: the fields are filled or marked as assumptions and the user has seen them.

### 2. Expert process and dependency map

Ask the model to act as a 20-year practitioner in the field and describe the step-by-step process that produces the final output: per step the goal, the deliverable and a KPI. Then map dependencies: which input each step needs, and which step's output becomes which step's input.

Done when: a step list with KPIs and a dependency map without broken links exist.

### 3. Reality Check

Compare the steps with the data the user really has. Table: step, doable now (yes or no), what is missing, how to fill it, temporary assumption with its risk. Then self-verify the assumptions: which is most likely wrong, what sign would show it, what the alternative is. Use only information the user gave; ask the 5 most important questions when more is needed.

Done when: every step has a doable verdict and every gap has a fix or a marked assumption.

### 4. Plan and outline (gate)

Trim the steps to what the real deadline, people, tools and constraints allow. Per step: goal, required input, output, time, done-criterion. Propose the output spec: section outline, length, tone, format and an acceptance checklist of 5-10 checkable criteria (these become scoring criteria in prompt-test). Stop and wait for approval.

```
Chain: <name> | Model: <target> | N links
1. <step> in: <input> out: <output> -> feeds link <n>
Acceptance checklist: <5-10 criteria>
Approve to continue? (yes / change X)
```

Done when: the user approved the plan and the checklist.

### 5. Build the links

For every link write:
1. Step name and a one-line explanation.
2. The prompt in a code block, with at least Role, Context, Task and Format, and quality limits (length, structure, what to avoid).
3. The inputs the user must fill.
4. The expected output and the line "The output of this prompt becomes the input of step N".

Chain rules:
- One job per link. Split every "analyse then fix" into two prompts (the greedy error).
- The first prompt lists all placeholders in square brackets, each with an inline example. Later prompts list only new ones.
- Each later prompt names the earlier output it consumes.
- Add a confirmation or fallback branch where a wrong output is costly.
- Drop links the user can do by copy-paste.

Variants, used where a test shows a need:

| Need | Add |
|---|---|
| The user wants control at each step | Step-by-step mode: give only link 1, end with "Paste the output of step 1 here and I will write the prompt for step 2" |
| A step benefits from options | A 3-prompt cluster: generate 3-5 options, score them on named criteria, pick and develop the best |
| A step holds claims that are easy to get wrong | A verification link: list verification questions, answer each from the user's data only, give a conditional conclusion and name what the user must confirm |

Ready-to-paste wording for each stage and three sample chains (launch plan, insight report, content engine) are in [references/stage-prompts.md](references/stage-prompts.md). Read it when the user asks for the kit or wants prompts to paste into another chat model. The steps above are enough without it.

Done when: every link is written, the handoff map between links is shown, and every placeholder has an example.

### 6. Walk the chain

Run the chain once on a small sample input, link by link, and check each output against the next link's required input. Fix a broken handoff first. For 5-10 cases, scoring and a changelog, hand over to prompt-test.

Hand off with exactly 5 fields, in this order: Goal, Inputs, Deliverable, Done when, Open items. Mark untested links as untested.

Done when: the sample run reaches the final output, with each handoff checked, and the handoff is sent.

## Reference files

- [references/stage-prompts.md](references/stage-prompts.md): paste-ready prompts for stages 0-5B and three sample chains. Read when the user wants the kit.
- [references/vi.md](references/vi.md): Vietnamese edition. Read when the user writes Vietnamese and wants the process in Vietnamese.

## Sources

- Masonshare, Prompt Architect process and stage prompt kit (original work).
- Schulhoff et al., "The Prompt Report" (2024): https://arxiv.org/abs/2406.06608
