#!/usr/bin/env bash
# Verify (and optionally repair) GitHub remote mapping for Agentico-Public.
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
CANONICAL="$REPO/GITHUB_REPO.json"
EXPECTED_HTTPS="https://github.com/Shane-Burns-Dot-US/Agentico-Public.git"
EXPECTED_SSH="git@github.com:Shane-Burns-Dot-US/Agentico-Public.git"
FIX=false
[[ "${1:-}" == "--fix" ]] && FIX=true

die() { echo "⛔ $*" >&2; exit 1; }
ok() { echo "✅ $*"; }

[[ -f "$REPO/.PUBLIC_STAGING_ONLY" ]] || die "Not in Agentico-Public/"
[[ -f "$CANONICAL" ]] || die "Missing GITHUB_REPO.json"

if ! python3 -c "
import json, sys
d = json.load(open('$CANONICAL'))
assert d['https_url'] == '$EXPECTED_HTTPS'
assert d['ssh_url'] == '$EXPECTED_SSH'
assert d['owner'] == 'Shane-Burns-Dot-US'
assert d['repo'] == 'Agentico-Public'
"; then
  die "GITHUB_REPO.json does not match canonical Shane-Burns-Dot-US/Agentico-Public"
fi
ok "GITHUB_REPO.json canonical mapping OK"

if [[ ! -d "$REPO/.git" ]]; then
  if $FIX; then
    git -C "$REPO" init -b main
    git -C "$REPO" remote add origin "$EXPECTED_HTTPS"
    ok "Initialized git and set origin"
  else
    die "No .git/ — run: ./.public-gate/verify-github.sh --fix"
  fi
fi

CURRENT="$(git -C "$REPO" remote get-url origin 2>/dev/null || true)"
case "$CURRENT" in
  "$EXPECTED_HTTPS"|"$EXPECTED_SSH") ok "origin remote OK: $CURRENT" ;;
  "")
    if $FIX; then
      git -C "$REPO" remote add origin "$EXPECTED_HTTPS"
      ok "Added origin: $EXPECTED_HTTPS"
    else
      die "No origin remote — run: ./.public-gate/verify-github.sh --fix"
    fi
    ;;
  *)
    if $FIX; then
      git -C "$REPO" remote set-url origin "$EXPECTED_HTTPS"
      ok "Fixed origin: $CURRENT → $EXPECTED_HTTPS"
    else
      die "Wrong origin: $CURRENT (expected Agentico-Public)"
    fi
    ;;
esac

BRANCH="$(git -C "$REPO" branch --show-current 2>/dev/null || true)"
[[ "$BRANCH" == "main" ]] || die "Expected branch 'main', got '${BRANCH:-<none>}'"
ok "Branch: main"

if git -C "$REPO" rev-parse --abbrev-ref main@{upstream} &>/dev/null; then
  UPSTREAM="$(git -C "$REPO" rev-parse --abbrev-ref main@{upstream})"
  [[ "$UPSTREAM" == "origin/main" ]] || die "main should track origin/main (got $UPSTREAM)"
  ok "main tracks origin/main"
elif $FIX; then
  git -C "$REPO" branch --set-upstream-to=origin/main main 2>/dev/null || true
  ok "Set main to track origin/main (after first push)"
fi

if git -C "$REPO" ls-remote origin HEAD &>/dev/null; then
  REMOTE_HEAD="$(git -C "$REPO" ls-remote origin HEAD | awk '{print $1}')"
  LOCAL_HEAD="$(git -C "$REPO" rev-parse HEAD 2>/dev/null || echo none)"
  ok "Remote reachable — origin/HEAD ${REMOTE_HEAD:0:8}"
  echo "   Local HEAD: ${LOCAL_HEAD:0:8}"
else
  echo "⚠️  Could not reach remote (network/auth) — local mapping still verified"
fi

echo ""
echo "Mapped to: https://github.com/Shane-Burns-Dot-US/Agentico-Public"