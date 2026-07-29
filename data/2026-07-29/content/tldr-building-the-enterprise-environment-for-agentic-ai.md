---
title: Building the enterprise environment for agentic AI | MIT Technology Review
url: https://www.technologyreview.com/2026/07/27/1140668/building-the-enterprise-environment-for-agentic-ai/
site_name: tldr
content_file: tldr-building-the-enterprise-environment-for-agentic-ai
fetched_at: '2026-07-29T12:28:39.266186'
original_url: https://www.technologyreview.com/2026/07/27/1140668/building-the-enterprise-environment-for-agentic-ai/
date: '2026-07-29'
description: For the enterprise, the promise of agentic AI is much more than just a better chatbot. It is software agents that execute business tasks end-to-end across people, business workflows, data, and systems. The platform best-suited to run agents is built with proper CPU capacity, resilient data access, policy-aware tool use, observability, memory management, and the…
tags:
- tldr
---

Sponsored

Provided byIntel

 

For the enterprise, the promise of agentic AI is much more than just a better chatbot. It is software agents that execute business tasks end-to-end across people, business workflows, data, and systems. The platform best-suited to run agents is built with proper CPU capacity, resilient data access, policy-aware tool use, observability, memory management, and the ability to predictably plan and scale agents.

 
 

To better understand some of these dependencies, Intel performed thousands of agentic AI workload experiments. Our initial findings create and support five practical lessons for enterprise leaders:

 
 
1. Agentic AI is a larger systems problem, not just one of inference.
2. The majority of existing agentic AI harnesses are limited and do not measure overall system performance.
3. Plan capacity is done using agents per virtual CPU (vCPU) density, not agent count.
4. Monitor agent task latency, not just average CPU utilization.
5. Default to scale-out for systems hosting agents. Reserve scale-up for workloads with heavier per-agent compute or architectural constraints.
 

### Beyond inference: Agents as workflow automation

 

Agentic AI is more than LLM inference. Its enterprise value depends on the full system, task orchestration, data access, tool execution, latency management, governance, and scalable infrastructure. An agent is a goal-driven automated enterprise workflow process: It plans a multi-step task, calls tools, reads results, and retries when something fails. Enterprise agents are therefore not just an inference problem; they are a systems problem.

 

Defining what good looks like

 

Most agentic AI metrics focus on evaluating the LLM used. Platform teams also need to know how long the tasks take, how many agents a fleet can support, what users experience at the end of the execution process, and how costs change as more agents work simultaneously.

 

A more useful enterprise view looks at six metrics:

 

1. Task success rate
2. Cost per task
3. Time per task
4. Task throughput
5. Agent density (agents per vCPU)
6. Latency
 

Together, these answer the questions enterprise AI operators care about: Is the system performing as expected? How many agents can the system sustain? How should it scale to support more agents?

 

### Building on solid foundations

 

To gain a deeper insight into agentic AI workload performance, Intel extendedTerminal-Bench, an open source benchmarking harness for evaluating AI agents with profiling, telemetry, and replay capabilities. This made it possible to understand where the agents spent time beyond LLM inference.

 

The benchmark extension used a deterministic record-replay of LLM responses to separate agent performance from LLM variability. LLM responses were recorded once and replayed identically across runs, reducing run-to-run variance and creating a more reliable basis for comparison.

 

The Terminal-Bench task mix used was intentionally broad. It included compilation, testing, database operations, Boolean logic, interpretation, ray tracing, compression, linear algebra, video transcoding, and machine learning training. That wide variety made the findings more relevant to real enterprise environments.

 
 

### Agentic AI in three dimensions

 

Deploying agentic AI should be approached in three phases:

 

Plan in terms of agent density, not agent count: The first sizing rule is to normalize agent count by available compute. Agent density, measured as agents per vCPU, is the leading signal for saturation. For example, 10 agents on an 8-vCPU system and 20 agents on a 16-vCPU system behave similarly if the density is the same. This gives architects a portable way to compare capacity across instance sizes and processor generations.

 

The right density also depends on the business goal. Interactive copilots and user-facing assistants should favor lower density because response time matters. Batch workloads such as IT workflows can often run at higher density. This gives teams a practical way to tune fleets around service-level objectives and total cost of ownership.

 

Agentic AI requires a new form of observability: Average compute (CPU) utilization is a weak primary performance monitoring signal for agentic workloads. Agents often alternate between waiting for model responses and then doing short bursts of compute-intensive work. Because of that “bursty” pattern, average utilization can look acceptable even when those bursts are creating queues and slowing down the user experience. Task latency (P95) is a better leading metric. It shows when workflows are starting to wait, even before average task duration meaningfully degrades. A practical operating model is to alert on P95 latency first, then confirm the issue by looking at sustained task duration.

 

Scale out by default:Scaling out adds more systems, increasing total agent capacity, while scaling up adds cores or memory to a single system for agents with heavier compute bursts.

 

Our testing data showed that scale-out is usually the better default. That aligns with the fact that agents are typically semi-independent and have modest per-agent bursts, it improves overall performance, supports high availability, often lowers cost, and makes it easier to preserve the target agents-per-vCPU ratio as the platform grows.

 

Scale up when agents require heavier parallel compute, shared state limits partitioning, memory locality matters, or licensing constraints apply.

 

Consider business implications:Where will agentic AI create business value first? The organizations getting production-grade results are wrapping an automation layer around workflows that already have codified rules and measurable service levels: code creation, regression test farms, ticket triaging, market analysis, and security review.

 

The ideal enterprise persona for agentic AI is therefore not the experimental user chasing novelty; it is the accountable leader who must improve cycle time and productivity, protect service quality, enforce policy, and scale adoption with cost in mind.

 

Agentic AI’s value comes from helping businesses complete real work across teams, systems, data, and processes. For enterprises, the priority is not just better model performance; it is creating a reliable environment where AI agents can support business workflows, improve productivity, operate within governance requirements, and scale as adoption grows.

 

In practice, success with agentic AI depends on the right foundation to deliver consistent outcomes, manage cost, maintain control, and move confidently from pilots to production.

 

This content was produced by Intel. It was not written by MIT Technology Review’s editorial staff.

### Deep Dive

### Artificial intelligence

### A startup claims it broke through a bottleneck that’s holding back LLMs

Subquadratic has now shared more details about its new model. But some are still skeptical.

By 
* Will Douglas Heavenarchive page

### Anthropic found a hidden space where Claude puzzles over concepts

A new technique has let the company probe deeper than ever into the weird workings of an LLM.

By 
* Will Douglas Heavenarchive page

### Claude Science is Anthropic’s newest flagship product

The company is doubling down on AI for science.

By 
* Grace Huckinsarchive page

### The $400 million machine powering the future of chipmaking

The AI era needs ever faster chips. ASML has a monopoly on the expensive contraptions needed to pattern them. Can anyone catch up?

By 
* Clive Thompsonarchive page

### Stay connected

Illustration by Rose Wong

## Get the latest updates fromMIT Technology Review

Discover special offers, top stories,
 upcoming events, and more.

Enter your email
Privacy Policy

Thank you for submitting your email!

Explore more newsletters

It looks like something went wrong.

We’re having trouble saving your preferences.
 Try refreshing this page and updating them one
 more time. If you continue to get this message,
 reach out to us atcustomer-service@technologyreview.comwith a list of newsletters you’d like to receive.