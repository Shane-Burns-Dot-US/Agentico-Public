#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LOCAL_ONLY = {"private-drafts"}
MANIFEST = REPO / "GATE_MANIFEST.json"


def is_local(rel: str) -> bool:
    return any(rel == d or rel.startswith(f"{d}/") for d in LOCAL_ONLY)


files = sorted(
    p.relative_to(REPO).as_posix()
    for p in REPO.rglob("*")
    if p.is_file()
    and ".git" not in p.parts
    and not is_local(p.relative_to(REPO).as_posix())
    and p.relative_to(REPO).as_posix() != ".public-gate/PUBLISH_APPROVED"
)

data = {
    "description": "Explicit allowlist of publishable files in Agentico-Public/.",
    "public_repo": "https://github.com/Shane-Burns-Dot-US/Agentico-Public",
    "files": files,
}
MANIFEST.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
print(f"Updated {MANIFEST} ({len(files)} files)")