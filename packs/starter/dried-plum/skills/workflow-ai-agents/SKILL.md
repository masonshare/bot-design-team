---
name: workflow-ai-agents
description: Guide a user through a four-step build (identify, research, blueprint, build and verify) that turns one repeatable business task into a single-purpose AI agent, ending with a blueprint document and a reusable draft of the agent's instructions. Use for "build an agent for this task", "automate this repeated job with AI", "turn my chat routine into an agent", "agent blueprint". Tiếng Việt - dẫn dắt 4 bước biến một việc lặp lại thành agent một mục đích. Dùng khi nói "tạo agent", "tự động hóa nghiệp vụ", "biến quy trình thành agent", "viết bản thiết kế agent", "soạn hướng dẫn cho agent".
---

# Dựng AI agent từ một nghiệp vụ lặp lại

Một agent tốt là một **việc hẹp, làm đúng, làm lặp lại được**. Skill này đi qua bốn bước, mỗi bước kết thúc bằng một cổng xác nhận. Chưa qua cổng thì chưa sang bước sau. Sản phẩm cuối: một **bản thiết kế agent** và một **bản nháp hướng dẫn (soul)** để người dùng dùng lại.

## Khi không dùng skill này

- Việc làm một lần, không lặp lại: cứ làm thẳng trong cuộc trò chuyện.
- Chưa rõ vấn đề gốc nằm đâu, chưa biết nên tự động hóa khâu nào: dùng `system-thinking` nếu đã cài; nếu chưa, hỏi ba câu ở Bước 1 trước.
- Muốn học cách làm việc với agent nói chung: dùng `agentic-vibe-working` nếu đã cài.
- Đã có sẵn agent và chỉ cần chỉnh hình dạng, giọng, phạm vi: dùng skill thiết kế bot cùng bộ (ví dụ `bot-shape`, `bot-design`) nếu đã cài; nếu chưa, chỉnh ngay ở Bước 3.

## Cách chạy

- Nếu người dùng có sẵn mô tả nghiệp vụ, đọc rồi hỏi bù tối đa một lượt; mỗi câu hỏi kèm đáp án mặc định để người dùng chỉ cần gật.
- Từ khóa chế độ: **express** (đi nhanh, bỏ qua cổng nhỏ), **guided** (mặc định, dừng ở mỗi cổng), **deep** (thêm vòng thử nghiệm ở Bước 4).
- Mọi giả định phải ghi nhãn "Giả định" trong bản thiết kế để người dùng sửa.

## Bước 1 - Nhận diện: nghiệp vụ này có hợp với agent không?

Hỏi: (1) việc cụ thể là gì, ai yêu cầu, kết quả cuối trông ra sao? (2) bao lâu lặp lại một lần? (3) hiện làm bằng cách nào và mất bao lâu?

Nếu câu trả lời mơ hồ ("tự động hóa kinh doanh", "để AI giúp công ty"), đừng tiến tiếp: dùng `system-thinking` nếu có, nếu không thì thu hẹp bằng cách hỏi "việc nào tuần trước bạn làm đi làm lại?".

Chấm đạt/chưa đạt từng tiêu chí:

| Tiêu chí | Đạt khi |
|---|---|
| Lặp lại | Xảy ra đều (mốc tham khảo: ít nhất vài lần mỗi tháng) |
| Có quy trình | Hai người làm sẽ ra kết quả gần giống nhau |
| Đầu vào lấy được | Dữ liệu nằm trong nguồn agent chạm tới được |
| Kết quả kiểm chứng được | Có cách nói "đúng" hay "sai" |
| Rủi ro chấp nhận được | Sai một lần không gây hậu quả không đảo ngược |

Quyết định: đạt cả năm là **Go**; thiếu một hai là **Go có điều kiện** (nêu điều kiện, ví dụ luôn có người duyệt trước khi gửi); thiếu nhiều hơn hoặc việc cần phán đoán thuần túy (đàm phán, chọn chiến lược) là **No-go**, giải thích rồi dừng.

**Cổng 1:** "Mình chốt Go cho nghiệp vụ này chứ?"

## Bước 2 - Nghiên cứu: cách việc này thực sự được làm

Mục tiêu: dựng được chuỗi thao tác thật của người làm giỏi, không suy từ trí nhớ.

1. Hỏi nguồn và công cụ: việc dùng trang web, phần mềm, tệp hay tài khoản nào? Người làm giỏi quan tâm điều gì, bỏ qua điều gì?
2. Chọn cách đọc theo loại nguồn:

| Loại nguồn | Cách làm |
|---|---|
| Trang tĩnh, đọc được không cần đăng nhập | Dùng công cụ tìm kiếm / đọc web của nền tảng; rẻ nhất, thử đầu tiên |
| Cần đăng nhập, nhiều script, ứng dụng một trang | Dùng công cụ điều khiển trình duyệt nếu nền tảng có; nếu không, nhờ người dùng dán nội dung hoặc xuất tệp |
| Biểu đồ, bảng phức tạp | Chụp màn hình rồi đọc ảnh, hoặc nhờ người dùng xuất bảng |
| Muốn biết dữ liệu đến từ đâu | Quan sát yêu cầu mạng khi tải trang nếu công cụ cho phép; nếu tìm được nguồn dữ liệu chính thức thì dùng nguồn đó, bền hơn cào giao diện |

3. **Không bao giờ xin mật khẩu hay mã xác thực.** Cần đăng nhập thì bảo người dùng tự đăng nhập trong cửa sổ đã mở, báo "xong", rồi mới tiếp tục. Gặp captcha thì dừng và nhờ người dùng xử lý.
4. Thiếu công cụ nào thì nói thẳng, rồi hạ cấp sang cách nhờ người dùng dán hoặc xuất nội dung. Không giả vờ đã vào được.
5. Vừa làm vừa ghi **nhật ký thao tác**: bước nào, nguồn nào, công cụ nào, kết quả mong đợi, chỗ nào kẹt.
6. Mời người dùng cho một ví dụ thật (đầu vào và kết quả họ cho là đúng) để đối chiếu.

