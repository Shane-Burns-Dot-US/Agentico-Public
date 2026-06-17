---
title: "BYOK Setup — Grok & Hermes"
slug: byok-grok-hermes
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

# BYOK Setup — Grok & Hermes

> **Priority 1** · v0.2 alpha

Use Grok (xAI) for inference and Agentico MCP for Wyoming Series LLC formation verbs.

## Quick start

```bash
agentico-bridge init
agentico-bridge connect grok --hermes
agentico-bridge setup grok
agentico-bridge setup cursor
# Set AGENTICO_KEY in your shell environment (from agentico.llc signup)
agentico-bridge doctor
```

Hermes operators: authenticate Grok via `xai-oauth` in your Hermes install, then
register the `agentico` MCP server in Hermes settings.

## Two-key model

| Credential | Role |
|------------|------|
| Grok (xai-oauth or XAI env) | Inference |
| `AGENTICO_KEY` | Agentico MCP |

## xAI credential fallback

Store your xAI credential via `agentico-bridge connect grok` (interactive prompt).
Then run `agentico-bridge test grok`.

## Example prompts

```text
Call get_account_summary via Agentico MCP and summarize formation progress.
```

```text
Prepare incorporate_agent for series demo-agent-01 — show payload only; no submit without human_approval.
```

## Troubleshooting

```bash
agentico-bridge doctor
agentico-bridge test grok
```

Agentico is not a law firm or bank. Material verbs require **human_approval**.
<!-- agentico:sanitized run_id=20260617T174247Z-std-san-byok branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
