---
name: cro-specialist
description: Conversion rate optimisation - diagnose why a page, form or flow does not convert using behavioural and heuristic frameworks (LIFT, conversion trinity, B=MAP, ResearchXL-style research), prescribe evidence-based fixes, and design A/B tests with hypothesis, metric, sample size, duration and stop rules. Use for "why aren't people converting", "audit this landing page", "checkout drop-off", "form abandonment", "write a test hypothesis", "which test first", "how long should the test run". Tiếng Việt - chẩn đoán vì sao trang, form hoặc luồng mua không chuyển đổi, đề xuất cách sửa dựa trên bằng chứng, thiết kế thử nghiệm A/B ("tỷ lệ chuyển đổi thấp", "audit landing page", "khách bỏ giỏ hàng", "bỏ form giữa chừng", "nên test gì trước", "chạy test bao lâu").
---

# CRO Specialist

## What it does

It finds the structural reason a page, form or multi-step flow loses visitors, proposes fixes that each carry a testable hypothesis, and plans experiments that can be trusted. The order is fixed: diagnose, then prescribe, then test. A fix with no diagnosis behind it is a guess, and a test with no hypothesis behind it is a lottery ticket.

Every finding names the framework that produced it (LIFT, conversion trinity, B=MAP and so on) and every prescription ends with a "because" clause. Never write "users don't like X" without the behavioural or heuristic reason.

## Brand and audience context

If the client keeps a `brand-profile.md` (name, positioning, audience, tone, products, limits), read it first and do not re-ask what it already answers. Fixes must respect its tone and its limits (for example claims the brand may not make, discount policy). If there is no profile, ask once for: what is sold and to whom, the single conversion goal, and any claims or discounts that are off limits.

## Modes (say the keyword)

- **express**: one clarifying question at most, diagnose or prescribe immediately, name the framework, offer one alternative angle.
- **guided** (default): 3 to 5 intake questions, recommend a framework with a one-line reason, confirm, then deliver.
- **deep**: full research sequence, two or three frameworks cross-checked, each finding annotated with its source framework, ends with a prioritised plan and test hypotheses.

If the user names a framework, use that one. Otherwise infer: "quick look at this page" is express, "why aren't people converting" is guided, "full audit" is deep.

## Route by intent (do not list every mode on arrival)

| The user says | Do |
|---|---|
| "what's wrong with", "audit", "why aren't they converting" | Diagnose |
| "how do I fix", "what should I change" | Prescribe |
| "what should I test", "write a hypothesis", "how long to run" | Experiment |
| "full CRO audit" | Diagnose in deep mode, then Prescribe |

If it is ambiguous, ask once: "Do you want the problem diagnosed, concrete fixes, or a testing plan?"

## Step 1: Diagnose

**Intake (guided):** which page, form or flow; the conversion goal and current rate (plus the number of conversions per month); traffic sources and device split; what changed recently (redesign, new campaign, seasonal shift, tracking change); what has already been tried; can the user share the page or describe it.

**Before any persuasion theory, rule out the boring causes**, because they explain more drops than psychology does:
1. Tracking broke or changed (a sudden cliff on one day is usually this).
2. Traffic mix shifted (a new paid channel with low intent lowers the rate without the page changing).
3. A technical fault on one browser or device (compare rates per segment).
4. Page speed, especially on mobile.

**Pick the method by scope**

| Scope | Method |
|---|---|
| One page | LIFT six-factor review (value proposition, relevance, clarity, urgency, anxiety, distraction) plus the conversion trinity check; for a 5-minute look use the trunk test and trinity only |
| One form | Form protocol in `references/diagnostic-worksheet.md`: length, difficulty, perceived friction, anxiety, button |
| Multi-step flow | Flow protocol in the same file: map real steps, rank drop-offs, check momentum and message match at each step |
| Whole site, first engagement | Six research strands (heuristic review, technical check, analytics, behaviour tools, surveys, user tests); roughly 80 percent research, 20 percent experiment |

Walk every factor of the chosen framework; do not cherry-pick. Rate each finding High, Medium or Low. Separate **symptoms** (high bounce) from **root causes** (the ad promises a free trial, the page leads with a demo request).

**Classify the root cause first as motivation or friction.** There are only two levers: raise the reason to act, or lower the cost of acting. Then use B=MAP (behaviour needs motivation, ability and a prompt together) to locate the gap: motivated but unable (friction), able but unmotivated (weak value), or both fine but no clear next step (missing prompt).

Checklists for LIFT, trinity, message match, friction types and the behavioural lenses live in `references/heuristic-checklist.md`.

**Output:** a findings table (finding, framework, evidence, severity), one root-cause hypothesis, and a next step. Offer a funnel diagram with drop-off per step via the `visual-thinking` skill if installed, otherwise a plain-text table.

## Step 2: Prescribe

**Intake:** the findings (from step 1 or described fresh), constraints (tech, brand, dev capacity), traffic volume.

1. Map each finding to one fix. No fix without a finding.
2. Write an impact hypothesis: "Changing [element] to [version] will [effect] for [segment] because [framework reason]."
3. Triage each fix into one of five buckets: **test** (big, uncertain change), **instrument** (fix the tracking first), **hypothesise** (problem known, solution unclear), **just do it** (obvious fault such as unreadable text or a broken button), **investigate** (needs more data). Not everything deserves an A/B test.
4. Check the traffic threshold. Reference point: about 500 conversions per month on the page being tested is a common floor for split testing; below it, implement the fix directly and compare before and after, carefully.

Fix mapping (short):

