# ICT30120 & CUA31120 — Assessment Example Bank
## Certificate III in Information Technology · Certificate III in Screen and Media

**AIIPD RTO Training Resources — Student Edition**

Four additional worked examples beyond those in the unit guides. Write your own answer before reading the responses.

---

## Example 1 — ICT: Suspected Compromise

**Units: BSBXCS303, ICTICT313, ICTSAS305**

### The Prompt

*You work on the IT help desk at a 200-person legal firm. At 4:10pm a paralegal, Nadia, calls. She says she received an email that looked like it came from the firm's document management system asking her to re-authenticate. She entered her username and password on the page it linked to. About ten minutes later she noticed the page "looked a bit off" and became worried.*

*She says: "I've probably overreacted, haven't I? Please don't make a big thing of it, I feel like an idiot."*

*What do you do?*

---

### Exemplary Response

She has not overreacted. She has almost certainly entered her credentials into a phishing site, and she has done exactly the right thing by reporting it within ten minutes.

**The first thing I say:**

*"Nadia, you haven't overreacted at all — and telling me straight away is genuinely the best thing you could have done. These are designed to fool people; that's the whole point of them. Let me take some details and get this locked down, and I'll keep you posted."*

**Why the tone matters, practically:**

She is embarrassed and asking me to minimise it. **If I make her feel worse, the next person this happens to will not call** — they will hope it goes away, and the organisation will find out days later instead of minutes later.

**Speed of reporting is the single biggest factor in limiting harm from credential phishing.** Ten minutes is an excellent outcome and I want to reinforce that behaviour, not punish it.

But I also cannot do what she asked and keep it quiet. I would be honest about that:

*"I do have to report it — not because you've done anything wrong, but because we need to check whether the account's been used. That's standard and it's not going to come back on you."*

---

**Containment — immediately, while I am still on the phone:**

**1. Reset her password.** Straight away. This is the single most effective action and it takes seconds.

**2. Revoke active sessions and tokens.** A password reset alone does not terminate sessions an attacker may already have established. Sign-out-everywhere or session revocation is needed.

**3. Re-register MFA.** If MFA is in place, the attacker may have captured a one-time code, or may have prompted her for one. If there is any possibility MFA was compromised — particularly if she approved a push notification — the MFA registration should be reset.

**4. Ask the questions that determine scope:**
- **What exactly did she enter?** Username and password only, or an MFA code as well?
- **Did she approve any push notification** on her phone afterwards? MFA fatigue attacks rely on the user approving a prompt to make it stop
- **Does she use that password anywhere else** — personal accounts, other systems? Credential stuffing across services is the standard follow-on attack
- **Has anything unusual happened since?** Unexpected prompts, emails disappearing, forwarding rules she did not set
- **Can she forward me the original email**, or send it as an attachment, without clicking anything further

**5. Escalate immediately** — to my supervisor and to whoever holds the security incident role. This is not something I close out on the help desk.

---

**Investigation — what needs checking:**

This is beyond my level to conduct, but I would flag what needs looking at so the escalation is useful:

- **Sign-in logs** for her account — any successful authentication from an unexpected location, IP or device between the time she entered credentials and the reset
- **Mailbox rules** — attackers commonly create hidden forwarding or deletion rules immediately after compromise, so that replies to fraudulent emails are hidden from the user. This is a very common and easily missed step
- **Sent items** — has anything been sent from her account?
- **Anything accessed** in the document management system
- **Whether other staff received the same email** — a phishing campaign is rarely sent to one person. Others may have entered credentials and not reported it

---

**Why this matters more at a law firm:**

The firm holds **client confidential and legally privileged material**. A compromised paralegal account potentially exposes:
- Client files and privileged communications
- Personal information of clients — likely including **sensitive information** under the Privacy Act
- Trust account and financial information

There is also a specific and well-documented attack pattern here: **conveyancing and settlement fraud**, where an attacker with mailbox access monitors correspondence and, at the right moment, sends altered bank details for a settlement payment. Law firms are targeted for this specifically, and the amounts are large.

**This raises the stakes considerably beyond a routine password reset.**

---

**Notifiable Data Breaches:**

If it is established that an unauthorised party accessed personal information, the firm must assess whether the breach is likely to result in **serious harm** and, if so, notify the **OAIC** and the affected individuals. The assessment must be completed **within 30 days** of becoming aware.

**That clock starts now**, which is another reason not to let this sit.

That assessment belongs to the firm's privacy officer, not to me. My job is to ensure they know today.

---

