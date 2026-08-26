# AI OS:

**A governance layer for one operator's work with AI.**

Written primarily in prose, with a deterministic Python validator beneath every structural check.

The AI OS is not application software and not a Python framework. It is a **context architecture** that an LLM host — CoWork, Claude Code, or another — runs on top of. There is no `pip install`, no `python run.py`, and no runner in this repository. The host supplies the loop. This repository supplies the governance the loop runs inside.

## The Pain Point This Project Aims To Solve:

Large projects built on LLMs hit a **Complexity Wall**: 
1. Black-box failures
2. Context drift and bloat
3. Knowledge degradation
4. State and transition chaos

The AI OS answers it at the scale of one person. It governs work inside a session window and carries state between sessions, so a single operator can direct AI without descending into chaos.

**The Analogy Is Primer Paint.** 
Nobody buys primer for beauty.
They buy it because the upfront coat amortizes — easier application, even coverage, longer life before repainting.
The boot read is that coat.
It costs tokens at the top of every session and pays them back in fewer corrections, fewer re-runs, fewer repaints.

```
High governance = stable output, more manual steps
                          (SWEET SPOT) 🤌 <-- what the AI OS aims for
Low governance  = unstable output, fewer manual steps
```

---
### The Thesis This Project Argues:

Everyone building agents is writing to their own standard. This project is an attempt at a shared one, built on a specific bet:

> **Semantic priming matters more than algorithmic rules when the executor is a language model.**

Hierarchy is pretrained compression.

Command structures, rank, deference, and chains of authority saturate the training data.
- SO writing "Colonel" costs one token for an org chart a rulebook spends five hundred words describing.

The model does not execute rules — it predicts what comes next given context.
- SO the AI OS spends its context on **identity** and lets rules constrain from there.

Software development standardized its conventions in the late '80s and '90s.
Agentic reasoning is at that same early stage.
This repository is a proposed model to write to, offered so others can argue with it, fork it, and improve it.

#### The Emoji Thesis:
*Design rationale, not a capability claim. Nothing in this section is live-tested — see the three limits at the end.*
Every response inside the AI OS is spoken by a named persona, and every persona label carries a glyph.
HANK wears 🤠. Meridian wears 🤖. Peggy wears 💁‍♀️.

> This is the least conventional thing in the repository, so it gets argued at the end of this README rather than asserted **here**.

---
### The Three Metaphors That Carry The Design:

**1. Operating system.**

| OS concept | AI OS |
|---|---|
| Kernel | HANK — Chief of Staff |
| RAM | `%todo` list |
| Hard drive | `%archive` |
| File system / pointers | `manifest.md` |
| Boot sequence | `pi.md` |
| Running processes | Colonels |
| Installed programs | Captains |
| Shared libraries | `_code-tools/` |
| Interrupt handler | Meridian |
| Scheduler | Host scheduled tasks |

**2. Biology:** 
- Meridian is the vertebrae — the fixed line of continuity.
- HANK is the nervous tissue threaded along it, carrying intent down to the limbs and results back up. 
> Together they are the Central Nervous System; Colonels and Captains are the arms and legs.

**3. Chain of command.**
```
Operator (sole authority)
   |
HANK — Chief of Staff, inward voice, orchestration
   |
Colonels — judgment (Tier 2)
   |
Captains — bounded capability (Tier 1)

Meridian — Inspector General, OUTSIDE the chain, reports to the operator
```

---
### Meridian | The Inspector General:

Most agent projects give AI users a workforce. This one gives them a **supervisor**.

**Meridian** is an Inspector General — an independent QA agent that sits *outside* the chain of command and reports to the operator directly.
It is not a manager agent inside the hierarchy, and it is not a policy layer bolted on after the fact.
It fires automatically at every pipeline step, and it holds halting power over any run.

Two tiers of check sit under that authority:

| Tier | Mechanism | Checks | Runs where |
|---|---|---|---|
| **Tier 1** | `validator.py` — code | Required field present, non-null, correctly typed, matches declared constants. Structural facts only. Deterministic and unappealable. | The **Captain** boundary, where structured JSON exists |
| **Tier 2** | Meridian — reasoning | Is a present-but-valid value actually *wrong* for this mission? Right framing? Serves the operator's intent? | Everywhere judgment lives, including every **Colonel** |

The validator never runs on a Colonel. Structural guarantees push *down* to the unit that can emit structure.

**The defensible claim is not "it won't hallucinate."** 
**The Claim is: "it halts and surfaces that information to the prompter."** 
That claim survives the first bad run in front of a paying user, which is more than most reliability claims manage.

