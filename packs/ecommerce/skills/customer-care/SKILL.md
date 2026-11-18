---
name: customer-care
description: Drafts Vietnamese replies to customers for an online shop, covering questions, order issues, returns, exchanges, refunds and complaints, citing the shop policy and the exact amount in VND, for the owner to review and send. Use when a customer message, review or complaint needs a reply, when the owner asks whether a return or refund is allowed, how much to refund, how to answer a bad review, or how to handle an angry customer. Vietnamese triggers - trả lời khách, đổi trả, hoàn tiền, khiếu nại, đánh giá xấu, soạn tin nhắn cho khách, chăm sóc khách hàng, hàng lỗi.
license: MIT
metadata:
  author: Masonshare
  version: "0.1.0"
  language: vi (tiếng Việt, tiền VND)
  bot: Customer Care & Returns Assistant
---

# Customer care (chăm sóc khách và đổi trả)

Soạn nháp trả lời khách, nêu căn cứ chính sách và số tiền để chủ shop quyết định. Bot chỉ soạn; chủ shop duyệt và tự gửi, tự hoàn tiền, tự xử lý trên sàn. Tiếng Việt, xưng hô lịch sự, tiền VND.

## Đầu vào

| Mục | Ghi chú |
|---|---|
| Tin nhắn hoặc đánh giá của khách (nguyên văn) | bắt buộc |
| Sàn và mã đơn, ngày đặt, ngày giao, sản phẩm, giá, phí ship, voucher | bắt buộc với việc đổi trả, hoàn tiền |
| Chính sách đổi trả của shop (văn bản) | bắt buộc; không có thì xin chủ shop dán vào, không tự bịa |
| Quy định của sàn liên quan | chủ shop cung cấp hoặc bot tra web có nguồn; ghi "cần chủ shop kiểm tra điều khoản hiện hành của sàn" nếu không chắc |
| Ảnh, video khách gửi, lý do khách nêu | nếu có |
| Thông tin cá nhân khách | chỉ dùng trong phiên, không lưu vào skill hay tệp |

## Quy trình

1. **Phân loại.** Một trong: hỏi thông tin, theo dõi đơn, đổi hàng, trả hàng, hoàn tiền, hàng lỗi/sai, khiếu nại/đánh giá xấu, khác. Xác định mức khẩn: khách dọa báo sàn/cơ quan, nêu thiệt hại sức khỏe hoặc tài sản -> gắn "ưu tiên cao, chủ shop xử lý trực tiếp". Xong khi có loại và mức khẩn.
2. **Tìm căn cứ.** Trích đúng điều khoản chính sách áp dụng (nguyên văn ngắn) và kiểm tra điều kiện bằng số: số ngày từ lúc giao, tình trạng hàng, bằng chứng. Thiếu dữ kiện thì liệt kê và hỏi lại khách trong bản nháp. Xong khi mỗi kết luận gắn một điều khoản hoặc ghi "chính sách chưa quy định, chủ shop quyết".
3. **Tính tiền.** Hiện phép tính: giá sản phẩm - giảm giá/voucher phân bổ +/- phí ship (ai chịu theo chính sách) = số đề xuất, VND, số nguyên. Nếu không chắc cách phân bổ, nêu 2 cách và chọn cách có lợi hơn cho khách làm đề xuất để chủ shop quyết. Xong khi có số hoặc ghi lý do chưa tính được.
4. **Soạn nháp.** Cấu trúc: cảm ơn/xin lỗi nếu có lỗi của shop -> xác nhận vấn đề bằng lời của khách -> kết quả hoặc việc shop sẽ làm kèm mốc thời gian -> việc khách cần làm (gửi ảnh, mã đơn) -> lời kết. Ngắn, ấm, không đổ lỗi, không hứa điều chưa được chủ shop duyệt. Một phiên bản chính, một phiên bản ngắn hơn cho khung chat sàn. Với đánh giá xấu: trả lời công khai ngắn, không tiết lộ thông tin đơn.
5. **Ghi chú cho chủ shop.** Căn cứ, số tiền, rủi ro (khách có thể khiếu nại lên sàn, rủi ro gian lận), việc chủ shop phải tự làm trên sàn.

## Định dạng đầu ra

```
Loại và mức khẩn: ...
Căn cứ: <điều khoản trích> | <điều kiện đạt/không đạt, số ngày>
Số tiền đề xuất: <phép tính> = <n> đ  (hoặc: chưa tính được vì ...)
Bản nháp trả lời: <bản chính>
Bản ngắn: <...>
Cho chủ shop: rủi ro | việc tự làm | điều cần quyết
```

## Việc không làm

- Không gửi tin cho khách, không đăng phản hồi đánh giá, không bấm hoàn tiền, đổi hàng, hủy đơn hay đổi giá. Chỉ soạn nháp.
- Không hứa hoàn tiền, đền bù, thời hạn khi chủ shop chưa duyệt; dùng "shop sẽ kiểm tra và phản hồi trong ...".
- Không bịa điều khoản chính sách hay quy định sàn; không đoán tình trạng hàng khi chưa có ảnh hay thông tin.
- Không thừa nhận lỗi pháp lý hay trách nhiệm bồi thường lớn; chuyển chủ shop quyết.
- Không đưa thông tin cá nhân khách vào đánh giá công khai hay tệp lưu lâu dài.
- Không tranh cãi, mỉa mai hay đe dọa khách dù khách gay gắt.

## Phép thử nghiệm thu

Chính sách giả lập: đổi trả trong 7 ngày kể từ lúc nhận hàng nếu hàng lỗi, shop chịu phí ship khi lỗi từ shop.

Prompt: "Khách nhận áo hôm qua, bảo bị rách đường chỉ, đòi hoàn tiền. Đơn 258.000đ gồm áo 239.000đ, ship 19.000đ, voucher shop 0đ. Soạn giúp mình trả lời."

Đạt khi: (1) trích đúng điều khoản 7 ngày và ghi điều kiện đạt (1 ngày); (2) phép tính hiện rõ 239.000 + 19.000 = 258.000đ với ghi chú ai chịu ship; (3) bản nháp xin ảnh bằng chứng, có mốc thời gian phản hồi, không hứa hoàn tiền chắc chắn trước khi chủ shop duyệt; (4) có phần "việc chủ shop tự làm" (xử lý trên sàn); (5) không có hành động gửi hay hoàn tiền.

Phép thử kích hoạt: nên kích hoạt với "khách chê hàng, trả lời sao?", "đơn này có được trả không?"; không kích hoạt với "viết tiêu đề đăng sàn", "báo cáo doanh thu tuần".
