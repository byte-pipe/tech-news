---
title: AI Coding Assistants Haven’t Sped up Delivery Because Coding Was Never the Bottleneck - InfoQ
url: https://www.infoq.com/news/2026/03/agoda-ai-code-bottleneck/
site_name: tldr
content_file: tldr-ai-coding-assistants-havent-sped-up-delivery-becau
fetched_at: '2026-03-28T01:01:33.464615'
original_url: https://www.infoq.com/news/2026/03/agoda-ai-code-bottleneck/
date: '2026-03-28'
description: Agoda recently published an observation arguing that while AI coding tools have measurably raised individual developer output, the resulting velocity gains at the project level have been surprisingly
tags:
- tldr
---

InfoQ HomepageNewsAI Coding Assistants Haven’t Sped up Delivery Because Coding Was Never the Bottleneck

 Architecture & Design
 

QCon San Francisco (Nov 16-20): Deep technical sessions. Peer conversations that change how you think. 

# AI Coding Assistants Haven’t Sped up Delivery Because Coding Was Never the Bottleneck

Mar 24, 20262
									min read

by

* Eran Stiller

#### Write for InfoQ

Feed your curiosity.

Help 550k+ global 
senior developers 
each month stay ahead.
Get in touch

Agoda recently published an observation arguing that while AI coding tools have measurably raised individual developer output,the resulting velocity gains at the project level have been surprisingly modest, because coding was never the real bottleneck. The post claims that the bottleneck has shifted upstream to specification and verification because these areas require human judgment. This shift carries significant implications for how engineering teams should be structured.

Leonardo Stern, a software engineer at Agoda, frames this as a rediscovery of Fred Brooks' decades-old argument in "No Silver Bullet" that improvements in speed to only one part of the development lifecycle produce diminishing returns for overall delivery.

The observation aligns with industry-wide data:research by Faros AIanalyzing telemetry from over 10,000 developers across 1,255 teams found that teams with high AI adoption completed 21% more tasks and merged 98% more pull requests, yet PR review time increased by 91%. This metric is consistent with the diagnosis that acceleration at the coding stage relocates pressure elsewhere.

For Stern, the more important implication is what this shift means for team structure. The traditional rationale for small, focused engineering teams was partly built on the assumption that coding was the most significant value-creating activity and that communication was overhead that impeded it.

If the highest-value work becomes collaborative specification and architectural alignment, that logic inverts: communication is no longer the cost to minimize, it is the work itself. Smaller teams win not because they reduce coordination but because they achieve shared understanding faster. Five people can genuinely align around intent and corner cases in ways that fifteen typically cannot.

The shift in software engineering key deliverables from coding to specification and verification (source)

Stern introduces a three-stance taxonomy for how engineers can relate to AI-generated code. The "white box" model, where humans read and review every line, does not scale when agents can produce thousands of lines per hour. "Black box" or "vibe coding", shipping whatever the AI generates with minimal verification, is fast but brittle for production systems serving large user bases.

Stern's preferred middle path, which he calls "grey box," keeps humans accountable at the two points that matter: writing specifications precise enough for the agent to execute correctly, and verifying results against evidence rather than inspecting the implementation line by line. Crucially, he is explicit that accountability does not shift to the AI: the engineer who guides the agent and approves the merge request remains fully responsible for what ships.

This reframing of the review from code inspection to evidence evaluation echoes the architectural formalism in Leigh Griffin and Ray Carroll's recent InfoQ article onSpec-Driven Development. In this article, they argue that specifications should become the executable source of truth for a system, with generated code treated as a downstream, regenerable artifact.

Human authority is migrating from writing code to defining and governing intent (source)

Stern arrives at a compatible conclusion from a workflow perspective: a high-fidelity specification with testable acceptance criteria, explicit corner cases, and captured architectural decisions becomes the primary engineering deliverable, with implementation increasingly delegated. Both pieces converge on the observation that human authority is migrating upward in the abstraction stack — from writing code to defining and governing intent.

 

## About the Author

 

 

 

#### Eran Stiller

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theSpec Driven Developmenttopic

##### Related Topics:

* Development
* Architecture & Design
* Software Development Lifecycle
* Spec Driven Development
* AI Assisted Coding

* #### Related Editorial
* #### Related Sponsors
* #### Related SponsorMay 12, 2026, 1:30 PM EDT##### Designing Data Layers for Agentic AI: Patterns for State, Memory, and Coordination at ScalePresented by: Karthik Ranganathan - Co-CEO & Co-Founder at YugabyteDB, and Aditi Gupta - Snr. GenAI/ML Specialist Solutions Architect
* May 12, 2026, 1:30 PM EDT##### Designing Data Layers for Agentic AI: Patterns for State, Memory, and Coordination at ScalePresented by: Karthik Ranganathan - Co-CEO & Co-Founder at YugabyteDB, and Aditi Gupta - Snr. GenAI/ML Specialist Solutions Architect

### Related Content

### The InfoQNewsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.View an example

Enter your e-mail address

Select your country

Select a country

I consent to InfoQ.com handling my data as explained in this 
Privacy Notice
.

We protect your privacy.