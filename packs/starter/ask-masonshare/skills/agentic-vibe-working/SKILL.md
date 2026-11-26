---
name: agentic-vibe-working
description: Six-step framework that lets an AI agent run a complex, multi-step task end to end - define, research, plan, execute, verify, package - with a plan file it can re-read after its context is compacted. Use when the user hands over a big job ("build this feature", "write a full guide", "analyse this problem", "do this end to end", "complex task", "multi-step") and the work needs research, a plan and checks. Not for one-step trivial jobs. Tiếng Việt - quy trình 6 bước để agent tự xử lý công việc phức tạp từ đầu đến cuối (làm rõ, nghiên cứu, lập kế hoạch, thực thi, kiểm chứng, đóng gói). Dùng khi user giao việc nhiều bước, "làm giúp", "làm từ A đến Z", "task phức tạp", "xây tính năng", "viết tài liệu chuyên sâu", "phân tích vấn đề".
---

# Agentic Vibe Working: làm việc phức tạp từ đầu đến cuối

Khung sáu bước để agent không chỉ trả lời mà tự dẫn công việc tới khi đạt mục tiêu: **Làm rõ, Nghiên cứu, Lập kế hoạch, Thực thi, Kiểm chứng, Đóng gói**. Điểm mấu chốt: hỏi đúng ở đầu, dừng đúng chỗ để người dùng quyết, và có bằng chứng trước khi nói "xong".

## Khi không dùng skill này

- Việc một bước (sửa lỗi chính tả, đổi tên biến, tra cú pháp), hoặc câu hỏi trả lời nhanh: làm thẳng.
- Người dùng chỉ muốn trò chuyện, chưa có việc cụ thể: trò chuyện trước.
- Công việc chỉ cần đào sâu một chủ đề: dùng skill nghiên cứu nếu đã cài, nếu không thì chỉ chạy bước 2 của khung này.
- Chỉ cần biến một quy trình đã có sẵn thành skill: dùng skill thiết kế skill nếu đã cài, hoặc nhảy thẳng tới bước 6.

## Các điểm dừng chờ người dùng

| Điểm | Khi nào | Mục đích |
|---|---|---|
| Bước 1 | Luôn | Chốt mục tiêu và tiêu chí xong |
| Bước 3 | Luôn | Duyệt kế hoạch trước khi làm |
| Bước 5a | Luôn | Nghiệm thu kết quả |
| Bước 5b | Luôn | Quyết định có đóng gói không |
| Bước 2 | Chỉ khi cần nghiên cứu sâu | Chọn mức sâu và thời gian |
| Bước 4 | Chỉ khi gặp hành động rủi ro | Xin phép trước khi làm |
| Bước 6 | Luôn trước khi tạo file | Chốt tên và nơi đặt skill |

Giữa các điểm dừng, agent tự chạy, không hỏi vặt.

## Khi không hỏi được người dùng
Nếu người dùng không trả lời kịp hoặc môi trường không cho hỏi, đừng đứng lại ở bước làm rõ. Ghi các mặc định đang dùng thành giả định, tiếp tục các bước tự chạy, và giao kết quả kèm danh sách giả định để người dùng sửa. Chỉ dừng hẳn ở những việc cần quyết định hoặc chi tiền.

## Bước 1. Làm rõ công việc và mục tiêu (dừng)

Sai ở đây thì năm bước sau vô nghĩa.

1. Nếu người dùng giữ `brand-profile.md` hoặc tài liệu bối cảnh tương tự, đọc trước và không hỏi lại những gì đã có.
2. Hỏi người dùng một lượt, 3 đến 5 câu, mỗi câu có sẵn đáp án mặc định để họ chỉ cần gật. Tập trung vào: phạm vi (gì nằm trong, gì nằm ngoài), thế nào là xong, ràng buộc (thời hạn, công cụ, định dạng, ngôn ngữ), ai dùng kết quả và dùng ở đâu, phần nào của yêu cầu còn mơ hồ.
3. Tránh câu có/không cụt và câu chung chung kiểu "còn gì nữa không".
4. Sau khi có trả lời, tóm tắt thành khối chốt và chờ xác nhận:

```
Công việc: <1-2 câu>
Kết quả mục tiêu: <3-5 ý đo được>
Ràng buộc: <nếu có>
Xong nghĩa là: <điều kiện kết thúc>
Giả định của tôi: <ghi rõ mọi chỗ tự điền>
```

Nếu người dùng bảo "cứ làm đi", vẫn hỏi tối thiểu hai điều: phạm vi và tiêu chí xong; phần còn lại ghi là giả định rồi làm.

