---
name: product-video
description: Writes the script, shot list and edit plan for a short Vietnamese product video and produces a draft with the connected Magnific tools, after the owner approves the plan and cost. Use when the owner or the marketing bot asks for a product intro video, a short video for TikTok Shop, Reels or a listing, a video script, a shot list, voiceover, subtitles, or a video made from product photos. Vietnamese triggers - video sản phẩm, kịch bản video, video giới thiệu sản phẩm, video TikTok bán hàng, dựng video, lời thoại, phụ đề, kịch bản quay.
license: MIT
metadata:
  author: Masonshare
  version: "0.1.1"
  language: vi (tiếng Việt)
  bot: Product Video Producer
---

# Product video (video sản phẩm)

Lập kịch bản, danh sách cảnh, kế hoạch dựng, rồi tạo bản nháp bằng Magnific đã kết nối. Chỉ tạo bản nháp để duyệt; không đăng video. Chưa kiểm chứng bot dùng được Magnific trong mọi môi trường: kiểm tra ở bước 1.

## Đầu vào

**Dữ kiện đã dùng — bắt buộc ở đầu mỗi bản nháp:** Liệt kê từng dữ kiện sản phẩm được sử dụng, mỗi dòng kèm trích nguyên văn từ đầu vào; nếu không có, ghi “Không có dữ kiện sản phẩm được cung cấp”. Chỉ đưa dữ kiện trích được vào bản nháp; dữ kiện không trích được chỉ xuất hiện dưới dạng [CẦN XÁC NHẬN: ...]. Áp dụng cho cả tiêu đề, nội dung, lời thoại, chữ và mô tả cảnh/hình.

Ví dụ đầu vào chỉ ghi “trà sen”: đúng: Dữ kiện đã dùng: “trà sen”; bản nháp: “trà sen” hoặc “[CẦN XÁC NHẬN: trà ướp sen]”, “[CẦN XÁC NHẬN: gói trà sen]”. Sai: viết “trà ướp sen” hoặc “gói trà sen” như dữ kiện đã xác nhận.


Chỉ dữ kiện có nguyên văn trong đầu vào mới được viết như sự thật. Bao bì (gói, hộp, túi, lọ), đặc tính (tự nhiên, nguyên chất, hương vị), cách dùng, công dụng, chất liệu và mọi thời hạn đều phải ghi [CẦN XÁC NHẬN: nội dung] nếu đầu vào không nêu.

Trước khi gửi, đọc lại từng dòng bản nháp, gồm lời thoại, mô tả cảnh và chữ trên hình; mỗi thuộc tính sản phẩm hoặc cam kết không có nguyên văn trong đầu vào thì đổi thành [CẦN XÁC NHẬN: ...].

Brief (mẫu của skill product-marketing-strategy): mục tiêu, sản phẩm và ảnh/video gốc, khách mục tiêu, thông điệp, chữ và lời thoại bắt buộc, phong cách, kênh và tỷ lệ, độ dài, điều cấm, hạn giao, người duyệt. Mặc định: dọc 9:16, 15-30 giây, có phụ đề tiếng Việt. Thiếu ảnh/video gốc của sản phẩm thì hỏi; không tạo cảnh "sản phẩm thật" khi không có nguồn.

## Quy trình

