# Routine healthcheck (optional template)

Optional. Use it only when a bot owns routines that run unattended and the user wants a periodic audit. It is not part of the starter pack and no bot needs it by default. Idea adapted from Lauren Tan's dr-eggbot-v2 page (healthcheck routines); see Sources in `SKILL.md`.

## What it does

Once a week it reads the bot's automation list and the recent run results, and proposes changes. It never applies them.

## Setup rules

- Create it **paused**. Run it by hand twice, read both results, then enable it.
- Read-only: it may read automations, run history and usage. It may not edit, pause, delete or create anything.
- **Silent when there is no proposal.** No "all fine" message. A message appears only when there is something to decide.
- One short message per run: what it found, why it matters, the proposed change, where to approve.
- Schedule: weekly, in the user's time zone, outside quiet hours. Do not poll more often.

## Routine instructions (paste as the routine text)

```
Read the list of automations for this bot and their last 4 runs.
For each automation, check:
1. Did it run on schedule, and did the runs produce a useful result?
2. Is it enabled but never producing anything, or failing repeatedly?
3. Does its schedule fire more often than its output needs?
4. Does it duplicate another automation?
If every check passes, end the run and send nothing.
Otherwise send ONE message: the automation name, what you found, the change you
propose (pause, slow down, merge, fix the instructions), and ask me to approve.
Do not change anything yourself.
```

## Done when

- The routine exists and is paused, with the text above.
- Two manual runs were read: one with nothing to report (no message) and one with a real finding (one short message).
- The user decided whether to enable it.

---

# Routine kiểm tra sức khỏe (mẫu tùy chọn)

Tùy chọn. Chỉ dùng khi bot có routine chạy không người trông và người dùng muốn kiểm tra định kỳ. Không nằm trong gói starter và không bot nào cần nó mặc định. Ý tưởng lấy từ trang dr-eggbot-v2 của Lauren Tan (routine kiểm tra sức khỏe); xem mục Nguồn trong `references/vi.md`.

## Nó làm gì

Mỗi tuần một lần, nó đọc danh sách tự động hóa của bot và kết quả các lần chạy gần đây, rồi đề xuất thay đổi. Nó không bao giờ tự áp dụng.

## Quy tắc cài đặt

- Tạo ở trạng thái **tạm dừng**. Chạy tay hai lần, đọc cả hai kết quả, rồi mới bật.
- Chỉ đọc: được đọc tự động hóa, lịch sử chạy và mức dùng. Không được sửa, tạm dừng, xóa hay tạo gì.
- **Im lặng khi không có đề xuất.** Không gửi tin "mọi thứ ổn". Chỉ có tin khi có điều cần quyết định.
- Mỗi lần chạy một tin ngắn: thấy gì, vì sao đáng quan tâm, đề xuất đổi gì, duyệt ở đâu.
- Lịch: mỗi tuần, theo múi giờ người dùng, ngoài giờ yên lặng. Không quét dày hơn.

## Nội dung routine (dán làm văn bản routine)

```
Đọc danh sách tự động hóa của bot này và 4 lần chạy gần nhất của từng cái.
Với mỗi tự động hóa, kiểm tra:
1. Có chạy đúng lịch và cho kết quả hữu ích không?
2. Có đang bật nhưng không tạo ra gì, hoặc lỗi liên tục không?
3. Lịch có dày hơn mức đầu ra cần không?
4. Có trùng với tự động hóa khác không?
Nếu mọi mục đều đạt, kết thúc và không gửi gì.
Nếu không, gửi MỘT tin: tên tự động hóa, điều đã thấy, thay đổi đề xuất
(tạm dừng, giãn lịch, gộp, sửa hướng dẫn), và nhờ tôi duyệt.
Không tự thay đổi gì.
```

## Xong khi

- Routine đã tạo và đang tạm dừng, với nội dung trên.
- Đã đọc hai lần chạy tay: một lần không có gì để báo (không tin nào) và một lần có phát hiện thật (một tin ngắn).
- Người dùng đã quyết định có bật hay không.