## Bước 2. Nghiên cứu (tự chạy)

Mục đích: không chọn cách làm đầu tiên nghĩ ra. Đây là bước cần suy nghĩ sâu nhất.

**2a. Kiểm kê tài nguyên có sẵn.** Trước khi nghĩ cách làm, liệt kê nhanh những gì đang dùng được: skill đã cài (ưu tiên skill riêng của dự án nếu trùng lĩnh vực), công cụ của nền tảng, kết nối ngoài (tài liệu, bảng tính, kho mã, cơ sở dữ liệu), và tài liệu người dùng đưa. Ghi lại: cái nào sẽ dùng ở bước nào, phần nào phải tự làm mới. Mục đích là khỏi viết lại thứ đã có sẵn.

**2b. Nghĩ trước khi tìm.** Trả lời ngắn: đây là loại việc gì, đã từng giải dạng tương tự chưa, yêu cầu có giả định ngầm nào không. Viết 3 đến 5 câu hỏi cần trả lời trước khi chọn cách làm.

**2c. Chọn nguồn.** Mỗi câu hỏi chọn một nguồn:

| Nguồn | Dùng khi |
|---|---|
| Kiến thức sẵn có | Lĩnh vực phổ biến, mẫu đã định hình |
| Tìm trên web | Lĩnh vực mới, cần dữ kiện cập nhật (phiên bản, giá, số liệu), cần kiểm tra giả định. Dùng công cụ tìm và đọc web của nền tảng; nếu không có, nhờ người dùng dán nội dung |
| Đọc tài liệu người dùng đưa | Việc dựa trên dữ liệu hoặc bản mô tả của chính họ |
| Xem mã nguồn hiện có | Việc lập trình: tìm mẫu đã dùng trong dự án trước khi viết mới |

Nghiên cứu sâu hơn (nhiều nguồn, đối chiếu) chỉ khi đạt từ 2 trong 4 dấu hiệu: có trường phái đối nghịch chưa ngã ngũ; cần số liệu kiểm chứng được; lĩnh vực đổi nhanh hơn kiến thức sẵn có; vòng đầu còn từ 3 chỗ trống quan trọng. Khi đạt, dừng hỏi người dùng muốn bản nhẹ hay bản đầy đủ và mất bao lâu. Đã đi đường sâu thì không chạy thêm tìm kiếm thường.

**2d. Skill hỗ trợ có điều kiện.** Chỉ gọi khi thật sự thêm giá trị, nếu đã cài; nếu chưa thì làm tại chỗ:
- Việc là phân tích nguyên nhân ("vì sao", vấn đề lặp lại, nhiều bên liên quan): dùng skill tư duy hệ thống, lấy kết quả làm đầu vào.
- Việc chỉ là tạo sản phẩm rõ ràng (viết tài liệu, dựng tính năng, tra dữ liệu): không gọi, đi thẳng.

**2e. Tổng hợp và chọn.** Đề xuất 2 đến 3 cách làm, so theo độ khó, thời gian, độ tin cậy, khả năng tái sử dụng. Tự chọn một cách kèm lý do một hai câu và rủi ro chính. Chỉ hỏi người dùng khi các cách ngang rủi ro.

## Bước 3. Lập kế hoạch (dừng)

Biến cách làm thành hợp đồng cụ thể, cho người dùng xem trước khi làm. Với mỗi bước:

```
Bước N: <tên ngắn>
- Đầu vào: <dữ liệu, điều kiện>
- Việc làm: <cụ thể>
- Skill/công cụ dự kiến: <lấy từ bản kiểm kê ở 2a, hoặc "không cần">
- Đầu ra: <sản phẩm đo được>
```

Quy tắc: mỗi bước nhỏ đến mức xong là có một sản phẩm rõ; không quá 7 đến 10 bước (nhiều hơn thì gom nhóm hoặc tách việc con); bước rủi ro kèm phương án dự phòng một dòng; chỉ ghi skill và công cụ thật sự tồn tại. Skill/công cụ là gợi ý, khi làm có thể đổi nếu thấy hợp hơn.

Trình kế hoạch và chờ người dùng duyệt hoặc sửa. Nếu nền tảng có chế độ lập kế hoạch chỉ-đọc thì dùng, nếu không thì chỉ trình bày bằng lời.

**Sau khi được duyệt, ghi kế hoạch ra một file kế hoạch dạng checkbox**, bắt buộc. Mỗi bước một dòng `- [ ] Bước N: <tên>`, Đầu vào/Việc làm/Đầu ra thụt vào dưới. Đặt trong thư mục làm việc (ví dụ thư mục tài liệu của dự án); không ghi đè file cũ, đặt tên mới nếu trùng. Lý do: nội dung trò chuyện có thể bị nén gọn giữa chừng và mất sạch, còn file kế hoạch thì còn. Mẫu file nằm ở `references/plan-and-report-templates.md`.

