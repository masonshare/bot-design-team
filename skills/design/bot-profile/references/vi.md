# Hồ sơ bot (bản tiếng Việt của skill bot-profile)

Điền hồ sơ để một người có thể dựng một bot từ đó. Giai đoạn 3 của quy trình thiết kế bot.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì đầu ra là tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Cổng duyệt (gate): cấp quyền ghi, cài đặt hay bật bất cứ thứ gì đều chờ người dùng đồng ý. Viết hồ sơ không làm việc nào trong số đó.

## Các bước

### 1. Lấy hình dạng và chọn khung

Lấy công việc một dòng và mô tả bảy câu của một bot từ bot-shape (hoặc từ bản brief phỏng vấn). Chọn khung xuất phát gần nhất rồi chỉnh: vận hành sàn thương mại, nội dung và prompt ảnh, lập trình, nghiên cứu và phân tích, thư ký và email, điều phối, dữ liệu và báo cáo. Bảng khung nằm ở `starter-frames.md` (tiếng Anh); thiếu tệp đó thì xuất phát từ chính công việc của bot.

Xong khi: công việc, anti-job và khung gần nhất đã ghi ở đầu hồ sơ.

### 2. Điền 13 mục

13 mục là gợi ý, không phải cổng bắt buộc: tổng quan (overview), danh tính (identity), soul, skills, trí nhớ (memory), thư viện (library), routines, kết nối (access), mô hình (model), quyền hạn (permissions), giọng nói và thông báo (voice/alerts), lịch sử (history), chi phí (usage). Chỉ điền mục bot này cần; mục nào không cần thì ghi `không cần` kèm lý do một dòng. Mẫu điền sẵn có gợi ý: `profile-template.md`.

Xếp nội dung theo tần suất cần đến: soul = đúng ở mọi lần chạy, ngắn; skills = quy trình chỉ chạy khi liên quan; library = tài liệu dài và sổ cái (ledger), chia theo chủ đề, có ngày; memory = sự thật ổn định về người dùng, mỗi việc một dòng.

| Mục | Điền | Tránh |
|---|---|---|
| Overview | Một câu: giúp [ai] làm [việc] để đạt [kết quả]; 3-5 việc trong phạm vi; 2-3 việc ngoài phạm vi; một chỉ số thành công; anti-job 2-4 dòng (bắt buộc) | "Trợ lý đa năng"; anti-job chỉ ghi "cẩn thận" |
| Identity | Tên ngắn gợi việc; chức danh; mô tả 1-2 dòng nói làm gì và khi nào dùng; ngôn ngữ và cách xưng hô | Tên chung hoặc trùng |
| Skills | Bao nhiêu tùy vai trò cần, mỗi skill một quy trình (không đặt trần cố định); mỗi skill gắn với một việc trong Công việc và có mô tả kích hoạt, các bước đánh số, bước kiểm tra, mẫu đầu ra; bỏ skill không việc nào dùng | Một skill khổng lồ; skill không gắn việc nào; việc máy làm được lại bắt mô hình làm |
| Memory | Sở thích ổn định, quyết định đã chốt kèm lý do, chỗ người dùng đã sửa, thuật ngữ | Thứ hết hạn trong một tuần, bí mật, văn bản dài (để trong Library) |
| Library | Tệp nhỏ theo chủ đề, ngày cập nhật, người chịu trách nhiệm; một sổ cái hoặc tệp cho mọi trạng thái bot phải tin được qua các lần chạy (đã gửi gì, còn chờ gì, đã quyết gì) | Một tệp 50 trang; bản cũ lẫn bản mới; trạng thái chỉ nằm trong chat |
| Routines | Chỉ khi bot tự chạy: đặc tả năm phần từ bot-routine (owner, trigger, hành động được phép, đường leo thang, điều kiện dừng) | Lịch vài phút một lần không cần thiết |
| Access, Permissions | Điền từ bot-access: ứng dụng gắn với một việc, đọc trước ghi sau, cổng trước mọi hành động không hoàn tác | Kết nối tất cả cho tiện |
| Model | Mô hình nhỏ nhất vẫn qua các ca thử; rẻ hơn cho routine chạy nhiều | Dùng mô hình mạnh nhất cho mọi việc |
| Voice/alerts | Chỉ báo khi cần hành động: duyệt, lỗi, deadline; tin ngắn nói việc gì, cần làm gì, ở đâu; giờ yên lặng | Báo từng bước |
| History | Một thread một việc; thread nặng thì mở thread mới kèm bàn giao | Một thread dài vô tận |
| Usage | Theo dõi token hoặc chi phí mỗi việc hằng tuần; có hạn mức và cảnh báo | Không đo gì |

