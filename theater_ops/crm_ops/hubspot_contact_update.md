# Captain Function Contract
**Captain Name:** hubspot_contact_update
**Version:** 1.1
**Runtime:** HubSpot MCP

---

## Prose Layers (human register)

| Layer | Description |
| --- | --- |
| Purpose | Update one or more of a fixed set of confirmed-writable properties on an existing HubSpot contact, identified by `contact_id`. |
| Inputs | `contact_id` (string, required) — HubSpot object id of the contact to update. `invoked_by` (string, required) — the calling Colonel's name, or `%compose`, injected by HANK at orchestration time. At least one of the following twelve optional properties must also be supplied, or the Captain holds and is not invoked: `firstname`, `lastname` (Name); `company`, `company_size`, `industry` (Company); `jobtitle`, `job_function` (Title); `phone` (Phone); `city`, `state`, `country` (Location); `hs_linkedin_url`, `twitterhandle`, `website` (Social). All twelve confirmed live as plain `string` properties on this portal. **Plus one pipeline-state property (v1.1):** `ai_os_enrichment_status` (Pipeline State) — an enumeration accepting exactly `Processed`, `Skipped`, or `Error`, case-sensitive and verbatim. It is the sole admitted enum and the sole non-person field; see the Pipeline-State Exception in Constraints for why it is admitted where `lifecyclestage` and `hs_seniority` are not. The Captain accepts no other fields — `email` is out of scope (no identity-changing path through this Captain, avoiding the uniqueness-conflict risk `hubspot_contact_create` guards against), and `lifecyclestage` / `hs_seniority` remain deliberately excluded as enumerations (see Constraints). |
| Outputs | `updated` (boolean) — true if the contact was written. `captain_source` (string) — always "hubspot_contact_update". `contact_id` (string) — echoed back regardless of outcome. `invoked_by` (string) — the caller, echoed back. When `updated: true`: `contact_url` (string) — the HubSpot record URL, and `updated_fields` (array of strings) — the property names actually written, not just a pass/fail flag. When `updated: false`: `error` (string) — the failure reason. |
| Error Behavior | On HubSpot MCP rejection (e.g. `contact_id` does not resolve to a real record), returns `{ "updated": false, "captain_source": "hubspot_contact_update", "contact_id": "<id>", "invoked_by": "<caller>", "error": "<reason>" }`. If `contact_id` is missing, or no optional field is supplied alongside it, the Colonel must surface this before invocation — the Captain is never called with nothing to write. No fabrication: if the MCP does not return a field, the Captain returns `null` for it. The Colonel must not proceed on error, and must not silently retry with altered data — surface to HANK per Halt Protocol. |
| Constraints | Runtime: HubSpot MCP (`manage_crm_objects`, update path) only. Single call — no two-call pattern. Storing free-text notes is out of scope entirely; HubSpot's `NOTE` object is a distinct object type from a contact property and is handled by its own Captain, never bundled here — SRP holds the same line drawn for `hubspot_contact_create`. One contact per invocation — batch updates are the Colonel's responsibility. `lifecyclestage` and `hs_seniority` are both enumerations on this portal (confirmed live), not free text — deliberately cut rather than silently treated as strings, since the current Validation Schema vocabulary (`required`/`types`/`constants`/`conditional`) has no "must be one of N values" check. Cut for KISS; an explicit future upgrade, not an oversight, if enum support is ever added to the schema standard. **Pipeline-State Exception (v1.1) — narrow, and the only one.** `ai_os_enrichment_status` is admitted as an enum where those two are refused, on three grounds that do not generalize: (1) **Ownership** — it is an AI OS-authored custom property whose three values are fixed by this system's own spec, not a HubSpot-managed option set that can change underneath us; (2) **Category** — it carries *pipeline* state, not *person* data, which is a deliberate widening of this Captain's scope stated here rather than left to be discovered in a diff; (3) **Necessity** — without a write path for it no enrichment batch is resumable, because `hubspot_contact_search` would re-pull the same population every run forever. **Case is load-bearing and un-checkable at Tier 1.** The three literals are `Processed`, `Skipped`, `Error` — capitalized, confirmed live against the portal. The Validation Schema still has no "must be one of N" check, so a wrong-cased value passes Tier 1, is rejected by HubSpot, and surfaces as `error` — which a naive Colonel would read as a transient failure and retry forever. Copy the literals; never retype them. Meridian verifies the value at Tier 2. Any future enum admitted to this Captain requires the same three-ground justification written here — the exception is a door held open by hand, not a precedent. The underlying `manage_crm_objects` MCP tool requires its own explicit confirmation table plus `confirmationStatus: CONFIRMED` before it will execute — HANK presents that exact table to [the_prompter], and [the_prompter]'s `%shipit` on the table satisfies `confirmationStatus` directly. One approval, satisfied twice — never a second, independent gate. `website` may come back portal-normalized rather than verbatim — confirmed live (HubSpot silently prepends a protocol). Not a Captain failure and not fabrication; a Colonel comparing the sent value against the stored value on this field should expect that normalization, not treat it as a discrepancy. |

