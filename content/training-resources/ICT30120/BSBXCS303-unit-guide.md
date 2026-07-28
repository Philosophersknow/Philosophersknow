# BSBXCS303 — Securely Manage Personally Identifiable Information and Workplace Information
## Complete Student Assessment Guide

**Unit Code:** BSBXCS303
**Unit Title:** Securely manage personally identifiable information and workplace information
**Training Package:** BSB Business Services (imported into ICT qualifications)
**Qualification:** ICT30120 Certificate III in Information Technology (CORE unit)
**AIIPD Resource Pack — Student Edition**

---

## What This Unit Is About

Almost every organisation holds information that would cause harm if it escaped — customer records, employee files, financial data, health information, commercial plans. IT workers have privileged access to nearly all of it.

BSBXCS303 sits alongside ICTICT313 but has a different emphasis. Where ICTICT313 covers the *legal and ethical framework*, this unit covers the *practical security behaviours*: how you classify information, how you store and transmit it, how you control who reaches it, and what you do when it leaks.

---

## What Counts as Personally Identifiable Information

**Personally Identifiable Information (PII)** is information that identifies, or could reasonably identify, an individual.

### Direct identifiers
Information that identifies a person on its own:
- Full name
- Address
- Email address
- Phone number
- Tax File Number, Medicare number, driver licence number, passport number
- Photograph or video of an identifiable person
- Biometric data (fingerprint, face template, voiceprint)

### Indirect identifiers
Information that identifies a person **in combination**:
- Date of birth
- Postcode
- Gender
- Job title
- IP address, device ID, cookie ID
- Transaction records

**The combination problem:** Date of birth alone identifies nobody. Date of birth + postcode + gender identifies a surprisingly large proportion of the population uniquely. Treating indirect identifiers as harmless because "it's not a name" is a common and serious misjudgement.

### Sensitive information — a higher category

Under the Privacy Act 1988 (Cth), **sensitive information** attracts stronger protection and generally requires consent to collect:

- Health information (including genetic and biometric)
- Racial or ethnic origin
- Political opinions or association membership
- Religious beliefs or affiliations
- Philosophical beliefs
- Trade union membership
- Sexual orientation or practices
- Criminal record

A breach involving sensitive information is far more likely to constitute "serious harm" and trigger mandatory notification.

---

## Information Classification

Organisations classify information so that handling requirements are proportionate to sensitivity. A typical scheme:

| Classification | Meaning | Examples | Handling |
|---|---|---|---|
| **Public** | Approved for release | Published marketing, annual reports, public website | No restriction |
| **Internal** | For staff generally | Internal newsletters, org charts, general procedures | Not for external release |
| **Confidential** | Restricted to those with a business need | Customer records, contracts, financial data, employee records | Access controlled; encrypted in transit; not on personal devices |
| **Restricted / Highly Confidential** | Severe harm if disclosed | Health records, security credentials, unreleased financials, litigation material | Strict access control; encryption at rest and in transit; audit logging; often approval required per access |

**Your obligations:** Know your organisation's scheme. Apply the classification when you create a document. Handle information according to its classification, not according to how sensitive it feels to you.

---

## Access Control

### The Principle of Least Privilege

Users, systems, and processes should have **only the minimum access required** to perform their function — and no more.

Applied properly this means:
- A receptionist does not have access to payroll
- A developer does not have standing access to the production database
- An IT administrator has a **separate** privileged account, used only for administrative tasks, distinct from their day-to-day account

**Why the separate admin account matters:** If an administrator browses the web and reads email on an account with domain admin rights, a single phishing click compromises the entire environment. Separating privileges limits blast radius.

### Role-Based Access Control (RBAC)

Access is granted to **roles**, and users are assigned roles — rather than permissions being granted to individuals ad hoc.

**Why RBAC is better than individual grants:**
- Consistent — everyone in a role has the same access
- Auditable — you can answer "who can see payroll?" by listing the role
- Maintainable — when someone changes jobs, you change their role, not thirty individual permissions

### Privilege Creep

**Privilege creep** occurs when a person accumulates access over time as they change roles, without old access being removed. After five years and three role changes, an employee may hold access to systems from every position they have ever held.

**Controls:**
- Remove old access at the point of role change, not "later"
- Conduct periodic **access reviews** — managers confirm that each person's access is still appropriate
- Automate deprovisioning where possible

### Onboarding and Offboarding

