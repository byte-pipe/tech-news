---
title: Medium
url: https://blog.opendataproducts.org/ai-agents-need-data-product-context-not-more-rag-99fa4690f4c8
site_name: tldr
content_file: tldr-medium
fetched_at: '2026-07-20T19:34:41.025712'
original_url: https://blog.opendataproducts.org/ai-agents-need-data-product-context-not-more-rag-99fa4690f4c8
author: Dr. Jarkko Moilanen
date: '2026-07-20'
published_date: '2026-07-17T16:59:34.270Z'
description: AI Agents Need Data Product Context Not More RAG Amarnath Byakod’s article, “Context Engineering and Knowledge Cataloging for AI Agents,” begins with a problem that many enterprise AI teams …
tags:
- tldr
---

Data
Context Engineering
AI
AI Agent

# AI Agents Need Data Product Context Not More RAG

Dr. Jarkko Moilanen
13 min read
·
3 days ago

--

Listen

Share

Amarnath Byakod’s article, “Context Engineering and Knowledge Cataloging for AI Agents,” begins with a problem that many enterprise AI teams will recognize. Documents are divided into chunks, converted into embeddings and stored in a vector database. An agent retrieves passages that appear relevant and produces a fluent answer. The demonstration looks successful until someone asks where each statement came from, whether the passages belong together and whether the answer reflects the correct business context.

## Context Engineering and Knowledge Cataloging for AI Agents

### The Cognitive Architecture Blueprint

medium.com

In Byakod’s clinical experiment, the retrieval process combined information from different patients into one invented clinical profile. The system found semantically related text, but it failed to preserve the boundaries and relationships that made the information meaningful. His conclusion is direct:

“This isn’t a retrieval problem. It’s a knowledge catalog problem.”

That distinction applies far beyond clinical systems. It is equally relevant to enterprise data, data products and the growing number of AI agents expected to use them. Retrieval helps an agent find information, but it does not tell the agent what that information represents, how different pieces relate to each other or under which conditions the information should be used.

## Retrieval Does Not Give an Agent Business Context

Most enterprise agent initiatives begin with access. Teams connect an agent to SharePoint, Confluence, databases, APIs or document repositories. They add embeddings and retrieval, then test whether the agent can answer questions. At first, this often creates the impression that the agent now understands the organization.

In reality, access and understanding are different things. An agent still needs to know which information belongs together, which source owns a fact, which product supports a business use case and which terms carry an agreed meaning. It also needs to understand quality expectations, service commitments, access methods and governance restrictions. These are data product questions.

A vector store might retrieve passages mentioning customer churn, revenue risk and customer segmentation. It does not tell the agent whether those passages belong to an approved customer risk product, whether they support the same KPI or whether the agent is allowed to use them for a specific decision. It does not explain who owns the information, whether the source is current or whether the data meets the quality level required for the task.

Enterprise context must therefore contain more than retrieved content. It must preserve product meaning, source evidence, relationships and operating conditions.

Press enter or click to view image in full size
Retrieved fragments versus compiled product context

## One Governed Model Needs Several Representations

Byakod proposes an architecture in which one extraction process produces several parallel representations of the same knowledge. A graph supports relationship traversal. A compiled Markdown wiki gives a language model dense and connected context. A portable Open Knowledge Format bundle supports local or offline use. A query engine then selects the representation that best fits the question.

This is closely aligned with the direction of the Open Data Products ecosystem and the Data Product SDK.

ODPS describes an individual data product and its operational contract. ODPC provides a catalog and portfolio structure. ODPG describes relationships between products, objectives, use cases and other portfolio elements. ODPV provides shared vocabulary, while ODPR defines repeatable processes for creating and maintaining products. The SDK already produces compact TOON and GCF sidecars and supports OKF import and export.

These formats do not compete with each other. They represent different projections of the same governed product model.

