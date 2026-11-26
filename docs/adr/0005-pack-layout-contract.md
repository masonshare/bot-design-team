# 0005. Pack layout contract

Status: Accepted

## Context

Parallel tickets broke each other: the CI frontmatter rule hard-coded one pack layout while the pack tickets used another, and CI only went red after the merge (retro #30). This ADR is the single place that states the layout. CI rules and pack tickets both reference it. Builds on ADR 0001.

## Decision

For a pack `packs/<pack>/`:

| Thing | Location |
| --- | --- |
| Pack-level skill | `packs/<pack>/skills/<name>/SKILL.md` |
| Bot-level skill (bot-home form) | `packs/<pack>/<bot>/skills/<name>/SKILL.md` |
| Bot soul | `packs/<pack>/<bot>/SOUL.md` |
| Docs page for every pack skill | `docs/skills/<name>.md` (flat, one per skill name, with the four sections: What it does, When to reach for it, Common questions, It's working if) |
| Fake data | `packs/<pack>/fake-data/`, files named `FAKE-*` |
| Scenarios | `packs/<pack>/scenarios/<ticket>-<slug>.md`, must contain `FAKE` |
| Scenario results | `packs/<pack>/scenarios/results/<agent>-<date>[-note].md` |

Rules:

1. A `SKILL.md` anywhere under `packs/` must sit at one of the two skill paths above. Any other depth or folder is rejected.
2. In every `SKILL.md`, frontmatter `name` equals the skill's directory name, and `description` is present.
3. Every pack skill has its docs page at `docs/skills/<name>.md`. Because docs pages are flat, a skill name must not be reused by another skill.
4. Fake data and scenarios hold FAKE data only (ADR 0003).
5. (Void since ADR 0006.) There are no repo-level skills outside packs.

## Enforcement

- `scripts/check-frontmatter.py`: rules 1, 2, 5.
- `scripts/check-layout.sh`: rule 3 and the buckets of rule 5.
- `scripts/check-no-real-data.py` and `scripts/check-scenarios.sh`: fake data, scenarios.
- `scripts/check-columns.py`: the `Kịch bản` / `Đề xuất` column lists agree across the template, FAKE CSV headers and `run-scenarios.py`.
- `scripts/check-glossary-avoid.py`: terms under `## Avoid` in `GLOSSARY.md` do not appear in `.md` files (ADRs exempt).
- `scripts/check-no-build-artifacts.sh`: no tracked `__pycache__/` or `*.pyc`.
- `scripts/check-soul-rules.py`: bot SOULs point at their skills and do not restate sheet columns or status vocabulary.
- `scripts/tests/run.sh`: one failing case per rule.

To change the layout: change this ADR first, then the checks and their failing-case tests in the same change, and announce it to open tickets before merging.
