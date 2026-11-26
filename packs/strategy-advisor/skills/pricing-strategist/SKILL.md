---
name: pricing-strategist
description: Decide what to charge - compares value-based, cost-plus and competitor-based pricing, checks the unit-economics floor, designs tiers, discounts and price increases, and plans a price test with stop rules. Output is a pricing recommendation memo. Use when the user asks "what should we charge", "should we raise prices", "design pricing tiers", "how much will customers pay", "is our discount policy OK", "price test". Tiếng Việt - định giá sản phẩm hoặc dịch vụ, so sánh định giá theo giá trị, theo chi phí, theo đối thủ, thiết kế gói giá, chính sách giảm giá, kế hoạch tăng giá, thử nghiệm giá ("nên bán giá bao nhiêu", "có nên tăng giá", "chia gói giá", "khách chịu trả bao nhiêu").
---

# Pricing Strategist

## What it solves

Most prices are set by copying a competitor or adding a margin to cost. Both ignore what the product is worth to the buyer and what the business needs to survive. This skill sets a price from three sides at once: the floor (what the business needs), the ceiling (what the buyer will pay), and the reference points in between (what alternatives cost). It ends with a memo and a small, safe test, not a leap of faith.

## Keywords for modes

Say a word to pick a mode (no slash commands):
- **express**: one round of at most 3 questions, then a short memo.
- **guided** (default): the full intake below, then the memo.
- **deep**: adds a research plan for willingness to pay and a modelled scenario table.

If the user names a framework (for example a price-sensitivity survey or Jobs-to-be-Done), use it.

## Brand context

If the client keeps a `brand-profile.md` (positioning, audience, tone, products, limits), read it first and do not re-ask what it answers. Positioning decides how much premium is believable. If there is no profile, ask once for positioning in one sentence.

## When to use

- A new product or service needs a first price.
- Prices have not changed for a long time, or margins look thin.
- A price increase, a new tier, a bundle or a discount policy is on the table.
- The team is arguing about price with no shared method.

## Intake (ask once, each question with a default the user can accept)

1. **Product and model**: what is sold and how (one-off, subscription, usage, hybrid)? Default: as described.
2. **Cost structure**: variable cost per unit (materials, fulfilment, payment fees, support), fixed monthly costs, and any acquisition cost per customer. Say "unknown" if unknown.
3. **Customers**: who buys, what job they hire the product for, what they use today, how often they buy.
4. **Competitors and substitutes**: names or types, their visible prices, and what they include.
5. **Current price and volume**: price, units or customers per month, conversion rate if known. Default for a new product: none.
6. **Goal and limit**: more profit, more volume, or a premium image? Any price the brand will never go below or above?

Numbers the user did not give are **labelled assumptions** or **reference points** in the memo. Never present an invented market figure as fact; ask the user to check reference points against their own market.

## Workflow

1. **Frame the job and the value.** State what the buyer is trying to get done (functional, emotional, social). Estimate the full cost of the buyer's current way of doing it: money, time, risk, frustration. That total is the value ceiling to test; the product's price should sit well under the value it delivers.
2. **Compute the floor.** Use the unit-economics section below. No price under the floor is recommended unless the user states a deliberate loss-leader reason and a cap on the loss.
3. **Collect reference prices.** List 3 to 6 alternatives with price and what is included. Compare on a like-for-like unit (per use, per month, per outcome).
4. **Compare the three methods** and show them side by side:
   - **Cost-plus**: cost plus a target margin. Simple, safe, but ignores value; leaves money behind when value is high, and loses when the market is cheaper.
   - **Competitor-based**: anchored to rivals. Good as a sanity check and for commodity goods; weak when the product is different, because rivals may be wrong.
   - **Value-based**: anchored to the buyer's gain. Strongest when the product clearly beats alternatives and the gain can be shown; needs evidence of willingness to pay.
   Default recommendation: value-based inside the band set by the floor and the reference prices.
