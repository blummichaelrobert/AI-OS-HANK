# Captain Function Contract
**Captain Name:** hubspot_contact_lookup
**Version:** 3.0
**Runtime:** HubSpot MCP

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Find a contact in HubSpot CRM from whatever identifier the human has — a name or an email — and return every matching contact record. |
| Inputs | `identifier` (string, required) — a name (e.g. "Wes-Schaeffer") or an email (e.g. "wes@example.com"). The Captain uses HubSpot search, which resolves either. HANK/Colonel arm the Captain with the best identifier available. |
| Outputs | `found` (boolean) — true if one or more contacts matched. `match_count` (number) — how many contacts matched (0, 1, or many). `captain_source` (string) — always "hubspot_contact_lookup". `identifier` (string) — the query echoed back. When `found: true`: `candidates` (array) — one object per match, each with `contact_id`, `firstname`, `lastname`, `email`, `company`, `jobtitle`, `phone`, `city` (any profile field may be null). When `found: false`: `{ "found": false, "match_count": 0, "identifier": "<query>", "captain_source": "hubspot_contact_lookup" }`. |
| Error Behavior | On MCP failure returns `{ "found": false, "match_count": 0, "identifier": "<query>", "error": "<reason>", "captain_source": "hubspot_contact_lookup" }`. The Colonel must not proceed on error — surface to HANK. |
| Constraints | The Captain **retrieves**; it does **not disambiguate**. When `match_count > 1`, the Captain returns all candidates and the judgment layer (Colonel / Meridian / HANK) chooses the intended contact or escalates. The Captain never guesses which match is "the right one." Profile-field nullness is a Tier 2 concern, not a validator concern. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `found` present and boolean; `match_count` present and a number; `captain_source` present, string, equal to "hubspot_contact_lookup"; and when `found: true`, `candidates` present and non-null. Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** which candidate is the intended contact when `match_count > 1`; whether a null profile field should have carried a value; whether the identifier the human gave was specific enough. All judgment — the validator holds no opinion here.

---

## Validation Schema (machine register)

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

---

## Confirmation Discipline
`Status: [C]` — live-confirmed
