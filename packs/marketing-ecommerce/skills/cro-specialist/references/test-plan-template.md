# Test plan template

One plan per test. All numbers in the example are invented. Reference points need checking against the user's own data.

```
# Test: [short name]

## 1. Hypothesis
Because we observed [evidence: data, recording count, survey wording],
we believe [one specific change]
will [directional effect]
for [segment],
because [mechanism, linked to a framework].

## 2. Metrics
Primary (one only): [metric, how counted]
Secondary: [supporting]
Guardrails (must not worsen): [revenue per visitor / lead quality / refund or complaint rate / page speed]

## 3. Design
Control: [description]
Variant(s): [description, screenshot or wireframe note]
Audience and eligibility: [who enters, devices, sources, exclusions]
Split: [50/50 unless reasoned otherwise]
Change is a single variable: yes / no (if no, call it a bundle test and accept less learning)

## 4. Size and duration
Baseline rate: [x percent from the last 4 to 8 weeks]
Minimum detectable effect worth acting on: [relative lift, and why that size matters in money]
Confidence / power: [95 percent / 80 percent as reference points]
Visitors needed per variant: [calculated]
Eligible visitors per week: [number]
Planned duration: [whole weeks, at least one full business cycle]
If longer than about 6 to 8 weeks: [bigger change / higher-funnel metric / direct implementation]

## 5. Stop rules (fixed before launch)
- Run until [sample] and [weeks], whichever is later.
- No early stop on significance.
- Early stop only for: [guardrail breach limit], [technical fault].
- No mid-test edits; edits mean restart.

## 6. Pre-launch checks
- Tracking verified on both arms, event counts sensible in a short soak.
- Variant renders on main devices and browsers.
- Sample ratio monitor in place.
- No overlapping test on the same audience, or overlap is accepted and noted.
- Known disturbances in the window (promotions, holidays, pay cycles) listed.

## 7. Decision rules
- Ship if: [primary lift interval clearly above zero, guardrails fine].
- Keep control if: [interval spans zero or guardrail harmed].
- Iterate if: [segment pattern suggests a follow-up, to be tested as a new hypothesis].

## 8. Results log (fill after the test)
Sample reached, dates, sample ratio check, lift with interval, guardrails, segment notes, decision, learning, next hypothesis.
```

## Priority scorecards

**PIE** (1 to 10 each, average): potential (how bad is it now), importance (traffic volume and cost), ease (technical and political).

**PXL-style** (yes = 1, selected criteria weigh 2): above the fold; noticeable in five seconds (2); adds or removes an element rather than tweaking one (2); aims to raise motivation; on a high-traffic page; backed by user testing; backed by survey or support evidence; backed by analytics; backed by behaviour-tool data; easy to build. Ideas with no evidence score near zero by design.

**ICE** (1 to 10 each): impact, confidence, ease. Use for a short list; confidence must cite evidence.

Pick one method per backlog and stay with it. Re-score each quarter.

## Hypothesis quality checklist

| Check | Fails when |
|---|---|
| Evidence-backed | The observation is anecdote or opinion |
| Specific treatment | A designer could not build it without a question ("improve the headline") |
| Single variable | Several changes are bundled and unlabelled |
| Measurable outcome | Success is "feels better" |
| Mechanism named | "Because we think it is better" |
| Segment defined | "Everyone" with no segmentation reasoning |
| Guardrail set | Nothing is protected from harm |
| Prioritised | Chosen by recency or loudest voice |

Minimum to run: evidence, specific treatment, measurable primary metric, at least one guardrail.
