#!/usr/bin/env python3
"""Multi-layer gate validator for Agentico-Public on Desktop.

Lives entirely inside Agentico-Public/. Nothing in Agentico/ is required.
"""

from __future__ import annotations

import fnmatch
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class GateResult:
    passed: int = 0
    failures: list[str] = field(default_factory=list)

    def ok(self, name: str) -> None:
        self.passed += 1
        print(f"  [PASS] {name}")

    def fail(self, name: str, detail: str) -> None:
        self.failures.append(f"{name}: {detail}")
        print(f"  [FAIL] {name}: {detail}")


def load_config(gate_dir: Path) -> dict:
    with open(gate_dir / "config.json", encoding="utf-8") as f:
        return json.load(f)


def resolve_paths() -> tuple[Path, Path]:
    gate_dir = Path(__file__).resolve().parent
    repo_root = gate_dir.parent
    return repo_root, gate_dir


def matches_any(name: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(name, pat) for pat in patterns)


def is_local_only(rel_posix: str, config: dict) -> bool:
    for d in config.get("local_only_dirs", []):
        if rel_posix == d or rel_posix.startswith(f"{d}/"):
            return True
    return False


def is_gate_path(rel_posix: str, config: dict) -> bool:
    gate = config.get("gate_dir", ".public-gate")
    return rel_posix == gate or rel_posix.startswith(f"{gate}/")


def check_01_desktop_partition(repo_root: Path, config: dict, result: GateResult) -> None:
    forbidden = config.get("forbidden_parent_dir", "Agentico")
    parts = repo_root.resolve().parts
    if forbidden in parts:
        idx = parts.index(forbidden)
        if idx < len(parts) - 1 and parts[idx + 1] == config.get("repo_dir_name", "Agentico-Public"):
            result.fail("CHECK-01", f"Agentico-Public must not live inside {forbidden}/")
            return
    agentico_gate = repo_root.parent / forbidden / ".public-gate"
    if agentico_gate.exists():
        result.fail("CHECK-01", f"Remove {forbidden}/.public-gate — gate belongs only in Agentico-Public/")
        return
    if repo_root.name != config.get("repo_dir_name", "Agentico-Public"):
        result.fail("CHECK-01", f"Repo folder must be named Agentico-Public (got {repo_root.name})")
        return
    result.ok("CHECK-01: Agentico-Public is independent on Desktop")


def check_02_staging_marker(repo_root: Path, result: GateResult) -> None:
    marker = repo_root / ".PUBLIC_STAGING_ONLY"
    if not marker.is_file():
        result.fail("CHECK-02", "Missing .PUBLIC_STAGING_ONLY at repo root")
        return
    result.ok("CHECK-02: Public staging marker present")


def check_03_no_private_runtime_paths(repo_root: Path, config: dict, result: GateResult) -> None:
    blocked_dirs = set(config["blocked_directory_names"])
    blocked_files = config["blocked_filenames"]
    local_only = set(config.get("local_only_dirs", []))
    violations: list[str] = []

    for root, dirs, files in os.walk(repo_root):
        dirs[:] = [d for d in dirs if d != ".git"]
        rel_root = Path(root).relative_to(repo_root)
        rel_root_posix = rel_root.as_posix() if str(rel_root) != "." else ""
        if rel_root.parts and rel_root.parts[0] in local_only:
            dirs.clear()
            continue
        if is_gate_path(rel_root_posix, config):
            continue
        for d in list(dirs):
            if d in local_only:
                continue
            if d in blocked_dirs:
                violations.append(str(rel_root / d) if str(rel_root) != "." else d)
            elif d.startswith(".") and d not in {".public-gate"}:
                violations.append(str(rel_root / d) if str(rel_root) != "." else d)
        for f in files:
            if rel_root.parts and rel_root.parts[0] in local_only:
                continue
            allowed_dotfiles = {".gitignore", ".PUBLIC_STAGING_ONLY", ".gitkeep"}
            if matches_any(f, blocked_files) or (
                f.startswith(".") and f not in allowed_dotfiles
            ):
                violations.append(str(rel_root / f) if str(rel_root) != "." else f)

    if violations:
        result.fail("CHECK-03", f"Blocked private-runtime paths: {violations[:10]}")
        return
    result.ok("CHECK-03: No private-runtime paths in publishable tree")


def check_04_allowlist_top_level(repo_root: Path, config: dict, result: GateResult) -> None:
    allowed = set(config["allowed_top_level_in_staging"])
    actual = {p.name for p in repo_root.iterdir()}
    extra = sorted(actual - allowed - {".git"})
    if extra:
        result.fail("CHECK-04", f"Unexpected top-level entries: {extra}")
        return
    result.ok("CHECK-04: Top-level contents match allowlist")


