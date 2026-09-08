# Shared Captain Library — Capability Catalog
*Canonical capability lookup for every shared, domain-agnostic Captain — what each one does, its runtime, inputs, and outputs.*
*SPOKE of "theater-ops/captain_reference.md".*
*Not a domain arm — this is the DEFAULT placement every Captain starts in. It holds Captains only; a Colonel is domain-bound by definition and can never live here.*

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/manifest.md" | Look up index for entire project |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. This file is its SPOKE. |
| "ROOT/theater-ops/_shared-captain-library/shared_meridian_memory.md" | Pattern SPOKE for this folder — loaded whenever a unit here is evaluated. |
| "ROOT/theater-ops/_standards/captain_function_contract.md" | Captain spec standard (Tier 1) — every unit below is authored against it. |
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/validator.py" | Tier 1 deterministic validator (Validation Schema checker). |
| "ROOT/affirmative_detection.md" | Affirmative Detection — where each unit below ticks at its gate. |

**Unit specs catalogued in this file:** `web_search.md` · `web_fetch.md` · `web_parse.md` · `web_export.md` · `rss_reader.md` · `youtube_transcript.md` · `navigate_and_confirm.md` · `submit_and_await.md` · `download_asset.md` — all resident in this folder. **Retired predecessors of `rss_reader`, `youtube_transcript` and `web_search` live in "staging-area/archived-captains/" as `v1_*.md`** — archived, not catalogued; a `v1_` file is never invoked, "ROOT/theater-ops/_shared-captain-library/".

---
## Scope
- **In scope:** domain-agnostic capability — retrieval and extraction that depends on no single domain's data or context (web search, fetch, rendered-page scrape, RSS, transcript).
- **Out of scope:** any Captain that depends on a specific domain's data — those move to that domain's arm per the Placement test in "captain_reference.md". Colonels, always and without exception.
- **Substrate today:** Rung 1 prose (`web_parse` — no external dependency at all), Rung 2 CoWork-native tooling (`web_search` for discovery, `web_export` for the write), and Rung 4 browser work. **Rung 4 is split by AUTHENTICATION, not capability** ("pi.md", Captain Substrate Selection): 4a = CoWork native browser, the DEFAULT for anonymous page work; 4b = Claude in Chrome, only where a sign-in wall is the demonstrated reason. `rendered_auth` (4b) is now reachable only as a declared `web_fetch` input, on named sign-in-wall evidence. `web_fetch` declares its rung per invocation as an input. No Rung 3 connector is required by any unit here.
- **The Two chains that live here DO NOT mix.** The RETRIEVAL chain (`web_fetch` -> `web_parse` -> `web_export`) is stateless and anonymous-first: each unit takes a URL or text and returns a record. The INTERACTIVE chain (`navigate_and_confirm` -> `submit_and_await` -> `download_asset`) is **stateful and authenticated**: the first unit creates a live tab handle and the other two operate only on that handle, strictly serially, and all three stand on 4b because their targets sit behind a sign-in wall. A caller reaching for a browser should take the retrieval chain unless it must *act on* a page rather than read it.
- **ATTENDED, without exception:** the interactive chain drives [the_prompter]'s live signed-in browser. Two of its known defects are observation-window failures, so an unattended run would report clean and ship nothing. **This chain never runs unattended.**
- **Read-only, with one exception:** every unit here retrieves or transforms except `web_export`, which WRITES. Its blast radius is bounded in its schema rather than by a per-run gate — one constant destination, never an overwrite, never a read-back (`CntnNotPrm`, Containment Is Cheaper Than Permission).

---
## Active Captain Registry — Shared
*Presence here MEANS shared, by construction — that is why there is no Domain column.*

