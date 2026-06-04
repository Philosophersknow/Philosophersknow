# AIIPD Civic Intelligence™ — Onboarding UI Copy

**Purpose:** Every piece of UI copy for the onboarding flow, in intelligence framing. Covers progress indicators, step labels, field labels, helper text, confirmation messages, error messages, completion states, and next step prompts.

---

## PART 1: PROGRESS INDICATORS

### Overall Onboarding Progress Bar

**Label:** Intelligence Environment Setup
**Step progress format:** Step [n] of [n] — [Step Name]
**Completion label:** Your Intelligence Environment is Ready

**Example progression:**
- Step 1 of 5 — Welcome and Context
- Step 2 of 5 — Your Intelligence Profile
- Step 3 of 5 — Intelligence Focus
- Step 4 of 5 — Your Team
- Step 5 of 5 — Your Intelligence Environment

---

### Section Completion Indicators

**Not started:** Not yet configured
**In progress:** Configuring...
**Complete:** ✓ Intelligence configured
**Optional:** Optional — configure anytime

---

## PART 2: STEP LABELS

### Step 1: Welcome and Context
**Header:** Welcome to AIIPD Civic Intelligence™
**Subheader:** Let's set up your intelligence environment — it takes about 5 minutes.
**Body copy:** Your Civic Intelligence Centre will be configured for your role, your organisation, and your intelligence priorities. The more context you provide, the more relevant your intelligence experience from day one.

---

### Step 2: Your Intelligence Profile
**Header:** Tell us about your role
**Subheader:** This helps us surface the most relevant intelligence for your work.

---

### Step 3: Intelligence Focus
**Header:** Set your intelligence priorities
**Subheader:** Which intelligence dimensions matter most for your current work?

---

### Step 4: Your Team
**Header:** Invite your team
**Subheader:** Add colleagues who should have access to your organisation's intelligence environment.

---

### Step 5: Review and Confirm
**Header:** Your intelligence environment is almost ready
**Subheader:** Review your configuration before we finalise your Civic Intelligence Centre.

---

## PART 3: FIELD LABELS AND HELPER TEXT

### Step 2: Intelligence Profile Fields

**Field: Full name**
Label: Full name
Helper text: How you would like to be addressed in your intelligence environment.

**Field: Role title**
Label: Role title
Helper text: Your current role within your organisation. This helps us tailor your intelligence view.

**Field: Role type**
Label: I am primarily a...
Options:
- Local Government CEO or General Manager
- Executive Director or Director
- Mayor or Elected Member
- Strategic Planner or Policy Analyst
- Infrastructure or Engineering Professional
- Finance or Corporate Services Professional
- Community Services Professional
- Management Consultant or Advisor
- Academic Researcher
- Community Organisation Leader
- State Government Officer
- Other

Helper text: Select the role type that most closely matches your primary professional function.

**Field: Primary organisation**
Label: Primary organisation
Helper text: The organisation this intelligence environment is configured for. Usually your employer or your primary client organisation.

**Field: Organisation type**
Label: Organisation type
Options:
- Local government (metropolitan)
- Local government (regional)
- Local government (rural)
- Local government (remote)
- State government agency
- Management consulting firm
- Research institution
- Community organisation
- Infrastructure or planning firm
- Investment or funding body
- Other

Helper text: Select the type that best describes your primary organisation.

---

### Step 3: Intelligence Focus Fields

**Field: Intelligence priorities**
Label: Select your top intelligence priorities (choose up to 3)
Options:
- Governance Intelligence — understanding governance structures, decision patterns, and organisational health
- Financial Intelligence — financial sustainability, trajectory, and comparative financial position
- Community Intelligence — demographic, social, and community conditions
- Infrastructure Intelligence — asset condition, investment patterns, and infrastructure gap analysis
- Strategic Foresight — emerging trends, risks, and opportunities
- Comparative Place Intelligence — learning from comparable organisations
- Emerging Risk Intelligence — identifying developing risks before they escalate
- Regional Intelligence — cross-jurisdictional and regional patterns

Helper text: Your selected priorities will determine which intelligence dimensions are most prominently featured in your Civic Intelligence Centre. You can adjust these at any time.

