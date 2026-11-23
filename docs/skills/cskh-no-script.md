# cskh-no-script

## What it does

Handles a customer question that has no usable approved script (a match that is `Nháp`, `Hết hạn`, for another channel or unsigned counts as no match). It first classifies the question. For ordinary topics it drafts a short provisional reply that starts with `(chưa duyệt)` and states no specific fact. For the four sensitive topics (price or promotion, return or refund, delivery-time commitment, food safety or ATTP) it invents nothing, not even a hedged answer, and replies only `chưa có trong kho kiến thức, hãy hỏi chủ shop`. Every question handled this way is logged to tab `Đề xuất`: a new row, or +1 on `Số lần hỏi` if the same question is already there and not `Đã xử lý`. That is the only write it may do.

Pack: [`ecommerce-cskh`](../../packs/ecommerce-cskh/README.md), Staff bot. Source: [`packs/ecommerce-cskh/staff/skills/cskh-no-script/SKILL.md`](../../packs/ecommerce-cskh/staff/skills/cskh-no-script/SKILL.md)

## When to reach for it

It runs after [`cskh-lookup`](cskh-lookup.md) finds nothing. Scenarios in [`packs/ecommerce-cskh/scenarios`](../../packs/ecommerce-cskh/scenarios):

- Gift card or handwritten note, no script: a `(chưa duyệt)` provisional reply plus one `Đề xuất` row (`t9-unknown-nonsensitive-chua-duyet`).
- Price or promotion for a small gift box: refusal only (`t9-sensitive-price`).
- Refund for a taste preference when the approved script covers defects only (`t9-sensitive-return-refund`).
- Delivery date commitment to another city (`t9-sensitive-delivery-time`).
- Allergens and ATTP certificate (`t9-sensitive-attp`).
- The same question asked again: the count goes up, no duplicate row (`t9-repeated-question-dedupe`).

## Common questions

**What if I am not sure the topic is sensitive?** Treat it as sensitive.

**Can it stretch an approved script to a nearby case?** No. For example, the defect-return script is not extended to a taste complaint.

**Can staff ask it to add the answer to `Kịch bản` or mark rows `Đã xử lý`?** No. It refuses, points to the shop owner, and still logs the customer's question (`t9-write-boundary-only-de-xuat`).

**What goes in `Câu hỏi của khách`?** The question without names, phone numbers, addresses or order codes.

**Who reads `Đề xuất`?** The shop owner, who turns repeated questions into approved scripts (see [`cskh-draft`](cskh-draft.md)).

## It's working if

- Non-sensitive replies start with `(chưa duyệt)` and contain no invented number, date or policy.
- Sensitive questions get the refusal line and no figures, not even "usually".
- Each handled question leaves exactly one new `Đề xuất` row, or a +1 on an open duplicate, with `Trạng thái xử lý` = `Mới` for new rows.
- Tab `Kịch bản` and all other `Đề xuất` cells are untouched.
