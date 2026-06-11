# AiIPD Current Website and Backend Specification

**Version:** 0.1-draft
**Date:** 11 June 2026
**Status:** DRAFT — pending live verification by Codex

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

---

## Executive Summary

This document is a draft current-state specification for the AiIPD website and backend, prepared as part of a developer handover pack. It is built from the AIIPD Master Technical Specification (v0.1 and v0.2) and is intended to give an incoming developer (Codex, or any team member) an accurate starting picture of what exists, what is configured, and what remains to be verified once the live codebase is available on GitHub.

The platform currently consists of a static public website and an early-stage Next.js 15 / React 19 / TypeScript application backed by a Prisma schema against PostgreSQL (Supabase intended as the hosted provider). The authenticated application is a scaffold: a Civic Intelligence dashboard, an evidence workspace, a report workspace, and an admin import page, supported by a small set of API routes and NextAuth credentials-based authentication.

Several known issues are documented in the Master Specification, including a typed-route build failure and an incomplete ESLint migration. The brief that commissioned this handover pack also references additional routes, additional Prisma models, and additional limitations (public workspace access, missing middleware, a demo-backed report endpoint) that are not yet confirmed in the Master Specification and are marked `[VERIFY]` throughout this document.

This document should be read alongside Document 2 (progress and 12-week launch pipeline), which sets out the path from this current state to a protected pilot and beyond.

---

## 1. Current Public Website Architecture

Source: Master Specification v0.2, section 3.1.

- Primary file: `public/index.html`.
- Currently the public-facing AIIPD website.
- Hosted locally via static preview at `http://127.0.0.1:4173/index.html`. `[VERIFY: confirm current hosting location and whether this is still the active preview URL]`
- Contains: homepage, hero, intelligence centres, assistant demo, Place Intelligence, training, publishing, pricing, ethics, FAQ, contact, legal modals and footer.

Technical characteristics:

- Single large static HTML file.
- Embedded CSS.
- Embedded JavaScript for tabs, accordions, FAQ, guided assistant demo, contact success state and modal controls.
- Uses `public/assets/images` and `public/assets/data`.

Development rules carried forward from the Master Specification:

- Preserve existing anchors unless intentionally changing navigation.
- Keep the public demo assistant guided and labelled as sample scenarios.
- Do not claim live real-time analysis on the public static homepage.
- Terminology on the public site should align with the AIIPD Civic Intelligence content style guide (`/content/governance/style-guide.md`).
- The URL path `council-benchmark/` should be updated to `civic-intelligence/` in Phase 1 navigation work, with anchor references updated before the change is made.

---

## 2. Authenticated Application Architecture

Source: Master Specification v0.2, section 3.2.

Primary framework:

- Next.js 15.
- React 19.
- TypeScript.
- App Router under `src/app`.

Current role:

- Early authenticated platform scaffold.
- Civic Intelligence Centre (formerly described as "Council Intelligence Dashboard"; a Phase 0 rename to "Civic Intelligence Centre" is noted in the Master Specification).
- Evidence workspace.
- Report workspace.
- Admin import page.
- API assistant route.
- Report API route.

---

## 3. Technology Stack

| Layer | Technology |
|---|---|
| Frontend framework | Next.js 15 (App Router) |
| UI library | React 19 |
| Language | TypeScript |
| ORM | Prisma |
| Database | PostgreSQL, configured via `DATABASE_URL` |
| Hosted database provider (intended) | Supabase |
| Authentication | NextAuth, credentials provider, JWT session strategy |

`[VERIFY: confirm exact package versions, build tooling, and any additional libraries (e.g. validation, UI component libraries) once package.json is available]`

---

## 4. Route Map

### 4.1 Confirmed routes (Master Specification v0.2, section 3.2)

| Route | Status |
|---|---|
| `src/app/page.tsx` | Built but unverified |
| `src/app/evidence/page.tsx` | Built but unverified |
| `src/app/reports/page.tsx` | Built but unverified |
| `src/app/admin/import/page.tsx` | Built but unverified |
| `src/app/api/assistant/route.ts` | Built but unverified |
| `src/app/api/reports/route.ts` | Built but unverified |
| `src/app/api/auth/[...nextauth]/route.ts` | Built but unverified |

