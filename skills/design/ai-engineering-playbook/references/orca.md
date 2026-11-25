# Orca: kiến thức chắt lọc từ tài liệu công khai

Nguồn: tài liệu công khai tại https://orca.dev/docs và https://github.com/stablyai/orca, đọc ngày 2026-11-25 (bản chụp ngày 2026-11-23). Đây là bản tóm tắt, không phải kinh nghiệm riêng của ai. Những chỗ ghi "(suy luận)" là phần người tổng hợp tự suy ra, không có trong tài liệu.

## 1. Tóm tắt 10 dòng

1. Orca là một ADE/IDE desktop (macOS, Windows, Linux) để chạy nhiều AI coding agent song song: Claude Code, Codex, Cursor CLI và khoảng 40 CLI agent khác.
2. Mỗi task có git worktree thật, terminal agent và tab trình duyệt riêng, nên không phải stash hay đổi branch liên tục.
3. Orca không phải model. Người dùng tự mang subscription của mình (BYO). Orca cũng không phải dịch vụ VPS: compute từ xa chạy trên máy do bạn kiểm soát.
4. Vòng làm việc cốt lõi: Add repo → worktree → agent → split pane → diff/annotate → commit/PR → xóa worktree.
5. **Bots** là lớp trên cùng. Bot có tên, mục đích (soul), bộ nhớ, abilities và automations, và nằm trong một thư mục trên một máy.
6. Bot nhận việc từ chat, Slack, GitHub, Linear, webhook hoặc theo lịch. Việc sửa code được giao cho **worker**, tức một phiên agent trong worktree riêng, kết quả trả về dạng PR.
7. **Orchestration** (Experimental) cho coordinator điều phối worker qua Run/Task/Dispatch, mailbox, `worker_done`, `ask` và decision gate.
8. Có thể chạy local, qua SSH, trên Remote Orca Server (khuyến nghị dùng Tailscale) hoặc Cloud VM. Mobile app (iOS/Android) đóng vai remote control.

## 2. Khái niệm

### Worktree và workspace
- Repo có **base ref** (thường là `origin/main`). Mỗi worktree có **start-from ref**, có thể là branch, SHA, nhánh remote hoặc nhánh khác (để stack PR).
- Việc tạo worktree chạy nền (`git fetch` + `git worktree add`). Nếu lỗi thì có nút Retry.
- Worktree con có **Parent workspace**. Quan hệ cha con chỉ để lồng trong sidebar, không ảnh hưởng git.
- Có lệnh "Sleep/Delete with Descendants" cho cả cây worktree, ví dụ cây do orchestration sinh ra.
- Có ba cách chia sẻ file gitignored cho worktree mới:
  - **Worktree Shared Paths** (cấu hình trong Settings): clone hoặc symlink.
  - **`worktree.sharedDirectories`** trong `orca.yaml`: symlink, dùng cho cây lớn như `node_modules`.
  - **`.worktreeinclude`**: copy riêng cho từng worktree, dùng cho `.env` và file tương tự.
- `orca.yaml` có `scripts.setup` (chạy sau khi tạo worktree) và `scripts.archive` (chạy trước khi xóa). Nó cũng chứa `environmentRecipes` cho Cloud VM.
- Biến môi trường có sẵn: `ORCA_ROOT_PATH`, `ORCA_WORKTREE_PATH`, `ORCA_WORKSPACE_NAME`. Orca không cấp port riêng cho từng worktree.
- **Quick Commands** là các lệnh hoặc prompt đã lưu, phạm vi Project hoặc Global, đồng bộ sang mobile.

### Agent, phiên, trạng thái
- Trạng thái lấy từ OSC title và **agent status hooks**:
  - spinner: đang làm;
  - vàng/hổ phách: Needs You;
  - xanh: xong;
  - đỏ: lỗi;
  - xám: idle.
- **Agent Dashboard** là kanban, và **Activity feed** gom sự kiện từ mọi worktree.
- Theo mặc định Orca chạy agent với cờ bypass quyền (`--dangerously-skip-permissions`, `--yolo`…). Lý do: Orca coi worktree là sandbox có thể vứt đi. Có thể đổi sang Manual hoặc Auto trong Settings → Agents.
- **Chat UI** (native chat) là lựa chọn thay cho terminal CLI. Hỗ trợ `/plan`, `/fork`, `/btw`, `/compact`, hàng đợi tin nhắn kèm Steer, và tự tiếp tục khi usage limit reset.
- **Session history**: Orca quét transcript trên đĩa và cho Resume với cùng cwd và session ID.
- **Session restore**: một daemon giữ PTY sống qua Cmd-Q, update hoặc crash của app. Reboot thì mất.
- **Agent hibernation** (Experimental): tạm dừng PTY của agent đã `done` và idle quá 30 phút, tự resume khi quay lại terminal.
- **Multi-account**: hot-swap tài khoản Claude/Codex để có thêm quota. Theo dõi usage theo khung 5 giờ, ngày và tuần, có cảnh báo khi vượt 80%.
- Agent hooks và memory: Orca đọc `.claude/` và `.codex/` của repo, nhưng không động vào `CLAUDE.md`/`AGENTS.md`.

