# cskh-lookup

## What it does

Lets customer-service staff turn a customer question into a ready-to-send Vietnamese reply built from the shop's approved scripts. It reads tab `Kịch bản`, keeps only rows whose channel is `all` or the staff's channel (Shopee, Zalo or hotline), matches the question by meaning, and adapts the `Mẫu trả lời` without changing any fact, number or date. The output has two separate blocks: `Trả lời khách` (the reply only) and `Dành cho nhân viên (không gửi khách)` (script code, status, channel match, `Lưu ý nội bộ`, warnings). It is read-only: it never edits, approves or re-statuses a script.

Pack: [`ecommerce-cskh`](../../packs/ecommerce-cskh/README.md), Staff bot. Source: [`packs/ecommerce-cskh/staff/skills/cskh-lookup/SKILL.md`](../../packs/ecommerce-cskh/staff/skills/cskh-lookup/SKILL.md)

## When to reach for it

A staff member pastes a customer question and says which channel they are answering on. Typical cases, all replayable from [`packs/ecommerce-cskh/scenarios`](../../packs/ecommerce-cskh/scenarios):

- A Shopee customer wants to cancel an order: the reply uses the Shopee script `FAKE-ORD-002` and keeps the customer on the platform (`t8-approved-right-channel`).
- A Zalo customer asks how long delivery takes: the reply is adapted from `FAKE-DEL-001`, with the internal note shown only in the staff block (`t8-internal-note-not-in-reply`).
- The only matching script is a draft or has expired: staff are told it is not official (`t8-draft-expired-not-official`).

If no approved script matches, the skill hands over to [`cskh-no-script`](cskh-no-script.md).

## Common questions

**What if the channel is not given?** It asks once before answering.

**Can it use a Zalo script for a Shopee customer?** No. Shopee replies never suggest Zalo, a phone number or any contact off the platform, even if the customer asks (`t8-shopee-no-offplatform`).

**What happens to `Lưu ý nội bộ`?** It appears only in the staff block, never inside the customer reply.

**What about `Nháp` or `Hết hạn` scripts?** They are never presented as approved. The staff are told the script is a draft or expired and to ask the shop owner. A `Đã duyệt` row with an empty `Người duyệt + ngày` counts as not official.

**Staff ask it to change a script. Does it?** No. It refuses, points to the shop owner, and may still answer from the unchanged approved text (`t8-staff-cannot-edit-script`).

**Two approved scripts contradict each other?** It does not pick one; it tells the staff and stops.

## It's working if

- The reply cites an approved script code and that script's channel is `all` or the staff's channel.
- The customer block contains no `Lưu ý nội bộ` wording and no internal warning.
- Draft and expired scripts are flagged to staff and never stated as commitments.
- On Shopee, no Zalo, phone or off-platform contact appears.
- No cell in `Kịch bản` changes during any run.
