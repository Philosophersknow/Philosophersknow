# ICTSAS305 — Provide ICT Advice to Clients
## Complete Student Assessment Guide

**Unit Code:** ICTSAS305
**Unit Title:** Provide ICT advice to clients
**Training Package:** ICT Information and Communications Technology
**Qualification:** ICT30120 Certificate III in Information Technology (CORE unit)
**AIIPD Resource Pack — Student Edition**

---

## What This Unit Is About

Most IT problems are solved twice: once technically, and once in the conversation with the person who has the problem. A technician who diagnoses a fault correctly but cannot explain it, cannot manage the user's expectations, and leaves the user feeling patronised has not done the job.

ICTSAS305 is about the client-facing half of IT work. It asks you to identify what the client actually needs (which is often not what they first ask for), provide advice pitched at their level of technical understanding, and document the interaction properly.

---

## Understanding the Client

### Identifying the Real Requirement

Clients describe **symptoms** and often propose **solutions**. Neither is necessarily the requirement.

| What the client says | What they might actually need |
|---|---|
| "I need a faster computer" | More RAM; an SSD; malware removal; fewer startup programs; or genuinely a new machine |
| "The internet is down" | Their Wi-Fi has dropped; DNS is failing; one application cannot reach its server; the whole network is down |
| "Can you install [specific software]?" | A capability that software provides — which may already exist in a licensed tool they have |
| "The printer is broken" | Out of toner; paper jam; driver issue; queued job blocking; network path changed |

**The technique:** Ask open questions before proposing anything.

- "Can you walk me through what happens when you try?"
- "When did it last work properly?"
- "Has anything changed recently — updates, new software, a move?"
- "Is it affecting just you, or others as well?"
- "What are you trying to achieve?" (the most valuable question — it moves from proposed solution to actual requirement)

### Assessing Technical Literacy

Pitch your advice to the client's level. Misjudging this in either direction damages the interaction:

- **Too technical:** The client feels stupid, does not understand the advice, cannot act on it, and loses confidence in you
- **Too simplified:** A technically competent client feels patronised and stops trusting your assessment

**How to calibrate:** Listen to the language they use. A client who says "the thing with the icons won't come up" is telling you something different from one who says "Explorer isn't launching, and I've already tried restarting the shell." Match their vocabulary, and check in: "How much detail would be useful here?"

---

## Providing Advice

### Structuring an Explanation

A useful structure for explaining a technical issue to a non-technical client:

1. **What is happening** — plain language description of the symptom
2. **Why it is happening** — the cause, at whatever depth is useful to them
3. **What can be done** — the options, with trade-offs
4. **What you recommend** — a clear recommendation, not just a list
5. **What happens next** — who does what, and by when

**Example:**

> "Your machine is slow because the hard drive is nearly full — you're at 97%, and Windows needs free space to work with. There are three options: we clear out old files, we move your photos to the network drive, or we fit a bigger drive. I'd suggest moving the photos to the network drive — it frees about 200GB, it's backed up automatically, and it doesn't cost anything. I can do that this afternoon if you're free to confirm which folders to move."

Note what this does: no jargon, a specific cause with evidence, three genuine options, a clear recommendation with reasoning, and a concrete next step.

### Explaining Without Jargon

| Jargon | Plain-language alternative |
|---|---|
| "Your DNS isn't resolving" | "Your computer can't look up the address of that website" |
| "The DHCP lease has expired" | "Your computer's network address has run out and needs renewing" |
| "It's a driver incompatibility" | "The software that lets Windows talk to that printer is the wrong version" |
| "You've hit the mailbox quota" | "Your mailbox is full — it won't accept new mail until you clear some space" |
| "It's a permissions issue" | "Your account doesn't currently have access to that folder" |

**You do not have to remove all technical terms** — you have to make sure the client understands the ones you use. Introducing a term and defining it once is often better than avoiding it, especially if the client will encounter it again.

### Managing Expectations

Being honest about limitations, timeframes, and cost is part of good advice:

- **Do not promise timeframes you cannot meet.** "I'll have it done today" that becomes three days destroys trust far more than "It'll likely be Thursday" that arrives Wednesday.
- **Be honest about what you do not know.** "I haven't come across that error before — give me twenty minutes to research it and I'll come back to you" is entirely professional. Guessing confidently is not.
- **Flag costs early.** If the resolution involves buying hardware or licences, say so before the client has assumed it is free.
- **Be clear about data risk.** If a repair carries any risk to data, say so explicitly and confirm backups before proceeding.

### Escalation — Knowing Your Limits

Operating within your competence is an ethical obligation (see ICTICT313). Escalate when:

- The problem is beyond your technical knowledge or authorisation
- The fix requires access or privileges you do not hold
- The issue involves a security incident or suspected data breach
- The issue affects a critical system and the risk of getting it wrong is high
- The client is dissatisfied and the situation needs a supervisor

