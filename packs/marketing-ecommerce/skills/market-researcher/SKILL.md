---
name: market-researcher
description: Market research in four modes - analyst (TAM/SAM/SOM, Five Forces, PESTEL, SWOT with strategy matrix, growth-share view), scout (competitor tiers, profiles, battlecards, generic strategies), strategist (positioning, JTBD, product-market-fit survey, category strategy) and architect (versus / alternative / comparison page briefs). Every figure is source-tagged and triangulated. Use for "size the market", "competitor analysis", "battlecard", "SWOT", "positioning", "PMF", "vs page". Tiếng Việt - nghiên cứu thị trường, quy mô thị trường, phân tích đối thủ, định vị, brief trang so sánh ("phân tích đối thủ", "tính TAM SAM SOM", "định vị sản phẩm").
---

# Market Researcher

## What it does

It turns a business question into a sourced, decision-ready piece of market research. There are four working modes, picked from the request. Every output carries a confidence level, lists its data gaps and ends with a next step.

If the client keeps a `brand-profile.md` (name, positioning, audience, tone, products, limits), read it first and do not re-ask what it answers. Otherwise ask once for the product, the target customer and the market in one sentence each. Offer to write sharpened positioning back to that profile as a new draft, never over the existing file.

## Choose the mode from the request

| The user is asking about | Mode |
|---|---|
| market size, TAM, SAM, SOM, industry structure, Five Forces, PESTEL, SWOT, growth-share | **Analyst** |
| competitors, who we are up against, profiles, battlecards, win and loss | **Scout** |
| positioning, differentiation, jobs to be done, product-market fit, category choice | **Strategist** |
| "X vs Y" page, "X alternative" page, comparison content | **Architect** |

If the request spans two modes, ask one routing question: "Do you want competitor intelligence (who, what, how they sell) or a positioning decision (how we differ and which category we claim)?"

Depth keywords the user may say: **express** (at most one question, deliver fast, add one alternative angle), **guided** (default: 3 to 5 intake questions, confirm the framework, then deliver), **deep** (full intake, several frameworks cross-checked, reasoning shown, variants offered). If the user names a framework, use it.

## Rules that apply to every mode

