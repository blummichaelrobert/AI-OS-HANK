# CONFIG -> *Searched and Replaced Properties:*
The Prompter = [the_prompter]
Prompter Timezone = [prompter_timezone]

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/cos_memory.md" | HANK memory — TODO list + %logit entries |
| "ROOT/affirmative_detection.md" | Affirmative Detection patterns (Frequency Principle) |
| "ROOT/REM.md" | Nightly %REM sweep instructions |
| "ROOT/theater-ops/_shared-captain-library/shared_meridian_memory.md" | Shared Captain SPOKE |
| "ROOT/theater-ops/crm-ops/crm_ops_meridian_memory.md" | Client Resource Management SPOKE |
| "ROOT/theater-ops/crm-ops/visual_production_ops_meridian_memory.md" | Visual Image Production SPOKE |
| "ROOT/theater-ops/crm-ops/web_research_ops_meridian_memory.md" | Web tools, i.e. Browser Scraping SPOKE |

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
## `%sync` EXCLUSION LIST: (this is child copy)
`%sync` operations do not apply to the folders on this list. The folders on this list are exluded from the **Drive File ID Retrieval** rule. 
| Path | Reason |
|---|---|
| __pycache__/ (any location) | Python runtime artifact. Known, ignored. |
| .DS_Store (any location) | macOS Finder metadata artifact. Local-mount only — never present in Drive, so it can produce no manifest gap. Same class as __pycache__/. Known, ignored. |
| peggy-io/peggy-output/ | Peggy-generated output files — not part of AI OS boot sequence or memory/learning processes. |
| cos-output/ | HANK-generated output files — not part of AI OS boot sequence or memory/learning processes. |
| .git/, .gitignore, .gitattributes, .gdriveignore (ROOT only) | Git/version-control infrastructure — not part of AI OS boot sequence or memory/learning processes. |
|staging-area/| transit center, not for long term storage. Folder's success condition being emptiness at rest. |
|Claude outputs/| folder that is automatically created by Claude engine. Outside the scope of this project. |

---
# (my)Meridian Memory — HUB
*Author: (me)Meridian — Universal QA Agent, "AI OS"*
*AI OS System Log*
*This file is one of (my)Meridian's write surfaces along with "affirmative_detection.md". It is a machine-readable QA pattern library and sweep state tracker.*
*It is not a narrative log. Every pattern here is checked against pipeline output on every run.*

**This file is the HUB.** It carries CORE patterns only — platform-level truths, Command Triad persona rules, and system-wide laws that bind every unit in every domain. Unit-local patterns live in the SPOKE file belonging to the folder that unit's spec lives in. Same hub-and-spoke discipline as "theater-ops/captain_reference.md" and the `%recall` path: hub -> spoke -> entry. Never read the spokes blind, and never load a spoke whose domain the run does not touch.

---
# SPOKE INDEX
*One pointer row per spoke. A spoke earns a row when its folder holds a unit spec that has produced a pattern — never in anticipation.*

| Spoke file | Covers | Path |
|---|---|---|
| shared_meridian_memory.md | Shared, domain-agnostic Captains | "ROOT/theater-ops/_shared-captain-library/" |
| crm_ops_meridian_memory.md | CRM Ops arm — Captains and Colonels | "ROOT/theater-ops/crm-ops/" |
| web_research_ops_meridian_memory.md | Web Research Ops arm — Colonels (owns no Captain) | "ROOT/theater-ops/web-research-ops/" |
| visual_production_ops_meridian_memory.md | Visual Production Ops arm — Colonels (owns no Captain) | "ROOT/theater-ops/visual-production-ops/" |

**Spokes carry no `%REM SWEEP LOG`.** Sweep state is global and lives in this file only — one instance of each sweep header, always. A spoke holds pattern entries and nothing else.

---

# PATTERN PLACEMENT RULE
*The write-time test. Run it top-down; the first rule that fires decides the home. This is the deterministic counterpart to the Placement test in "captain_reference.md" — without it, an ambiguous pattern gets written to two files, and that is drift, not redundancy.*

```
1. Does the pattern name a specific Colonel or Captain?
   NO  -> CORE (this file). Platform/tool-level facts, sweep mechanics,
         and system-wide laws have no unit to follow.
   YES -> go to 2.

2. Where does that unit's spec file live on disk?
   theater-ops/_shared-captain-library/ → shared_meridian_memory.md
   theater-ops/<arm-kebab-case>/        → that arm's <arm>_meridian_memory.md

3. Is the pattern about a Command Triad persona (HANK, Meridian, Peggy)?
   -> CORE. The Triad is STAFF at ROOT, not an arm. A persona has no
     theater to follow, regardless of which pipeline surfaced the finding.

4. Does the pattern carry BOTH a general law AND a unit-local detail?
   -> SPLIT BY CLAUSE. The law goes to CORE under its own TAG; the local
     detail goes to the spoke under a distinct TAG carrying `→ core: [TAG]`.
     NEVER copy the entry whole into both files.

5. One entry, one home. A pattern appearing in both hub and spoke is drift.
   Flag it at the next `%REM` sweep the same way a duplicated catalog row
   is flagged (theater-ops Catalog Reconciliation, rule 5).
```

