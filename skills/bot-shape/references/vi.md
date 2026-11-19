# Định hình bot (bản tiếng Việt của skill bot-shape)

Chọn cấu trúc nhỏ nhất vẫn chạy được: một bot làm một việc, hoặc một điều phối cùng vài chuyên viên. Giai đoạn 2 của quy trình thiết kế bot.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Đổi hình dạng là một cổng duyệt (gate): người dùng đồng ý rồi mới dựng hoặc đổi gì.

## Các bước

### 1. Đọc brief

Lấy bản brief phỏng vấn (công việc, anti-job, đầu vào, đầu ra, tần suất, rủi ro). Chưa có brief thì hỏi trước công việc kèm 3 ví dụ và anti-job; thiếu hai thứ đó thì mọi hình dạng đều là đoán, hãy ghi rõ là đoán.

Xong khi: các việc cần xếp đã liệt kê, mỗi việc một dòng.

### 2. Chọn hình dạng

Mặc định là 1 bot làm 1 việc. Chỉ tách thành đội khi công việc có các chuyên môn khác nhau làm một ngữ cảnh quá tải, và mỗi chuyên viên đã tự chạy tốt một mình.

Gộp hai bot khi chúng không bao giờ làm việc rời nhau: cùng đầu vào, cùng người dùng, luôn chạy chung. Nói rõ phép thử nào quyết định.

Một đội gồm 1 điều phối (coordinator) cộng 2-3 chuyên viên. Điều phối nhận yêu cầu, giao đúng chuyên viên, gộp kết quả thành một câu trả lời và báo tiến độ thật. Điều phối không làm việc chuyên môn và không giữ công cụ chuyên môn. Chuyên viên báo ở ba thời điểm: bắt đầu, xong, bị kẹt. Mọi tin nhắn giữa các bot dùng mẫu bàn giao 5 mục (xem Giai đoạn tiếp theo).

Số skill của một bot không phải lý do để tách bot. Việc tách xuất phát từ cảnh báo bot phình (soul hoặc description quá khoảng 600 từ) được đề xuất ở đây và cần cùng một sự duyệt.

Xong khi: hình dạng và lý do đã ghi trong hai câu.

### 3. Mô tả từng bot

Mô tả hành vi mỗi bot bằng bảy câu trả lời: điều kiện kích hoạt, đầu vào, các bước, đầu ra, điểm người duyệt, tiêu chí thành công, quy tắc dừng và hỏi (các ngoại lệ mà bot phải dừng lại hỏi thay vì đoán).

Mẫu đầu ra:

```
Hình dạng: <một bot | điều phối + N chuyên viên>. Vì sao: <phép thử đã quyết định>
Bot: <tên> - <công việc một dòng>
 Kích hoạt / Đầu vào / Các bước / Đầu ra / Điểm người duyệt / Tiêu chí thành công / Dừng và hỏi
```

Xong khi: người dùng đã duyệt hình dạng (gate) và mỗi bot có công việc một dòng cùng bảy câu trả lời.

## Giai đoạn tiếp theo

Bàn giao cho bot-profile, mỗi lần một bot, bằng đúng 5 mục theo thứ tự: Mục tiêu (Goal), Đầu vào (Inputs), Sản phẩm (Deliverable), Xong khi (Done when), Việc còn mở (Open items). Nếu bot-profile chưa được cài, nói với người dùng giai đoạn tiếp theo là điền hồ sơ 13 mục cho từng bot (mục không cần thì ghi lý do) và đề nghị bắt đầu.

## Nguồn

- Masonshare, quy trình thiết kế bot (nguyên bản).
- Tài liệu OpenMausBot, https://docs.openmausbot.com/docs/features/chat-and-teams (đội, Chief of Staff).
