---
name: luu-vao-notion-second-brain
description: Optional storage module - when the user switches it on, save outputs (notes, tasks, new projects) into their Notion second-brain workspace instead of the default Google Docs / Sheets / Slides, under strict rules - create only, never edit or delete, always mark pages with a user-chosen prefix and tag. Use when the user says "lưu vào Notion", "save to Notion", "bật Notion", "ghi vào second brain", "tạo task trong Notion". Tiếng Việt - mô-đun lưu trữ tùy chọn, chỉ chạy khi người dùng bật; lưu kết quả thành Note, Task, Project mới trong Notion, không sửa hay xóa trang có sẵn, mọi trang tạo ra đều gắn tiền tố và thẻ do người dùng chọn.
---

# Lưu vào Notion second-brain

Mặc định các skill khác lưu kết quả vào Google Docs, Sheets hoặc Slides. Skill này là **mô-đun lưu trữ tùy chọn**: chỉ khi người dùng bật, kết quả mới đi vào Notion. Chưa bật thì không đụng tới Notion.

Workspace kỳ vọng là một mẫu Notion "second brain" có các cơ sở dữ liệu: ghi chú, công việc, dự án, mục tiêu, con người, và các trang kế hoạch ngày, tuần, năm. Skill chỉ làm việc với ba cơ sở dữ liệu đầu: **Notes, Tasks, Projects**.

## Khi không dùng skill này

- Người dùng chưa nói muốn dùng Notion: lưu theo mặc định (Google), đừng gợi ý đổi.
- Muốn sửa, dọn, lưu trữ, xóa trang Notion có sẵn: skill này không làm; hướng dẫn người dùng tự làm trong Notion.
- Muốn đọc hoặc sắp xếp mục tiêu, danh bạ, kế hoạch ngày/tuần/năm: ngoài phạm vi.
- Cần phân tích hay viết nội dung: dùng skill chuyên môn tương ứng nếu đã cài; skill này chỉ lo khâu lưu.

## Quy tắc (không thương lượng)

1. **Được tạo:** Note và Task.
2. **Project mới:** chỉ khi cần. Trước khi tạo, báo đúng một dòng "sẽ tạo Project X", rồi tạo và gửi liên kết cho người dùng.
3. **Không bao giờ** sửa, xóa hay lưu trữ trang có sẵn, kể cả trang do chính agent tạo từ lần trước. Muốn thay đổi thì tạo trang mới và nói rõ.
4. **Không chạm** vào mục tiêu, con người, và các trang kế hoạch ngày, tuần, năm. Không đọc chúng khi không cần thiết; để tìm một Project có sẵn thì chỉ tìm trong cơ sở dữ liệu Projects.
5. **Mọi trang tạo ra đều có dấu nhận diện:**
   - Tên bắt đầu bằng **tiền tố do người dùng chọn** (ví dụ "[BOT]"). Người dùng đưa tiền tố; không tự nghĩ ra.
   - Nếu người dùng nêu một **thẻ (tag) đã có**, gắn thẻ đó. Chỉ gắn thẻ có sẵn, không tạo thẻ mới. Thẻ không tồn tại thì dừng lại và hỏi người dùng.
6. **Việc làm cho khách hàng có tên:** nội dung đầy đủ, gồm cả số liệu, lưu nguyên trong Note; không tóm tắt cho ngắn.
7. **Nói thật về giới hạn:** các quy tắc trên là điều agent tự tuân thủ, không phải thứ kết nối Notion cưỡng chế. Quyền thật của kết nối do người dùng cấp; nếu muốn chắc chắn hơn, nên chia sẻ riêng ba cơ sở dữ liệu cho kết nối đó.

## Danh sách thiết lập (làm một lần)

Hỏi người dùng một lượt, mỗi câu có mặc định gợi ý:

- [ ] **Kết nối:** Notion đã được kết nối với agent chưa? Chưa thì xem phần xử lý lỗi.
- [ ] **Ba cơ sở dữ liệu:** tên hoặc liên kết của Notes, Tasks, Projects.
- [ ] **Tiền tố:** chuỗi đặt đầu tên mọi trang (ví dụ "[BOT]").
- [ ] **Thẻ:** có thẻ có sẵn nào cần gắn không? Nếu có, tên chính xác là gì?
- [ ] **Phạm vi:** xác nhận lại các quy tắc ở trên, kể cả lời nhắc ở quy tắc 7.

Lưu câu trả lời **chỉ trong tài liệu hồ sơ riêng của người dùng** (profile document, cùng chỗ với `brand-profile.md` nếu có). Không ghi tên cơ sở dữ liệu, liên kết hay mã định danh vào skill này. Lần sau đọc hồ sơ trước, không hỏi lại. Chưa có hồ sơ thì hỏi và đề nghị tạo một tài liệu mới để lưu.

## Quy trình mỗi lần lưu

1. Xác nhận người dùng đang bật Notion cho lần này (hoặc đã bật lâu dài trong hồ sơ).
2. Đọc thiết lập từ hồ sơ. Thiếu mục nào thì hỏi đúng mục đó.
3. Quyết định loại trang: kết quả để đọc lại là **Note**; việc cần làm là **Task**; một mảng việc mới chưa có chỗ chứa là **Project** (báo một dòng trước).
4. Nếu gắn Task vào Project: tìm Project có sẵn trong cơ sở dữ liệu Projects. Có thì liên kết; không có thì hỏi người dùng muốn tạo mới không.
5. Kiểm tra thẻ (nếu có) tồn tại trước khi tạo trang. Không tồn tại: dừng, hỏi.
6. Tạo trang với tiền tố, thẻ và nội dung theo mẫu dưới đây.
7. Gửi báo cáo liên kết ngược.

