#!/usr/bin/env python3
"""Copy a rewritten skill into a pack: drops junk (see scripts/lib/skill_rules.py) and cuts the
frontmatter down to name + description. Does not touch the skill's wording.
Usage: import-skill.py <skill-dir> <pack> [--force]   -> packs/<pack>/skills/<name>/
Then: write docs/skills/<name>.md, add the credits row, run sh scripts/ci.sh."""
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "lib"))
from skill_rules import is_junk_name  # noqa: E402

root = Path(__file__).resolve().parent.parent


def slim_frontmatter(text):
    """Keep only top-level `name` and `description` (with their indented continuation lines)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise SystemExit("SKILL.md has no frontmatter")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        raise SystemExit("SKILL.md frontmatter is not closed")
    keep, on = [], False
    for line in lines[1:end]:
        m = re.match(r"^([A-Za-z0-9_-]+):", line)
        if m:
            on = m.group(1) in ("name", "description")
        if on:
            keep.append(line)
    return "\n".join(["---", *keep, "---", *lines[end + 1:]]) + "\n"


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    force = "--force" in argv
    if len(args) != 2:
        raise SystemExit(__doc__)
    src, pack = Path(args[0]).resolve(), args[1]
    if not (src / "SKILL.md").is_file():
        raise SystemExit(f"{src} has no SKILL.md")
    if not (root / "packs" / pack).is_dir():
        raise SystemExit(f"packs/{pack} does not exist")
    dest = root / "packs" / pack / "skills" / src.name
    if dest.exists():
        if not force:
            raise SystemExit(f"{dest.relative_to(root).as_posix()} exists; use --force to replace it")
        shutil.rmtree(dest)
    dropped = []
    for f in sorted(src.rglob("*")):
        rel = f.relative_to(src)
        if any(is_junk_name(p, True) for p in rel.parts[:-1]) or is_junk_name(rel.name, f.is_dir()):
            dropped.append(rel.as_posix())
            continue
        if f.is_dir():
            continue
        out = dest / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        if rel.as_posix() == "SKILL.md":
            out.write_text(slim_frontmatter(f.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        else:
            shutil.copy2(f, out)
    print(f"imported {src.name} -> {dest.relative_to(root).as_posix()}")
    for d in dropped:
        print(f"  dropped {d}")
    print(f"next: docs/skills/{src.name}.md (from docs/templates/skill-page.md), a row in docs/credits.md, sh scripts/ci.sh")


main(sys.argv[1:])
