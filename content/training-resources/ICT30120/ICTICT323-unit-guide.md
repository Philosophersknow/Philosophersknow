# ICTICT323 — Align Work Practices with the ICT Industry Environment
## Complete Student Assessment Guide

**Unit Code:** ICTICT323
**Unit Title:** Align work practices with the ICT industry environment
**Training Package:** ICT Information and Communications Technology
**Qualification:** ICT30120 Certificate III in Information Technology (CORE unit)
**AIIPD Resource Pack — Student Edition**

---

## What This Unit Is About

ICT is not a stable industry with a fixed body of knowledge. The tools, platforms, delivery models, and job roles change continuously. A technician whose skills were current in 2016 — on-premises servers, desktop imaging, perimeter firewalls — is not employable on that basis alone in 2026.

ICTICT323 asks you to understand the industry you are entering: how it is structured, how work is organised within it, what standards and frameworks govern practice, where it is heading, and how you keep yourself current in it.

---

## Industry Structure

### Where ICT Work Happens

| Setting | Description | What Work Looks Like |
|---|---|---|
| **Internal IT department** | IT function inside a non-IT organisation (bank, hospital, retailer, council) | Supporting one organisation's staff and systems; deep knowledge of one environment |
| **Managed Service Provider (MSP)** | Outsourced IT for multiple client organisations | Supporting many environments; broad exposure; ticket-driven; SLA-bound |
| **Vendor / product company** | Builds and sells software or hardware | Development, product support, pre-sales engineering |
| **Consultancy / systems integrator** | Project-based delivery and advisory | Implementations, migrations, architecture; project rather than BAU |
| **Cloud / hosting provider** | Operates infrastructure at scale | Platform operations, automation, site reliability |
| **Government** | Federal, state, local | Larger scale, stronger governance and procurement constraints, security clearances for some roles |

**Career implication:** MSPs are a common and effective entry point because the variety of environments accelerates skill development. Internal IT offers depth and often better work-life balance. Neither is superior — they suit different people and stages.

### Common Role Families

| Role Family | Entry Roles | Progression |
|---|---|---|
| **Support / service desk** | Level 1 support, desktop support | Level 2/3, team lead, service delivery manager |
| **Infrastructure / operations** | Junior sysadmin | Systems administrator, engineer, architect |
| **Networking** | Network technician | Network engineer, network architect |
| **Cybersecurity** | SOC analyst (L1) | Security analyst, incident responder, security engineer |
| **Cloud / DevOps** | Cloud support, junior engineer | Cloud engineer, platform engineer, SRE |
| **Development** | Junior developer, tester | Developer, senior developer, tech lead |
| **Data** | Data entry, junior analyst | Data analyst, data engineer, BI developer |
| **Business-facing** | Junior BA, project coordinator | Business analyst, project manager |

**Most ICT careers begin on a service desk.** This is not a limitation — it provides exposure to the widest range of systems and, crucially, to how users actually behave, which is knowledge that infrastructure and security specialists frequently lack.

---

## How ICT Work Is Organised

### ITIL and Service Management

**ITIL** (Information Technology Infrastructure Library) is the most widely adopted framework for IT service management. You will encounter its vocabulary in almost any support role, so the distinctions matter.

| Term | Definition | Example |
|---|---|---|
| **Incident** | An unplanned interruption or reduction in quality of a service | A user cannot log in; email is down |
| **Service request** | A user request for something standard and pre-approved | New laptop; software install; password reset; access request |
| **Problem** | The underlying cause of one or more incidents | Twenty login incidents this week all trace to a failing domain controller |
| **Known error** | A problem with a documented root cause and workaround | "Known issue with driver v4.2 — roll back to 4.1 as workaround" |
| **Change** | Any addition, modification, or removal that could affect services | Server patching; firewall rule change; software deployment |
| **Major incident** | High-impact incident requiring coordinated urgent response | Entire site offline; ransomware detected |