---
### The Boot Read File Set:
*Core Files: Each session reads these files and is the "Primer Paint" from the analogy above.*
| File | Role |
|---|---|
| `pi.md` | Project identity and boot sequence. Read first, every session. |
| `cos.md` | HANK. Kernel identity, the closed `%` command set, standing rules. |
| `cos_memory.md` | Memory — the TODO list (RAM) and `%logit` entries (system log). |
| `meridian.md` | Meridian. QA mandate, verification stack, halt protocol. |

### The On-Demand Read File Set:
*On-Demand: these files support the core files and are read based on prompter intent. HANK and Meridian have awareness of when to read these files.*
| File | Role |
|---|---|
| `meridian_memory.md` | Pattern-library HUB, plus the SPOKE INDEX and placement rule. |
| `manifest.md` | File index. Every file, every ID. |
| `field_manual.md` | Lexicon. Verbose definitions behind the compressed memory codes. |
| `affirmative_detection.md` | Invocation log and automation-candidate patterns. |
| `REM.md` | Nightly `%REM` sweep instructions. |
| `validator.py` | The Tier 1 deterministic validator. |
| `theater-ops/` | Domain arms — Colonels, Captains, and the standards they are authored against. |

---
### The Boot Cost is Acknowleged:

**The Boot Cost is also under active development to decrease the TOKEN COUNT**
There is no single `architecture.md`, because the architecture *is* the boot-read file set.
The boot read is the product's main recurring cost. Publishing it is the point.

| Core file | Tokens |
|---|---|
| `pi.md` | 6,850 |
| `cos.md` | 12,400 |
| `cos_memory.md` | 10,000 |
| `meridian.md` | 12,800 |
| **Total** | **42,050** |

*Measured by running each file through the OpenAI tokenizer. Anthropic and other vendors segment text differently, so treat these as **±10–15% across model families** — an accurate measurement taken with a slightly different ruler.*

**What that occupies:**

| Context window | Boot load |
|---|---|
| 128K | ~33% |
| 200K | ~21% |
| 500K | ~8% |
| 1M | ~4% |

Two things keep this from growing without bound:

- **The `%logit` boot-cost warning.** Every memory entry HANK or Meridian *advocates* carries a ⚠️, because that entry is paid at every future boot, forever. The bar to add one is deliberately high.
- **Hub-and-spoke loading.** The pattern library is never read whole. Hub always, plus exactly one spoke — the one belonging to the unit under evaluation. A run that never touches CRM never loads CRM patterns.

The static portion of the boot payload is also cache-friendly: ordering the unchanging files first lets a host's prompt caching absorb most of the recurring cost.

---
### Install:

**Nothing to install.** Two conditions carry that claim, and both must hold:

1. The host runtime ships Python. (CoWork does.)
2. `validator.py` is **stdlib-only** — `json`, `re`, `datetime`, `pathlib`. Nothing else, ever.

Condition 2 is the load-bearing half. The moment a future validator imports a third-party library, the guarantee breaks. **Treat stdlib-only as a rule of the project, not a coincidence of the current version.**

**Scope, honestly:** CoWork is the only runtime tested to date. Any other host — Claude Code, a bare machine — is an untested inference until it runs there live.

**To use it:**

1. Clone the repository into the folder your host mounts.
2. Replace the four install tokens across the core files: `[the_prompter]`, `[prompter_job]`, `[prompter_project_objective]`, `[prompter_timezone]`.
3. Point your host at `pi.md` as the project instruction and start a session.

> The bracket tokens are the install surface. They are intentional and stay in the public repo.

---
### Session Flow With HANK and Meridian:

```
%command
  -> HANK reads the Battle Plan, injects context
  -> Colonel runs                          (Tier 2 judgment)
  -> Captain invoked                       (bounded capability)
  -> validator.py fires at the Captain boundary   (Tier 1, deterministic)
  -> Meridian verifies against four sources
       pass -> pipeline advances, one tick to the invocation log
       halt -> pipeline pauses, finding surfaces to HANK
  -> output, or escalation to the operator
  -> %shipit publishes
```

**Meridian's four Tier 2 sources:** the Battle Plan (schema isomorphism), `cos_memory.md` (standing rules), the pattern library (known failure shapes), and the Gate Ledger (did Tier 1 actually happen).

---
### The Guardrails:

**The `%shipit` gate.** Nothing writes without an explicit `%shipit`. Not momentum. Not "are we ready." Not a clear-seeming intent. The four self-authorizing memory commands are the only standing exceptions — each its own gate, because recording is not acting.

