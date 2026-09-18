---
title: Introducing Astra for Law | OpenAI
url: https://openai.com/index/astra-for-law/
site_name: hackernews_api
content_file: hackernews_api-introducing-astra-for-law-openai
fetched_at: '2026-09-19T06:00:22.700261'
original_url: https://openai.com/index/astra-for-law/
author: vertigoruntime
date: '2026-09-18'
description: OpenAI for Law brings frontier intelligence for law, custom firm workflows, connected legal data sources, and legal-grade controls for confidential client work.
tags:
- hackernews
- trending
---

OpenAI

September 17, 2026

Company

# Introducing Astra for Law

Our most powerful model, configured into a new AI foundation for law.

Explore solutions for law
Contact Legal sales
Loading…
Share

Today, we’re introducing Astra for Law: a new foundation for law firms and legal technology companies to build AI products and workflows around their expertise. It combines GPT‑6 Astra, our latest and most powerful model, with settings, tools, and context tailored for professional legal work.

API customers including Harvey and Legora will be able to build on Astra for Law, bringing this intelligence into their own products and workflows. As our frontier models advance, we’ll bring these legal capabilities to our latest models.

We are also expanding our work on privacy and governance to give law firms specific controls for confidential client work. Firms can also customize Astra for Law using our 26 new ecosystem plugins that connect ChatGPT to the specialist tools firms already use, like Relativity and Clio.

## Frontier intelligence for law

Astra for Law combines GPT‑6 Astra with a powerful legal search index and instructions for legal analysis and writing. Together, they amplify Astra’s capabilities across the legal practice, while giving firms and legal technology companies the freedom to build their own applications and workflows.

### Legal research: from facts to a supported answer

Our new legal search index is one of the tools Astra for Law can use. Legal research often begins with finding the exact right authority, locating the relevant passages, and understanding how relevant and binding they are to the situation at hand. The index helps Astra for Law do that work, and complements the licensed content and specialist products firms rely on from providers such as Thomson Reuters.

By using the legal search index, Astra for Law can search U.S. case law, statutes, regulations, court rules, and administrative decisions across a corpus of more than 230 million URLs, with sources added daily. Our work with Free Law Project, the nonprofit behind CourtListener, brings its case-law collection coveringmore than 99.9% of published U.S. precedential case law⁠(opens in a new window)into this research experience.

To measure how this configuration improves legal research, we tested Astra for Law’s complete setup on 200 U.S. legal research questions from the private validation set ofVals AI’s Legal Research Bench⁠(opens in a new window). This benchmark measures how well the model can find relevant sources and passages, and how well its research answers meet the evaluation criteria.

At the highest reasoning effort for both systems, Astra for Law passed the evaluation’s overall correctness check on 54.0% of questions, compared with 38.7% for GPT‑6 Astra using web search alone – a 40% relative improvement. Astra for Law also produces more comprehensive answers.

On case-law-focused questions, Astra for Law found 24% more reference cases than GPT‑6 Astra using web search alone at the highest reasoning effort. On the audited set of target passages, it retrieved up to 54% more relevant passages from the correct court opinions, when comparing the systems at the same reasoning effort.

The result is a stronger research foundation for advising on a deal, assessing a dispute, or developing a legal strategy, with reliable authorities the lawyer can examine for herself.

Astra for Law and GPT‑6 Astra’s performance on the Vals AI Legal Research Bench validation set, across reasoning effort settings.

### Improving performance on end-to-end legal workflows

Legal research is only the first step. Custom instructions for legal analysis and writing guide Astra for Law in applying that research to the client’s facts, developing arguments or deal terms, and identifying weaknesses and uncertainty. That can mean distinguishing a court’s holding from its other observations, addressing cases that weaken an argument, or explaining how a contract exception shifts risk between the parties.

For example, when prompted to identify good law with similar fact patterns, Astra for Law could both pinpoint relevant precedent and match fact patterns better than other frontier models:

Astra for Law will be initially offered to selected law firms through Trusted Access in ChatGPT and Codex, and will be coming soon to the API. It will appear in the model picker as “GPT‑6 Astra Law” and in the API as gpt-6-astra-law.

