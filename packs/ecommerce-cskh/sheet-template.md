# Google Sheet template: kho kiến thức CSKH

Create TWO Google Sheet files in the owner's own Google account. Names and tab names are exact.

| File | Tab | Who edits |
|---|---|---|
| Scripts file (any name, for example `Kịch bản CSKH`) | `Kịch bản` | Owner and Editor bot. Staff: view-only |
| `Đề xuất CSKH` | `Đề xuất` | Staff (and the Staff bot as the signed-in staff member). Owner reads and manages |

Google shares per file, never per tab. That is why `Đề xuất` is its own file: staff can then be editors there and stay view-only on the scripts.

## Tab 1: `Kịch bản`

One row per script. Row 1 holds these headers, in this order.

| Column | Header | Content |
|---|---|---|
| A | Mã | Unique code, for example `GIFT-001`. Prefix by group: GIFT, ORD, DEL, RET, PRD, ATTP |
| B | Nhóm | One of: `B2B gift box`, `order`, `delivery`, `returns`, `product`, `food safety` |
| C | Tình huống | Short description of the situation |
| D | Câu khách hay hỏi | Typical customer questions, separated by ` / ` |
| E | Mẫu trả lời | The approved reply text, in Vietnamese, in the shop's voice |
| F | Kênh áp dụng | One of: `all`, `Shopee`, `Zalo`, `hotline` |
| G | Lưu ý nội bộ | Internal note for staff. Never sent to the customer |
| H | Trạng thái | One of: `Nháp`, `Đã duyệt`, `Hết hạn` |
| I | Người duyệt + ngày | Approver name and date, for example `Chủ shop, 2026-01-15`. Empty while `Nháp` |

### Status vocabulary

- `Nháp`: written by the Editor bot or a person, not yet approved. The Staff bot must not treat it as approved.
- `Đã duyệt`: approved by the owner. The only status the Staff bot answers from as authoritative. Column I must be filled.
- `Hết hạn`: no longer valid (old promotion, changed policy). The Staff bot must not use it.

### Channel vocabulary

- `all`: any channel.
- `Shopee`, `Zalo`, `hotline`: only that channel. A `Shopee` script is not used on the other channels.

## File 2, tab `Đề xuất` (file `Đề xuất CSKH`)

The Staff bot's inbox, in its own file named `Đề xuất CSKH` with a single tab `Đề xuất`. One row per question the knowledge base could not answer, or answered only provisionally.

| Column | Header | Content |
|---|---|---|
| A | Ngày | Date logged |
| B | Kênh | `Shopee`, `Zalo` or `hotline` |
| C | Câu hỏi của khách | The customer's question, with no personal data |
| D | Câu đã trả lời | What the bot answered, or `chưa trả lời` |
| E | Mã gần nhất | Closest script code, if any |
| F | Người hỏi | Staff member who asked |
| G | Trạng thái xử lý | `Mới` or `Đã xử lý` |
| H | Số lần hỏi | Times this same question was asked. Starts at `1`; the Staff bot adds 1 instead of adding a duplicate row (see `staff/skills/cskh-no-script`) |

The owner reviews the `Đề xuất CSKH` file (daily during the pilot); the owner or the Editor bot turns useful rows into `Nháp` scripts in tab `Kịch bản` of the scripts file.

## Access model

- Scripts file: staff get a view-only share. They cannot edit scripts.
- `Đề xuất CSKH` file: staff get editor access (this file only). The bot signs in as the staff member, so it can append there.
- The Staff bot reads the scripts file read-only and writes only to `Đề xuất CSKH` (append a row, or add 1 to `Số lần hỏi`). It never edits `Kịch bản` or changes other `Đề xuất` cells.
- Known cost: a staff editor could edit or delete rows in `Đề xuất CSKH`. Accepted; the owner reviews the file daily during the pilot and may protect the header row.
- Only the Editor bot and the owner write to `Kịch bản`. The Editor bot writes `Nháp` only. Only the owner sets `Đã duyệt` and fills column I.
- Real Sheet IDs, links, prices and chats stay in the owner's Google account and are never committed to this repo.
