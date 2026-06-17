# Awaiting Approval — Content Branch

**Branch:** `awaiting-approval`  
**Last publish to `main`:** 2026-06-17 (`92593c2` — standard-sanitation pipeline)  
**Live site sync:** 2026-06-17 (`0cdb47b` on `Shane-Burns-Dot-US/Agentico` `main`)

---

## Purpose

`awaiting-approval` is the **pipeline staging branch** for content that completes sanitization before merge to `main`. Human review happens here; production merges after `approve-publish.sh`.

Lifecycle reference: [docs/content-lifecycle.md](docs/content-lifecycle.md)

---

## Pieces awaiting approval

*None — queue cleared 2026-06-17 after standard-sanitation publish (`20260617T132624Z-standard-sanitation`).*

**Staged posts #6–#10** remain **LOCKED** in private `Agentico/private-drafts/content-export/` only — not present in this public repo until each `publish_after` date.

---

## Published (2026-06-17 standard sanitation)

| ID | Source path | Pipeline run | Live URL |
|----|-------------|--------------|----------|
| `ai-agent-llc-formation-faq` | `docs/ai-agent-llc-formation-faq.md` | `20260617T132624Z-standard-sanitation` | https://www.agentico.llc/faq/ai-agent-llc-formation |
| `schema-formation-faq-jsonld` | `docs/schema/ai-agent-llc-formation-faqpage.jsonld.json` | `20260617T132624Z-standard-sanitation` | (embedded in FAQ HTML) |
| `blog-pillar-llc-formation` | `docs/blog/ultimate-guide-ai-agent-llc-formation-2026.md` | `20260617T132624Z-standard-sanitation` | https://www.agentico.llc/blog/ultimate-guide-ai-agent-llc-formation-2026 |
| `blog-wyoming-series-llc` | `docs/blog/wyoming-series-llc-ai-agents-setup-guide.md` | `20260617T132624Z-standard-sanitation` | https://www.agentico.llc/blog/wyoming-series-llc-ai-agents-setup-guide |
| `blog-legal-wrapper` | `docs/blog/ai-agent-legal-wrapper-liability-protection.md` | `20260617T132624Z-standard-sanitation` | https://www.agentico.llc/blog/ai-agent-legal-wrapper-liability-protection |
| `blog-agentic-ai-business` | `docs/blog/agentic-ai-business-legal-considerations.md` | `20260617T132624Z-standard-sanitation` | https://www.agentico.llc/blog/agentic-ai-business-legal-considerations |
| `blog-contracts-bank` | `docs/blog/ai-agent-contracts-bank-account.md` | `20260617T132624Z-standard-sanitation` | https://www.agentico.llc/blog/ai-agent-contracts-bank-account |
| `blog-index` | `docs/blog/README.md` | `20260617T132624Z-standard-sanitation` | https://www.agentico.llc/docs/blog-index |

**Pipeline verdicts:** Red → Redflag → Judge → Scale → White · Semantic equivalence **PASS** (fidelity 5/5) · Gate **14/14 PASS** · `document_status: SANITIZED`

---

## Approve and merge

```bash
cd Agentico-Public
git checkout awaiting-approval

python3 .public-gate/validate.py
./.public-gate/approve-publish.sh
python3 .public-gate/validate.py --for-publish

git checkout main
git merge awaiting-approval
git push origin main

# Site HTML from published markdown:
AGENTICO_PUBLIC_DOCS=/path/to/Agentico-Public/docs \
AGENTICO_SITE_LANDING=/path/to/Agentico-site/apps/landing \
python3 Agentico/private-drafts/site-ship/migrate-docs-to-site.py
# commit + push Shane-Burns-Dot-US/Agentico main
```

---

## Branch map

| Branch | Role |
|--------|------|
| `main` | Public mainstream — includes 2026-06-17 full-pipeline publish |
| `awaiting-approval` | Review channel — synced with `main` after publish |
| `content/aeo-faq-and-blog-drafts-2026-06-16` | Superseded |

**Private canonical:** `Agentico/private-drafts/content-export/` (never pushed as-is).

**DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**