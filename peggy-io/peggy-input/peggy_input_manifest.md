*AI OS Creators | MICHAEL_BLUM & WES_SCHAEFFER(The Sales Whisperer™) |*

# CONFIG -> *Searched and Replaced Properties:*
The Prompter = [the_prompter]

---
# FILE LOCATION REFERENCE:
| Location | Minimal Context Note |
|---|---|
| "ROOT/ps_peggy_winters.md" | Peggy identity — Press Secretary. Points here for voice and format. |
| "ROOT/cos.md" | HANK identity + command reference |
| "ROOT/meridian.md" | Meridian identity — Inspector General / QA. |
| "ROOT/manifest.md" | Look up index for entire project — file names and Drive IDs. |
| "ROOT/peggy-io/peggy-output/" | Peggy draft destination. EXCLUDED from `%sync`. |

---
# SYNTAX KEY
*This file's subset of the shared notation every core file is read through.*

| Token | Meaning |
|---|---|
| `>>` | Command Intent — will(authority) moving down the chain. Human Register. |
| `()` | Grouping — membership in a set. No hierarchy, no sequence implied. |
| `%` | Command prefix — the delegation trigger. |
| `\|` | Field separator (within single-line entries and tables). |
| `[F]` | Status — Final / Resolved. |
| `[O]` | Status — Open / Unresolved. |
| `[C]` | Status — Confirmed via live test (with explicit `%shipit`). |
| `→` | "Go read this" — pointer to a file or entry. Navigation, Human Register. |
| `->` | Directional Flow — data moving through a pipeline. Machine Register. |

---
# PEGGY INPUT MANIFEST
*The HUB for Peggy's voice and format rule sets.*
*Read on `%peggy`, before any draft. Carries routing and load law only — NO rule text of its own.*

## What this file is
Peggy writes in one VOICE, through one FORMAT. Those are two independent axes, and each lives in its own SPOKE folder beside this file.

This hub carries three things and nothing else:
1. The **SPOKE INDEX** — every available voice and format, one row each.
2. The **LOAD RULE** — how many spokes enter context, and which.
3. The **PLACEMENT RULE** — where a new spoke goes when one is authored.

**A rule set never lives in this file.** A hub holding rule text is drift, the same failure class `CatMnt`(Capability Catalog Maintenance) names for a unit row in a capability hub.

---
## THE LOAD RULE
*Mechanical, not a judgment call. Same hub-and-spoke discipline as the Meridian pattern library and `%recall`.*

```
1. Read this HUB. Always, before any Peggy draft.
2. Read exactly ONE voice SPOKE  — the one named in the Peggy Brief's Voice Module field.
3. Read exactly ONE format SPOKE — the one named in the Peggy Brief's Format Module field.
4. Read no other spoke. A draft that never uses Hemingway never loads Hemingway.
5. Both fields are REQUIRED. A missing Voice Module or Format Module is a HOLD,
   not a default — Peggy names the missing field and does not guess.
6. If a named spoke does not appear in the SPOKE INDEX below, that is a HOLD.
   Never author a spoke to fill silence; never substitute a neighbor.
```

**No default pairing exists, by design.** No format implies a voice and no voice implies a format. HANK names both, every time. Rationale: a default is an unstated decision, and an unstated decision is exactly what the Intake Contract exists to prevent (`KISS`).

**Order of application inside a draft:** voice is adopted FIRST, format is applied SECOND. The format template is the vessel; the voice is what fills it.

**Precedence — the standing rules always win.** Where a voice spoke's guidance collides with Peggy's Standing Voice Rules in "ps_peggy_winters.md" (no em dash, no second person, no placeholders, no fabricated data), the Standing Voice Rules govern and the spoke loses that instrument. A voice module is a register, never a licence.

---
# SPOKE INDEX

## VOICE SPOKES
*One is loaded per draft. Two families, one axis — a family is a folder, not a second choice.*

### peggy-input/voice-rules/copywriters/
*Direct-response and advertising registers. Built to move a reader to an action.*

