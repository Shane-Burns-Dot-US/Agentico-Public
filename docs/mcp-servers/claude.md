---
title: "Claude MCP — Agentico"
slug: mcp-server-claude
status: draft
legal_status: NOT_LEGAL_ADVICE
priority: 3
last_updated: 2026-06-17
document_status: SANITIZED
sanitization_state: sanitized
sanitization_run_id: 20260617T174608Z-std-san-03238817
sanitization_completed: 2026-06-17
---

# Claude MCP Integration

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Agentico is **not a law firm** and **not a bank**. Your Anthropic key powers Claude inference;
> `AGENTICO_KEY` authenticates formation tools.

## Direct answer

Connect **Claude Desktop** or **Claude Code** to `@agentico/mcp-server` so Claude can read
account state, advance guided setup, and prepare formation verbs — with **human_approval**
on every material action.

## Prerequisites

```bash
export AGENTICO_KEY=agk_…
export ANTHROPIC_API_KEY="${ANTHROPIC_API_KEY}"   # BYOK inference
cd private-drafts/product/byok-ai-integration && npm install && npm run build
```

Optional vault:

```bash
node packages/bridge/dist/cli.js init
node packages/bridge/dist/cli.js connect claude
```

## Claude Desktop config

Generate project snippet:

```bash
node packages/bridge/dist/cli.js setup claude --dir /path/to/your/project
```

Merge `mcpServers.agentico` into Claude Desktop config:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "agentico": {
      "command": "node",
      "args": ["/absolute/path/to/packages/mcp-server/dist/cli.js", "stdio"],
      "env": {
        "AGENTICO_KEY": "agk_…",
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}",
        "AGENTICO_ENV": "sandbox"
      }
    }
  }
}
```

Use **absolute paths** — relative paths often fail on Claude Desktop restart.

## Verify

Restart Claude Desktop fully. Confirm MCP indicator shows **agentico** connected.

```
Use Agentico MCP to call get_account_summary and describe my formation progress.
```

```
What is the current guided setup step? Call get_guided_setup_state.
```

## Claude Code CLI

Same MCP block in project `.claude/mcp.json` or user-level config. Claude Code discovers
tools at session start.

## Policy reminder

| Tool class | human_approval |
|------------|----------------|
| Formation verbs | **Required** |
| Read tools | Not required |
| Configure tools | Soft confirm |

Claude cannot autonomously file with Wyoming — tools return illustrative `docs[]`.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| MCP not listed | Verify absolute path in desktop config |
| Tool call fails auth | Check `AGENTICO_KEY` in env block |
| Material verb rejected | Add `human_approval.attested_by` + `method` |

## Related

- Site: [/claude-connector](https://www.agentico.llc/claude-connector) (when deployed)
- BYOK overview: [/bring-your-own-ai](https://www.agentico.llc/bring-your-own-ai)
- Canonical tools: [agentico.md](agentico.md)
<!-- agentico:sanitized run_id=20260617T174608Z-std-san-03238817 branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
