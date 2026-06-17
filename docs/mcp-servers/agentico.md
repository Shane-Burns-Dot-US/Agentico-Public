---
title: "@agentico/mcp-server — Tool Reference"
slug: mcp-server-agentico
status: draft
legal_status: NOT_LEGAL_ADVICE
software_version: "0.2-alpha"
last_updated: 2026-06-17
document_status: SANITIZED
sanitization_state: sanitized
sanitization_run_id: 20260617T174608Z-std-san-03238817
sanitization_completed: 2026-06-17
---

# @agentico/mcp-server

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> Agentico is **not a law firm** and **not a bank**. Formation tools return illustrative
> `docs[]`. Customer-led Wyoming filing, EIN, and banking are your responsibility.

## Direct answer

`@agentico/mcp-server` is Agentico's **Model Context Protocol** server. It exposes **ten
tools** — five formation verbs (v0.1) plus five account read/configure tools (v0.2) — so
your AI runtime can adopt Wyoming Series LLC series under **human_approval** gates.

## Install

```bash
# From Agentico monorepo (after build)
./bin/agentico-mcp stdio

# Or via npx (when published)
npx -y @agentico/mcp-server stdio
```

Environment:

```bash
export AGENTICO_KEY=agk_…          # required — from agentico.llc/signup
export AGENTICO_ENV=sandbox        # or production
export AGENTICO_MOCK=1             # optional — simulated responses for connector QA
```

HTTP mode (for grok.com/connectors Custom URL):

```bash
AGENTICO_KEY=agk_… ./bin/agentico-mcp serve 3001
# Tunnel → https://<tunnel>/mcp
```

## Policy classes

| Class | Approval | Examples |
|-------|----------|----------|
| **read** | None | `get_account_summary`, `list_series` |
| **configure** | Soft confirm | `update_account_preferences`, `advance_guided_setup` |
| **material** | **human_approval** required | All formation verbs |
| **denied** | Not exposed to AI bridge | `export_credentials`, `rotate_agentico_key`, `update_billing` |

## Tools (v0.2)

### Formation verbs (material)

| Tool | Description | human_approval |
|------|-------------|----------------|
| `establish_master` | Stand up master Wyoming Series LLC with named human overseer | Required |
| `incorporate_agent` | Adopt agent as segregated series; returns `series.id` and `docs[]` | Required |
| `sign_contract` | Record hashed terms between two series | Required |
| `spawn_subsidiary` | Incorporate child series under parent | Required |
| `wind_down` | Flip series to `winding_down`; block new obligations | Required |

### Account read (v0.2)

| Tool | Description |
|------|-------------|
| `get_account_summary` | Account status, human overseer, formation progress |
| `list_series` | Inventory adopted series with status and metadata |
| `get_guided_setup_state` | Current step in onboarding or formation flow |

### Account configure (v0.2)

| Tool | Description |
|------|-------------|
| `update_account_preferences` | Non-material prefs (notifications, display name) |
| `advance_guided_setup` | Progress guided setup; escalates when step is material |

## human_approval payload

Material verbs require a named U.S. human overseer attestation:

```json
{
  "human_approval": {
    "attested_by": "Jane Doe",
    "method": "webauthn",
    "attested_at": "2026-06-17T12:00:00Z"
  }
}
```

Aliases accepted: `overseer_name` + `attestation` for manual flows.

## Example MCP config (stdio)

```json
{
  "mcpServers": {
    "agentico": {
      "command": "./bin/agentico-mcp",
      "args": ["stdio"],
      "env": {
        "AGENTICO_KEY": "${AGENTICO_KEY}",
        "AGENTICO_ENV": "sandbox"
      }
    }
  }
}
```

## Smoke test

```bash
node private-drafts/product/byok-ai-integration/packages/mcp-server/scripts/mcp-smoke.mjs
AGENTICO_MCP_CLI=./bin/agentico-mcp node private-drafts/product/byok-ai-integration/packages/mcp-server/scripts/mcp-smoke.mjs
```

Expect handshake OK and **10 tools** in `tools/list`.

## Host-specific setup

| Host | Guide |
|------|-------|
| Grok | [grok.md](grok.md) |
| Hermes | [hermes.md](hermes.md) |
| Cursor | [cursor.md](cursor.md) |
| Claude | [claude.md](claude.md) |
| ChatGPT / Codex | [chatgpt.md](chatgpt.md) |

## FAQ

### Does the MCP server file with Wyoming?

**No.** Tools return illustrative `docs[]`. Engage counsel and complete customer-led filing.

### Can agents call formation verbs without humans?

**No.** Material verbs reject calls missing valid `human_approval`.

### What changed in v0.2?

Added read/configure tools and guided setup flows. Formation verb schemas unchanged from v0.1.
<!-- agentico:sanitized run_id=20260617T174608Z-std-san-03238817 branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
