# Output templates

Three templates, one per mode. Fill them with the client's data. All names and numbers in the examples are invented. Mark every assumption.

---

## Template 1: Journey map

```
# Journey map: <business or offer>

Mode: lifecycle mapper | Journey type: <type> | Depth: <express/guided/deep>

## Overview
| Item | Value |
|---|---|
| Journey type | B2C direct / B2C subscription / B2B transactional / B2B enterprise / creator-course |
| Primary goal | <the conversion that matters> |
| Typical cycle length | <time from first contact to purchase> |
| Main channels | <list> |

## Stage map
### Stage <n>: <name>
| Item | Detail |
|---|---|
| Core question | <what the customer is asking now> |
| Channels | <where it happens> |
| Touchpoints | <concrete assets, pages, messages> |
| Transition trigger | <event that moves them on> |
| Exit risk | <why they leave here> |
(repeat for every stage)

## Moments of truth
| Moment | Stage | Touchpoint | At stake | Current protection |
|---|---|---|---|---|
| Before search (ZMOT) | | | | |
| First impression (FMOT) | | | | |
| First use (SMOT) | | | | |
| Story afterwards (UMOT) | | | | |

## Gaps
| Gap | Stage | Effect on conversion | Priority |
|---|---|---|---|
| <missing touchpoint, owner or trigger> | | | High / Medium / Low |

## Diagram (optional)
Via the `visual-thinking` skill if installed, otherwise this text flow:
Awareness -> Acquisition -> Activation -> Retention -> Revenue -> Referral (mark moments of truth with *)

## Assumptions
- <label each>

## Next step
Run the leak finder on the stages with the weakest transitions.
```

Invented example row: Stage "Activation" for a fictional meal-kit brand "Lumen Table": core question "Will this be easy on a weeknight?", touchpoint "first-box unboxing card", trigger "first recipe cooked", exit risk "box sits unopened for four days".

---

## Template 2: Diagnostic report

```
# Journey diagnostic report: <business>

Mode: leak finder | Period analysed: <dates> | Depth: <depth>

## Summary
<2 to 3 sentences: biggest leaks and estimated impact per period>

## Funnel health
| Stage | Volume | Conversion to next | Reference point | Status | Lost per period |
|---|---|---|---|---|---|
| Awareness | | | | green/yellow/red | |
| Acquisition | | | | | |
| Activation | | | | | |
| Retention | | | | | |
| Revenue | | | | | |
| Referral | | | | | |
Reference points are rough and vary by industry and stage. Own history comes first.

## Leak <n>: <stage> to <stage>
| Item | Finding |
|---|---|
| Drop-off | <percent and people per period> |
| Friction type | motivation / ability / trigger / trust / value |
| Evidence | <recordings, tickets, survey, flow data; say what is missing> |
| 5 whys | 1. ... 2. ... 3. ... -> root cause |
| Root cause | <one sentence a team can act on> |
| Revenue impact | people lost x recovery rate x downstream conversion x order value = <amount>; inputs marked measured or assumed |

## ICE ranking
| Rank | Fix | Impact | Confidence | Ease | Score | Quick win? |
|---|---|---|---|---|---|---|
| 1 | | /10 | /10 | /10 | | |

## Quick wins this week
- [ ] <item>

## Next step
Run routing for the top ranked fixes.
```

---

## Template 3: Routing package

```
# Routing package: <business>

Mode: routing

## Summary
| Fix | Specialist skill | Rank | Depends on | Success metric | Check date |
|---|---|---|---|---|---|
| <fix 1> | <skill or "in place"> | 1 | none | | |
| <fix 2> | | 2 | fix 1 | | |

## Handoff block <n>: <specialist skill>
Paste this block into any agent or send it to any person. It needs no other context.

~~~
HANDOFF
Task for: <specialist skill or role>. If that skill is not installed, do the task directly.

Journey context
- Stage transition: <stage> to <stage>
- Drop-off: <percent and people per period>
- Friction type: <type>
- Root cause: <one sentence>
- Before this point: <what the customer has just done>
- After this point: <what should happen next>

Brand context
- Read the client's brand profile if one exists. Otherwise: <offer, audience, tone, limits in two lines>

Constraints
- <the fix must ...>
- <the fix must not ...>

Deliverable requested
- <specific output, format, length>

Connections
- Entry point: <how people arrive>
- Exit point: <where they go next>
- Success metric and check date: <metric, date>

Rules: label assumptions; do not publish, send or spend anything without the owner's approval.
~~~
(repeat per fix)

## Implementation sequence
| Week | Work | Why now | Dependency |
|---|---|---|---|
| 1 | <fix> | no dependency, highest ICE | none |
| 2 | <fix> | needs week 1 output | fix 1 |
| 3 | <fix> | builds on both | fixes 1, 2 |

## Re-diagnosis checkpoint
Date: <date>. Minimum sample or period before judging: <number>. Compare against the baseline in the diagnostic report, list what improved, what did not, and which new leaks appear.

## Next step
<one concrete action for the owner this week>
```
