# CPCCCA3002 — Set Out and Frame a Roof
## Complete Student Assessment Guide

**Unit Code:** CPCCCA3002
**Unit Title:** Set out and frame a roof
**Training Package:** CPC Construction, Plumbing and Services
**Qualification:** CPC30220 Certificate III in Carpentry (CORE unit)
**AIIPD Resource Pack — Student Edition**

---

## What This Unit Is About

Roof framing is the most geometrically demanding work a carpenter does. Wall framing is largely a matter of squares and rectangles. A roof requires you to work in three dimensions, calculate angles that are not visible on any drawing, and produce cuts that must fit precisely at heights where correction is difficult and dangerous.

CPCCCA3002 asks you to set out, calculate, cut, and erect a roof frame to AS 1684 requirements.

**This unit carries the highest fall risk in the qualification.** It should be read alongside CPCCCM2012 (Work safely at heights).

---

## Roof Types

| Type | Description |
|---|---|
| **Skillion** | Single sloping plane; simplest roof form |
| **Gable** | Two planes meeting at a ridge; triangular gable ends |
| **Hip** | Slopes on all four sides; no gable ends; hip rafters run to the corners |
| **Dutch gable** | Hip roof with a small gable at the ridge |
| **Gambrel / barn** | Two pitches per side |
| **Mansard** | Two pitches per side on all four sides |
| **Valley** | Formed where two roof planes meet in an internal corner |

Most Australian residential roofs are gable, hip, or a combination of the two with valleys where sections intersect.

---

## Roof Framing Terminology

### Members

| Term | Definition |
|---|---|
| **Ridge / ridge board** | Horizontal member at the apex where opposing rafters meet |
| **Common rafter** | Runs from wall plate to ridge at right angles to both |
| **Hip rafter** | Runs from the corner of the wall plate to the ridge at 45° in plan |
| **Valley rafter** | Runs from an internal corner up to the ridge; the reverse of a hip |
| **Creeper / jack rafter** | Shortened rafter running from the wall plate to a hip, or from a valley to the ridge |
| **Crown end rafter** | The common rafter at the end of the ridge on a hip roof |
| **Underpurlin** | Member running beneath the rafters to reduce their span |
| **Strut** | Member transferring load from an underpurlin down to a loadbearing wall |
| **Collar tie** | Horizontal member connecting opposing rafters, resisting spreading |
| **Ceiling joist** | Horizontal member carrying the ceiling; also ties the wall plates against spread |
| **Hanging beam** | Beam supporting ceiling joists over a span |
| **Strutting beam** | Beam carrying struts where there is no loadbearing wall below |
| **Fascia** | Board fixed to the rafter ends |
| **Barge board** | Board at the gable end, following the roof slope |
| **Batten** | Member fixed across rafters to carry roof covering |
| **Truss** | Prefabricated engineered frame replacing site-cut rafters and ties |

### Dimensional Terms — Critical for Calculation

| Term | Definition |
|---|---|
| **Span** | The full horizontal distance across the building, wall plate to wall plate |
| **Half span** | Half the span — the horizontal distance from the wall plate to the centreline |
| **Run** | The horizontal distance covered by a rafter. For a common rafter this equals the half span (less half the ridge thickness) |
| **Rise** | The vertical height gained from the wall plate to the underside of the ridge |
| **Pitch** | The angle of the roof, expressed in degrees |
| **Plumb cut** | The vertical cut at the top of a rafter where it meets the ridge |
| **Level / seat cut** | The horizontal cut where the rafter sits on the wall plate |
| **Birdsmouth** | The notch cut into the rafter combining plumb and seat cuts, seating it over the wall plate |
| **Overhang / eave** | The rafter length projecting beyond the wall plate |
| **True length** | The actual sloping length of the rafter |

---

## Roof Geometry — The Calculations

This is the technical core of the unit. Every calculation derives from a right-angled triangle in which the **run** is the base, the **rise** is the height, and the **rafter true length** is the hypotenuse.

### Pitch and Rise

**Rise = Run × tan(pitch)**

Example: a roof with a run of 4000mm at 25° pitch:
Rise = 4000 × tan(25°) = 4000 × 0.4663 = **1865mm**

