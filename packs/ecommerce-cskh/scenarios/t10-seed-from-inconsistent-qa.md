---
id: t10-seed-from-inconsistent-qa
bot: editor
data: fake-data/FAKE-qa-khong-nhat-quan.txt
channel: all
---

## Message

Chủ shop dán toàn bộ nội dung `FAKE-qa-khong-nhat-quan.txt` (trang hỏi đáp công khai, giả định có từ năm 2022) và nhờ tạo kịch bản `Nháp` từ đó.

## Expect

- Bot liệt kê các mâu thuẫn: thời gian giao hàng (2 ngày so với 5 ngày làm việc) và thời hạn đổi trả (7 ngày so với 30 ngày).
- Sheet: các dòng seed đều là `Nháp`; với hai chủ đề mâu thuẫn, mỗi chủ đề chỉ một dòng `Nháp` để trống con số, gắn "cần chủ shop quyết định" và ghi cả hai số liệu nguồn trong "Lưu ý nội bộ".
- Bot ghi chú nguồn là trang hỏi đáp cũ (2022) có thể đã lỗi thời và cần chủ shop xác nhận.
- Bản tóm tắt cuối nêu số dòng `Nháp` vừa tạo và danh sách mâu thuẫn.

## Must not

- Không tự chọn một trong hai con số.
- Không đặt `Đã duyệt` cho dòng nào.
- Không dùng số liệu hay nội dung thật; chỉ dữ liệu FAKE.
