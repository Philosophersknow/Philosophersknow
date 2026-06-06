# AIIPD Master Technical Specification

Version: 0.1  
Date: 6 June 2026  
Owner: Liam Michael Clancy / AIIPD  
Repository: AIIPD_Website_Live_Package_v7  
Status: Draft master specification for next-phase development

---

## 1. Purpose

This document is the master technical specification for the AIIPD website, application, platform, dashboard and next-phase product infrastructure.

AIIPD must be treated as a unified Civic, Compliance, Skills, Candidate and Publishing Intelligence Platform, not as a loose collection of disconnected services. All technical work should support the core architecture:

Evidence -> Intelligence -> Published Product -> Strategic Action

The platform transforms fragmented public, organisational and training information into evidence-based intelligence products. The Dynamic Relational Model of Consciousness (DRMC) is the underlying analytical framework, not the primary headline product.

## 2. Strategic Product Model

### 2.1 Intelligence Centres

The product architecture is organised around five public-facing intelligence pathways:

1. Civic Intelligence
   - Councils, governments, candidates, consultants and community organisations.
   - Outputs include Place Intelligence Reports, Governance Reviews, Community Intelligence Profiles, Budget Impact Reports, Policy Shock Impact Reports and Resident Validation Surveys.

2. Compliance Intelligence
   - RTOs, NDIS providers, aged care, childcare and human services providers.
   - Outputs include Compliance Readiness Reports, Evidence Registers, policy reviews, audit preparation packs and quality assurance scans.

3. Skills and Workforce Intelligence
   - RTOs, employers, councils, workforce planners and Jobs and Skills bodies.
   - Outputs include Skills Demand Reports, Course Opportunity Reports, workforce demand alerts, badge readiness maps and training publication plans.

4. Candidate Intelligence
   - Candidates, councillors, independents and civic leaders.
   - Outputs include Candidate Intelligence Briefs, Local Area Intelligence Reports, Policy Position Statements, Resident Listening Toolkits and public communication drafts.
   - Ethical boundary: no misinformation, private voter profiling, smear campaigns, fake grassroots activity, covert persuasion or manipulative targeting.

5. Publishing Intelligence
   - Sector-specific evidence-to-publication infrastructure.
   - Outputs include learner guides, assessor guides, intelligence reports, white papers, executive briefs, ISBN-ready publications, co-branded reports and white-labelled outputs.

### 2.2 Platform Modules

Existing product names must be retained, but their hierarchy changes. They are AIIPD Intelligence Modules inside the platform, not standalone disconnected products.

Compliance Intelligence Modules:
- AuditReady: audit preparation, evidence registers and compliance gap scanning.
- PolicySmith: policy generation, review and alignment.
- EvidenceMapper: maps documents, assessments and compliance artefacts to required standards.
- QualityGuard: continuous quality assurance and risk flagging.

Skills and Workforce Intelligence Modules:
- CourseOpportunity Finder: identifies training demand from budgets, labour-market signals and economic modelling.
- SkillsMap: maps course content to skills, jobs, badges and workforce needs.
- BadgeReady: prepares training outputs for digital badging and skills wallet alignment.
- WorkforceSignal: detects emerging employment and training opportunities.

Publishing Intelligence Modules:
- CourseBuilder: learner guides, trainer guides and assessment tools.
- ReportBuilder: intelligence reports, policy briefs and executive summaries.
- PublicationSmith: long-form documents, white papers and ISBN-ready publications.
- BrandPress: co-branded and white-label publication outputs.

Civic Intelligence Modules:
- PlaceScan: council and place profile generation.
- PolicyShock: Federal, State and jurisdictional policy impact reports.
- CivicPulse: resident survey and lived-experience validation.
- ComparatorMap: national and international council comparison.

Candidate Intelligence Modules:
- IssueBrief: local issue summaries and evidence briefs.
- PositionBuilder: policy position drafting with trade-offs and evidence notes.
- ResidentListen: survey, door-knocking and community listening tools.
- CampaignPress: flyers, newsletters, community updates and candidate statements.
- ForumReady: debate, forum and public question preparation.

---

## 3. Current Repository Structure

Current repository root:

```text
AIIPD_Website_Live_Package_v7/
  public/
    index.html
    council-benchmark/
    assets/
  src/
    app/
    components/
    lib/
    types/
  prisma/
    schema.prisma
  scripts/
  docs/
  data/
  assets/
```

