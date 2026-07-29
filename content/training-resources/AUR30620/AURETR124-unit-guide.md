# AURETR124 — Inspect and Test Electrical Circuits
## Complete Student Assessment Guide

**Unit Code:** AURETR124
**Unit Title:** Inspect and test electrical circuits
**Training Package:** AUR Automotive Retail, Service and Repair
**Qualification:** AUR30620 Certificate III in Light Vehicle Mechanical Technology (CORE unit)
**AIIPD Resource Pack — Student Edition**

---

## What This Unit Is About

A modern vehicle contains kilometres of wiring, dozens of control modules, and multiple communication networks. Electrical faults are now the largest single category of vehicle faults, and they are the category where guesswork is most expensive — electrical components are frequently non-returnable once fitted.

AURETR124 asks you to test circuits systematically using the correct instruments and interpret what the readings actually mean.

---

## Electrical Fundamentals

### The Three Quantities

| Quantity | Symbol | Unit | Analogy |
|---|---|---|---|
| **Voltage** | V | Volts | Pressure |
| **Current** | I | Amps | Flow rate |
| **Resistance** | R | Ohms (Ω) | Restriction |

### Ohm's Law

**V = I × R**

Rearranged:
- **I = V ÷ R**
- **R = V ÷ I**

**Worked example:** A headlight bulb draws 4.6A at 13.8V.
R = 13.8 ÷ 4.6 = **3Ω**

**Power: P = V × I**

Same bulb: P = 13.8 × 4.6 = **63.5W**

**Practical use of power calculations:** knowing the wattage tells you the current draw, which determines the correct fuse and wire size.

Current from power: **I = P ÷ V**

A 55W headlight at 13.8V draws 55 ÷ 13.8 = **4A**. A 10A fuse is appropriate; a 30A fuse would not protect the circuit at all.

---

## Circuit Types

### Series Circuits
Components in a single path. Current is the same everywhere; voltage divides across components.

- **Total resistance = R₁ + R₂ + R₃...**
- If one component fails open, **the whole circuit stops**

### Parallel Circuits
Components on separate branches. Voltage is the same across each branch; current divides.

- **Total resistance is less than the smallest individual resistance**
- If one branch fails, **the others continue**

**Vehicle lighting is wired in parallel** — which is why one blown bulb does not extinguish the rest.

### Circuit Requirements

Every complete circuit needs:
1. **Power source** — battery or alternator
2. **Protection** — fuse or circuit breaker
3. **Conductor** — wiring
4. **Control** — switch or relay
5. **Load** — the component doing work
6. **Return path** — earth/ground back to the source

**The earth path is part of the circuit and is where a very large proportion of automotive electrical faults occur.** Earth points corrode, particularly where a wire attaches to a body panel exposed to moisture and road salt.

---

## Fault Types

| Fault | Description | Symptom |
|---|---|---|
| **Open circuit** | Break in the path — broken wire, blown fuse, failed switch, corroded connector | Component does not operate at all |
| **Short to earth** | Conductor contacts earth before the load | **Blows the fuse**, usually immediately |
| **Short to power** | Conductor contacts a live feed | Component operates when it should not |
| **High resistance** | Partial restriction — corrosion, loose connection, damaged wire | **Component operates weakly, intermittently, or slowly** |

**High resistance is the most commonly missed fault type.** It does not blow a fuse and it does not stop the circuit. It just makes things work badly — a dim light, a slow motor, a starter that cranks lazily.

**A resistance test often will not find it, but a voltage drop test will.** See below.

---

## Test Equipment

### Digital Multimeter

| Function | Connection | Circuit state |
|---|---|---|
| **Voltage** | **Parallel** — across the component or section | **Powered** |
| **Current** | **Series** — meter in line with the circuit | **Powered** |
| **Resistance** | Across the component | **De-energised and isolated** |

