---
title: "Hermes MCP — Agentico + Grok"
slug: mcp-server-hermes
status: draft
legal_status: NOT_LEGAL_ADVICE
priority: 1
last_updated: 2026-06-17
document_status: SANITIZED
sanitization_state: sanitized
sanitization_run_id: 20260617T193709Z-std-san-mcp
sanitization_completed: 2026-06-17
---

# Hermes MCP Integration

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Agentico is **not a law firm** and **not a bank**. Hermes runs Grok inference; Agentico MCP
> handles formation verbs under human_approval gates.

## Direct answer

**Hermes** is the recommended operator stack for Agentico on WSL/macOS. Wire
`@agentico/mcp-server` as a native Hermes MCP server alongside **xai-oauth** for Grok
inference — two keys, one workflow.

## Quick start

```bash
cd /path/to/Agentico
./setup-byok-grok.sh
# Set AGENTICO_KEY in your shell environment
```

This chains: Hermes OAuth → bridge init → `.cursor/mcp.json` → Hermes native MCP → Grok CLI connector.

## Two-key model

| Key | Role |
|-----|------|
| Hermes `xai-oauth` or `XAI_API_KEY` | Grok inference (BYOK) |
| `AGENTICO_KEY` | Agentico MCP authentication |

```text
Hermes/Grok  ──BYOK──►  xAI API
     │
     │ MCP (AGENTICO_KEY)
     ▼
@agentico/mcp-server  →  formation verbs + human_approval
```

## Manual Hermes MCP wiring

```bash
export HERMES_HOME=/path/to/Agentico
./hermes mcp add agentico --command ./bin/agentico-mcp --args stdio \
  -e AGENTICO_KEY=$AGENTICO_KEY
./hermes mcp list | rg agentico
```

## Verify

```bash
./hermes auth status xai-oauth
./hermes doctor
./hermes chat -q "Call get_account_summary via Agentico MCP, then explain guided setup step 1"
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| OAuth callback fails (WSL) | `./hermes auth add xai-oauth --manual-paste` |
| MCP tools not listed | Re-run `./hermes mcp add agentico …` |
| Material verb rejected | Include `human_approval` with `attested_by` + `method` |

## Related

- Grok connector: [grok.md](grok.md)
- Cursor (shares MCP config): [cursor.md](cursor.md)
- Site: [/bring-your-own-ai](https://www.agentico.llc/bring-your-own-ai)
<!-- agentico:sanitized run_id=20260617T174608Z-std-san-03238817 branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
<!-- agentico:sanitized run_id=20260617T193709Z-std-san-mcp branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->