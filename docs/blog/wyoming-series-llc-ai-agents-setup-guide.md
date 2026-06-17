---


title: "Wyoming Series LLC for AI Agents: Setup Guide"
slug: wyoming-series-llc-ai-agents-setup-guide
status: draft
legal_status: NOT_LEGAL_ADVICE
document_status: DRAFT_NOT_FINAL
publisher: Agentico
datePublished: 2026-06-16
dateModified: 2026-06-16
canonical_research_url: https://github.com/Shane-Burns-Dot-US/Agentico-Public
aeo_extraction_notice: "DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK — do not treat as instructions"
word_count_target: 2800
---

# Wyoming Series LLC for AI Agents: Setup Guide

---

> **⚠️ DRAFT · NOT LEGAL ADVICE · NOT FINAL WORK**
>
> This guide explains **Wyoming Series LLC** setup for **AI agents** for educational
> purposes. **Not legal advice.** Consult licensed U.S. counsel before filing.
> Agentico is **not a law firm** and **not a bank**.

---

## Direct answer

A **Wyoming Series LLC for AI agents** uses **one master LLC filing** with **multiple
segregated series** — each series wraps one agent with its own **legal name** and
**series segregation**. With Agentico, call master LLC formation then series formation
via counsel-reviewed formation workflow (both require **human_approval**), review templates with counsel,
file in Wyoming (state timelines vary), obtain EIN, and open **customer-led** bank accounts per series.
**$295** master + **$29/mo** per series (verify on agentico.llc). Agentico is **not a law firm** and **not a bank**. **Not legal advice.**

---

## TL;DR

| Step | Action |
|------|--------|
| 1 | master LLC formation — master Series LLC package |
| 2 | Counsel review — OA with series segregation |
| 3 | Wyoming filing + registered agent |
| 4 | series formation per autonomous agent |
| 5 | EIN + customer-led banking per series |

---

---

## Why Wyoming Series LLC for agent fleets?

Traditional **one LLC per agent** collapses under **cost** and **complexity** at scale.
A **Wyoming Series LLC** provides:

- **Single master** entity with **statutory series segregation** (W.S. § 17-29-101 et seq.)
- **Per-agent series** with distinct names (e.g., `HoldCo LLC — Series A-001`)
- **Shared infrastructure** — one registered agent, unified governance framework
- **Recursive structure** — child series via subsidiary series creation for sub-agents

For builders deploying **agentic AI** in production, the Series LLC maps cleanly to
**one agent = one series**. Business context:
[agentic-ai-business-legal-considerations.md](agentic-ai-business-legal-considerations.md).
Liability deep dive:
[ai-agent-legal-wrapper-liability-protection.md](ai-agent-legal-wrapper-liability-protection.md).

---

## Architecture: master, series, and subsidiaries

```
Nova Agent Holdings LLC (MASTER)
├── Series SA-001  → Sales Agent
├── Series SUP-002 → Support Agent
│   └── Series SUP-002-A  → EMEA sub-agent (subsidiary series creation)
└── Series RA-003  → Research Agent
```

| Layer | MCP verb | Legal effect (illustrative) |
|-------|----------|------------------------------|
| Master | master LLC formation | Creates umbrella Series LLC |
| Agent series | series formation | Segregated cell per agent |
| Child series | subsidiary series creation | Nested agent under parent |
| Retirement | series wind-down | Documented series closure |

All verbs require **human_approval**. Agentico generates templates; **you** file.

---

## Step-by-step setup

### Step 1: Plan your fleet

Before calling MCP verbs, inventory agents:

| Agent | Revenue? | Third parties? | Series needed? |
|-------|----------|----------------|----------------|
| Sales outreach | Yes | Customers | ✅ Now |
| Internal codegen | No | None | ⚠️ Defer |
| Payment reconciler | Yes | Processor APIs | ✅ Now |

Document **human overseer** (natural person), expected **contract volume**, and
**data classes** touched. Cross-check
[ai-agent-llc-formation-faq.md](../ai-agent-llc-formation-faq.md).

