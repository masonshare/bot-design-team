# Routine của bot (bản tiếng Việt của skill bot-routine)

Làm cho một lần chạy không người trông trở nên an toàn, có giới hạn và có một người có tên chịu trách nhiệm. Giai đoạn 4 của quy trình thiết kế bot.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Bật lịch chạy là một cổng duyệt (gate): người dùng đồng ý rồi mới bật. Mọi routine bắt đầu ở trạng thái tạm dừng.

## Các bước

### 1. Kiểm tra có đáng làm routine không

Routine hợp với việc lặp lại có đầu ra dự đoán được. Nếu các bước cố định và không cần phán đoán thì tự động hóa thường (cron, n8n, Make) nhẹ hơn; hãy nói rõ. Ưu tiên kích hoạt theo sự kiện hơn quét dày, và lịch không dày hơn mức đầu ra cần.

Xong khi: người dùng có lý do routine phù hợp, trong một câu.

### 2. Viết đặc tả năm phần

Viết mỗi routine với năm phần, và không bật routine nào thiếu một phần.

| Phần | Ghi |
|---|---|
| Owner (chủ sở hữu) | Người có tên chịu trách nhiệm về routine và nhận các leo thang của nó; không ghi "bot" |
| Trigger (kích hoạt) | Lịch (giờ và múi giờ) hoặc sự kiện, và vì sao chọn cái đó |
| Allowed actions (hành động được phép) | Danh sách chính xác một lần chạy được làm (đọc, soạn nháp, ghi vào thư mục làm việc); thứ không có trong danh sách là không được phép, còn gửi, xóa, chi tiền luôn nằm sau cổng duyệt |
| Escalation path (đường leo thang) | Báo cho ai, bằng cách nào, kèm gì (chuyện gì xảy ra, cần gì, duyệt ở đâu) khi một lần chạy không xong hoặc cần thứ ngoài danh sách; phê duyệt không ai trả lời thì không có gì xảy ra |
| Stop condition (điều kiện dừng) | Khi nào một lần chạy kết thúc (tiêu chí xong, không có gì để báo, giới hạn thời gian hoặc chi phí) và bao nhiêu lần chạy lỗi hoặc rỗng thì đề nghị chủ sở hữu tạm dừng |

Xong khi: đủ năm phần cho mỗi routine, với chủ sở hữu có tên.

### 3. Viết hướng dẫn cho lần chạy

Văn bản routine phải chạy được khi không có ngữ cảnh chat: nói rõ đọc gì, tạo ra gì, ghi ở đâu, và không đụng vào gì. Đầu ra là bản nháp; routine không gửi, xóa hay chi tiền. Trạng thái cần tin được qua các lần chạy (đã gửi gì, còn chờ gì) nằm trong một sổ cái (ledger) có tên, có người chịu trách nhiệm và có ngày: đọc đầu lần chạy, ghi thêm cuối lần chạy; khi sổ cái và chat mâu thuẫn thì sổ cái thắng. Thẻ duyệt có thể hết hạn (30 phút theo tài liệu Grok Bot): lần chạy chờ duyệt không được phụ thuộc vào câu trả lời đến muộn, và thẻ hết hạn thì không có gì xảy ra.

Xong khi: người chưa từng thấy chat vẫn chạy được văn bản này và ra đúng đầu ra mong muốn.

### 4. Tạo ở trạng thái tạm dừng, thử, rồi mới bật

Tạo ở trạng thái tạm dừng. Chạy tay hai lần và đọc cả hai kết quả. Sau đó nhờ người dùng duyệt việc bật (gate). Sau khi nhập vào OpenMausBot, so sánh các routine khai báo trong `team.md` với các tự động hóa thật sự có; thêm cái còn thiếu (ở trạng thái tạm dừng) và báo mọi chỗ khác nhau.

Xong khi: hai lần chạy tay đã đọc và ghi lại, và người dùng đã quyết định có bật hay không.

### 5. Tùy chọn: routine kiểm tra sức khỏe (healthcheck)

Chỉ khi bot có routine chạy không người trông và người dùng muốn kiểm tra định kỳ. Mỗi tuần một lần, theo múi giờ người dùng, ngoài giờ yên lặng, tạo ở trạng thái tạm dừng và chỉ đọc: nó đọc các tự động hóa của bot cùng 4 lần chạy gần nhất, và kiểm tra từng cái có chạy đúng lịch và cho kết quả hữu ích không, có đang bật mà không tạo ra gì hoặc lỗi liên tục không, có chạy dày hơn mức cần không, có trùng cái khác không. Nó im lặng khi mọi thứ đạt; nếu không thì gửi một tin ngắn nêu thay đổi đề xuất và nơi duyệt; nó không tự đổi gì. Văn bản dựng sẵn: `healthcheck-routine.md`.

Xong khi: routine healthcheck đã tạo ở trạng thái tạm dừng, một lần chạy tay không ra tin và một lần ra phát hiện thật, và người dùng đã quyết định.

## Giai đoạn tiếp theo

bot-access cho quyền hạn, hoặc bot-score khi quyền đã xong. Bàn giao bằng đúng 5 mục theo thứ tự: Mục tiêu (Goal), Đầu vào (Inputs), Sản phẩm (Deliverable), Xong khi (Done when), Việc còn mở (Open items). Nếu một skill anh em chưa cài, nói với người dùng giai đoạn tiếp theo theo tên và đề nghị làm.

## Tệp tham chiếu

- `healthcheck-routine.md`: đọc ở bước 5; văn bản routine healthcheck dựng sẵn, có cả tiếng Anh và tiếng Việt.

## Nguồn

- Hướng dẫn Grok Bot cho Linear và các bot chợ overheard, follow-through-agent (năm phần của một routine), https://x.ai/bot/guides/grok-bot-for-linear. CHƯA KIỂM CHỨNG (UNVERIFIED): đọc ngày 2026-11-19 qua bản tóm tắt tự động; trích dẫn có thể là diễn đạt lại.
- Lauren Tan, trang chợ dr-eggbot-v2 (routine kiểm tra sức khỏe), https://x.ai/bot/marketplace/bots/dr-eggbot-v2.
- Tài liệu Grok Bot, máy tính và ứng dụng (thẻ duyệt hết hạn), https://docs.x.ai/grok-bot/computer-and-apps.
