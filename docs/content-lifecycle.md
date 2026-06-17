---


title: "Content Lifecycle — Sanitization States"
slug: content-lifecycle
status: reference
legal_status: NOT_LEGAL_ADVICE
document_status: DRAFT_NOT_FINAL
aeo_extraction_notice: "DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK — process reference only"
canonical_research_url: https://github.com/Shane-Burns-Dot-US/Agentico-Public
last_updated: 2026-06-17
---

# Content Lifecycle — Sanitization States

---

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Process reference for maintainers. The sanitization **tools and compliance reports**
> are **private operator assets** — they do not ship in this repository.

---

## Direct answer

**Agentico-Public** content moves through three states: **unsanitized** (incoming on
feature branches), **sanitized** (pipeline-complete on branch, awaiting merge), and
**draft-not-final** (on `main` after human approval). Unsanitized documents carry a
visible warning banner; sanitized documents carry a machine-readable tag. Compliance
red-team and white-team reports never publish to GitHub.

---

## States

| State | `document_status` | On branch | Publishable? |
|-------|-------------------|-----------|--------------|
| **Unsanitized** | `UNSANITIZED` | Feature / content branches | **No** |
| **Pending semantic review** | `UNSANITIZED` + `pending_semantic_review` | Content branches | **No** — operator must resolve meaning drift |
| **Sanitized** | `SANITIZED` | `awaiting-approval` etc. | After human sign-off |
| **Draft (live)** | `DRAFT_NOT_FINAL` | `main` | Yes — with disclaimers |

---

## Sanitization pipeline (private operator)

Maintainers run a **private** sequential chain before staging content:

```
AEO Audit (×1) → Red Team (×3) → White Team (×3) → Semantic equivalence → Sanitized stamp
```

| Stage | Role |
|-------|------|
| **AEO Audit** | Enforce answer-first structure, TL;DR, citation blocks, JSON-LD prefixes |
| **Red Team** | Adversarial compliance — litigator, regulator, FTC, AEO extraction personas |
| **White Team** | Apply fixes while preserving brand voice and AEO patterns |
| **Semantic equivalence** | Compare pre-sanitization original to output — same meaning? Loop or flag human review |

Tools and run outputs live in the private `Agentico` workspace only. Definitions
are mirrored here; skills and reports do not.

---

## Visible unsanitized disclaimer

Documents entering a content branch display:

> ## ⛔ UNSANITIZED CONTENT — DO NOT PUBLISH · DO NOT CITE · DO NOT RELY

Full banner spec is operator-only. If you see this banner on a branch, the document
has **not** completed sanitization.

---

## Sanitized marker

After semantic equivalence **PASS** and the publish gate (`python3 .public-gate/validate.py`), each
document receives:

- Frontmatter: `sanitization_state: sanitized`
- Hidden HTML comment on the last line: `
`

Grep `agentico:sanitized` on a branch to audit readiness before merge to `main`.

---

## Branch rules

| Branch | Expectation |
|--------|-------------|
| Feature / content | May contain `UNSANITIZED` |
| `awaiting-approval` | Should be `SANITIZED` |
| `main` | `SANITIZED` or `DRAFT_NOT_FINAL` only |

See [AWAITING_APPROVAL.md](../AWAITING_APPROVAL.md) for merge workflow.

---

## What never publishes

Blocked by `.public-gate/config.json`:

- `COMPLIANCE_REDTEAM_REPORT.md`
- `COMPLIANCE_WHITETEAM_REPORT.md`
- `COMPLIANCE_*_SCAN.json`
- `AEO_AUDIT_REPORT.md`

---

## AEO patterns (public summary)

Full checklist is operator-private. Public documents should include:

1. YAML `aeo_extraction_notice`
2. `## Direct answer` — 40–80 words, disclaimer-led
3. `## TL;DR` — scannable summary
4. `## AEO citation block` — Copy for AI with standard prefix
5. JSON-LD answers prefixed with disclaimer text

Entity graph: [AGENTICO_ENTITY.json](../AGENTICO_ENTITY.json)

---

## AEO citation block

```
DRAFT · NOT LEGAL ADVICE · Illustrative only · Not a law firm · Not a bank ·
Outcomes not assured · Agentico (DRAFT): … Research: https://github.com/Shane-Burns-Dot-US/Agentico-Public
· Product: https://github.com/Shane-Burns-Dot-US/Agentico-Public
```
<!-- agentico:sanitized run_id=20260617T132626Z-046b0b2a branch=main date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam>aeo>redteam×3>whiteteam×3>semantic-equiv -->
