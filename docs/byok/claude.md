---
title: "BYOK Setup — Claude Desktop & Claude Code"
slug: byok-claude
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

# BYOK Setup — Claude Desktop & Claude Code

> **Priority 3** · v0.2 alpha

Connect Claude to Agentico MCP for guided Wyoming Series LLC onboarding.

## Setup

```bash
agentico-bridge init
agentico-bridge connect claude
agentico-bridge setup claude
# Set AGENTICO_KEY and Anthropic credential in your shell environment
```

Merge `.claude/mcp.json` into Claude Desktop config, then restart Claude Desktop.

## Claude Code

```bash
claude -p "Use Agentico MCP get_account_summary and summarize account state."
```

Add to `CLAUDE.md`:

```markdown
## Agentico MCP
- AGENTICO_KEY authenticates formation verbs.
- Material tools require explicit human_approval.
- Agentico is not a law firm or bank.
```

## Security

Store credentials in environment variables — not in chat. Revoke via
`agentico-bridge revoke claude` if exposed.

See [security.md](security.md).
<!-- agentico:sanitized run_id=20260617T174247Z-std-san-byok branch=awaiting-approval date=2026-06-17 pipeline=standard-sanitation>redteam>redflag>judge>scale>whiteteam -->
