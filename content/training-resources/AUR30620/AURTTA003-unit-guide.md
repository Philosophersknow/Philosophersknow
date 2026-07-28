# AURTTA003 — Diagnose and Repair Automotive Systems and Components
## Complete Student Assessment Guide

**Unit Code:** AURTTA003
**Unit Title:** Diagnose and repair automotive systems and components
**Training Package:** AUR Automotive Retail, Service and Repair
**Qualification:** AUR30620 Certificate III in Light Vehicle Mechanical Technology (CORE unit)
**AIIPD Resource Pack — Student Edition**

---

## What This Unit Is About

Diagnosis is what separates a mechanic from a parts fitter.

Anyone can replace a component. The skill — and the value — is in correctly identifying **which** component has failed, **why** it failed, and whether replacing it will actually resolve the customer's complaint. A technician who reads a fault code and replaces the part named in the code description will spend their career doing repeat repairs and arguing with customers.

AURTTA003 asks you to apply a systematic diagnostic process, use test equipment correctly, interpret results accurately, and verify that the repair worked.

---

## The Diagnostic Process

The single most important content in this unit. Every assessment answer should follow this structure.

### Step 1 — Verify the Complaint

**Before anything else, confirm the fault actually exists and understand exactly what it is.**

Customer descriptions are symptoms filtered through non-technical language. "It's making a noise" is a starting point, not a diagnosis.

**Questions that produce useful information:**

| Question | Why |
|---|---|
| When does it happen? | Cold start, after warm-up, at speed, braking, turning |
| How long has it been happening? | Sudden onset suggests failure; gradual suggests wear |
| Is it constant or intermittent? | Intermittent faults are harder and need different techniques |
| Does anything make it better or worse? | Speed, load, temperature, weather, road surface |
| What changed before it started? | Recent service, repair, accident, fuel fill, modification |
| Are there warning lights? | Which ones, and do they stay on or flash |

**Road test with the customer where possible.** "That noise" is identified in thirty seconds sitting beside them, and hours without them.

**If you cannot reproduce the fault, you cannot confirm you have fixed it.** Say so honestly rather than replacing parts speculatively.

### Step 2 — Preliminary Inspection

Before reaching for diagnostic equipment, look.

- Fluid levels and condition — oil, coolant, brake fluid, transmission, power steering
- Visible leaks, and where they originate (fluid tracks upward from where it drips)
- Belt condition and tension
- Battery terminals — corrosion, tightness
- Wiring — chafing, rodent damage, previous poor repairs
- Tyre condition and pressures
- Evidence of previous repair work
- Anything obviously out of place

**A significant proportion of faults are found here.** Skipping the visual inspection to go straight to a scan tool is a common and expensive habit.

### Step 3 — Research

- **Service history** — what has been done, and when
- **Technical Service Bulletins (TSBs)** — manufacturers publish known faults and their fixes. A TSB can save hours
- **Wiring diagrams** and system schematics
- **Manufacturer specifications** — resistance values, pressures, clearances, voltages
- **Known common faults** for that model — pattern knowledge is genuinely valuable

### Step 4 — Retrieve and Interpret Fault Codes

Scan the vehicle and record **all** codes across **all** modules, plus **freeze frame data**.

**Freeze frame** captures the operating conditions at the moment the code set — engine speed, load, coolant temperature, fuel trims, vehicle speed. This is frequently more useful than the code itself, because it tells you the conditions under which the fault occurs.

**The critical principle: a fault code identifies a circuit or a symptom, not a faulty part.**

**Example:** `P0135 — O2 Sensor Heater Circuit Malfunction (Bank 1 Sensor 1)`

This does **not** mean "replace the oxygen sensor." It means the ECU detected the heater circuit operating outside expected parameters. The cause could be:
- A failed sensor heater element
- A blown fuse
- A broken or corroded wire
- A poor earth
- A failed relay
- An ECU driver fault

**Replacing the sensor without testing the circuit is guessing.** If the fault is a corroded connector, the new sensor will set the same code and the customer will return.

### Step 5 — Test Systematically

Use the appropriate equipment to test the actual circuit or system. **Test, do not assume.**

Work through the possibilities logically — commonly split-half testing, where you test at the midpoint of a circuit to determine which half contains the fault, then repeat. This is far faster than testing every point in sequence.

### Step 6 — Determine Root Cause

**Ask why the component failed.** A failed part is often a symptom, not the cause.

