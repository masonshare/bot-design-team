---
name: brand-architect
description: Define a brand or personal voice and package it as a portable "Voice DNA" - extract the voice from writing samples (mirror), build one from scratch with archetypes and tone sliders (forge), or analyse then tune (hybrid) - and end with a copy-paste system prompt, a voice chart and a handoff block for writing skills. Use for "extract my writing style", "build a brand voice", "sound like me", "tone of voice", "brand persona". Tiếng Việt - xác định giọng thương hiệu hoặc giọng cá nhân, đóng gói thành bộ chỉ dẫn giọng văn dùng lại được ("rút giọng văn của tôi", "xây giọng thương hiệu", "viết giống tôi").
---

# Brand Architect

## What it does

It turns a voice into something a person or an AI can reuse: a **Voice DNA**, meaning a short system prompt, a do-and-don't voice chart, and measurable settings. The system prompt is the product; everything else supports it.

If the client already keeps a `brand-profile.md` (name, positioning, audience, tone, limits), read it first and treat it as the starting point. Do not re-ask what it already answers. If this skill produces or sharpens a voice, offer to write the result back into section 3 (voice) of that profile as a new draft, never overwriting the file.

## Choose the mode from the request (do not list all modes up front)

| The user says | Mode |
|---|---|
| "analyse my writing", "extract my voice", pastes samples | **Mirror**: reverse-engineer a voice from samples |
| "build a brand voice", "create a persona", "I need a voice from scratch" | **Forge**: construct a voice |
| "keep my style but make it more X", "evolve my voice" | **Hybrid**: Mirror first, then tune |
| "give me a system prompt for my voice" | Any mode, make sure the output ends with the system prompt |

If it is unclear, ask one routing question: "Do you have writing samples to analyse, or are we building from scratch?"

Depth keywords the user may say: **express** (one clarifying question at most, deliver fast), **guided** (default: 3 to 5 intake questions, confirm approach, deliver in full), **deep** (full diagnostic, show reasoning, variants, scenario adjustments). If unspecified: a clear request with samples is express, a broad "help me build a brand voice" is guided.

## Mirror: extract a voice from samples

**Samples:** at least 3 pieces, ideally 2,500+ words, from 2 or more contexts (for example a blog post and a message to a customer). With under about 1,500 words, continue but mark the affected features **low confidence**. Never refuse for thin data.

**Steps**
1. **Measure the surface.** Sentence length and its spread, paragraph length, vocabulary level, favourite connecting words, pronoun use (you versus I versus we), punctuation habits, how sections open, share of fragments and questions, a readability score.
2. **Separate what is personal from what is just the genre.** Some features come from the medium (a product page is short and punchy) or the writer's role. Keep only features that would still show in a different genre. These are the distinctive ones.
3. **Pick the top 5 to 7 distinctive features**, each with a number or a pattern, never an adjective alone.
4. **Place the voice**: one primary archetype (and an optional secondary, as a percentage split), and the five tone sliders below.
5. **Score confidence** by convergence: if several independent feature groups point the same way, confidence is higher; if they disagree, say so and lower it.
6. **Assemble the Voice DNA** with `assets/identity-matrix-template.md`.

## Forge: build a voice from scratch

**Intake (guided):** who the audience is; the emotional job (what should they feel after reading); two or three voices the client admires, in any industry; a voice that would make them cringe; where the voice appears most (product pages, email, social, support).

**Steps**
1. **Message architecture** via a three-round sort: attributes that describe the brand now, attributes it is *not*, attributes it wants to become. Reduce to 3 to 5 primary attributes, a rejected list, and an aspirational list. Cap the primary list; a brand that is everything is nothing.
2. **Archetype.** Choose one of the 12 classic archetypes (innocent, explorer, sage, hero, outlaw, magician, everyman, lover, jester, caregiver, creator, ruler), optionally blended ("70% sage, 30% outlaw" means wise but challenging). Archetypes are a thinking aid; they must end up as behaviours, not labels.
3. **Personality profile.** Score the five brand-personality dimensions (sincerity, excitement, competence, sophistication, ruggedness) from 1 to 10. Two should clearly dominate.
4. **Tone sliders (1 to 10)** and what each means in writing:
   - Accessibility: academic (1) to casual speech (10)
   - Empathy: clinical (1) to warm and supportive (10)
   - Energy: calm (1) to high voltage (10)
   - Structure: free-flowing (1) to rigid and linear (10)
   - Directness: diplomatic (1) to blunt (10)
5. **Voice chart.** 3 to 5 characteristics, each with a "do this" example and a "don't do this" example.
6. **Readability target** as a score range suited to the audience.
7. **Assemble** the Voice DNA and validate (below).

In deep mode add the scenario adjustment matrix: how the sliders shift in a crisis, a launch, and customer support, while the voice stays recognisably the same. Voice is constant; tone flexes.

## Hybrid

Run Mirror, show the extracted settings, ask "which dimensions do you want to shift, and which way?", apply the shift and predict the concrete linguistic effect of each change, then output baseline versus target with before-and-after example sentences.

## Every output must

1. **End with the system prompt** in a copy-paste block (see the template).
2. **Tie every slider to behaviour.** "Energy 8" must mean something measurable: sentence length, share of exclamations, density of active verbs.
3. **Pass the cover test.** Hide the persona tagline; if the voice could belong to any brand, it fails. Sharpen and redo.
4. **Score confidence** in Mirror and Hybrid, and flag low confidence instead of hiding it.
5. **Offer validation**: write a test paragraph in the voice so the user can hear it. Never skip this offer.
6. **Avoid empty words**: no "find your authentic voice" without method, no "professional yet approachable", no personality adjectives (bold, fresh, innovative) without turning them into writing behaviours. Treat voice (constant identity) and tone (how it adapts) as different things.

## Handoff to writing skills

When the result will be used by another skill (a copywriting, email, SEO content or social skill), finish with the handoff block from the template. The user can paste it into a new conversation. If a skill is not installed, the block still works as a standalone brief.

## Soft suggestions (use if installed, otherwise do the step in place)

- `market-researcher` for competitor voices and audience personas as input to the sort.
- `stp-marketing-strategy` for positioning and the target job.
- `journey-mapper` for lifecycle stages that feed the scenario adjustments.

## When not to use

- A single piece of copy, an ad or an email: use the matching writing skill (after this skill if a voice does not exist yet).
- A full strategy or positioning decision: use `stp-marketing-strategy` or a strategy skill.
- A logo, colours or visual identity: out of scope; this skill covers language only.

## Style of the output

Direct, concrete, numbers over adjectives. Keep examples synthetic (invented brands and sentences); never reproduce a real company's copy. Express output is lean; deep output shows the reasoning. Save as a new Google Doc if a connection exists, otherwise reply in the conversation; never overwrite an existing file.
