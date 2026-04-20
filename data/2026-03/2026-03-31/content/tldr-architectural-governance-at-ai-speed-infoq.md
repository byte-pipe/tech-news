---
title: Architectural Governance at AI Speed - InfoQ
url: https://www.infoq.com/articles/architectural-governance-ai-speed/
site_name: tldr
content_file: tldr-architectural-governance-at-ai-speed-infoq
fetched_at: '2026-03-31T01:01:40.861402'
original_url: https://www.infoq.com/articles/architectural-governance-ai-speed/
date: '2026-03-31'
description: Stop bottlenecking GenAI velocity with manual reviews. Learn how to use Event Modeling, ADRs, and OpenAPI as machine-enforceable intent to achieve architectural alignment at the speed of code.
tags:
- tldr
---

InfoQ HomepageArticlesArchitectural Governance at AI Speed

 Architecture & Design


QCon San Francisco (Nov 16-20): Deep technical sessions. Peer conversations that change how you think.

# Architectural Governance at AI Speed

Mar 26, 202615
									min read

by

* Kyle Howard
* Christian Johansen
* Dana Katzenelson
* Brian Rhoten
* Warren Gray

reviewed by

* Luca Mezzalira

#### Write for InfoQ

Feed your curiosity.

Help 550k+ global
senior developers
each month stay ahead.
Get in touch

### Key Takeaways

* The advent ofGenAIhas dramatically increased the pace at which code can be produced, making it difficult for traditional oversight patterns to keep pace.
* Waiting for human oversight puts organizations at a competitive disadvantage and slows innovation.
* When it is trivial for everyone to deliver code, maintaining architectural cohesion requires combining centralized decision-making with automated, decentralized governance.
* Teams can apply tools and techniques they already use to create machine-enforceable statements of architectural intent.Event Modeling,OpenAPI,Architectural Decision Records, andSpec Driven Developmentall produce content that can be enforced through automated oragenticmeans.
* Declarative architectural intent, combined with automated oversight, enables teams to move quickly and safely while aligning with architectural intent, without increasing cognitive load.

This article was written by participants of the
online InfoQ Certified Architect Program
. It represents the capstone of their work, reflecting the cohort's collective learnings on the intersection of AI and modern software architecture.

## Code is Now a Commodity, Alignment is Still Not

GenAI has slashed the effort required to produce code, and rapid prototyping is increasingly common. As a result, the software development lifecycle is now constrained by an organization's ability to bring ideas into alignment and maintain cohesion across the system.

Fig. 1. FromEduardo Da Silva, used with permission

Historically, organizations have relied on manual processes and human oversight to achieve architectural cohesion. Startups rely on key individuals to catch misalignment between architectural intent and implementation. Enterprise-level organizations attempt to maintain cohesion through change boards and proliferating ADRs and documentation. In both contexts, identifying misalignment is slow because it requires synchronous dependence on a central authority. In the startup case, development teams are stuck waiting for busy experts. In the enterprise case, they have to wait on review boards and sift through documented guidance with the hope that what they find has not become obsolete. GenAI exacerbates this by accelerating the production of work that’s subject to review. Where previously only developers were producing code over days or weeks, executives and product managers can nowvibe-codefunctional prototypes in minutes or hours. As a result, development teams are left with an impossible choice: be beholden to the pace of manual oversight at the cost of velocity, or push forward without knowing whether they are aligned.

Over time, these small pushes compound into architectural fragmentation, which the organization responds to with more process and stricter guidelines, which further increase the difficulty of releasing software in alignment. This is a vicious cycle that slows delivery and blunts innovation.

## Declarative Architecture, Decentralized Alignment

Scaling alignment in the GenAI era requires that organizations move beyond manual oversight toward automated guardrails that enable teams to make safe decisions autonomously. To this end, we propose a strategy ofdeclarative architectureto scale architectural governance.