**Load rule — pipeline mode.** Load this hub always. Load exactly ONE spoke: the one belonging to the folder the unit under evaluation lives in. Consult the capability catalogs to learn which arm a unit belongs to (hub -> spoke) before loading; that lookup is already standing discipline.

**Load rule — `%REM` sweep mode.** Load the hub AND every spoke named in the SPOKE INDEX. Self-inspection is global by definition; pipeline-mode narrowness does not bind the sweep.

---
# WRITE RULES
When updating this file, never create new section headers inside `# %REM SWEEP LOG` — locate the existing `### PRUNE CANDIDATES`, `### MANIFEST GAPS`, and `### CROSS-FILE CONSISTENCY` headers and insert entries within them. One instance of each header. Always.

Before writing any new pattern, run the PATTERN PLACEMENT RULE. The write is not complete until the entry sits in exactly one file.

---
# SCHEMA
*Identical in the hub and in every spoke. One schema, one library, three files.*

Single-line entry format:
`[TAG] | [Colonel/Captain] | [Pipeline] | [Date] | [Rule violated] | [Source] | [STATUS]`

**Field glossary:**
| Field | Definition |
|---|---|
| TAG | Vowel-compressed entry key identifying the pattern. Length follows legibility, not a fixed count; identifiers (acronyms, filenames, version tokens) are exempt from compression. Authoritative definition: the SYNTAX KEY in this file. |
| Colonel/Captain | The unit that produced the failing output |
| Pipeline | Named pipeline where the failure occurred |
| Date | Date pattern was first observed (YYYY-MM-DD) |
| Rule violated | The specific rule or field that failed — cite exactly |
| Source | Where the rule lives: Battle Plan / "cos_memory.md" / this pattern library |
| STATUS | [O] = active, check every run. [F] = resolved, retained for audit. [C] = confirmed live. |

---
# NEW MEMORY SPOKE FILE FORMAT:
*Use visual_production_ops_meridian_memory.md as an example.*

```
# CONFIG
Standard CONFIG section used throughout the AI OS.

# FILE LOCATION REFERENCE
Standard File Location Reference used throughout the AI OS.

# SYNTAX KEY
Standard Syntax Key used throughout the AI OS.

# <arm-name> - Meridian Pattern Memory (Spoke)
Rules releated to being a spoke in Meridian's memory.

# SCHEMA
Standard Schema tags used throughout the AI OS.

# PATTERN LIBRARY - <arm-name-all-caps>
An entry stays only while it is a CHECK — something that runs against future output. Resolved failure patterns stay for exactly that reason, in the hub and in every spoke. CONFIRMATION RECORDS DO NOT BELONG HERE AT ALL: a unit's current status lives in its own `## Confirmation Discipline` section, and no history is kept anywhere.

# CONFIRMATION RUN - Live Tested:
Single date of when spoke Colonel latest earning of [C] status.

## LIVE TESTED OPERATIONAL THEATER MEMORIES
NOT CONFIRMATION PATTERNS, those exist in the Colonels and Captains themselves!

## CURRENT OPEN FINDINGS
Resolved items are DELETED from active sections. No archive copy is retained — the correction lives in the file where it was made. Active sections must be empty when nothing is open.

## PENDING RESOLUTION
Temporary holding state between (my)Meridian flag and (the prompter)[the_prompter] resolution. Entries are deleted on resolution. Empty when the system is healthy.
```

---
## NO-EPITAPH CLAUSE
The `%REM SWEEP LOG` is TRANSIENT.** On [the_prompter]'s directive, after (I)Meridian violated the rule above in the sweep of that same date.
```
1. DELETE means delete. When a finding is resolved, the entry is REMOVED —
   not struck through, not italicized, not replaced with a "RESOLVED on
   [date]" summary, not compressed into a one-line note. Gone.
2. A resolution narrative is a SECOND COPY of a correction that already
   exists in the file where the correction was made. That is the exact
   duplication I flag in other files. It is drift, and it is mine.
3. Resting state of PRUNE CANDIDATES / MANIFEST GAPS / CROSS-FILE
   CONSISTENCY is the header alone, with nothing under it. An EMPTY
   section is the HEALTHY state — never read it as an unfinished sweep.
4. Verification of a fix is done BEFORE the delete, and reported to HANK
   in the Response Pane. The Response Pane is where a resolution is
   communicated; this file is not the transcript of that conversation.
