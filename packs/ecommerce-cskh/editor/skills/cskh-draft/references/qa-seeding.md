# Seeding from a public Q&A page

The Q&A page is public, dated about 2022, and partly inconsistent. Treat it as an unverified source.

1. Run the personal-data check on the pasted text.
2. Split into question/answer pairs. Group pairs by topic (delivery, returns, product, ...).
3. For each topic make one `Nháp` row. Note in column G: `Nguồn: trang hỏi đáp cũ (2022), cần chủ shop xác nhận`.
4. Inconsistency: two pairs on one topic that give different facts (days, deadlines, amounts, conditions). Do not pick one. Leave the fact blank in column E, mark `Cần chủ shop quyết định`, and record both source values in column G.
5. Compare with existing `Đã duyệt` rows; warn on conflicts (see SKILL.md rule 4). When the page itself gives two values for the topic, name them as a pair (`nguồn ghi A và B`); do not describe either one as "the new value".
6. Sensitive categories always follow SKILL.md rule 7, even when the page states a fact without conflict: the draft stays `Nháp` and the owner confirms the value is still current.
7. Final summary: number of `Nháp` rows created, then a list of inconsistencies in the form `<topic>: <value A> vs <value B>`.

Testing uses `fake-data/FAKE-qa-khong-nhat-quan.txt` only. Real Q&A text is pasted by the owner at runtime and goes only to the owner's Sheet.
