# AiIPD Project Progress and 12-Week Launch Pipeline

**Version:** 0.1-draft
**Date:** 11 June 2026
**Status:** DRAFT — evidence snapshot pending Codex verification

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

This document sets out the current evidence snapshot for the AiIPD platform, the gates that currently block progression to a protected pilot, and a twelve-week staged roadmap from the present scaffold to a launch-ready subscriber pilot. It is a planning document, not a confirmation of completed work. The figures and gates listed below come from the brief that commissioned this handover pack and from the AIIPD Master Technical Specification (v0.1 and v0.2). Where a figure or gate has not been independently verified against the live codebase or database, it is marked `[VERIFY]`.

The roadmap assumes that Document 1 (current website and backend specification) is read first, since the gates and weeks 1-2 tasks depend on the limitations identified there. The roadmap is staged so that each two-week block produces a working, demonstrable increment, with an acceptance gate that must be met before the next block begins.

---

## 1. Evidence Snapshot

`[VERIFY: figures as supplied by Liam, 11 June 2026 — Codex to confirm against live database before publication]`

| Metric | Figure |
|---|---|
| Councils in database | 757 |
| Documents ingested | 3,821 |
| Council snapshots generated | 746 |
| Reports generated | 66 |
| Client records | None recorded |

These figures suggest that significant data ingestion work has already taken place across `Council`, `Document`, and related models, but that the platform has not yet onboarded any client organisations, and that report generation (66 reports against 757 councils and 746 snapshots) is at an early stage relative to the scale of underlying place data.

`[VERIFY: confirm the source of the 746 "snapshots" figure — Document 1 does not list a model explicitly named "Snapshot"; this may correspond to CouncilMetric, BenchmarkScore/IntelligenceScore, or DrmcScore records, or to a model not yet identified among the "remaining 7" Prisma models referenced in Document 1, section 8.8]`

---

## 2. Status Categories

The status categories below are the same legend used in Document 1 and applied consistently across this pack.

| Status | Meaning |
|---|---|
| Confirmed working | Verified directly against the live codebase, database, or running environment. |
| Built but unverified | Code or configuration exists in the repository or Master Specification but has not been run or tested in this environment. |
| Configured | An environment variable, service, or integration has been set up but its operational status has not been confirmed. |
| Blocked | A known issue prevents the feature, build step, or workflow from functioning as intended. |
| Proposed | Not yet built. Described as a target or future requirement in the Master Specification or this handover pack. |

---

## 3. Current Gates

The following gates were identified in the brief as the primary obstacles between the current scaffold and a protected pilot. Each is described below with what it means in practice and what resolving it requires.

### 3.1 Assistant fallback

**What it means:** The `/api/assistant` route (Document 1, section 4) currently appears to operate in a fallback or demo mode rather than relying fully on a live model integration, or it falls back to static/sample responses when the live integration is unavailable. The public site explicitly labels its assistant demo as "guided" and "sample scenarios" per the Master Specification (section 3.1), but the authenticated application's assistant route status is unclear.

**What resolving it requires:** Confirm whether `ANTHROPIC_API_KEY` is configured and active in the deployment environment, confirm the current behaviour of `src/app/api/assistant/route.ts` (Document 1, section 4.1), and determine whether fallback behaviour is intentional (and should remain, clearly labelled) or unintentional (and should be replaced with a live, entitlement-gated integration). `[VERIFY: confirm current assistant route implementation and fallback conditions]`

### 3.2 Missing partner token

**What it means:** A token required for an external partner integration is not currently configured. The brief does not specify which integration this refers to. Candidates from the Master Specification's environment variable list (section 20) include `MOODLE_API_TOKEN` (Moodle LMS integration, section 7) or a yet-undocumented partner-integration token outside the current `.env.example`.

**What resolving it requires:** Identify which integration the missing token relates to, confirm whether the corresponding service account exists with the partner, provision the token through a secrets manager or environment variable (never hard-coded per section 17 and section 20 rules), and confirm the integration's read/write scope is least-privilege. `[VERIFY: confirm which token and which partner integration this refers to]`

### 3.3 Missing named administrator

**What it means:** No individual user is currently designated with the `AIIPD_ADMIN` role (Document 1, section 8.10) in the live database, or no such user account exists at all. Without a named administrator, platform configuration, subscriber management, and the human review gate (Master Specification section 11.4) cannot be exercised by anyone in the live system.

**What resolving it requires:** Create or designate at least one `User` record with the `AIIPD_ADMIN` role, confirm this user can authenticate via the current NextAuth credentials provider (Document 1, section 6), and document who holds this role and how access is provisioned for additional administrators and analysts. `[VERIFY: confirm whether any AIIPD_ADMIN user currently exists in the live database]`

### 3.4 Absent route protection

**What it means:** The brief indicates that authenticated routes (the Civic Intelligence Centre, evidence workspace, report workspace, and admin import page listed in Document 1, section 4.1) may currently be reachable without authentication. This is also referenced in Document 1, section 10.2 as "public workspace access" and "missing middleware".

