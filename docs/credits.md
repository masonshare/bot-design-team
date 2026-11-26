# Skill credits (marketing-ecommerce, strategy-advisor, starter additions)

The skills in these packs are written in our own words. Skill files carry no author names, book titles, URLs or quotes; every source is listed here instead. Credits for the original Starter skills are in the root [`CREDITS.md`](../CREDITS.md).

## How to read the tables

- **Source**: where the ideas come from (author and work, course, or "Masonshare, from practice").
- **Licence**: the licence of the source when we copied code; "none (ideas only)" when we only rewrote ideas in our own words.
- Framework names that practitioners use as everyday words (AIDA, JTBD, BATNA, ERRC) stay in the skills; the people behind them are named here.

## marketing-ecommerce

| Skill | Source | Licence | Notes |
|---|---|---|---|
| `ecommerce-channel-strategy` | Masonshare, from practice and study notes | none (ideas only) | Eight channel types and stage-based criteria; earlier internal version rewritten. Platform names are examples only |
| `ecommerce-kpi-analytics` | Masonshare, from practice and study notes; standard e-commerce metric definitions (GMV, NMV, AOV, sell-in, sell-out) | none (ideas only) | Earlier internal version rewritten |
| `ecommerce-product-strategy` | Masonshare, from practice and study notes | none (ideas only) | Three SKU roles, 1 + X bundles, four-stage test-and-scale; earlier internal version rewritten |
| `ecommerce-promotion-design` | Masonshare, from practice and study notes | none (ideas only) | Six mechanisms and the post-promotion dip calculation; earlier internal version rewritten |
| `ecommerce-store-optimization` | Masonshare, from practice and study notes | none (ideas only) | Four-page audit and quick gate; earlier internal version rewritten |
| `niche-finder` | Masonshare (own design: synthesis and five-criteria scoring). Frameworks named in per-niche notes: Five Forces (Michael E. Porter) and the general strategy literature on durable advantages | none (ideas only) |  |
| `playbook-documentation` | Masonshare, from practice and study notes; SOP, runbook and checklist are common practice | none (ideas only) | Earlier internal version rewritten |
| `youtube-digest` | Masonshare (own script `fetch_youtube.py`) | own code | Calls the external tool `yt-dlp` (see below) |

## strategy-advisor

| Skill | Source | Licence | Notes |
|---|---|---|---|
| `startup-financial-modeling` | Rewritten in our own words; ideas from community skill material and standard finance practice (runway, burn, dilution) | none (ideas only) | Earlier version looked like a community collection; its licence could not be verified, so nothing was copied |
| `startup-metrics-framework` | Rewritten in our own words; ideas from community skill material and standard startup-metric formulas | none (ideas only) | Same note as startup-financial-modeling |
| `system-thinking` | Masonshare, from practice and study notes | none (ideas only) | Feedback loops and delays are general systems-thinking concepts |
| `business-strategist` | Masonshare (own design: four modes, evidence rule, handoff block). Ideas from: Five Forces, generic strategies, value chain (Michael E. Porter); strategy canvas and ERRC grid (W. Chan Kim and Renee Mauborgne, Blue Ocean Strategy); sources of durable advantage (Hamilton Helmer, 7 Powers); TOWS matrix (Heinz Weihrich); growth vector matrix (H. Igor Ansoff); LTV to CAC and CAC payback (David Skok); burn multiple (David Sacks); growth loops and the four fits (Brian Balfour); the 40 percent product-market-fit test and north star metric (Sean Ellis); AARRR (Dave McClure); flywheel (Jim Collins); second-level thinking (Howard Marks); inversion, pre-mortem and mental models (Charlie Munger); regret minimisation (Jeff Bezos); price sensitivity meter (Peter van Westendorp); anchoring (Daniel Kahneman and Amos Tversky); Jobs To Be Done (Clayton Christensen, Bob Moesta). Standard economics (opportunity cost, expected value, contribution margin, break-even, demand elasticity) and OKRs are common practice with no single author | none (ideas only) | Rewritten from scratch; six reference libraries condensed to three small files; the earlier pricer mode moved to `pricing-strategist`; example product invented |
| `pricing-strategist` | Masonshare (own design: eight-step process, floor-then-ceiling, test with stop rules), split from the pricer mode of the earlier business-strategist. Ideas from: price sensitivity meter (Peter van Westendorp, 1976, with the Newton-Miller-Smith extension); anchoring and adjustment (Daniel Kahneman and Amos Tversky); Jobs To Be Done (Clayton Christensen and Bob Moesta); willingness to pay and demand elasticity from standard economics (Alfred Marshall and common textbooks), the Gabor-Granger method (1966) and conjoint analysis (Paul Green, 1971); unit-economics floor (David Skok, SaaS Metrics 2.0, mostly standard arithmetic). The five-layer pricing stack of the earlier version was an internal synthesis with no single author | none (ideas only) | Rewritten from scratch; specific examples, brand names and experiment figures from the earlier version were removed |

## starter additions

| Skill | Source | Licence | Notes |
|---|---|---|---|
| `skill-spec-generate` | Masonshare (own design: keep the why of a skill apart from the skill) | none (ideas only) | Lives in `packs/starter/mango-spring-roll/skills/` |

## Third-party code copied with its licence

Code written by others and copied into a pack as is. The folder keeps its `LICENSE` file and copyright line unchanged; `scripts/check-skill-neutral.py` skips a folder that holds a `LICENSE`.

| Folder | Author | Licence |
|---|---|---|
| (none yet) | | |

## Linked only, not copied

Tools and skills the docs point to but this repo does not include.

| Name | Why not copied |
|---|---|
| (none yet) | |

## Tools called from outside

Command-line tools a skill asks the user to install (not shipped here).

| Tool | Used by |
|---|---|
| `yt-dlp` (command-line tool, not shipped here; its licence has not been verified from this machine) | `youtube-digest` |
