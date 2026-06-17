---
title: "BYOK AI Integration — Setup Index"
slug: byok-index
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

# BYOK AI Integration — Setup Guides

> **⚠️ DRAFT · NOT LEGAL ADVICE · Illustrative only · Not a law firm · Not a bank · Outcomes not assured**

## Priority order

1. [Grok & Hermes](grok-hermes.md)
2. [Cursor](cursor.md)
3. [Claude](claude.md)
4. [ChatGPT / OpenAI](chatgpt.md)

## Quick commands

```bash
agentico-bridge init
agentico-bridge connect grok --hermes
agentico-bridge setup cursor
# Set AGENTICO_KEY in your shell environment
agentico-bridge doctor
```

## Two-key model

| Key | Purpose |
|-----|---------|
| `AGENTICO_KEY` | Agentico platform authentication |
| Provider env vars | Inference (Anthropic, OpenAI, xAI) |

Material verbs require **human_approval**. Agentico is not a law firm or bank.
<!-- agentico:sanitized run_id=20260617T174247Z-std-san-byok branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
