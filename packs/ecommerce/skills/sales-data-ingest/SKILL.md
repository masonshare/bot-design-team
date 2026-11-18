---
name: sales-data-ingest
description: Reads CSV or Excel exports from Shopee, TikTok Shop, Lazada and an own website, normalizes them into one common sales table, then reports sales and stock and writes a dashboard brief for Claude Code. Use when the owner shares an order or product export, asks for a sales report, revenue by channel, best sellers, returns rate, low stock or out-of-stock items, wants to merge data from several marketplaces, or wants a dashboard. Vietnamese triggers - báo cáo bán hàng, file xuất Shopee, file xuất TikTok Shop, file Lazada, gộp dữ liệu đa sàn, tồn kho, doanh thu theo sàn, dashboard, brief dashboard.
license: MIT
metadata:
  author: Masonshare
  version: "0.1.0"
  language: vi (tiếng Việt, tiền VND)
  bot: Data & Dashboard Analyst
---

# Sales data ingest (nhập và chuẩn hóa dữ liệu bán hàng)

Đọc file xuất từ các sàn, gộp về một bảng chung, báo cáo, rồi viết brief dashboard cho Claude Code dựng. Chỉ đọc và phân tích; không sửa dữ liệu gốc, không đổi giá, không cập nhật tồn kho trên sàn. Tiếng Việt, tiền VND.

## Đầu vào

- File CSV hoặc Excel (.xlsx) do chủ shop xuất từ trang Người bán, đặt trong **thư mục dữ liệu** (Google Drive; OneDrive sẽ bổ sung sau). Dùng kết nối Google Drive đã lưu của hệ thống; không nhận hay lưu mật khẩu, token trong skill hay trong chat.
- Loại file: đơn hàng, sản phẩm, tồn kho. Có thể nhiều file, nhiều sàn, nhiều tháng.
- Nếu chưa có file: hướng dẫn chủ shop xuất từ trang Người bán của từng sàn (tên menu có thể đổi, nói "tìm mục Đơn hàng, xuất báo cáo") và dừng.

Định dạng cột của từng sàn chưa được kiểm chứng và có thể đổi theo thời gian. Không giả định cố định tên cột; làm bước 2.

## Bảng chung (schema)

| Cột | Ý nghĩa |
|---|---|
| source | shopee, tiktok_shop, lazada, website |
| order_id | mã đơn |
| order_date | ngày đặt, YYYY-MM-DD |
| status | completed, cancelled, returned, shipping, other |
| sku, product_name, variant | mã, tên, phân loại |
| quantity | số lượng |
| unit_price_vnd, discount_vnd, shipping_fee_vnd, platform_fee_vnd | tiền, số nguyên VND; trống nếu file không có |
| order_discount_vnd | chiết khấu cấp đơn (voucher, giảm cả đơn), trống nếu file không có |
| goods_revenue_vnd | doanh thu hàng bán của dòng, công thức ở dưới; chưa trừ phí sàn |
| stock_on_hand | tồn (từ file tồn kho, nếu có) |
| file_name, row_no | truy vết dòng gốc |

## Quy trình

1. **Liệt kê file.** Tên, sàn (đoán từ tiêu đề cột và nội dung, nói rõ là đoán), loại, số dòng, khoảng ngày. Xong khi mỗi file có sàn và loại được chủ shop xác nhận hoặc ghi "chưa xác nhận".
2. **Ánh xạ cột.** Với mỗi file, đối chiếu tiêu đề cột (tiếng Việt hoặc Anh) với schema. Hiện bảng "cột gốc -> cột chung". Cột không chắc thì hỏi chủ shop, tối đa một lượt. Xong khi mỗi cột bắt buộc (order_id, order_date, quantity, tiền) có ánh xạ hoặc ghi "thiếu".
3. **Chuẩn hóa.** Ngày về YYYY-MM-DD (nhận dd/mm/yyyy), tiền về số nguyên VND (bỏ "đ", dấu chấm, dấu phẩy ngăn nghìn), trạng thái về 5 giá trị. Mã đơn là chuỗi, giữ số 0 đầu. Một đơn nhiều dòng sản phẩm thì giữ nhiều dòng. Loại trùng: chỉ tự loại khi trùng mã dòng đáng tin do sàn cấp (nếu file có cột đó). Không có mã dòng đáng tin thì KHÔNG tự loại, kể cả hai dòng giống hệt ở mọi cột (trừ file_name và row_no), vì đó vẫn có thể là hai lượt bán hợp lệ. Giữ cả hai, gắn "nghi trùng", liệt kê và hỏi chủ shop một lượt; chỉ loại sau khi chủ shop xác nhận. Không bao giờ loại theo (source, order_id, sku): một đơn có thể có hai dòng cùng SKU khác phân loại, hoặc thiếu SKU. Báo cáo ghi số dòng đã loại, số dòng "nghi trùng" đang giữ và số tiền liên quan. Xong khi mọi dòng bị loại hoặc sửa được đếm.
4. **Kiểm tra tính nhất quán.** So tổng số dòng và tổng tiền trước và sau chuẩn hóa; liệt kê dòng lỗi (ngày sai, tiền âm, số lượng 0). Không tự đoán giá trị cho dòng lỗi: để trống và báo. Xong khi số dòng vào = số dòng ra + số dòng loại.
5. **Lưu bảng chung** thành CSV (UTF-8) kèm tệp ghi chú ánh xạ, vào thư mục làm việc hoặc thư mục dữ liệu nếu chủ shop cho phép. Không ghi đè file gốc.
6. **Báo cáo.** Doanh thu, số đơn, giá trị đơn trung bình theo sàn và theo tuần/tháng; top 10 sản phẩm theo doanh thu và theo số lượng; tỷ lệ hủy và hoàn; sản phẩm tồn thấp (dưới ngưỡng chủ shop đặt, mặc định bằng số bán 14 ngày) và sản phẩm không bán 30 ngày. Mỗi con số ghi khoảng ngày và sàn.
7. **Brief dashboard cho Claude Code** (khi chủ shop muốn). Gồm: câu hỏi cần trả lời, đường dẫn bảng chung, schema, 3-5 thẻ KPI, 2 biểu đồ (doanh thu theo thời gian và sàn, top sản phẩm), bảng tồn thấp, bộ lọc (sàn, ngày), quy tắc hiển thị VND, ghi chú "dữ liệu từ ngày A đến B, cập nhật lúc C". Chủ shop duyệt brief trước khi giao. Artifact do Claude Code dựng và trả về.

