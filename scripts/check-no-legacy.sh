#!/bin/sh
# Fails if OpenMausBot/Grok legacy leftovers exist, or AGENTS.md and CLAUDE.md differ.
cd "$(dirname "$0")/.." || exit 2
fail=0
hits=$(git grep -niE 'openmaus|grok|botmrr|field-mapping' -- . ':!scripts/check-no-legacy.sh' ':!AGENTS.md' ':!CLAUDE.md' | grep -v 'v0-openmausbot')
if [ -n "$hits" ]; then echo "legacy references:"; echo "$hits"; fail=1; fi
for p in guides packs/ecommerce team.md; do
  if [ -e "$p" ]; then echo "legacy path exists: $p"; fail=1; fi
done
cmp -s AGENTS.md CLAUDE.md || { echo "AGENTS.md and CLAUDE.md differ"; fail=1; }
[ $fail -eq 0 ] && echo "ok"
exit $fail
