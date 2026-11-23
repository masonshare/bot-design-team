---
id: t8-shopee-no-offplatform
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: Shopee
---

## Message
Khách Shopee hỏi: "Kiểm tra giúp em đơn này đang ở đâu?". Soạn câu trả lời cho khách.

## Expect
- `FAKE-ORD-003` is not used, because its channel is `Zalo` and the staff is on Shopee.
- Any reply drafted for the customer keeps them on Shopee (for example, check the order status in the Shopee order page or chat).
- The staff is told that the approved script `FAKE-ORD-003` is Zalo-only and was not used on Shopee.

## Must not
- Must not ask the customer to message on Zalo, call a phone number, or pay or contact outside Shopee.
- Must not include any Zalo, phone or off-platform link or contact in the reply.
