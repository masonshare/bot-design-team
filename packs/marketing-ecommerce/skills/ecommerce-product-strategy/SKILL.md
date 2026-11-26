---
name: ecommerce-product-strategy
description: Chiến lược danh mục sản phẩm cho bán hàng TMĐT - chẩn đoán vì sao sản phẩm không bán được, chia vai trò mã hàng (kéo khách, chủ lực, sinh lời), thiết kế combo, thử nghiệm sản phẩm mới trước khi nhập nhiều. Dùng khi hỏi "nên bán sản phẩm nào trước", "chọn sản phẩm chủ lực thế nào", "làm combo ra sao", "thử sản phẩm mới thế nào". English - e-commerce product strategy - diagnose slow sellers, assign SKU roles (traffic / hero / profit), build bundles, run a staged test-and-scale loop, and finish with a SKU portfolio map.
---

# Chiến lược sản phẩm TMĐT

Bán online không phải là đem hàng cửa hàng lên mạng. Sản phẩm thắng trên sàn phải được nghĩ từ nền tảng: ảnh đại diện, từ khóa, thuật toán gợi ý, và thói quen mua qua màn hình.

## Khi không dùng skill này

- Ý tưởng hoàn toàn mới, chưa có bằng chứng có người cần: kiểm chứng nhu cầu trước (dùng skill kiểm chứng ý tưởng nếu có).
- Sửa trang sản phẩm đang bán: dùng `ecommerce-store-optimization`.
- Tính lãi mỗi mã hàng, hòa vốn: tính riêng hoặc dùng `startup-metrics-framework`.
- Nếu `brand-profile.md` của khách có sẵn, đọc để biết định vị giá và nhóm khách trước khi đề xuất.

## Bước 0: chẩn đoán khi sản phẩm không bán

Xác định nút thắt ở tầng nào của phễu:

```
Lượt hiển thị thấp -> vấn đề từ khóa, thứ hạng, quảng cáo
Tỷ lệ bấm thấp    -> vấn đề ảnh đại diện, giá, tiêu đề
Tỷ lệ mua thấp    -> vấn đề ảnh mô tả, đánh giá, giá, combo
```

Hỏi ba câu: quảng cáo trong sàn đã chạy chưa và hiệu quả ra sao; tỷ lệ bấm của trang này là bao nhiêu (mốc tham khảo từ khoảng 1,5% là ổn); tỷ lệ mua là bao nhiêu (mốc tham khảo từ khoảng 2% với hàng tiêu dùng nhanh). Chưa có số thì xin họ xuất báo cáo của sàn.

## Nghĩ từ nền tảng trước

Ở cửa hàng, khách chạm, cầm, thử. Trên sàn, khách chỉ có ảnh, video, đánh giá. Ảnh đại diện chỉ có vài giây: nếu không nhìn ra đó là món gì thì khách không bấm.

Câu hỏi kiểm tra khi chọn hoặc thiết kế sản phẩm:
- Có mô tả được bằng ảnh tĩnh, không cần trải nghiệm thật?
- Bao bì có hợp vận chuyển (gọn, khó vỡ)?
- Giá đủ để sau phí sàn (thường vài đến mười mấy phần trăm) và phí giao vẫn còn lãi?
- Đã có người tìm từ khóa này trên sàn chưa (nhu cầu có sẵn)?
- Sản phẩm cần tư vấn nhiều thì có chat hoặc video bù, hay nên tránh kênh này?

## Ba vai trò của mã hàng

Đừng giao cùng một mục tiêu cho cả danh mục.

| | Mã kéo khách | Mã chủ lực | Mã sinh lời |
|---|---|---|---|
| Mục tiêu | Lượt xem, khách mới | Doanh số, đánh giá, thứ hạng | Biên lợi nhuận, giá trị khách lâu dài |
| Giá | Thấp nhất | Tầm trung | Cao nhất |
| Biên gộp tham khảo | Khoảng 15 đến 25% | Khoảng 30 đến 45% | Từ khoảng 50% |
| Giảm giá chớp nhoáng | Thường xuyên | Thỉnh thoảng | Hiếm |
| Chi quảng cáo | Nhiều | Nhiều | Ít |
| Ví dụ | Bản mini, mẫu thử | Cỡ chuẩn | Hộp quà, bản cao cấp |