A portfolio manager might need a visual view of products, gaps and strategic alignment. A platform might need a machine-readable graph. A governance process might need the full ODPS contract. An agent might need a compressed context package that contains only the details relevant to one task. A developer might need a local bundle exposed through the CLI, Python API or MCP server.

The important design choice is not to force every consumer into one format. It is to maintain one governed model and compile the representation required by each use case.

## Compile Context Around the Work the Agent Must Perform

One of the strongest recommendations in Byakod’s article is:

“Compile context, don’t just retrieve it.”

This principle should have a direct influence on how agents consume data products.

An agent assessing customer retention risk should not receive the entire enterprise catalog or fifty fragments that happen to mention churn. It should receive a prepared context package containing the products, definitions, relationships and operating conditions relevant to that task.

That package might include the business objective, the KPI, the approved use case, the products supporting it, the required quality conditions, the available access services and the vocabulary used by the organization. It should also include product dependencies, source evidence, permitted purposes and the current product version.

The Data Product SDK already creates summaries and compact sidecars. The next step is to treat this as a context compilation problem rather than a document summarization problem.

A context compiler could accept an agent task, a portfolio scope, a consumer identity and a token budget. It would then assemble the smallest complete package that allows the agent to operate correctly. Instead of exposing every available field, it would prepare only the product context required for the task.

This would move the SDK beyond specification generation. It would position the SDK as an execution layer between governed data products and AI agents.

## Maysano Portfolio Studio Already Applies This Model

This context engineering model is not only theoretical. Maysano Portfolio Studio already applies many of the same principles to data product portfolios.

The Studio starts from source documents rather than from manually completed catalog forms. Business objectives, signals, use cases and data product needs are extracted from those materials and organized into a connected portfolio model. The source documents remain attached to the portfolio, which means the original evidence stays close to the context created from it.

That is an important difference from a typical retrieval setup. The system does not treat source files as a loose collection of text chunks. It transforms them into explicit business objects.

An objective becomes a defined node. A signal becomes a defined node. A use case becomes a defined node. A data product becomes a defined node. These objects are not stored as isolated records. Their relationships appear in a graph that shows how business intent, evidence, use cases and product needs connect.

Each node also has a structured YAML representation. This gives the same portfolio several useful forms at the same time. Business users see a rich, understandable portfolio. The graph reveals the relationships. The YAML gives platforms, developers and agents a machine-readable definition.

The source document, the business object, the graph relationship and the YAML node all describe the same underlying context from different perspectives.

This closely matches the architecture described by Byakod. One source-grounded model produces several representations for different consumers. The difference is that Maysano Portfolio Studio is not cataloging clinical or domain knowledge alone. It is compiling business and data product context.

The Studio therefore acts as a business context compiler for data products.

It prepares the context before an agent needs it. The source documents explain where the knowledge came from. The portfolio objects explain what that knowledge means. The graph explains how the objects connect. The YAML provides the structure needed by software and AI agents.

This also creates a direct path into the Data Product SDK. The Studio produces the portfolio context, while the SDK validates, packages, traverses, transforms and exposes that context through ODPC, ODPG, ODPS, sidecars, workflows and agent interfaces. Together, the Studio and the SDK form two layers of the same system.

Maysano Portfolio Studio is the business development and portfolio formation layer. It turns unstructured source material into a reviewed and connected model of objectives, signals, use cases and products.

The Data Product SDK is the technical and operational layer. It turns that model into validated specifications, graphs, portable context packages, workflows and agent-ready interfaces.

This is stronger than connecting an agent directly to a document repository. The agent receives structured product context that has already been connected to business intent.

Press enter or click to view image in full size
Source documents through Maysano Portfolio Studio and the Data Product SDK into governed context for humans, platforms and AI agents

## Every Generated Product Claim Needs Evidence

Byakod places provenance at the center of the architecture. Extracted entities point back to exact locations in the source material. The system then verifies those references independently rather than trusting the language model’s output.

This principle matters greatly when the Studio and SDK generate data product definitions from business documents.