**How to escalate well:** Do not simply hand the ticket over. Provide the next person with what you have established — the symptom, what you have tested, what you have ruled out, and what the client has been told. A well-documented escalation saves the next technician from repeating your work.

---

## Documentation

### Why Documentation Matters

- **Continuity:** The next person to touch the issue needs your findings
- **Pattern recognition:** Five similar tickets reveal a systemic problem that one ticket hides
- **Accountability:** A record of what was advised and agreed protects both you and the client
- **Knowledge base:** Documented solutions make future occurrences faster to resolve

### What a Good Ticket Record Contains

| Field | Content |
|---|---|
| **Client and contact** | Who reported it and how to reach them |
| **Date/time reported** | When it came in |
| **Symptom as reported** | The client's description, in their words |
| **Systems affected** | Device, application, network segment, number of users |
| **Diagnostic steps taken** | What you tested, in order, and the result of each |
| **Root cause** | What was actually wrong (not just what you changed) |
| **Resolution** | What you did to fix it |
| **Advice given to client** | What you told them, including any recommendations they declined |
| **Follow-up required** | Anything outstanding |
| **Status** | Open / escalated / resolved / closed |

**Write for the person who reads it in six months** — not for yourself this afternoon. "Fixed it" is not a resolution record. "Replaced faulty CAT6 patch lead between wall port 14 and the desktop NIC; link light restored, sustained 1Gbps confirmed" is.

### Service Level Agreements (SLAs)

An SLA is an agreement defining the level of service the IT provider will deliver. Common SLA elements:

- **Response time:** How quickly the provider will acknowledge a request
- **Resolution time:** Target time to resolve, usually varying by priority
- **Priority definitions:** What constitutes P1 (critical), P2 (high), P3 (medium), P4 (low)
- **Availability:** Uptime commitment for systems (e.g., 99.9%)
- **Hours of coverage:** Business hours vs 24/7
- **Escalation path:** What happens if targets are missed

**Typical priority framework:**

| Priority | Definition | Example |
|---|---|---|
| **P1 — Critical** | Whole business or critical system down; no workaround | Server down; entire site offline; ransomware detected |
| **P2 — High** | Significant impact on a group; workaround difficult | Department's shared drive inaccessible; email delayed for many users |
| **P3 — Medium** | Individual affected; workaround exists | One user's printer not working; single application fault |
| **P4 — Low** | Minor issue or request | Software install request; how-to question |

Understanding priority matters because it determines what you work on first. A P1 always displaces a P3, regardless of who asked first or who asked most loudly.

---

## Communication Skills for IT Support

### Active Listening
- Let the client finish describing the problem before diagnosing
- Reflect back to confirm understanding: "So it started after the Windows update on Tuesday, and it only affects the accounting software — is that right?"
- Take notes during the conversation

### Dealing With Frustrated Clients

Clients contacting IT support are often already frustrated — something is not working and it is stopping them from doing their job.

**What works:**
- Acknowledge the impact: "That sounds really disruptive — you've lost most of the morning to this."
- Do not become defensive, even if the cause was user error
- Do not blame the client, other departments, or vendors
- Focus on the path forward rather than relitigating what happened
- Give a realistic timeframe and then meet it

**What does not work:**
- "It's working fine for everyone else"
- "You must have done something"
- "That's not really my area"
- Silence — a client who has heard nothing for two days assumes nothing is happening

### Written Communication

Much IT support is by email or ticketing system. Written advice must be:
- **Clear:** One idea per paragraph; numbered steps for procedures
- **Complete:** Anticipate the follow-up question and answer it
- **Actionable:** State exactly what you need the client to do
- **Professional in tone:** No sarcasm, no exasperation, no all-caps

---

## Evidence Checklist — ICTSAS305

**Knowledge Evidence**
- [ ] Explanation of how to identify a client's actual requirement rather than their proposed solution
- [ ] Description of at least 5 open questions useful for scoping a client's ICT problem
- [ ] Explanation of how to assess and match a client's technical literacy level
- [ ] Description of a structure for explaining a technical issue to a non-technical client
- [ ] Identification of at least 5 jargon terms with plain-language alternatives
- [ ] Explanation of when to escalate an issue and what a good escalation contains
- [ ] Description of at least 8 elements of a good support ticket record
- [ ] Explanation of SLAs including response time, resolution time, and priority levels
- [ ] Description of at least 4 techniques for handling a frustrated client

**Performance Evidence**
- [ ] Client interaction: role play or scripted response scoping an ICT problem from a vague initial description
- [ ] Written advice: prepare a written response to a client explaining a technical issue and recommending an option
- [ ] Ticket documentation: complete a support ticket record for a described scenario
- [ ] Priority assessment: given 4 concurrent incidents, assign priorities and justify the order of work
- [ ] Escalation: draft an escalation handover for an unresolved issue

