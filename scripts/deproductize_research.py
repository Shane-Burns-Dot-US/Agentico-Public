#!/usr/bin/env python3
"""Remove Agentico commercial product content from docs/ in Agentico-Public."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
GITHUB_RESEARCH = "https://github.com/Shane-Burns-Dot-US/Agentico-Public"
DRAFT_NOTICE = (
    "DRAFT · NOT LEGAL ADVICE · Illustrative only · Not a law firm · Not a bank · "
    "Outcomes not assured"
)

REMOVE_SECTION_PATTERNS = [
    r"Agentico MCP workflow",
    r"How Agentico implements",
    r"Step 1: Form the series with Agentico",
    r"Comparison: Agentico vs",
    r"Comparison: formation paths for Wyoming Series LLC",
    r"Comparison: wrapper approaches",
    r"MCP verbs reference",
    r"SDK error handling",
    r"Pricing and total cost of ownership",
    r"Pricing and cost stack",
    r"^Pricing reference$",
    r"^Pricing$",
    r"Governance: human_approval and MCP verbs",
    r"Build vs\. buy: legal infrastructure",
    r"MCP verbs \(all posts\)",
    r"Post index \(10 posts",
    r"Staged locked",
    r"STAGED CONTENT",
]

FRONTMATTER_KEYS_TO_DROP = {
    "related_product_url",
    "canonical_product_url",
    "official_website",
    "related_product",
    "staged_posts_locked_until",
}

BANNED_PATTERNS = {
    "agentico.llc": re.compile(r"agentico\.llc", re.I),
    "@agentico": re.compile(r"@agentico", re.I),
    "$295": re.compile(r"\$295"),
    "establish_master": re.compile(r"\bestablish_master\b"),
    "doola": re.compile(r"\bdoola\b", re.I),
    "OtoCo": re.compile(r"\bOtoCo\b"),
}


def remove_sections(text: str, patterns: list[str]) -> str:
    lines = text.splitlines()
    out: list[str] = []
    skip = False
    skip_level = 0
    for line in lines:
        m = re.match(r"^(#{2,6})\s+(.+)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if any(re.search(pat, title, re.IGNORECASE) for pat in patterns):
                skip = True
                skip_level = level
                continue
            if skip and level <= skip_level:
                skip = False
        if skip:
            continue
        out.append(line)
    return "\n".join(out)


def remove_code_blocks_with_product(text: str) -> str:
    parts = re.split(r"(```[^\n]*\n.*?```)", text, flags=re.DOTALL)
    cleaned: list[str] = []
    for part in parts:
        if part.startswith("```") and (
            "@agentico" in part
            or "AgenticoClient" in part
            or "establish_master" in part
            or "incorporate_agent" in part
        ):
            continue
        cleaned.append(part)
    return "".join(cleaned)


def clean_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    if end == -1:
        return text
    fm = text[3:end].splitlines()
    kept: list[str] = []
    skip_block = False
    drop_keys = FRONTMATTER_KEYS_TO_DROP | {"target_questions", "target_phrases"}
    for line in fm:
        key_match = re.match(r"^([a-z_]+):", line)
        if key_match:
            key = key_match.group(1)
            skip_block = key in drop_keys
            if skip_block:
                continue
            kept.append(line)
        elif skip_block:
            continue
        else:
            kept.append(line)
    return "---\n" + "\n".join(kept) + "\n---" + text[end + 4 :]


def apply_text_replacements(text: str) -> str:
    rules: list[tuple[str, str]] = [
        (r"https?://(?:www\.)?agentico\.llc[^\s\)\]\"']*", GITHUB_RESEARCH),
        (r"\[([^\]]+)\]\(https?://(?:www\.)?agentico\.llc[^\)]*\)", rf"[\1]({GITHUB_RESEARCH})"),
        (r"@agentico/sdk", "counsel-guided workflow"),
        (r"\*\*Agentico\*\* automates[^\n]*", "**Research** discusses formation steps"),
        (r"Agentico automates[^\n]*", "Formation research discusses"),
        (r"\*\*Agentico\*\* is (?:built|purpose-built)[^\n]*", "**Wyoming Series LLC** is commonly discussed in this research"),
        (r"Use \*\*Agentico\*\* to", "Work with **counsel** to"),
        (r"With \*\*Agentico\*\*", "With **counsel-reviewed documents**"),
        (r"\| \*\*Pricing\*\* \|[^\n]*\n", ""),
        (r"\| Pricing[^\n]*\n", ""),
        (r"\(\*\*\s*\n", "\n"),
        (r"file with counsel \(\*\*", "file with counsel."),
        (r"counsel-reviewed formation workflow", "counsel-guided workflow"),
        (r"formation steps\s+generation", "formation document steps"),
        (r"\| \*\*Agentico\*\* \| Templates \+ MCP[^\n]*\n", "| **Research** | Draft essays only — **not** a law firm or bank |\n"),
        (r"file with counsel \s*\n---", "file with counsel. **Not legal advice.**\n\n---"),
        (r"`establish_master`", "master LLC formation"),
        (r"`incorporate_agent`", "series formation"),
        (r"`sign_contract`", "contract recording"),
        (r"`spawn_subsidiary`", "subsidiary series creation"),
        (r"`wind_down`", "series wind-down"),
        (r"\bestablish_master\b", "master LLC formation"),
        (r"\bincorporate_agent\b", "series formation"),
        (r"\bsign_contract\b", "contract recording"),
        (r"\bspawn_subsidiary\b", "subsidiary series creation"),
        (r"\bwind_down\b", "series wind-down"),
        (r"\bOtoCo\b", "on-chain formation platforms"),
        (r"\bdoola\b", "online formation services"),
        (r"\$295[^\n]*", ""),
        (r"\$29/mo[^\n]*", ""),
        (r"purpose-built for (?:Agentico|MCP-native )", "discussed in research on "),
        (r"MCP-native formation product", "MCP workflow research"),
        (r"AgenticoClient", ""),
        (r"related_product_url:.*\n", ""),
        (r"canonical_product_url:.*\n", ""),
        (r"official_website:.*agentico\.llc.*\n", ""),
        (r"agentico\.llc", ""),
        (r"www\.agentico\.llc", ""),
        (r"STAGED_CONTENT_ALERT\.md", "content-lifecycle.md"),
    ]
    for pattern, repl in rules:
        text = re.sub(pattern, repl, text, flags=re.IGNORECASE)
    return text


def drop_lines_with_banned_terms(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if any(p.search(line) for p in BANNED_PATTERNS.values()):
            if line.strip().startswith("|"):
                continue
            continue
        lines.append(line)
    return "\n".join(lines)


def process_markdown_file(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    text = clean_frontmatter(text)
    text = remove_sections(text, REMOVE_SECTION_PATTERNS)
    text = remove_code_blocks_with_product(text)
    text = apply_text_replacements(text)
    text = drop_lines_with_banned_terms(text)
    text = re.sub(r"## Copy for AI\n+(?=##|\Z|---)", "", text)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.rstrip() + "\n"


def process_schema_file(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data.get("publisher"), dict) and "agentico.llc" in str(data["publisher"].get("url", "")):
        data["publisher"] = {
            "@type": "ResearchProject",
            "name": "Agentico — The Incorporation of Agents in America",
            "url": GITHUB_RESEARCH,
        }
    data.pop("mentions", None)
    if isinstance(data.get("keywords"), list):
        data["keywords"] = [k for k in data["keywords"] if k != "establish_master"]
    blob = json.dumps(data, indent=2, ensure_ascii=False)
    blob = apply_text_replacements(blob)
    blob = drop_lines_with_banned_terms(blob)
    return json.dumps(json.loads(blob), indent=2, ensure_ascii=False) + "\n"


def update_publish_pieces(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    for piece in data.get("pieces", []):
        if piece.get("status") == "awaiting_approval":
            piece["status"] = "draft"
            for key in ("redteam_cleared", "whiteteam_cleared", "gate_commit", "branch", "ship_note"):
                piece.pop(key, None)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def update_gate_config() -> None:
    cfg_path = REPO / ".public-gate" / "config.json"
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    allowed = cfg.setdefault("allowed_top_level_in_staging", [])
    if "scripts" not in allowed:
        allowed.append("scripts")
        allowed.sort()
        cfg_path.write_text(json.dumps(cfg, indent=2) + "\n", encoding="utf-8")


def verify_docs_clean() -> list[str]:
    violations: list[str] = []
    for path in sorted(DOCS.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for name, pat in BANNED_PATTERNS.items():
            if pat.search(text):
                violations.append(f"{path.relative_to(REPO)}: {name}")
    return violations


def main() -> int:
    sys.path.insert(0, str(Path(__file__).parent))
    from deproductize_content import FULL_MARKDOWN, FULL_JSONLD

    changed: list[str] = []

    for rel, content in FULL_MARKDOWN.items():
        target = DOCS / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.read_text(encoding="utf-8") != content:
            target.write_text(content, encoding="utf-8")
            changed.append(str(target.relative_to(REPO)))

    for rel, obj in FULL_JSONLD.items():
        target = DOCS / rel
        new_text = json.dumps(obj, indent=2, ensure_ascii=False) + "\n"
        if target.read_text(encoding="utf-8") != new_text:
            target.write_text(new_text, encoding="utf-8")
            changed.append(str(target.relative_to(REPO)))

    skip_md = {DOCS / k for k in FULL_MARKDOWN}
    for md in sorted(DOCS.rglob("*.md")):
        if md in skip_md:
            continue
        new_text = process_markdown_file(md)
        if md.read_text(encoding="utf-8") != new_text:
            md.write_text(new_text, encoding="utf-8")
            changed.append(str(md.relative_to(REPO)))

    skip_json = {DOCS / k for k in FULL_JSONLD}
    for jf in sorted(DOCS.rglob("*.jsonld.json")):
        if jf in skip_json:
            continue
        new_text = process_schema_file(jf)
        if jf.read_text(encoding="utf-8") != new_text:
            jf.write_text(new_text, encoding="utf-8")
            changed.append(str(jf.relative_to(REPO)))

    pp = REPO / ".public-gate" / "publish-pieces.json"
    old_pp = pp.read_text(encoding="utf-8")
    update_publish_pieces(pp)
    if pp.read_text(encoding="utf-8") != old_pp:
        changed.append(".public-gate/publish-pieces.json")

    update_gate_config()
    subprocess.run([sys.executable, str(REPO / ".public-gate" / "update-manifest.py")], check=True, cwd=str(REPO))
    changed.append("GATE_MANIFEST.json")

    violations = verify_docs_clean()
    print("=" * 72)
    print("DEPRODUCTIZE RESEARCH — SUMMARY")
    print("=" * 72)
    print(f"Files changed: {len(changed)}")
    for f in sorted(set(changed)):
        print(f"  - {f}")
    print("-" * 72)
    if violations:
        print("Grep verification: FAIL")
        for v in violations:
            print(f"  {v}")
        return 1
    print("Grep verification: PASS (no agentico.llc, @agentico, $295, establish_master, doola, OtoCo)")
    return 0


if __name__ == "__main__":
    sys.exit(main())