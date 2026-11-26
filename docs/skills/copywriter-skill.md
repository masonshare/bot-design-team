# copywriter-skill

## What it does

Drafts and rewrites persuasive copy (landing and sales pages, headlines, ads, product descriptions, blog posts and long-form articles, email body copy, video sales letter and webinar scripts). It runs a short process: a six-item brief, a framework chosen by the reader's awareness level (AIDA, PAS, story-based, 4Ps-style), writing, a self-review checklist, then A/B variants. It never invents proof. Body in English, description bilingual. An optional helper, `scripts/copy_check.py`, prints counts, a reading-level estimate, stock-phrase hits, number claims that need a source, and open placeholders.

Sales writing usually starts from a vague request ("write me a landing page"), so the skill forces the brief first. Every draft must offer at least 3 headlines from different angles with one recommended and why. Reference points: reading level about grade 6 to 8 (a rough estimate that applies to English only); the script warns above grade 9; email subject under about 50 characters; 2 to 3 variants; a short video sales letter of 3 to 6 minutes and a long one of 15 to 60. Every number in this skill is a labelled reference point, not a fact about your market or channel; the skill asks for your own figures and does not use Vietnamese market data. Trade-off: few full worked outputs to keep SKILL.md short, made up for by templates in `templates.md`; no numeric "sounds human" score, because it encourages writing for the scorer.

Source: [`packs/marketing-ecommerce/skills/copywriter-skill/SKILL.md`](../../packs/marketing-ecommerce/skills/copywriter-skill/SKILL.md)

## When to reach for it

Someone asks to write copy for a page, a headline, an ad or a product description, to rewrite a page to be more persuasive, or to script a video. For SEO planning use `content-strategist-seo`; for email journeys use `email-specialist`; for the brand voice to follow use `brand-architect`. Links are soft.

## Common questions

**Does it need a brand voice?** No, but it reads `brand-profile.md` if you have one (template in `packs/marketing-ecommerce/`) and follows the voice section.

**Do I need Python for the helper?** No. If a shell with Python 3 is available it runs `copy_check.py`; otherwise it runs the same checklist by hand.

**Does the script judge quality?** No. It flags things for a person to review, and its reading level formula is for English only.

## It's working if

- The brief's six items were asked or confirmed before drafting.
- The answer has at least 3 headline options from different angles, one recommended with the reason.
- Every claim with a number or a guarantee has a source or is marked as needing one.
