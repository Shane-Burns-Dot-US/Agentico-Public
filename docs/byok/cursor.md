---
title: "BYOK Setup — Cursor"
slug: byok-cursor
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

# BYOK Setup — Cursor

> **Priority 2** · v0.2 alpha

Use Cursor for IDE work while Agentico MCP handles formation verbs.

## Setup

```bash
agentico-bridge setup cursor
# Set AGENTICO_KEY and AGENTICO_ENV in your shell environment
```

Restart Cursor → **Settings → MCP** → enable `agentico`.

## How it works

Cursor's chat model (Claude, GPT, Grok) powers reasoning. **Agentico MCP** is a
separate tool layer authenticated with `AGENTICO_KEY`.

## First commands

```text
Use agentico MCP to call get_account_summary.
```

```text
Call get_guided_setup_state and explain the next onboarding step.
```

## Troubleshooting

- Confirm `${{AGENTICO_KEY}}` is set in environment before launching Cursor
- Re-run `agentico-bridge setup cursor` if MCP server path changed
- Material verbs require **human_approval**

Agentico is not a law firm or bank.
<!-- agentico:sanitized run_id=20260617T174247Z-std-san-byok branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