**Field: Primary intelligence question**
Label: What is your most important intelligence question right now? (Optional)
Helper text: For example: "What are the emerging risks for [Organisation Name] in the next three years?" or "How does our infrastructure investment compare to similar councils?" Your Intelligence Partner will use this to ensure your environment is configured to address it.
Placeholder: Describe your current intelligence priority in plain language...
Character limit note: Up to 300 characters

**Field: Upcoming decisions**
Label: What major decisions is your organisation facing in the next 12 months? (Optional)
Helper text: This helps us surface the most relevant intelligence immediately. Examples: strategic planning cycle, major capital investment decision, community strategic plan development, governance review.
Placeholder: E.g., "Annual strategic planning cycle beginning next quarter" or "Infrastructure investment decision for [asset type]"

---

### Step 4: Team Fields

**Field: Invite team members**
Label: Invite colleagues to your intelligence environment
Helper text: Enter email addresses for colleagues who should have access. You can assign different access levels to different team members.

**Field: Email address**
Label: Email address
Helper text: Colleagues will receive an invitation to create their AIIPD account and access your organisation's intelligence environment.

**Field: Access level**
Label: Access level
Options:
- Intelligence Viewer — can view all intelligence outputs, cannot generate new briefs
- Intelligence User — can view and generate intelligence outputs
- Intelligence Administrator — full access, including configuration and team management

Helper text: Select the appropriate level for this team member's role and intelligence needs. You can adjust access levels at any time.

**Field: Add message (optional)**
Label: Personal message to include in invitation (optional)
Helper text: Add a brief context note to help your colleagues understand what AIIPD is and why they are being invited.
Placeholder: E.g., "I've set us up with AIIPD's civic intelligence platform — it will give us the evidence base we need for our planning work."

---

### Step 5: Review and Confirm Fields

**Section: Review intelligence environment configuration**
Label: Your Civic Intelligence Centre configuration
Helper text: Review the details below before confirming. You can edit any configuration at any time after setup.

**Review item: Primary organisation**
Label: Primary organisation
Edit link: Edit

**Review item: Your role**
Label: Your role profile
Edit link: Edit

**Review item: Intelligence focus**
Label: Intelligence priorities
Edit link: Edit

**Review item: Team access**
Label: Team invitations
Edit link: Edit

**Confirm button:** Confirm and Activate My Intelligence Environment

---

## PART 4: CONFIRMATION MESSAGES

### Step 2 Completion
**Title:** Role profile saved
**Message:** Your intelligence profile has been configured. Your Civic Intelligence Centre will prioritise intelligence relevant to your role as [Role Type].

### Step 3 Completion
**Title:** Intelligence focus confirmed
**Message:** Your intelligence priorities have been noted. [Organisation Name]'s Civic Intelligence Centre will feature [selected priority 1], [selected priority 2], and [selected priority 3] prominently in your view.

### Step 4 Completion — Invitations Sent
**Title:** Team invitations sent
**Message:** [n] invitation(s) have been sent to your colleagues. They will receive an email from intelligence@aiipd.com.au with instructions for creating their account and accessing your organisation's intelligence environment.

### Final Confirmation
**Title:** Your Intelligence Environment is Active
**Message:** Your AIIPD Civic Intelligence Centre for [Organisation Name] is now configured and ready. Your first intelligence output — a Council Intelligence Profile — has been queued for generation and will be available within [timeframe]. Your Intelligence Partner, [Partner Name], will be in contact within one business day to schedule your Intelligence Briefing.

**[Enter Your Intelligence Centre]**

---

## PART 5: ERROR MESSAGES

### Form Validation Errors

**Required field empty:**
*Field-level:* This field is required to configure your intelligence environment.

**Invalid email format:**
*Field-level:* Please enter a valid email address. This is needed to send your colleague an access invitation.

**Duplicate email:**
*Field-level:* This email address has already been added to your team invitations.

**Organisation not found:**
*Field-level:* We could not find an organisation matching that name. Please try a different spelling, or contact your AIIPD Intelligence Partner if your organisation is not yet in our system.

---

### System Errors

