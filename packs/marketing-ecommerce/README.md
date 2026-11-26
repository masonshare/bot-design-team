# Pack: marketing-ecommerce (marketing and e-commerce skills)

A set of skills for marketing and selling online: reading e-commerce numbers, planning channels and products, and later brand voice, copy, SEO, ads, email and conversion. The skills are written to be neutral, so they run on Claude Code and on Codex.

Needs the Starter pack first (`packs/starter/`): install it before this one.

This pack is filled in batches. What is in it now is listed below; each skill has a docs page in `docs/skills/`. Sources and licences are in `docs/credits.md`.

## What is in the pack

```
packs/marketing-ecommerce/
  README.md                     this file
  brand-profile-template.md     the customer's brand profile, one file the skills read
  fake-data/                    FAKE sample data (FAKE-brand-profile.md)
  skills/<name>/SKILL.md        pack-level skills (ADR 0005)
```

| Skill | Docs |
|---|---|
| `ecommerce-kpi-analytics` | [docs/skills/ecommerce-kpi-analytics.md](../../docs/skills/ecommerce-kpi-analytics.md) |

## The customer's brand profile

Skills that need to know the brand (voice, audience, products, limits) read one file, `brand-profile.md`, instead of carrying any company's details. Copy `brand-profile-template.md`, fill it in, and keep it where you like (Google Docs by default). `fake-data/FAKE-brand-profile.md` shows a filled-in example with invented data.

## Rules for skills in this pack

Skills here use no tool names tied to one agent, no machine paths, no real company names and no URLs. `scripts/check-skill-neutral.py` enforces it. How a rewritten skill is imported (`scripts/import-skill.py`) is in `CONTRIBUTING.md`.

Everything in this folder that looks like company data is FAKE.