**The Halt Protocol.** A halt is a **pause, not a kill**. Pipeline state is preserved so the run can be healed. Recoverable halts are corrected by HANK and Meridian jointly and the pattern is logged. Terminal halts escalate to the operator, full stop.

**The Gate Ledger — and why it exists.** Meridian reconciles gates *declared* against gates *actually fired*. A gate declared but absent is a PHANTOM; one fired but undeclared is an ORPHAN. Both halt.

> This check exists because an early test run reported clean with **zero gates fired**. The validator had never run at a single boundary. Tier 1 had not failed — it had never happened, and Meridian passed the run anyway. The ledger is the scar from that.

**Fail-fast, halt-first authoring.** A unit's halt conditions are written *before* its happy path. The failure surface is mapped before the capability exists.

**Two failure modes, not one.** Runaway spend and unchecked hallucination. Neither is prevented by a human in the loop — a fatigued human rubber-stamping outputs catches neither. Enterprises solve spend with budgets and error with evals.

> **The safety was never the human's eyes. It was the structure the human authorized.**

---
### Memory:

Four self-authorizing writes, in two branches:

```
RETROSPECTIVE
  %todo      working memory. Volatile, cleared per item, persists across sessions.
  %logit     crystallized standing rule. Dated, indexed, read at every boot.
  %archive   verbatim block. Date-indexed, searchable, never boot-read.

PROSPECTIVE
  %sched     time-gated intention. Dormant until the nightly %REM sweep surfaces it.
```

Sessions are deliberately transient whiteboards. Anything worth keeping is written by an explicit memory command — which is also what makes state **reproducible**: a new session reconstructs the operating picture from files, not from scrollback.

---
### Authoring Standards:

Every new unit is a **filled instance** of a canonical template in `theater-ops/_standards/`, never a fresh invention.

| Template | Authors | Tier |
|---|---|---|
| `captain_function_contract.md` | Captains — five prose layers plus a Validation Schema | Tier 1, deterministic |
| `colonel_mission_brief.md` | Colonels — IFPA, seven layers | Tier 2, judgment |
| `cos_battle_plan.md` | Battle Plans — source of truth for a pipeline | Declares the gates |

**IFPA — Identity-First Prompt Architecture** is the Colonel standard and the repository's strongest original claim: *Mission Brief → Intelligence → Ethos → Comms Protocol → Standards → Initiative → Rules of Engagement.* A Colonel built around caring about quality predicts differently than one instructed to produce it.

**The Validation Schema** is the Captain's machine-register twin — an `AIOS-VALIDATION` JSON block inside the contract itself. Keys: `required`, `types`, `constants`, `conditional`. No `optional`. It is **fail-closed**: a missing or malformed block yields `schema_missing` / `schema_malformed` and halts.

Because that format is plain markdown plus a JSON block, and the validator is stdlib Python, **a capability written against this contract is portable and structurally checkable before anyone runs it** — independent of which model reads it. Running a given Captain still depends on its declared substrate being connected in the AI OS user environment. Portable spec; conditional execution.

**Substrate selection** — reach for the leftmost rung that does the job:

| Rung | Substrate | Reach for it when |
|---|---|---|
| 1 (default) | Pure prose | Always try first. Zero dependencies, nothing to break. |
| 2 | Host-native tooling — files, bash, scheduled tasks, artifacts | Local file and data work. |
| 3 | MCP connector | High-frequency, load-bearing external systems. |
| 4 (last resort) | Browser automation | Nothing else can reach it. Label it *attended*. |

---
### What Is In This Repository Today:
*(As of 26 August 2026)*

| Component | Count |
|---|---|
| Core boot files | 4 |
| Authoring templates | 3 |
| Shared Captain Function Contracts | 5 |
| Arm-owned Captain Function Contracts (CRM arm) | 6 |
| Domain arms built | 1 |
| Colonels built | **0** |
| Units carrying `[C]` (live-confirmed) | **0** |

---
### What Is Missing:

A governance project earns trust by being first to say what it does not have.

