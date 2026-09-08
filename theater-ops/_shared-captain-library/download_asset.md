# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** download_asset
**Version:** 0.1
**Runtime:** Claude in Chrome (Rung 4b) [Anthropic Ecosystem Exclusive] — ATTENDED

---

## Stage Position — RETRIEVE
*Third and final stage of the interactive browser chain: **Arrive -> Submit -> Retrieve.** It creates no state and reaches no URL; it operates only on a handle it was handed.*

**One job: actuate the download control for one named asset on an already-rendered response, and report what it could observe about where it went.**

It does not navigate (Arrive), does not prompt (Submit), does not choose WHICH asset (the Colonel does that, from `candidates[]`), and **never opens, decodes, or inspects the file** — whether the image is good cannot be answered from a file record.

**This Captain is the AI OS's canonical example of an observability boundary**, and its schema is shaped by it: what a browser will tell you about a completed download is far less than what a caller would like to know, and the contract admits that rather than papering over it.

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Trigger the download of one identified asset from an already-rendered response on a handed tab, and report what was observed about the transfer. |
| Inputs | `tab_id` (string, required) — the handle from `submit_and_await`, passed through opaquely. `asset_description` (string, required) — a natural-language description identifying WHICH asset to retrieve, supplied by the Colonel after it chose from `candidates[]`. This Captain locates; it does not select. `invoked_by` (string, required) — the calling Colonel, or `%compose`. **Caller-supplied, no default.** |
| Outputs | `tab_id` (string) — passed through unchanged. `download_triggered` (boolean) — **the verdict, and the whole of it**: the download control was found and actuated. `download_confirmed` (boolean) — **observe-and-report-if-visible**, `null` where the runtime exposed no completion within the observation window. `file_name` / `landing_path` / `file_type` (string) — all observe-and-report-if-visible, `null` where not exposed; **never predicted, never constructed.** `captain_source` (string) — always "download_asset". `invoked_by` (string). `error` (string) — populated only on a failure branch. |
| Error Behavior | **Runtime unreachable / tab invalid** (the connector is absent, or the handle is stale, closed, or navigated away): `{download_triggered: false, error: "tab_invalid"}` — a RECOVERABLE halt; the fallback is rung 1, the closed loop, where [the_prompter] retrieves the asset by hand. **Download control not found** (`asset_description` matches nothing actionable on the page): `{download_triggered: false, error: "control_not_found"}`. **Actuated, nothing observable followed** (the control fired and neither a completion nor a failure was exposed within the window): `{download_triggered: true, download_confirmed: null, error: "outcome_unobservable"}` — **this is NOT a failure claim.** It states that this Captain's scope did not reach the answer, which is a fact about scope and not about the transfer. **A guessed filename, a constructed path, or an assumed completion is a fabricated field and violates the never-mask rule of `FlFst`(Fail-Fast) outright.** Do not retry. Surface to the Colonel. |
| Constraints | One asset per invocation. **Operates ONLY on the handed `tab_id`** — never navigates, never submits, never re-prompts, never downloads from a source other than the response already rendered on that tab. **Reports the landing location; never moves, renames, copies, or deletes the file** — relocation is out of scope by design and belongs to the operator or a unit with filesystem scope. **Never opens, decodes, or inspects the file's contents.** Never selects among assets: the Colonel supplies `asset_description` having already chosen. **THE OBSERVABILITY BOUNDARY, stated as a constraint because that is where it belongs:** download metadata does not live on the handed tab, and this Captain's scope is that tab — so a filename, a path, a type, and often the completion itself are things it may report if visible and must otherwise leave `null`. **ATTENDED**: this rung carries [the_prompter]'s live session. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `tab_id`, `download_triggered`, `captain_source`, `invoked_by` present and correctly typed; `captain_source` equals "download_asset". **No conditional on success**, by design.

**Every required field is an ECHOED INPUT, a CONSTANT, or an ACTION THIS UNIT PERFORMED.** `download_triggered` is the only success-side fact this Captain can guarantee on every run, because actuating a control is something it DOES; everything after the actuation is something it may or may not be shown.

> **`download_confirmed` was demoted from required to observable, and it is the reason `ScopeObs` exists.** An earlier contract required it. Live evidence across runs: a completion toast rendered and was observed on one run, and on two actuations of the same control on the same page **no completion appeared in the observation window at all**. The contract behaved correctly every time — it reported what it saw — but a required field whose truth depends on what happened to render forces the unit either to halt on a successful run or to invent a value. **`ScopeObs`, canonical in the hub: a unit may not be required to report what its own declared scope cannot observe.** Its sibling `PartGate` governs VARIABILITY; this field failed both tests at once.

