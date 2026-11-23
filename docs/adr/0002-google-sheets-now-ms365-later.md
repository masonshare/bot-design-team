# Google Sheets now, Microsoft 365 later

Status: accepted

The knowledge base of reply scripts (Kịch bản) and the `Đề xuất` tab live in a Google Sheet in the owner's own Google account, accessed through Orca's native Google connector and shared view-only with staff. We chose this because it needs no approval from anyone else and works today.

Migrating to Microsoft 365 / OneDrive through an MS-365 MCP server is a recorded later option, not part of v1. It requires the owner's boss to approve the app permissions, so it cannot be assumed. Pack skills should keep storage access narrow (read approved scripts, append to `Đề xuất`) so that swapping the backend later changes little.

Consequence: setup docs must state which Google permissions are needed, and the choice of Sheets must not be read as permanent.
