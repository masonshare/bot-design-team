# Bước 0: bản thiết kế dùng chung cho mọi nền tảng

Hãy điền bản thiết kế này trước khi mở bất kỳ ứng dụng nào. Nó không đổi dù bạn chọn ứng dụng nào, và nhờ nó, mỗi màn hình sau đó chỉ còn là việc sao chép và dán. Muốn dùng mẫu đầy đủ hơn, có cả bảng chấm điểm, xem [profile-template.md](../../skills/bot-design/references/profile-template.md).

Mỗi bot chỉ làm một việc. Trả lời ngắn gọn. Mục nào chưa biết thì để trống và ghi "cần quyết định".

## Các mục cần điền

1. **Nhiệm vụ (job).** Bot làm gì, trong 3 đến 5 câu? Kết thúc bằng một câu bắt đầu bằng "Bot này không...".
2. **Người dùng (user).** Ai nói chuyện với bot, và họ đã biết những gì?
3. **Đầu vào (inputs).** Mỗi lần bot nhận gì (một mục tiêu, một tệp, một liên kết, một sự kiện)? Thiếu thông tin thì tìm ở đâu?
4. **Đầu ra (outputs).** Bot trả lại gì (bản nháp, báo cáo, tệp)? Định dạng nào? Ai nhận tiếp theo?
5. **Soul.** Chỉ dẫn thường trực, giữ ngắn: vai trò, giọng điệu, vòng làm việc (làm rõ, nghiên cứu, lập kế hoạch, thực hiện, kiểm tra), và chỗ phải dừng lại hỏi. Quy trình dài thì đưa vào skill, không nhét vào soul.
6. **Skill.** Mỗi quy trình lặp lại là một skill. Với mỗi skill ghi: điều kiện kích hoạt, các bước, và cách kiểm tra kết quả.
7. **Bộ nhớ (memory).** Vài sự thật ban đầu đáng nhớ (sở thích, quy ước đặt tên, bối cảnh lặp lại). Dữ liệu lớn để chỗ khác.
8. **Quyền truy cập (access).** Bot được dùng ứng dụng, thư mục, công cụ nào. Bắt đầu với mức tối thiểu bot cần. Ghi rõ bí mật nào cần dùng và cất trong kho bí mật của ứng dụng, tuyệt đối không ghi vào bản thiết kế.
9. **Quyền hạn (permissions).** Hành động nào bot tự làm, hành động nào phải chờ bạn duyệt. Đặt một cổng duyệt (gate) trước mọi việc khó hoàn tác: đăng, gửi, xóa, tiêu tiền, cài đặt, cấp quyền ghi, bật lịch chạy.
10. **Lịch chạy (routines).** Việc nào chạy theo lịch hoặc theo sự kiện. Ghi lịch, nhiệm vụ, và bài thử bạn sẽ chạy trước khi bật.
11. **Mô hình (model).** Cấp mô hình nào hợp với việc: mô hình mạnh hơn cho suy luận và thiết kế, mô hình nhẹ hơn cho kiểm tra định kỳ. Lưu ý có ứng dụng tự chọn mô hình cho bạn.

## Kiểm tra trước khi dựng

- Nhiệm vụ gói gọn trong một đoạn.
- Mỗi đầu ra có tiêu chí "xong khi" kiểm tra được.
- Mỗi cổng duyệt gắn với một hành động cụ thể.
- Bản thiết kế không chứa bí mật nào.

## Tiếp theo

Mang bản thiết kế đã điền sang [openmausbot.md](openmausbot.md) hoặc [grok-bot.md](grok-bot.md). Bảng trong [field-mapping.md](field-mapping.md) cho biết từng mục đi vào đâu.