**Incident vs problem is the distinction students most often get wrong.** Incident management restores service as fast as possible — often with a workaround. Problem management finds and eliminates the root cause so the incidents stop recurring. Both are necessary. An organisation that only does incident management fixes the same thing forever.

**Change management** exists because unplanned changes are a leading cause of outages. A typical change process requires: a documented change request, risk and impact assessment, a rollback plan, approval (Change Advisory Board for significant changes), a scheduled window, and post-implementation review.

**Emergency changes** have an expedited path — but expedited is not the same as unapproved. "I just fixed it quickly" without a record is how nobody can work out what broke the environment three weeks later.

### Ways of Working

| Approach | Characteristics | Typical Use |
|---|---|---|
| **Waterfall** | Sequential phases: requirements → design → build → test → deploy | Infrastructure projects, regulated environments, fixed-scope contracts |
| **Agile** | Iterative delivery in short cycles; responsive to change | Software development, product teams |
| **Scrum** | An agile framework — sprints, daily stand-ups, sprint review and retrospective, product backlog | Development teams |
| **Kanban** | Continuous flow, visualised on a board, work-in-progress limits | Support and operations teams, where work arrives unpredictably |
| **DevOps** | Development and operations integrated; automation, CI/CD, shared responsibility for running what you build | Cloud-native and platform teams |

**For a Certificate III support role, Kanban is the most likely to be encountered** — a board of tickets moving through states, with limits on how much is in progress at once.

---

## Standards, Frameworks, and Compliance

| Standard / Framework | Domain | Relevance to You |
|---|---|---|
| **ISO/IEC 27001** | Information security management systems | Your employer may be certified; you will have security procedures to follow and evidence to produce for audits |
| **ISO/IEC 20000** | IT service management | Formal service management requirements |
| **ACSC Essential Eight** | Australian baseline cyber mitigation strategies | The de facto Australian security baseline — see below |
| **PCI DSS** | Payment card data security | Applies if the organisation handles card payments |
| **Australian Privacy Principles** | Personal information handling | Applies broadly — see ICTICT313 and BSBXCS303 |
| **WCAG 2.x** | Web content accessibility | Legal obligation for government; good practice and DDA-relevant for all |
| **NIST Cybersecurity Framework** | Cyber risk management | Common in larger and international organisations |

### The ACSC Essential Eight

Published by the **Australian Cyber Security Centre**, the Essential Eight is the baseline set of mitigation strategies for Australian organisations. Knowing these by name is genuinely expected in Australian ICT roles.

1. **Application control** — only approved applications can execute
2. **Patch applications** — patch security vulnerabilities in applications promptly
3. **Configure Microsoft Office macro settings** — block macros from the internet
4. **User application hardening** — disable or restrict risky features (Flash, ads, Java in browsers)
5. **Restrict administrative privileges** — least privilege for admin accounts
6. **Patch operating systems** — patch OS vulnerabilities promptly
7. **Multi-factor authentication** — MFA for users and privileged access
8. **Regular backups** — backups performed, retained, and **tested for restoration**

Each strategy is assessed against **Maturity Levels 0 to 3**, where Level 0 means the strategy is not implemented and Level 3 represents the strongest implementation.

**[VERIFY: Essential Eight strategies and maturity model definitions are periodically revised by the ACSC. Confirm current definitions at cyber.gov.au.]**

**The most commonly failed strategy is backups** — specifically the "tested for restoration" part. An untested backup is a hope, not a control. Organisations discover their backups do not restore at the worst possible moment.

---

## Emerging Trends

You are expected to be able to discuss where the industry is going, not just where it is.

### Cloud and the Shift in Skills
The move from on-premises infrastructure to cloud (AWS, Azure, Google Cloud) has changed what infrastructure work is. Racking servers and managing physical hardware has largely been replaced by configuring services, managing identity, controlling cost, and automating deployment.

**Service models:**
- **IaaS** (Infrastructure as a Service) — you manage the OS and up; the provider manages hardware and virtualisation
- **PaaS** (Platform as a Service) — you manage the application; the provider manages the platform
- **SaaS** (Software as a Service) — you manage configuration and data; the provider manages everything else