“
We were grateful to preview early versions of Astra for Law, which were built with legal use-cases in mind. Across both litigation and transactional matters, the models demonstrated impressive research depth and sensitivity to authority. Even at this early stage, they felt like a significant step toward legal-focused AI that is carefully grounded in research that is both current and comprehensive.
”
John Savva, Partner, 
Sullivan & Cromwell
“
In our early testing, Astra for Law showed strength across key aspects of legal research: grounding answers in on-point authorities, citing with precision, and offering practical, advisory guidance.
”
Niko Grupen, Head of Applied Research at Harvey
1 of 2
“
We were grateful to preview early versions of Astra for Law, which were built with legal use-cases in mind. Across both litigation and transactional matters, the models demonstrated impressive research depth and sensitivity to authority. Even at this early stage, they felt like a significant step toward legal-focused AI that is carefully grounded in research that is both current and comprehensive.
”
John Savva, Partner, 
Sullivan & Cromwell
“
In our early testing, Astra for Law showed strength across key aspects of legal research: grounding answers in on-point authorities, citing with precision, and offering practical, advisory guidance.
”
Niko Grupen, Head of Applied Research at Harvey
* Sullivan & Cromwell
* Harvey
* Sullivan & Cromwell
* Harvey

## Legal-grade trust and controls

Law firms need to protect client confidences and control how AI is used in their practice. We’ve created a special Trusted Access Program for eligible law firms to give lawyers and people working under their supervision access to Astra for Law for professional legal work. For eligible firms, the offering includes Zero Data Retention (ZDR) on our API, and usage of ChatGPT Enterprise is excluded from human review by default.

We are also working withLatham & Watkins, a leader in AI governance, to design for information permissions, ethical walls, client instructions, and firm oversight.

“
As AI becomes more capable, so too does the ability to deploy it in environments that demand rigorous governance, oversight, and accountability. This collaboration builds on 
Latham’s
 broader investments in AI development, governance, and infrastructure across the firm, which underpin our enterprise-wide strategy for responsible AI.
”
Michael Rubin, Chair of 
Latham’s
 AI Strategy Committee

## Build ChatGPT around your firm’s expertise

With frontier intelligence and the right controls, firms can turn their own precedents, methods, and judgment into AI tools and workflows built to their standards.

Working with selected firms, our forward-deployed engineers have been adapting ChatGPT Enterprise with custom interfaces and integrations to proprietary data, creating tools for each firm’s workflows:

* Sullivan & Cromwellbuilt an agreement analyzer that brings the firm’s negotiating playbooks and selected precedents into the review of a new deal. It helps lawyers spot risks that emerge when provisions are read together, then turns those findings into proposed redlines and draft client advice they can challenge and refine.
* Ropes & Graybuilt a deal diligence system around how its lawyers work through a data room and decide what matters to the deal. It helps them trace findings back to the source and pinpoint questions that could affect an acquisition, such as whether key customer contracts require notice or consent.
* Cooleybuilt GO Public to bring its capital markets expertise into how companies prepare to go public, from drafting the IPO filing to identifying the risks that deserve management’s attention. When the deal changes, it carries that change across the filing so lawyers can review the implications together.
1 of 3
“
Our collaboration with OpenAI has allowed us to rethink how this work gets done – moving lawyers and management teams more quickly through intensive preparation and into questions that require judgment, market experience and strategic thinking.
”
Dave Peinsipp, partner and co-chair of 
Cooley’s
 global capital markets group
“
AI is fundamentally transforming the way legal services are delivered, and 
Sullivan & Cromwell
 is committed to being at the forefront of that evolution. Our team is developing custom AI applications aligned with the way our lawyers work. OpenAI's world-class engineering expertise is helping us bring our vision to life through an initial test application. Our collaboration refined the application, enhanced its performance and prepared it for broad deployment. The experience demonstrated the value of purpose-built AI tools supported by a strong technology platform and shaped by our firm's standards. We are excited to continue exploring how such tools can enhance the way our lawyers work and help us deliver even greater value to our clients.
