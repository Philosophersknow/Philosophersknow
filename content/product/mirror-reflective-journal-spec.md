# The Mirror — Reflective Journal and Professional Development Tool
## Product Specification v0.1

**Status:** Design specification for development
**Author:** Liam Michael Clancy
**Date:** 15 June 2026
**Platform:** AIIPD Civic Intelligence (aiipd.com.au) — subscriber feature

---

## 1. What the Mirror Is

The Mirror is a structured reflective journal embedded in the AIIPD subscriber platform. It is not a diary app. It is a professional development and learning instrument built on the DRMC framework — designed to help practitioners, students, and elected representatives reflect on their experiences in a way that builds capacity over time.

The Mirror's central proposition is this: **the most powerful professional development resource available to most people is their own direct experience — but only if they can see it clearly.** The Mirror is the instrument that makes that possible.

It uses the DRMC 26-domain framework as a reflective lens, the AIIPD course coach (Iris) as a thinking partner, and a structured journaling process to help users:

- Identify what relational dynamics are actually at play in their professional situations
- Track patterns across time (what domains recur, where growth is happening, where stuck patterns persist)
- Build evidence of professional learning and practice development
- Connect lived experience to framework knowledge and assessment criteria

---

## 2. Core Functionality

### 2.1 Journal Entry Creation

The subscriber opens a new entry with a simple prompt:

> *What happened? What did you notice? What are you trying to understand?*

No format is required. The entry can be free-form text — a paragraph, a page, a single sentence. The subscriber writes what they actually experienced, thought, or observed.

After submission, the Mirror processes the entry through two layers:

**Layer 1 — DRMC Domain Tagging**
The entry is automatically analysed to identify which of the 26 DRMC domains are present in the experience described. Tags are suggested (not imposed) — the subscriber can accept, reject, or add their own. This is the mechanism that connects lived experience to the framework.

Example: A subscriber writes about a community meeting where they felt residents were not genuinely heard. The Mirror suggests Domain 7 (Community Voice and Representation), Domain 3 (Trust and Relational Capital), and Domain 14 (Consultation Integrity). The subscriber can confirm these and add Domain 5 (Place Attachment and Identity) based on their own reading.

**Layer 2 — Coach Prompt (Optional)**
After domain tagging, the Mirror offers to open a coaching conversation with Iris about the entry. This is not automatic — the subscriber chooses. Iris can:
- Ask deepening questions ("What did you notice about how the facilitator responded to that question?")
- Connect the experience to specific course content ("Chapter 6 of the DRMC book addresses exactly this dynamic — want me to walk you through the relevant passage?")
- Suggest assessment connections ("This experience directly relates to Assessment Task 3 — would it be useful to draft a reflection now while it's fresh?")

### 2.2 Pattern Tracking

The Mirror tracks tagged domains across all entries over time and presents the subscriber with:

- **Domain frequency map:** which of the 26 domains appear most often in their lived experience (visualised as a heat map of the coding matrix)
- **Temporal patterns:** how domain patterns shift across weeks or months (growth, recurring challenges, emerging awareness)
- **Reflection depth score:** a simple indicator of how analytical versus descriptive entries have become over time (not a grade — a development signal)

This tracking turns the Mirror from a collection of isolated journal entries into a developmental portrait.

### 2.3 Assessment Evidence Export

For subscribers completing AIIPD courses or using the Mirror for CPD (continuing professional development), any entry or set of entries can be exported as a structured reflection document. The export:

- Includes the raw entry text
- Shows the domain tags applied
- Includes any coach exchange linked to the entry
- Maps the reflection to specific assessment criteria or CPD competency frameworks

This export can be submitted as reflective evidence for assessment, used in performance reviews, or included in professional portfolios.

### 2.4 Prompted Reflection Templates

For subscribers who prefer structure, the Mirror offers a set of templated prompts organised by context:

| Template | For |
|---|---|
| After a council meeting | Councillors and council officers |
| After a community consultation | Community engagement practitioners |
| After delivering training or assessment | VET/FE educators and assessors |
| After receiving Ofsted/ASQA feedback | Training provider staff |
| After a significant decision | Any practitioner or elected member |
| End-of-month practice review | CPD/professional development focus |
| After reading a course chapter | Students in AIIPD courses |
| After a difficult conversation | Any practitioner |

Each template uses DRMC-informed prompts to scaffold the reflection. For example, the "after a council meeting" template asks:

