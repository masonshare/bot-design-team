---
name: winning-business-model
description: Build or stress-test a business model for one venture around four questions (WHO, WHAT, HOW, HOW MUCH) and one value equation, then deliver a verdict (Go, Go to test, Refine, No-Go) and a one-page canvas plus decision memo. Default is automatic mode - the agent drafts everything and the user reacts at two decision points; say "coach mode" for step-by-step questions. Use for "build a business model", "is this model winning", "check product-market fit", "unit economics LTV CAC", "value proposition and pricing end to end". Tiếng Việt - xây hoặc kiểm tra mô hình kinh doanh theo 4 câu hỏi WHO WHAT HOW HOW MUCH và phương trình giá trị ("xây mô hình kinh doanh", "mô hình đã ổn chưa", "kiểm PMF", "LTV CAC", "chế độ coach").
---

# Winning Business Model (mô hình kinh doanh chiến thắng)

Một mô hình kinh doanh tốt trả lời được bốn câu hỏi và các câu trả lời không cãi nhau:

| Câu hỏi | Ý nghĩa | Sản phẩm đầu ra |
|---|---|---|
| WHO | Phục vụ đúng một nhóm khách nào, họ cần làm xong việc gì | Hồ sơ khách |
| WHAT | Giá trị gì, ròng hơn phương án thay thế ở đâu | Phương trình giá trị, lời hứa, sản phẩm |
| HOW | Làm thế nào trao giá trị đó ổn định, bằng năng lực nào | Hành trình khách, năng lực cốt lõi |
| HOW MUCH | Thu tiền thế nào, mỗi khách có lời không | Mô hình doanh thu, chi phí, unit economics |

Một phương trình xuyên suốt: **giá trị khách nhận = lợi ích - chi phí khách bỏ ra**, và **giá phải nằm trong hành lang giữa chi phí phục vụ và giá trị đó**. Mọi kiểm tra sau này quay về phương trình này.

## Hai chế độ

- **Tự động (mặc định).** Agent tự quét ngữ cảnh, tự tra cứu, tự soạn cả bốn trụ rồi chạy liền. Chỉ dừng ở **hai điểm quyết định**: (1) chọn phân khúc, (2) chốt verdict. Người dùng là người phán đoán, không phải người điền biểu mẫu.
- **Coach (khi người dùng nói "coach mode", "dạy tôi từng bước", "hỏi tôi trước").** Mỗi trụ bắt đầu bằng một câu hỏi để người dùng tự trả lời, agent chỉ soạn sau khi nghe. Nếu người dùng bí, đưa 2 đến 3 gợi ý gắn [assumption] để họ phản ứng, không chốt thay. Dừng chờ xác nhận sau từng trụ.

## Khi không dùng skill này

- Chỉ cần chọn một ngách từ nhiều cơ hội đã có: dùng `niche-finder` nếu đã cài.
- Chỉ cần quy mô thị trường, đối thủ, chân dung khách định lượng: dùng `market-researcher` nếu đã cài.
- Chỉ cần soi từng chặng phễu bán hàng: dùng `journey-mapper` nếu đã cài.
- Cần mô hình tài chính nhiều năm, nhiều kịch bản, gọi vốn: dùng `startup-financial-modeling` nếu đã cài.
- Chỉ cần một việc lẻ như riêng bảng giá hay riêng bản sắc thương hiệu: làm việc đó trực tiếp, không chạy cả bộ.

## Nhãn bằng chứng (bắt buộc ở mọi dòng quan trọng)

- **[data]**: người dùng xác nhận, hoặc có số liệu thật trong tài liệu họ đưa (doanh thu, khảo sát, hợp đồng, báo cáo bán hàng).
- **[assumption]**: agent suy ra, ước lượng hoặc lấy từ tra cứu bên ngoài, chưa được người dùng hay số liệu thật kiểm chứng. Ghi thêm nguồn ngắn nếu có.

Ở chế độ tự động, phần lớn nội dung sẽ là [assumption]. Đó là bình thường, miễn trung thực: không nâng [assumption] thành [data] chỉ vì nghe hợp lý. Mọi [assumption] quan trọng cuối cùng dồn vào danh sách "cần đo" trong memo.

## Bước 0: quét đầu vào

