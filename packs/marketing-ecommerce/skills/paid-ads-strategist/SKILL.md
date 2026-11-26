---
name: paid-ads-strategist
description: Plan paid advertising on any platform - campaign architecture (objectives, audiences, structure, test design), ad creative drafts (hooks, angles, formats, copy variants), media budget and scaling rules, and cut-hold-scale decision rules. Planning and drafting only: it never creates campaigns, connects ad accounts or spends money. Use for "plan my ads", "ad campaign structure", "write ad copy", "hooks for ads", "ad budget", "when to scale", "ads not converting", "CPA too high", "ROAS". Tiếng Việt - lập kế hoạch quảng cáo trả phí - cấu trúc chiến dịch, viết nháp nội dung quảng cáo, ngân sách và quy tắc nhân rộng, quy tắc cắt hay giữ hay tăng ("lên kế hoạch chạy ads", "viết quảng cáo", "ngân sách quảng cáo", "khi nào tăng ngân sách", "quảng cáo không ra đơn").
---

# Paid Ads Strategist

## What it does

It produces a plan an owner can approve and a person can execute: who to reach, with which objective, in what campaign structure, with which creative, on what budget, and by which rules to cut, hold or scale. The method is platform-neutral. Platform buttons and policies change often, so platform notes are short and flagged as "check current".

## Cost gate (read first)

This skill only plans and drafts. It never creates a campaign, connects an ad account, uploads creative to a platform or spends money. Every figure that implies spend (budgets, bids, caps, test costs) is a **proposal for the owner to approve**. Say so in the output and let the owner run it, or give an explicit go-ahead to someone who will.

## Brand context first

If the client keeps a `brand-profile.md` (name, positioning, audience, tone, products, limits), read it before anything else and do not re-ask what it answers. Take the **banned claims and limits** from it and apply them to every draft: no banned claim, no off-voice line, no excluded audience. If no profile exists, ask once for: what is sold and at what price, who buys, tone limits, and claims that must never be made. Offer to record the answers as a new draft profile, never overwriting an existing file.

## Pick the job from the request (do not list everything up front)

| The user says | Job |
|---|---|
| "plan the campaign", "which platform", "structure", "audiences" | **Architecture** |
| "write ads", "hooks", "creative brief", "variants" | **Creative** |
| "how much to spend", "budget", "scale", "when to cut" | **Media plan** |
| "ads not working", "CPA too high", "stopped converting" | **Diagnosis** (walk the chain below, then route to the job that fixes the broken link) |
| "full plan", "from scratch" | Architecture, then Creative, then Media plan |

Depth keywords the user may say: **express** (one question at most, deliver fast), **guided** (default: 3 to 5 intake questions, confirm approach, deliver), **deep** (full diagnosis, show reasoning, alternatives, a scaling roadmap). If the user names a framework, use it. If unclear which job is wanted, ask one routing question: "Plan the structure, draft the ads, or set the budget and rules?"

## Intake (guided mode, ask once, each question with a default)

1. What is sold, at what price, and what is the entry offer for strangers? (default: the cheapest way to start)
2. Gross margin and what a customer is worth over time? (default: first-order margin only, labelled as an assumption)
3. Do people already search for this, or must they be interrupted? (default: interrupt)
4. Existing assets: customer list, site traffic, social following, past winning ads? (default: none)
5. Target cost per result and monthly budget the owner is willing to consider? (default: derived below, as a proposal)

If a number is unknown, continue with a labelled assumption and list it under "Assumptions to confirm".

## Architecture

1. **Audience as a situation, not a demographic.** Describe who is in a moment of need (a trigger event, a pain, a deadline) and why they would act now. Demographics only narrow it afterwards.
2. **Awareness level** (Unaware, Problem Aware, Solution Aware, Product Aware, Most Aware). It sets how long the ad can be and what it must explain. Cold strangers are mostly the first three levels; people who visited or bought are the last two.
3. **Market sophistication.** If many rivals already make the obvious claim, a plain claim is invisible; the angle must change (mechanism, specific result, a new framing of the problem).
4. **Offer and ladder.** Cold traffic is sent to an entry offer matched to its temperature (free resource, trial, low-price starter, a call), not straight to the most expensive product. Name the next rung after the entry.
5. **Platform choice.** First split: intent (people searching) versus interruption (people scrolling) versus professional context. Start with 1 or 2 platforms; add one only after the first has a stable result. See the platform notes in the architecture file.
6. **Objective.** Choose the objective that matches the real outcome (purchase, qualified lead), because the platform optimizes for what the objective names. A click objective brings clickers, not buyers. If there is not enough conversion history, state the bridge step and when to switch.
7. **Structure.** Keep it small: one campaign per objective and temperature (prospecting, retargeting, existing customers), a few ad groups or ad sets per distinct audience, 3 to 5 ads per group. Keep tests and winners in separate places so a test never starves a proven ad. Detail in the architecture file.
8. **Measurement setup before launch.** List the events to track, the attribution window, a blended check (total revenue against total spend), and a way to count real sales or qualified leads outside the platform's own report.

## Creative

