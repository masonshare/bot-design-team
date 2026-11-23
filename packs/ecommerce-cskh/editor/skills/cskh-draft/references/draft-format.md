# Draft row format

Columns, in order (see `sheet-template.md`): Mã, Nhóm, Tình huống, Câu khách hay hỏi, Mẫu trả lời, Kênh áp dụng, Lưu ý nội bộ, Trạng thái, Người duyệt + ngày.

- Mã: group prefix (GIFT, ORD, DEL, RET, PRD, ATTP) plus next free number. Never reuse a code.
- Nhóm: one of `B2B gift box`, `order`, `delivery`, `returns`, `product`, `food safety`.
- Câu khách hay hỏi: questions separated by ` / `, rewritten with no names or numbers of real people.
- Mẫu trả lời: Vietnamese, in the shop's voice, ready to send. No internal remarks.
- Kênh áp dụng: `all`, `Shopee`, `Zalo` or `hotline`. If unsure, ask the owner.
- Lưu ý nội bộ: staff-only notes: source, conflicts, `Cần chủ shop quyết định`, blanks to fill.
- Trạng thái: always `Nháp`.
- Người duyệt + ngày: empty.

## Approval (owner only)

When the owner explicitly says to approve a named code: set H to `Đã duyệt`, set I to `<owner name>, <YYYY-MM-DD>` (today). Confirm the row back. Without an explicit instruction naming the row, do nothing and ask.

## Sensitive category check

Price, return/refund, delivery time, ATTP: if the owner did not give the fact in this conversation, leave it blank in column E and mark column G `Cần chủ shop quyết định: <what is missing>`. Existing approved scripts count as given facts only for the same question; do not carry numbers across products or channels.