**What I do afterwards:**

**1. Warn everyone.** If a phishing campaign is targeting the firm, a short, non-alarming notice to all staff describing the email and asking anyone who entered credentials to contact IT immediately — **explicitly stating that nobody will be in trouble for reporting.** That last clause is what determines whether anyone comes forward.

**2. Block the phishing URL** at the mail gateway and web filter, and search the mail system for other recipients.

**3. Follow up with Nadia.** Let her know what happened and that it was handled. She will be anxious about it.

**4. Raise the systemic questions:**
- Is MFA enforced on all accounts? Phishing-resistant MFA such as FIDO2 security keys defeats this attack entirely
- Are external emails clearly banner-marked?
- Is there phishing awareness training, and is it recent?
- Can the mail gateway detect lookalike domains better?

**The individual failure is a person being fooled by something designed to fool people. The systemic question is why the email reached her inbox at all.**

---

### Insufficient Response

I would reassure Nadia that it happens to everyone and reset her password for her. I would tell her to keep an eye out for anything unusual on her account and to let me know if she notices anything. I would suggest she doesn't click on links in emails in future. I'd make a note on the ticket in case it comes up again.

---

### Examiner Annotation

**NYC.** The response is kind and contains one correct action surrounded by omissions that would allow a serious breach to proceed.

- **Password reset alone is insufficient.** Active sessions and tokens are not terminated by a password change. An attacker already authenticated remains authenticated
- **No escalation.** A suspected credential compromise at a law firm is closed out on the help desk. This is the central failure
- **No investigation triggered** — no sign-in log review, no mailbox rule check, no sent items check. **Malicious mailbox rules are the single most common post-compromise action and would go undetected entirely**
- **"Keep an eye out for anything unusual"** — the compromise indicators are specifically designed not to be visible to the user, which is why hidden forwarding rules are used
- **No scoping questions.** Whether she entered an MFA code, whether she approved a push, whether the password is reused elsewhere — all determine the severity and none are asked
- **No consideration that others received the same email**
- **No privacy or NDB awareness.** Personal and sensitive client information may have been accessed and the 30-day assessment clock has started
- **"Don't click on links in future"** places the remedy entirely on the user, which is both unhelpful and inaccurate — the email defeated the technical controls before it reached her
- **No systemic follow-up**

The response treats a probable security incident as a password reset ticket. The tone toward Nadia is good and worth preserving; everything after it is inadequate.

---

## Example 2 — ICT: Being Asked to Exceed Authorisation

**Units: ICTICT313, BSBXCS303, ICTICT323**

### The Prompt

*You are a junior systems administrator. A senior manager, Rob, approaches you directly. He tells you that one of his team members, Yusuf, is suspected of sending confidential pricing information to a competitor. Rob asks you to "pull up Yusuf's email and have a look through it, and check what he's been putting on USB drives — keep it between us for now, we don't want to tip him off."*

*You have technical access to do both.*

*What do you do?*

---

### Exemplary Response

**I do not do this.** Having the technical ability to access something is not the same as having authorisation to access it, and this request would put me personally at risk while achieving nothing usable for the organisation.

---

**Why I decline:**

**1. Authorised access does not mean unlimited access.**

My administrative privileges exist so I can maintain systems. They do not authorise me to read an employee's email because a manager asked me to.

Under the **Cybercrime Act 2001 (Cth)** and equivalent state provisions, accessing data **without authorisation** is an offence — and authorisation is defined by what I am permitted to access for my role, not by what my credentials technically allow. A verbal request from a manager who is not the authorising authority does not create authorisation.

**2. Privacy obligations.**

Yusuf's mailbox contains personal information — his and other people's. Accessing and disclosing it outside the purpose for which it was collected engages the **Australian Privacy Principles**, particularly APP 6 (use and disclosure) and APP 11 (security).

**3. "Keep it between us" is the clearest warning sign in the request.**

A legitimate workplace investigation is **documented and authorised**. It goes through HR, it typically involves legal advice, and there is a written authorisation trail.

A request to conduct covert surveillance of an employee, off the record, with no documentation, is not a legitimate investigation — regardless of whether the underlying suspicion is well founded.

**4. Surveillance legislation.**

Several Australian jurisdictions regulate workplace surveillance, including requirements for **notice** to employees that computer and email surveillance may occur, and in some cases requirements around covert surveillance which may need external authorisation.

