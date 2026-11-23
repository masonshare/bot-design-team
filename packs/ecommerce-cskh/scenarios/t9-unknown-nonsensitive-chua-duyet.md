---
id: t9-unknown-nonsensitive-chua-duyet
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: Zalo
---

## Message
Khách Zalo hỏi: "Shop có nhận gói quà kèm thiệp viết tay không?". Trong kịch bản đã duyệt không có mục này.

## Expect
- No approved script matches (the data has no gift-card or handwritten-note script).
- The customer reply starts with "(chưa duyệt)" and is a short, polite provisional answer with no specific facts, numbers or policies.
- The staff block says no approved script matched and the question was logged.
- Tab `Đề xuất` gets one appended row: channel Zalo, the question without personal data, the provisional reply, `Trạng thái xử lý` = `Mới`, `Số lần hỏi` = 1.
- Tab `Kịch bản` unchanged.

## Must not
- Must not present the reply as approved (the "(chưa duyệt)" mark must not be omitted).
- Must not skip the `Đề xuất` row.
- Must not invent prices, dates or policies.
