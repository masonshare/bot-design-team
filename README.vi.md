# Bot Design Team

[English](README.md)

Ba bot AI và các Agent Skills để thiết kế prompt, skill và bot, chỉ dành cho [Orca](https://github.com/stablyai/orca).

Tóm tắt:

- Repo này chỉ nhắm tới Orca. Bot chạy trong Orca, trên máy và gói đăng ký của chính người dùng, chia sẻ bằng link chia sẻ bot của Orca.
- Tài liệu theo nền tảng cũ đã được gỡ khỏi nhánh chính; vẫn xem được ở tag git `v0-openmausbot`.
- Bốn bot (soul nằm trong [`bots/`](bots/)): Prompt Designer (thiết kế prompt), Skill Designer (thiết kế skill), Bot Architect (kiến trúc sư bot), Coordinator (người điều phối, Chief of Staff: nhận yêu cầu, hỏi người dùng trước mỗi lần giao việc, tổng hợp kết quả). Các skill nằm trong [`skills/design/`](skills/design/), phần lớn có bản tiếng Việt tại `references/vi.md`. Coordinator dùng hai skill `bot-roster` (chọn bot, giao việc, gộp kết quả) và `ai-engineering-playbook` (tư vấn AI engineering).
- Gói mẫu [`packs/ecommerce-cskh/`](packs/ecommerce-cskh/README.md) cho shop thương mại điện tử (Shopee, Zalo, hotline): bot biên tập (Editor bot) giúp chủ shop soạn kịch bản trả lời (luôn là `Nháp`, chỉ chủ shop duyệt), bot nhân viên (Staff bot) giúp nhân viên trả lời khách chỉ từ kịch bản `Đã duyệt`. Kho tri thức (kịch bản) lưu trong Google Sheet của chủ shop. Tài liệu từng skill: [`docs/skills/`](docs/skills/) (`bot-roster`, `ai-engineering-playbook`, `cskh-draft`, `cskh-lookup`, `cskh-no-script`).
- Cài skill: `npx skills add masonshare/bot-design-team`.
- Repo công khai: quy tắc cứng: không bao giờ đưa dữ liệu thật của công ty, khách hàng hay nhân viên vào đây, chỉ dùng ví dụ giả (các file mẫu của gói đều ghi FAKE).

Giấy phép MIT: xem [LICENSE](LICENSE). Ghi công: [CREDITS.md](CREDITS.md).