## Mẫu nội dung trang

### Note

```
Tên: [TIỀN TỐ] <tiêu đề rõ nghĩa>
Thẻ: <thẻ có sẵn, nếu có>
Project: <nếu có liên quan>

Nội dung trang:
- Bối cảnh: 1 đến 2 dòng, vì sao có ghi chú này
- Nội dung chính: đầy đủ, giữ nguyên số liệu, bảng, nguồn
  (việc cho khách hàng có tên: không rút gọn)
- Giả định: những điều chưa xác minh
- Bước tiếp theo: 1 việc cụ thể, ai làm, khi nào
- Nguồn: dữ liệu hoặc cuộc trò chuyện nào sinh ra ghi chú
```

### Task

```
Tên: [TIỀN TỐ] <động từ + việc cụ thể>
Thẻ: <thẻ có sẵn, nếu có>
Project: <nếu có>
Hạn: <chỉ điền khi người dùng đã nêu>

Nội dung trang:
- Việc cần làm: 1 đến 3 dòng
- Tiêu chí xong: nhìn vào là biết đã xong hay chưa
- Liên quan: liên kết tới Note hoặc tài liệu gốc
```

Không tự đặt mức ưu tiên, trạng thái hay ngày hạn nếu người dùng chưa nói; để trống hoặc để mặc định của cơ sở dữ liệu.

## Báo cáo liên kết ngược

Sau khi tạo, trả lời ngắn theo mẫu:

```
Đã lưu vào Notion:
- Note: [TIỀN TỐ] <tên> - <liên kết>
- Task: [TIỀN TỐ] <tên> - <liên kết>
- Project mới (nếu có): <tên> - <liên kết>
Gắn thẻ: <thẻ hoặc "không">
Không sửa hay xóa trang nào có sẵn.
Bước tiếp theo: <1 việc>
```

Chỉ liệt kê những gì thực sự đã tạo; trang nào lỗi thì nói rõ là lỗi.

## Xử lý lỗi

| Tình huống | Làm gì |
|---|---|
| Chưa có kết nối Notion | Dừng. Nói rõ cần kết nối Notion cho agent và chia sẻ ba cơ sở dữ liệu cho kết nối đó. Trong lúc chờ, hỏi người dùng có muốn lưu tạm sang Google Docs/Sheets mới không; chỉ làm khi họ đồng ý hoặc đã đặt Google làm mặc định. |
| Không tìm thấy cơ sở dữ liệu hoặc không có quyền | Dừng, nói cơ sở dữ liệu nào, đề nghị người dùng kiểm tra tên hoặc quyền chia sẻ. Không đi tìm ở chỗ khác. |
| Thẻ không tồn tại | Dừng, hỏi: dùng thẻ khác, bỏ thẻ, hay người dùng tự tạo thẻ rồi bảo agent tiếp tục. Agent không tạo thẻ. |
| Thiếu tiền tố | Hỏi, không tạo trang không có dấu nhận diện. |
| Tạo trang lỗi giữa chừng | Kiểm tra trang đã tạo trước khi thử lại để khỏi tạo trùng; không xóa trang lỗi, chỉ báo cho người dùng. |
| Tên Project trùng Project có sẵn | Dùng Project có sẵn hoặc hỏi; không tạo bản trùng. |

## Không bao giờ

- Sửa, xóa, lưu trữ, di chuyển trang có sẵn.
- Tạo thẻ mới, hay đổi thẻ của trang có sẵn.
- Đọc hoặc ghi mục tiêu, con người, kế hoạch ngày/tuần/năm.
- Tạo trang không có tiền tố, hoặc tự chọn tiền tố.
- Rút gọn số liệu trong Note của việc làm cho khách hàng có tên.
- Ghi tên cơ sở dữ liệu, liên kết, mã định danh hay thông tin tài khoản vào skill.
- Khẳng định Notion "chặn" được các hành vi trên; đó là quy tắc agent tuân theo.

## Quy tắc đầu ra

- Gắn nhãn giả định trong Note; kết thúc bằng một bước tiếp theo cụ thể.
- Chưa bật Notion hoặc chưa kết nối: lưu theo mặc định (Google mới nếu có kết nối, không thì trả lời ngay trong cuộc trò chuyện), không ghi đè tệp có sẵn.
- Không gửi, xuất bản, chi tiền hay đổi thứ gì ngoài cuộc trò chuyện (kể cả tạo Project) khi chưa có sự đồng ý của người dùng; riêng Project mới thì dòng báo "sẽ tạo Project X" là bước thông báo bắt buộc.

## Chất lượng

- Mọi trang có tiền tố; thẻ có sẵn hoặc không gắn.
- Không có thao tác sửa, xóa; không chạm vùng cấm.
- Note khách hàng giữ đủ số liệu; có giả định và bước tiếp theo.
- Báo cáo liên kết ngược khớp với những gì đã tạo thật.
- Thiết lập chỉ nằm trong hồ sơ của người dùng.

Nếu cần minh họa quan hệ giữa Note, Task và Project, đề nghị vẽ sơ đồ bằng skill `visual-thinking` nếu đã cài, không thì dùng bảng văn bản.
