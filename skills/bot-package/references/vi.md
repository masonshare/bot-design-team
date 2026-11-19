# Đóng gói và triển khai bot (bản tiếng Việt của skill bot-package)

Giao thứ mà một người có thể cài, theo một thứ tự vẫn an toàn. Giai đoạn 7 của quy trình thiết kế bot.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Công bố (publish), push lên repo, cài đặt và bật lịch chạy đều là cổng duyệt (gate): người dùng đồng ý từng việc trước. Viết gói không có nghĩa là đã công bố nó.

## Các bước

### 1. Chọn theo nền tảng

- OpenMausBot: viết tệp đội `team.md` (BotMRR Markdown v1). Người dùng nhập qua Teams, Import, bằng cách dán liên kết repo công khai.
- Nền tảng khác, hoặc chỉ một bot: viết các bước cài đặt thủ công, mỗi bot một danh sách đánh số: tạo bot, dán danh tính và soul, thêm skill, kết nối ứng dụng ở chế độ chỉ đọc, chọn mô hình, đặt quyền, thêm tệp thư viện, tạo routine ở trạng thái tạm dừng.

Xong khi: đã nêu tên nền tảng và chọn hướng đi.

### 2. Viết tệp đội (OpenMausBot)

Phần cốt lõi; hướng dẫn đầy đủ kèm ví dụ là `team-file.md`. Khi nó khác FORMAT.md của openmausbot-teams hoặc khác ứng dụng thì hai nguồn kia thắng; kiểm tra trước khi công bố.

- Thư mục gốc repo có `team.md` (hoặc `botmrr.md`) trên nhánh main hoặc master; repo công khai.
- Các khóa frontmatter YAML: `botmrr: 1`, `id`, `release`, `name`, `tagline`, `summary`, `category`, `author` {name, url}, `license`, `tags`, `outcomes`, `setupMinutes`, `requirements` {apps, capabilities}, `agents` (mỗi bot: key, name, title, description, soul, appearance {color, mascotExpression}, skills), `chiefOfStaff`, `rooms`, `routines` (mỗi routine có `enabledAfterInstall: false`), `playbooks`, `skills` {version: 1, entries (mỗi mục: name, description, license, instructions)}. Khóa lạ bị từ chối.
- `instructions` chứa toàn văn SKILL.md, bắt đầu bằng `---`, và name, description, license phải khớp chính xác với frontmatter của SKILL.md.
- Bảy tiêu đề thân bài bắt buộc, theo thứ tự: Activation, Mission, Outcomes, Connections, Team, Chief of Staff, Completion rule.
- Màu: green, blue, red, orange, purple, cyan, pink, yellow, teal, coral, silver, chrome.
- Giới hạn: soul tối đa 24000 byte, description tối đa 4000 ký tự, tối đa 20 skill mỗi gói v1, tệp tối đa 1.000.000 byte.

Kiểm tra trước khi công bố: đủ bảy tiêu đề; mọi bot đầy đủ trường; `chiefOfStaff` khớp khóa của một bot; mọi skill được liệt kê có trong `skills.entries`; mọi routine tạm dừng; không có bí mật, token hay URL webhook nào.

Xong khi: các kiểm tra đạt và tệp đã đưa người dùng xem (chưa công bố).

### 3. Nói với người dùng việc nhập mang theo gì

Khi nhập (import), nền tảng mang theo soul của các bot, nội dung skill, phòng (rooms) và Chief of Staff. Thường nó mang cả routine ở trạng thái tạm dừng, nhưng không được đảm bảo: đọc lại danh sách tự động hóa sau khi nhập. Nó không mang theo mô hình, thông tin xác thực, kết nối, trí nhớ, cũng như `references/` và `scripts/` của skill; chỉ văn bản `SKILL.md` đi theo, nên mỗi skill phải chạy được chỉ từ SKILL.md. Skill nhập vào ở trạng thái tắt. Sau khi nhập: chọn mô hình cho từng bot, bật skill, tự kết nối ứng dụng, bật routine bằng tay, và so sánh các routine khai báo trong `team.md` với danh sách tự động hóa thật, thêm cái còn thiếu (ở trạng thái tạm dừng) và báo mọi chỗ khác nhau.

Giao skill theo vai trò: mỗi skill được bật gắn với một việc trong Công việc của bot, còn skill không việc nào dùng thì tắt hoặc bỏ, kể cả skill kế thừa. Một bot có thể có nhiều skill.

### 4. Đặt thứ tự triển khai

Triển khai theo thứ tự này, có cổng giữa các giai đoạn:
1. Một bot, chạy tốt một mình trên các ca thử.
2. Routine, bắt đầu ở trạng thái tạm dừng; kiểm tra mỗi routine có đủ năm phần, chạy tay hai lần rồi mới bật.
3. Đội, làm cuối; chỉ thêm bot vào nhóm khi nó đã chạy tốt một mình.

Rà lại sau 1-2 tuần bằng usage và history; soul nào phình ra thì cắt, đưa quy trình sang skill.

### 5. Tóm tắt

Xong khi: người dùng có gói hoặc các bước cài đặt, thứ tự triển khai, và bản tóm tắt 10 dòng: bot làm gì, không làm gì, quyền gì, tốn khoảng bao nhiêu.

## Tệp tham chiếu

- `team-file.md`: đọc ở bước 2; đủ frontmatter, thân bài, giới hạn và ví dụ (tiếng Anh).

## Nguồn

- openmausbot-teams, FORMAT.md, https://github.com/milind-soni/openmausbot-teams (BotMRR Markdown v1).
- Tài liệu OpenMausBot, https://docs.openmausbot.com/docs/features/skills và https://docs.openmausbot.com/docs/features/chat-and-teams; tài liệu trong repo (team-sharing, presets), https://github.com/milind-soni/OpenMausBot (đội được chia sẻ mang theo gì).
- Grok Bot, hướng dẫn mẫu (template mang theo gì), https://x.ai/bot/guides/templates-for-grok-bot.