**The shared responsibility model** is critical and widely misunderstood: moving to cloud does not transfer all security responsibility to the provider. The provider secures the cloud; **you remain responsible for securing what you put in it** — your data, your access controls, your configuration. Most cloud breaches are customer misconfiguration, not provider failure.

### Artificial Intelligence in ICT Practice
AI coding assistants, AI-assisted troubleshooting, and AI-driven security tooling are now normal parts of ICT work. Professionally, this means:

- **Verify AI output.** AI tools generate plausible, confidently-worded, and sometimes wrong answers. Running an AI-suggested command on production without understanding it is professional negligence
- **Do not paste confidential data into public AI tools.** Customer data, credentials, proprietary code, and internal configurations pasted into a public model may be retained and used for training. Check your organisation's AI use policy
- **AI-generated code carries licensing and security questions.** It may reproduce licensed code, and it may reproduce known-vulnerable patterns
- **Understanding remains the job.** A technician who can only produce solutions they cannot explain is not employable in the medium term

### Cybersecurity as a Constant
Ransomware, supply chain compromise, and business email compromise have made security a concern in every ICT role, not a specialist silo. Even entry-level support staff are expected to recognise phishing, follow least privilege, and escalate suspected incidents.

### Automation
Repetitive manual tasks are increasingly scripted (PowerShell, Bash, Python) or handled by platform automation. Technicians who can automate parts of their own work are substantially more valuable than those who cannot.

### Sustainability
Data centre energy consumption, e-waste, and device lifecycle management are now genuine considerations in ICT procurement and operations — connecting to BSBSUS211.

---

## Professional Development

### Certifications

Vendor and industry certifications are widely used in ICT hiring, sometimes more heavily than formal qualifications.

| Certification | Domain | Level |
|---|---|---|
| **CompTIA A+** | Hardware, OS, troubleshooting | Entry |
| **CompTIA Network+ / Security+** | Networking / security fundamentals | Entry–intermediate |
| **Microsoft Certified: Azure Fundamentals (AZ-900)** | Cloud fundamentals | Entry |
| **Microsoft 365 / Azure Administrator** | Platform administration | Intermediate |
| **AWS Certified Cloud Practitioner / Solutions Architect** | AWS | Entry / intermediate |
| **Cisco CCNA** | Networking | Intermediate |
| **ITIL Foundation** | Service management | Entry |

**Certifications complement rather than replace demonstrated capability.** A certification with no hands-on experience is visible to any competent interviewer within a few questions.

### Building Practical Experience

- **Home lab** — virtual machines, a spare machine, or a cloud free tier. Building, breaking, and fixing your own environment teaches more than any course
- **Cloud free tiers** — Azure, AWS, and Google Cloud all offer free tiers sufficient for meaningful learning
- **Documentation** — write up what you fix. It reinforces learning and becomes portfolio evidence
- **Open-source contribution** — even documentation improvements demonstrate engagement
- **Volunteering** — community organisations frequently need IT help and are grateful for it

### Staying Current

- Vendor release notes and product blogs for platforms you support
- **ACSC alerts and advisories** — cyber.gov.au publishes current threat advisories relevant to Australian organisations
- Industry communities — user groups, meetups, forums, relevant subreddits and Discords
- **Australian Computer Society (ACS)** — the professional association for ICT in Australia; offers certification, CPD, and professional recognition

**Set a rhythm rather than relying on motivation.** A consistent few hours a week substantially outperforms occasional intensive bursts.

---

## Professional Conduct

### Communication Across the Divide
ICT workers routinely translate between technical and non-technical contexts. The ability to explain a technical constraint to a manager in terms of business impact — cost, risk, time — is what separates technicians who stay technicians from those who progress. See ICTSAS305.

### Working Within Your Scope
- Know what you are authorised to do, and do not exceed it
- Escalate when a problem exceeds your competence — this is professional, not weak
- Never make undocumented changes to production systems
- Never access data beyond what your role requires, even when you technically can

