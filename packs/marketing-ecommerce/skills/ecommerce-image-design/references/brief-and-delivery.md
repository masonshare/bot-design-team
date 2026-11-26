# Brief, delivery template, review checklist

## 1. Normalised brief (fill after intake)

```text
IMAGE BRIEF
Requested by / date: ___
1. Product (name, pack, SKU count): ___
2. Category: ___
3. Platform or tool: ___
4. Image types and counts: cover ___ | detail ___ | shop banner ___ | campaign or ad ___
5. Main message / USP (verified): ___
6. Brand rules (brand-profile.md read: yes / no): colours ___ fonts ___ logo ___ banned visuals ___
7. Target customer and buying motive: ___
8. Deadline and revisions: ___
9. Mood: ___
10. Product fidelity route: composite real product / reference-guided draft / undecided
11. Exact on-image copy supplied: yes / no (if no, placeholders marked)
12. Generation: prompts only / tool connected (name) and cost approved for this run (yes / no)
Notes: ___
```

Blockers: product, platform, message. Everything else may carry a labelled assumption.

## 2. Plan table

| # | Role | Mode | Angle and composition | Mood | On-image copy | Fidelity note |
|---|---|---|---|---|---|---|
| 1 | cover | studio product | front, centred | clean | ___ | real label kept |
| 2 | ___ | ___ | ___ | ___ | ___ | ___ |

## 3. Delivery template

```text
# Image prompt package - [product]

1. Normalised brief (section 1)
2. Inputs and specs: supplied assets, ratio, export size, safe zone, assets that stay manual (logo, QR, seals, legal text)
3. Plan table (section 2) and a two-line visual rationale
4. Prompts, one block per image:
   Image N - [role]
   Vietnamese prompt (for review)
   English prompt (for the generator)
5. Checklist result (section 4): pass / exceptions
6. Open questions and missing data
7. Status: NOT GENERATED  |  generated with approved cost (tool, count, cost)
8. Next step: one action
```

## 4. Review checklist

Prompt
- Vietnamese version and English version say the same thing; copy and numbers identical in both.
- Stack present: role, subject, setting, composition and camera, light and colour, style, fidelity, text, ratio, constraints.
- Reference image attached or requested when the product must look exact.
- Quoted copy: spelling, diacritics, capitalisation, line breaks, hierarchy, position, contrast, inside the central 80 percent.
- Claims, prices, certificates, reviews supplied by the user or shown as placeholders.
- Constraints present and not contradicting the requested text.

Generated or supplied image
- Product shape, label, colour and packaging match the reference; no duplicate, mirror error or fake text.
- One clear focal point; product is seen before props; readable on a phone.
- Angle fits the role; crop for the banner does not cut the product.
- Light and palette match the brand profile; props support, not distract.
- Food looks fresh and appetising; gift sets show a complete offer (product, box, card, logo zone).
- Cultural motifs refined, not cluttered.

Export
- Ratio and size match the platform; file size within the limit; names clear (`01-cover`).
- Logo, QR, seals and legal text placed from real source files and checked.
- Client logo placement approved by the client.

## 5. Prompt repair table

Name the failure, then change one thing.

| Symptom | Likely cause | Smallest fix |
|---|---|---|
| Generic, flat look | No light or material cues | Add one light direction and one surface material |
| Label or shape changed | Weak fidelity lock, busy scene | Repeat the lock, simplify the scene, or generate background only and composite |
| Cluttered | Too many props | Cap props at three, say "large clean negative space on the left" |
| Wrong or garbled text | Too much copy, long lines | Shorten copy, quote each line, move small print to post-production |
| Product too small | No size instruction | State percent of frame, say "product fills about 70 percent" |
| Off brand | Palette or style not stated | Paste palette and photo style from the brand profile |
| Not the right market feel | Foreign setting | Name the local setting, food, people and materials |
| Banner crop cuts the product | Product too near edge | Place product within the central 80 percent, state which side holds copy |

Repair order: product accuracy, then composition, then light, then style, then text.