### 4.2 Additional routes referenced in the handover brief

These routes were named in the handover brief but are not yet listed in the Master Specification's current API section (section 16). Each requires confirmation that it exists and a description of its current behaviour.

| Route | Status |
|---|---|
| `GET /api/councils` | `[VERIFY: confirm exists and current behaviour]` |
| `GET /api/councils/:id/snapshot` | `[VERIFY: confirm exists and current behaviour]` |
| `POST /api/assistant` | `[VERIFY: confirm exists and current behaviour]` (note: `/api/assistant` route file is referenced in section 3.2 as `route.ts`; method-level behaviour to be confirmed) |
| `POST /api/onboarding` | `[VERIFY: confirm exists and current behaviour]` |
| `POST /api/reports` | `[VERIFY: confirm exists and current behaviour]` (note: `/api/reports` route file is referenced in section 3.2; method-level behaviour to be confirmed) |
| `GET /api/intelligence` | `[VERIFY: confirm exists and current behaviour]` |
| `GET /api/intelligence/:council` | `[VERIFY: confirm exists and current behaviour]` |

### 4.3 Target API groups (Proposed, Master Specification section 16)

The Master Specification describes a target API surface that the current routes are an early subset of:

```text
/api/auth/*
/api/organisations/*
/api/subscriptions/*
/api/entitlements/*
/api/uploads/*
/api/evidence/*
/api/projects/*
/api/reports/*
/api/publications/*
/api/moodle/*
/api/blog/*
/api/social/*
/api/schedules/*
/api/budget-impact/*
```

API requirements (Proposed): validate input with Zod or equivalent, enforce auth and organisation scope, log sensitive operations, return clear error messages, do not expose secrets, separate public demo routes from authenticated production routes.

---

## 5. Data Flows

This section is a narrative description based on Master Specification sections 6 (Data Architecture) and 11.2 (Report Pipeline). It describes the intended flow of evidence through the platform; the extent to which each stage is implemented in the current codebase requires verification.

### 5.1 Evidence and source data flow (section 6.1)

The data architecture is designed to preserve separation between distinct stages of evidence handling:

1. Raw public source data is ingested (for example, council documents, budget papers, public registers).
2. Uploaded client documents are received separately and kept organisation-scoped.
3. Structured extracted data is derived from raw sources and uploads.
4. AI-assisted suggestions are generated from structured data, clearly labelled as such.
5. Analyst interpretation is applied to AI-assisted suggestions.
6. Verified findings emerge once source verification status and confidence levels are assigned.
7. Published outputs are produced from verified findings, carrying source traceability through to the final report.

Every source-backed claim is intended to carry: source title, source URL or file reference, publication date where available, date accessed, source type, reliability rating, verification status, confidence level, analyst comments, related intelligence pathway, and related DRMC/RSC interpretation where applicable.

`[VERIFY: confirm which of these stages are implemented in the current Document, SourceVerification, and DrmcScoreClaim models, and which exist only as schema fields without supporting workflow]`

### 5.2 Report pipeline flow (section 11.2)

The intended report pipeline is:

```text
Project created
  -> sources selected
  -> evidence extracted
  -> claims generated
  -> source verification status assigned
  -> intelligence modules run
  -> draft report assembled
  -> analyst review
  -> client review
  -> approval
  -> export
  -> publication/archive
```

The Master Specification states that the current `src/lib/report-generator.ts` is a demo generator and should be replaced with a modular report engine (`report/types.ts`, `report/templates/`, `report/sections/`, `report/evidence-summary.ts`, `report/render-html.ts`, `report/render-pdf.ts`, `report/render-docx.ts`, `report/versioning.ts`, `report/review-workflow.ts`).

`[VERIFY: confirm current behaviour of /api/reports and src/lib/report-generator.ts — the brief describes this as a "demo-backed report endpoint", which suggests the pipeline above is not yet implemented end to end]`

---

## 6. Authentication

Source: Master Specification v0.2, section 14.1.

Current state:

