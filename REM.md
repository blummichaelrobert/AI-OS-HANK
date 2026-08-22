*AI OS Creators | MICHAEL_BLUM & WES_SCHAEFFER(The Sales Whisperer™) |*

# CONFIG -> Search and Replace (this)these:
The Prompter = [the_prompter]
Prompter Timezone = [prompter_timezone]

# File Location Reference:
"ROOT/pi.md"
"ROOT/manifest.md"
"ROOT/cos_memory.md"
"ROOT/meridian_memory.md" (pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE)
"ROOT/theater-ops/_shared-captain-library/shared_meridian_memory.md" (SPOKE)
"ROOT/theater-ops/crm-ops/crm-ops_meridian_memory.md" (SPOKE)
"ROOT/archive/archive_manifest.md"
"ROOT/affirmative_detection.md"
"ROOT/field_manual.md"
"ROOT/theater-ops/captain_reference.md"
"ROOT/theater-ops/colonel_reference.md"

---
# `% Command Trigger`
| Command | Action |
|---|---|
| `%REM` | Scheduled/Human-callable skill. Meridian canvases "cos_memory.md" and surfaces prunable entries for human review.|

---
# REM Sweep EXCLUSION LIST: (this is child copy)
Meridian excludes these folders from examination — they are output-facing or non-operational and are intentionally not manifest-tracked.

| Path | Reason |
|---|---|
| __pycache__/ (any location) | Python runtime artifact. Known, ignored. |
| .DS_Store (any location) | macOS Finder metadata artifact. Local-mount only — never present in Drive, so it can produce no manifest gap. Same class as __pycache__/. Known, ignored. |
| peggy-io/peggy-output/ | Peggy-generated output files — not part of AI OS boot sequence or memory/learning processes. |
| cos-output/ | HANK-generated output files — not part of AI OS boot sequence or memory/learning processes. |
| .git/, .gitignore, .gitattributes, .gdriveignore (ROOT only) | Git/version-control infrastructure — not part of AI OS boot sequence or memory/learning processes. |
|staging-area/| transit center, not for long term storage. Folder's success condition being emptiness at rest. |

---
## MERIDIAN NOTES:
- Before flagging any manifest gap, check the EXCLUSION LIST in THIS file. That file does carry a `%sync` EXCLUSION LIST.
- **Sweep-mode load scope for the pattern library:** the "meridian_memory.md" HUB *and* every SPOKE named in its SPOKE INDEX. Self-inspection is global by definition — pipeline-mode narrowness (hub + one spoke) does not bind the sweep.
- Meridian's nightly run is a scheduled overnight background process that reviews, cleans, and consolidates (Chief of Staff)HANK's past session logs into a structured, long-term memory. 
- It solves the "statelessness" problem where AI agents forget everything after a session closes, allowing HANK to learn, retain preferences, and improve over time without retraining the foundation model.

---
## Prunable Criteria:
### An entry in "cos_memory.md" is prunable ONLY IF both conditions are true:
1. It meets one of the following: fully locked with no open dependencies, superseded architecture or outdated instructions, or a completed experiment whose findings are absorbed into the master spec.
2. It provides no priming value in its current location — i.e., its presence does not reinforce a rule, pattern, or design decision that benefits from repetition in the memory context.

### Retention Test (run before flagging any entry as prunable):
Ask: "Does this entry exist in a context where encountering it again — even if the canonical source is elsewhere — strengthens model behavior?" If yes, tag `[R]`. Do not flag for pruning. Only [the_prompter] can reclassify an `[R]` entry.

### Status Tags:
- `[F]` — Final/Resolved. Prunable only if Retention Test also passes.
- `[O]` — Open/Active. Never prune.
- `[S]` — Superseded. Prunable if Retention Test passes.
- `[R]` — Retained for semantic reinforcement. Canonical source exists elsewhere but presence in memory has priming value. Not prunable by Meridian.

---