5. **Estimate willingness to pay** with the cheapest method that fits (next section). Do not guess it from inside the team.
6. **Design the offer structure**: single price or tiers, fences, anchors, discount rules.
7. **Model the effect** for 2 or 3 options (price, expected volume, contribution). Label every assumption.
8. **Design the test** with stop rules, then write the memo.

## Willingness-to-pay research (pick by situation)

| Situation | Method | Notes |
|---|---|---|
| No traffic yet, early idea | 5 to 10 buyer interviews about the job and the current spend | Ask what they pay today and what a bad outcome costs; avoid "would you buy at X" |
| New product, want a price band | Four-question price-sensitivity survey (Van Westendorp style): too cheap, a bargain, getting expensive, too expensive | Randomise question order; segment results; it gives a range, not a demand curve |
| Existing product, want demand at several prices | Step-by-step accept/reject at rising prices (Gabor-Granger style) | Shows the drop-off point; stated intent overstates real buying |
| Features versus price trade-offs | Conjoint-style choice tasks | Heavier; only when the decision is large |
| Live traffic | Controlled price experiment | Best evidence; follow the test rules below |

Rules: ask about a specific segment and context, never "the market" in general. Stated answers run higher than real behaviour, so treat survey results as a range to test, and always confirm in the real market. Small samples are directional; say so. Detail and a survey script: `references/wtp-methods.md`.

## Elasticity in one paragraph

Elasticity is the percentage change in volume divided by the percentage change in price. If volume falls less than price rises, a rise lifts revenue; if more, it hurts. Many substitutes, low switching cost and big share of budget push demand toward elastic; few substitutes, high switching cost and strong brand push toward inelastic. Estimate it per segment from past price changes or tests; do not assume.

## Unit-economics floor

- **Contribution margin per unit** = price minus variable cost per unit (include payment fees, shipping, packaging, support, returns allowance).
- **Contribution margin %** = contribution per unit divided by price.
- **Break-even volume** = fixed costs for the period divided by contribution per unit.
- **Price needed for a target volume** = variable cost plus fixed costs divided by that volume, plus the margin wanted.
- **Subscriptions**: also check customer lifetime value against acquisition cost and the payback period. Reference point: lifetime value several times acquisition cost and payback within about a year are common targets; check against the user's own market and cash position.
- **Discount test**: a discount of d% on a product with contribution margin m% needs volume to rise by d / (m - d) to keep the same total contribution. Show this number whenever a discount is proposed.

Use `startup-metrics-framework` and `startup-financial-modeling` for deeper metric or model work if installed; otherwise do the arithmetic here.

## Tiers and packaging

- **Good / better / best**: two to four tiers is usual. Differences must map to real segments or jobs, not to arbitrary feature removal.
- **Anchor**: show the top option first or visually, so the target tier looks reasonable next to it. The anchor must be a real offer, never a fake "original price".
- **Decoy**: a tier that exists mainly to make the target tier look better. Use sparingly and honestly; a decoy nobody ever buys is a signal to redesign.
- **Fences**: rules that keep high-value buyers from buying the cheap tier (usage caps, support level, licences, speed, commitment length). A tier without a fence invites everyone to the bottom.
- **Value metric**: charge on what grows with the customer's gain (seats, orders, volume), not on something unrelated.
- **Charm and round prices**: test them; round prices signal premium, "9" endings signal value.
- For a promotion calendar or voucher mechanics, use `ecommerce-promotion-design` if installed; otherwise follow the discount rules below.

## Discount policy

- Discount only with a reason and an end: clearing stock, acquiring a segment, rewarding a commitment (longer term, larger basket).
- Prefer adding value (bonus, service, bundle) over cutting price; it protects the reference price.
- Set a floor per product (never below the unit-economics floor) and a maximum depth per channel.
- Do not discount when: demand already exceeds supply, the product is new and the price is still being learned, the buyer base is loyal and price-insensitive, margins are thin, or past discounts already trained buyers to wait.
- Track the share of sales on discount; if it keeps rising, the list price is no longer believed.

