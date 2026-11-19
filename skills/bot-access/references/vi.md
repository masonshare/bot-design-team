# Quyền hạn của bot (bản tiếng Việt của skill bot-access)

Chỉ cho bot những gì nó cần, và đặt cổng duyệt trước mọi thứ không hoàn tác được. Giai đoạn 5 của quy trình thiết kế bot.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Cấp quyền ghi, và mọi hành động gửi, đăng, xóa, chi tiền, cài đặt, commit hoặc push, đều là cổng duyệt (gate): người dùng đồng ý trước. Skill này đề xuất quyền; người dùng là người áp dụng.

## Các bước

### 1. Gắn mọi công cụ với một việc

Liệt kê mọi công cụ, kết nối và skill mà bot đang có hoặc sắp được cấp, và việc trong Công việc cần từng thứ. Không gắn việc nào thì bỏ: dọn đồ thừa giữ ngữ cảnh gọn và bề mặt tấn công ngắn. Với bot hiện hữu, đọc trực tiếp trạng thái đã lưu; thứ không đọc được thì ghi `chưa xác minh`, và lời đồng đội báo không thay thế việc tự đọc lại.

Xong khi: mỗi mục có một việc, hoặc nằm trong danh sách cần bỏ.

### 2. Đặt mức rủi ro và kiểm soát

Đọc và tìm kiếm thì cho thoải mái, bản nháp và ghi trong thư mục làm việc thì cho trong phạm vi, còn mọi hành động ra ngoài hoặc không hoàn tác thì đặt cổng duyệt phía trước.

| Mức rủi ro | Ví dụ | Kiểm soát |
|---|---|---|
| Thấp | Đọc, tìm, tóm tắt | Tự chạy, có ghi nhật ký |
| Vừa | Bản nháp, tệp trong thư mục làm việc | Duyệt trước khi ra ngoài |
| Cao | Đăng nhập, thanh toán, thay đổi hàng loạt | Cổng duyệt mỗi lần; người dùng tự nhập mật khẩu, mã xác thực, CAPTCHA |
| Tới hạn | Xóa dữ liệu, ký, đổi chính sách | Không tự động hóa |

Xong khi: mọi hành động bot làm được đều có một mức.

### 3. Áp dụng các quy tắc

- Đọc trước ghi sau: mọi kết nối bắt đầu ở chế độ chỉ đọc; thêm quyền ghi theo từng công cụ khi một ca thử cần.
- Cổng trước khi gửi, đăng, xóa, chi tiền, cài đặt, commit hoặc push mã, bật lịch chạy.
- Hạn mức tiền nằm trong cài đặt của nền tảng, không viết trong prompt.
- Thông tin xác thực chỉ đặt trong kho bí mật (secret store) hoặc kho kết nối của nền tảng. Không để bí mật, URL webhook hay ghi chú đăng nhập trong prompt, skill, memory, chat hay tệp; nhờ người dùng nhập qua kho bí mật.
- Nhiều tài khoản có nhãn rõ cho một ứng dụng thì tốt hơn nhân đôi bot.
- Điều khiển máy local: tài liệu Grok Bot đặt mặc định là "Ask every time" (hỏi mỗi lần), không phải "chặn". Chọn "Never allow" (không bao giờ cho) với bot mà Công việc không cần máy local.
- Routine chờ duyệt không được phụ thuộc vào câu trả lời đến muộn: thẻ hết hạn (30 phút theo tài liệu Grok Bot) và kết quả an toàn của thẻ hết hạn là không có gì xảy ra.
- Các bot trong một tài khoản dùng chung một máy cloud. Nó không phải ranh giới bảo mật giữa các bot: đừng dựa vào nó để giấu tệp hay bí mật của bot này khỏi bot khác.

### 4. Cho thấy trường hợp xấu nhất

Viết bảng quyền (hành động, mức, kiểm soát, thiệt hại tối đa nếu bot làm sai).

Xong khi: bảng cho thấy thiệt hại tối đa nếu bot làm sai, mọi hành động không hoàn tác đều có cổng, và không có bí mật nào xuất hiện trong đầu ra.

## Giai đoạn tiếp theo

bot-score. Bàn giao bằng đúng 5 mục theo thứ tự: Mục tiêu (Goal), Đầu vào (Inputs), Sản phẩm (Deliverable), Xong khi (Done when), Việc còn mở (Open items). Nếu bot-score chưa được cài, nói với người dùng giai đoạn tiếp theo là bảng điểm cùng 5-10 ca thử (baseline rồi retest) và đề nghị chạy.

## Nguồn

- Masonshare, các mức rủi ro và quy tắc quyền tối thiểu (nguyên bản).
- Tài liệu Grok Bot, máy tính và ứng dụng (mặc định máy local, máy cloud dùng chung, thẻ duyệt hết hạn), https://docs.x.ai/grok-bot/computer-and-apps.
- Lauren Tan, trang chợ dr-eggbot-v2 (không để công cụ thừa), https://x.ai/bot/marketplace/bots/dr-eggbot-v2.
