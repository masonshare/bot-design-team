# Changelog template

Read this when writing a MAJOR entry or the first entry for a skill. Adapted from Masonshare's distill-to-skill templates.

One entry per version bump. A reader should see what changed, why, and how to go back.

```markdown
## v<X.Y.Z> - <YYYY-MM-DD>

**Bump:** PATCH | MINOR | MAJOR
**Backward compatible:** yes | no
**Driver:** <one line: the failure or request that caused the change>

### Changes
- Added: <new section, field or file>
- Changed: <what was altered>
- Removed: <what was deleted; MAJOR only>
- Fixed: <bug or typo>

### Migration
<"none" for PATCH and MINOR; for MAJOR, exact instructions, such as "skill X is now skills A and B">

### Rollback
<the git tag or commit to return to, for example: git checkout v<previous> -- skills/<name>>
```

## Worked entry

```markdown
## v2.0.0 - 2026-11-19

**Bump:** MAJOR
**Backward compatible:** no
**Driver:** one 15 KB skill loaded in full for single-stage jobs; split into six skills, one per job.

### Changes
- Added: skill-search, skill-write, skill-test, skill-review, skill-package
- Changed: skill-design is now a short router
- Removed: nothing

### Migration
Install all six. A prompt that named step numbers of the old skill now names a skill.

### Rollback
git checkout v1.1.0 -- skills/skill-design
```

Bump rules: PATCH for wording, typos and description tightening with no behaviour change. MINOR for new sections, scripts or references where old use still works. MAJOR for renamed steps, changed output format, changed defaults, removed fields or a split. Torn between two levels: take the higher.
