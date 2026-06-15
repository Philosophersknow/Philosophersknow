# Phase 0 Technical Task List

**Version:** 0.1-draft
**Date:** 15 June 2026
**Status:** DRAFT — ready for Codex on resume (~19 June 2026)

---

## Purpose

This document is the concrete, actionable starting point for Codex when token availability resumes around 19 June 2026. It breaks down Master Specification v0.2 Section 18 ("Phase 0: Stabilise Current Platform") and Section 19 ("Immediate Technical Priorities") into granular tasks with sources, dependencies, acceptance criteria and effort estimates. Tasks are ordered by dependency, not just by priority, so Codex can work through the table roughly top to bottom without getting blocked partway through.

This document does not replace the Master Specification or the handover pack (documents 01-04). It is the execution layer on top of them.

---

## Pre-work checklist

These items do not require Codex's runtime access and can be confirmed by anyone (Claude, Liam, or a human team member) before Codex starts on 19 June 2026. Confirming these in advance removes friction from Codex's first session.

- [ ] Confirm `.env.example` exists in the AiIPD application root and lists all variable names (no values), matching Master Spec v0.2 Section 20 plus any additional variables discovered in the live codebase. If it does not exist, create it using the template in `docs/handover/2026-06-11/00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md` Section 4 as the starting point.
- [ ] Confirm the location of the Hearts Co-op logo file. The handover instructions (file `00`, Section 2.2 and the safety checklist) note it is "currently untracked locally" — locate it and add it to `assets/` before or during the Hearts Co-op codebase push (TASK-007).
- [ ] Review `AGENTS.md` (repository root) for the status legend, branch conventions and folder ownership rules. Codex should work on `codex/aiipd-application`, `codex/hearts-coop-website` and `codex/update-master-specification` as described in handover file `00`, Section 3.1.
- [ ] Read the handover pack in order: `docs/handover/2026-06-11/README.md`, then documents `01` through `04`, then this document (`05`). This gives the full current-state picture before any code changes.
- [ ] Confirm with Liam who holds the `AIIPD_ADMIN` designation (referenced in document `02`, gate 3.3) — this does not block Phase 0 build/lint work but is needed before Phase 1 (Weeks 3-4) middleware and rate-limiting work begins.

---

## Phase 0 task table

