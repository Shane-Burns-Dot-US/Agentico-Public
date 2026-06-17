#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
GATE="$(cd "$(dirname "$0")" && pwd)"
VALIDATOR="$GATE/validate.py"
APPROVAL="$GATE/PUBLISH_APPROVED"

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

die() { echo -e "${RED}⛔ $*${NC}" >&2; exit 1; }
ok() { echo -e "${GREEN}✅ $*${NC}"; }

[[ "$REPO" == *"/Agentico/Agentico-Public"* ]] && die "Agentico-Public must not be inside Agentico/"
[[ -f "$REPO/.PUBLIC_STAGING_ONLY" ]] || die "Missing .PUBLIC_STAGING_ONLY — wrong directory?"
[[ -f "$APPROVAL" ]] || die "Missing PUBLISH_APPROVED — run: ./.public-gate/approve-publish.sh"

mapfile -t APPROVED_FILES < <(grep '^approved_file=' "$APPROVAL" | cut -d= -f2-)
[[ "${#APPROVED_FILES[@]}" -gt 0 ]] || die "No approved pieces in PUBLISH_APPROVED"

"$GATE/verify-github.sh" || die "GitHub mapping check failed — run: ./.public-gate/verify-github.sh --fix"

if [[ -d "$REPO/.git" ]]; then
  REMOTE_URL="$(git -C "$REPO" remote get-url origin 2>/dev/null || true)"
  case "$REMOTE_URL" in
    *Agentico-Public*) ;;
    *) die "origin must be Agentico-Public. Got: ${REMOTE_URL:-<none>}" ;;
  esac
fi

echo "========================================================================"
echo "AGENTICO PUBLIC PUBLISH — PIECES ONLY"
echo "========================================================================"
echo "Repo: $REPO"
echo "Approved pieces: ${#APPROVED_FILES[@]}"
for f in "${APPROVED_FILES[@]}"; do echo "  • $f"; done
echo ""

( cd "$REPO" && python3 "$VALIDATOR" --for-publish ) || die "Gate validation failed."

git -C "$REPO" status --short 2>/dev/null || true
echo ""
read -r -p "Type PUSH-PUBLIC to push approved pieces only: " FINAL
[[ "$FINAL" == "PUSH-PUBLIC" ]] || die "Push cancelled."

if [[ ! -d "$REPO/.git" ]]; then
  git -C "$REPO" init -b main
  git -C "$REPO" remote add origin "https://github.com/Shane-Burns-Dot-US/Agentico-Public.git"
fi

MISSING=0
for f in "${APPROVED_FILES[@]}"; do
  [[ -f "$REPO/$f" ]] || { echo "⛔ Missing approved piece: $f" >&2; MISSING=1; }
done
[[ "$MISSING" -eq 0 ]] || die "One or more approved pieces are missing on disk."

for f in "${APPROVED_FILES[@]}"; do
  git -C "$REPO" add -- "$f"
done

if [[ -n "$(git -C "$REPO" diff --cached --name-only 2>/dev/null)" ]]; then
  git -C "$REPO" commit -m "Publish approved Agentico research pieces"
fi

git -C "$REPO" push -u origin main 2>/dev/null || git -C "$REPO" push -u origin master
rm -f "$APPROVAL"
ok "Published approved pieces only. Approval token revoked."