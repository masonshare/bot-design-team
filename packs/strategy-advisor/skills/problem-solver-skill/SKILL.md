---
name: problem-solver-skill
description: Strategic problem solver for founders and executives - frames the problem, diagnoses root causes, maps competitive dynamics, compares options with explicit criteria and turns the pick into an action plan with owners and checkpoints. Use for "why does this keep happening", "root cause", "we are stuck on an operational or organisational problem", "pre-mortem", "action plan" (market and competitive strategy choices belong to business-strategist). Tiếng Việt - giải quyết vấn đề chiến lược - xác định vấn đề, tìm gốc rễ, phân tích cạnh tranh, so sánh phương án theo tiêu chí rõ ràng, lập kế hoạch hành động có người phụ trách và mốc kiểm tra ("tìm nguyên nhân gốc", "nên chọn A hay B", "kế hoạch hành động"; chiến lược thị trường và cạnh tranh thuộc business-strategist).
---

# Problem Solver

## What it solves

Leaders often act on the first explanation, or stall because the problem is too broad to start. This skill turns a messy situation into: a framed question, a structured breakdown, evidence-backed causes, a short list of scored options, one recommendation and a dated action plan. It names every framework it uses so the reasoning can be checked.

## Keywords for modes

Say one word to pick a mode (no commands needed):
- **express**: the problem is already clear; give a fast analysis with one alternative lens and a next step.
- **guided** (default): ask the intake questions once, confirm the framework sequence, then deliver.
- **deep**: full diagnosis across several frameworks, with a note on which framework produced which insight.
- **diagnose / strategize / decide**: bias the run toward root cause, competitive dynamics, or a decision under time pressure.

If the user names a framework, use it. If the request is ambiguous, ask one routing question, never list every mode.

## Brand and company context

If the client keeps a `brand-profile.md`, read it first and do not re-ask what it already answers (positioning, audience, products, limits). Otherwise use the intake below. The skill is not tied to marketing: it works on operations, sales, product, finance and organisation problems.

## Intake (ask once, each question with a default)

Ask only what is missing, in one message:
1. **Problem**: what is observable (numbers, events), not the interpretation. Default: use the user's wording and label it as a claim.
2. **Stakes and deadline**: what happens if nothing changes, and by when a decision is needed. Default: next quarter.
3. **Past attempts**: what was tried and what happened. Default: none.
4. **Constraints**: budget, people, time, regulation, politics. Default: none stated.
5. **Success criterion**: what "solved" looks like and how it is measured. Default: propose one and mark it as an assumption.

In express mode, work with whatever was given. Never invent figures: if a number is missing, say so, state the assumption and show what would change if it were wrong.

## Workflow

### 1. Frame the problem
Write one sentence each for the **question** (open, answerable, owned by someone), the **scope** (in, out, time window) and the **success criterion** (metric, target, date). Use a situation, complication, question, answer frame when the audience is an executive or the issue is political. Separate symptom from problem: a drop in a metric is a symptom until a cause is shown.

### 2. Structure it
Break the question into parts that do not overlap and together cover the whole (an issue tree, MECE rule). Pick the cut that fits the decision, for example by funnel stage, customer segment, value driver or process step. Write the lead hypothesis if one exists (hypothesis-driven analysis): "we believe X is the main driver; this is what would prove it wrong".

### 3. Gather evidence
For each branch list the cheapest data that would confirm or reject the hypothesis, who holds it, and what is already known. Prefer comparisons (before and after, segment against segment, us against the market) over single numbers. Use the platform's search or read-web tool for external facts if available; if none, ask the user to paste the content. Mark each finding as **observed**, **reported by someone**, or **assumed**.

### 4. Find causes
Pick the tool by problem type (details in `references/framework-toolkit.md`):
- Single event or recurring failure: five whys, tracing at least three levels, each answer backed by evidence; a cause-and-effect (fishbone) layout when many contributors compete.
- Several interacting variables: change one variable at a time where possible, otherwise compare cases with and without the problem.
- Persistent pattern despite past fixes: feedback loops, delays, and the places in the system where a small change has a large effect (leverage points).
- Multiple parties with conflicting aims: players, options, payoffs, one-shot or repeated game, equilibrium check.

