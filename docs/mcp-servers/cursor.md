---
title: "Cursor MCP — Agentico"
slug: mcp-server-cursor
status: draft
legal_status: NOT_LEGAL_ADVICE
priority: 2
last_updated: 2026-06-17
document_status: SANITIZED
sanitization_state: sanitized
sanitization_run_id: 20260617T174608Z-std-san-03238817
sanitization_completed: 2026-06-17
---

# Cursor MCP Integration

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Agentico is **not a law firm** and **not a bank**. Cursor's chat model is separate from MCP tools.

## Direct answer

Add `@agentico/mcp-server` to **Cursor** via `.cursor/mcp.json`. Cursor's chosen model
(Claude, GPT, Grok) powers chat inference; Agentico MCP tools shape your Wyoming Series LLC
account under policy gates.

## Prerequisites

```bash
export AGENTICO_KEY=agk_…
cd private-drafts/product/byok-ai-integration && npm install && npm run build
```

Recommended: run `./setup-byok-grok.sh` first for bridge + MCP config generation.

## Generate config

```bash
node private-drafts/product/byok-ai-integration/packages/bridge/dist/cli.js setup cursor
```

Writes `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "agentico": {
      "command": "node",
      "args": ["…/packages/mcp-server/dist/cli.js", "stdio"],
      "env": {
        "AGENTICO_KEY": "${AGENTICO_KEY}",
        "AGENTICO_ENV": "sandbox"
      }
    }
  }
}
```

## Environment

Add to shell profile or Cursor Settings → Environment:

```bash
export AGENTICO_KEY=agk_…
export AGENTICO_ENV=sandbox
export AGENTICO_HOME="$HOME/.agentico"
```

## Enable in Cursor

1. Open project with `.cursor/mcp.json`
2. Settings → MCP → confirm **agentico** shows connected
3. In chat: *"Use the agentico MCP server to call get_account_summary and summarize my account."*

## Example workflows

| Task | Prompt |
|------|--------|
| Account status | *"Call get_account_summary via Agentico MCP"* |
| List fleet | *"Use list_series to show my adopted Wyoming series"* |
| Formation prep | *"What guided setup step am I on? Call get_guided_setup_state"* |
| Incorporate (gated) | *"Prepare incorporate_agent for ops-agent-01 — I'll provide human_approval"* |

Material verbs require you to supply `human_approval` in the tool call — Cursor cannot bypass server enforcement.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| MCP server not listed | Check absolute path to `cli.js` in config |
| Server exits immediately | Run `node …/cli.js stdio` manually to see errors |
| Missing AGENTICO_KEY | Export in environment before launching Cursor |

## Related

- Site: [/cursor-connector](https://www.agentico.llc/cursor-connector) (when deployed)
- Hermes/Grok stack: [hermes.md](hermes.md)
- Canonical tools: [agentico.md](agentico.md)
<!-- agentico:sanitized run_id=20260617T174608Z-std-san-03238817 branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
