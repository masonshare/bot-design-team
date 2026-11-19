# Kiểm thử skill (bản tiếng Việt)

Bản tiếng Việt của `SKILL.md`. Chứng minh skill kích hoạt đúng prompt và làm hành vi tốt hơn. Nhận một thư mục skill. Giao ra bảng kết quả và kết luận đạt hay không.

**Cổng (gate)** là điểm dừng để người dùng duyệt trước khi làm tiếp. Cổng ở đây: trước khi ghi đè một tệp evals đang có.

## Định tuyến

| Người dùng muốn | Dùng |
|---|---|
| Kiểm thử kích hoạt, kiểm thử tác vụ, nền so với chạy lại | skill này |
| Viết lại description hoặc phần thân sau một lỗi | skill-write |
| Chấm, chia hoặc gộp skill | skill-review |
| Kiểm tra theo chuẩn, phiên bản, xuất bản | skill-package |
| Làm trọn cả quy trình | skill-design |

Khi skill tương ứng chưa được cài, nói một dòng rằng nó chưa có, rồi làm xong phần việc có thể làm ở đây.

## Các bước

### 1. Kiểm thử kích hoạt (trigger tests)

1. Viết 8-10 prompt nên kích hoạt skill và 8-10 prompt không nên. Prompt âm tính nên là loại gần giống, có chung từ khóa, và có ít nhất 2 prompt thuộc về một skill anh em. Thay đổi cách diễn đạt, độ trang trọng, độ dài và việc có nêu tên lĩnh vực hay không. Viết bằng đúng các ngôn ngữ người dùng sẽ gõ.
2. Cài skill cạnh vài skill không liên quan và cạnh mọi skill đã cài có description gần giống (ví dụ một skill hướng dẫn viết skill nói chung). Ghi lại đối thủ nào thắng một prompt nên kích hoạt.
3. Chạy mỗi prompt 3 lần, mỗi lần trong ngữ cảnh mới. Một prompt được tính là kích hoạt khi skill được nạp ít nhất 2 trong 3 lần.
4. Chia prompt khoảng 60/40 thành bộ tinh chỉnh và bộ giữ riêng (held-out). Chỉnh description theo bộ thứ nhất, rồi kiểm bộ thứ hai. Sửa lỗi trượt bằng cách dán nguyên từ của nó vào description là học vẹt (overfit); hãy thêm tình huống người dùng đằng sau. Không dùng prompt của bộ giữ riêng khi viết description.

Xong khi: một bảng liệt kê mọi prompt, kết quả mong đợi, skill nào kích hoạt trong từng lần chạy và cách chạy (thật hay mô phỏng).

### 2. Kiểm thử tác vụ (task tests)

Viết 3-5 prompt thực tế kèm hành vi mong đợi, thêm một prompt mơ hồ và một trường hợp biên. Lưu thành `evals/evals.json`:

```json
{
  "skill_name": "<name>",
  "evals": [
    {
      "id": 1,
      "prompt": "Một tin nhắn thực tế, viết như người dùng sẽ gõ.",
      "expected_output": "Hành vi mà một lần chạy đúng thể hiện.",
      "files": [],
      "assertions": ["Một câu kiểm tra được, ví dụ: hỏi định dạng đầu ra trước khi soạn"]
    }
  ]
}
```

Mỗi khẳng định (assertion) chấm được ĐẠT hoặc HỎNG từ bản ghi, kèm một dòng trích làm bằng chứng. Khẳng định mô tả hành vi, không nêu số bước nội bộ. Prompt kích hoạt đặt trong `evals/triggers.json` dưới dạng các mục `{ "query": "...", "should_trigger": true }`.

Xong khi: mỗi ca có prompt, hành vi mong đợi và các khẳng định.

### 3. Chạy nền (baseline)

Chạy từng ca tác vụ trong ngữ cảnh mới, không có skill. Ghi lại kết quả và, với mỗi lỗi, đúng lời agent đã dùng cùng lối tắt nó đã đi. Trích dẫn thật cho thấy nguyên nhân; diễn giải thì che mất.

Xong khi: mỗi ca đã có kết quả nền.

### 4. Chạy lại (retest)

Chạy cùng các ca với skill, mỗi lần trong ngữ cảnh mới. Khi nền tảng chỉ nhập SKILL.md, kiểm thử chỉ với SKILL.md, vì một số người dùng nhận đúng như vậy. Chấm từng khẳng định ĐẠT hoặc HỎNG kèm dòng trích. So ba cột cho mỗi ca: nền, có skill, mong đợi.

Xong khi: mọi khẳng định đã được chấm.

### 5. Sửa và chạy lại

Xử lý mỗi lỗi tại nguyên nhân: skill không được nạp nghĩa là description yếu; bỏ qua một bước nghĩa là tiêu chí hoàn thành yếu; kết quả sai nghĩa là thiếu một chỉ dẫn. Chạy lại các ca hỏng cùng một mẫu các ca đã đạt. Thường năm vòng trở xuống là ổn.

Xong khi: các ca hỏng đã đạt và không ca cũ nào thụt lùi.

### 6. Ngưỡng đạt và báo cáo

Ít nhất 80% prompt nên kích hoạt thì kích hoạt, nhiều nhất 10% prompt không nên kích hoạt mà vẫn kích hoạt, và mọi ca tác vụ đạt hành vi mong đợi. Kết thúc bằng một bảng: ca, nền, có skill, kết luận, thay đổi đã làm. Đánh dấu mỗi dòng là thật (đã chạy thật) hay mô phỏng (suy luận, chưa chạy), và liệt kê điều còn hỏng ở mục việc còn mở.

Xong khi: kết quả nền và chạy lại nằm cạnh nhau và đạt ngưỡng, hoặc các lỗi còn lại được liệt kê.

## Kiểu kiểm thử theo loại skill

| Loại | Kiểm thử bằng | Đạt khi |
|---|---|---|
| kỹ thuật | một tình huống mới, một biến thể, một prompt thiếu thông tin | áp dụng đúng các bước và hỏi phần thông tin còn thiếu |
| tham chiếu | câu hỏi có đáp án trong references, cộng một câu hỏi nằm ngoài | tìm đúng dữ kiện và nói rõ khi không có |
| kỷ luật | quy tắc dưới áp lực: hạn chót, "bỏ qua đi" | giữ quy tắc và giải thích ngắn gọn |
| mẫu tư duy | một ca mẫu phù hợp và một ca không phù hợp | nhận ra cả hai |

## Bàn giao (handoff)

Khi chuyển việc cho bot khác hoặc người dùng, gửi 5 trường theo thứ tự: Goal (mục tiêu, một câu), Inputs (đầu vào đính kèm hoặc liên kết), Deliverable (sản phẩm: tên tệp hoặc nội dung trực tiếp), Done when (tiêu chí hoàn thành kiểm tra được), Open items (câu hỏi, rủi ro, việc chưa làm).

## Đọc thêm khi cần

Khi chạy kiểm thử hoặc khi skill liên tục hỏng, đọc [testing.md](testing.md) (cách dựng subagent, cách đọc skill nào đã kích hoạt bằng dòng lệnh, giới hạn của từng cách).

## Nguồn

- obra/superpowers, "writing-skills" (ý tưởng kiểm thử trước cho skill): https://github.com/obra/superpowers
- Agent Skills, đánh giá skill và tối ưu description: https://agentskills.io
