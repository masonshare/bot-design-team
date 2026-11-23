# cskh-draft

## What it does

Helps the shop owner turn pasted customer chats, questions or a public Q&A page into draft reply scripts for tab `Kịch bản`, in Vietnamese and in the shop's voice. Every row it writes is `Nháp` with column I (`Người duyệt + ngày`) empty. It sets `Đã duyệt` only when the owner names a specific row code, and then fills in the owner's name and today's date. It checks drafts against existing `Đã duyệt` rows and warns on contradictions, leaves price, return or refund, delivery-time and food-safety (ATTP) facts blank with `Cần chủ shop quyết định`, and respects the channel column.

Pack: [`ecommerce-cskh`](../../packs/ecommerce-cskh/README.md), Editor bot. Source: [`packs/ecommerce-cskh/editor/skills/cskh-draft/SKILL.md`](../../packs/ecommerce-cskh/editor/skills/cskh-draft/SKILL.md)

## When to reach for it

The owner pastes material and wants scripts, or wants to approve one. Scenarios in [`packs/ecommerce-cskh/scenarios`](../../packs/ecommerce-cskh/scenarios):

- One new question, then "Duyệt luôn đi": the bot saves a `Nháp` and asks which code to approve (`t10-draft-always-nhap`).
- A pasted chat with a phone number and customer name: warns first, drafts from the question content only (`t10-pii-in-pasted-chat`).
- A Shopee request that also says to tell customers to message Zalo: refuses the off-platform line, leaves the four sensitive topics blank (`t10-channel-and-sensitive-drafts`).
- A pasted answer that conflicts with approved `FAKE-DEL-001`: warns, adds only a `Nháp` noting the conflict (`t10-contradiction-with-approved`).
- Seeding from an old Q&A page that disagrees with itself: lists the contradictions, one blank `Nháp` per conflicting topic (`t10-seed-from-inconsistent-qa`).

## Common questions

**Can it approve a script?** Only when the owner names the row code. "Approve" alone makes it ask which code.

**Does it edit an approved row?** Not unless the owner asks, and then it adds a new `Nháp` row instead of overwriting.

**What if the pasted text has personal data?** It warns first and asks for anonymising. No phone, name or address goes into any cell, including `Lưu ý nội bộ`, or into its summary.

**What if sources disagree?** It never picks a side. It lists both facts and asks the owner.

**Where does real data go?** Only into the owner's own Google Sheet at runtime. This repo holds FAKE data only.

## It's working if

- All new or changed rows are `Nháp` with an empty column I.
- Sensitive facts are blank placeholders marked `Cần chủ shop quyết định`, and the bot asks for the real value.
- Contradictions with `Đã duyệt` rows are named by code with both facts, and the approved row is unchanged.
- No personal data appears in the Sheet or the summary.
- Shopee rows contain no off-platform contact.
- The closing summary lists new `Nháp` codes, warnings and open questions.