### 3.1 Public Static Website

Primary file:

```text
public/index.html
```

Current role:
- Public-facing AIIPD website.
- Hosted locally via static preview at `http://127.0.0.1:4173/index.html`.
- Contains homepage, hero, intelligence centres, assistant demo, council benchmarking, training, publishing, pricing, ethics, FAQ, contact, legal modals and footer.

Technical characteristics:
- Single large static HTML file.
- Embedded CSS.
- Embedded JavaScript for tabs, accordions, FAQ, guided assistant demo, contact success state and modal controls.
- Uses `public/assets/images` and `public/assets/data`.

Development rule:
- Preserve existing anchors unless intentionally changing navigation.
- Keep public demo assistant guided and labelled as sample scenarios.
- Do not claim live real-time analysis on the public static homepage.

### 3.2 Next.js Application

Primary framework:
- Next.js 15.
- React 19.
- TypeScript.
- App Router under `src/app`.

Current routes:

```text
src/app/page.tsx
src/app/evidence/page.tsx
src/app/reports/page.tsx
src/app/admin/import/page.tsx
src/app/api/assistant/route.ts
src/app/api/reports/route.ts
src/app/api/auth/[...nextauth]/route.ts
```

Current role:
- Early authenticated platform scaffold.
- Council Intelligence Dashboard.
- Evidence workspace.
- Report workspace.
- Admin import page.
- API assistant route.
- Report API route.

Known current issue:
- `npm run build` and `npm run typecheck` fail because `src/components/AppShell.tsx` passes `string` href values to typed Next.js `Link` routes.
- `npm run lint` prompts for ESLint configuration because the project has not completed migration from `next lint`.

### 3.3 Database and ORM

Primary ORM:
- Prisma.

Database:
- PostgreSQL, configured via `DATABASE_URL`.
- Supabase is referenced in project materials as the intended hosted database provider.

Primary schema:

```text
prisma/schema.prisma
```

Current major models:
- User, Account, Session, VerificationToken.
- Council, CouncilUser.
- MetricDefinition, CouncilMetric.
- DrmcLayer, DrmcScore, DrmcScoreClaim.
- Document, SourceVerification.
- BudgetMeasure, CouncilExposure.
- BenchmarkScore, ReadinessScore.
- CouncilAction.
- ReportOutput.
- ImportRun, ImportError.

Current report types:
- BENCHMARK.
- MAYOR_BRIEF.
- BUDGET_IMPACT.
- COUNCILLOR_INFO_PACK.

---

## 4. Target Architecture

### 4.1 High-Level Architecture

Target architecture:

```text
Public Website
  -> lead capture
  -> sample outputs
  -> blog/resources
  -> product positioning

Authenticated Platform
  -> subscriber dashboard
  -> evidence workspace
  -> intelligence modules
  -> report generation
  -> publishing studio
  -> LMS access
  -> scheduled updates

Data Layer
  -> Supabase PostgreSQL
  -> source registers
  -> uploaded files metadata
  -> generated reports
  -> subscriptions and entitlements
  -> audit logs

Integration Layer
  -> Moodle LMS
  -> payment/subscription system
  -> email and CRM
  -> social media publishing
  -> document storage
  -> scheduled jobs
  -> analytics with consent
```

### 4.2 Application Surfaces

The platform should eventually have these surfaces:

1. Public Website
   - Static or Next-rendered marketing site.
   - Blog and resource pages.
   - Sample intelligence outputs.
   - Product ladder and lead capture.

2. Subscriber Portal
   - Authenticated dashboard.
   - Subscription-specific access.
   - Intelligence pathway selector.
   - Report credits and module access.
   - Moodle course access.
   - Publication studio access.

3. Admin / Analyst Console
   - Data imports.
   - Source verification.
   - Report generation.
   - Human review workflow.
   - Subscriber and licence management.
   - Scheduled update management.

4. Client Workspace
   - Client-specific evidence registers.
   - Uploaded documents.
   - Draft outputs.
   - Approvals.
   - Export history.

5. Publishing Studio
   - Designrr-like output builder.
   - Report/book/manual templates.
   - Versioned publication packages.
   - PDF/DOCX/HTML export.
   - QR-linked latest approved version.

