# Bảng ánh xạ các mục

Mỗi mục của [bản thiết kế chung](00-platform-neutral.md) nằm ở đâu trong từng ứng dụng. "Chat" nghĩa là bạn đặt mục đó bằng cách nhắn cho Bot trong khung chat, vì Grok Bot cá nhân không có trang cài đặt.

| Mục thiết kế | OpenMausBot | Grok Bot |
|---|---|---|
| Tên | Bot settings, Name (hoặc **Set me up**) | **Create New Bot**, ô tên |
| Nhiệm vụ (dòng vai trò) | Title và description | Label (trên điện thoại gọi là Title); tin nhắn đầu tiên |
| Người dùng | Văn bản Instructions (một phần của soul) | Tin nhắn đầu tiên, trong chat |
| Đầu vào | Văn bản Instructions; ứng dụng đã kết nối và working folder | Tin nhắn đầu tiên; **Connect apps** |
| Đầu ra | Văn bản Instructions (định dạng và người nhận) | Tin nhắn đầu tiên, trong chat |
| Soul | Ô Instructions (tối đa 24 KB); lưu thành `SOUL.md` (nguồn: repo của sản phẩm, chưa kiểm chứng) | Không có ô riêng. Gửi làm tin nhắn đầu tiên và nhờ Bot ghi nhớ |
| Skill | Bot profile, **Skills**: dán `SKILL.md` hoặc nhập thư mục, rồi bật | Nhờ Bot lưu skill, hoặc **Teach a task**; bật theo từng Bot ở **Connect apps** > **Private skills**. Chưa có tài liệu về hỗ trợ `SKILL.md` (chưa kiểm chứng) |
| Bộ nhớ | Memory: `MEMORY.md` cùng các ghi chú theo chủ đề, sửa được | Nhắn "remember: ..." trong chat; không có màn hình bộ nhớ |
| Quyền truy cập (ứng dụng, công cụ) | Connected apps: mọi công cụ, danh sách cụ thể, hoặc không; máy chủ MCP | **Connect apps**; **Add a custom connector** |
| Bí mật | Tham chiếu Vault, thẻ thông tin xác thực | **Vault**, 1Password, thẻ bí mật an toàn |
| Quyền hạn | Mức truy cập, như **Ask for approval** hoặc Full access | **Settings > General > Bot**: **Auto Review**, **Custom Rules** (Allow automatically hoặc Ask first) |
| Lịch chạy | Lịch theo từng bot: một lần, theo khoảng, theo ngày trong tuần; thử rồi mới bật | Nhờ Bot trong chat; tab **Details** có Test và Pause |
| Mô hình | Engine và model theo từng bot, từng cuộc trò chuyện, từng lịch | Không có bộ chọn; tự động chọn |
| Nhóm và người điều phối | Department, Chief of Staff (**Also in charge of**), **Bots it may talk to** | Primary Bot, chat nhóm, Team Bot (gói Team hoặc Enterprise) |
| Chia sẻ | Nhập repo này qua **Teams → Import** (nhãn chưa kiểm chứng); gói phòng ban | Liên kết mẫu: **Share** > **Create a copy** > **Publish** |

## Thứ gì đi theo khi chia sẻ

| | Nhập vào OpenMausBot | Mẫu của Grok Bot |
|---|---|---|
| Soul hoặc chỉ dẫn | Có | Có |
| Skill | Có, chỉ văn bản `SKILL.md`, đang tắt | Có, trừ skill riêng tư |
| Lịch chạy | Có, đang tạm dừng | Có |
| Bộ nhớ | Không (khi nhập từ repo) | Tài liệu không thống nhất (chưa kiểm chứng) |
| Mô hình | Không | Không áp dụng |
| Bí mật và thông tin đăng nhập | Không | Không |
| Máy chủ MCP | Không | Không |
