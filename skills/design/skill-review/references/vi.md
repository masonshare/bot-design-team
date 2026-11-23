# Rà soát skill (bản tiếng Việt)

Bản tiếng Việt của `SKILL.md`. Đánh giá một skill đã có, hoặc cả một họ skill, và nói cần đổi gì. Nhận một SKILL.md hoặc thư mục (kèm các skill lân cận khi cần xét chồng chéo). Giao ra một bản đánh giá có điểm và danh sách sửa theo thứ tự ưu tiên.

Trả lời theo ngôn ngữ của người dùng. Người dùng Việt nhận đầu ra tiếng Việt, kèm thuật ngữ tiếng Anh trong ngoặc ở lần dùng đầu.

**Cổng (gate)** là điểm dừng để người dùng duyệt trước khi làm tiếp. Cổng ở đây: trước khi ghi đè hoặc xóa một skill đang có.

## Định tuyến

| Người dùng muốn | Dùng |
|---|---|
| Chấm, chia, gộp một skill có sẵn hoặc sửa từ một lỗi | skill này |
| Viết lại khi đã có kết luận | skill-write |
| Kiểm thử chứng minh bản sửa | skill-test |
| Kiểm tra theo chuẩn, phiên bản, xuất bản | skill-package |
| Một skill hoàn toàn mới | skill-design |

Khi skill tương ứng chưa được cài, nói một dòng rằng nó chưa có, rồi làm xong phần việc có thể làm ở đây.

## Các bước

### 1. Đọc

Đọc SKILL.md, các tệp tham chiếu và các bài kiểm thử nếu có. Liệt kê description của các skill lân cận đã cài. Với báo cáo lỗi, hỏi prompt và điều agent đã làm.

Xong khi: skill, các skill lân cận và (nếu có) prompt lỗi đều đã nằm trước mặt.

### 2. Chấm điểm

Skill sẵn sàng phát hành khi nó:

1. **Tối giản (minimal)**: một công việc mạch lạc; mỗi dòng đều làm thay đổi hành vi.
2. **Chính xác (accurate)**: các bước khớp với cách việc diễn ra thật, đã đối chiếu với một lần chạy thật.
3. **Mô-đun (modular)**: chiều sâu ở `references/`, việc tất định ở `scripts/`, mỗi dữ kiện có một nguồn duy nhất.
4. **Đầu vào và đầu ra rõ ràng**: nêu skill nhận gì và giao ra gì, để skill hoặc bot khác nối vào được.

Thêm ba kiểm tra: description nêu đúng một việc người dùng sẽ gõ; SKILL.md chạy được khi thiếu references; trong thư mục không có thông tin xác thực hay đường dẫn cá nhân. Đánh dấu từng mục đạt hoặc hỏng, kèm một dòng trích làm bằng chứng.

Xong khi: mỗi tiêu chí có dấu và một dòng trích.

### 3. Chồng chéo

Với mỗi skill lân cận, lấy ba câu người dùng sẽ gõ cho skill này và ba câu cho skill kia. Nếu một description có thể nhận nhầm câu của bên kia thì hai skill chồng chéo. Cách xử lý: thu hẹp description về đúng việc, thêm mệnh đề `Not for`, hoặc gộp.

Xong khi: mỗi cặp được đánh dấu rõ hay chồng chéo, kèm câu chỉ ra vấn đề.

### 4. Chia hay gộp

Chia khi: SKILL.md vượt khoảng 300 dòng, hai việc có câu kích hoạt khác nhau, hoặc một phần ít dùng hơn hẳn phần còn lại mà làm nặng mọi lần chạy. Gộp khi: hai skill luôn được nạp cùng nhau, hoặc description của chúng không phân biệt được.

Cân chi phí: description luôn nằm trong ngữ cảnh, nên mỗi skill thêm vào cộng thêm độ dài description của nó ở mọi lượt, còn phần thân nhỏ hơn tiết kiệm token ở mỗi lần chạy. Chỉ chia khi phần thân tiết kiệm được mỗi lần chạy lớn hơn phần description tăng thêm, tính trên số lần chạy dự kiến. Giữ một skill định tuyến ngắn để cả họ vẫn có một cửa vào. Giữ các dòng nhỏ lặp lại (quy tắc ngôn ngữ, cổng, bàn giao 5 trường) trong từng skill, vì mỗi SKILL.md phải chạy được một mình; lập danh sách chúng để một lần sửa đến được mọi bản sao. Chi tiết và công thức chi phí: [split-merge.md](split-merge.md).

Xong khi: có kết luận (giữ, chia, gộp hay viết lại) kèm các con số.

### 5. Sửa từ một lỗi thật

1. Tái hiện lỗi thành một ca kiểm thử kích hoạt hoặc tác vụ, chạy khi chưa sửa để xác nhận nó hỏng.
2. Sửa phần nhỏ nhất giải thích được lỗi: description nếu trượt kích hoạt, bước hoặc tiêu chí hoàn thành của nó nếu hành vi sai.
3. Chạy lại toàn bộ bộ kiểm thử và trình kiểm tra; xác nhận không ca cũ nào thụt lùi (dùng skill-test và skill-package).
4. Tăng phiên bản và thêm mục changelog nêu rõ nguyên nhân.

Xong khi: ca hỏng đã đạt, không ca cũ nào thụt lùi, và changelog nêu rõ nguyên nhân.

### 6. Báo cáo

Gửi bảng điểm, các dấu chồng chéo, kết luận và danh sách sửa theo thứ tự ưu tiên, theo mẫu bàn giao bên dưới.

## Bàn giao (handoff)

Khi chuyển việc cho bot khác hoặc người dùng, gửi 5 trường theo thứ tự: Goal (mục tiêu, một câu), Inputs (đầu vào đính kèm hoặc liên kết), Deliverable (sản phẩm: tên tệp hoặc nội dung trực tiếp), Done when (tiêu chí hoàn thành kiểm tra được), Open items (câu hỏi, rủi ro, việc chưa làm).

## Đọc thêm khi cần

Khi bước 4 quyết định chia hay gộp, đọc [split-merge.md](split-merge.md) (công thức chi phí, ví dụ chia và gộp, cách giữ các dòng lặp đồng bộ).

## Nguồn

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Anthropic, "Agent Skills overview" (các mức nạp): https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
