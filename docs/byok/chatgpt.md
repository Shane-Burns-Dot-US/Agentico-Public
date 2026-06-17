---
title: "BYOK Setup — ChatGPT & OpenAI"
slug: byok-chatgpt
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

# BYOK Setup — ChatGPT & OpenAI

> **Priority 4** · v0.2 alpha

Connect ChatGPT or OpenAI API clients to Agentico MCP.

## Local MCP

```bash
agentico-bridge init
agentico-bridge connect openai
agentico-bridge setup openai
# Set AGENTICO_KEY and OpenAI credential in your shell environment
agentico-mcp stdio
```

## ChatGPT web connector

ChatGPT cloud requires a public HTTPS MCP endpoint:

```bash
# With AGENTICO_KEY and AGENTICO_ENV set in environment:
agentico-mcp serve 3001
```

Tunnel port 3001 (ngrok or cloudflared), then register the `/mcp` URL in ChatGPT
connector settings with bearer authorization using your platform key.

## Example prompts

```text
Connect to Agentico MCP and call get_guided_setup_state.
```

```text
Draft incorporate_agent payload for series trading-bot-alpha with human_approval placeholder — do not execute.
```

Agentico does not resell OpenAI tokens. Material verbs require **human_approval**.
Not a law firm or bank.
<!-- agentico:sanitized run_id=20260617T174247Z-std-san-byok branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
