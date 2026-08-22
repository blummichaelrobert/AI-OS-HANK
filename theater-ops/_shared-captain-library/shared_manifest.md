# Shared Captain Library — Capability Catalog
*Canonical capability lookup for every shared, domain-agnostic Captain — what each one does, its runtime, inputs, and outputs.*
*SPOKE of "theater-ops/captain_reference.md".*
*Not a domain arm — this is the DEFAULT placement every Captain starts in. It holds Captains only; a Colonel is domain-bound by definition and can never live here.*

---
## Scope
- **In scope:** domain-agnostic capability — retrieval and extraction that depends on no single domain's data or context (web search, fetch, rendered-page scrape, RSS, transcript).
- **Out of scope:** any Captain that depends on a specific domain's data — those move to that domain's arm per the Placement test in "captain_reference.md". Colonels, always and without exception.
- **Substrate today:** CoWork-native tooling (`web_search`, `web_fetch`) and Claude in Chrome MCP (`youtube_transcript`, `browser_scrape`, `rss_reader`). Rung 2 and Rung 4 of the Captain Substrate Selection ladder; no Rung 3 connector is required by any unit here.

---
## Active Captain Registry — Shared
*Presence here MEANS shared, by construction — that is why there is no Domain column.*

| Captain | Runtime | Purpose | Inputs | Outputs | Status |
|---|---|---|---|---|---|
| `youtube_transcript` | Claude in Chrome MCP | Extract full transcript + metadata from a YouTube video page | `video_url` | `extracted` / `video_title` / `transcript_raw` (or `failure_reason`) | [C] |
| `web_search` | CoWork native WebSearch [Anthropic Ecosystem Exclusive] | Query the open web and return structured search results. Not a HANK ad hoc web search, it's for agentic workflows that need a validated, schema-checked result downstream. | `query` / `date_range` (optional) | `result_count` / `results[]` / `captain_source` (or `error`) | [C] |
| `web_fetch` | CoWork native WebFetch [Anthropic Ecosystem Exclusive] | Fetch a URL, return raw text — Rung 2, cheap first-tier retrieval. `content_length` is a COST signal, never a currency or quality signal | `url` | `page_text` / `content_length` / `captain_source` (or `error`) | [C] |
| `browser_scrape` | Claude in Chrome MCP [Anthropic -> Google Exclusive] | Fetch rendered page text via browser — Rung 4, escalation-only, never a workaround for a blocked domain. | `source_url` | `page_text` / `page_char_count` / `extraction_scope` / `extraction_status` / `captain_source` (or `failure_reason`) | [C] |
| `rss_reader` | Claude in Chrome MCP (primary, `navigate` + `get_page_text`) — CoWork native WebFetch attempted first, confirmed unreliable for this content-type | Fetch one RSS/Atom feed, return structured items — no feed selection, that's Colonel-layer | `feed_url` / `max_items` / `source_name` / `recency_filter` (all but feed_url optional) | `item_count` / `items[]` / `captain_source` (or `error`) | [C] |

---
## No Colonel Registry
*Absence is structural, not an omission.* A Colonel carries judgment ABOUT a domain, so it is domain-bound by definition and always lives in a domain arm. This library holds shared capability only. If a Colonel ever appears to belong here, the placement reasoning is wrong — not this file.

---
## Related Files
| File | Relationship |
|---|---|
| "theater-ops/captain_reference.md" | The HUB this file is a spoke of — placement law, reading order, `%compose` brief template. |
| "shared_meridian_memory.md" | Meridian's pattern-library SPOKE for these same Captains. Sits in this folder; loaded alongside the hub whenever a unit here is under evaluation. |
| Each Captain's `.md` in this folder | The Function Contract — full spec, Validation Schema, and Confirmation Discipline. This catalog says what a Captain does; the contract says exactly how. |