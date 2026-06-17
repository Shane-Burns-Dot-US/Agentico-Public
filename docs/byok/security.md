---
title: "BYOK Security Overview"
slug: byok-security
status: draft
legal_status: NOT_LEGAL_ADVICE
document_status: SANITIZED
feature: byok-ai-integration
version: 0.2-alpha
last_updated: 2026-06-17
sanitization_state: sanitized
sanitization_run_id: 20260617T174247Z-std-san-byok
sanitization_completed: 2026-06-17
---

# BYOK Security Overview

> **⚠️ DRAFT · NOT LEGAL ADVICE · Illustrative only · Not a law firm · Not a bank · Outcomes not assured**

## Principles

1. **Write-only ingestion** — credentials accepted once; plaintext never returned
2. **Fingerprint display** — UI shows suffix only (e.g. `…x7Kp`)
3. **Separation** — BYOK credentials ≠ `AGENTICO_KEY`
4. **Revocation** — delete propagates within 60 seconds (target SLA)
5. **Audit** — AI-initiated actions logged with tool, actor, outcome

## Local storage

| OS | Preferred backend |
|----|-------------------|
| macOS | Keychain |
| Windows | Credential Manager |
| Linux / WSL | Encrypted file vault with passphrase |

## Web vault (Phase 2)

Dashboard at agentico.llc encrypts credentials with KMS envelope encryption.
Plaintext never stored in database or backups.

## Threat mitigations

| Threat | Mitigation |
|--------|------------|
| Key in logs | Redaction policy; structured logging |
| Prompt injection → unauthorized action | Policy envelope; material verb blocks |
| Stolen AGENTICO_KEY | Short-lived sessions; audit alerts |

## Operator checklist

- Never paste credentials into chat
- Use environment variables or OS secret store
- Rotate if exposed
- Review audit log after AI-guided sessions

Not a penetration test report. Not legal advice.
<!-- agentico:sanitized run_id=20260617T174247Z-std-san-byok branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