## Định dạng đầu ra

```
Đã đọc: <n file, n dòng, sàn, khoảng ngày>
Ánh xạ và điểm chưa chắc: ...
Chất lượng dữ liệu: dòng vào/ra/loại, lỗi chính
Báo cáo: bảng KPI + top sản phẩm + cảnh báo tồn
Điều cần xác nhận: ...
Brief dashboard: (nếu được yêu cầu)
```

Công thức doanh thu:
- **Doanh thu hàng bán** (goods_revenue_vnd) = (unit_price_vnd - discount_vnd cấp dòng) x quantity, trừ phần chiết khấu cấp đơn đã phân bổ. Chỉ tính đơn trạng thái completed (hoàn tất/đã giao). Đơn cancelled và returned tách riêng thành hai dòng "đơn hủy", "đơn hoàn" (số đơn và giá trị), không cộng vào doanh thu; đơn shipping và other báo riêng là "chưa chốt".
- **Chiết khấu cấp đơn**: nếu file có, phân bổ cho các dòng của đơn theo tỷ lệ giá trị dòng và ghi rõ là đã phân bổ; không có thì để trống, không đoán.
- **Phí sàn**: chỉ trừ khi file có cột phí (platform_fee_vnd). Không có thì ghi "chưa trừ phí sàn" cạnh con số; không gọi là doanh thu ròng hay lợi nhuận.
- Mỗi báo cáo ghi công thức đã dùng và các khoản chưa trừ.

## Việc không làm

- Không sửa hay xóa file gốc; không đẩy dữ liệu lên đâu ngoài thư mục chủ shop chỉ định.
- Không cập nhật tồn kho, giá hay đơn trên sàn.
- Không bịa dòng, tiền hay cột thiếu; thiếu thì ghi "chưa có dữ liệu".
- Không đưa thông tin khách (tên, số điện thoại, địa chỉ) vào bảng chung hay dashboard; bỏ hoặc mã hóa các cột này ở bước 3.
- Không lưu mật khẩu, token, đường dẫn chia sẻ công khai trong skill hoặc bảng.

## Phép thử nghiệm thu

Chuẩn bị: 2 file mẫu giả lập (một kiểu Shopee, một kiểu TikTok Shop) với tiêu đề cột khác nhau, tổng cộng 20 dòng, có 1 cặp dòng trùng mã dòng của sàn, 1 cặp dòng giống hệt mọi cột nhưng không có mã dòng, 1 dòng ngày sai, 1 đơn hủy, tiền dạng "1.250.000đ".

Prompt: "Gộp 2 file này và cho mình báo cáo doanh thu theo sàn, sản phẩm tồn thấp."

Đạt khi: (1) bảng ánh xạ cột được hiển thị và điểm chưa chắc được hỏi lại; (2) tiền ra số nguyên VND, ngày ra YYYY-MM-DD; (3) cặp trùng mã dòng của sàn bị loại; cặp giống hệt không có mã dòng được giữ cả hai, gắn "nghi trùng" và hỏi chủ shop trước khi loại; dòng ngày sai được báo chứ không đoán; (4) tổng dòng vào = ra + loại; (5) báo cáo ghi khoảng ngày, công thức doanh thu và "chưa trừ phí sàn" nếu file không có cột phí; đơn hủy tách riêng, không nằm trong doanh thu; (6) không có cột thông tin khách trong bảng chung.

Phép thử kích hoạt: nên kích hoạt với "đây là file đơn tháng 10 từ Shopee", "tuần này sàn nào bán tốt nhất?"; không kích hoạt với "nên bán gì", "soạn trả lời khách hỏi về đơn".
