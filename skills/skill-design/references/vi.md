# Thiết kế skill, bộ định tuyến (bản tiếng Việt)

Bản tiếng Việt của `SKILL.md`. Skill này nhận phần tiếp nhận, giao từng giai đoạn cho skill anh em tương ứng và giữ đúng thứ tự. Vòng làm việc (work loop): làm rõ, nghiên cứu, lập kế hoạch, xây dựng, kiểm chứng.

Trả lời theo ngôn ngữ của người dùng. Người dùng Việt nhận đầu ra tiếng Việt, kèm thuật ngữ tiếng Anh trong ngoặc ở lần dùng đầu.

**Cổng (gate)** là điểm dừng để người dùng duyệt trước khi làm tiếp. Các cổng trong cả họ skill này: trước khi cài bất cứ thứ gì tìm được trên mạng, trước khi ghi đè một skill đang có, trước khi xuất bản.

## Skill là gì

**Agent Skill** là một thư mục có tệp `SKILL.md` (frontmatter YAML gồm `name` và `description`, rồi các bước bằng Markdown) và tùy chọn `scripts/`, `references/`, `assets/`. Agent nạp skill theo từng mức: `description` luôn nằm trong ngữ cảnh, thân `SKILL.md` nạp khi prompt khớp, các tệp khác chỉ nạp khi được đọc hoặc chạy.

| Thứ | Khi nào được nạp | Dùng khi |
|---|---|---|
| Prompt | Chỉ lượt đó | Việc làm một lần |
| Soul (chỉ dẫn thường trực của bot) | Mọi lượt, xếp trên skill | Bot là ai và không bao giờ làm gì |
| AGENTS.md / CLAUDE.md | Mọi phiên | Sự kiện và quy tắc ngắn của dự án |
| Skill | Description luôn nạp, thân nạp khi khớp | Quy trình lặp lại, mỗi lần chạy giống nhau |

## Định tuyến trước

| Người dùng muốn | Dùng |
|---|---|
| Làm trọn một skill mới, hoặc chưa biết bắt đầu từ đâu | skill này |
| Biết đã có skill chưa, hoặc ý tưởng có đáng làm skill không | skill-search |
| Viết hoặc cấu trúc lại description, SKILL.md | skill-write |
| Kiểm thử kích hoạt, chạy nền so với chạy lại, skill không bao giờ kích hoạt | skill-test |
| Đánh giá, chia, gộp một skill có sẵn, hoặc sửa từ một lỗi thật | skill-review |
| Kiểm tra theo chuẩn, đặt phiên bản, xuất bản, chia sẻ | skill-package |

Khi một skill anh em chưa được cài, nói một dòng rằng nó chưa có, rồi làm phần việc của nó bằng phương án dự phòng ở bước 3. Không bao giờ dừng cả công việc chỉ vì thiếu một skill anh em.

## Các bước

### 1. Tiếp nhận (làm rõ)

Hỏi gộp một lần tất cả trường còn thiếu. Trường nào chưa có thì điền mặc định và nói rõ.

| Trường | Câu hỏi | Mặc định |
|---|---|---|
| chủ đề (topic) | Quy trình, SOP hay kiến thức nào sẽ thành skill? | bắt buộc |
| người dùng đích (target user) | Ai chạy skill, trong agent nào? | bắt buộc |
| đầu vào sẵn có (inputs) | Tài liệu, bản ghi, ví dụ, một lần chạy thật? | không có |
| mức chi tiết | cao, vừa hay thấp | vừa |
| ngôn ngữ | Ngôn ngữ của thân skill | tiếng Anh, kèm bản tiếng Việt cho người dùng Việt |
| chế độ chạy (execution mode) | `coach` (hỏi từng bước), `auto` (chạy trọn vẹn, chỉ dừng ở cổng) hoặc `hybrid` | hybrid |
| nơi triển khai | cài toàn cục, thư mục dự án, hay repo công khai | thư mục dự án |
| tiêu chí hoàn thành | Một lần chạy đúng trông như thế nào | một tác vụ mẫu |

Xong khi: mọi trường đã có câu trả lời hoặc mặc định được nêu rõ, và người dùng xác nhận bản tóm tắt.

### 2. Chạy các giai đoạn theo thứ tự

| Giai đoạn | Skill | Đầu ra nuôi giai đoạn sau |
|---|---|---|
| Tìm và quyết định làm hay không | skill-search | kết luận (dùng, tùy biến, làm mới, hoặc không làm) kèm danh sách ứng viên |
| Mô tả và phần thân | skill-write | một thư mục skill |
| Kiểm thử kích hoạt và tác vụ | skill-test | bảng kết quả, nền so với chạy lại |
| Rà soát (tùy chọn, cho skill lớn hoặc đông đúc) | skill-review | điểm và kết luận chia hay gộp |
| Kiểm tra và đóng gói | skill-package | thư mục đạt chuẩn, phiên bản, changelog, người dùng đã duyệt |

Sau mỗi giai đoạn, báo cho người dùng một dòng kết quả rồi đi tiếp. Dừng ở cổng. Ở chế độ `coach`, hỏi trước mỗi giai đoạn.

Xong khi: người dùng cầm một thư mục skill đã qua skill-test và skill-package, hoặc biết giai đoạn nào còn mở.

### 3. Dự phòng khi thiếu skill anh em

Làm bản nhỏ nhất mà trung thực, ghi chú "tối thiểu, skill anh em chưa cài":

- skill-search: chạy `npx skills find <nhu cầu trong 2-4 từ>`, đọc các ứng viên đầu bảng, hỏi dùng, tùy biến hay làm mới. Chỉ làm khi tác vụ lặp lại, agent sai khi thiếu hướng dẫn, các bước viết ra và kiểm tra được, và kiến thức còn đúng quá một tuần.
- skill-write: viết description trước (một dòng, tối đa 1024 ký tự, không dấu nháy kép, không có `: `, động từ trước, `Use when` kèm 3-6 tình huống người dùng, 4-8 từ khóa bằng ngôn ngữ người dùng). Sau đó đánh số các bước, mỗi bước kết thúc bằng "Xong khi" kiểm tra được. SKILL.md phải chạy được một mình, không cần references hay scripts.
- skill-test: viết 3 prompt nên kích hoạt và 2 prompt không nên, chạy mỗi prompt khi không có và khi có skill trong ngữ cảnh mới, ghi kết quả vào bảng.
- skill-review: kiểm tra skill chỉ làm một việc, mỗi dòng đều làm thay đổi hành vi, và chạy được chỉ từ SKILL.md.
- skill-package: kiểm tra `name` trùng tên thư mục, chữ thường và gạch ngang đơn, description không rỗng và tối đa 1024 ký tự, SKILL.md dưới 500 dòng, mọi liên kết tương đối trỏ đúng, không có đường dẫn cục bộ tuyệt đối. Hỏi trước khi xuất bản.

## Bàn giao (handoff)

Khi chuyển việc cho bot khác hoặc người dùng, gửi 5 trường theo thứ tự: Goal (mục tiêu, một câu), Inputs (đầu vào đính kèm hoặc liên kết), Deliverable (sản phẩm: tên tệp hoặc nội dung trực tiếp), Done when (tiêu chí hoàn thành kiểm tra được), Open items (câu hỏi, rủi ro, việc chưa làm).

## Nguồn

- Anthropic, "Skill authoring best practices": https://docs.claude.com/en/docs/agents-and-tools/agent-skills/best-practices
- Đặc tả Agent Skills: https://agentskills.io/specification
- Thư mục skill: https://skills.sh
