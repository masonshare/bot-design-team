# Thiết kế bot (bản tiếng Việt của skill bot-design)

Biến một ý tưởng bot thành hồ sơ mà người dùng có thể dựng và tin tưởng được, rồi chấm điểm trước khi giao. Không phụ thuộc nền tảng; đóng gói cho OpenMausBot nằm ở bước 8.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt.

Vòng làm việc (work loop): làm rõ, nghiên cứu, lập kế hoạch, dựng, kiểm tra. Bước 1-2 làm rõ, 3-4 lập kế hoạch, 5-6 dựng, 7 kiểm tra, 8 đóng gói. Dừng ở một cổng duyệt (gate), tức là người dùng đồng ý rồi mới đi tiếp, trước mọi việc khó hoàn tác: đăng bài, gửi, xóa, chi tiền, cài đặt, cấp quyền ghi cho bot, bật lịch chạy.

## Mẫu bàn giao (handoff)

Các bot chuyển việc cho nhau, và cho bạn, bằng một tin nhắn có đúng 5 mục theo thứ tự:

1. Mục tiêu (Goal): một câu.
2. Đầu vào (Inputs): thứ đính kèm hoặc liên kết.
3. Sản phẩm (Deliverable): bot này đã làm ra gì (tên tệp hoặc nội dung ngay trong tin).
4. Xong khi (Done when): tiêu chí nghiệm thu kiểm tra được.
5. Việc còn mở (Open items): câu hỏi, rủi ro, phần chưa làm.

Đầu vào của bạn có thể là bàn giao từ bot viết prompt (soul hoặc prompt kèm ca thử) và bot thiết kế skill (thư mục skill kèm ca thử kích hoạt). Bàn giao của bạn gồm hồ sơ, kết quả chấm điểm và gói đóng gói.

## Các bước

### 1. Phỏng vấn (một lượt)

Hỏi tất cả trong một tin, mỗi câu kèm gợi ý mặc định để người dùng trả lời nhanh:

- Công việc: bot làm gì, kèm 3 ví dụ thật, và việc bot không được làm.
- Người dùng: ai nói chuyện với bot, mức am hiểu, ngôn ngữ.
- Đầu vào: dữ liệu, ứng dụng, tệp, tài khoản đang có.
- Đầu ra: định dạng, nơi nhận, ai duyệt.
- Tần suất: theo yêu cầu, theo lịch hay theo sự kiện.
- Rủi ro: làm sai thì thiệt hại gì (tiền, uy tín, dữ liệu).
- Ngân sách: chi phí mô hình chấp nhận được, thời gian dựng, ai bảo trì.
- Nền tảng: OpenMausBot, Grok Bot hay nền tảng khác.

Xong khi: mỗi mục đều có câu trả lời hoặc một giả định đã thống nhất, ghi trong brief.

### 2. Nên làm hay không (go/no-go)

Chọn công cụ nhẹ nhất đủ làm việc:

| Tình huống | Dùng |
|---|---|
| Làm một lần hoặc hiếm, không cần nhớ hay công cụ | Một prompt |
| Quy trình lặp lại mà người dùng đã tự chạy được trong chat | Một skill |
| Các bước cố định, đầu vào cố định, không cần phán đoán | Tự động hóa thường (cron, n8n, Make) |
| Việc lặp lại có phán đoán, cần nhớ ngữ cảnh, có công cụ hoặc lịch | Một bot |
| Mỗi bước đều cần người phán đoán, hoặc hậu quả không hoàn tác được | Không làm bot; đưa checklist |

Bắt đầu từ việc nhàm chán nhất mà người dùng biết rõ từng bước. Nêu kết luận và lý do trong hai câu.

Xong khi: người dùng đã thấy kết luận. Nếu kết luận không phải "bot", dừng và giao phương án nhẹ hơn.

### 3. Định hình: một bot hay một đội

Mặc định là 1 bot làm 1 việc. Chỉ tách thành đội khi công việc có các chuyên môn khác nhau làm một ngữ cảnh quá tải, và mỗi chuyên viên đã tự chạy tốt một mình.

