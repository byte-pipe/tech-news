---
title: 'AI infrastructure security: Why it deserves its own category | Sysdig'
url: https://www.sysdig.com/blog/ai-infrastructure-security-why-it-deserves-its-own-category
site_name: tldr
content_file: tldr-ai-infrastructure-security-why-it-deserves-its-own
fetched_at: '2026-04-03T19:18:59.852561'
original_url: https://www.sysdig.com/blog/ai-infrastructure-security-why-it-deserves-its-own-category
date: '2026-04-03'
description: AI attacks are increasingly targeting infrastructure, not prompts. Explore real-world risks, architecture patterns, and practical strategies to secure AI workloads across cloud environments.
tags:
- tldr
---

< back to blog

# AI infrastructure security: Why it deserves its own category

Published by:
Manuel Boira
@
linkedin
@
linkedin
Get our AIBOM
Published:
March 26, 2026
Table of contents
falco feeds by sysdig

## Falco Feeds extends the power of Falco by giving open source-focused companies access to expert-written rules that are continuously updated as new threats are discovered.

learn more

Attacks on artificial intelligence infrastructure are rising, but not in the way most people expect. While AI security headlines focus on prompt manipulation, attackers are going after the infrastructure behind these systems. This article takes a broader view of AI security, unpacking this shift and outlining practical strategies to respond.

To understand the risk, step into the shoes of a security engineer.

On a routine Friday afternoon, a retailer’s security team receives an alert: customer addresses and bank information are circulating on underground forums. The news is unexpected. Production systems are tightly monitored, data is segmented, and no exfiltration has been detected.

The investigation takes an uncomfortable turn. The source is not the hardened e-commerce platform, but a newly created AI research environment training recommendation models on real customer data. It isn’t production. It isn’t meant to be exposed. Yet it is running in the cloud.

The scenario is hypothetical. The risk pattern is not.

## It is about the cloud infrastructure after all

AI workloads may be in their infancy and still have an aura of experimentation, but the infrastructure behind them is real, and the data they manage is often massive and sensitive. As such, the risk surface is usually larger than teams initially assume.

AI looks like magic, so people let their guard down around it. To make this clearer, let’s start by clarifying something that is not intuitive:

Once you stripaway the abstraction,AI is still a workloadrunning somewhere.

The real question is not whether AI depends on computing services, but what your organization controls versus what relies on third parties.

Next, let’s see what artificial intelligence actually looks like in the modern enterprise.

## The shape of enterprise AI today

Pinning down what AI means is harder than it sounds. Ask ten IT professionals and you’ll get ten different answers. It can mean chatbots, foundation models, ML pipelines, algorithms, infrastructure, depending on who you ask. They are all correct.

AI, as an academic discipline, has been around since the 1960s. At its core, it is computing that simulates aspects of intelligent behavior. Today, as AI matures and intersects with cloud and DevOps, it is evolving from a scientific field into an industrial domain.‍

### AI operating models

Security teams must understand how AI actually shows up in their organization. The next sections break down what these systems look like, how they are built, and why they are adopted in different ways.‍

The AI value stack

A useful way to think about this is themakers,shapers, andtakersframework often used by firms such asMcKinseywhen discussing generative AI.

‍

Takers, Makers, and Shapers process map

Makersare a relatively small group of frontier model vendors, cloud providers, startups, and research institutions that train foundation models using massive GPU capacity and vast amounts of data.

Takersinclude organizations and individuals consuming AI capabilities directly through platforms such as ChatGPT, Gemini, or Copilot.

Between them sits a broad ecosystem ofshapers: companies building products on top of AI systems and adapting models through fine tuning, retrieval layers, or proprietary data integration.

For a more operational perspective, theAI Security Scoping Matrixfrom Amazon Web Services separates AI systems into five distinct responsibility domains. It is a useful reference when thinking about security responsibilities.

AWS AI Security Scoping Matrix

The architecture puzzle

As mentioned earlier, AI is a broad discipline. Below, we’ll review some basic distinctions and their risk profiles. This is only a high-level overview. For a deeper discussion, see the related blog series.

The AI architecture puzzle

Generative vs. predictive

Generative AI has gained significant traction in recent years, but AI extends well beyond it.Whilegenerativesystems produce open-ended output and are typically interactive,predictivesystems are more constrained and decision-oriented. Generative systems power copilots, agents, and assistants that generate text, code, images, or responses, often by combining multiple data sources. Predictive systems operate within business logic and transactional flows, supporting use cases such as fraud detection, demand forecasting, recommendation engines, or risk scoring.

This distinction shapes architecture, exposure, and control strategy.From a security perspective, generative systems tend to aggregate data and guide users across workflows, making security more accessible. Predictive systems, by contrast, operate as profilers, identifying patterns and flagging suspicious activity.

