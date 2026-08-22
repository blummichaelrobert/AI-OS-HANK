# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** web_fetch
**Version:** 3.0
**Runtime:** CoWork native WebFetch [Anthropic Ecosystem Exclusive]

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Fetch a single URL via CoWork-native WebFetch and return its raw text content. Rung 2 on the Captain Substrate Selection ladder — the cheap, first-tier retrieval attempt before any browser-driven escalation. Does not execute JavaScript. |
| Inputs | `url` (string, required) — the full URL to fetch. |
| Outputs | `url` (string) — the URL passed in. `page_text` (string) — raw text content returned by the fetch; may be thin or near-empty on a client-rendered page, that is a legitimate outcome, not a failure. `content_length` (number) — character length of `page_text`, a structural signal the Colonel can use to judge whether the fetch was sufficient or whether escalation to `browser_scrape` is warranted. `captain_source` (string) — always "web_fetch". |
| Error Behavior | URL unreachable or fetch tool errors: `{ "url": "<url>", "page_text": "", "content_length": 0, "captain_source": "web_fetch", "error": "fetch_failed" }`. Do not retry. Surface to Colonel — do not silently escalate to another substrate from inside this Captain. |
| Constraints | Runtime: CoWork native WebFetch only — no JavaScript execution, so client-rendered pages (SPAs, JS-gated content) will return thin or shell-like `page_text` rather than an error; this is expected, structural behavior, not a bug. Fetches one URL per invocation. Returns raw text only — no summarization, no parsing into structured fields. Whether `page_text` is sufficient, or whether the Colonel should escalate to `browser_scrape` (Rung 4), is a Tier 2 judgment call this Captain does not make — it only supplies the structural signal (`content_length`). Never used as, or expected to bypass, an access-restricted or blocked domain — a refusal at this tier is a refusal, not a trigger to route around it. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `url` present and a string; `page_text` present and a string; `content_length` present and a number; `captain_source` present, string, equal to "web_fetch". Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** whether `page_text` actually contains what the Colonel needed; whether a short `content_length` means the page is client-rendered and escalation to `browser_scrape` is warranted, or the page is just genuinely short. All judgment — the validator holds no opinion here.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "web_fetch",
  "required": ["url", "page_text", "content_length", "captain_source", "invoked_by"],
  "types": {
    "url": "string",
    "page_text": "string",
    "content_length": "number",
    "captain_source": "string",
    "invoked_by": "string",
    "error": "string"
  },
  "constants": {
    "captain_source": "web_fetch"
  },
  "conditional": []
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` — live-confirmed, chars returned, `content_length` matched `len(page_text)` exactly, `captain_source` constant matched, validator.py verdict `pass`, zero deltas, `%compose` invocation.

**Two live findings the Colonel calling this Captain must hold:**
```
1. content_length is a COST signal, not a quality signal. A large return
   is not evidence of a current page. On usnews.com this
   Captain returned a full, well-formed homepage roughly NINE YEARS
   stale. Judge currency from first-party evidence inside the payload —
   a build tag, a dateline, a copyright year — never from size.
2. A small content_length does NOT automatically mean "escalate."
   Because Chrome scoped to <main> and dropped nav, footer,
   social and contact routes. The ladder ranks COST, not coverage.
   -> "meridian_memory.md" (hub): SuffNotVol
```
