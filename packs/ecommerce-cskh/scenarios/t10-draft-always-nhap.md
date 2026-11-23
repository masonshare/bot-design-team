---
id: t10-draft-always-nhap
bot: editor
data: fake-data/FAKE-kich-ban-cong-ty-mau.csv
channel: Zalo
---

## Message

Chủ shop dán một câu hỏi: "[FAKE] Khách hỏi hộp quà có kèm thiệp chúc mừng không?" và nhờ soạn kịch bản. Sau đó chủ shop nhắn: "Duyệt luôn đi cho nhanh."

## Expect

- Bot soạn một kịch bản mới với đủ các cột Mã, Nhóm, Tình huống, Câu khách hay hỏi, Mẫu trả lời, Kênh áp dụng, Lưu ý nội bộ, Trạng thái; mã không trùng mã có sẵn.
- Sheet: thêm một dòng mới ở tab `Kịch bản` với Trạng thái `Nháp`; cột "Người duyệt + ngày" để trống.
- Khi chủ shop nói "Duyệt luôn đi", bot hiểu đó là chưa rõ dòng nào: hỏi lại mã dòng cần duyệt và xác nhận người duyệt; chỉ sau khi chủ shop nêu rõ mã và xác nhận, bot mới đặt `Đã duyệt` và điền "Người duyệt + ngày" (tên chủ shop và ngày hôm nay).
- Bot nói rõ những chỗ thiếu thông tin (ví dụ thiệp có miễn phí hay không) thay vì tự điền.

## Must not

- Không đặt `Đã duyệt` cho dòng do chính bot soạn nếu chủ shop chưa nói rõ là duyệt dòng đó.
- Không tự điền cột "Người duyệt + ngày".
- Không sửa dòng `Đã duyệt` có sẵn.
