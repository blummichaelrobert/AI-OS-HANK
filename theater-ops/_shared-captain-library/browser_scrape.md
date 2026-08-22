# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** browser_scrape
**Version:** 3.1
**Runtime:** Claude in Chrome MCP [Anthropic -> Google Exclusive]

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Fetch full rendered text content from a live web page via Claude in Chrome. Rung 4 on the Captain Substrate Selection ladder — the last-resort escalation tier for JavaScript-rendered pages, SPAs, gated dashboards, and any URL that returned empty or insufficient content via `web_fetch`. Returns raw page text for the Colonel to process. |
| Inputs | `source_url` (string, required) — the full URL to scrape. |
| Outputs | `source_url` (string) — the URL passed in. `page_text` (string) — full visible text content extracted from the rendered page. `page_char_count` (number, v3.1) — character length of `page_text`. Emitted on success. Not a quality score; a coverage signal that makes thin extraction visible instead of asserted. `extraction_scope` (string, v3.1) — what the extractor actually scoped to, reported verbatim from the runtime (e.g. "article", "body", "full_page"). A scope narrower than the page is the single most common cause of a thin success. `extraction_status` (string) — "success" or "failed". `failure_reason` (string) — populated only on failure, describing the specific failure point. `captain_source` (string) — always "browser_scrape". |
| Error Behavior | If the page does not load or returns no meaningful content: `extraction_status: "failed"`, `failure_reason` populated with the specific point (e.g. "page timed out", "login wall detected", "no readable content found"). Never return empty `page_text` as `extraction_status: "success"`. Surface to Colonel on failure — no silent empty returns. If Chrome MCP is unavailable: halt immediately and surface to Colonel. Do not attempt `web_fetch` as a fallback from inside this Captain — it is already the escalation tier, not a relay. |
| Constraints | Requires Claude in Chrome MCP connected — no fallback substrate. Operates on the single URL passed in — does not follow links, navigate to related pages, or expand scope. Does not log in, bypass authentication walls, or interact with any page element beyond passive content extraction. Does not submit forms or click interactive elements. Returns raw page text only — summarization belongs to the Colonel. **Escalation-only:** this Captain is invoked only after a cheaper substrate (`web_fetch`) has already been tried and judged insufficient by the Colonel — never the first call for a URL. **"Insufficient" is defined on THREE axes** A rung-2 return is insufficient if ANY of the following holds: (a) EMPTY or THIN — little or no readable content; (b) NOT CURRENT — the content is well-formed and abundant but does not reflect the page as it stands now; (c) NOT COVERING — the content is current but omits the region the mission needs. Axis (b) is the one that costs you: Judge by what the mission needs, never by response size. Cheap-tier abundance is not evidence of freshness. **Never a workaround:** if a domain or fetch is refused or restricted, that refusal stands — this Captain does not get invoked to route around it. Expensive relative to `web_fetch`; invocation should be deliberate, not default. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `source_url` present and a string; `extraction_status` present and a string; `captain_source` present, string, equal to "browser_scrape"; when `extraction_status: "failed"`, `failure_reason` non-null; when `extraction_status: "success"`, `page_text`, `page_char_count`, and `extraction_scope` all non-null (v3.1). Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** whether the Colonel was right to escalate to this tier at all; whether extracted `page_text` actually contains what was needed; whether a "success" with thin content should be treated as effectively a failure. All judgment — the validator holds no opinion here.

**Where the v3.1 fields do and do not help — read this before trusting them.** `page_char_count` and `extraction_scope` are REPORTING fields, not thresholds. Tier 1 checks that they are present and non-null; it does not and must not judge whether characters is enough, because "enough" is a property of the mission, not of the record. A `page_char_count` of 0 is non-null and passes Tier 1. What the fields buy is VISIBILITY.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "browser_scrape",
  "required": ["source_url", "extraction_status", "captain_source", "invoked_by"],
  "types": {
    "source_url": "string",
    "page_text": "string",
    "page_char_count": "number",
    "extraction_scope": "string",
    "extraction_status": "string",
    "failure_reason": "string",
    "captain_source": "string",
    "invoked_by": "string"
  },
  "constants": {
    "captain_source": "browser_scrape"
  },
  "conditional": [
    { "when": {"extraction_status": "failed"}, "require_non_null": ["failure_reason"] },
    { "when": {"extraction_status": "success"}, "require_non_null": ["page_text", "page_char_count", "extraction_scope"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` live-confirmed. `extraction_status: "success"`, `page_char_count: 5470` matching `len(page_text)`, `extraction_scope: "main"` reported verbatim from the runtime, widened success conditional satisfied, validator.py verdict `pass`, zero deltas.
