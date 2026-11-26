"""Shared rules for the skill-content checks and scripts/import-skill.py (stdlib only).

Junk is what must never ship in a public pack skill. Neutral terms are the things a skill
in the marketing-ecommerce / strategy-advisor packs (and the starter skills listed in
NEUTRAL_STARTER) must not contain: they tie it to one agent, one machine or one company."""
import fnmatch
import re
from pathlib import Path

JUNK_DIRS = {".versions", "working", ".git", "__pycache__", "node_modules", ".claude"}
JUNK_FILES = ["*.bak", "*.bak.*", "*.orig", "*.tmp", ".DS_Store", "Thumbs.db", "progress.md", "SPEC.md", "*transcript*"]

NEUTRAL_PACKS = ["marketing-ecommerce", "strategy-advisor"]
# Starter skills added by the pack-public stream (the older starter skills may name Claude on purpose).
NEUTRAL_STARTER = ["skill-spec-generate", "workflow-ai-agents", "agentic-vibe-working", "luu-vao-notion-second-brain"]

# (regex, label). Case-insensitive. Framework names (AIDA, JTBD ...) are fine; people, books, URLs are not.
NEUTRAL_TERMS = [
    (r"AskUserQuestion", "AskUserQuestion (say: ask the user once, each question with a default)"),
    (r"~/\.claude|\.claude\b", "a .claude path (say: the skill folder)"),
    (r"CLAUDE\.md", "CLAUDE.md (say: the project instruction file, CLAUDE.md or AGENTS.md)"),
    (r"masonshare-brain|masonshare brain", "masonshare-brain"),
    (r"nam\s*xanh|namori", "a real company brand (use the customer's brand-profile and FAKE examples)"),
    (r"\bstrategy/<", "a strategy/<venture> path (say: the customer's profile, wherever they keep it)"),
    (r"(?<![\w/])/(?:express|guided|deep)\b", "a slash command (say: the mode keyword)"),
    (r"\bWebSearch\b|\bWebFetch\b", "WebSearch/WebFetch (say: the platform's search/read-web tool)"),
    (r"https?://", "a URL (sources go to docs/credits.md)"),
]
NEUTRAL_RE = [(re.compile(p, re.IGNORECASE), label) for p, label in NEUTRAL_TERMS]

TEXT_SUFFIXES = {".md", ".txt", ".csv", ".json", ".yml", ".yaml", ".py", ".sh", ".html"}


def is_junk_name(name, is_dir):
    if is_dir:
        return name in JUNK_DIRS
    return any(fnmatch.fnmatch(name.lower(), pat.lower()) for pat in JUNK_FILES)


def skill_dirs(root, neutral_only=False):
    """Yield skill directories (those holding a SKILL.md) under root/packs."""
    for f in sorted(Path(root).glob("packs/**/SKILL.md")):
        d = f.parent
        if neutral_only:
            parts = f.relative_to(root).parts
            if not (parts[1] in NEUTRAL_PACKS or (parts[1] == "starter" and d.name in NEUTRAL_STARTER)):
                continue
        yield d