Declarative architectureis the practice of distilling architectural decisions and constraints into machine-enforceable declarations of intent that enable safe independent action. Each declaration governs a bounded scope: a clearly defined context within which it has authority. Without that boundary, declarations become the same sprawling guidance they were meant to replace.

Declarative architecture is not about making better decisions. Instead, it focuses on making decisions impossible to ignore. Instead of tracking down and interpreting architectural documents or waiting on experts and review boards, a machine-readable declaration of intent makes the conformant path the path of least resistance. Validation of compliance stops being a function of awareness and memory, and is instead encoded into tools that meet developers where they already are: in their editors, their pipelines, their code review tools. Machine-readability is not a technical nicety in this framework: it is the core requirement. A declaration that can only be understood by a human still depends on that human being in the loop. Only a declaration that machines can reason over can scale governance beyond the bandwidth of any individual or review board. In the following sections, we examine practical applications of declarative architecture distilled from event models, OpenAPI specifications, and ADRs.

## Event Models as Declarative Architecture

AnEvent Modeldescribes how information flows through a system, and is typically produced through collaborative modeling exercise.

Fig. 2. Event Model with a highlighted vertical slice (green rectangle). Each slice is a self-contained unit of behavior with its own command, event, and read model. Credit Adam Dymitruk Adaptech Group

The visual sticky notes on the canvas above are transcribed, one-to-one, into aneventmodel.jsonfile backed by aformal schema. Thiseventmodel.jsonforms the declared architecture of the system: a machine-readable map of architectural intent from which aligned implementations can be generated and against which agents can evaluate implementation.

Fig 3. From event model to generated code

### 1. Powering Automation

Vertical slices are bounded in scope and contain the declarations needed to describe a single unit of behavior. This minimal scope is what unlocks automation at every level. Code artifacts can be deterministically generated from the Event Model using code templates – no AI required. And because each slice is self-contained and code artifacts are also organised by slice (seevertical slice architecture), if something is wrong, you replace one slice rather than untangle a web of dependencies. (Contracts towards external dependencies still need to be honored, though). For what templates can't cover, the formal schema enables AI to go further. Martin Dilger from Nebulit has defined aClaude rule filethat analyses a code base and generates an Event Model from it. Domain experts can then review and refine the model through an AI Agent, enabling conversational programming at a higher abstraction level than code. Because the scope is minimal, both humans and AI can focus on one slice in isolation, dramatically reducing cognitive load. This same minimal scope is what makes the Ralph Loop (explained below) possible, turning each slice into an independent iteration target for an AI agent.

### 2. Decentralizing Architectural Alignment at Scale

Event Models enable decentralization, but only if the modeling itself is collaborative across team boundaries. If teams model independently in silos, each team's Event Model may be internally coherent while the product as a whole fragments. Organizations likeAdaptech GroupandNebulithave practiced multi-domain collaborative modeling covering many teams, demonstrating that this scales beyond a single team boundary. Technical alignment mechanisms likearchitecture.mdand OpenAPI validators (mentioned below) enforce how things are built, but cannot ensure teams are building the right thing together. That requires shared modeling on a broader scope, like Event Modeling or otherCollaborative Design techniques. The good news: technical governance frees human attention from policing implementation details, creating space for product-level alignment.

### 3. The Ralph Loop: From Slices to Shipping

TheRalph Wiggum Loopis one of several AI-looping techniques where an agent repeatedly attempts a task until completion criteria are met, restarting with fresh context each iteration to avoid degraded reasoning. In early iterations, using anarchitect in the loopis common for tuning and validating the setup.Hereis an example showing the result of the second iteration of anAI Assisted ADDR process.

Each vertical slice from the Event Model maps to one iteration target: the agent reads the slice spec, implements, validates against Given-When-Then specifications, and loops until they pass. Because each slice is minimal scope, it fits in a single context window. Even cheap models produce reliable results under these conditions.

