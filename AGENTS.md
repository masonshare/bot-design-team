## Agent skills

### Issue tracker

Issues live in GitHub Issues of masonshare/bot-design-team (via `gh` CLI). See `docs/agents/issue-tracker.md`.

### Triage labels

Default five labels: needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one `GLOSSARY.md` and `docs/adr/` at repo root. See `docs/agents/domain.md`.

## Hard rule: Orca-only, no real data

This repo is public and targets Orca only. Never commit real company data (scripts, prices, chats, customer names, phone numbers, staff details) or secrets. Use fake examples only. Legacy OpenMausBot and Grok material lives only at the git tag v0-openmausbot.

CLAUDE.md must stay byte-identical to this file.