def check_05_manifest_coverage(repo_root: Path, config: dict, result: GateResult) -> None:
    manifest_path = repo_root / "GATE_MANIFEST.json"
    if not manifest_path.is_file():
        result.fail("CHECK-05", "Missing GATE_MANIFEST.json")
        return

    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)

    declared = set(manifest.get("files", []))
    discovered: set[str] = set()
    for path in repo_root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(repo_root).as_posix()
        if is_local_only(rel, config):
            continue
        if rel == ".public-gate/PUBLISH_APPROVED":
            continue
        discovered.add(rel)

    undeclared = sorted(discovered - declared)
    ghost = sorted(declared - discovered)
    if undeclared or ghost:
        parts = []
        if undeclared:
            parts.append(f"undeclared: {undeclared[:8]}")
        if ghost:
            parts.append(f"missing: {ghost[:8]}")
        result.fail("CHECK-05", "; ".join(parts))
        return
    result.ok("CHECK-05: GATE_MANIFEST.json matches publishable files exactly")


def check_06_secret_scan(repo_root: Path, config: dict, result: GateResult) -> None:
    patterns = [re.compile(p) for p in config["secret_patterns"]]
    hits: list[str] = []

    for path in repo_root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(repo_root).as_posix()
        if is_local_only(rel, config):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            for pat in patterns:
                if pat.search(line):
                    hits.append(f"{rel}:{i}")
                    break

    if hits:
        result.fail("CHECK-06", f"Potential secrets: {hits[:8]}")
        return
    result.ok("CHECK-06: No secret patterns detected")


def check_07_private_string_scan(repo_root: Path, config: dict, result: GateResult) -> None:
    needles = config["blocked_path_substrings"]
    hits: list[str] = []

    for path in repo_root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(repo_root).as_posix()
        if is_local_only(rel, config) or is_gate_path(rel, config):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for needle in needles:
            if needle in text:
                hits.append(f"{rel} contains blocked substring")
                break

    if hits:
        result.fail("CHECK-07", f"Private markers in content: {hits[:8]}")
        return
    result.ok("CHECK-07: No private-runtime substrings in content")


def check_08_symlink_safety(repo_root: Path, result: GateResult) -> None:
    unsafe: list[str] = []
    for path in repo_root.rglob("*"):
        if path.is_symlink():
            target = path.resolve()
            try:
                target.relative_to(repo_root.resolve())
            except ValueError:
                unsafe.append(f"{path.relative_to(repo_root)} -> {target}")

    if unsafe:
        result.fail("CHECK-08", f"Symlinks escape repo: {unsafe}")
        return
    result.ok("CHECK-08: No symlinks escape Agentico-Public/")


def check_09_github_canonical(repo_root: Path, config: dict, result: GateResult) -> None:
    mapping_path = repo_root / "GITHUB_REPO.json"
    if not mapping_path.is_file():
        result.fail("CHECK-09", "Missing GITHUB_REPO.json canonical mapping")
        return
    with open(mapping_path, encoding="utf-8") as f:
        mapping = json.load(f)
    expected = {
        "owner": config["public_repo_owner"],
        "repo": config["public_repo_name"],
        "https_url": config["public_repo_url"],
        "ssh_url": config["public_repo_ssh"],
    }
    for key, val in expected.items():
        if mapping.get(key) != val:
            result.fail("CHECK-09", f"GITHUB_REPO.json {key} mismatch")
            return
    git_config = repo_root / ".git" / "config"
    if git_config.is_file():
        text = git_config.read_text(encoding="utf-8")
        if config["public_repo_url"] not in text and config["public_repo_ssh"] not in text:
            result.fail("CHECK-09", ".git/config missing Agentico-Public origin URL")
            return
    result.ok("CHECK-09: Canonical GitHub mapping (GITHUB_REPO.json + .git/config)")