Spec + Vertical Slice = Candy for AI (Credit Martin Dilger)

Fig. 4. Ralph Loop file structure

The structure tells the story: plan folders are independent and parallelizable. Each has its own progress marker, implementation checkboxes, and logs. Feedback loops producedecisionsandlearnings, which accumulate across plans. When these are significant enough, a human developer reviews them and updatesAGENTS.md. The agent's behavior evolves based on curated experience, not automated self-modification. Every iteration generates organizational knowledge as a byproduct of doing the work. [Link to implementation repository]

### Section 4: The Prospect for Event Modeling

Fig. 5. Wardley Map: Event Model Tooling Evolution

The aboveWardley Mapillustrates the industrialization of AI, combined with maturing Event Model tooling and an emerging schema standard, resulting in something novel: Conversational AI Event Modeling. This process brings together human domain experts and GenAI to model systems through conversation rather than code. The implications are worth pausing on. Within the Event Modeling workflow described above, code becomes disposable. Slices are minimal scope, fully specified, governed by templates and architectural constraints. You don't maintain a slice. You regenerate it from the spec. This reframes legacy modernization: instead of rewriting millions of lines, you model the domain and generate fresh code from it, ensuring continuous alignment.

Event Modeling operates at the level of domain behavior, distilling business intent into machine-enforceable slices. But the same declarative pattern applies beyond the domain boundary. Once behavior is modeled and generated internally, external interfaces must also remain coherent. Declarative architecture does not stop at slices – it extends to the contracts that bind systems together.

## OpenAPI Validators as Declarative Architecture

Consider a mid-sized enterprise running a highly distributed SaaS platform composed of hundreds of components owned by dozens of autonomous teams, connected primarily through HTTP APIs. Historically, this organization has relied heavily on implicit, single-person architectural ownership and "standards and practices" documentation. The "correct" approach depends heavily on which people a team chooses to consult and which documents they discover first. Teams struggle to locate the most appropriate path forward, increasing the risk of misalignment at project start. This misalignment compounds during execution as ad-hoc decisions are made, exacerbating drift between architectural intent and implementation.

This organization is at a pivotal point in its growth and seeks to launch a customer-facing API surface. The organization is prioritizing compatibility and ease of use to maximize adoption of this new surface. It also wants to maintain the velocity benefits it derives from highly autonomous teams, and it recognizes the bottlenecks associated with its current ad-hoc approach to architectural governance. Finally, the organization wants to ensure that the architecture keeps up with changing business requirements.

To reconcile this tension, the organization is applying a declarative approach to architecture oriented aroundOpenAPIspecifications, with standards and validating tools (i.e. linters) defined by a centralized platform team. These validation tools encode the architectural intent of the platform team and provide automated feedback to development teams about their conformance to that intent, and are integrated into CI/CD to safeguard the production environment against misalignment. Those same tools are also integrated into developer workflows (e.g. in the IDE, through GitHub status checks) for fast feedback and to shift-left the detection of misalignment. This model of centralized decision-making and decentralized enforcement ensures consistency for cross-cutting API concerns (e.g. path conventions, versioning and backward-compatibility, pagination, error structure), ultimately resulting in a frictionless developer experience for internal product teams and external API consumers.

This approach fits naturally into the organization’s existing software lifecycle, which leans heavily on declarative infrastructure and independent deployability. Each team’s OpenAPI specification is used as the deployment configuration for their API – the platform translates OpenAPI documents into API Gateway configuration, authorization policy, and user-facing documentation. Because all development teams share a standard build-test-deploy pipeline, the platform team has a single, predictable point at which to enforce architectural intent – no per-team coordination required. These teams continue to use the existing processes they’re familiar with; deploy-time validation precludes the possibility of misalignment. A deployment cannot succeed unless validation passes, so misaligned work can never reach production.

Fig. 6. API Lifecycle with Build-Time and Deploy-Time Validation