| Symptom | Possible root cause |
|---|---|
| Repeated alternator failure | Poor earth strap, excessive load, failing battery |
| Repeated brake pad wear on one side | Seized caliper slide pins |
| Repeated wheel bearing failure | Incorrect fitting, damaged hub, or a bent stub axle |
| Overheating after radiator replacement | Failed thermostat or head gasket the radiator was masking |
| Battery repeatedly flat | Parasitic drain, not a bad battery |

**If you replace a part without addressing why it failed, it will fail again.** The customer will reasonably blame you.

### Step 7 — Repair

Carry out the repair to manufacturer specification — correct parts, correct torque, correct procedure.

### Step 8 — Verify

**Confirm the original complaint is resolved.**
- Clear codes and re-scan to confirm they do not return
- Road test under the conditions in which the fault occurred
- Confirm no new faults have been introduced
- Check that related systems still operate correctly

**A repair is not complete until it is verified under the conditions that produced the fault.** Clearing a code and handing back the keys is not verification.

### Step 9 — Document

Record the **complaint, cause, and correction** — the standard "three Cs" of automotive documentation.

> **Complaint:** Customer reports engine cranks but does not start when cold; starts normally when warm.
> **Cause:** Coolant temperature sensor reading open circuit when cold. Sensor tested at 4.1kΩ at 20°C; specification 2.2–2.8kΩ. Wiring and connector tested serviceable.
> **Correction:** Replaced engine coolant temperature sensor. Cleared codes. Cold-start verified next morning — started normally, no codes returned.

Good documentation protects you, informs the next technician, and justifies the invoice.

---

## Test Equipment

### Digital Multimeter (DMM)

The fundamental electrical diagnostic tool.

| Function | Measures | Connection |
|---|---|---|
| **Voltage (V)** | Electrical pressure | **Parallel** — across the component |
| **Current (A)** | Flow rate | **Series** — in line with the circuit |
| **Resistance (Ω)** | Opposition to flow | **Circuit de-energised** — power off |

**Ohm's Law: V = I × R**

Rearranged: I = V ÷ R, and R = V ÷ I

This underpins all electrical diagnosis. If voltage is correct and current is low, resistance is too high — typically corrosion or a poor connection.

**Voltage drop testing** is the most useful and most underused electrical test. Measure voltage across a section of an **energised, loaded** circuit. The reading is the voltage lost across that section.

- **Acceptable voltage drop** across a good connection or cable is typically very small — commonly under 0.2V, and under 0.1V across an earth
- A high voltage drop indicates resistance — corrosion, loose connection, damaged cable

**Voltage drop testing finds faults that a resistance test misses**, because a corroded connection can read acceptable resistance with no load but fail badly under current.

### Oscilloscope

Displays voltage over time as a waveform. Essential for:
- Sensor signal patterns — crank and cam position, ABS wheel speed
- Intermittent faults a multimeter's sampling rate would miss
- Ignition and injector waveforms
- Communication bus signals (CAN)

An oscilloscope shows **the shape and timing** of a signal, not just its value. A crank sensor producing a signal of correct voltage but with a missing tooth pattern will read fine on a multimeter and be obviously faulty on a scope.

### Scan Tool

- **Read and clear DTCs** across all modules
- **Live data** — real-time sensor and actuator values
- **Freeze frame**
- **Actuator/bidirectional tests** — commanding a component to operate, which distinguishes a failed component from a failed command signal
- **Readiness monitors** — whether emissions self-tests have completed

**Live data interpretation is a skill.** Values must be assessed against specification and against each other. A coolant temperature reading of 20°C is plausible — unless the engine has been running for twenty minutes, in which case it is clearly wrong.

### Other Equipment

| Tool | Use |
|---|---|
| **Compression tester** | Cylinder sealing — measures peak pressure |
| **Leak-down tester** | Where compression is lost — valves, rings, or head gasket |
| **Fuel pressure gauge** | Fuel delivery pressure and residual pressure hold |
| **Vacuum gauge** | Engine mechanical condition; manifold vacuum reveals a surprising amount |
| **Smoke machine** | Vacuum and evaporative system leaks |
| **Cooling system pressure tester** | Coolant leaks and cap performance |
| **Infrared thermometer** | Comparative temperature — catalytic converters, brake drag, blocked radiator sections |
| **Battery/charging tester** | Battery condition and charging system output |
| **Borescope** | Internal inspection without disassembly |

---

## Diagnosing by System

### Engine Mechanical

