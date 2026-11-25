# Repo map

One page: where things live. Steering files point here; `scripts/check-repo-map.sh` fails CI if a path below stops existing. The pack layout rules are in `docs/adr/0005-pack-layout-contract.md`.

| What | Where |
|---|---|
| Steering file for agents (same bytes in both) | `AGENTS.md`, `CLAUDE.md` |
| Domain terms (and terms to avoid) | `GLOSSARY.md` |
| Decisions | `docs/adr/` |
| Agent workflow docs (tracker, labels, dispatch) | `docs/agents/` |
| Design skills (promoted) | `skills/design/<name>/SKILL.md` |
| Skills being written, retired skills | `skills/in-progress/`, `skills/deprecated/` |
| One docs page per promoted or pack skill | `docs/skills/<name>.md` |
| Design bots (EN, VI) | `bots/`, `bots/vi/` |
| Packs | `packs/<pack>/` |
| Pack bot homes (SOUL.md and skills) | `packs/<pack>/staff/`, `packs/<pack>/editor/` |
| FAKE sample data | `packs/<pack>/fake-data/` |
| Behavioural scenarios and results | `packs/<pack>/scenarios/`, `packs/<pack>/scenarios/results/` |
| Sheet template, voice guide | `packs/<pack>/sheet-template.md`, `packs/<pack>/voice-guide.md` |
| CI entrypoint and checks | `scripts/ci.sh`, `scripts/check-*` |
| Failing-case tests for the checks | `scripts/tests/run.sh` |
| Scenario runner (smoke by default, `--full` explicit) | `scripts/run-scenarios.py` |
| How scenarios are run, Windows quirks | `docs/scenario-testing.md` |
| How Orca loads skills and bots (tested on one Orca version) | `docs/orca-skill-loading.md` |
| Contributing, merge gate | `CONTRIBUTING.md` |