1. **Brief first.** Audience situation, awareness level, single promise, proof available (only what the brand profile or the owner can substantiate), offer, call to action, format and length limits, banned claims.
2. **Angles before words.** Produce 4 to 6 distinct angles (pain, desire, mechanism, proof, comparison, objection, story, myth-busting). Each angle gets 2 to 3 hooks. One angle per ad.
3. **Structure** by awareness: PAS (problem, agitate, solve) for Problem Aware; AIDA for Solution Aware; BAB (before, after, bridge) for story and transformation; hook, story, offer for video. Short and proof-led for Most Aware.
4. **Specific beats vague.** Replace "fast" and "better" with a number, a time or a concrete result, but only a true one that the owner can back. Never invent statistics, testimonials or scarcity.
5. **Variants for a test.** Change one element at a time (hook, then format, then offer wording). Label each variant by the hypothesis it tests.
6. **Formats.** Match format to awareness and placement: short video for cold attention, carousel for stepwise stories, static for proof and retargeting, text for search intent. Library and a creative checklist: see the creative file.
7. **Handoff when needed.** If longer copy or visual production is needed, write a handoff block any agent can read: platform and placement, audience and awareness level, offer, hook angle, tone and banned claims, length limits, required proof, call to action. Use `copywriter-skill` if installed for final copy; otherwise draft in place.

## Media plan and rules

1. **Start from economics.** Maximum acceptable cost per acquisition = value of a customer in the chosen window x the share the owner is willing to spend on acquisition. Budget = target number of customers x that cost. If the value is unknown, say that measuring it is the first project.
2. **Allocate.** Default split as a reference point: about 70% to proven, 20% to promising, 10% to experiments. In a new account, there is no "proven" yet, so reserve most of the initial budget for a time-boxed learning phase with a stated end.
3. **Test budget.** Each variant must be able to collect enough results to read, not only impressions. Set the minimum from target cost per result times the number of results needed (see the budget file for reference points). If the budget cannot fund the tests, test fewer things.
4. **Test order** (highest leverage first): offer, audience, hook, format, body copy, call to action.
5. **Decision rules (set before launch).** For each campaign define in advance: the metric, the minimum data, and the action. Cut, hold or scale tables are in the budget file. A decision made without the minimum data is a guess; write "hold" instead.
6. **Scale** vertically first (small, spaced budget steps on a winner), then horizontally (new audiences, angles, formats, platforms) when cost per result rises with extra spend. Track the cost of the incremental spend, not only the blended average.
7. **Fatigue.** Plan the next batch of creative before the current batch fades; a new hook is the cheapest refresh.

## Diagnosis: walk the chain from left to right

| Symptom | Where the break is | Fix first |
|---|---|---|
| Not spending or no impressions | Delivery: approval, audience too small, bid or budget too low | Setup check |
| Impressions but few clicks | Creative or audience mismatch | New hooks and angles |
| Clicks but few conversions | Landing page, message match, form friction, wrong traffic | Page review; use `cro-specialist` if installed |
| Conversions but unprofitable | Economics: price, margin, attribution, offer | Unit-economics review, offer rework |
| Good cost, cannot scale | Saturation or a bid ceiling | Horizontal scaling |
| Was fine, then declined | Fatigue, competitor, seasonality, tracking change | Check fatigue first, then external causes |

Diagnose before changing anything. Most "the ads are not working" cases turn out to be offer, page or tracking problems.

## Output rules

- Label every assumption and every reference point; tell the user to check them against their own market, margin and platform.
- A plan contains: summary, audience and offer, structure, creative angles and drafts, budget proposal with the economics behind it, decision rules, measurement setup, risks, and a concrete next step.
- End with one next step the owner can take (for example "approve the test budget of X and the stop rule, then I draft the final copy").
- Save as a NEW Google Doc or Sheet if a connection exists, otherwise reply in the conversation. Never overwrite an existing file. Never publish, send or spend anything without the user's go-ahead.
- Offer a diagram of the funnel or the test grid through the `visual-thinking` skill if installed, otherwise a plain-text table.

## Quality bar

1. Every budget figure traces to the economics step or is labelled a reference point.
2. Every campaign has a pre-set metric, minimum data and action (cut, hold, scale).
3. Objective and measured outcome match.
4. Every ad states its angle, awareness level and hypothesis; no ad claims anything the profile bans or the owner cannot support.
5. Tests change one variable at a time and have enough budget to be read.
6. No fake urgency, invented numbers or disguised ads; the user remains responsible for each platform's policy.
7. Vanity metrics (reach, likes) are never presented as success without a link to a business result.
8. Plain-language terms: explain platform jargon the first time it appears.

## Soft links (use if installed, otherwise do the step in place)

- `copywriter-skill`: final copy from the handoff block.
- `cro-specialist`: landing page problems found in diagnosis.
- `niche-finder`: if the audience or niche is still undecided, choose it first.
- `brand-architect`: voice constraints when no brand profile exists.

## When not to use

- Choosing which niche or market to enter: use `niche-finder` or a strategy skill first.
- Final long-form copy, scripts or emails: use a copywriting skill.
- Fixing a landing page or checkout in depth: use a conversion-optimization skill.
- Organic content, SEO or email programs: use the matching skills.
- Anything requiring actions inside an ad account: out of scope; this skill plans only.

## Reference files

- `references/architecture-and-platforms.md`: structure patterns, audience tiers, objective mapping, platform notes (flagged as changing).
- `references/creative-library.md`: angle and hook prompts, copy structures, format guide, creative checklist and diagnostic order.
- `references/budget-and-decision-rules.md`: economics formulas, allocation, test budgets, bidding progression, cut-hold-scale tables, fatigue and scaling.

This file is self-sufficient when the references are absent; the references add detail.
