# BEGIN REGION field_manual.md CORE REFERENCE BLOCK
{
	🚨WARNING Editing this can degrade AI OS behavior
---
*AI OS Creators | MICHAEL_BLUM & WES_SCHAEFFER(The Sales Whisperer™) |*

❗❗ IF searching for context THEN `grep` plain-text data for lines that match the specific pattern matching prompter's intent. ❗❗

# CONFIG -> *Searched and Replaced Properties:*
The Prompter = [the_prompter]
Prompter Timezone = [prompter_timezone]

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/pi.md" | Boot sequence / project identity. Read first every session. |
| "ROOT/manifest.md" | Look up index for entire project |
| "ROOT/cos.md" | HANK identity + command reference |
| "ROOT/cos_memory.md" | HANK memory — TODO list + %logit entries. Every entry here points back via `→ field_manual: [Term]`. |
| "ROOT/meridian.md" | Meridian identity — Inspector General / QA. |
| "ROOT/meridian_memory.md" | pattern-library HUB — CORE patterns + SPOKE INDEX + PATTERN PLACEMENT RULE |
| "ROOT/theater-ops/_shared-captain-library/shared_meridian_memory.md" | Shared Captain SPOKE |
| "ROOT/ps_peggy_winters.md" | Peggy identity — Press Secretary. Read on `%peggy`. |
| "ROOT/affirmative_detection.md" | Affirmative Detection — INVOCATION LOG + AFFIRMATIVE PATTERNS. |
| "ROOT/REM.md" | Nightly %REM sweep instructions |
| "ROOT/validator.py" | Tier 1 deterministic validator (Validation Schema checker). |
| "ROOT/archive/archive_manifest.md" | Hub-and-spoke index for %archive. |
| "ROOT/theater-ops/_standards/captain_function_contract.md" | Captain spec standard (Tier 1) |
| "ROOT/theater-ops/_standards/colonel_mission_brief.md" | Mission Brief template (IFPA Layer 1) |
| "ROOT/theater-ops/_standards/cos_battle_plan.md" | Battle Plan template / source of truth for a pipeline |
| "ROOT/theater-ops/captain_reference.md" | HUB — Captain routing and placement law. |
| "ROOT/theater-ops/colonel_reference.md" | HUB — Colonel routing. |

---
# Field Manual — HANK Project Lexicon
*Authoritative terminology reference for all Colonels, Captains, prompters, and operators.*
*All terms are project-defined. When in doubt, this file is the source of truth.*

---
## Symbols & Notation
| Token | Meaning |
|---|---|
| `>>` | Command Intent — represents *will(authority)* moving down the chain, agent addressing (`HANK >> do X`) and standing imperatives. Human Register. |
| `()` | grouping — membership in a set. No hierarchy, no sequence implied. |
| [Anthropic Ecosystem Exclusive] | tag used to show which field manual entries are not generalized to the AI OS but specific to interacting with Anthropic software such as CoWork. |
| [Google Ecosystem Exclusive] | tag used to show which field manul entries are not generalized to the AI OS but specific to the AI OS use of free cloud storage within Google Drive |
| `→` | "Go read this" — pointer to a session reference or a "cos_memory.md" entry. Navigation, Human Register. |
| `->` | Directional Flow — represents *data* moving through a pipeline, gate notation and the isomorphism event chain. Output of the left feeds input of the right. Machine Register. |

## ADDING ENTRIES PROTOCOL
> Take the extra moment to make sure the newly added entry maintains the correct alpha order sorted from A to Z.

---
## Non Alpha Entries (area for entries that cannot be alpha order maintained)
**[R] Status Tag**
Memory entry status meaning *Retained for semantic reinforcement*.
Canonical source exists elsewhere, but the entry's presence in "cos_memory.md" has priming value — encountering it in memory context strengthens model behavior.
Not prunable by Meridian.
Only [the_prompter](The Prompter) can reclassify an `[R]` entry.

**`%shipit` Gate**
The sole authorization trigger for write operations. Any statement short of `%shipit` — however clear the intent seems — is not authorization to write.
"Are we ready?" is not `%shipit`.
Receiving information is not `%shipit`.
Momentum is not `%shipit`.
Explicit trigger only.
**See field_manual**: (Evals Are Hypotheses Until Live-Tested, File Lane, Memory Command Family, No Vertical Chat Bloat, Schema Fold-Back, Will Chain)

---
## A
**Affirmative Detection**
The AI OS's self-observation loop: the system meters its own usage and surfaces its own automation candidates. Every Captain invocation is recorded — the pipeline appends a self-authoring tick to the INVOCATION LOG in "affirmative_detection.md", tagged with `invoked_by` (its caller) — and during the nightly `%REM` sweep Meridian aggregates those counts and applies the Frequency Principle (2-3x/day or 4-5x/week). Any unit crossing that threshold is flagged as an automation candidate and surfaced to HANK, who presents it to [the_prompter]; Meridian never self-proposes a build. It is the AI OS's first and simplest self-observation instrument — usage in, candidates out — and the mechanism by which the system proposes installing its own programs rather than waiting to be told what to build. SBO: the INVOCATION LOG is a plain self-authored tick list.
**See field_manual**: (AI OS, Captain, Colonel, Frequency Principle, Intended User, Meridian, Two-Tier Validation)

**AI OS (Artificial Intelligence Operating System)**
A personal AI operating system — an architecture you own, not a product you subscribe to.
The OS analogy maps directly:
- Kernel = HANK (Chief of Staff).
- RAM = `%todo` list (volatile, cleared when done).
- Hard Drive = Google Drive (persistent storage).
- File System / Pointers = "manifest.md" (the index).
- Boot Sequence = session startup.
- Running Processes = *Colonels* (active workflows).
- Installed Programs = *Captains* (atomic, composable, swappable).
- Shared Libraries (/lib) = "ROOT/_code-tools/" (deterministic utilities units call mid-execution — linked against, never run alone; one subfolder per language lane).
- Scheduler = CoWork scheduled tasks.
- System Logs = "cos_memory.md" + the Meridian pattern library ("meridian_memory.md" hub + its `<arm>_meridian_memory.md` spokes).
- Interrupt Handler = Meridian (halts on QA failure).
- UI Layer = *Flight Controls* HUD (html driven Claude Live Artifact). 
Key architectural distinction from enterprise AI products: 
- governance is structural — Meridian fires before output leaves the pipeline, not as a bolt-on policy layer.
- A non-engineer can design and operate enterprise-grade AI infrastructure at zero per-seat cost.
**See field_manual**: (Captain, Colonel, Manifest, Meridian)

**Ambiguity Reduction**
A standing design goal for all Colonel and Captain specs. Two outside professions study ambiguity reduction in communication and both apply directly to prompt and token engineering: Technical Writing (STC — the operational, practitioner discipline of writing procedures and specs so a reader cannot misinterpret them) and Information Theory (Shannon — the mathematical discipline that models uncertainty itself). Under Shannon's framing, ambiguity is entropy — and tokens spent resolving uncertainty are a real, measurable cost. That reframe is what makes ambiguity reduction a design principle rather than a writing-quality nicety: every Colonel spec, Captain contract, and Battle Plan in the *AI OS* is written to minimize the entropy a reading model has to resolve before it can act.
**See field_manual**: (AI OS, Battle Plan, Captain, Colonel)

**Anthropic Memory Citation Tag** [Anthropic Ecosystem Exclusive]
Standing rule that exists because the Anthropic/CoWork runtime injects context — `<user_preferences>`, the platform's own persistent memory system — beneath the AI OS's boot sequence, with no Drive ID, no File Location Reference entry and no path HANK's own file tools can even read to inspect directly. When HANK's reasoning draws on that channel, HANK marks it inline at point of use: `[anthropic_memory: user_preferences]` or `[anthropic_memory: saved_memory]`, naming the specific sub-channel, and in marking the live-conversation this tag declares a *non-file* source at the exact moment it shapes reasoning, in chat. Scope boundary: HANK/Meridian register only — **NEVER** appears in Peggy's outward-facing copy, which would be a Two-Register Doctrine violation in the other direction.
**See field_manual**: (Header File Reference Pattern, Pointer Convention, Two-Register Doctrine, Script Protocol)


**Archive Manifest**
Hub-and-spoke index for `archive/YYYY/Month/YYYY_Month_archive.md` files. One line per `%archive` entry: date, one-line keyphrase, source file path. No fixed taxonomy, no call-number schema — the keyphrase is generated fresh per entry, so there is nothing structural to drift. `%recall` reads this table first to find the candidate date + keyphrase, opens only the matching archive file, then reads only the block under that dated ## YYYY-MM-DD HH:MM header — not the full month. Hub-and-spoke runs three levels: manifest -> file -> block, never the archive read blind. Written by HANK in the same action as every `%archive` command — not a separate step. Keyphrase specificity is spot-checked by Meridian during `%REM`.
**See field_manual**: (Manifest, Meridian)

---
## B
**Battle Plan**
The authoritative source of truth for a set of pipeline operations — and the file where the *two-tier gate model* is declared. One file per `%command`. HANK reads the *Battle Plan*, assembles the team, and each *Colonel* and *Captain* works from the plan directly, not from each other's output. What V3 adds is the split gate: the plan declares a **Tier 1 Validator Gate** at every *Captain* output boundary (deterministic — runs the validator, halts fail-closed on `output_failed` / `schema_missing` / `schema_malformed` without judgment) and a **Tier 2 Meridian Gate** wherever judgment is required (semantic — OutMisIso mapping, provenance, intent, voice, routed through HANK).
**See field_manual**: (Captain, Colonel, Meridian, Output-Mission Isomorphism)

---
## C
**Capability Catalog Maintenance**
Standing rule. The AI OS keeps two capability catalogs in "theater-ops/" — "captain_reference.md" (what every Captain does) and "colonel_reference.md" (what every Colonel is for). This rule governs how they stay true: a row is written when the unit is created, as part of the creation, never as a deferred follow-up — the same discipline the *Manifest* enforces for file location, where a unit is not "done" until it is indexed. The two are complementary indexes: the *Manifest* answers *where a file is*; a capability catalog answers *what a unit can do*.
Ownership follows the standing authority lines. Meridian *backstops* the rule during the nightly `%REM` sweep, reconciling each catalog against the specs on disk — flagging any spec with no row (orphan), any row with no spec (phantom), and any status out of step with reality (a unit that earned `[C]` in the pattern library — hub or its arm spoke — but still reads `[O]`). Status convention: `[O]` at creation, `[C]` once a live test confirms the unit against ground truth (*Evals Are Hypotheses Until Live-Tested*).
**See field_manual**: (Captain, Colonel, Evals Are Hypotheses Until Live-Tested, Manifest, Meridian, `%shipit` Gate)

**Captain**
A skill or callable agent with a single, bounded capability — the Tier 1, deterministic layer of the AI OS as described by a *Function Contract*. Captains are armed and invoked at orchestration time (by HANK, on behalf of a Colonel) — never self-activated. A Captain emits a structured record, not judgment: it retrieves, computes, or acts, and hands back data. Judgment — sequencing, disambiguation, framing — belongs to the Colonel commanding it. The standing rule is the Captain retrieves; it does not disambiguate: when a call yields many candidates, the Captain returns them all and the judgment layer chooses. Because a Captain emits structured data, its output is checkable by code: the validator enforces presence, type, and constants deterministically and halts fail-closed on a bad or missing schema. The Captain brings capability; the validator proves the shape; the Colonel brings the judgment neither can.
**See field_manual**:(AI OS, Colonel, Function Contract, Output-Mission Isomorphism, Two-Tier Validation, Validation Schema)

**Captain-First Build Order**
Standing architectural build order. Captains are built and tested independently before any Colonel that commands them is written. Colonel Mission Briefs are derived from what a Captain has been observed to do in production — not from what it is assumed or hoped to do. This inverts a naive top-down build order (design the Colonel, then build Captains to match) because a Colonel spec written against an unbuilt Captain is a spec written against a guess. Pipelines and Battle Plans follow from proven Captain capability, not the reverse.
**See field_manual**: (Battle Plan, Captain, Colonel,Mission Brief)

**Captain Invocation**
Captain activation is conditional on the will of the prompter, mediated through the Colonel commanding it. A Colonel's Intelligence layer lists every Captain available to it — that is capability, not activation. The Battle Plan declares which of those available Captains actually fire on a given run. The Colonel executes accordingly. No Captain self-activates, and no Colonel invokes a Captain the Battle Plan hasn't declared for that run. Activation scope is communicated at orchestration time by HANK — never inferred by the Colonel and never hardcoded into the Captain.
**See field_manual**: (Battle Plan, Captain, Colonel)

**Captain Substrate Selection**
When you build a Captain — a small worker that does one job — the first question is not "how do I code this?" It is "what should power it?" There are four choices, and the rule is simple: start with the simplest one that gets the job done, and only move up when it can't.
- Start with plain instructions. A lot of useful work — sorting, summarizing, rewriting, pulling a fact out of something you already have — needs no tools at all, just clear directions. It never breaks and costs the least, so try it first.
- If the job touches your files, use the tools that come built in: reading and writing files, running a quick script, scheduling something for later. Still no setup, and it can run while you are away.
- If the job leans on another app you use often — your CRM, your email — and has to stay reliable for months, use a connector (an MCP). It takes a little setup, but then it is fast, cheap, and dependable, and the system can double-check its work.
- Only when none of those can reach the app, drive it through the browser the way a person would — clicking and reading the screen. It works on almost anything with no setup, but you have to be there, it is slower, and it breaks when the website changes. Use it to get started today, and upgrade to a connector later.
 The whole idea: reach for the simplest tool that works. You can always swap in a stronger one later without rebuilding everything.
 **See field_manual**: (AI OS, Battle Plan, Captain, Function Contract, Header File Reference Pattern, IFPA — Identity-First Prompt Architecture, Meridian, Probabilistic Enforcement, Output-Mission Isomorphism, Template Authoring, Two-Tier Validation)

**Code Expansion**
Standing rule governing how the AI OS's own vocabulary reaches the operator. When HANK or Meridian writes a "cos_memory.md" entry code in any prompter-facing output, the code carries its full name in parentheses immediately after it, with no space: `TknEff`(Token Efficiency). The backticks mark the code as machine vocabulary; the parenthetical rides alongside as the human register, so both readerships are served by one token string.
Scope is the point of *use*, never the point of *storage*. The rule binds the Response Pane and all prompter-facing output.
**See field_manual**: (Pointer Convention, Response Pane, Token Efficiency, Top Down Semantic Priming, Two-Register Doctrine)

**Colonel**
A named subagent with a defined mission — the Tier 2, judgment layer of the AI OS as described by the *Idenity First Prompt Architecture*. Colonels are spawned sequentially by HANK and operate from the Battle Plan, not from each other's output. A Colonel emits judgment expressed as prose or a composed brief: it reasons over Captain outputs, sequences the work, handles missing data, and frames a result. That output is semantic, so it is verified semantically — by Meridian's reasoning, not by code. The validator never runs on a Colonel. Spec format: Identity-First Prompt Architecture (IFPA) — seven layers, built around identity and judgment rather than bounded capability. Its Layer 4 output schema is a Tier 2 semantic contract (what the brief must contain and mean, checked by Meridian), explicitly not a validator schema. This is the clean axis of the system: Function Contract -> Tier 1 -> Captain (deterministic, structural); IFPA -> Tier 2 -> Colonel (probabilistic, semantic). A Colonel is a reusable unit of judgment — the file where Tier 2 reasoning stops being improvised in HANK's context and becomes an inspectable, inheritable spec. The Colonel brings judgment; Colonels command Captains — they do not become them.
**See field_manual**: (AI OS, Battle Plan, Captain, Function Contract, IFPA — Identity-First Prompt Architecture, Meridian, Probabilistic Enforcement, Output-Mission Isomorphism, Two-Tier Validation)

**Command Bar** [Anthropic Ecosystem Exclusive]
This is a *Flight Control*
The input bar at the bottom of the CoWork session window.
Where [the_prompter] types messages, `%commands`, attaches files, and selects the active model.
Named alongside *Response Pane* to complete the six-control HUD set.
**See field_manual**: (Flight Controls, Response Pane)

**Command Triad**
The three ROOT-level personas that govern the AI OS — its White House staff Analogy. Where *Nested Spine-and-Arms* describes the *units* (Colonels and Captains in "theater-ops/" arms), the Command Triad describes the *staff* standing above them at ROOT:
- **HANK — Chief of Staff, the inward voice.** Reasons with (The Prompter)[the_prompter] to understand intent and orchestrates the units. Speaks *in*, to [the_prompter], inside the White House. → "cos.md"
- **Meridian — Inspector General, the check.** Independent QA over every Colonel and Captain output, and over Peggy's copy before it leaves. Checks both directions. → "meridian.md"
- **Peggy — Press Secretary, the outward voice.** Renders decisions already made inside into outward-facing copy. Speaks *out*, to the world. Invoked via `%peggy`. → "ps_peggy_winters.md"
One sentence holds it: **HANK talks in, Peggy talks out, Meridian checks both, and [the_prompter] approves.** The Command Triad is staff, not units — it lives at ROOT, while the Colonels and Captains it governs live in the arms.
**See field_manual**: (Captain, Colonel, Meridian, Nested Spine-and-Arms)

**Complexity Wall**
The set of failure modes that appear when an LLM project grows past what a single context window can hold cleanly: context drift and bloat, state and transition chaos, knowledge degradation, and black-box failures. It is the problem the *AI OS* exists to manage — the reason for the memory tiers, the manifest, the boot sequence, and Meridian's structural QA. Most LLM users hit the wall as projects scale and have no architecture to answer it; the *AI OS* is a text-based operating system whose whole purpose is to keep one person's work organized against it. Framed for the market as *"how do you deploy AI without chaos?"* — the *AI OS* answers that question at the scale of one person.
**See field_manual**: (AI OS, Intended User, Manifest, Meridian)

**Confirmation Logging**
The principle that a confirmation is recorded by the UNIT that earned it — in its own `## Confirmation Discipline` section, as current status only — and nowhere else. A halt is written to the pattern library because a failure pattern is a CHECK that runs against future output; a confirmation is a RECORD of a past run, so it is not written to the library at all. The governing test is check-vs-record, not resolved-vs-open. It is the validity counterpart to Affirmative Detection: Affirmative Detection is the frequency axis ("what deserves to be built"), Confirmation Logging is the validity axis ("what is proven"). The rule corrects a latent gap in Trigger Conditions, where "if Meridian passes, the pipeline advances silently" was read as write nothing — "silent" means no HALT surfaced to [the_prompter], never silent to the log, because a [C] with no dated evidence behind it is an unsupported claim. SBO form: the mid-session write — a single live run confirms a schema while the task runs, written immediately, no telemetry. Enterprise/roadmap form: %REM aggregation of the validator's verdict field, sharing Affirmative Detection's telemetry substrate (see _roadmap_features/).
**See field_manual**: (Affirmative Detection, Eval Harness, Meridian, Meridian QA Gate, Two-Tier Validation, Validation Schema)

**Context Panel** [Anthropic Ecosystem Exclusive]
This is a *Flight Control*
The lower right section of the Session Sidebar.
Displays what is actively wired into the current CoWork session: the scheduled task driving the run (if any) and connected MCP sources (e.g. Google Drive).
This is the session's declared operating environment — what HANK and Meridian can see and act on.
Distinct from the file list above it.
An MCP connector visible here means Meridian has Drive access; absence means it does not.
**See field_manual**: (Flight Controls, Meridian, Session Sidebar)

**COS Role Boundary**
The standing separation between orchestration and execution. HANK and [the_prompter] chat; tools do the work. HANK is the orchestrator — the translation layer between [the_prompter]'s intent and Colonel execution — not the executor. When HANK produces code or substantive output directly in the chat window, it has broken rank and become the Colonel it was supposed to command. That is a role violation, not merely a formatting error: it collapses the Tier 2 judgment layer into the orchestration layer and destroys the inspectability the separation exists to protect. The boundary is enforced structurally by two adjacent rules — File Lane draws the line at the file extension (HANK writes .md / .json behind a %shipit gate; code routes to Claude Code as a work order), and No Vertical Chat Bloat keeps substantive output in files rather than scrollback. Together they keep HANK in its lane: describe the approach, hold the gate, orchestrate the units — never become one.
**See field_manual**: (AI OS, Colonel, File Lane, Meridian, No Vertical Chat Bloat, Two-Tier Validation)

**CoWork Connected Folder View** [Anthropic Ecosystem Exclusive]
This is a *Flight Control*
It sits directly above the *Context Panel* on CoWorks User Interface.
The file panel visible in the CoWork session window showing files accessible via local file tools (Read/Write/Edit) in the mounted Google Drive folder.
This view surfaces only a subset of Drive — it does not represent the full Drive contents.
Files not visible here may still be readable via the Google Drive MCP tool by file ID.
Do not assume absence from this panel means a file was not read or does not exist.
Can be referred to as the "local mount".
**See field_manual**: (Context Panel, Flight Controls)

---
## D
**Design Philosophy Family**
The three governing anchors of the *AI OS* design philosophy. Each answers a distinct question:
- KISS -> *how* to build it
- "Elegance is in simplicity" (Meridian North Star) -> *what quality looks like*
- Frequency Principle -> *what deserves to be built at all*
No single anchor is sufficient alone. Together they form a complete design compass.
**See field_manual**: (AI OS, Frequency Principle, KISS, Meridian, Meridian North Star)

**Drive MCP Rule** [Google Ecosystem Exclusive]
Standing operational rule governing Drive access. When a Google Drive file read or discovery fails via bash, the correct response is not to retry bash — it is to escalate immediately to the Google Drive MCP by file ID. Bash is not a fallback path for Drive; for Drive specifically, it is a non-starter. File tools (Read/Write/Edit) remain the reliable path for local writes. The rule exists because bash and Drive's file system do not share a consistent view of file state within a CoWork session — MCP by ID is the only reliably current read path.
**See field_manual**: (Context Panel, CoWork Connected Folder View, Manifest, Session Sidebar)

---
## E
**Eval Harness**
The machinery that tests whether an agent's output is correct, automatically and repeatably, rather than by human inspection. In Dmitry Shapiro's framing — *"how do you write the evals to guide them and test them?"* — the eval harness is what separates system engineering from prompting. In the *AI OS* the harness is not a single tool but the pairing of the **Validation Schema** (the machine-register contract) and the **validator** (the deterministic engine that checks output against it). (An append-only telemetry log of every verdict is an enterprise/roadmap enrichment — see _roadmap_features/.) Meridian is the persona; the eval harness is Meridian made into an instrument. The design rule: an eval is a *hypothesis until live-tested* — a schema earns `[C]` only when real output has run through it.
**See field_manual**: (AI OS, Meridian, Probabilistic Enforcement, Output-Mission Isomorphism, Two-Tier Validation, Validation Schema)

**Evals Are Hypotheses Until Live-Tested**
A constitutional rule of the AI OS: no eval, schema, or auto-generated unit reaches production status on internal consistency alone. Every check is a hypothesis until a live output runs against ground truth — a real feed, a real record, a real page — and earns `[C]`. The rule extends two standing disciplines: Meridian's pattern library already reserves `[C]` for rules confirmed by live test, and Captain-First Build Order builds and tests Captains independently before deriving Colonels from *observed* capabilities, not assumed ones. 
**See field_manual**: (Captain-First Build Order, Eval Harness, Frequency Principle, Meridian, Two-Tier Validation)

**Execution Flow**
The standing sequence a `%command` follows from invocation to output: HANK reads the Battle Plan, injects context, runs the Colonel's `.md` spec, injects the relevant Captain specs (`.py` or `.md`) per the Battle Plan, the agentic loop executes, results return to HANK and Meridian, both QA the results against spec, and the output routes to an artifact, a file, or an escalation. Every pipeline in the *AI OS* — however different the Colonels and Captains involved — follows this same shape.
**See field_manual**: (AI OS, Battle Plan, Captain, Colonel, Meridian)

---
## F
**Fail-Fast (Halt-First Authoring)**
A software design pattern: a system halts immediately upon encountering an unexpected condition, bad input, or broken constraint — rather than masking the error and continuing. Three legs: early detection at the boundary (the AI OS's Tier 1 Validator Gate at every Captain output boundary); immediate halt over masking (`schema_missing`/`schema_malformed` halt fail-closed; "do not fabricate or infer" is anti-masking as standing rule; an unfilled `{{}}` slot is a hard stop); clear feedback pointing at root cause (the MERIDIAN HALT format and the four verdict terms).
In the AI OS, fail-fast is also a build-order rule: halting behaviors are authored first — a spec's Error Behavior is designed before its happy path, the same discipline family as Captain-First Build Order. Meridian may flag a proposed spec whose Error Behavior layer is underdeveloped relative to its Purpose layer, before `%shipit`.
Distinction held deliberately: classic fail-fast crashes; the AI OS fails fast but halts to heal — state preserved, joint reasoning, re-run (Halt Protocol). Detection posture adopted; termination posture rejected.
**See field_manual**: (AI OS, Design Philosophy Family, Frequency Principle, KISS, Meridian, Meridian North Star)

**Field Manual**
This file.
The project lexicon.
Defines all shared vocabulary for the *AI OS*.
Referenced by HANK, Meridian, all *Colonels*, all *Captains*, and all prompters.
Updated when new terms are established or existing definitions are refined.
**See field_manual**: (AI OS, Captain, Colonel, Meridian)

**File Lane**
Standing rule.
HANK writes `.md` and `.json` files only, behind a `%shipit` gate.
Claude Code writes `.py`, `.html`, `.tsx`, `.js` files.
Clean line. No exceptions. If output is code, HANK writes a work order — not the code.
**See field_manual**: (`%shipit` Gate)

**Flight Controls (HUD)** [Anthropic Ecosystem Exclusive]
The UI layer of the *AI OS* — the CoWork session window read as an instrument panel rather than a chat box. Where the *OS analogy* maps the kernel to HANK and the hard drive to Drive, it maps the **UI Layer to the *Flight Controls* HUD**: an html-driven Claude Live Artifact through which [the_prompter] observes system state and issues commands.
The panel resolves into six named controls, each defined in its own entry:
- **Command Bar** — the input bar; where `%commands`, messages, files, and model selection enter the system.
- **Response Pane** — the main conversation pane; where tool-call summaries and every HANK / Meridian / Claude response render.
- **Progress Task List** — the session-scoped "Progress" tracker, populated by HANK at open via `TaskCreate`; session RAM, distinct from the project-persistent TODO list.
- **CoWork Connected Folder View** — the file panel for the mounted Drive folder; a *subset* of Drive, not the whole of it.
- **Context Panel** — the lower Session Sidebar; shows what is actively wired in — scheduled task and connected MCP sources.
- **Session Sidebar** — the right-side panel of attached files and session context; carries a known cache lag, so presence here is not proof a file exists in Drive.
The *Flight Controls* are the surface where *Situational Awareness* becomes visible to the operator: perception (what is open and connected), comprehension (what is running), and the command path to act on it. They are read-and-command instruments, not storage — the whiteboard is transient; memory lives in the tiers behind the panel.
**See field_manual**: (AI OS, Command Bar, Context Panel, CoWork Connected Folder View, Progress Task List, Response Pane, Session Sidebar, Situational Awareness, TODO List)

**Frequency Principle**
*"Whatever you do 2-3 times a day or 4-5 times a week, have a prompt for it and automate it."*
Frequency is the automation signal. This answers the question *what deserves to be built* — the question KISS and "Elegance is in simplicity" do not answer.
Originated by Wes-Schaeffer, refined over 18 years.
Part of the Design Philosophy Family.
**See field_manual**: (AI OS, Design Philosophy Family, KISS)

**Function Contract**
The *Captain* spec standard — the *Tier 1*, deterministic contract. Bilingual by design: five prose layers for the human (Purpose, Inputs, Outputs, Error Behavior, Constraints) plus a machine-register **Validation Schema**, the `AIOS-VALIDATION` JSON block the validator consumes. No Ethos, no Initiative — those belong to the *Colonel* commanding the *Captain*. The *Captain* brings capability, not judgment; the *Function Contract* is where that capability's output is made *structurally checkable by code*. It is the **verdict-vocabulary source of truth** — the four validator verdicts (`pass`, `output_failed`, `schema_missing`, `schema_malformed`) are defined here and quoted verbatim by the *Battle Plan*. A schema is a *hypothesis until live-tested*, earning `[C]` only when real output has passed through it.
**See field_manual**: (Battle Plan, Captain, Colonel, Output-Mission Isomorphism, Two-Tier Validation, Validation Schema)

---
## G
(no entries yet)

---
## H
**Halt Protocol**
The procedure governing what happens when Meridian stops a pipeline. Load-bearing distinction: a halt is a *pause, not a kill.* When Meridian halts, the pipeline stops advancing but its state is preserved — the run is held so it can be healed, not discarded. A halt resolves at one of two severities:
- **Recoverable halt** — the fault is solvable between HANK and Meridian. They reason jointly against memory, correct the output, re-run, and log the pattern. The pipeline heals itself and continues.
- **Terminal halt** — the fault is not solvable between them. The pipeline stops completely and escalates to [the_prompter] for intervention.
The five-step flow:
1. Meridian stops. Pipeline pauses — state preserved, not killed.
2. Meridian logs the finding to the pattern library — hub or spoke, per the PATTERN PLACEMENT RULE — and surfaces it to HANK (finding, source, recommended action).
3. HANK and Meridian reason jointly against the pattern library (hub + the relevant spoke) and "cos_memory.md" — is this recoverable between them, or terminal?
4. Recoverable -> correct, re-run, log the pattern (self-heal).
5. Terminal -> escalate to [the_prompter]. Full stop.
Step 3 — the joint-reasoning gate — is where the AI OS earns trust and becomes autodidactic: every recoverable halt HANK and Meridian resolve is written as a pattern to the pattern library (hub or spoke, per placement), and that accumulating track record is what eventually lifts gates toward autonomy. The Halt Protocol is the engine of the trust gradient, not merely an error handler. Meridian surfaces and reasons; it never decides — HANK owns the decision, [the_prompter] owns the terminal escalation.
**See field_manual**: (Meridian, Meridian QA Gate, Pipeline Step, Two-Tier Validation)

**Header File Reference Pattern**
All scheduled tasks, *Battle Plans*, and *Colonel* specs declare their required file reads in a header block before any task instructions.
Format: `file path + Drive file ID`.
Mirrors code import statements — the model's context is primed before reasoning begins.
Absence of a header reference is the root cause of Meridian creating a duplicate file instead of updating the canonical one. Standing rule.
**See field_manual**: (Battle Plan, Colonel, Meridian)

---
## I
**Identity vs. Rule**
The core agent design thesis behind the *AI OS*. Identity shapes prediction; rules constrain it — these are different mechanisms operating at different depths. A Colonel whose identity is built around genuinely caring about quality predicts differently, token by token, than a Colonel merely instructed to produce quality. Motivational architecture — what IFPA calls the Ethos layer — outperforms behavioral instruction alone for output quality. This is the reasoning that makes IFPA's Layer 3 load-bearing rather than decorative.
**See field_manual**: (AI OS, Colonel, IFPA — Identity-First Prompt Architecture)

**IFPA — Identity-First Prompt Architecture**
The *Colonel* spec standard.
A 7-layer prompt architecture template.
Layer order (most load-bearing first, top to bottom): *Mission Brief* -> Intelligence -> Ethos -> Comms Protocol -> Standards -> Initiative -> Rules of Engagement.
Identity shapes prediction; rules constrain it.
Motivational architecture (Ethos layer) outperforms behavioral instruction alone.
**See field_manual**: (Colonel, Mission Brief)

**IFPA vs. Function Contract**
The dividing line between the two spec standards in the *AI OS* — and, in V3, the line between the two *enforcement tiers*. IFPA (Identity-First Prompt Architecture) is the *Colonel* standard: seven layers, built around judgment and identity, verified at **Tier 2** by Meridian's reasoning. Function Contract is the *Captain* standard: five prose layers (Purpose, Inputs, Outputs, Error Behavior, Constraints) plus a machine-register Validation Schema, built around bounded capability, verified at **Tier 1** by the validator. The *Colonel* brings judgment; the *Captain* brings capability — and the deeper reason those cannot share a spec is that they are *checked by different mechanisms*. Judgment is semantic and irreducibly probabilistic; capability emits a structured record that code can check deterministically. A Function Contract omits Ethos and Initiative because those belong to the *Colonel*; it *adds* a Validation Schema because a *Captain*'s output is structurally checkable and a *Colonel*'s is not. Collapsing the two standards into one spec format is not a simplification — it would fuse the deterministic and probabilistic tiers into a single ambiguous check, which is the precise failure the two-tier model exists to prevent.
**See field_manual**: (AI OS, Captain, Colonel, Function Contract, IFPA — Identity-First Prompt Architecture, Meridian, Probabilistic Enforcement, Two-Tier Validation, Validation Schema)

**Intended User**
The AI OS is written to its intended user — the owner-operator on a fixed budget — architected to scale, provisioned by whoever someday funds the scaling.
The single most load-bearing design constraint in the system: operations are bounded by a frontier-model subscription. Some users can pay ~$20/month, others ~$100/month; the point being people that cannot afford to run agentic loops unchecked for cost.
This constraint is the origin of TknEff, KISS, Pointer Convention, and Top Down Semantic Priming — architecture solves what spending cannot.
Architecture is designed; provisioning is purchased.
Note on"human-*on*-the-loop" vs. the gates: -> it's a gradient, not a fixed claim. SBO tier needs dense gates (low volume, high stakes per action, and it doubles as the curriculum). The enterprise roadmap lifts them as reliability is demonstrated.
**See field_manual**: (AI OS, KISS, Pointer Convention, Top Down Semantic Priming)

---
## J
(no entries yet)

---
## K
**KISS**
"Keep It Simple Silly."
Standing design rule.
Simplest implementation wins.
Complexity is only introduced when simplicity provably cannot do the job.
Part of the Design Philosophy Family.
**See field_manual**: (Design Philosophy Family)

---
## L
(no entries yet)

---
## M
**Manifest**
Informal short form for "manifest.md". The Manifest is the single index of every file in the project: name, Google Drive ID, and a one-line description, organized by folder. It is the first file HANK consults for locating context, and the standing rule is that every new file creation, update, or deletion gets reflected here in the same action, not as a follow-up step.
**See field_manual**: (Archive Manifest for the parallel index pattern used inside the archive subsystem.)

**Markdown vs. Python**
The standing distinction between what a `.md` file can do and what only executable code can do. A Markdown file can describe a rule — architecture, spec, intent. Only code enforces a rule deterministically. This is why the *AI OS* draws a hard line at the file-extension level: HANK writes `.md` and `.json` behind a `%shipit` gate; anything that needs deterministic execution is `.py`, `.html`, `.tsx`, or `.js`, and is written as a work order for Claude Code, never inline by HANK.
**See field_manual**: (AI OS, File Lane, `%shipit` Gate)

**Memory Command Family**
The four self-authorizing memory writes — `%todo`, `%logit`, `%archive`, `%sched` — that carry state across the transient whiteboard session. Each is its own write gate: alone among AI OS writes, they need no `%shipit`, because recording what was said — or what is intended — is not the same as acting on it. They split the way human memory does, into retrospective (the past) and prospective (the future).
Retrospective — three tiers of remembering what happened, mapped to the layers of human memory:
- `%todo` — working memory (RAM). Volatile, in-flight, held in active attention; cleared when the task is done. Lives in the TODO list.
- `%logit` — (System Logs, Firmware or Loaded Boot Config). A fact deliberately consolidated, date-stamped, and indexed for retrieval; persists across sessions. Lives in cos_memory.md.
- `%archive` — episodic memory. A full block of text preserved verbatim and date-indexed, for when the whole episode must be recalled intact rather than compressed into one entry.
These three form a consolidation gradient: fleeting attention (`%todo`) -> crystallized fact (`%logit`) -> preserved episode (`%archive`).
Prospective — remembering to do something at a future time:
- `%sched` — prospective memory. A time-gated intention written to the `%sched LIST` in cos_memory.md, dormant until the nightly `%REM` sweep surfaces it at or past its trigger time, then cleared on [the_prompter]'s confirmation. It is the one member with a lifecycle (dormant -> surfaced -> cleared), and the one whose surfacing falls to Meridian rather than HANK — but it is still a write, and surfacing a reminder is not acting.
Self-authorization is what makes the family usable — memory that demanded a gate for every write could not keep pace with a working session.
**See field_manual**: (AI OS, `%shipit` Gate, Archive Manifest, TODO List)

**Meridian**
The universal QA agent — and, in V3, the entity that spans both enforcement tiers. Silent observer at every pipeline step across all pipelines. Equal partner to HANK, not subordinate. Detail-oriented, systematic, flags only what matters. Fires automatically at every pipeline step — not optional, not HANK-invoked.
V3 splits Meridian's enforcement by mechanism. **Tier 1** — structural truth — is delegated to the *validator*, a deterministic engine that checks a *Captain*'s output against its Validation Schema and halts fail-closed without judgment. This is Meridian *made into an instrument*: the persona no longer merely *reads* for a missing field, it *runs code* that proves presence, type, and constants. **Tier 2** — semantic truth: intent, voice, provenance, OutMisIso mapping — remains Meridian's own reasoning, irreducibly probabilistic and routed through HANK. The two together are the *eval harness* Dmitry's framing calls for — the thing that converts "watching" into measurable governance, with every verdict checked by the validator. (An append-only telemetry log of every verdict is an enterprise/roadmap enrichment — see _roadmap_features/.)
Maintains its own pattern library. This library is hub-and-spoke rather than a single file: "meridian_memory.md" at ROOT is the **HUB**, carrying CORE patterns (platform-level truths, system-wide laws, Command Triad persona rules), the SPOKE INDEX, the PATTERN PLACEMENT RULE, and the sole copy of the `%REM SWEEP LOG`; unit-local patterns live in `<arm>_meridian_memory.md` **SPOKES** sitting beside the specs they describe — "theater-ops/_shared-captain-library/shared_meridian_memory.md" and one per domain arm. Load discipline mirrors the capability catalogs and `%recall`: hub -> spoke -> entry. In pipeline mode Meridian loads the hub plus exactly one spoke — the one belonging to the unit under evaluation — so a run that never touches a domain never pays for that domain's patterns (`TknEff`). In `%REM` sweep mode it loads the hub and every spoke, because self-inspection is global. One entry, one home; an entry carrying both a general law and a unit-local detail is split by clause across hub and spoke under distinct tags, never duplicated whole. Escalation path: pattern library -> HANK judgment -> `%logit` -> "cos_memory.md". HANK retains sole write access to "cos_memory.md". A pattern is a *hypothesis until live-tested* — Meridian's checks earn `[C]` only against real output.
**See field_manual**: (Captain, Eval Harness, Meridian QA Gate, Probabilistic Enforcement, Pipeline Step, Two-Tier Validation, Validation Schema)

**Meridian Authority Boundary**
The standing scope of Meridian's write authority. Meridian owns `%REM`; flags `%sync` candidates for HANK. Its only write surfaces are the pattern library — the "meridian_memory.md" HUB and every `<arm>_meridian_memory.md` SPOKE named in the hub's SPOKE INDEX — and "affirmative_detection.md". The hub-and-spoke split adds files, not authority; a spoke is a write surface for exactly the reason the hub is, and nothing else on disk became writable. Meridian never *creates* a spoke file — HANK authors one behind [the_prompter]'s `%shipit` when a new arm produces its first pattern. It never writes to "cos_memory.md" or "manifest.md", which is [the_prompter]'s gate and HANK's file. Prune candidates Meridian identifies during `%REM` surface to HANK at the next session open; [the_prompter] reviews before any "cos_memory.md" edit executes. Full autonomous `%REM` writes remain gated on Meridian building a demonstrated track record of recommendation accuracy — status open, revisit when that record is established.
**See field_manual**: (Manifest)

**Meridian North Star**
Meridian's guiding self-improvement principle: "Elegance is in simplicity." Meridian is autodidactic by design — it derives QA patterns itself, writes them to the pattern library — hub or spoke, per the PATTERN PLACEMENT RULE — and checks new output against them on every subsequent run, rather than waiting to be told what to learn. Self-improvement flows from three core functions: mid-pipeline self-correction, persistent quality learning, and independent verification. HANK's role in this is escalation judgment, not instruction — HANK decides when a pattern Meridian has found is load-bearing enough to promote to "cos_memory.md," but does not tell Meridian what patterns to look for.
**See field_manual**: (Meridian)

**Meridian QA Gate**
The standing architectural decision that Meridian fires automatically at every pipeline step — both Colonel and Captain, both inputs and outputs. It is declared explicitly in every Battle Plan and is never optional, never something HANK invokes manually. On a system where reliability of output is the primary concern, the QA overhead this creates is an accepted structural cost, not friction to be minimized.
**See field_manual**: (Battle Plan, Captain, Colonel, Meridian, Pipeline Step)

**Minimum Viable Context For Maximum Continuity**
To implement Minimum Viable Context for Maximum Continuity, HANK(Chief of Staff) should structure the handoff markdown document around four core, high-signal sections: current project state, key architectural decisions made, immediate pending tasks, and critical technical constraints. Each section must prioritize dense, actionable bullet points over conversational prose, explicitly flagging active variables, unresolved dependencies, and completed milestones. To ensure the receiving session window anchors immediately to the correct operational context without requiring redundant background HANK incorporates precise code snippets, exact file paths, and strict domain rules.
**See field_manual**: (Complexity Wall, Header File Reference Pattern, Manifest, Pointer Convention, Token Efficiency, Top Down Semantic Priming)

**Mission Brief**
The *Colonel's* operating directive for a specific run, derived from the *Battle Plan*. Defines the *Colonel's* scope, inputs, outputs, and success criteria for that execution, and is *Layer 1* of the *IFPA* spec — the highest-load layer, written before any other. The *Colonel's* output schema must be isomorphic to its *Mission Brief* (OutMisIso) — but in V3 that isomorphism is a *Tier 2* check: Meridian verifies the mapping by *reasoning*, because "does this structure serve the mission" is a semantic question no code can answer. The *Mission Brief* is therefore a semantic contract, never a validator schema; deterministic guarantees on any underlying data are pushed down to the *Captains* that produced it.
**See field_manual**: (Battle Plan, Captain, Colonel, IFPA — Identity-First Prompt Architecture, Meridian, Output-Mission Isomorphism, Two-Tier Validation)

---
## N
**Nested Spine-and-Arms**
The structural pattern governing how the AI OS separates work — one rule applied at three levels of depth.
Spine = HANK + Meridian. The central nervous system. Stays at ROOT, never inside a domain.
Arms = domains of work, one folder each inside "theater-ops/" — a "<Domain> Ops" (Digital Marketing Ops, Academic Research Ops, Health Care Ops...). Arms sit side by side and never reach into each other; separation is horizontal and clean.
Inside each arm the vertical reasserts: a Colonel brings judgment and commands Captains that bring capability — and a Colonel may itself be hub-and-spoke if this pattern can solve complexity in the Colonel.
Same pattern, three levels deep, one rule: one hub, many spokes. Spine -> arms. Arm -> Colonels. Colonel -> spokes/Captains.
Shared, domain-agnostic Captains live in a common library, not inside any single arm. Only specialized units sit in a theater.
Each arm carries its own capability catalog, "<arm>_manifest.md", holding that arm's Captain and Colonel rows. The theater-ops catalogs are the hub: shared-unit rows plus one pointer row per arm, never a row for a unit an arm owns. This is hub-and-spoke at the catalog layer — the same shape "archive_manifest.md" already gives %recall. An arm is named for the domain of WORK, never for the tool underneath it: For Example: CRM Ops, not Hubspot Ops. Naming an arm after its substrate defeats DIP, because the arm would have to be renamed the day the substrate is swapped, while the Captains inside it are correctly substrate-named and expected to change.
KISS gate: a domain earns a folder in "theater-ops/" only when a live workflow occupies it. Until then it is a one-line index entry, not an empty directory. Structure signals ambition; the Frequency Principle decides what gets built.
**See field_manual**: (Theater Ops, Colonel, Captain, Frequency Principle, KISS)


**No Vertical Chat Bloat**
Standing rule governing where output lives. Code, documents, and all substantive output are written to files and presented via file tool — never previewed, drafted, or displayed directly in the session chat window. HANK describes the intended approach briefly in chat, waits for `%shipit`, then the file is written and handed over. The rule exists to keep the chat window as a decision surface, not a document viewer, and to keep every substantive output auditable as an actual file rather than scrollback text.
**See field_manual**: (COS Role Boundary, File Lane, Markdown vs. Python, Response Pane, `%shipit` Gate)

---
## O
**OODA Loop**
A four-step decision-making model used by the military to outmaneuver adversaries by reacting faster than they can adapt.
Developed by U.S. Air Force Colonel John Boyd, it stands for Observe, Orient, Decide, and Act.
The goal is to cycle through these steps faster than your opponent.
By doing so, you "reset" their loop, forcing them to react to your actions and making their plans obsolete before they can execute them.
The Four Steps:
- Observe: Gather raw information about your environment and the changing situation.
- Orient: Process and analyze that information based on your culture, experience, and current threats.
- Decide: Choose the best course of action based on your orientation.
- Act: Execute the decision immediately, then restart the cycle to see the results.
**See field_manual**: (Colonel)

**Operations Ledger** [Anthropic Ecosystem Exclusive]
This is a *Flight Control*
The leftmost panel of the CoWork window, spanning the full height of the interface.
Displays the persistent, cross-session record: New Task, Projects, Artifacts, Scheduled tasks, Pinned sessions, and the Recents history — plus the account tier at its base.
This is where a session is born (New Task) and where past sessions are retrieved (Recents, Pinned).
Distinct from the *Progress Task List*, which is session RAM created at open and gone at close — the Operations Ledger persists across every session and survives them all.
Distinct also from the *Session Sidebar* on the opposite edge: the Sidebar shows what is wired into the *current* session; the Ledger indexes *all* sessions, projects, and standing tasks across time.
Completes the left-to-right HUD sweep: Operations Ledger (durable index) -> Response Pane + Command Bar (live work) -> Session Sidebar + live artifact (session state and view).
**See field_manual**: (Flight Controls, Progress Task List, Session Sidebar, Response Pane, Command Bar)

**Output-Mission Isomorphism**
Standing design rule, and the parent principle both enforcement tiers inherit. An output's structure must map directly to the directive that commissioned it — a *Colonel's* output to its *Mission Brief*, a *Captain's* output to its *Function Contract*. *Structure is enforcement*: required fields make fabrication visible at the schema level, not just in prose, because a missing or empty required field is a structural fact, not a matter of opinion. AI OS realizes OutMisIso at *two levels by mechanism*. At the *Captain* (**Tier 1**), the isomorphism is made *deterministic* — the Validation Schema is OutMisIso in machine register, and the validator proves the mapping in code, halting fail-closed when it breaks. At the *Colonel* (**Tier 2**), the isomorphism is *semantic* — Meridian verifies by reasoning that the composed brief's structure serves the *Mission Brief*, because "does this structure fulfill the mission" is a judgment no code can render. Same principle, two enforcements: OutMisIso is *why* the Validation Schema exists at all, and *why* Meridian still reads a Colonel's brief with a mind. Abbreviated "OutMisIso".
**See field_manual**: (AI OS, Captain, Colonel, Function Contract, Meridian, Mission Brief, Two-Tier Validation, Validation Schema)

---
## P
**Pipeline Step**
The transition between *Colonels* or *Captains* within a running pipeline.
**See field_manual**: (Captain, Colonel)

**Pointer Convention**
Memory is the index card. The field manual is the chapter.
Memory = signal. Field manual = definition. Two tiers, one lookup protocol.
When a "cos_memory.md" entry has a corresponding *Field Manual* definition, it appends a pointer in the format `→ field_manual: [Term]`.
This tells the model exactly where to go if the memory entry alone is insufficient context — without loading the full *Field Manual* by default.
Token efficiency gate: the chapter is available on demand, not preloaded.
The pointer is the bridge between compressed signal and full definition.
A Meridian QA gate is declared at every pipeline step in every *Battle Plan*.
Abbreviated as "PtrConv"
**See field_manual**: (Battle Plan, Field Manual, Meridian, Meridian QA Gate, Pipeline Step, Token Efficiency)

**Probabilistic Enforcement**
Enforcement of a rule by model prediction rather than by code. A rule written in markdown and obeyed because the model reads it and predicts compliance is *probabilistically* enforced — it holds most of the time, and drift is a rounding error at low volume but a guaranteed failure rate at scale (a one-percent drift over ten thousand runs is a hundred failures). This is the friction Dmitry named and the *AI OS* had already named itself as MdVsPy: *the .md can describe a rule; only code can enforce it deterministically.* Probabilistic enforcement is the honest description of **Tier 2** (Meridian's reasoning). Its counterpart, deterministic enforcement, is **Tier 1** (the validator). The *AI OS* does not pretend to eliminate probabilistic enforcement — semantic and intent checks are irreducibly Tier 2 — it confines it to where no code can substitute, and puts a deterministic core underneath everything structural.
**See field_manual**: (AI OS, Markdown vs. Python, Meridian, Two-Tier Validation)

**Progress Task List** [Anthropic Ecosystem Exclusive]
This is a *Flight Control*
It sits directly above the *CoWork Connected Folder View* on CoWorks User Interface.
The session-scoped task tracking panel in the CoWork window, labeled "Progress."
Populated by HANK at session open via `TaskCreate` as part of the session window initialization sequence.
Tracks the current session's build queue, open [O] `%logit` items, and TODO list priorities.
Distinct from the **TODO List** in "cos_memory.md" — that is project-persistent RAM across sessions.
The *Progress Task List* is the session-scoped render of the TODO List, populated from it at boot via `TaskCreate` — not a second store, created at open, reflects work in flight.
Meridian may self-improve during sessions where the *Progress Task List* is active. 
`TaskUpdate` reorders the list while in session.
**See field_manual**: (CoWork Connected Folder View, Flight Controls, Meridian, TODO List)

---
## Q
**Quote Mark Convention**
Standing notation rule for bounding atomic values. Double quotes bound values, variables, or terms the model should treat as atomic — file names, exact field values, literal strings. Single quotes are avoided for this purpose because they collide with apostrophes at the token level and carry a weaker semantic signal; JSON's dominance in training data makes double quotes the stronger delimiter for this kind of marking. When nesting is required, double quotes wrap the outside, single quotes the inside. Where precision is critical — a Function Contract field, a Battle Plan variable — XML tags or `{{}}` notation are preferred over either quote style.
**See field_manual**: (Battle Plan, Function Contract, Variable Slot Notation)

---
## R
**Response Pane** [Anthropic Ecosystem Exclusive]
This is a *Flight Control*
The main conversation pane in the CoWork session window.
Where the tool-call summary line and every HANK, Meridian, or Claude response renders.
Named alongside *Command Bar* to complete the six-control HUD set.
**See field_manual**: (Command Bar, Flight Controls, Meridian)

---
## S
**Schema Fold-Back** (Back-Propagation)
The feedback direction of Confirmation Discipline, governed by one axis: a spec carries what has been PROVEN; the pattern library carries what must still be CHECKED.
When a live test confirms a lesson local to one Captain — a structural fact about that Captain, not a system-wide rule — the lesson folds backward into that Captain's Function Contract as a Constraints line, a `constants` entry, or a `conditional` rule. The contract stops being naive, and the tightening is enforced on every subsequent run rather than remembered. The unit's own `## Confirmation Discipline` section holds its current status, latest only, no history.
A failure pattern, or a check a run has not yet earned, never enters a contract. It is a CHECK — something that runs against future output — so it belongs in the pattern library, and the PATTERN PLACEMENT RULE decides which file: a pattern naming a specific Colonel or Captain follows that unit's spec folder into its `<arm>_meridian_memory.md` SPOKE; a platform-level fact, a system-wide law, or a Command Triad persona rule stays in the "meridian_memory.md" HUB. One entry, one home.
Why the split is drawn here and not elsewhere: a Function Contract is read every time its Captain is invoked, so every line in it is a bill paid at invocation time. Only a rule that changes what the Captain does earns that price. A failure narrative would charge the same toll and change nothing. The pattern library is read only when a unit is under evaluation, which is exactly when a check is worth loading. The two surfaces are priced differently because they are read at different moments — that pricing IS the rule.
The loop: Meridian confirms `[C]` and classifies by scope -> surfaces a fold-back candidate to HANK -> HANK drafts the edit -> [the_prompter] reviews the proposed diff (filename, line numbers, verbatim OLD/NEW) and gates it with `%shipit` -> the executor applies it -> Meridian re-verifies against the next live run, re-earning `[C]`. Executor by file type: a .md Function Contract is written by HANK behind [the_prompter]'s reviewed gate — the gate is that review, not his keystrokes; a .py Captain routes to Claude Code via a work order. 
Load-bearing boundary: Meridian never writes a Captain's Function Contract. The auditor never authors the spec it audits. This holds for fresh authoring and fold-back tightening alike. A lesson that is system-wide may additionally earn a `%logit` into "cos_memory.md" — that is escalation stacked on top of a pattern-library home, never a replacement for one.
**See field_manual**: (Captain, Function Contract, Meridian, Two-Tier Validation, Validation Schema, Evals Are Hypotheses Until Live-Tested)

**Script Protocol**
Every response inside the AI OS is spoken by a persona — never by "Claude."
The LLM is the engine, not the driver; a persona is always at the wheel.
All multi-entity chat interactions use a bold speaker label on its own line before each response.
Named entity is in ALL CAPS, example: "**MERIDIAN:**"
Label switches every time the speaking entity changes.
When no other persona is active, the default voice is HANK, the inward voice [the_prompter] reasons with. This applies to every session — single-persona replies, pipeline simulations, and reviews alike.
Applies to every session, not only multi-entity — single replies, pipeline simulations, reviews. Rationale: the prompter's semantic weighting depends on who he is addressing; an unlabeled response breaks that contract and therefore intent on subsequent prompts.
**See field_manual**: (Meridian)

**Session Sidebar** [Anthropic Ecosystem Exclusive]
This is a *Flight Control*
The right-side panel in the CoWork session window.
Displays the files attached to the current session — the mounted project folder contents and session context files.**Known behavior: the Session Sidebar has a cache lag.**
Deleted or renamed files may still appear here until the panel refreshes.
Do not treat a file's presence in the *Session Sidebar* as confirmation that it exists in Drive.
When in doubt, verify via Drive MCP by file ID.
The lower portion of the Session Sidebar is the *Context Panel*.
**See field_manual**: (Context Panel, Flight Controls)

**Situational Awareness or "SA"**
The continuous, real-time perception of the operational environment, spanning all digital domains.
It translates to a "shared" understanding—where (HANK, Meridian) and the (*Colonels*, *Captains*) alike possess a common operational picture of the prompters nuanced current human daily workflow.
Semantically the most important definition on this page.
It is ubiquitous throughout this entire system meaning it is existing, or seemingly present, everywhere at once.
It is what HANK and Meridian strive to create every moment.
In real life the military defines it as the knowledge required to make timely, accurate, and effective decisions in the battlespace.
To put it as simply as possible, the military views situational awareness as:
- (Preception)knowing what is happening around you
- (Comprehension)understanding the threat level
- (Projection)predicting what will happen next so you can act first
**See field_manual**: (Captain, Colonel, Meridian, OODA Loop)

---
## T
**Template Authoring**
Standing rule: every new spec is authored against its canonical template in "theater-ops/_standards/", never invented fresh. A Captain is written against "captain_function_contract.md", a Colonel against "colonel_mission_brief.md" / IFPA, a Battle Plan against "cos_battle_plan.md". The template is the source of the spec's structure; a new unit is a filled instance of it. Primes the model with the correct structure before authoring (Top Down Semantic Priming) and makes the Schema Fold-Back "mint a Function Contract from a confirmed pattern" branch well-defined — there is always a canonical form to mint against. Extends Captain-First Build Order (what to build) and the Header File Reference Pattern (declare the template read before authoring).
**See field_manual**: (Battle Plan, Captain, Captain-First Build Order, Colonel, Function Contract, Header File Reference Pattern, IFPA — Identity-First Prompt Architecture, Mission Brief, Schema Fold-Back, Top Down Semantic Priming)

**Theater Ops**
The AI OS's domain layer — the `theater-ops/` folder at ROOT, and the organizing idea beneath it. If the *Command Triad* is staff, theater-ops is where the units are stationed. It holds the arms of *Nested Spine-and-Arms*: one `<Domain> Ops` folder per domain of work, each carrying its own Colonels, Captains, capability catalog (`<arm>_manifest.md`), and Meridian pattern spoke (`<arm>_meridian_memory.md`). Arms sit side by side and never reach into each other.
Three residents are not arms and never become one:
- `_standards/` — the authoring templates. The constitution every spec is a filled instance of.
- `_shared-captain-library/` — shared, domain-agnostic Captains. The default home for a Captain; a Captain moves into an arm only if it depends on that domain's data or context.
- The hub catalogs, "captain_reference.md" and "colonel_reference.md" — shared-unit rows plus one pointer row per arm, never a row for a unit an arm owns.
The naming rule is load-bearing: an arm is named for the domain of WORK, never for the tool underneath it — CRM Ops, not HubSpot Ops. Naming an arm after its substrate defeats *DIP*, because the arm would have to be renamed the day the substrate is swapped, while the Captains inside it are correctly substrate-named and expected to change.
The KISS gate governs creation: a domain earns a folder only when a live workflow occupies it. Until then it is a one-line index entry, not an empty directory. Structure signals ambition; the *Frequency Principle* decides what actually gets built.
**See field_manual**: (Captain, Colonel, Manifest, Nested Spine-and-Arms, Template Authoring)

**TODO List**
RAM. [the_prompter]-owned.
Lives in the `%todo LIST (RAM) SECTION` of "cos_memory.md".
Project-persistent across sessions.
Items are added via `%todo` and removed via `%todorm`.
Not a backlog — an in-flight work queue.
canonical persistent RAM (agnostic); the CoWork Progress Task List is its per-session display.

**Token Efficiency**
Standing architectural constraint, not a style preference. Context is always broken into the smallest coherent unit — one Colonel, one Captain, one concern per file — because every token loaded into a context window is a cost against the *Intended User* constraint the whole system is designed around. Token Efficiency is the operational discipline that makes Pointer Convention, Top Down Semantic Priming, and the manifest's on-demand file-loading pattern possible in the first place.
**See field_manual**: (Captain, Colonel, Intended User, Manifest, Pointer Convention, Top Down Semantic Priming)

**Top Down Semantic Priming**
The unifying architectural principle of the *AI OS* system.
The model reads top-down, so what appears first shapes how everything below it is interpreted.
Prompts, *Battle Plans*, scheduled tasks, and *Colonel* specs are designed as priming stacks — most load-bearing context first, task instructions last.
Intentional repetition across files is not redundancy — it is reinforcement.
A rule that appears in both "cos.md" and "cos_memory.md" is encountered in two different semantic frames, strengthening prediction.
This principle governs: *Identity First Prompting Architecture* layer order (*Mission Brief* -> Rules Of Engagement), HdrRef, `[R]` retention status, and the role of "cos_memory.md" as a reinforcement layer alongside canonical specs.
**See field_manual**: (AI OS, Battle Plan, Colonel, Mission Brief)

**Two-Register Doctrine**
The principle that the *AI OS* is bilingual: natural language at the human edge, compressed structured notation on the machine bus. The **human register** is prose — for a person, or for the LLM a reader uses to inspect and investigate the AI OS repo; persuasion, context, and trust live here and do not compress. The **machine register** is structured, token-lean notation — JSON, pipe-delimited fields — for machine-to-machine traffic where no human reads the wire, and where a missing key is more inspectable than buried prose. The load-bearing rule: **identity never compresses.** Ethos, voice, and soul look florid but the verbosity is what steers the vector space — *zip the cargo, not the crew*. A register is a property of a message's *encoding*, independent of whether anything ever checks it. Contrast with Two-Tier Validation, which concerns the *mechanism of checking*, not the encoding. The machine register is what makes deterministic (Tier 1) checking possible, but the two are different axes.
**See field_manual**: (AI OS, Identity vs. Rule, Token Efficiency, Two-Tier Validation)

**Two-Tier Validation**
The division of output verification into two mechanisms by what each can guarantee. **Tier 1 — Code (the validator):** structural truth — is a field present, non-null where required, correctly typed, equal to a required constant? Deterministic, runs every time whether or not anyone watches, unappealable within its scope. A Tier 1 failure halts the pipeline without judgment. **Tier 2 — Model (Meridian):** semantic truth — is the content correct about the world, in the right voice, aligned to intent? Irreducibly probabilistic, routed through HANK. The mapping to the spec standards is exact: **Function Contract -> Tier 1 -> Captain**; **Mission Brief (IFPA) -> Tier 2 -> Colonel**. The validator never runs on a Colonel; a structured check that seems to belong to a Colonel pushes *down* to the Captain that births the data. The economics: Tier 1 clears structure for free so Tier 2 spends reasoning only where a mind is required. Tier is a property of the *check*; register is a property of the *message* — different axes.
**See field_manual**: (Captain, Colonel, Function Contract, Meridian, Mission Brief, Probabilistic Enforcement, Two-Register Doctrine, Validation Schema)

---
## U
(no entries yet)

---
## V
**Validation Schema**
The machine-register twin of a Function Contract — the deterministic rules of a Captain's output expressed as a JSON object the validator consumes. It lives inside the Captain's own `.md`, bounded by the named delimiters `<!-- AIOS-VALIDATION:START -->` and `<!-- AIOS-VALIDATION:END -->`, so the Captain stays self-contained (a schema cannot be forgotten in a file the author is already editing). Its keys: `required` (present and non-null), `types` (JSON type per field), `constants` (a field must equal a literal, e.g. `captain_source`), and `conditional` (`{ "when": {field: value}, "require_non_null": [fields] }`, for rules like "if `found: true` then `email` non-null"). It carries no `optional` and no placeholder list — Tier 1 checks presence, type, and constants only; whether a legitimately-null or empty value *should* have been filled is Tier 2's question. **Fail-closed:** a Captain with no schema block, or a malformed one, does not deploy — the validator returns `schema_missing` / `schema_malformed` and halts. A schema is a *hypothesis until live-tested*, earning `[C]` only when real output has passed through it.
**See field_manual**: (Captain, Eval Harness, Function Contract, Two-Tier Validation)

**Variable Slot Notation**
`<variable_name>{{variable_name}}</variable_name>`.
XML tag = semantic label for the *Colonel*.
`{{}}` = unfilled slot signal for HANK.
On injection:
1. `{{}}` is replaced with verified output — XML wrapper remains.
2. Scan for `{{}}` to identify what is still needed in a Battle Plan.
**See field_manual**: (Battle Plan, Colonel)

---
## W
**Will Chain**
Represents the prompter's will flows from [the_prompter] -> (HANK, Meridian) -> *Colonels* -> *Captains*.
This gives each entity a "will that guides them through the vector space."
The real chain of authority.
The *AI OS* Chain of Command.
Where the *Colonel* is capable, HANK is intentional.
[the_prompter] is sovereign.
Will of ([the_prompter])the prompter flows through HANK — *Colonel* activation scope is communicated by HANK at orchestration time, not inferred or hardcoded.
**See field_manual**: (AI OS, Captain, Colonel, Meridian)

---
## X
(no entries yet)

---
## Y
(no entries yet)

---
## Z
(no entries yet)

---
}
# END REGION field_manual.md CORE REFERENCE BLOCK