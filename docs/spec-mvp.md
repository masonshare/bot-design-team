# Đặc tả MVP: Bot Design Team Community (v2)

Nguồn: báo cáo của Product Strategist, ngày 2026-11-18. Chưa thử trên app thật.

Nhãn:
- **[TL]** có trong tài liệu OpenMausBot (`team-sharing.md`, `presets.md`), chưa thử trên app thật.
- **[QĐ]** Hoàng Tổng đã chốt (Câu 1, 2, 3 đều chọn A).
- **[SL]** suy luận, cần kiểm chứng.

## 1. Người dùng

Người dùng OpenMausBot, kể cả người mới, muốn có sẵn đội bot mà không phải tự dựng từ đầu. Họ dùng miễn phí. [QĐ]

## 2. Cách cài (thứ tự bắt buộc)

1. Bấm **+** → **Import…**, dán link GitHub của `packs/starter/`. [TL] [QĐ]
2. Xem trước nội dung rồi bấm **Add**. [TL]
3. **Bật skill thủ công cho từng bot.** Sau khi nhập, skill ở trạng thái tắt. Chủ máy mở từng bot trong đội, vào mục **Skills** của bot đó và bật các skill của bot. Đối chiếu bảng "bot ↔ skill" trong hướng dẫn. [TL] [SL: tên mục và vị trí nút bật có thể khác, cần xác nhận trên app thật]
4. Gói có routine: routine vào ở trạng thái tạm dừng, bật lại có chủ đích. Starter hiện không có routine. [TL]
5. Gói có ứng dụng kết nối: nối lại bằng tài khoản của chính mình. Starter chưa có. [TL]

Yêu cầu với hướng dẫn cài (`guides/`, cả bản Anh và Việt):
- Bước 3 là một bước riêng, đánh số, không giấu trong chú thích.
- Kèm bảng "bot ↔ skill cần bật", và nói rõ nếu bỏ bước này thì bot vẫn xuất hiện nhưng chưa dùng được skill của mình. [SL]
- Nói rõ cái gì không đi theo khi nhập: bộ nhớ, chat, khóa API, mô hình. Người dùng tự chọn mô hình cho từng bot. [TL]

## 3. Gói Starter (`packs/starter/team.md`) [QĐ]

- 4 bot: Ginger Honey (Chief) + Dried Plum, Mango Spring Roll, Pink Pepper Coated Lotus Seeds.
- Skill ở `packs/starter/skills/<tên>/SKILL.md`: bot-design, prompt-design, skill-design (hiện nằm trong `skills/`).
- Việc cần làm: soạn Ginger Honey thành một bot trong `team.md` (hiện chỉ có trong tài liệu hướng dẫn), chuyển `team.md` hiện tại vào `packs/starter/`, thêm bảng "bot ↔ skill".
- Hiện trạng: `team.md` ở gốc repo đã đúng định dạng có danh sách `agents`; repo chưa có `packs/`.

## 4. Cách thêm use case

Mỗi use case là một gói `packs/<tên>/team.md` [QĐ], cài bằng cùng các bước ở mục 2, gồm cả bước bật skill. Hoặc nhờ đội Bot Design tạo bot theo công việc riêng. Mỗi gói cần: `team.md`, README ngắn (làm gì, cho ai), bảng "bot ↔ skill", và 3 phép thử riêng theo mẫu mục 5.

## 5. Tiêu chí nghiệm thu

OpenMausBot sạch (chưa có bot nào); Quality & Release chấm đạt/không đạt. Phần (a)-(c) [QĐ].

Làm đúng thứ tự mục 2, kể cả bước bật skill, rồi chạy:
- **(a)** Đủ 4 bot xuất hiện sau khi nhập.
- **(b)** Ginger Honey giao việc được cho Dried Plum và có kết quả trả về.
- **(c)** Đội tạo được một bot mẫu.
- **(d)** Sau bước bật skill, mỗi bot cho thấy skill của mình đã bật và dùng được: mở mục Skills của bot thấy trạng thái bật, kèm một yêu cầu ngắn mà bot trả lời đúng theo skill. Bot không có skill ghi "không áp dụng". [SL: cách thử cụ thể do Quality & Release thiết kế]
- **(e)** Tùy chọn: chạy (c) trước và sau bước bật skill để thấy khác biệt. [SL]

Đạt = cả (a)-(d) đạt, mỗi phép thử có bằng chứng (ảnh chụp hoặc nhật ký). Một phép thử không đạt thì Starter không đạt.

## 6. Giả định chưa kiểm chứng

Lead Engineer thử đầu tiên trên OpenMausBot sạch:
1. Link GitHub trỏ vào thư mục con `packs/starter/` có nhập được không. Nếu không, đổi cấu trúc (mỗi gói một repo hoặc một nhánh).
2. Nhập đội có tạo đủ 4 bot một lần không. `presets.md` cho thấy preset chỉ vào danh sách "Starting role", rồi phải bấm Create bot từng bot. Chưa rõ hai cơ chế có phải một.
3. Chief (Ginger Honey) có được gán đúng sau khi nhập không.
4. Skill có thật sự vào ở trạng thái tắt khi đội nhập từ link GitHub không. Nếu thực tế là bật, bước 3 trở thành bước kiểm tra và hướng dẫn phải sửa.
5. Giao diện bật skill: mục tên gì, bật theo bot hay theo thư viện chung. Cần ảnh chụp thật.

## 7. Việc để sau

- Grok Bot: chỉ làm sau khi OpenMausBot đạt nghiệm thu. [QĐ]
- Cộng đồng đóng góp: tạm thời chỉ chủ repo thêm gói; quy trình nhận gói ngoài (PR, người duyệt, tiêu chuẩn tối thiểu) làm sau.
- Danh sách use case ngoài Starter: chưa quyết định.

## 8. Rủi ro

Gói của người ngoài là chỉ dẫn cho bot, có thể chứa chỉ dẫn xấu, nên chưa nhận gói ngoài trước khi có quy trình duyệt. Bật skill là giao quyền cho bot, nên chủ máy nên đọc `SKILL.md` trước khi bật, nhất là với gói không phải của chủ repo. [SL]

---

## Phụ lục: đề xuất `GLOSSARY.md` (chưa tạo)

| Thuật ngữ | Nghĩa |
|---|---|
| Pack (gói) | Thư mục `packs/<tên>/` có `team.md`, nhập được vào OpenMausBot. |
| Starter | Gói đầu tiên: Ginger Honey + 3 bot Bot Design. |
| Use case | Bộ bot cho một công việc cụ thể, đóng thành một pack. |
| Chief | Bot điều phối, nhận việc và giao đúng bot (Ginger Honey). |
| Bot Design team | Đội 3 bot thiết kế bot, skill và prompt. |
| team.md | Tệp mô tả đội: bot, hướng dẫn, Chief. |
| Skill | Gói hướng dẫn (`SKILL.md`) để bot làm một việc theo chuẩn. |
| Bật skill thủ công | Bước chủ máy tự bật từng skill cho từng bot sau khi nhập, vì skill vào ở trạng thái tắt. |
| MVP | Phiên bản nhỏ nhất vẫn dùng được: Starter chạy trên OpenMausBot. |
| Nghiệm thu | Các phép thử (a)-(d) trên máy sạch, Quality & Release chấm. |