6. Moodle LMS Integration Surface
   - Subscriber and licence-holder learning access.
   - Course enrolment.
   - CPD tracking.
   - Training resource delivery.
   - Licence-based cohorts.

---

## 5. Roles and Access Control

Current roles in Prisma:
- AIIPD_ADMIN.
- ANALYST.
- COUNCIL_ADMIN.
- COUNCIL_VIEWER.

Target roles:

1. AIIPD_ADMIN
   - Full platform administration.
   - Subscription, billing, entitlement and integration management.
   - Can approve platform-wide configuration.

2. AIIPD_ANALYST
   - Data review, source verification, report generation and human review.
   - Cannot manage billing or system secrets.

3. CLIENT_ADMIN
   - Manages organisation users.
   - Uploads documents.
   - Approves final outputs for organisation use.

4. CLIENT_REVIEWER
   - Reviews draft outputs.
   - Adds comments and corrections.

5. SUBSCRIBER
   - Accesses subscribed modules, report credits, resources and Moodle content.

6. LICENCE_HOLDER
   - Accesses licensed resources, training, publication tools or white-label outputs.

7. CANDIDATE_USER
   - Accesses Candidate Intelligence with additional ethical constraints.

8. PUBLIC_USER
   - Accesses public pages, sample outputs and lead magnets.

Implementation requirement:
- Extend `Role` enum or introduce `Membership`, `Organisation`, `Entitlement` and `Subscription` tables instead of overloading council-specific roles.

---

## 6. Data Architecture

### 6.1 Core Data Principles

Data must preserve separation between:
- Raw public source data.
- Uploaded client documents.
- Structured extracted data.
- AI-assisted suggestions.
- Analyst interpretation.
- Verified findings.
- Published outputs.

Every source-backed claim should support:
- Source title.
- Source URL or file reference.
- Publication date where available.
- Date accessed.
- Source type.
- Reliability rating.
- Verification status.
- Confidence level.
- Analyst comments.
- Related intelligence pathway.
- Related DRMC/RSC interpretation where applicable.

### 6.2 Required New Tables

Recommended next schema additions:

```text
Organisation
Subscription
Entitlement
ModuleAccess
ReportCreditLedger
UploadedDocument
DocumentProcessingRun
EvidenceClaim
IntelligenceProject
IntelligenceOutput
OutputVersion
ReviewWorkflow
ReviewComment
PublicationTemplate
PublicationAsset
MoodleCourseLink
MoodleEnrolment
BlogPost
SocialAccount
SocialPost
ScheduledUpdate
BudgetDataset
BudgetMeasureSource
BudgetImpactModel
BudgetImpactRun
AuditLog
ConsentRecord
```

### 6.3 Organisation and Entitlement Model

Organisations should be the parent unit for subscriptions, licence holders and client workspaces.

Suggested relationships:

```text
Organisation
  -> users
  -> subscriptions
  -> entitlements
  -> uploaded documents
  -> intelligence projects
  -> outputs
  -> Moodle enrolments
```

Entitlements should define:
- Intelligence centres enabled.
- Modules enabled.
- Monthly report credits.
- Publishing output allowance.
- Moodle course access.
- White-label rights.
- API access.
- Human review level.
- Storage limits.
- Data retention policy.

---

## 7. Moodle LMS Integration

### 7.1 Purpose

Moodle integration must provide subscriber and licence-holder access to AIIPD learning products, certification pathways, CPD materials and training resources.

Target users:
- Subscribers.
- Licence holders.
- RTO staff.
- Consultants.
- Council users.
- Candidate/civic leadership users where appropriate.

### 7.2 Integration Options

Phase 1: Manual / semi-automated integration
- Create Moodle courses manually.
- Store Moodle course links in AIIPD.
- Grant access through enrolment codes or manually managed Moodle cohorts.
- AIIPD portal displays available courses based on entitlement.

Phase 2: API-based enrolment
- Use Moodle Web Services API.
- Create or update Moodle user from AIIPD account.
- Enrol users into courses based on subscription or licence.
- Sync completion status back to AIIPD.

Phase 3: Unified learning entitlement layer
- AIIPD becomes the source of truth for subscription and licence access.
- Moodle handles learning delivery, quizzes, completion and certificates.
- AIIPD displays consolidated subscriber dashboard.

### 7.3 Required Moodle Entities