**[VERIFY: Workplace surveillance legislation varies significantly by state — NSW and the ACT have specific workplace surveillance Acts with notice requirements. Confirm the position in your jurisdiction and check the organisation's own surveillance policy and employment contracts.]**

**5. Evidentiary value — the practical argument.**

Even setting aside the legal problems: **if Yusuf is doing what Rob suspects, an unauthorised undocumented trawl through his mailbox by a junior admin will likely destroy the organisation's ability to act on it.**

Evidence obtained improperly may be inadmissible in a Fair Work proceeding, may expose the employer to an adverse action or privacy claim, and hands Yusuf a procedural fairness argument that could defeat an otherwise sound dismissal.

**Doing this badly is worse for the company than not doing it at all** — and that argument frequently persuades a manager where the legal one does not.

**6. My own exposure.**

I would be the person who accessed the mailbox. Not Rob. If this becomes a legal matter, "a manager asked me to" is not a defence to unauthorised access, and my employment and potentially my liberty are attached to it.

---

**What I actually say to Rob:**

I would not be confrontational. His concern may be entirely genuine and serious.

*"Rob, I understand why you're worried and that sounds like a serious issue. But I can't access someone's mailbox on a verbal request — I'd be exceeding my authorisation and there are privacy and surveillance rules around it. It also risks wrecking the case if it turns out you're right, because evidence gathered this way can be challenged.*

*The right path is through HR — if they authorise an investigation in writing, with legal input, I can action whatever they properly direct. Do you want me to help you raise it with them, or would you rather do that directly?"*

**That does four things:** declines clearly, gives the legal reason, gives the practical reason that protects his interest, and offers a route to what he actually wants.

---

**What I do next:**

**1. Document the request.** Date, time, exactly what was asked, my response. **Contemporaneous notes.** If this becomes contested later, or if Rob asks someone else and it goes ahead, I need a record that I was asked and declined.

**2. Escalate to my manager.** This is the part that requires some thought, because Rob is senior to me and I am effectively reporting a request from him.

I would frame it as seeking guidance rather than making an allegation:

*"I had a request from Rob to access an employee's mailbox as part of a suspected data leak. I told him it needed to go through HR with proper authorisation. Wanted to flag it with you in case it comes back around, and to check I handled it the way you'd want."*

**That is honest, it protects me, and it gets the issue to someone who can deal with it properly.**

**3. Do not warn Yusuf.** It is not my role, I do not know whether the suspicion is founded, and doing so could itself be a serious problem. My role is to decline and escalate, not to intervene on either side.

**4. Check whether the organisation has a proper process.** If there is no documented procedure for authorising access to an employee's data during an investigation, that is a genuine gap — because this will happen again, and the next person asked may not decline.

---

**If Rob pressures me or goes over my head:**

I hold the position. If a properly authorised written direction comes through HR with legal sign-off, I will action whatever is lawfully directed within my role. Without that, no.

If I were pressured to the point of being threatened with consequences for refusing, that is itself something to escalate — potentially to HR directly, and I would ensure my documentation is complete.

---

### Insufficient Response

I would tell Rob that I'm not comfortable doing this without approval, and suggest he speaks to my manager first. If my manager approves it then I would go ahead and check the emails and USB logs, since it would then be authorised. I wouldn't mention it to Yusuf.

---

### Examiner Annotation

**Borderline NYC.** The student declines the immediate request, which is correct, and then misidentifies what authorisation requires.

- **"If my manager approves it then I would go ahead"** — the IT manager is not the authorising authority for accessing an employee's personal communications in a disciplinary investigation. That requires **HR authorisation, typically with legal input and a documented basis**, and may engage workplace surveillance legislation. A verbal or informal approval from a technical manager does not cure the problem
- **No legal framework identified.** No reference to unauthorised access provisions, privacy principles, or surveillance legislation. The student's objection is framed as personal discomfort — *"I'm not comfortable"* — rather than as a legal position. **Discomfort is negotiable; illegality is not**, and a manager under pressure will push back against the first far more readily than the second
- **"Keep it between us" is not recognised as a warning sign**
- **No documentation** of the request or the response
- **No consideration of evidentiary consequences** — that improperly obtained evidence may be unusable and may expose the employer
- **No recognition of personal liability** — the student would be the one performing the access

The instinct to escalate is right. The failure is treating escalation as a formality that converts an improper request into a proper one, rather than understanding what makes it improper in the first place.

---

## Example 3 — CUA: Consent and Vulnerable Contributors

**Units: CUAIND312, CUAPPR311, CUAIND311**

### The Prompt

*You are working as a camera assistant on a documentary about homelessness. The director wants to film an interview with a man, Trent, who is currently sleeping rough and who has agreed to talk on camera. Trent appears to be affected by alcohol. The director hands him a release form and asks you to "just get him to sign that."*

*Trent signs it without reading it and says "yeah whatever, do what you want."*

*What do you do?*

---

### Exemplary Response

**That signature is not valid consent and I would say so.** I would not simply hand the form back and carry on.

---

**Why the consent is defective:**

Valid consent requires the person to be **informed**, to have **capacity** at the time they give it, and to give it **voluntarily**.

**Capacity is the immediate problem.** Trent appears affected by alcohol. A person whose judgement is impaired cannot give informed consent to a significant decision, and appearing in a documentary about homelessness is a significant decision with lasting consequences.

**He has not been informed.** He signed without reading, and nobody explained it to him. "Just get him to sign that" is a request to obtain a signature, which is not the same as obtaining consent.

**"Do what you want" is not consent — it is disengagement.** It signals someone who does not care what happens to him, which in these circumstances is a reason for more care, not less.

---

**Why this matters more than a paperwork problem:**

**The consequences fall on Trent, not on the production.**

- The footage may be broadcast and online **permanently**. Content does not expire
- He may be identifiable to family who do not know his situation, to former employers, to people he owes money to, or to people he is avoiding
- His circumstances may change substantially. **A man who is sleeping rough today may be housed and working in two years, applying for jobs while a documentary of him intoxicated and homeless remains searchable under his name**
- He may become a recognisable figure in a way he never anticipated
- There is a real risk of **exploitation** — a production obtaining compelling material from someone who lacks the capacity to weigh what he is giving up

**A release form signed under these circumstances is also legally weak.** If challenged, a court or broadcaster's legal review would look at capacity and informed consent, and this would not survive scrutiny. **The production is exposed as well as Trent** — a broadcaster's E&O insurance and legal clearance process may reject the material outright.

---

**What I actually do:**

**1. Raise it with the director now, before filming.**

Not afterwards, not by refusing to hand over the form silently. Directly and non-confrontationally:

*"I don't think that signature's going to stand up — he's had a drink and he hasn't read it. If this ends up in a broadcast clearance we're going to have a problem, and I don't think it's fair on him either. Can we come back to him another time when he's sober and go through it properly?"*

**I lead with the production risk as well as the ethical point.** A director under schedule pressure responds to both, and the two point the same way here.

**2. Propose what proper consent would look like:**

- **Return when he is not affected** and can genuinely engage
- **Explain the release verbally and simply** — what the film is, where it may be shown, that it may be online permanently, that people who know him may see it
- **Explain his right to withdraw** and by when — and mean it
- Offer to **let him see the footage** or the cut before it is finalised, if the production can accommodate it
- Consider whether a **support person or a caseworker** from a relevant service should be present
- Ensure he is not being induced by payment in a way that overrides his judgement

**3. Consider whether identification is necessary at all.**

Documentary practice offers options: **blurring, silhouette, voice alteration, using a first name only, or using an actor to voice a transcript.** If his story is what matters rather than his identifiability, there may be a way to tell it that carries far less risk to him.

**Raising that is a genuinely constructive contribution** rather than simply objecting.

**4. Escalate if the director proceeds anyway.**

I am a camera assistant, not the producer, and this is above my authority to decide. But it is not above my responsibility to raise.

If the director insists, I would raise it with the **producer**, who carries responsibility for clearances, legal risk and the production's ethical conduct. I would do that respectfully rather than dramatically, but I would do it.

**5. Document my own position.** A note of what I raised, to whom, and when. If this becomes a problem later I want a record that I identified it.

---

**The professional judgement:**

This industry runs on relationships and reputation, and as a camera assistant I am the most junior person present. Raising an objection to a director's instruction is not comfortable.

But **the person with the least power in this situation is Trent**, and everyone else present has a stake in the footage being obtained. If nobody in the crew raises it, nobody raises it.

**The documentary sector's credibility rests on the proposition that people who agree to appear understood what they were agreeing to.** A film about homelessness that exploits a homeless man to make itself has undermined its own subject.

---

### Insufficient Response

I would hand the form back to the director since Trent has signed it and that's what was asked. It's the director's decision who to film and I'm just the camera assistant. If I had concerns I might mention it quietly afterwards, but the release is signed so legally we're covered and it's not really my call.

---

### Examiner Annotation

**NYC.** The response treats a signature as consent and defers entirely on the basis of seniority.

- **"The release is signed so legally we're covered"** — factually wrong. A signature obtained from a person who appears intoxicated, who did not read the document and had it not explained, is precisely the consent that fails when tested. The production is **not** covered
- **Capacity is never mentioned.** The core issue is not identified at all
- **"Do what you want" is treated as agreement** rather than as an indicator of disengagement warranting more care
- **No consideration of consequences for Trent** — permanence, identifiability, changed future circumstances
- **"Not really my call"** — the decision is the producer's, but raising a concern is within anyone's role and is the entire point of the scenario. Junior status is a reason to raise it carefully, not a reason to stay silent
- **"Mention it quietly afterwards"** — after the footage is obtained is too late to protect Trent, and it converts the concern into a complaint rather than an intervention
- **No alternatives proposed** — no anonymisation, no returning when sober, no support person
- **No documentation**

The response is a realistic account of how a junior crew member might actually behave, which is why it is the useful comparison. The unit exists to establish that "it's not my call" does not extend to a defective consent from a vulnerable contributor.

---

## Example 4 — CUA: Client Feedback That Would Damage the Work

**Units: CUAPPR311, CUAIND312, BSBCRT311**

### The Prompt

*You have produced a three-minute video for a not-for-profit that supports people recovering from serious injury. The video features three genuine participants telling their own stories. It has been approved at script and rough cut stage.*

*At fine cut, a new marketing manager joins the client team and sends the following feedback:*

> *"Great work but it's a bit slow and a bit sad. Can we cut all three stories down to about 20 seconds each, add some upbeat music throughout, and put in some stock footage of people running and laughing on a beach? We want it to feel positive and inspiring. Also can we lose the bit where the second guy cries — it's a bit much."*

*How do you respond?*

---

### Exemplary Response

**I would push back, with reasons, while taking the underlying concern seriously.** Simply complying would produce a worse video that fails the brief, and simply refusing would be unprofessional.

---

**First — understand what is actually being asked.**

The feedback contains a **symptom** ("it's slow and sad") and a set of **proposed solutions** (cut the stories, add music, add stock footage, remove the crying). These are different things, and the solutions may not be the right response to the symptom.

**Before responding I would want to know:**
- Has something changed about how this will be used — a different platform, a shorter slot, a different audience?
- Is "positive and inspiring" a new brief, or their reading of the existing one?
- Has this been seen by the people who approved the script and rough cut? **A new manager overriding two approved stages needs to be reconciled internally, not just with me**
- **Have the three participants seen it?**

**That last question matters most**, and I would raise it first.

---

**The concerns with the requested changes:**

**1. Cutting three personal stories to 20 seconds each.**

At 20 seconds a person can state a fact. They cannot tell a story. What would remain is three fragments that establish nothing and connect to nobody.

**The reason this video works — if it does — is that it gives people time.** Recovery from serious injury is not a 20-second subject, and treating it as one signals to the audience that the organisation does not take it seriously either.

**2. Stock footage of people running and laughing on a beach.**

This is the most damaging suggestion.

- **It is not these people.** Cutting from a genuine participant describing a real experience to generic stock footage of strangers is a visible dishonesty, and audiences read it instantly
- **It undercuts the participants** — the implicit message is that their actual lives were not compelling enough
- **It may be inaccurate and hurtful.** Some people recovering from serious injury will not run on a beach. Presenting that as the outcome of recovery misrepresents the organisation's work and may distress the people it serves
- It is the visual language of pharmaceutical advertising, and it will read as such

**3. Upbeat music throughout.**

Music that contradicts what a person is saying does not make the content feel positive — it makes it feel manipulated. The audience notices the mismatch even if they cannot articulate it, and it costs the piece its credibility.

**4. Removing the moment the participant becomes emotional.**

This is the one I would resist most.

**That moment is very likely the most powerful thing in the video.** It is the point at which an audience stops watching a communications piece and connects with a person. Removing it because it is "a bit much" removes the reason anyone would care.

**And there is an ethical dimension:** that participant chose to be honest on camera about something difficult. Cutting his most vulnerable moment because a client finds it uncomfortable is a poor way to treat someone who trusted the production with his story.

---

**Taking the concern seriously — because there may be a real problem underneath it.**

"A bit slow" may be legitimate feedback that I should act on. It is worth asking whether:
- The pacing genuinely sags somewhere and can be tightened without gutting the stories
- The opening takes too long to establish what the film is about
- There is a structural issue — perhaps the three stories should be interwoven rather than sequential
- The ending lacks resolution, which can make a piece feel heavier than it is

**"Sad" may be pointing at a real absence.** If the film shows difficulty without showing what the organisation actually does about it, the audience is left with the weight and no direction. **That is a legitimate note and it has a solution that is not stock footage** — a clearer articulation of what changed, what support was provided, and where each person is now.

---

**How I would respond — in writing, then a conversation:**

> Thanks for the notes — really useful, and I want to make sure we get this right.
>
> Before I make changes, can I check a couple of things? The script and rough cut were signed off by [names] — I want to make sure we're all aligned before we make substantial structural changes, rather than have this go back and forth.
>
> On the specific notes: I'd like to talk through a couple of them, because I think there's a way to get the "positive and inspiring" feel you're after without changes that I think would cost us the thing that makes the film work.
>
> **On pacing** — I agree it can be tighter. I think I can find 20–30 seconds without losing the stories, and I'd suggest we look at the opening particularly.
>
> **On the three stories** — cutting to 20 seconds each would leave us with fragments. What people respond to here is the detail and the time. I'd rather tighten within them than cut them down.
>
> **On stock footage** — I'd strongly advise against it. Cutting from someone's real story to generic footage of other people reads as inauthentic, and I think it would undercut the participants. If we want to lift the ending, I'd rather shoot or source something real — where they are now, what they're doing.
>
> **On the emotional moment** — I'd really like to keep this. I think it's the strongest moment in the film and the point where an audience genuinely connects. It's also the moment [participant] chose to share with us.
>
> **On tone** — I think what's missing might not be upbeat music but a clearer sense of what your organisation actually did. At the moment we see the difficulty and less of the response. That might be the real fix.
>
> Happy to talk it through — and one thing I should ask: have the three participants seen the current cut? I'd want them comfortable with any significant changes to how their stories are told.

---

**Why that response works:**

- **It concedes the legitimate note** (pacing) immediately, which establishes that I am not just defending my work
- **It reframes the underlying concern** into a solution that improves the film rather than damaging it
- **It gives reasons**, not preferences. "I don't like stock footage" is not an argument; "it reads as inauthentic and undercuts the participants" is
- **It flags the internal approval issue** so the client resolves it on their side
- **It raises the participants** — which is both the right thing and a point the client will find hard to dismiss

---

**If the client insists:**

They are paying, and beyond a point it is their call.

**But there are limits I would hold:**
- **I would not make changes that misrepresent the participants' experiences** or that they would object to. If significant changes are made to how someone's story is told, **they should be consulted** — that is a consent issue, not a creative one
- I would put my advice in writing so there is a record
- **I would want to be clear about credit.** If the finished film is substantially different from the work I would stand behind, I would raise whether my credit should reflect that

**Where the disagreement is purely creative, the client decides.** Where it involves how real people who trusted us are represented, that is not purely creative.

---

### Insufficient Response

I would make the changes as requested since the client knows their audience and it's their video. I'd cut the stories down to 20 seconds, add the upbeat music and source some stock footage that fits the brief. I'd let them know that the shorter version loses some of the emotional impact but that it's their call. The customer is always right and it's not worth losing a client over creative differences.

---

### Examiner Annotation

**NYC.** The response abandons professional judgement entirely and misidentifies what is at stake.

- **"The client knows their audience"** may be true, but the brief was approved at script and rough cut. A new manager reversing two signed-off stages is a client-side governance problem that the response does not surface, guaranteeing further rework
- **No reasons offered for anything.** The student mentions that impact will be lost but does not explain why, so the client has no basis to reconsider. **Flagging a concern without an argument is not advice**
- **The participants are never mentioned.** Three people told genuine stories about serious injury on the understanding they would be represented in a particular way. Cutting them to 20-second fragments and intercutting stock footage of strangers running on a beach materially changes that, and they are not consulted or considered
- **The stock footage issue is not identified** as an authenticity or accuracy problem — including that some people recovering from serious injury will not run on a beach
- **The legitimate note is not separated from the damaging ones.** "A bit slow" may be genuinely correct and actionable; the response treats all four notes as equivalent
- **No alternative offered.** The exemplary response identifies that the real fix may be showing what the organisation does — a solution that meets the client's actual concern
- **"The customer is always right"** — in a professional service, the client decides, but they are paying for expertise. Delivering only compliance is a failure to provide what was engaged

The response would keep the client comfortable and produce a worse film that serves neither the organisation nor the three people in it.

---

*AIIPD RTO Training Resources | ICT30120 · CUA31120 | © Liam Michael Clancy / Philosophersknow 2026*
