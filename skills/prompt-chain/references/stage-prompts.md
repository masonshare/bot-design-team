# Stage prompt kit 0-5B

Ready-to-paste prompts for the Prompt Architect process by Masonshare. Stages 0-4 map to steps 1-5 of this skill's SKILL.md; stage 5 (Feedback Loop) maps to the prompt-test skill. Replace every `[ ]` with your own text; the words inside the brackets are examples. Reply in the user's language; translate the prompts when needed.

Use the kit in two ways:
- As the bot: run a stage yourself and show the user the result.
- As the user's toolbox: hand a stage prompt to the user to paste into any chat model.

## Stage 0: Start a chain project

```
Project: a multi-step task with a prompt chain.
Final goal: [what the finished result is, e.g. a 4-week launch plan for a new tea brand]
Context: [field, e.g. small F&B business]. Reader or user: [who, e.g. the shop owner]. Channel: [web / email / ads / internal].
Constraints: [time, budget, legal, brand voice, length]
Data I have: [list it, or "none yet, assume where needed"]
Success criteria: [measurable, e.g. plan fits one page, 3 KPIs, owner can start Monday]
Walk me through 5 stages. Before stage 1, ask me the minimum you still need, in one batch.
```

## Stage 1: Gold Standard

### 1A. Expert process and KPIs

```
Act as [specific role, e.g. an SEO manager for B2B clients] in [field, e.g. industrial kitchens] with 20 years of experience.
Describe the step-by-step process you use to produce [final output, e.g. a keyword table for one topic].
For each step give: the goal of the step, its deliverable, and the KPI that shows the step was done well.
List the common risks and how to avoid them. Think step by step before answering. Use bullets.
```

### 1B. Dependency map

```
From the process above, draw a dependency map:
- What input does each step need?
- Which step's output becomes which step's input?
The aim is a prompt chain with no broken links.
```

## Stage 2: Reality Check

### 2A. What can be done with my data

```
Here is the data I have:
- [data 1, e.g. the topic I want keywords for]
- [data 2, e.g. my target customers]
- [data 3, if any]

Assess:
1. Which steps can you do well with only this data?
2. Which steps need more data, and what kind (give examples)?
3. Where data is missing, propose controlled assumptions, each with its risk.
Answer as a table: Step | Doable? | What is missing | How to fill it | Temporary assumption
```

### 2B. Self-verification (fewer invented facts)

```
For the assumptions you proposed:
- Which is most likely wrong, and why?
- What sign would show it is wrong?
- If it is wrong, what is the alternative?
Use only the information I gave. If you need more, ask the 5 most important questions.
Reason in this order, and keep answers short:
1. Give your answer.
2. Try to prove the answer wrong.
3. Try to show the objection in step 2 does not hold. If it does hold, redo step 1 with that test added.
```

## Stage 3: Co-create the Plan

### 3A. Plan under real resources

```
Using the Reality Check, make the best execution plan given:
- Deadline: [date or weeks]
- People: [one person / a team]
- Tools and channels: [list]
- Constraints: [brand, legal, budget]

Give a trimmed list of steps. Each step has: goal, required input, output, estimated time, and a done-criterion.
End with: "If this is OK, I will move to stage 4 and build the prompt chain."
```

### 3B. Output spec and acceptance checklist

```
Before stage 4, propose the final output spec:
- Section outline
- Target length
- Tone of voice
- Format (Markdown / document / JSON / table)
- Acceptance checklist of 5-10 criteria, each checkable
Then ask whether I want to change the spec.
```

The acceptance checklist becomes the scoring criteria in stage 5A.

## Stage 4: Architect the Prompt Chain

### 4A. A prompt for every step

```
Build the prompt chain for the agreed plan.
Every prompt must have at least Role + Context + Task + Format.
Use [ ] placeholders, with an example inside each [ ].
State: "The output of this prompt becomes the input of step [N]."
Add quality limits: length, structure, what to avoid.
If data is missing, ask me for exactly what you need.

For each step output:
(1) Step name and a one-line explanation
(2) The prompt, in a code block
(3) The inputs I must fill
(4) The expected output
```

Rules that keep the chain clean:
- The first prompt carries all placeholders. Later prompts add only new ones.
- Each later prompt links explicitly to the earlier output it uses.
- Drop steps the user can do by hand (for example copying a table), to save tokens.

### 4B. Approve step by step (CR mode)

```
Rewrite the chain for step-by-step approval.
Give only the prompt for step 1 now.
End with: "Paste the output of step 1 here and I will write the prompt for step 2."
```

### 4C. Add candidates and choice (ToT)

```
Which step in the chain benefits most from several options (ideas, strategy)?
For that step, write a 3-prompt cluster:
1. Generate 3-5 options.
2. Score each option on [criteria, e.g. cost, speed, risk].
3. Pick the best option and develop it into the full output.
```

### 4D. Add verification (CoVe)

```
Which step in the chain contains facts or claims that are easy to get wrong?
For that step, write a verification prompt:
- List the verification questions.
- Answer each using only the data I provide.
- Give a conditional conclusion and name what I must confirm.
```

## Stage 5: Feedback Loop

### 5A. Score and revise

```
This is the output I got from step [x]:
[paste the output]

Do this:
1. Score it against the acceptance checklist, 1-10 per criterion.
2. Name the 3 biggest problems.
3. Write a revised prompt (Prompt v2) that fixes exactly those problems.
4. Give a short reason for each change.
```

### 5B. Debug with the 4 errors

```
Current prompt:
[paste the prompt]
The result is wrong in this way:
[describe it]

Diagnose it against the 4 common errors: vague, greedy, unbounded, trapping.
Quote the line behind each finding. Then write a new prompt with a clear format and measurable criteria.
```

## Sample chains

Each starts with stage 0 filled in. Paste, then continue with stages 1-5.

### Pack A: launch marketing plan

```
Goal: a marketing plan to launch [product] in [timeframe].
Target customer: [portrait].
Channels: [Facebook / TikTok / email / website].
Data: [USP, price, competitors, insight].
Final output: one plan with goals, messages, a weekly content plan, KPIs, risks.
Run the 5 stages and build the prompt chain.
```

### Pack B: insight report from raw data

```
Task: an insight report from [source: survey / interviews / logs].
Reader: [CEO / marketing / product].
Constraint: use only the data I provide; no guesses beyond it.
Final output: executive summary, key findings, evidence, recommendations, limitations.
Run the 5 stages and build a chain with a verification (CoVe) prompt for the conclusions.
```

### Pack C: multi-channel content engine

```
Task: a content engine for [brand] over [30 / 60 / 90 days].
Inputs: pillar topics, brand voice, offer, customer portrait.
Outputs: content calendar, post briefs, outlines, drafts, QC checklist, repurposing across channels.
Design the chain with step-by-step approval (CR mode) so I can approve each step.
```
