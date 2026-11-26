---
name: copywriter-skill
description: Draft and rewrite persuasive copy - landing pages, sales pages, headlines, ads, product descriptions, blog posts and long-form articles, email body copy, VSL and webinar scripts - with a brief intake, awareness-level targeting, framework choice (AIDA, PAS, story-based, 4Ps-style), a self-review checklist and A/B variants. Use for "write copy for", "headline for", "rewrite this page", "make this more persuasive", "copy is flat", "why doesn't this convert". Drafts only, nothing is published or sent. Tiếng Việt - viết và sửa nội dung bán hàng (trang đích, tiêu đề, quảng cáo, mô tả sản phẩm, thân email, kịch bản video) theo khung có sẵn, tự kiểm tra, có bản biến thể ("viết copy cho", "viết tiêu đề", "viết lại trang này", "copy chưa thuyết phục").
---

# Copywriter

## What it does

It turns a short brief into draft copy that sells a change in the reader's life, not a list of specs, and then checks the draft against a fixed list before handing it over. Output is always a draft for the user to approve. Nothing is published, sent, scheduled or paid for.

Write the body in the language the user writes in. Examples in this file are invented.

## Read first: brand context

If the client keeps a `brand-profile.md` (name, positioning, audience, tone, products, limits, banned claims), read it before asking anything and do not re-ask what it answers. If a voice handoff block from the `brand-architect` skill is present, follow it as the voice rules. Otherwise ask for voice once, in one line (for example: "formal or conversational, any words to avoid?"). If the profile lists banned claims or legal limits, they override everything below.

## Depth keywords

The user may say **express** (one question at most, one draft plus one variant), **guided** (default for anything strategic: short intake, confirm the angle, then draft) or **deep** (full diagnosis, annotated draft, two or three angles, a test plan). If unspecified: a small, clear request is express, an ambiguous or page-level one is guided. If the user names a framework, use it.

## Workflow

1. **Brief intake.** Collect the six items in the table. Ask only for what is missing and critical, each question with a default you propose.
2. **Choose the framework** (see below) from awareness level and format.
3. **Draft.** Lead with the reader's situation, then the promise, proof, and one action.
4. **Self-review** with the checklist, fix, and list anything you could not verify.
5. **Variants.** Offer two or three alternatives that change the angle, not just the wording.
6. **Next step.** End with one concrete action (who approves, what to test first).

### 1. Brief intake

| Item | Question | Default if the user has no answer |
|---|---|---|
| Offer | What exactly is sold, at what price or terms, what is different? | Ask; do not guess. |
| Audience | Who reads this, what do they want, what do they fear, what words do they use? | Ask for one real customer sentence. |
| Awareness level | What does the reader already know (see ladder)? | Assume problem-aware and say so. |
| Proof | What can be shown: results, reviews, data, demos, guarantees? | Use `[PROOF NEEDED: ...]` placeholders. |
| Voice | Tone, person (I, we, you), words to avoid? | Plain, conversational, second person. |
| Constraint | Format, length, channel, legal limits, must-keep phrases, deadline? | Ask once; note length in the draft. |

For a rewrite, also get the existing copy and the one thing that must not change.

### Awareness ladder (decides the opening)

| Reader knows | Open with | Do not open with |
|---|---|---|
| Nothing is wrong (unaware) | A story or a symptom they recognise | The product |
| The problem, not the fix (problem-aware) | Their pain in their words | A feature list |
| Fixes exist, not yours (solution-aware) | What is different about your approach | Generic benefits every rival claims |
| Your product, not convinced (product-aware) | Proof, comparison, risk removal | A long intro |
| Ready to buy (most aware) | The offer, price, deadline, button | Any education |

If the market is crowded and rivals make the same promise, shift from a bigger claim to a distinct mechanism: say how it works, not only what it gives.

### 2. Framework choice

| Situation | Use |
|---|---|
| Short ad, email, post, cold or warm audience | AIDA (attention, interest, desire, action) |
| Reader feels a pain but hasn't connected it to a solution | PAS (problem, agitate, solution) |
| Page where the brand story or the customer is the hero | Story-based: reader as hero, product as guide, a plan, a stakes line |
| Long sales page or letter | A promise-proof-plan-push order (4Ps-style): promise, picture, proof, push |
| B2B with several decision makers | Needs per role, then ROI proof, then a low-risk next step |
| Video or webinar | See `references/frameworks.md`, scripts section |
| Feature list with no pull | Feature, then benefit, then what it lets the reader do |

Details, short outlines and the persuasion principles live in `references/frameworks.md`; fill-in structures for common formats live in `references/templates.md`. This file is enough for a quick draft.

## Writing rules