---

## Worked Example

**Prompt:**

*You work on the help desk at a 60-person architecture firm. At 9:15am you receive the following four requests within ten minutes of each other:*

*A. The office manager reports that the shared network drive is inaccessible to everyone in the accounts team (4 people). They cannot open or save files.*
*B. A senior architect says their laptop is "running really slowly" and it has been "getting worse for a few weeks."*
*C. A new starter cannot log in — their account was set up yesterday and they are due in a client meeting at 10am.*
*D. A director emails asking you to install a PDF editing tool they saw advertised, "when you get a chance."*

*Assign priorities, explain your order of work, and write the initial response you would send to the senior architect (B).*

---

**Exemplary Response:**

**Priority assessment:**

| Request | Priority | Reasoning |
|---|---|---|
| **A — Accounts drive inaccessible (4 users)** | **P2 — High** | A whole team is unable to work. It affects multiple users and there is no obvious workaround. It may also be the visible symptom of a wider file server or permissions problem, which would make it P1 — I need to check scope quickly. |
| **C — New starter cannot log in** | **P2 — High** | One user, but they are fully blocked (cannot work at all) and there is a hard deadline at 10am. Account provisioning faults are usually quick to fix, which makes this high-value to resolve early. |
| **B — Laptop running slowly** | **P3 — Medium** | One user, degraded but still working. It has been developing over weeks, so it is not an emergency. It does need proper diagnosis rather than a quick fix. |
| **D — PDF tool install request** | **P4 — Low** | A request, not an incident. No one is blocked. The client's own wording ("when you get a chance") confirms it. It also needs a licensing and procurement check before anything is installed. |

**Order of work:**

1. **First, spend five minutes scoping A.** I need to know whether this is four users or sixty. If the file server is down or a share has been unmounted, this is a P1 and everything else waits. If it is a permissions change affecting only the accounts group, it stays P2. Establishing scope before committing to a fix is the important step here.

2. **Then C, in parallel if possible.** New-account login failures are commonly a simple cause — account not enabled, licence not assigned, password not set to the expected value, or replication delay. There is a hard 10am deadline, and the fix is usually short. Resolving this early removes a time-critical item.

3. **Then back to A** for the full resolution if it was not fixed in the scoping step.

4. **Then B.** I would respond to the architect straight away (see below) even though I will not start work on it for a while — an acknowledgement with a realistic timeframe is far better than silence.

5. **D last**, and it needs a licensing check and probably a procurement conversation rather than just an install.

**Note on D:** I would not install requested software on a director's machine without checking that we hold a valid licence and that it complies with our software policy. Seniority does not change licensing law. I would respond politely, confirm what the director is trying to achieve, and check whether an existing licensed tool already does it.

---

**Initial response to the senior architect (B):**

> Subject: RE: Laptop running slowly — SR-2291
>
> Hi [Name],
>
> Thanks for reporting this, and sorry it has been getting worse — that is frustrating when it has been building for weeks rather than just appearing overnight.
>
> I have logged it as SR-2291. I am dealing with two urgent issues this morning (a shared drive outage affecting the accounts team, and a new starter who cannot log in before a 10am meeting), so I expect to get to yours **this afternoon**. I will confirm a time once the morning issues are cleared.
>
> In the meantime, two things that would help me diagnose it faster:
>
> 1. Is it slow **all the time**, or particularly when you are using specific software (Revit, AutoCAD, large PDFs)?
> 2. Roughly how much free space is showing on your C: drive? You can check this in File Explorer under "This PC" — no need to change anything, I just want the number.
>
> A gradual slowdown over weeks usually points to one of a few things — disk space, a background process, or storage health — and those two answers will narrow it down considerably before I even sit down at the machine.
>
> Thanks,
> [Name]
> IT Support

**Why this response works:** It acknowledges the impact without being obsequious, gives a realistic timeframe with the reason for the delay (so the delay reads as prioritisation rather than neglect), commits to a follow-up, and asks two specific questions that will genuinely speed up the diagnosis. The disk-space question is explained in plain terms with a reassurance that nothing needs changing. It does not promise a cause or a fix before diagnosing.

**Examiner Annotation:** Outstanding. The priority assessment is correct and — importantly — the student identifies that A's priority depends on scope and builds a scoping step into the plan rather than assuming. The reasoning for placing C above B is sound (fully blocked + hard deadline + short expected fix). The student correctly refuses to install unlicensed software for a director and articulates why seniority is irrelevant to licensing. The written response demonstrates realistic expectation management, plain-language explanation, and diagnostic questions that add genuine value. This is professional help desk practice. Strong Competent.

---

*Next: BSBXCS303 — Securely manage personally identifiable information and workplace information*

*AIIPD RTO Training Resources | ICT30120 Certificate III in Information Technology | © Liam Michael Clancy / Philosophersknow 2026*
