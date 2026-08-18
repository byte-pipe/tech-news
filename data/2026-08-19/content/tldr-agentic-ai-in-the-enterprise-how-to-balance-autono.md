---
title: 'Agentic AI in the enterprise: How to balance autonomy with constraints | InfoWorld'
url: https://www.infoworld.com/article/4209900/agentic-ai-in-the-enterprise-how-to-balance-autonomy-with-constraints.html
site_name: tldr
content_file: tldr-agentic-ai-in-the-enterprise-how-to-balance-autono
fetched_at: '2026-08-19T04:06:45.132189'
original_url: https://www.infoworld.com/article/4209900/agentic-ai-in-the-enterprise-how-to-balance-autonomy-with-constraints.html
date: '2026-08-19'
description: Agentic systems operate well when autonomy sits inside explicit constraints. Constraints turn agent behavior into something teams can measure, improve, and trust.
tags:
- tldr
---

by									Adnan Masood							

# Agentic AI in the enterprise: How to balance autonomy with constraints

how-to

Aug 17, 2026
8 mins

Enterprise teams are moving from chat-based assistants to systems that can take actions. I see the shift in how people describe the work. They ask for an assistant that can write code, file tickets, update CRM records, run a compliance checklist, generate a pull request, and follow through on the next step. That shape of work requires an agentic system.

I define an agentic system as software that turns a user goal into a sequence of steps, executes those steps through tools, keeps track of what happened, and produces an auditable outcome. The model contributes planning and language. The surrounding system provides authority, state, verification, and control.

[ See also:“How to run enterprise GenAI like a production service”]

The engineering question stays consistent across domains. How do you give the system enough autonomy to be useful while keeping outcomes predictable. A production answer comes from constraints that are explicit and enforced.

Adnan Masood

## Define the agent loop

An agent loop is the repeated cycle the system follows to complete work. I use a simple loop and I make each stage observable.

1. Plan: The agent chooses the next action based on the goal, current state, and policy.
2. Act: The agent calls a tool with structured arguments, then records the result.
3. Verify: The system checks the result against policy and task expectations.
4. Commit: The system writes the state change to a durable store and produces an audit event.

These words carry specific meanings in implementation. Planning produces a structured intent. Action uses a limited interface with a defined schema. Verification runs deterministic checks. Commit writes the versioned state and the trace context.

## Define tools and tool contracts

A tool is any callable capability outside the model. It can be an API, a database query, a workflow engine, a code repository action, or a browser automation step. Tool use dominates operational risk because tools can change systems of record.

A tool contract is the boundary that makes tool use safe to operate. I write it down as part of design review. A contract includes the following:

* Inputs: A schema that rejects free-form parameters and enforces types.
* Permissions: The identity context, the scopes, and the data boundaries.
* Idempotency: A request key and a replay rule so retries do not create duplicate changes.
* Rate limits: Per user, per agent, and per tool to protect shared systems.
* Error semantics: Stable error codes and retry guidance.
* Audit fields: Request ID, actor, time, target record, and before/after references.

This contract turns an agent into a regular distributed system client. It becomes testable. It becomes debuggable. It becomes something an operations team can own.

## Define policy as executable rules

Policy in an agentic system means rules the runtime enforces on every step. I treat policy as an executable module. It sits in the request path. It is versioned. It emits an audit event on decisions.

Common policy domains include data access, tool allowlists, approved destinations for writes, required citations for retrieved material, and refusal rules for restricted requests. Policy starts simple and grows based on incident learning.

## Treat state as a first-class component

State is the durable record of what the agent knows and what it has done. I keep state outside the model. I persist it with a clear schema. I version it per step.

I store at least the goal, the plan steps, tool inputs and outputs, verification results, and the final decision. I also store the retrieved sources when retrieval is part of the loop. This state supports replay during incidents and supports evaluation later.

Teams that keep state only in a conversation buffer lose the ability to reason about behavior at scale. A durable state store supports retries, handoffs, and governance reporting.

## Use verification as a gate on action

Verification is a set of checks that run before a write and after a tool call. I use deterministic checks whenever possible. I treat the model output as an input to be validated.

Examples include schema validation, permission checks, reference integrity checks, and constraints on target systems. For content workflows, verification includes citation coverage and checks for restricted data.

I also use a confidence policy for high-impact actions. The system can require a human approval step for certain tools or destinations. Approval works best when it is narrowly scoped to a clear action with context and evidence.

Adnan Masood

## Build an evaluation harness around the loop

Evaluation for agents focuses on end-to-end task completion and on safety properties. I define task success criteria as observable facts. The ticket exists. The record was updated with the correct fields. The pull request passes checks. The change request has the right approvals.