### Bots
- **Tạo bot**: Sidebar Bots → `+` → New bot. Có thể bắt đầu từ đầu, từ một trong 24 template, hoặc Import từ app khác. Bot chạy bằng agent và đăng nhập của bạn trên máy được chọn.
- **Lưu trữ**: soul, memory và abilities là file Markdown thuần trong thư mục bot. Chat history nằm trong kho riêng của Orca.
- **Home của bot**: mục **Needs you** chứa các câu hỏi, yêu cầu phê duyệt hoặc đăng nhập đang chờ owner, kèm danh sách việc đang chạy và automations.
- **Worker**: phiên agent trong worktree mới, nằm dưới bot trong sidebar. PR của worker quay về bot. Owner có thể "step in" vào worktree đó bất cứ lúc nào.
- **Automations**:
  - Theo lịch: hourly, daily, weekdays, weekly, cron, RRULE.
  - Theo sự kiện: phụ thuộc connector.
  - Khi mới tạo, lịch của template đang tắt.
- **Việc bot tự chạy**:
  - **Look around**: chỉ đọc, chạy mỗi 4 giờ từ 8h đến 20h các ngày trong tuần, rồi đưa gợi ý vào Suggestions.
  - **Memory upkeep**: dọn `MEMORY.md` hằng đêm sau 3h sáng, có Undo, không có tool.
- **Connectors**:
  - Slack: mỗi bot là một Slack app riêng, cần App Configuration Token `xoxe-`.
  - GitHub: trả lời tại chỗ qua app Orca; các việc khác dùng `gh` của owner.
  - Linear: gọi `@Orca <handle>` hoặc gắn nhãn `bot:<handle>`.
  - Google: Gmail, Calendar, Drive, Docs, Sheets, qua Google Cloud app của chính owner, đi thẳng từ máy.
  - Webhooks.
  - Composio: cho Outlook, HubSpot và các dịch vụ khác.
  - MCP servers.
- Slack, GitHub, Linear và webhook đi qua **Orca Cloud**. Máy owner kết nối ra ngoài, không cần mở port.
- **Who can ask**: mặc định chỉ owner. Người được thêm sẽ dùng quyền của owner.
- **Chế độ quyền** của chat bot: Ask for approval / Accept edits / Approve for me / Full access. Mặc định là Full access.

### Orchestration (Experimental)
- Thành phần:
  - **Run**: namespace bền cùng mailbox của coordinator, không tự lập lịch.
  - **Task**: có spec, các phụ thuộc và trạng thái `pending|ready|dispatched|completed|failed|blocked`.
  - **Dispatch**: một lần thử chạy task trên một terminal.
  - **Message** gồm các loại `status`, `dispatch`, `worker_done`, `escalation`, `question`, `heartbeat`.
  - **Decision gate**: câu hỏi do coordinator giữ, chặn task cho đến khi được trả lời.
- Group address: `@all`, `@idle`, `@claude`, `@codex`, `@worktree:<id>`…
- Worker có thể lồng nhau tối đa 4 tầng (mặc định). Heartbeat mặc định 5 phút.
- **Federated workers** (`--on <host>`) chạy worker trên host khác.

### CLI, skills, chạy từ xa
- `orca` CLI có các nhóm lệnh:
  - repo, worktree, terminal;
  - browser (snapshot/click/fill);
  - computer use (beta);
  - linear, automations, reference, search, artifacts, skills, serve, environment.
- Trên Linux, lệnh tên là `orca-ide`.
- 7 skill: `orca-cli`, `orchestration`, `computer-use`, `orca-linear`, `orca-emulator`, `orca-emulator-android`, `orca-per-workspace-env`. Bản cài là "hybrid stub": agent phải gọi `orca skills get <topic> --full` để lấy nội dung khớp phiên bản.
- **Worktree checkpoints**: `orca worktree set --comment … --workspace-status …`.
- **Remote Orca Server** (Beta): chạy `orca serve`. Có thể cài thành service (LaunchAgent hoặc systemd), xác thực bằng token riêng cho từng client.
- **SSH targets**: cài managed server trên host. Mặc định CLI trên host chỉ điều khiển được chính host đó.

## 3. Cách làm tốt (best practices)