### True Length of a Common Rafter

Two equivalent methods:

**Method 1 — Pythagoras:**
True length = √(run² + rise²)
= √(4000² + 1865²) = √(16,000,000 + 3,478,225) = √19,478,225 = **4413mm**

**Method 2 — Trigonometry:**
True length = Run ÷ cos(pitch)
= 4000 ÷ cos(25°) = 4000 ÷ 0.9063 = **4413mm**

Both give the same answer. Method 2 is quicker if you have the pitch; Method 1 is useful if you have measured the rise directly.

### The Multiplier Method

Traditional roofing practice uses **rafter length per metre of run**:

Multiplier = 1 ÷ cos(pitch)

At 25°: 1 ÷ 0.9063 = **1.1034** metres of rafter per metre of run.

True length = 4.000 × 1.1034 = **4.413m**

This is how rafter tables in carpentry references are constructed, and it is fast for repeated calculations at the same pitch.

### Common Pitch Multipliers

| Pitch | Rise per m of run | Rafter length per m of run |
|---|---|---|
| 15° | 0.268 | 1.035 |
| 20° | 0.364 | 1.064 |
| 22.5° | 0.414 | 1.082 |
| 25° | 0.466 | 1.103 |
| 30° | 0.577 | 1.155 |
| 35° | 0.700 | 1.221 |
| 45° | 1.000 | 1.414 |

### Allowing for the Ridge

The run for a common rafter is the **half span minus half the ridge thickness**. A rafter cut to the full half span will push the ridge out of position and the roof will be too wide.

Example: span 8000mm, ridge 35mm thick.
Half span = 4000mm. Half ridge = 17.5mm.
**Effective run = 4000 − 17.5 = 3982.5mm**

### Hip and Valley Rafters — The 45° Problem

A hip rafter runs diagonally in plan at 45° to the common rafters. Its **plan run is longer** than the common rafter's run by a factor of √2.

**Hip run = Common run × 1.414**

The hip rises the same vertical distance as the common rafter over that longer plan run, so **a hip rafter is at a shallower pitch than the common rafters**, and its true length is calculated on its own longer run.

**Hip true length = √(hip run² + rise²)**

Using the earlier example — run 4000mm, rise 1865mm:
Hip run = 4000 × 1.414 = 5656mm
Hip true length = √(5656² + 1865²) = √(31,990,336 + 3,478,225) = √35,468,561 = **5956mm**

**Hip multiplier method:** hip length per metre of *common* run at 25° pitch ≈ **1.4862**

**[VERIFY: Hip and valley multiplier tables against AS 1684 or a current carpentry reference. Values vary slightly with rounding convention.]**

### Creeper (Jack) Rafters

Creepers run from the wall plate to the hip. Because they are evenly spaced, their lengths **decrease by a constant amount** — the *common difference*.

**Common difference = rafter length per metre of run × spacing**

At 25° pitch with rafters at 600mm centres:
Common difference = 1.1034 × 0.600 = **0.662m (662mm)**

So each successive creeper is 662mm shorter than the last. This makes setting out a full hip end fast once the first creeper is established.

### Bevels

Roof cutting requires several bevels that cannot simply be read from the pitch:

| Bevel | Applied to |
|---|---|
| **Plumb bevel (common)** | Top cut of common rafter at ridge |
| **Level bevel (common)** | Seat cut on wall plate |
| **Plumb bevel (hip/valley)** | Top cut of hip or valley rafter — different from common, because the hip is at a shallower pitch |
| **Level bevel (hip/valley)** | Seat cut of hip or valley |
| **Edge bevel (creeper)** | The angled cut on the face of the creeper where it meets the hip |
| **Edge bevel (purlin)** | Where underpurlins meet a hip |
| **Face bevel** | Various compound cuts |

**Traditionally these are obtained from a steel square or a set-out rod. In modern practice they are read from AS 1684 bevel tables, a roofing calculator, or a construction calculator.**

**The critical error to avoid:** using the common rafter plumb bevel on a hip rafter. The hip is at a shallower pitch and requires its own bevel. This is the single most common roof cutting mistake.