When the system extracts a business objective, product need, KPI, consumer, restriction or relationship, it should preserve the evidence behind that extraction. A statement such as “the customer risk product supports the churn reduction objective” should link back to the page, slide, spreadsheet cell or text section that supports it.

Maysano Portfolio Studio already keeps the source documents attached to the portfolio. The next step is to deepen that relationship at node level. Each objective, signal, use case and product should retain direct references to the exact source evidence from which it was created.

## GetDr. Jarkko Moilanen’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe
Subscribe

Remember me for faster sign in

The system should also separate three layers of information.

* The first layer is source evidence. This records what the original material states.
* The second layer is machine interpretation. This records what the extraction process inferred from that evidence.
* The third layer is approved portfolio knowledge. This records what a human accepted into the active model.

This separation prevents generated specifications from becoming detached from the source material that created them. Without it, reviewers see a polished product description but cannot determine which parts came directly from evidence, which parts came from interpretation and which parts were added during review.

Source-grounded generation would make portfolio decisions easier to explain, challenge and audit.

## Schema Validation Is Not Enough

The SDK already validates specification structure, but structural validity does not prove that generated content is correct.

A product definition can conform perfectly to the ODPS schema while containing an unsupported objective, an invented consumer or an incorrect relationship. The file is technically valid, but the product knowledge inside it is unreliable.

This is where Byakod’s approach offers an important lesson. The language model proposes entities and relationships, but deterministic code verifies whether the source evidence exists. The model assists with interpretation. It does not act as the final authority. The same principle should guide Maysano Portfolio Studio and the Data Product SDK.

The language model should first propose portfolio objects and product metadata from the source material. Deterministic checks should then confirm that the evidence exists. Vocabulary resolution should verify that the extracted terms match agreed business language. Schema validation should confirm that the resulting ODPS, ODPC or ODPG artifact is structurally correct. Cross-object checks should ensure that referenced products, objectives and use cases exist. A human should then approve the result before it enters the active portfolio.

This creates a more reliable sequence. Source material becomes proposed context. Proposed context becomes verified metadata. Verified metadata becomes approved portfolio knowledge.

## Product Graphs Need Evidence-Aware Relationships

A graph becomes useful when agent questions depend on relationships rather than isolated facts.

An agent might need to know which products support a use case, which objective a product contributes to or which dependencies must exist before a workflow can operate. ODPG provides the structure for representing these relationships, while Maysano Portfolio Studio makes those relationships visible during portfolio development.

The relationship itself should retain its origin. A graph edge should state whether it came from an approved specification, a source document, a machine inference or a human review. It should also retain the evidence supporting that connection.

This matters because not every relationship has the same level of authority. A declared dependency in an approved product contract is different from a connection inferred from similar wording across two documents. Both might be useful, but they should not look identical to an agent or reviewer.

Evidence-aware graph relationships would allow the Studio and SDK to support reasoning without presenting every generated connection as an established business fact.

This is especially important in a living portfolio. A graph might show that a signal supports a use case, that a use case depends on a product or that several products contribute to one objective. Those relationships become more trustworthy when the reviewer can see whether they were extracted, inferred or approved.

## Data Product Context Goes Beyond Knowledge Cataloging

The architecture in Byakod’s article focuses on entities, relationships, source grounding and query routing. That is suitable for the clinical prototype he describes, but enterprise data products require a broader operational context.

An agent does not only need to know that information exists. It needs to know how that information should be consumed.

That includes ownership, lifecycle status, access interfaces, data quality commitments, service levels, permitted purposes, policies, pricing conditions, version information and strategic contribution. These are the elements that turn a body of knowledge into a governed data product.

This is where the ODPS family extends the knowledge catalog model. The catalog tells the agent what is known and how concepts connect. The product contract tells the agent how the information is offered, who is accountable for it and under which conditions it should be used.

Maysano Portfolio Studio adds another layer before the operational contract. It shows why the product should exist in the first place.

The objective explains the intended business outcome. The signals explain why action is needed. The use case explains how value will be created. The product explains which reusable capability must support that use case. The graph connects these elements into one business story. The SDK then carries that story into the operational and technical layer.