Reactive vs. agentic

An agentic system operates across steps, maintains longer-lived sessions, invokes tools, and accesses systems to achieve an objective, while areactivesystem executes requests and returns results.

These differences shape security exposure and control.

Training and inference

Training pipelines sit closer to the makers category defined earlier. They concentrate data, model artifacts, and, in many cases, specialized computing resources such as GPUs within a highly privileged control plane. They are not frequently internet-facing, but they often have custody of critical intellectual property.

Inference services are where shapers operate. These services connect models to live traffic, APIs, and internal systems. They handle credentials, retrieval layers, and real-time execution. The primary risk shifts from concentrated model assets to runtime exposure and system integration.

Seen through a security lens, training is about protecting the asset. Inference is about controlling exposure and runtime processes.

IaaS, PaaS, and SaaS

The same problem can be solved using very different architectures.One setup trains or fine-tunes models on a Kubernetes-based environment backed by GPU clusters, leveraging high-throughput networking while keeping primary datasets in object storage for data gravity. The resulting model is then deployed for inference in the same or a different cloud, exposed through APIs and integrated into business applications. A detailed example of this pattern is covered inSecuring GPU-accelerated AI workloads in Oracle Kubernetes Engine.

Another adopts a foundation model using a managed service such as AWS Bedrock, or GCP Vertex, connecting it to a RAG database through platform APIs.

Even for similar use cases, architecture and responsibility boundaries can differ significantly. The reasons vary, from sovereignty requirements to performance and accuracy constraints.

#### How companies operate today

Generative AI is no longer experimental.

Turing’sState of AI Adoption 2025reports that 80% of companies are deploying or integrating generative and LLM-based tools into core workflows.McKinseyplaces regular generative AI use at 65% of organizations, roughly doubling year over year.

Momentum, however, does not mean maturity.Information Services Groupfinds that only 31% of enterprise use cases are in full production, suggesting many initiatives remain in transition.

Some signals distinguish generative from predictive systems. TheFederal Reserve Bank of Philadelphiareports that 50% of surveyed firms use generative tools, while 23% report traditional AI deployments. Generative workloads are rising quickly, but predictive systems remain embedded across operational platforms.

Adoption patterns also show how organizations consume this technology.Menlo Venturesreports that 76% of solutions are purchased rather than built internally. Infrastructure follows the same pattern. A survey fromBentoMLshows that 77% of organizations run inference workloads on public cloud, while 30% report using on-premises deployments, often in hybrid setups.

Agentic systems remain in the early stages of adoption.McKinseyreports that 23% of organizations are scaling them in at least one function, while 39% are experimenting.

### Securing a moving target

The previous sections show that AI is diverse and fragmented, and so is its rapidly evolving stack.

For security professionals, the priority is visibility:you can’t protect what you can’t see. They must understand the AI systems their organizations adopt and secure them at the required scale and speed.

## What recent attacks and vulnerabilities reveal

To understand the real risk of AI systems and the effectiveness of our controls, we should examine the attacks that have targeted AI infrastructure in recent years.

The following metrics are not directly comparable. Most of the figures reflect download volumes. Taken together, however, they point to a clear trend: Attacks are increasing in scale as AI adoption accelerates and infrastructure becomes more interconnected.

Increased technical depth points to more capable adversaries, often leveraging AI-driven tooling. Broader impact reflects the speed of adoption and the expansion of exposed infrastructure.

Period

Attack Name

Estimated Reach

Information

Layer

Q1–26

Hackerbot-claw

150,000+

Supply Chain RCE: Autonomous bot injecting code into build runners

AI pipeline (CICD)

Q1–26

Copilot YOLO Mode

5,000,000+

Autonomous AI executing actions without safeguards

Agentic workflow

Q1–26

OpenClaw/MCP

50,000+

Agentic AI misuses tools causing harmful actions

Agent protocol

Q4–25

Keras Arbitrary Access & SSRF

4,000,000+

Victims download and load the malicious model. The attacker retrieves the SSH keys

AI software library

Q4–25

BodySnatcher

500,000+

Context hijack enables agentic misuse of actions

AI agent identity

Q4–25

LangGrinch

3,000,000+

Derived from monthly download spikes for langchain-core on PyPI (approx. 98M monthly) during the unpatched window

AI orchestrator

Q4–25

ShadowRay 2.0

100,000+

Up to 15,000 clusters were affected. The botnet could have affected 100,000+ elements

AI infrastructure and software library

Q1–25

Hugging Face Hub

1,200,000+

Model supply chain compromise through malicious artifacts

Model registry

Q4–24

Ultralytics Poison

260,000+

Supply chain poisoning causes compromised model behavior

ML pipeline

Q3–24

NVIDIA Escape

1,000,000+

