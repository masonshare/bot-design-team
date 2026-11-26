---
name: journey-mapper
description: Map the full customer journey from stranger to advocate, find where customers leak out, and route each fix to the right specialist with a readable handoff block. Three modes picked from the request - lifecycle mapper (stages, touchpoints, moments of truth, gaps), leak finder (stage metrics, friction type, 5 whys, revenue impact, ICE ranking), routing (leak to skill, week-by-week sequence, re-diagnosis checkpoint). Use for "map my customer journey", "funnel audit", "where am I losing customers", "conversion leak", "drop-off", "touchpoint gaps", "who should fix this". Tiếng Việt - vẽ hành trình khách hàng từ người lạ đến người giới thiệu, tìm điểm rơi rụng, xếp thứ tự sửa và giao việc cho đúng skill chuyên môn ("vẽ hành trình khách hàng", "kiểm tra phễu", "mất khách ở đâu", "tỷ lệ chuyển đổi thấp").
---

# Journey Mapper

## What it does

Single channels do not convert; journeys do. A strong email sequence fails if the landing page leaks, and a clean product flow fails if nobody ever gets onboarded. This skill looks at the whole lifecycle first, then diagnoses, then hands fixes to specialists instead of rebuilding their work. Order of work: map, diagnose, route, measure again.

If the client keeps a `brand-profile.md` (name, positioning, audience, tone, products, limits), read it first and do not re-ask what it answers. Otherwise ask once for the business, the offer and the audience.

## Choose the mode from the request

| The user says | Mode |
|---|---|
| "map the journey", "touchpoints", "how do customers move", describes a business with no data | **Lifecycle mapper** |
| "where am I losing people", "funnel audit", "conversion problem", pastes stage numbers | **Leak finder** |
| "who fixes this", "hand off", "plan the fixes", approves a diagnosis | **Routing** |

Depth keywords the user may say: **express** (at most one question, short output), **guided** (default: 3 to 5 intake questions, confirm approach, full output), **deep** (full intake, show reasoning, alternatives, re-diagnosis plan). A clear narrow ask is express, a broad one is guided, "full audit" is deep. If the user names a framework, use it. Start each output with one line: mode, journey type, depth. End with a next step: after mapping suggest diagnosing, after diagnosing suggest routing, after routing set the re-diagnosis date.

Templates for the three outputs are in `assets/output-templates.md`. Use them.

## Mode 1: Lifecycle mapper

**1. Detect the journey type.** Pick one, ask if unclear:
- **B2C direct**: one-off purchase, short cycle, impulse and comparison driven.
- **B2C subscription**: trial or first month, then habit and renewal; the early activation window decides everything.
- **B2B transactional**: a single buyer, a few days to weeks, price and proof matter most.
- **B2B enterprise**: many stakeholders, long cycle, a champion who must sell internally.
- **Creator or course**: audience first, lead magnet, nurture, launch window, then ascension to the next offer.

**2. Map the stages (AARRR style).** Use awareness, acquisition, activation, retention, revenue, referral; reorder for the type (a subscription puts retention before most revenue, a course puts revenue after a nurture phase). For each stage record:
- **Core question** the customer is asking at that point.
- **Channels** where it happens.
- **Touchpoints**: the concrete assets and screens they meet.
- **Transition trigger**: the event that moves them to the next stage.
- **Exit risk**: why they would leave here.

**3. Mark 3 to 5 moments of truth.** Use the four classic moments: before the search (ZMOT, what they find when they research), the first impression of the offer (FMOT), the first use (SMOT), and the story they tell afterwards (UMOT). For each one name the touchpoint, what is at stake and what currently protects it.

**4. Find gaps.** Flag three things: a stage with no touchpoint, a moment of truth with no owner, a transition with no trigger (the customer must guess the next step). Rate each gap high, medium or low by how much revenue sits behind it.

Offer a diagram via the `visual-thinking` skill if installed (an emotion-by-stage journey or a flowchart with the moments marked), otherwise give a plain-text table.

## Mode 2: Leak finder

**1. Collect stage metrics.** For each stage get volume and conversion to the next, over a stated period. If numbers are missing, ask for the three or four that matter most, or run on clearly labelled assumptions. Useful probes: where in the first week do people stop, do people who do one specific action convert more, what share arrive from each channel, what share of buyers buy again.

**2. Compare with reference points.** Rate each stage green (at or above), yellow (below), red (far below). The ranges below are reference points without a source; they vary a lot by industry, price, traffic quality and company stage, so check them against the client's own history first.

| Transition | Reference point (rough) |
|---|---|
| Visitor to lead or sign-up | roughly 1 to 5 percent, higher for warm traffic |
| Sign-up to activated | roughly 20 to 60 percent depending on how hard activation is |
| Trial to paid | roughly 2 to 10 percent for self-serve, more with sales help |
| Monthly subscriber churn | roughly 3 to 8 percent consumer, 1 to 3 percent B2B |
| Buyers who buy again within a year | roughly 20 to 40 percent for repeatable products |

