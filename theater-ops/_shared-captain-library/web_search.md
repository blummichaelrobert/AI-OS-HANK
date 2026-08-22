# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** web_search
**Version:** 3.0
**Runtime:** CoWork native WebSearch [Anthropic Ecosystem Exclusive]

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Query the open web and return structured search results for a given query string. |
| Inputs | `query` (string, required) — the search query. `date_range` (enum, optional, default: Any) — one of: Any / Past Hour / Past 24 Hours / Past Week / Past Month / Past Year. |
| Outputs | `result_count` (number) — how many results were returned (0 or more). `results` (array) — always present, may be empty; each item contains `title` (string), `description` (string), `url` (string). `captain_source` (string) — always "web_search". |
| Error Behavior | On failure returns `{ "result_count": 0, "results": [], "error": "<reason>", "captain_source": "web_search" }`. The Colonel must not proceed on error — surface to HANK. |
| Constraints | Meridian enforces: `url` present and non-empty on every item in `results`. A zero-length `results` array with no `error` is a valid, passing outcome — a genuine no-match search, not a failure. Fabricated or unverifiable sources are a Tier 2 concern (Meridian's judgment), not a schema-level guarantee. Colonel declares `date_range` in the battle plan — not hardcoded in this Captain. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `result_count` present and a number; `results` present and an array; `captain_source` present, string, equal to "web_search". Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** whether returned results are actually relevant to the query; whether a source is genuine and not fabricated; whether zero results warrants a broader retry. All judgment — the validator holds no opinion here.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "web_search",
  "required": ["result_count", "results", "captain_source", "invoked_by"],
  "types": {
    "result_count": "number",
    "results": "array",
    "captain_source": "string",
    "invoked_by": "string",
    "error": "string"
  },
  "constants": {
    "captain_source": "web_search"
  },
  "conditional": []
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [O]` -> `Status: [C]` — live-confirmed. Query "is there any relation between the golden ratio and the pauli exclusion principal?" — 8 results, `result_count`/`results`/`captain_source`/`invoked_by` all present and correctly typed, `captain_source` constant matched, `validator.py` verdict `pass`, zero deltas.