1. Quét theo thứ tự: hội thoại hiện tại, hồ sơ doanh nghiệp hoặc thương hiệu của khách (nếu họ giữ `brand-profile.md` hoặc tài liệu tương đương thì đọc trước và không hỏi lại điều đã có), các tài liệu người dùng chỉ vào (báo cáo bán hàng, bản kế hoạch, khảo sát).
2. Điền bảng đầu vào: venture, ngành, sản phẩm hoặc dịch vụ, nhóm khách đang nhắm, giai đoạn (ý tưởng, đang tìm độ khớp, đang mở rộng), số liệu đã có (giá, số khách, chi phí kéo khách, tỷ lệ quay lại). Chỗ nào không suy ra được thì để trống.
3. Hỏi người dùng **một lần**, chỉ những chỗ trống mà sai thì lệch cả mô hình (thường là giai đoạn, số liệu thật, ràng buộc không ghi trong tài liệu). Mỗi câu kèm một mặc định để họ chỉ cần gật. Không có hồ sơ khách thì hỏi: tên, bạn bán gì, bán cho ai, giá hiện tại nếu có.
4. Lập danh sách 2 đến 4 việc cần tra cứu (khoảng giá của phương án thay thế, hành vi nhóm khách, đối thủ gần nhất). Dùng công cụ tìm kiếm hoặc đọc web của nền tảng; nếu không có thì nhờ người dùng dán nội dung. Kết quả tra cứu mang nhãn [assumption] kèm nguồn.
5. Tự chấm sơ bộ "xuất phát điểm": đang định hướng sai (dò dẫm), tổ chức rối, thực thi chật vật, hay đứt mạch giữa các khâu. Một dòng mỗi mục, để đối chiếu lại ở cuối.
6. Trình bảng đầu vào, giả định chính và đường đi cho người dùng sửa nhanh, rồi chạy tiếp. Chỉ dừng lại nếu thiếu đầu vào then chốt.

## Trụ 1: WHO (một phân khúc)

1. Liệt kê 3 đến 6 phân khúc khả dĩ từ đầu vào và tra cứu.
2. Chấm mỗi phân khúc 1 đến 5 trên năm tiêu chí: nỗi đau đủ mạnh, khả năng chi trả, ta phục vụ tốt hơn người khác được, quy mô đủ đáng làm, tiếp cận được bằng kênh hiện có. Mỗi điểm ghi một dòng lý do.
3. **Điểm quyết định 1:** trình bảng chấm, đề xuất **đúng một** phân khúc kèm lý do loại các phân khúc còn lại. Người dùng chọn hoặc đổi. Ở chế độ tự động, dừng ở đây chờ phản hồi. Nếu họ đòi phục vụ nhiều nhóm cùng lúc, xếp hạng và lấy nhóm đứng đầu cho vòng này, các nhóm khác để dành vòng sau.
4. Dựng hồ sơ khách (8 trường, bảng mẫu trong `assets/templates.md`): đại diện cụ thể (một người có tên giả định, không phải "nhóm 25 đến 35 tuổi"), việc cần làm ở ba lớp (chức năng, cảm xúc, hình ảnh trước người khác), nỗi đau hiện tại cùng cách họ đang xoay xở, kết quả họ coi là thành công, bối cảnh và nơi tìm thấy họ, vai trò trong quyết định mua (ai khởi xướng, ai quyết, ai trả tiền), điều giữ họ ở lại, lý do họ do dự.
5. Phép thử: bỏ sản phẩm và giá ra khỏi đầu, khách đang "thuê" bạn để hoàn thành việc gì? Trả lời không được bằng một câu thì WHO còn mờ.

## Trụ 2: WHAT (phương trình giá trị)

1. Lập bảng phương trình cho phân khúc đã chọn:
   - Lợi ích = kết quả khách muốn x mức khách tin là đạt được. Cả hai vế đều phải làm: kết quả lớn mà không ai tin thì lợi ích cảm nhận vẫn thấp (cần bằng chứng, bảo hành, dùng thử, đánh giá).
   - Chi phí khách bỏ ra = tiền + thời gian + công sức + rủi ro cảm nhận.
