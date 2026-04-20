---
title: Can your governance keep pace with your AI ambitions? AI risk intelligence in the agentic era | Artificial Intelligence
url: https://aws.amazon.com/blogs/machine-learning/can-your-governance-keep-pace-with-your-ai-ambitions-ai-risk-intelligence-in-the-agentic-era/
site_name: tldr
content_file: tldr-can-your-governance-keep-pace-with-your-ai-ambitio
fetched_at: '2026-04-02T19:24:49.435880'
original_url: https://aws.amazon.com/blogs/machine-learning/can-your-governance-keep-pace-with-your-ai-ambitions-ai-risk-intelligence-in-the-agentic-era/
date: '2026-04-02'
published_date: '2026-03-31T07:36:17-08:00'
description: AWS AI Risk Intelligence (AIRI) for non-deterministic agentic systems (7 minute read)
tags:
- tldr
---

## Artificial Intelligence

# Can your governance keep pace with your AI ambitions? AI risk intelligence in the agentic era

DevOps used to be predictable: same input, same output, binary success, static dependencies, concrete metrics. You could control what you could predict, measure what was concrete, and secure what followed known patterns.

Then agentic AI arrived, and everything changed.

Agents operate non-deterministically; they don’t follow fixed patterns. Ask the same question twice, get different answers. They select different tools and approaches as they work, rather than following predetermined workflows. Quality exists on a gradient from perfect to fabricated rather than binary pass-fail. Predictable dependencies and processes have given way to autonomous systems that adapt, reason, and act independently. Traditional IT governance frameworks designed for static deployments can’t address these complex multi-system interactions. Organizations face inconsistent security postures across agentic workflows, compliance gaps that vary by deployment, and observability metrics opaque to business stakeholders without deep technical expertise.

This shift requires rethinking security, operations, and governance as interdependent dimensions of agentic systemhealth. It’s also the origin story of AI Risk Intelligence (AIRI): the enterprise-grade automated governance solution fromAWS Generative AI Innovation Centerthat automates security, operations, and governance controls’ assessments into a single viewpoint spanning the entire agentic lifecycle. To build this solution, we used theAWS Responsible AI Best Practices Framework, our science-backed guidance built on our experience with hundreds of thousands of AI workloads, helping customers address responsible AI considerations throughout the AI lifecycle and make informed design decisions that accelerate deployment of trusted AI systems.

## From static controls to dynamic governance

Consider a common security risk in agentic systems. The Open Worldwide Application Security Project (OWASP)—a nonprofit that tracks cybersecurity vulnerabilities—identifies “Tool Misuse and Exploitation” as one of itsTop 10 for Agentic Applications in 2026. Here’s what that looks like in practice:

An enterprise AI assistant has legitimate access to email, calendar, and CRM. A bad actor embeds malicious instructions in an email. The user requests an innocent summary, but the compromised agent follows hidden directives—searching sensitive data and exfiltrating it via calendar invites—while providing a benign response that masks the breach. This unintended access operates entirely within granted permissions: the AI assistant is authorized to read emails, search data, and create calendar events. Standard data loss prevention tools and network traffic monitoring are not designed to evaluate whether an agent’s actions are aligned with its intended scope — they flag anomalies in data movement and network traffic, neither of which this unintended access produces. To govern multi-agent systems at scale, security must integrate directly into how agents operate, and vice versa.

## The systemic nature of Agentic Risk

The calendar exfiltration scenario reveals a critical insight: in agentic systems, security vulnerabilities cascade across multiple operational dimensions simultaneously. When the AI assistant misuses its calendar tool, the breach cascades across multiple dimensions:

* Multi-agent coordination: One agent’s action triggered other agents to amplify the violation
* Permission management: Access controls weren’t continuously validated while the agent was running
* Human oversight:There was no checkpoint requiring human confirmation before the agent executed a high-risk action—the system operated autonomously through the entire exploit sequence without surfacing the decision for review.
* Visibility: Risk managers couldn’t interpret the monitoring data to detect the problem before data was stolen

Traditional approaches that treat security, operations, and governance as separate concerns create blind spots precisely where agents coordinate, share context, and propagate decisions. AIRI operationalizes frameworks like the NIST AI Risk Management Framework, ISO and OWASP — transforming them from static reference documents that require human interpretation into automated, continuous evaluations embedded across the entire agentic lifecycle, from design through post-production. Critically, AIRI is framework-agnostic: it calibrates against governance standards, which means the same engine that evaluates OWASP security controls also assesses organizational transparency policies or industry-specific compliance requirements. This is what makes it applicable across diverse agent architectures, industries, and risk profiles — rather than hardcoding rules for known threats, AIRI reasons over evidence the way an auditor would, but continuously and at scale.

## AIRI in action

Let us now explore how AIRI operationalizes the automated governance of agentic systems in practice. Let’s return to our AI assistant’s example. Assume, for instance, that the development team has just produced a POC using this AI assistant. Before they deploy their solution to production, they run AIRI. To assess the foundations of their system, the team starts by leveraging AIRI’s automated technical documentation review capability to automatically collect evidence of the control implementations contained in the table below — assessing not only security but also operational quality controls: transparency, controllability, explainability, safety, and robustness. The analysis spans the design of the use case, the infrastructure serving it, and organizational policies to facilitate alignment with enterprise governance and compliance requirements.

For each control dimension, AIRI runs a reasoning loop. First, it extracts the relevant evaluation criteria from the applicable framework. Then it pulls evidence from the system’s actual artifacts — architecture documents, agent configurations, organizational policies. From there, it reasons over the alignment between what the framework requires and what the system demonstrates, ultimately determining whether the control is effectively implemented. This reasoning-based approach is what makes AIRI broadly applicable. Rather than relying on static rule sets that break when agent architectures change, AIRI evaluates intent against evidence. That means it adapts to new agent designs, new frameworks, and new risk categories — without being re-engineered.

