# Change Summary: AIIPD Master Technical Specification v0.1 to v0.2

Date: 6 June 2026  
Prepared by: Claude (on behalf of Liam Michael Clancy / AIIPD)  
Status: Awaiting owner review and approval

---

## Note on Source File Preservation

The original v0.1 source file is preserved unchanged at:
`/content/governance/master-technical-specification/AIIPD_MASTER_TECHNICAL_SPECIFICATION.md`

The v0.2 update is a new file at:
`/content/governance/master-technical-specification/AIIPD_MASTER_TECHNICAL_SPECIFICATION_v0.2.md`

No changes were made to the original v0.1 file.

---

## Change Table

| # | Section | Change | Type | Reason |
|---|---|---|---|---|
| 1 | Header block | Version updated from 0.1 to 0.2; status updated to "Updated draft — awaiting owner review and approval" | Structural update | Version control and approval workflow |
| 2 | Section 1 — Purpose | Added paragraph explicitly naming the five Intelligence Centres and stating the unified intelligence architecture | Structural addition | Makes the platform's architecture explicit at the outset |
| 3 | Section 2.1 — Intelligence Centres | Added sixth item: Cross-Centre Intelligence Infrastructure | Structural addition | Formalises the shared infrastructure that supports all five centres |
| 4 | Section 3.1 — Public Static Website (current role) | Replaced "council benchmarking" with "Place Intelligence" in the description of homepage content areas | Terminology update | Aligns with AIIPD Civic Intelligence content style guide |
| 5 | Section 3.1 — Public Static Website (development rules) | Added two new rules: style guide alignment note; URL path migration note for `council-benchmark/` to `civic-intelligence/` with migration note | Structural addition + migration note | Ensures terminology alignment and flags navigation work needed |
| 6 | Section 3.2 — Next.js Application (current role) | Added migration note to "Council Intelligence Dashboard" entry, flagging rename to "Civic Intelligence Centre" | Migration note | Terminology alignment — Prisma/code identifier not changed in place |
| 7 | Section 3.3 — Database and ORM (major models) | Added migration note to `BenchmarkScore` entry flagging rename to `IntelligenceScore` | Migration note | Terminology alignment — Prisma model name not changed in place |
| 8 | Section 3.3 — Database and ORM (report types) | Added migration note to `BENCHMARK` entry; added full target report type nomenclature block with four renamed enum values and migration guidance | Migration note + structural addition | Establishes clear migration path for report type enum; preserves existing values until migration complete |
| 9 | Section 6.1 — Core Data Principles | Added "Intelligence outputs must also carry" list with five required metadata fields | Structural addition | Formalises intelligence product metadata requirements |
| 10 | Section 9.1 — Blog and Resource Publishing | "Intelligence briefs" updated to "Intelligence Briefs" (capitalised for consistency) | Terminology update | Aligns with Intelligence Centres naming conventions |
| 11 | Section 11.3 — Required Report Generator Improvements | Added report naming taxonomy block covering all five Intelligence Centres with specific output names; added style guide reference | Structural addition | Establishes authoritative naming for all report types; links to style guide for full reference |
| 12 | Section 17 — Security, Privacy and Ethics | Added new subsection 17.4 — Intelligence Framing Safeguards with six requirements for all intelligence outputs | Structural addition | Formalises ethical and framing safeguards for all AI-assisted outputs |
| 13 | New Section 24 — Content and Terminology Governance | Added entire new section covering: Style Guide Reference (24.1), Content Architecture table of 17 content files (24.2), Codex-to-Claude Routing key (24.3), Missing AGENTS.md note (24.4) | Structural addition | Reconciles content architecture with technical specification; provides authoritative reference for all platform content files |

---

## Terminology Replacements Applied

| Old Term | New Term | Notes |
|---|---|---|
| "council benchmarking" | "Place Intelligence" | Applied in Section 3.1 current role |
| "Council Intelligence Dashboard" | "Civic Intelligence Centre" | Applied as migration note in Section 3.2 (code identifier not changed) |
| "BenchmarkScore" | "IntelligenceScore" | Applied as migration note in Section 3.3 (Prisma model name not changed) |
| "BENCHMARK" (report type) | "PLACE_INTELLIGENCE_REPORT" | Applied as migration note and target nomenclature in Section 3.3 |
| "council-benchmark/" (URL path) | "civic-intelligence/" | Applied as migration note in Section 3.1 |
| "Intelligence briefs" | "Intelligence Briefs" | Capitalisation consistency in Section 9.1 |

---

## Terms NOT Changed (Preserved as Migration Notes Only)

The following identifiers were flagged with migration notes but NOT changed in place, as they are Prisma model names, file paths, or code identifiers:

- `BenchmarkScore` Prisma model name — migration note added only
- `BENCHMARK` enum value — migration note added, target value specified
- `council-benchmark/` URL path — migration note added only
- "Council Intelligence Dashboard" code references — migration note added only

---

## Open Items Requiring Liam's Decision

| # | Item | Required Decision |
|---|---|---|
| 1 | AGENTS.md file | Approve content and creation of AGENTS.md to define agent roles and handoff protocols between Claude and Codex. Currently flagged as missing in Section 24.4. |
| 2 | Phase 0 migration scope | Confirm which migration notes in this specification are approved for Phase 0 implementation (BenchmarkScore rename, report type enum updates, URL path changes). |
| 3 | Style guide existence | Confirm whether `/content/governance/style-guide.md` exists and is current — this file is referenced multiple times in v0.2 as the authoritative terminology source. |
| 4 | Content architecture files | Confirm which of the 17 content files listed in Section 24.2 exist and are current. Table lists intended architecture — actual file inventory should be verified. |
| 5 | Report type enum migration | Approve the four target enum values (PLACE_INTELLIGENCE_REPORT, EXECUTIVE_INTELLIGENCE_BRIEF, BUDGET_IMPACT_INTELLIGENCE, COUNCIL_INTELLIGENCE_PROFILE) before Codex implements schema migration. |

---

## What Was Not Changed

- No Prisma model names were changed in the specification.
- No file paths were changed in the specification.
- No code identifiers were changed in the specification.
- All existing section numbers 1–23 were preserved (Section 24 is new).
- All original technical requirements, roadmap phases, and open decisions were preserved unchanged.
- The original v0.1 source file was not modified.
