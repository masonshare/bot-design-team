---
name: niche-finder
description: Pick one niche to commit to from a broad market map - scores 3 to 5 candidate niches on five criteria using the user's existing strategy, market, customer-journey and brand material, then recommends one with risks and handoffs. Use when the user has many options and must choose one before planning ("which niche", "narrow our focus", "pick a market", "scored shortlist"). Tiếng Việt - chọn một ngách để đầu tư từ bản đồ thị trường rộng, chấm điểm 3 đến 5 ngách theo 5 tiêu chí rồi khuyến nghị một ngách ("chọn ngách nào", "thu hẹp thị trường", "chọn phân khúc để tập trung").
---

# Niche Finder

## What it solves

Strategy and research work usually ends with a flat list of opportunities: gaps in the market, customer groups, weak spots in the customer journey. Plans built on a flat list stay diluted and execution loses focus. This skill is the bridge between "we mapped the market" and "we bet on this specific corner of it".

It is a **synthesis** skill. It does not research new data. It reads what already exists, extracts candidate niches, scores them, and recommends one.

## Keywords for modes

Say one of these words to pick a mode (the user does not need slash commands):
- **express**: score and shortlist right away, minimal questions.
- **guided** (default): ask three short questions first, then score.
- **rubric**: just show the five-criteria scoring table.

## Required inputs (stop if missing)

Do not score on guesswork. Ask for all four, or accept an equivalent document pasted in the chat:

1. **Strategy and market map**: where the white spaces and competitive structure are.
2. **Market intelligence**: market size, growth, competitor comparison, customer segments.
3. **Customer journey**: funnel, drop-off points, where customers get stuck.
4. **Brand profile**: positioning and voice limits. If the client has a `brand-profile.md`, use it.

If something is missing, say exactly which one and what to provide (or offer to produce a rough version with the matching skill if it is installed: `business-strategist`, `market-researcher`, `journey-mapper`, `brand-architect`). Missing inputs make scores unreliable, so state that plainly.

## Scoring rubric

Five criteria, each 1 to 5, total 25.

| Criterion | What to look at | Where the evidence comes from |
|---|---|---|
| Strategic fit | Match with positioning, brand voice limits, and permission to play | Brand profile, strategy |
| Market attractiveness | Size, growth, buyer power (low is attractive), how many substitutes | Market intelligence |
| Defensibility | Durable-advantage sources: switching cost, network effect, scale, brand, cornered resource, counter-positioning, process power | Strategy |
| Speed to revenue | Time to first customer, capital need, sales cycle length | Strategy, journey |
| Founder-market fit | Existing skills, capital, certifications, relationships, assets | Brief, strategy |

Tiers: 20 to 25 strong (recommend); 15 to 19 viable (watch list); under 15 reject.

Every score cites specific evidence from a named input. Opinions without a source do not count.

## Workflow

1. **Read the four inputs.** Pull niche candidates from the white spaces, customer segments from the market work, funnel-specific openings from the journey, and voice or permission limits from the brand profile.
2. **List 5 to 8 candidates.** Merge duplicates (one niche with two names is one niche). Drop any candidate that breaks the brand limits or that no input supports.
3. **Score the best 3 to 5.** Fill one row per niche, cite evidence per cell, sum, sort high to low. Optionally offer a radar chart with five axes (one line per niche) to show which niches are even and which are lopsided. Draw it with `visual-thinking` if installed, otherwise a plain text table.
4. **Write a short defensibility note per niche.** Use your own judgment, or hand it to `business-strategist` if installed. Each note is four short paragraphs: industry-forces summary (Five Forces), durable-advantage view, trend alignment, residual risks.
5. **Package the result** in the structure below.

## Output structure

```
# Niche selection: [project]

## Summary
[2-3 sentences: recommended niche, score, one-line reason]

## Scored shortlist
| Niche | Fit | Market | Defensibility | Speed | Founder | Total | Tier |

## Per-niche notes
### [Niche A] (score X/25)
Industry forces: ...
Durable advantage: ...
Trend alignment: ...
Residual risks: ...

## Recommendation
Pick: [niche]
- three bullets tied to the scores and notes
(Optional: a 2x2 chart, market attractiveness against founder-market fit, showing where the pick and the rejected niches sit.)

## Risks and open questions
- What must be true for this niche to win
- What would kill it
- Data gaps to close before planning

## Handoff to planning
- Ads: target persona is ...
- Content: topic clusters anchor on ...
- Email: lifecycle stages follow ...
- Lead generation: the lead magnet solves ...
```

## Guided mode: three questions

Ask once, each with a default the user can accept:
1. Strongest constraint: capital, skills, or time to revenue? (default: time to revenue)
2. Any candidate the founder has already ruled in or out?
3. Decision horizon: this week, this month, or this quarter?

Use the answers to break ties and to flag any overriding constraint.

## Quality bar

1. Every score cell cites evidence from a named input.
2. Every per-niche note names at least one framework used.
3. The recommended niche is the top scorer unless a stated constraint overrides it (for example the founder rejects it on principle). State the override.
4. The risks section is never omitted.
5. The handoff gives the next skill concrete instructions, not generic remarks.
6. Avoid vague claims: no "high potential" without a number, no "underserved" without a count of substitutes, no "growing fast" without a growth rate.

## Related skills (soft suggestions, never required)

Use if installed, otherwise do the step in place: `business-strategist` (defensibility notes), `market-researcher` (market inputs), `journey-mapper` (journey inputs), `brand-architect` (brand profile), `visual-thinking` (charts). Handoff targets after the pick: `paid-ads-strategist`, `content-strategist-seo`, `email-specialist`, `lead-gen-expert`.

## When not to use

- The user wants the whole market mapped: use market research or strategy skills first.
- Competitive analysis of one niche only, or persona detail for one niche: use those skills directly.
- The user wants copy or positioning text: use a copywriting skill.
