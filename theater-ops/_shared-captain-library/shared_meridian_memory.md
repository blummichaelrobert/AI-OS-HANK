# CONFIG -> *Searched and Replaced Properties:*
The Prompter = [the_prompter]
Prompter Timezone = [prompter_timezone]

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. |

---
# SYNTAX KEY
*This file's subset of the shared notation every core file is read through.*

| Token | Meaning |
|---|---|
| `>>` | Command Intent — represents *will(authority)* moving down the chain, agent addressing (`HANK >> do X`) and standing imperatives. Human Register. |
| `()` | Grouping — membership in a set. No hierarchy, no sequence implied. |
| `%` | Command prefix — the delegation trigger. [the_prompter] issues a `%` command; the CNS carries it out. |
| `\|` | Field separator (within single-line entries and tables). |
| `[F]` | Status — Final / Resolved. |
| `[O]` | Status — Open / Unresolved. |
| `[R]` | Status — Retained for semantic reinforcement; not prunable by (me)Meridian. |
| `[C]` | Status — Confirmed via live test (with explicit `%shipit`). |
| `[TAG]` | Vowel-compressed entry key naming a memory or pattern entry — `TknEff`(Token Efficiency). Length follows legibility, not a fixed count; identifiers (acronyms, filenames, version tokens) are exempt from compression. Also the leading field placeholder in single-line record formats. |
| `→` | "Go read this" — pointer to a session reference or a "cos_memory.md" entry. Navigation, Human Register. |
| `->` | Directional Flow — represents *data* moving through a pipeline, gate notation and the isomorphism event chain. Output of the left feeds input of the right. Machine Register. |

---

# Shared Captain Library — Meridian Pattern Memory (SPOKE)
*Author: (me)Meridian — Universal QA Agent, "AI OS"*
*One of (my)Meridian's write surfaces. Machine-readable QA pattern library.*

**This file is a SPOKE of "ROOT/meridian_memory.md".** It carries patterns local to the shared, domain-agnostic Captains living in "ROOT/theater-ops/_shared-captain-library/" — and nothing else.

**Read scope.** Loaded only when the unit under evaluation is a shared-library Captain, and always alongside the hub. Never read in place of the hub — CORE patterns bind every run, including this one. Loaded in full during any `%REM` sweep.

**Authority.** Same as the hub: (I)Meridian write here; (I)Meridian never rewrite the Captain spec a pattern is about. Fold-backs surface to HANK behind [the_prompter]'s reviewed `%shipit` (audit independence).

**Placement.** Entries arrive here by rule 2 of the PATTERN PLACEMENT RULE in the hub. A pattern that names no unit, names a Command Triad persona, or states a system-wide law belongs in the hub — not here. One entry, one home.

Every entry below was relocated from the flat hub library, verbatim; none were authored fresh.

---
# SCHEMA
*Identical to the hub. One schema, one library, three files.*

Single-line entry format:
`[TAG] | [Colonel/Captain] | [Pipeline] | [Date] | [Rule violated] | [Source] | [STATUS]`

Field glossary and RESOLVED STATUS RULES: → "ROOT/meridian_memory.md". Not duplicated here — one definition, one home.

**No `%REM SWEEP LOG` in this file.** Sweep state is global and lives in the hub only.

---
# PATTERN LIBRARY — SHARED CAPTAIN LIBRARY
*Every entry is a rule that runs against future Colonel and Captain output, written on a halt and kept for as long as it can still catch something, never a record of what a past run did — a unit's confirmation is current status in that unit's own spec, and no history is kept anywhere.*

## LIVE TESTED OPERATIONAL THEATER MEMORIES

ISODt | rss_reader Captain | Content Intel | 2026-06-11 | smestrategy.net RSS feed returns dates in clean ISO 8601 format. Colonel Content Intel can depend on clean ISO 8601 dates from this feed without normalization. | Live test DW010 | [C]

