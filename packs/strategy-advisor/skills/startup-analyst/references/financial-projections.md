# Financial projections: light workflow

This is the in-place fallback. If `startup-financial-modeling` is installed, hand the full model to it; if `startup-metrics-framework` is installed, use it to choose and read unit economics. Do not duplicate them. Use this page for a one-page, 12 to 36 month sketch that supports a business case. Every number is tagged `given`, `sourced` or `assumption`. All ratios below are reference points; check them against the user's market.

## Step 1. Inputs (ask once, each with a default)

1. Business model and pricing. (default: infer and confirm)
2. Starting cash, monthly spend, headcount. (default: none, mark as missing)
3. Currency and first month. (default: user's local currency, next month)
4. Purpose: internal, board, fundraising. (default: internal)
5. Horizon. (default: 12 months detailed, then yearly to year 3)

## Step 2. Revenue build

Build from the bottom, never from a market percentage.

```
New customers per month = leads x conversion
Active customers = previous active + new - churned
Revenue = active customers x average revenue per customer
```
Record: lead source and volume, conversion rate, churn rate, price, expansion or discounts. Start with a slow ramp: month one rarely matches the plan. Show which input has the least evidence.

## Step 3. Costs

- **Direct costs** that move with customers: hosting, payment fees, delivery, support time.
- **Team**: roles, start month, loaded cost per person in the local currency (include taxes and benefits as a stated percentage).
- **Acquisition spend**: channel budget, sales tools.
- **Overhead**: software, office, legal, accounting.
- **One-off**: equipment, set-up, legal formation.

Separate fixed from variable so break-even can be calculated.

## Step 4. Cash and runway

```
Net cash flow = cash in - cash out
Cash balance = previous balance + net cash flow
Runway (months) = cash now / average monthly net burn
```
Note timing differences: customers who pay annually in advance, invoices paid in 30 to 60 days, refunds. Flag the month the balance would turn negative.

## Step 5. A few numbers to read

Gross margin, customer acquisition cost, payback in months, churn, burn per month, break-even month. Give each with its formula and tag. For a judgement on whether the values are healthy, use `startup-metrics-framework` if installed; otherwise state your reading as a reference-point comparison and say the user must test it.

## Step 6. Three scenarios

| | Conservative | Base | Optimistic |
|---|---|---|---|
| Conversion | | | |
| Churn | | | |
| Price realised | | | |
| Hiring pace | | | |
| Result: month cash runs out | | | |

Change only the inputs with the weakest evidence. Provide a one-line "if this input is wrong by X" sensitivity for the top two.

## Step 7. Funding implication (only if asked)

Work backwards: the milestone needed for the next stage, the months to reach it in the conservative case, plus a buffer (reference point: 6 months), gives a minimum raise. Present it as an assumption-based range, never as a recommendation to raise a specific amount from specific people.

## Output layout

```
# Projection sketch: [venture]
Summary (runway, break-even month, biggest unknown)
Assumptions table
Monthly table (revenue, costs, cash)
Scenarios and sensitivity
Gaps and next step
```

Prefer a new spreadsheet if a connection exists, with assumptions in one sheet and formulas that reference them; otherwise a table in the reply.

## Quality checks

- Revenue ties to customer counts, not to market share.
- Hiring plan matches the cost lines.
- Cash, not profit, drives the runway.
- Assumptions are in one place and change the result when edited.
- No figure is presented as a forecast of fact.