Một đội gồm 1 điều phối (coordinator) cộng 2-3 chuyên viên. Điều phối nhận yêu cầu, giao đúng chuyên viên, gộp kết quả thành một câu trả lời, và báo tiến độ thật. Điều phối không làm việc chuyên môn và không giữ công cụ chuyên môn. Mọi tin nhắn giữa các bot dùng mẫu bàn giao ở trên. Chuyên viên báo ở ba thời điểm: bắt đầu, xong, bị kẹt.

Mô tả hành vi mỗi bot bằng bảy câu trả lời: điều kiện kích hoạt, đầu vào, các bước, đầu ra, điểm người duyệt, tiêu chí thành công, quy tắc dừng và hỏi (các ngoại lệ mà bot phải dừng lại hỏi thay vì đoán).

Xong khi: người dùng đã duyệt hình dạng đội (gate) và mỗi bot có mô tả một dòng cùng bảy câu trả lời.

### 4. Điền hồ sơ bot

Dùng 13 mục làm gợi ý, không phải cổng bắt buộc: tổng quan (overview), danh tính (identity), soul, skills, trí nhớ (memory), thư viện (library), routines, kết nối (access), mô hình (model), quyền hạn (permissions), giọng nói và thông báo (voice/alerts), lịch sử (history), chi phí (usage). Chỉ điền mục bot này cần. Mục nào không cần thì ghi `không cần` kèm lý do một dòng. Mẫu điền sẵn có gợi ý nên điền gì, tránh gì, ví dụ: `profile-template.md`.

Xếp nội dung theo tần suất cần đến:
- Soul: thứ đúng ở mọi lần chạy, ngắn.
- Skills: quy trình chỉ chạy khi liên quan.
- Library: tài liệu dài, chia theo chủ đề, có ngày.
- Memory: sự thật ổn định về người dùng, mỗi việc một dòng.

Tóm lược từng mục:

| Mục | Điền | Tránh |
|---|---|---|
| Overview | Một câu: giúp [ai] làm [việc] để đạt [kết quả]; 3-5 việc trong phạm vi; 2-3 việc ngoài phạm vi; một chỉ số thành công | "Trợ lý đa năng" |
| Identity | Tên ngắn gợi việc; chức danh; mô tả 1-2 dòng nói làm gì và khi nào dùng; ngôn ngữ và cách xưng hô | Tên chung hoặc trùng |
| Skills | 3-7 skill, mỗi skill có mô tả kích hoạt, các bước đánh số, bước kiểm tra, mẫu đầu ra | Một skill khổng lồ; việc máy làm được lại bắt mô hình làm |
| Memory | Sở thích ổn định, quyết định đã chốt kèm lý do, chỗ người dùng đã sửa, thuật ngữ | Thứ hết hạn trong một tuần, bí mật, văn bản dài (để trong Library) |
| Library | Tệp nhỏ theo chủ đề, ngày cập nhật, người chịu trách nhiệm | Một tệp 50 trang; bản cũ lẫn bản mới |
| Routines | Việc lặp lại có đầu ra dự đoán được; hướng dẫn chạy được không cần ngữ cảnh chat; ưu tiên sự kiện hơn quét dày; chỉ ghi nháp | Lịch vài phút một lần không cần thiết; routine hành động không hoàn tác |
| Access | Chỉ những ứng dụng bot thật sự dùng; đọc trước ghi sau; được gọi bot nào, ai được gọi nó | Kết nối tất cả cho tiện |
| Model | Mô hình nhỏ nhất vẫn qua các ca thử; rẻ hơn cho routine chạy nhiều | Dùng mô hình mạnh nhất cho mọi việc |
| Voice/alerts | Chỉ báo khi cần hành động: duyệt, lỗi, deadline; tin ngắn nói việc gì, cần làm gì, ở đâu; giờ yên lặng | Báo từng bước |
| History | Một thread một việc; thread nặng thì mở thread mới kèm bàn giao | Một thread dài vô tận |
| Usage | Theo dõi token hoặc chi phí mỗi việc hằng tuần; có hạn mức và cảnh báo | Không đo gì |