### Documentation as a Professional Obligation
Undocumented work is a liability. If you are the only person who knows how something works, you have created a single point of failure — and you cannot take leave, change roles, or be promoted without leaving damage behind. Documentation is not administrative overhead; it is part of doing the work.

---

## Evidence Checklist — ICTICT323

**Knowledge Evidence**
- [ ] Identification of at least 5 settings where ICT work occurs and how the work differs in each
- [ ] Identification of at least 5 ICT role families with entry roles and progression paths
- [ ] Explanation of the ITIL distinction between incident, service request, problem, and change
- [ ] Explanation of why incident and problem management are both necessary
- [ ] Description of a change management process with at least 4 elements
- [ ] Comparison of at least 3 ways of working (waterfall, agile/scrum, kanban, DevOps)
- [ ] Identification of at least 4 standards or frameworks relevant to Australian ICT practice
- [ ] Identification of all 8 ACSC Essential Eight strategies
- [ ] Explanation of IaaS, PaaS, and SaaS and the cloud shared responsibility model
- [ ] Description of at least 3 professional considerations when using AI tools in ICT work
- [ ] Identification of at least 4 relevant entry-level certifications
- [ ] Description of at least 4 methods of maintaining currency in the industry

**Performance Evidence**
- [ ] Classification: given a list of described work items, classify each as incident, service request, problem, or change
- [ ] Career plan: prepare a 12-month professional development plan identifying a target role, skills gaps, certifications, and practical experience activities
- [ ] Trend analysis: describe an emerging ICT trend and its implications for an entry-level support role
- [ ] Essential Eight: assess a described organisation against at least 4 Essential Eight strategies and identify gaps
- [ ] Scenario: describe how you would handle a request to make an urgent undocumented change to a production system

---

## Worked Example

**Prompt:**

*You are a Level 1 support technician at an MSP. Over the past three weeks you have personally resolved fourteen tickets from the same client where staff report "Outlook keeps asking me to sign in again." Each time, you have walked the user through clearing their cached credentials and re-authenticating, which resolves it. Your average handle time is good and your ticket closure rate is the highest on the team. Your team leader has praised your numbers.*

*Using ITIL concepts, explain what is actually happening here, what you should do, and how you would raise it.*

---

**Exemplary Response:**

My numbers look good, and that is precisely the issue. I am efficiently resolving the same incident fourteen times instead of getting it fixed once.

---

**What is happening in ITIL terms:**

Each of the fourteen tickets is an **incident** — an unplanned interruption to a service. I have handled each one correctly by restoring service quickly, and clearing cached credentials is a legitimate **workaround**.

But fourteen incidents with an identical symptom, at the same client, within three weeks is not fourteen unrelated events. It is a **problem** — a single underlying cause producing recurring incidents. Nobody has raised it as one.

This is the classic failure mode of incident management without problem management: the service desk gets very good at applying the workaround, the metrics look healthy, and the root cause is never touched. The organisation pays for the same fix fourteen times, and the users experience the same disruption fourteen times.

**Incident management restores service. Problem management stops it happening again.** Both are needed, and only one is occurring here.

---

**Why the metrics are misleading:**

My handle time and closure rate are good *because* the workaround is quick and I have done it repeatedly. Those metrics reward volume of resolution, not elimination of cause. If I keep optimising against them, my incentive is for the problem to continue.

This is worth naming explicitly when I raise it, because a team leader looking only at dashboards sees a high performer, not a systemic issue.

---

**What I should do:**

**1. Raise a problem record.**

I would formally log this as a problem, linking the fourteen incident tickets as evidence. The linkage matters — it converts "Sam has a hunch" into a documented pattern with supporting records.

**2. Gather the pattern data before proposing a cause.**

Before theorising, I would establish what the fourteen tickets have in common and what they do not:

- Is it the same users repeatedly, or fourteen different users?
- What client, what site, what network?
- Are the affected machines on a particular OS build, Outlook version, or patch level?
- Is it laptop users, remote users, VPN users, or everyone?
- What is the timing — does it cluster at a particular time of day, or around a specific date?
- Did it start around a known change? Three weeks is a specific window — what changed three weeks ago?

