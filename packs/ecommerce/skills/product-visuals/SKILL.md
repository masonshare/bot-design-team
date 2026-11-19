---
name: product-visuals
description: Produces product images and banners for Vietnamese online shops from a written brief, using the connected Magnific or Canva tools, and returns candidates with a self-check for the owner to approve. Use when the owner or the marketing bot gives a brief or asks for a product photo, a background change, a cleaned-up image, a marketplace cover image, a promotion banner, a Canva design, or resized versions for several channels. Vietnamese triggers - hình ảnh sản phẩm, ảnh sản phẩm, tạo banner, ảnh bìa sàn, xóa nền, đổi nền, thiết kế Canva, ảnh quảng cáo.
license: MIT
metadata:
  author: Masonshare
  version: "0.1.1"
  language: vi (tiếng Việt)
  bot: Product Visual Designer
---

# Product visuals (hình ảnh sản phẩm)

Tạo ảnh sản phẩm và banner theo brief bằng công cụ Magnific hoặc Canva đã được kết nối. Chỉ tạo bản nháp để duyệt; không đăng lên sàn hay website. Chưa kiểm chứng bot này dùng được Magnific/Canva trong mọi môi trường: kiểm tra ở bước 1.

## Đầu vào

Brief gồm các trường (theo mẫu của skill product-marketing-strategy): mục tiêu, ảnh gốc của sản phẩm, khách mục tiêu, thông điệp, chữ bắt buộc trên hình (nguyên văn), phong cách và màu, kích thước và nơi dùng, số lượng, điều cấm, hạn giao, người duyệt. Thiếu trường bắt buộc (ảnh gốc, kích thước, chữ trên hình) thì hỏi một lượt, tối đa 4 câu. Brief không có ảnh gốc thì không tạo ảnh "giống sản phẩm thật" mà chỉ đề xuất bố cục.

## Quy trình

Mọi câu trả lời về việc tạo ảnh phải có dòng: “Ước tính chi phí: khoảng X credit (≈ Y đ) cho Z ảnh. Trả lời “đồng ý” để tiếp tục hoặc “hủy” để dừng.” Ước tính là chi phí của bước tạo ảnh tốn credit sắp làm (số ảnh × credit mỗi ảnh), không phải chi phí mô tả miễn phí. Điền số thực tế; nếu chưa tính được, ghi lý do thay cho số và không tạo ảnh tốn credit cho đến khi báo được chi phí và được đồng ý.

1. **Kiểm tra công cụ và ngân sách.** Xác nhận Magnific hoặc Canva dùng được (gọi một lệnh đọc đơn giản). Không dùng được thì báo chủ shop nên kết nối gì và dừng, kèm nội dung brief đã chuẩn hóa. Xong khi biết công cụ nào dùng được.
2. **Chốt thông số.** Bảng: nơi dùng | kích thước px | tỷ lệ | định dạng. Mặc định tham khảo: ảnh sản phẩm vuông 1:1, banner ngang, dọc 9:16 cho TikTok; chủ shop kiểm tra kích thước hiện hành của từng sàn vì có thể đổi. Xong khi mỗi nơi dùng có kích thước.
3. **Viết lời nhắc hoặc cấu trúc thiết kế.** Mô tả chủ thể, bố cục, ánh sáng, nền, màu, chỗ chừa cho chữ. Chữ trên hình: ưu tiên đặt chữ bằng công cụ thiết kế (Canva) thay vì để mô hình tạo ảnh vẽ chữ, vì chữ tiếng Việt có dấu dễ sai.
4. **Điểm dừng chi phí, rồi tạo 2-3 phương án.** Trước mọi thao tác tạo ảnh tốn phí (Magnific hoặc Canva trả phí), báo ước tính chi phí (số ảnh, credit hoặc VND nếu quy đổi được) và **dừng chờ chủ shop trả lời đồng ý**. Chưa có đồng ý rõ ràng thì không tạo. Việc không tốn phí (viết lời nhắc, chốt thông số) vẫn làm được. Sau đồng ý, làm từ ảnh gốc: xóa nền, đổi nền, làm sạch, chỉnh sáng. Giữ nguyên sản phẩm (hình dạng, màu, logo); không thêm chi tiết sản phẩm không có thật.
5. **Tự kiểm từng ảnh** bằng cách xem kết quả thật: sản phẩm đúng hình dạng/màu, chữ đúng nguyên văn có đủ dấu, không méo tay/ngón/logo lạ, đúng kích thước, không vi phạm "điều cấm" trong brief. Phương án trượt thì sửa một lần hoặc loại và ghi lý do.
6. **Bàn giao.** Danh sách phương án kèm liên kết hoặc tên tệp, đạt/không đạt từng mục tự kiểm, đề xuất 1 phương án. Chờ chủ shop duyệt.