---

## Two-Tier Assignment

**Tier 1 (validator):** `updated` present and boolean; `captain_source` present, string, equal to "hubspot_contact_update"; `invoked_by` present and string; `contact_id` present and non-null (always echoed, success or failure); when `updated: true`, `contact_url` and `updated_fields` present and non-null; when `updated: false`, `error` present and non-null. Structural facts only.

**Tier 2 (Meridian / Colonel / HANK):** whether `contact_id` actually names the contact the Colonel intended — this Captain trusts the id given, it does not verify identity (that's `hubspot_contact_lookup`'s job, upstream). Whether the values supplied are semantically correct or current — a Colonel writing a stale job title is a Tier 2 problem, not a structural one. Whether a successful-but-partial update (some fields land, others were never supplied) is a problem worth flagging for this mission.

---

## Validation Schema (machine register)

<!-- AIOS-VALIDATION:START -->
```json
{
  "captain": "hubspot_contact_update",
  "required": ["updated", "captain_source", "invoked_by", "contact_id"],
  "types": {
    "updated": "boolean",
    "captain_source": "string",
    "contact_id": "string",
    "contact_url": "string",
    "updated_fields": "array",
    "invoked_by": "string",
    "error": "string"
  },
  "constants": {
    "captain_source": "hubspot_contact_update"
  },
  "conditional": [
    { "when": {"updated": true}, "require_non_null": ["contact_url", "updated_fields"] },
    { "when": {"updated": false}, "require_non_null": ["error"] }
  ]
}
```
<!-- AIOS-VALIDATION:END -->

---

## Confirmation Discipline
`Status: [C]` — live-confirmed. Test: `hubspot_contact_lookup`, confirmed the record, then `hubspot_contact_update` wrote `company`, `jobtitle`, `hs_linkedin_url`, and `website` in one call. Independently re-read via `get_crm_objects` — all four fields confirmed written, not just trusted from the update response (which returned an empty `properties: {}`, same pattern already known from `hubspot_contact_create`). One finding folded back into Constraints: `website` was portal-normalized on write.

**v1.1 — `[C]` re-confirmed live.** Test: `ai_os_enrichment_status` written as `Processed`. Independently re-read via `get_crm_objects` — value confirmed stored verbatim and correctly cased, not trusted from the update response (which again returned an empty `properties: {}`, the known pattern). `validator.py` verdict `pass`, zero deltas. The enum input path holds; capitalization accepted exactly as specified. Original v1.0 note follows. The Pipeline-State Exception adds `ai_os_enrichment_status` to the accepted input set. Per `EvalHyp`, the thirteenth field is a hypothesis until a live write of that specific property lands and re-reads clean. The Validation Schema is unchanged by this edit — no output field was added or retyped — so the machine-register contract carries forward intact; what is unproven is the *input* path for an enum, which Tier 1 never checked in the first place. `[C]` is retained on the strength of the output-schema confirmation and re-earned for the new field on the v1.1 live test.