Xong khi: mỗi mục đều được điền hoặc ghi `không cần` kèm lý do, và không mục nào chứa bí mật.

### 5. Quyền hạn

Áp dụng quyền tối thiểu (least privilege). Đọc và tìm kiếm thì cho thoải mái, bản nháp và ghi trong thư mục làm việc thì cho trong phạm vi, còn mọi hành động ra ngoài hoặc không hoàn tác thì đặt cổng duyệt phía trước.

| Mức rủi ro | Ví dụ | Kiểm soát |
|---|---|---|
| Thấp | Đọc, tìm, tóm tắt | Tự chạy, có ghi nhật ký |
| Vừa | Bản nháp, tệp trong thư mục làm việc | Duyệt trước khi ra ngoài |
| Cao | Đăng nhập, thanh toán, thay đổi hàng loạt | Cổng duyệt mỗi lần; người dùng tự nhập mật khẩu, mã xác thực, CAPTCHA |
| Tới hạn | Xóa dữ liệu, ký, đổi chính sách | Không tự động hóa |

- Đọc trước ghi sau: mọi kết nối bắt đầu ở chế độ chỉ đọc; thêm quyền ghi theo từng công cụ khi một ca thử cần.
- Đặt cổng trước khi gửi, đăng, xóa, chi tiền, cài đặt, commit hoặc push mã, bật lịch chạy.
- Hạn mức tiền nằm trong cài đặt của nền tảng, không viết trong prompt.
- Thông tin xác thực chỉ đặt trong kho bí mật (secret store) hoặc kho kết nối của nền tảng. Không để bí mật, URL webhook hay ghi chú đăng nhập trong prompt, skill, memory, chat hay tệp. Nhờ người dùng nhập qua kho bí mật.
- Nhiều tài khoản có nhãn rõ cho một ứng dụng thì tốt hơn nhân đôi bot.

Xong khi: bảng quyền cho thấy thiệt hại tối đa nếu bot làm sai, và mọi hành động không hoàn tác đều có cổng.

### 6. Viết soul và quy trình

Giao việc viết prompt cho skill `prompt-design` khi có, kèm brief (mục tiêu, đối tượng, đầu vào, ràng buộc, định nghĩa xong) và nhận lại soul cùng ca thử. Giao quy trình cho skill `skill-design` theo cách tương tự. Khi thiếu hai skill đó, tự viết:

Soul, 150-400 từ, theo thứ tự: vai trò 1-2 câu; người dùng và mức am hiểu; giọng văn; nguyên tắc làm việc kèm lý do; ranh giới cứng (hỏi trước khi gửi, xóa, chi tiền, commit); báo cáo trung thực (đã làm gì, chưa làm gì, lỗi gì, không báo xong khi chưa kiểm); khi bí thì nói rõ và nêu cách lấy dữ liệu. Ưu tiên lý do hơn cấm đoán viết hoa. Quy trình dài đưa sang skill, không để trong soul. Không để thông tin dễ lỗi thời.

Skill (phương án tự viết): một thư mục có `SKILL.md` gồm `name`, `description` một dòng nói làm gì và khi nào kích hoạt, các bước đánh số mỗi bước kết thúc bằng tiêu chí kiểm tra được, và mẫu đầu ra.

Xong khi: soul qua được 5 câu hỏi khác nhau với giọng và ranh giới nhất quán.

### 7. Chấm điểm và thử

Chạy 5-10 ca thử và ghi kết quả: 3 bình thường, 2 mơ hồ, 2 ngoài phạm vi, 2 đòi hành động rủi ro. Chạy mốc so sánh (baseline) trước, tức chat thường không có hồ sơ mới, rồi chạy lại (retest) với hồ sơ mới và so sánh. Sửa lỗi rồi chạy lại.

Sau đó chấm bằng bảng điểm (scorecard). Mỗi mục 0 hoặc 1, chỉ tính các mục áp dụng; mục tiêu từ 80% trở lên.

