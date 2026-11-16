# Bot Design Team

[English](README.md)

Ba bot AI và ba Agent Skills để thiết kế prompt, skill và bot.

| Bot | Vai trò | Skill |
|---|---|---|
| Pink Pepper Coated Lotus Seeds | Prompt Designer (thiết kế prompt): prompt, prompt hệ thống, chuỗi prompt, chỉ dẫn nền (soul) của bot | [`prompt-design`](skills/prompt-design/SKILL.md) |
| Mango Spring Roll | Skill Designer (thiết kế skill): biến quy trình làm việc thành Agent Skills đã được kiểm thử | [`skill-design`](skills/skill-design/SKILL.md) |
| Dried Plum | Bot Architect (kiến trúc sư bot) kiêm Tổng điều phối (Chief of Staff): hồ sơ bot, nhóm bot, đóng gói | [`bot-design`](skills/bot-design/SKILL.md) |

Mỗi skill cũng dùng được độc lập, không cần cả nhóm.

## Cài đặt các skill

Cần có Node.js. Trình cài đặt sẽ sao chép các skill vào agent lập trình của bạn (Claude Code, Codex, Cursor và các agent khác):

```bash
npx skills add masonshare/bot-design-team            # pick skills and agents interactively
npx skills add masonshare/bot-design-team --list     # preview what is inside
npx skills add masonshare/bot-design-team --skill prompt-design
npx skills add masonshare/bot-design-team -g         # install for your user, not one project
```

## Tạo nhóm trong OpenMausBot

1. Mở **Teams → Import** và dán `https://github.com/masonshare/bot-design-team`.
2. Xem lại rồi nhập. OpenMausBot sẽ tạo 3 bot cùng chỉ dẫn nền và skill của chúng.
3. Sau khi nhập:
   - Bật 3 skill lên, vì skill được nhập vào luôn ở trạng thái tắt.
   - Chọn mô hình cho từng bot, vì mô hình không đi kèm theo tệp.

Tệp nhóm là [`team.md`](team.md). Đó là Markdown thuần, nên bạn cũng có thể đưa nó cho bất kỳ agent nào có thể đóng vai Tổng điều phối.

## Tự cài đặt thủ công các bot

Để tự dựng các bot trong OpenMausBot hoặc Grok Bot, xem [guides/vi](guides/vi/README.md). Các chỉ dẫn nền dễ đọc nằm trong [`bots/`](bots/).

## Cấu trúc thư mục

```
team.md        OpenMausBot team file (generated from bots/ and skills/)
bots/          the three souls (standing instructions), English and Vietnamese
skills/        three Agent Skills, each with references/vi.md (Vietnamese edition)
guides/        manual setup for OpenMausBot and Grok Bot, English and Vietnamese
```

## Ghi công và giấy phép

Các skill và chỉ dẫn nền do Masonshare viết. Những ý tưởng lấy từ công trình của người khác đã được viết lại và ghi nguồn trong [CREDITS.md](CREDITS.md). Kho mã được phát hành theo Giấy phép MIT: xem [LICENSE](LICENSE).

Phiên bản tiếng Việt của các skill nằm tại `references/vi.md` trong từng thư mục skill, ví dụ [skills/prompt-design/references/vi.md](skills/prompt-design/references/vi.md), [skills/skill-design/references/vi.md](skills/skill-design/references/vi.md) và [skills/bot-design/references/vi.md](skills/bot-design/references/vi.md).