To strengthen the reliability of these judgments, AIRI repeats each evaluation multiple times and measures the consistency of its conclusions — a technique called semantic entropy. When outputs vary significantly across runs, it signals that the evidence is ambiguous or insufficient and triggers human review rather than forcing a potentially unreliable judgment. This is how AIRI bridges the gap between abstract framework requirements and concrete agent behavior: turning governance intent into a structured, repeatable evaluation that scales across agentic systems.

The assessment of our AI assistant evaluated the system across hundreds of controls and returned an overall Medium risk rating with a pass rate just above 50%. More telling than the aggregate score is the risk distribution — and it maps directly to the cascading vulnerabilities we described.

Eight Critical and seven High severity findings signal that foundational controls — particularly around safety, controllability, and security — are either absent or insufficiently operationalized. Fourteen Medium severity findings indicate systemic gaps in areas such as explainability and robustness that, while not immediately catastrophic, compound the overall risk posture if left unaddressed. On the more resilient end, findings concentrated in governance, fairness, and transparency reflect areas where the organization has invested meaningfully and where controls are functioning as intended. After human validation of the results, the team accesses a dashboard that synthesizes the findings alongside prioritized, actionable recommendations — from configuring responses with traceable references to reduce hallucination risk, to implementing input guardrails that block variables which could introduce bias, to strengthening explainability through surfaced decision evidence. Each recommendation is grounded in the assessment evidence and mapped to specific AWS capabilities that can remediate the gap.

Critically, AIRI is not a one-time audit. Integration with the development environment enables AIRI to function as a continuous governance engine. Every time the project undergoes a change — whether a code commit, an architecture update, or a policy revision — AIRI automatically re-runs the assessment, making sure governance keeps pace with development velocity. Teams gain a living record of how their risk posture evolves with each iteration.

## Turn governance into your edge

The shift to dynamic governance determines which organizations confidently scale agentic workloads and which remain constrained by manual oversight.

* For security teams: AIRI transforms reactive vulnerability management into proactive risk identification.
* For operations teams: AIRI alleviates manual auditing across multi-agent systems with automated assessments and mitigations plans.
* For risk managers: AIRI translates technical monitoring data into business-relevant metrics—controllability, explainability, transparency—enabling confident decisions without deep technical expertise.
* For executives: AIRI represents competitive advantage: deploy faster, scale reliably, maintain compliance efficiently.

Traditional frameworks designed for static deployments cannot address the dynamic interactions that define agentic workloads. AIRI provides the automated rigor required to govern agents at enterprise scale—a fundamental reimagining of how security, operations, and governance work together systemically.

The question is no longer whether to adopt agentic AI, but whether your governance capabilities cankeep pace with your ambition.

Ready to scale your agentic workloads with confidence?Explore how AIRI can transform your AI governance strategy—contact usto learn more or schedule a demo today.

### About the authors

Segolene Dessertine-Panhardis the global tech lead for Responsible AI and AI governance initiatives at the AWS Generative AI Innovation Center. In this role, she supports AWS customers in scaling their generative AI strategies by implementing robust governance processes and effective AI and cybersecurity risk management systems, leveraging AWS capabilities and state-of-the-art scientific models. Prior to joining AWS in 2018, she was a full-time professor of Finance at New York University’s Tandon School of Engineering. She also served for several years as an independent consultant in financial disputes and regulatory investigations. She holds a Ph.D. from Paris Sorbonne University.

Sri Elaproluis Director of the AWS Generative AI Innovation Center, where he leads a global team implementing cutting-edge AI solutions for enterprise and government organizations. During his 13-year tenure at AWS, he has led ML science teams partnering with global enterprises and public sector organizations. Prior to AWS, he spent 14 years at Northrop Grumman in product development and software engineering leadership roles. Sri holds a Master’s in Engineering Science and an MBA.

Florian Feliceis a Senior Data Scientist at the AWS Generative AI Innovation Center. In his role, he is the science lead for AI Risk Intelligence, where he develops frameworks and tools to evaluate and govern responsible AI practices at scale. In this role, he focuses on quantifying and measuring AI models’ uncertainty, risks, and benefits, drawing on his statistical background to bring rigor and precision to AI governance. He holds a Master’s degree in Statistics and Econometrics from Toulouse School of Economics.

Daniel Ramirezis a Data Scientist in Responsible AI at the AWS Generative AI Innovation Center. With over 10 years of experience automating processes with machine learning and generative AI, he works at the intersection of advanced AI systems and AI governance, helping organizations build trustworthy and accountable AI at scale.Before joining AWS, Daniel served as a Data Science Manager focused on fraud detection, and prior to that, as a Tech Lead at a Series D startup. He holds a Master’s in Computer Science from Universidad de los Andes and a Master’s in Data Science from Columbia University.

Randi Larsonconnects AI innovation with executive strategy for the AWS Generative AI Innovation Center, shaping how organizations understand and translate technical breakthroughs into business value. Shehosts the Innovation Center’s podcast seriesand combines strategic storytelling with data-driven insight through global keynotes and executive interviews on AI transformation. Before Amazon, Randi refined her analytical precision as a Bloomberg journalist and consultant to economic institutions, think tanks, and family offices on financial technology initiatives. Randi holds an MBA from Duke University’s Fuqua School of Business and a B.S. in Journalism and Spanish from Boston University.
