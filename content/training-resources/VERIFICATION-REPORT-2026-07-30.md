# Training Package Currency Verification Report

**Date:** 30 July 2026
**Conducted by:** Claude (Opus 5) — automated verification pass
**Scope:** Qualification code currency and packaging rules for all nine training packages in the library
**Status:** **Findings require Liam's review and confirmation before commercial release**

---

## Method and Its Limits

**Read this section before relying on anything below.**

### What was possible

`training.gov.au`, `myskills.gov.au`, the Queensland skills gateways and RTO websites were **all blocked by this session's egress policy** — every direct fetch returned HTTP 403 at the proxy CONNECT stage, including a control fetch to `example.com`. The agent proxy README is explicit that a 403 is an organisation egress policy denial and must be reported rather than routed around.

**Web search was available and was used.** The findings below are drawn from search result summaries citing training.gov.au and RTO sources.

### What this means for confidence

| Finding type | Confidence | Reason |
|---|---|---|
| **Qualification code exists / is current / is superseded** | **Reasonably high** | Consistently reported across multiple independent sources |
| **Total unit counts and core/elective split** | **Moderate** | Reported in search summaries citing training.gov.au packaging rules; not read from the source document |
| **Which specific units are core** | **NOT VERIFIED** | Cannot be established from search summaries. **No core unit list in this library has been confirmed unit-by-unit** |
| **Individual unit code currency** | **NOT VERIFIED** | Not attempted — requires direct register access |

**This report resolves the qualification-level `[VERIFY]` flags. It does not resolve the unit-level ones.**

**A human must confirm every finding against training.gov.au directly before release.** This is a triage document identifying where the problems are, not a substitute for the register.

---

## Summary

| Qualification | Code status | Packaging status | Action |
|---|---|---|---|
| CHC33021 Individual Support | ✅ Current | Not verified | Confirm core list |
| BSB30120 Business | ✅ Current | ✅ **Matches** (6 core + 7 elective = 13) | Confirm core list |
| CPP41419 Real Estate Practice | ✅ Current (R3) | Not verified | Confirm core list |
| CPC30220 Carpentry | ✅ Current (R5, Dec 2024) | Not verified | Confirm core list |
| SIT30821 Commercial Cookery | ✅ Current (Jun 2022) | Not verified | Confirm core list |
| AUR30620 Light Vehicle | ⚠️ Current — **new release 17 Mar 2026** | Not verified | **Check what changed in R2026** |
| **RII30820 "Civil Construction"** | ❌ **WRONG CODE AND TITLE** | ❌ **Wrong** | **Re-badge — see Finding 1** |
| **CUA31120 Screen and Media** | ❌ **CODE DOES NOT APPEAR TO EXIST** | — | **Re-badged to CUA31020 — see Finding 2** |
| ICT30120 Information Technology | ✅ Current (R Feb 2022) | ❌ **Wrong** | **Correct — see Finding 3** |

**Six of nine qualification codes confirmed current. Three material errors found.**

---

## Finding 1 — RII30820 is the wrong qualification (HIGH SEVERITY)

**Affects: 13 documents — the entire RII pack**

### What the library says

The pack is titled **"RII30820 — Certificate III in Civil Construction"** with packaging stated as **12 core + 8 elective = 20 units**.

### What the register says

**RII30820 is "Certificate III in Civil Construction *Plant Operations*"** — a plant operator qualification for people operating excavators, rollers, graders and dozers. It supersedes RII30815 (equivalent).

**The general qualification is a different code: RII30920 — "Certificate III in Civil Construction"**, with packaging of **25 units: 8 core + 17 elective**, structured across **9 specialisations (8 specialist + 1 general)**, of which one specialisation's requirements must be met for the qualification to be awarded.

### Why this happened

The two codes are adjacent and similarly named. The content that was written — measurements and calculations, materials testing, pipe laying, quality standards, traffic management, confined spaces, civil works — is **general civil construction content**, not plant operations content. A plant operations qualification would be built around RIIMPO plant operation units.

