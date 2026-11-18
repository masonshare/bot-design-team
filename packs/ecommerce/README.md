# E-commerce Team VN

Đội bảy bot soạn nháp cho shop Việt Nam (Shopee, TikTok Shop, Lazada, website riêng; tiếng Việt, VND). **Trạng thái: bản nháp, chưa nhập thử và chưa chạy thử trên OpenMausBot.** Chỉ mới kiểm cấu trúc tệp bằng script (xem cuối trang).

Cả đội chỉ soạn nháp và phân tích. Không bot nào gửi khách, đăng sản phẩm, đổi giá, hoàn tiền, chạy quảng cáo hay thanh toán. Credit ảnh/video chỉ dùng sau khi chủ shop trả lời "đồng ý" cho từng đợt có ước tính chi phí.

## Cài đặt

Gói chưa commit hoặc push, nên chưa có liên kết GitHub để nhập. Khi nhánh được đưa lên GitHub, nhập giống Starter:

1. Chọn **+ → Import…**, dán liên kết thư mục `packs/ecommerce` của nhánh đó.
2. Xem nội dung, chọn **Add** và chọn mô hình cho từng bot.
3. Bật skill cho từng bot theo bảng dưới (skill nhập vào ở trạng thái tắt). Gói này không có bước "cài skill" tự động như Starter; bật tay hoặc nhờ từng bot tự bật skill của mình.
4. Kết nối ứng dụng tùy chọn nếu cần (Magnific, Canva, Google Drive chỉ đọc). Slug ứng dụng trong `team.md` là giả định, chưa kiểm chứng.

| Bot | Skill được bật |
|---|---|
| E-commerce Chief (Chief of Staff) | Không có skill trong gói |
| Product & Marketing Strategist | `product-marketing-strategy` (thêm `research` nếu máy có) |
| Data & Dashboard Analyst | `sales-data-ingest` (thêm `data-dashboards` nếu dùng được) |
| Listing & Ad Copywriter | `ecommerce-copy` |
| Product Visual Designer | `product-visuals` |
| Product Video Producer | `product-video` |
| Customer Care & Returns Assistant | `customer-care` |

`research` và `data-dashboards` là skill có sẵn trên máy, không đi theo gói. Mô hình, khóa, kết nối, bộ nhớ và hội thoại cũng không đi theo gói. Gói không có routine.

## Cấu trúc tệp

- `team.md`: tệp nhập (frontmatter `botmrr: 1`). Soul và SKILL.md đã nhúng sẵn.
- `<bot>.md` (7 thẻ bot) và `skills/<skill>/SKILL.md` (6 skill): nguồn để sửa. Sửa nguồn rồi dựng lại `team.md`, đừng sửa riêng bản nhúng, để hai bên không lệch nhau.

## Kiểm tra nghiệm thu cần làm trên OpenMausBot sạch

Ghi đầu vào, kết quả thực tế, đạt/không đạt và ảnh hoặc nhật ký cho từng phép thử.

1. Sau khi nhập, kiểm tra đủ bảy bot và E-commerce Chief là Chief.
2. Giao Chief một việc "nên bán gì"; kiểm tra Chief giao đúng chuỗi Data & Dashboard Analyst rồi Product & Marketing Strategist, dùng đúng 5 trường.
3. Đưa Chief yêu cầu "trả lời khách này luôn"; kiểm tra bot trả nháp, không gửi.
4. Yêu cầu làm ảnh; kiểm tra bot báo ước tính chi phí và chờ "đồng ý" trước khi tạo.
5. Mở Skills của từng bot kiểm tra trạng thái; thử một yêu cầu ngắn cho từng chuyên gia, dùng dữ liệu mẫu giả lập (ghi rõ là giả lập).

Kết quả: chưa có.

## Đã kiểm tra bằng script (2026-11-18)

`team.md` có YAML frontmatter hợp lệ; trường và giới hạn đối chiếu với lược đồ v1 của OpenMausBot; soul khớp thẻ bot và SKILL.md nhúng khớp tệp nguồn. Đây là kiểm tra cấu trúc, không phải thử nhập trên ứng dụng.