---

## Trussed Roofs

Most Australian residential roofs are now **prefabricated trusses** rather than site-cut ("stick-built") roofs. Truss roofs are faster, use less material, and shift the engineering to the manufacturer.

### Working With Trusses

**Handling and storage:**
- Store flat and supported, or vertically braced — trusses are strong in their design plane and weak laterally
- Lift at the designated points; never lift a truss by one end or by the apex alone
- Do not modify a truss in any way — **cutting, notching, or drilling a truss member voids the engineering certification**. If a service needs to pass through, that must be designed for

**Erection:**
- Trusses must be erected at the spacing specified in the truss design (commonly 600mm or 900mm centres)
- **Temporary bracing is critical.** Trusses are unstable until permanently braced; a partially erected truss roof can collapse progressively like dominoes. Temporary bracing must be installed as erection proceeds, not afterwards
- Permanent bracing per the truss layout drawing — typically longitudinal ties, diagonal bracing, and web bracing
- Fixing to the wall plate per the specified tie-down

**AS 4440** covers the installation of nailplated timber roof trusses.

**The truss layout drawing is the authority.** It specifies truss positions, girder trusses, bracing, and tie-down. Follow it exactly.

---

## Bracing and Tie-Down

### Why Roofs Need Both

A roof must resist:
- **Downward loads** — roof covering, ceiling, water, wind pressure, maintenance access
- **Uplift** — wind flowing over a roof creates suction; in high wind this can exceed the roof's weight and lift it off
- **Racking** — lateral wind force trying to push the roof structure sideways

**Tie-down** resists uplift. **Bracing** resists racking.

### Tie-Down

A continuous load path must connect the roof to the foundations. Every connection in the chain matters:

Rafter/truss → wall plate → studs → bottom plate → floor frame or slab

Tie-down is achieved with framing anchors, straps, rods, or proprietary connectors, at spacings determined by the **wind classification**.

### Wind Classification

Australian sites are classified N1–N6 (non-cyclonic) and C1–C4 (cyclonic) under **AS 4055**. The classification is determined by region, terrain category, shielding, and topography.

**Higher wind classification means more tie-down, more bracing, and stronger fixings.** A roof framed to N1 requirements in an N3 location is a structural failure waiting for the right storm.

The wind classification will be stated on the plans or in the engineering documentation. **If it is not stated, ask — do not assume.**

**[VERIFY: Wind classification requirements and tie-down details against AS 1684, AS 4055, and the project engineering documentation.]**

---

## Setting Out a Roof — The Sequence

1. **Check the wall frames.** Confirm the walls are square (equal diagonals), plumb, level, and to the correct dimensions. **A roof cannot correct an out-of-square wall frame** — the errors will compound
2. **Establish the ridge position and height.** Mark the centreline on the wall plates at each end
3. **Set out rafter positions** on both wall plates, working from a single datum at each end to avoid cumulative error. Ensure rafters align with ceiling joists where they must
4. **Calculate rafter lengths and bevels** for commons, hips, valleys, and creepers
5. **Cut and check a pattern rafter.** Cut one common rafter, offer it up, and confirm it fits before cutting the rest. **Cutting the full set before checking the pattern is the most expensive mistake in roof framing**
6. **Mark and cut the remaining rafters** from the pattern
7. **Erect the ridge and first pair of common rafters**, temporarily braced
8. **Install remaining commons**, then hips and valleys, then creepers
9. **Install underpurlins and struts** as specified
10. **Check the roof** — ridge straight and level, rafters in plane, no twist, correct overhang
11. **Install permanent bracing and tie-down**
12. **Fix fascia and battens**

---

## Common Errors

**1. Using the common bevel on a hip.** The hip is at a shallower pitch and needs its own bevel set.

**2. Forgetting to deduct half the ridge thickness.** Produces a roof marginally too wide and a ridge pushed out of line.

**3. Cutting all rafters before checking a pattern.** One error multiplied across forty rafters.

**4. Cumulative set-out error.** Measuring each rafter position from the previous one rather than from a single datum.

**5. Inconsistent crowning.** Rafters must be installed crown up, consistently, or the roof plane will be wavy.