### Assessment of the damage

**The unit guide content is likely sound.** The units written about (RIIWHS201E, RIIWHS202E, RIIWHS302D, RIIRIS301E, RIICOM201D, RIICCM201D, RIICMT201D, RIICWD201D, RIICWD301E, RIICWD302E, RIICWM201D) are real RII units, and the technical content on confined space entry, materials testing, traffic management and measurement is not affected by which qualification packages them.

**What is wrong is the framing:** the qualification code, the title, the packaging rules, the absence of the specialisation structure, and the claim that all 11 units are core.

**RII30920 has only 8 core units. The library contains 11 RII unit guides. Several are therefore electives, not core** — and which ones is unverified.

### Recommended action

1. **Re-badge the pack to RII30920** and correct the title to "Certificate III in Civil Construction"
2. **Correct the packaging rules** to 25 units, 8 core + 17 elective
3. **Add the specialisation structure** to the overview — 9 specialisations, one must be met
4. **Remove the claim that the 11 units are all core.** State that core/elective status requires confirmation and that the guides are valid as unit guides regardless
5. **Do not claim "core complete" for this package** until the 8 core units are confirmed and covered
6. Consider whether a separate RII30820 Plant Operations pack is a distinct product opportunity — it would need RIIMPO plant operation units, which have not been written

---

## Finding 2 — CUA31120 does not appear to exist (HIGH SEVERITY)

**Affects: 6 documents — the entire CUA pack**

### What the library says

The pack was titled **"CUA31120 — Certificate III in Screen and Media"** with packaging of 6 core + 10 elective.

### What the register says

**Every search result returns CUA31020 — Certificate III in Screen and Media**, which supersedes CUA31015 (equivalent). **No result exists for CUA31120.**

The overview already carried a `[VERIFY]` noting that some providers may use an older code. That flag was correct in identifying uncertainty and wrong in its direction — the code in use is CUA31020, and CUA31120 appears to have been an error rather than a newer release.

### Recommended action

1. ✅ **DONE — pack re-badged to CUA31020** throughout, directory and filenames included (6 documents)
2. ⬜ **Confirm the core unit list for CUA31020.** The six units written (CUADIG303, CUAIND311, CUAIND312, CUAPPR311, CUASOU313, plus the BSBCRT311 cross-reference) were drawn from an assumed CUA31120 list and **require confirmation against the actual CUA31020 core units**
3. ⬜ **Confirm the packaging rules** — total units and core/elective split
4. ✅ **DONE — "core complete" claim removed** from the master index pending confirmation

---

## Finding 3 — ICT30120 packaging rules are wrong (MODERATE SEVERITY)

**Affects: 1 document (the overview), plus the master index**

### What the library says

**"6 core + 12 elective"** — implying 18 units total.

### What the register says

**12 units total: 6 core + 6 elective.**

### Assessment

**The qualification code is correct and current** (released 21 Jul 2020, current release 3 Feb 2022, supersedes ICT30118 non-equivalent).

**The core unit content is unaffected** — the six core units written about remain six core units. Only the elective count and the total are wrong.

This is the least damaging of the three findings and the easiest to fix.

### Recommended action

Correct the overview and the master index to 12 units, 6 core + 6 elective.

---

## Finding 4 — AUR30620 has a release dated after the knowledge cutoff (FLAG, NOT AN ERROR)

**Affects: 6 documents — potentially**

AUR30620 is **current**, but the release date reported is **17 March 2026** — after the assistant's May 2026 training data would reliably reflect and, more importantly, after the content in this library was drafted from general knowledge.

**This does not mean the content is wrong.** It means the packaging rules, core unit list, and individual unit codes may have changed in that release and **the library has no way of knowing what changed**.

### Recommended action

**Treat AUR30620 as the highest-priority detailed check** after the two re-badging exercises. Specifically compare the library's stated 20 core units against the current release, and check whether any AUR unit codes were superseded.

---

## What Was Confirmed Correct

