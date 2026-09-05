# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** web_fetch
**Version:** 0.1
**Runtime:** MULTI-SUBSTRATE — declared per invocation, never chosen by this Captain. `rendered_anon` = CoWork native browser (Rung 4a) · `rendered_auth` = Claude in Chrome (Rung 4b). Both [Anthropic Ecosystem Exclusive].

---

## Stage Position — FETCH
*First stage of the four-stage retrieval chain: **Fetch -> Parse -> Extract -> Export.** This Captain does exactly one of those four things.*

**One job: get the page, say whether it worked, hand back the text.**

It does not read markup structure (Parse), does not target named values (Extract), does not write anything anywhere (Export), and forms **no opinion whatsoever** about what came back.

**Why the rung is an INPUT and not a second Captain.** One action, two costs. Under `DIP`(Dependency Inversion) the caller depends on the FETCH capability and names which rung to pay for — so a new browser, or a new rung, changes a parameter rather than minting a Captain. `SRP`(Single Responsibility) holds because the job is still one job.

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Retrieve the visible text of one URL at a caller-declared substrate rung, and report whether the retrieval succeeded. |
| Inputs | `url` (string, required) — the full URL to fetch. `substrate` (string, required) — `rendered_anon` \| `rendered_auth`. The CALLER declares the rung; this Captain never selects one. `invoked_by` (string, required) — calling Colonel, or `%compose`. |
| Outputs | `url_requested` (string) — the URL passed in. `substrate_used` (string) — the rung that ran. Always equal to the declared `substrate`; this Captain never climbs, and the field exists so that invariant is auditable rather than trusted. `fetched` (boolean) — **the verdict, and the whole of it**: a page was retrieved and text was returned. `page_text` (string) — the visible text, verbatim. `content_length` (number) — `len(page_text)`, COMPUTED from the returned text, never estimated. `extraction_scope` (string) — what the runtime scoped to, reported VERBATIM from the runtime (e.g. "article", "main", "body"). `failure_reason` (string) — populated only when `fetched: false`. `captain_source` (string) — always "web_fetch". `invoked_by` (string). |
| Error Behavior | **Runtime unreachable** (the declared substrate is absent, unauthorized, or no browser is selected): `{fetched: false, failure_reason: "runtime_unreachable"}`, verdict `output_failed`. RECOVERABLE halt under the Halt Protocol — the fallback is rung 1, the closed loop, where [the_prompter] supplies the page content in context. **This Captain does NOT retry on another rung; a substrate failure is surfaced, never absorbed.** **Fetch failed** (unreachable URL, DNS, HTTP error, timeout, no text returned): `{fetched: false, failure_reason: "fetch_failed"}`. **Access refused by the runtime** (the substrate declines the site): `{fetched: false, failure_reason: "access_refused"}` — the refusal stands and is reported, never routed around. **Everything else is `fetched: true`.** A thin page, a shell page, a sign-in wall, a consent gate, a stale page, a page missing the section the mission wanted — **all of these fetched successfully.** Whether what came back is USABLE is not this Captain's question. Do not retry. Surface to the Colonel. |
| Constraints | One URL, one substrate, per invocation. **Never climbs a rung from inside** — escalation is a per-URL Tier 2 judgment belonging to the Colonel (`SuffNotVol`, Sufficiency Is Not Volume: a higher rung is a DIFFERENT instrument with a different failure mode and can subtract content as easily as add it). Never authenticates, never dismisses a consent banner, never solves a challenge, at any rung. Never used to route around a refused or access-restricted domain — a refusal is a refusal, not a trigger. Returns raw text ONLY: no markup reading, no field targeting, no summarization, no writing. **Reports only what it observed** — it never infers, completes, or constructs a value it did not see, and it carries no field whose truth depends on what happened to render. **Both rungs are ATTENDED.** `rendered_auth` carries [the_prompter]'s live session and therefore the largest PII surface in the AI OS; a caller declares it deliberately, never by default. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `url_requested`, `substrate_used`, `fetched`, `captain_source`, `invoked_by` present and correctly typed; `captain_source` equals "web_fetch"; when `fetched: true`, `page_text`, `content_length`, and `extraction_scope` are non-null; when `fetched: false`, `failure_reason` is non-null. Structural facts only.