| Task ID | Task | Source/Reference | Dependencies | Acceptance Criteria | Status | Estimated Effort |
|---|---|---|---|---|---|---|
| TASK-001 | Fix typed-route build issue in `src/components/AppShell.tsx`. The component currently passes `string` href values to typed Next.js `Link` routes, which fails `npm run build` and `npm run typecheck`. Update href values to use the typed route helpers/literal route types Next.js 15 expects (or disable `typedRoutes` only if Liam approves a temporary opt-out, with a follow-up task to re-enable). | Master Spec v0.2 Section 3.2 "Known current issue"; Section 18 Phase 0; Section 19 item 1; handover doc 01 Section 10.1; handover doc 02 gate 3.6 | None — first task, no prerequisites | `npm run build` completes without the `AppShell.tsx` typed-route error; `npm run typecheck` passes with zero errors related to `AppShell.tsx` | Blocked | M |
| TASK-002 | Configure ESLint for Next.js 15 or complete migration away from `next lint`. Run the Next.js 15 ESLint migration (`npx @next/codemod@latest` or manual `eslint.config.mjs` flat-config setup), ensure `npm run lint` runs non-interactively (no setup prompts) so it is CI-safe. | Master Spec v0.2 Section 3.2, Section 18 Phase 0, Section 19 item 1; handover doc 02 gate 3.6 | None — can run in parallel with TASK-001 | `npm run lint` runs to completion with no interactive prompts, in both local and CI environments; lint output is either clean or contains only known/triaged warnings documented in a follow-up issue | Blocked | M |
| TASK-003 | Confirm `.next/types` handling in `tsconfig.json`. Verify the `include`/`exclude` arrays correctly reference `.next/types/**/*.ts` (Next.js 15 typed routes), confirm `.next/` is gitignored, and confirm the typed-route fix in TASK-001 does not require manual edits to `.next/types` (these are generated, not hand-edited). | Master Spec v0.2 Section 18 Phase 0; Section 19 item 1 | Best done alongside or immediately after TASK-001, since the typed-route fix and `tsconfig.json` configuration are closely related | `tsconfig.json` includes the generated `.next/types` path; `.next/` is confirmed in `.gitignore`; `npm run typecheck` passes cleanly with no manual edits required inside `.next/types` | Blocked | S |
| TASK-004 | Verify the public homepage static preview still works after TASK-001 to TASK-003. Confirm `public/index.html` still renders correctly via local static preview (e.g. `http://127.0.0.1:4173/index.html` or current equivalent), confirm anchors, tabs, accordions, FAQ, guided assistant demo and contact form JS still function, and confirm no Next.js build changes have broken the static asset paths (`public/assets/images`, `public/assets/data`). | Master Spec v0.2 Section 3.1, Section 18 Phase 0; handover doc 01 Section 1 `[VERIFY: confirm current hosting location]` | TASK-001, TASK-002, TASK-003 (run after build/lint/typecheck changes to confirm nothing broke the static site) | Static preview loads at the confirmed local URL; all interactive elements (tabs, accordions, FAQ, assistant demo, contact success state, legal modals) work as before; no console errors related to missing assets | Blocked | S |
| TASK-005 | Document all environment variables. Cross-check the Master Spec v0.2 Section 20 list against the live `.env.example` and any variables actually referenced in code (`process.env.*` usage across `src/`). Add any variables found in code but missing from Section 20 or `.env.example`. Update `.env.example` to match exactly, with variable names only and no values. | Master Spec v0.2 Section 18 Phase 0, Section 20; handover doc 01 Section 7 `[VERIFY: confirm additional environment variables exist in the live .env.example]`; handover doc 02 gate 3.2 (missing partner token) | None — can run in parallel with TASK-001 to TASK-003, but should be finished before TASK-006/TASK-007 push the codebase (so `.env.example` is correct on first push) | `.env.example` contains every environment variable referenced anywhere in `src/`, `scripts/`, and `prisma/`; Master Spec Section 20 table updated if new variables are found; no values, only variable names, appear in `.env.example` | Blocked | S |
| TASK-006 | Push the AiIPD application codebase to GitHub per handover instructions file `00`. Create branch `codex/aiipd-application` from `origin/claude/awesome-bardeen-dzqcI`, place the application under `app/aiipd/` (per Section 6 layout to avoid collisions with `content/` and `docs/`), push `public/`, `src/`, `prisma/`, `scripts/`, `docs/`, `data/`, `assets/`, `package.json`, lockfile, `tsconfig.json`, `next.config.*`, `.env.example`, `README.md`. Exclude `.env`/`.env.local`, `node_modules/`, `.next/`, and any real council data dumps not explicitly approved. | Handover doc `00`, Sections 2.1, 3, 6, 8 (safety checklist); Master Spec v0.2 Section 24.4 | TASK-001 to TASK-005 should be completed (or at least committed locally) before push, so the first GitHub state of `codex/aiipd-application` already has a passing build/lint/typecheck and a correct `.env.example`. Not a hard technical dependency, but strongly recommended to avoid pushing a known-broken state as the baseline | Branch `codex/aiipd-application` exists on `origin`, contains the full application codebase at `app/aiipd/`, passes the safety checklist in handover doc `00` Section 8, and `npm run build`/`typecheck`/`lint` pass on a fresh clone | Blocked | M |
| TASK-007 | Push the Hearts Co-op codebase to GitHub. Create branch `codex/hearts-coop-website` from `origin/claude/awesome-bardeen-dzqcI`, place the site under `app/hearts-coop/`, include the Hearts logo in `assets/` (currently untracked locally — locate and add per pre-work checklist), push static site files (HTML/CSS/JS or Next.js structure as currently built) and `README.md`. | Handover doc `00`, Sections 2.2, 3, 6, 8 (safety checklist); handover docs 03 and 04 | Hearts logo located (pre-work checklist item). Can run independently of TASK-006, in parallel if convenient | Branch `codex/hearts-coop-website` exists on `origin`, contains the Hearts Co-op site at `app/hearts-coop/`, Hearts logo is present and tracked in `assets/`, passes the safety checklist in handover doc `00` Section 8 | Blocked | M |
| TASK-008 | Resolve all `[VERIFY]` items in handover documents 01-04 against the live codebase/database, and update each document with confirmed findings. Broken into sub-items per document below. | Handover docs 01-04 (all `[VERIFY]` markers); AGENTS.md Section 2.2 (Codex resolves `[VERIFY]` items left by Claude) | TASK-006 (AiIPD codebase must be on GitHub for Claude/other agents to cross-check Codex's findings); TASK-007 for the Hearts-specific sub-items in TASK-008d | Blocked | L (sum of sub-items) |
| TASK-008a | Doc 01 `[VERIFY]` items: confirm current static-site hosting location/URL (Section 1); confirm exact package versions and build tooling in `package.json` (Section 3); confirm existence and behaviour of `/api/councils`, `/api/councils/:id/snapshot`, `POST /api/assistant`, `POST /api/onboarding`, `POST /api/reports`, `/api/intelligence`, `/api/intelligence/:council` (Section 4.2); confirm which evidence-pipeline stages (Section 5.1) are implemented vs schema-only; confirm `/api/reports` and `src/lib/report-generator.ts` behaviour as demo vs production (Section 5.2); confirm whether middleware/route protection exists (Section 6); confirm additional `.env.example` variables beyond Section 7 table (overlaps TASK-005); confirm the remaining 7 of 28 Prisma models (Section 8.8); confirm whether Google OAuth is wired into NextAuth (Section 7 table) | Handover doc 01, all `[VERIFY]` markers | TASK-006 | Each `[VERIFY]` marker in doc 01 is replaced with a confirmed status (Confirmed / Built but unverified / Configured / Blocked / Proposed per AGENTS.md legend) and a short factual note; doc 01 updated in place or as a versioned addendum | Blocked | L |
| TASK-008b | Doc 02 `[VERIFY]` items: confirm the evidence snapshot figures (757 councils, 3,821 documents, 746 council snapshots, 66 reports, 0 client records) against the live database (Section 1); confirm the source of the "746 snapshots" figure — identify which model it corresponds to (`CouncilMetric`, `BenchmarkScore`/`IntelligenceScore`, `DrmcScore`, or an unidentified model) (Section 1); confirm assistant route fallback behaviour and conditions (gate 3.1); identify which integration the "missing partner token" refers to (gate 3.2); confirm whether any `AIIPD_ADMIN` user exists (gate 3.3); confirm current middleware/route-protection status (gate 3.4, overlaps TASK-008a); confirm whether any rate limiting exists on any API route (gate 3.5) | Handover doc 02, all `[VERIFY]` markers and gates 3.1-3.6 | TASK-006 | Each `[VERIFY]` marker and gate in doc 02 is updated with a confirmed status and factual note; risks register (Section 6) updated if findings change likelihood/impact ratings | Blocked | M |
| TASK-008c | Doc 03 and 04 (Hearts Co-op) `[VERIFY]` items: read both documents in full once the Hearts codebase is on GitHub, identify and list all `[VERIFY]` markers (not enumerated here as they were out of scope for this task list's source documents), confirm each against the live Hearts codebase | Handover docs 03, 04 | TASK-007 | All `[VERIFY]` markers in docs 03 and 04 are replaced with confirmed statuses and factual notes | Blocked | M |
| TASK-009 | Address known limitation: public workspace access. Confirm the actual current scope (per TASK-008a, doc 01 Section 10.2) — determine which authenticated routes (`src/app/evidence`, `src/app/reports`, `src/app/admin`) are reachable without a session. If confirmed reachable, this becomes the scoping input for TASK-010 (middleware). If already protected by some existing mechanism, document that mechanism. | Master Spec v0.2 Section 17; handover doc 01 Section 10.2; handover doc 02 gate 3.4 | TASK-008a (route protection findings) | Written confirmation of which routes are/are not reachable without authentication, with evidence (request/response or code reference); feeds directly into TASK-010 scope | Blocked | S |
| TASK-010 | Address known limitation: missing middleware. Implement or extend `src/middleware.ts` to require an authenticated session for all routes under `src/app/evidence`, `src/app/reports`, and `src/app/admin`. Add automated tests confirming unauthenticated requests are redirected or rejected (e.g. 302 to sign-in, or 401/403 for API routes). | Master Spec v0.2 Section 17, Section 18 Phase 1/2 (route protection precedes subscriber portal work); handover doc 01 Section 6, Section 10.2; handover doc 02 gate 3.4, Week 3-4 tasks | TASK-009 (confirms current state and exact route scope); TASK-008a (confirms whether `src/middleware.ts` exists at all) | `src/middleware.ts` exists and enforces session checks on `evidence`, `reports`, `admin` route trees; automated test(s) demonstrate unauthenticated requests are rejected/redirected; at least one `AIIPD_ADMIN` test user can still authenticate and reach these routes | Blocked | M |
| TASK-011 | Address known limitation: demo-backed report endpoint. Confirm (via TASK-008a) that `/api/reports` and `src/lib/report-generator.ts` currently produce demo output rather than a production report. Document this clearly as a known limitation in user-facing terms (no pilot client should receive output from this endpoint as-is) and create a tracking note/issue for the Phase 4 modular report engine replacement (Master Spec Section 11.3, Phase 4 in Section 18). This task is about confirming, labelling and tracking — not building the full report engine, which is out of Phase 0 scope. | Master Spec v0.2 Section 11.3, Section 18 Phase 4; handover doc 01 Section 5.2; handover doc 02 risks register (demo-backed report endpoint risk) | TASK-008a (confirms current `/api/reports` behaviour) | `/api/reports` behaviour is documented as demo/production in doc 01; if demo, a clear in-app or code-level label/comment marks it as non-production; a tracking item exists referencing the Phase 4 modular report engine plan (`report/types.ts`, `report/templates/`, etc.) | Blocked | S |
| TASK-012 | Confirm the `council-benchmark/` to `civic-intelligence/` URL migration plan. Per Master Spec v0.2 Section 3.1 migration note, the public site URL path `council-benchmark/` should become `civic-intelligence/` in Phase 1 navigation work. For Phase 0, produce a migration plan only: inventory every internal anchor/link referencing `council-benchmark/` in `public/index.html` and elsewhere, propose a redirect strategy (e.g. static redirect or rewrite rule) so old links do not break, and confirm this aligns with the "Council Intelligence Dashboard" -> "Civic Intelligence Centre" rename noted in Master Spec Section 3.2. Do not execute the rename in Phase 0 — that is Phase 1 work. | Master Spec v0.2 Section 3.1, Section 3.2 migration notes, Section 18 Phase 1; handover doc 01 Section 1 | TASK-004 (static site confirmed working before planning further changes to it) | A short migration plan document or section listing: all current `council-benchmark/` references found, the proposed `civic-intelligence/` replacement paths, and a redirect approach; explicitly scoped as "plan only, execution in Phase 1" | Blocked | S |
| TASK-013 | Confirm the Prisma enum rename sequence for report types (`BENCHMARK` -> `PLACE_INTELLIGENCE_REPORT`, `MAYOR_BRIEF` -> `EXECUTIVE_INTELLIGENCE_BRIEF`, `BUDGET_IMPACT` -> `BUDGET_IMPACT_INTELLIGENCE`, `COUNCILLOR_INFO_PACK` -> `COUNCIL_INTELLIGENCE_PROFILE`) and the related `BenchmarkScore` -> `IntelligenceScore` model rename. For Phase 0, produce a migration sequence plan only: confirm the current enum values and model name in the live `prisma/schema.prisma` (cross-check against handover doc 01 Sections 8.3 and 8.9), and document the additive-first sequence (add new enum values, write a data migration to backfill new values onto existing `ReportOutput` records, deprecate but do not delete old values, then rename `BenchmarkScore` to `IntelligenceScore` as a final step once no code references the old name). Do not execute the schema migration in Phase 0. | Master Spec v0.2 Section 3.3 migration notes, Section 18 (Phase 0 cleanup references); handover doc 01 Sections 8.3, 8.9 | TASK-008a (confirms live schema matches Master Spec's documented 21 models and current enum values before planning the migration) | A written migration sequence (ordered steps) for both the report-type enum rename and the `BenchmarkScore` -> `IntelligenceScore` rename, following the "add new, migrate data, deprecate old, do not delete" rule from Master Spec Section 3.3; explicitly scoped as "plan only, execution in Phase 0 cleanup or Phase 1 as agreed with Liam" | Blocked | S |

---

## Sequencing diagram

```text
TASK-005 (env vars) ----------------------------------------+
                                                              |
TASK-001 (AppShell typed routes) --+                         |
TASK-002 (ESLint config)  ---------+--> build/typecheck/lint |
TASK-003 (.next/types in tsconfig) +     all pass            |
                                          |                   |
                                          v                   v
                                    TASK-004 (static preview check)
                                          |
                                          v
                              TASK-006 (push AiIPD codebase)
                                          |
                    +---------------------+----------------------+
                    |                                             |
                    v                                             v
        TASK-007 (push Hearts codebase)              TASK-008a (resolve doc 01 [VERIFY])
                    |                                             |
                    v                                             v
        TASK-008c (resolve doc 03/04 [VERIFY])       TASK-008b (resolve doc 02 [VERIFY])
                                                                  |
                                                  +---------------+---------------+
                                                  |               |               |
                                                  v               v               v
                                          TASK-009          TASK-011        TASK-008a feeds
                                       (public access)   (demo report)     TASK-012 / TASK-013
                                                  |                          (migration plans)
                                                  v
                                          TASK-010 (middleware)
```

Notes on the diagram:
- TASK-001, TASK-002, TASK-003 and TASK-005 have no dependencies on each other and can be worked in any order or in parallel, but all should be done before TASK-006 so the first GitHub push of the AiIPD codebase already builds, lints, typechecks cleanly and has a correct `.env.example`.
- TASK-004 is a final check after the build/lint/typecheck fixes, before pushing.
- TASK-006 unblocks TASK-008a/b (Codex needs the codebase on GitHub so other agents, including Claude, can cross-check findings against the same source).
- TASK-007 unblocks TASK-008c and depends on the Hearts logo being located (pre-work checklist).
- TASK-008a results feed directly into TASK-009, TASK-011, TASK-012 and TASK-013.
- TASK-009 must complete before TASK-010 (middleware scope depends on confirming what is currently exposed).
- TASK-012 and TASK-013 are both "plan only" deliverables for Phase 0; their execution is Phase 1 work and depends on Liam's sign-off.

---

## First-day script

A literal, ordered checklist for Codex's first session on or after 19 June 2026.

1. Read `AGENTS.md`, then this document (`05_Phase_0_Technical_Task_List.md`), then re-skim handover docs 01 and 02 for context on gates and known issues.
2. Confirm local environment: clone/pull the repository, confirm `node`/`npm` versions match `package.json` engines (if specified), run `npm install`.
3. Start TASK-005 (env var documentation) first — it is quick and de-risks the later push (TASK-006). Cross-check `.env.example` against `process.env` usage in `src/`.
4. Start TASK-001 (AppShell typed routes). Run `npm run build` and `npm run typecheck` to see the exact current error, fix the `Link` href typing in `src/components/AppShell.tsx`, re-run until clean.
5. Start TASK-002 (ESLint migration). Run `npm run lint`, follow the Next.js 15 ESLint migration path, confirm it runs non-interactively.
6. Do TASK-003 (`.next/types` in `tsconfig.json`) alongside TASK-001 — verify generated types are picked up correctly and `.next/` is gitignored.
7. Run TASK-004 (static preview check). Start the static preview, click through tabs/accordions/FAQ/assistant demo/contact form, confirm no regressions from steps 4-6.
8. Commit the Phase 0 stabilisation fixes locally with a clear message referencing TASK-001 through TASK-005.
9. Do TASK-006 (push AiIPD codebase to `codex/aiipd-application` under `app/aiipd/`), following the safety checklist in handover doc `00` Section 8.
10. Do TASK-007 (push Hearts Co-op codebase to `codex/hearts-coop-website` under `app/hearts-coop/`), confirming the Hearts logo is included.
11. Begin TASK-008a (resolve doc 01 `[VERIFY]` items) — this is the largest single task; budget the most time for it. Work through each `[VERIFY]` marker in document order, update doc 01 as findings are confirmed.
12. Continue with TASK-008b (doc 02) and TASK-008c (docs 03/04).
13. Complete TASK-009 (confirm public workspace access scope) using findings from TASK-008a.
14. Complete TASK-010 (implement middleware route protection) using the scope confirmed in TASK-009.
15. Complete TASK-011 (confirm and label the demo-backed report endpoint, create Phase 4 tracking note).
16. Complete TASK-012 (council-benchmark to civic-intelligence migration plan, plan only).
17. Complete TASK-013 (Prisma enum/model rename migration sequence, plan only).
18. At end of session, update this document's task table Status column for any tasks completed or progressed, and leave a short handoff note for the next session referencing routing key `AIIPD-BRIDGE-CLAUDE-TO-CODEX-V1`.

---

## Open questions for Liam

Pulled from Master Spec v0.2 Section 22 ("Open Decisions") and the broader change summary. Each requires a yes/no or choice answer before the related Phase 0/1 work can proceed with confidence.

- [ ] **Public site strategy** (Section 22, item 1): Keep `public/index.html` as a static site for speed, or migrate the homepage into Next.js for maintainability? (Affects TASK-012 and Phase 1 navigation work.)
- [ ] **Moodle provider** (Section 22, item 2): MoodleCloud, self-hosted Moodle, or a managed Moodle provider? (Affects Phase 3 but should be decided early so `MOODLE_BASE_URL`/`MOODLE_API_TOKEN` provisioning in TASK-005/TASK-008b can be scoped correctly.)
- [ ] **Publishing engine** (Section 22, item 3): Build a custom HTML/CSS/PDF pipeline, or integrate a third-party document editor/export service? (Affects Phase 5, no Phase 0 dependency, but worth flagging early.)
- [ ] **CRM and email** (Section 22, item 4): HubSpot, Mailchimp, Brevo, or another CRM/email platform? (No Phase 0 dependency.)
- [ ] **Social media automation** (Section 22, item 5): Manual publishing first, or API-based scheduling from the start? (No Phase 0 dependency.)
- [ ] **Payment model** (Section 22, item 6): Stripe subscriptions only, or Stripe plus invoiced enterprise contracts? (No Phase 0 dependency, but affects the entitlement schema design referenced in TASK-013's broader context.)
- [ ] **Storage** (Section 22, item 7): Supabase Storage, Google Drive, SharePoint/OneDrive connector, or a mixed storage model? (No Phase 0 dependency.)
- [ ] **Report export** (Section 22, item 8): HTML/PDF first with DOCX later, or DOCX-first for client editing? (Relevant to TASK-011's Phase 4 tracking note — affects how the modular report engine is scoped.)
- [ ] **AppShell typed-route fix approach** (TASK-001): if the proper typed-route fix turns out to be non-trivial, is a temporary `typedRoutes` opt-out acceptable as an interim measure, with a follow-up task to re-enable it properly?
- [ ] **`council-benchmark/` -> `civic-intelligence/` rename timing** (TASK-012, Master Spec Section 3.1 migration note): confirm this stays scoped to Phase 1 and is not pulled forward into Phase 0.
- [ ] **Prisma enum/model rename timing** (TASK-013, Master Spec Section 3.3 migration note): confirm whether the additive enum changes (adding new report-type values without removing old ones) can begin in Phase 0, or should wait until Phase 1.
- [ ] **`AIIPD_ADMIN` designation** (handover doc 02 gate 3.3): who is the named administrator for the live database? Needed before TASK-010 testing and before Phase 1 (Weeks 3-4) begins.
- [ ] **Missing partner token** (handover doc 02 gate 3.2): which integration does this refer to? Needed to scope TASK-005 and TASK-008b correctly.