def check_10_git_remote(repo_root: Path, config: dict, result: GateResult) -> None:
    if not (repo_root / ".git").exists():
        result.fail("CHECK-10", "Agentico-Public is not a git repository")
        return

    proc = subprocess.run(
        ["git", "-C", str(repo_root), "remote", "-v"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        result.fail("CHECK-10", "Unable to read git remotes")
        return

    allowed = {config["public_repo_url"], config["public_repo_ssh"]}
    origin_urls = [line.split()[1] for line in proc.stdout.strip().splitlines() if line.startswith("origin")]
    if not origin_urls:
        result.fail("CHECK-10", "No origin remote configured")
        return
    if any(url not in allowed for url in origin_urls):
        result.fail("CHECK-10", f"origin must be Agentico-Public only; got {origin_urls}")
        return
    result.ok("CHECK-10: Git origin locked to Agentico-Public")


def is_negated_claim_line(line: str) -> bool:
    lowered = line.lower()
    negation_markers = (
        "no guaranteed",
        "not guaranteed",
        "does not guarantee",
        "do not guarantee",
        "nothing is guaranteed",
        "outcomes not guaranteed",
        "outcomes not assured",
        "not assured",
        "not promise",
        "does not promise",
        "do not promise",
        "must not",
        "do not claim",
        "does not claim",
        "what we do not claim",
        "not be read to promise",
        "target query also phrased",
        "not recognized",
        "does not become",
        "not a legal person",
        "not ai personhood",
        "personhood and entity status are distinct",
        "entity-level contracting capacity (not ai personhood)",
        "clarify human",
        "human overseer",
        "human accountable",
    )
    return any(marker in lowered for marker in negation_markers)


def marketing_scan_lines(text: str) -> list[tuple[int, str]]:
    """Return (1-based line number, line) for publishable body only — skips YAML frontmatter."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4 :]
    lines: list[tuple[int, str]] = []
    for i, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("target_questions:") or stripped.startswith("target_phrases:"):
            continue
        if stripped.startswith("- ") and (
            "personhood" in stripped.lower() or "responsible party" in stripped.lower()
        ):
            # SEO metadata bullets — not affirmative marketing copy
            continue
        lines.append((i, line))
    return lines


def is_process_path(rel_posix: str, config: dict) -> bool:
    for prefix in config.get("publish_process_paths", []):
        if rel_posix == prefix.rstrip("/") or rel_posix.startswith(prefix):
            return True
    name = Path(rel_posix).name
    return matches_any(rel_posix, config.get("publish_process_globs", [])) or matches_any(
        name, config.get("publish_process_globs", [])
    )


def load_publish_piece_paths(repo_root: Path, gate_dir: Path, config: dict) -> set[str]:
    catalog_rel = config.get("publish_pieces_catalog", ".public-gate/publish-pieces.json")
    catalog_path = repo_root / catalog_rel
    if not catalog_path.is_file():
        catalog_path = gate_dir / "publish-pieces.json"
    if not catalog_path.is_file():
        return set()

    with open(catalog_path, encoding="utf-8") as f:
        catalog = json.load(f)

    paths: set[str] = set()
    for section in ("shell", "pieces"):
        for entry in catalog.get(section, []):
            path = entry.get("path")
            if path:
                paths.add(path)
    return paths


def collect_marketing_scan_files(repo_root: Path, config: dict) -> list[Path]:
    excluded = set(config.get("marketing_scan_excluded_files", []))
    globs = config.get("marketing_scan_globs", ["README.md", "docs/*.md"])
    found: set[Path] = set()
    for pattern in globs:
        for path in repo_root.glob(pattern):
            if not path.is_file():
                continue
            rel = path.relative_to(repo_root).as_posix()
            if rel in excluded or is_local_only(rel, config):
                continue
            found.add(path)
    return sorted(found)


def check_11_publish_approval(
    repo_root: Path, gate_dir: Path, config: dict, result: GateResult
) -> None:
    approval = gate_dir / "PUBLISH_APPROVED"
    if not approval.is_file():
        result.fail("CHECK-11", "Missing PUBLISH_APPROVED — run: ./.public-gate/approve-publish.sh")
        return

    piece_paths = load_publish_piece_paths(repo_root, gate_dir, config)
    if not piece_paths:
        result.fail("CHECK-11", "Missing publish-pieces catalog")
        return

    approved_files: set[str] = set()
    scope_mode = ""
    for line in approval.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("approved_file="):
            approved_files.add(line.split("=", 1)[1])
        elif line.startswith("scope="):
            scope_mode = line.split("=", 1)[1]

    if not approved_files:
        result.fail("CHECK-11", "PUBLISH_APPROVED missing approved_file= piece lines")
        return

    if scope_mode != "pieces-explicit":
        result.fail("CHECK-11", "PUBLISH_APPROVED must use scope=pieces-explicit")
        return

    blocked = set(config.get("blocked_publish_filenames", []))
    blocked_globs = config.get("blocked_publish_filename_globs", [])
    scope_violations: list[str] = []
    for rel in sorted(approved_files):
        name = Path(rel).name
        if name in blocked or matches_any(name, blocked_globs):
            scope_violations.append(f"blocked internal doc in scope: {rel}")
        if is_process_path(rel, config):
            scope_violations.append(f"process path cannot ship: {rel}")
        if rel not in piece_paths:
            scope_violations.append(f"not a registered publish piece: {rel}")

    if scope_violations:
        result.fail("CHECK-11", "; ".join(scope_violations[:8]))
        return

    result.ok(f"CHECK-11: Pieces-only publish approval verified ({len(approved_files)} files)")


def jsonld_marketing_strings(path: Path) -> list[tuple[str, str]]:
    """Extract answer/description fields only — skip FAQ Question names (SEO queries)."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    found: list[tuple[str, str]] = []
    if data.get("@type") == "FAQPage":
        for q in data.get("mainEntity", []):
            ans = q.get("acceptedAnswer", {}).get("text", "")
            if ans:
                found.append(("acceptedAnswer", ans))
    else:
        for key in ("description",):
            val = data.get(key, "")
            if val:
                found.append((key, val))
    return found


def check_13_marketing_claims(repo_root: Path, config: dict, result: GateResult) -> None:
    patterns = [re.compile(p) for p in config.get("marketing_claim_patterns", [])]
    if not patterns:
        result.ok("CHECK-13: Marketing claim scan skipped (no patterns)")
        return

    hits: list[str] = []
    for path in collect_marketing_scan_files(repo_root, config):
        rel = path.relative_to(repo_root).as_posix()
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        if path.suffix == ".json" and path.name.endswith(".jsonld.json"):
            for field, blob in jsonld_marketing_strings(path):
                if is_negated_claim_line(blob):
                    continue
                for pat in patterns:
                    if pat.search(blob):
                        hits.append(f"{rel}:{field}")
                        break
            continue
        for i, line in marketing_scan_lines(text):
            if is_negated_claim_line(line):
                continue
            for pat in patterns:
                if pat.search(line):
                    hits.append(f"{rel}:{i}")
                    break

    if hits:
        result.fail("CHECK-13", f"Overstrong marketing claims: {hits[:8]}")
        return
    result.ok("CHECK-13: No banned marketing claims in public-facing copy")


def check_14_internal_doc_block(repo_root: Path, config: dict, result: GateResult) -> None:
    blocked = set(config.get("blocked_publish_filenames", []))
    blocked_globs = config.get("blocked_publish_filename_globs", [])
    violations: list[str] = []

    for path in repo_root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(repo_root).as_posix()
        if is_local_only(rel, config):
            continue
        name = path.name
        if name in blocked or matches_any(name, blocked_globs):
            violations.append(rel)

    if violations:
        result.fail(
            "CHECK-14",
            f"Internal legal docs outside private-drafts/: {violations}",
        )
        return
    result.ok("CHECK-14: No internal legal analyses in publishable tree")


def check_12_cwd_safety(repo_root: Path, result: GateResult) -> None:
    cwd = Path.cwd().resolve()
    try:
        cwd.relative_to(repo_root.resolve())
    except ValueError:
        result.fail("CHECK-12", f"Gate must run with cwd inside Agentico-Public/ (cwd={cwd})")
        return
    result.ok("CHECK-12: Working directory confined to Agentico-Public/")


def main() -> int:
    for_publish = "--for-publish" in sys.argv
    repo_root, gate_dir = resolve_paths()
    config = load_config(gate_dir)
    result = GateResult()

    mode = "PUBLISH" if for_publish else "STAGING"
    print("=" * 72)
    print(f"AGENTICO PUBLIC GATE — HARD VALIDATION ({mode})")
    print("=" * 72)
    print(f"Repo root    : {repo_root}")
    print(f"Gate dir     : {gate_dir}")
    print(f"Public repo  : {config['public_repo_url']}")
    print("-" * 72)

    check_01_desktop_partition(repo_root, config, result)
    check_02_staging_marker(repo_root, result)
    check_03_no_private_runtime_paths(repo_root, config, result)
    check_04_allowlist_top_level(repo_root, config, result)
    check_05_manifest_coverage(repo_root, config, result)
    check_06_secret_scan(repo_root, config, result)
    check_07_private_string_scan(repo_root, config, result)
    check_08_symlink_safety(repo_root, result)
    check_09_github_canonical(repo_root, config, result)
    check_13_marketing_claims(repo_root, config, result)
    check_14_internal_doc_block(repo_root, config, result)
    if (repo_root / ".git").exists():
        check_10_git_remote(repo_root, config, result)
    else:
        result.ok("CHECK-10: Git remote check skipped (repo not initialized)")
    if for_publish:
        check_11_publish_approval(repo_root, gate_dir, config, result)
        check_12_cwd_safety(repo_root, result)

    print("-" * 72)
    required = config.get("min_gate_checks_required", 8)
    if result.failures:
        print("⛔ PUBLISH BLOCKED — GATE FAILED")
        print(f"   Passed: {result.passed} | Failed: {len(result.failures)}")
        for failure in result.failures:
            print(f"   • {failure}")
        return 1

    if result.passed < required:
        print(f"⛔ PUBLISH BLOCKED — only {result.passed}/{required} checks ran")
        return 1

    print(f"✅ GATE PASSED — {result.passed} checks OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())