Worth stating explicitly, because six of nine codes are fine:

- **CHC33021** — current, supersedes CHC33015 (non-equivalent, Nov 2022)
- **BSB30120** — current, and **the packaging rules match the library exactly**: 6 core + 7 elective = 13 units, with BSBCRT311, BSBPEF201 and BSBSUS211 confirmed among the core units. One RTO page described it as "superseded"; no evidence of a successor code was found and the qualification is actively offered for 2026, so this is assessed as imprecise marketing copy
- **CPP41419** — current, Release 3 (19 May 2021), supersedes four earlier Property Services qualifications non-equivalently
- **CPC30220** — current, **Release 5 (24 Dec 2024)**, supersedes CPC30211 (equivalent). Note: training in CPC30211 could not continue past 31 Jan 2024
- **SIT30821** — current (10 Jun 2022), supersedes SIT30816 (equivalent)
- **ICT30120** — code current; packaging wrong (Finding 3)

**Note on CPC30220:** Release 5 dated December 2024 is recent enough that the core unit list should be checked against it specifically, rather than assumed from an earlier release.

---

## Residual Verification Still Required

**None of the following has been verified and all of it must be before release.**

### Per qualification
- [ ] Core unit list, unit by unit, against the current release
- [ ] Total unit count and core/elective split
- [ ] Specialisation or stream structure where one exists
- [ ] Release version and date of the packaging rules used
- [ ] Whether any individual unit code within the qualification is superseded

### Highest priority order
1. **RII** — re-badge to RII30920 and establish the 8 core units
2. **CUA** — re-badge to CUA31020 and establish the core units
3. **AUR30620** — establish what changed in the March 2026 release
4. **CPC30220** — check against Release 5 specifically
5. **ICT30120** — correct packaging (mechanical)
6. CHC33021, SIT30821, CPP41419 — confirm core lists
7. BSB30120 — lowest risk; packaging already matches

### Non-training-package verification still outstanding

The library also contains `[VERIFY]` flags on material that is **not** resolved by this report:

- State-specific licensing — real estate licensing tiers, builder registration thresholds, food safety supervisor requirements, High Risk Work Licence classes and thresholds
- Statutory timeframes — tenancy notice periods, bond lodgement windows, cooling-off periods, NDB assessment windows
- Exposure standards and thresholds — respirable crystalline silica, oxygen entry limits, LEL thresholds, excavation depth triggers, fall height triggers, EWP wind ratings
- Technical standards — ASCIA anaphylaxis action plans, IDDSI framework levels, ACSC Essential Eight maturity model, declarable allergen list, AS/NZS fall arrest ratings, AS 1742.3 traffic control, service marking colour codes
- Rates and entitlements — superannuation guarantee, award rates, screen production offsets

---

## What This Report Demonstrates

Three material errors existed in a library of 245,000 words, and **two of them would have been visible on the first page a paying customer read** — a qualification code that does not exist, and a pack named for the wrong qualification.

The errors were found in approximately fifteen minutes of searching, before a further 36 unit guides were written on the same foundations.

**Recommendation carried forward:** resolve the register-level verification before any further content is produced. Content built on an unverified code multiplies the correction cost with every document.

---

*This report is a draft finding requiring Liam Michael Clancy's review. No finding in it should be treated as authoritative until confirmed against training.gov.au directly.*

*© Liam Michael Clancy / Philosophersknow 2026*

---

## Addendum — 30 July 2026

**Liam has advised he will download the current training packages and validate the core unit lists manually.**

That resolves the principal outstanding item. The residual verification listed above should be worked against the downloaded packaging rules rather than against search results, and this report's method limits then no longer constrain the outcome.

**Two items to carry into that manual validation:**

1. **RII30920 vs RII30820.** Confirm which qualification the pack should target. The content written is general civil construction. If the intended market is plant operators, the pack needs RIIMPO units instead and is a different product.
2. **AUR30620 Release 17 March 2026.** Compare the library's stated core units against that release specifically — it postdates the drafting.