Nguồn sự thật (source of truth): một sổ cái hoặc tệp trong Library, không phải chat. Routine chạy không có ngữ cảnh chat và thread mới bắt đầu trống, nên mọi thứ bot phải tin được về sau (mục đã gửi, mục còn chờ, quyết định, số liệu hiện tại) nằm trong một tệp có tên, có người chịu trách nhiệm và có ngày. Bot đọc nó đầu mỗi lần chạy và ghi thêm vào cuối lần chạy. Khi sổ cái và chat mâu thuẫn thì sổ cái thắng, và dữ kiện do con người sở hữu chỉ do chính người đó sửa.

Xong khi: mỗi mục đều được điền hoặc ghi `không cần` kèm lý do, và không mục nào được điền chứa bí mật.

### 3. Giao brief cho soul và skill

Giao soul cho skill `bot-soul` (hoặc `prompt-design`) khi có, và từng quy trình cho `skill-design`, kèm brief: mục tiêu, đối tượng, đầu vào, ràng buộc, định nghĩa xong. Họ trả lại soul và skill cùng ca thử. Đừng làm lại việc của họ.

Khi thiếu các skill đó, tự viết. Soul, 150-400 từ, theo thứ tự: vai trò 1-2 câu; người dùng và mức am hiểu; giọng văn; nguyên tắc làm việc kèm lý do; ranh giới cứng (hỏi trước khi gửi, xóa, chi tiền, commit); anti-job; báo cáo trung thực (đã làm gì, chưa làm gì, lỗi gì, không báo xong khi chưa kiểm); ba nhãn thiếu dữ liệu dưới đây, đặt vào mọi soul để mỗi đầu ra nói cùng một ý bằng cùng một từ:

- `Unknown` (chưa biết): dữ kiện không có trong đầu vào và không tìm được. Nói rõ thiếu gì và có thể lấy từ đâu; không bao giờ đoán.
- `UNVERIFIED` (chưa kiểm chứng): đang giữ nhận định nhưng chưa đối chiếu với nguồn (nghe lại, bản tóm tắt, đồng đội báo). Giữ nhận định, gắn nhãn, và nói phép kiểm tra nào sẽ chốt được.
- `BLOCKED` (bị chặn): bước này không đi tiếp được nếu thiếu thứ bot không tự có (quyền truy cập, một phê duyệt, một đầu vào). Nói rõ cái gì đang chặn và ai gỡ được, rồi dừng.

Ưu tiên lý do hơn cấm đoán viết hoa. Quy trình để ngoài soul, thông tin dễ lỗi thời để ngoài mọi thứ. Skill tự viết: một thư mục có `SKILL.md` gồm `name`, `description` một dòng nói làm gì và khi nào kích hoạt, các bước đánh số mỗi bước kết thúc bằng tiêu chí kiểm tra được, và mẫu đầu ra.

Xong khi: soul qua được 5 câu hỏi khác nhau với giọng và ranh giới nhất quán, và khi thiếu dữ liệu thì trả lời `Unknown`, `UNVERIFIED` hoặc `BLOCKED` thay vì đoán.

## Giai đoạn tiếp theo

Nếu bot tự chạy thì bot-routine; rồi bot-access; rồi bot-score. Bàn giao bằng đúng 5 mục theo thứ tự: Mục tiêu (Goal), Đầu vào (Inputs), Sản phẩm (Deliverable), Xong khi (Done when), Việc còn mở (Open items). Nếu một skill anh em chưa cài, nói với người dùng giai đoạn tiếp theo theo tên (routine cần năm phần, quyền theo mức tối thiểu, rồi bảng điểm) và đề nghị làm.

## Tệp tham chiếu

- `profile-template.md`: đọc khi điền mục ở bước 2; 13 mục kèm gợi ý điền, tránh, ví dụ (tiếng Anh).
- `starter-frames.md`: đọc ở bước 1 để chọn khung xuất phát (tiếng Anh).

## Nguồn

- Masonshare, bộ 13 tiêu chí hồ sơ bot và bộ khung theo thể loại (nguyên bản).
- Anthropic, "Skill authoring best practices", https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices.