**Critical safety and equipment point:** measuring **current** requires the leads in the dedicated amps sockets. **Leaving the leads in the amps sockets and then attempting to measure voltage creates a direct short across the source** — this blows the meter's internal fuse at best and can cause arcing and injury.

**Resistance measurement must be on an unpowered, isolated circuit.** Applying voltage to a meter set to ohms damages it, and any parallel path in the circuit gives a false low reading.

### Test Lamp
- Simple and fast for confirming presence of power
- **A conventional filament test lamp draws significant current and can damage sensitive electronic circuits and modules.** Use a **high-impedance LED test lamp** or a multimeter on electronic circuits
- A test lamp confirms voltage is present; it does not tell you how much

### Oscilloscope
Shows voltage over time. Required for:
- Sensor waveforms — crank, cam, ABS wheel speed
- Intermittent faults faster than a meter's sample rate
- Communication bus signals
- Injector and ignition patterns

**A signal can have the correct voltage and the wrong shape.** A meter reads the voltage; only a scope shows the pattern.

### Ammeter / Current Clamp
An **inductive clamp** measures current without breaking the circuit — far more practical than putting a meter in series.

Used for parasitic drain testing, starter draw, and charging output.

---

## Voltage Drop Testing — The Most Useful Test

**This is the technique that separates competent electrical diagnosis from parts swapping, and it is under-used.**

### The Principle

Voltage drop is measured across a section of a **live, loaded circuit**. The reading shows how much voltage is being lost across that section — which is a direct measure of unwanted resistance **under actual working conditions**.

### Why It Beats a Resistance Test

A corroded connection may read a perfectly acceptable resistance with a multimeter, because the meter passes only a tiny test current, which finds a path through the corrosion.

Put **real load current** through the same connection and the restriction becomes obvious.

**This is why circuits pass a resistance test and still fail in service.** Resistance tests are static; voltage drop tests are dynamic.

### Method

1. Circuit **powered and operating under normal load**
2. Meter on **DC volts**
3. Place probes **across the section** being tested — from one end of a cable to the other, or across a connection, switch, or earth point
4. Read the voltage lost across that section

### Acceptable Values — Guide

| Section | Maximum acceptable drop |
|---|---|
| Across a single connection or terminal | ~0.1V |
| Across a length of cable | ~0.2V |
| Across an **earth** connection | **~0.1V or less** |
| Total across a complete circuit's supply side | ~0.5V |