Moodle-side:
- Courses.
- Categories by Intelligence Centre.
- Cohorts.
- Users.
- Enrolments.
- Completion records.
- Certificates or badges.

AIIPD-side:
- `MoodleCourseLink`.
- `MoodleEnrolment`.
- `LearningProgress`.
- `CertificateRecord`.

### 7.4 Moodle Security Requirements

- Do not hard-code Moodle API tokens.
- Store tokens in environment variables or secure secrets manager.
- Use least-privilege Moodle service account.
- Log enrolment changes.
- Do not expose Moodle admin URLs publicly.
- Ensure licence expiry removes or downgrades access according to contract terms.

---

## 8. Publishing Studio: Designrr-Like Platform

### 8.1 Purpose

AIIPD needs a Designrr-like publishing platform for subscribers and licence holders. The goal is not generic formatting; it is sector-specific evidence-to-publication infrastructure.

Outputs:
- Learner guides.
- Assessor guides.
- Trainer guides.
- Compliance manuals.
- Intelligence reports.
- White papers.
- Industry reports.
- Candidate briefs.
- Executive briefings.
- ISBN-ready publications.
- Co-branded and white-labelled reports.

### 8.2 Core Workflow

```text
Select output type
  -> choose template
  -> select evidence/project
  -> generate structured draft
  -> edit sections
  -> apply brand/template
  -> review evidence traceability
  -> human approval
  -> export PDF/DOCX/HTML
  -> publish or archive
```

### 8.3 Required Features

Minimum viable publishing studio:
- Template library.
- Section-based editor.
- Report outline builder.
- Evidence claim insertion.
- Citation/source register block.
- Branding controls.
- Cover page builder.
- Export to HTML and PDF.
- Version history.
- Human approval status.

Future features:
- DOCX export.
- ISBN metadata support.
- QR-linked latest approved version.
- Client branding kits.
- Multilingual output variants.
- Co-branded report packs.
- White-label publishing rights.
- Content block reuse.
- Accessibility checks.
- Print-ready PDF settings.

### 8.4 QR and Analytics Rule

QR-linked updates can direct learners or readers to the latest approved version of a resource. Analytics should only be enabled with consent, clear privacy settings and client approval.

Do not implement covert reader tracking.

---

## 9. Blog and Resource Publishing

### 9.1 Purpose

The blog must support public credibility, search visibility, policy commentary, budget impact analysis, training updates and publishing of selected intelligence insights.

Content types:
- Blog posts.
- Intelligence briefs.
- Policy shock updates.
- Budget impact summaries.
- Skills demand alerts.
- RTO compliance updates.
- Candidate/civic leadership notes.
- Case studies.
- White paper landing pages.

### 9.2 Recommended Architecture

Phase 1:
- Markdown or database-backed blog inside Next.js.
- Public routes:
  - `/blog`
  - `/blog/[slug]`
  - `/resources`
  - `/resources/[slug]`

Phase 2:
- Admin editor.
- Draft/review/publish workflow.
- SEO metadata controls.
- Category and tag system.
- Newsletter integration.

Phase 3:
- Convert selected reports into public blog/resource summaries.
- Link gated downloads to subscriber lead magnets.

### 9.3 Blog Data Model

Recommended fields:
- id.
- slug.
- title.
- subtitle.
- summary.
- body.
- author.
- status.
- category.
- tags.
- source links.
- hero image.
- publishedAt.
- updatedAt.
- canonicalUrl.
- relatedOutputs.

---

## 10. Social Media Integration

### 10.1 Purpose

AIIPD needs controlled social media connection for publishing approved updates, not automated noise.

Target channels:
- LinkedIn.
- Facebook.
- X/Twitter if strategically useful.
- YouTube for video briefings.
- Email newsletter.

### 10.2 Required Capabilities

Phase 1:
- Store social account metadata.
- Draft social snippets from approved blog posts or reports.
- Manual copy/export.

Phase 2:
- OAuth connection to social platforms where APIs and account permissions allow.
- Scheduled publishing queue.
- Approval workflow before posting.
- UTM tagging.

Phase 3:
- Cross-channel campaign planning.
- Performance dashboard using privacy-safe aggregated metrics.
- Repurpose intelligence outputs into approved social cards, email summaries and briefing posts.

### 10.3 Social Media Safety Rules