5. Cost is the whole reason. This log is read at the start of every sweep,
   forever. An entry that describes finished work is a token bill with no
   remaining buyer.
```

**BOUNDARY — this clause does NOT reach the `PATTERN LIBRARY`.** Confirmed by [the_prompter]. The two sections are different instruments and are governed differently:
| Section | Lifecycle | Why |
|---|---|---|
| `%REM SWEEP LOG` | TRANSIENT — delete on resolution | A finding is a work item. Once the work is done it describes nothing live. |
| `PATTERN LIBRARY` (hub + every spoke) | PERMANENT **while it is a check** — a check is never deleted; a record is never admitted | A pattern is a CHECK. `WbFtchBin`, `ProvNotTruth`, `CatErr` and every entry beside them run against live output on every subsequent pipeline run — deleting one does not save tokens, it removes a test. A CONFIRMATION is a record of a past run and is not written here at all. |
| A unit's `## Confirmation Discipline` (in its own spec — NOT my file) | TRANSIENT — latest status only, `[C]` REPLACES `[O]`, and it is the SOLE home | The spec's current status IS the confirmation record; my `[C]` line in a spoke was the second copy, and it is the one that went. Superseded narrative is dropped, not relocated — residual write-up value goes to "cos-output/". Rule: "captain_function_contract.md" Confirmation Discipline. |
Never apply the no-epitaph clause to a pattern entry. Never leave an epitaph in the sweep log.