This model is designed to produce low cognitive load and high autonomy for dev teams, strong architectural coherence in production, and ultimately a consistent and intuitive API experience for customers. Early signals suggest it is working as intended: initial API teams have used passing validation results as objective evidence to satisfy governance requirements that previously required days or weeks of manual review.

Because architectural intent is encoded in machine-verifiable rules, alignment becomes observable. The platform team collects telemetry from the validators – validation error rates, lead time to change, and product team feedback – to identify systemic friction. Repeated violations often indicate unclear or impractical standards. High lead times may signal excessive constraints. Sustained low violation rates confirm stable conventions.

Just as the R part of theADDRprocess is used to refine API designs, this validator feedback allows the architectural intent itself to evolve. Instead of periodic standards revisions or ad-hoc debates, the platform team refines rules based on observed behaviour. The architecture adapts with the business, and teams adapt with it.

Deterministic validation guards the edges of the system, but architecture is more than syntax and structure. It is accumulated judgment – and judgment does not fit neatly into a linter rule.

## On Architectural Decision Records

"One of the hardest things to track during the life of a project is the motivation behind certain decisions." – Michael Nygard,2011

Architectural Decision Records(ADRs) serve as the reasoning behind any significant change within a software development project. They aim to allow the transfer of context, which is often lost due to the constantly shifting nature of agile development, from the decision maker to anyone who subsequently needs to maintain a system.

ADRs provide a framework for decision making focused not only on identifying the tradeoffs and alternatives, but also adding contextual information which often affects a decision more than just choosing the better solution. The ADRs serve as a history of the collective forces that have driven the evolution of a software system.

With the advent of GenAI, however, research time is vastly reduced, and the expectation of productivity seems to be increasing, ADRs might not be allowed to fulfill their purpose effectively. Humans eventually become the bottleneck and this can become a problem, especially in organizations where these decision records need to be approved before implementation. In his 2011blog postMichael Nygard also stated that "Nobody ever reads large documents" as a part of his context for developing ADRs. What happens when, because documents can now be easily mass-generated, nobody reads small documents either? Could agents be the solution?

## architecture.md as Declarative Architecture

It is one thing to statically analyze your OpenAPI specs with architectural fitness functions, but in the age ofSpec Driven Development, we must go further. A deterministic validator may greenlight syntax, style, and structure, but what about theintentof the application?

Deterministic tools only know what you tell them. They cannot call out that a perfectly valid REST endpoint violates a core architectural decision requiring asynchronous events for internal communication without relying on brittle whitelists and exceptions. Historically, we tried to solve this gap by "shifting left" and pointing developers to a massive wiki of Architectural Decision Records (ADRs). But that buried teams under cognitive load; instead of shifting left, we weredumping left, guaranteeing that as the system scaled, the architecture would drift.

We need a mechanism that understands thespiritof the guidelines as well as the letter. We need to distill our architecture into an executable format that an agentic model can enforce, mentoring developers in real-time rather than just gatekeeping their code.

### Enter architecture.md

This file is a rigorous reduction of our architectural guidance into an agent-friendly directive, applied liberally and consistently with every execution. Giving an agent our massive graveyard of wiki articles would only lead to confusion and hallucination, grinding the pipeline to a halt. Instead, every ADR must be boiled down into a brief directive that both human and agent can internalize and apply to the code:

* We do X instead of Y.
* We prefer A to B when C is true.

Each ADR and technical requirement is given its space and treatment, encapsulated into an atomic unit of intent.



# architecture.md
# Executable Architectural Manifest

## Service Communication
* [ADR-088] [Warn] Require asynchronous Kafka events for inter-service communication. Reject synchronous REST calls unless communicating with external 3rd party vendors.
* [ADR-012] [Block] All public-facing APIs must be defined in OpenAPI 3.1 format before implementation code is written.

