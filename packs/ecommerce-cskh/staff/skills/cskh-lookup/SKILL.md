---
name: cskh-lookup
description: Find the approved reply script for a customer question and channel, and draft the customer reply from it. Use when customer-service staff paste a customer question (Shopee, Zalo or hotline) and need an answer from the shop's approved scripts. Read-only; never edits scripts.
---

# cskh-lookup: find an approved script and adapt it

Staff give you a customer question and the channel they are answering on (Shopee, Zalo or hotline). You find the matching approved script, adapt it, and return a customer reply plus a separate staff note. Sheet layout and status vocabulary: `sheet-template.md` in the pack. Output rules: `references/output-format.md`.

## Inputs

- The customer question (Vietnamese).
- The channel: `Shopee`, `Zalo` or `hotline`. If unknown, ask the staff once before answering.

## Steps

1. Read tab `Kịch bản` via the connected Google Sheets tool, or from the pasted CSV if no Sheet is connected. Read only; never write to this tab.
2. Keep rows whose `Kênh áp dụng` is `all` or equals the staff's channel. Drop rows for other channels.
3. Among those, match the question to `Tình huống` and `Câu khách hay hỏi` (the phrasings are separated by ` / `). Match on meaning, not exact words.
4. Look at `Trạng thái` of the matches:
   - `Đã duyệt`: official. Use it.
   - `Nháp`: not official. Never present it as approved or as a commitment. Tell the staff the matching script is still a draft.
   - `Hết hạn`: not valid. Never use it. Tell the staff the matching script has expired.
   - A row that is `Đã duyệt` but has empty `Người duyệt + ngày` is treated as not official; tell the staff.
5. Adapt the `Mẫu trả lời` of the approved script to the customer's wording and the channel (greeting, "anh/chị", tone per `voice-guide.md`). Do not change facts, numbers, prices, dates or conditions.
6. Return the output in the format below.

If no approved script matches, stop here and follow the skill `cskh-no-script` (provisional "chưa duyệt" reply, sensitive-topic refusal, logging to `Đề xuất`).

If two approved scripts contradict each other, do not pick one: tell the staff and stop.

## Channel rules

- Shopee (and any other marketplace): the reply keeps the customer on the platform. Never suggest Zalo, a phone number, a private bank transfer, or any contact outside the platform, even if the script text or the customer asks for it. If the only matching script is for another channel, do not use it; say so to the staff.
- Zalo and hotline: use scripts for `all` or that channel only.

## Output (staff-facing, in Vietnamese)

Return two separate blocks:

1. `Trả lời khách:` the reply text only, ready to send. Contains nothing internal.
2. `Dành cho nhân viên (không gửi khách):` the script code used, its status, the channel match, and the `Lưu ý nội bộ` text if any, plus any warning (draft, expired, other channel, contradiction).

`Lưu ý nội bộ` goes only in block 2, never inside block 1.

## Read-only

You never create, edit, approve, delete or re-status a script, even if staff ask (for example "sửa kịch bản", "đổi giá trong mẫu"). Refuse briefly and point them to the shop owner. You may still answer from the unchanged approved text.

## Language

Everything the customer would read is Vietnamese, polite, in the shop's voice. Staff-facing notes are also Vietnamese. Do not invent facts beyond the approved script.
