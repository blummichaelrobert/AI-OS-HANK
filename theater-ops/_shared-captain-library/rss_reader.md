# Captain Function Contract
**AI OS Apps or Software — V3 Standard**
**Captain Name:** rss_reader
**Version:** 3.1
**Runtime:** Claude in Chrome (`navigate` + `get_page_text`) — primary. CoWork native WebFetch attempted first as a cheap probe, but confirmed unreliable for RSS/XML content-types (see Constraints, `WbFtchBin` in meridian_memory.md).

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Fetch a single RSS/Atom feed URL and return a structured list of recent items. Raw retrieval and parse only — no summarization, no filtering, no editorial judgment. That belongs to the Colonel commanding this Captain. |
| Inputs | `feed_url` (string, required) — a direct RSS/Atom feed endpoint, not a webpage. Source selection (which feed, why) is entirely the Colonel's responsibility — this Captain has no opinion on where the URL came from. `max_items` (integer, optional, default 10, max 25 — capped silently, never errors). `source_name` (string, optional, default derived from feed domain) — human-readable label used in output tagging. `recency_filter` (string, optional, default null) — ISO 8601 date; excludes items with an older `published_date`. Items with `published_date: null` are always included. |
| Outputs | `feed_url` (string) — the URL fetched. `source_name` (string) — label passed in or derived from domain. `item_count` (number) — count of items returned. `items` (array) — always present, may be empty; each item contains `title` (string, verbatim, no paraphrasing), `url` (string), `summary` (string, verbatim feed description, null if absent), `published_date` (string, ISO 8601 verbatim from feed, null if absent). `captain_source` (string) — always "rss_reader". |
| Error Behavior | Feed URL unreachable (via WebFetch or Chrome navigate): `{ "feed_url": "<url>", "item_count": 0, "items": [], "captain_source": "rss_reader", "error": "fetch_failed" }`. Do not retry. URL fetched (by either substrate) but not valid RSS/Atom XML — including WebFetch's own `"[binary data]"` response, or a Chrome `get_page_text` result that is empty, non-XML, or an error page: `{ "feed_url": "<url>", "item_count": 0, "items": [], "captain_source": "rss_reader", "error": "parse_failed" }`. Do not attempt to extract content from HTML on a parse failure. Field missing in a feed item: set that field `null` — never infer or fabricate. Surface all errors to the Colonel; Colonel owns any fallback (e.g. to `web_search`). |
| Constraints | Runtime, in order: (1) CoWork native `WebFetch` — cheap, Rung 2, attempt first; confirmed unreliable for this Captain's own content-type (RSS/Atom is XML, and WebFetch returns literal `"[binary data]"` for any non-text/html content-type — a WebFetch tool limitation, not a gzip or source-content problem, per `WbFtchBin`). (2) Claude in Chrome, `navigate` + `get_page_text` — Rung 4, attended. This Captain currently runs at a higher-cost, attended tier than its original Rung 2-only design; Rung 3 (an MCP with raw fetch) was searched for and does not currently exist in the connector registry. Revisit substrate if either a suitable MCP appears or the CoWork Python sandbox's network restriction (`SbxNoNet` in meridian_memory.md) is lifted. Fetches one feed URL per invocation; batching across feeds is the Colonel's responsibility. Returns raw feed data only — no summarization, scoring, filtering, or ranking. `published_date` is taken verbatim from the feed; no date normalization unless the feed provides ISO 8601 natively — most feeds do not (e.g. RFC 822 `pubDate`), and that is not itself an error. `recency_filter` comparison is string-based ISO 8601 only, applied after fetch — no date parsing; if `published_date` is not ISO 8601, the item is included rather than excluded on ambiguity. This Captain does not source, whitelist, or validate feed URLs — that intelligence lives with the Colonel commanding it, never hardcoded here. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `feed_url` present and a string; `item_count` present and a number; `items` present and an array; `captain_source` present, string, equal to "rss_reader". Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** whether a feed was the right one to select (whitelist/sourcing judgment, entirely Colonel-side); whether a null `summary` or `published_date` should have carried a value; whether zero items warrants trying a different feed. All judgment — the validator holds no opinion here.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "rss_reader",
  "required": ["feed_url", "item_count", "items", "captain_source", "invoked_by"],
  "types": {
    "feed_url": "string",
    "source_name": "string",
    "item_count": "number",
    "items": "array",
    "captain_source": "string",
    "invoked_by": "string",
    "error": "string"
  },
  "constants": {
    "captain_source": "rss_reader"
  },
  "conditional": []
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` — live-confirmed. Feed `https://www.forbes.com/small-business-strategy/feed/` returned no parseable RSS/Atom content via CoWork WebFetch; Captain correctly classified as `error: "parse_failed"` with `item_count: 0`, `items: []`. `feed_url`/`item_count`/`items`/`captain_source`/`invoked_by` all present and correctly typed, `captain_source` constant matched, `validator.py` verdict `pass`, zero deltas. This confirmed the failure-path output shape.

Success path confirmed. Feed `https://www.uschamber.com/co/feeds/rss` — WebFetch returned `"[binary data]"` (per `WbFtchBin`); Claude in Chrome `navigate` + `get_page_text` returned the full, well-formed feed as plain text. 25 items extracted with real `title`/`url`/`summary`/`published_date`, `item_count` matched `len(items)`, `captain_source` constant matched, `validator.py` verdict `pass`, zero deltas. Both failure-path and success-path output shapes are now live-confirmed. Runtime substrate updated to Chrome-primary accordingly (see header, Constraints).