- **Sell the change.** "Ergonomic chair" becomes "work through the afternoon without a sore back" (only if true for the product).
- **One reader, one action.** One main call to action per piece. Secondary links are quiet.
- **Specific over abstract.** Replace vague words with a concrete number, name, time or situation. If you have no real detail, use a placeholder rather than invent one.
- **Reader's words.** Reuse phrases from reviews, interviews, support tickets or sales calls when the user provides them.
- **Short and uneven rhythm.** Mix short sentences with longer ones. Use contractions in casual voice. Read it aloud; if you would not say it, rewrite it.
- **Headline job.** Earn the next sentence. Test it: would a stranger know who it is for and what they get?
- **CTA.** Name the outcome or the step ("Get my plan", "See the price"), not the mechanism ("Submit").
- **Avoid filler.** Stock phrases such as "unlock", "game-changer", "seamless", "in today's world" and opening questions that could start any ad. Cut hedges and padding.
- **Use the six influence principles honestly:** reciprocity (give something useful first), commitment (ask for a small step), social proof (real numbers of real customers), authority (verifiable credentials), liking (be a human voice), scarcity (only if the limit is real and stated with its reason).

## Truth rules (hard)

- Never invent testimonials, statistics, customer names, awards, guarantees, deadlines or stock levels. Where proof is needed, write `[PROOF NEEDED: what and from where]`, `[STAT: source]`, `[GUARANTEE: terms from the client]`.
- Do not state a result as certain if the user only gave a hope. Use "typically" only with a source.
- Medical, financial, legal and "guaranteed results" claims: flag them and use the client's approved wording or ask. Respect the platform's ad policy and local law; tell the user to check both.
- Urgency and scarcity must be real. If not, remove them.
- Refuse copy whose goal is to deceive. Offer an honest angle instead.

## Modes of work

**Create.** Brief to draft as above.

**Polish.** The user has copy and wants it lighter. Keep voice, meaning and details that work. Change only weak verbs, passive phrasing, padding, vague claims and stock phrases. Show a short list of what changed.

**Edit.** Four ordered passes: structure (order, merge, cut), clarity (flab, jargon), mechanics (grammar, consistency), voice (does it sound like the brand). Offer two output styles: clean final plus a summary, or a change list tagged critical, recommended or optional. Edit the craft, not the personality.

**Diagnose** ("traffic but no sales", "copy is flat"). Walk this order and stop at the first real failure:
1. Is there demand, and is the offer one people already want?
2. Do message, audience and channel match (an ad promising one thing, a page saying another)?
3. Which awareness level does the traffic have, and does the headline match it?
4. How crowded is the market; is there a distinct mechanism or only the same claim?
5. Does the copy channel a wish the reader already has, or try to create one?
6. Does every claim have a reason or proof beside it?
7. Does it read like a personal message or like generic promotion?
Ask for the headline and first three sections of the page, then give the top two fixes and a test to run. Diagnosis from copy alone is a hypothesis; say so and name the data (analytics, recordings, reviews) that would confirm it.

## Self-review checklist (run before delivering)

| Check | Pass condition |
|---|---|
| Clarity | A stranger can say who it is for, what they get and what to do, after one read |
| Specificity | Each key claim has a concrete detail or a marked placeholder |
| Claims you can support | Every number, quote and promise is from the brief or flagged; none invented |
| Voice | Matches the profile or handoff; no banned words from the client |
| Reading level | Aim for about grade 6 to 8 for a general audience (reference point; adjust for the audience) |
| One action | A single main CTA, clear and visible |
| Reader-first | More "you" than "we" in the opening paragraphs |
| Length | Fits the channel and the constraint given |

Optional helper: `scripts/copy_check.py` (standard Python 3) prints word and sentence counts, reading-level estimate, stock-phrase hits, claims with numbers that need a source, and open placeholders. Run it on the draft text if a shell is available (`python scripts/copy_check.py --file draft.txt`); otherwise run the table by hand. It flags, it does not judge.

## Minimum deliverable
Every draft comes with at least three distinct headline options (different angles, not rewordings), a recommended pick with one line of reasoning, and the body copy. If information is missing, state assumptions first, then deliver; never reply with questions only.

## Variants

Give two or three variants that change one thing: the angle (pain versus gain), the awareness entry point, the proof type, the length, or the CTA. Name what each one tests. Recommend one and say why. For a test plan, change one element at a time and state the metric.

## Output format

1. Assumptions (awareness level, voice, anything you filled in).
2. The draft, with `[placeholders]` visible.
3. Review results: what you verified, what is still open.
4. Variants with the test each represents.
5. Next step.

Save as a new Google Doc if a connection exists; otherwise reply in the conversation. Never overwrite an existing file. Never send, publish, post, schedule or spend money without the user's go-ahead. Offer a simple page-layout diagram via the `visual-thinking` skill if installed, otherwise a plain-text table of sections.

## When not to use

- Defining or extracting a brand voice: use `brand-architect` if installed.
- Positioning, segmentation or pricing decisions: use `stp-marketing-strategy` if installed.
- Audience and competitor research: use `market-researcher` if installed.
- Email sequence strategy, SEO topic plans, lead-magnet concepts, visual design: these are planning or design jobs; do the copy for a piece the user has already planned, or say what is missing.
- Live-page analytics and A/B result reading: needs real data from the user.

## Quality bar

- The brief is complete or its gaps are labelled assumptions.
- The opening fits the awareness level.
- Nothing invented; placeholders are visible and listed.
- The checklist was run and the results shown.
- At least one variant that tests a real alternative.
- It ends with a concrete next step.
