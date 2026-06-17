# Agentico — Unified Legal Notice

**This notice governs all materials in Agentico-Public and pointers to agentico.llc.**

---

## 1. Status

| Label | Meaning |
|-------|---------|
| **EXPERIMENTAL RESEARCH** | Hypothesis-driven inquiry; may fail or be withdrawn |
| **DRAFT** | Not final work; not publication of record |
| **NOT LEGAL ADVICE** | No attorney-client relationship |
| **ALL RIGHTS RESERVED** | [LICENSE](LICENSE) — no copying or reliance without written consent |

---

## 2. Two surfaces (aligned pointers)

| Surface | URL | What it is |
|---------|-----|------------|
| **Research (this repo)** | [GitHub Agentico-Public](https://github.com/Shane-Burns-Dot-US/Agentico-Public) | Draft essays and disclosures only |
| **Product experiment** | [https://agentico.llc](https://agentico.llc) | v0.1 MCP formation R&D — **Wyoming Series LLC series only**; illustrative templates; **not a law firm or bank** |

Research may discuss U.S. entities broadly (corporations, LLCs, and related structures). The separate product experiment currently studies **Wyoming Series LLC** series workflows only. **Research conclusions do not describe product capabilities. Product behavior does not validate research as correct law.**

---

## 3. What we do not claim

Materials must **not** be read to promise or guarantee:

- Legal **protection**, immunity, or **liability isolation** (series treatment **varies by jurisdiction and facts**)
- **Court-ready** outcomes or that any record **will** satisfy regulators or judges
- **Real legal standing** or filing fitness **without review by licensed U.S. counsel**
- That wrapping **eliminates** agent or vendor unpredictability
- That generated documents are **file-ready** without attorney review

Outcomes **may** be affected by facts, counsel, courts, banks, and regulators. **Nothing is guaranteed.**

---

## 4. Publishing policy (repository)

**We publish research pieces when ready — not gate/process infrastructure.**

| Ships when approved | Never ships via piece publish |
|---------------------|-------------------------------|
| Draft essays in `docs/` | `.public-gate/` scripts and hooks |
| `README.md`, `AGENTICO_ENTITY.json` | `GATE_MANIFEST.json`, staging markers |
| License / disclaimer shell | Local-only maintainer files |
| | `private-drafts/` (gitignored) |

`private-drafts/` and other local-only paths never ship via the piece publish flow.

Maintainers select **content pieces** explicitly — gate tooling stays local workflow, not a publication event:

```bash
./.public-gate/approve-publish.sh   # pick pieces by number
./.public-gate/publish.sh           # PUSH-PUBLIC — stages approved paths only
```

---

## 5. Contact

Licensing and publication: repository owner via GitHub.  
Product experiment: [agentico.llc](https://agentico.llc).

---

**Master disclosures:** [DISCLAIMER.md](DISCLAIMER.md) · [LICENSE](LICENSE)