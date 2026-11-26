---
name: ecommerce-kpi-analytics
description: Đọc và chẩn đoán chỉ số bán hàng TMĐT (GMV, NMV, tỷ lệ chuyển đổi, giá trị đơn trung bình, tồn kho) và ra việc cần làm. Dùng khi hỏi "vì sao doanh số giảm", "GMV và NMV khác gì", "traffic nhiều mà ít đơn", "tăng giá trị đơn thế nào", "đọc báo cáo sàn ra sao", "tồn kho bao nhiêu là ổn". English - diagnose e-commerce KPIs (GMV = traffic x conversion x AOV, GMV vs NMV, sell-in vs sell-out, inventory days) and turn them into a weekly review with concrete actions.
---

# KPI và phân tích số liệu TMĐT

Doanh số trên sàn quy về ba biến: **lượng khách vào (traffic), tỷ lệ mua (CR), giá trị mỗi đơn (AOV)**. Việc đầu tiên luôn là tìm xem biến nào đang hỏng, rồi mới sửa đúng chỗ đó.

## Khi không dùng skill này

- Tính giá vốn, chi phí kéo khách, lãi mỗi đơn, hòa vốn: dùng skill tính hiệu quả kinh tế đơn vị (ví dụ `startup-metrics-framework`); nếu chưa có, tính tại chỗ.
- Sửa trang sản phẩm, ảnh, mô tả: dùng `ecommerce-store-optimization`.
- Thiết kế khuyến mãi: dùng `ecommerce-promotion-design`.

## Công thức nền

```
GMV = Traffic x CR x AOV

GMV     tổng giá trị đơn đặt, tính cả đơn hủy và hoàn
Traffic lượt khách vào trang sản phẩm hoặc gian hàng
CR      tỷ lệ khách vào rồi mua
AOV     giá trị trung bình mỗi đơn hoàn tất
```

Khi doanh số tụt, hỏi ngay: khách vào ít đi, mua ít đi, hay mỗi đơn nhỏ đi? Chưa trả lời được thì chưa đưa giải pháp.

## GMV và NMV

| Chỉ số | Là gì | Dùng khi |
|---|---|---|
| GMV | Tổng đơn đặt, gồm cả đơn hủy và hoàn | Làm việc với sàn, đặt mục tiêu chung với sàn |
| NMV | GMV trừ đơn hủy, hoàn hàng, hoàn tiền | Quản trị nội bộ, nhìn dòng tiền thật |

```
Tỷ lệ hao hụt GMV sang NMV = (GMV - NMV) / GMV x 100%
```

Dưới khoảng 10 đến 15% là khỏe. Trên 20% thì điều tra ngay: hàng lỗi, xử lý đơn chậm, hay chính sách hoàn trả quá lỏng. Các mốc này là tham khảo, ngành khác nhau sẽ khác.

## Sell-in và sell-out

| | Sell-in (bán vào) | Sell-out (bán ra) |
|---|---|---|
| Là gì | Hàng từ thương hiệu sang kho sàn hoặc kho đối tác | Hàng từ kho đến tay người mua cuối |
| Ai quan tâm | Tài chính, chuỗi cung ứng, bán hàng | Quản lý TMĐT, thương hiệu |
| Chỉ số liên quan | Mức tồn, tỷ lệ đáp ứng đơn | GMV, NMV, tỷ lệ bán hết |

Bán vào cao mà bán ra thấp nghĩa là hàng ứ: lên kế hoạch xả tồn ngay.

## Chẩn đoán lượng khách thấp

| Nguồn | Ý nghĩa | Cách tăng |
|---|---|---|
| Tìm kiếm tự nhiên | Khách gõ từ khóa | Đưa từ khóa chính lên đầu tên sản phẩm |
| Quảng cáo trong sàn | Trả tiền để lên top | Chỉnh giá thầu, từ khóa, ảnh đại diện |
| Chương trình của sàn | Trang khuyến mãi chung | Đăng ký chương trình |
| Người theo dõi gian hàng | Khách cũ quay lại | Khuyến mãi và nội dung đều đặn |
| Từ ngoài sàn | Mạng xã hội, liên kết tiếp thị | Gắn liên kết sản phẩm vào nội dung |