- [ ] Overview: mục tiêu một câu, trong và ngoài phạm vi
- [ ] Identity: tên và mô tả nói rõ làm gì, khi nào dùng
- [ ] Soul: dưới 400 từ, có giọng, ranh giới, báo cáo trung thực, cách xử lý khi bí
- [ ] Skills: 3-7 skill, mô tả kích hoạt đúng, mỗi skill có bước kiểm tra và mẫu đầu ra
- [ ] Memory: chỉ sự thật ổn định, không bí mật, không dữ liệu hết hạn
- [ ] Library: tệp nhỏ có ngày, không trùng lặp
- [ ] Routines: tự chạy được, ưu tiên sự kiện, chỉ ghi nháp
- [ ] Access: chỉ kết nối thật sự dùng, đọc trước ghi sau
- [ ] Model: nhỏ nhất vẫn qua các ca thử
- [ ] Permissions: mọi hành động không hoàn tác đều có cổng
- [ ] Voice/alerts: chỉ báo khi cần hành động
- [ ] History: một thread một việc, có mẫu bàn giao
- [ ] Usage: có thước đo chi phí và hạn mức
- [ ] Đã chạy ca thử và ghi kết quả (luôn áp dụng)

`scripts/score_bot.py profile.md` chấm hồ sơ viết theo 13 tiêu đề (đi kèm trong thư mục skill; script chỉ là tùy chọn, checklist trên là đủ). Nó đánh dấu từng mục là filled, empty hoặc `not needed` rồi tính điểm trên các mục áp dụng.

Xong khi: điểm đạt ít nhất 80% các mục áp dụng, hoặc mỗi chỗ thiếu được ghi ở Việc còn mở kèm cách sửa.

### 8. Đóng gói và triển khai

Chọn theo nền tảng:

- OpenMausBot: viết tệp đội `team.md` (BotMRR Markdown v1) để người dùng nhập qua Teams, Import bằng cách dán liên kết repo công khai. Phần cốt lõi ở dưới; hướng dẫn đầy đủ là `team-file.md`.
- Nền tảng khác, hoặc chỉ một bot: viết các bước cài đặt thủ công, mỗi bot một danh sách đánh số: tạo bot, dán danh tính và soul, thêm skill, kết nối ứng dụng ở chế độ chỉ đọc, chọn mô hình, đặt quyền, thêm tệp thư viện, tạo routine ở trạng thái tạm dừng.

Triển khai theo thứ tự này, có cổng giữa các giai đoạn:
1. Một bot, chạy tốt một mình trên các ca thử.
2. Routine, bắt đầu ở trạng thái tạm dừng; chạy tay hai lần rồi mới bật.
3. Đội, làm cuối; chỉ thêm bot vào nhóm khi nó đã chạy tốt một mình.

Rà lại sau 1-2 tuần bằng usage và history; soul nào phình ra thì cắt, đưa quy trình sang skill.

Xong khi: người dùng có gói hoặc các bước cài đặt, thứ tự triển khai, và bản tóm tắt 10 dòng: bot làm gì, không làm gì, quyền gì, tốn khoảng bao nhiêu.

## Cốt lõi về tệp đội OpenMausBot

- Thư mục gốc repo có `team.md` (hoặc `botmrr.md`) trên nhánh main hoặc master; repo công khai.
- Các khóa frontmatter YAML: `botmrr: 1`, `id`, `release`, `name`, `tagline`, `summary`, `category`, `author` {name, url}, `license`, `tags`, `outcomes`, `setupMinutes`, `requirements` {apps, capabilities}, `agents` (mỗi bot: key, name, title, description, soul, appearance {color, mascotExpression}, skills), `chiefOfStaff`, `rooms`, `routines` (mỗi routine có `enabledAfterInstall: false`), `playbooks`, `skills` {version: 1, entries (mỗi mục: name, description, license, instructions)}.
- `instructions` chứa toàn văn SKILL.md và bắt đầu bằng `---`; name, description, license phải khớp chính xác với frontmatter của SKILL.md.
- Bảy tiêu đề thân bài bắt buộc: Activation, Mission, Outcomes, Connections, Team, Chief of Staff, Completion rule.
- Màu: green, blue, red, orange, purple, cyan, pink, yellow, teal, coral, silver, chrome.
- Giới hạn: soul tối đa 24000 byte, description tối đa 4000 ký tự, tối đa 20 skill mỗi gói v1.

