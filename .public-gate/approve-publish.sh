#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
GATE="$(cd "$(dirname "$0")" && pwd)"
APPROVAL="$GATE/PUBLISH_APPROVED"
CATALOG="$GATE/publish-pieces.json"
VALIDATOR="$GATE/validate.py"

[[ "$REPO" == *"/Agentico/Agentico-Public"* ]] && { echo "⛔ Agentico-Public must not be inside Agentico/" >&2; exit 1; }
[[ -f "$REPO/.PUBLIC_STAGING_ONLY" ]] || { echo "⛔ Not in Agentico-Public/" >&2; exit 1; }
[[ -f "$CATALOG" ]] || { echo "⛔ Missing publish-pieces catalog" >&2; exit 1; }

echo "========================================================================"
echo "AGENTICO PUBLIC PUBLISH — PIECES ONLY (NOT PROCESS)"
echo "========================================================================"
echo "Repo: $REPO"
echo "Target: https://github.com/Shane-Burns-Dot-US/Agentico-Public"
echo ""
echo "Gate/process files (.public-gate/, GATE_MANIFEST.json) never ship."
echo "You approve content pieces when ready — not the validation pipeline."
echo ""

( cd "$REPO" && python3 "$VALIDATOR" ) || {
  echo "⛔ Staging gate failed — fix issues before approving pieces." >&2
  exit 1
}

mapfile -t PIECE_LINES < <(
  python3 - "$CATALOG" <<'PY'
import json, sys
from pathlib import Path

catalog = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
idx = 1
for section in ("shell", "pieces"):
    for entry in catalog.get(section, []):
        status = entry.get("status", "shell")
        print(f"{idx}\t{entry['id']}\t{entry['path']}\t{entry['title']}\t{status}")
        idx += 1
PY
)

echo "Publishable pieces:"
for line in "${PIECE_LINES[@]}"; do
  IFS=$'\t' read -r num id path title status <<<"$line"
  printf "  [%s] %s — %s (%s) [%s]\n" "$num" "$id" "$title" "$path" "$status"
done
echo ""
echo "Shell (license/disclaimer/mapping) is auto-included when any piece is selected."
echo "Never in scope: private-drafts/ and other local-only paths"
echo ""
read -r -p "Enter piece numbers to approve (comma-separated), or 'none' to abort: " SELECTION
[[ "$SELECTION" != "none" && -n "$SELECTION" ]] || { echo "⛔ No pieces selected." >&2; exit 1; }

mapfile -t APPROVED_PATHS < <(
  python3 - "$CATALOG" "$SELECTION" <<'PY'
import json, sys
from pathlib import Path

catalog = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
raw = sys.argv[2].replace(" ", "")
nums = {int(x) for x in raw.split(",") if x}

entries = []
for section in ("shell", "pieces"):
    entries.extend(catalog.get(section, []))

piece_ids = {e["id"] for e in catalog.get("pieces", [])}
shell_count = len(catalog.get("shell", []))
selected = [entries[i - 1] for i in sorted(nums) if 1 <= i <= len(entries)]
if not any(e["id"] in piece_ids for e in selected):
    raise SystemExit("Select at least one content piece (not shell-only).")

paths = {e["path"] for e in catalog.get("shell", [])}
paths.update(e["path"] for e in selected)
for rel in sorted(paths):
    print(rel)
PY
) || { echo "⛔ Invalid selection." >&2; exit 1; }

echo ""
echo "Pieces approved for push (${#APPROVED_PATHS[@]}):"
for f in "${APPROVED_PATHS[@]}"; do
  echo "  • $f"
done
echo ""
read -r -p "Type PUBLISH-AGENTICO-PUBLIC to approve these pieces only: " CONFIRM
[[ "$CONFIRM" == "PUBLISH-AGENTICO-PUBLIC" ]] || { echo "⛔ Denied." >&2; exit 1; }

{
  echo "approved_at=$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "approved_by=${USER:-unknown}"
  echo "repo=Agentico-Public"
  echo "scope=pieces-explicit"
  for f in "${APPROVED_PATHS[@]}"; do
    echo "approved_file=$f"
  done
} > "$APPROVAL"
chmod 600 "$APPROVAL"
echo "✅ Pieces-only approval token written (${#APPROVED_PATHS[@]} files)."