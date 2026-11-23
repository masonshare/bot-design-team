# 0002. Google Sheets now, Microsoft 365 later

Status: Accepted

## Context

The knowledge base of reply scripts (`Kịch bản`) and the `Đề xuất` tab need shared storage that the owner can set up alone. Orca has a native Google connector. Microsoft 365 / OneDrive would need an MS-365 MCP server and the owner's boss to approve its app permissions, so it cannot be assumed.

## Decision

The knowledge base lives in a Google Sheet in the owner's own Google account, accessed through Orca's native Google connector and shared view-only with staff. The `Đề xuất` tab is its own Google Sheet file (see the amendment below). Migrating to Microsoft 365 is a recorded later option, not part of v1. Pack skills keep storage access narrow (read approved scripts, append to `Đề xuất`) so a later backend swap changes little.

## Consequences

- Setup docs must state which Google permissions are needed.
- The choice of Sheets must not be read as permanent.

## Amendment (PR #28, spec #14): `Đề xuất` is a separate file

Google shares per file, not per tab, and the Staff bot signs in as the staff member. A view-only share cannot let the bot append to `Đề xuất`. So the decision above is refined: the scripts knowledge base (`Kịch bản`) stays in the main Sheet, shared view-only with staff, and `Đề xuất` lives in its own Google Sheet file named `Đề xuất CSKH`, shared with staff as editor. The Staff bot reads the scripts file read-only and appends only in `Đề xuất CSKH`. Cost: staff editors could edit or delete rows there; accepted, the owner reviews the file daily. Status stays Accepted; the Google-now, Microsoft-365-later decision is unchanged.