**Tier 2 (Meridian / Colonel):**
```
- Is the retrieved asset the one the mission wanted?
- Does the image satisfy the brief? (unanswerable from a file record)
- Is an unobservable outcome acceptable for this run, or a halt?
- Where did the file actually go? — obtain it from the operator or a
  unit with filesystem scope; NEVER ask this Captain to infer it.
```

**The consequence a commanding Colonel must hold:** `download_confirmed: null` is the EXPECTED value, not an anomaly. A Colonel that treats `null` as a failure will report honest runs as broken; a Colonel that treats it as success will report unshipped work as delivered. **It is neither — it is a question this chain cannot answer, and the honest brief says so.**

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "download_asset",
  "required": ["tab_id", "download_triggered", "captain_source", "invoked_by"],
  "types": {
    "tab_id": "string",
    "download_triggered": "boolean",
    "download_confirmed": "boolean",
    "file_name": "string",
    "landing_path": "string",
    "file_type": "string",
    "captain_source": "string",
    "invoked_by": "string",
    "error": "string"
  },
  "constants": {
    "captain_source": "download_asset"
  },
  "conditional": [
    { "when": {"download_triggered": false}, "require_non_null": ["error"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` at v0.1 — live-confirmed against a generated asset at Rung 4b. **Gate ledger: `gates_expected: 3`, `gates_fired: 3`, `reconciled: true`** — every verdict returned by `validator.py` run against the record, never asserted.

Confirmed: `download_triggered: true` — the control was located from `asset_description` among two candidates and actuated — and the record **passed Tier 1 with `download_confirmed`, `file_name`, `landing_path` and `file_type` ALL null**, which is the whole point of the demotion: an honest run no longer halts on fields the runtime declined to expose. `error: "outcome_unobservable"` fired correctly, stating that the answer lay outside this unit's scope rather than claiming a failure. **The observability boundary reproduced exactly as recorded**: no completion metadata appeared on the handed tab within the window, on a transfer that was actuated successfully. Gate integrity proven independently: adversarial records — a wrong `captain_source` constant, and `download_triggered: false` with no `error` — **both returned `output_failed`**, each naming the offending field.

**No INVOCATION LOG tick was written.** These were build-mode runs, and `AffDet` counts landed work, never tests.

Not yet demonstrated: the `control_not_found` and `tab_invalid` branches; and a run in which `download_confirmed`, `file_name`, `landing_path` and `file_type` are all populated — **no runtime has yet exposed them**, so the optional half of this contract's Outputs has never been exercised.

---

## Fold-Back Record
*Section order is mandatory, not stylistic — `FldBkTail`(Fold-Back Tail), canonical in "captain_function_contract.md". Spec PROVENANCE only. Newest first.*

### FOLD-BACK v0.1 — `download_confirmed` demoted, `outcome_unobservable` branch added
*Live-discovered: a completion toast on one run, and none on two actuations of the same control on the same page.*

The prior contract treated `download_confirmed` as a dependable success signal. It is not: it is an observation, and the same page produced it and withheld it on different runs.

**THE RULE, twice over.** `PartGate`: a required field must never be an observation whose truth can vary between two runs of the same page. `ScopeObs`: a unit may not be required to report what its own declared scope cannot observe. Download metadata does not live on the handed tab, and this Captain's scope IS that tab — so the boundary belongs in Constraints, and the schema may only require what that boundary admits.

The `outcome_unobservable` branch was added so the record can distinguish *"I actuated and was told nothing"* from *"I actuated and it failed"* — previously the same shape. Naming the branch turns a silence into a reportable state.

**What a caller loses:** the illusion of a confirmed download. **What it gains:** a run that does not halt when the browser simply declines to say.

### FOLD-BACK v0.1 — `file_name`, `landing_path`, `file_type` kept but never required
*Carried forward from a confirmed live halt.*

An earlier version required `file_name` and `file_type` non-null on a confirmed download. The live run halted `output_failed` on a transfer that had genuinely completed, because the only route to a `pass` was inventing a filename. The keys are retained — a future runtime with filesystem scope could fill them — but they are **observe-and-report-if-visible, and are never constructed.**

### FOLD-BACK v0.1 — `tab_id` typed `string`
*Applied at authoring, from the chain-wide substrate finding.*

The handle is a verbatim runtime report whose shape belongs to the substrate; this Captain treats it as an opaque token and does no arithmetic on it. Typing it `number` rejected valid handles such as `"seed"` and `"tab-1"` on runs that had succeeded.

Built on the rule the Fetch rebuild produced, and on the boundary this Captain's own history established: *a required output field must be an echoed input, a constant, a computed value, or a verbatim runtime report — and it must be REACHABLE within the unit's declared scope.*
