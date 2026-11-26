# market-researcher

## What it does

Market research in four modes picked from the request: analyst (market size, industry structure, PESTEL, SWOT), scout (competitor tiers, profiles, battlecards), strategist (positioning, jobs to be done, product-market-fit survey, category strategy) and architect (briefs for versus, alternative and comparison pages). Every figure carries a source tag and key figures are cross-checked. It ends with a next step. Body in English, description bilingual.

Market research tends to fail in two ways: numbers with no source, and analysis frameworks left empty. The skill folds four jobs into one process with four mandatory source labels (primary, analyst, news, estimate) and a rule of two independent sources for key figures. It uses no real market data: worked examples use invented numbers (a made-up startup), labelled as illustration. If the platform has no search tool, it asks the user to paste data. Positioning must fill six components in order, from the alternative to the category. Reference points: if two sizing methods differ by about 2 times, hunt for the assumption causing it before reporting; product-market-fit "very disappointed" at 40 percent or more, from about 40 responses; a comparison table of 6 to 10 rows with at least one row where the competitor wins; page title about 60 and description about 155 characters. Every number in this skill is a labelled reference point, not a fact about your market or brand; the skill asks for your own figures. Trade-off: it drops a large reference library to stay short and self-contained, so each framework has only its core.

Source: [`packs/marketing-ecommerce/skills/market-researcher/SKILL.md`](../../packs/marketing-ecommerce/skills/market-researcher/SKILL.md)

## When to reach for it

Someone asks to size a market, run competitor analysis, build a battlecard, do a SWOT, position a product, test product-market fit, or plan a versus page. Without data it returns the framework plus labelled illustrative estimates, which is correct but less useful; bring your own data. For brand voice use `brand-architect`; for choosing one niche use `niche-finder`. Links to other skills are soft.

## Common questions

**Where do the numbers come from?** From what you give it or what a search tool finds, each tagged primary, analyst, news or estimate. Invented example numbers are labelled illustrations.

**What if no search tool is available?** It asks you to paste the data instead of guessing.

**Which mode will it use?** It picks from your request and asks one routing question only when the request sits between two modes.

## It's working if

- Every figure has a source tag, and key figures were cross-checked against a second independent source.
- Positioning has all six components in order.
- The answer ends with a clear next step and a plain-text handoff block.
