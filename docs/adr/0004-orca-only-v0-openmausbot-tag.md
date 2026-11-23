# 0004. Orca-only repo; legacy preserved at tag v0-openmausbot

Status: Accepted

## Context

The first design partner runs bots in Orca on staff's own machines and subscriptions. The repo also held earlier non-Orca material (old guides, mapping tables, legacy frontmatter, the old `packs/ecommerce` pack). Keeping two targets would double the surface to test and document.

## Decision

`main` targets Orca only. The pre-removal state was tagged `v0-openmausbot` and the legacy material was then removed from `main`. Anyone who needs it can check out that tag.

## Consequences

- The old target is out of scope for v1 and no longer supported on `main`.
- `scripts/check-no-legacy.sh` fails CI if legacy terms return.