**Configuration save failure:**
*Title:* Configuration could not be saved
*Message:* We were unable to save your intelligence environment configuration. Your progress has been preserved. Please try again, or contact your AIIPD Intelligence Partner at intelligence@aiipd.com.au if the issue continues.
*Action button:* Try again

**Invitation send failure:**
*Title:* Invitations could not be sent
*Message:* We were unable to send invitations to [email address(es)]. Please check the addresses and try again. Invitations can also be resent from your Team Management settings after onboarding.
*Action button:* Try again | Continue without sending

**Session timeout during onboarding:**
*Title:* Your session has timed out
*Message:* For your security, your session has ended due to inactivity. Your configuration progress has been saved. Please log in again to continue your setup.
*Action button:* Return to login

---

## PART 6: COMPLETION STATES

### Onboarding Complete State

**Headline:** Welcome to Your Civic Intelligence Centre

**Body:**
Your AIIPD Civic Intelligence™ environment for [Organisation Name] is now active.

Your intelligence priorities are set. Your team has been invited. Your first intelligence brief is being generated.

Here is where to start:

**[Review Your Intelligence Summary]** — Your current intelligence picture across all dimensions for [Organisation Name].

**[Open Your Council Intelligence Profile]** — Your comprehensive, synthesised intelligence portrait. Available in [timeframe].

**[Explore Comparative Intelligence]** — See how your context relates to comparable organisations.

**Intelligence Partner:** [Partner Name] will be in touch within one business day. You can also reach them directly at [partner@aiipd.com.au].

---

### Individual Brief Generation Complete State

**Headline:** Your Intelligence Brief is ready

**Body:** Your [Brief Type] for [Organisation / Topic] has been generated and is now available in your Intelligence Library.

**[Open Intelligence Brief]**

*Generated: [Date and time] | Intelligence period: [Period] | Evidence dimensions: [n]*

---

### Invitation Accepted State

**Headline:** Welcome to [Organisation Name]'s Intelligence Environment

**Body:** You have accepted [Inviting User Name]'s invitation to access AIIPD Civic Intelligence™ for [Organisation Name]. Complete your Intelligence Profile to configure your experience, or explore the Civic Intelligence Centre directly.

**[Complete My Intelligence Profile]** | **[Go to Intelligence Centre]**

---

## PART 7: NEXT STEP PROMPTS

### After Step 2 Complete
> **Next:** Set your intelligence priorities — so your Civic Intelligence Centre surfaces what matters most for your work.
> **[Continue to Intelligence Focus →]**

### After Step 3 Complete
> **Next:** Invite your team — your colleagues can access intelligence relevant to their roles.
> **[Continue to Team Setup →]**
> *or*
> **[Skip for now — I'll add team members later]**

### After Step 4 Complete
> **Next:** Review your configuration and activate your intelligence environment.
> **[Continue to Review →]**

### After Onboarding — In-Platform
> **Suggested next action:** Review your Intelligence Summary to see your current intelligence picture.
> **[View Intelligence Summary]**

### 24 Hours After First Login — Notification Prompt
> **Intelligence Partner check-in:** [Partner Name] from AIIPD will be in contact today to schedule your Intelligence Briefing. In the meantime, your Council Intelligence Profile is available in Intelligence Briefs.
> **[View Intelligence Briefs]**

### 7 Days After First Login — Engagement Prompt
> **Intelligence tip:** Have you explored Comparative Place Intelligence? See how comparable organisations approach challenges similar to yours — without rankings, just contextual learning.
> **[Explore Comparative Intelligence]**

### 14 Days After First Login — Deepening Prompt
> **Generate a specialist brief:** Now that you've explored your core intelligence, try generating a specialist brief — Governance Intelligence Review, Financial Intelligence Review, or Strategic Foresight Report. Select from Intelligence Briefs → Generate New Brief.
> **[Generate a Brief]**

### 30 Days After First Login — Review Prompt
> **30-day intelligence review:** It's been 30 days since you set up your intelligence environment. Your Intelligence Partner [Partner Name] would like to schedule a brief check-in to review what you've found and discuss your intelligence needs for the coming quarter.
> **[Schedule a Review]**

---

*Last updated: June 2026 | AIIPD Civic Intelligence™ Onboarding UI Copy v1.0*
