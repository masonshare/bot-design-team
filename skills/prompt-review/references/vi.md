# Prompt Review: bản tiếng Việt

Bản tiếng Việt của SKILL.md. Tìm vì sao prompt có sẵn bị lỗi, sửa các nguyên nhân chính, đưa bằng chứng.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì trả lời tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

## Các bước

Đầu vào: một prompt có sẵn cùng triệu chứng (hoặc không có triệu chứng).

1. Đọc prompt và triệu chứng. Chưa có đầu ra lỗi thì xin một ví dụ.
2. Chẩn đoán theo 4 lỗi và 6 yếu tố (bảng bên dưới). Mỗi phát hiện trích đúng dòng liên quan.
3. Xếp phát hiện theo mức ảnh hưởng. Sửa 3 cái đầu trước.
4. Viết lại prompt. Đánh dấu mỗi thay đổi bằng phát hiện mà nó giải quyết.
5. Kiểm chứng: chạy prompt cũ và mới trên đầu vào đang lỗi cộng 2 đầu vào khác (một biên, một điển hình). Muốn 5-10 case và changelog thì chuyển cho prompt-test.

Xong khi: mỗi phát hiện trích một dòng, bản viết lại trả lời từng phát hiện, và kết quả test cho thấy triệu chứng đã hết.

### 4 lỗi phổ biến (Masonshare)

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Mơ hồ (vague) | Dùng "hay hơn", "chuyên nghiệp", "tối ưu" mà không có thước đo | Thay mỗi từ bằng tiêu chí đo được: giọng văn, độ dài, thuật ngữ, số lượng |
| Tham lam (greedy) | Một prompt bắt model vừa đánh giá vừa hành động | Tách thành prompt đánh giá và prompt hành động dùng kết quả đánh giá |
| Thả rông (unbounded) | Không giới hạn định dạng, độ dài, phong cách, phạm vi | Thêm hàng rào: độ dài, cấu trúc, đối tượng, mục bắt buộc, ngoài phạm vi |
| Gài bẫy (trapping) | Câu hỏi chứa sẵn đáp án ("giải thích vì sao A tốt nhất") | Hỏi trung lập ("so sánh A, B, C theo mục tiêu") hoặc giao vai phản biện |

### Checklist 6 yếu tố (Masonshare)

Không phải prompt nào cũng cần đủ sáu. Kiểm từng yếu tố và chỉ giữ yếu tố nào làm thay đổi đầu ra.

| Yếu tố | Kiểm tra |
|---|---|
| Bối cảnh (Context) | Model có biết tình huống, đối tượng, mục đích chưa? |
| Vai trò (Role) | Vai có cụ thể (lĩnh vực, kinh nghiệm, lập trường) không? |
| Nhiệm vụ (Task) | Mỗi việc một động từ mạnh, việc ghép đã tách chưa? |
| Ví dụ (Example) | Có 2-5 ví dụ nhất quán, đa dạng, tách rõ đầu vào và đầu ra không? Tác vụ đơn giản thì không cần ví dụ. |
| Giọng điệu (Tone) | Giọng được nêu bằng cặp tính từ hoặc mẫu chưa? |
| Định dạng (Format) | Hình dạng đầu ra có rõ: bảng, JSON, gạch đầu dòng, độ dài? |
