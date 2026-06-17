---
title: "Grok Connector for Agentico — Custom MCP Wyoming Series LLC Formation"
description: "Connect Grok to Agentico via Custom MCP connector. Ten formation tools, human_approval gates, CLI and grok.com/connectors setup."
classification: UNSANITIZED
pipeline_branch: awaiting-approval
last_updated: 2026-06-17
---

# Grok Connector for Agentico

> **TL;DR:** Agentico ships a Custom MCP connector for Grok. Add at grok.com/connectors or via `grok mcp add agentico`. Ten tools expose Wyoming Series LLC formation verbs with `human_approval` on material actions. Agentico is not an LLM host. Not a law firm. Not a bank.

## What ships

- `@agentico/mcp-server` — stdio + HTTP transports
- `./setup-grok-connector.sh` — one-command Grok CLI setup
- `./bin/agentico-mcp` — WSL-fast launcher (Linux FS cache)
- Landing: https://www.agentico.llc/grok-connector

## Tools (10)

| Tool | Class | human_approval |
|------|-------|----------------|
| establish_master | material | Required |
| incorporate_agent | material | Required |
| sign_contract | material | Required |
| spawn_subsidiary | material | Required |
| wind_down | material | Required |
| get_account_summary | read | — |
| list_series | read | — |
| get_guided_setup_state | read | — |
| update_account_preferences | configure | — |
| advance_guided_setup | configure | — |

## Setup paths

1. **Grok CLI:** `grok mcp add agentico -e AGENTICO_KEY=$AGENTICO_KEY -- ./bin/agentico-mcp stdio`
2. **grok.com/connectors:** `./bin/agentico-mcp serve 3001` → ngrok → Custom URL `/mcp`
3. **Verify:** `grok mcp doctor agentico` — expect 10 tools, handshake OK

## Compliance

- Material verbs require named `human_approval` from a U.S. responsible party
- Documents are illustrative templates — review with counsel before Wyoming SOS filing
- Agentico does not file on your behalf in v0.1 by default
- BYOK overview: https://www.agentico.llc/bring-your-own-ai

## Related

- Developers hub: https://www.agentico.llc/developers
- BYOK: https://www.agentico.llc/bring-your-own-ai