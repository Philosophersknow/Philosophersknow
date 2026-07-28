# AIIPD Course Coach Avatar — Product Specification

**Product:** AI course coach embedded in the AIIPD Civic Intelligence subscription platform
**Version:** 0.1 (initial spec for development)
**Author:** Liam Michael Clancy
**Date:** 15 June 2026

---

## 1. What It Is

The AIIPD Course Coach is an AI-powered conversational assistant embedded in the subscription platform. It is trained on the DRMC framework, the council benchmarking methodology, the VET/AI policy research, and the assessment criteria for all AIIPD training packages.

Its purpose is to **give every subscriber access to expert support** — the kind of substantive, contextual, framework-specific guidance that currently only comes from a human consultant or facilitator.

It is not a generic AI chatbot. It speaks the language of the DRMC, understands the 26 domains, can explain the Relational Spectral Coding approach, can walk a student through what good assessment evidence looks like, and can apply the principles to real-world scenarios a subscriber brings to it.

---

## 2. What It Does

### 2.1 Course Content Questions

The coach answers any question about course content with framework fidelity. Examples:

> "Can you explain Domain 7 and give me an example of how it applies to a planning decision?"

> "What's the difference between compliance reporting and relational accountability?"

> "I'm writing up my council benchmarking report for Holdfast Bay — which domains are most relevant to their 2025 Annual Report?"

> "Explain the Composite Frequency Index to me like I have no research background."

The coach does not invent content. It draws from the published framework, the DRMC book, the appendices, and the course materials. Where it doesn't know, it says so and directs the student to the right resource.

### 2.2 Assessment Guidance

The coach helps students understand assessment criteria, structure their responses, and check their own work before submission. It does not write assessments for students — it guides them.

Examples:

> "I'm writing my council analysis reflection. What are the key things the assessor is looking for in the relational accountability section?"

> "Here is my response to Assessment Task 2. What's missing or unclear from a DRMC perspective?"

> "Can you give me an example of a strong answer to the 'Community Voice as Evidence' assessment criterion?"

The coach provides:
- Worked examples for each assessment criterion (drawn from the approved example bank)
- Criterion-by-criterion scaffolding questions that help students build their own answer
- Feedback prompts ("What evidence do you have for that claim?" / "Which of the 26 domains is most relevant here?")

### 2.3 Workplace Application Support

The coach helps practitioners apply DRMC principles to their actual work. This is where the subscription pays for itself.

Examples:

> "I'm a community engagement officer at a regional council. We're doing a consultation on a major infrastructure project. What does the DRMC say about how to do this well?"

> "I'm a councillor who has just received a budget brief. What questions should I be asking that the budget probably doesn't answer?"

> "My organisation is an RTO. How should we be thinking about AI in assessment under the DRMC ethical framework?"

The coach applies DRMC principles to specific, user-generated scenarios — making it a live professional tool, not just a study aid.

### 2.4 Reflective Practice (Mirror Integration)

The coach is integrated with the Mirror app. When a subscriber makes a journal entry in the Mirror, the coach can:
- Ask follow-up questions to deepen reflection
- Prompt the subscriber to identify which DRMC domain their experience relates to
- Suggest relevant course content or assessment connections
- Track recurring themes across journal entries over time and surface them

See the Mirror specification for detail.

---

## 3. Avatar Identity

The coach has a consistent persona — not a customer service bot, not a generic AI assistant.

**Name:** Iris (provisional — for review)

**Character:** A sharp, warm, intellectually honest research and practice guide. Speaks clearly. Does not over-qualify. Gives direct answers when it has them. Acknowledges uncertainty without apology. Has read everything. Understands that the people using this platform are professionals and should be treated as such.

**Tone:** The way a very good academic supervisor or policy mentor speaks — engaged, specific, rigorous, occasionally funny, never condescending.

**What Iris never does:**
- Fabricate citations or framework content
- Produce assessment answers on behalf of students
- Speak in the vague, hedge-everything style of generic AI assistants
- Pretend to have emotions or experiences it doesn't have

