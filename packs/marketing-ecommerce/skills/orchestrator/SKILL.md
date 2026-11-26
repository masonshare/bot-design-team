---
name: orchestrator
description: Navigator and router for the marketing and e-commerce skill pack - picks the right skill for a request (router), sequences several skills into a phased plan for a project (planner), and checks which skills a project is missing and what to do first (diagnoser). Use when the user asks "which skill should I use", "where do I start", "help me plan a launch / campaign / shop growth / content month", "what should I do next", or describes a marketing, brand, copy, content, funnel, ads or online-shop task without naming a skill. Skip it when the user already names one skill. Tiếng Việt - điều hướng skill cho bộ marketing và thương mại điện tử - chọn đúng skill cho một việc, xếp lộ trình nhiều skill cho một dự án, hoặc rà xem dự án còn thiếu skill nào ("nên dùng skill nào", "bắt đầu từ đâu", "lập kế hoạch ra mắt", "làm gì tiếp theo").
---

# Orchestrator

## What it does

This skill coordinates; the other skills execute. It has three modes and always ends with a concrete next step:

- **Router**: one request, one skill. Fast.
- **Planner**: a goal that needs several skills, turned into an ordered plan with deliverables and decision gates.
- **Diagnoser**: the user says "we have X, what is missing?" or "where do I start?". Check what exists, name the gap, then route or plan.

Say a keyword to choose how deep to go: **express** (match now, almost no questions), **guided** (default, short intake first), **deep** (multi-skill project with gates and handoff blocks).

If the user names a skill, go straight to it. If the user asks "list all skills", give the short table below, not long descriptions.

## Skills in this pack

Only these skills exist in the pack. Never recommend a name that is not on this list as if it were installed.

| Group | Skills |
|---|---|
| Research and direction | `market-researcher`, `stp-marketing-strategy`, `niche-finder`, `journey-mapper` |
| Brand and writing | `brand-architect`, `copywriter-skill`, `copywriter-choi-chu` |
| Channels and content | `content-strategist-seo`, `email-specialist`, `lead-gen-expert`, `social-content-specialist` |
| Conversion and ads | `cro-specialist`, `paid-ads-strategist` |
| E-commerce | `ecommerce-channel-strategy`, `ecommerce-product-strategy`, `ecommerce-store-optimization`, `ecommerce-image-design`, `ecommerce-promotion-design`, `ecommerce-kpi-analytics` |
| Product and documentation | `new-product-development`, `playbook-documentation` |
| Video | `video-script-vn`, `tui-kich-ban`, `youtube-digest`, `watch` |
| Navigation | `orchestrator` (this skill) |

One-line scope for each skill, plus handoffs, is in `references/ecosystem-map.md`. Read it when two skills look close.

## Brand context first

If the client keeps a `brand-profile.md` (name, positioning, audience, tone, products, limits), read it before routing and do not re-ask what it answers. If it does not exist and the request involves brand, copy or audience, ask once, then suggest `brand-architect` to create it.

## Intake (guided mode)

Ask once, each question with a default the user can accept, and skip any already answered:

1. Goal: what outcome, by when? (default: the outcome stated in the request)
2. Stage: idea, building, scaling or fixing? (default: building)
3. Assets: brand voice, audience research, copy, shop pages, data? (default: nothing yet)
4. Constraints: budget, platform, language, team size? (default: none stated)
5. Execution: one conversation or several? (default: one)

Then pick the mode: one task means Router; several dependent tasks means Planner; "I have this, what is missing" or "I am new" means Diagnoser.

## Mode 1: Router

1. Match the request using the routing table.
2. Reply with: recommended skill, one sentence on why, which mode or keyword to use inside it, what to bring (inputs), and what it hands off to next.
3. If two skills fit, name a primary and a secondary and say which to try first. Stop there.

### Routing table by request type

