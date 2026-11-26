---
name: startup-metrics-framework
description: Choose, calculate and read the right startup metrics for the business model and stage (recurring revenue, CAC, LTV, payback, retention, burn multiple, marketplace and consumer engagement metrics) and set up a reporting rhythm. Use when the user asks about "key metrics", "CAC and LTV", "unit economics", "burn multiple", "which numbers to show investors". Tiếng Việt - chọn, tính và đọc các chỉ số startup theo mô hình và giai đoạn (CAC, LTV, hoàn vốn, giữ chân, tốc độ đốt tiền), thiết lập nhịp báo cáo.
---

# Startup metrics

Track the few numbers that matter for the stage, and read them with context. Every figure is either supplied by the user or labelled **assumption**. Ranges below are common rules of thumb from software and marketplace startups: present them as reference points the user should check against their own market, not as facts.

## When not to use

- A full multi-year projection: use `startup-financial-modeling`.
- Online shop traffic, conversion and inventory: use `ecommerce-kpi-analytics`.
- A market-size estimate: use `startup-analyst` or a market research skill.

## Step 1: pick the model and stage

Ask once, with defaults: business model (subscription, marketplace, consumer app, business-to-business sales, online shop), stage (idea or product-market fit, early revenue, growth), and what the numbers are for (internal, board, fundraising). Then choose **5 to 7 core metrics**, not 50.

| Stage | Focus | Do not obsess over |
|---|---|---|
| Finding product-market fit | Active users, retention at day 7 and day 30, depth of use, qualitative feedback | Revenue, acquisition cost, unit economics |
| Early revenue | Monthly growth, CAC and LTV baseline, gross retention, burn and runway | Fine-grained sales efficiency |
| Growth | Annual growth, unit economics, net retention, burn multiple, magic number | Vanity totals |

## Core metric formulas

**Revenue**
```
Monthly recurring revenue (MRR) = sum of (active subscriptions x monthly price)
Annual recurring revenue (ARR)  = MRR x 12
Month-on-month growth = (this month - last month) / last month
Year-on-year growth   = (this year - last year) / last year
```

**Unit economics**
```
CAC = total sales and marketing spend / new customers won   (include salaries, tools, overhead)
LTV = average revenue per user x gross margin % / churn rate
      (simple form: revenue per user x average lifetime x gross margin %)
LTV to CAC = LTV / CAC
CAC payback (months) = CAC / (monthly revenue per user x gross margin %)
```
Reference points: LTV to CAC above about 3 is healthy, 1 to 3 needs work, under 1 loses money; payback under about 12 months is excellent, 12 to 18 good, 18 to 24 borderline (watch closely), over about 24 worrying.

**Cash**
```
Net burn = cash out - cash in, per month
Runway (months) = cash balance / net burn
Burn multiple = net burn / net new ARR
```
Common guidance: keep 12 to 18 months of runway; burn multiple under 1 is exceptional, 1 to 2 acceptable, over 2 inefficient.

## By business model

### Subscription software
- **Revenue movement**: net new MRR = new + expansion - contraction - churned.
- **Retention**: logo retention (share of customers kept); net dollar retention = (starting ARR + expansion - contraction - churn) / starting ARR (above about 120% is best-in-class, 100 to 120 good, under 100 needs work); gross retention = (starting ARR - churn - contraction) / starting ARR (above about 90% excellent, below about 85% worrying).
- **Efficiency**: magic number = net new ARR in a quarter / sales and marketing spend of the prior quarter (above about 0.75 ready to scale, under 0.5 not yet); rule of 40 = growth % + profit margin % (40 or more is strong); quick ratio = (new + expansion) / (churned + contraction) (above about 4 is healthy growth, under 2 is a churn problem).

### Marketplace
- Transaction value (GMV) and its growth; **take rate** = net revenue / GMV (rough ranges: payment processing 2 to 3%, product marketplaces 10 to 20%, service marketplaces 15 to 25%, high-value business-to-business 5 to 15%).
- **Liquidity**: time to first transaction, fill rate (share of requests that end in a transaction; above about 80% is strong), repeat rate (above about 60% strong).
- **Balance**: track supply and demand growth separately. Too much supply gives low fill rates; too much demand gives long waits.

### Consumer and mobile
- Daily and monthly active users; **DAU/MAU** (above about 50% is a daily habit, 20 to 50 good, under 20 weak); session frequency and length.
- Retention at day 1, day 7, day 30 (day-30 above about 40% excellent, under about 25% weak). A curve that flattens means users form a habit; a steep fall points to weak product-market fit.
- Viral coefficient = invites per user x invite conversion rate (above 1 is viral growth).

### Business-to-business sales
- Win rate (about 20 to 30% for a new team, 30 to 40% mature); sales cycle length (small business about 30 to 60 days, mid-market 60 to 120, enterprise 120 to 270); average contract value.
- Pipeline coverage = pipeline value / quota (3 to 5 times is typical). Stage conversion rates vary a lot, so use the user's own history.

### Online shop
Use traffic x conversion x average order value, and see `ecommerce-kpi-analytics`.

## Reporting rhythm

| Cadence | What |
|---|---|
| Daily | Revenue, active users, sign-ups, conversions |
| Weekly | Growth rates, retention cohorts, pipeline |
| Monthly | Full metric set, board and investor update |
| Quarterly | Trends, benchmarking, strategy review |

Set up one source of truth, automated calculation, and history. Tools are optional; a shared Google Sheet is enough early on.

## Common mistakes

1. **Vanity metrics**: total users without retention, page views without engagement, downloads without activation.
2. **Too many metrics**: 5 to 7 tracked closely beat 50 tracked loosely.
3. **Skipping unit economics** even at an early stage.
4. **Not segmenting** by customer type, channel and cohort.
5. **Gaming the dashboard** instead of the business.

## What investors usually look at

- Early rounds: growth rate, retention, early unit economics, engagement.
- Growth rounds: ARR and growth, CAC payback, LTV to CAC, net retention, burn multiple.
- Later rounds: rule of 40, efficient growth, path to profit.

Presentation format for a headline slide or message, each with trend and benchmark:
```
MRR: ___ (growth vs last month)   ARR: ___ (growth vs last year)
CAC: ___  LTV: ___  LTV to CAC: ___x
Net retention: ___%  Logo retention: ___%
Net burn: ___ per month   Runway: ___ months
```

## Output

1. The 5 to 7 chosen metrics with a one-line reason each, and the formula next to every number.
2. The user's own numbers where given, marked **given** or **assumption**, with the benchmark beside them.
3. A short reading: what is healthy, what is not, and the one number to fix first.
4. A reporting plan (cadence and owner). Save as a new Google Sheet or Doc if a connection exists; otherwise reply in the conversation. Never overwrite an existing file.

Metrics inform decisions; they are not financial advice.
