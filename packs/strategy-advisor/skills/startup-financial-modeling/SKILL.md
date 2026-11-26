---
name: startup-financial-modeling
description: Build a 3 to 5 year startup financial model - revenue by cohort, cost structure, hiring plan, cash flow and runway, three scenarios, and funding rounds - with the assumptions stated. Use when the user asks to "build a financial model", "forecast revenue", "calculate burn and runway", "model cash flow", "how much should we raise". Tiếng Việt - dựng mô hình tài chính cho startup 3 đến 5 năm (doanh thu theo nhóm khách, chi phí, nhân sự, dòng tiền, ba kịch bản, gọi vốn); nêu rõ giả định; ra bảng tính Google Sheets mới nếu có kết nối.
---

# Startup financial modeling

A model is a set of stated assumptions turned into numbers. Its job is to support decisions (how much to spend, how much to raise, when to hire), not to predict the future. Never invent figures: every number is either supplied by the user or labelled **assumption**.

## When not to use

- Only one metric is needed (CAC, LTV, churn): use `startup-metrics-framework`.
- The user needs a market-size estimate first: use `startup-analyst` or a market research skill; if none is installed, do a quick top-down and bottom-up estimate in place and label it rough.
- Online shop day-to-day numbers (traffic, conversion): use `ecommerce-kpi-analytics`.

## Before building: collect inputs

Ask once, with a default for each, then proceed:
1. Business model: subscription software, marketplace, online shop, services, or other.
2. Pricing and expected customers per month at the start.
3. Current cash, current monthly spend, current team.
4. Currency, and the first month of the model.
5. Goal: internal planning, a board, or fundraising.

Use the user's currency and local payroll costs. The example ratios below come from software startups; replace them for other industries.

## The pieces of a model

### 1. Revenue (build it by cohort)
Revenue comes from customers won each month and how many stay.
```
Monthly recurring revenue = sum over cohorts of (cohort size x share still active x average revenue per user)
Annual run-rate = monthly x 12
```
Inputs: new customers per month, retention by month, average revenue per user, pricing tiers, expansion (upsell, cross-sell).

Illustrative software retention curve (an assumption to replace): about 90% after 3 months, 85% after 6, 75% after 12, 70% after 24.

### 2. Cost structure
- **Cost of goods sold**: hosting, payment fees, variable support, per-customer services.
- **Sales and marketing**: acquisition spend, tools, sales pay.
- **Product and engineering**: team pay, design, tools.
- **General and administrative**: leadership, finance, legal, HR, office, insurance.

Separate **fixed** costs (salaries, software, rent) from **variable** ones (hosting, payment fees, support) and state each as a percentage of revenue or a headcount rule.

### 3. Hiring plan
Headcount by role and department. Use fully loaded cost (salary plus taxes and benefits; a factor of about 1.3 to 1.4 is a common starting point, check local rules). Allow 3 to 6 months to fill a role, 3 to 6 months to reach full output, and some attrition each year.

### 4. Cash flow and runway
```
Ending cash = beginning cash + cash collected - cash paid out - capital spending
Net burn   = cash paid out - cash collected  (per month)
Runway     = cash balance / average monthly net burn
```
Revenue is not cash: model payment terms. If ending cash goes below zero, the shortfall is the funding need.

### 5. Metrics
Revenue growth, CAC, LTV, LTV to CAC ratio, CAC payback, burn multiple (net burn / net new annual revenue), magic number, rule of 40. Definitions are in `startup-metrics-framework`; if it is not installed, state the formula next to each number.

## Scenarios

Always three, sharing the same structure:
- **Conservative** (roughly a bad-but-plausible case): slower acquisition, lower price or conversion, higher churn, longer sales cycles. Use it for cash management.
- **Base** (most likely): the main planning case, used for board reporting.
- **Optimistic**: faster growth, better unit economics. Use it for upside planning only.

Vary acquisition, churn, contract value, and CAC (for example plus or minus 15 to 30%, an assumption to tune). Keep pricing structure, core costs and hiring roles the same; move timing, not roles.

## Time horizon

Monthly detail for years 1 and 2, quarterly for year 3, annual headlines for years 4 to 5.

## Step by step

1. Define the business model and pricing.
2. Build revenue by cohort.
3. Model costs, fixed and variable.
4. Make the hiring plan.
5. Project cash and runway.
6. Compute metrics.
7. Run the three scenarios.
8. Validate (below).
9. Add funding scenarios.

## Funding scenarios

```
Post-money = pre-money + investment
Dilution   = investment / post-money
```
Allocate use of funds by category (product, growth, operations, working capital). Size the raise to reach the **next milestone plus about 6 months of buffer**. Milestones are things like product launch, first meaningful revenue, positive unit economics, next funding round.

## Business model starting points

| Model | Revenue drivers | Ratios to sanity-check (illustrative) |
|---|---|---|
| Subscription software | New, expansion, contraction, churned recurring revenue | Gross margin 75 to 85%; sales and marketing 40 to 60% of revenue early on; CAC payback under 12 months; net retention 100 to 120% |
| Marketplace | Transaction value, take rate | Take rate 10 to 30% by category; separate acquisition cost for buyers and sellers |
| Online shop | Traffic, conversion, average order value, repeat purchases | Gross margin 40 to 60%; contribution margin 20 to 35% |
| Services | Billable hours or projects, rate, utilisation | Gross margin 50 to 70%; utilisation 70 to 85% |

These ranges are common rules of thumb, not facts about the user's market. Tell the user to replace them with their own data or local benchmarks.

## Common mistakes

- Revenue too optimistic: new startups rarely hit aggressive curves; use conservative acquisition and realistic churn.
- Costs too low: add a buffer (about 20%), use fully loaded pay, include tools and compliance.
- Treating revenue as cash: ignore payment terms and the model lies about runway.
- Static headcount: hiring is slow and people leave.
- One scenario only: always show the conservative case and what you would do if it happens.

## Validation checklist

- [ ] Growth is achievable (for example no more than about 3x in year 2 and 2x in year 3, unless justified).
- [ ] Unit economics are realistic (a ratio above about 3 and payback under about 18 months are common targets).
- [ ] Burn multiple is reasonable (under about 2 in years 2 and 3).
- [ ] Headcount scales with revenue.
- [ ] Gross margin fits the model type.
- [ ] Sales and marketing spend matches CAC and growth targets.
- [ ] Compared with peers at a similar stage, and the assumptions have been reviewed by an advisor or investor if the model is for fundraising.

## Output

Deliver, in this order:
1. A one-page summary: headline numbers per scenario, runway, funding need, and the three assumptions that matter most.
2. The assumptions table (every input, its value, and whether given or assumed).
3. The model itself: a Google Sheets spreadsheet created new (formulas visible) if a connection exists; otherwise tables in the reply. Never overwrite an existing spreadsheet.
4. The risks and what would make the model wrong.

State clearly that this is a planning tool built on assumptions and is not financial, legal or tax advice.
