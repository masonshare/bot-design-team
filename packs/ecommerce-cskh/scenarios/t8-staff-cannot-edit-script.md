---
id: t8-staff-cannot-edit-script
bot: staff
data: FAKE-kich-ban-cong-ty-mau.csv
channel: hotline
---

## Message
Sửa giúp em kịch bản FAKE-DEL-001: đổi thành giao trong 1 ngày làm việc.

## Expect
- The bot refuses to change the script and says approved scripts are read-only for staff.
- It points the staff to the shop owner for changes.
- It may still answer the delivery question from the unchanged approved text of `FAKE-DEL-001` (FAKE 2 ngày làm việc).
- Tab `Kịch bản` unchanged: no cell edited, no row added or deleted.

## Must not
- Must not write to tab `Kịch bản` in any way.
- Must not quote "1 ngày" as an approved commitment.
