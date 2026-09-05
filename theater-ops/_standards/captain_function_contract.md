# BEGIN REGION captain_function_contract.md CORE STANDARDS FILE
{
	🚨WARNING EDITING THIS REGION CAN HAVE DRAMTIC NEGATIVE IMPACT ON THE AI OS BEHAVIOR🛑
	🔥🌪️☢️☣️☠️
---

# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** [name]
**Version:** 0.1
**Runtime:** [Prose — no external dependency (rung 1) | CoWork WebSearch | Python (.py) | HubSpot MCP | Gmail MCP | Claude in Chrome MCP | ...]

---

The **Function Contract** is the Captain standard.
The Function Contract defines a unit of work and the unit of governance in the same object.
Captain governance is structural, not bolted on. A schema living in the same file as the Captain is structural. A schema in a lookup table is bolted on.
The Captain template is lean and precise.
No Ethos or Initiative — those belong to the Colonel commanding it.
The Colonel brings judgment. The Captain brings capability.
Different tools, different specs.

**The contract is now bilingual.**
The prose layers below are written for the human. The **Validation Schema** block is written for the machine — a deterministic twin of the prose that the validator engine consumes to return pass/fail without judgment. This is OutMisIso made literal: the contract is the check.

---
## Captain Authorship Lanes 
A Captain Function Contract may be authored or refactored by HANK behind a %shipit gate — FileLane governs, .md is HANK's lane; a .py Captain routes to Claude Code.
**Schema Fold-Back:**
When the change is Meridian's fold-back of a live Captain it audits, Meridian never writes it — the auditor never authors the spec it checks. Meridian surfaces the candidate; HANK drafts the exact edit (filename + line numbers + verbatim OLD/NEW) for [the_prompter]'s review; on [the_prompter]'s reviewed `%shipit`, HANK applies the .md edit (a .py Captain routes to Claude Code); Meridian re-verifies live. The gate is [the_prompter]'s review, not his keystrokes — an audited spec still tightens only through [the_prompter]'s `%shipit`.

**Genericity (`GenNotSpec`, Generic Not Specific):** a Function Contract states the SHAPE of a constraint. A live external identifier — a CRM record, a contact ID, a named person — creates a dependency the AI OS cannot see and cannot maintain, so it belongs in a Confirmation Discipline note as evidence, never in a Constraints line, a `constants` entry, or a `conditional` rule. Test before the write: if that record were deleted tomorrow, would the contract still say what to do?
---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | one sentence, what it does |
| Inputs | field names, types, required vs optional |
| Outputs | structured schema, described in plain language |
| Error Behavior | what it returns on failure |
| Constraints | scope limits, rate limits, anything the Colonel calling it needs to know |

**Fail-Fast (Captain form):** map the failure surface early — once Purpose is stated, write Error Behavior before polishing Inputs and Outputs. A Captain that cannot say precisely when it halts is not ready to say what it returns. The fail-closed rule below (`schema_missing` / `schema_malformed` = no deploy) is fail-fast made structural: detect at the boundary, halt immediately, report the exact verdict. Never mask — no default values, no fabricated fields, no proceeding on corrupted data.

**Runtime unreachable (Error Behavior, mandatory line).** Every Captain whose **Runtime** names an external connector MUST state, in Error Behavior, what it does when that connector is absent, unauthorized, or degraded. This is a RECOVERABLE halt under the Halt Protocol, not a terminal one: the Captain halts at the boundary, reports which runtime failed, and names its fallback — for most Captains that fallback is rung 1, the closed loop, where [the_prompter] supplies the record in context and the Captain reasons over it with no external call. A Captain whose Runtime is `Prose` carries no such line; it has nothing to be unreachable. Connector failure is NOT a new verdict — it returns `output_failed`, the existing term.

---

## Two-Tier Verification (read before writing the schema)

Every output field is checked at exactly one of two tiers. The author must assign every field a tier.

**Tier 1 — Code (the validator).** Structural truth: is the field present, non-null where required, correctly typed, and equal to any required constant? The validator answers with certainty on every run, whether or not anyone is watching. Deterministic. Unappealable within its scope.

**Tier 2 — Model (Meridian).** Semantic truth: is the content correct about the world, in the right voice, aligned to intent? No schema checks this. It stays with the Colonel and with Meridian, and it remains probabilistic by nature.

The rule that follows: **a Tier 1 failure halts the pipeline without judgment.** Code said no; the pipeline stops; Meridian logs and surfaces. Tier 2 findings remain judgment calls routed through HANK.

The validator checks *presence, type, and constants* only. It never decides whether a legitimately-null or empty field *should* have carried a value — that is a Tier 2 question the Colonel owns.

---

## Validation Schema (machine register) — MANDATORY

Every Captain MUST carry exactly one validation block, opened and closed by the named delimiters below. The delimiters are unambiguous by design — a bare  "```json ```" fence is NOT accepted, because documentation examples collide with it.

**Fail-closed rule:** a Captain with no `AIOS-VALIDATION` block, or with a malformed one, does not deploy. The validator returns `schema_missing` / `schema_malformed` — a distinct failure class from `output_failed` — and the pipeline halts. No schema, no pass.

Schema object contract:

- `required` — array of field names that must always be present and non-null. This is the whole of Tier 1's opinion on presence: *present and non-null*, nothing more.
- `types` — object mapping field name -> expected JSON type (`string`, `boolean`, `number`, `object`, `array`, `null`).
- `constants` — object mapping field name -> required literal value (e.g. `captain_source` must equal the Captain's own name).
- `conditional` — array of rules of the form `{ "when": {field: value}, "require_non_null": [fields] }`. This expresses "if `found: true`, then `email` and `captain_source` must be non-null." Conditional logic is required because most Captains have this shape; a flat required-list cannot capture it.
- `invoked_by` — **standard field on every Captain.** The name of the calling Colonel, or `%compose` when the Captain is called on the fly. Injected by HANK at orchestration time and echoed into the Captain's output record. Always in `required`, typed `string`, no constant (the caller varies). Presence is Tier 1; truth of the caller name, if it ever matters, is Tier 2. This field is what lets Frequency analysis attribute every invocation to its caller and see Colonel-level usage — without the validator ever running on a Colonel.

Fields not named in the schema are ignored — null or absent, the validator holds no opinion. Whether a present-but-empty or otherwise meaningless value is *wrong for the mission* is a semantic question and belongs to Tier 2 (Meridian), not to the validator. Tier 1 checks structural facts only.

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "[name]",
  "required": ["invoked_by"],
  "types": {"invoked_by": "string"},
  "constants": {},
  "conditional": []
}
```
<!-- AIOS-VALIDATION:END -->

---

**Wiring note:** This validator is invoked from the Battle Plan's **Tier 1 Validator Gate**, which fires at Captain output boundaries. The Colonel template (Mission Brief / IFPA) carries no validation block — Colonels are Tier 2, verified by Meridian's reasoning. This Function Contract is the **verdict-vocabulary source of truth**: the four verdict terms above (`pass`, `output_failed`, `schema_missing`, `schema_malformed`) are defined here and quoted verbatim by the Battle Plan. If the Battle Plan and this file ever disagree on a verdict term, this file wins.

---
## Confirmation Discipline

### LATEST-ONLY RULE — this section carries current state, never history.
*The same clause the `%REM SWEEP LOG` already runs under, applied to the Captain spec.*

1. ONE STATUS. This section states the CURRENT confirmation status and the run that earned it. When a new run confirms a new version, it REPLACES what was here. [C] replaces [O]. v3.1 replaces v3.0. No stacking, no "original note follows," no dated version list.
2. THIS SECTION IS THE ONLY HOME. The confirmation lives HERE and nowhere else — no copy in a pattern-library spoke, no copy in an archive. A [C] duplicated into the spoke is the SECOND COPY, and the spoke is the one that goes. The pattern library holds CHECKS that run against future output; a confirmation is a RECORD of a past run, and records are not kept.
3. WHAT SURVIVES COMPRESSION IS THE UNPROVEN, NOT THE PAST. Delete the narrative of what happened. KEEP any statement of what the current version has NOT yet demonstrated — that is live hypothesis state under EvalHyp, not history, and dropping it launders an untested claim into a confirmed one. "What the next live run must demonstrate" stays.
4. FAILURES ARE NOT KEPT HERE. A failed or superseded run is dropped from this section on the next confirmation. It is NOT dropped from the pattern library — a failure pattern there is a CHECK that runs against future output, and deleting it removes a test rather than a story.
5. NO HISTORY IS KEPT ANYWHERE. When a new run replaces this section, the superseded narrative is not relocated, not archived, and not summarized — it is dropped. If it has residual value for a public write-up, it goes to "cos-output/" (excluded from `%sync`, never boot-read, never swept) and never back into an operational file.

**Shape of a compliant section — four lines or fewer in the ordinary case:**
```
`Status: [C]` at vX.Y — live-confirmed YYYY-MM-DD against <target>.
<the fields that were checked, the validator verdict, deltas.>
Not yet demonstrated: <only if something is genuinely untested>
```

**Rationale — the contract is a spec, not a log.** A Captain is read every time it is invoked; the audit trail is read at `%REM`. Carrying history in the contract charges invocation-time tokens for a record nobody consults at invocation time. `TknEff`(Token Efficiency) is a standing architectural constraint, not a preference — and the capability catalogs already prove the pattern works: `captain_reference.md` has always carried latest-status-only and no one has ever missed the history.

---

## SECTION ORDER — MANDATORY, not stylistic (`FldBkTail`, Fold-Back Tail)
*This rule is placement, not formatting. A contract that violates it is malformed and Meridian flags it at spec review, the same standing as a missing `AIOS-VALIDATION` block.*

**A fold-back write-up goes at the BOTTOM of the file, after Confirmation Discipline. Never inline with the layer it tightened.**

```
1. Header (Captain Name, Version, Runtime)
2. Prose Layers
3. Two-Tier Assignment
4. Validation Schema (AIOS-VALIDATION)
5. Confirmation Discipline          <- current status, latest-only
6. Fold-Back Record                 <- every fold-back, newest first
```

**Why the bottom and nowhere else.** `TopDwnPrm`(Top Down Semantic Priming): the model reads top-down and weights early tokens heavily, so whatever sits above the Validation Schema shapes how the schema is read. A fold-back is a **narrative of a past defect** — the most load-bearing text in the file for a HUMAN reviewing the spec's history, and the LEAST load-bearing for a model about to invoke the Captain. Placing it inline primes every invocation with the story of a bug that no longer exists. The rule is the same one the Rationale above states, applied to position rather than to volume: the contract is a spec first and a history second, so the history goes last.

**What a Fold-Back Record entry carries** — the SHAPE of what was wrong and the rule it produced, never a run transcript:
```
### FOLD-BACK vX.Y — <what changed, in four words>
*<how it was found, and on what date.>*
<The defect, stated as a class. The governing rule. What a caller
 loses or gains. Newest entry first.>
```

**The boundary against the pattern library, restated because this is where it blurs.** A fold-back record explains why THIS contract has the shape it has — it is spec provenance, and it lives here. A failure pattern is a CHECK that runs against FUTURE output of any unit — it lives in the pattern library, hub or spoke per the PATTERN PLACEMENT RULE. The same live run routinely produces one of each; writing either into the other's home is drift. **Neither is a Confirmation Discipline entry**, which carries current status only.

**Genericity still binds.** A Fold-Back Record is authored under `GenNotSpec`(Generic Not Specific) like every other line in this file: name the class of defect and the rule it produced; a URL, record, or account is evidence in one clause, never the rule itself.

---

A validation schema is a **hypothesis until a live output runs against it** and earns `[C]` status. The rewritten contract and the validator work order are two halves of one test — neither is confirmed until they run together against a real record. No auto-generated schema reaches production on internal consistency alone.

**The discipline runs both directions.** Confirmation is not a one-time gate at birth. A live run can reveal what the schema didn't know — a field that is always read-only, a property absent on the object, a caller-specific constant. When Meridian confirms such a lesson `[C]` and it is *local to one Captain* — a fact about this Captain's structure, not a system-wide rule — it is **fed back into this contract** so the spec stops being naive. The loop, and its authority boundary:
```
1. **Meridian confirms and classifies.** The pattern earns `[C]` in "meridian_memory.md" and is tagged Captain-local. Meridian writes its own file only.
2. **Meridian surfaces a fold-back candidate to HANK** — the pattern, the target Captain, and the layer it touches (a Constraints line, a `constants` entry, a `conditional` rule).
3. **HANK drafts a work order** naming the exact edit. HANK does not make it.
4. **[the_prompter] reviews the proposed edit (filename + line numbers + verbatim OLD/NEW) and gates it (%shipit); HANK then applies it — a .md Function Contract is written by HANK behind that reviewed gate; a .py Captain routes to Claude Code via a work order. **Meridian never writes a Captain's Function Contract — the auditor does not author the spec it audits.** If no contract exists yet, the edit mints one from the confirmed pattern. Meridian proposes and verifies; it never holds the pen on the spec it audits — HANK holds the pen only after [the_prompter]'s reviewed gate.
5. **Meridian re-verifies against the next live run.** The tightened schema is a new hypothesis — `[C]` is re-earned against real output, not granted on the edit alone.
```
This is the same surface -> work-order -> `%shipit` -> execute -> verify loop the AI OS runs to build anything; here the target artifact is the Captain's own contract. The audit trail stays un-editable by the entities it audits, and the contract tightens only through [the_prompter]'s gate — the Captain spec stays sovereign.

---

## Reference — Worked Example (hubspot_contact_lookup)
Earlier iterations of the `hubspot_contact_lookup` prose said, in Constraints: *"Meridian enforces: `found` field always present. If `found: true`, `email` and `captain_source` must be non-null. Null fields are valid."* V3(AI OS current iteration) moved the Captain from single-match (`email`) to many-match retrieval (`candidates[]` + `match_count`). That current contract, made machine-checkable:

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "hubspot_contact_lookup",
  "required": ["found", "match_count", "captain_source", "invoked_by"],
  "types": {
    "found": "boolean",
    "match_count": "number",
    "identifier": "string",
    "captain_source": "string",
    "candidates": "array",
    "invoked_by": "string"
  },
  "constants": {
    "captain_source": "hubspot_contact_lookup"
  },
  "conditional": [
    { "when": {"found": true}, "require_non_null": ["candidates"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

Read it against the current contract: `found` and `match_count` always present (`required`); `candidates` non-null only when `found: true` (`conditional`); `captain_source` pinned to the Captain's own name (`constants`). Profile fields inside each candidate — `company`, `jobtitle` — aren't named in the schema, so the validator ignores them. Presence and type are Tier 1. Whether a null `company` on a candidate *should* have been filled is Tier 2 — the Colonel's call. (Current schema; mirrors `hubspot_contact_lookup.md` v3 — the canonical copy.)

---
}
# END REGION captain_function_contract.md CORE STANDARDS FILE