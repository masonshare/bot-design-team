# Thiết kế bot (bản tiếng Việt của skill bot-design)

Biến một ý tưởng bot thành một bot mà người dùng có thể dựng và tin tưởng được. Skill này là cửa vào: giữ các quy tắc chung và chuyển từng giai đoạn cho skill phụ trách.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Vòng làm việc (work loop): làm rõ, nghiên cứu, lập kế hoạch, dựng, kiểm tra. Dừng ở một cổng duyệt (gate), tức là người dùng đồng ý rồi mới đi tiếp, trước mọi việc khó hoàn tác: đăng bài, gửi, xóa, chi tiền, cài đặt, cấp quyền ghi cho bot, bật lịch chạy.

## Các giai đoạn

| # | Giai đoạn | Skill | Kết quả |
|---|---|---|---|
| 1 | Phỏng vấn và nên làm hay không (go/no-go) | bot-interview | Bản brief và kết luận: prompt, skill, tự động hóa, bot, hoặc không làm bot |
| 2 | Định hình (shape) | bot-shape | Một bot, hoặc một điều phối cộng 2-3 chuyên viên; mô tả hành vi mỗi bot |
| 3 | Hồ sơ (profile) | bot-profile | Hồ sơ 13 mục, cùng brief cho soul và skill |
| 4 | Routine | bot-routine | Đặc tả năm phần cho mỗi lần chạy không người trông (chỉ khi bot tự chạy) |
| 5 | Quyền hạn (access) | bot-access | Quyền, kết nối và cách giữ bí mật theo nguyên tắc quyền tối thiểu |
| 6 | Chấm điểm và thử | bot-score | Bảng điểm, ca thử, bằng chứng cho từng kết luận |
| 7 | Đóng gói | bot-package | Các bước cài đặt thủ công hoặc link chia sẻ Orca, thứ tự triển khai, bản tóm tắt |

Chạy từng giai đoạn một, theo thứ tự, bắt đầu từ giai đoạn đầu tiên mà người dùng chưa duyệt kết quả. Chuyển kết quả sang giai đoạn sau bằng mẫu bàn giao ở dưới. Bỏ giai đoạn 4 khi bot không có lần chạy không người trông. Nếu người dùng nêu đúng một giai đoạn ("chấm điểm hồ sơ này") thì chỉ chạy skill của giai đoạn đó.

## Khi skill của một giai đoạn chưa được cài

Tự chạy giai đoạn đó theo bản tóm tắt dưới đây, rồi nói với người dùng skill nào sẽ làm sâu hơn.

1. Phỏng vấn: hỏi tất cả trong một tin, mỗi câu kèm mặc định: công việc kèm 3 ví dụ thật, anti-job (2-4 dòng về điều bot tuyệt đối không làm), người dùng, đầu vào, đầu ra, tần suất, rủi ro, ngân sách, nền tảng. Rồi chọn công cụ nhẹ nhất: một prompt (làm một lần), một skill (quy trình lặp lại mà người dùng tự chạy trong chat), tự động hóa thường (các bước cố định, không cần phán đoán), một bot (việc lặp lại có phán đoán, trí nhớ, công cụ hoặc lịch), hoặc không làm bot và đưa checklist (cần phán đoán nặng hoặc hậu quả không hoàn tác). Nêu kết luận và lý do trong hai câu.
2. Định hình: mặc định 1 bot làm 1 việc. Một đội gồm 1 điều phối cộng 2-3 chuyên viên, chỉ khi các chuyên môn khác nhau làm một ngữ cảnh quá tải và mỗi chuyên viên đã tự chạy tốt một mình. Điều phối giao việc, gộp kết quả và báo tiến độ; không giữ công cụ chuyên môn. Viết một dòng công việc cho mỗi bot. Cổng: người dùng duyệt hình dạng đội.
3. Hồ sơ: điền 13 mục bot cần (overview, identity, soul, skills, memory, library, routines, access, model, permissions, voice/alerts, history, usage), mục nào không cần thì ghi `không cần` kèm lý do. Giữ soul ngắn (150-400 từ), quy trình để trong skill.
4. Routine: mỗi routine có chủ sở hữu (một người có tên), kích hoạt, hành động được phép, đường leo thang và điều kiện dừng; bắt đầu ở trạng thái tạm dừng.
5. Quyền: quyền tối thiểu. Đọc trước ghi sau. Cổng trước mọi hành động gửi, đăng, xóa, chi tiền, cài đặt, commit hoặc push. Thông tin xác thực chỉ nằm trong kho bí mật của nền tảng.
6. Chấm điểm: báo riêng bốn trạng thái (đã thiết kế, đã áp dụng, đã đọc lại, đã kiểm thử hành vi), mỗi kết luận kèm bằng chứng; chạy 5-10 ca thử, baseline trước rồi retest; chấm 14 mục trong bảng kiểm, mỗi mục 0 hoặc 1 (13 mục hồ sơ và mục kiểm thử luôn áp dụng), chỉ tính mục áp dụng; mục tiêu 80%.
7. Đóng gói: viết các bước thủ công có đánh số cho Orca, hoặc chia sẻ bot bằng link chia sẻ của Orca; nhớ rằng chỉ văn bản SKILL.md của mỗi skill có thể đi theo. Triển khai một bot trước, routine tạm dừng, đội làm cuối.

## Quy tắc chung

- Bot hiện hữu: kiểm kê chỉ dẫn, skill, quyền, kết nối và tự động hóa trước khi đổi vai trò. Lời đồng đội báo không thay thế việc tự đọc lại; thứ chưa đọc được thì ghi `chưa xác minh`.
- Thông tin xác thực, token và URL webhook không bao giờ nằm trong prompt, skill, memory, chat hay tệp. Nhờ người dùng nhập qua kho bí mật hoặc kho kết nối của nền tảng.
- Một bot có thể có bao nhiêu skill tùy vai trò cần, mỗi skill một quy trình; số lượng không phải dấu hiệu cảnh báo, mô tả chồng chéo mới là.
- Khi đã có bot thiết kế prompt hoặc thiết kế skill, giao việc viết soul và skill cho họ kèm brief; không làm lại ở đây.

## Mẫu bàn giao (handoff)

Các bot chuyển việc cho nhau, và cho bạn, bằng một tin nhắn có đúng 5 mục theo thứ tự:

1. Mục tiêu (Goal): một câu.
2. Đầu vào (Inputs): thứ đính kèm hoặc liên kết.
3. Sản phẩm (Deliverable): bot này đã làm ra gì (tên tệp hoặc nội dung ngay trong tin).
4. Xong khi (Done when): tiêu chí nghiệm thu kiểm tra được.
5. Việc còn mở (Open items): câu hỏi, rủi ro, phần chưa làm.

Đầu vào của bạn có thể là bàn giao từ bot viết prompt (soul hoặc prompt kèm ca thử) và bot thiết kế skill (thư mục skill kèm ca thử kích hoạt). Bàn giao của bạn gồm hồ sơ, kết quả chấm điểm và gói đóng gói.

## Nguồn

- Masonshare, bộ 13 tiêu chí hồ sơ bot và bảng điểm (nguyên bản).
- Đặc tả Agent Skills, https://agentskills.io/specification.
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
