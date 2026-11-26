# journey-mapper

## What it does

Maps the full customer journey from stranger to advocate, finds where customers leak out, and routes each fix to the right specialist with a handoff block any agent or person can read. Three modes picked from the request: lifecycle mapper (stages, touchpoints, moments of truth, gaps), leak finder (stage metrics, friction type, 5 whys, revenue impact, ICE ranking) and routing (leak to skill, week-by-week sequence, re-diagnosis checkpoint). Body in English, description bilingual.

Single-channel skills (email, content, UX) tune one touchpoint but do not see the whole journey. This skill looks at the whole first, finds measured leaks, then hands work to the right specialty instead of redoing it. Five journey types and six stages (AARRR-style, order adjusted per type) are kept. Diagnosis runs in order: data, reference points, drop-off, friction type, 5 whys, revenue estimate, ICE. Reference points: 3 to 5 moments of truth; flag a step where more than 50 percent leave; assume only one tenth to one third of lost customers can be recovered; ICE is three axes scored 1 to 10 and multiplied. The conversion and churn ranges in the skill are wide starting points with no source; compare them with your own history. Every number in this skill is a labelled reference point, not a fact about your market or brand; the skill asks for your own figures. Trade-off: wide ranges instead of industry-specific figures, so no unverifiable data is presented as fact.

Source: [`packs/marketing-ecommerce/skills/journey-mapper/SKILL.md`](../../packs/marketing-ecommerce/skills/journey-mapper/SKILL.md)

## When to reach for it

Someone asks to map the customer journey, audit the funnel, find where customers are lost, fix a conversion leak or drop-off, find touchpoint gaps, or decide who should fix an issue. A diagram is optional through a diagramming skill. Related skills (brand voice, SEO content, email, copywriting, lead generation, STP, UX) are soft suggestions with an in-place fallback.

## Common questions

**Does it need my funnel numbers?** It is much better with them. Without them it uses assumed recovery rates and a guessed webinar-style benchmark, both labelled.

**What is the handoff block?** A short plain-text block with brand context, constraints, expected output, and entry and exit points, readable by any agent or person.

**Does it fix the leaks itself?** It diagnoses and routes. The fixes belong to the specialist skills or people it points to.

## It's working if

- Each leak has a stage metric, a friction type and a root cause from the 5 whys.
- Leaks are ranked by ICE and carry a labelled revenue estimate.
- The routing step names who or which skill takes each fix, with a re-diagnosis checkpoint.