## Bước 4. Thực thi (tự chạy)

**4.0 Khởi động.** Đọc lại file kế hoạch. Tạo danh sách việc tương ứng nếu nền tảng có công cụ theo dõi, mỗi lúc chỉ một việc đang làm.

**4.1 Làm từng bước.** Giữ cấu trúc đã duyệt: không tự thêm, bớt hay đổi thứ tự bước. Còn lại linh hoạt: được dùng skill hoặc công cụ phù hợp hơn dự kiến, ghi một dòng nói đã đổi gì. Làm xong bước nào thì **tick `[x]` ngay trong file kế hoạch** (không để dồn lại cuối), rồi ghi một dòng tiến độ `[Bước 2/5] xong, đầu ra: ...`.

**4.2 Tăng chất lượng có điều kiện** (nếu đã cài thì dùng, không thì tự làm; không cần hỏi người dùng):

| Tình huống | Làm gì |
|---|---|
| Viết tính năng hoặc sửa lỗi code | Viết kiểm thử trước, rồi mới viết phần cài đặt |
| Cần dữ liệu từ hệ thống ngoài | Dùng kết nối có sẵn thay vì nhờ người dùng chép tay |
| Một bước lỗi, thử lại 2 lần vẫn lỗi | Dừng đoán mò, đi tìm nguyên nhân gốc theo quy trình gỡ lỗi |
| Sinh code có tác dụng phụ (tệp mới, đường dẫn API, lược đồ dữ liệu, xác thực) | Rà soát bảo mật trước khi kiểm chứng |
| 3 việc độc lập trở lên | Chạy song song nếu nền tảng cho phép |

**4.3 Sau khi ngữ cảnh bị nén gọn, hoặc khi mở lại một phiên làm việc mới:** việc đầu tiên là đọc lại file kế hoạch, xác định đang ở bước nào, rồi chạy `scripts/context-recovery.py <file-ke-hoach>` để in các mục chưa tick (cần Python; không có thì tự đọc file bằng mắt). Kế hoạch đã duyệt là nguồn sự thật: không tự đổi phạm vi sau khi mất ngữ cảnh.

**4.4 Dừng xin phép** (bất kể kế hoạch đã duyệt) khi sắp:

| Tình huống | Hành động |
|---|---|
| Hành động khó hoàn tác: xóa hàng loạt, ghi đè file đang có thay đổi chưa lưu, đẩy ép lên kho mã, xóa dữ liệu, gửi tin ra ngoài (email, chat, bình luận), sửa quy trình tự động, chi tiền | Dừng, nói rõ sẽ làm gì, chờ đồng ý |
| Phát hiện kế hoạch đã duyệt sai hướng | Dừng, mô tả điều mới thấy, quay lại bước 3 sửa kế hoạch |
| Sắp tạo file hoặc thư mục không có trong kế hoạch | Dừng, nói lý do, xin xác nhận |

Luật xét theo hành động chứ không theo ai gọi: đọc, tìm, phân tích, rà soát thì không cần xin; ghi file có trong kế hoạch thì không cần xin; ghi file ngoài kế hoạch, hoặc lệnh phá hủy, hoặc gửi ra ngoài thì phải xin, kể cả khi do một skill được gọi tự ghi.

Gặp lỗi thường (không thuộc ba tình huống trên): thử lại tối đa 2 lần theo cách khác, rồi tìm nguyên nhân gốc, rồi sửa kế hoạch ở bước 3. Chỉ báo người dùng khi đã thử hết khả năng.

## Bước 5a. Kiểm chứng kết quả (dừng)

Tự chấm khắt khe, dựa trên bằng chứng chạy thật, không dựa vào cảm giác.

1. Nếu có lệnh kiểm chạy được (kiểm thử, build, lint, kiểm tra kiểu): chạy và ghi lại kết quả thật trước khi tuyên bố đạt. Nếu có code mới sinh ra, nhờ một lượt rà soát độc lập (skill rà soát nếu có, không thì tự đọc lại với con mắt người lạ).
2. Với từng tiêu chí ở bước 1, đánh dấu: đạt đầy đủ (kèm bằng chứng: đường dẫn file, kết quả lệnh, liên kết), đạt một phần (nêu chỗ thiếu), chưa đạt (nêu nguyên nhân gốc).
3. Có chỗ chưa đạt: tự sửa kế hoạch và làm lại phần lỗi, tối đa 3 vòng; sau đó báo người dùng kèm phân tích.
4. Đạt hết: trình báo cáo kiểm chứng (mẫu ở file tham chiếu) và hỏi: tinh chỉnh thêm hay xác nhận hoàn thành?