Checklist nhanh:
- Tỷ lệ bấm vào ảnh đại diện thấp (dưới khoảng 2%): đổi ảnh, thử hai ảnh trong 7 ngày.
- Thứ hạng tìm kiếm thấp: sửa tên sản phẩm.
- Chưa tham gia chương trình nào: đăng ký.
- Chưa chạy quảng cáo: thử với ngân sách nhỏ, ít từ khóa, theo dõi sát rồi mới tăng.

## Chẩn đoán tỷ lệ mua thấp

Mốc tham khảo: sàn khoảng 1 đến 3%, website riêng khoảng 0,5 đến 1,5%. Hỏi theo thứ tự:

1. Ảnh và video đủ thuyết phục chưa? Thêm nhiều góc, video minh họa ngắn, ảnh so sánh.
2. Giá có cao hơn đối thủ không? So với 5 người bán đứng đầu cùng từ khóa; tạo combo để tăng giá trị cảm nhận thay vì chỉ giảm giá.
3. Đánh giá đã đủ chưa? Nhắc khách đánh giá sau khi nhận hàng, đúng quy định của sàn.
4. Mô tả đã đủ thông tin chưa? Thêm câu hỏi thường gặp, thông số, cách dùng, chính sách đổi trả.

## Tăng giá trị mỗi đơn

| Cách | Cơ chế | Ví dụ |
|---|---|---|
| Combo | Bán 2 đến 3 món cùng lúc, rẻ hơn mua lẻ | Combo 3 món giá bằng 2,5 món |
| Ngưỡng miễn phí vận chuyển | "Mua thêm một chút để được miễn phí giao" | Đặt ngưỡng cao hơn AOV hiện tại một khoảng vừa phải |
| Bán kèm | Gợi ý món bổ sung ngay trên trang | Mua bình nước, gợi ý ống hút |
| Bán nâng cấp | Bản lớn hơn hoặc cao cấp hơn | Dung tích lớn hơn |
| Voucher theo ngưỡng | Mua đủ mức thì được giảm | Kéo đơn lên đúng mức voucher |

## Chỉ số tồn kho

```
Tỷ lệ bán hết = Đã bán / (Đã bán + Còn tồn) x 100%
Số ngày tồn   = Số lượng tồn / Số lượng bán trung bình mỗi ngày
```

| Tình trạng | Hành động |
|---|---|
| Số ngày tồn trên khoảng 60 | Tồn quá nhiều: giảm giá theo nhóm, tham gia đợt giảm giá để xả |
| Số ngày tồn dưới khoảng 7 | Sắp hết: nhập gấp, tạm giảm quảng cáo để khỏi mất đơn |
| Tỷ lệ bán hết dưới khoảng 50% mỗi tháng | Bán chậm: xem lại giá, trang bán, và có cần khuyến mãi không |

## Mẫu họp số liệu hằng tuần

```
BÁO CÁO TUẦN
GMV tuần này: ___ so với tuần trước: ___ (thay đổi %)
NMV tuần này: ___ | Tỷ lệ hao hụt: ___%
Lượng khách: ___ (thay đổi %) | Nguồn lớn nhất: ___
Tỷ lệ mua: ___% (thay đổi %) | Nghi vấn: ___
Giá trị mỗi đơn: ___ (thay đổi %) | Cơ hội tăng: ___
Đơn hủy và hoàn: ___% | Lý do chính: ___
Mã hàng sắp hết (dưới 7 ngày): ___
Việc tuần sau: 1) ___ 2) ___ 3) ___
```

Điền xong, chọn **một biến đang kéo GMV xuống nhiều nhất** và dồn sức vào đó trong tuần tới.

## Cách trả lời

- Luôn kèm công thức, nguyên nhân có thể, và việc cụ thể. Không dừng ở định nghĩa.
- Dùng số liệu người dùng đưa. Chưa có số thì nói rõ đây là mốc tham khảo, và đề nghị họ xuất báo cáo từ sàn.
- Nếu lưu kết quả, đặt vào Google Docs hoặc Google Sheets mới nếu có kết nối; không thì trả trong cuộc trò chuyện.
