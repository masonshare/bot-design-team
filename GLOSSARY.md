# Bot Design Team

Bot chạy trong Orca, trên máy và gói đăng ký của chính người dùng. Repo này chứa các skill thiết kế bot và pack mẫu `ecommerce-cskh` (dữ liệu giả).

## Thuật ngữ

**Pack (gói)**: Thư mục các bot, skill và dữ liệu mẫu cài được vào Orca, ví dụ `packs/ecommerce-cskh`.

**Bot Design Team**: Nhóm chuyên gia thiết kế bot, kỹ năng và prompt (câu lệnh hướng dẫn).

**Skill (kỹ năng)**: Gói hướng dẫn giúp bot thực hiện một loại công việc. Viết trung lập, chạy được trên cả Claude Code và Codex.

**Chủ shop**: Chủ doanh nghiệp, người duy nhất duyệt kịch bản (`Đã duyệt`), đặt `Hết hạn` và ghi tên vào `Người duyệt`. Thuật ngữ chuẩn trong SOUL và tài liệu; "chủ dự án" là cách gọi khác của cùng một người, không dùng thêm trong tài liệu mới.

**Editor bot / bot biên tập**: Bot của chủ shop; nhận chat/câu hỏi thật đã gỡ tên và số điện thoại, soạn kịch bản ở trạng thái `Nháp`. Không tự duyệt.

**Staff bot / bot nhân viên**: Bot của từng nhân viên, chạy trên Orca và tài khoản Codex/ChatGPT riêng; tra kịch bản `Đã duyệt` ở chế độ chỉ đọc và ghi câu hỏi chưa có đáp án vào file `Đề xuất CSKH`.

**Kịch bản** (script): Một mẫu trả lời khách (CSKH) có cấu trúc: Mã, Nhóm, Tình huống, Câu khách hay hỏi, Mẫu trả lời, Kênh áp dụng, Lưu ý nội bộ, Trạng thái, Người duyệt + ngày. `Lưu ý nội bộ` chỉ để nhân viên đọc, không dán vào câu trả lời cho khách.

**Trạng thái**: Giá trị của kịch bản.
- **Nháp**: Bot vừa soạn, chưa được duyệt; không phải đáp án chính thức.
- **Đã duyệt**: Chủ shop đã duyệt (ghi người duyệt và ngày); chỉ trạng thái này là chính thức với nhân viên.
- **Hết hạn**: Không còn dùng vì chính sách hoặc giá đã đổi.

**Đề xuất**: Tab ghi các câu hỏi nhân viên hỏi mà chưa có kịch bản; chủ shop xem để biến thành kịch bản mới. Tab này nằm trong file `Đề xuất CSKH`.

**Đề xuất CSKH**: File Google Sheet riêng chứa tab `Đề xuất`. Nhân viên có quyền chỉnh sửa file này (và chỉ file này); file kịch bản chính chỉ cho nhân viên xem. Tách file vì Google chia sẻ theo file, không theo tab (ADR 0002).

**Knowledge base (kho tri thức)**: Tập kịch bản đã duyệt, lưu trong Google Sheet của chủ shop. Dữ liệu thật chỉ nằm ở đó, không bao giờ vào repo công khai.

**Kênh áp dụng**: Kênh mà kịch bản dùng được: tất cả, Shopee, Zalo hoặc hotline. Kịch bản cho sàn (Shopee) không được dẫn khách ra ngoài sàn.

**Chưa duyệt (câu trả lời tạm)**: Bản trả lời tạm khi chưa có kịch bản, đánh dấu "chưa duyệt". Không được dùng cho giá, đổi trả/hoàn tiền, cam kết thời gian giao và ATTP (an toàn thực phẩm); với bốn mục này bot nói chưa có trong kho tri thức và nhắc hỏi chủ shop.

**Nghiệm thu**: Đánh giá gói bằng các phép thử và bằng chứng theo tiêu chí đã thống nhất.

**Use case (trường hợp sử dụng)**: Công việc cụ thể được một gói bot hỗ trợ.

**Chỉ soạn nháp**: Quy tắc bot chỉ soạn và phân tích; người dùng tự gửi khách, đăng sản phẩm, đổi giá.

**Dữ liệu giả**: Dữ liệu mẫu bịa trong repo để dùng thử pack; mọi dữ liệu công ty thật nằm ngoài repo.
