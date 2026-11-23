# Orca-only repo; legacy preserved at tag v0-openmausbot

Status: accepted

`main` targets Orca only. The earlier non-Orca material (old guides, mapping tables, legacy frontmatter, the old `packs/ecommerce` pack) was removed from `main` after the pre-removal state was tagged `v0-openmausbot`. Nothing is lost: anyone who needs it can check out that tag.

We chose a clean Orca-only `main` over keeping two targets because the first design partner runs bots in Orca on staff's own machines and subscriptions, and dual support would double the surface to test and document.

Consequence: the old target is out of scope for v1 and no longer supported on `main`; `scripts/check-no-legacy.sh` fails CI if legacy terms return.