**[VERIFY: Acceptable voltage drop values against the manufacturer's specification for the circuit in question. Figures vary with circuit current and application.]**

**Anything above these indicates unwanted resistance in that section.** Move the probes progressively to isolate exactly where.

### Worked Example

A starter cranks slowly. Battery tests good.

Voltage drop testing while cranking:

| Test point | Reading | Assessment |
|---|---|---|
| Battery positive post to starter terminal | 0.15V | Good |
| Battery negative post to engine block | **0.9V** | **Excessive** |
| Engine block to starter body | 0.05V | Good |

**Diagnosis:** the fault is in the earth path between the battery negative and the engine block — a corroded or loose earth strap.

**0.9V lost on the earth side is 0.9V not available to the starter.** At the currents a starter draws, that is a substantial loss of cranking power.

**The starter itself is fine.** Replacing it — which is what many technicians would do on a "slow crank" complaint — would cost the customer several hundred dollars and would not fix the fault.

---

## Circuit Protection

### Fuses

A fuse is a deliberate weak point that fails before the wiring does.

| Type | Application |
|---|---|
| **Blade (ATO/ATC, mini, micro)** | Standard modern automotive |
| **Maxi / cartridge** | High current |
| **Fusible link** | Main circuit protection near the battery |
| **Circuit breaker** | Resettable; used where nuisance trips are likely |

**Fuses are colour-coded by rating.** Common ratings: 5A tan, 7.5A brown, 10A red, 15A blue, 20A yellow, 25A clear/natural, 30A green.

**[VERIFY: Fuse colour coding against the standard applying to the fuse type in use.]**

**The rules:**
- **Never fit a higher-rated fuse than specified.** The fuse protects the wiring. A higher fuse allows enough current to melt insulation and start a fire before it blows
- **Never bypass a fuse** with wire, foil, or a bolt
- **A fuse that blows repeatedly indicates a fault.** Replacing it without diagnosing is treating a symptom, and the fault is usually a short to earth
- Check a fuse **visually and with a meter** — some fuses fail without an obvious visible break

### Relays

A relay uses a small control current to switch a large load current. This allows a low-current switch and thin control wiring to operate a high-current device.

**Standard terminal numbering:**

| Terminal | Function |
|---|---|
| **85** | Coil (control) |
| **86** | Coil (control) |
| **30** | Common / power in |
| **87** | Normally open output |
| **87a** | Normally closed output |

**Testing a relay:**
1. Confirm power and earth at the **control side** (85/86)
2. Confirm power at **30**
3. Listen or feel for the click when energised
4. Check for output at **87** when energised
5. **Substitute a known good identical relay** — the fastest test where one is available

**Measure the coil resistance** — an open coil reads infinite resistance.

---

## Wiring Diagrams

Reading a wiring diagram is essential and is directly assessed.

**Key elements:**
- **Circuit symbols** — battery, fuse, switch, relay, motor, lamp, earth, connector, module
- **Wire colour codes** — usually a base colour and a tracer, e.g. RD/BK is red with a black tracer
- **Wire gauge**
- **Connector identification** — C101, C204 — matched to a connector location table
- **Earth points** — G101, G203 — with locations
- **Splices** — where circuits join
- **Component location references**

**Approach to reading:**
1. Identify the component that is faulty
2. Trace its **supply** back to the fuse and the power source
3. Trace its **earth** to the earth point
4. Identify the **control** — switch, relay, or module
5. Note **shared circuits** — a fuse feeding multiple components tells you which other symptoms should be present if the fuse is the fault

**Shared circuits are a powerful diagnostic shortcut.** If three unrelated components fail together, look for what they have in common — a shared fuse, a shared earth, or a shared connector.

---

## Diagnostic Method

**1. Verify the fault.** Confirm the symptom and the conditions.

**2. Check the obvious.** Fuse, battery voltage, connector security, obvious damage.

**3. Get the wiring diagram.** Do not trace circuits by guess.

**4. Determine the fault type.** Does the component do nothing (open circuit), blow a fuse (short to earth), operate weakly (high resistance), or operate when it should not (short to power)?

**5. Split-half testing.** Test at the midpoint of the circuit to determine which half contains the fault, then repeat within that half. This is dramatically faster than testing every point in sequence.

**6. Test, do not assume.** Confirm each finding with a measurement.

**7. Find the root cause.** A chafed wire is a symptom — what was it chafing on? Repairing the wire without addressing the chafe point means it recurs.

**8. Verify the repair** under the conditions that produced the fault.

---

## Safety

- **Disconnect the battery** before working on circuits where a short is possible — negative terminal first
- **Remove rings and watches.** A ring bridging a battery terminal to chassis heats to glowing in seconds and causes severe burns and degloving injuries
- **Never work on high voltage systems without specific training and authorisation.** Orange cabling means stop — see AURAFA004
- Airbag/SRS circuits require the manufacturer's disable procedure and waiting period
- Beware of back-probing damaging connector seals — use proper back-probe pins
- **Do not pierce insulation** to test — the hole admits moisture and creates the next corrosion fault

---

## Evidence Checklist — AURETR124

**Knowledge Evidence**
- [ ] Statement and application of Ohm's Law and the power formula with worked calculations
- [ ] Explanation of series and parallel circuits and how resistance combines in each
- [ ] Identification of the six elements of a complete circuit
- [ ] Explanation of why the earth path is a common fault location
- [ ] Identification of four fault types and their characteristic symptoms
- [ ] Explanation of why high resistance is the most commonly missed fault
- [ ] Explanation of correct multimeter connection for voltage, current and resistance
- [ ] Explanation of the hazard of leaving leads in the amps sockets
- [ ] Explanation of why a filament test lamp can damage electronic circuits
- [ ] Explanation of voltage drop testing, why it must be done under load, and why it finds faults a resistance test misses
- [ ] Acceptable voltage drop values for connections, cables and earths
- [ ] Explanation of fuse function and why a higher-rated fuse must never be fitted
- [ ] Identification of standard relay terminal numbering and a relay test procedure
- [ ] Explanation of how to read a wiring diagram including colour codes, connectors and earth points
- [ ] Explanation of how shared circuits assist diagnosis
- [ ] Description of split-half testing

**Performance Evidence**
- [ ] Measure voltage, current and resistance correctly on a live circuit
- [ ] Perform voltage drop testing on a starting or charging circuit and interpret the result
- [ ] Diagnose an open circuit, a short to earth and a high resistance fault
- [ ] Test a relay and determine serviceability
- [ ] Trace a circuit using a wiring diagram from supply through control to load and earth
- [ ] Identify the correct fuse rating for a specified load
- [ ] Diagnose a fault to root cause and identify why the component failed

---

## Worked Example

**Prompt:**

*A customer complains that the headlights on their vehicle are dim, and it has been getting gradually worse over several months. Both headlights are affected equally. New bulbs were fitted last month by another workshop and made no difference. The battery and charging system test normal, and all other electrical items work correctly.*

*Describe your diagnostic approach.*

---

**Exemplary Response:**

The information given already rules out most of the possibilities, and the pattern points clearly at one fault type.

---

**What the symptoms tell me before I touch anything:**

**Both headlights equally affected.** Headlights are wired in **parallel**, so a fault in one branch would affect only that light. Both being equally dim means the fault is in a section **common to both** — the shared supply, the shared earth, the relay, or the switch.

**New bulbs made no difference.** The bulbs are eliminated, and the previous workshop has effectively already run that test for me.

**Battery and charging normal, everything else works.** The fault is not a system-wide supply problem. It is specific to the headlight circuit.

**Gradual onset over months.** This is the most informative detail. **Sudden failures suggest a break; gradual degradation suggests progressive corrosion.** A wire either breaks or it does not — but a corroding connection gets worse steadily over time.

**Dim, not off.** The circuit is complete — current is flowing, just not enough.

---

**Diagnosis: high resistance somewhere in the shared portion of the headlight circuit.**

Almost certainly a **corroded connection or earth point**.

**Why high resistance produces exactly this symptom:** the resistance forms a voltage divider with the bulb. Some of the available voltage is consumed across the corroded connection instead of across the filament. Less voltage across the bulb means substantially less light output — light output falls off sharply with voltage, so even a modest drop is very visible.

---

**Why I would not start with a resistance test:**

A corroded connection frequently reads acceptable resistance on a multimeter, because the meter passes only a few milliamps and finds a path through the corrosion.

Put the headlight's actual current through it and the restriction appears. **This fault must be found under load, which means voltage drop testing.**

---

**My test sequence:**

**1. Obtain the wiring diagram.** I need to know the actual circuit — where the fuse is, whether there is a relay, where the earth points are and their locations, and where the supply splits to the two lamps. Tracing by guess wastes time.

**2. Measure voltage at the bulb connector, headlights on.**

This is the single most informative first measurement.

- If I have close to system voltage (around 13.5–14V with the engine running) at the connector, the supply and earth are fine and the problem is elsewhere
- If I have significantly less — say 10V — I have confirmed a voltage drop somewhere in the circuit and I now need to find which side

**3. Split the circuit — supply side versus earth side.**

With the lights on and drawing current:

- **Supply side test:** meter across from battery positive to the bulb's supply terminal
- **Earth side test:** meter across from the bulb's earth terminal to battery negative

Whichever reads high is the side with the fault. This immediately halves the search.

**In my experience of this symptom pattern, the earth side is the more likely candidate** — earth points bolt to body panels, are exposed to moisture and road spray, and corrode. But I test rather than assume.

**4. Work along the faulty side to isolate the section.**

Progressively move the probes to narrow it down — across the fuse and holder, across the relay contacts (30 to 87), across the switch, across each connector, across the earth strap and the earth point.

**Split-half testing** rather than sequential testing: probe the midpoint, determine which half contains the drop, then repeat within that half. Far faster than working through every connection in order.

**5. Interpret against limits.**

| Section | Acceptable | Action if exceeded |
|---|---|---|
| Single connection | ~0.1V | Clean and remake |
| Cable run | ~0.2V | Investigate |
| Earth connection | ~0.1V | Clean and remake |

**6. Check the relay specifically.**

Relay contacts erode and develop resistance with age and switching cycles. A voltage drop across terminals 30 and 87 while the relay is energised and carrying load will reveal worn contacts. **Substituting a known good relay is a fast confirmation** if one is available.

---

**Most likely findings, in order of probability:**

1. **Corroded headlight earth point** — a bolted connection to the body, green or white corrosion, sometimes under an apparently sound bolt
2. **Corroded or high-resistance connector** in the shared supply
3. **Worn relay contacts**
4. **Corroded fuse holder** — the holder rather than the fuse itself
5. **Degraded switch contacts**, if the switch carries the full load rather than controlling a relay

---

**The repair — and the root cause:**

If I find a corroded earth point:

- **Clean it properly** — remove the bolt, wire-brush both the terminal and the body contact face back to bright metal, remove all paint and corrosion from the mating surface
- **Remake it tight** with the correct fastener
- **Protect it** — dielectric grease or a suitable corrosion inhibitor over the finished joint

**Then ask why it corroded.** If moisture is getting to that earth point because of a missing seal, a blocked drain, a damaged grommet, or previous accident repair, the same fault returns in a year. **Cleaning the connection treats the symptom; addressing the water ingress treats the cause.**

---

**Verification:**

- **Re-test voltage drop** across the repaired section — it should now be within limits
- **Measure voltage at the bulb** with the lights on — it should now be close to system voltage
- **Confirm the customer's complaint is resolved** — the lights should be visibly brighter, and I would check both
- Check the other side has not been masking a second, smaller drop

---

**What I would not do:**

Fit another set of bulbs. Another workshop has already done that and it did not work — which is useful information rather than a failed attempt. Repeating it would be charging the customer for a test that has already returned a negative result.

**Examiner Annotation:** Outstanding. The student extracts a great deal from the symptom description before touching the vehicle, and every inference is sound: parallel wiring means both lamps affected points to a shared section, gradual onset indicates progressive corrosion rather than a break, and dim rather than off confirms a complete but restricted circuit. The explanation of why high resistance produces dimming — voltage division with the filament — is technically correct and explains the mechanism rather than just naming the fault. The key judgement is refusing to start with a resistance test and explaining precisely why it would give a false pass, which is the central insight of this unit. The split of supply side versus earth side to halve the search space, followed by split-half testing within the faulty side, is efficient methodology rather than sequential guessing. The student states a probability judgement about earth points while explicitly noting they will test rather than assume — the correct balance between pattern knowledge and evidence. The repair section addresses root cause by asking why the earth corroded, and identifies that cleaning without fixing water ingress guarantees recurrence. Declining to refit bulbs, and correctly framing the previous workshop's attempt as a completed negative test, avoids charging the customer for redundant work. Strong Competent.

---

*This completes the current AUR30620 unit guide series.*

*AIIPD RTO Training Resources | AUR30620 Certificate III in Light Vehicle Mechanical Technology | © Liam Michael Clancy / Philosophersknow 2026*