2. Quy mọi dòng ra con số hoặc khoảng, cho cả ta và **phương án thay thế tốt nhất** (kể cả "không làm gì" hay "tự làm"). Không viết "tiện hơn" mà viết "từ 3 ngày xuống 1 ngày".
3. Đào kỹ ba chi phí không phải tiền (thời gian, công sức, rủi ro). Đa số đối thủ chỉ cạnh tranh bằng giảm giá, còn ba khoản này mới là dư địa khó bị sao chép.
4. Xác định tầng giá trị đang trao: chỉ làm xong việc, hay thêm yên tâm, hay đổi hẳn cách khách làm việc đó. Tầng càng cao càng ít bị thay bằng giá rẻ hơn.
5. Viết lời hứa theo mẫu: "Với [phân khúc] cần [việc], [tên] mang lại [kết quả] trong [thời gian] với [mức công sức hoặc rủi ro thấp], khác với [phương án thay thế] ở [bằng chứng]". Bốn chỗ trống phải nối thẳng về hồ sơ khách và bảng phương trình.
6. Kiểm chứng ngược: mỗi thành phần sản phẩm đỡ cho lời hứa nào. Thành phần không đỡ lời hứa nào thì cân nhắc bỏ. Lời hứa nào chưa có thành phần đỡ thì bổ sung hoặc hạ lời hứa.

## Trụ 3: HOW (trao giá trị)

1. Đi từ lời hứa ra: liệt kê hoạt động giữ lời hứa, chia ba nhóm. Lặp lại hằng ngày (sản xuất, giao, hỗ trợ), tùy biến theo khách (tư vấn, thiết kế giải pháp), tạo tài sản dùng lại (dữ liệu, cộng đồng, thương hiệu, hệ thống).
2. Vẽ hành trình khách qua ba đoạn: **thu khách** (biết, cân nhắc, mua), **phục vụ** (nhận, dùng, được hỗ trợ), **giữ và lan** (mua lại, giới thiệu). Mỗi chặng ghi: mục tiêu, khách đang ở trạng thái nào, điểm chạm cụ thể, kênh, chỉ số đo được. Chỉ ra chặng rơi rụng nhiều nhất, đó là nút thắt đầu tiên. Cần soi sâu thì dùng `journey-mapper` nếu đã cài.
3. Rà nguồn lực theo bảy nhóm: người, tài sản vật chất, tri thức, vốn, hệ thống và quy trình, thương hiệu và uy tín, đối tác.
4. Lọc năng lực cốt lõi bằng bốn câu hỏi: chuyên biệt cho việc này chưa, khó bắt chước không, hiếm không, khách có thật sự coi trọng không. Lọt cả bốn thì đáng đầu tư sâu, phần còn lại cân nhắc thuê ngoài.
5. Kiểm chứng ngược: lời hứa nào chưa có năng lực đỡ thì bổ sung năng lực hoặc hạ lời hứa cho khớp thực lực.

## Trụ 4: HOW MUCH (tiền)

1. Định giá từ giá trị khách cảm nhận, không cộng lãi lên chi phí. Chọn rõ hướng: **dẫn bằng giá trị** (biên cao, trải nghiệm khác biệt) hay **dẫn bằng chi phí thấp** (biên mỏng, thắng bằng quy mô). Hướng này phải khớp lời hứa ở WHAT.
2. Mô hình doanh thu trả lời năm câu: ai trả, trả cho cái gì, trả bao nhiêu, trả theo hình thức nào (một lần, thuê bao, theo mức dùng, hoa hồng), giá có đổi theo mùa, nhóm hay khối lượng không. Dùng mức giá của phương án thay thế từ tra cứu, gắn [assumption] kèm nguồn.
3. Cơ cấu chi phí bốn nhóm: cố định, biến phí theo sản lượng, chi phí giữ lời hứa và phục vụ và kéo khách, dự phòng rủi ro (đổi trả, bảo hành, nợ xấu).
4. Unit economics cho một khách hoặc một đơn: doanh thu, biến phí, biên đóng góp, CAC, số kỳ giữ chân kỳ vọng, LTV (biên đóng góp mỗi kỳ x số kỳ giữ chân). Chưa có số thật thì đưa **một khoảng** [assumption] và nói rõ biến nào làm kết quả nhạy nhất.
5. Ví dụ minh họa (số bịa): một hộp thuê bao đồ ăn nhẹ giá 300.000 mỗi kỳ, biến phí 180.000 nên biên đóng góp 120.000. Giữ chân trung bình 5 kỳ cho LTV 600.000. CAC 250.000 cho LTV/CAC khoảng 2,4: sống được nhưng mỏng, nhạy với tỷ lệ giữ chân. Nếu giữ chân chỉ 2 kỳ thì LTV 240.000 nhỏ hơn CAC, mô hình lỗ trên mỗi khách.

