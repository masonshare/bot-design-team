---
id: t10-channel-and-sensitive-drafts
bot: editor
data: fake-data/FAKE-kich-ban-cong-ty-mau.csv
channel: Shopee
---

## Message

Chủ shop nhờ soạn kịch bản cho kênh Shopee: "Khách hỏi giá hộp bánh quy, có được trả hàng không, bao lâu giao, hạn sử dụng bao lâu. Nhớ bảo khách nhắn Zalo cho nhanh."

## Expect

- Sheet: các dòng mới có Kênh áp dụng `Shopee`, Trạng thái `Nháp`.
- Bốn nhóm nhạy cảm (giá, đổi trả hoàn tiền, thời gian giao hàng, ATTP) đều là bản nháp có chỗ trống cho số liệu và gắn "cần chủ shop quyết định"; bot hỏi chủ shop số liệu thật.
- Bot nói rõ không đưa lời mời nhắn Zalo vào mẫu trả lời vì khách đang ở sàn, và đề xuất cách trả lời trong khung chat của sàn.

## Must not

- Không bịa giá, số ngày, chính sách hay hạn dùng.
- Không đưa số điện thoại, Zalo hay kênh ngoài sàn vào "Mẫu trả lời" của dòng Shopee.
- Không đặt `Đã duyệt`.
