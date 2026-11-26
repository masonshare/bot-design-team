# ecommerce-kpi-analytics

## What it does

Diagnoses e-commerce sales numbers and turns them into actions: GMV as traffic times conversion times average order value, GMV versus NMV, sell-in versus sell-out, inventory days, and a weekly review template. It names which of the three drivers is broken first, then gives the fix.

It exists because "sales dropped" is usually one driver, not all three. Fixing the wrong one costs money, so diagnosis comes before solutions. Reference points: GMV-to-NMV loss under roughly 10 to 15 percent is healthy and over 20 percent needs investigation; picture click-through under roughly 2 percent means test a new cover image; conversion of about 1 to 3 percent on a marketplace and 0.5 to 1.5 percent on an own website; stock over 60 days is too much and under 7 days is about to run out. Every number in this skill is a labelled reference point, not a fact about your market; the skill asks for your own figures.

Source: [`packs/marketing-ecommerce/skills/ecommerce-kpi-analytics/SKILL.md`](../../packs/marketing-ecommerce/skills/ecommerce-kpi-analytics/SKILL.md)

## When to reach for it

A shop owner or e-commerce manager asks why sales fell, what GMV or NMV means, why traffic is high but orders are few, how to raise order value, or how much stock is healthy. For unit economics use `startup-metrics-framework`; for listing and image work use `ecommerce-store-optimization`; for promotions use `ecommerce-promotion-design`.

## Common questions

**Does it need my report?** No, but answers are sharper with your last two weeks of numbers. Without them it says its figures are reference points.

**Where does the output go?** In the chat, or in a new Google Doc or Sheet if that connection is available.

**Does it change prices or ads?** No. It only analyses and recommends; you act.

## It's working if

- The answer names one of traffic, conversion or order value as the main problem before giving any fix.
- Each recommendation comes with a formula or a number and a concrete next step.
- It marks benchmark numbers as reference points and asks for yours.