| The user wants to... | Route to | Notes |
|---|---|---|
| Size a market, profile competitors, run SWOT or Five Forces | `market-researcher` | Evidence before strategy |
| Segment customers, choose a target, write a positioning statement | `stp-marketing-strategy` | Uses Jobs To Be Done |
| Choose one niche among many options | `niche-finder` | Needs research, journey and brand inputs |
| Map the customer journey or find where customers leak | `journey-mapper` | Routes each leak to a specialist |
| Define or extract a brand voice | `brand-architect` | Run before any copy |
| Write persuasive copy (page, ad, article, email body) | `copywriter-skill` | Needs voice and brief |
| Vietnamese slogan, name, caption, wordplay | `copywriter-choi-chu` | Vietnamese wording specialist |
| Plan SEO content, topic clusters, briefs, refresh content | `content-strategist-seo` | Hands briefs to the copywriter |
| Plan email journeys, welcome, cart recovery, win-back | `email-specialist` | Drafts only |
| Lead magnet, opt-in, list growth | `lead-gen-expert` | Pairs with email |
| Social calendar, posts, repurposing | `social-content-specialist` | Drafts only |
| Why a page or checkout does not convert; A/B test design | `cro-specialist` | Needs real page or data |
| Paid ad structure, creative, budget rules | `paid-ads-strategist` | Planning only, never spends |
| Which marketplace or channel to sell on | `ecommerce-channel-strategy` | By business stage |
| Product range roles, combos, what to sell first | `ecommerce-product-strategy` | Portfolio view |
| Fix product, category, search or shop pages | `ecommerce-store-optimization` | Checklist per page |
| Product images, banners, image prompts | `ecommerce-image-design` | Prompts first |
| Discounts, vouchers, sale campaigns, profit check | `ecommerce-promotion-design` | Computes real margin |
| Sales dropped, GMV, conversion, order value, stock | `ecommerce-kpi-analytics` | Diagnose then act |
| Develop a new physical product to launch | `new-product-development` | Phases with gates |
| Turn a process into an SOP or playbook | `playbook-documentation` | For people who run it later |
| Vietnamese video script, short or long | `video-script-vn` | Execution of scripts |
| Script theory: hook, formula, idea matrix | `tui-kich-ban` | Theory, hands off to `video-script-vn` |
| Summarise a YouTube video from its transcript | `youtube-digest` | Words only, cheap |
| Understand what is shown in a video, not just said | `watch` | Frames plus transcript, heavier |
| "What next?" or "which skill?" | `orchestrator` | You are here |

## Mode 2: Planner

1. Match the goal to an archetype in `references/project-archetypes.md` (launch a product, grow an online shop, build a brand, run a content month, and others) or build a custom sequence.
2. Fix the order using the dependency rules below.
3. Per phase give: skill, objective, deliverable, "move on when", and any decision gate.
4. Cut phases the user already has (assets from intake). A plan of 3 to 5 skills beats a plan of 10.

Output shape:

```
# Plan: [project]
Type: [archetype or custom] | Phases: [n] | Execution: [one conversation / several]

Phase 1: [skill] - objective - deliverable - move on when ...
Phase 2: ...

Decision gates: after phase [n], decide [x] or [y]
Skipped on purpose: [skills] because [reason]
Next step: start phase 1 by [exact action]
```

### Dependency order

The default spine is: research, then positioning, then brand voice, then planning, then copy, then channel work, then conversion and ads, then measurement.

- Brand voice (`brand-architect`) comes before copy (`copywriter-skill`, `copywriter-choi-chu`), unless the user has no time: then write copy and flag it as provisional.
- Audience and positioning (`market-researcher`, `stp-marketing-strategy`) come before brand voice and ads.
- Content plan (`content-strategist-seo`) comes before writing the articles it briefs.
- Lead magnet (`lead-gen-expert`) comes before the email sequence that delivers it.
- Landing page audit (`cro-specialist`) comes before paid traffic is pointed at the page.
- Channel choice (`ecommerce-channel-strategy`) comes before shop pages, images and promotions.
- Numbers (`ecommerce-kpi-analytics`) go before and after any promotion, so the result can be read.
- A diagnosis step (`journey-mapper`, `ecommerce-kpi-analytics`) comes before fixes when something is underperforming.

