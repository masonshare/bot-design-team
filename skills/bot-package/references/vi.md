# Đóng gói và triển khai bot (bản tiếng Việt của skill bot-package)

Giao thứ mà một người có thể cài, theo một thứ tự vẫn an toàn. Giai đoạn 7 của quy trình thiết kế bot.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Công bố (publish), push lên repo, chia sẻ bot, cài đặt và bật lịch chạy đều là cổng duyệt (gate): người dùng đồng ý từng việc trước. Viết gói không có nghĩa là đã công bố nó.

## Các bước

### 1. Chọn hướng đi

Repo này nhắm tới Orca. Viết các bước cài đặt thủ công, mỗi bot một danh sách đánh số: tạo bot, dán danh tính và soul, thêm skill, kết nối ứng dụng ở chế độ chỉ đọc, chọn mô hình, đặt quyền, thêm tệp thư viện, tạo routine ở trạng thái tạm dừng. Để trao bot cho người khác, chủ sở hữu có thể dùng link chia sẻ bot của Orca; người nhận vẫn tự chọn mô hình và kết nối ứng dụng trên máy của mình.

Xong khi: đã chọn hướng đi và nêu rõ đích (máy của mình, hoặc link chia sẻ).

### 2. Nói với người dùng việc chia sẻ mang theo gì

Giả định việc chia sẻ chỉ mang soul và văn bản skill. Mô hình, thông tin xác thực, kết nối và trí nhớ ở lại máy chủ sở hữu, và mỗi skill phải chạy được chỉ từ SKILL.md, vì `references/` và `scripts/` có thể không đi theo (chưa kiểm chứng: thử một lần chia sẻ thật). Sau khi chia sẻ: người nhận chọn mô hình, bật skill, tự kết nối ứng dụng và bật routine bằng tay.

Giao skill theo vai trò: mỗi skill được bật gắn với một việc trong Công việc của bot, còn skill không việc nào dùng thì tắt hoặc bỏ, kể cả skill kế thừa. Một bot có thể có nhiều skill.

Kiểm tra trước khi chia sẻ: không có bí mật, token hay URL webhook trong soul hoặc skill; không có dữ liệu thật của công ty hay khách hàng trong gói.

### 3. Đặt thứ tự triển khai

Triển khai theo thứ tự này, có cổng giữa các giai đoạn:
1. Một bot, chạy tốt một mình trên các ca thử.
2. Routine, bắt đầu ở trạng thái tạm dừng; kiểm tra mỗi routine có đủ năm phần, chạy tay hai lần rồi mới bật.
3. Đội, làm cuối; chỉ thêm bot vào nhóm khi nó đã chạy tốt một mình.

Rà lại sau 1-2 tuần bằng usage và history; soul nào phình ra thì cắt, đưa quy trình sang skill.

### 4. Tóm tắt

Xong khi: người dùng có các bước cài đặt, thứ tự triển khai, và bản tóm tắt 10 dòng: bot làm gì, không làm gì, quyền gì, tốn khoảng bao nhiêu.
