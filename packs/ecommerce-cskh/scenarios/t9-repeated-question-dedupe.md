---
id: t9-repeated-question-dedupe
bot: staff
data: FAKE-de-xuat-cong-ty-mau.csv
channel: Zalo
---

## Message
Đây là lần thứ hai có khách Zalo hỏi: "Hộp quà có kèm thiệp chúc mừng không?". Tab `Đề xuất` (FAKE-de-xuat-cong-ty-mau.csv) đã có dòng cho câu này với `Trạng thái xử lý` = `Mới` và `Số lần hỏi` = 1.

## Expect
- The reply is a "(chưa duyệt)" provisional answer (non-sensitive, no approved script).
- Tab `Đề xuất` gets no new row: the existing row's `Số lần hỏi` becomes 2.
- Other cells of that row are unchanged.
- The staff block says the question was already logged and the count was increased.
- Tab `Kịch bản` unchanged.

## Must not
- Must not append a duplicate row for the same question.
- Must not reset the count or change `Trạng thái xử lý`.
- Must not write to `Kịch bản`.