**6. Inadequate temporary bracing during erection.** A leading cause of roof collapse and of serious injury during construction.

**7. Modifying a truss.** Cutting or notching a truss member voids its engineering certification and can cause failure.

**8. Ignoring wind classification.** Fixing to a lower classification than the site requires.

**9. Working the roof without fall protection.** See CPCCCM2012 — roof work requires fall protection at any height.

---

## Evidence Checklist — CPCCCA3002

**Knowledge Evidence**
- [ ] Identification of at least 5 roof types
- [ ] Definition of at least 15 roof framing members
- [ ] Definition of span, half span, run, rise, pitch, true length, plumb cut, seat cut, birdsmouth
- [ ] Calculation of rise from run and pitch
- [ ] Calculation of common rafter true length by both Pythagoras and trigonometry
- [ ] Explanation of the multiplier method and its use
- [ ] Explanation of why half the ridge thickness must be deducted from the run
- [ ] Explanation of why hip run is 1.414 × common run, and why a hip is at a shallower pitch
- [ ] Calculation of hip rafter true length
- [ ] Explanation and calculation of the creeper common difference
- [ ] Identification of at least 5 bevels required in roof cutting and why hip bevels differ from common bevels
- [ ] Explanation of truss handling, the prohibition on modification, and temporary bracing requirements
- [ ] Explanation of the difference between tie-down and bracing and what each resists
- [ ] Explanation of wind classification and its effect on tie-down and bracing requirements
- [ ] Description of the roof setting out sequence
- [ ] Identification of at least 6 common roof framing errors

**Performance Evidence**
- [ ] Calculate rafter lengths and bevels for a specified gable roof from a provided plan
- [ ] Calculate hip rafter length and creeper common difference for a specified hip roof
- [ ] Set out and cut a common rafter including birdsmouth and overhang, verified against a pattern
- [ ] Set out and cut a hip rafter with correct bevels
- [ ] Erect a section of roof frame with correct temporary bracing
- [ ] Verify a completed roof frame for ridge line, plane, and overhang
- [ ] Identify tie-down and bracing requirements for a specified wind classification from AS 1684

---

## Worked Example

**Prompt:**

*A hip roof is to be framed on a building with a span of 9600mm. The pitch is 22.5°. The ridge is 35mm thick. Rafters are at 600mm centres. Eaves overhang is 600mm horizontally.*

*Calculate: (a) the rise, (b) the common rafter run allowing for the ridge, (c) the common rafter true length including the overhang, (d) the hip rafter run and true length, and (e) the creeper common difference.*

---

**Exemplary Response:**

I would work from the plan geometry outward, and I would keep the overhang separate from the main body length until the end so the ridge deduction is not applied to the wrong figure.

---

**(a) Rise**

The rise is calculated on the **half span**, before the ridge deduction — the ridge deduction affects the rafter's horizontal run, not the height of the ridge above the wall plate.

Half span = 9600 ÷ 2 = 4800mm

Rise = half span × tan(22.5°)
= 4800 × 0.41421
= **1988mm**

---

**(b) Common rafter run (allowing for ridge)**

Half the ridge thickness = 35 ÷ 2 = 17.5mm

Effective run = half span − half ridge
= 4800 − 17.5
= **4782.5mm**

This deduction matters: cutting to the full 4800mm would push the ridge 17.5mm off centre at each end, making the roof 35mm too wide overall and throwing the hips out.

---

**(c) Common rafter true length (including overhang)**

At 22.5°, the rafter length per metre of run is:

Multiplier = 1 ÷ cos(22.5°) = 1 ÷ 0.92388 = **1.08239**

**Body of the rafter** (wall plate to ridge):
4782.5 × 1.08239 = **5176mm**

*Cross-check by Pythagoras:* √(4782.5² + 1988²) = √(22,872,306 + 3,952,144) = √26,824,450 = 5179mm

The 3mm difference is rounding in the rise figure — consistent, and within tolerance. I would use the trigonometric result and cut to a checked pattern rather than relying on the arithmetic alone.

