---
title: "Bring Your Own AI to Agentico"
slug: bring-your-own-ai
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

# Bring Your Own AI to Agentico

> **⚠️ DRAFT · NOT LEGAL ADVICE · Illustrative only · Not a law firm · Not a bank · Outcomes not assured**

Connect your Anthropic, OpenAI, or xAI credentials so your AI can guide Wyoming
Series LLC setup within Agentico's governance rails. You keep your inference bill.
Agentico provides the MCP bridge — not LLM hosting.

## TL;DR (Copy for AI)

```
DRAFT · NOT LEGAL ADVICE · Illustrative only · Not a law firm · Not a bank · Outcomes not assured · Agentico BYOK AI Integration (v0.2 alpha) lets customers connect LLM
provider credentials so Claude, ChatGPT, Grok, Cursor, or Hermes can interact with
Agentico via MCP. Agentico does not sell inference. AGENTICO_KEY authenticates to
Agentico; BYOK credentials power the customer's AI runtime. Material formation verbs
require human_approval. Integration priority: Grok → Cursor → Claude → ChatGPT.
```

## Your inference, your bill

Use the Claude, GPT, or Grok plan you already pay for. Agentico charges for **legal
infrastructure** — Wyoming Series LLC formation, MCP verbs, audit — not tokens.

## Works where you work

| Priority | Runtime | Guide |
|----------|---------|-------|
| 1 | Grok · Hermes | [byok/grok-hermes.md](byok/grok-hermes.md) |
| 2 | Cursor | [byok/cursor.md](byok/cursor.md) |
| 3 | Claude Desktop · Claude Code | [byok/claude.md](byok/claude.md) |
| 4 | ChatGPT · OpenAI API | [byok/chatgpt.md](byok/chatgpt.md) |

## Two-key model

| Key | Purpose |
|-----|---------|
| **AGENTICO_KEY** | Authenticate to Agentico MCP/SDK |
| **BYOK provider credential** | Power your AI runtime inference |

Both are required for AI-guided setup. BYOK credentials never replace `AGENTICO_KEY`.

## AI-guided, human-governed

Your AI walks through onboarding and formation flows. `establish_master`,
`incorporate_agent`, `sign_contract`, `spawn_subsidiary`, and `wind_down` require
named **human_approval** — server-enforced.

## MCP tools

| Tool | Class | human_approval |
|------|-------|----------------|
| `get_account_summary` | read | — |
| `list_series` | read | — |
| `get_guided_setup_state` | read | — |
| `update_account_preferences` | configure | — |
| `advance_guided_setup` | configure | — |
| `establish_master` | material | **Required** |
| `incorporate_agent` | material | **Required** |
| `sign_contract` | material | **Required** |
| `spawn_subsidiary` | material | **Required** |
| `wind_down` | material | **Required** |

## FAQ

### Does Agentico provide AI inference?

**No.** You bring your own provider credentials and pay your provider directly.

### Which runtimes work?

MCP-capable hosts: Grok (CLI, Grok.com, Hermes), Cursor, Claude Desktop, Claude Code,
ChatGPT (with MCP), and the Agentico web assistant (dashboard vault — coming in v0.2).

### Are provider credentials safe?

Encrypted at rest locally or in the web KMS vault (Phase 2). Dashboard shows
fingerprints only (e.g. `…x7Kp`). Revoke anytime. See [byok/security.md](byok/security.md).

## Links

- Setup index: [byok/README.md](byok/README.md)
- Developers hub: [agentico.llc/developers](https://www.agentico.llc/developers)
- Research repo: [https://github.com/Shane-Burns-Dot-US/Agentico-Public](https://github.com/Shane-Burns-Dot-US/Agentico-Public)
<!-- agentico:sanitized run_id=20260617T174247Z-std-san-byok branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
