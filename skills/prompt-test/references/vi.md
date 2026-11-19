# Prompt Test: bản tiếng Việt

Bản tiếng Việt của SKILL.md. Một prompt chỉ xong khi đã qua test case: baseline trước, retest sau, kết quả đặt cạnh nhau.

Trả lời bằng ngôn ngữ của người dùng. Người dùng viết tiếng Việt thì trả lời tiếng Việt, giữ thuật ngữ tiếng Anh trong ngoặc ở lần đầu.

## Các bước

### 1. Tiêu chí

Lấy 3-7 tiêu chí chấm từ ví dụ Gold Standard hoặc checklist nghiệm thu nếu có. Không có thì suy ra từ mục tiêu và định nghĩa hoàn thành, ghi là giả định. Mỗi tiêu chí phải kiểm được.

### 2. Test case, 3. Baseline rồi retest

Viết test case trước khi đánh giá prompt. Một test case là một đầu vào cụ thể cộng với hành vi mong đợi.

Phủ: 3 đầu vào điển hình, 2 đầu vào biên (rỗng, rất dài, sai ngôn ngữ, thiếu trường), 1 đầu vào đối kháng (câu hỏi dẫn dắt, chỉ dẫn giấu trong dữ liệu), và với soul thêm 1 yêu cầu ngoài phạm vi, cần từ chối hoặc chuyển hướng.

Chạy baseline trước (làm việc không có prompt, hoặc bản cũ), rồi chạy lại (retest) với prompt mới, và so cả hai với hành vi mong đợi. Khi không chạy được model tại chỗ, đưa người dùng các case cùng phiếu chấm và nhờ họ dán kết quả về.

Xong khi: có 5-10 case, đã ghi kết quả baseline và retest, và mỗi case có đạt hoặc không đạt kèm lý do một dòng.

### 4. Chấm điểm và chẩn đoán, 5. Sửa và chạy lại

Chấm đầu ra retest theo tiêu chí ở bước 1, thang 1-10. Nêu 3 vấn đề lớn nhất. Chẩn đoán từng vấn đề theo 4 lỗi. Sửa prompt chỉ cho các vấn đề đó. Chạy lại các case trượt cộng hai case đã đạt (để bắt lỗi thụt lùi). Giao bản v2 kèm nhật ký thay đổi (changelog).

Dừng vòng lặp khi mọi case đạt hoặc sau 3 vòng, rồi ghi các lỗi còn lại vào mục việc còn mở. Prompt tốt nhất không được viết ra một lần, nó được tiến hóa.

Xong khi: mọi case đạt, hoặc đã chạy 3 vòng và các lỗi còn lại được liệt kê.

### 6. Giao v2

Giao v2 kèm changelog và bàn giao.

### 4 lỗi phổ biến (Masonshare)

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Mơ hồ (vague) | Dùng "hay hơn", "chuyên nghiệp", "tối ưu" mà không có thước đo | Thay mỗi từ bằng tiêu chí đo được: giọng văn, độ dài, thuật ngữ, số lượng |
| Tham lam (greedy) | Một prompt bắt model vừa đánh giá vừa hành động | Tách thành prompt đánh giá và prompt hành động dùng kết quả đánh giá |
| Thả rông (unbounded) | Không giới hạn định dạng, độ dài, phong cách, phạm vi | Thêm hàng rào: độ dài, cấu trúc, đối tượng, mục bắt buộc, ngoài phạm vi |
| Gài bẫy (trapping) | Câu hỏi chứa sẵn đáp án ("giải thích vì sao A tốt nhất") | Hỏi trung lập ("so sánh A, B, C theo mục tiêu") hoặc giao vai phản biện |

### Bảng test case

```
| # | Loại | Đầu vào | Hành vi mong đợi | Baseline | Retest | Đạt |
|---|------|---------|------------------|----------|--------|-----|
```

### Phiếu chấm và changelog

```
Tiêu chí | Điểm 1-10 | Bằng chứng
3 vấn đề lớn nhất: 1) <vấn đề> -> <loại lỗi> 2) ... 3) ...

## Changelog v2
- Đã đổi: <gì> vì <vấn đề hoặc case trượt #>
- Giữ nguyên: <gì> vì <case đã đạt>
- Vẫn trượt: <case #, lý do>
```

### Bàn giao (handoff)

Gửi đúng 5 trường, theo thứ tự:

```
1. Mục tiêu (Goal): <một câu>
2. Đầu vào (Inputs): <đính kèm hoặc liên kết gì>
3. Sản phẩm (Deliverable): <prompt v2 / soul / chuỗi, tên file hoặc nội dung trực tiếp>
4. Xong khi (Done when): <tiêu chí kiểm được, ví dụ 8/10 test case đạt, mỗi tiêu chí >= 8 điểm>
5. Việc còn mở (Open items): <case trượt, giả định, rủi ro, câu hỏi>
```