State the root cause as a testable sentence, then name what evidence would disprove it.

### 5. Generate options
List 3 to 6 options, always including "do nothing or delay" and one that attacks the cause rather than the symptom. For customer-facing problems add an empathise, define, ideate, prototype, test pass. Merge near-duplicates. Do not score yet.

### 6. Evaluate with explicit criteria
Build a decision matrix: 4 to 6 criteria agreed with the user (impact on the success metric, cost, time to effect, risk, reversibility, fit with constraints), weights that sum to 100, scores 1 to 5, each score with a one-line reason. Then stress-test the leader:
- **Second-order check**: "and then what" for at least two consequences, including how competitors and customers respond.
- **Scenario thinking**: best, base and worst case for the top two options, and the signal that tells which scenario is unfolding.
- **Reversibility**: a reversible choice should be made fast with partial information; an irreversible one deserves more analysis or a pilot.
- **Pre-mortem**: imagine it failed in twelve months; list the three most likely reasons and what would prevent each.

### 7. Recommend
One pick, stated in a sentence, with the three reasons that carry it, the main risk, and what would make you change your mind. If the top score is overridden by a constraint or judgement call, say so. If two options are close, recommend a cheap test to separate them.

### 8. Plan the actions
Turn the pick into 5 to 10 actions in a table: action, owner (a role or a name supplied by the user), start and due date, deliverable, dependency. Add 2 to 4 checkpoints, each with a metric, a threshold and a decision (continue, adjust or stop), plus a first step doable within a week. Prioritise with an urgent-important matrix when there are too many items.

## Output structure

```
# [Problem title]

## Frame
Question / scope / success criterion

## Diagnosis
Issue tree (short), evidence table (finding | status: observed, reported, assumed), root cause and what would disprove it

## Options and evaluation
Decision matrix, second-order notes, scenarios, pre-mortem

## Recommendation
Pick, three reasons, main risk, change-of-mind trigger

## Action plan
Actions table and checkpoints

## Assumptions and open questions
Each assumption, how to test it, cost if wrong

## Next step
One concrete action for this week
```

Express mode may shorten each section to two or three lines but keeps the headings. A fill-in version lives in `assets/problem-brief-template.md`.

## Output rules
- Label every assumption; never fabricate data, quotes or benchmarks. A rule-of-thumb number must be marked "reference point" and checked against the user's own market.
- End with one concrete next step.
- Save as a new Google Doc, Sheet or Slides if a connection exists, otherwise reply in the conversation. Never overwrite an existing file.
- Never send, publish, spend money or change anything outside the conversation without the user's go-ahead.
- Optional visual layer: offer an issue tree, loop diagram or matrix through the `visual-thinking` skill if installed, otherwise a plain-text table.

## Quality bar
1. The problem is a question with scope and a measurable success criterion, not a topic.
2. Root cause traced at least three levels, with evidence per level, and a falsifier named.
3. Options include "do nothing" and a cause-level option; criteria and weights are visible before scores.
4. Every recommendation carries a second-order consequence and a failure scenario.
5. Facts are separated from assumptions; no invented numbers.
6. Actions have an owner, a date, a deliverable and a checkpoint with a stop rule.
7. Frameworks are named where used; no filler such as "synergy" or "best practices" without saying which.

## Related skills (soft, never required)
Use if installed, otherwise do the step in place: `system-thinking` (deep feedback-loop and delay mapping), `business-strategist` (market position, competitive moves), `visual-thinking` (diagrams). For hard market facts or customer paths use a market research or journey-mapping skill if present.

## When not to use
- The user only wants a market map or sizing: use a market research skill.
- The user wants a positioning or brand decision: use `business-strategist` or a brand skill.
- The user wants pure systems mapping of a large organisation: start with `system-thinking`, then return here for options and actions.
- The user wants copy, a financial model or a code fix: use the matching skill; this one is for the decision and the plan around it.
