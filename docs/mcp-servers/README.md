---
title: "Agentico MCP Servers — Integration Index"
status: draft
legal_status: NOT_LEGAL_ADVICE
last_updated: 2026-06-17
document_status: SANITIZED
sanitization_state: sanitized
sanitization_run_id: 20260617T174608Z-std-san-03238817
sanitization_completed: 2026-06-17
---

# Agentico MCP Servers

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Agentico is **not a law firm** and **not a bank**. Consult licensed U.S. counsel before
> any filing, contract, or banking action.

## Overview

Agentico ships **one product MCP server** — `@agentico/mcp-server` — that exposes Wyoming
Series LLC formation verbs to any MCP-capable host. Customers connect that server through
their preferred AI runtime (Grok, Hermes, Cursor, Claude, or ChatGPT/Codex).

| MCP integration | Host runtime | Guide |
|-----------------|--------------|-------|
| **Agentico MCP** (canonical) | Any MCP host | [agentico.md](agentico.md) |
| **Grok connector** | Grok CLI · grok.com/connectors | [grok.md](grok.md) |
| **Hermes** | Hermes agent (xai-oauth) | [hermes.md](hermes.md) |
| **Cursor** | Cursor IDE | [cursor.md](cursor.md) |
| **Claude** | Claude Desktop · Claude Code | [claude.md](claude.md) |
| **ChatGPT / OpenAI** | ChatGPT · OpenAI API · Codex CLI | [chatgpt.md](chatgpt.md) |

## Two-key model (every integration)

| Key | Purpose |
|-----|---------|
| `AGENTICO_KEY` | Authenticates to Agentico MCP/SDK (`agk_…` from signup) |
| BYOK provider key | Powers your AI runtime inference (optional where host bills you separately) |

Material formation verbs require named **human_approval** on every call — server-enforced,
not prompt-bypassable.

## Site pages

| URL | Content |
|-----|---------|
| `/mcp-ai-agent-llc` | MCP AI agent LLC query landing |
| `/grok-connector` | Grok Custom MCP setup |
| `/bring-your-own-ai` | BYOK overview |
| `/developers` | SDK + MCP quickstart |

## Related

- [MCP wrappers for business](../blog/mcp-wrappers-for-business.md)
- [MCP business use cases](../blog/mcp-business-use-cases.md)
- [AI agents for business FAQ](../ai-agents-for-business-faq.md)
<!-- agentico:sanitized run_id=20260617T174608Z-std-san-03238817 branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
