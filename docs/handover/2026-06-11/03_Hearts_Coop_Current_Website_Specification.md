# Hearts Co-op Current Website Specification

**Version:** 0.1-draft
**Date:** 11 June 2026
**Status:** DRAFT — pending Codex verification once codebase is pushed

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

This document is a draft current-state specification for the Hearts Co-op website, prepared as part of the same developer handover pack as the AiIPD documents (Documents 1 and 2). Hearts Co-op is, as currently understood, a separate static website with no application backend and no database, distinct from the AiIPD platform described in Documents 1 and 2.

This draft is written without access to the live Hearts Co-op codebase. Every architectural detail below is therefore marked `[VERIFY]` and should be treated as a placeholder structure to be confirmed once the codebase is pushed to GitHub per `00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md` (section 2.2, Hearts Co-op codebase). The purpose of this document is to give Codex a checklist against which to confirm or correct the as-built reality, not to assert facts about the live site.

Two items are known with reasonable confidence from the brief rather than from the codebase: the authoritative domain is `www.heartscoop.com`, and the Hearts Co-op logo exists locally but is not yet tracked in any repository. Both are addressed below as action items.

---

## 1. As-Built Architecture

`[VERIFY: all items in this section — codebase not yet accessible]`

As currently understood from the brief:

- Hearts Co-op is a static website.
- The site is structured around 11 content sections (see section 2 below for placeholder section list).
- The site includes one expression-of-interest (EOI) form, which submits via a `mailto:` link rather than a server-side form handler.
- There is no database.
- There is no application backend (no API routes, no server-side logic beyond static hosting).

`[VERIFY: confirm whether the site is built with plain HTML/CSS/JS, a static site generator, or a minimal Next.js static export — Document 1 describes the AiIPD public site as a single static `index.html`; confirm whether Hearts Co-op follows a similar pattern or a different one]`

---

## 2. Content Structure

The table below is a placeholder. Section names, order, and count (11 sections, per the brief) require confirmation against the live site.

| Section | Purpose | Status |
|---|---|---|
| Section 1 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 2 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 3 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 4 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 5 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 6 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 7 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 8 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 9 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 10 | `[VERIFY: confirm actual section name]` | `[VERIFY: confirm actual section names and order against live site]` |
| Section 11 (EOI form) | Expression-of-interest capture, submitting via `mailto:` | `[VERIFY: confirm actual section names and order against live site]` |

`[VERIFY: based on common co-operative/community organisation site structures, plausible section names might include Home/Hero, About, Mission/Values, Membership, Governance, Projects/Programs, News/Updates, Get Involved, FAQ, Contact, and the EOI form — but these are illustrative only and must not be treated as confirmed]`

---

## 3. Branding and Assets

The Hearts Co-op logo is available locally but is currently **untracked** in any repository.

**Action item:** Add the logo to the Hearts Co-op codebase repository (or its assets folder) as part of the codebase publish described in `00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md`, section 2.2 and the safety checklist (section 8): "Hearts logo added to assets (currently untracked locally per brief)".

`[VERIFY: confirm logo file format, dimensions, and current storage location prior to adding to the repository]`

---

## 4. Domain

The authoritative domain for Hearts Co-op is **`www.heartscoop.com`**.

The brief notes that the README and the live site currently reference an incorrect domain, **`www.hearts.com`**, and that this needs correction.

**Action items:**

- Audit the Hearts Co-op codebase (README, site footer, metadata, structured data, any hard-coded links) for references to `www.hearts.com` and replace them with `www.heartscoop.com`.
- Confirm whether `www.hearts.com` is held by Hearts Co-op or a third party. If held, configure a redirect from `www.hearts.com` to `www.heartscoop.com` (see section 6, Acceptance Requirements, deployment).
- Confirm DNS and hosting configuration for `www.heartscoop.com` once the codebase is accessible.

`[VERIFY: confirm all locations in the codebase referencing www.hearts.com]`

---

## 5. Deployment Configuration

`[VERIFY: Codex to document current hosting/deployment setup]`

This section is a placeholder pending codebase access. Once available, this section should record:

- Hosting provider and deployment method (for example, static hosting, Vercel, Netlify, GitHub Pages).
- Build and deploy pipeline, if any.
- Domain and DNS configuration for `www.heartscoop.com`.
- HTTPS/TLS certificate configuration.
- Any redirect configuration from `www.hearts.com`, if that domain is held (see section 4).

---

## 6. Acceptance Requirements

The following acceptance requirements apply to the Hearts Co-op website regardless of its current implementation state. They should be used as a checklist for any work undertaken on the site.

### 6.1 Accessibility

- Baseline: WCAG 2.1 Level AA conformance across all 11 sections.
- `[VERIFY: confirm current accessibility status — likely not yet assessed]`

### 6.2 Performance

- Baseline: Core Web Vitals targets (Largest Contentful Paint, Interaction to Next Paint, Cumulative Layout Shift) within "Good" thresholds as defined by current Core Web Vitals guidance at time of assessment.
- `[VERIFY: confirm current Core Web Vitals scores once the live site is accessible]`

### 6.3 Legal review

- Privacy policy: required, covering any data collected via the EOI form.
- Terms of use: required.
- EOI data handling: the EOI form's data handling practices (where submissions go, how long they are retained, who has access) must be documented and reviewed for compliance with applicable privacy law.
- `[VERIFY: confirm whether a privacy policy, terms of use, or EOI data handling statement currently exist on the site]`

### 6.4 Form capture

- The EOI form must reach a monitored inbox. A `mailto:` link depends on the visitor's local mail client being configured correctly, which is not reliable across all users and devices.
- Spam protection for the EOI form must be confirmed (for example, a honeypot field, CAPTCHA, or equivalent), particularly if the form is migrated from `mailto:` to a server-side or third-party form handler.
- `[VERIFY: confirm current EOI form implementation, destination inbox, and spam protection]`

### 6.5 Deployment

- Custom domain: `www.heartscoop.com` must be the live, authoritative domain.
- HTTPS: the site must be served over HTTPS.
- Redirect: if `www.hearts.com` is held by Hearts Co-op, it must redirect to `www.heartscoop.com`.
- `[VERIFY: confirm current deployment meets these requirements]`

---

This document should be read alongside Document 4 (Hearts Co-op back-office foundation specification), which describes a proposed future platform that would integrate with this website's EOI capture but is architecturally separate from it.