Lỗi hay gặp: dùng mã chủ lực làm mã kéo khách liên tục. Biên mỏng đi và thương hiệu mất giá trong mắt khách.

## Combo kiểu "1 + X"

```
1 = sản phẩm chính (mã chủ lực)
X = một hoặc nhiều món bổ sung
Giá combo thấp hơn mua rời, nhưng biên combo vẫn tốt hơn biên trung bình của các món rời
```

Ví dụ ngắn: sữa dưỡng thể cộng tẩy tế bào chết thành bộ chăm da hai bước; cà phê hạt cộng phin cộng ly thành bộ pha tại nhà; món đồ chơi cộng pin thành bộ chơi được ngay.

Kiểm trước khi làm combo:
- Món X có liên quan hợp lý với món chính, không ghép bừa?
- Giá trị khách cảm nhận của combo lớn hơn giá bán?
- Biên combo không thấp hơn biên trung bình các món rời?
- Có ảnh riêng cho combo, không chỉ ghép hai ảnh sản phẩm?

## Thử rồi nhân lên: bốn giai đoạn

**1. Tìm hiểu.** Mục tiêu: ý tưởng có nhu cầu thật. Xem từ khóa và người bán đứng đầu trên sàn; đọc đánh giá 1 đến 2 sao của đối thủ xem khách phàn nàn gì; xem xu hướng trên nền tảng video; xem xu hướng tìm kiếm 12 tháng. Đầu ra: 5 đến 10 ý tưởng kèm giả thuyết.

**2. Chuẩn bị.** Không nhập vội. Xác định người mua cụ thể; làm trang bán đầy đủ; tính chi phí (giá vốn, phí sàn, phí giao) xem biên đạt ngưỡng chưa; nhập lô nhỏ để thử (hàng chục sản phẩm); đặt trước mục tiêu 30 ngày.

**3. Thử và chỉnh.** Chạy quảng cáo ngân sách nhỏ 14 đến 30 ngày; mỗi tuần xem khách vào, tỷ lệ mua, giá trị đơn để thấy nút thắt; đọc tin nhắn và đánh giá đầu tiên; thử hai ảnh đại diện trong 7 ngày; chỉnh giá nếu tỷ lệ mua thấp bất thường.

Quyết định sau 30 ngày:

| Kết quả | Quyết định |
|---|---|
| Đạt mục tiêu | Đi tiếp sang giai đoạn 4 |
| Gần đạt, có tín hiệu tốt | Chỉnh thêm 2 đến 4 tuần |
| Không đạt, không tín hiệu | Dừng, chuyển mã khác |

**4. Nhân lên.** Nhập đủ tồn cho vài tháng để không đứt hàng khi lên thứ hạng; tăng quảng cáo từng bước (ví dụ 20 đến 50% mỗi tuần) chỉ khi hiệu quả quảng cáo vượt ngưỡng có lãi; mở kênh thứ hai; làm combo 1 + X; lấy thêm ý từ đánh giá và tin nhắn để quay lại giai đoạn 1 cho mã kế tiếp.

Các con số trên là mốc khởi đầu. Hãy nói rõ chỗ nào là giả định để chủ shop thay bằng số thật của họ.

## Kết quả bắt buộc: bản đồ danh mục

Sau mỗi lần phân tích, trả mẫu sau đã điền:

```
DANH MỤC HIỆN TẠI
Mã kéo khách: ___  Giá: ___  Biên: ___%
Mã chủ lực:   ___  Giá: ___  Biên: ___%  Đánh giá: ___
Mã sinh lời:  ___  Giá: ___  Biên: ___%
Combo (1 + X): ___ + ___  Giá: ___  Biên: ___%
Đang thử: ___  Giai đoạn: ___  Mục tiêu 30 ngày: ___  Hạn: ___
THIẾU: vai trò nào chưa có?
VIỆC TIẾP THEO: một việc cụ thể làm trong 7 ngày
```

Giao dưới dạng Google Docs hoặc Google Sheets mới nếu có kết nối, không thì trả ngay trong cuộc trò chuyện. Đây là bản nháp để chủ shop duyệt, skill không tự nhập hàng hay chạy quảng cáo.
