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

## starter additions

| Skill | Source | Licence | Notes |
|---|---|---|---|
| `skill-spec-generate` | Masonshare (own design: keep the why of a skill apart from the skill) | none (ideas only) | Lives in `packs/starter/mango-spring-roll/skills/` |
| `agentic-vibe-working` | Six-step framework (define, research, plan, execute, verify, package) from the Agentic Vibe Working programme by Neurons-AI (session 02, a paid course); rebuilt in our own words. The idea of re-reading a checkbox plan after context compaction was borrowed from a tool kit of the same programme (vibecodekit); only that idea is kept. Skill packaging rules follow the Agent Skills specification. The safety checkpoint, evidence-based verification and conditional skill calls are Masonshare's own additions | Course material, no licence (ideas only) | Rewritten from scratch; the recovery script is our own code. The tool kit's licence was not verified, and none of its code was copied |
| `workflow-ai-agents` | Masonshare's own skill, based on the Agentic Vibe Working programme by Neurons-AI (session 06, the master blueprint part): research chain, workflow, packaging, agent; single-purpose agents that refuse out-of-scope work. The identify step (Go or No-go) is Masonshare's own addition | Course material, no licence (ideas only) | Rewritten around an agent blueprint; the earlier industry examples and evals were not carried over |
| `luu-vao-notion-second-brain` | Masonshare (new skill; the rules are the owner's). The expected workspace shape (notes, tasks, projects, goals, people, plans) follows the ready-made Notion template Ultimate Brain by Thomas Frank, which the owner uses; the skill contains none of the template's content | none (ideas only) | Optional storage module; other skills may point to it as a soft suggestion |
| `skill-write (`references/from-topic.md`)` | The knowledge, systems thinking, workflow, skill packaging chain of an earlier distilling skill, taken from session 04 of the Agentic Vibe Working programme (Neurons-AI); only the useful ideas were moved into a new reference file. The earlier skill and its working folder of course material are not shipped | Course material, no licence (ideas only) | Added to an existing starter skill, with one row in its Route table |

## Third-party code copied with its licence

Code written by others and copied into a pack as is. The folder keeps its `LICENSE` file and copyright line unchanged; `scripts/check-skill-neutral.py` skips a folder that holds a `LICENSE`.

| Folder | Author | Licence |
|---|---|---|
| `packs/marketing-ecommerce/skills/watch` | Bradley Bonanno (repository `bradautomates/claude-video` on GitHub) | MIT, copyright 2026 Bradley Bonanno; the `LICENSE` file is kept unchanged and no file was edited |

## Linked only, not copied

Tools and skills the docs point to but this repo does not include.

| Name | Why not copied |
|---|---|
| `skill-creator` (Anthropic skill, repository `anthropics/skills` on GitHub; Apache-2.0 per the licence file we saw; original source not verified from this machine) | Relies on sub-agents and the `claude -p` command, and overlaps `skill-write` and `skill-test` in the Starter pack; install it from its own repository if wanted |
| `distilly` (repository `titanwings/distilly` on GitHub; MIT, copyright 2026 titanwings; a `CITATION` file asks users to cite its technical report by Tianyi Zhou, Dongrui Liu, Leitao Yuan, Jing Shao and Xia Hu) | An independent project of over a hundred files with its own tools; it serves a different purpose, so it is linked here only |

## Tools called from outside

Command-line tools a skill asks the user to install (not shipped here).

| Tool | Used by |
|---|---|
| `yt-dlp` (command-line tool, not shipped here; its licence has not been verified from this machine) | `youtube-digest` |