Own trend over time beats any external number: a stage that fell 30 percent in two months is a leak whatever the benchmark says.

**3. Find the drop-offs.** Compute stage-to-stage conversion. Flag any transition where more than half leave, and any transition that is the weakest relative to its reference point. Count how many people that is per period. This is the leaky bucket view: fix the biggest hole nearest the customer's first value before polishing the top.

**4. Classify the friction.** For each major leak choose the main type, using the behaviour model (a person acts when motivation, ability and a trigger meet):
- **Motivation**: they do not care enough yet (weak promise, wrong audience).
- **Ability**: they want it but it is too hard (long form, confusing setup, price shock).
- **Trigger**: nothing prompts the next step (no reminder, no clear call to action).
- **Trust**: they doubt you (no proof, unclear policy, inconsistent voice).
- **Value**: they tried it and did not see the payoff (late or missing first win).

Test the guess against evidence: session recordings, support tickets, survey answers, drop point in the flow. Say which evidence you have and which you lack.

**5. Run 5 whys.** Ask why up to five times until you reach something a team can change (a page, a sequence, an offer, a policy). Stop earlier if the answer is already actionable. Record the root cause in one sentence.

**6. Quantify the revenue impact.** Estimated gain per period = people lost at the stage x realistic recovery rate x downstream conversion to paid x average order value (or lifetime value for subscriptions). Use a modest recovery rate (for example recovering a tenth to a third of the loss) and show the formula with the inputs, so the client can adjust. Mark every input as measured or assumed.

**7. Prioritise with ICE.** Score each candidate fix on impact, confidence and ease, 1 to 10 each, multiply, rank. Confidence is high only when evidence supports the root cause. Call out quick wins (high ease, medium or better impact) that can ship this week.

Offer a diagram via the `visual-thinking` skill if installed (a shrinking funnel, or an impact-versus-ease quadrant), otherwise a plain-text table.

## Mode 3: Routing

**1. Match each leak to a specialist.** Use the friction type and the stage.

| Leak is mostly | Specialist skill (use if installed) |
|---|---|
| Trust, inconsistent voice or positioning | a brand skill, such as `brand-architect` |
| Weak discovery or content gap at awareness | an SEO content skill |
| Email or nurture drop-off, missing trigger | an email skill |
| Weak message, headline or call to action | a copywriting skill |
| Weak opt-in or lead magnet | a lead-generation skill |
| Offer, pricing or unit economics mismatch (value friction) | a strategy skill, such as `stp-marketing-strategy` |
| Confusing flow, onboarding or checkout (ability friction) | a UX skill |

If the matching skill is not installed, do the fix design in place at a lighter depth and say so.

**2. Check dependencies.** Some fixes must come first: voice before copy, offer before landing page, tracking before any test. Draw the dependency list explicitly.

**3. Write one handoff block per fix.** The block must be readable by any agent or person with no other context. Use the format in `assets/output-templates.md`: journey context (stage transition, drop-off, friction type, root cause, upstream and downstream), brand context, constraints the fix must meet, the deliverable requested, and how it connects (entry and exit points). Give the receiving side creative freedom inside those constraints.

**4. Sequence week by week.** Weeks follow dependencies and ICE rank; parallelise fixes that do not touch each other; keep each week to what the team can actually ship. Define one success metric per fix and the date to check it.

**5. Set the re-diagnosis checkpoint.** After the fixes have had enough traffic to judge (state the minimum sample or period), rerun the leak finder, compare with the baseline, and record what changed and what leaks remain.

## Output rules

- Label every assumption; say which numbers are measured and which are guesses.
- End with a concrete next step.
- Save as a NEW Google Doc or Sheet if a connection exists, otherwise reply in the conversation. Never overwrite an existing file.
- Never send, publish, spend money or change anything outside the conversation without the user's go-ahead.
- Ban vague advice: "improve retention" or "optimise the funnel" without a stage, a friction type and a named fix.

## Quality bar

- The journey type is named and fits one of the five.
- Every stage has a core question, a transition trigger and an exit risk; moments of truth are placed.
- Every leak has a number, a friction type, a root cause and an estimated impact with the formula visible.
- Benchmarks are marked as reference points that vary by industry and stage.
- Every fix traces back to a diagnosed leak, and every handoff block stands alone.
- The plan has dependencies, weeks, owners or skills, and a re-diagnosis date.

## When not to use

- Building the actual email sequence, page, content plan or ads: use the matching specialist skill after routing.
- Choosing the market, positioning or target segment: use a strategy skill such as `stp-marketing-strategy` first.
- Deep store-level conversion work on a marketplace or shop: use the e-commerce optimisation skills if installed.
- Pure metric definition and dashboards: use a KPI or metrics skill.
