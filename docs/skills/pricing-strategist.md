# pricing-strategist

## What it does

Decides what to charge: it compares value-based, cost-plus and competitor-based pricing side by side, checks the unit-economics floor first, designs tiers, discount policy and price increases, and plans a price test with a numeric stop rule. The output is a pricing recommendation memo with a draft customer message. It never recommends a price below the floor without a stated reason. Body in English, description bilingual.

Pricing needs its own inputs (costs, competitors, current price) and its own methods (the unit-economics floor, willingness-to-pay research, tests), so it was split off from the old pricer mode of `business-strategist`. The default is value-based pricing inside the band between the floor and a reference price. New compared with the old mode: a discount policy with the volume needed to break even, a price-increase plan with communication, and test design with stop rules. A test run showed a thin customer message and a vague stop rule, so the skill now always includes a draft customer message and a numeric stop rule; with a small customer base it advises raising in stages. Two helper files: a memo template and a guide to willingness-to-pay methods. Reference points: 2 to 4 price tiers; 2 to 3 options compared in the memo; 5 to 10 buyer interviews as a qualitative minimum; a price-sensitivity survey of about 100 or more respondents per consumer segment; 30 to 60 days notice before raising a subscription price (check your contract); lifetime value of several times acquisition cost with payback in about a year; follow results for two billing cycles after a rise. Every number in this skill is a labelled reference point, not a fact about your market; the skill asks for your own figures. Trade-off: no sample market data is included, so there is no risk of invented data; you supply or check the numbers.

Source: [`packs/strategy-advisor/skills/pricing-strategist/SKILL.md`](../../packs/strategy-advisor/skills/pricing-strategist/SKILL.md)

## When to reach for it

Someone asks what to charge, whether to raise prices, how to design pricing tiers, how much customers will pay, whether a discount policy is sound, or how to test a price. For the wider strategy use `business-strategist`; for unit economics and metrics use `startup-metrics-framework`; for e-commerce promotions use `ecommerce-promotion-design`.

## Common questions

**Will it tell me the exact price?** It recommends a price or a range with the reasoning, the floor and the test to confirm it; the number rests on the inputs you give.

**What if I have only a few customers?** It warns that a split test is weak and advises raising in stages with a numeric stop rule.

**Does it include market price data?** No. Numbers you do not provide are labelled assumptions or reference points.

## It's working if

- The unit-economics floor is calculated before any price is recommended.
- The memo compares value, cost and competitor views and gives 2 to 3 options.
- A draft customer message and a numeric stop rule are included for any price change.