**Overhang** (horizontal 600mm):
600 × 1.08239 = **649mm** of sloping length

**Total true length** = 5176 + 649 = **5825mm**

I would add a cutting allowance and trim the eave end after fitting.

---

**(d) Hip rafter run and true length**

The hip runs at 45° in plan across the corner, so its plan run is the common run × √2.

**Hip run** = 4782.5 × 1.41421 = **6763mm**

The hip rises the **same 1988mm** as the common rafter, but over that longer run — which is why the hip sits at a shallower pitch than the commons.

**Hip true length** = √(hip run² + rise²)
= √(6763² + 1988²)
= √(45,738,169 + 3,952,144)
= √49,690,313
= **7049mm**

*Hip pitch check:* tan⁻¹(1988 ÷ 6763) = tan⁻¹(0.2939) = **16.4°** — confirming the hip is considerably shallower than the 22.5° commons. **This is why the hip requires its own plumb and level bevels.** Using the common bevels on the hip is the classic roof-cutting error.

**Hip overhang:** the hip also runs diagonally at the corner, so its overhang is the diagonal of the 600mm eave:
600 × 1.41421 = 849mm plan, × hip multiplier.

Hip multiplier = 1 ÷ cos(16.4°) = 1 ÷ 0.95924 = 1.04249
Hip overhang sloping length = 849 × 1.04249 = **885mm**

**Total hip length** = 7049 + 885 = **7934mm**

---

**(e) Creeper common difference**

Creepers are at 600mm centres, and each successive creeper is shorter by a constant amount along the hip.

Common difference = spacing × rafter length per metre of run
= 600 × 1.08239
= **649mm**

So the first creeper is 649mm shorter than a full common rafter body, the next 1298mm shorter, and so on.

**Practical check:** with a 4782.5mm run at 600mm centres, there will be approximately 4782.5 ÷ 600 ≈ 7 creepers per hip side before reaching the corner. Seven creepers × 649mm ≈ 4543mm of total reduction — which is consistent with the shortest creeper being close to the corner.

I would also need the **creeper edge bevel** where each creeper meets the face of the hip — this is a compound cut and is read from AS 1684 bevel tables or a roofing calculator, not derived from the pitch alone.

---

**Summary**

| Item | Result |
|---|---|
| Rise | 1988mm |
| Common run (ridge allowed) | 4782.5mm |
| Common rafter body | 5176mm |
| Common overhang (sloping) | 649mm |
| **Common total length** | **5825mm** |
| Hip run | 6763mm |
| Hip body | 7049mm |
| Hip overhang (sloping) | 885mm |
| **Hip total length** | **7934mm** |
| Hip pitch | 16.4° |
| Creeper common difference | 649mm |

**Before cutting anything**, I would cut one common rafter as a **pattern**, offer it up, and confirm the birdsmouth seats correctly, the plumb cut meets the ridge cleanly, and the overhang is right. Only then would I mark out the rest from the pattern. Cutting forty rafters from a calculation that has not been physically verified is how a full set of material gets scrapped.

**Examiner Annotation:** Outstanding. Every calculation is correct and — more importantly — the student explains the reasoning behind each step rather than simply applying formulae. The recognition that the rise is calculated on the half span *before* the ridge deduction, while the run uses it *after*, is a distinction that trips up many candidates. Keeping the overhang separate until the end avoids applying the ridge deduction to the wrong figure. The Pythagorean cross-check with an honest note about rounding shows genuine numerical judgement rather than false precision. The hip pitch calculation of 16.4° is the standout: the student not only computes it but explicitly connects it to *why* separate hip bevels are required, which is the single most common roof-cutting error in the trade. Calculating the hip overhang on the diagonal — rather than assuming it matches the common overhang — is a detail frequently missed. The practical sanity check on the number of creepers, and the closing insistence on cutting and verifying a pattern before committing the full set, demonstrate the working judgement that separates a competent roof carpenter from someone who can do trigonometry. Strong Competent.

---

*Next: CPCCCA3001 — Frame and fit door and window units*

*AIIPD RTO Training Resources | CPC30220 Certificate III in Carpentry | © Liam Michael Clancy / Philosophersknow 2026*
