#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
RISK=0

bad() { echo "⛔ $*"; RISK=2; }

[[ "$REPO" == *"/Agentico/"* ]] && bad "Agentico-Public is inside Agentico/ — move to Desktop"
[[ -d "$(dirname "$REPO")/Agentico/.public-gate" ]] && bad "Remove Agentico/.public-gate — gate lives only in Agentico-Public/"

for f in .env config.yaml auth.lock SOUL.md hermes; do
  [[ -f "$REPO/$f" ]] && bad "Private runtime file in public repo: $f"
done

if [[ -d "$REPO/.git" ]]; then
  ORIGIN="$(git -C "$REPO" remote get-url origin 2>/dev/null || true)"
  [[ -n "$ORIGIN" && "$ORIGIN" != *"Agentico-Public"* ]] && bad "Wrong git remote: $ORIGIN"
fi

[[ "$RISK" -eq 0 ]] && echo "✅ No leak risks detected" && exit 0
echo "⛔ Critical leak risks — do not publish"
exit 2