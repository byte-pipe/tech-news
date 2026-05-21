---
title: AI can write code, but the CIOs still owns the operating model | CIO
url: https://www.cio.com/article/4173269/ai-can-write-code-but-the-cios-still-owns-the-operating-model.html
site_name: tldr
content_file: tldr-ai-can-write-code-but-the-cios-still-owns-the-oper
fetched_at: '2026-05-21T19:36:34.238449'
original_url: https://www.cio.com/article/4173269/ai-can-write-code-but-the-cios-still-owns-the-operating-model.html
date: '2026-05-21'
description: Employees are adopting AI fast, but CIOs still need to manage the operating model so quick productivity gains don't turn into risky shadow IT.
tags:
- tldr
---

by									
Thai Vong

Contributor

# AI can write code, but the CIOs still owns the operating model

Opinion

May 20, 2026
8 mins
 

## Employees are adopting AI fast, but CIOs still need to manage the operating model so quick productivity gains don't turn into risky shadow IT.

 

							Credit: 															
Andrea Zanenga

AI is moving into the enterprise faster than most organizations are prepared for it. What began as experimentation with chat interfaces and narrow use cases is now showing up in real workflows, productivity tools and early agentic capabilities that are becoming part of how work gets done.

That shift is creating a new challenge for CIOs.

The question is no longer whether the business wants AI. It is how the enterprise is going to govern what the business is already using.

I am seeing the same pattern repeat across organizations. Business teams are drawn to speed, convenience and immediate productivity gains. Employees are finding their own ways to summarize meetings, draft communications, analyze data, generate code and automate workflows on their own. From their perspective, AI feels like acceleration. From IT’s perspective, it can look like a more visible version of shadow IT.

That tension is real. IT can easily be cast as the function slowing everything down. In practice, CIOs are often the ones looking across the full risk picture, including cybersecurity exposure, data leakage, identity controls, auditability, workflow approvals and accountability when AI moves from suggestion to action. That is why the operating model still matters. Governance is part of it, but the bigger issue is deciding how AI enters the enterprise, how decisions get made, who owns outcomes and where accountability sits. Once AI starts influencing workflows, decisions and shared data, the conversation has to expand beyond the tool itself. It becomes a broader enterprise question about how AI is introduced, where accountability sits and how the usual concerns around security and risk are applied when the technology is more visible and moving more quickly than most other tools.

## The harder challenge is bringing AI into the enterprise without losing control.

Most organizations no longer need to be convinced that AI matters. The harder problem is bringing it into the enterprise without losing control.

The shift becomes more practical once AI moves beyond individual productivity and into business processes. A tool that helps summarize a meeting is not the same as a tool that reviews a dashboard and recommends a decision. A tool that pulls approved data for reporting is not the same as one that moves files, triggers downstream tasks or approves an exception.

That is where the risk profile starts to change.

In my experience, the real challenge is deciding which use cases can move quickly and which ones require tighter control. If everything is forced through a heavyweight architecture review, the business may look for other ways to move forward outside of IT. If everything is waved through because it looks lightweight, risk accumulates quietly until it becomes an operational problem.

The excitement is real, and so is the pressure to move fast. But enterprise readiness is not determined by how quickly a tool can be turned on. It is determined by whether the organization understands what the tool touches, what it can influence and who is accountable when it fails.

## Governance has to move faster without losing control.

Many governance models fail because they are too rigid for the speed of modern technology adoption. AI will expose that weakness faster than almost anything else.

That does not mean governance should be relaxed. It means governance has to become practical enough to keep up with how AI is actually being used.NIST’s AI Risk Management Frameworkis useful here because it treats AI risk management as an organizational discipline, not a one-time control exercise.

The first step is to evaluate AI use cases by what they can do, not just what they are called. I look at three questions. What data can the tool access? What action can it take? What is the consequence if it gets it wrong?

If an AI capability is only reading approved information and helping a user retrieve or summarize it, that is one level of criticality. If it is drafting content that a human reviews before release, that is another. If it is making recommendations tied to audits, financial controls, customer commitments or regulated activity, the bar needs to rise quickly. And if it can move files, trigger workflow changes, approve transactions or interact with production environments, it should be treated very differently.

The difference becomes even clearer in practical cases. Hosting shared dashboards in a managed cloud environment is not the same as allowing an AI agent built on a personal desktop to connect to enterprise data and take action. One is a managed environment that can be governed through identity, access, logging and platform controls. The other may begin as individual experimentation, but it quickly becomes an enterprise issue if it touches flawed or inconsistent data, workflow approvals or operational decisions, because bad data can lead to the wrong action being taken at scale.

This is where human-in-the-loop design still matters. Critical decisions, approvals and exceptions should not quietly drift into automation simply because the tool is capable of doing it. Someone still needs to be accountable for the decision, the audit trail and the outcome.

The same is true for core controls, where identity and access controls, logging, endpoint protection and data retention still matter. AI does not replace those disciplines. It makes them more important. That matters even more as AI starts to move beyond prompts and into action.OWASP’s guidance on agentic AIhighlights emerging threats tied to autonomous workflows and multi-step actions, which is one reason governance cannot stop at the prompt layer.

Security teams are right to ask hard questions. Verizon’s2025 Data Breach Investigations Reportanalyzed 12,195 confirmed breaches, the highest number the report has analyzed in a single year. That does not mean every AI tool creates breach conditions on its own. It does mean the enterprise environment is already high risk, and the same acceleration that makes these tools useful to enterprises also makes them easier for attackers to exploit, which is why organizations have to be more intentional in how they apply security and risk controls as these tools become more widely used.