1. What was formally on the agenda? What was informally driving the conversation?
2. Who was heard? Who wasn't? Why might that be?
3. Which DRMC domains feel most relevant to what happened?
4. What would you do differently — and what framework principle supports that?
5. What do you need to understand better?

### 2.5 Privacy and Data

All Mirror entries are private by default. The subscriber alone can see their entries. No entry content is used to train models or shared with third parties. Coach conversations linked to Mirror entries are stored only for the subscriber's use.

Subscribers can:
- Make individual entries private, semi-private (visible to a nominated supervisor), or shareable (for group reflection in organisational subscriptions)
- Export or delete all their data at any time
- Control whether the coach can read their Mirror entries at all

---

## 3. User Journeys

### 3.1 The Student

A subscriber completing the DRMC Council Benchmarking course uses the Mirror to:
- Log observations from their workplace or community that relate to course content
- Draft and refine reflective assessment tasks with coach support
- Track which domains they are most confident about (and which they are avoiding)
- Export a portfolio of reflective entries as assessment evidence at course completion

### 3.2 The Councillor

An elected councillor subscribes and uses the Mirror to:
- Debrief after council meetings — identifying what was really happening beneath the agenda
- Develop their own analysis of community dynamics in their ward
- Build a record of their decision-making reasoning over their term of office
- Prepare for accountability conversations with their community

### 3.3 The FE Educator

An FE college teacher subscribes during an Ofsted preparation period and uses the Mirror to:
- Reflect on AI-related issues arising in their classroom
- Track their own professional development around AI governance
- Build evidence of reflective practice for their Ofsted inspection portfolio
- Access coaching support when facing novel assessment integrity questions

### 3.4 The Council Officer

A community engagement manager uses the Mirror to:
- Log consultation experiences and analyse them against the DRMC framework
- Identify patterns in how their organisation handles community feedback
- Build a professional development narrative for annual review
- Connect their practice to the DRMC's distinction between authentic consultation and tokenistic process

---

## 4. Interface Design Principles

**Frictionless entry:** The Mirror should take less than 60 seconds to open a new entry from the subscriber dashboard. No loading screens. No mandatory fields. Write first, structure later.

**Minimal and calm:** The visual design reflects the Mirror name — clean, quiet, white space dominant. The journaling canvas is not cluttered with features. Everything non-essential is hidden until needed.

**Depth on demand:** Advanced features (domain mapping, pattern tracking, coach integration, export) are available but not forced. A subscriber who just wants to write can just write.

**Mobile-first:** Most reflection happens in the moments after meetings, consultations, or significant events — on a phone, in a car park, on a train. The Mirror must work beautifully on mobile.

---

## 5. Technical Requirements (For Codex)

- **Storage:** Encrypted journal entry storage per subscriber (PostgreSQL, encrypted at rest)
- **NLP layer:** DRMC domain classification model or RAG-based domain tagging (Claude API with 26-domain matrix as context)
- **Coach integration:** Shared session state between Mirror entry and Iris coach (subscriber-permission-gated)
- **Visualisation:** Domain frequency heat map using D3.js or Recharts (26-cell grid representing the matrix)
- **Export:** PDF generation for assessment evidence export (structured format, AIIPD branded)
- **Authentication:** Integrated with AIIPD subscriber authentication (Next.js auth + Prisma)
- **Mobile:** Responsive Next.js frontend; consider PWA for offline entry (sync when connected)

---

## 6. Companion Resources

The Mirror is complemented by:

- **Reflective Practice Guide:** a short (10-page) PDF subscriber resource explaining what reflective practice is, why the DRMC framework makes it more powerful, and how to use the Mirror effectively
- **Domain Quick Reference Card:** a one-page subscriber resource listing all 26 domains with one-sentence definitions — to use while reading a journal entry and deciding on tags
- **Monthly Review Template:** a structured PDF that subscribers complete at month-end, drawing on their Mirror entries to identify key learning, domain patterns, and next development priorities

---

## 7. Subscription Positioning

The Mirror is the **retention mechanism** of the subscription model. A subscriber's journal is their personal professional development record, built over months and years. The Mirror makes the subscription genuinely irreplaceable — the subscriber's own reflective history cannot be taken with them if they leave. 

This is not a dark pattern — it is an honest value proposition: the longer you use the Mirror, the more valuable your subscription becomes, because your developmental record deepens. The first month's value is the course content and coach. The twelfth month's value is a year of reflective development that you can see, map, and demonstrate.

---

*This specification is a draft for Liam's review and Codex implementation. Development dependencies: AIIPD Next.js platform, Claude API integration, subscriber database. See `docs/handover` for platform architecture.*
