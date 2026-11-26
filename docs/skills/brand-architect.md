# brand-architect

## What it does

Defines a brand or personal voice and packages it as a portable "Voice DNA": a copy-paste system prompt, a do and don't table, voice sliders, and a handoff block that writing skills can read. Three modes are picked from the request: mirror (extract the voice from writing samples), forge (build one from scratch with archetypes and tone sliders), hybrid (extract, then adjust). The skill body is in English; the description is bilingual.

Brand voice is usually described with vague adjectives ("professional but friendly"), so every writer and every AI reads it differently. The skill turns voice into something measurable and reusable: every slider ties to an observable writing behaviour, and voice (fixed) is kept apart from tone (varies by situation). Thin samples are not refused; they get a low-confidence label. It reads the customer's `brand-profile.md` first and does not ask again for what is already there. Reference points: at least 3 samples from 2 contexts, about 2,500 words (under about 1,500 words means low confidence); 5 to 7 standout traits; 5 sliders on a 1 to 10 scale; 3 to 5 main message attributes. Every number in this skill is a labelled reference point, not a fact about your market or brand; the skill asks for your own figures. Trade-off: it skips deep linguistic analysis (function-word counts, detailed classification) so it runs on any platform without measuring tools.

Source: [`packs/marketing-ecommerce/skills/brand-architect/SKILL.md`](../../packs/marketing-ecommerce/skills/brand-architect/SKILL.md)

## When to reach for it

Someone asks to extract their writing style, build a brand voice, "sound like me", define tone of voice or a brand persona. It feeds the writing skills in the pack (copywriting, email, SEO content, social content); for who the customer is, use `market-researcher`, and for positioning use `stp-marketing-strategy`. Those links are soft: the skill works without them.

## Common questions

**Does it need a brand profile?** No, but it reads `brand-profile.md` first if you have one (template: `packs/marketing-ecommerce/brand-profile-template.md`) and asks only for what is missing.

**What if I have only one short writing sample?** It still works and labels the result low confidence, and says what more samples would fix.

**What do I get at the end?** A copy-paste system prompt, a voice chart, and a handoff block; paste the prompt into any writing tool or agent.

## It's working if

- The output ends with a copy-paste system prompt, a voice chart and a handoff block.
- Every voice slider is tied to a writing behaviour you can check in a sample.
- Thin input gets a low-confidence label instead of a refusal or false certainty.