The right response is not to say no, but to move with the right level of control.

Low-criticality use cases should move through a lightweight path with basic security, privacy and architecture review. Higher-risk use cases should require deeper review, tighter controls and explicit ownership. The goal is not bureaucracy, but to create enough structure to prevent avoidable risk, reduce the need for mitigation later and keep AI decisions from becoming ad hoc.

## AI demand needs structure, not just policy.

Most AI governance discussions stall because they stay theoretical. Policy alone will not solve this. Organizations need a practical way to evaluate AI demand before it scales.

In my experience, putting a cross-functional steering structure in place early is one of the most effective ways to govern AI demand because it creates shared accountability around decisions that go well beyond technology. Those mechanisms do not define the operating model on their own, but they are what make it actionable. They help distinguish low-risk productivity gains from higher-risk use cases that touch sensitive data, workflows or approvals.

That structure matters because not every AI request deserves the same treatment. A team asking to use AI to draft internal notes does not need the same level of review as a team asking for an agent to review contracts, approve exceptions or move documents across shared environments. The first can often move quickly with guardrails. The second requires tighter review, clearer ownership and stronger controls before it gets anywhere near production.

The intake process also needs to do more than register business demand. It needs to classify requests early. Is this a personal productivity use case, a workflow support use case or an agentic use case that can initiate or influence action? What systems or data does it touch? Is the output advisory, operational or decision-shaping? Who owns it after launch? How will it be monitored? Those questions create discipline before scale creates problems.

Just as important, the process should not end at approval. Every production use case should have a named owner, clear boundaries, logging, periodic review and a defined path for escalation when behavior drifts or risk changes. Models evolve, users adapt and business reliance grows over time. A use case that starts as low-risk can become high-impact faster than many organizations expect.

That is one reason this cannot be treated as a technology experiment alone. It has to be governed as part of the enterprise operating model.

The organizations that get this right will not stand out for moving first. They will stand out for bringing AI into the enterprise with control, clarity and accountability. That is why I believe the operating model is still the real differentiator. CIOs still decide whether AI enters the enterprise with discipline or drifts in without control.

This article is published as part of the Foundry Expert Contributor Network.Want to join?

Artificial Intelligence
Software Development
IT Governance
IT Leadership
 

 

				SUBSCRIBE TO OUR NEWSLETTER			

### From our editors straight to your inbox

				Get started by entering your email address below.			

 

Please enter a valid email address

Subscribe

 

														by 															

																Thai Vong															

Contributor

1. Follow Thai Vong on LinkedIn

Thai Vongis a CIO recognized for leading enterprise technology transformation, innovation and large-scale modernization. He was named Global CIO of the Year by the ORBIE Awards and selected as a Titan 100 honoree for his leadership in advancing technology-driven business strategy.With more than 20 years of experience, Thai has led global technology organizations across public companies and private equity-backed enterprises, guiding digital transformation, complex technology integrations and enterprise platform modernization. His experience spans industries including supply chain, financial services and life sciences. Thai frequently shares insights on artificial intelligence, innovation and the evolving role of the CIO in helping organizations scale technology, navigate complexity and unlock long-term business value.

## More from this author

* opinion### Why a modern data foundation takes more than a new platformMay 7, 20269 mins
* opinion### Why M&A technology integrations are harder than expected. Here’s what you should look for earlyMar 13, 20269 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

brandpost
 
Sponsored by CyberNewsWire
 

### Tribal Raises $10M to Make Enterprise AI Production-Ready

 
By Cyber NewsWire
May 21, 2026
4 mins

Artificial Intelligence
Security

opinion
 
 

### Reflections on RSAC and the Mythos of agents

 
By Rick Grinnell
May 21, 2026
5 mins

Data and Information Security
Markets
Technology Industry

feature
 
 

### CIOs should beware the AI confidence trap

 
By Grant Gross
May 21, 2026
6 mins

Artificial Intelligence
ROI and Metrics

podcast
 
 

### The Hardest Part of Digital Transformation Is Not the Technology - BizLink Tech Group CIO's Perspective

 
By Estelle Quek
18 May 2026
38 mins

CIO
Digital Transformation
Manufacturing Industry

podcast
 
 

### Building to Last - How Standard Chartered's Group CIO Balances Bold Innovation with Uncompromising Resilience

 
By Estelle Quek
11 May 2026
30 mins

Banking
Financial Services Industry
Generative AI

podcast
 
 

### CIO Leadership Live ASEAN with Sandeep Shahi, VP IT FEDEX APAC

 
6 May 2026
42 mins

Data Integration
Digital Transformation
Transportation and Logistics Industry

video
 
 

### Watch Revenium track AI costs, hidden spending, and ROI in real time

 
May 20, 2026
12 mins

Budget
CFO
CIO

video
 
 

### The Hardest Part of Digital Transformation Is Not the Technology - BizLink Tech Group CIO's Perspective

 
By Estelle Quek
18 May 2026
38 mins

CIO
Digital Transformation
Manufacturing Industry

video
 
 

### Deploy a secure branch network in under 2 minutes, using Cisco Unified Branch

 
May 12, 2026
10 mins

Artificial Intelligence
Networking
Networking Devices