**Offboarding is the higher risk.** A departing employee — particularly one leaving involuntarily — with retained access is a serious threat.

**Offboarding checklist:**
- [ ] Disable (do not immediately delete) the user account at the agreed time
- [ ] Revoke VPN and remote access
- [ ] Revoke MFA tokens and registered devices
- [ ] Revoke access to SaaS applications (often missed — these sit outside the domain)
- [ ] Recover and wipe company devices
- [ ] Recover physical access cards and keys
- [ ] Change any **shared** credentials the person knew
- [ ] Transfer ownership of files, mailboxes, and any systems they administered
- [ ] Review recent activity for unusual data access or bulk downloads

**Why disable rather than delete:** Deleting immediately can destroy audit trails and orphan data. Disable, then delete on a defined schedule after data has been transferred.

---

## Protecting Information in Practice

### Passwords and Authentication

**Current guidance favours length over complexity theatre.** A long passphrase is stronger and more usable than a short string with forced substitutions.

| Practice | Guidance |
|---|---|
| **Length** | Longer is better — a passphrase of four or more unrelated words substantially outperforms an eight-character complex password |
| **Uniqueness** | Never reuse passwords across systems. Credential-stuffing attacks exploit reuse directly |
| **Password managers** | Recommended. They enable unique, long, random passwords per site without memorisation |
| **Forced rotation** | Modern guidance discourages routine forced expiry for user accounts — it drives predictable patterns (Summer2025!, Summer2026!). Rotate on suspicion of compromise |
| **Never** | Share accounts, write credentials on notes, email or message credentials, or store them in plain-text files |

### Multi-Factor Authentication (MFA)

MFA requires two or more of:
- **Something you know** — password, PIN
- **Something you have** — authenticator app, hardware key, smartcard
- **Something you are** — fingerprint, face

**MFA is the single most effective control against credential compromise.** It defeats most phishing and virtually all credential stuffing.

**Not all MFA is equal:**
- **SMS codes** — better than nothing, but vulnerable to SIM swapping and interception
- **Authenticator apps (TOTP)** — good; codes generated on-device
- **Push notifications** — good, but vulnerable to **MFA fatigue attacks**, where an attacker spams approval prompts until the user taps "approve" to make it stop. Number matching mitigates this
- **Hardware security keys (FIDO2/WebAuthn)** — strongest; resistant to phishing because the key verifies the site's identity

### Encryption

| Type | What It Protects | Examples |
|---|---|---|
| **Encryption at rest** | Data stored on a device or server — protects against theft of the physical media | BitLocker, FileVault, encrypted database columns, encrypted backups |
| **Encryption in transit** | Data moving across a network — protects against interception | HTTPS/TLS, SFTP, VPN, encrypted email |

**Practical requirements:**
- Full-disk encryption on all laptops and mobile devices — a stolen unencrypted laptop is a data breach
- Never transmit confidential information over unencrypted channels (plain HTTP, unencrypted FTP, SMS)
- Verify HTTPS before entering credentials
- Encrypted backups — an unencrypted backup tape or drive is as sensitive as the live system

### Physical Security

Digital controls are defeated by physical access:

- **Lock your screen** whenever you leave your desk (Win+L / Ctrl+Cmd+Q). An unlocked, unattended workstation is an open door with your identity attached
- **Clear desk** — do not leave confidential documents, notes, or removable media visible
- **Secure disposal** — shred paper containing PII; do not put it in general recycling
- **Device disposal** — drives must be securely wiped or physically destroyed before disposal. Deleting files does not remove data
- **Server rooms and comms cabinets** — locked, access logged
- **Visitors** — escorted; not left alone with systems
- **Tailgating** — do not hold a secure door for someone you do not recognise, however awkward it feels

### Removable Media and BYOD

- USB drives are a major vector for both **data exfiltration** and **malware introduction**
- Never plug in a USB device of unknown origin — "found" USB drives are a genuine attack technique
- Where removable media is used for confidential data, it must be encrypted
- **Bring Your Own Device (BYOD):** personal devices accessing company data must meet minimum standards — screen lock, encryption, current OS, remote wipe capability. Confidential data should not be stored locally on personal devices

### Working Remotely and in Public

- Use the corporate VPN on untrusted networks
- Treat public Wi-Fi as hostile
- **Shoulder surfing** is real — be aware of who can see your screen on public transport, in cafés, on planes. Privacy screens help
- Do not discuss confidential matters on calls in public spaces
- Do not leave devices unattended in vehicles or public areas