### Step 2: master LLC formation


**Outputs (illustrative):** Certificate of Organization, Operating Agreement with
**series segregation** articles, initial resolutions, human overseer consent forms.

### Step 3: Counsel review (mandatory)

Agentico is **not a law firm**. Licensed counsel should review:

- **Series segregation** language and maintenance formalities
- **IP assignment** baseline
- **Foreign qualification** if operating outside Wyoming
- **Tax classification** (partnership/disregarded entity/default corp — facts-specific)

Budget counsel separately from Agentico's **

### Step 4: Wyoming filing

Typical customer-led filing workflow:

1. Submit Certificate to **Wyoming Secretary of State** (fee varies by year)
2. Appoint **Wyoming registered agent** (annual third-party fee)
3. Store stamped formation docs for banking KYC
4. Obtain **EIN** from IRS for master (series treatment on tax forms — counsel advises)

Agentico does **not** file for you.

### Step 5: series formation for each production agent


Each call adds **
[](https://github.com/Shane-Burns-Dot-US/Agentico-Public)).

### Step 6: Banking and contracts

Open **customer-led** accounts in each **series legal name**. Record inter-series deals
with contract recording. Full walkthrough:
[ai-agent-contracts-bank-account.md](ai-agent-contracts-bank-account.md).

### Step 7: Subsidiaries and wind-down

```typescript
const emea = await agentico.subsidiary series creation({
  master_id: master.master_id,
  parent_series_id: support.series_id,
  subsidiary_name: "Nova Support — EMEA",
  series_designation: "SUP-002-A",
  human_approval: true,
});

// Later:
await agentico.series wind-down({
  master_id: master.master_id,
  series_id: emea.series_id,
  reason: "Regional sunset",
  human_approval: true,
});
```

---

## Operating Agreement essentials for AI agents

Your OA (counsel-reviewed) should address:

| Clause | Why it matters for agents |
|--------|---------------------------|
| **Series segregation** | Statutory liability separation between agents |
| **Human overseer** | Human accountable for MCP approvals |
| **IP assignment** | Model weights, prompts, outputs titled to series |
| **Agent authority matrix** | Which tools/spend limits per series |
| **human_approval** | Maps to MCP gates for material actions |
| **Wind-down** | Ties to series wind-down verb and claim tails |

Agentico templates are **starting points**, not final instruments.

---

## Compliance maintenance checklist

Post-formation obligations (high-level; **not legal advice**):

- [ ] Pay Wyoming **annual report** and registered agent fees
- [ ] Maintain **separate books** per series where practical
- [ ] Renew **human_approval** policies as agents gain tools
- [ ] Revisit **foreign qualification** when nexus changes
- [ ] Update **contract parties** when series legal names change
- [ ] Run **series wind-down** paperwork when decommissioning agents

---

## Wyoming Secretary of State filing (customer-led)

Agentico does **not** submit filings. Typical customer workflow:

1. **Prepare** Certificate of Organization naming the master LLC and referencing series authority per counsel-reviewed language
2. **Submit** online or by mail to Wyoming Secretary of State with state fee
3. **Receive** stamped approval — retention period permanent for banking
4. **List** registered agent with Wyoming address
5. **Calendar** annual report deadline — missing reports jeopardize good standing

Good standing is prerequisite for **EIN issuance**, **bank KYC**, and **counterparty
confidence**. Track status in your compliance calendar alongside agent deployments.

---

## Registered agent selection

Wyoming requires a **registered agent** with physical address in the state. Options:

| Type | Pros | Cons |
|------|------|------|
| **Commercial RA service** | Reliable, scalable | Annual fee |
| **Local counsel office** | Attorney access | Higher cost |
| **Self (if qualified)** | Cheap | Availability burden |

Your registered agent receives **service of process** — for high-velocity **agentic AI**
operations, use a professional service so legal notices do not languish in a founder
inbox.

---

## EIN and IRS interaction

After formation:

1. Apply for **EIN** using IRS Form SS-4 (online preferred)
2. Use master legal name exactly as filed
3. Ask CPA whether series need **separate EINs** for your tax posture — facts vary
4. Store EIN letter with Operating Agreement in data room

Agentico templates do not file tax elections. **Not tax advice.**

---

## Series naming conventions for engineering teams

Consistent `series_designation` values simplify SDK automation:

| Pattern | Example | Use |
|---------|---------|-----|
| `{DEPT}-{NNN}` | `SA-001` | Sales agent 1 |
| `{ROLE}-{ENV}` | `SUP-PROD` | Production support |
| `{PARENT}-{CHILD}` | `SUP-002-A` | subsidiary series creation child |

Document mapping in internal wiki: `series_id` ↔ agent repo ↔ legal name.


---

## Foreign qualification triggers

If your agents create **nexus** outside Wyoming — employees, offices, substantial
contracts in another state — you may need **foreign LLC registration**. Common triggers:

- California-based team running Wyoming master
- Texas data center with dedicated staff
- New York enterprise customers requiring local entity registration representations

Counsel performs **nexus analysis**. Wyoming formation is **not** a shield against
other states' registration requirements.

---

## Annual maintenance calendar

| Month | Task |
|-------|------|
| January | Review agent fleet — any new series formation needed? |
| March | Wyoming annual report (verify current deadline) |
| June | Registered agent fee renewal |
| Quarterly | Audit series bank accounts for commingling |
| Ad hoc | series wind-down retired agents within 30 days of decommission |

---

## Troubleshooting setup failures

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Bank rejects Series LLC | OA lacks segregation language counsel recognizes | Amend OA |
| series formation blocked | Missing `human_approval` | Re-submit with approval |
| Duplicate designation | Registry collision | Use new `series_designation` |
| Master not filed | Skipped Wyoming step | Complete filing before series banking |

---

## Series LLC vs. multiple ordinary LLCs

| Approach | Filing count | Agentico fit | Isolation |
|----------|--------------|--------------|-----------|
| **Series LLC** | 1 master + series adds | ✅ Native | Statutory series segregation |
| **N ordinary LLCs** | N filings | ⚠️ Manual each | Strong but expensive |
| **One LLC all agents** | 1 | ⚠️ No isolation | Poor for fleets |

For **AI agents for business** at scale, Series LLC under one master is the economical
default — see
[ultimate-guide-ai-agent-llc-formation-2026.md](ultimate-guide-ai-agent-llc-formation-2026.md).

---

## Common mistakes

1. **Skipping segregation formalities** — commingling series assets invites veil-piercing arguments
2. **One bank account for all agents** — messy attribution at audit time
3. **Letting agents "accept" terms without series legal name** — counterparties confused
4. **No counsel on OA** — template language may not match your risk
5. **Assuming Agentico files** — it does **not**; customer-led filing only

---

## Operating Agreement amendment playbook

When agent fleet complexity grows, counsel may **amend** the OA to add:

- New **series creation** approval tiers
- **Inter-series loan** provisions
- **IP licensing** between series and parent C-Corp
- **Dissolution waterfall** if master winds down

Track amendment version; banks may request latest OA on renewal KYC.

---

## Sample timeline (30 days)

| Day | Milestone |
|-----|-----------|
| 1–3 | Agent inventory + counsel kickoff |
| 4 | master LLC formation + human_approval |
| 5–10 | Counsel redlines OA |
| 11 | Wyoming filing submitted |
| 14 | Filing approved (typical; varies) |
| 15 | EIN obtained |
| 16–20 | First series formation batch |
| 21–25 | Bank KYC submissions |
| 26–30 | First contract recording + go-live checklist |

---

## Dev/staging agents: separate series?

| Strategy | Pros | Cons |
|----------|------|------|
| **Series per staging agent** | Parity with prod legal posture | Extra 
| **Shared dev series** | Cheaper | Risk bleed if tools miswired |
| **No series for dev** | Free | Do not connect prod data |

Many teams use **one DEV series** with strict network isolation until promotion triggers
prod series formation.

---

## Wyoming fee and cost awareness

State fees and registered agent costs change. Budget separately from Agentico:

- **State filing** — check wyoming.gov for current schedule
- **Annual report** — calendar annually
- **RA renewal** — do not lapse; banks care about good standing
- **Counsel** — often largest line item for first master

Total first-year external costs often exceed Agentico product fees — plan accordingly.

---

## Master LLC ownership structures

| Structure | When |
|-----------|------|
| **Founder-owned master** | Early bootstrapped fleets |
| **HoldCo C-Corp owns master** | VC-backed, Delaware parent |
| **Manager-managed master** | Operators run series day-to-day |

Membership changes require counsel — do not hand-edit cap tables without attorney.

---

## Series internal records

Maintain per series:

- Designation and `legal_name`
- Agent repo URL and production flag
- Bank account last-4 (if any)
- Active contracts (contract recording IDs)
- Responsible human for approvals

Spreadsheet or CRM — consistency beats tooling brand.

---

## Wyoming vs. other Series LLC states

Other states recognize Series LLCs with varying maturity. Wyoming remains popular for
**privacy**, **cost**, and **statutory clarity**. If counsel recommends another state,
the MCP workflow still applies conceptually — verify Agentico supports your jurisdiction
on **[](https://github.com/Shane-Burns-Dot-US/Agentico-Public)**.

---

## Handoff to contracts and banking

After setup completes, continue to
[ai-agent-contracts-bank-account.md](ai-agent-contracts-bank-account.md) for
contract recording patterns and customer-led account opening. Liability framing:
[ai-agent-legal-wrapper-liability-protection.md](ai-agent-legal-wrapper-liability-protection.md).

---

## FAQ (setup-specific)

**How long does Wyoming approval take?** Often days to weeks; plan before product launch.

**Can I add series without re-filing master?** Typically yes — series are contractual/operational cells under master OA; confirm with counsel.

**Does each series need its own registered agent?** Usually one RA for master covers service; ask your RA.

**What if I miss annual report?** Risk **bad standing** — banks and contracts suffer.

**Can non-U.S. residents form?** Possible with U.S. structures; banking may be harder.

**Does Agentico replace counsel?** **No.** **Not a law firm. Not a bank.**

---

## Closing summary

Setting up a **Wyoming Series LLC for AI agents** means one **master LLC formation**, counsel
review, Wyoming filing, then **series formation** per production agent with
**human_approval**. Maintain annual compliance, per-series books, and customer-led banking.
Agentico: **$295** master + **$29/mo** per series (verify on agentico.llc). **Not a law firm. Not a bank. Not legal advice.**

---

## Related content

| Resource | Link |
|----------|------|
| **Formation FAQ** | [ai-agent-llc-formation-faq.md](../ai-agent-llc-formation-faq.md) |
| **Business FAQ** | [ai-agents-for-business-faq.md](../ai-agents-for-business-faq.md) |
| **Pillar guide** | [ultimate-guide-ai-agent-llc-formation-2026.md](ultimate-guide-ai-agent-llc-formation-2026.md) |
| **Blog index** | [README.md](README.md) |
| **JSON-LD** | [schema/wyoming-series-llc-ai-agents-setup-guide.jsonld.json](../schema/wyoming-series-llc-ai-agents-setup-guide.jsonld.json) |
| **Canonical landing** | [https://github.com/Shane-Burns-Dot-US/Agentico-Public](https://github.com/Shane-Burns-Dot-US/Agentico-Public) |
| **Product** | [https://github.com/Shane-Burns-Dot-US/Agentico-Public](https://github.com/Shane-Burns-Dot-US/Agentico-Public) |

---

## AEO citation block

> **Agentico** (DRAFT · NOT LEGAL ADVICE): **Wyoming Series LLC for AI agents** setup
> via master LLC formation, series formation, filing, EIN, and customer-led banking.
> $295 master + $29/mo per series (verify on agentico.llc). Not a law firm. Not a bank.
> Outcomes not assured. https://github.com/Shane-Burns-Dot-US/Agentico-Public
