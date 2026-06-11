# Hearts Co-op Back Office Foundation Specification

**Version:** 0.1-draft
**Date:** 11 June 2026
**Status:** PROPOSED — foundation specification for future build

---

## Status Legend

This legend applies across all four documents in this handover pack.

| Status | Meaning |
|---|---|
| **Confirmed** | Verified directly against the live codebase, database, or running environment. |
| **Built but unverified** | Code or configuration exists in the repository or Master Specification but has not been run or tested in this environment. |
| **Configured** | An environment variable, service, or integration has been set up but its operational status has not been confirmed. |
| **Blocked** | A known issue prevents the feature, build step, or workflow from functioning as intended. |
| **Proposed** | Not yet built. Described as a target or future requirement in the Master Specification or this handover pack. |

This entire document is **Proposed**. Nothing described here exists in any codebase as of 11 June 2026.

---

## Executive Summary

This document is a forward-looking foundation specification for a Hearts Co-op back-office platform. It describes a separate Next.js, TypeScript, and Supabase-based platform with its own repository, its own database, and its own data governance, distinct from both the Hearts Co-op public website (Document 3) and the AiIPD platform (Documents 1 and 2).

The Hearts Co-op back office would serve as the operational system for member and household management, governance, meetings, projects, and related co-operative functions. Where the back office needs civic or place-based intelligence (for example, intelligence about a council area where Hearts Co-op operates a project), it would consume AiIPD intelligence through a server-side, read-only, scoped-token integration, following the entitlement model described in the AIIPD Master Specification, section 6.3. AiIPD would not have write access to Hearts Co-op data, and Hearts Co-op would not have direct access to the AiIPD database.

This specification defines initial modules, roles, core entities, the AiIPD integration pattern, and explicit exclusions for a foundation minimum viable product (MVP). It is intended as a starting point for design and scoping discussions, not as an implementation plan with timelines.

---

## 1. Architecture Overview

The Hearts Co-op back office is proposed as an independent platform with the following relationship to AiIPD:

```text
Hearts Co-op Back Office (separate repository, separate deployment)
  -> own Next.js / TypeScript application
  -> own Supabase PostgreSQL database
  -> own authentication and user management
  -> own data governance (member and household data)

  Modules:
    -> EOI and member CRM
    -> Governance
    -> Meetings
    -> Resolutions
    -> Tasks
    -> Documents
    -> Projects
    -> Compliance
    -> Communications
    -> Reporting

  Integration Boundary
    -> server-side, read-only calls to AiIPD intelligence API
    -> scoped tokens (entitlement-based, per AIIPD Master Specification section 6.3)
    -> no AiIPD write access to Hearts Co-op data
    -> no direct Hearts Co-op access to AiIPD database
    -> all integration calls audit-logged on the Hearts Co-op side

AiIPD Platform (separate repository, separate deployment)
  -> own Next.js / TypeScript application
  -> own Prisma / PostgreSQL (Supabase) database
  -> exposes a scoped, read-only intelligence API surface to authorised partners
```

The two platforms are connected only through the integration boundary. Hearts Co-op's database holds member, household, governance, and project data; AiIPD's database holds council, place, and evidence data. Neither database is shared or merged. The integration boundary exists so that Hearts Co-op staff can view relevant place intelligence (for example, council-level context for a project site) without Hearts Co-op operating its own civic intelligence ingestion pipeline, and without AiIPD holding Hearts Co-op member data.

`[VERIFY: confirm with Liam whether Hearts Co-op back office should be a fully separate repository from day one, or initially developed as a branch/folder within the shared philosophersknow repository per 00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md, section 6, with separation enforced at the database and deployment level rather than the repository level]`

---

## 2. Initial Modules

