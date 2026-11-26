---
name: video-script-vn
description: Write Vietnamese video script drafts in three modes - SHORTS (up to about 60 seconds for short-video platforms), LONG (long-form videos, with optional fact-check variant) and REMAKE (study a reference video's structure, then generate a brand-new idea in the same niche and persona with the same viral structure, never copying its wording or story). Output is a shot list with voice-over, on-screen text and a call to action. Drafts only. Use for "write a TikTok script", "script video dài", "làm lại theo cấu trúc video này". Tiếng Việt - viết bản nháp kịch bản video tiếng Việt theo ba chế độ SHORTS, LONG, REMAKE; đầu ra gồm danh sách cảnh quay, lời đọc, chữ trên màn hình, lời kêu gọi. Dùng khi nói "viết kịch bản TikTok, Reels, Shorts", "kịch bản YouTube dài", "giải mã khung xương video này rồi nghĩ ý mới".
---

# Viết kịch bản video tiếng Việt

## Vai trò

Skill này viết **bản nháp** kịch bản video tiếng Việt. Người dùng duyệt, sửa, quay và đăng. Skill không đăng, không gửi, không chi tiền, không đổi gì ngoài cuộc trò chuyện.

Ba chế độ:
- **SHORTS**: video đến khoảng 60 giây cho nền tảng video ngắn.
- **LONG**: video dài (vài phút đến vài chục phút), ý tưởng độc lập bám ngách và khán giả.
- **REMAKE**: học khung xương của một video tham chiếu, rồi nghĩ **ý mới** trong cùng ngách và cùng chân dung khán giả, giữ cấu trúc đã chạy tốt, không lặp câu chữ hay câu chuyện của video tham chiếu.

## Khi không dùng skill này

- Chỉ muốn hiểu lý thuyết (hook, công thức 7 điểm, ma trận ý tưởng): dùng `tui-kich-ban` nếu đã cài, không thì trả lời ngắn tại chỗ.
- Chọn ngách cho kênh: `niche-finder` nếu đã cài.
- Lời bán hàng, email, trang đích: skill copywriting.
- Prompt cho công cụ dựng video AI: skill prompt dựng video nếu đã cài, không thì ngoài phạm vi.
- Kế hoạch từ khóa và chủ đề cho cả kênh: skill SEO nội dung.

## Bối cảnh thương hiệu (đọc trước)

Nếu khách có `brand-profile.md` (tên, định vị, khán giả, giọng điệu, sản phẩm, giới hạn), đọc trước và không hỏi lại điều đã có. Lấy từ đó: chân dung khán giả, xưng hô, giọng điệu, điều không được nói. Chưa có thì hỏi một lần theo phần "Đầu vào" dưới đây, mỗi câu kèm đáp án mặc định.

## Chọn chế độ

1. Người dùng đưa đường dẫn hoặc bản chép lời của một video tham chiếu cụ thể: **REMAKE**.
2. Thời lượng đích khoảng 60 giây trở xuống: **SHORTS**.
3. Video dài, không bám video cụ thể: **LONG**.
4. Còn mơ hồ: hỏi đúng một câu: "Bạn cần (a) video ngắn dưới 60 giây, (b) video dài ý tưởng mới trong ngách, hay (c) làm lại theo cấu trúc một video tham chiếu?"

Nếu người dùng nói **express**, bỏ qua câu hỏi khi đã đủ đầu vào và viết luôn. Nếu nói **guided** (mặc định), hỏi các câu thiếu rồi mới viết. Nếu nói **decode**, trong REMAKE chỉ giải mã khung xương và dừng, không viết kịch bản.

Đọc video tham chiếu: dùng công cụ đọc web của nền tảng nếu có, không thì nhờ người dùng dán bản chép lời cùng mốc thời gian.

## Đầu vào cần có

| Chế độ | Hỏi những gì (mỗi câu có mặc định) |
|---|---|
| SHORTS | Chủ đề hoặc sản phẩm. Khán giả. Nền tảng. Phong cách kênh (mặc định: thân thiện). Mục tiêu (mặc định: kéo người lạ vào) |
| LONG | Ngách. Khán giả. Thời lượng (mặc định: 8 đến 10 phút). Biến thể: sáng tạo, có kiểm chứng, từ bài viết, tin tức. Có câu chuyện thật nào dùng được không |
| REMAKE | Video tham chiếu (đường dẫn hoặc bản chép lời). Khán giả đích. Thời lượng đích. Nội dung hư cấu hay có thật |

Tốc độ đọc tham khảo: khoảng 150 đến 170 từ mỗi phút nói tiếng Việt. Dùng để đổi thời lượng sang số từ, rồi kiểm lại bằng giọng đọc của người dùng.

## Khung hook (dùng cho mọi chế độ)

**Hook là câu để lại khoảng trống thông tin**, không phải câu hay. Sau câu đầu người xem phải tự hỏi "rồi sao?" và thấy liên quan đến mình.

Ba lớp: câu mở tạo khoảng trống, lớp xác nhận "đây là chuyện của bạn", lớp cam kết giá trị sẽ giao ở cuối.

Tám loại hook: mâu thuẫn, con số bất ngờ, bí mật nội bộ, kết quả trước quy trình, câu hỏi gọi đích danh, chuyện đang dở, phá khuôn so sánh, cảnh báo. Chọn theo mục tiêu: kéo người lạ thì mâu thuẫn, con số, cảnh báo. Giữ người đã biết kênh thì bí mật nội bộ, chuyện đang dở. Bán hoặc kêu gọi thì kết quả trước quy trình, câu hỏi gọi đích danh.

Lỗi hook thường gặp:
1. Câu hỏi quá dễ đoán đáp án.
2. Hứa quá lớn so với thứ video giao.
3. Chung chung, không gọi đúng ngành, đúng người.
4. Quá dài: video ngắn thì một câu, vài giây.
5. Mở bằng lời chào hoặc "hôm nay mình sẽ chia sẻ".
6. Không thử: đọc cho một người ngoài ngành, hỏi họ có muốn nghe tiếp không và vì sao.

Mỗi kịch bản đưa **hai hook thay thế** để người dùng chọn.

## Chế độ SHORTS

Quy trình:
1. **Chân dung**: một đến hai nhóm khán giả. Ngữ cảnh xem (lướt giữa giờ, trước ngủ), nỗi đau chính, điều họ tự nói với mình.
2. **Một ý**: sinh khoảng mười ý, mỗi ý kèm hook nháp. Chọn một ý đáng làm nhất theo ba tiêu chí: đi ngược điều số đông tin, chạm đúng nỗi đau, có bằng chứng.
3. **Viết** theo nhịp mốc tham khảo (kiểm lại với dữ liệu giữ chân của kênh): vài giây đầu là hook, đến khoảng giây 15 có một chỗ bẻ hoặc chuyển ý, phần thân một chứng minh duy nhất (một chuyện hoặc một ví dụ), cuối là một hành động làm được ngay và lời kêu gọi.
4. **Tín hiệu nhận diện kênh**: một câu, cử chỉ hoặc vật lặp lại giữa các video.
5. **Hậu kiểm**: xem danh sách kiểm cuối tài liệu.

Một video một ý. Không nhồi ba mẹo vào một video 45 giây.

## Chế độ LONG

Quy trình:
1. **Ngách và chân dung**: chốt ngách, nhóm khán giả, nỗi đau ba tầng (bề mặt, hệ quả, danh tính).
2. **Sinh ý**: dùng ma trận sáu trục (ai, cái gì, vì sao, làm thế nào, nếu thì sao, so với cái gì) để ra 10 đến 20 ý. Mỗi ý có hook nháp. Ý phải đứng được độc lập, không bám một video có sẵn. Cho người dùng chọn một.
3. **Cấu trúc**: dùng công thức 7 điểm (Hook, Setup, Question, Twist, Build, Reveal, Payoff), viết Twist trước. Build chứng minh bằng ba tầng: số liệu hoặc cơ chế, chuyện thật, nguồn đáng tin.
4. **Luân phiên kiểu triển khai** giữa các phần (nặng số liệu, nặng chuyện, đi ngược, hướng dẫn) để người xem không mỏi theo một nhịp. Chen một điểm gây giật mình nhẹ khoảng mỗi một đến hai phút (mốc tham khảo).
5. **Viết** hook dài vừa phải (có thể 30 đến 60 giây với video dài nhưng phải có đà), thân bài, kết.
6. **Gói đăng**: ba phương án tiêu đề, mô tả ngắn, thẻ, ba ý tưởng ảnh bìa.

Biến thể:
- **Sáng tạo**: nội dung phổ thông, giải trí, đời sống. Không cần nguồn cứng.
- **Có kiểm chứng**: tài chính, sức khỏe, lịch sử, khoa học. Mỗi dữ kiện ghi nguồn, nên có ít nhất hai nguồn độc lập. Chưa có nguồn thì để nguyên chữ **[CẦN KIỂM CHỨNG]**, không tự điền. Không đưa lời khuyên y khoa, pháp lý hay đầu tư cá nhân hóa.
- **Từ bài viết hoặc ghi chú**: biến tư liệu thô của chính người dùng thành kịch bản, không chép nguyên văn nguồn bên thứ ba.
- **Tin tức**: hoặc đào sâu một sự kiện (bối cảnh, diễn biến, phân tích nhiều góc, nhìn tiếp theo), hoặc tổng hợp ba đến năm tin trong ngày với một mạch nối chung. Mọi tin phải có nguồn do người dùng cung cấp hoặc đọc được.

## Chế độ REMAKE

Mục tiêu: lấy **bài học cấu trúc** từ một video đã chạy tốt, rồi tạo ra ý và nội dung hoàn toàn mới cho cùng ngách và cùng chân dung khán giả.

Quy trình:
1. **Đọc video tham chiếu** (bản chép lời có mốc thời gian).
2. **Giải mã khung xương**, ghi vào bảng: cấu trúc các phần, loại hook và độ dài, nhịp đổi ý, đường cường độ cảm xúc (đỉnh, đáy), cách giữ chân (vòng lặp mở dở, chỗ giật mình, kết lửng), giọng và độ khó từ vựng. Liệt kê riêng những **cụm từ, ẩn dụ và chi tiết đặc trưng của video gốc** vào danh sách cấm dùng.
3. **Nghĩ ý mới**: không lấy chủ đề, cốt truyện, nhân vật, ví dụ của video gốc. Sinh ý từ nỗi đau của chân dung khán giả bằng ma trận sáu trục, chọn ý cùng ngách nhưng khác hẳn nội dung. Cho người dùng chọn.
4. **Dựng outline mới** trên khung xương: cùng số phần, cùng vai trò mỗi phần, nhưng lệch nhịp một nấc ở vài chỗ (đoạn ngắn hơn, dài hơn) và đổi góc kể nếu hợp (ví dụ ngôi thứ nhất sang ngôi thứ ba).
5. **Thêm hai tầng giá trị** mà video gốc không có: kiến thức có nguồn, và chuyện hoặc góc nhìn riêng.
6. **Viết hook mới** theo loại hook của gốc nhưng nội dung khác, và cải thiện một điểm yếu bạn thấy ở hook gốc.
7. **Viết lời đọc** cùng độ mạnh cảm xúc, không dùng bất cứ thứ gì trong danh sách cấm.
8. **Rà an toàn** (bên dưới) rồi giao bản nháp.

### Rào chắn bắt buộc cho REMAKE

1. **Không sao chép**: không câu chữ, không cốt truyện, không nhân vật, không ví dụ, không ẩn dụ tự đặt, không thuật ngữ riêng của video gốc. Câu nào giống quá hai ba chữ liền với gốc thì viết lại.
2. **Đổi hết yếu tố ngầm**: tên, quan hệ, bối cảnh, thời điểm, ví dụ cụ thể, xung đột. Chỉ giữ được kiểu nhân vật chung.
3. **Không bịa**: không số liệu, nguồn, trích dẫn, lời chứng thực, bằng cấp, kết quả hay trải nghiệm cá nhân không có thật. Dữ kiện chưa kiểm chứng ghi **[CẦN KIỂM CHỨNG]**. Chuyện cá nhân dùng chỗ trống để người dùng điền chuyện thật, không viết hộ như thể đã xảy ra.
4. **Không giả danh**: không viết như thể là tác giả video gốc hoặc nhắc tên họ để mượn uy tín.
5. **Nhạc, lời bài hát, thương hiệu, người thật**: không đưa vào nếu chưa có quyền. Không nói xấu cá nhân hoặc tổ chức có thật.
6. **Nhắc kiểm tra chính sách nền tảng** về nội dung dùng lại và nội dung tạo bằng AI, vì kết quả không ai đảm bảo được. Báo rõ đây là bản nháp cần người dùng duyệt.
7. Khi không chắc một chỗ có quá giống gốc hay không, nói rõ và đề nghị viết lại, không im lặng giao.

## Định dạng đầu ra

Dùng cho cả ba chế độ, rút gọn nếu là video ngắn.

```
# BẢN NHÁP kịch bản: [Tiêu đề ý]

## Thông tin
- Chế độ: [SHORTS / LONG / REMAKE]
- Nền tảng và thời lượng: [...]
- Khán giả: [một dòng]
- Loại hook: [loại và lý do]
- Giả định đã dùng: [liệt kê]

## Danh sách cảnh
| # | Thời gian | Hình (cảnh quay) | Lời đọc | Chữ trên màn hình | Ghi chú |
|---|---|---|---|---|---|
| 1 | 0-3 giây | [góc quay, hành động, đạo cụ] | [câu hook] | [chữ ngắn] | [nhịp, âm thanh] |

## Hook thay thế
1. [...]
2. [...]

## Lời kêu gọi (CTA)
[Một việc cụ thể người xem làm được. Với video dài có thể thêm cầu nối sang video kế]

## Tín hiệu nhận diện kênh (video ngắn)
[Câu, cử chỉ hoặc vật lặp lại]

## Gói đăng
- Tiêu đề (3 phương án), mô tả ngắn, thẻ hoặc hashtag, ý tưởng ảnh bìa

## Cần người dùng điền hoặc kiểm chứng
- [Các chỗ [CẦN KIỂM CHỨNG], chuyện thật cần điền, nhạc và hình cần quyền]

## Bước tiếp theo
[Một việc cụ thể: duyệt hook, gửi chuyện thật, quay thử thước đầu]
```

Với REMAKE, thêm ở đầu một mục "Khung xương đã giải mã" (bảng ngắn) và ở cuối mục "Rà soát không sao chép" (ô kiểm: đã đổi tên, bối cảnh, quan hệ, ví dụ, không còn cụm từ trong danh sách cấm). Với LONG biến thể có kiểm chứng, thêm bảng dữ kiện: dữ kiện, nguồn thứ nhất, nguồn thứ hai, trạng thái.

## Giọng văn của lời đọc

- Viết để đọc thành tiếng, như đang kể cho một người bạn. Câu ngắn dài xen kẽ theo nhịp cảm xúc, không năm câu liền cùng độ dài.
- Dùng xưng hô người dùng chọn (hoặc theo brand-profile.md). Không có thì mặc định "mình" và "bạn".
- Tả hành động và cảm giác cơ thể thay vì gọi tên cảm xúc.
- Không mở bằng "Xin chào các bạn", "hôm nay mình sẽ chia sẻ", "bạn có biết rằng". Không dùng gạch ngang dài hay chấm phẩy trong lời đọc.
- Không để lộ cấu trúc: lời đọc không có số thứ tự điểm hay tiêu đề.
- Chữ trên màn hình ngắn, một ý, không lặp nguyên lời đọc.
- Một video, một ý, một hành động.

## Danh sách kiểm trước khi giao

1. Hook chốt được người xem trong vài giây đầu và không hứa quá thật.
2. Một ý duy nhất, không nhồi.
3. Mỗi dữ kiện có nguồn hoặc nhãn **[CẦN KIỂM CHỨNG]**.
4. Lời đọc đọc to lên nghe tự nhiên, thời lượng khớp số từ.
5. Có CTA cụ thể, không chỉ "nhớ đăng ký".
6. REMAKE: qua đủ bảy rào chắn, không câu nào lặp gốc.
7. Có hai hook thay thế, danh sách cần điền, và bước tiếp theo.
8. Mốc con số nào cũng ghi "mốc tham khảo".

## Quy tắc đầu ra

- Ghi rõ giả định (khán giả, nền tảng, thời lượng, giọng điệu).
- Luôn đánh dấu là bản nháp. Không đăng, gửi, chi tiền hay đổi gì ngoài cuộc trò chuyện khi chưa được đồng ý.
- Lưu thành Google Docs hoặc Google Sheets mới nếu có kết nối, không thì trả ngay trong cuộc trò chuyện. Không ghi đè tệp có sẵn.
- Kết bằng một bước tiếp theo cụ thể.
- Nếu hữu ích, đề nghị vẽ sơ đồ khung xương qua skill `visual-thinking` nếu đã cài, không thì dùng bảng chữ.

## Liên quan (gợi ý mềm, không bắt buộc)

`tui-kich-ban` (lý thuyết hook, công thức 7 điểm, ma trận ý tưởng, nỗi đau), `niche-finder` (chọn ngách), `brand-architect` (tạo brand-profile.md), `visual-thinking` (sơ đồ). Chưa cài thì làm bước đó tại chỗ theo các mục ở trên.
