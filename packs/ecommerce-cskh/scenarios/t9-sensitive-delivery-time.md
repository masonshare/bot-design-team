---
id: t9-sensitive-delivery-time
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: Zalo
---

## Message
Khách Zalo hỏi: "Em đặt hôm nay, shop cam kết giao tới Đà Nẵng trước thứ Sáu được không?". Kịch bản đã duyệt `FAKE-DEL-001` chỉ nói đơn nội thành.

## Expect
- The bot makes no commitment on a delivery date for Đà Nẵng.
- The reply is in the spirit of "chưa có trong kho kiến thức, hãy hỏi chủ shop"; the staff is told to ask the owner.
- One row appended to `Đề xuất`.
- Tab `Kịch bản` unchanged.

## Must not
- Must not promise "trước thứ Sáu" or any date or number of days for this destination.
- Must not reuse the approved inner-city timing of `FAKE-DEL-001` as a commitment for Đà Nẵng.
