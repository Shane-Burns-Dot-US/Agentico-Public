#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
HOOK_SRC="$REPO/.public-gate/hooks"
HOOK_DST="$REPO/.git/hooks"

mkdir -p "$HOOK_DST"
for hook in pre-commit pre-push; do
  install -m 755 "$HOOK_SRC/$hook" "$HOOK_DST/$hook"
  echo "Installed $hook"
done