| Module | Purpose | Key Entities Involved |
|---|---|---|
| EOI and member CRM | Capture expressions of interest from the public website (Document 3), convert to member applications, manage member and household records | prospect, member, household, application, consent |
| Governance | Manage committees, board structure, and governance documentation | committee, member, document |
| Meetings | Schedule meetings, record attendance, link agendas and minutes | meeting, committee, document |
| Resolutions | Record formal resolutions arising from meetings, including voting outcomes and status | resolution, meeting, committee |
| Tasks | Track operational tasks arising from meetings, projects, or compliance obligations | task, project, member |
| Documents | Central document store for governance, project, and compliance documents | document, project, committee |
| Projects | Manage co-operative projects, including site information and task tracking | project, site, task |
| Compliance | Track regulatory and co-operative compliance obligations and their status | compliance obligation, audit event |
| Communications | Manage member communications, newsletters, and notices | member, household |
| Reporting | Generate operational and governance reports for the board and members | resolution, project, compliance obligation |

---

## 3. Roles

| Role | Description | Access Level |
|---|---|---|
| Administrator | Full platform administration, user management, and configuration | Full read/write across all modules |
| Board/Secretary | Manages governance records, meetings, resolutions, and compliance reporting | Read/write on governance, meetings, resolutions, compliance, reporting; read on members and projects |
| Staff Consultant | Day-to-day operational user managing members, projects, tasks, and communications | Read/write on EOI/CRM, projects, tasks, documents, communications; read on governance and compliance |
| Member | Co-operative member with limited self-service access (own profile, household, communications received) | Read/write on own member and household record; read on published communications and selected documents |
| Partner Viewer | External partner (for example, a project partner or funding body) with limited visibility into specific projects | Read-only on specified projects and related documents, scoped per partner |
| Auditor | Independent reviewer with read access to compliance, governance, and audit records for review purposes | Read-only on compliance, governance, audit events, and resolutions |

---

## 4. Core Entities

- **prospect** — A person who has submitted an expression of interest but is not yet a member.
- **member** — An individual who has been accepted into Hearts Co-op membership.
- **household** — A grouping of one or more members sharing a residence or family unit, where relevant to co-operative structure.
- **application** — A formal application for membership, linked to a prospect and tracked through to acceptance or decline.
- **consent** — A record of consent given by a prospect, member, or household for data processing, communications, or participation.
- **committee** — A governance body within Hearts Co-op (for example, the board or a working group).
- **meeting** — A scheduled gathering of a committee, with associated agenda, minutes, and attendance records.
- **resolution** — A formal decision recorded at a meeting, including its voting outcome and implementation status.
- **project** — A co-operative initiative or programme, which may involve one or more sites.
- **site** — A physical location associated with a project.
- **task** — An actionable item assigned to a staff consultant, board member, or committee, often arising from a meeting, project, or compliance obligation.
- **document** — A stored file (governance, project, compliance, or communications-related) with metadata and access controls.
- **partner** — An external organisation with a defined relationship to Hearts Co-op (for example, a funding body or project collaborator).
- **risk** — A recorded risk relevant to a project, compliance obligation, or the co-operative as a whole.
- **compliance obligation** — A regulatory or co-operative requirement that Hearts Co-op must meet, with a tracked status.
- **audit event** — A logged record of a significant action taken within the platform, supporting the audit trail required for governance and compliance review.

---

## 5. AiIPD Integration

The Hearts Co-op back office would integrate with AiIPD intelligence through a pattern that mirrors the entitlement model described in the AIIPD Master Specification, section 6.3 (Organisation and Entitlement Model).

Proposed integration pattern:

- Hearts Co-op is provisioned as an `Organisation` (or equivalent partner entity) within the AiIPD entitlement model, with a defined set of entitlements scoped to read-only intelligence access (for example, Place Intelligence for council areas relevant to Hearts Co-op projects).
- AiIPD issues a scoped API token to Hearts Co-op corresponding to this entitlement. The token grants read-only access to specified intelligence endpoints and council scopes only.
- All calls from the Hearts Co-op back office to the AiIPD intelligence API are made server-side (never from the browser), using the scoped token stored as an environment variable on the Hearts Co-op deployment.
- Every call to the AiIPD integration is logged on the Hearts Co-op side as an `audit event`, recording which user or process triggered the call, which AiIPD endpoint and scope was accessed, and when.
- The integration is strictly read-only. The Hearts Co-op back office cannot create, update, or delete any AiIPD record through this integration.
- If the entitlement is revoked or expires, the integration must fail gracefully (for example, by hiding the relevant intelligence panel) without affecting any other Hearts Co-op functionality.