This gives the agent more than knowledge and more than access. It gives the agent a connected explanation of business intent, product structure and operating conditions.

Press enter or click to view image in full size
Data Product Graph Explorer with typical rich context with related use cases, signals, business objectives, and other data products.

## Context Must Change When the Business Changes

Byakod also describes an incremental maintenance model. Source files receive checksums. New and changed files are processed, while unchanged material is skipped. Only affected graph and wiki outputs are rebuilt. Grounding metrics then show whether the quality of the catalog has declined.

This pattern fits naturally with the render, sync and refresh levels already introduced through Data Product SDK recipe contracts.

Maysano Portfolio Studio should maintain a source manifest that links each input document to the objectives, signals, use cases, products and relationships generated from it. When a source changes, the Studio should identify which parts of the portfolio might be affected.

The SDK should then regenerate only the related technical artifacts, preserve approved manual edits and present a semantic change report for review. The result should not be an automatic replacement of the approved portfolio. It should be a controlled proposal that explains what changed, which products depend on the changed source, which relationships were added or removed and which context packages are now stale.

This would support a living portfolio rather than a periodic catalog rebuild.

It also strengthens the relationship between the Studio and the SDK. The Studio manages the evolution of business context. The SDK manages the evolution of the corresponding machine-readable and operational artifacts.

## The Studio and SDK Form a Context Engineering System

The Data Product SDK already supports validation, explanation, generation, catalogs, graphs, vocabulary, workflows and compact context formats. Maysano Portfolio Studio adds the business-facing layer that turns source material into structured portfolio knowledge. Together, they form a broader context engineering system.

For each portfolio, the Studio can retain the source material, the business objects, the graph and the YAML representation. The SDK can then transform those into validated ODPS, ODPC and ODPG artifacts, compact sidecars, portable bundles and runtime interfaces.

For each product, the combined system could generate an agent-ready package containing the governed specification, compiled Markdown context, compact TOON and GCF representations, source evidence, vocabulary references, access instructions and a maintenance manifest.

The ODPS file would remain the governed contract. The Markdown file would provide dense, model-readable context. TOON and GCF would support token-efficient agent use. The evidence file would preserve source grounding. The manifest would support incremental updates. The access instructions would explain how the agent should consume the product.

The SDK could then route questions to the correct representation. Catalog questions would use ODPC. Relationship questions would use ODPG. Product contract questions would use ODPS. Terminology questions would use ODPV. Process questions would use ODPR. Runtime context would use compact sidecars.

Maysano Portfolio Studio would provide the business meaning behind those artifacts. It would show which objective the product supports, which signals created the need and which use cases depend on it.

This is more precise than generic retrieval over product documentation. It gives the agent a compiled operating context built from source-grounded business knowledge and governed product definitions.

## From Knowledge Catalogs to Governed Agent Context

Byakod closes his article with another compact principle:

“Ground every fact. Route every query. Monitor every metric.”

For data products, one more requirement should be added: govern every use. Enterprise AI agents need knowledge catalogs, but they also need product contracts. They need evidence, relationships and compact context, along with ownership, access rules, quality expectations and lifecycle control.

They also need the business story around the product. They need to understand which objective matters, which signals created urgency, which use case creates value and which product provides the capability.

This is where Maysano Portfolio Studio and the Open Data Product Specifications family come together.

Maysano Portfolio Studio compiles unstructured business material into structured portfolio context. The ODPS family provides the common language for describing products, catalogs, graphs, vocabulary and processes. The Data Product SDK turns that language into validated artifacts, workflows and agent-ready packages.

Press enter or click to view image in full size

The opportunity is larger than improving retrieval. It is to create a governed context layer through which AI agents understand what enterprise data means, where it came from, why it matters, how it connects and under which conditions it should be used.

That is the foundation required for agents that do more than locate information. It is the foundation for agents that participate safely in real business operations.