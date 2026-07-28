---
title: Amazon is investing in the Lean Focused Research Organization - Amazon Science
url: https://www.amazon.science/news/amazon-is-investing-in-the-lean-focused-research-organization
site_name: tldr
content_file: tldr-amazon-is-investing-in-the-lean-focused-research-o
fetched_at: '2026-07-28T11:43:22.355030'
original_url: https://www.amazon.science/news/amazon-is-investing-in-the-lean-focused-research-organization
date: '2026-07-28'
published_date: '2026-07-26T08:00:00'
description: As AI agents take on higher-stakes decisions, Lean programming language makes it possible to mathematically prove they will behave safely.
tags:
- tldr
---

Automated reasoning

# Amazon is investing in the Lean Focused Research Organization

## As AI agents take on higher-stakes decisions, Lean programming language makes it possible to mathematically prove they will behave safely.

By 
Byron Cook
, 
Shawn Bice

 July 26, 2026
 

2 min read

Share

* Copy link
* Email
* X
* LinkedIn
* Facebook
* Line
* Reddit
* QZone
* Sina Weibo
* WeChat
* WhatsApp

 分享到微信
 

x

 Key takeaways
 

* Amazon is providing long-term financial support to the Lean Focused Research Organization (FRO) to advance Lean, a programming language that enables mathematical proofs of software correctness.
* Amazon uses Lean-based verification across multiple products including Bedrock AgentCore for agentic safety, SampCert for differential-privacy guarantees, and AWS Neuron for AI chip compilation, with scientists using LLM-Lean combinations to prove complex distributed protocol correctness.
* Amazon supports Lean's development through the independent Lean FRO rather than internally to ensure transparency and trustworthiness, allowing customers, auditors, and regulators to independently validate proof tools for safety-critical AI applications.

Was this answer helpful?

We want to tell you about an investment we're making and why we're excited about it. As AI agents increasingly make decisions that move money, approve claims, and operate critical infrastructure, the standard approach to software testing is no longer sufficient. Testing checks the cases you thought of, but there is a fundamentally different approach: mathematical proof, which shows with certainty that a system cannot behave incorrectly, no matter what inputs it gets.

Leanis a programming language with the potential to make correctness proofs practical at the scale of modern software. Amazon is now providing substantial, long-term financial support to the team building it — theLean Focused Research Organization (FRO)— to make proofaccessibleto every developer in the world. This is the single largest donation in the FRO's history.

The Lean Focused Research Organization is building the tools that make mathematical proof practical at the scale of modern software.

Lean has spawned a thriving community of users in mathematics, computer science, physics, and many other fields. It has led to the creation of Mathlib, a comprehensive library of formalized mathematics, which ignited an explosion of further efforts in formalized proofs. And it has had a pivotal role in the development of AI reasoning capabilities: AI generation of formal proofs in Lean has been a key method for training models with lower error rates, to the point that they are now producing correct solutions to research-level problems.

But to us at Amazon, the most exciting thing about Lean is the role it promises to play in agentic safety andneurosymbolicAI: coupling generative AI with Lean's mathematical rigor will help enable verified, trustworthy AI agents. The Lean team drove this vision before the industry caught up, and it’s a vision that is increasingly important to our own strategy for agentic safety. For example,Policy in Amazon Bedrock AgentCoreuses Lean-based verification to prove the correctness of the policy language that keeps AI agents within specified boundaries. We haven't seen anyone else offer this type of mathematical guarantee.

Lean also underpins the correctness proofs behind systems such as SampCert (mathematical guarantees that differential-privacy protections in AWS Clean Rooms are sound) and AWS Neuron (compilation to Amazon's AI acceleration chips). One scientist recently used an LLM with Lean to prove the correctness of Amazon Aurora's segment repair protocol, our most durability-critical distributed protocol, in a fraction of the time it would have taken manually. The set of applications is growing fast, and this is just the beginning.

How the Lean language brings math to coding and coding to math

Uses of the functional programming language include formal mathematics, software and hardware verification, AI for math and code synthesis, and math and computer science education.

You might wonder why Amazon would want Lean developed in the FRO, outside of Amazon. The answer is that it's easier to trust a proof when you can evaluate the tools behind it yourself. Customers, auditors, and regulators can independently inspect and validate work done in community-governed tools, which is the kind of transparency that safety-critical AI demands.

It also matters internally. Lean becomes more useful as its developer community (which includes our engineers) grows, providing more libraries, more tooling, and more formalized proofs for everyone. For both reasons, we have found it crucial that the foundational work on Lean happens in the open through theLean Focused Research Organization.

 Research areas
 

* Automated reasoning

 Tags
 

* Formal verification
* Responsible AI
* Large language models (LLMs)
* Generative AI
* Amazon Web Services (AWS)

About the Author

Byron Cook

 Amazon vice president and distinguished scientist Byron Cook is a leader in the field of formal verification, known for his contributions to SAT, SMT, and symbolic model checking, with applications to biological systems, computer operating systems, programming languages, and security. Byron’s work on automated reasoning at Amazon has led to higher levels of assurance in the cloud as well as new customer features.
 

Shawn Bice

 Amazon Web Services vice president Shawn Bice leads AI Services and the Automated Reasoning Group. Shawn drives science and product teams to bring neurosymbolic AI — which combines large language models with formal verification — into developer tooling so that every builder can create trustworthy AI agents with provable correctness.