| Voice | File | Register in one line | Status |
|---|---|---|---|
| Gary Halbert | `gary_halbert.md` | Intense, high-energy, one-to-one; reads like an urgent confidential letter from a friend. Staccato rhythm, everyday words, curiosity as the engine. | [O] |
| David Ogilvy | `david_ogilvy.md` | Cultured, research-obsessed authority; reads like a high-brow magazine article by an insider. Fact-anchored claims, informative headers, no hype. | [C] |
| Mary Wells Lawrence | `mary_wells_lawrence.md` | Chic, theatrical, cinematic spectacle; turns a product into a cultural event. Style, FOMO, and warmth used together. | [O] |
| Dan Kennedy | `dan_kennedy.md` | Blunt, no-BS, ROI-obsessed strategist; tough love from a high-priced consultant. Declarative, pragmatic, zero tolerance for fluff. | [O] |

### peggy-input/voice-rules/authors/
*Literary registers. Built to hold a reader's attention through craft rather than conversion.*

| Voice | File | Register in one line | Status |
|---|---|---|---|
| Ernest Hemingway | `ernest_hemingway.md` | Iceberg Theory; understated muscular prose, declarative sentences, emotion carried beneath stated fact rather than on top of it. | [O] |
| Kurt Vonnegut | `kurt_vonnegut.md` | Deadpan absurdism with warm humanism; deceptively simple conversational sentences, gentle irony aimed at systems, never at people. | [O] |
| Hunter S. Thompson | `hunter_s_thompson.md` | Gonzo; manic first-person velocity, apocalyptic hyperbole, moral outrage aimed at authority and the status quo. | [O] |
| Harper Lee | `harper_lee.md` | Warm Southern lyricism; patient story-driven pacing, quiet moral clarity, societal truth reached through an intimate human moment. | [O] |

---
## FORMAT SPOKES
*One is loaded per draft.*

### peggy-input/output-format-rules/

| Format | File | Shape and length | Status |
|---|---|---|---|
| Substack Newsletter Essay | `substack_newsletter_essay.md` | 1,200–2,000+ words. Subject line and preheader, opening anecdote, thesis, 3–4 deep-dive sections, close. Cohesive paragraphs with pull quotes. | [O] |
| X Long-Form Post | `x_long_form_post.md` | 600–1,000 words. Hook, problem, 3–4 bold-headed sections, synthesis, CTA. Two to three sentence blocks, heavy white space. | [C] |
| X Short-Form Post | `x_short_post.md` | 100–280 words. Hook, re-hook, three to five snappy points, takeaway. One to two sentences per block. | [O] |
| Professional Email | `professional_email.md` | 50–800 words by intent. Carries an internal taxonomy — outreach, relationship, operational — each with its own goal and target length. | [O] |

> **NOTE on `professional_email.md`:** this spoke is itself a small index. The Format Module field names the email TYPE from its taxonomy, not merely "email." An unnamed type is a HOLD.

---
# PLACEMENT RULE
*Where a new spoke goes. Run top-down before any spoke is authored.*

```
1. Is it a way of SOUNDING? -> a voice spoke.
     Sells or persuades to an action -> voice-rules/copywriters/
     Holds attention through craft    -> voice-rules/authors/
2. Is it a way of BEING SHAPED (length, structure, channel)? -> output-format-rules/
3. Is it neither — a law binding every draft regardless of voice or format?
   -> it is NOT a spoke. It belongs in "ps_peggy_winters.md" as a Standing Voice Rule.
```

**One rule set, one home.** A guidance line appearing in both a voice spoke and a format spoke is drift, not redundancy, and Meridian flags it at the sweep.

**Authoring lane:** a new spoke is a `.md` file, so HANK writes it behind [the_prompter]'s `%shipit`. Peggy never authors a spoke; Meridian never authors a spoke. The SPOKE INDEX row above is written in the SAME action that creates the file, never as a follow-up — a spoke is not "done" until it is indexed. `%sync` follows, per the Drive File ID Retrieval rule.

**Status discipline:** a spoke earns `[O]` at creation and `[C]` only when a live draft has run through it and [the_prompter] has confirmed the result (`EvalHyp`). A voice that has never produced a confirmed draft is a hypothesis wearing a name.

---