**Every required field is either an ECHOED INPUT, a CONSTANT, a COMPUTED value, or a VERBATIM runtime report.** None of them depends on what happened to render, and that is the design rule this contract is built on — a required field whose truth varies between two runs of the same page is a field the contract can be forced to lie in, and Tier 1 will pass the lie every time.

**Tier 2 (Meridian / Colonel) — everything the old design tried to put in the record:**
```
- Is a sign-in wall, consent gate, or paywall standing between us and
  the content? Infer it from CONTENT ABSENCE against mission
  expectation. Never from a Captain-emitted boolean: a wall is a thing
  that HAPPENED TO RENDER, and the same gated page has rendered with
  and without one on the same substrate.
- Did the fetch land where it was aimed? Not observable at every rung.
- Was the declared rung the right one to pay for?
- Is this content CURRENT, and does it COVER what the mission needs?
- Is a thin success effectively a failure for this mission?
```
None of that is visible to code, and none of it belongs in this record.

> **`content_length` and `extraction_scope` are REPORTING fields, not thresholds.** Tier 1 checks presence and type; it does not judge whether the number is *enough*, because "enough" is a property of the mission, not of the record. A `content_length` of 0 with `fetched: true` is valid and passes. What these fields buy is VISIBILITY — a thin success is seen rather than asserted.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "web_fetch",
  "required": ["url_requested", "substrate_used", "fetched", "captain_source", "invoked_by"],
  "types": {
    "url_requested": "string",
    "substrate_used": "string",
    "fetched": "boolean",
    "page_text": "string",
    "content_length": "number",
    "extraction_scope": "string",
    "failure_reason": "string",
    "captain_source": "string",
    "invoked_by": "string"
  },
  "constants": {
    "captain_source": "web_fetch"
  },
  "conditional": [
    { "when": {"fetched": true}, "require_non_null": ["page_text", "content_length", "extraction_scope"] },
    { "when": {"fetched": false}, "require_non_null": ["failure_reason"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` at v0.1 — live-confirmed 2026-09-05 against five real targets across both rungs, and RE-CONFIRMED after the rename to `web_fetch` (the `captain_source` constant changed, so the artifact Tier 1 checks changed — the five gates and six adversarial records were re-run against the renamed contract, same results). **Gate ledger: `gates_expected: 5`, `gates_fired: 5`, `reconciled: true`, all five `pass`, zero deltas** — every verdict returned by `validator.py` run against the record, not asserted.

Confirmed: `fetched: true` with `page_text`, `content_length` and `extraction_scope` non-null at `rendered_anon` (open page, `main`, 927 chars) and at `rendered_auth` (authenticated page, `main`, 474 chars); `fetched: false` with `failure_reason` non-null on a runtime-refused target; and the design's load-bearing claim — **a thin page (42 chars, `article`) and a sign-in wall (216 chars, `main`) both reported `fetched: true`**, because both were successful fetches and judging them is Tier 2.

Gate integrity was proven independently: six adversarial records were run against the same schema — wrong `captain_source` constant, null `extraction_scope` on a success, `fetched: false` with no `failure_reason`, `content_length` as a string, missing `invoked_by`, `fetched` as a string — and **all six returned `output_failed`, each naming the offending field.** A gate that never fails is not a gate; this one fails on exactly what it should.

**No INVOCATION LOG tick was written.** These were build-mode runs, and `AffDet` counts landed work, never attempts or tests.

Not yet demonstrated: the `runtime_unreachable` branch (no substrate was absent during this test) and the `fetch_failed` branch (the unreachable target was refused by the runtime before a fetch was attempted, which is `access_refused` — a different path).

---

## Fold-Back Record
*Section order is mandatory, not stylistic — `FldBkTail`(Fold-Back Tail), canonical in "captain_function_contract.md". This section carries spec PROVENANCE: why this contract has the shape it has. It is not a confirmation record (that is current status only, above) and not a failure pattern (those are CHECKS and live in the pattern library). Newest first.*.

**THE RULE THIS CONTRACT IS BUILT ON:** *a required output field must be an echoed input, a constant, a computed value, or a verbatim runtime report — never an observation whose truth can vary between two runs of the same page.* Anything that varies is a judgment, and judgments are Tier 2.

**What was kept, because it worked:** the substrate-as-input design (`DIP`), and both browser rungs, which each proved out live — a URL gated at `rendered_anon` returned in full at `rendered_auth`.
