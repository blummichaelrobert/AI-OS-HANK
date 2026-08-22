# CONFIG -> Search and Replace (this)these:
The Prompter = [the_prompter]
Prompter Timezone = [prompter_timezone]

---
# File Location Reference:
"ROOT/meridian_memory.md"
"ROOT/theater-ops/captain_reference.md"

---
# SYNTAX KEY
*One symbol, one definition — the shared notation every core file is read through.*

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

## Confirmed Patterns — Live Tested

ISODt | rss_reader Captain | Content Intel | 2026-06-11 | smestrategy.net RSS feed returns dates in clean ISO 8601 format. Colonel Content Intel can depend on clean ISO 8601 dates from this feed without normalization. | Live test DW010 | [C]

YtTx | youtube_transcript Captain | ad-hoc %compose | 2026-08-03 | v1.0 schema (extracted / video_url / video_title / transcript_raw / failure_reason / captain_source / invoked_by) holds against live YouTube — clean end-to-end extraction, both tiers pass. Dual-variant selector path confirmed live: legacy panel `engagement-panel-searchable-transcript` / `ytd-transcript-segment-renderer` / `.segment-text` (also modern `PAmodern_transcript_view` / `transcript-segment-view-model` on prior runs). Scope to EXPANDED panel to avoid double-count; retry-safe (toggle re-click collapses panel); async poll — empty-but-loading != no transcript. | Live test, %compose invocation | [C]
