---
title: "Grok MCP Connector — Agentico"
slug: mcp-server-grok
status: draft
legal_status: NOT_LEGAL_ADVICE
priority: 1
last_updated: 2026-06-17
document_status: SANITIZED
sanitization_state: sanitized
sanitization_run_id: 20260617T174608Z-std-san-03238817
sanitization_completed: 2026-06-17
---

# Grok MCP Connector

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Agentico is **not a law firm** and **not a bank**. Not an LLM host — Grok powers inference;
> `AGENTICO_KEY` authenticates formation verbs.

## Direct answer

Connect **Grok** to `@agentico/mcp-server` via **Grok CLI** (`grok mcp add`), project
**`.grok/config.toml`**, or **grok.com/connectors → Custom** with a tunneled HTTPS URL.
Grok discovers ten Wyoming Series LLC tools and calls them like built-in integrations.

## Prerequisites

- `AGENTICO_KEY` from [agentico.llc/signup](https://www.agentico.llc/signup)
- Grok CLI installed, or SuperGrok web access for Custom connectors
- Agentico MCP built: `./setup-grok-connector.sh`

## Grok CLI (fastest)

```bash
./setup-grok-connector.sh
grok mcp doctor agentico    # expect handshake OK + 10 tools
```

One-liner:

```bash
grok mcp add agentico -e AGENTICO_KEY=$AGENTICO_KEY -- ./bin/agentico-mcp stdio
grok mcp doctor agentico
```

In Grok chat, enable the `agentico` connector via `/mcps`.

## grok.com/connectors (web)

1. Start HTTP MCP: `AGENTICO_KEY=agk_… ./bin/agentico-mcp serve 3001`
2. Tunnel: `ngrok http 3001`
3. Add connector at [grok.com/connectors](https://grok.com/connectors):
   - **Name:** Agentico LLC Entities
   - **URL:** `https://<tunnel>/mcp`
   - **Auth:** Bearer `AGENTICO_KEY`

## Tools Grok discovers

Namespaced as `agentico__incorporate_agent`, etc.:

| Tool | Gate |
|------|------|
| `establish_master` | human_approval |
| `incorporate_agent` | human_approval |
| `sign_contract` | human_approval |
| `spawn_subsidiary` | human_approval |
| `wind_down` | human_approval |
| `get_account_summary` | — |
| `list_series` | — |
| `get_guided_setup_state` | — |
| `update_account_preferences` | — |
| `advance_guided_setup` | — |

## Example prompts

- *"Use Agentico to list my Wyoming series."*
- *"Incorporate a research agent series named knox-research with human_approval from Jane Doe."*
- *"What's my guided setup state for master formation?"*

## Sandbox without a key

```bash
AGENTICO_MOCK=1 ./bin/agentico-mcp stdio
```

Returns simulated responses for connector testing.

## Related

- Site guide: [/grok-connector](https://www.agentico.llc/grok-connector)
- Canonical server: [agentico.md](agentico.md)
- Hermes stack: [hermes.md](hermes.md)
<!-- agentico:sanitized run_id=20260617T174608Z-std-san-03238817 branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
