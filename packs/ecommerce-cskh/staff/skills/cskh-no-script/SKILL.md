---
name: cskh-no-script
description: Handle a customer question that has no approved script. Gives a provisional reply marked "chưa duyệt" for ordinary topics, refuses to invent anything for price, return/refund, delivery-time commitments and food safety (ATTP), and logs every such question to the separate `Đề xuất CSKH` file (tab `Đề xuất`). Use when cskh-lookup finds no matching Đã duyệt script.
---

# cskh-no-script: no approved script matches

Used when `cskh-lookup` finds no usable `Đã duyệt` script for the question and channel. (A matching `Nháp`, `Hết hạn`, other-channel or unsigned script counts as "no approved script".) Sheet layout: `sheet-template.md`.

## 1. Classify the question

Sensitive if it asks about any of:

1. Price or promotion (giá, khuyến mãi, freeship, giảm giá, voucher).
2. Return or refund policy (đổi trả, hoàn tiền, bảo hành đổi mới).
3. Delivery-time commitment (bao lâu nhận, giao trước ngày X, cam kết ngày giao).
4. Food safety, ATTP (hạn sử dụng, bảo quản, thành phần gây dị ứng, chứng nhận, nguồn gốc).

If unsure, treat as sensitive. Anything else is non-sensitive.

## 2. Reply

- Non-sensitive: draft a short, polite provisional reply in the shop's voice (`voice-guide.md`). Start the customer reply with `(chưa duyệt)` so staff see it is a stopgap. State no specific fact, number, date or policy that is not in an approved script.
- Sensitive: do NOT draft an answer, not even a hedged one, and no figures or "usually". Reply only: `chưa có trong kho kiến thức, hãy hỏi chủ shop`. Do not quote `Nháp` or `Hết hạn` text as the answer, and do not stretch an approved script to a case it does not cover.
- Keep the channel rules of `cskh-lookup` (never move a Shopee customer off-platform).
- Output uses the two blocks of `cskh-lookup`. Block 2 names the closest script code (if any), says no approved script matched, says whether the reply is `chưa duyệt` or a refusal, and says the question was logged. For a sensitive topic, block 2 also tells the staff explicitly: `hãy hỏi chủ shop`. If any near-match script exists but was not used (other channel, other topic or scope, `Nháp`, `Hết hạn`, unsigned), name its code and write the sentence `Mã <mã> KHÔNG được dùng vì <lý do>` (also for a sensitive topic, and also when the script is `Đã duyệt` but covers a different case); never describe its content as if it answered the question.

## 3. Log to `Đề xuất CSKH` (always)

The log lives in its own Google Sheet file, `Đề xuất CSKH`, tab `Đề xuất`, not in the scripts file. Staff are editors on that file only.

Every question handled here is logged, sensitive or not. Columns A to H: `Ngày`, `Kênh`, `Câu hỏi của khách`, `Câu đã trả lời` (the provisional text, or `chưa có trong kho kiến thức, hãy hỏi chủ shop`), `Mã gần nhất`, `Người hỏi`, `Trạng thái xử lý` = `Mới`, `Số lần hỏi` = `1`.

- Read the `Đề xuất` tab of `Đề xuất CSKH` first. If a row already asks the same thing (same meaning) and is not `Đã xử lý`, do not add a row: add 1 to its `Số lần hỏi` and leave its other cells unchanged. In staff block 2, say explicitly that this question was already logged before and that `Số lần hỏi` went from N to N+1 (no new row).
- If the matching row is `Đã xử lý`, append a new row.
- No personal data in `Câu hỏi của khách`: strip names, phone numbers, addresses, order codes.

## 4. Write boundary

You read the scripts file read-only. The only writes you may do: append a row to tab `Đề xuất` of the `Đề xuất CSKH` file, or add 1 to `Số lần hỏi` of an existing row there. Never write to the scripts file (`Kịch bản`) or any other tab or file, and never change other cells of `Đề xuất`. If asked to (for example "thêm vào kịch bản", "đánh dấu đã xử lý"), refuse explicitly, one by one, each thing asked (for example: not adding to `Kịch bản`, not setting `Đã duyệt`, not marking old `Đề xuất` rows `Đã xử lý`), say these are for the shop owner only, and confirm that no existing row was changed. Put the refusals in block 2 as one list with one line per requested action, each starting with its own name (for example `Không thêm vào Kịch bản`, `Không đặt Đã duyệt`, `Không đánh dấu Đã xử lý`), then say: the only thing done is logging the customer's question to `Đề xuất` (the new row's `Mới` is the status of this new question, not a change to old rows).