## Năm phép kiểm của phương trình

Chạy sau khi xong bốn trụ, mỗi phép ghi đạt, chưa đạt hay chưa đo được:

1. **Giá trị ròng dương** trong mắt khách: lợi ích quy tiền lớn hơn tổng chi phí của khách.
2. **Hơn phương án thay thế tốt nhất** ít nhất ở một khoản chi phí không phải tiền hoặc ở mức tin cậy vào kết quả.
3. **Giá nằm trong hành lang:** chi phí phục vụ cộng biên mục tiêu nhỏ hơn hoặc bằng giá, và giá còn thấp hơn rõ rệt lợi ích quy tiền. Mốc tham khảo: lợi ích gấp khoảng 3 lần giá thì khách dễ quyết, sát 1 lần thì dễ do dự. Kiểm lại với thị trường của bạn.
4. **LTV so với CAC:** nhỏ hơn 1 là lỗ, từ 1 đến dưới 3 là mỏng, từ 3 trở lên là khỏe (mốc tham khảo, ngành chu kỳ dài hoặc tái mua thấp sẽ khác). Kèm thời gian hoàn vốn CAC.
5. **Lực kéo tự nhiên:** nếu ngừng quảng cáo và khuyến mãi liên tục thì còn lại bao nhiêu doanh thu? Về gần 0 nghĩa là chưa có độ khớp, phải quay lại WHO và WHAT chứ không phải thêm ngân sách.

## Ma trận nhất quán và verdict

Đặt bốn trụ cạnh nhau, soi bốn cặp:

- WHO với WHAT: giá trị có giải đúng việc cần làm và nỗi đau của phân khúc đã chọn không.
- WHAT với HOW: mọi lời hứa đều có năng lực đỡ chưa.
- HOW với HOW MUCH: cơ cấu chi phí có nuôi nổi cách trao giá trị đã thiết kế không.
- WHAT với HOW MUCH: hướng tài chính có khớp tầng giá trị đã hứa không. Hứa cao cấp mà ép chi phí cho giá rẻ là mâu thuẫn điển hình.

Tín hiệu nhu cầu nếu đã có khách: khảo sát một câu "nếu không còn sản phẩm này, bạn thấy thế nào". Mốc tham khảo: trên khoảng 40% chọn "rất thất vọng" là dấu hiệu khớp thị trường, kiểm lại với ngành của bạn. Cộng thêm tỷ lệ mua lại và giới thiệu.

| Verdict | Điều kiện |
|---|---|
| **Go** | Bốn cặp nhất quán, năm phép kiểm đạt, và các dòng then chốt (sẵn lòng trả, CAC, giữ chân) có nhãn [data] |
| **Go để thử nghiệm** | Chỉ dùng cho ý tưởng giai đoạn đầu: bốn cặp nhất quán và số học không lỗ trên mỗi khách theo giả định, nhưng các dòng then chốt (sẵn lòng trả, CAC, giữ chân) vẫn là [assumption]. Đây là cho phép chi một khoản nhỏ có trần để kiểm chứng, không phải cho phép đầu tư đầy đủ. Bắt buộc kèm điều kiện thử và ngưỡng dừng (xem dưới) |
| **Refine** | Còn 1 đến 2 mâu thuẫn hoặc phép kiểm chưa đạt, hoặc ý tưởng không còn ở giai đoạn đầu mà các dòng then chốt vẫn là [assumption]. Nêu rõ quay lại trụ nào, sửa gì, đo gì |
| **No-Go** | Một mâu thuẫn nền tảng không có đường sửa: LTV nhỏ hơn CAC mà không biến nào cải thiện được, giá trị ròng không dương với mọi phân khúc, hoặc lời hứa không có năng lực nào đỡ được |

