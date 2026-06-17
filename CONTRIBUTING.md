# Contributing to Agentico Public

---

> **⚠️ DRAFT REPOSITORY · NOT LEGAL ADVICE · ALL RIGHTS RESERVED**
>
> By contributing you acknowledge [DISCLAIMER.md](DISCLAIMER.md) and [LICENSE](LICENSE).
> Contributions become part of draft materials protected under the restrictive
> proprietary license unless a separate written agreement applies.

---

Thank you for your interest in Agentico.

## Before you contribute

1. Read [DISCLAIMER.md](DISCLAIMER.md) in full.
2. Read [LICENSE](LICENSE) — contributions are **not** automatically licensed
   under permissive open-source terms.
3. Understand: this repo is **draft**, not final work, and **not legal advice**.

## Separation

`Agentico-Public/` lives on the Desktop as its own folder. It is **not** nested
inside any private agent runtime workspace.

## How to contribute

1. Open an issue describing your proposal.
2. Fork only for the purpose of submitting a pull request back to the canonical
   repository — **not** for independent redistribution (see LICENSE).
3. Submit a pull request with clear scope and no secrets or personal data.
4. Maintainers review for safety and alignment. Acceptance does not imply legal
   accuracy or final publication status.

## Content sanitization

Documents on **content branches** enter as **unsanitized** with a visible
`⛔ UNSANITIZED` banner. Before merge toward `main`, maintainers run the private
sanitization pipeline:

**AEO Audit → Red Team (×3) → White Team (×3) → sanitized stamp**

| State | Meaning |
|-------|---------|
| `UNSANITIZED` | Not pipeline-reviewed — do not cite or publish |
| `SANITIZED` | Pipeline + gate pass — eligible for `awaiting-approval` |
| `DRAFT_NOT_FINAL` | On `main` after human sign-off |

Full lifecycle: [docs/content-lifecycle.md](docs/content-lifecycle.md)

**Never submit** compliance reports (`COMPLIANCE_REDTEAM_*`, `COMPLIANCE_WHITETEAM_*`,
`AEO_AUDIT_REPORT.md`) — private operator work product only.

## What not to submit

- API keys, tokens, passwords, or credentials
- Personal data or private correspondence
- Private agent runtime files (sessions, logs, config, memories)
- Content presented as legal advice or final authoritative guidance
- Foreign or non-U.S. entity structures — U.S. scope only

## Contributor warranty

You represent that your contribution is your original work or you have rights
to submit it, and you grant no rights beyond what the LICENSE and maintainer
acceptance expressly allow.