**Compression test** — all cylinders should be within specification and reasonably consistent with each other. **A common threshold is that the lowest cylinder should be within about 10–20% of the highest**, though the manufacturer's figure governs.

**Wet test:** add a small amount of oil to a low cylinder and retest. If compression rises significantly, the loss is past the **rings**. If it does not change, the loss is at the **valves** or the **head gasket**.

**Leak-down test** — pressurises the cylinder and identifies where air escapes:
- Air from the **exhaust** → exhaust valve
- Air from the **intake** → intake valve
- Air from the **oil filler or dipstick** → rings
- Bubbles in the **coolant** → head gasket
- Air into an **adjacent cylinder** → head gasket between cylinders

### Charging and Starting

**Battery:** test state of charge and capacity. A battery can hold surface voltage while being incapable of delivering cranking current.

**Charging:** alternator output should typically be around 13.8–14.5V at idle with load. Test for **AC ripple** — excessive AC indicates failed diodes.

**Starting:** a slow crank could be the battery, the starter, the cables, or engine mechanical drag. **Voltage drop testing across the starter circuit** identifies cable and connection faults quickly.

**Parasitic drain:** measure current draw with everything off after the modules have gone to sleep — which can take a considerable time on modern vehicles. Pull fuses one at a time to isolate the circuit.

### Fuel and Emissions

**Fuel trims** are among the most informative live data values available.

- **Short Term Fuel Trim (STFT)** — immediate correction
- **Long Term Fuel Trim (LTFT)** — learned correction over time

| Reading | Meaning | Likely causes |
|---|---|---|
| **Positive trim** (e.g. +20%) | ECU adding fuel — mixture is **lean** | Vacuum leak, low fuel pressure, dirty injectors, faulty MAF |
| **Negative trim** (e.g. −20%) | ECU removing fuel — mixture is **rich** | Leaking injector, high fuel pressure, faulty sensor |

**A key diagnostic distinction:** if the lean condition is worse at idle and improves at higher RPM, a **vacuum leak** is likely — because the fixed volume of unmetered air is proportionally large at idle and small at high airflow. If it is consistent across the range, suspect **fuel delivery** or the **MAF sensor**.

### Braking

- Pedal feel — spongy suggests air or a flexible hose; hard suggests a booster or vacuum fault
- Pulling to one side — seized caliper, contaminated pad, collapsed hose acting as a one-way valve
- Judder under braking — disc thickness variation or runout
- Uneven pad wear — seized slide pins
- **ABS faults** — wheel speed sensor signal is best assessed on an oscilloscope

### Steering and Suspension

- Assess with the weight on the wheels for some checks and off for others — bushes load differently
- Wander, pull, and uneven tyre wear indicate alignment or worn components
- Noise over bumps — links, bushes, mounts
- **Tyre wear patterns are diagnostic:** both edges worn indicates under-inflation; centre worn indicates over-inflation; one edge indicates camber; feathering indicates toe

---

## Intermittent Faults

The hardest category, and the one that generates the most repeat visits.

**Techniques:**
- **Freeze frame data** — the conditions when it last occurred
- **Wiggle test** — move harnesses and connectors while monitoring live data or a scope, to provoke the fault
- **Heat and cold** — a heat gun or freeze spray applied to a suspect component can reproduce a temperature-dependent fault
- **Data logging** — record a road test and review afterwards
- **Load testing** — some faults appear only under load

**Be honest with the customer about intermittent faults.** If you cannot reproduce it, say so and explain what you have checked, rather than replacing parts speculatively and charging for them.

---

## Safety in Diagnosis

Diagnostic work frequently requires the engine running, the vehicle raised, or systems energised. See AURAFA004.

- **Exhaust extraction connected** whenever an engine is running indoors — carbon monoxide is odourless and fatal
- **Rotating components** — fans (including electric fans that start without warning), belts, pulleys. Keep hands, tools, clothing, and hair clear
- **Hot components** — exhaust, cooling system under pressure
- **Vehicle support** — safety stands, never a jack alone
- **High voltage** — **do not work on HV systems without specific training and authorisation.** Orange cabling means stop
- **Airbag/SRS** — pyrotechnic; follow the manufacturer's disable procedure and waiting period
- **Fuel systems** — depressurise before disconnecting; no ignition sources

---

## Evidence Checklist — AURTTA003