”
Robert Giuffra Jr. and Scott Miller, Co-Chairs, 
Sullivan & Cromwell
“
Our clients rely on us for judgment on the deals, disputes, and regulatory challenges that define their industries. We see an extraordinary opportunity in partnering with OpenAI on how its technology can enhance and elevate our capabilities. Together, we are shaping how frontier AI applies to the most demanding legal work, starting with transactional due diligence. Our goal is to put more of our lawyers' insight to work earlier in the process, so clients get faster execution, sharper analysis, and the industry-leading counsel they depend upon.
”
Ropes & Gray
* Cooley
* Sullivan & Cromwell
* Ropes & Gray
* Cooley
* Sullivan & Cromwell
* Ropes & Gray

Firms can build with their own teams and partner products, with permitted sources and review processes defined for the work.

## Frontier intelligence, connected to the most trusted tools in legal

We’re proud to work with the specialist companies who are advancing legal AI. Today, we’re launching26 partner-built plugins⁠that help firms go deeper with the tools and knowledge they already use. These plugins cover the practice and business of law. With iManage, a lawyer can draft a negotiation brief in ChatGPT and save it to the matter file; Intapp can surface activities that may need a time entry for review; DeepJudge can bring prior deals into a comparison. Thomson Reuters is bringing HighQ matter context into ChatGPT and previewing a forthcoming CoCounsel Legal connector.

“
As AI becomes more open and interoperable, the value is not in connectivity alone. Legal professionals need more than access to information. They need trusted intelligence, relevant enterprise and matter context, purpose built legal capabilities, and the governance required for high stakes work. That is what Thomson Reuters delivers through HighQ and CoCounsel Legal. CoCounsel remains the trusted professional AI system designed to help complete that work. Our work with OpenAI helps make these capabilities available in the environments customers choose, while preserving the accuracy, confidentiality, and accountability they depend on.
”
Joel Hron, Chief Technology Officer, Thomson Reuters

The launch includes 9 community plugins from lawyers and legal engineers at LegalQuants, LECG, and Skills.law, with 47 custom skills that practitioners can adapt, extend, or draw inspiration from to do their work in ChatGPT. Community plugins give the people closest to the work a way to keep setting the standard for what these skills can do. We’re also making ChatGPT for Word generally available today, so lawyers can proofread, get suggested edits, and flag formatting issues in the tool they already rely on for drafting.

Our approach is open and composable: firms can use specialist products, bring their own tools and knowledge, and adapt community-built skills to their practice. Partners can keep developing their own applications and workflows, while firms choose how those capabilities fit together. Building on OpenAI should mean getting more from the ecosystem, not replacing it.

## Build with us

OpenAI is investing in law for the long term. We’ll keep advancing Astra for Law’s model, settings, tools, and instructions together, guided by rigorous evaluations and feedback from lawyers and legal technology partners. We’ll also keep improving ChatGPT so firms can build around their expertise and connect the tools they use.

Our work withWachtell, Lipton, Rosen & Katzbrings the firm’s litigation and corporate expertise together with our frontier research and engineering to explore how AI can support the work involved in providing sophisticated legal judgment.

“
We’ve appreciated the technical depth and willingness to listen that OpenAI’s forward deployed engineering team has brought to our conversations about AI's role in supporting legal work, and are excited about the possibilities of AI to shape the next era of legal practice.
”
Wachtell, Lipton, Rosen & Katz

The most ambitious applications will come from the people who practice law and the companies building alongside them. We’re committed to working with this ecosystem so firms can bring their own expertise, standards, and judgment to AI—and serve clients in ways only they can.

To explore early access to Astra for Law, build it into your product, or develop tools around your firm’s expertise, contact OpenAI.

* 2026
* Legal
* ChatGPT

## Author

OpenAI

## Keep reading

View all
Paul Christiano joins OpenAI Foundation Board

CompanySep 9, 2026

The Work Now Within Reach

CompanySep 8, 2026

Supporting journalism from classrooms to newsrooms

CompanySep 8, 2026