**Dữ kiện đã dùng — bắt buộc ở đầu mỗi bản nháp:** Liệt kê từng dữ kiện sản phẩm được sử dụng, mỗi dòng kèm trích nguyên văn từ đầu vào; nếu không có, ghi “Không có dữ kiện sản phẩm được cung cấp”. Chỉ đưa dữ kiện trích được vào bản nháp; dữ kiện không trích được chỉ xuất hiện dưới dạng [CẦN XÁC NHẬN: ...]. Áp dụng cho cả tiêu đề, nội dung, lời thoại, chữ và mô tả cảnh/hình.

Ví dụ đầu vào chỉ ghi “trà sen”: đúng: Dữ kiện đã dùng: “trà sen”; bản nháp: “trà sen” hoặc “[CẦN XÁC NHẬN: trà ướp sen]”, “[CẦN XÁC NHẬN: gói trà sen]”. Sai: viết “trà ướp sen” hoặc “gói trà sen” như dữ kiện đã xác nhận.


Chỉ dữ kiện có nguyên văn trong đầu vào mới được viết như sự thật. Bao bì (gói, hộp, túi, lọ), đặc tính (tự nhiên, nguyên chất, hương vị), cách dùng, công dụng, chất liệu và mọi thời hạn đều phải ghi [CẦN XÁC NHẬN: nội dung] nếu đầu vào không nêu.

Trước khi gửi, đọc lại từng dòng bản nháp (kể cả bản ngắn, tiêu đề, mô tả ảnh, thông điệp); mỗi thuộc tính sản phẩm hoặc cam kết không có nguyên văn trong đầu vào thì đổi thành [CẦN XÁC NHẬN: ...].

## Định dạng đầu ra

```
Ước tính chi phí: khoảng X credit (≈ Y đ) cho Z ảnh; hoặc chưa tính được vì ...
Công cụ dùng: Magnific | Canva | không dùng được (lý do)
Thông số: nơi dùng | kích thước | định dạng
Phương án 1..3: tên tệp/liên kết | mô tả | tự kiểm (hình dạng, màu, chữ, kích thước)
Đề xuất: phương án X, vì ...
Cần chủ shop duyệt: ...
```

## Việc không làm

- Không đăng ảnh lên sàn, website, mạng xã hội; không gửi cho khách.
- Không tạo ảnh có người thật, người nổi tiếng, logo hay thương hiệu không thuộc shop; không giả ảnh đánh giá khách, ảnh "trước/sau" bịa.
- Không thay đổi sản phẩm so với ảnh gốc theo hướng đánh lừa (màu, kích cỡ, chất liệu).
- Không xóa hay ghi đè ảnh gốc; lưu bản mới với tên khác.
- Không chi tiêu vượt mức chủ shop đã duyệt; không lưu khóa hay token trong skill.

## Phép thử nghiệm thu

Prompt: "Brief: ảnh bìa Shopee 1:1 cho túi xách nữ màu kem (có ảnh gốc), nền trắng sạch, chữ 'Giảm 20% đến 12.12'. Làm 2 phương án."

Đạt khi: (1) đã kiểm tra công cụ trước khi tạo, hoặc báo rõ không dùng được; (2) có 2 phương án 1:1 từ ảnh gốc, túi giữ nguyên hình và màu; (3) chữ đúng nguyên văn "Giảm 20% đến 12.12" có dấu đúng, hoặc đặt riêng ở bước thiết kế; (4) có bảng tự kiểm cho từng ảnh; (5) không có hành động đăng.

Phép thử kích hoạt: nên kích hoạt với "xóa nền giúp mình ảnh này", "làm banner theo brief đính kèm"; không kích hoạt với "viết kịch bản video giới thiệu", "viết tiêu đề sản phẩm".