- NextAuth credentials provider.
- Demo password via `DEMO_ADMIN_PASSWORD`.
- JWT session strategy.

Target state (Proposed):

- Production email/password or passwordless login.
- Organisation membership.
- Role-based and entitlement-based access.
- Optional SSO later for enterprise clients.

`[VERIFY: confirm whether route protection / middleware currently enforces authentication on any routes — the brief references "absent route protection" as a current gate]`

---

## 7. Environment Variables

Source: Master Specification v0.2, section 20.

| Name | Purpose | Required | Notes |
|---|---|---|---|
| `DATABASE_URL` | PostgreSQL connection string for Prisma | Yes | Supabase is the intended hosted provider |
| `DEMO_ADMIN_PASSWORD` | Demo administrator password for NextAuth credentials provider | Yes (current state) | To be replaced with production auth per section 14.1 |
| `ANTHROPIC_API_KEY` | API key for Claude/Anthropic model access (assistant route) | Yes | Never hard-code; keep out of version control |
| `NEXTAUTH_SECRET` | NextAuth session signing secret | Yes | Standard NextAuth requirement |
| `NEXTAUTH_URL` | Base URL for NextAuth callbacks | Yes | Must match deployment URL |
| `STRIPE_SECRET_KEY` | Stripe API secret key | Configured (Proposed use) | For subscriptions, product purchases, invoices (section 14.2) |
| `STRIPE_WEBHOOK_SECRET` | Stripe webhook signature verification secret | Configured (Proposed use) | For entitlement provisioning via webhooks |
| `MOODLE_BASE_URL` | Base URL of the Moodle LMS instance | Configured (Proposed use) | For Moodle integration (section 7) |
| `MOODLE_API_TOKEN` | Moodle Web Services API token | Configured (Proposed use) | Must use least-privilege service account; never hard-code |
| `GOOGLE_CLIENT_ID` | OAuth client ID for Google sign-in | Configured (Proposed use) | `[VERIFY: confirm whether Google OAuth is wired into NextAuth]` |
| `GOOGLE_CLIENT_SECRET` | OAuth client secret for Google sign-in | Configured (Proposed use) | `[VERIFY: confirm whether Google OAuth is wired into NextAuth]` |
| `LINKEDIN_CLIENT_ID` | OAuth client ID for LinkedIn integration | Configured (Proposed use) | For social media integration (section 10) |
| `LINKEDIN_CLIENT_SECRET` | OAuth client secret for LinkedIn integration | Configured (Proposed use) | For social media integration (section 10) |

General rules: never hard-code secrets, keep `.env.local` out of version control, document required variables in `.env.example`.

`[VERIFY: brief references a "missing partner token" as a current gate — confirm which environment variable this corresponds to (likely MOODLE_API_TOKEN or a yet-undocumented partner-integration token) and whether additional environment variables exist in the live .env.example beyond those listed in Master Specification section 20]`

---

## 8. Database

Source: Master Specification v0.2, section 3.3.

Primary ORM: Prisma. Primary schema: `prisma/schema.prisma`. Database: PostgreSQL via `DATABASE_URL`, with Supabase as the intended hosted provider.

The handover brief references 28 existing Prisma models in total. The Master Specification confirms 21 models by name. These 21 are grouped below into logical categories for this handover pack; the grouping itself is an organisational aid for this document and not a schema change.

### 8.1 Identity and Access

- `User`
- `Account`
- `Session`
- `VerificationToken`
- `CouncilUser`

### 8.2 Council / Place Data

- `Council`
- `MetricDefinition`
- `CouncilMetric`

### 8.3 DRMC / Intelligence Scoring

- `DrmcLayer`
- `DrmcScore`
- `DrmcScoreClaim`
- `BenchmarkScore` (Migration note: Master Specification v0.2 proposes renaming this to `IntelligenceScore` in Phase 0 cleanup)
- `ReadinessScore`

### 8.4 Documents and Evidence

- `Document`
- `SourceVerification`

### 8.5 Budget and Exposure

- `BudgetMeasure`
- `CouncilExposure`

### 8.6 Reporting

- `ReportOutput`
- `CouncilAction`