### Làm việc song song
- **Đua ba agent**: tạo 3 worktree từ cùng ref, chạy 3 agent khác nhau với cùng một prompt, chọn bản thắng, xóa hai bản còn lại (xóa luôn branch). Nếu cả ba ra cùng kết quả thì nhiều khả năng đó là đáp án đúng. Nếu chúng bất đồng thì đó chính là phần khó của bài toán.
- **Review diff**: đi qua từng hunk bằng `j/k`, bấm `c` để comment bằng câu hoàn chỉnh, rồi **Send to agent** theo lô. Gửi theo lô nghĩa là agent sửa một lần và chính xác hơn. Resolve comment sau khi kiểm tra bản sửa.
- **Quản lý khoảng 10 worktree**:
  - Dùng `Cmd-J` (Jump Palette) và xử lý worktree đang chờ input (chấm vàng) trước.
  - Bấm chip Restart sau khi máy ngủ dậy.
  - Xóa worktree đã merge để palette không bị chậm.
- **Rời máy an toàn**: xếp hàng nhiều agent, bỏ đi, rồi quay lại khi có thông báo hoặc chuông báo xong. Dùng Activity feed để nắm lại tình hình.
- **Chọn cách chia sẻ file**: `sharedDirectories` cho cây lớn có thể build lại, `.worktreeinclude` cho secrets hoặc config cần bản riêng. Luôn chạy `cleanup preview` trước khi bật quy tắc cleanup.

### Điều phối bot và worker
- **Viết yêu cầu cho bot** nêu đủ bốn ý: khi nào chạy (lịch, sự kiện hoặc ngay bây giờ), làm gì (một câu), báo cáo ở đâu, và việc gì phải hỏi trước. Template mặc định đều theo nguyên tắc báo cáo trước rồi mới hành động ("report first, then act").
- **Vòng giám sát chuẩn**:
  1. `orchestration run-create`
  2. `task-create`
  3. `worker-start --task … --worktree new-child --agent …`
  4. `check --wait --types worker_done,escalation,question`
  5. `check --ack <deliveryId>` (hàng đợi FIFO, thư được phát lại cho đến khi ack)
  6. `worker-release` khi xong
- **Hợp đồng của worker**:
  - Gửi `worker_done` đúng một lần, kể cả khi thất bại, kèm `--outcome`.
  - Có `--task-id` và `--dispatch-id`.
  - Body nói rõ đã làm gì, tìm thấy gì, còn lại gì.
  - Gặp câu hỏi chặn tiến độ thì dùng `orchestration ask --options … --timeout-ms`.
- **Chọn công cụ theo mức độ**:
  - `terminal send` cho prompt nhẹ;
  - `worker-start` hoặc `dispatch --inject` khi cần `worker_done` và theo dõi;
  - Run + Task cho vòng làm việc bền.
  - Luôn tải `orca skills get orchestration --full` trước.
- **Thói quen khi dùng CLI**:
  - Luôn thêm `--json`.
  - Dùng selector (`id:`, `path:`, `branch:`) thay vì nhãn hiển thị trên UI.
  - Đọc terminal trước khi gửi.
  - Đặt base ref trước khi tạo nhiều worktree.
  - Ghi checkpoint bằng comment worktree; đọc `worktree current` trước để không ghi đè mục tiêu owner đã viết.
- **Handoff sang agent đã có**: `orca reference find`, rồi `terminal send` hoặc `orchestration send --to <mailbox> --type question`.
- **Automations**:
  - Tạo với `--disabled`, rồi `show` và `run` thử, sau đó mới bật.
  - Dùng `--precheck` để bỏ lượt chạy khi điều kiện không đạt.
  - Nếu cần chạy cả khi laptop tắt, đặt automation trên Remote Orca Server.
- **Bảo mật**:
  - Bot nhận yêu cầu từ người khác hoặc đọc nội dung bên ngoài (mail, issue, tin nhắn) thì nên chuyển sang **Ask for approval**, với agent hỗ trợ chế độ này (Claude Code, Codex).
  - Chỉ bật connector cần thiết. Để Google tắt nếu không dùng.
  - Nếu team cần dùng chung, tạo bot riêng cho team.
- **Import bot**: automations nhập vào ở trạng thái paused. Tắt bot cũ trước, rồi mới bật bot mới để tránh chạy trùng.
- **Remote server**: cài và đăng nhập git cùng CLI agent ngay trên server (đăng nhập trên laptop không tự chuyển sang). Giữ ACL Tailscale hẹp.

## 4. Hạn chế và bẫy

### Máy và vận hành
- Bot chỉ chạy khi máy của nó thức và có mạng. Yêu cầu từ Slack, GitHub, Linear được giữ tối đa 1 ngày. Trên Mac, gập nắp thì máy vẫn ngủ dù có "Keep computer awake".
- Reboot, cập nhật OS hoặc mất điện sẽ giết daemon PTY. Layout được khôi phục nhưng phải khởi động lại agent.
- **SSH và remote**: mất liên lạc với host không có nghĩa là công việc đã dừng. Kiểm tra host trước khi chạy agent thứ hai trên cùng worktree. Nếu không nhận được phản hồi khi launch, dùng `--retry-launch`, đừng mở agent mới.
- Thiếu `hostScope` hoặc `executionHostId` nghĩa là "không xác minh được", không phải "đang chạy local".