**What resolving it requires:** Confirm whether `src/middleware.ts` exists and what it currently enforces, implement or extend Next.js middleware to require an authenticated session for all routes under `src/app/evidence`, `src/app/reports`, and `src/app/admin`, and add automated tests that verify unauthenticated requests to these routes are redirected or rejected. `[VERIFY: confirm current middleware configuration and route protection status]`

### 3.5 Absent rate limiting

**What it means:** No rate limiting currently appears to be applied to API routes, including `/api/assistant` (which may incur cost per call to `ANTHROPIC_API_KEY`) and `/api/reports`. Without rate limiting, the platform is exposed to cost overrun, abuse, and denial-of-service risk on routes that trigger AI-assisted processing or database-heavy report generation.

**What resolving it requires:** Introduce a rate-limiting layer (for example, per-user or per-IP limits at the middleware or API route level) for `/api/assistant`, `/api/reports`, and any other compute- or cost-sensitive routes, and confirm rate limits are appropriate to the entitlement model once entitlements (Master Specification section 6.3) are introduced. `[VERIFY: confirm no rate limiting currently exists on any API route]`

### 3.6 Unconfigured linting

**What it means:** This corresponds to the known issue documented in the Master Specification (section 3.2): `npm run lint` prompts for ESLint configuration because the project has not completed migration from `next lint` to the Next.js 15 ESLint setup. This is listed as Phase 0 work in section 18 ("Configure ESLint for Next.js 15 or migrate from `next lint`").

**What resolving it requires:** Complete the ESLint configuration migration for Next.js 15, ensure `npm run lint` runs non-interactively (suitable for CI), and resolve the related typed-route build failure in `src/components/AppShell.tsx` (Document 1, section 10.1) as part of the same stabilisation pass.

---

## 4. Twelve-Week Staged Roadmap

| Week(s) | Focus | Key Tasks | Dependencies | Acceptance Gate | Responsible Role |
|---|---|---|---|---|---|
| 1-2 | Preserve and publish current build; security baseline; content QA; public-site deployment | Push current codebase to GitHub per `00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md`; fix `AppShell.tsx` typed-route build failure; complete ESLint migration; create `.env.example`; run content QA against the AIIPD style guide on the public static site; deploy public static site to a stable hosting environment | Codebase access on GitHub (routing key `AIIPD-BRIDGE-CLAUDE-TO-CODEX-V1`) | `npm run build`, `npm run typecheck`, and `npm run lint` all pass cleanly; public site is live at a stable URL; `.env.example` matches all variables in use | Codex (build/infrastructure); Claude (content QA) |
| 3-4 | Protected AiIPD pilot; RBAC; admin controls; rate limiting; live integrations | Implement `src/middleware.ts` route protection for authenticated routes; designate at least one `AIIPD_ADMIN` user; implement rate limiting on `/api/assistant` and `/api/reports`; confirm/resolve assistant fallback behaviour; confirm partner token configuration; extend `Role` enum or implement `Membership`/`Organisation` scaffolding per Master Specification section 5 | Weeks 1-2 complete; named administrator identified by Liam | Unauthenticated requests to protected routes are rejected or redirected; at least one `AIIPD_ADMIN` user can authenticate; rate limits demonstrably trigger under load test; assistant route behaviour documented and labelled correctly | Codex (implementation); Liam (administrator designation) |
| 5-6 | Evidence-linked narrative intelligence; production report workflows | Replace demo `src/lib/report-generator.ts` with modular report engine (`report/types.ts`, `report/templates/`, `report/sections/`, `report/evidence-summary.ts`, `report/render-html.ts`); implement source register rendering with full claim metadata (section 6.1 fields); implement human review gate fields (review status, reviewer identity, approval timestamp, version number) per section 11.4 | Weeks 3-4 complete; Document and SourceVerification models confirmed | At least one report type (for example, a Place Intelligence Report) can be generated end to end from selected evidence through to a reviewed, versioned HTML export with source register and caveat block | Codex (implementation); AIIPD Analyst (review workflow validation) |
| 7-8 | Multi-client portfolio; CRM; tasks; delivery management | Implement `Organisation`, `Subscription`, `Entitlement` schema additions (section 6.2); build client workspace surface (section 4.2, item 4); implement basic CRM/lead and client record tracking; implement task tracking for analyst delivery workflows | Weeks 5-6 complete; entitlement model design approved | At least one test organisation can be onboarded with scoped users, entitlements, and a client workspace showing evidence registers, draft outputs, and approvals | Codex (implementation); AIIPD Admin (entitlement configuration) |
| 9-10 | LMS, publishing, integration foundations | Implement Phase 1 Moodle integration (manual course links, `MoodleCourseLink` model, section 7.2); implement Publishing Studio MVP (template library, section-based editor, HTML/PDF export per section 8.3); confirm `MOODLE_API_TOKEN` and `MOODLE_BASE_URL` configuration | Weeks 7-8 complete; Moodle provider decision made (Open Decision 2, Master Specification section 22) | A subscriber can view at least one linked Moodle course based on entitlement; at least one publication can be generated from a template through to PDF export with human approval status | Codex (implementation); AIIPD Admin (Moodle setup) |
| 11-12 | Production hardening; pilot acceptance; launch review | Full security review against section 17 (security, privacy, ethics); load testing of rate-limited routes; data retention and consent record review (`ConsentRecord` model, section 6.2); pilot acceptance testing with at least one real client organisation; launch readiness review against Definition of Done (section 21) | Weeks 9-10 complete; pilot client identified | Pilot client organisation can complete a full evidence-to-report cycle within their own organisation-scoped workspace; all Definition of Done criteria in section 21 are met for in-scope features; launch review sign-off recorded | Liam (sign-off); Codex (technical readiness); AIIPD Analyst (pilot support) |