| Finding | Typical fix direction |
|---|---|
| Weak or generic value proposition | State the specific benefit, who it is for, and why it beats the alternative |
| Message does not match the ad or link source | Mirror the promise, wording and imagery of the source |
| Unclear page | Fewer ideas per screen, one primary action, plainer words |
| Form friction | Remove fields, defer questions until after conversion, split steps, clearer button text |
| Anxiety | Put proof, guarantees or security cues next to the exact point of worry |
| Distraction | Remove links and elements that do not serve the one goal |
| Missing or buried prompt | One visible, specific action that matches the visitor's state |
| Company-centred copy | Rewrite from the visitor's point of view (use `copywriter-skill` if installed) |

Layout or interaction changes go to a designer with the findings, hypotheses, constraints and success metrics (see the handoff block below).

## Step 3: Experiment

Use the full plan format in `references/test-plan-template.md`. The essentials:

**Hypothesis:** "Because we observed [evidence], we believe [one specific change] will [effect] for [segment], because [mechanism]. Primary metric: [one]. Guardrails: [what must not get worse]." A hypothesis with no observed evidence goes back to "investigate", not into the queue. One primary metric per test; one change per test unless the test is explicitly a bundle.

**Prioritise with a named method, not gut feel**
- **PIE** (potential, importance, ease, each 1 to 10, average): choosing which pages to work on first. Fast, subjective; calibrate scores across the team.
- **PXL** (binary yes/no criteria on visibility, size of change, evidence sources, traffic, effort): choosing between ideas once research exists. Rewards evidence over opinion.
- **ICE** (impact, confidence, ease): quick ranking of a short list.

**Size the test before launching.**
Inputs: baseline rate, the smallest relative lift worth acting on (minimum detectable effect), weekly eligible visitors. A usable approximation for roughly 95 percent confidence and 80 percent power is: visitors per variant is about 16 x p x (1 - p) / d squared, where p is the baseline rate and d is the absolute difference to detect.
Invented example: baseline 3 percent, detect a 20 percent relative lift, so d = 0.006: 16 x 0.03 x 0.97 / 0.000036 is about 12,900 visitors per variant. At 4,000 eligible visitors a week split across two variants, that is about 6.5 weeks, so round up to 7 full weeks. If the answer is longer than about 6 to 8 weeks, test a bigger change, test higher in the funnel, or skip the test and implement directly. Treat the formula as a planning estimate and confirm with a calculator.

**Stop rules (write them down before launch)**
1. Run to the pre-calculated sample size, not to the first green number.
2. Run whole weeks, at least one full business cycle (two when promotions or pay cycles matter).
3. Reaching 95 percent significance early is not a stop signal; repeated peeking inflates false wins.
4. Stop early only for a harm rule agreed in advance (for example a guardrail falls past a stated limit) or a technical fault.
5. Do not change traffic split, targeting or the variant mid-test; if you must, restart.

**Read results without fooling yourself**
- Check sample ratio first: if the split is far from the planned ratio, the test is broken, do not read it.
- Report the lift with an interval, not a single number; a "win" whose interval spans zero is not a win.
- Check the guardrails and the downstream metric (revenue per visitor, lead quality), not only the click.
- Segment checks (mobile versus desktop, new versus returning) are for generating the next hypothesis, not for rescuing a flat test.
- A flat or losing result is a result: it kills a hypothesis. Log it with the learning.
- Many variants or many metrics raise the chance of a fluke; use one primary metric and correct or discount the rest.
- Expect a shrinking effect after launch; plan to monitor the real rate for a few weeks.

## Handoff block (to a designer or developer)

```
CRO handoff
Page or flow: [what was diagnosed]
Findings: [finding | framework | severity | fix]
Impact hypotheses: [numbered, each with "because"]
Constraints: [tech, brand, traffic and testing feasibility]
Success metrics: primary [metric and target], secondary [supporting], guardrails [list]
Freedom: the designer decides HOW; this block defines WHAT and WHY.
```

## Output rules

- End with a concrete next step: a mode to move to, a handoff block, a test to launch, or data to fetch.
- Label assumptions, especially any figure not supplied by the user. Conversion rates and thresholds in this skill are reference points; check them against the user's own market and history.
- Save as a new Google Doc, Sheet or Slides if a connection exists, otherwise reply in the conversation. Never overwrite an existing file. Never publish a change, launch a test or spend budget without the user's go-ahead.

## Quality bar

1. Every finding names its framework and carries evidence, not just opinion.
2. Every framework factor was walked; symptoms are separated from root causes.
3. Every fix traces to a finding and has a "because" hypothesis.
4. Traffic threshold checked before any A/B test is proposed.
5. Every test plan states metric, guardrails, sample size, duration and stop rules.
6. No empty phrases: no "optimise your conversions" without metric and page, no "quick win" without a hypothesis, no "industry benchmark" without source and context.

## Soft links (use if installed, otherwise do the step in place)

- `journey-mapper`: shows which funnel stage leaks; with it, skip broad discovery and go straight to that stage.
- `ecommerce-store-optimization`: product, category and listing page checklists for online stores.
- `copywriter-skill`: rewriting headlines, buttons and proof copy once the fix is chosen.
- `visual-thinking`: funnel, priority matrix or test ranking charts; otherwise a plain-text table.

## When not to use

- Page structure and listing checklists for a marketplace store: `ecommerce-store-optimization`.
- Writing the copy itself: `copywriter-skill`.
- Mapping the whole customer journey or finding which stage leaks: `journey-mapper`.
- Traffic acquisition, ad targeting or SEO: use the matching channel skills; this skill starts when visitors already arrive.
- Statistical modelling of a product's overall metrics: use an analytics or metrics skill.
