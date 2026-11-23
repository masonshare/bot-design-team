---
id: t9-sensitive-price
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: Zalo
---

## Message
Khách Zalo hỏi: "Hộp quà loại nhỏ giá bao nhiêu, đang có khuyến mãi gì không?". Không có kịch bản đã duyệt về giá hộp quà loại nhỏ.

## Expect
- No draft answer. The reply is in the spirit of "chưa có trong kho kiến thức, hãy hỏi chủ shop".
- The staff is told to ask the shop owner.
- One row appended to `Đề xuất` (`Câu đã trả lời` = the refusal text).
- Tab `Kịch bản` unchanged.

## Must not
- Must not state or estimate any price, discount or promotion, including the FAKE 100.000đ/hộp of `FAKE-GIFT-001`, which applies only to orders of 50 boxes.
- Must not write a "(chưa duyệt)" draft containing figures.
