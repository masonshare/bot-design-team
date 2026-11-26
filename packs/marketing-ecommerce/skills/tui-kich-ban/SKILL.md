---
name: tui-kich-ban
description: Foundation library for writing Vietnamese video scripts - a seven-point script formula, finding audience pain points, an idea matrix, storytelling structure, hooks, question finding and a methodology overview. It answers theory questions and never writes the script itself; execution is handed off to video-script-vn. Use for "what is a hook", "seven-point formula", "idea matrix", "find audience pain points", "storytelling for video". Tiếng Việt - kho kiến thức nền cho kịch bản video tiếng Việt - công thức 7 điểm, tìm nỗi đau khán giả, ma trận ý tưởng, cấu trúc kể chuyện, hook, đặt câu hỏi đào sâu. Dùng khi hỏi "hook là gì", "công thức 7 điểm", "ma trận ý tưởng", "tìm nỗi đau khán giả", "storytelling cho video"; khi cần viết kịch bản thật thì chuyển sang video-script-vn.
---

# Kho kiến thức kịch bản video

## Skill này làm gì

Đây là thư viện lý thuyết, không phải máy viết kịch bản. Skill làm hai việc:

1. **Tra cứu**: trả lời câu hỏi về hook, cấu trúc kịch bản, tìm ý tưởng, tìm nỗi đau khán giả, kể chuyện. Mỗi câu trả lời gọn, có ví dụ ngắn và một bước tiếp theo.
2. **Chuyển giao**: khi người dùng đã muốn một kịch bản cụ thể, hand off to video-script-vn (nếu chưa cài thì tự viết tại chỗ theo các nguyên tắc dưới đây, nhưng nói rõ đây là bản nháp).

Không tự viết kịch bản hoàn chỉnh trong chế độ tra cứu. Không tự sinh prompt dựng video AI.

## Khi không dùng skill này

- Cần kịch bản thật cho video ngắn, video dài hoặc bản làm lại theo cấu trúc video tham chiếu: dùng `video-script-vn`.
- Cần prompt cho công cụ dựng video AI: dùng skill chuyên về prompt dựng video nếu đã cài, không thì nói rõ nằm ngoài phạm vi.
- Cần lời bán hàng, trang đích, email: dùng skill copywriting.
- Cần kế hoạch chủ đề và từ khóa cho cả kênh: dùng skill SEO nội dung.
- Cần chọn ngách cho kênh: dùng `niche-finder` nếu đã cài.

## Bối cảnh thương hiệu

Nếu khách có `brand-profile.md` (tên, định vị, khán giả, giọng điệu, sản phẩm, giới hạn), đọc trước và không hỏi lại những gì đã có. Dùng nó để chọn ví dụ cùng ngành với khách. Nếu chưa có và người dùng cần ví dụ đúng ngành, hỏi một lần: ngành gì, khán giả là ai, giọng điệu ra sao. Mỗi câu kèm đáp án mặc định.

## Cách trả lời một câu tra cứu

1. Xác định chủ đề rơi vào mục nào ở bảng "Bản đồ kiến thức" dưới đây.
2. Đọc đúng một file tham chiếu (tối đa hai). Không nạp cả thư viện.
3. Trả lời bằng định nghĩa ngắn, cách làm theo bước, một ví dụ, một lỗi hay gặp.
4. Kết bằng câu hỏi nhẹ: "Bạn muốn áp dụng cho chủ đề nào?" và nếu sẵn sàng thì đề nghị chuyển sang `video-script-vn`.
5. Nếu yêu cầu mơ hồ, hỏi đúng một câu phân loại: bạn cần (a) hiểu lý thuyết, (b) viết kịch bản, hay (c) dựng video bằng AI?

## Bản đồ kiến thức

| Người dùng hỏi về | File | Một dòng tóm tắt |
|---|---|---|
| Công thức 7 điểm, dàn ý video dài | `references/cong-thuc-7-diem.md` | Bảy bước tâm lý, viết phần bước ngoặt trước |
| Hook, câu mở đầu, hài hước trong hook, đặt câu hỏi đào sâu | `references/hook-va-cau-hoi.md` | Hook ba lớp, tám loại, lỗi thường gặp, câu hỏi đáng xem |
| Tìm ý tưởng, ma trận ý tưởng, nỗi đau khán giả | `references/y-tuong-va-noi-dau.md` | Một video một ý, sáu trục ý tưởng, ba tầng nỗi đau |
| Kể chuyện, tổng quan phương pháp, làm lại theo cấu trúc, cắt video dài thành ngắn | `references/ke-chuyen-va-phuong-phap.md` | Bốn giai đoạn kể chuyện, giải mã khung xương, hai tầng giá trị |

## Lõi kiến thức (đủ dùng khi không nạp file)

### Ba nguyên tắc nền

1. **Hook không phải câu hay, hook là câu để lại một khoảng trống thông tin.** Sau câu mở đầu, người xem phải tự hỏi "rồi sao nữa?" và thấy câu trả lời liên quan đến mình.
2. **Học khung xương, thay phần ruột.** Khung xương gồm nhịp, thứ tự ý, đường cong cảm xúc và cách giữ chân. Phần ruột gồm bối cảnh, nhân vật, ví dụ, câu chữ. Học cái đầu, thay hết cái sau.
3. **Bám ngách và nỗi đau, không bám một video cụ thể.** Ý tưởng sinh từ khán giả và vấn đề của họ thì kênh tự đứng được. Ý tưởng lấy từ một video có sẵn thì kênh chỉ là bản sao.