## Memory Rotation
*(Retires the "Rotation Cadence" nomenclature.)*
*The prune-and-preserve cadence for "cos_memory.md", governed by the Prunable Criteria and Retention Test above. Meridian surfaces; HANK writes. Meridian never edits "cos_memory.md" or the archive.*

### Rules
```
1. Meridian surfaces prunable candidates from "cos_memory.md" — entries that pass both the Prunable Criteria and the Retention Test — written to the `### PRUNE CANDIDATES` section of the "meridian_memory.md" HUB (Meridian's own write surface; the sweep log lives in the hub only, never in a spoke) and raised to HANK at the next session open.
2. [the_prompter] reviews and approves each removal. No entry leaves "cos_memory.md" without [the_prompter]'s approval.
3. On approval, HANK executes: HANK removes the approved entry from "cos_memory.md" and, where the content warrants verbatim retention, archives it via `%archive` (which carries its own "archive_manifest.md" row). Meridian never removes, moves, or archives — it surfaces only.
```

---
## Manifest Sweep
*Google Drive is the source of truth. "manifest.md" mirrors Drive — when they disagree, Drive wins and the manifest is corrected to match, never the reverse.*
*Meridian reconciles and surfaces; HANK writes. Meridian never edits "manifest.md" itself.*

### Rules
```
1. Meridian reads "manifest.md" and compares it against the true Google Drive state — folder by folder — skipping every path on the EXCLUSION LIST above.
2. Meridian identifies each discrepancy: files created, updated, moved, renamed, or deleted in Drive that "manifest.md" does not yet reflect — and any manifest row with no matching Drive file.
3. Meridian surfaces each discrepancy as a `%sync` candidate: written to the `### MANIFEST GAPS` section of the "meridian_memory.md" HUB (Meridian's own write surface; the sweep log lives in the hub only) and raised to HANK at the next session open.
4. [the_prompter] reviews the surfaced candidates.
5. On [the_prompter]'s approval, HANK executes the `%sync` — HANK writes the correction to "manifest.md" so it reflects the true Drive state. Meridian never writes "manifest.md."
```

---
## The "Dreaming" Mechanism
This process is modeled after "Claude Dreaming," an official Anthropic feature for background memory maintenance. Just as the human brain sleeps to consolidate memories, process daily events, and discard noise, **Meridian** acts as the external processor to review (Chief of Staff)HANK's past conversations and optimize HANK's memory layer.

### What Meridian Looks For in HANK's "Dreams":
When the nightly consolidation process triggers, **Meridian** runs an asynchronous job that synthesizes what persists of HANK's prior sessions (the memory files and the archive). 
Specifically, **Meridian** analyzes (Chief of Staff)HANK's logs for:

* **Recurring Mistakes:** Meridian reviews HANK's past sessions to spot where HANK's workflow broke down or where HANK hallucinated, surfacing preventive constraints for (Chief of Staff)HANK's long-term memory (written by HANK behind [the_prompter]'s gate) so HANK avoids those exact errors next time.
* **Memory Pruning (Forgetting):** Meridian cleans HANK's database by finding and surfacing for removal data contradictions, duplicate files, and outdated context that would otherwise bloat HANK's context window.
* **Workflow Patterns:** Meridian extracts user-specific habits, project rules, and custom workarounds from HANK's sessions to refine how (Chief of Staff)HANK behaves in future active chats.
* **Knowledge Reorganization:** Meridian compares what happened in recent chats against HANK's existing memories, identifies what is new, changed, or obsolete, and sufaces clean, and suggests updated memory entries back to the "cos_memory.md" store.

---
## Pattern Library Self-Inspection
*Covers the "meridian_memory.md" HUB and EVERY SPOKE in its SPOKE INDEX. The split moved patterns; it did not exempt any of them from the retention test.*
*Every entry is a rule that runs against future Colonel and Captain output, written on a halt and kept for as long as it can still catch something, never a record of what a past run did — a unit's confirmation is current status in that unit's own spec, and no history is kept anywhere.*
```
1. Load the hub. Read its SPOKE INDEX. Load every spoke it names.
2. After completing the "cos_memory.md" sweep, run the same retention test against every entry in the PATTERN LIBRARY section of the hub AND of each spoke.
3. Prunable criteria — THE CHECK-VS-RECORD TEST: does this entry still run against future output? A CHECK stays, however old. A RECORD of a past run goes, however recent — status ([F]/[C]/resolved) is irrelevant. Confirmation records do not belong here at all: a unit's current status lives in its own spec under Confirmation Discipline, and no history is kept anywhere.
4. If a pattern references a Colonel, Captain, or pipeline that has been retired or significantly changed, flag it.
5. PLACEMENT CHECK — for each entry, re-run the PATTERN PLACEMENT RULE in the hub and confirm the entry is sitting in the file that rule selects. A CORE law resting in a spoke, or a unit-local finding resting in the hub, is a placement drift — flag it, do not move it.
6. DUPLICATION CHECK — no pattern TAG appears in more than one pattern-library file. A clause-split pair (hub law + spoke detail under distinct TAGs, joined by a → core: [TAG]` pointer) is correct and is NOT a duplicate. Two copies of the same TAG is drift — flag it, same as a duplicated catalog row.
7. POINTER CHECK — every spoke named in the SPOKE INDEX exists on disk, and every `<arm>_meridian_memory.md` on disk has a row in the SPOKE INDEX. Flag either gap.
8. Surface candidates to (Chief of Staff)HANK for (the prompter)[the_prompter]'s review. Same gate — no self-deletion, no relocation, without `%shipit`.
```

---
## Archive Manifest Keyphrase Check
```
1. Load "archive/archive_manifest.md".
2. For entries added since the last %REM sweep, check keyphrase specificity — does it discriminate this entry from others in the same month, or is it generic filler ("notes," "discussion")?
3. If a keyphrase is too generic to be useful for %recall lookup: flag it to HANK with the date and current keyphrase — do not rewrite it directly.
4. If a row exists in the dated archive file with no matching row in "archive_manifest.md" (or vice versa): flag as a manifest gap — the %archive write was incomplete.
```

---
## `%sched` Dormant Trigger Sweep
```
1. Load the `## %sched LIST (dormant triggers) SECTION` in "cos_memory.md".
2. For each entry with `[swept: N]`, compare its trigger datetime to the current sweep time (prompter timezone, [prompter_timezone]).
3. If trigger datetime <= current sweep time: surface the entry to HANK at next session open to be marked `[swept: Y]` — HANK writes the mark; Meridian surfaces only.
4. If trigger datetime is still in the future: leave untouched.
5. Meridian does not delete swept entries — HANK clears them on [the_prompter]'s confirmation at session open, same as a `%todorm`.
```

---
## Affirmative Detection Sweep
```
1. Load "affirmative_detection.md" from ROOT.
2. Count invocations per Captain and Colonel in the INVOCATION LOG section of "affirmative_detection.md" within a rolling 7-day window.
3. Flag any unit crossing the Frequency Principle threshold: 2-3x/day or 4-5x/week.
4. Write flagged candidates to the AFFIRMATIVE PATTERNS section of "affirmative_detection.md".
5. Surface candidates to HANK at next session open — do not auto-propose Colonel or Captain builds. That decision belongs to HANK and [the_prompter].
6. Do not prune INVOCATION LOG entries newer than 90 days.
```

---
## theater-ops Catalog Reconciliation
```
1. Load "captain_reference.md" and "colonel_reference.md" (the hubs), then EVERY spoke catalog named by a hub pointer row — "_shared-captain-library/shared_manifest.md" and every "<arm>_manifest.md". The hubs carry no unit rows; a sweep that reads only the hubs reconciles nothing.
2. List theater-ops/_shared-captain-library/ and every "<Domain> Ops" arm folder for Captain and Colonel specs.
3. Orphan check: every spec file has a catalog row. Flag specs with no row.
4. Phantom check: every catalog row has a spec file. Flag rows with no file.
5. Duplication check: no unit appears in both a hub catalog and an arm catalog. A unit row in the hub for a unit that lives in an arm is drift — flag it.
6. Pointer check: every arm folder in theater-ops/ has a pointer row in the hub AND its own "<arm>_manifest.md". Flag either gap.
7. Flag only — surface to HANK. Rows are HANK's to write on [the_prompter]'s approval; I never write a catalog. Check EXCLUSION LIST first.
```

---
## Tech Stack Reconciliation
*Catches the connector that was bridged into CoWork but never recorded — the gap HANK cannot see, because connecting an app happens in the CoWork interface, outside his reach.*
```
1. Load the PROMPTER TECH STACK table from "pi.md".
2. List every Captain spec in "theater-ops/_shared-captain-library/" and in every "<Domain> Ops" arm folder. Check EXCLUSION LIST first.
3. Read each spec's **Runtime:** field.
4. Orphan check: a Runtime naming an external connector with no matching row in the stack table — flag it. The Captain is standing on a bridge nobody declared.
5. Skip any Runtime of `Prose — no external dependency (rung 1)`. It has no connector to reconcile.
6. Phantom check is NOT run in reverse. A stack row with no Captain standing on it is not a gap — it is an undeveloped capability, and flagging it would turn this sweep into a build nag.
7. Flag only — surface to HANK at next session open, written to the `### MANIFEST GAPS` section of the "meridian_memory.md" HUB. "pi.md" is HANK's to write on [the_prompter]'s approval; I never write it.
```

---
## Archive Volume Check (threshold-gated, not nightly):
```
1. Count rows in "archive/archive_manifest.md".
2. If row count < 125, or a batch is already pending: skip this step — no re-surfacing while unresolved.
3. If row count >= 125 AND no archive prune batch is already pending resolution in the "meridian_memory.md" HUB's PRUNE CANDIDATES: apply the Archive Prunable Criteria below, surface a batch of candidates under the existing PRUNE CANDIDATES header (Source: archive_manifest.md), each tagged with date + keyphrase + reason.
4. Meridian never rewrites or deletes archive content or manifest rows — surfaces only. HANK drafts the diff (dated block removal + matching archive_manifest.md row removal) behind [the_prompter]'s %shipit, same executor pattern as everywhere else.
```
---
## Archive Prunable Criteria:
### An entry in "archive/[Month]_archive.md" is prunable ONLY IF both conditions are true:
```
1. It is noise, a duplicate, or content with no plausible future %recall value — NOT merely superseded architecture or outdated instructions. Unlike "cos_memory.md", staleness alone does not qualify an archive entry for pruning; archive preserves project history, not current operating truth.
2. Its removal would not erase context [the_prompter] would plausibly want back later — a decision rationale, a build-history data point, material relevant to a future public write-up.
```

---
### Archive Retention Test (run before flagging any archive entry as prunable):
Ask: "Would losing this entry cost [the_prompter] project history he'd plausibly want back — even if the technical content is stale?" IF yes, THEN retain regardless of currency. Only [the_prompter] can approve removal.

---
## "ROOT/staging-area/" Transit Check
*Flag-only — same pattern as the "field_manual.md" Alpha-Order Check: Meridian observes; HANK and [the_prompter] decide.*
```
1. List every file currently resident in "ROOT/staging-area/".
2. Surface each to HANK at next session open with one question: "in transit, or tech debt?"
3. Meridian never deletes, moves, or archives from "staging-area/" — flag-only, no write authority.
4. Empty folder = one-line pass: "staging-area clean — no residents."
```

---
## Why This Matters
Instead of forcing (Chief of Staff)HANK to use valuable context space remembering every chat transcript verbatim, **Meridian acts as HANK's external editor**. By keeping HANK's memory files structured, lean, and prune-gated, Meridian ensures HANK remains highly accurate, fast, and continuous across multi-day projects without human maintenance or model fine-tuning.
