---
title: 'Contexts graphs, AI memory, and enterprise knowledge: Are decision traces enough? | InfoWorld'
url: https://www.infoworld.com/article/4156909/context-graphs-and-decision-traces-to-the-rescue.html
site_name: tldr
content_file: tldr-contexts-graphs-ai-memory-and-enterprise-knowledge
fetched_at: '2026-05-24T18:00:34.681663'
original_url: https://www.infoworld.com/article/4156909/context-graphs-and-decision-traces-to-the-rescue.html
date: '2026-05-24'
description: A context graph could capture the full context, reasoning, and causal relationships behind critical business decisions. It’s a powerful idea.
tags:
- tldr
---

by									Dominik Tomicevic							

# Contexts graphs, AI memory, and enterprise knowledge: Are decision traces enough?

opinion

May 19, 2026
6 mins
 

## A context graph could capture the full context, reasoning, and causal relationships behind critical business decisions. It’s a powerful idea.

 

							Credit: 															
Sasun Bughdaryan

A December 2025 paper from Silicon Valley venture capital firm Foundation Capital, titled “AI’s trillion-dollar opportunity,” has generated significant excitement in the enterprise AI industry. The reason? It introduces the new concept of a “context graph,” aknowledge graphdesigned to capture a new AI paradigm known as “decision traces.” The context graph is emerging as a potentially powerful idea.

The context graph approach could capture the full context, reasoning, and causal relationships behind critical business decisions, making it a highly practical concept. As the paper notes, “Agents don’t simply need rules; they need access to the decision traces that show how rules were applied in the past, where exceptions were granted, how conflicts were resolved, who approved what, and which precedents actually govern reality.” This point is echoed by some ofthe commentaryon the prediction, which points out that the most important knowledge comes from the data about the decisions that surround those transactions as the workflow proceeds.

We see value in the idea. Decision traces are crucial because they reveal the observable reasoning behind how decisions were actually made. That said, like much in enterprise AI today, where new breakthroughs seem to emerge every few weeks, we see decision traces as part of the emerging solution to AI decision-making challenges, not as a single magic key. Context graphs only work if they can store enterprise knowledge and map how all organizational data connects.

## A part of the picture

The paper identifies a layer we hadn’t paid enough attention to before, however, and that’s important. But we need to broaden the definition to include entities, relationships, provenance, time, permissions, policies—and yes, traces of important decisions, but notonlythem.

Comparing this to another class of reasoning entities, homo sapiens, helps illustrate the point. Humans rely on different types of memory: episodic memory, which records how decisions were made and what happened; semantic memory, which stores facts and their meanings; and procedural memory, which governs skills and how to perform tasks.

Decision traces fall mostly into the episodic category, but we can’t ignore the other types of reasoning. The semantic layer—the facts and schemas—and the procedural layer—the skills and operating principles—are as important. If we know the facts but don’t understand how decisions were made, for example, it’s hard to reason about future decisions. If we know how decisions were made but not the underlying facts, we can’t ensure conclusions are correct. And if we don’t understand the procedural side, how work is actually done, we’re missing the operational principles people rely on.

In other words, serious AI requires all three types of reasoning. Skip one, and you effectively give AI the freedom to hallucinate in that domain. The AI will try to fill gaps using general world knowledge, which may not match an organization’s reality.

The semantic layer, namely the concrete, numerically trackable facts about an organization, is probably where we should start. There’s plenty of public information on reasoning or decision-making, but internal business facts are private.Large language modelsweren’t trained on that data, and organizations wouldn’t want them to be, because everyone else would then have access. Without it, the model will simply invent answers.

## A reminder on why we need graphs

A context graph may well serve as a source of truth for explainable autonomy, but not for everything. Real-world organizations still rely on systems like ERPs, CRMs, and data warehouses, which need to remain the canonical sources for transactions, raw data, and records.

What the context graph adds are elements such as which evidence mattered, which relationships were relevant, what policies applied, what exceptions were made, and why a particular action was acceptable at a given moment. In other words, the context graph is a kind of operational memory that complements existing enterprise systems, rather than replacing them.