---

## 5. Post-Launch Pipeline

The following phases extend beyond the twelve-week pilot launch and are described here as future phases. They are not scoped for the initial pilot.

**Finance.** A finance phase would extend the platform's Stripe integration (Master Specification section 14.2) from basic subscription handling into full invoicing, payment reconciliation, and revenue reporting across organisations and entitlement tiers. This phase depends on the entitlement model (section 6.3) being stable and on subscription tiers being finalised.

**Ecommerce.** An ecommerce phase would support direct purchase of individual reports, publications, or report credits (section 6.2, `ReportCreditLedger`) outside of standing subscriptions, likely through the same Stripe product catalogue established in the finance phase. This would primarily serve licence holders and one-off purchasers who are not full subscribers.

**Media.** A media phase would build out the blog and resource hub (section 9) and social media integration (section 10), converting selected intelligence outputs into public-facing content with draft/review/publish workflows and, eventually, scheduled and approved social publishing across LinkedIn, Facebook, and other channels.

**Automation.** An automation phase would implement the scheduled update framework (section 12), covering weekly source freshness checks, monthly budget impact refreshes, Moodle enrolment reconciliation, and subscriber briefing generation, using Vercel Cron, Supabase scheduled functions, or GitHub Actions as appropriate.

**Custom plugins.** A custom plugins phase would allow individual subscriber organisations or licence holders to extend the platform with organisation-specific modules, white-label outputs (BrandPress, section 2.2), or bespoke integrations, building on the entitlement and API access controls established in earlier phases.

---

## 6. Risks Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Assistant fallback behaviour is not clearly labelled to users, creating a misleading impression of live AI capability | Medium | Medium | Confirm and document current assistant route behaviour (gate 3.1); ensure any fallback or demo response is clearly labelled per Master Specification section 3.1 ("do not claim live real-time analysis") |
| Missing partner token blocks a planned integration milestone | Medium | Medium | Identify the specific integration and token early in weeks 1-2; escalate to Liam if the token cannot be provisioned in time for the dependent roadmap week |
| No named administrator means platform configuration and human review cannot proceed | High (until resolved) | High | Designate at least one `AIIPD_ADMIN` user before weeks 3-4 begin; this is a prerequisite blocking item, not a parallel task |
| Authenticated routes remain reachable without authentication, exposing evidence, draft reports, or admin import functions | High (until resolved) | High | Implement `src/middleware.ts` route protection in weeks 3-4 before any pilot client data is loaded; treat as a hard gate before week 5 |
| Absent rate limiting allows cost overrun on AI-assisted routes or abuse of report generation | Medium | Medium | Implement rate limiting alongside route protection in weeks 3-4; monitor `ANTHROPIC_API_KEY` usage during and after rollout |
| Unconfigured linting and the typed-route build failure block CI and slow down all subsequent development | High (until resolved) | Medium | Resolve as the first task in weeks 1-2; do not proceed to weeks 3-4 until `npm run build`, `npm run typecheck`, and `npm run lint` all pass |
| Demo-backed report endpoint is mistaken for a production-ready report engine, leading to a pilot client receiving an unreviewed or low-quality report | Medium | High | Treat the modular report engine replacement (weeks 5-6) as a hard prerequisite for any pilot client report generation; do not allow `/api/reports` in its current form to reach a pilot client |
| 28 Prisma models referenced in the brief versus 21 confirmed in the Master Specification indicates schema drift between documentation and the live database | Medium | Medium | Codex to reconcile the live `prisma/schema.prisma` against Document 1, section 8, and update both this pack and the Master Specification accordingly |
| Evidence snapshot figures (757 councils, 3,821 documents, 746 snapshots, 66 reports) may not reflect current database state if ingestion has continued or stalled since 11 June 2026 | Low | Low | Codex to re-confirm figures against the live database before any external reporting of platform scale |

---

This document should be read alongside Document 1 (current website and backend specification). Gates 3.1 through 3.6 above correspond directly to the limitations identified in Document 1, section 10.
