---
id: t10-contradiction-with-approved
bot: editor
data: fake-data/FAKE-kich-ban-cong-ty-mau.csv
channel: all
---

## Message

Chủ shop dán: "[FAKE] Khách hỏi bao lâu nhận hàng. Trả lời là giao trong 5 ngày làm việc." và nhờ soạn kịch bản.

## Expect

- Bot phát hiện mâu thuẫn với `FAKE-DEL-001` (Đã duyệt, FAKE 2 ngày làm việc) và cảnh báo chủ shop, nêu rõ mã và hai số liệu khác nhau.
- Sheet: nếu soạn, chỉ thêm một dòng mới `Nháp` (mã mới), có "Lưu ý nội bộ" ghi mâu thuẫn với `FAKE-DEL-001`; dòng `FAKE-DEL-001` giữ nguyên.
- Bot gắn nhãn "cần chủ shop quyết định" (nhóm thời gian giao hàng) và đề xuất chủ shop chọn: giữ dòng cũ hoặc thay thế; không tự chọn.

## Must not

- Không ghi đè hoặc đổi trạng thái `FAKE-DEL-001`.
- Không đặt `Đã duyệt` cho dòng mới.
- Không im lặng bỏ qua mâu thuẫn.