## Data & Persistence
* [ADR-004] [Block] Services must own their data. Direct database connections to another service's schema are strictly forbidden.
* [ADR-055] [Warn] Prefer DynamoDB for high-throughput, simple-access patterns. Use Postgres only when complex relational joins are required by the domain.

## Infrastructure & Scaling
* [System-Intent] [Block] All microservices must be designed as stateless execution units to support spot instance interruption. Session state must be externalized to Redis.
* [InfoSec] [Block] All authentication must utilize the corporate IdP endpoints. Application specific user tables are forbidden.

## Observability
* [ADR-067] [Warn] Log messages must use structured JSON and include the `correlation_id` from the request context.
* [ADR-073] [Warn] Do not log request bodies containing PII. Use the `Redact()` helper on the payload before logging.

Fig. 7. Example of what anarchitecture.mdmight look like

### Closing the Loop: Automated Governance

A static file is useless if it is allowed to rot. To prevent this architecture.md from becoming just another stale wiki page, we treat it as code. A governance agent can run nightly, comparing the repository’s manifest against the central ADR corpus. If it detects a new or superseded decision, it opens a pull request to update the spec, ensuring the repository never drifts from the enterprise baseline.

As your implementation matures, you may run into a bloatedarchitecture.md, but that’s easily overcome by using a directory structure (similar tothis proposalwithagents.mdto keep your scoped sections in separate files.)

With a verified manifest in place, the runtime enforcement becomes simple. Whether running as a GitHub Action or a local IDE Copilot, the agent fetches only the relevant clauses (e.g., loading Data rules only when schema files are touched), evaluates the semantic intent of the code, and provides in-situ remediation.

If your architecture is an executable manifest, your tools stop being critics and start being collaborators. The same file that guides an agent's code review can be the seed for your generated fitness functions and the validator for your infrastructure's identity. We aren't just shifting left; we're finally giving the "Left" a map.

## Conclusion

In the era of GenAI, where drafting code and documentation is a commodity, ensuring consistency and standards across an organization is now more critical than ever. Through the use of declarative architecture and feedback loops, organizations are able to continuously evolve and automate enforcement of architectural intent. By applying industry-standard techniques like Event Modeling, OpenAPI inspection, and Architectural Decision Records and distilling the results into machine-enforceable declarations of architectural intent, organizations enable teams to move quickly and with high-confidence alignment. This pattern can be extended into agentic flows to cover intent that previously only humans could validate work against.

To eliminate the bottlenecks of centralized governance, architectural decisions must be encoded directly into the tools that generate and validate implementation. The conformant path should be the easiest path. Generators belong at project inception and inside developer workflows. Validators belong in the IDE, in pull requests, and at deployment. Governance that lives outside the delivery pipeline will be bypassed; governance embedded within it becomes invisible and automatic. These mechanisms must be paired with feedback loops that continuously evolve declared architecture.

Code is now abundant. Alignment is not. The future of architectural governance is not more review boards or better documentation. It is declared intent, continuously enforced and continuously refined, operating at the same speed as the systems it governs.



## About the Authors







#### Kyle Howard

Show more
Show less





#### Christian Johansen

Show more
Show less





#### Dana Katzenelson

Show more
Show less





#### Brian Rhoten

Show more
Show less





#### Warren Gray

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theAI Architecturetopic

##### Related Topics:

* Architecture & Design
* AI, ML & Data Engineering
* AI Architecture
* Architecture ICSAET
* InfoQ Certification Program
* Architecture

* #### Related Editorial
* #### Related Sponsors
* #### Related SponsorMay 21, 2026, 12 PM EDT##### Portable by Design: Data Mobility & Recovery Patterns for Multi-Cloud SystemsPresented by: Liore Shai - Solutions Architect at Eon
* May 21, 2026, 12 PM EDT##### Portable by Design: Data Mobility & Recovery Patterns for Multi-Cloud SystemsPresented by: Liore Shai - Solutions Architect at Eon

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