---

## Email, Messaging, and Human Error

**The largest single cause of reportable data breaches in Australia is not hacking — it is human error, and the most common form is sending information to the wrong recipient.**

### Reducing send errors

- **Check the recipient before sending**, especially where autocomplete has filled the address. Autocomplete confusing two similar names is the classic mechanism
- **Use BCC** when emailing a group of external recipients. Putting a hundred customer addresses in the To field discloses every address to every recipient — a reportable breach in its own right
- **Check attachments** — confirm you have attached the right file, and that the file does not contain more than intended (hidden columns and rows, other worksheet tabs, tracked changes, document metadata)
- **Delay-send** — a one to two minute outbound delay lets you recall genuine mistakes
- **Do not forward chains** containing information the new recipient should not see

### Phishing Recognition

| Indicator | Detail |
|---|---|
| **Urgency and threat** | "Your account will be closed in 24 hours" — pressure suppresses scrutiny |
| **Unexpected attachment or link** | Particularly invoices, delivery notices, and shared documents you were not expecting |
| **Mismatched sender** | Display name says the CEO; the actual address is a free mail domain or a lookalike |
| **Lookalike domains** | `micros0ft.com`, `company-invoices.com`, `rnicrosoft.com` (rn reads as m) |
| **Requests for credentials** | Legitimate IT will not email asking for your password |
| **Payment or bank detail changes** | **Business Email Compromise** — always verify by a known phone number, never by replying to the email or calling a number in it |
| **Unusual language or tone** | Especially a request from a senior person that bypasses normal process |

**If you suspect phishing:** Do not click, do not reply, do not open attachments. Report it through the organisation's reporting mechanism. If you have already clicked or entered credentials, report it **immediately** — speed of response dramatically reduces harm, and no one is punished for reporting fast.

---

## Data Retention and Disposal

Holding data forever is a liability, not an asset. Under **APP 11.2**, personal information must be destroyed or de-identified when it is no longer needed for the purpose for which it was collected — unless law requires retention.

**Competing obligations:**
- Tax and financial records typically require retention for a defined period (commonly 5–7 years)
- Employment records have their own retention requirements
- Some industry-specific legislation mandates longer retention

**Practical position:** Follow the organisation's documented **data retention schedule**. Do not delete on your own initiative, and do not hoard "just in case." Both are failures.

**Secure disposal methods:**

| Medium | Method |
|---|---|
| Paper | Cross-cut shredding or secure destruction bin |
| Hard drives (magnetic) | Multi-pass overwrite, degaussing, or physical destruction |
| SSD / flash | Cryptographic erase or physical destruction (overwriting is unreliable on SSDs due to wear levelling) |
| Cloud data | Deletion through the provider's process, confirming backup and replica removal |
| Mobile devices | Factory reset with encryption enabled, or remote wipe |

---

## Responding to a Data Breach

### Recognising a breach

A data breach is unauthorised access to, unauthorised disclosure of, or loss of personal information. It includes:
- Emailing information to the wrong person
- A lost or stolen unencrypted laptop, phone, or USB drive
- A misconfigured system exposing data publicly
- Ransomware or unauthorised system access
- A paper file left in a public place
- An employee accessing records without a business reason

**Note that most of these are not attacks.** Most breaches are mistakes.

### The four-step response

**1. Contain**
Stop the breach continuing. Recall the email, disable the compromised account, take the exposed system offline, retrieve the document. Do not destroy evidence.

**2. Assess**
What information was involved? How many people? Who now has access? What is the risk of serious harm — identity theft, financial loss, physical safety, humiliation, reputational damage?

**3. Notify**
Under the **Notifiable Data Breaches (NDB) scheme**, if a breach is likely to result in **serious harm** and cannot be remediated, the organisation must notify:
- The **Office of the Australian Information Commissioner (OAIC)**, and
- The **affected individuals**

Assessment must be completed **within 30 days** of becoming aware of a suspected eligible breach.

**4. Review**
What allowed this to happen? What control failed or was absent? Fix the underlying cause, not just the instance.

### Your personal obligation

**Report immediately.** Do not attempt to assess seriousness yourself, and do not attempt to fix it quietly and say nothing.

Concealment turns a manageable incident into a serious one:
- The 30-day assessment clock runs from when the *organisation* became aware — delay burns the window
- Containment options narrow rapidly with time
- Concealment is itself a disciplinary and potentially legal matter