### 8.7 Import / Operations

- `ImportRun`
- `ImportError`

### 8.8 Outstanding models

`[VERIFY: brief references 28 models total — Codex to confirm the remaining 7 and update this table]`

### 8.9 Current report types

- `BENCHMARK` (Migration note: proposed rename to `PLACE_INTELLIGENCE_REPORT`)
- `MAYOR_BRIEF` (Migration note: proposed rename to `EXECUTIVE_INTELLIGENCE_BRIEF`)
- `BUDGET_IMPACT` (Migration note: proposed rename to `BUDGET_IMPACT_INTELLIGENCE`)
- `COUNCILLOR_INFO_PACK` (Migration note: proposed rename to `COUNCIL_INTELLIGENCE_PROFILE`)

The Master Specification notes that new enum values should be added and existing records migrated before old values are deprecated; old values should not be deleted until all reports are migrated.

### 8.10 Current roles in Prisma

- `AIIPD_ADMIN`
- `ANALYST`
- `COUNCIL_ADMIN`
- `COUNCIL_VIEWER`

Target roles (Proposed, section 5): `AIIPD_ADMIN`, `AIIPD_ANALYST`, `CLIENT_ADMIN`, `CLIENT_REVIEWER`, `SUBSCRIBER`, `LICENCE_HOLDER`, `CANDIDATE_USER`, `PUBLIC_USER`. The Master Specification recommends extending the `Role` enum or introducing `Membership`, `Organisation`, `Entitlement` and `Subscription` tables rather than overloading council-specific roles.

---

## 9. Security, Privacy, DRMC and Human-Review Requirements

Source: Master Specification v0.2, section 17.

### 9.1 Core rules

- Use public institutional data wherever possible.
- Do not collect private citizen personal data unless there is a clear authorised purpose.
- Do not profile private residents, voters, complainants or consultation participants.
- Public officials may be referenced only in their public role and where relevant.
- Store the minimum data required.
- Make source status, confidence and verification visible.
- AI-assisted outputs require human review before formal use.

### 9.2 DRMC/RSC caveat

DRMC/RSC outputs are interpretive civic intelligence assessments. They are not psychological diagnoses, moral rankings, validated psychological measurements, or automated character judgements.

### 9.3 Candidate Intelligence caveat

Candidate Intelligence supports civic issue literacy, evidence-based communication, public leadership preparation, and community listening. It must not support misinformation, smear campaigns, private voter profiling, fake grassroots activity, covert persuasion, or manipulative targeting.

### 9.4 Intelligence framing safeguards (added in v0.2)

All intelligence outputs must:

- Be clearly labelled as evidence-based analytical products, not predictions or guarantees.
- Carry a confidence level indicator where AI-assisted analysis is involved.
- Distinguish between verified source data, AI-assisted synthesis, and analyst interpretation.
- Include a scope and caveat statement in every formal output.
- Not present intelligence indicators as validated psychological measurements, moral rankings, or regulatory determinations.
- Reference the full ethics framework in the AIIPD Style Guide (`/content/governance/style-guide.md`).

---

## 10. Known Limitations

### 10.1 Confirmed in Master Specification (v0.1 and v0.2, section 3.2 "Known current issue")

- `npm run build` and `npm run typecheck` fail because `src/components/AppShell.tsx` passes `string` href values to typed Next.js `Link` routes. **Status: Blocked.**
- `npm run lint` prompts for ESLint configuration because the project has not completed migration from `next lint`. **Status: Blocked.**

### 10.2 Additional limitations referenced in the handover brief

- Public workspace access: `[VERIFY: confirm current scope — the brief indicates the authenticated workspace, or parts of it, may be reachable without authentication]`
- Missing middleware: `[VERIFY: confirm whether src/middleware.ts exists and what, if any, route protection or request handling it currently performs]`
- Demo-backed report endpoint: `[VERIFY: confirm that /api/reports currently relies on the demo report generator described in Master Specification section 11.3 (src/lib/report-generator.ts), rather than a production report engine]`

These limitations, together with the build/lint issues above, define the Phase 0 stabilisation work described in Document 2.