GPU memory isolation failure leading to data leakage

Cloud containers

Q1–24

ShadowRay 1.0

230,000+

Exposed Ray clusters enable remote code execution

AI infrastructure and software library

Q1–23

PyTorch RCE

2,300+

Unsafe model deserialization enables arbitrary code execution

Software library

Notably, several agent-related security issues have been disclosed during the editorial process of this post, including a recentMeta incident involving AI-generated instructionsthat led to internal data exposure, reflecting the rapid expansion of agent capabilities and their deep integration with external systems.

### The problem was understood, but the control point was not

In all these incidents, the breach vector was not related to prompt manipulation or corrupted training data. It was infrastructure: access control, network exposure, storage configuration, altered components, or runtime manipulation.

Much of today’s AI security conversation focuses on prompt analysis and red teaming through text inputs. These practices matter, but they address only one side of the problem. The infrastructure layer receives comparatively less attention, even though some prompt-level risks are, in reality, design failures.

Zero-day vulnerabilities remain an unavoidable risk, capable of emerging without warning. Misconfigurations slip into production. Shadow AI systems appear outside formal governance and remain unmonitored. Even well-intended architectures drift over time.

That is why AI infrastructure protection deserves its own category in the security conversation.

### Adopting the neurologist perspective

In the same way that psychologists study behavior while neurologists study the system that produces that behavior, cybersecurity tools operate at different layers.

Acloud workload protection platform (CWPP)analyzes the internal composition, accesses, and real-time signals of the workload itself.

By contrast, tools like a web application firewall (WAF), and more recently, LLM protection platforms, primarily analyze inputs and outputs.

In our analogy:

* Psychologist →Analyzes inputs and outputs
* Neurologist →Analyzes internal composition and signals

If we secure the conversation but ignore the infrastructure that generates it, we are treating symptoms while missing the source.

### From perspective to practice

This is the shift. Meaningful AI risk does not necessarily originate in prompts, but in infrastructure, supply chains, and execution environments.

Addressing that risk requires moving beyond surface level controls and focusing on how AI systems are actually built and operated. It means understanding where they run, how they are configured, and how they behave in production.

This is where the approach becomes concrete.

## A complete protection approach

The neurologist workflow described earlier translates into four practical control areas.

Asset Discovery → Posture & Risk → Pipeline → Runtime perimeter

Discovery must account for AI-specific assets across SaaS, PaaS, and IaaS layers.Posture management must continuously evaluate misconfigurations, exposed endpoints, excessive privileges, and vulnerable dependencies. Attack paths matter more than isolated findings.Shift left controls are critical. Vulnerabilities and risky configurations should be identified in images, pipelines, and infrastructure definitions before deployment.And finally, runtime protection is non-negotiable. Exploitation happens inside containers and cloud services. Monitoring execution behavior, privilege use, and anomalous activity is what prevents a misconfiguration from becoming a breach.

AI-SPM and AIBOM are not enough. AI infrastructure requires the same depth of control we apply to any high-value cloud workload, or arguably more given the concentration of data, compute, and privileges involved, and the rising cost of AI-related breaches. Those controls must also be specialized to address the specific technologies and high fragmentation across the AI stack.

## Operationalizing AI infrastructure security

At Sysdig, we apply this approach to infrastructure security, extending cloud-native controls to AI services and software, including ML and LLM systems.

The framework includes:

* AIBOMto surface related services, workloads, and trusted boundaries. This is essential to get rid of shadow AI blind spots.
* Risk managementthat prioritizes real attack paths, in-use vulnerabilities, and dangerous misconfigurations.
* Shift left securitythat prevents vulnerable images and risky configurations from reaching production.
* Protection of the runtime perimeterthat monitors execution behavior and privilege use inside containers and cloud services.

Increasingly, AI can assist in securing AI. Using an AI analyst, such asSysdig Sage™, or integrating security insights directly intoenterprise LLM workflows, helps teams investigate faster and reduce operational friction.

### Using Sysdig for an LLM application

TheOWASP Top 10 for Large Language Modelsprovides a useful way to connect these ideas to real security scenarios. This list spans both training and inference risks and reflects the challenges practitioners face when securing LLM systems. The following diagram maps those risks to the relevant Sysdig CNAPP capabilities.

The OWASP Top 10 for LLM Applications, also referenced in our 
OKE GPU whitepaper

## Conclusion

Enterprise AI runs on cloud infrastructure. It concentrates data, compute, and privilege in ways that increase both exposure and impact.

Securing inputs and outputs is not enough. You need to secure the system. Read more aboutSysdig AI workload protectioncapabilities and exploreSysdig threat researchpublications for more information on AI attacks.

## About the author

Cloud Security
featured resources

## Test drive the right way to defend the cloud with a security expert

GET A DEMO