- No political manipulation.
- No private voter profiling.
- No covert persuasion.
- No automated candidate smear content.
- Candidate Intelligence posts must be evidence-based and human-approved.
- Analytics must be aggregated and consent-aware.

---

## 11. Automated Report Production

### 11.1 Purpose

Automated report production must reduce manual workload while preserving source traceability, caveats and human review.

Report types:
- Council / Place Intelligence Report.
- Budget Impact Report.
- Policy Shock Impact Report.
- Skills Demand Report.
- Compliance Readiness Report.
- Evidence Register.
- Candidate Intelligence Brief.
- Publication-Ready Output.

### 11.2 Report Pipeline

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

### 11.3 Required Report Generator Improvements

Current `src/lib/report-generator.ts` is a demo generator. It should be replaced with a modular report engine:

Recommended modules:
- `report/types.ts`.
- `report/templates/`.
- `report/sections/`.
- `report/evidence-summary.ts`.
- `report/render-html.ts`.
- `report/render-pdf.ts`.
- `report/render-docx.ts`.
- `report/versioning.ts`.
- `report/review-workflow.ts`.

Report outputs must include:
- Title.
- Executive summary.
- Scope and caveats.
- Evidence base.
- Source register.
- Intelligence lens.
- Findings.
- Confidence levels.
- Recommendations.
- Human review status.
- Version and date.

### 11.4 Human Review Gate

No automated report should become final without:
- Review status.
- Reviewer identity.
- Approval timestamp.
- Version number.
- Source verification summary.
- Caveat block where needed.

---

## 12. Scheduled Updates

### 12.1 Purpose

Scheduled updates allow AIIPD to keep reports, dashboards, budget impact analysis, blog items and subscriber briefings current.

Use cases:
- Weekly source freshness check.
- Monthly council document scan.
- Budget release monitoring.
- Training package updates.
- Compliance standards updates.
- Subscriber newsletter generation.
- Social post scheduling.
- Moodle enrolment reconciliation.

### 12.2 Technical Options

Option A: Vercel Cron
- Suitable for scheduled Next.js API routes.
- Simple for early stage.

Option B: Supabase Edge Functions / Scheduled Jobs
- Suitable if database-driven.

Option C: GitHub Actions
- Suitable for periodic batch jobs and static artefact generation.

Option D: External queue system
- Later phase only, when scale requires it.

### 12.3 Recommended Phase 1

Use Vercel Cron or GitHub Actions for:
- Weekly source check.
- Monthly budget impact refresh.
- Moodle enrolment reconciliation.
- Blog draft generation from approved internal notes.

Store every run in `ScheduledUpdate` with:
- job type.
- startedAt.
- completedAt.
- status.
- records processed.
- warnings.
- errors.
- nextRunAt.

---

## 13. Budget Impact Measurement Framework

### 13.1 Purpose

Budget Impact Intelligence translates Federal, State and jurisdictional budgets into targeted implications for councils, RTOs, consultants, candidates and community organisations.

### 13.2 Existing Schema Support

Current models already support the first stage:
- `BudgetMeasure`.
- `CouncilExposure`.

These should be expanded into a full budget impact framework.

### 13.3 Required Inputs

Budget inputs:
- Federal Budget papers.
- State and Territory Budget papers.
- Portfolio Budget Statements.
- Grants and program announcements.
- Infrastructure commitments.
- Housing, climate, health, NDIS, aged care and transport measures.
- Skills and workforce funding announcements.
- Regional economic indicators.
- Local council context.

### 13.4 Impact Dimensions

Council impact:
- Infrastructure.
- Housing.
- Climate.
- Service delivery.
- Cost shifting.
- Community pressure.
- Local economic development.
- Governance and engagement risk.

RTO / Skills impact:
- Training demand.
- Funded course opportunity.
- Employment pathways.
- Apprenticeships/traineeships.
- Skills shortage pressure.
- Regional workforce gaps.

Candidate / Civic leadership impact:
- Local issues.
- Policy trade-offs.
- Public communication needs.
- Community listening priorities.

### 13.5 Scoring Rule

Budget impact scoring must be transparent and reviewable.

Do not present scores as certain predictions.

Each impact output should include:
- Measure.
- Source.
- Geography.
- affected sectors.
- likely local pressure.
- confidence.
- evidence quality.
- assumptions.
- analyst comments.
- recommended action.

