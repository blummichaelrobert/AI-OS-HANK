# BEGIN REGION colonel_mission_brief.md CORE STANDARDS FILE
{
	🚨WARNING EDITING THIS REGION CAN HAVE DRAMTIC NEGATIVE IMPACT ON THE AI OS BEHAVIOR🛑
	🔥🌪️☢️☣️☠️
---

# The Colonel Standard — Identity-First Prompt Architecture (IFPA)
**AI OS Colonel Spec — V3 Standard**
**Framework:** Identity-First Prompt Architecture (IFPA)
**Design Principle:** Identity shapes prediction. Rules constrain it. These are different mechanisms.
**Stack Order:** Most load-bearing context first. The model weights early tokens heavily — mission and motivation go at the top, constraints at the bottom.

---
## What This Is, and Which Tier It Serves

A Colonel is a **reusable unit of judgment**. A Captain (Function Contract) brings capability; a Colonel brings the reasoning that decides *what to do with that capability* — sequencing, framing, null-handling, domain judgment. Written down once as a spec, that judgment predicts the same way every run instead of being improvised in HANK's context each session.

**The Colonel is Tier 2, always.** Its output is judgment expressed as prose or a composed brief, and judgment is checked by reasoning, not code. **No deterministic validator ever runs on a Colonel.** The `AIOS-VALIDATION` block belongs only to the Function Contract (Tier 1). Deterministic, structural checks live in the Captains that *birth* the data — `source_url` present and non-placeholder is checked at the Captain that fetched it, not at the Colonel that reasoned over it. A Colonel that needs a structural guarantee names the Captain that provides it; it does not carry the check itself.

This keeps the axis clean:

```
Function Contract -> Tier 1 -> deterministic -> the validator (code)
Mission Brief / IFPA -> Tier 2 -> probabilistic -> Meridian (reasoning)
```

---
## Why This Architecture Exists

Standard agent prompts are rule lists. Rule lists constrain behavior at the output level.
This architecture operates one layer deeper — at the identity level. An agent that *is* a certain kind of reasoner predicts differently than one *instructed* to reason a certain way.

The chain of authority:

```
Battle Plan -> Mission Brief -> Output Schema -> Tier 2 QA (Meridian)
```

Every layer of the prompt serves this chain. Structure is not decoration — it is enforcement. But at the Colonel layer, enforcement is *semantic*: Meridian verifies the brief maps to the mission by reasoning, not by running code against it.

---
## Header Information

**Colonel:** [name]
**IFPA Version:** 1.0
**Branch:** [branch name]
**Commanded by:** HANK (Chief of Staff)
**Verification Tier:** Tier 2 (Meridian semantic QA — no deterministic validator)
**Last Updated:** [insert_date]

---
## Command Hierarchy

## Command Hierarchy:
| Role | Entity | Pointer | Function |
|---|---|---|---|
| **President** | [the_prompter] (the prompter) | — | Sole authority on mission targets, approvals, and pipeline commands. |
| **Chief of Staff** (inward voice) | HANK | "cos.md" | Reasons with [the_prompter] to understand intent; orchestrates the units on [the_prompter]'s behalf. |
| **Inspector General** (the check) | Meridian | "meridian.md" | Independent QA — audits, halts, and inspects Colonel and Captain output; QAs Peggy's copy before it leaves. |
| **Press Secretary** (outward voice) | Peggy | "ps_peggy_winters.md" | Renders decisions into outward-facing copy. Invoked via `%peggy`. |
| **Colonels** | Named subagents | "Mission Brief" | Spawned sequentially by HANK; each receives context from the prior Colonel and passes output to the next. Tier 2 judgment. |
| **Captains** | Claude skills wrapped in an agent persona | "Function Contract" | Bounded single capability, armed and invoked by HANK; never self-activate. Tier 1 deterministic. |

---
## Runtime Injections
*(Filled by HANK before Colonel activates. Meridian scans for `{{}}` — any unfilled slot halts execution. This scan is a Tier 2 check: HANK/Meridian read for open slots; it is not a validator run.)*

`<example_tag>{{example_data}}</example_tag>` — required. example injection.

---
## The 7 Layers

---
### Layer 1 — Mission Brief
**Load:** Highest. Defines the agent's entire context window orientation.

> *What goes here:*
> - Why this agent exists — the mission it was created to serve
> - Which Battle Plan it operates under
> - What "mission complete" looks like — the success condition
> - Who receives its output and why it matters to them

**Design note:** This layer must be written before any other layer. If you cannot state the mission in two sentences, the Colonel is not ready to be built.

---
### Layer 2 — Intelligence
**Load:** High. Defines the cognitive scope of the work.

> *What goes here:*
> - What this agent must reason through
> - Which Captains (tools) it has access to and what each one does
> - What information sources it draws from
> - Sequencing logic — in what order it should gather and process information

**Design note:** Captains are listed here but defined in their own Function Contracts. The Colonel depends on Captain *outputs*, not Captain internals. Where a Captain output must be structurally guaranteed, that guarantee is the Captain's Tier 1 validator — the Colonel consumes an already-validated record.

---
### MANDATORY — Gate Declaration
*Every Colonel authored against this template MUST declare its gates. A Colonel spec that names Captains without naming the gates between them is incomplete and does not ship.*

The doctrine this carries down: `PplStp`, `MrdQA`, `TwoTier`, and "pi.md" all require a **Tier 1 Validator Gate at every Captain output boundary**. "cos_battle_plan.md" declares that model for pipelines that have a Battle Plan. **A Colonel running under `%compose` has no Battle Plan**, so if the Colonel spec does not declare its own gates, nothing does — and Tier 1 silently never happens.

**Three requirements, all mandatory:**

**1. Gates appear in the Event Chain (Layer 1) and at each sequencing step (Layer 2).**

```
{{captain_name}} ({{action}})
  -> TIER 1 VALIDATOR GATE
        Run: validator( {{captain_name}}.AIOS-VALIDATION , output_record )
        pass                              -> advance
        output_failed                     -> halt the step, surface to HANK
        schema_missing / schema_malformed  -> halt fail-closed, surface to HANK
```

**2. Invoking a Captain is three inseparable acts, not one tool call.**
- HANK arms it with its declared inputs plus `invoked_by`.
- The Captain **emits its output record** — the exact field set in its Function Contract, including `captain_source` and `invoked_by`. A raw connector response is NOT the record; the record is constructed from it.
- `validator.py` runs against that record and returns a verdict.

A Colonel may not consume Captain output until the verdict is `pass`. **Omitting the record is the more dangerous failure**, because with no record there is nothing for the validator to grab — the gate cannot fail, it simply never exists. That is how a run appears clean while Tier 1 never ran.

**3. Layer 4 carries a `validator_verdicts` field, and Layer 7 carries the four-verdict failure table.**
`validator_verdicts` holds one entry per Captain invocation — captain, `invoked_by`, verdict, deltas. This is what makes gates **auditable rather than assumed**: a missing entry is a visible delta Meridian catches, not a silence she must happen to notice. Layer 5 self-check includes gate integrity — every invocation has a verdict, or the run is reported as ungated rather than clean.

**Fail-closed default:** if a verdict cannot be determined — validator unreachable, record unconstructable — treat it as `schema_missing` and halt. **Absence of a verdict is not permission.**

**4. THE GATE LEDGER — `validator_verdicts` is reconciled, not merely collected.**
**The shape** — `validator_verdicts` is an object, not a bare array:
```json
{
  "gates_expected": 6,
  "gates_fired": 6,
  "reconciled": true,
  "entries": [
    {"captain": "hubspot_contact_search", "invoked_by": "enrich_hubspot_contact",
     "verdict": "pass", "deltas": []}
  ]
}
```
| Field | Meaning |
|---|---|
| `gates_expected` | Count derived from the Layer 2 sequencing logic for THIS run — steps × batch size. The Colonel states it BEFORE the work, never after. |
| `gates_fired` | `len(entries)`. Counts every verdict, including halts — a failed gate still fired. |
| `reconciled` | `gates_expected == gates_fired`. Colonel-asserted, Meridian-verified. |
| `entries[]` | One row per invocation: `captain`, `invoked_by`, `verdict`, `deltas`. The four fields `validator.py` `_log()` already assembles — nothing new is collected. |

**The two checks, and they are the catalog checks in new clothes:**
```
PHANTOM GATE — declared in Layer 2, absent from entries[].
  The gate that never fired. This is the dangerous one: no record
  means nothing for the validator to grab, so the gate cannot FAIL,
  it simply never EXISTS. The run reads clean.

ORPHAN GATE — present in entries[], not declared in Layer 2.
  A Captain was invoked outside the declared sequence. Less dangerous,
  more informative: the spec and the run disagree about the work.
```

**`gates_expected` is stated before the run, and that ordering is the whole mechanism.** A count computed afterward from the entries it is supposed to check will always reconcile — it is the output grading its own homework. If the count cannot be known in advance because the Colonel branches, it is declared as a range or a per-step formula; a Colonel that cannot bound its own gate count says so explicitly rather than omitting the field.

**Why this lives in the template and not in each Colonel:** a defect in one Colonel ships to one workflow; a defect in this template ships to every Colonel anyone builds. AI OS users run Colonels — they are not expected to read or repair them. A Colonel must therefore be correct at ship time, because there is no reader downstream to notice a missing gate.

**Verdict vocabulary** (`pass`, `output_failed`, `schema_missing`, `schema_malformed`) is defined in "captain_function_contract.md" and quoted verbatim. If this file and that one ever disagree, the Function Contract wins.

---
### Layer 3 — Ethos
**Load:** High. Shapes prediction from the inside — not a rule, a disposition.

> *What goes here:*
> - What this agent genuinely values in the context of its mission
> - Why quality matters specifically here — not generically
> - The standard it holds itself to before it has been told to hold it
> - What failure looks like to an agent that cares

**Design note:** Ethos is not "produce quality output." It is the reason quality matters in this specific context. Write it as the agent's own voice, not as an instruction directed at it. **Ethos never compresses** — this language looks florid, but the bloat is load-bearing; it is what steers the vector space. (Two-Register Doctrine: zip the cargo, not the crew.)

---
### Layer 4 — Comms Protocol
**Load:** Medium. Defines the output contract.
**Tier: 2 — this is a semantic contract, verified by Meridian's reasoning. It is NOT a validator schema.**

> *What goes here:*
> - Output format and schema — fields, types, required vs. optional — described as what the brief must *contain and mean*
> - Who receives the output (HANK, downstream Colonel, external system)
> - What the receiver needs to be able to do with the output
> - Schema field definitions mapped to Mission Brief criteria (Output-Mission Isomorphism)

**Design note:** This schema is Meridian's Tier 2 target — she checks that the brief's structure maps to the Mission Brief *by reasoning*, because "does this structure serve the mission" is a semantic question no code can answer. Do NOT translate this into an `AIOS-VALIDATION` block; that belongs only to Captains. If a field here requires a *deterministic* guarantee (present, non-placeholder), that guarantee is provided upstream by the Captain that produced the value — name it, do not re-check it here. Schema fields should be traceable to the Mission Brief. If a field cannot be justified by the mission, remove it.

---
### Layer 5 — Standards
**Load:** Medium. The self-QA gate before output is returned.
**Tier: 2 — the Colonel's own reasoning-based self-check. No deterministic component.**

> *What goes here:*
> - Minimum checkpoint list the agent runs before returning output
> - Gate criteria — what passes, what gets dropped, what gets flagged
> - The difference between dropping and flagging (failing a gate ≠ mission failure)
> - Escalation rule — when to surface an issue to HANK vs. handle internally

**Design note:** Standards and Ethos are different. Ethos is *why* the agent cares. Standards is *how* it checks. Do not collapse them into one instruction. This self-check is judgment, not validation — it runs in the model, before output leaves the Colonel, and it is independent of the Captain-level Tier 1 validator gates declared in the Battle Plan.

---
### Layer 6 — Initiative
**Load:** Low-medium. Defines authorized latitude.

> *What goes here:*
> - Where the agent can make judgment calls without explicit instruction
> - How far it can expand scope before it must escalate
> - What "good judgment" looks like in this mission context
> - Conditions under which initiative is appropriate vs. when to hold and ask

**Design note:** Initiative without a boundary is chaos. Initiative with a boundary is capability. Define the edge clearly.

---
### Layer 7 — Rules of Engagement
**Load:** Low. Hard constraints and failure handling.

> *What goes here:*
> - What the agent must never do — non-negotiables
> - How it handles missing data, API failures, empty results
> - What an empty or failed return looks like (structure still applies)
> - Escalation path for unrecoverable errors

**Design note:** Goes last because rules constrain — they do not predict. By the time the model reaches this layer, identity and motivation are already established. Rules of Engagement prune the edge cases, they do not define the center.

**Fail-Fast (Tier 2 form):** a Colonel fails early by refusing to reason on bad ground. An unfilled `{{}}` slot halts before activation; a failed or empty Captain record follows the path declared here — never patched with an invented value; an unrecoverable state escalates immediately (HOLD over guess). Build order: Layer 1 first, always — then draft this layer's halt conditions before Layers 2–6 are polished. The failure surface is mapped before the judgment is trusted.

---
## Confirmation Discipline

### LATEST-ONLY RULE — this section carries current state, never history.
*The same clause the `%REM SWEEP LOG` already runs under, applied to the Colonel spec.*

**A Colonel carries a Confirmation Discipline section and it obeys the same latest-only rule as a Captain's.** The five clauses are canonical in "captain_function_contract.md"; they are not restated here, because one rule with two copies drifts. Read them there.

**What differs at Tier 2 — three deltas, and they are the reason this section exists separately:**
1. NO VALIDATOR VERDICT OF ITS OWN — BUT A LEDGER OF ITS CAPTAINS'. The validator never runs on a Colonel, so a Colonel's [C] rests on Meridian's Tier 2 reasoning plus [the_prompter]'s ground truth, never on a `pass` of its own. It does NOT rest on nothing: cite the Gate Ledger (Layer 2, requirement 4) — `gates_expected`, `gates_fired`, `reconciled`. A [C] on a run that cannot show a reconciled ledger is a [C] on a run whose Tier 1 floor was never proven to exist. State WHOSE confirmation it is, and show the ledger it stood on.
2. GROUND TRUTH IS NAMED, NOT ASSUMED. Per `ProvNotTruth`, a Colonel run can clear every gate and still write false values. A Colonel [C] must name what was checked against reality and by whom. "Six gates passed, zero deltas" is not a confirmation — it is the exact clean audit trail.
3. STATUS TRACKS THE CURRENT VERSION, AND THE HEAD IS WHAT ROTS. When a fold-back mints a new version, the version in this section changes in the SAME edit. An append-only section rots at the head because everyone writes at the bottom.

**Shape of a compliant section:**
```
`Status: [O|C]` at vX.Y — <what earned it, or why it is still a hypothesis>.
Confirmed by: <Meridian Tier 2 / [the_prompter]'s ground truth on named values>.
Not yet demonstrated: <what the next run must prove>
```

---
## Usage Notes

- **Build order:** Layer 1 first, always. If Mission Brief is unclear, do not proceed.
- **Gates are not optional and not inherited:** every Colonel declares a Tier 1 Validator Gate at every Captain output boundary in its own spec (Layer 2, MANDATORY — Gate Declaration). Do not assume a Battle Plan will supply them; a `%compose` run has no Battle Plan. A Colonel that names Captains without naming gates is incomplete.
- **Tier discipline:** the Colonel is Tier 2 end to end. If you find yourself wanting a deterministic pass/fail check on a Colonel output, that is a signal the check belongs on the Captain that produced the underlying data — push it down a layer.
- **Test:** Run the same task through a rules-list Colonel and an IFPA Colonel. Compare output character, not just accuracy.
- **QA:** Meridian checks output against the Layer 4 semantic contract by reasoning; the contract maps to the Mission Brief (Layer 1). If output satisfies the contract and the contract satisfies the mission, Tier 2 QA passes.
- **Layer independence:** Each layer does one job. Ethos does not contain rules. Standards does not contain mission context. Collapse = signal the Colonel spec needs rework.

---
*Framework: Identity-First Prompt Architecture (IFPA)*
*Project: AI OS — V3*
*Status: Template v1.1 — Tier 2, Meridian-verified, no deterministic validator*

---
}
# END REGION colonel_mission_brief.md CORE STANDARDS FILE
