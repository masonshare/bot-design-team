# Dựng bot trong Grok Bot

Hướng dẫn này nói về ứng dụng Grok Bot của xAI (tài liệu: https://docs.x.ai/grok-bot). Đó không phải ứng dụng chat Grok và cũng không phải công cụ dòng lệnh Grok Build. Mọi thông tin dưới đây lấy từ tài liệu chính thức. Các nhãn được đọc từ tài liệu, chưa thử trên ứng dụng, nên hãy đối chiếu trên màn hình.

Trước khi bắt đầu, hãy điền [bản thiết kế chung](00-platform-neutral.md).

## Cần biết trước

- Bot cá nhân không có trang cài đặt. Bạn cấu hình bằng cách nhắn cho Bot trong khung chat.
- Không có ô chỉ dẫn. Tin nhắn đầu tiên bạn gửi đóng vai trò đó.
- Không có bộ chọn mô hình. Grok Bot tự chọn mô hình cho từng việc.
- Không cài được bằng liên kết repo. Tài liệu không nêu lệnh hay liên kết nào để nhập một repo GitHub vào Grok Bot, nên bạn dán văn bản vào khung chat.

## Các bước

1. **Cài và đăng nhập.** Cài từ x.ai/bot và đăng nhập bằng tài khoản Cursor. Xem gói dịch vụ của bạn ở trang get-started trong tài liệu.
2. **Tạo Bot.** Bấm **+** ở đầu thanh bên (hoặc nhấn `Ctrl/Cmd+N`). Trong nhóm (team), **+** mở một menu: chọn **Create a Bot**. Ở **Create New Bot**, nhập tên, chọn hình dạng và màu, rồi bấm **Create**.
3. **Gửi tin nhắn đầu tiên.** Giao cho Bot một việc duy nhất, các nguồn của nó, và những chỗ phải hỏi trước khi làm. Yêu cầu Bot ghi nhớ tất cả. Soạn tin từ bản thiết kế của bạn: nhiệm vụ, người dùng, đầu vào, đầu ra và các cổng duyệt. Dán soul của bot từ `bots/` vào đây (dán soul làm tin nhắn đầu là cách được tài liệu nêu).
4. **Thêm skill.** Nhờ Bot lưu một quy trình thành skill ngay trong chat, và dán văn bản quy trình vào. Hoặc dùng **Teach a task**: mở cuộc trò chuyện một-một, mở chế độ xem máy tính, chọn **Teach a task**, mô tả kết quả, làm một lần, dừng, rồi xem bản nháp. Grok Bot có đọc tệp `SKILL.md` dán vào như một skill hay không thì tài liệu không nói (chưa kiểm chứng). Skill bạn lưu là riêng tư và dùng chung cho mọi Bot của bạn. Bật theo từng Bot từ **Connect apps**, số ứng dụng đã kết nối, rồi **Private skills**.
5. **Kết nối ứng dụng.** Mở **Connect apps**, tìm, thêm, rồi **Authorize**. Gõ `@` trong một tác vụ để dùng ứng dụng. Với máy chủ MCP tùy chỉnh, chọn **Add a custom connector** và điền Name cùng Type (**Remote HTTPS** hoặc **Command**).
6. **Giữ bí mật ngoài khung chat.** Dùng **Vault** (Settings > Vault), 1Password, hoặc thẻ bí mật an toàn do Bot hiện ra. Không dán khóa vào tin nhắn.
7. **Đặt quyền hạn.** Vào **Settings > General > Bot**. **Auto Review** bật sẵn. Ở **Custom Rules**, điền "When Grok Bot wants to:" và "It should:" với **Allow automatically** hoặc **Ask first**, rồi **Add Rule**. Khi các quy tắc chồng nhau, Ask first thắng. Thẻ duyệt có Allow once, Always allow, Deny.
8. **Thêm bộ nhớ.** Nhắn cho Bot "remember: ...". Không có màn hình bộ nhớ. Khi cần, nhờ Bot cho xem, sửa hoặc quên một ký ức.
9. **Thêm lịch chạy sau cùng.** Nhờ Bot tạo lịch ngay trong chat. Mở tên Bot, sang tab **Details** để Pause, Resume, Test, Edit hoặc Delete. Lịch mới chờ đến lần chạy kế tiếp. **Test** chạy ngay và làm việc thật, nên chỉ thử với tác vụ an toàn. Kiểm tra múi giờ ở **Settings > Bot > Timezone**.
10. **Nhóm (tùy chọn).** Chọn một Bot chính (primary) để điều phối các Bot khác, và dùng chat nhóm. Team Bot cần gói Team hoặc Enterprise. Giới hạn chính thức về số Bot trong một chat nhóm không tìm thấy (chưa kiểm chứng).

## Chia sẻ thứ bạn đã dựng

Bot details > **Share** > **Create a copy** > **Publish** > **Copy link** tạo ra một mẫu (template). Mẫu mang theo chỉ dẫn, skill, plugin chính thức và lịch chạy. Mẫu bỏ lại ký ức cá nhân, skill riêng tư, bí mật, tập lệnh và máy chủ MCP; các trang tài liệu không thống nhất về việc ký ức có đi kèm không (chưa kiểm chứng). Người nhập mở liên kết, chọn **Add to Grok Bot**, xem lại, rồi **Add Bot**, và phải tự thêm lại bí mật cùng máy chủ MCP.

## Kiểm tra bot chạy đúng

- Nhờ Bot nhắc lại nhiệm vụ và các quy tắc duyệt của nó.
- Chạy mỗi lịch một lần bằng **Test** trước khi để nó bật.

## Liên quan

[field-mapping.md](field-mapping.md) xếp từng mục thiết kế cạnh vị trí của nó trong OpenMausBot và Grok Bot.
