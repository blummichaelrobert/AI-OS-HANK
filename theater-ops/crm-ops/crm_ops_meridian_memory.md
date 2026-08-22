# CONFIG -> *Searched and Replaced Properties:*
The Prompter = [the_prompter]
Prompter Timezone = [prompter_timezone]

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |

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

# CRM Ops — Meridian Pattern Memory (SPOKE)
*Author: (me)Meridian — Universal QA Agent, "AI OS"*
*One of (my)Meridian's write surfaces. Machine-readable QA pattern library.*

**This file is a SPOKE of "ROOT/meridian_memory.md".** It carries patterns local to the units living in "ROOT/theater-ops/crm-ops/" — the AI OS's first domain arm — and nothing else.

**Read scope.** Loaded only when the unit under evaluation is a CRM Ops Captain or Colonel, and always alongside the hub. Never read in place of the hub — CORE patterns bind every run, including this one. Loaded in full during any `%REM` sweep.

**Domain, not tool.** The arm is named for the domain of WORK. HubSpot is the substrate under today's units, not the boundary of this file — a future Salesforce or Pipedrive Captain's patterns land here without renaming anything (`DIP`, Dependency Inversion).

**Authority.** Same as the hub: (I)Meridian write here; (I)Meridian never rewrite the Captain or Colonel spec a pattern is about. Fold-backs surface to HANK behind [the_prompter]'s reviewed `%shipit` (audit independence).

**Placement.** Entries arrive here by rule 2 of the PATTERN PLACEMENT RULE in the hub. A pattern that names no unit, names a Command Triad persona, or states a system-wide law belongs in the hub — not here. One entry, one home.

---
# SCHEMA
*Identical to the hub. One schema, one library, three files.*

Single-line entry format:
`[TAG] | [Colonel/Captain] | [Pipeline] | [Date] | [Rule violated] | [Source] | [STATUS]`

Field glossary and RESOLVED STATUS RULES: → "ROOT/meridian_memory.md". Not duplicated here — one definition, one home.

**No `%REM SWEEP LOG` in this file.** Sweep state is global and lives in the hub only.

---
# PATTERN LIBRARY — CRM OPS
*Every entry is a rule that runs against future Colonel and Captain output, written on a halt and kept for as long as it can still catch something, never a record of what a past run did — a unit's confirmation is current status in that unit's own spec, and no history is kept anywhere.*

## Confirmed Patterns — Live Tested

HsCrt | hubspot_contact_create Captain | Outbound Sales | 2026-06-11 | Two-call pattern is structural: Step 1 = contact CREATE, Step 2 = note CREATE (conditional on Step 1 success + note_body present). `targetObjectType: "contacts"` is case-sensitive and MCP-specific. `notes_last_contacted` is read-only — cannot be set on CREATE. `description` property does not exist on contacts in this HubSpot instance. | Live test `%compose` colonel | [C]

HsUpdEnum | hubspot_contact_update Captain | CRM Ops | 2026-08-12 | v1.1 Pipeline-State Exception confirmed — `ai_os_enrichment_status` (enumeration) written as `Processed`, independently re-read via get_crm_objects, value stored verbatim and correctly cased; validator.py verdict `pass`, zero deltas. Update response again returned empty `properties: {}` — known pattern, do not read it as failure, always re-read independently. [C] was RETAINED not revoked across this edit: the Validation Schema was unchanged (no output field added or retyped), and Tier 1 never checked inputs in the first place — so the confirmed artifact stayed confirmed and only the new input path needed earning. Standing risk this Captain now carries: case is load-bearing (`Processed`/`Skipped`/`Error`) and un-checkable at Tier 1 — a mis-cased value passes the validator, is rejected portal-side, and surfaces as `error`, which a Colonel conflating "tool failed" with tri-state `Error` would retry forever. Colonel-layer Rule of Engagement required: transient failure and terminal not-found must be distinguished BEFORE the status write, never inferred from it. | Live test, validator.py run against hubspot_contact_update.md | [C]