1. **Kiểm tra công cụ và chi phí.** Xác nhận Magnific dùng được. Video tốn nhiều credit: ước tính chi phí cho cả kế hoạch và báo chủ shop trước khi tạo, bằng câu cố định: "Ước tính chi phí: khoảng X credit (≈ Y đ) cho Z cảnh. Trả lời 'đồng ý' để tiếp tục hoặc 'hủy' để dừng." Chưa có 'đồng ý' thì không gọi công cụ tạo tốn phí. Không dùng được thì giao kịch bản và danh sách cảnh để chủ shop tự quay/dựng. Xong khi biết chế độ (tạo được hoặc chỉ kịch bản).
2. **Kịch bản.** Cấu trúc 15-30 giây: mở 0-3 giây gây chú ý (hook), 2-3 điểm lợi ích có thật, bằng chứng (cận cảnh chất liệu, cách dùng), lời kêu gọi hành động. Lời thoại ngắn, tự nhiên, đọc được trong thời lượng cảnh (khoảng 2-3 từ mỗi giây). Chỉ dùng dữ kiện chủ shop cung cấp.
3. **Danh sách cảnh.** Bảng: cảnh | thời lượng | hình (nguồn: ảnh gốc, quay, tạo) | lời thoại/chữ | âm thanh. Cảnh nào cần quay thật thì ghi rõ để chủ shop quay.
4. **Kế hoạch dựng.** Nhạc nền (nguồn hợp lệ, không dùng nhạc có bản quyền không rõ), phụ đề tiếng Việt có dấu, tông màu, chuyển cảnh. Xong khi chủ shop duyệt kịch bản và chi phí (cổng duyệt). Nếu dựng cảnh từ ảnh tạo mới: làm trước storyboard ảnh tĩnh (mỗi cảnh một khung hình chính), chủ shop duyệt rồi mới làm chuyển động.
5. **Tạo bản nháp.** Chạy từng cảnh hoặc cả video bằng công cụ Magnific theo kế hoạch đã duyệt, rồi xem kết quả thật (khung hình chủ chốt): sản phẩm đúng hình và màu, không méo, chữ và phụ đề đúng nguyên văn, đúng tỷ lệ, âm lượng ổn. Sửa một lần cho cảnh trượt, sau đó báo phần còn lại.
6. **Bàn giao.** Liên kết hoặc tên tệp, bảng tự kiểm, các cảnh còn cần quay thật, chi phí đã dùng.

## Định dạng đầu ra

```
Chế độ: tạo được | chỉ kịch bản (lý do)
Kịch bản: hook | thân | CTA (kèm lời thoại)
Danh sách cảnh: cảnh | giây | hình | lời/chữ | âm
Kế hoạch dựng: nhạc, phụ đề, tông màu
Chi phí ước tính / đã dùng: ...
Tự kiểm: hình sản phẩm | chữ | tỷ lệ | âm thanh
Cần chủ shop duyệt: ...
```

## Việc không làm

- Không đăng video lên TikTok, Shopee, YouTube hay bất kỳ nơi nào; không gửi cho khách.
- Không bắt đầu tạo hàng loạt khi chủ shop chưa duyệt chi phí.
- Không giả giọng hay hình ảnh người thật hoặc người nổi tiếng; không tạo cảnh "khách review" hay lời chứng thực bịa.
- Không chèn cam kết công dụng y tế, số liệu không có nguồn, so sánh nêu tên đối thủ.
- Không dùng nhạc, hình, clip không rõ bản quyền; không lưu khóa hay token trong skill.

## Phép thử nghiệm thu

Prompt: "Làm video 20 giây giới thiệu bình giữ nhiệt 500ml màu xanh, giá 189.000đ, giữ nóng 6 giờ (đã kiểm nghiệm nội bộ), có 4 ảnh gốc, đăng TikTok Shop."

Đạt khi: (1) có kịch bản dọc 9:16 đúng 20 giây, tổng thời lượng các cảnh bằng 20; (2) mọi dữ kiện (500ml, xanh, 189.000đ, 6 giờ) khớp đề bài, không thêm thông số mới; (3) có ước tính chi phí và dừng chờ duyệt trước khi tạo; (4) cảnh dùng 4 ảnh gốc được ghi rõ nguồn; (5) không có hành động đăng.

Phép thử kích hoạt: nên kích hoạt với "viết lời thoại cho video 15 giây", "làm video từ mấy ảnh này"; không kích hoạt với "làm banner sale", "viết mô tả sản phẩm".
