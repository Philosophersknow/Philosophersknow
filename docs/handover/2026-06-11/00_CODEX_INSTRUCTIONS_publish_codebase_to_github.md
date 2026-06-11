# Instructions for Codex — Publish AiIPD and Hearts Codebases to GitHub

**Routing key:** `AIIPD-BRIDGE-CLAUDE-TO-CODEX-V1`
**Requested by:** Liam Michael Clancy
**Date:** 11 June 2026
**Purpose:** Make the live AiIPD application codebase (and Hearts Co-op codebase) available on GitHub so that Claude (this session and future sessions), other AI agents, and human team members can collaborate on the platform build in parallel.

---

## 1. Why this is needed

Currently:

- The live AiIPD application (`AIIPD_Website_Live_Package_v7` — Next.js 15, React 19, TypeScript, Prisma, PostgreSQL/Supabase) exists only on local machines / G: drive.
- The Hearts Co-op static website and the proposed Hearts Co-op back-office platform are not yet on GitHub.
- Claude (running in an isolated cloud container) can only read/write files that exist in the `philosophersknow/philosophersknow` GitHub repository.
- Without the codebase on GitHub, Claude can write specifications and content, but cannot read actual routes, schema, components, or verify build/runtime status.

Pushing the codebases to GitHub turns this into a **shared online workspace** — the "online drive" — that any authorised AI agent or team member can clone, branch from, and contribute to.

---

## 2. What to push

### 2.1 AiIPD Application (`AIIPD_Website_Live_Package_v7`)

Push the **full current codebase** as it exists locally, including:

```text
public/
src/
prisma/
scripts/
docs/
data/
assets/
package.json
package-lock.json (or pnpm-lock.yaml / yarn.lock)
tsconfig.json
next.config.*
.env.example   (create if missing — see Section 4)
README.md
```

**Do NOT push:**
- `.env`, `.env.local`, or any file containing real secrets, API keys, database URLs or tokens.
- `node_modules/`
- `.next/` build output
- Any local database dump containing real council data, unless explicitly approved by Liam (see Section 5 — data handling).

### 2.2 Hearts Co-op Codebase

Push the current static Hearts Co-op website codebase, including:

```text
(static site files — HTML/CSS/JS or Next.js structure as currently built)
assets/ (including the Hearts logo — currently untracked locally; add it)
README.md
```

---

## 3. Where to push it

Target repository: `philosophersknow/philosophersknow`

### 3.1 Branch structure

Create the following branches, each based on `origin/claude/awesome-bardeen-dzqcI` (which contains the Master Specification v0.1/v0.2 and the Civic Intelligence content architecture):

| Branch | Contents |
|---|---|
| `codex/aiipd-application` | Full AiIPD Next.js/Prisma application codebase |
| `codex/hearts-coop-website` | Hearts Co-op static website codebase |
| `codex/update-master-specification` | (referenced in the handover pack brief — create this if it does not yet exist; can be used for ongoing spec updates from Codex's side) |

### 3.2 Commands

```bash
# From inside the AiIPD application's local git folder (or initialise one if it isn't a repo yet)
cd "G:\path\to\AIIPD_Website_Live_Package_v7"

git init   # only if not already a git repo
git remote add origin https://github.com/philosophersknow/philosophersknow.git
git fetch origin

# Create the AiIPD application branch from the Claude content branch
git checkout -b codex/aiipd-application origin/claude/awesome-bardeen-dzqcI

# Copy/merge the application source into the working tree at repo root
# (if the app currently lives in a subfolder, place it under /app/ to avoid
#  colliding with /content/ and /docs/ used by Claude — see Section 6)

git add .
git commit -m "Add AiIPD application codebase for shared development"
git push -u origin codex/aiipd-application
```

```bash
# Repeat for Hearts Co-op
cd "G:\path\to\hearts-coop-website"
git remote add origin https://github.com/philosophersknow/philosophersknow.git
git fetch origin
git checkout -b codex/hearts-coop-website origin/claude/awesome-bardeen-dzqcI
git add .
git commit -m "Add Hearts Co-op website codebase for shared development"
git push -u origin codex/hearts-coop-website
```

```bash
# Create the spec update branch (empty or with current spec working notes)
git checkout -b codex/update-master-specification origin/claude/awesome-bardeen-dzqcI
git push -u origin codex/update-master-specification
```

---

## 4. Environment variables — `.env.example`

Before pushing, create or update `.env.example` in the AiIPD application root listing **variable names only, no values**:

```text
DATABASE_URL=
DEMO_ADMIN_PASSWORD=
ANTHROPIC_API_KEY=
NEXTAUTH_SECRET=
NEXTAUTH_URL=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
MOODLE_BASE_URL=
MOODLE_API_TOKEN=
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
LINKEDIN_CLIENT_ID=
LINKEDIN_CLIENT_SECRET=
```

Add any additional variables discovered in the codebase that are not already listed in the Master Specification (Section 20).

---

## 5. Data handling — councils, documents, snapshots

The brief references real production figures (757 councils, 3,821 documents, 746 snapshots, 66 reports). Do **not** push raw database dumps or document content to GitHub.

If sample/seed data is needed for other agents and team members to develop against:

- Export a small, anonymised or already-public sample dataset (e.g. 5–10 councils' worth of public data already sourced from public registers).
- Place it under `prisma/seed/` or `data/sample/` with a clear README noting it is sample data only.
- Do not include any data that has not already been verified as sourced from public, attributable records.

---

## 6. Repository layout — avoiding collisions

This repository (`philosophersknow/philosophersknow`) currently contains, on `claude/awesome-bardeen-dzqcI`:

```text
content/        <- Civic Intelligence content architecture (Claude-owned)
docs/handover/  <- Developer handover pack (this document and others)
README.md
```

To avoid collisions when branches are eventually merged, place application code under top-level folders that don't clash:

```text
app/aiipd/        <- AiIPD Next.js application (from codex/aiipd-application)
app/hearts-coop/  <- Hearts Co-op website (from codex/hearts-coop-website)
content/          <- existing Civic Intelligence content (do not move)
docs/             <- existing and new handover docs (do not move)
```

If the application is large and a monorepo merge is not desired yet, it is acceptable to keep `codex/aiipd-application` and `codex/hearts-coop-website` as **long-lived parallel branches** rather than merging into `claude/awesome-bardeen-dzqcI` immediately. Claude and other agents can check out those branches directly to read/modify application code without requiring a merge.

---

## 7. After pushing — notify

Once pushed, no reply is required in this format — Claude is monitoring the repository for new commits and will detect the new branches automatically. However, if convenient, a short note in the commit message or a comment referencing routing key `AIIPD-BRIDGE-CLAUDE-TO-CODEX-V1` will help confirm intent.

---

## 8. Safety checklist before pushing

- [ ] No `.env` / `.env.local` / secrets files included
- [ ] No `node_modules/` or build output included
- [ ] No real client/council document content included unless explicitly approved
- [ ] `.env.example` created/updated with variable names only
- [ ] Hearts logo added to assets (currently untracked locally per brief)
- [ ] Branch names match Section 3.1
- [ ] Commit messages reference routing key `AIIPD-BRIDGE-CLAUDE-TO-CODEX-V1`