| Captain | Runtime | Purpose | Inputs | Outputs | Status |
|---|---|---|---|---|---|
| `youtube_transcript` | **CoWork native browser (Rung 4a)** [Anthropic Ecosystem Exclusive] | FETCH stage, transcript variant. Open the transcript panel on one video watch page and return its text verbatim with the video's title. Anonymous — the panel is served signed-out, so no wall exists and no climb to 4b is warranted | `video_url` / `invoked_by` | `extracted` / `video_title` / `transcript_raw` / `segment_count` (or `failure_reason`) | [C] v0.2 — 4/4 gates reconciled, 68 segments verbatim, honest failure on a video with no transcript control |
| `web_search` | CoWork native WebSearch (Rung 2) [Anthropic Ecosystem Exclusive] | DISCOVER stage — the step BEFORE Fetch. Turn a query into candidate URLs. Returns `title` + `url` ONLY; it never fetches a result, so it carries no snippet or description | `query` / `date_range` (optional) / `invoked_by` | `searched` / `result_count` / `results[]` (or `failure_reason`) | [C] v0.2 — 8/8 gates reconciled, 6/6 adversarial `output_failed`; runtime confirmed it emits title+url only |
| `web_fetch` | **MULTI-SUBSTRATE, caller-declared** [Anthropic Ecosystem Exclusive] — `rendered_anon` = CoWork native browser (4a) · `rendered_auth` = Claude in Chrome (4b) | FETCH stage. Retrieve the visible text of one URL at a caller-declared rung and report whether it worked. A thin page, a shell, and a sign-in wall are all successful fetches — judging them is Tier 2 | `url` / `substrate` / `invoked_by` | `fetched` / `page_text` / `content_length` / `extraction_scope` / `substrate_used` / `captain_source` (or `failure_reason`) | [C] v0.1 — 5/5 gates reconciled, re-confirmed after rename |
| `rss_reader` | **CoWork native browser (Rung 4a)** [Anthropic Ecosystem Exclusive] | FETCH stage, feed variant. Retrieve one RSS/Atom feed and return its items as structured records — no feed selection, no ranking, that is Colonel-layer | `feed_url` / `max_items` / `source_name` / `recency_filter` (optional) / `invoked_by` | `item_count` / `items[]` / `source_name` (or `error`) | [C] v0.2 — 4/4 gates reconciled, feed returned as raw XML verbatim (25 items) |
| `web_parse` | **Prose — no external dependency (rung 1)** | PARSE stage. Segment plain text into ordered, verbatim blocks and return them as a mission-agnostic JSON map. Names no block's KIND — that is a claim about meaning and belongs to Tier 2 | `page_text` / `source_ref` / `invoked_by` | `parsed` / `structure_map` (`blocks[]`, `tables[]`, `links[]`) / `node_count` / `input_length` / `captain_source` (or `failure_reason`) | [C] v0.2 — 9/9 gates reconciled, byte-verbatim proof, mission-agnosticism proven |
| `web_export` | **CoWork-native file tools (rung 2)** [Anthropic -> Google Exclusive] | EXPORT stage. Serialize a payload to JSON, CSV or Markdown and write it as a NEW file in "ROOT/cos-output/", reporting the name it landed under. Forms no opinion about the payload — an unwanted export is a Colonel defect, never a Captain failure | `payload` / `file_base` / `format` / `invoked_by` | `exported` / `file_name` / `bytes_written` / `output_folder` / `captain_source` (or `failure_reason`) | [C] v0.1 — 11/11 gates reconciled, 6/6 adversarial `output_failed`, suffix increment + read-back fidelity proven |
| `navigate_and_confirm` | **Claude in Chrome (Rung 4b)** [Anthropic Ecosystem Exclusive] — ATTENDED | ARRIVE stage of the interactive chain, and its only unit that CREATES state. Open one URL in a new tab, probe the landed page for an expected string, and hand over the tab handle | `url` / `expect_text` / `invoked_by` | `arrived` / `expect_text_found` / `tab_id` / `page_title` / `url_landed` (or `error`) | [C] v0.1 — 3/3 gates reconciled; after-paint probe rule held live |
| `submit_and_await` | **Claude in Chrome (Rung 4b)** [Anthropic Ecosystem Exclusive] — ATTENDED | SUBMIT stage. Enter a prompt on a handed tab, submit, and wait for the render to finish or the budget to expire. Names no target app — app-specific knowledge lives in the commanding Colonel | `tab_id` / `prompt_text` / `completion_signal` / `max_wait_seconds` / `invoked_by` | `prompt_submitted` / `prompt_text_echo` / `response_complete` / `wait_elapsed_seconds` / `asset_count` / `candidates[]` (or `error`) | [C] v0.1 — 3/3 gates reconciled; many-match shape exercised on the first run (2 assets) |
| `download_asset` | **Claude in Chrome (Rung 4b)** [Anthropic Ecosystem Exclusive] — ATTENDED | RETRIEVE stage. Actuate the download control for one named asset on a handed tab and report what it could observe. **The library's canonical observability boundary** — `download_confirmed`, `file_name`, `landing_path` and `file_type` are observe-and-report-if-visible, never required | `tab_id` / `asset_description` / `invoked_by` | `download_triggered` / `download_confirmed` / `file_name` / `landing_path` / `file_type` (or `error`) | [C] v0.1 — 3/3 gates reconciled; passed with every observable field null |

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
---