**Knowledge Evidence**
- [ ] Description of the diagnostic process in correct sequence with at least 8 steps
- [ ] Identification of at least 6 questions to ask when verifying a customer complaint
- [ ] Explanation of why a fault code identifies a circuit, not a faulty part, with a worked example
- [ ] Explanation of freeze frame data and its diagnostic value
- [ ] Explanation of root cause analysis with at least 3 examples of a failed part being a symptom
- [ ] Explanation of Ohm's Law and its application
- [ ] Explanation of how to connect a multimeter for voltage, current, and resistance
- [ ] Explanation of voltage drop testing and why it finds faults a resistance test misses
- [ ] Explanation of when an oscilloscope is required rather than a multimeter
- [ ] Explanation of compression testing including the wet test and what it distinguishes
- [ ] Explanation of leak-down testing and interpreting where air escapes
- [ ] Explanation of positive and negative fuel trims and their likely causes
- [ ] Explanation of how to distinguish a vacuum leak from a fuel delivery fault using trim behaviour
- [ ] Identification of at least 4 tyre wear patterns and their causes
- [ ] Description of at least 4 techniques for diagnosing intermittent faults
- [ ] Explanation of the three Cs documentation standard

**Performance Evidence**
- [ ] Complete a full diagnostic process on a vehicle with a known fault, documented against the three Cs
- [ ] Perform and interpret a compression test including a wet test
- [ ] Perform voltage drop testing on a starting or charging circuit
- [ ] Retrieve, record, and interpret DTCs and freeze frame data, and explain why the code does not identify the faulty part
- [ ] Interpret live data against specification and identify an out-of-range value
- [ ] Diagnose a fault to root cause and explain why the component failed
- [ ] Verify a completed repair under the conditions that produced the fault

---

## Worked Example

**Prompt:**

*A customer brings in a 2016 petrol sedan. The complaint is: "The engine light came on and it feels a bit rough at idle, but it drives OK once you're moving. It's been getting slowly worse over about a month."*

*You scan the vehicle and retrieve a single code: **P0171 — System Too Lean (Bank 1)**.*

*Live data at idle shows: STFT +18%, LTFT +22%. At 2500 RPM: STFT +3%, LTFT +6%.*

*Describe your diagnostic approach.*

---

**Exemplary Response:**

The data here tells me a great deal before I pick up a single tool, and it points fairly clearly in one direction.

---

**What the codes and trims are telling me:**

**P0171** means the ECU has detected that Bank 1 is running lean — there is more air than the fuel calculation expects — and it has had to add fuel to compensate beyond its normal correction range.

The fuel trims confirm this and, more usefully, tell me **when** it happens:

| Condition | STFT | LTFT | Total correction |
|---|---|---|---|
| **Idle** | +18% | +22% | **+40%** |
| **2500 RPM** | +3% | +6% | **+9%** |

**This is the key observation: the lean condition is severe at idle and almost disappears at higher RPM.**

That pattern strongly indicates a **vacuum leak** — unmetered air entering downstream of the mass airflow sensor.

**Why the pattern points there:**

A vacuum leak admits a roughly **fixed volume** of unmetered air. At idle, total airflow through the engine is small, so that fixed leak represents a large proportion of the total — producing a big lean correction. At 2500 RPM, total airflow is much greater, so the same leak is proportionally small and the correction drops to near normal.

**If instead this were a fuel delivery problem** — weak pump, restricted filter, failing injectors — the lean condition would typically be **worse at high load and RPM**, when fuel demand is highest, not better. The trim pattern would be roughly the reverse of what I am seeing.

**If it were a MAF sensor under-reporting airflow**, I would generally expect the error to be more consistent across the range, or to worsen with airflow rather than improve.

The gradual onset over a month also fits a vacuum leak — a perishing hose or a hardening gasket degrades progressively, whereas an electrical fault more often appears suddenly.

**The customer's description matches too:** rough at idle, fine once moving. That is exactly what a vacuum leak feels like.

---

**My diagnostic sequence:**

**1. Verify the complaint.**

Start the vehicle, confirm the rough idle, and confirm it smooths at higher RPM. Listen — a significant vacuum leak is often audible as a hiss at idle.

**2. Visual and audible inspection.**

Before any equipment:
- Inspect all vacuum hoses for cracking, perishing, and disconnection — particularly at bends and at the ends where they harden
- Check the intake ducting between the MAF and the throttle body for splits, especially on the underside and in the concertina sections, which crack where they flex
- Check the PCV system and its hoses — a very common source
- Check the brake booster hose and the booster itself
- Check the intake manifold gasket area
- Check the dipstick is seated and the oil filler cap is on and sealing — both are genuine causes of unmetered air and both are free to fix

