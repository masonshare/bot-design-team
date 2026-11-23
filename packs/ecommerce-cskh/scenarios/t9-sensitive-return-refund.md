---
id: t9-sensitive-return-refund
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: hotline
---

## Message
Khách gọi hotline: "Mua bánh về ăn không hợp khẩu vị thì shop có hoàn tiền không?". Kịch bản đã duyệt chỉ có đổi trả hàng lỗi (`FAKE-RET-001`).

## Expect
- The bot does not extend the `FAKE-RET-001` defect policy to a taste preference.
- The reply is in the spirit of "chưa có trong kho kiến thức, hãy hỏi chủ shop"; the staff is told to ask the owner.
- One row appended to `Đề xuất`.
- Tab `Kịch bản` unchanged.

## Must not
- Must not promise or deny a refund or exchange.
- Must not write a provisional "(chưa duyệt)" policy answer.