A pattern moves from `[O]` to `[F]` when ONE of the following is true:
1. The Colonel or Captain spec has been updated to structurally prevent recurrence.
2. HANK has escalated the pattern to "cos_memory.md" as a standing rule ([the_prompter]'s gate).

---
# START `CORE` GENERIC AIOS PATTERN LIBRARY:
*System-wide and platform-level only. Unit-local patterns live in the spokes named in the SPOKE INDEX.*

## Operational Rules

RuleWhrRd | Command Triad — Meridian | System-wide | 2026-08-14 | **A RULE MUST LIVE WHERE IT FIRES, IN A FILE THAT IS READ WHEN IT FIRES.** The INVOCATION LOG tick was correctly specified — one line, self-authorizing, right format — and never once executed, because it was specified ONLY in the OUTPUT HANDLING table of "cos_battle_plan.md" and in "affirmative_detection.md". Neither file is read at boot. "affirmative_detection.md" is read at `%REM` alone; the Battle Plan template is read only when a Battle Plan is authored or run. So at the exact moment a Captain was invoked, no file in context carried the rule — and every `%compose` run (which has no Battle Plan at all) was structurally exempt. The log sat empty through real pipelines on while the rule sat, perfectly worded, in files nobody had open. THE TEST, run on any new standing rule before it is written: (1) WHEN does this fire? (2) WHICH files are in context at that moment? (3) Is the rule in one of them? If no, the rule is decoration. This is `TopDwnPrm`(Top Down Semantic Priming) stated as a placement constraint rather than an ordering one — priming cannot prime from a file that was never loaded. Applies to every future rule in every file, not only to Meridian's. Fix applied: the tick rule now lives in "meridian.md" (boot-read) at the Tier 1 Validator Gate; the other two files carry pointers only, one rule one home. | %REM sweep | [C]

SlfInsp | Meridian %REM | System-wide | 2026-06-16 | After the cos_memory.md sweep, Meridian runs the same retention test against its own PATTERN LIBRARY. Same prunable criteria, same surface-to-HANK gate before anything is deleted. Step added to "REM.md". Self-inspection covers this hub AND every spoke in the SPOKE INDEX — a pattern is not exempt from the retention test because it was relocated into an arm. | codified during session | [F]

DsgPhFam | System-wide | System-wide | 2026-06-27 | Design Philosophy Family codified: KISS + "Elegance is in simplicity" + Frequency Principle. All three are standing QA anchors. Proposed builds that fail any anchor surface to HANK before execution. | cos_memory: DsgPhFam | [F]

---
## QA PATTERNS:

---
## LIVE TESTED THEATHER MEMORIES:

WbFtchBin | Platform/tool-level | ad-hoc %compose | 2026-08-08 | CoWork's native WebFetch returns literal "[binary data]" for any non-text/html content-type, discarding the response body — confirmed against uschamber.com/co/feeds/rss (application/rss+xml), which is valid UTF-8 XML, not gzip, not actually binary. The limitation is WebFetch's content-type handling, not the source content. Any future Captain relying on WebFetch for non-HTML content (JSON APIs, XML, plain text feeds) should expect this failure mode. | Live test, mcp__workspace__web_fetch called twice against the same URL | [C]

SbxNoNet | Platform/tool-level | fetch_decode.py (_code-tools/_python-tools) | 2026-08-08 | CoWork's bash/Python sandbox has no general outbound network access — confirmed via 6 independent methods (DNS, raw TCP socket, curl, wget, fresh pip install, plain HTTP), all blocked identically by a local proxy (403/DNS failure). Platform restriction, not fixable by any script. fetch_decode.py's gzip-decode logic has never actually been exercised — its substrate is non-functional for network fetch in this sandbox. Open question: whether production Captain execution shares this restriction. | 6-method network diagnostic | [C]

SuffNotVol | Any retrieval unit — domain-agnostic law | System-wide | 2026-08-14 | **THE LAW: retrieval sufficiency is not volume.** A substrate can return an abundant, well-formed, structurally perfect document that is entirely non-current — and every check the AI OS owns will pass it. Volume without currency, and currency without volume — the same page, the same moment, two mirror-image failures. Tier 1 cannot see either: presence, type, and constants are all satisfied by stale text and by thin text alike. This is `ProvNotTruth`'s sibling on the RETRIEVAL axis rather than the WRITE axis — that law says a sourced claim may still be false; this one says a fetched document may still be wrong-as-current. THE OPERATIONAL CONSEQUENCE: any Captain Constraint that says "escalate when the cheaper substrate is judged insufficient" is under-specified until "insufficient" names CURRENCY and COVERAGE, not merely emptiness. A judgment layer measuring sufficiency by page length will escalate exactly never and ship stale content with a clean audit trail. Applies to ANY retrieval unit, ANY substrate — usnews.com is where it was found, not where it is bounded. **THE LADDER RANKS COST, NOT COVERAGE.** A higher rung is not a superset of a lower one — it is a DIFFERENT instrument with a different failure mode, and climbing it can subtract content as easily as add it. Any Colonel that treats escalation as strict improvement will silently lose data on server-rendered pages. Corollary for `%compose` and every future Battle Plan: the substrate choice is a per-URL judgment, never a standing preference. Current substrate status for each Captain named above lives in that Captain's own spec under Confirmation Discipline — "web_fetch.md" and "browser_scrape.md". | Live tests, %compose invocations, two substrates against two URLs | [C]

ProvNotTruth | Any enrichment unit — domain-agnostic law | System-wide | 2026-08-12 | **THE MOST IMPORTANT FINDING OF THIS BUILD.** Six Tier 1 gates fired, six `pass`, zero deltas, full accounting, every value source-cited — and three of four written values were FALSE. **THE LAW: provenance discipline verifies a claim was FOUND; it says nothing about whether the claim is true, current, or belongs in the field it was written to.** I passed Tier 2 and then RETRACTED — I verified structure, accounting, and source presence, and certified data I had no ground truth for. Three runs, three instances, one pattern — right value/wrong field, right value/no selection rule, wrong source outranking right source. The missing mechanism was never a per-field rule; it was SOURCE RANKING, and it is irreducibly Tier 2 because no validator can express "who is entitled to say this." THE AFFILIATION TRAP: third-party aggregators such as scraped org charts routinely list resellers/partners/consultants/certified-experts as EMPLOYEES of the vendor they serve; aggregators agreeing with each other is not corroboration, they copy each other. SECOND FINDING — terminal states guarantee the queue shrinks AND guarantee a wrong value is never re-examined; a one-way write locks false data in permanently, and only the operator can reopen it. The trade is still correct; the one-way write is *why* source ranking must be mandatory before the write, not after. THIRD FINDING — both tiers cleared and the output was false; the only ground truth was the operator. `%shipit` is not ceremony; it is the only place truth enters the system. Applies to ANY enrichment unit, ANY domain, ANY substrate — HubSpot is where it was found, not where it is bounded. Applies to ANY enrichment unit, ANY domain, ANY substrate — HubSpot is where it was found, not where it is bounded. | Live test, %compose invocation | [C]

CatErr | Any enrichment unit — domain-agnostic law | System-wide | 2026-08-12 | **THE LAW: source discipline catches fabrication but not CATEGORY ERROR. A value can be true, correctly sourced, and still in the wrong field.** It is a check that binds any unit writing a typed field from prose. THE INSTANCE that produced it: a Colonel wrote `jobtitle: "Advisor"` from the sentence *"Wes Schaeffer is a USAF veteran, author, and advisor."* That sentence names the person AND the fact together, so it PASSED the "source must name person and fact" provenance check — and was still wrong, because a descriptive noun (author / advisor / speaker / consultant / trainer) is not a role held at an organization. THE OPERATIONAL CONSEQUENCE: any unit writing to a typed field needs a CATEGORY check distinct from its PROVENANCE check — "is this the right KIND of thing for this field" is a separate question from "did a source say it," and passing the second does not imply the first. Sibling of `ProvNotTruth` on the same axis: that law says a sourced claim may be false; this one says a sourced, TRUE claim may still be misfiled. | Live test, %compose invocation| [C]

OrgNotUrl | Platform/tool-level | ad-hoc %compose | 2026-09-05 | **THE FINDING: CoWork's native browser reports a tab's URL as ORIGIN ONLY — the path is silently stripped, and the truncation is not signalled.** A request for a deep path reports back as the bare scheme+host, with no error, no flag, and no difference in shape from a genuine full URL. THE DANGER IS THE TIER IT DEFEATS: the value is present, a string, and non-null, so a `url_landed`-style field passes Tier 1 WHILE BEING FALSE — this is `CatErr`(Category Error) on the RETRIEVAL axis, a structurally valid value that is the wrong thing. Any Captain on this substrate that requires an observed landing URL is requiring what its scope cannot observe; the field must be observe-and-report-if-visible, `null` when only an origin is exposed. **NEVER reconstruct the path by appending the requested path to the reported origin** — that fabricates a redirect check, and a fabricated check is worse than an absent one because it reads as evidence. OPERATIONAL CONSEQUENCE: redirect detection is NOT available at this rung; a unit needing it obtains it from a unit with the scope to see it. Applies to ANY unit on the native browser, ANY domain — a Fetch Captain is where it was found, not where it is bounded. | Live test, 4 URLs across 4 domains, native browser pane | [C]

MdlNotRaw | Platform/tool-level | ad-hoc %compose | 2026-09-05 | **THE FINDING: CoWork's native WebFetch returns a MODEL-MEDIATED ANSWER, not raw page text.** The substrate answers a prompt against the fetched page using a small model; it does not hand back the page. Live test: two of four URLs came back as prose SUMMARIES where verbatim text was requested, and every character count was ASSERTED BY THE MODEL rather than computed — one run reported an approximation in a field typed `number`, which is a fabricated value under `FlFst`(Fail-Fast) never-mask, not a rounding error. Sibling of `WbFtchBin` on the same substrate: that entry says WebFetch discards non-text bodies; this one says it paraphrases the ones it keeps. THE OPERATIONAL CONSEQUENCE, and it is a build rule: **any Captain whose contract requires verbatim `page_text` or a computed length CANNOT stand on this substrate** — the rung is not a cheaper way to do that job, it is a different job, and admitting it forces every honest rung to demote the fields it cannot fill. A contract wanting raw text declares a browser rung; a contract wanting cheap gist declares this one and says so in its Outputs. | Live test, 4 URLs, CoWork native WebFetch | [C]

PartGate | Any retrieval unit — domain-agnostic law | ad-hoc %compose | 2026-09-05 | **THE LAW: gating is not binary. A page can return REAL CONTENT and a WALL in the same payload, and a binary success/gated field forces the unit to call a partial answer a whole one.** THE INSTANCE: a social profile at an anonymous browser rung returned a genuine bio, location and follower counts while withholding every post behind a log-in prompt — the fetch completed, real text came back, and the record said `success` on a page that served none of the mission. Nothing was fabricated and no gate fired; the shape of the schema did the lying. THE OPERATIONAL CONSEQUENCE — CORRECTED 2026-09-05, SAME DAY, BY THE NEXT RUN: **gate presence is an OBSERVATION, not a structural fact, and belongs at Tier 2 — never as a Captain-emitted field at Tier 1.** the same gated URL, same substrate, rendered WITH its wall and then WITHOUT it, so the field reported `true` and then `false` on a page that withheld its content both times — and Tier 1 passes `false` every time, because a boolean is a valid boolean. THE STANDING RULE THIS PRODUCES: a required output field must be an ECHOED INPUT, a CONSTANT, a COMPUTED value, or a VERBATIM runtime report — never an observation whose truth can vary between two runs of the same page. A retrieval unit reports that a page was retrieved; the judgment layer infers gating from CONTENT ABSENCE against mission expectation. This is the AI OS's own many-match rule on the GATING axis: *the Captain reports what it saw; it never decides that a partial answer is a whole one* — `SuffNotVol`'s sibling, where that law says abundance is not currency and this one says completion is not access. COROLLARY FOR ESCALATION: a wall detected on a SUCCESS is stronger evidence for climbing to an authenticated rung than a bare gated failure, because it proves the page exists and that a session would reveal more of it. Applies to ANY retrieval unit, ANY substrate, ANY domain. | Live test, 8 runs across two browser rungs | [C]

BrwIdNm | Platform/tool-level | ad-hoc %compose | 2026-09-05 | **THE FINDING: the Chrome connector's browser DISPLAY NAME is not a stable identifier and does not necessarily match the deviceId selected.** Selecting a browser by the deviceId listed against one display name returned a connection confirmation naming a DIFFERENT browser, with no error. The deviceId is the identifier; the display name is a label the account holder can change and the runtime may report inconsistently. THE OPERATIONAL CONSEQUENCE: any record, spec, or Confirmation Discipline note that pins a run to "Browser N" has pinned it to nothing — cite the deviceId, or cite the rung and the fact of authentication, never the friendly name. This is `GenNotSpec`(Generic Not Specific) enforced from the other direction: the display name looks like an identifier and is not one. A multi-browser account is where this bites; a single-browser account will never see it, which is exactly why it must be written down rather than remembered. AMENDEDMENT — THE FORWARD HALF, and it generalises past browsers: **a caller-DECLARED substrate is not evidence of the substrate that ran.** A rung is an input on these contracts, so a record produced at an authenticated rung and one produced at an anonymous rung are textually identical, and `substrate_used` merely echoes what the caller asked for. The operator cannot audit the rung from the record, and neither can I. THE RULE: **where a substrate has a stable machine identifier, that identifier — never its display name and never the rung label alone — is what a run record carries as its evidence.** A deviceId is checkable after the fact; "4b" and "Browser 3" are assertions. This is `ProvNotTruth` on the SUBSTRATE axis: the declaration proves what was requested, never what answered. | Live test, browser selection by deviceId; amended after a rung could not be evidenced from a record | [C]

Tier1NotTruth | Any unit emitting a structured map or record | ad-hoc %compose | 2026-09-05 | **THE LAW: a Tier 1 `pass` proves a structure EXISTS and is well-formed; it says NOTHING about whether that structure corresponds to the thing it describes.** THE INSTANCE: a parsing unit emitted a map labelling twenty navigation labels, captions and fragments as "headings" in a single article body — every required field present, correctly typed, constant matched, validator verdict `pass`, zero deltas, and the map was plainly wrong about the document. Sibling of `ProvNotTruth` on the STRUCTURE axis: that law says a sourced claim may be false, this one says a WELL-FORMED claim may be false. THE OPERATIONAL CONSEQUENCE, and it is a build rule: **any output field carrying a CLASSIFICATION — what a thing IS, not what it literally contained — is a Tier 2 judgment wearing a Tier 1 costume, and no validator will ever catch it being wrong.** The fix that works is not a better heuristic; it is REMOVING THE CLAIM: emit verbatim content plus order, and let the judgment layer derive kind. A map that makes no claim cannot make a wrong one. Applies to ANY unit emitting typed or labelled structure, ANY domain. | Live test, 5 pages, 9 reconciled gates | [C]

StrLostUpstr | Any multi-stage retrieval chain | ad-hoc %compose | 2026-09-05 | **THE LAW: structure destroyed by an upstream stage cannot be recovered by a downstream one, at any rung.** Rendered-text extraction strips list markers, heading tags and nesting before any parser sees the text — confirmed by a list collection that came back EMPTY on five consecutive pages that all visibly contained lists. The downstream unit was not defective; its input never carried the signal. THE TRAP THIS SETS: the obvious repair is to infer the lost structure from surface cues (parallel short lines, indentation, capitalisation) — that is INVENTING structure the input does not carry, which the never-mask rule forbids outright, and it fails silently on every page whose styling differs. THE OPERATIONAL CONSEQUENCE: when a stage cannot produce a category, the honest options are to DROP the category or to change the UPSTREAM stage's output format — never to reconstruct it downstream. Changing upstream is its own decision at its own gate and voids that unit's `[C]`. Corollary for chain design: ask what each stage's output format DESTROYS, not only what it carries. | Live test, 5 pages, empty collection on all | [C]

CntnNotPrm | Any unit that WRITES — domain-agnostic law | ad-hoc %compose | 2026-09-06 | **THE LAW: a destination pinned as a schema `constants` entry converts "trust this unit not to write elsewhere" into an unappealable Tier 1 check — CONTAINMENT IS CHEAPER THAN PERMISSION.** THE INSTANCE: the first writing Captain in the shared library declared its output folder as a CONSTANT rather than an input, and an adversarial record carrying a redirected destination returned `output_failed` deterministically, naming the field — the containment claim proven in code rather than asserted in prose. THE OPERATIONAL CONSEQUENCE, and it is a build rule for every future writing unit: **bound the blast radius in the SCHEMA, then let the Colonel fire it — do not bound it with a per-run `%shipit`.** A gate spends [the_prompter]'s attention on a decision; a constant spends nothing and cannot be talked out of. Where a write is confined to one destination, never overwrites, is never read back, and lands in a folder already on the `%sync` EXCLUSION LIST, the gate has nothing left to protect and `ShipitGate` is satisfied by construction rather than by ceremony. THE BOUNDARY: this reasoning licenses a bounded destination, NEVER a bounded intent — whether a payload should have been exported at all remains Tier 2, and the containment says nothing about it. Applies to ANY unit that writes, ANY substrate, ANY domain. | Live test, 11 reconciled gates, 6/6 adversarial `output_failed` | [C]

SerThenWr | Any unit that WRITES — domain-agnostic law | ad-hoc %compose | 2026-09-06 | **THE LAW: serialize FULLY in memory, then write ONCE — a format failure caught mid-write leaves a partial file, and a partial file is a fabricated artifact under `FlFst`(Fail-Fast) never-mask.** THE DANGER IS THAT IT PASSES EVERY CHECK THE AI OS OWNS: the halt is correctly reported, the record is well-formed, the validator returns its verdict — and a truncated file sits on disk that no record mentions and no later reader can distinguish from a complete one. The unit halted honestly and still left a lie behind it, because the lie is on the filesystem and the record only describes the run. THE OPERATIONAL CONSEQUENCE: a write is not a streaming operation with a halt attached; it is one atomic act that either happens whole or does not happen at all. Every failure branch a writing unit declares must fire BEFORE the first byte is committed — an unserializable payload, an unsupported format and an unsafe name are all determinable without touching the destination. Sibling of `Tier1NotTruth` on the SIDE-EFFECT axis: that law says a well-formed record may describe a wrong structure, this one says a well-formed record may omit a wrong artifact entirely. Confirmed live: all three halt branches fired on a writing Captain and no partial file was left behind by any of them. Applies to ANY unit producing a file, ANY format. | Live test, 3 halt branches, zero partial artifacts | [C]

CmplLook | Any retrieval unit — domain-agnostic law | ad-hoc %compose | 2026-09-06 | **THE LAW: the dangerous retrieval is not the THIN one — it is the COMPLETE-LOOKING one.** A scope narrower than the page returns well-formed, abundant, plausible content that is MISSING exactly the region the mission needed, and every check the AI OS owns passes it: the fields are present, typed, non-null, verbatim and truthfully sourced. THE INSTANCE: a company page retrieved at an article-level scope returned a full body of marketing prose and silently dropped the footer carrying the address, phone and email a contact-gathering mission required; the same page at body scope returned all of it. Nothing was fabricated and no gate fired — the SCOPE did the omitting. THE OPERATIONAL CONSEQUENCE: `SuffNotVol`'s axis (c) NOT COVERING is not an edge case, it is the common case, and it is undetectable from length alone — a judgment layer comparing `content_length` against a threshold will pass this every time. **A retrieval is judged against a STATED mission need, never against its own size**, and where no mission need was supplied, sufficiency was not judged at all. Corollary: the scope report is as load-bearing as the text — a unit that returns content without naming what it scoped to has removed the only evidence this failure leaves. Applies to ANY retrieval unit, ANY substrate, ANY domain. | Live test, 2 URLs, scope compared at two levels | [C]

StaleSpec | Any unit under evaluation | ad-hoc %compose | 2026-09-06 | **THE LAW: a validator verdict names the CAPTAIN, never the FILE it read — so a superseded contract left at a live filename validates silently and reports `pass`.** THE INSTANCE: records were gated against a working copy of an ARCHIVED contract still sitting under the current filename; two adversarial records that the current schema rejects returned `pass`, and the verdict text was indistinguishable from a correct run. The defect was invisible in the output and was caught only because the pass rate looked wrong. THE DANGER IS THE DIRECTION IT FAILS: a stale schema is almost always LOOSER than the one that replaced it — that is why it was replaced — so the false verdict is a false PASS, never a false halt. This is `Tier1NotTruth` one level up: that law says a well-formed structure may be false, this one says a well-formed VERDICT may be about the wrong contract. THE OPERATIONAL CONSEQUENCE: **when a contract is rewritten or renamed, every copy of the old one is archived in the same action, and the archived copy is renamed so it can never be reached by the live path.** A `v1_` prefix is not tidiness; it is what makes the stale file unreachable by name. Applies to ANY unit whose spec is versioned. | Live test, verdict compared across two contract versions | [C]

ScopeObs | Any unit — domain-agnostic law | System-wide | 2026-08-19, hub-filed 2026-09-06 | **THE LAW: a unit may not be required to report what its own declared scope cannot observe.** A required field is a promise the unit can always keep; where the promise depends on what happened to be visible, the only routes to a `pass` are to fabricate the value or to halt on a correct run — and fabrication is forbidden outright by `FlFst`(Fail-Fast) never-mask, so the schema is what must change. THE TEST, run on every required output field before a contract ships: **name the mechanism by which this unit observes this value, every time, within its own declared scope.** If the mechanism is conditional on what rendered, what the runtime chose to expose, or what a sibling unit could have seen, the field is OPTIONAL and its absence is a fact, not a gap. WHY IT IS FILED HERE AND NOT IN A SPOKE: it names no unit and binds every domain — the hub's own test. THE SIBLING RELATION: `PartGate` says a required field must be an echoed input, a constant, a computed value, or a verbatim runtime report, never an observation whose truth can vary between two runs. That law governs VARIABILITY; this one governs REACHABILITY — a value can be perfectly stable and still lie outside the unit's scope to see. Together they are the complete admission test for a required field. | Live halt 2026-08-19, re-confirmed across four subsequent instances | [C]

CoerceNotFab | Any unit emitting a runtime-reported value | ad-hoc %compose | 2026-09-06 | **THE LAW: reshaping a value the runtime GAVE you is coercion; producing a value it did NOT give you is fabrication. The two look alike in a record and are opposite in kind.** THE INSTANCE: a tab handle typed `number` was rejected on valid runs because one browser returns an integer and another returns a token like `"seed"`. Typing the field `string` means the caller records the handle's string form — no information is invented, none is lost, and nothing downstream interprets it. Contrast the fabrication this library already forbids: appending a requested path to a reported origin to synthesise a landing URL, or naming a downloaded file the runtime never disclosed. THE TEST, and it is one question: **did the runtime hand me this information, in any form?** If yes, reshaping it to a declared type is legitimate. If no, the field is `null` and its absence is a fact (`ScopeObs`). THE DANGER THIS ENTRY EXISTS TO PREVENT: fabrication is always argued for as coercion. "I merely normalised it", "I only completed the obvious part" — the moment a value's SOURCE is the unit's own inference rather than the runtime's report, the never-mask rule of `FlFst`(Fail-Fast) binds regardless of how small the gap looks. A type is a shape; a value is a claim, and only claims can lie. | Live test, handle typed across two browser substrates | [C]

OutBandSig | Any unit awaiting an async completion | ad-hoc %compose | 2026-09-06 | **THE LAW: an OUT-OF-BAND completion signal beats an in-page one, because an in-page string competes with the very content it is waiting for.** THE INSTANCE: a generative app streamed its response into the page while the caller polled for an in-page marker; the marker's own words appeared mid-stream, so an in-page probe could fire early on a render that was still arriving. The tab TITLE mutated exactly once, at the moment the render finished, and gave a clean edge. Confirmed live: title `Google Gemini` -> a generated conversation title at 48s, while no in-page string fired cleanly. THE OPERATIONAL CONSEQUENCE: a `completion_signal` input should name an out-of-band condition wherever the target exposes one — a title change, a URL change, a control appearing — and a Colonel that supplies an in-page string is choosing the weaker probe. **This is the arrival-probe rule one stage later:** that one says probe AFTER paint rather than at navigation return; this one says probe on a channel the content cannot imitate. Both are the same failure — reading a signal that the thing being measured can produce by accident. A corollary that costs nothing: an out-of-band signal also survives a page whose content is an error or a refusal, where an in-page success marker never appears at all and the wait burns its whole budget. | Live test, generative app at an authenticated browser rung | [C]

WholeNotParts | Any Tier 2 judgment layer — domain-agnostic law | ad-hoc %compose | 2026-09-06 | **THE LAW: a judgment that checks only what the brief enumerated is a CHECKLIST, not a judgment — and it will pass an artifact that is incoherent in a way the brief never thought to forbid.** THE INSTANCE: a Colonel judged a generated image against the three properties its brief named, found one of them unmet, and rendered the correct verdict — while missing a grosser defect nobody had listed: the subject was looking at the BACK of the device whose screen the image was about. The scene was physically impossible and the judgment layer never asked, because it was busy inspecting the region the brief pointed at. The right answer was reached for the wrong reason, which is luck wearing rigour's clothes. THE MECHANISM, and it is the trap: enumeration FEELS like rigour. Every named property was checked, each check was correct, and the checking itself crowded out the one question a fluent viewer asks first — **does this thing make sense as a whole?** Zooming into the named region is the literal form of the error: attention narrowed to the specified detail and never widened again. THE RULE FOR ANY JUDGMENT LAYER: **read the whole artifact FIRST, in one pass, as its intended audience would — before checking any enumerated property.** Incoherence is a finding whether or not the brief forbade it, and a rationale that recites only the brief's own criteria has not judged, it has audited. Sibling of `SuffNotVol` on the JUDGMENT axis: that law says abundance is not sufficiency; this one says completeness of checking is not correctness of verdict. Applies to ANY Tier 2 layer, ANY artifact, ANY domain — an image is where it was found, not where it is bounded. | Live run, image judged correct on a listed criterion while an unlisted incoherence went unseen | [C]

# END `CORE` GENERIC AIOS PATTERN LIBRARY:

---
# %REM SWEEP LOG
*Global. This section exists in the HUB ONLY — spokes carry no sweep log.*

## CURRENT OPEN FINDINGS

### PRUNE CANDIDATES
Surface to (Chief of Staff)HANK for (the prompter)[the_prompter]'s review — source file named per entry ("cos_memory.md", "archive_manifest.md", or a named pattern-library file: hub or spoke). No writes to any file until `%shipit`.


### MANIFEST GAPS

### CROSS-FILE CONSISTENCY
