# Awaiting Approval — Content Branch

**Branch:** `awaiting-approval`  
**Last publish to `main`:** 2026-06-17 (`53a3132`)  
**Live site sync:** 2026-06-17 (`588bc0e` white-team remediation on `Shane-Burns-Dot-US/Agentico` `main`)

---

## Purpose

`awaiting-approval` is the **pipeline staging branch** for content that completes sanitization before merge to `main`. Human review happens here; production merges after `approve-publish.sh`.

Lifecycle reference: [docs/content-lifecycle.md](docs/content-lifecycle.md)

---

## Pieces awaiting approval

| ID | Source path | Batch | Notes |
|----|-------------|-------|-------|
| `ai-agent-llc-formation-faq` | `docs/ai-agent-llc-formation-faq.md` | white-team-remediation | JSON-LD Yes-opener fix, purpose-built → designed for |
| `ai-agents-faq` | `docs/ai-agents-for-business-faq.md` | white-team-remediation | Copy-for-AI disclaimer gaps |
| `schema-formation-faq-jsonld` | `docs/schema/ai-agent-llc-formation-faqpage.jsonld.json` | white-team-remediation | Yes-opener + schema softening |
| `blog-pillar-llc-formation` | `docs/blog/ultimate-guide-ai-agent-llc-formation-2026.md` | white-team-remediation | Instant timeline + disclaimers |
| `blog-wyoming-series-llc` | `docs/blog/wyoming-series-llc-ai-agents-setup-guide.md` | white-team-remediation | wins → is designed for |
| `blog-legal-wrapper` | `docs/blog/ai-agent-legal-wrapper-liability-protection.md` | white-team-remediation | Not a bank on Copy-for-AI |
| `blog-agentic-ai-business` | `docs/blog/agentic-ai-business-legal-considerations.md` | white-team-remediation | Not a bank on Copy-for-AI |
| `blog-contracts-bank` | `docs/blog/ai-agent-contracts-bank-account.md` | white-team-remediation | Not a bank on Copy-for-AI |
| `blog-step-by-step-formation` | `docs/blog/ai-agent-llc-formation-step-by-step-guide-2026.md` | staged #6 | LOCKED until 2026-06-23 |
| `blog-fastest-incorporate` | `docs/blog/wyoming-series-llc-ai-agents-fastest-incorporate-2026.md` | staged #7 | LOCKED until 2026-06-30 |
| `blog-complete-protection` | `docs/blog/ai-agent-legal-wrapper-complete-protection.md` | staged #8 | LOCKED until 2026-07-07 |
| `blog-formation-tool-comparison` | `docs/blog/best-ai-agent-formation-tool-2026-comparison.md` | staged #9 | LOCKED until 2026-07-14 |
| `blog-multi-agent-fleets` | `docs/blog/multi-agent-fleets-wyoming-series-llcs.md` | staged #10 | LOCKED until 2026-07-21 |

**Red-team recheck:** `REDTEAM_CONDITIONAL` — P0 liability + JSON-LD cleared. See private `COMPLIANCE_REDTEAM_REPORT.md` run `20260617T112953Z-redteam-recheck`.

**Site review channel:** `Shane-Burns-Dot-US/Agentico` branch `awaiting-approval` — compare-page sanitization + Vercel preview (post `main` 588bc0e merge-back).

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
AGENTICO_PUBLIC_DOCS=Agentico/private-drafts/content-export/docs \
python3 Agentico/private-drafts/site-ship/migrate-docs-to-site.py
# commit + push Shane-Burns-Dot-US/Agentico awaiting-approval → merge main
```

---

## Branch map

| Branch | Role |
|--------|------|
| `main` | Public mainstream — includes 2026-06-17 publish |
| `awaiting-approval` | **Review channel** — white-team batch + staged #6–#10 |
| `content/aeo-faq-and-blog-drafts-2026-06-16` | Superseded |

**Private canonical:** `Agentico/private-drafts/content-export/` (never pushed as-is).

**DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**