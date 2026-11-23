# Phỏng vấn bot và go/no-go (bản tiếng Việt của skill bot-interview)

Tìm hiểu bot phải làm gì, rồi chọn công cụ nhẹ nhất đủ làm việc. Giai đoạn 1-2 của quy trình thiết kế bot; giai đoạn sau là bot-shape.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Dừng ở một cổng duyệt (gate), tức là người dùng đồng ý rồi mới đi tiếp, trước mọi việc khó hoàn tác. Skill này chỉ đọc và hỏi; không thay đổi gì.

## Các bước

### 1. Kiểm kê (chỉ với bot đã có)

Trước khi đổi vai trò của một bot hiện hữu, liệt kê chỉ dẫn, kỹ năng và trạng thái bật, quyền và kết nối, mô hình, và mọi tự động hóa truy cập được (trạng thái bật, mục đích, nơi nhận, lịch hoặc sự kiện). Đọc trực tiếp trạng thái đã lưu nếu có quyền và tìm hoạt động xung đột với vai trò mới. Không sửa hoặc tạm dừng gì nếu chưa được phép.

Ghi cho từng mục: nguồn và thời điểm, thay đổi dự kiến, kết quả đọc lại, xung đột còn mở. Thiếu quyền hoặc không xác nhận được danh sách đầy đủ thì ghi `chưa xác minh`; lời đồng đội báo không thay thế việc tự đọc lại. Báo xung đột còn mở trước khi kết luận, và ghi việc thiết kế lại chưa hoàn tất cho đến khi xử lý xong hoặc người dùng chấp nhận rõ rủi ro còn lại.

Nếu yêu cầu đổi cấu hình có nhiều cách hiểu hợp lý và phạm vi ảnh hưởng lớn, trình bày các cách hiểu cùng điều mỗi cách sẽ ảnh hưởng, và làm rõ lựa chọn quyết định trước khi ghi bất kỳ thay đổi nào.

Xong khi: bản kiểm kê đã ghi kèm nguồn, hoặc bot là bot mới và bỏ qua bước này.

### 2. Hỏi trong một tin

Hỏi tất cả trong một tin, mỗi câu kèm gợi ý mặc định để người dùng trả lời nhanh:

- Công việc: bot làm gì, kèm 3 ví dụ thật.
- Việc không bao giờ làm (anti-job, bắt buộc): 2-4 dòng về điều bot tuyệt đối không làm, kể cả khi được nhờ.
- Người dùng: ai nói chuyện với bot, mức am hiểu, ngôn ngữ.
- Đầu vào: dữ liệu, ứng dụng, tệp, tài khoản đang có.
- Đầu ra: định dạng, nơi nhận, ai duyệt.
- Tần suất: theo yêu cầu, theo lịch hay theo sự kiện.
- Rủi ro: làm sai thì thiệt hại gì (tiền, uy tín, dữ liệu).
- Ngân sách: chi phí mô hình chấp nhận được, thời gian dựng, ai bảo trì.
- Nền tảng: Orca (repo này chỉ nhắm tới Orca).

Xong khi: mỗi mục đều có câu trả lời hoặc một giả định đã thống nhất, ghi trong brief.

### 3. Nên làm hay không (go/no-go)

Chọn công cụ nhẹ nhất đủ làm việc:

| Tình huống | Dùng |
|---|---|
| Làm một lần hoặc hiếm, không cần nhớ hay công cụ | Một prompt |
| Quy trình lặp lại mà người dùng đã tự chạy được trong chat | Một skill |
| Các bước cố định, đầu vào cố định, không cần phán đoán | Tự động hóa thường (cron, n8n, Make) |
| Việc lặp lại có phán đoán, cần nhớ ngữ cảnh, có công cụ hoặc lịch | Một bot |
| Mỗi bước đều cần người phán đoán, hoặc hậu quả không hoàn tác được | Không làm bot; đưa checklist |

Bắt đầu từ việc nhàm chán nhất mà người dùng biết rõ từng bước. Nêu kết luận và lý do trong hai câu.

Xong khi: người dùng đã thấy kết luận. Nếu kết luận không phải "bot", dừng và giao phương án nhẹ hơn.

## Giai đoạn tiếp theo

Nếu kết luận là "bot", bàn giao cho bot-shape bằng đúng 5 mục theo thứ tự: Mục tiêu (Goal), Đầu vào (Inputs), Sản phẩm (Deliverable), Xong khi (Done when), Việc còn mở (Open items). Sản phẩm là bản brief. Nếu bot-shape chưa được cài, nói với người dùng giai đoạn tiếp theo là quyết định một bot hay một đội (mặc định một bot, một việc) và đề nghị làm từ bản brief.

## Nguồn

- Masonshare, quy trình thiết kế bot (nguyên bản).
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
