# Awaiting Approval — Content Branch

**Branch:** `awaiting-approval`  
**Published to `main`:** 2026-06-17 (`2e63671` merge + white-team remediation)  
**Live site sync:** 2026-06-17 (`51f9c45` on `Shane-Burns-Dot-US/Agentico` `main`)

---

## Purpose

`awaiting-approval` is the **pipeline staging branch** for content that completes sanitization before merge to `main`. Pieces listed below were **published** on 2026-06-17. New work lands here first; repeat approve → merge when ready.

Lifecycle reference: [docs/content-lifecycle.md](docs/content-lifecycle.md)

---

## Published to `main` + agentico.llc (2026-06-17)

| ID | Source path | GitHub `main` | Live URL |
|----|-------------|---------------|----------|
| `ai-agent-llc-formation-faq` | `docs/ai-agent-llc-formation-faq.md` | [FAQ](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/ai-agent-llc-formation-faq.md) | https://www.agentico.llc/faq/ai-agent-llc-formation |
| `schema-formation-faq-jsonld` | `docs/schema/ai-agent-llc-formation-faqpage.jsonld.json` | [JSON-LD](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/schema/ai-agent-llc-formation-faqpage.jsonld.json) | (embedded in FAQ page) |
| `blog-index` | `docs/blog/README.md` | [Index](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/blog/README.md) | https://www.agentico.llc/docs/blog-index |
| `blog-pillar-llc-formation` | `docs/blog/ultimate-guide-ai-agent-llc-formation-2026.md` | [Pillar](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/blog/ultimate-guide-ai-agent-llc-formation-2026.md) | https://www.agentico.llc/blog/ultimate-guide-ai-agent-llc-formation-2026 |
| `blog-wyoming-series-llc` | `docs/blog/wyoming-series-llc-ai-agents-setup-guide.md` | [Setup](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/blog/wyoming-series-llc-ai-agents-setup-guide.md) | https://www.agentico.llc/blog/wyoming-series-llc-ai-agents-setup-guide |
| `blog-legal-wrapper` | `docs/blog/ai-agent-legal-wrapper-liability-protection.md` | [Wrapper](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/blog/ai-agent-legal-wrapper-liability-protection.md) | https://www.agentico.llc/blog/ai-agent-legal-wrapper-liability-protection |
| `blog-agentic-ai-business` | `docs/blog/agentic-ai-business-legal-considerations.md` | [Business](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/blog/agentic-ai-business-legal-considerations.md) | https://www.agentico.llc/blog/agentic-ai-business-legal-considerations |
| `blog-contracts-bank` | `docs/blog/ai-agent-contracts-bank-account.md` | [Contracts](https://github.com/Shane-Burns-Dot-US/Agentico-Public/blob/main/docs/blog/ai-agent-contracts-bank-account.md) | https://www.agentico.llc/blog/ai-agent-contracts-bank-account |

**Not published (staged private only):** blog posts #6–#10 — see private `STAGED_CONTENT_ALERT.md`.

---

## Pieces awaiting approval

*None — queue cleared 2026-06-17. Next batch adds rows here before merge.*

---

## Approve and merge (next batch)

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
python3 Agentico/private-drafts/site-ship/migrate-docs-to-site.py
# commit + push Shane-Burns-Dot-US/Agentico main
```

---

## Branch map

| Branch | Role |
|--------|------|
| `main` | Public mainstream — **includes 2026-06-17 publish** |
| `awaiting-approval` | Pipeline staging — synced with `main` after publish |
| `content/aeo-faq-and-blog-drafts-2026-06-16` | Superseded |

**Private canonical:** `Agentico/private-drafts/content-export/` (never pushed as-is).

**DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**