Graphs are important in the growing understanding of how to build practical, non-trivial AI structures in business because enterprise context is fundamentally based on connections. The interesting questions aren’t about retrieving similar text. They’re about relationships: who approved something, what policy applied, which systems were affected, what changed before an incident, and how a customer connects to tickets, contracts, and transactions.

Those are all relationship questions, and they’re difficult to process with simplevector search. Remember, vector search finds similar text but doesn’t capture the structure of relationships. Graphs give you a much higher chance of modeling and querying those connections directly.

Context graphs won’t replace other types of graphs in enterprise systems; they’ll compose them. A context graph sits on top of existing systems to help AI know where to look, acting as a central “hive mind” for agents. For example, if a bank asks an accounting question, it might query the accounting database; if it’s a fraud question, it might query a fraud detection graph. A well-designed context graph acts as a layer connecting everything. It’s a kind of “graph of graphs” that guides queries.

## Where does GraphRAG fit?

A related question is whereretrieval-augmented generation(RAG) as instantiated in graphs, orGraphRAG, fits into the emerging context graph ecosystem. GraphRAG is proving highly effective at improving retrieval from graphs so AI systems can access structured knowledge more effectively, so it forms an essential part of this landscape.

Bigger questions remain. How do we represent skills? How do we manage procedural knowledge? How do agents develop capabilities over time?

Initially, we’ll define skills manually, but emerging frameworks are starting to allow systems to create and evaluate skills automatically, ensuring they enhance performance rather than degrade it.

All of this needs to be unified. Right now, the market is moving and learning incredibly quickly and we’re experimenting. We’re figuring out what the full AI architecture will look like. Our advice to enterprise AI teams is to absorb as many innovations as possible, including context graphs and decision traces, but don’t set anything in stone yet. The landscape evolves so quickly that a new critical idea could emerge next week.

What a great time to be a developer, no?

—

New Tech Forumprovides a venue for technology leaders—including vendors and other outside contributors—to explore and discuss emerging enterprise technology in unprecedented depth and breadth. The selection is subjective, based on our pick of the technologies we believe to be important and of greatest interest to InfoWorld readers. InfoWorld does not accept marketing collateral for publication and reserves the right to edit all contributed content. Send allinquiries todoug_dineley@foundryco.com.

Generative AI
Artificial Intelligence
Databases
Data Management
Software Development
 

 

														by 															
Dominik Tomicevic

Contributor

1. Follow Dominik Tomicevic on LinkedIn

Dominik Tomicevic is CEO ofMemgraph. In 2011, Dominik was one of only four people worldwide to receive the Microsoft Imagine Cup Grant, personally awarded by Bill Gates. In 2016, he founded Memgraph, a venture-backed graph database company specializing in high-performance, real-time connected data processing. In 2017, Forbes recognized Dominik as one of the top 10 Technology CEOs to watch. Today, Memgraph boasts an open-source community of 150,000 members and customers including NASA, Cedars-Sinai, and Capitec Bank.

## More from this author

* feature### When it comes to AI, bigger isn’t always betterSep 12, 20257 mins
* feature### LLMs aren’t enough for real-world, real-time projectsJun 24, 20257 mins
 

## Show me more

Popular
Articles
Videos

opinion
 
 

### The sovereign cloud illusion

 
By David Linthicum
May 22, 2026
6 mins

Cloud Architecture
Enterprise Architecture
Multicloud

news
 
 

### Microsoft releases open-source tools to operationalize AI agent safety

 
By Shweta Sharma
May 21, 2026
3 mins

Code Security
Development Tools
Security

feature
 
 

### Angular Signal Forms: From event pipelines to signal-driven state

 
By Sonu Kapoor
May 21, 2026
8 mins

Angular
Development Approaches
Web Development

video
 
 

### Why developers are so divided about using AI tools

 
May 19, 2026
6 mins

Python

video
 
 

### Profile Python Functions With ZERO Extra Code

 
May 12, 2026
4 mins

Python

video
 
 

### Two powerful tools for viewing Python app performance stats

 
May 5, 2026
5 mins

Python