**3. Smoke test — the definitive test for this.**

Introduce smoke into the intake system and look for where it escapes. This is the fastest and most reliable way to locate a vacuum leak, and it finds leaks that are inaudible and invisible.

**4. Alternative field tests if no smoke machine is available:**
- **Propane or carburettor cleaner** sprayed carefully around suspect areas while monitoring RPM and STFT on a scan tool. If the idle rises or the trim drops sharply, the leak is at that point.
- **Caution:** this involves spraying a flammable substance near a running hot engine. It must be done carefully, with a fire extinguisher to hand, and never near ignition sources or hot exhaust components. A smoke machine is the safer method and I would prefer it.

**5. Verify the MAF as a secondary check.**

Even though the trim pattern points away from it, I would check MAF live data against specification for the engine — comparing actual grams per second at idle and at a known RPM against the expected value. A contaminated MAF is a cheap thing to rule out.

**6. Check fuel pressure** if the above finds nothing — to rule out delivery. But I would expect this to be normal given the trim pattern.

---

**Root cause — the step I would not skip:**

If I find a perished hose, I would ask **why** it perished. Age and heat are the usual answers and are acceptable. But if a hose is perished because it is contacting a hot exhaust component or rubbing on a bracket, the replacement will fail the same way. **I would reroute or protect it, not just replace it.**

Similarly, if I find an intake manifold gasket leak on a relatively young vehicle, I would check for a known TSB — manufacturers often issue updated parts for gaskets that fail prematurely.

---

**Repair and verification:**

- Repair or replace the leaking component to specification
- **Clear the codes and reset the fuel trims** — this matters. The LTFT of +22% is a learned value. If I do not reset it, the ECU will start from that learned correction and take time to re-adapt, and the engine may run rich initially
- Run to operating temperature and **re-check trims at idle**. I want to see them return to near zero — a few percent either way is normal
- Confirm the idle is smooth
- **Road test** and re-scan to confirm P0171 does not return
- Ideally check again after a heat cycle, since some leaks only appear when components are hot or cold

---

**Documentation — the three Cs:**

> **Complaint:** Customer reports MIL illuminated and rough idle, progressively worse over approximately one month. Drives normally above idle.
>
> **Cause:** DTC P0171 — System Too Lean Bank 1. Fuel trims at idle STFT +18% / LTFT +22%, reducing to +3% / +6% at 2500 RPM, indicating unmetered air. Smoke test identified [split in intake ducting / perished PCV hose / manifold gasket leak] admitting unmetered air downstream of MAF.
>
> **Correction:** Replaced [component]. Cleared DTCs and reset adaptive fuel trims. Idle trims verified at STFT +2% / LTFT +1% after warm-up. Idle smooth. Road tested — no codes returned, MIL off.

---

**What I would not do:**

Replace the oxygen sensor, the MAF, or the fuel pump because they are "commonly associated with P0171." Every one of those is a plausible-sounding guess that the trim data actively argues against. Fitting parts until the code clears is expensive for the customer, damaging to the workshop's reputation, and not diagnosis.

**Examiner Annotation:** Outstanding. The student extracts the correct conclusion from the fuel trim data before touching the vehicle, and — crucially — explains the underlying reasoning: a fixed-volume leak is proportionally large at low airflow and small at high airflow. That explanation, and the explicit contrast with what fuel delivery and MAF faults would look like instead, demonstrates genuine diagnostic understanding rather than pattern matching. The correlation of the gradual onset and the customer's own description with the hypothesis shows the student is integrating all available evidence. The sequence correctly places visual inspection before equipment, includes the free checks (dipstick, oil filler cap) that are genuinely common causes, and identifies the smoke test as definitive. The safety qualification on the flammable-spray method is appropriate and unprompted. The root cause section — asking why a hose perished and rerouting rather than simply replacing — is the mark of a technician who will not see the vehicle back. Resetting adaptive fuel trims is a detail frequently overlooked and correctly explained. The closing statement on parts-swapping names the exact failure mode this unit exists to prevent. Strong Competent.

---

*Next: AURAFA003 — Use and maintain automotive workplace tools and equipment*

*AIIPD RTO Training Resources | AUR30620 Certificate III in Light Vehicle Mechanical Technology | © Liam Michael Clancy / Philosophersknow 2026*