**A culture where people report mistakes immediately is safer than one where people are punished for making them.** If your organisation punishes reporting, that is a governance failure worth naming.

---

## Evidence Checklist — BSBXCS303

**Knowledge Evidence**
- [ ] Definition of PII with at least 5 direct and 5 indirect identifiers
- [ ] Explanation of the "combination problem" with indirect identifiers
- [ ] Identification of at least 6 categories of sensitive information under the Privacy Act
- [ ] Description of an information classification scheme with at least 4 levels and handling requirements
- [ ] Explanation of the principle of least privilege and why administrators need separate privileged accounts
- [ ] Explanation of RBAC and its advantages over individual permission grants
- [ ] Explanation of privilege creep and at least 2 controls for it
- [ ] Description of an offboarding checklist with at least 6 items
- [ ] Explanation of the difference between encryption at rest and in transit with examples
- [ ] Comparison of at least 3 MFA methods including their weaknesses
- [ ] Identification of at least 6 phishing indicators
- [ ] Explanation of Business Email Compromise and the correct verification method
- [ ] Explanation of APP 11.2 retention obligations and the tension with legal retention requirements
- [ ] Identification of secure disposal methods for at least 4 media types
- [ ] Description of the four-step data breach response
- [ ] Explanation of the NDB scheme — threshold, who is notified, and the assessment timeframe

**Performance Evidence**
- [ ] Classification: classify a set of described documents and state the handling requirements for each
- [ ] Access review: given a described employee's role history, identify privilege creep and recommend removals
- [ ] Offboarding: complete an offboarding checklist for a described departure
- [ ] Phishing: review provided sample emails and identify which are phishing, with reasoning
- [ ] Breach response: describe your response to a described breach scenario, including notification assessment
- [ ] Secure handling: describe how you would transmit a confidential file to an external party

---

## Worked Example

**Prompt:**

*You work in IT support at a community health service with 200 staff. At 4:40pm on a Friday, a payroll officer comes to you visibly distressed. She was emailing the fortnightly payroll summary to the finance manager. She typed "Dave" in the To field, autocomplete selected the wrong Dave, and she has sent it to a Dave who is an external contractor with an outside email address.*

*The attached spreadsheet contains, for all 200 staff: full name, employee number, date of birth, home address, bank account BSB and number, tax file number, gross and net pay, and superannuation fund details.*

*She sent it eleven minutes ago. She has not told anyone else. She asks you whether you can "just delete it from his inbox and we can forget about it."*

*Describe your response.*

---

**Exemplary Response:**

This is a serious data breach and it must be reported. It cannot be quietly deleted and forgotten, and I need to tell her that clearly while she is already distressed.

---

**First — the immediate human response.**

She has made a mistake that anyone could make. Autocomplete selecting the wrong contact is one of the most common causes of reportable breaches in Australia. She came to me straight away, which is exactly the right thing to have done and materially improves the outcome.

I would say so: *"You did the right thing coming straight here — eleven minutes is fast and that genuinely helps. But I can't just delete it and leave it there. This one has to be reported, and I'll help you do that right now."*

Being straight with her is kinder than being vague. She needs to know what is going to happen.

---

**Second — containment, immediately and in parallel.**

Time matters, so I would act while we talk:

1. **Attempt recall/retraction.** If we use Microsoft 365 or Google Workspace, message recall only works reliably **internally**. Dave is external, so recall will almost certainly fail — but it costs nothing to attempt.

2. **Escalate to whoever can act on the mail gateway.** If the message is still queued in the outbound gateway, it may be stoppable. Eleven minutes makes this unlikely but not impossible. This may be above my authority — if so, I escalate immediately rather than experimenting.

3. **Preserve evidence.** Do not delete the sent item, the log entries, or anything else. We need the full record: exact send time, exact recipient address, exact attachment. Deleting anything now looks like concealment and destroys the assessment basis.

4. **Contact Dave — but carefully, and not on my own initiative.** He needs to be asked to delete the email and attachment without forwarding, opening, or retaining it, and to confirm deletion in writing. This should come from someone with authority, and by **phone to a known number** rather than by replying to the email thread. His cooperation is helpful but it is not a fix — we cannot verify deletion, he may have already opened it, it may be on a phone, in a backup, or synced to another device.

---

**Third — escalate. This is the non-negotiable part.**

