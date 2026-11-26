# startup-financial-modeling

## What it does

Builds a 3 to 5 year startup financial model: revenue by customer cohort, cost structure, hiring plan, cash flow and runway, three scenarios, and funding rounds, with every assumption stated. If a Google connection is available it creates a new Google Sheet and never overwrites an existing one. Body in English, description bilingual.

A financial model is a set of assumptions turned into numbers. Every figure is either given by the user or labelled an assumption. Cash flow is modelled separately from revenue because payment terms matter. Reference points: fully loaded staff cost about 1.3 to 1.4 times salary (check local rules); scenarios plus or minus 15 to 30 percent; about 20 percent cost buffer; raise enough to reach the next milestone plus about 6 months. Every number in this skill is a labelled reference point, not a fact about your market; the skill asks for your own figures. The test run showed the agent inventing a valuation for illustration (labelled); do not use illustrative valuations unless you supplied one.

Source: [`packs/strategy-advisor/skills/startup-financial-modeling/SKILL.md`](../../packs/strategy-advisor/skills/startup-financial-modeling/SKILL.md)

## When to reach for it

The user asks to build a financial model, forecast revenue, calculate burn and runway, model cash flow, or decide how much to raise. For choosing and reading metrics use `startup-metrics-framework`. Software-style ratios need adjusting for other industries.

## Common questions

**Can it make up the numbers?** No. Anything you did not provide is labelled as an assumption.

**Where does the model go?** A new Google Sheet if connected, otherwise tables in the chat.

**Is the funding advice a valuation?** No. It sizes the raise to a milestone; valuation is your call.

## It's working if

- Every number is either yours or marked as an assumption.
- There are three scenarios with the same structure.
- It ends with the validation checklist and the output summary.
