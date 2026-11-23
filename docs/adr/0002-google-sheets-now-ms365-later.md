# 0002. Google Sheets now, Microsoft 365 later

Status: Accepted

## Context

The knowledge base of reply scripts (`Kịch bản`) and the `Đề xuất` tab need shared storage that the owner can set up alone. Orca has a native Google connector. Microsoft 365 / OneDrive would need an MS-365 MCP server and the owner's boss to approve its app permissions, so it cannot be assumed.

## Decision

Both tabs live in a Google Sheet in the owner's own Google account, accessed through Orca's native Google connector and shared view-only with staff. Migrating to Microsoft 365 is a recorded later option, not part of v1. Pack skills keep storage access narrow (read approved scripts, append to `Đề xuất`) so a later backend swap changes little.

## Consequences

- Setup docs must state which Google permissions are needed.
- The choice of Sheets must not be read as permanent.