Kết thúc bằng workflow sạch: danh sách bước đánh số, mỗi bước ghi hành động, nguồn, và cách biết bước đã xong.

**Cổng 2:** "Chuỗi bước này đúng với cách bạn muốn làm chưa? Bước nào thừa, thiếu?"

## Bước 3 - Lập bản thiết kế

Dựng bản thiết kế theo mẫu trong `assets/agent-blueprint-template.md`. Tám phần: vai trò và phạm vi, đầu vào, các bước, công cụ và quyền, cổng duyệt, xử lý lỗi, kiểm thử, vận hành. Nếu không đọc được tệp mẫu, dùng tám tiêu đề đó trực tiếp.

Nguyên tắc khi lập:

- **Một agent, một việc.** Thêm nghiệp vụ mới thì lập agent mới, không nhồi vào agent cũ.
- **Hỏi đủ đầu vào trước khi chạy.** Liệt kê từng thông tin bắt buộc, kiểu của nó, và câu hỏi agent dùng để hỏi. Chạy định kỳ (không có người hỏi) thì đầu vào cố định sẵn trong cấu hình.
- **Tối thiểu.** Mỗi bước phải có lý do; bỏ bước nào mà kết quả không đổi.
- **Cổng duyệt cho hành động có hậu quả.** Gửi tin, chi tiền, sửa dữ liệu, đăng bài đều cần người duyệt, trừ khi người dùng chủ động tắt và chấp nhận rủi ro.
- **Từ chối ngoài phạm vi là tính năng.** Agent nói rõ việc đó nằm ngoài, rồi chỉ về đúng nơi.
- **Lỗi không được im lặng.** Với mỗi bước, ghi: lỗi có thể gặp, dấu hiệu, agent làm gì (thử lại bao nhiêu lần, dừng, hay báo người), và báo cho ai.

Sau đó viết **bản nháp soul** từ `assets/agent-soul-draft.md`: danh tính, phạm vi, cách hỏi đầu vào, các bước, quy tắc an toàn, quy tắc báo lỗi, giọng văn. Soul phải đủ để một agent khác đọc là chạy được.

**Cổng 3:** "Bản thiết kế và soul đã đúng ý chưa? Có giả định nào cần sửa không?"

## Bước 4 - Xây và kiểm chứng

1. Tạo agent theo soul. Nền tảng nào dùng cách nào thì làm theo cách đó; nếu chưa rõ nền tảng, hỏi người dùng, không đoán.
2. Chạy thử ít nhất ba ca bằng đầu vào thật hoặc gần thật: một ca thường, một ca thiếu dữ liệu, một ca ngoài phạm vi.
3. Chấm từng ca với danh sách này:
   - Agent có hỏi đủ đầu vào trước khi làm không?
   - Kết quả có đúng định dạng và đúng ví dụ người dùng cho không?
   - Gặp lỗi có báo rõ, không bịa kết quả không?
   - Yêu cầu ngoài phạm vi có bị từ chối lịch sự không?
4. Sửa soul theo chỗ hỏng, chạy lại ca hỏng. Ghi vào bản thiết kế mỗi lần sửa và lý do.
5. Chọn cách chạy: **theo yêu cầu** (người dùng nhắn, agent trả lời ngay) hoặc **theo lịch** (hệ thống tự gọi, cần bộ xử lý lỗi để báo khi thất bại). Chạy theo lịch thì thử tay hai lần trước khi bật lịch.

**Cổng 4:** "Agent chạy đúng với các ca thử chưa? Bật chính thức chứ?" Chỉ bật, gửi hoặc xuất bản khi người dùng đồng ý.

## Kết quả giao

1. **Bản thiết kế agent** (tám phần), có nhãn "Giả định".
2. **Bản nháp soul** dùng lại được cho nền tảng khác.
3. **Nhật ký kiểm thử**: các ca, kết quả, chỗ đã sửa.
4. **Bước tiếp theo** cụ thể (ví dụ: "chạy thử ca thứ tư với dữ liệu tuần trước, rồi duyệt bật lịch").

Lưu thành tài liệu mới (Google Doc nếu có kết nối); không thì trả trong cuộc trò chuyện. Không ghi đè tệp có sẵn. Không gửi, đăng, chi tiền hay đổi gì ngoài cuộc trò chuyện khi chưa được người dùng cho phép. Có thể đề nghị vẽ sơ đồ luồng qua skill `visual-thinking` nếu đã cài, không thì dùng bảng văn bản.

## Chất lượng đầu ra

- Nghiệp vụ đã qua Go/No-go bằng tiêu chí, không bằng cảm tính.
- Mỗi bước có nguồn, công cụ và dấu hiệu hoàn thành.
- Không có chỗ nào agent phải xin mật khẩu hay tự đoán dữ liệu thiếu.
- Mọi hành động có hậu quả đều có cổng duyệt.
- Có đường xử lý lỗi cho từng bước, không im lặng.
- Ít nhất ba ca thử, trong đó có ca lỗi và ca ngoài phạm vi.
- Soul đọc một mình vẫn chạy được.

## Vận hành sau khi bật

Xem lại sau hai tuần đầu (kết quả sai ở đâu), rồi định kỳ (mốc tham khảo: mỗi quý) kiểm tra nguồn hoặc công cụ có đổi không. Khi đổi thì quay lại Bước 2 cho phần bị ảnh hưởng.