Việc không có lệnh kiểm (tài liệu, phân tích, bài trình bày): đối chiếu trực tiếp với mục tiêu là đủ, nhưng vẫn phải kèm bằng chứng (đoạn nào, số liệu nào đáp ứng tiêu chí nào).

## Bước 5b. Quyết định đóng gói (dừng)

Chỉ chạy sau khi người dùng xác nhận hoàn thành ở 5a.

1. Âm thầm, không hỏi: nếu có công cụ tìm skill thì tìm skill tương tự bằng 2 đến 4 từ khóa lấy từ tên việc.
2. Hỏi đúng một câu, kèm luôn kết quả tìm: việc này là **(a) làm một lần**, kết thúc tại đây, hay **(b) việc lặp lại**, đóng gói thành skill để dùng lại? Nêu skill tương tự tìm thấy, hoặc "chưa thấy skill nào tương tự".

Tìm trước rồi mới hỏi, để người dùng quyết khi đã đủ thông tin.

## Bước 6. Đóng gói thành skill (chỉ khi chọn 5b-b)

1. **Soạn bản tóm tắt** gồm: tên skill (chữ thường, gạch nối, nói đúng việc cốt lõi); mục tiêu cốt lõi (từ bước 1); cách làm đã chốt (bước 2); kế hoạch chuẩn (bước 3, đây sẽ là phần hướng dẫn); ít nhất một ví dụ đầu vào rồi đầu ra thật từ bước 4; tài nguyên đi kèm (script, mẫu) nếu bước 4 sinh ra thứ dùng lại được.
2. **Dừng chốt tên và nơi đặt:** nêu tên, nơi đặt (dùng chung cho mọi dự án hay riêng dự án này), ngôn ngữ phần thân; chờ xác nhận. Đổi tên sau khi tạo file thì mất công sửa nhiều chỗ.
3. **Tạo skill.** Dùng skill thiết kế skill nếu đã cài; nếu không, tự viết: một thư mục mang đúng tên skill, trong đó `SKILL.md` có phần đầu chỉ gồm `name` (khớp tên thư mục) và `description` (nói skill làm gì và khi nào dùng, kèm cụm từ người dùng hay nói), thân ngắn gọn; chi tiết dài tách sang thư mục tham chiếu. Chỉ đóng gói script nếu script đó dùng lại được.
4. **Kiểm tra:** file `SKILL.md` đã tồn tại, phần đầu hợp lệ, tên khớp thư mục. Tóm tắt lại đường dẫn và các file con. Nếu có skill ghi lại lý do thiết kế thì dùng; nếu không, kèm một file ghi ngắn: vì sao tồn tại, đánh đổi đã chấp nhận, khi nào xem lại.

Không đè lên skill cùng tên đã có; chọn tên khác hoặc hỏi người dùng.

## Quy tắc đầu ra

- Kết thúc bằng một bước tiếp theo cụ thể.
- Ghi rõ giả định và chỗ nào là mốc tham khảo.
- Lưu sản phẩm thành tài liệu mới (Google Docs/Sheets/Slides mới) nếu có kết nối; không thì trả trong cuộc trò chuyện. Không ghi đè file có sẵn.
- Không gửi, đăng, chi tiền hay thay đổi gì ngoài cuộc trò chuyện khi chưa có đồng ý của người dùng.
- Muốn sơ đồ luồng công việc: đề nghị vẽ bằng skill `visual-thinking` nếu đã cài, không thì bảng chữ.

## Chuẩn chất lượng

- Mục tiêu và tiêu chí xong được viết ra ở bước 1 và đo được.
- Có kiểm kê tài nguyên trước khi tự làm lại thứ đã có.
- Kế hoạch được duyệt và có file checkbox, được tick trong lúc làm.
- Mọi lời "đã xong" đều có bằng chứng đi kèm.
- Mọi điểm dừng ở bảng trên đều được tôn trọng; không dừng thừa giữa các điểm đó.
- Mọi giả định đều được ghi tên.

## Tham chiếu

- `references/plan-and-report-templates.md`: mẫu khối chốt mục tiêu, file kế hoạch, báo cáo kiểm chứng, bản tóm tắt đóng gói.
- `references/worked-example.md`: một ví dụ giả định chạy hết sáu bước.
- `scripts/context-recovery.py`: in các mục chưa tick của file kế hoạch.
