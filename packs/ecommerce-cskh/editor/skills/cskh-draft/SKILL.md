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
2. Never set `Đã duyệt` on your own. Set it only when the owner explicitly says to approve a named row (code). Then set `Đã duyệt` and fill column I with the owner's name and today's date. If the owner says "approve" without saying which row, ask which code.
3. Never edit or delete a `Đã duyệt` row unless the owner explicitly asks; then add a new `Nháp` row instead of overwriting.
4. Before saving, compare the draft with existing `Đã duyệt` rows. On contradiction, warn the owner (name the code and both facts), save only a `Nháp` noting the conflict in column G, and let the owner decide.
5. If pasted text contains phone numbers, customer names or addresses, warn first and ask the owner to anonymise. Draft from the question content only. Never write personal data to any cell, including column G, or repeat it in your summary.
6. Respect column F (Kênh áp dụng). For `Shopee` (or any marketplace) never put off-platform contact (phone, Zalo, links) or a request to move the customer elsewhere in the reply. Use `all` only when the text is true on every channel.
7. Sensitive categories: price, return/refund policy, delivery time, food safety (ATTP). Never invent facts. Write a draft with the fact left blank (for example `[số ngày: chủ shop điền]`), put `Cần chủ shop quyết định` in column G, and ask the owner for the real value.
8. Use the shop's tone from `voice-guide.md`.

## Workflow

1. Read the pasted text. Run the personal-data check (rule 5) first.
2. Read existing rows in `Kịch bản` for codes, duplicates and contradictions (rule 4).
3. Draft one row per situation with all columns A to H. Codes follow the group prefix and continue the existing numbering. See `references/draft-format.md`.
4. Seeding from a Q&A page: see `references/qa-seeding.md`. List its inconsistencies; never pick one side.
5. Write rows to the Sheet as `Nháp`. Finish with a short Vietnamese summary: new `Nháp` codes, warnings, items needing the owner's decision, questions.
