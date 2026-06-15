# AGENTS.md

**Status:** DRAFT — proposed for Liam's review and approval
**Version:** 0.1
**Date:** 15 June 2026
**Purpose:** Define how AI agents (Claude, Codex, and others) and human team members collaborate on the AIIPD / Hearts Co-op repository.

This file is the entry point for any agent or contributor working in `philosophersknow/philosophersknow`. Read this before making changes.

---

## 1. Repository Purpose

This repository is the shared online workspace for the AIIPD Civic Intelligence platform and the Hearts Co-op platforms. It currently contains:

```text
content/    Civic Intelligence content architecture (website, dashboard,
            reports, marketing, onboarding, AI prompts, product, style guide)
docs/       Developer handover pack and project documentation
```

Application codebases (AiIPD Next.js/Prisma app, Hearts Co-op site) are not yet present here. See `docs/handover/2026-06-11/00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md` for the plan to add them.

**Final decision-maker:** Liam Michael Clancy. No agent should treat its own output as final or authoritative without Liam's review, particularly for:
- Overwriting or replacing existing specification documents
- Pushing to shared branches
- Any change affecting secrets, environment configuration, or production data

---

## 2. Agent Roles

### 2.1 Claude (this environment)

- **Scope:** Content strategy, intelligence framing, editorial work, report templates, AI prompts, onboarding content, style guide maintenance, specification review and drafting, documentation.
- **Does not have:** Access to local filesystems (G: drive, C: drive), the live AiIPD application, live databases, or Codex's environment.
- **Branch:** `claude/awesome-bardeen-dzqcI` (current working branch).
- **Constraints:**
  - Never overwrites an existing specification file in place. Updates are written as new versioned files (e.g. `_v0.2.md`) alongside a change summary, per the pattern established for the Master Technical Specification.
  - Marks any fact requiring live verification as `[VERIFY: ...]` with a note on what needs checking and by whom.
  - Does not invent application code, routes, schema, or runtime facts — these come from Codex or the live codebase.

### 2.2 Codex

- **Scope:** Technical implementation, build fixes, schema migrations, code generation, live codebase access, runtime verification, database queries, deployment.
- **Has access to:** Local development environment, G: drive, live AiIPD application, live database.
- **Branches (proposed):** `codex/aiipd-application`, `codex/hearts-coop-website`, `codex/update-master-specification` (see handover instructions, file `00`).
- **Constraints:**
  - Follows the safety checklist in `docs/handover/2026-06-11/00_CODEX_INSTRUCTIONS_publish_codebase_to_github.md` before any push (no secrets, no `node_modules`, no unapproved real data).
  - Resolves `[VERIFY]` items left by Claude by checking the live codebase/database and updating the relevant document.

**Current status (15 June 2026):** Codex is unavailable until approximately 19 June 2026 due to usage limits. Work that depends on live codebase/database access is blocked until then. Agents and team members should prioritise content, documentation, and planning work that does not require live verification (see Section 5).

### 2.3 Other AI agents / future contributors

- Any new agent joining this project should:
  1. Read this file first.
  2. Read `docs/handover/2026-06-11/README.md` for the current handover pack and reading order.
  3. Read the Master Technical Specification (`content/governance/master-technical-specification/AIIPD_MASTER_TECHNICAL_SPECIFICATION_v0.2.md` — the current draft) and its change summary.
  4. Read `content/governance/style-guide.md` before writing any user-facing content.
  5. Identify their own scope (content, code, design, etc.) and work within branch conventions in Section 3.

### 2.4 Human team members

- Same reading order as Section 2.3.
- Human review and approval is required before any `[VERIFY]` item is marked resolved in a way that changes a published specification's conclusions.
- Liam approves all branch merges into `claude/awesome-bardeen-dzqcI` or any future `main` branch.

---

## 3. Branch Conventions

| Branch pattern | Owner | Purpose |
|---|---|---|
| `claude/*` | Claude | Content architecture, specifications, documentation |
| `codex/*` | Codex | Application code, schema, infrastructure |
| `feature/*` | Human team members | Feature-specific work, proposed for new contributors |

Avoid pushing directly to another agent's branch. If cross-branch changes are needed, open the change as a new commit on your own branch and note the dependency in the commit message, referencing the routing key (Section 4).

**Folder ownership** (to avoid collisions — see handover instructions file `00`, Section 6):

```text
content/          Claude — Civic Intelligence content architecture
docs/             Shared — handover packs, project documentation
app/aiipd/        Codex — AiIPD application code (once pushed)
app/hearts-coop/  Codex — Hearts Co-op website code (once pushed)
```

---

## 4. Handoff Protocol

Use the routing key **`AIIPD-BRIDGE-CLAUDE-TO-CODEX-V1`** in commit messages or comments when a change is intended as a handoff between Claude and Codex (or vice versa). This makes intent traceable without requiring real-time coordination between agents that may run in different sessions, environments, or token-availability windows.

When leaving work for another agent:
- State clearly what is done, what is pending, and what `[VERIFY]` items remain.
- Do not assume the next agent has read the full conversation history — write enough context into the document or commit message to stand alone.

---

## 5. Status Legend

Used consistently across all specification and handover documents:

| Status | Meaning |
|---|---|
| **Confirmed working** | Verified against the live system as of the document date |
| **Built but unverified** | Code/content exists but has not been tested against the live system |
| **Configured** | Infrastructure or settings are in place but not yet exercised end-to-end |
| **Blocked** | Cannot proceed without a dependency (e.g. Codex access, a decision, a credential) |
| **Proposed** | Future specification, not yet built |

---

## 6. Working While Codex Is Unavailable

Until Codex resumes (~19 June 2026), prioritise:

- Content and editorial work in `content/`
- Specification refinement and `[VERIFY]` annotation in `docs/`
- Planning documents (roadmaps, task breakdowns, acceptance criteria)
- DOCX/branded output generation from existing Markdown sources, where assets are available
- Anything that does not require reading or modifying the live AiIPD/Hearts codebase or database

Do not fabricate runtime facts, database figures, or live test results to fill `[VERIFY]` gaps. Leave them marked and move on.

---

## 7. Non-Negotiable Safeguards (carried from Master Specification Section 23)

- AI does not make final civic, ethical, regulatory, political or compliance judgements.
- Candidate Intelligence must not become voter manipulation infrastructure.
- DRMC/RSC outputs must remain interpretive and caveated.
- Uploaded client documents must only be used for authorised analysis and output generation.
- Public examples must be labelled if simulated.
- No fake precision. No claims of validated measurement unless validation evidence exists.
- Human review remains mandatory for formal use.
- No secrets, credentials, or real personal/council data committed to this repository without explicit approval.