That last question is usually the most productive one.

**3. Form a theory of probable cause.**

Repeated Outlook re-authentication prompts commonly trace to a small number of causes:

- A **change to conditional access or authentication policy** (token lifetime reduced, a new policy applied)
- **MFA or token configuration change** — refresh tokens expiring or being revoked more aggressively
- **A recent client or OS update** affecting the authentication broker or credential store
- **Hybrid identity synchronisation issues** — time skew, certificate expiry, or a failing sync between on-premises directory and cloud identity
- A **certificate approaching or past expiry**
- Roaming profile or credential manager corruption if it is the same subset of machines

The three-week onset strongly suggests a change rather than a gradual degradation. I would ask the client's change record and our own for anything applied around that date.

**4. Escalate with what I have.**

Diagnosing identity and conditional access configuration is beyond a Level 1 scope and probably beyond my access. That is fine — my job here is to identify the pattern, document it properly, and hand it up with the evidence assembled so the Level 2/3 engineer does not have to reconstruct three weeks of tickets.

A good escalation contains: the pattern, the linked tickets, what is common across them, what I have ruled out, the workaround currently in use, and my theory with the reasoning.

**5. Document the workaround as a known error.**

Until the root cause is fixed, the workaround should be written up as a **known error** record in the knowledge base — so any technician on the team can apply it consistently, and so the next person seeing this symptom recognises it as part of the known pattern rather than treating it as new.

---

**How I would raise it with my team leader:**

I would not frame it as a complaint about metrics, and I would not frame it as someone else's failure. Something like:

> "Something I wanted to flag — I've closed fourteen tickets for [client] in three weeks that are all the same Outlook re-auth symptom, and I've been clearing cached credentials each time. It works, but I think we're treating a problem as fourteen incidents. It started roughly three weeks ago, which makes me think something changed around then — possibly conditional access or a token lifetime setting.
>
> I've raised a problem record and linked the tickets. It's beyond my access to diagnose the identity side, so I'd like to escalate it to Level 2 with what I've gathered. I've also drafted a known error entry so the rest of the team applies the same workaround consistently while it's open.
>
> One thing worth saying — my closure numbers look good partly *because* this keeps recurring. I'd rather it stopped."

That last line matters. It is honest, it makes the metric issue visible without being accusatory, and it demonstrates that I understand what the numbers are actually measuring.

---

**The broader point:**

Fourteen incidents also means fourteen instances of a user losing time and confidence in the system, multiplied across however many users have not raised a ticket and are just living with it. Reported tickets are almost always an undercount. The real impact on that client is larger than fourteen.

**Examiner Annotation:** Outstanding. The student correctly identifies the incident/problem distinction and — critically — recognises that their own good metrics are a symptom of the failure rather than evidence of good performance. That is a genuinely sophisticated insight and the central point of the scenario. The methodology is correct: gather pattern data *before* forming a theory, then use the three-week onset to point at change rather than degradation. The candidate causes are technically plausible and appropriately ranked. The student correctly identifies the limits of Level 1 scope and escalates with assembled evidence rather than either overreaching or simply passing the ticket up. The known error record shows understanding of the full ITIL picture. The script for raising it is professionally pitched — non-accusatory, evidence-led, and it surfaces the metrics problem honestly. The closing observation about ticket undercount demonstrates thinking beyond the immediate task. Strong Competent.

---

*This completes the ICT30120 core unit guide series.*

*Note: BSBSUS211 (Participate in sustainable work practices) and BSBCRT301 (Develop and extend critical and creative thinking skills) are also core to ICT30120. See the BSB30120 pack for [BSBSUS211](../BSB30120/BSBSUS211-unit-guide.md) and [BSBCRT311](../BSB30120/BSBCRT311-unit-guide.md), which cover substantially the same competency at an adjacent level.*

*AIIPD RTO Training Resources | ICT30120 Certificate III in Information Technology | © Liam Michael Clancy / Philosophersknow 2026*