### Quyền và bảo mật
- Mặc định là Full access và cờ yolo, nên agent không hỏi trước khi chạy lệnh hay sửa file.
- Một số agent không có chế độ phê duyệt, nên luôn chạy Full access.
- Các quy tắc sau chỉ là lời dặn bot, Orca **không** cưỡng chế:
  - approve hoặc merge PR chỉ khi owner yêu cầu;
  - soạn nháp email thay vì gửi;
  - coi nội dung bên ngoài là thông tin, không phải lệnh;
  - không lưu secret vào memory.
  
  Model vẫn có thể bị prompt injection.
- Những gì Orca **có** cưỡng chế:
  - kiểm tra Who can ask;
  - Look around chỉ đọc;
  - memory upkeep không có tool;
  - import bỏ qua file key (chỉ ở mức best effort);
  - tạo bot mới phải có người bấm nút;
  - tự ghi "asked by X via bot".
- Automation theo sự kiện chạy với **bất kỳ ai** ở nơi có cả owner và bot, độc lập với Who can ask. "Keep only me" không dừng automation hay webhook.
- Ai có URL webhook đều kích hoạt được automation. Nên thêm signing secret, và Rotate key nếu URL bị lộ.
- Orca Cloud giữ một phần dữ liệu: payload webhook tối đa 7 ngày, tin nhắn thread gần đây, và các yêu cầu chưa giao.
- Key của MCP server chạy dạng lệnh được lưu không mã hóa (chỉ user đọc được).

### Orchestration và CLI
- Orchestration là Experimental. Các lệnh `orchestration run`, `run-stop`, `coordinator-start/stop` đã bị ngừng và không làm gì. Bảng UI Orchestration hiện không dùng được.
- Không dùng group address cho `worker_done` hay heartbeat. Trong PowerShell phải để trong ngoặc kép: `--to "@all"`.
- `orchestration reset` ảnh hưởng toàn runtime. Đừng chạy khi có coordinator khác đang hoạt động.
- Khi gặp `release_pending` hoặc `release_unknown`, làm theo receipt, đừng `terminal close` hàng loạt.
- `worker-start --retry-of` không kế thừa `--on` hay worktree, phải ghi lại tường minh.
- Automation `--extra-agent-args` chỉ nhận model và effort, phải viết dạng `=`, và không dùng chung được với `--reuse-session`. `remove` xóa luôn lịch sử chạy.
- `linear save-issue` labels **thay thế** toàn bộ tập nhãn.

### Worktree và git
- Workspace cleanup xóa thật, không archive, và có thể chạy trong vài giây.
- Xóa worktree là xóa cả thư mục lẫn branch. Branch chưa merge được giữ lại, còn thư mục thì không.
- `sharedDirectories` và `.worktreeinclude` chỉ nhận path literal, đã gitignore, và có thật trong checkout chính.
- Rate limit GitHub được chia chung giữa Orca, `gh`, các agent và CI. `GH_TOKEN` trong shell profile được ưu tiên hơn keyring. Mỗi SSH host cần `gh auth login` riêng.

### Linh tinh
- Không resume được trong terminal một cuộc hội thoại đã chuyển sang Chat UI. Chat không gửi tin khi cùng hội thoại đang mở trong terminal.
- Tự resume khi limit reset quá 24 giờ phải làm thủ công. Chi phí trong Stats chỉ là ước tính.
- Codex chạy mỗi tab một server riêng, nên `codex agents` không thấy các phiên trong Orca. Lỗi `SUN_LEN` xảy ra khi đường dẫn home quá dài.
- Telemetry là pseudonymous, gửi đến PostHog ở Mỹ. Tắt bằng `DO_NOT_TRACK=1` hoặc `ORCA_TELEMETRY_DISABLED=1`.
- Conductor Cloud đã đóng ngày 2026-11-20. Đừng archive workspace Conductor đã mở bằng Orca, vì làm vậy sẽ xóa thư mục.

## 5. Danh sách nguồn

- https://orca.dev/docs (tài liệu chính thức: worktree, agent, bots, orchestration, CLI, skills, chạy từ xa)
- https://github.com/stablyai/orca

Lưu ý về độ bao phủ:
- Orca thay đổi nhanh và orchestration còn ở mức thử nghiệm (Experimental); hãy kiểm tra lại tài liệu hoặc `orca skills get` trước khi dựa vào chi tiết.
- Tài liệu có thể ghi hai chỗ khác nhau cho việc đăng ký Orca CLI: Settings → General và Settings → Experimental.
