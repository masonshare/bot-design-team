# No real company data in the public repo

Status: accepted

This repo is public and MIT-licensed, and is meant to be reused for other businesses. Real company data (scripts, product names with prices, customer chats, names, phone numbers) must never be committed. It lives only in the owner's Google Sheet. The pack ships FAKE data only.

Enforcement: the rule is stated in `AGENTS.md`/`CLAUDE.md`, and CI runs a scan that fails the build on phone-number-like strings, customer-name patterns and price lists outside a fake-data allowlist. Editor-bot skills also warn when pasted chats contain personal data, and seed chats are anonymised by hand before pasting.

Consequence: a false positive in the scan is fixed by making the sample data clearly fake, not by weakening the rule.
