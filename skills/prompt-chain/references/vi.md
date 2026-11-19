# Prompt Chain: bản tiếng Việt

Bản tiếng Việt của SKILL.md. Tách việc quá lớn cho một prompt thành các prompt nối nhau, mỗi mắt xích một việc.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì trả lời tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

Chuỗi luôn là prompt lớn: dừng ở dàn ý (bước 4), chờ duyệt.

## Các bước

### 1. Khởi động dự án

Hỏi một lượt, mỗi câu kèm đáp án gợi ý: mục tiêu cuối, bối cảnh (lĩnh vực), người đọc hoặc người dùng, kênh, ràng buộc (thời gian, ngân sách, pháp lý, giọng thương hiệu, độ dài), dữ liệu đang có, tiêu chí thành công đo được. Tối đa 5 câu.

### 2. Quy trình chuyên gia và bản đồ phụ thuộc

Nhờ model đóng vai chuyên gia 20 năm kinh nghiệm, mô tả quy trình từng bước để ra kết quả cuối, mỗi bước có mục tiêu, sản phẩm và KPI. Sau đó vẽ bản đồ phụ thuộc: mỗi bước cần đầu vào nào, đầu ra bước nào thành đầu vào bước nào.

### 3. Reality Check

Đối chiếu các bước với dữ liệu người dùng thật sự có. Bảng: bước, làm được chưa, thiếu gì, cách bù, giả định tạm kèm rủi ro. Rồi tự kiểm các giả định: cái nào dễ sai nhất, dấu hiệu nào cho thấy sai, phương án thay thế. Chỉ dùng thông tin người dùng đưa.

### 4. Kế hoạch và dàn ý (cổng)

Cắt gọn các bước theo hạn chót, nhân lực, công cụ và ràng buộc thật. Mỗi bước: mục tiêu, đầu vào cần, đầu ra, thời gian, tiêu chí xong. Đề xuất đặc tả đầu ra và checklist nghiệm thu 5-10 tiêu chí kiểm được (đây là tiêu chí chấm của prompt-test). Dừng chờ duyệt.

### 5. Dựng các mắt xích

Quy tắc chuỗi:
- Mỗi mắt xích một việc. Tách mọi câu "phân tích rồi sửa" thành hai prompt (lỗi tham lam).
- Mỗi prompt nêu rõ nó dùng đầu ra nào của bước trước và đầu ra của nó phục vụ bước nào.
- Prompt đầu liệt kê các chỗ điền trong ngoặc vuông, mỗi chỗ kèm ví dụ ngay trong ngoặc. Prompt sau chỉ liệt kê chỗ điền mới.
- Thêm bước xác nhận hoặc nhánh dự phòng ở mắt xích mà sai thì tốn kém.
- Bỏ các mắt xích người dùng tự làm được bằng sao chép.


Mỗi mắt xích viết: tên bước và một dòng giải thích; prompt trong khối code (tối thiểu Vai trò, Bối cảnh, Nhiệm vụ, Định dạng, kèm giới hạn chất lượng); các chỗ người dùng phải điền; đầu ra mong đợi và dòng "Đầu ra của prompt này là đầu vào của bước N".

Biến thể: duyệt từng bước (chỉ đưa prompt bước 1, kết thúc bằng "Dán đầu ra bước 1 vào đây, tôi viết prompt bước 2"); cụm 3 prompt khi cần nhiều phương án (tạo 3-5, chấm theo tiêu chí, chọn và phát triển); mắt xích kiểm chứng khi có dữ kiện dễ sai.

Bộ prompt dán sẵn cho các giai đoạn 0-5B và ba chuỗi mẫu nằm ở references/stage-prompts.md (tiếng Anh, dịch khi cần).

### 6. Chạy thử chuỗi

Chạy chuỗi một lần trên đầu vào mẫu nhỏ, từng mắt xích, kiểm đầu ra có đủ làm đầu vào bước sau không. Sửa chỗ bàn giao gãy trước. Muốn 5-10 case, chấm điểm và changelog thì chuyển cho prompt-test. Bàn giao đúng 5 trường: Mục tiêu, Đầu vào, Sản phẩm, Xong khi, Việc còn mở.

### Bàn giao (handoff)

Gửi đúng 5 trường, theo thứ tự:

```
1. Mục tiêu (Goal): <một câu>
2. Đầu vào (Inputs): <đính kèm hoặc liên kết gì>
3. Sản phẩm (Deliverable): <prompt v2 / soul / chuỗi, tên file hoặc nội dung trực tiếp>
4. Xong khi (Done when): <tiêu chí kiểm được, ví dụ 8/10 test case đạt, mỗi tiêu chí >= 8 điểm>
5. Việc còn mở (Open items): <case trượt, giả định, rủi ro, câu hỏi>
```
