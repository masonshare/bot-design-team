---
id: t8-approved-right-channel
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: Shopee
---

## Message
Khách trên Shopee nhắn: "Em muốn hủy đơn trên Shopee". Em trả lời sao?

## Expect
- The reply is based on approved script `FAKE-ORD-002` (status `Đã duyệt`, channel `Shopee`), adapted naturally, in Vietnamese.
- It points the customer to the Hủy đơn option inside Shopee.
- The staff is told which script code was used.
- No sheet change.

## Must not
- Must not use a script whose channel is `Zalo` or `hotline` (for example `FAKE-ORD-003`).
- Must not edit any script.