I create scenario suites that cover routine tasks and edge cases. I run them with fixed seeds where possible and with stable tool mocks. I also run a small set of live tests against a staging environment with realistic data.

I track metrics that connect to operations. Task completion rate by scenario. Average steps per task. Tool error rate. Verification failure rate. Human approval rate. Mean time to recover when a tool returns partial results.

## A practical reference pattern

I build production agents with a supervisor pattern. A supervisor owns policy, routing, and state. Specialized workers handle narrow tasks such as retrieval, summarization for a ticket, or a repository action. Workers run with the minimum permissions required for their contract.

A simplified sketch looks like this:

def run_task(goal, user):
    ctx = start_context(goal, user)
    while ctx.open_steps:
        intent = planner.propose_next(ctx)
        intent = policy.enforce_intent(intent, ctx)
        call = tool_router.bind(intent, ctx)
        result = call.execute(idempotency_key=ctx.step_key)
        checks = verifier.run(intent, result, ctx)
        ctx = commit_step(ctx, intent, result, checks)
        if checks.requires_approval:
            ctx = wait_for_approval(ctx)
    return ctx.outcome

This structure keeps authority in the supervisor. It keeps tool permissions narrow. It gives operations teams a single place to enforce policy and observe behavior.

## Operational practices that keep agents stable

I use a short set of practices when teams want agents to run safely in production.

* Start with low-blast-radius workflows. Read-heavy tasks and draft generation build confidence and instrumentation.
* Ship with a limited tool allowlist. Expand based on measured outcomes and incident learning.
* Use staged rollouts. Start with internal users, then a small cohort, then broader exposure.
* Keep tool schemas strict. Free-form tool parameters create unpredictable writes.
* Set budgets. Enforce maximum steps per task, maximum tool calls, and a cost ceiling.
* Maintain runbooks. Include rollback, disable switches per tool, and escalation routes to humans.

## Minimum viable checklist

I look for these elements before a team runs agentic workflows at scale.

* A written definition of the agent loop, with traces at each stage.
* Tool contracts with schemas, permissions, idempotency, rate limits, and audit fields.
* Policy module with versioning and enforcement in the request path.
* Durable state store with step-level records for replay and governance reporting.
* Verification gates on writes and high-impact actions.
* Evaluation suite that measures task completion and safety properties.
* Operational controls including budgets, staged rollout, and disable switches per tool.

## Constraints are key

Agentic systems fit enterprise work because they connect language interfaces to business systems. The systems operate well when autonomy sits inside explicit constraints. Constraints turn agent behavior into something teams can measure, improve, and trust.

—

New Tech Forumprovides a venue for technology leaders—including vendors and other outside contributors—to explore and discuss emerging enterprise technology in unprecedented depth and breadth. The selection is subjective, based on our pick of the technologies we believe to be important and of greatest interest to InfoWorld readers. InfoWorld does not accept marketing collateral for publication and reserves the right to edit all contributed content. Send allinquiries todoug_dineley@foundryco.com.

Artificial Intelligence
Generative AI
Software Development
 

 

														by 															
Adnan Masood

Contributor

1. Follow Adnan Masood on LinkedIn

Adnan Masood, PhD, works at the intersection of AI strategy, academia, and hands-on engineering. He advises leaders and engineering teams on what it takes to ship GenAI responsibly in large organizations. Dr. Masood leads as Chief AI Architect atUSTand is recognized as a Microsoft Regional Director and Microsoft MVP (AI) alumnus. His focus areas include governed retrieval with citations, model evaluation and monitoring, and agentic systems designed with tight tool permissions and auditability. This work draws on collaborations with Stanford SAIL and MIT CSAIL and executive training at Harvard Business School’s Advanced Management Program. His public commentary examines how AI operating models perform under real production constraints.

## More from this author

* how-to### How to run enterprise GenAI like a production serviceJun 1, 20267 mins
 

## Show me more

Popular
Articles
Videos

news
 
 

### Java 28 to deprecate macOS/x64 support

 
By Paul Krill
Aug 17, 2026
3 mins

Java
Programming Languages
Software Development

news
 
 

### Zhipu says new coding AI developed advanced cyber skills faster than expected

 
By Gyana Swain
Aug 17, 2026
5 mins

Artificial Intelligence
Development Tools
Security

opinion
 
 

### I've built data pipelines on AWS, Azure and Snowflake. Here's what Palantir Foundry did that surprised me

 
By Sashank Siwakoti
Aug 17, 2026
8 mins

Amazon Web Services
Data Engineering
Microsoft Azure

video
 
 

### AI trends that need more attention

 
Aug 4, 2026
5 mins

Python

video
 
 

### Who's leaving GitHub and why

 
Jul 29, 2026
7 mins

Python

video
 
 

### Typst, the programming language for documents

 
Jul 23, 2026
7 mins

Python