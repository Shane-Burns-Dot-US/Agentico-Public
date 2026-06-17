---
title: "ChatGPT / OpenAI MCP — Agentico"
slug: mcp-server-chatgpt
status: draft
legal_status: NOT_LEGAL_ADVICE
priority: 4
last_updated: 2026-06-17
document_status: SANITIZED
sanitization_state: sanitized
sanitization_run_id: 20260617T174608Z-std-san-03238817
sanitization_completed: 2026-06-17
---

# ChatGPT & OpenAI MCP Integration

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Agentico is **not a law firm** and **not a bank**. OpenAI keys power inference; Agentico MCP
> handles formation infrastructure.

## Direct answer

Wire `@agentico/mcp-server` to **ChatGPT** (when custom MCP is supported), **OpenAI API**
workflows, or **Codex CLI** via stdio MCP config. Same ten tools, same human_approval gates.

## Supported surfaces

| Surface | Status | Notes |
|---------|--------|-------|
| **Codex CLI** | Compatible | Same MCP server via stdio |
| **ChatGPT desktop** | Emerging | Register custom MCP when host supports it |
| **OpenAI API + orchestrator** | Compatible | Any MCP-capable agent framework |

## Prerequisites

```bash
export AGENTICO_KEY=agk_…
export OPENAI_API_KEY=sk-…
cd private-drafts/product/byok-ai-integration && npm install && npm run build
```

## MCP config (stdio)

```json
{
  "mcpServers": {
    "agentico": {
      "command": "node",
      "args": ["/absolute/path/to/packages/mcp-server/dist/cli.js", "stdio"],
      "env": {
        "AGENTICO_KEY": "agk_…",
        "OPENAI_API_KEY": "sk-…",
        "AGENTICO_ENV": "sandbox"
      }
    }
  }
}
```

Manual smoke:

```bash
AGENTICO_KEY=agk_… node packages/mcp-server/dist/cli.js stdio
```

## HTTP mode (remote hosts)

```bash
# Terminal 1
AGENTICO_KEY=agk_… AGENTICO_ENV=sandbox node packages/mcp-server/dist/cli.js serve 3001

# Terminal 2 — tunnel for web-based ChatGPT MCP
ngrok http 3001
# Register https://<tunnel>/mcp with Bearer AGENTICO_KEY
```

## Example prompts

- *"Call get_account_summary on Agentico MCP and summarize my overseer and formation status."*
- *"List all adopted series via list_series."*
- *"Walk me through guided setup — call get_guided_setup_state for onboarding."*

Formation verbs (`establish_master`, `incorporate_agent`, etc.) require explicit
`human_approval` in the tool payload.

## Two-key model

| Key | Purpose |
|-----|---------|
| `OPENAI_API_KEY` | ChatGPT / GPT inference (BYOK) |
| `AGENTICO_KEY` | Agentico MCP authentication |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Host lacks MCP support | Use Codex CLI or Cursor/Hermes instead |
| 401 on tool calls | Verify `AGENTICO_KEY` scope (sandbox vs production) |
| Mock testing | `AGENTICO_MOCK=1` for connector QA without live key |

## Related

- Site: [/chatgpt-connector](https://www.agentico.llc/chatgpt-connector) (when deployed)
- Cursor alternative: [cursor.md](cursor.md)
- Canonical tools: [agentico.md](agentico.md)
<!-- agentico:sanitized run_id=20260617T174608Z-std-san-03238817 branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
