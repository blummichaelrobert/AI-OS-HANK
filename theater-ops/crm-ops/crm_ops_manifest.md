# CRM Ops — Arm Capability Catalog
*Canonical capability lookup for every unit that lives in this arm — Captains and Colonels both.*
*Arm: CRM Ops — customer-relationship data as a domain of work. HubSpot is the current substrate, not the arm's identity (DIP).*

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/manifest.md" | Look up index for entire project |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. This file is its SPOKE. |
| "ROOT/theater-ops/colonel_reference.md" | HUB — Colonel routing. This file is its SPOKE. |
| "ROOT/theater-ops/crm-ops/crm_ops_meridian_memory.md" | Pattern SPOKE for this arm — loaded whenever a unit here is evaluated. |
| "ROOT/theater-ops/_shared-captain-library/shared_manifest.md" | SPOKE catalog for the shared Captains this arm depends on. |
| "ROOT/theater-ops/_standards/captain_function_contract.md" | Captain spec standard (Tier 1) |
| "ROOT/theater-ops/_standards/colonel_mission_brief.md" | Mission Brief template (IFPA Layer 1) — the Colonel spec standard. |
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/validator.py" | Tier 1 deterministic validator (Validation Schema checker). |
| "ROOT/affirmative_detection.md" | Affirmative Detection — where each unit below ticks at its gate. |

**Unit specs catalogued in this file:** `enrich_hubspot_contact.md` (Colonel) · `hubspot_contact_lookup.md` · `hubspot_contact_create.md` · `hubspot_contact_update.md` · `hubspot_contact_search.md` · `hubspot_contact_note_create.md` — all resident in this folder, "ROOT/theater-ops/crm-ops/".

---

## Arm Scope
- **In scope:** retrieval, creation, update, search, and annotation of CRM contact records; judgment roles that reason over them.
- **Out of scope:** domain-agnostic retrieval (web search, fetch, browser, RSS, transcript) — those stay in "_shared-captain-library/".
- **Substrate today:** HubSpot MCP. A future Salesforce or Pipedrive Captain joins this arm without renaming it.

---

## Active Captain Registry

| Captain | Runtime | Purpose | Inputs | Outputs | Status |
|---|---|---|---|---|---|
| `hubspot_contact_lookup` | HubSpot MCP | Pull existing contact record(s) from HubSpot | contact identifier (name / email) | `found` / `match_count` / `candidates[]` (or `found: false`) | [C] |
| `hubspot_contact_create` | HubSpot MCP (`manage_crm_objects`) | Create exactly one new HubSpot contact from a name and email already confirmed not to exist by `hubspot_contact_lookup` — no dedup, no enrichment | `firstname` / `lastname` / `email` | `created` / `contact_id` / `contact_url` / `captain_source` (or `created: false` / `error` / `conflict`) | [O] |
| `hubspot_contact_update` | HubSpot MCP (`manage_crm_objects`) | Update one or more of 12 confirmed-writable string properties PLUS `ai_os_enrichment_status` (the one admitted enum — Pipeline-State Exception, v1.1) on an existing contact by `contact_id` — no note logic, no email/identity changes | `contact_id` + at least one of 13 optional properties | `updated` / `contact_id` / `contact_url` / `updated_fields` / `captain_source` (or `updated: false` / `error`) | [C], v1.1 enum path re-confirmed |
| `hubspot_contact_search` | HubSpot MCP (`search_crm_objects`) | Retrieve a page of contacts matching ONE property filter — batch retrieval, mission-agnostic, read-only. Distinct from `hubspot_contact_lookup`: that resolves one identifier to candidates for a single intended person; this filters for a population | `filter_property` / `filter_operator` (+ `filter_value`, `limit`, `properties`, `offset` optional) | `found` / `match_count` / `total` / `contacts[]` / `offset` / `captain_source` (or `error`) | [C] (v1.1 — offset-normalization fold-back applied) |
| `hubspot_contact_note_create` | HubSpot MCP (`manage_crm_objects`) | Create one free-text NOTE engagement associated to exactly one existing contact — no file attachments, no contact create/update | `contact_id` / `note_body` / `timestamp` (optional) | `created` / `note_id` / `captain_source` (or `created: false` / `error`) | [C] live |

---

## Active Colonel Registry

| Colonel | Mission (standing charge) | Output | Status |
|---|---|---|---|
| `enrich_hubspot_contact` | Pull a batch of never-attempted HubSpot contacts, scour the open web for the priority four (`company`, `jobtitle`, `hs_linkedin_url`, `website`), write only source-confirmed values, and close every contact with a terminal `ai_os_enrichment_status` so no contact is ever researched twice | Enrichment report — per-contact terminal verdict + per-field accounting with `source_url` on every written value | [O] at v1.3 — two live runs. Run 2 passed all six Tier 1 gates with zero deltas and still wrote three false values (rank-4 aggregator outranked the contact's own email domain); Meridian retracted Tier 2 pass. `[C]` denied — structural cleanliness is not evidence of truth. v1.3 adds a mandatory ranked Source Hierarchy; awaiting a run whose values survive [the_prompter]'s inspection |

---

## Shared Captains This Arm Depends On
*Listed for reasoning convenience only. These live in "theater-ops/_shared-captain-library/" and are catalogued in "shared_manifest.md" — never duplicated here as owned rows. Route through the hub: "captain_reference.md" -> Shared Captain Library pointer row -> "shared_manifest.md".*

`web_search` · `web_fetch` · `browser_scrape`