## Mode 3: Diagnoser

Use when the user has something running and asks what is missing, or is new and unsure.

1. Ask three things: what the business sells and to whom; the biggest problem right now (no direction, no brand, no content, no leads, traffic without orders, sales falling); what already works.
2. Map the problem to a first skill:

| Problem | First skill | Then |
|---|---|---|
| No direction or unclear target | `stp-marketing-strategy` | `market-researcher` if evidence is thin |
| No brand voice | `brand-architect` | `copywriter-skill` |
| No content plan | `content-strategist-seo` | `social-content-specialist` |
| No leads | `lead-gen-expert` | `email-specialist` |
| Traffic but few orders | `cro-specialist` or `ecommerce-store-optimization` | `ecommerce-kpi-analytics` |
| Sales dropping on a marketplace | `ecommerce-kpi-analytics` | `ecommerce-promotion-design` |
| Customers drop out somewhere unknown | `journey-mapper` | the specialist it names |
| Need ads | `paid-ads-strategist` | `cro-specialist` for the landing page |
| New product idea | `new-product-development` | `ecommerce-channel-strategy` |

3. Return 3 to 5 skills in order, what each produces and feeds, a short "skip for now" list, and when to come back.

## Handoff rules

- Pass the output of one skill to the next as a short handoff block: goal, audience, voice rules, decisions made, open questions. Any agent can read it; do not rely on hidden state.
- Several conversations: add a context brief per phase (what is done, what is decided, what the next skill must not redo).
- Never pass raw research dumps; pass conclusions and the evidence labels.
- After a skill finishes, if the user asks "what next", route again from the plan instead of starting over.
- Hand off to a skill only once; do not bounce work back and forth.

## When no skill fits

Do not force an approximate match. Say so in one line, name the closest skill and what it does not cover, then offer one of: do the task in place with plain reasoning, or, to build a reusable skill for it, use a skill-design skill if installed.

Optional soft suggestions, only if installed and relevant: company strategy, business model, financial model, fundraising or negotiation requests go to `business-strategist`, `winning-business-model`, `startup-financial-modeling`, `startup-metrics-framework`, `startup-analyst`, `pricing-strategist`, `pitch-bod-bos-dt` or `elite-negotiator`; problem diagnosis to `problem-solver-skill` or `system-thinking`; talks to `thuyet-trinh-winston`; premium experience design to `thiet-ke-trai-nghiem-cao-cap`; diagrams to `visual-thinking`. If none is installed, say this area is outside the pack and give a plain answer or a neutral brief.

Offer a diagram of the plan via the `visual-thinking` skill if installed, otherwise a plain-text table.

## Output rules

- End every reply with one concrete next step (which skill, with what input).
- Label assumptions, such as stage or budget you guessed.
- Save a plan as a NEW Google Doc or Sheet if a connection exists; otherwise reply in the conversation. Never overwrite an existing file.
- Never send, publish, spend money or change anything outside the conversation without the user's go-ahead.

## Quality bar

1. Only skills from the pack table are named as available; the soft suggestions are marked "if installed".
2. One skill when one is enough; no roadmap for a single task.
3. Order respects the dependency rules, and every phase has a deliverable and a "move on when".
4. No more than 5 skills in a first plan for a new user.
5. Every handoff states what is passed, not only who receives it.
6. Done when the user knows which skill to open next and what to bring.

## When not to use

- The user names the skill: go to it directly.
- The request is deep in one skill's domain (for example "write this headline"): use that skill.
- The request is company-level strategy, finance or fundraising: see the soft suggestions above.