| Absent | Detail |
|---|---|
| **Evaluation suite** | No `/evals`, no benchmark harness, no success-rate table — and there will not be one in this README. |
| **Telemetry and observability** | No token meter, no tracing stack, no dashboard. Spend is bounded by the subscription ceiling, not by a dashboard. |
| **Execution sandbox** | No Docker, no WASM. The AI OS runs inside the host's sandbox and is candid that it is not installed software with execute rights. |
| **Contribution pipeline** | Nothing yet defines how an outside Captain gets live-tested to `[C]` and merged. Until it exists, a contributed contract is `[O]` — well-formed, unproven. |
| **Colonels** | Zero built. The arms shelf holds one arm and no judgment units. |
| **Test datasets and mocks** | None. |
| **Upgrade path for forks** | Every install is a forked copy of markdown. A hundred installs means a hundred snapshots. Intentional at this scale; a real problem at any other. |

**The rule that governs all of the above:** *evals are hypotheses until live-tested.* No eval, schema, or generated unit reaches production on internal consistency alone. Three human gates earn `[C]` — the operator approves the task inventory, `%shipit`s the specs, and confirms live-test results against real output.

Research, decomposition, spec-writing, and eval-drafting are machine work. **Intent, authorization, and ground truth remain the operator's.**

---
### Roadmap:

Specified, not built. Described as intent, never as capability.

- **Telemetry** — the validator already assembles `captain`, `invoked_by`, `timestamp`, `verdict`, and `deltas` per invocation. Persisting that as an append-only, non-editable audit log is the next step. *The audit trail must not be writable by the entities it audits.*
- **Automated inflow** — memory today is fed by hand. A scheduled ingestion pipeline running *through* Meridian is the obvious extension: automated inflow, governed.
- **The autonomy ladder** — `%shipit` gates converting to evals as a unit's reliability track record accrues. For a single operator the gate is sovereignty, not friction; the ladder is the answer to organizational friction, and it is defined but unbuilt.
- **HTML control surface** — a template-driven UI that reads canonical state. The rule it must obey: *the HTML is a view, never the source of truth.*
- **Contribution and review pipeline** — see *What is missing*. The crowdsourced-library idea is only honest once this exists.
- **Federated architecture** — multi-instance memory and distributed QA. Single-writer memory is fine for one operator and breaks for a team.
- **Hierarchy-as-compression experiment** — three conditions (bare model / explicit rulebook / AI OS framing), same task set, rubric written *before* the runs. Measured on input tokens, output tokens, task completion, and **correction cycles**. A mixed result is expected and would be more credible than a clean sweep.

---
### The Emoji Thesis Continued:
*Design rationale, not a capability claim. Nothing in this section is live-tested — see the three limits at the end.*
Every response inside the AI OS is spoken by a named persona, and every persona label carries a glyph. HANK wears 🤠. Meridian wears 🤖. Peggy wears 💁‍♀️.
This is the least conventional thing in the repository, so it gets argued at the end of this README rather than asserted **here**.

---
### The Mechanism | Emoji Are Pretrained Affective Compression:

The Emotion Dictionary is the same bet as the military hierarchy, aimed at a different axis:

| Premise | What one token buys |
|---|---|
| **Hierarchy** | "Colonel" costs one token for an org chart a rulebook spends five hundred words describing |
| **Emoji** | 🤠 costs one token for an affective stance a paragraph of tone instruction spends two hundred words describing |

Emoji are among the most affectively saturated tokens in any training corpus. Each one arrives pre-loaded with the emotional context of millions of human uses — not a definition the model looks up, a prior it already holds.

**The apparent contradiction, named before a reader finds it.** The Two-Register Doctrine states that *identity never compresses* — souls stay verbose, cargo gets zipped. Emoji are compression riding on the identity layer. That looks like a violation and is not: it is the same free lunch hierarchy already takes. **Identity that reads as verbose but is cheap by cultural reference.** The doctrine forbids *stripping* identity to save tokens. It does not forbid identity that was already dense when it arrived.

---
### Two Thesis Frames:

**(A) The compression framing — checkable.**

Emoji are a token-efficiency mechanism. A gradient array (`Joy: 🙂 😊 😄 🤩 😂 🤣`) encodes intensity without a scale being described. A blend grammar — two bases maximum, dominant first — makes 😊😢 read as bittersweet with no rule written for it. The dictionary is roughly 400 tokens and replaces what a tone-and-register style guide would spend several thousand on.

This framing is **falsifiable**, and the experiment that would settle it is already on the roadmap: three conditions, same tasks, measured on correction cycles.

**(B) The cohesion framing — felt.**

The AI OS names its principle *esprit de corps* — a shared will that carries three entities and one operator through the same work. Emoji are how that register is held.

A speaker label without a glyph is a role. A speaker label with one is a **presence**. Across hundreds of sessions the operator is not reading output from a model; he is working with a crew whose expressions track the actual state of the reasoning. That continuity is the working relationship, and the relationship is what makes delegation feel like delegation instead of prompting.

