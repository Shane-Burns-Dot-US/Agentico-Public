# Awaiting Approval — Content Branch

**Branch:** `awaiting-approval`  
**Target:** merge into `main` after explicit human sign-off  
**Published to `main` 2026-06-17 — see links below.**

---

## Purpose

This branch holds **all content and gate updates** that are staging-complete but **not yet approved** for the public mainstream (`main` / `origin/main`).

- **Sanitization pipeline** (private) → AEO Audit → Red Team ×3 → White Team ×3  
- **Red team** → adversarial review (`COMPLIANCE_REDTEAM_REPORT` in private export)  
- **White team** → remediations applied; **CHECK-13 gate passes**  
- **Sanitized stamp** → `document_status: SANITIZED` + hidden `agentico:sanitized` tag  
- **Human approval** → you read pieces, run `approve-publish.sh`, then merge here → `main`

Lifecycle reference: [docs/content-lifecycle.md](docs/content-lifecycle.md)

---

## Status (2026-06-16)

| Check | Result |
|-------|--------|
| `python3 .public-gate/validate.py` | ✅ GATE PASSED |
| Gate commit | `ba98106` (white-team sync) |
| Remote | ✅ `origin/awaiting-approval` pushed — **do not merge to `main` without approval** |

---

## Pieces awaiting approval (`ready_once_read`)

| ID | Path | Action |
|----|------|--------|
| `ai-agent-llc-formation-faq` | `docs/ai-agent-llc-formation-faq.md` | Read → approve |
| `schema-formation-faq-jsonld` | `docs/schema/ai-agent-llc-formation-faqpage.jsonld.json` | Read → approve |
| `blog-index` | `docs/blog/README.md` | Read → approve |
| `blog-pillar-llc-formation` | `docs/blog/ultimate-guide-ai-agent-llc-formation-2026.md` | Read → approve |
| `blog-wyoming-series-llc` | `docs/blog/wyoming-series-llc-ai-agents-setup-guide.md` | Read → approve |
| `blog-legal-wrapper` | `docs/blog/ai-agent-legal-wrapper-liability-protection.md` | Read → approve |
| `blog-agentic-ai-business` | `docs/blog/agentic-ai-business-legal-considerations.md` | Read → approve |
| `blog-contracts-bank` | `docs/blog/ai-agent-contracts-bank-account.md` | Read → approve |

**Not on this branch (staged private only):** blog posts #6–#10 — see private `STAGED_CONTENT_ALERT.md`.

---

## Approve and merge to mainstream

```bash
cd Agentico-Public
git checkout awaiting-approval

# 1. Staging gate
python3 .public-gate/validate.py

# 2. Select approved pieces (creates .public-gate/PUBLISH_APPROVED — local only)
./.public-gate/approve-publish.sh

# 3. Publish gate
python3 .public-gate/validate.py --for-publish

# 4. Merge to main when satisfied
git checkout main
git merge awaiting-approval
git push origin main
```

---

## Branch map

| Branch | Role |
|--------|------|
| `main` | Public mainstream (matches `origin/main` until merge) |
| `awaiting-approval` | **This branch** — content + gate updates pending sign-off |
| `content/aeo-faq-and-blog-drafts-2026-06-16` | Prior working branch (superseded by `awaiting-approval`) |

**Private canonical:** `Agentico/private-drafts/content-export/` (never pushed as-is).

---

## Included updates (not just content)

- `.public-gate/validate.py` — frontmatter skip, JSON-LD answer-only scan, negation expansions  
- `.public-gate/publish-pieces.json` — piece catalog with `ready_once_read`  
- `DISCLAIMER.md`, `LEGAL_NOTICE.md`, `GITHUB_REPO.json` — shell docs  
- Gate scripts: `approve-publish.sh`, `publish.sh`, hooks, manifest tooling  

**DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**