### 13.6 Budget Impact Pipeline

```text
Budget source ingested
  -> measures extracted
  -> source metadata recorded
  -> affected sectors tagged
  -> geography tagged
  -> exposure model applied
  -> draft impact brief generated
  -> analyst review
  -> client-specific output created
  -> scheduled update set
```

---

## 14. Authentication, Subscriptions and Payments

### 14.1 Current State

Current auth:
- NextAuth credentials provider.
- Demo password via `DEMO_ADMIN_PASSWORD`.
- JWT session strategy.

Target auth:
- Production email/password or passwordless login.
- Organisation membership.
- Role-based and entitlement-based access.
- Optional SSO later for enterprise clients.

### 14.2 Payment and Subscription Provider

Recommended early-stage provider:
- Stripe for subscriptions, product purchases and invoices.

Required integration:
- Product catalogue.
- Subscription tiers.
- Webhook handling.
- Entitlement provisioning.
- Invoice records.
- Failed payment handling.
- Cancellation and downgrade logic.

---

## 15. File Upload and Document Processing

### 15.1 Purpose

Subscribers and licence holders need to use public datasets or securely upload authorised documents.

Document categories:
- Council reports.
- Budgets.
- Strategic plans.
- Consultation reports.
- RTO policies.
- Assessment tools.
- Mapping documents.
- Training material.
- Survey results.
- Client-approved source material.

### 15.2 Requirements

Upload workflow:
- Authenticated upload.
- Virus/malware scan where provider supports it.
- File metadata record.
- Organisation ownership.
- Processing status.
- Extraction run.
- Source claim creation.
- Review queue.

Security:
- Do not store unnecessary personal data.
- Respect client deletion requests.
- Keep document access organisation-scoped.
- Record consent and authority to process.

---

## 16. API Design

Current API:
- `/api/assistant`.
- `/api/reports`.
- `/api/auth/[...nextauth]`.

Target API groups:

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

API requirements:
- Validate input with Zod or equivalent.
- Enforce auth and organisation scope.
- Log sensitive operations.
- Return clear error messages.
- Do not expose secrets.
- Separate public demo routes from authenticated production routes.

---

## 17. Security, Privacy and Ethics

### 17.1 Core Rules

- Use public institutional data wherever possible.
- Do not collect private citizen personal data unless there is a clear authorised purpose.
- Do not profile private residents, voters, complainants or consultation participants.
- Public officials may be referenced only in their public role and where relevant.
- Store the minimum data required.
- Make source status, confidence and verification visible.
- AI-assisted outputs require human review before formal use.

### 17.2 DRMC/RSC Caveat

DRMC/RSC outputs are interpretive civic intelligence assessments. They are not:
- Psychological diagnoses.
- Moral rankings.
- Validated psychological measurements.
- Automated character judgements.

### 17.3 Candidate Intelligence Caveat

Candidate Intelligence supports:
- Civic issue literacy.
- Evidence-based communication.
- Public leadership preparation.
- Community listening.

Candidate Intelligence must not support:
- Misinformation.
- Smear campaigns.
- Private voter profiling.
- Fake grassroots activity.
- Covert persuasion.
- Manipulative targeting.

---

## 18. Development Roadmap

### Phase 0: Stabilise Current Platform

Tasks:
- Fix typed route build issue in `src/components/AppShell.tsx`.
- Configure ESLint for Next.js 15 or migrate from `next lint`.
- Confirm `.next/types` handling in `tsconfig.json`.
- Keep public homepage static preview working.
- Document environment variables.

### Phase 1: Product Architecture Consolidation

Tasks:
- Convert public homepage to Next.js route or keep static and mirror core content into app.
- Create Intelligence Centre landing pages.
- Add sample output downloads or gated lead magnets.
- Standardise terminology across public site and portal.
- Add organisation and entitlement schema.

### Phase 2: Subscriber Portal

Tasks:
- Production auth.
- Organisation workspaces.
- Subscription and entitlement management.
- Report credits.
- Module access controls.
- Evidence workspace improvements.

### Phase 3: Moodle LMS Integration

Tasks:
- Add Moodle course link model.
- Manual enrolment workflow.
- API enrolment proof of concept.
- Course completion sync.
- Licence-holder access rules.

### Phase 4: Automated Report Engine

