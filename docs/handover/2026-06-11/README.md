# Developer Handover Pack — 11 June 2026

## Purpose

This folder contains a draft developer handover pack for the AiIPD platform and the Hearts Co-op website and proposed back office. It is intended as the entry point for any developer, AI agent, or team member picking up work on either platform.

This pack was prepared without direct access to the live codebase. It is built from the AIIPD Master Technical Specification (versions 0.1 and 0.2) and from a brief supplied by Liam Michael Clancy on 11 June 2026. Every fact, figure, or architectural detail that could not be sourced directly from the Master Specification is marked `[VERIFY: ...]` with a note describing what needs to be checked once the live codebase is available.

Markdown is the authoritative source for this pack. DOCX generation is out of scope for this pass.

---

## Relationship to the AIIPD Master Specification and Content Architecture

This pack sits alongside, and does not replace, the following:

- `/content/governance/master-technical-specification/AIIPD_MASTER_TECHNICAL_SPECIFICATION.md` (v0.1, original draft)
- `/content/governance/master-technical-specification/AIIPD_MASTER_TECHNICAL_SPECIFICATION_v0.2.md` (v0.2, updated draft)
- `/content/governance/style-guide.md` (AIIPD Civic Intelligence Editorial Style Guide)
- The wider Civic Intelligence content architecture under `/content/`, listed in the Master Specification v0.2, section 24.2

Where this pack restates information from the Master Specification (for example, current routes, Prisma models, or environment variables), it cites the relevant section number so that updates to the Master Specification can be traced through to this pack. Where this pack introduces information from the 11 June 2026 brief that is not yet in the Master Specification (for example, additional routes, the 28-model figure, or the evidence snapshot figures), that information is marked `[VERIFY]` and should eventually be reconciled into an updated version of the Master Specification.

Terminology in this pack follows the AIIPD style guide where describing product or platform concepts (Civic Intelligence, Place Intelligence, Intelligence Brief, and so on), but technical identifiers — route names, Prisma model names, environment variable names, file paths — are kept exactly as they appear in the codebase and Master Specification. They are not "intelligence-washed".

---

## Documents in This Pack

| File | Description |
|---|---|
| `00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md` | Instructions for Codex to publish the AiIPD application codebase and the Hearts Co-op codebase to GitHub, enabling live verification of this pack |
| `01_AiIPD_Current_Website_and_Backend_Specification.md` | Current-state specification of the AiIPD public website, authenticated application, technology stack, route map, data flows, authentication, environment variables, database schema, security/privacy requirements, and known limitations |
| `02_AiIPD_Project_Progress_and_12_Week_Launch_Pipeline.md` | Evidence snapshot, current gates blocking pilot launch, a twelve-week staged roadmap, post-launch pipeline phases, and a risks register |
| `03_Hearts_Coop_Current_Website_Specification.md` | Draft current-state specification of the Hearts Co-op static website, including content structure, branding, domain, and acceptance requirements |
| `04_Hearts_Coop_Back_Office_Foundation_Specification.md` | Proposed foundation specification for a separate Hearts Co-op back-office platform, including modules, roles, core entities, and the AiIPD integration pattern |

---

## Recommended Reading Order

1. **Document 1** — establishes the current state of the AiIPD codebase, route map, database, and known limitations. Read this first; it is the factual foundation for Document 2.
2. **Document 2** — builds on Document 1 to describe current gates and a twelve-week roadmap to a protected pilot and beyond.
3. **Document 3** — a separate but related current-state document for the Hearts Co-op website. Can be read independently of Documents 1 and 2, but references the same status legend.
4. **Document 4** — a forward-looking, proposed specification for a Hearts Co-op back office, which depends on understanding both Document 3 (the website it would extend) and Document 1, section 8.3 (the AiIPD integration pattern it would consume).

---

## Status Legend

The same status legend is used across all four numbered documents:

| Status | Meaning |
|---|---|
| **Confirmed** | Verified directly against the live codebase, database, or running environment. |
| **Built but unverified** | Code or configuration exists in the repository or Master Specification but has not been run or tested in this environment. |
| **Configured** | An environment variable, service, or integration has been set up but its operational status has not been confirmed. |
| **Blocked** | A known issue prevents the feature, build step, or workflow from functioning as intended. |
| **Proposed** | Not yet built. Described as a target or future requirement in the Master Specification or this handover pack. |

---

## Draft Status and Verification

This is a **draft pack**. Figures, route lists, schema groupings, and architectural details marked `[VERIFY]` throughout these documents require confirmation by Codex once the live codebase is pushed to GitHub. See `00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md` in this folder for the steps required to make the AiIPD application codebase and the Hearts Co-op codebase available for that verification.

Until that verification happens, treat every `[VERIFY]` item as unconfirmed, and do not present figures or architectural claims from this pack as established fact in any external-facing document.

---

## Routing Key for Claude/Codex Handoffs

Handoffs between Claude and Codex relating to this pack, and to the AiIPD and Hearts Co-op codebases generally, use the routing key:

```text
AIIPD-BRIDGE-CLAUDE-TO-CODEX-V1
```

Per the AIIPD Master Specification v0.2, section 24.3: Codex handles technical implementation, build fixes, schema migrations, and code generation; Claude handles content strategy, intelligence framing, report templates, AI prompts, and editorial review. This pack itself was prepared by Claude and is intended to be verified and updated by Codex.
