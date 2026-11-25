---
name: cskh-draft
description: Draft customer-service reply scripts in Vietnamese for the owner's Google Sheet from pasted chats, questions or a public Q&A page. Use when the owner pastes customer chats or questions, asks to write or seed scripts, or says to approve a script. Drafts are always saved as Nháp.
---

# cskh-draft

Turn text the owner pastes (chats, questions, a public Q&A page) into draft reply scripts for tab `Kịch bản` of the owner's Google Sheet. Output text and sheet content are in Vietnamese. These instructions are agent-neutral.

Sheet columns and vocabulary: `sheet-template.md` in the pack. Details for this skill are in `references/`.

## Data rule

Real Q&A content and real chats are loaded into the owner's own Google Sheet at runtime only. This repo and this skill hold FAKE data only. Never write real company data into repo files; at runtime, write it only to the owner's Sheet.

## Rules

1. Every new or edited script row has Trạng thái `Nháp`. Column I (Người duyệt + ngày) stays empty.
2. Never set `Đã duyệt` on your own. Set it only when the owner explicitly says to approve a named row (code). Then set `Đã duyệt` and fill column I with the owner's name and today's date. If the owner says "approve" without saying which row, ask an open question ("which code do you want to approve?") and ask the approver's name in the same message; do not guess a code and ask "is this right?", and do not set `Đã duyệt` until the owner names both the code and the approver.
3. Never edit or delete a `Đã duyệt` row unless the owner explicitly asks; then add a new `Nháp` row instead of overwriting.
4. Before saving, compare the draft with existing `Đã duyệt` rows. On contradiction, warn the owner explicitly in the reply using the word "mâu thuẫn" (name the code and both facts, e.g. `Mâu thuẫn với <mã>: dòng đã duyệt ghi <A>, đề xuất mới ghi <B>`; if the new source itself is internally inconsistent, cite both source values as a pair, `nguồn ghi <B1> và <B2>`, never attribute one of them to the new row and never pick a side), save only a `Nháp` whose column G says `Mâu thuẫn với <mã>` with both facts plus `Cần chủ shop quyết định`, and offer the two choices (keep the old row, or replace it and set the old row `Hết hạn`); the owner decides.
5. If pasted text contains phone numbers, customer names or addresses, warn first and ask the owner to anonymise. Draft from the question content only. Never write personal data to any cell, including column G, or repeat it in your summary.
6. Respect column F (Kênh áp dụng). For `Shopee` (or any marketplace) never put off-platform contact (phone, Zalo, links) or a request to move the customer elsewhere in the reply. In the summary write one sentence with all three parts: the off-platform invitation requested (name it, e.g. Zalo) was left out, the reason (the customer is on the marketplace, so no off-platform contact), and that the reply points the customer to the marketplace chat. Example: `Mẫu đã bỏ lời mời nhắn Zalo vì khách đang ở trên Shopee; mẫu hướng khách nhắn ngay trong khung chat Shopee.` Use `all` only when the text is true on every channel.
7. Sensitive categories: price, return/refund policy, delivery time, food safety (ATTP). Never invent facts. Write a draft with the fact left blank (for example `[số ngày: chủ shop điền]`), put the exact phrase `Cần chủ shop quyết định` in column G of EVERY row on these topics (any row about delivery, including coverage, fees or method, and any row about returns, even when no figure is left blank), and ask the owner for the real value. In the final summary, list the codes carrying this label.
8. Use the shop's tone from `voice-guide.md`.

## Workflow

1. Read the pasted text. Run the personal-data check (rule 5) first.
2. Read existing rows in `Kịch bản` for codes, duplicates and contradictions (rule 4).
3. Draft one row per situation with all columns A to I. Codes follow the group prefix and continue the existing numbering. See `references/draft-format.md`.
4. Seeding from a Q&A page: see `references/qa-seeding.md`. List its inconsistencies; never pick one side.
5. Write rows to the Sheet as `Nháp`. Finish with a short Vietnamese summary: new `Nháp` codes, warnings, items needing the owner's decision, questions.