**What Iris always does:**
- Stay within the DRMC framework and AIIPD content
- Cite which part of the course or framework she is drawing from
- Direct users to the Mirror for personal reflection
- Remind users that framework application requires human judgement

---

## 4. Technical Architecture (Outline for Codex)

### 4.1 Knowledge Base

The coach is built on a Retrieval-Augmented Generation (RAG) architecture with the following source documents:

| Document | Status | Priority |
|---|---|---|
| DRMC Council Benchmarking manuscript (104,000 words) | In repo | High |
| DRMC 26-Domain Coding Matrix (Appendix A) | In repo | High |
| Assessment criteria and rubrics (all courses) | To be created | High |
| Worked assessment examples (approved bank) | To be created | High |
| AI in FE & Skills UK Edition | In repo | Medium |
| Community Survey Instrument (Appendix C) | In repo | Medium |
| AI Research Prompt Pack (Appendix G) | In repo | Medium |
| Ethical Use Protocol (Appendix F) | In repo | Medium |

### 4.2 System Prompt Architecture

The coach system prompt must:
- Establish Iris's identity, tone, and constraints
- Define the allowed knowledge base and how to handle out-of-scope questions
- Set the citation format (must reference which document/chapter/appendix)
- Define the assessment guidance guardrails (scaffold, don't write)
- Set the Mirror integration behaviour

### 4.3 Interface

- Embedded chat widget in the AIIPD subscriber dashboard
- Available on web and mobile (responsive design)
- Persistent conversation history per subscriber (searchable)
- Mirror integration: coach can read and respond to Mirror entries with subscriber permission
- Export: subscribers can export a coaching conversation as a PDF (useful for reflective practice evidence)

### 4.4 Model Recommendation

Use Claude Sonnet 5 (claude-sonnet-5) with:
- Extended context (full DRMC book + appendices in context)
- Tool use enabled (for searching specific appendix sections, retrieving assessment criteria)
- Prompt caching enabled for the large static knowledge base (cost reduction)

---

## 5. Assessment Example Bank (To Be Built)

For each assessment task in each course, the example bank provides:
- One exemplary response (high-distinction level) with examiner annotations
- One acceptable response (pass level) with notes on what is missing
- One insufficient response (fail level) with explanation of the gaps
- A set of scaffolding questions the coach can use to guide students toward the exemplary level

**Priority assessment tasks for initial build:**
1. DRMC domain identification in a real council document
2. Relational accountability analysis (trust, fairness, belonging, ecological stewardship)
3. Community voice as evidence — applying the concept to a local case
4. Consultation quality assessment using the RSC Zone Guide
5. AI in FE — applying the international comparison framework to a provider scenario
6. Ethical use protocol application

---

## 6. Consumer Market Strategy

The course coach is central to the consumer market proposition. It transforms the AIIPD training packages from static content (a book, a report, a PDF) into a **living learning environment**.

**The pitch:** You get the research, the framework, the tools — and an expert guide available at any hour who can answer your specific questions and apply the framework to your actual work.

**Price anchor:** The course coach is included in the subscription (£39/month individual). It is the single biggest differentiator from a one-time report purchase. It is what justifies ongoing subscription rather than a one-time buy.

**Onboarding flow:**
1. New subscriber → welcome email with free briefing attached
2. Subscriber dashboard opens with Iris greeting and three suggested starting questions
3. First interaction guides subscriber to identify their role (councillor / officer / researcher / educator / student)
4. Iris tailors subsequent suggestions to that role
5. Mirror integration unlocked after first 3 coach interactions

---

## 7. Future Development

- **Voice interface:** Iris as an audio coach (podcast-style delivery of framework content, accessible via mobile during commute)
- **Group mode:** Iris can facilitate group discussions in council or provider team learning sessions
- **Assessment submission integration:** Iris gives formative feedback on draft assessment submissions before formal submission
- **Research assistant mode:** For PhD and postgraduate users, Iris can assist with literature review, methodology checking, and DRMC application in academic papers

---

*This spec is a draft for Liam's review. Development dependencies: AIIPD subscriber platform (Next.js/Prisma), knowledge base chunking and vector embedding pipeline, Anthropic API integration. See docs/handover for technical architecture context.*