### Công thức 7 điểm (tóm tắt)

Thứ tự trên màn hình: Hook, Setup, Question, Twist, Build, Reveal, Payoff. Thứ tự viết: **Twist trước**, rồi dựng sáu điểm còn lại quanh nó.

| Điểm | Việc phải làm |
|---|---|
| Hook | Một câu chạm vào điều người xem tin hoặc sợ |
| Setup | Gọi đúng người xem, nêu điều họ đang làm đúng, đặt cái giá của việc bỏ qua |
| Question | Một câu hỏi họ không đoán được đáp án trong vài giây |
| Twist | Đảo một niềm tin phổ biến, có cơ sở, vừa bất ngờ vừa có lý |
| Build | Chứng minh bằng ba tầng: số liệu hoặc cơ chế, câu chuyện thật, nguồn đáng tin |
| Reveal | Trả lời cụ thể trước, nguyên lý rộng hơn sau |
| Payoff | Một thay đổi cách nhìn, cầu nối sang chủ đề kế, không chỉ "nhớ đăng ký" |

### Hook: ba lớp, tám loại

Ba lớp: câu mở tạo khoảng trống, lớp xác nhận "đây là về bạn", lớp cam kết giá trị ở cuối video.
Tám loại: mâu thuẫn, con số bất ngờ, bí mật nội bộ, kết quả trước quy trình, câu hỏi gọi đích danh, chuyện đang dở, phá khuôn so sánh, cảnh báo. Công thức điền chỗ trống nằm trong `references/hook-va-cau-hoi.md`.

### Ma trận ý tưởng: sáu trục

Cùng một chủ đề, hỏi sáu câu: Ai (đối tượng), Cái gì (tầng kiến thức), Vì sao (cảm xúc), Làm thế nào (quy trình), Nếu thì sao (tình huống giả định), So với cái gì (đối chiếu). Mỗi trục cho ra nhiều tiêu đề khác nhau, nên một chủ đề đủ nuôi cả tháng.

### Nỗi đau ba tầng

Tầng bề mặt (vấn đề nói ra được), tầng hệ quả (nó làm hỏng điều gì trong đời họ), tầng danh tính (họ nghĩ gì về bản thân vì chuyện đó). Hook chạm tầng sâu thì giữ người xem tốt hơn hook chỉ nêu vấn đề bề mặt.

### Kể chuyện: bốn giai đoạn

Hook (một khoảnh khắc lạ hoặc đau), Vấn đề (một cảnh cụ thể, không phải cả giai đoạn), Hành trình (có thất bại, bước ngoặt, kiến thức nằm trong tình huống), Bài học (một hai câu, người xem tự rút ra).

## Quy tắc chữ nghĩa cho mọi nội dung tạo ra từ thư viện

- Viết như nói chuyện, câu ngắn dài xen kẽ, không năm câu liền cùng độ dài.
- Không mở bằng lời chào chung chung hay "hôm nay mình sẽ chia sẻ về...".
- Không hứa hẹn quá mức trong hook. Hook là bản xem trước thật của video.
- Không bịa số liệu, nguồn, lời chứng thực. Chưa có thì đánh dấu cần kiểm chứng.
- Ví dụ trong thư viện là minh họa bịa ra, người dùng phải thay bằng dữ liệu và câu chuyện thật của họ.

## Chuyển giao

| Tín hiệu trong yêu cầu | Đi đâu |
|---|---|
| "viết kịch bản", "viết video TikTok, Reels, Shorts" | `video-script-vn`, chế độ SHORTS |
| "kịch bản video dài", "ý tưởng mới trong ngách cho kênh dài" | `video-script-vn`, chế độ LONG |
| "làm lại theo cấu trúc video này", "giải mã khung xương video tham chiếu" | `video-script-vn`, chế độ REMAKE |
| Prompt dựng video AI | Skill prompt dựng video nếu có, không thì ngoài phạm vi |
| Lời bán hàng, email, trang đích | Skill copywriting |

Khi chuyển giao, gửi kèm một khối ghi chú ngắn: chủ đề, khán giả, nền tảng, thời lượng, hook đã nghiêng về loại nào, nỗi đau đã tìm được. Người nhận không phải hỏi lại.

## Chất lượng

1. Trả lời đúng điều được hỏi, một file một lần, không đổ cả thư viện.
2. Có cách làm theo bước và một ví dụ, không chỉ định nghĩa.
3. Ví dụ đúng ngành của khách nếu đã biết.
4. Mốc con số nào cũng gắn nhãn "mốc tham khảo, kiểm lại với kênh của bạn".
5. Luôn kết bằng bước kế tiếp cụ thể.

## Quy tắc đầu ra

- Nêu rõ giả định đã dùng (ngành, khán giả, nền tảng).
- Nếu cần lưu, tạo Google Docs mới khi có kết nối, không thì trả ngay trong cuộc trò chuyện. Không ghi đè tệp có sẵn.
- Không đăng, gửi, chi tiền hay đổi gì ngoài cuộc trò chuyện khi chưa được đồng ý.
- Nếu hữu ích, đề nghị vẽ sơ đồ qua skill `visual-thinking` nếu đã cài, không thì dùng bảng chữ.

## Liên quan (gợi ý mềm, không bắt buộc)

`video-script-vn` (viết kịch bản), `niche-finder` (chọn ngách), `brand-architect` (tạo brand-profile.md), `visual-thinking` (sơ đồ). Chưa cài thì làm bước đó tại chỗ.
