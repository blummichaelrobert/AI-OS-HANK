In professional communication, business emails fall into clear, distinct categories based on **semantic intent**, **target audience**, and **expected outcome**.

Here is the standard taxonomy of professional business emails, organized by their core purpose, typical length, and semantic intent.

---

### Professional Email Taxonomy

| Category | Email Type | Semantic Intent | Primary Goal | Target Length |
| --- | --- | --- | --- | --- |
| **Outreach & Direct Sales** | **Cold Outreach** | Curiosity, Value Proposition | Get a reply or schedule an initial discovery call. | Short (75–150 words) |
|  | **Sales Follow-Up** | Persistence, Urgency, Friction Removal | Re-engage a prospect and move them to the next stage of the funnel. | Very Short (50–100 words) |
|  | **Warm Introduction** | Social Proof, Trust Transfer | Connect two third parties for mutual professional benefit. | Short (75–125 words) |
| **Relationship & Customer Success** | **Welcome / Onboarding** | Orientation, Reassurance | Guide a new client, customer, or user through their first steps. | Medium (150–300 words) |
|  | **Client Check-In / Health Check** | Relationship Maintenance, Proactive Service | Gauge satisfaction, identify risks, and surface expansion opportunities. | Short (100–150 words) |
|  | **Customer Win-Back / Re-engagement** | Incentivization, FOMO | Reactivate dormant accounts, past clients, or inactive leads. | Short (100–175 words) |
| **Operational & Internal** | **Status / Progress Update** | Alignment, Accountability | Inform stakeholders of project milestones, blockers, and timelines. | Medium (150–300 words) |
|  | **Decision / Approval Request** | Authority, Urgency, Scarcity | Secure an explicit "Yes/No" decision or sign-off from a manager/executive. | Very Short (50–120 words) |
|  | **Meeting Agenda / Pre-Read** | Preparation, Context Setting | Ensure meeting participants arrive informed and ready to make decisions. | Medium (150–250 words) |
| **Marketing & Lead Nurturing** | **Value / Educational Nurture** | Authority, Education | Build trust over time by sharing actionable industry insights. | Medium to Long (300–800 words) |
|  | **Product Announcement / Launch** | Excitement, Innovation | Drive awareness and adoption for a new feature, service, or product. | Short to Medium (150–300 words) |
|  | **Case Study / Social Proof** | Validation, Risk Reduction | Demonstrate real-world ROI and success stories to prospects. | Medium (250–500 words) |

---

### Module 4: Email Format System Prompt Rules

Here is the modular rule set to plug into your LLM agent alongside your voice rules (Halbert, Ogilvy, Wells Lawrence, or Kennedy).

```text
[TASK]
You will receive a CONCEPT and an EMAIL TYPE to write. 
First, adopt the loaded VOICE RULES. 
Second, apply the loaded VOICE to the following EMAIL FORMAT TEMPLATE.

[EMAIL FORMAT RULES]
1. SUBJECT LINE: Must reflect the voice's core mechanic (e.g., curiosity, direct benefit, high urgency, or authority). Keep under 60 characters.
2. PREHEADER / PREVIEW TEXT: 1 short line (under 90 characters) that complements the subject line.
3. SALUTATION & GREETING: Match the tone of the voice rules (e.g., Ogilvy = formal/gentlemanly, Halbert = intimate/direct, Kennedy = zero-fluff).

[TEMPLATED EMAIL STRUCTURE]

1. THE SUBJECT LINE & PREHEADER
   - Subject: [Subject Line]
   - Preheader: [Preview Text]

2. THE OPENING HOOK (1–2 sentences)
   - State the reason for writing immediately, or open with a voice-matched story/fact/statement.

3. THE CORE BODY (Length matched to Email Type)
   - Deliver the central value proposition, update, or argument.
   - Use short, single-idea paragraphs (1–3 sentences each).
   - Use bullet points or bold text where appropriate for scannability.

4. THE CALL TO ACTION (CTA)
   - Single, frictionless next step (e.g., reply to this email, click a link, confirm an approval, or pick a time).
   - Never offer multiple competing calls to action in a single email.

5. THE SIGN-OFF & P.S.
   - Sign-off matched to the persona's voice.
   - P.S. SECTION (Optional/Voice-dependent): Use a P.S. line to reinforce the primary benefit, restate urgency, or add a secondary curiosity hook.

```

---