## Price increase planning

1. Confirm the case: costs rose, value rose, or demand is inelastic (low churn, no complaints, strong demand).
2. Choose the size: small steps are easier than one jump; test with a segment or new customers first.
3. Choose the protection: grandfather loyal customers for a period, offer a locked-in term, or add visible value alongside the rise.
4. Communicate: give notice (reference point: 30 to 60 days for subscriptions, check contracts), explain the reason in plain terms, state what stays the same, offer a way to keep the old price by committing longer.
5. Watch the metrics for two billing cycles: conversion, churn, downgrades, support tickets, revenue per customer.

### Always include a draft customer message and a numeric stop rule
When the recommendation includes a price increase, write a short draft message the owner can edit: what changes and from when, the reason in plain words, what stays the same, and the option to keep the old price. Write the stop rule with a number the owner can check, for example "if monthly cancellations in the tested group exceed the control by more than a margin we agree now, pause and revert". The margin is theirs to set; give a reference point and say it is only that. For a small customer base, say the test will be weakly powered and prefer a staged rollout over a split test.

## Test design and stop rules

Define before launch, in writing:
- **Hypothesis**: "At price B, revenue per visitor rises at least X% versus price A, with conversion not falling more than Y points."
- **Unit and split**: random split of new visitors or new customers; never charge two prices to the same person at the same time if they can compare.
- **Primary metric**: revenue per visitor or contribution per visitor, not conversion alone. Guardrails: refunds, churn, support load, brand complaints.
- **Duration and sample**: run full weekly cycles; fix the sample or duration in advance and do not stop early on a good-looking day. If traffic is too small for a clean test, use sequential periods or a limited rollout and say the evidence is weak.
- **Stop rules**: stop and revert if a guardrail breaks by the agreed margin (for example conversion drops far below the limit set), if the price turns out to be under the floor, or if customers react publicly in a way that harms trust. Stop and adopt only when the pre-set sample is reached and the primary metric clears the pre-set bar.
- **Ethics**: no deceptive anchors, no hidden personal price discrimination, honour the price the customer saw.

## Output: pricing recommendation memo

Use the template in `assets/pricing-memo-template.md`. Sections: decision needed, context and inputs, floor and ceiling, options (2 to 3) with expected effect, recommendation (price or tiers), assumptions (labelled), risks and mitigations, test plan with stop rules, metrics to watch, next step.

## Output rules

- Label every number as: from the user, an assumption, or a reference point.
- End with one concrete next step (for example "run the price-sensitivity survey with 30 buyers this week").
- Save as a new document if a connection to Google Docs or Sheets exists; otherwise reply in the conversation. Never overwrite an existing file.
- Do not change prices, publish a price page, message customers or spend money without the user's go-ahead.
- Optional: offer a diagram (price ladder or break-even curve) via the `visual-thinking` skill if installed, otherwise a plain-text table.

## Quality bar

1. The floor is computed, not assumed; the recommendation never sits below it without a stated reason.
2. At least two options are compared, and value-based reasoning is shown, not only rivals' prices.
3. Each tier has a named segment and a fence.
4. Every expected effect shows its assumptions and a range, not a single point.
5. The test has a hypothesis, a primary metric, guardrails and stop rules written before launch.
6. No invented market data; reference points are marked and need checking.

## Related skills (soft, never required)

Use if installed, otherwise do the step in place: `business-strategist` (positioning and wider strategy), `startup-metrics-framework` (lifetime value, payback), `startup-financial-modeling` (scenarios and cash), `market-researcher` (competitor and market inputs), `ecommerce-promotion-design` (vouchers, campaigns, flash sales).

## When not to use

- The user needs market sizing or a competitor map first: use market research.
- The question is about wider strategy or a business-model choice: use strategy skills.
- The user wants campaign mechanics, vouchers or a sales calendar: use promotion design.
- The user wants a full financial forecast: use financial modelling.
- The user wants sales-page copy: use a copywriting skill.
