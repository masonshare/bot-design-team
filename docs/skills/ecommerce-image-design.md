# ecommerce-image-design

## What it does

Plans e-commerce visuals and writes image-generation prompts for product covers, product-detail images, shop and campaign banners, ads, landing page heroes, and food-and-beverage or gift-set visuals. It follows a fixed order: brief intake, visual language choice, shot or layout plan, prompts in Vietnamese plus an English version, review checklist and delivery. The real product is the highest constraint. Prompts come first; it generates images only if a tool is connected and the user approves the cost. Body in English, description bilingual.

E-commerce images are often made by feel: no brief, vague prompts, and an AI that redraws the product with the wrong label. The default is to write prompts for you to review first, with an English copy alongside. It reads `brand-profile.md` if you have one, and the example prompt uses an invented product. Platform pixel-size tables were dropped because they change, so check each platform's current rules. Known weak spot from testing: one prompt guessed an aspect ratio. Reference points: keep the main content in the central 80 percent; the product fills about 70 to 80 percent of a cover image; try 1 to 2 images first to keep cost low before a full batch; starting aspect ratios 1:1, 4:5, 9:16, 3:2 and about 8:3, to be checked against each platform. Every number in this skill is a labelled reference point, not a fact about your market or channel; the skill asks for your own figures.

Source: [`packs/marketing-ecommerce/skills/ecommerce-image-design/SKILL.md`](../../packs/marketing-ecommerce/skills/ecommerce-image-design/SKILL.md)

## When to reach for it

Someone asks for a cover image prompt, a sale banner, product description images, a gift-set image, or an image prompt for an ad. For checking the product page as a whole use `ecommerce-store-optimization`. Spending money on image generation always needs your approval first.

## Common questions

**Will it generate the images?** Only if you connect a tool and approve the cost. By default it writes prompts for you to review.

**Why does it insist on the real product?** Generators redraw products and change labels; the real product photo and details are the top constraint.

**Which sizes should I use?** The skill gives starting ratios; check the platform's current rules before you export.

## It's working if

- A brief was taken before any prompt, and each image has a plan (shot or layout).
- Prompts come in Vietnamese with an English copy, and keep the real product details.
- No image is generated and no cost is incurred without your approval.
