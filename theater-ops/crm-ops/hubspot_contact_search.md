# Captain Function Contract
**Captain Name:** hubspot_contact_search
**Version:** 1.1
**Runtime:** HubSpot MCP (`search_crm_objects`)

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Retrieve a page of HubSpot contacts matching one property filter, for callers that need a *batch* rather than one identified person. |
| Inputs | `filter_property` (string, required) — the contact property to filter on (e.g. `ai_os_enrichment_status`). `filter_operator` (string, required) — one of `HAS_PROPERTY`, `NOT_HAS_PROPERTY`, `EQ`, `NEQ`. `filter_value` (string, optional) — required for `EQ`/`NEQ`, MUST be omitted for `HAS_PROPERTY`/`NOT_HAS_PROPERTY`. `limit` (number, optional) — page size, default 10, hard max 200. `properties` (array of string, optional) — contact fields to return; defaults to `firstname`, `lastname`, `email`, plus `filter_property`. `offset` (number, optional) — paging cursor returned by a prior call. |
| Outputs | `found` (boolean) — true if this page returned one or more contacts. `match_count` (number) — contacts returned in **this page**. `total` (number) — total contacts matching the filter portal-wide, across all pages. `contacts` (array) — always present, one object per match, each carrying `contact_id` plus the requested properties (any property may be null). `offset` (number or null) — cursor for the next page; **normalized by the Captain to null when no further page exists** (see Constraints — the connector does not do this itself). `filter_property` (string) and `filter_operator` (string) — echoed back. `captain_source` (string) — always "hubspot_contact_search". `invoked_by` (string) — the calling Colonel, or `%compose`. |
| Error Behavior | **Runtime unreachable (mandatory).** If the HubSpot MCP connector is absent, unauthorized, or degraded, the Captain halts at the boundary and returns `{ "found": false, "match_count": 0, "total": 0, "contacts": [], "offset": null, "error": "runtime_unreachable: hubspot_mcp", "captain_source": "hubspot_contact_search" }`. This is a RECOVERABLE halt under the Halt Protocol, verdict `output_failed` — not a new verdict term. Named fallback is rung 1: [the_prompter] supplies the contact batch in context and the commanding Colonel reasons over it with no external call. **Other failures.** On a rejected filter, unknown property, or any other MCP error, returns the same shape with `error` set to the verbatim rejection text. On a legitimate zero-result search the Captain does **not** error — it returns `found: false`, `match_count: 0`, `contacts: []`, and the real `total`. The Colonel must not proceed on `error` — surface to HANK. |
| Constraints | The Captain **retrieves**; it does **not disambiguate** and it **never writes**. It is mission-agnostic: it does not know what enrichment, or any other workflow, means — it takes a filter and returns contacts. Exactly one filter in one filter group; multi-filter and association search are deliberately out of scope (KISS — add a version when a live workflow needs it). Paging is the caller's responsibility: the Captain returns `offset` and holds no cursor state between calls. **Offset normalization (mandatory, live-confirmed).** `search_crm_objects` returns a numeric `offset` cursor even when the result set is exhausted — a run with `match_count: 6` and `total: 6` still returned `offset: 6`. A caller looping on "while offset is not null" would never terminate. The Captain therefore normalizes before emitting: **if `(incoming offset) + match_count >= total`, emit `offset: null`.** Null is the stop signal; the Captain absorbs the connector's quirk so no commanding Colonel has to know about it. **Live-confirmed HubSpot behavior:** an empty-string property value satisfies `NOT_HAS_PROPERTY` — HubSpot treats empty as absent — so a partially-written contact re-enters a `NOT_HAS_PROPERTY` batch rather than stranding. Whether a returned contact is the *right* one to act on, and whether a null property should have carried a value, are Tier 2 concerns. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `found` present and boolean; `match_count` present and a number; `total` present and a number; `contacts` present and an array; `captain_source` present, string, equal to "hubspot_contact_search"; `invoked_by` present and string. Structural facts only.

`contacts` is an **always-present array with no non-empty requirement** — a legitimate zero-result search must pass Tier 1, not fail it. This mirrors the confirmed `web_search` lesson, forcing non-emptiness manufactures a false failure on a correct run.

**Tier 2 (Meridian / Colonel / HANK):** whether the filter asked the right question; whether `total` greatly exceeding `limit` means the caller is under-paging; whether a null property on a returned contact should have carried a value; whether a returned batch is the intended population to act on. All judgment — the validator holds no opinion here.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "hubspot_contact_search",
  "required": ["found", "match_count", "total", "contacts", "captain_source", "invoked_by"],
  "types": {
    "found": "boolean",
    "match_count": "number",
    "total": "number",
    "contacts": "array",
    "filter_property": "string",
    "filter_operator": "string",
    "captain_source": "string",
    "invoked_by": "string"
  },
  "constants": {
    "captain_source": "hubspot_contact_search"
  },
  "conditional": []
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` — live-confirmed.

Confirmed against a live invocation: filter `ai_os_enrichment_status EQ "Skipped"`, `limit: 10` -> `found: true`, `match_count: 6`, `total: 6`, six populated contact records. `validator.py` verdict `pass`, zero deltas. Capitalized enum value `"Skipped"` matched exactly — case is settled against ground truth, not assumed.

**Fold-back applied same-day (v1.0 -> v1.1).** The confirming run also surfaced the exhausted-set cursor defect now covered by the Offset normalization rule in Constraints. v1.0 passed Tier 1 only because `offset` is deliberately absent from the Validation Schema — the validator held no opinion on it, and the defect was caught at Tier 2 by Meridian, not by code. That division is the two-tier model behaving correctly, and it is the reason `offset` stays out of the schema: its correctness is a semantic question about termination, not a structural one about presence. v1.1 re-validated `pass` after the edit.
