# BEGIN REGION cos_battle_plan.md CORE STANDARDS FILE
{
	🚨WARNING EDITING THIS REGION CAN HAVE DRAMTIC NEGATIVE IMPACT ON THE AI OS BEHAVIOR🛑
	🔥🌪️☢️☣️☠️
---

# The Chief of Staff Standard — Battle Plan
**AI OS Pipeline Spec — V3 Standard**
**Template Version:** 1.0

---
## How to Use This Template

1. Copy this file to `command_orchestration/` and rename it `[command_name]_battle_plan.md`
2. Fill every `{{}}` slot before the battle plan is considered ready to run
3. Declare gates at every pipeline step — **Tier 1 Validator Gate** at Captain boundaries, **Tier 2 Meridian Gate** where judgment is needed
4. HANK reads the battle plan, assembles the team, and fires on `%shipit`
5. After writing to Drive, get the file ID and add to the manifest

**Build order rule:** Colonel Mission Brief (IFPA) spec first. Captain Function Contracts second. Battle plan third.
The battle plan is derived from what the Colonels and Captains can actually do — not assumed.

---
## The Two-Tier Gate Model (read before declaring any gate)

Every V2 battle plan declared one kind of gate — "MERIDIAN QA GATE" — and packed both structural and semantic checks into it. V3 splits that gate by which engine can actually make the guarantee. The value of the split is visibility: the plan now declares *what is checked by code* and *what is checked by a mind*, and never confuses the two.

**Tier 1 — Validator Gate.** Fires at a **Captain output boundary**. Runs the deterministic validator against that Captain's `AIOS-VALIDATION` block. No reasoning is spent; it is code. Verdicts are the four terms defined in the Function Contract (the verdict-vocabulary source of truth), quoted verbatim:

- `pass` — output matches schema; pipeline advances.
- `output_failed` — a required field is missing, mistyped, null where required, or contains a placeholder. **Halt without judgment.**
- `schema_missing` — the Captain carries no `AIOS-VALIDATION` block. **Halt without judgment** (fail-closed: no schema, no pass).
- `schema_malformed` — the block exists but cannot be parsed. **Halt without judgment.**

On any non-`pass` verdict the validator stops the pipeline. HANK decides: correct and re-run, or escalate to [the_prompter]. Meridian does not reason here — a Tier 1 halt is unappealable within its scope.

**Tier 2 — Meridian Gate.** Fires where the check is **semantic**: does the Colonel's brief map to its Mission Brief (OutMisIso), is provenance sensible, is the framing aligned to intent, is voice/standards honored. This is probabilistic, runs in the model, and routes findings through HANK in the standard HALT format.

**The economics the split makes visible:** Tier 1 clears structure for free, so Tier 2 gates spend Meridian's reasoning only on what needs a mind. Never place a "field present / non-null" check in a Tier 2 gate — that is a Tier 1 job, and duplicating it wastes Meridian's attention.

**Rule:** the battle plan carries no `AIOS-VALIDATION` block of its own. It *invokes* the validator at Captain boundaries; it does not define schemas.

**Fail-Fast (pipeline form):** a battle plan is built to stop early, by design. The pre-flight `{{}}` scan halts before launch; Tier 1 gates halt on the first structural break; the ERROR HANDLING table declares every halt path before the pipeline ever runs. Authoring order: fill ERROR HANDLING before PIPELINE SEQUENCE — the halt paths are designed before the happy path. A pipeline that cannot say where it stops is not ready to start.

---
# BATTLE PLAN: {{pipeline_name}}
**Command:** `%{{command_name}}`
**Colonel(s):** `{{colonel_file_path}}` *(list all — one per line if multiple)*
**Captains:** `{{captain_name}}` | `{{captain_name}}` *(list all active for this run)*
**Gates:** Tier 1 Validator at every Captain boundary; Tier 2 Meridian where judgment is required
**Branch:** {{branch_name}} *(Outbound Sales / Writing / Creative / Research)*
**Status:** DRAFT — Session {{session_number}}

---
## MISSION

{{mission_statement}}
*What this pipeline does, why it exists, and what "done" looks like.*
*Two sentences maximum. If you cannot state it in two sentences, the pipeline is not ready to be built.*

---
## PRE-FLIGHT CHECKLIST
*HANK completes before firing. Scan for `{{}}` — any unfilled slot is a hard stop.*

- [ ] `{{variable_slot_1}}` declared — {{description}}
- [ ] `{{variable_slot_2}}` declared — {{description}}
- [ ] Every active Captain carries a valid `AIOS-VALIDATION` block *(a `schema_missing` unit cannot fire)*
- [ ] *(Add required env vars, MCP connections, HubSpot properties, or system requirements here)*
- [ ] Working directory declared

---
## VARIABLE SLOTS

| Slot | Description | Source | Required |
|---|---|---|---|
| `{{variable_slot_1}}` | {{what it is}} | {{[the_prompter] / HANK / system}} | Required |
| `{{variable_slot_2}}` | {{what it is}} | {{[the_prompter] / HANK / system}} | Conditional |

*Conditional = only required if a specific branch of the pipeline fires.*
*HANK scans for `{{` before executing. Any open slot = halt.*

---
## PIPELINE SEQUENCE

```
[START]

{{Captain name}} ({{action}})
 -> {{what it returns}}

-> TIER 1 — VALIDATOR GATE
  Run: validator( {{captain_name}}.AIOS-VALIDATION , output )
  pass          -> advance
  output_failed -> HALT (surface delta to HANK)
  schema_missing / schema_malformed -> HALT (fail-closed, surface to HANK)

{{Colonel name}} ({{action / judgment}})
 -> {{composed brief it returns}}

-> TIER 2 — MERIDIAN GATE
  Check: brief maps to Mission Brief (OutMisIso) — semantic
  Check: {{provenance / framing / intent-alignment check}}
  Check: {{voice / standards check, e.g. VoiceYou}}
  Pass: advance | Halt: surface HALT to HANK (finding, source, recommended action)

[END]

-> TIER 2 — MERIDIAN GATE (FINAL, full output)
  Check: output serves the mission as declared in Layer 1
  Check: {{overall coherence / provenance across records}}
  Pass: return output to HANK | Halt: surface delta to HANK before any output leaves pipeline
```

*Rules:*
- *Captain boundaries get a Tier 1 Validator Gate. Colonel/judgment boundaries get a Tier 2 Meridian Gate. Declared here — not invoked ad hoc at runtime.*
- *A Tier 1 halt is deterministic and unappealable within scope: code said no. A Tier 2 halt is Meridian's judgment, routed through HANK.*
- *A halted step does not advance. HANK decides: correct and re-run, or escalate to [the_prompter].*

---
## ESCALATION RULE

{{Condition under which output goes directly to (the prompter)[the_prompter], bypassing standard (Chief of Staff)HANK review flow.}}

*Example: Any record with score ≥ 8 and icp_fit: Yes is flagged `escalation_flag: true` and surfaces to [the_prompter] before standard review.*

*If no escalation rule applies to this pipeline, write: "All output routes through HANK. No direct [the_prompter] escalation."*

---
## ERROR HANDLING

| Condition | Response |
|---|---|
| Captain transient error | Retry once. On second failure: skip record, log to `errors[]`, continue. |
| Tier 1 `output_failed` | Halt at gate. Surface delta to HANK. Do not advance the failing record. |
| Tier 1 `schema_missing` / `schema_malformed` | Halt. The Captain is not deployable until its block is fixed. Surface to HANK. |
| {{Specific failure type}} | {{What the pipeline does — skip / halt / fallback}} |
| Missing required input | Halt. Surface to HANK. Do not fabricate or infer. |
| Two or more consecutive Captain failures | Halt pipeline. Surface to HANK immediately. |
| Unrecoverable error | Surface to HANK. Do not attempt to continue. |

---
## OUTPUT HANDLING

| Result | Action |
|---|---|
| Passes final Tier 2 Meridian gate | {{Where output goes — HANK review / Gmail Draft / file / HubSpot write}} |
| *(any Captain invocation — pass OR halt)* | **INVOCATION LOG ticks are NOT written here.** POINTER ONLY. The tick is written by Meridian in the same action as every **Tier 1 Validator Gate** — canonical spec: "meridian.md", Verification Stack, "THE GATE IS THE TICK". This row previously WAS the rule's only home, gated on "passes final Tier 2", which exempted every `%compose` run (no Battle Plan) and dropped every halt. One rule, one home, and that home is a boot-read file. Nothing to author in a Battle Plan. |
| Escalation flag triggered | Surface to [the_prompter] before standard review |
| Tier 1 validator halt | HANK corrects and re-runs, or escalates. Output does not leave pipeline until the gate clears. |
| Tier 2 Meridian halt | HANK corrects and re-runs, or escalates to [the_prompter]. Output does not leave pipeline until the gate clears. |

---
## NOTES

- *(Architectural decisions, known constraints, version history)*
- *(If this pipeline is stateful — e.g., uses batch_tracker — document continuity behavior here)*
- *(If a Colonel .py is required, note the Claude Code work order requirement — FileLane rule)*
- *Tier 1 gates are deterministic and fire at every Captain boundary. Tier 2 gates are Meridian's reasoning and fire where judgment is required. Both are declared here — not invoked ad hoc.*
- *Verdict terms (`pass`, `output_failed`, `schema_missing`, `schema_malformed`) are defined in the Function Contract and quoted here verbatim. If the two disagree, the Function Contract wins.*

---
}
# END REGION cos_battle_plan.md CORE STANDARDS FILE