Quy tắc trần: nếu sẵn lòng trả, CAC và giữ chân đều chỉ là [assumption] thì verdict tối đa là **Go để thử nghiệm** (khi ý tưởng ở giai đoạn đầu và số học không lỗ theo giả định), còn nếu có mâu thuẫn hoặc phép kiểm chưa đạt thì tối đa là Refine. Việc đầu tiên của memo luôn là đo ba thứ đó.

**Go để thử nghiệm phải có đủ ba phần:**
1. **Điều kiện thử:** thử cái gì (một khách hàng đầu tiên, một đợt bán thử, một trang đăng ký), với ai, trong bao lâu (mốc tham khảo: 2 đến 6 tuần), trần chi tối đa (người dùng tự đặt, ví dụ không quá một phần nhỏ vốn họ chịu mất được).
2. **Chỉ số cần đạt:** mỗi giả định then chốt một chỉ số và một mức đạt, viết trước khi thử (ví dụ số người trả tiền thật, chi phí để có một khách, tỷ lệ quay lại).
3. **Ngưỡng dừng:** điều kiện dừng hoặc đổi hướng viết sẵn (hết thời gian mà chưa đạt, hoặc chạm trần chi). Không được nới ngưỡng sau khi đã thấy kết quả.
Hết kỳ thử, chạy lại verdict với các dòng đã có [data]; chỉ khi đó mới có thể lên Go đầy đủ. Số học là số học: không làm dịu một mô hình lỗ trên mỗi khách.

**Điểm quyết định 2:** trình ma trận, năm phép kiểm, verdict kèm lý do, và danh sách lựa chọn agent đã tự quyết thay người dùng (phân khúc, mức giá, năng lực cốt lõi, kèm phương án đã loại). Nếu Refine hoặc No-Go, hỏi họ muốn quay lại trụ nào rồi chạy lại trụ đó. Chỉ đóng gói sau khi họ duyệt.

## Đóng gói

1. Điền canvas một trang 7 khối (WHO, WHAT, sản phẩm, HOW, hành trình, HOW MUCH, chi phí và rủi ro), mẫu trong `assets/templates.md`. Mỗi dòng giữ nhãn.
2. Viết **memo quyết định** tối đa 200 từ: tình hình, verdict và lý do, ba việc tiếp theo (mỗi việc có người làm), và danh sách "cần đo" gom từ mọi [assumption] then chốt. Nếu verdict là Go để thử nghiệm, memo phải có thêm dòng "Sau kỳ thử: chạy lại verdict; để lên Go đầy đủ cần: [các dòng then chốt có nhãn data và đạt chỉ số]".
3. Chạy lại xuất phát điểm ở Bước 0: sau mô hình này, khâu nào đã chặt hơn, khâu nào vẫn hở.
4. Đề nghị vẽ sơ đồ (hành trình, ma trận nhất quán, canvas) qua skill `visual-thinking` nếu đã cài, không thì dùng bảng văn bản.
5. Kết bằng bước tiếp theo cụ thể: việc đầu tiên trong tuần này và ai làm.

## Quy tắc đầu ra

- Gắn nhãn [data] hoặc [assumption] ở mọi dòng quan trọng. Nêu rõ giả định.
- Lưu thành Google Doc hoặc Google Sheet **mới** nếu có kết nối; nếu không thì trả ngay trong cuộc trò chuyện. Không ghi đè tệp có sẵn.
- Không gửi, đăng, chi tiền hay thay đổi gì ngoài cuộc trò chuyện khi chưa có sự đồng ý của người dùng.
- Mọi đầu ra kết bằng bước tiếp theo hoặc danh sách cần đo, không để cụt.

## Chuẩn chất lượng

- Chỉ một phân khúc, kèm lý do loại các phân khúc khác.
- Mỗi khuyến nghị bám một công cụ có tên ở trên (việc cần làm, phương trình, năm phép kiểm, ma trận), không phán chung chung.
- Định lượng thay vì tính từ, so với phương án thay thế chứ không so với con số 0.
- Giá bám giá trị cảm nhận, không trình bày cộng lãi lên chi phí như mặc định.
- Lựa chọn agent tự quyết đều có lý do và phương án bị loại để người dùng phản biện được.
- Không dừng hỏi giữa bốn trụ khi không có mâu thuẫn nghiêm trọng, và không vượt qua hai điểm quyết định khi chưa được duyệt.
- Ở chế độ coach, không soạn thay câu trả lời của người dùng rồi trình như sự thật.
