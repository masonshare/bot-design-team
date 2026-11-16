# Hướng dẫn: dựng bot của bạn

Thư mục này giúp bạn biến ba bot trong repo thành bot chạy được, trên OpenMausBot hoặc Grok Bot. Bản tiếng Anh nằm ở `../en/`.

## Nên đọc hướng dẫn nào

| Bạn muốn... | Đọc |
|---|---|
| Thiết kế bot trước khi mở bất kỳ ứng dụng nào | [00-platform-neutral.md](00-platform-neutral.md) |
| Dựng 3 bot trong OpenMausBot, nhanh hoặc làm tay | [openmausbot.md](openmausbot.md) |
| Dựng một bot trong Grok Bot | [grok-bot.md](grok-bot.md) |
| Xem mỗi mục của bản thiết kế nằm ở đâu trong từng ứng dụng | [field-mapping.md](field-mapping.md) |

Thứ tự gợi ý: điền bản thiết kế chung trước, rồi làm theo hướng dẫn cho ứng dụng của bạn, cuối cùng đối chiếu bảng ánh xạ.

## Cài các skill

Ba skill (`prompt-design`, `skill-design`, `bot-design`) cài bằng công cụ dòng lệnh `skills`. Chạy trong terminal.

Cài cả ba skill vào dự án hiện tại:

```
npx skills add masonshare/bot-design-team
```

Chỉ cài một skill:

```
npx skills add masonshare/bot-design-team --skill prompt-design
```

Cài toàn cục, dùng cho mọi dự án trên máy, bằng cách thêm `-g`:

```
npx skills add masonshare/bot-design-team -g
npx skills add masonshare/bot-design-team --skill prompt-design -g
```

Mỗi skill chạy độc lập, nên bạn chỉ cần cài skill mình dùng.

Skill được cài cho tác nhân nào còn tùy các tác nhân (agent) mà lệnh tìm thấy trên máy bạn. Chạy `npx skills add --help` để xem tùy chọn. Các lệnh này dành cho tác nhân lập trình. Với OpenMausBot và Grok Bot, hãy theo đường dẫn trong hai hướng dẫn riêng bên dưới.

## Lưu ý an toàn

Không dán mật khẩu, khóa API hay token vào khung chat của bot, vào skill hoặc vào soul. Hãy dùng kho bí mật của ứng dụng: Vault ở cả OpenMausBot và Grok Bot.

## Về độ chính xác

Bước nào ghi "(chưa kiểm chứng)" là bước dựa trên tài liệu chưa được thử trên ứng dụng thật, hoặc các nguồn không khớp nhau. Hãy đối chiếu nhãn trên màn hình trước khi tin vào nó.