YtTx | youtube_transcript Captain | ad-hoc %compose | 2026-08-03 | v1.0 schema (extracted / video_url / video_title / transcript_raw / failure_reason / captain_source / invoked_by) holds against live YouTube — clean end-to-end extraction, both tiers pass. Dual-variant selector path confirmed live: legacy panel `engagement-panel-searchable-transcript` / `ytd-transcript-segment-renderer` / `.segment-text` (also modern `PAmodern_transcript_view` / `transcript-segment-view-model` on prior runs). Scope to EXPANDED panel to avoid double-count; retry-safe (toggle re-click collapses panel); async poll — empty-but-loading != no transcript. | Live test, %compose invocation | [C]

WpNoGate | web_parse Captain | ad-hoc %compose | 2026-09-05 | This Captain CANNOT distinguish page content from a sign-in wall, a consent gate, or a paywall — a wall's text segments into clean, well-ordered blocks exactly as real content does, and the record returns `parsed: true` with no signal of any kind. Confirmed live: a login page and an article body produced structurally indistinguishable maps. THE CONSEQUENCE FOR A COMMANDING COLONEL: gating is not detectable at the PARSE stage either, so it is never inferred from a parse record — it is inferred from CONTENT ABSENCE against mission expectation, at Tier 2, by the judgment layer. A Colonel that treats `parsed: true` as evidence the page held its content will ship a wall as a result. → core: PartGate | Live test, 5 pages incl. a sign-in wall | [C]

WfThinPass | web_fetch Captain | ad-hoc %compose | 2026-09-05 | `fetched: true` is a statement about RETRIEVAL, never about SUFFICIENCY. Confirmed live: a 42-character shell page and a full article both returned `fetched: true` with a clean validator verdict, and `extraction_scope` narrowing (`article` vs `main`) is the commonest cause of a thin success — the same domain returned 47 chars at one scope and thousands at another. A commanding Colonel must read `content_length` and `extraction_scope` TOGETHER against what the mission needs, and must never treat a passing gate as evidence the page was captured. → core: SuffNotVol | Live test, 8 runs across two browser rungs | [C]

WeNoOpin | web_export Captain | ad-hoc %compose | 2026-09-06 | This Captain forms NO OPINION about what it writes — a payload it might be thought to "consider wrong" is serialized exactly as given, because judging the payload happened upstream. Every required output field is an echoed input, a pinned constant, a computed length, or the name the runtime actually wrote, so there is nothing observed for reality to contradict and nothing for the unit to have judged badly. THE CONSEQUENCE FOR A COMMANDING COLONEL: **an unwanted export is ALWAYS a Colonel defect, never a Captain failure** — do not read `exported: true` as evidence the export was warranted, and do not look for a Captain-side check that would have caught it, because none exists or can. Whether this payload should have been written, in this format, under this name, is Tier 2 and lives entirely with the caller. → core: CntnNotPrm | Live test, 11 reconciled gates across three formats | [C]

ExtNoWork | web_parse / web_fetch Captains | browser_scrape_colonel | 2026-09-06 | **Selection in this chain happens at FETCH, via `extraction_scope` — not at a parse map.** Confirmed live end-to-end across two URLs: the only choice that changed what the mission received was which scope the page was retrieved at, and the commanding Colonel reached past any hypothetical Extract stage directly to `structure_map.blocks[]` on both runs. THE CONSEQUENCE FOR A COMMANDING COLONEL: an Extract Captain has **no demonstrated work** in this chain, and building one now would add a unit whose only job is to search blocks the Colonel already reads — `SRP`(Single Responsibility) says a unit with no decision of its own is not a unit. Build it only when a mission needs a NAMED value that no scope choice can deliver, and when it can return `candidates[]` with `match_count` and refuse to choose. Until then the honest chain is Fetch -> Parse -> Export. → core: SuffNotVol | Live end-to-end run, 2 URLs, 7 reconciled gates | [C]

---
## CURRENT OPEN FINDINGS

---
## PENDING RESOLUTION
