# Economics and growth (compact)

Use for Auditor, Architect and Operator modes. Every threshold below is a **reference point**, a rule of thumb that varies by industry, price level and stage. Tell the user to check it against their own market, and never present it as a fact about their market.

## 1. Unit economics

| Metric | Formula | Reference point |
|---|---|---|
| Customer lifetime (subscription) | 1 / monthly churn rate | Longer is better; under 12 months is fragile |
| Lifetime value (LTV) | monthly revenue per customer x gross margin x lifetime | Use margin, not revenue |
| Acquisition cost (CAC) | total sales and marketing spend / new customers in the same period | Count all spend, including salaries |
| LTV to CAC ratio | LTV / CAC | About 3 to 1 often seen as healthy; under 1 to 1 loses money on each customer; far above 5 to 1 may mean under-investing in growth |
| CAC payback | CAC / (monthly revenue x gross margin) | Roughly under 12 months for small teams; longer needs funding |
| Contribution margin | revenue minus variable costs (delivery, payment fees, support per unit) | Must cover fixed costs at planned volume |
| Break-even volume | fixed costs / contribution margin per unit | Compare with realistic sales in the next 2 to 4 quarters |

Method: compute by segment or channel, not only blended; blended numbers hide the segment that loses money. Show formulas with the user's numbers. Flag any input that is an assumption (for example gross margin).

Sensitivity: change churn, price, and CAC one at a time by 20% and report which moves the result most. That is the lever to work on first.

## 2. Capital efficiency (venture-backed or cash-constrained)

- Burn multiple = net cash burned / net new recurring revenue in the same period. Reference points: under about 1.5 is efficient, 1.5 to 3 acceptable with strong growth, above 3 is a warning. Higher burn needs a clear reason.
- Runway = cash / monthly net burn. Name the date cash runs out and what has to be true by then.
- Net revenue retention: revenue now from customers of 12 months ago / their revenue then. Above 100% means the base grows without new customers.

## 3. Product-market-fit check

Signals, strongest first:
1. Survey of active users: "How would you feel if you could no longer use this?" A common reference point is around 40% answering "very disappointed" for fit. Needs 40 or more responses to mean anything.
2. Retention curve flattens instead of falling to zero.
3. Organic referrals or inbound demand without paid push.
4. Customers accept price increases with little churn.
Read-out: fit not yet reached means fix the product and retention before scaling acquisition spend.

## 4. Funnel (acquire, activate, retain, revenue, refer)

For each stage give the metric, the count, and the conversion to the next stage. The weakest conversion relative to a reference or to the user's own past is the first place to look. Typical order of attack: retention first (fixes the leaking bucket), then activation, then acquisition. Vanity counts (visits, followers) are context only.

## 5. Growth loops and flywheel

- A loop is a closed path where output feeds input: a customer is acquired, uses the product, creates something (referral, content, data, revenue) that brings more customers. Draw it in four to six steps and find the slowest step.
- Loop types: referral or invite, content or search, paid (spend returns more than it costs within the payback window), sales-led (customer revenue funds more sales capacity).
- Check four fits before betting on a loop: market and product, product and channel, channel and revenue model, revenue model and market. Weakness in one fit blocks the loop.
- Flywheel: name three to five reinforcing components (for example better product, more customers, more data, better product). Pushing any one speeds the rest; find the one with the least friction.

## 6. North star and input metrics

- North star: one metric that counts value delivered to customers and predicts revenue (for example "weekly active teams completing a core action"). Not revenue itself and not signups.
- Input metrics: two or three levers a team can change this quarter (activation rate, time to first value, repeat usage).
- Mark each metric leading or lagging, give owner, current value, target, and source.

## 7. Pricing method (when price is part of the question)

1. Job: what job does the customer hire the product for (functional, emotional, social), and what do they use today?
2. Range: ask a sample of target buyers four questions (too cheap to trust, a bargain, getting expensive, too expensive) and read the acceptable range; the user must supply or collect the data, otherwise label the range an assumption.
3. Sensitivity: is demand elastic here (many substitutes, small budget item, easy to compare) or inelastic (high switching cost, small part of customer's cost, critical outcome)? Test with a small experiment before changing for everyone.
4. Presentation: three tiers usually work; place the target tier in the middle; show a higher anchor first; name tiers by customer type, not by feature count.
5. Check: does the price produce a viable LTV to CAC and contribution margin (section 1)? A price that wins deals but fails this check is a trap.
6. Changes: grandfather or notify existing customers, change for new customers first, watch churn for 60 to 90 days (reference point).
