#!/bin/sh
# Fail if any __pycache__ content or *.pyc file is tracked by git.
cd "$(dirname "$0")/.." || exit 2
git rev-parse --git-dir >/dev/null 2>&1 || { echo "not a git checkout, skipped"; exit 0; }
bad=$(git ls-files | grep -E '(^|/)__pycache__/|\.pyc$')
if [ -n "$bad" ]; then
  echo "FAIL tracked build artifacts (git rm --cached them):"; echo "$bad"; exit 1
fi
echo "no tracked __pycache__ or .pyc"