I do not own this decision. I would immediately notify:
- My IT manager
- The organisation's **Privacy Officer** (a health service will have one)
- The payroll officer's manager

I would do this before I go home. A Friday afternoon breach does not become a Monday morning breach because it is inconvenient.

---

**Why "just delete it and forget about it" is not available:**

**The data is about as bad as it gets.** TFN, bank BSB and account number, date of birth, full name, and home address is a complete identity theft and financial fraud package for 200 people. An attacker with this could open accounts, redirect salary payments, or lodge fraudulent tax returns.

**This will almost certainly meet the "serious harm" threshold** under the Notifiable Data Breaches scheme. The combination of TFN and bank details makes financial harm plausible rather than theoretical.

**We cannot verify remediation.** The NDB scheme allows an organisation to avoid notification if it takes remedial action such that serious harm is *no longer likely*. Dave saying "I deleted it" is not verification — we have no control over his mailbox, his backups, his devices, or whether he forwarded it in the eleven minutes before we called. A health service is not in a position to claim the risk has been eliminated.

**The 30-day clock has started.** The organisation must complete its assessment within 30 days of becoming aware of a suspected eligible breach. Concealing it does not stop the clock; it burns it.

**Concealment is worse than the breach.** The original error is a mistake. Deliberately hiding a notifiable breach involving 200 people's TFNs and bank details is misconduct, and it exposes both her and me. I am not going to participate in that, and I would not want her to either — it converts her worst-case outcome from "made a mistake" to "concealed a breach."

---

**Fourth — what happens next (so she knows):**

The Privacy Officer will lead an assessment: what was disclosed, to whom, how many people, and what harm is likely. On these facts I would expect the outcome to be:

- **Notification to the OAIC**
- **Notification to all 200 affected staff**, with practical advice — contact their bank, consider the ATO's process for a compromised TFN, watch for unusual account activity, and consider a credit report ban
- Possible engagement with **IDCARE**, Australia's national identity support service, which organisations commonly refer affected individuals to

---

**Fifth — the review, which is where I have most to contribute.**

The underlying question is not "why did she type the wrong name." It is **why a spreadsheet containing 200 unencrypted TFNs and bank accounts could be attached to an ordinary email at all.**

Controls I would raise:

| Control | Effect |
|---|---|
| **Data Loss Prevention (DLP)** | Rules that detect TFN and bank account patterns and block or quarantine external sends. This alone would have stopped it |
| **External recipient warning** | Banner or confirmation prompt when a message with attachments goes outside the organisation |
| **Outbound send delay** | One to two minutes would have made recall genuinely possible |
| **Encrypted transfer instead of email** | Payroll data should move via a secure portal or encrypted file transfer, not as an email attachment |
| **Minimise the payload** | Does the finance manager need TFNs and full bank details, or only names and net amounts? Least-privilege applies to data content, not just system access |
| **Visually distinct external contacts** | Address book display that makes internal vs external obvious at a glance |

The genuine fix is DLP plus not emailing this data at all. Retraining one person does not prevent the next person making the same autocomplete error — and they will.

---

**In one line:** contain what we can, preserve everything, escalate immediately to the Privacy Officer, support her through it, and then fix the system that allowed a spreadsheet of 200 TFNs to be one autocomplete error away from leaving the building.

**Examiner Annotation:** Outstanding. The student handles the human dimension without letting it compromise the obligation — acknowledging that fast reporting genuinely helps, while being clear that concealment is not available. Containment actions are correct and correctly qualified: recall is attempted but the student knows it does not work externally, and evidence preservation is explicitly protected. The refusal is well reasoned rather than merely rule-citing: the student explains *why* TFN plus bank details plus DOB plus address crosses the serious harm threshold, and correctly identifies that unverifiable third-party deletion does not constitute remedial action under the NDB scheme. Escalation is to the right roles and happens before the student leaves. The follow-up detail (IDCARE, TFN compromise process, credit bans) is practical and accurate. Most impressively, the review section reframes the root cause correctly — the failure is the ability to attach that payload to an ordinary email, not the typo — and the proposed controls are ranked with DLP and data minimisation ahead of retraining. This is professional information security practice. Strong Competent.

---

*Next: ICTICT323 — Align work practices with the ICT industry environment*

*AIIPD RTO Training Resources | ICT30120 Certificate III in Information Technology | © Liam Michael Clancy / Philosophersknow 2026*