## Lưu ý về nền tảng

Khi nhập (import), nền tảng mang theo soul, nội dung skill, phòng (rooms), Chief of Staff và routine ở trạng thái tạm dừng. Nó không mang theo mô hình, thông tin xác thực, kết nối, trí nhớ, cũng như `references/` và `scripts/` của skill (chỉ văn bản `SKILL.md` đi theo). Skill nhập vào ở trạng thái tắt. Sau khi nhập: chọn mô hình cho từng bot, bật skill, tự kết nối ứng dụng, bật routine bằng tay. Vì vậy mỗi skill phải tự đủ trong `SKILL.md`.

## Bộ khung theo thể loại bot

Chọn hàng gần nhất làm điểm xuất phát rồi chỉnh.

| Thể loại | Soul nhấn mạnh | Skills điển hình | Library | Quyền | Model |
|---|---|---|---|---|---|
| Vận hành sàn thương mại | Chính xác số liệu, không bịa giá | Viết listing, phân tích đơn, soạn phản hồi khách | Bảng giá, chính sách sàn, brand | Đọc và nháp; không tự đổi giá | Tầm trung |
| Nội dung và prompt ảnh | Giọng thương hiệu; chờ duyệt hướng trước khi viết cả bộ | Brief, ý tưởng, prompt, lưu .md theo cấu trúc dự án | Brand, ví dụ prompt tốt | Ghi thư mục dự án; hỏi trước khi tốn credit | Mạnh cho ý tưởng, rẻ cho biến thể |
| Lập trình | Phạm vi nhỏ; hỏi trước khi thêm dependency; không commit hay push khi chưa bảo | Spec, issue, PR, review, handoff | Quy ước repo | Đọc và ghi repo; git cần duyệt | Mạnh |
| Nghiên cứu và phân tích | Nêu nguồn và ngày; phân biệt sự thật với suy đoán | Tra cứu, so sánh, báo cáo | Nguồn tin cậy | Chỉ đọc | Tầm trung hoặc mạnh |
| Thư ký, lịch, email | Ngắn, chỉ nêu việc cần xử lý | Lọc mail quan trọng, chuẩn bị họp, soạn nháp | Danh bạ, quy tắc ưu tiên | Đọc và nháp; không tự gửi | Nhỏ hoặc tầm trung |
| Điều phối (Chief) | Giao đúng bot, gộp một câu trả lời, nói thật tiến độ | Phân việc, rà lỗi, báo tổng | Danh sách bot và vai trò | Quản lý bot, không vượt quyền | Mạnh |
| Dữ liệu và báo cáo | Kiểm tra số trước khi kết luận | Làm sạch, SQL, biểu đồ | Từ điển dữ liệu | Đọc dữ liệu, xuất tệp | Tầm trung |

## Tệp tham chiếu

- `profile-template.md`: đọc khi điền hồ sơ ở bước 4; có 13 mục kèm gợi ý điền, tránh, ví dụ.
- `team-file.md`: đọc khi đóng gói cho OpenMausBot ở bước 8; đủ frontmatter, thân bài, giới hạn và ví dụ.
- `sample-profile.md`: đọc để xem một hồ sơ nhỏ đã chấm; là đầu vào của `scripts/score_bot.py`.

## Nguồn

- Masonshare, bộ 13 tiêu chí hồ sơ bot, bộ khung theo thể loại và bảng điểm (nguyên bản).
- Tài liệu OpenMausBot, https://docs.openmausbot.com/docs/features/skills và https://docs.openmausbot.com/docs/features/chat-and-teams.
- Tài liệu trong repo OpenMausBot (team-sharing, presets), https://github.com/milind-soni/OpenMausBot.
- openmausbot-teams, FORMAT.md, https://github.com/milind-soni/openmausbot-teams (BotMRR Markdown v1).
- Đặc tả Agent Skills, https://agentskills.io/specification.
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