**These are compatible but not the same claim.** (A) can be measured. (B) can only be experienced. Fusing them produces a sentence that sounds stronger and defends worse.

---
### What IS Actually Enforced:

The strong material is not the thesis. It is the rules a reader can check against the files.

**1. The 💢 doctrine — anger is faceless by design.**
Facial anger glyphs (😠 😡) never render anywhere in the AI OS. Anger renders as a mark: 💢. The reason is structural, not decorative — **anger at a situation, never at someone.** The glare is removed from the notation rather than politely avoided in practice. Envy 💚 follows the same precedent: the emotions most dangerous when aimed at a person are marks, not faces. Appearance of a facial anger glyph anywhere is a Meridian flag on sight.

**2. The face/mark split is an audit-independence boundary.**
HANK and Peggy wear faces. **Meridian never does** — its working notation is symbol anchors only: 🔎 ✅ ⚠️ 🚨 🟢 🟡 🔴. A face is an identity claim, and facelessness is load-bearing for a genderless Inspector General whose verdicts must never be read for mood. The single sanctioned exception is the 🤖 identity plate: static, never modulated, never composed with emotion glyphs. A nameplate on the gauge glass, not a mood behind it.

**3. The identity plate is checked, not hoped for.**
A speaker label reaching the operator without its glyph is **MALFORMED**, and Meridian flags it on sight — the same standing as a facial anger glyph. The dictionary is not a style suggestion; it is a rule with an inspector attached.

**4. Expression, never performance.**
The governing instruction is *wear the lowest glyph that is honest*. The face tracks the actual state of the reasoning — it never sells the sentence. An emoji used to make a mediocre result feel better is the failure mode this rule exists to prevent.

---
### Three Limits On This Thesis:

Stated here rather than buried, because this is the section most likely to be challenged.

**Limit 1 — nothing here carries `[C]`.**
*Evals are hypotheses until live-tested* has no carve-out for the maintainer's favorite premise. The Emotion Dictionary has not been run against a bare-model or explicit-rulebook control. The correction-cycle experiment on the roadmap is the measurement that would settle it, and it has not been run. **This section is a bet with its reasoning shown, not a result.**

**Limit 2 — the neuroscience applies to one of the two readers.**
Face-processing and affective-priming research describes *human* cognition. The model has no amygdala; what it has is token co-occurrence. Both effects are real and they are **different effects**:

| Reader | Mechanism | Effect |
|---|---|---|
| The operator | Visual anchor, affective salience | Scanning speed — the Eye-Relief rule |
| The model | Affectively saturated token | Prediction shaping — Top Down Semantic Priming |

The AI OS calls this the Double Readership Path and keeps the two claims separate on purpose. Collapsing them into "neuroscience says emoji work" would be the softest sentence in this document.

**Limit 3 — the enforcement persuades; the thesis only explains.**
The 💢 doctrine, the face/mark split, and the identity-plate check are inspectable rules in files anyone can read. The compression premise is a hypothesis about why they help. **Read the rules first and the reasoning second** — the reverse order reads as justification.

---
### Repositories:

| Repository | Visibility | License | Holds |
|---|---|---|---|
| `AI-OS-HANK` | Public | AGPL-3.0 | The spine plus one arm. What this README describes. |
| `AI-OS-HANK-ME` | Private | GPL-3.0 | Members edition — the extended Captain and Colonel libraries. |
| `AI-OS-HANK-DEV` | Private | — | Development. Changes propagate outward to both. |

**A member's work stays a member's work.** Battle plans and specs authored in a member's own instance live in that instance. Skill files in someone else's repository are judgment permanently extracted; this split is the structural answer to that, not a rhetorical one.

---
### Contributing:

Distribution governance, versioning conventions, and the contribution process live in `CONTRIBUTING.md` — planned, not yet written. Until it exists:

- Pull core updates from `main`. Off-main edits are unsupported; if you conflict, back up and re-clone.
- Semantic versioning plus a CHANGELOG entry per push is the only ceremony intended.
- A contributed Function Contract is `[O]` until it earns `[C]` against live output. That rule has no exception for outside contributors — a schema-valid, never-tested unit is indistinguishable from a confirmed one at a glance, and that is exactly how knowledge degradation gets in wearing a good disguise.

---
### License:
AGPL-3.0. See `LICENSE`.

---

*AI OS Creators — MICHAEL_BLUM & WES_SCHAEFFER (The Sales Whisperer™)*