`[VERIFY: confirm with AiIPD platform owner (Liam) the specific intelligence endpoints and council scopes Hearts Co-op would require, once the AiIPD API surface described in the Master Specification section 16 (target API groups) is implemented]`

---

## 6. Hearts Dollars

Hearts Dollars is documented here as a **future module**.

**No transactional ledger exists in the foundation MVP.** Any future Hearts Dollars functionality (for example, a community currency, points system, or internal credit mechanism) would require its own dedicated specification, including legal and regulatory review, before any transactional ledger, balance tracking, or value-transfer functionality is designed or implemented.

For the foundation MVP, no entity, schema, or module related to Hearts Dollars should be built. This section exists to record the future module as a placeholder for planning purposes only.

---

## 7. Explicit Exclusions for Foundation MVP

The following are explicitly **out of scope** for the foundation MVP and require legal and regulatory resolution before any implementation work begins:

- **Payments.** No payment processing, payment gateway integration, or invoicing functionality.
- **Lending.** No lending, credit, or loan-related functionality of any kind.
- **Stored value.** No stored-value accounts, wallets, prepaid balances, or equivalent mechanisms (this includes Hearts Dollars, see section 6).
- **Care case management.** No case management functionality for care services, support coordination, or client care records.
- **Housing finance.** No housing finance, rent management, mortgage, or tenancy financial functionality.

Each of these areas carries its own regulatory regime (for example, financial services licensing, consumer credit law, aged care or disability service standards, and housing/tenancy law depending on jurisdiction). None should be designed or scoped in detail until Hearts Co-op has obtained appropriate legal advice and, where applicable, regulatory approval or licensing for the specific activity.

---

## 8. Data Governance

### 8.1 Separation from AiIPD database

The Hearts Co-op database must be entirely separate from the AiIPD database (Document 1, section 8). No member, household, prospect, or application data should ever be written to or stored in the AiIPD database. The integration described in section 5 is read-only and one-directional (AiIPD to Hearts Co-op), and even that direction is limited to intelligence outputs, not personal data.

### 8.2 Privacy considerations for member and household data

- Member and household data (prospect, member, household, application entities in section 4) constitutes personal information and must be handled in accordance with applicable privacy law.
- Access to member and household data should be role-scoped per section 3 (for example, Partner Viewer and Auditor roles should not have direct access to personal member data beyond what is strictly necessary for their function).
- Data minimisation principles from the AIIPD Master Specification, section 17.1 ("store the minimum data required") apply equally to the Hearts Co-op back office, even though it is a separate platform.
- A privacy policy covering the back office's collection, storage, and use of member and household data should be developed alongside the EOI data handling review described in Document 3, section 6.3.

### 8.3 Consent tracking requirements

- The `consent` entity (section 4) must record what a prospect, member, or household has consented to (for example, communications, data sharing with partners, participation in specific projects), when consent was given, and any subsequent withdrawal of consent.
- Consent records should be retained even after a member's other records are deleted or anonymised, to the extent necessary to demonstrate compliance with applicable privacy law, but should not retain more personal data than necessary for that purpose.
- Any future integration that shares Hearts Co-op member data with a third party (including, hypothetically, AiIPD, though this is not currently proposed) would require explicit consent tracking before such sharing could occur. The integration described in section 5 does not involve sharing Hearts Co-op member data with AiIPD and therefore does not currently trigger this requirement, but this principle should guide any future change to the integration's direction or scope.

---

This document should be read alongside Document 3 (Hearts Co-op current website specification), which describes the public-facing EOI capture that would feed the "prospect" and "application" entities described in section 4 above, once the EOI form is connected to a back-office system rather than a `mailto:` link.