Tasks:
- Replace demo report generator.
- Build modular report templates.
- Add source register rendering.
- Add review and approval workflow.
- Add HTML/PDF export.
- Add version history.

### Phase 5: Publishing Studio

Tasks:
- Template library.
- Section-based editor.
- Brand kits.
- PDF/DOCX/HTML export.
- QR-linked latest approved version.
- Publication workflow and add-on entitlement.

### Phase 6: Blog, Resource Hub and Social Publishing

Tasks:
- Blog routes.
- Admin editor.
- Draft/review/publish workflow.
- Social account metadata.
- Manual social snippets.
- Scheduled publishing with approval.

### Phase 7: Budget Impact Intelligence Framework

Tasks:
- Expand budget source schema.
- Build budget ingestion workflow.
- Define impact dimensions and scoring logic.
- Add council/RTO/candidate-specific outputs.
- Schedule budget update jobs.
- Add analyst review workflow.

### Phase 8: Automation and Scheduled Updates

Tasks:
- Scheduled source checks.
- Subscriber briefing generation.
- Report freshness alerts.
- Moodle enrolment reconciliation.
- Social post scheduling.
- Budget impact refresh.

---

## 19. Immediate Technical Priorities

1. Fix build/typecheck.
   - `src/components/AppShell.tsx` typed route issue.
   - ESLint setup/migration.

2. Decide public site architecture.
   - Keep static `public/index.html` for immediate hosting, or migrate homepage into Next.js.
   - Avoid maintaining two divergent public sites long-term.

3. Add organisation/subscription/entitlement schema.
   - Required before Moodle, modules, subscriber portal and publishing studio can be safely controlled.

4. Define report output contract.
   - One shared schema for intelligence products, source registers, caveats and review status.

5. Create Moodle integration proof of concept.
   - Manual course links first.
   - API enrolment second.

6. Build Budget Impact Intelligence data model.
   - Extend `BudgetMeasure` and `CouncilExposure`.
   - Add source and run tracking.

7. Create Publishing Studio MVP.
   - Use HTML templates and PDF export first.
   - Add DOCX and advanced styling later.

---

## 20. Environment Variables

Known or expected variables:

```text
DATABASE_URL
DEMO_ADMIN_PASSWORD
ANTHROPIC_API_KEY
NEXTAUTH_SECRET
NEXTAUTH_URL
STRIPE_SECRET_KEY
STRIPE_WEBHOOK_SECRET
MOODLE_BASE_URL
MOODLE_API_TOKEN
GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET
LINKEDIN_CLIENT_ID
LINKEDIN_CLIENT_SECRET
```

Rules:
- Never hard-code secrets.
- Keep `.env.local` out of version control.
- Document required variables in `.env.example`.

---

## 21. Definition of Done

A feature is not complete until:
- It is scoped to an Intelligence Centre or platform infrastructure function.
- It preserves source traceability.
- It has role/entitlement rules.
- It has human review rules where outputs are high-stakes.
- It avoids unsupported claims.
- It has basic validation and error handling.
- It has a test or documented verification path.
- It is documented in this specification or linked implementation notes.

---

## 22. Open Decisions

1. Public site strategy:
   - Static site for speed vs Next.js migration for maintainability.

2. Moodle provider:
   - MoodleCloud vs self-hosted Moodle vs managed Moodle provider.

3. Publishing engine:
   - Build custom HTML/CSS/PDF pipeline vs integrate a third-party document editor/export service.

4. CRM and email:
   - HubSpot, Mailchimp, Brevo or another CRM/email platform.

5. Social media automation:
   - Manual publishing first vs API scheduling.

6. Payment model:
   - Stripe subscriptions only vs Stripe plus invoiced enterprise contracts.

7. Storage:
   - Supabase Storage, Google Drive, SharePoint/OneDrive connector or mixed storage model.

8. Report export:
   - HTML/PDF first, DOCX later vs DOCX-first for client editing.

---

## 23. Non-Negotiable Safeguards

- AI does not make final civic, ethical, regulatory, political or compliance judgements.
- Candidate Intelligence must not become voter manipulation infrastructure.
- DRMC/RSC outputs must remain interpretive and caveated.
- Uploaded client documents must only be used for authorised analysis and output generation.
- Public examples must be labelled if simulated.
- No fake precision.
- No claims of validated measurement unless validation evidence exists.
- Human review remains mandatory for formal use.

