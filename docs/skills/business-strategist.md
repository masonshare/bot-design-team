# business-strategist

## What it does

Strategic counsel for founders and executives in four modes picked from the request: auditor (diagnose gaps in a business), cartographer (map market, competitors and white spaces), architect (formulate strategy and choose between options) and operator (turn strategy into priorities, OKRs and metrics). Every recommendation comes with options, one pick, the risks, and the evidence or assumption behind it. Depth keywords: express, guided, deep. Body in English, description bilingual.

Founders usually hit one of four problems: bad numbers with no clear cause, a blurred market, a stuck strategic choice, or a strategy that never became weekly priorities. About 2,000 lines of reference libraries were condensed into a self-sufficient SKILL.md plus three small reference files. The business stage (bootstrapped, funded, established) is asked once and applied to every analysis. The worked example uses an invented product with invented numbers. Pricing is no longer a mode: it moved to `pricing-strategist`; when that skill is not installed, the architect mode does a short price check instead. Trade-off: dropping a separate pricer mode made pricing shallower here, which is why it became its own skill. Reference points: LTV to CAC about 3 to 1; CAC payback under about 12 months; burn multiple under 1.5 efficient and over 3 a warning; product-market fit at about 40 percent "very disappointed" from at least 40 responses; OKR stretch goals scored at about 70 percent; at most 3 objectives with 3 to 4 key results each; follow churn for 60 to 90 days after a price change. Every number in this skill is a labelled reference point, not a fact about your market; the skill asks for your own figures.

Source: [`packs/strategy-advisor/skills/business-strategist/SKILL.md`](../../packs/strategy-advisor/skills/business-strategist/SKILL.md)

## When to reach for it

Someone asks what is wrong with their numbers, whether to enter a market, how to compete, which option to pick, how to set OKRs, whether unit economics are viable, or about a moat; also "competitors cut prices, follow or differentiate". For what to charge use `pricing-strategist`; for a root-cause and action-plan process use `problem-solver-skill`; for a deep market size and competitor study use `market-researcher`. Links are soft, with an in-place fallback.

## Common questions

**Why does it not set prices?** Pricing has its own inputs and methods, so it lives in `pricing-strategist`. Without it, a short price check is done inside the architect mode.

**Which mode will it use?** It picks from how you phrase the request; there is no menu.

**Does it make up numbers?** No. Numbers you do not give are labelled assumptions.

## It's working if

- Each recommendation has options, one pick, risks, and evidence or a labelled assumption.
- The business stage was asked once and shaped the analysis.
- The answer ends with a decision someone can act on this week.