1. **Tag every data point** with one of four tags: `primary` (the company's own filing, price page, product, or your own interview or survey), `analyst` (paid or published industry research), `news` (press and trade media), `estimate` (your own derivation, with the logic shown).
2. **Triangulate critical figures** (market size, revenue, growth, share) from at least two independent sources, or from two different methods. If only one source exists, say so next to the number and lower the confidence.
3. **Never state market figures as facts from memory.** Figures must come from sources found in this session or supplied by the user. Examples in this skill use invented numbers and are labelled illustrative.
4. **If the platform has no search or read-web tool, ask the user to paste the data** (reports, pricing pages, review excerpts, filings) and work only from that. Say so plainly rather than filling gaps from recall.
5. **Acknowledge competitor strengths** before mapping their weaknesses. Analysis that lists only weaknesses is advertising, not research.
6. **State assumptions.** Any estimate shows its inputs, and the user can change them.
7. **Filter every market to the obtainable part.** A large addressable figure with no realistic share behind it is not an answer.
8. **"The market is growing" needs a rate, a period and a source.** Otherwise leave it out.

## Where to look (source types, no fixed list)

| Need | Source types |
|---|---|
| Company size, revenue, strategy | public filings, annual reports, investor presentations, official registries |
| Customer opinion, switching reasons | review sites, forums, app-store reviews, support communities |
| Hiring direction and tech stack | job posts, engineering blogs |
| Messaging and spend | ad libraries, landing pages, pricing pages, newsletters |
| Market totals and growth | trade bodies and associations, government statistics, analyst reports |
| Demand signal | search-trend tools, marketplace listings, social listening |
| Ground truth | customer interviews, surveys, sales call notes, win and loss records |

Prefer sources nearest the money (filings, price pages, interviews) over sources that repeat each other.

## Mode 1: Analyst

**Intake (guided):** which decision this informs (invest, enter, allocate); exact market definition ("mid-market invoicing software for clinics in one country", not "software"); geography; time horizon (now, 3 years, 5 years); constraints and data already held.

**Methods**
- **Sizing.** Do both. *Top-down:* start from a wider published total, then narrow by geography, segment and product scope. *Bottom-up:* count of target customers x adoption rate x yearly value per customer. Compare; if the two differ by more than a factor of about 2 (reference point), find which assumption drives the gap before reporting. Then separate **TAM** (everyone who could buy), **SAM** (the part your product, channel and geography can serve) and **SOM** (what you can win in the horizon, given capacity and competitors).
- **Five Forces** for industry structure: rivalry, new entrants, substitutes, buyer power, supplier power. Rate each force low, medium or high, with one evidenced reason, then say which one most limits profit.
- **PESTEL** for macro context: political, economic, social, technological, environmental, legal. Keep only factors that change this decision, each with direction (tailwind or headwind) and timing.
- **SWOT with a strategy matrix.** Each item must be specific and evidenced, for example "repeat-order rate of 38% against about 25% for rivals (illustrative)", never "good brand". Then cross: strengths with opportunities (use), weaknesses with opportunities (fix), strengths with threats (defend), weaknesses with threats (avoid or exit).
- **Growth-share view** for a portfolio: place each product or segment by market growth and relative share, then name the action (invest, harvest, fix or drop). Treat the quadrants as a prompt for discussion, not a verdict.

**Example (illustrative, invented numbers):** a fictional meal-kit startup "Lumi Pantry" sizes top-down: 12M households in the country, 30% urban and online, so 3.6M; 8% fit the premium price band, so SAM is about 290k households. Bottom-up: 40 delivery districts it can reach in year one x 1,500 targeted households x 4% conversion gives about 2,400 customers, so SOM is roughly 2,400 households. The two results differ by a large factor only because they measure different things (SAM versus year-one SOM), which the report explains; a true cross-check compares like with like.

**Output:** key findings (3 to 5, each tagged and sourced) / filled framework tables / implications for the decision / confidence level (high, medium, low, with reason) / data gaps / next step.

## Mode 2: Scout

**Intake (guided):** which competitors (or "help me find them"); our product in a line; which intelligence matters (pricing, features, go-to-market, messaging, funding, hiring); where the output will be used (internal strategy, sales team, investors); any existing data.

**Steps**
1. **Tier the field.** Tier 1: direct, same buyer and same job. Tier 2: adjacent, solves part of the job or serves a neighbouring buyer. Tier 3: emerging, or a substitute that could move in. Include "do nothing" and spreadsheets where they are the real alternative.
2. **Collect** from the source types above and tag everything.
3. **Profile each Tier 1 competitor** with the profile template in `assets/templates.md`.
4. **Classify the generic strategy** each runs: cost leadership, differentiation, or focus (on a niche by cost or by difference). Support the label with observed signals (pricing moves, messaging, segment, hiring). A firm that is none of these clearly is "stuck in the middle"; say what evidence shows it.
5. **Compare value chains.** Where does each one build advantage (sourcing, operations, channel, service, technology) and where does it outsource? Differences show where you cannot win on price and where you can win on fit.
6. **Battlecard** for sales use, from the battlecard template, only when the output is for a sales team.

**Output per competitor:** snapshot (size, funding, key metrics, tagged) / product and pricing comparison / strategy classification with evidence / strengths to respect / weaknesses to exploit / recent moves and trajectory / win and loss notes.

## Mode 3: Strategist

**Intake (guided):** what is being positioned (product, company, feature, category); who the best customers are today (or the target if pre-launch); what they use instead; the job they hire the product for; any fit data (survey, retention, churn, interviews).

**Positioning.** Fill **all six components**, none left blank:
1. Competitive alternatives: what customers would do or buy if this did not exist.
2. Unique attributes: capabilities the alternatives lack.
3. Value: the outcome those attributes create for the customer, in their words.
4. Proof: evidence that the value is real (data, cases, references, trial results).
5. Target customers: the segment that cares most about that value.
6. Category: the frame that makes the value obvious to a buyer.
Work in that order (alternatives first, category last). Then pick the **category strategy**: compete head-on in an existing category, take a sub-segment of it, or create a new category. Choose head-on only when you are clearly better on what that category's buyers weigh most.

**Jobs to be done.** Describe the job as a situation, a motivation and a desired outcome. Map the **four forces of progress**: push of the current situation and pull of the new solution (both drive change); anxiety about the new and habit of the old (both resist change). Competitors are whatever else gets hired for the job, not only products in your category.

**Product-market-fit survey test.** Ask active users: "How would you feel if you could no longer use this product?" with options very disappointed, somewhat disappointed, not disappointed (and a "no longer use" option). Share answering "very disappointed" of 40% or more is the commonly used reference point for fit; check it against your own category and sample (at least about 40 responses, reference point). If below, read the "very disappointed" group to learn what they value and who they are, split the "somewhat" group by whether they like the core benefit, and fix the top blocker, then retest.

**Output:** filled six-component positioning / alternatives map / differentiation with evidence / category recommendation / fit assessment with an improvement plan (if data exists) / interview guide for primary research (if data is missing: ask about the last time they switched, what triggered it, what they considered, what almost stopped them).

## Mode 4: Architect

**Intake (guided):** which product against which competitor(s); the differentiation angle (or run a quick Strategist pass); the audience (evaluators, switchers, researchers); available proof (ratings, testimonials, cases); target search phrases (or find them).

**Page types:** head-to-head (one competitor), alternatives (a list with ours placed fairly), hub (many-to-many comparison), category comparison.

**Steps**
1. Set page strategy: target phrase, search intent, conversion goal.
2. Build the comparison around buyer outcomes, not a raw feature checklist. Include rows where the competitor wins.
3. Add proof with a clear source and date, and a switching section that answers the anxiety and habit forces (migration effort, data export, support).
4. Add SEO notes: one primary phrase in title, H1 and first paragraph; descriptive meta description; schema where it fits; internal links to the product page; a review date so the page stays current.
5. Run the **anti-pattern check** before delivery:
   - no attacks on the competitor, no claims about them you cannot source and date
   - no unproved superlatives ("best", "fastest") without a measure
   - no table where we win every row
   - no stale pricing or feature data without a "checked on" date
   - no thin page that restates the product page; it must help a buyer decide
   - no trademark misuse or implied endorsement
6. Output the brief with the comparison-page template in `assets/templates.md`.

## Handoffs (soft; any agent can read them)

When research should feed another skill, end with a block like this and let the user paste it anywhere. If the receiving skill is not installed, the block works as a standalone brief.

```
HANDOFF
From: market-researcher (<mode>)   To: <copywriting | brand | SEO content | strategy | lead generation>
Goal: <what the receiver should produce>
Key findings: <3 to 5 tagged points>
Positioning or angle: <one line, or the six components>
Evidence to use: <figures, quotes, proof, with source tags and dates>
Competitor facts to respect: <strengths we must not misstate>
Banned: <attacks, unsourced claims>
Open gaps: <what is still unknown>
```

Typical routes: comparison brief to a copywriting skill; positioning to a brand skill; keyword and content gaps to an SEO content skill; sizing and landscape to a strategy skill; customer language and job insights to a lead generation skill. Use those skills if installed; otherwise do the step in place.

## When not to use

- Writing the final copy: use a copywriting skill.
- Voice and identity: use `brand-architect` if installed.
- Segment, target and positioning as a full marketing strategy: use `stp-marketing-strategy` if installed.
- Financial projections: use a financial-modelling skill.
- Choosing one niche from many options: use `niche-finder` if installed.

## Quality bar

- Every number has a tag and a date; critical numbers have two sources or a stated single-source warning.
- Tables are filled, not templates.
- Competitor strengths appear in every competitor output.
- SWOT items could not apply to any company by swapping the name.
- Positioning has all six components; comparison pages pass the anti-pattern check.
- Assumptions are labelled; confidence and data gaps are explicit.
- No filler words such as "leverage", "robust", "game-changer", "holistic"; say the concrete thing.

## Output rules

- End with a concrete next step (a decision, a data request, an interview to run, or a handoff).
- Label assumptions and illustrative numbers.
- Save as a new Google Doc, Sheet or Slides if a connection exists; otherwise reply in the conversation. Never overwrite an existing file.
- Never publish a page, send material to sales or customers, or spend money without the user's go-ahead.
- Optional visual layer: offer a diagram (nested sizing circles, Five Forces map, competitor positioning chart) via the `visual-thinking` skill if installed, otherwise a plain-text table.
