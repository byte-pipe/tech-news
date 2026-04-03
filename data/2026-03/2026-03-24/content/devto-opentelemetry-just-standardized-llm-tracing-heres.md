---
title: OpenTelemetry just standardized LLM tracing. Here's what it actually looks like in code. - DEV Community
url: https://dev.to/vola-trebla/opentelemetry-just-standardized-llm-tracing-heres-what-it-actually-looks-like-in-code-2e5f
site_name: devto
content_file: devto-opentelemetry-just-standardized-llm-tracing-heres
fetched_at: '2026-03-24T19:28:01.717702'
original_url: https://dev.to/vola-trebla/opentelemetry-just-standardized-llm-tracing-heres-what-it-actually-looks-like-in-code-2e5f
author: Albert Alov
date: '2026-03-21'
description: Every LLM tool invents its own tracing format. Langfuse has one. Helicone has one. Arize has one. If... Tagged with ai, observability, typescript, opentelemetry.
tags: '#ai, #observability, #typescript, #opentelemetry'
---

Every LLM tool invents its own tracing format. Langfuse has one. Helicone has one. Arize has one. If you built your own — congratulations, you have one too.

OpenTelemetry just published a standard for all of them.

It defines how to name spans, what attributes a tool call should have, how to log prompts without leaking PII, and which span kind to use for an agent. It's called GenAI Semantic Conventions. It's experimental. And almost nobody has written about what it actually looks like when you implement it.

I know because I searched. "OTel GenAI semantic conventions" gives you spec pages. Zero practical articles. "How to trace LLM agent with OpenTelemetry" gives you StackOverflow questions with no answers.

We implemented it. Four PRs, a gap analysis, real before/after code. We also discovered, mid-implementation, that our traces never exported at all — but that's adifferent story.

Here's what the spec actually says, where we got it wrong, and what you should do today.

## The wild west of LLM tracing

Right now, if you trace LLM calls, you're probably doing something like this:

span
.
setAttribute
(
"
llm.provider
"
,
 
"
openai
"
);

span
.
setAttribute
(
"
llm.model
"
,
 
"
gpt-4o
"
);

span
.
setAttribute
(
"
llm.tokens.input
"
,
 
150
);

span
.
setAttribute
(
"
llm.cost
"
,
 
0.003
);

Enter fullscreen mode

Exit fullscreen mode

That's what we did in toad-eye v1. Made sense to us. Worked fine in our dashboards.

Problem: nobody else's dashboards understand these attributes. Switch from Jaeger to Arize Phoenix — reconfigure everything. Export traces to Datadog — they see raw spans with no LLM context. Your tracing is a walled garden. You built vendor lock-in into your own code.

This is exactly what OpenTelemetry was created to solve. And now it has a spec for GenAI.

## Three types of GenAI spans

The spec defines three operations. Every LLM-related span gets one:

chat gpt-4o ← model call
invoke_agent orchestrator ← agent invocation 
execute_tool web_search ← tool execution

Enter fullscreen mode

Exit fullscreen mode

The span name format is{operation} {name}. Not your custom format. Notgen_ai.openai.gpt-4o(that's what we had — no backend recognizes it).

Here's what we changed:

Span naming migration: the old format was invisible to every GenAI-aware backend.

## Agent attributes — we had the paths wrong

If you're building agents (ReAct, tool-use, multi-step), the spec defines identity and tool attributes:

// What OTel says:

span
.
setAttribute
(
"
gen_ai.agent.name
"
,
 
"
weather-bot
"
);

span
.
setAttribute
(
"
gen_ai.agent.id
"
,
 
"
agent-001
"
);

span
.
setAttribute
(
"
gen_ai.tool.name
"
,
 
"
search
"
);

span
.
setAttribute
(
"
gen_ai.tool.type
"
,
 
"
function
"
);

// What we had:

span
.
setAttribute
(
"
gen_ai.agent.tool.name
"
,
 
"
search
"
);
 
// wrong path

// gen_ai.agent.name — didn't exist at all

Enter fullscreen mode

Exit fullscreen mode

Thegen_ai.agent.tool.namepath looks reasonable. It even reads well. But the spec puts tool attributes atgen_ai.tool.*— flat, not nested under agent. Our format, again, invisible to any backend that follows the standard.

## Content recording — the spec agrees with us (feels good)

This was the one thing we got right from day one, and it's worth calling out because most teams get it wrong.

The spec says:don't record prompts and completions by default.Instrumentations SHOULD NOT capture content unless explicitly enabled.

Three official patterns:

1. Default: don't record.No prompt, no completion in spans. Privacy first.
2. Opt-in via span attributes.gen_ai.input.messagesandgen_ai.output.messagesas JSON strings.
3. External storage.Store content elsewhere, put a reference on the span.

We hadrecordContent: falseas default since v1. When the spec confirmed this approach, it was one of those rare moments where your gut feeling gets validated by a committee of very smart people.

If you're logging prompts in spans by default — you might want to reconsider before your security team does it for you.

## The honest gap analysis

Here's the full picture. No spin, no cherry-picking.

### What we got right from day 1

Our attribute

OTel spec

Verdict

gen_ai.provider.name

gen_ai.provider.name

✅ Exact match

gen_ai.request.model

gen_ai.request.model

✅ Exact match

gen_ai.usage.input_tokens

gen_ai.usage.input_tokens

✅ Exact match

error.type

error.type

✅ Exact match

### What we got wrong

What

Our version

OTel spec

Status

Span name

gen_ai.openai.gpt-4o

chat gpt-4o

Fixed

Tool name attribute

gen_ai.agent.tool.name

gen_ai.tool.name

Fixed

Custom attributes

gen_ai.agent.step.*

Reserved namespace

Moved to 
gen_ai.toad_eye.*

Agent identity

Didn't exist

gen_ai.agent.name

Added

### What we built beyond the spec

Feature

Namespace

Why it's not in OTel

Cost per request

gen_ai.toad_eye.cost

Pricing is vendor-specific

Budget guards

gen_ai.toad_eye.budget.*

Runtime enforcement ≠ observability

Shadow guardrails

gen_ai.toad_eye.guard.*

Validation is app-level

Semantic drift

gen_ai.toad_eye.semantic_drift

Quality metric, not trace standard

ReAct step tracking

gen_ai.toad_eye.agent.step.*

ReAct is one pattern; spec is pattern-agnostic

The key insight:OTel spec covers WHAT happened. We cover WHY and HOW MUCH.Not competing — complementary. Your custom metrics go under your namespace. The spec's attributes go where backends expect them.

## The migration: dual-emit, don't break users

We didn't do a clean break. v2.4 emits both old and new attribute names:

// New (OTel spec-compliant)

span
.
setAttribute
(
"
gen_ai.tool.name
"
,
 
toolName
);

// Old (deprecated, still emitted for backward compat)

span
.
setAttribute
(
"
gen_ai.agent.tool.name
"
,
 
toolName
);

Enter fullscreen mode

Exit fullscreen mode

Dual-emit approach: old attributes get@deprecated, new ones follow the spec. Both emitted until v3.

An environment variable controls when to stop emitting deprecated attributes:

OTEL_SEMCONV_STABILITY_OPT_IN
=
gen_ai_latest_experimental

Enter fullscreen mode

Exit fullscreen mode

This was four PRs (#170,#171,#172,#173). v3 will remove the deprecated aliases entirely.

## The irony

While implementing all of this, we did a round of manual testing.

Turns out our traces never exported. At all. Ever. The OTelNodeSDKsilently disables trace export when you passspanProcessors: []. We had 252 passing tests. All of them mocked the SDK.

So we standardized our attributes perfectly — for traces that nobody could see.

We fixed both. Published six patch versions in one day. Thefull story is in article #2.

## Which backends actually support this

This is the reason to care. Emit the right attributes today → six backends visualize your traces tomorrow:

Backend

Recognizes GenAI spans

Agent visualization

Cost

Jaeger

Basic (nested spans)

Hierarchy view

Free

Arize Phoenix

Full GenAI UI

Agent workflow

Free tier

SigNoz

GenAI dashboards

Nested spans

Free / Cloud

Datadog

LLM Observability

Agent tracing

Paid

Langfuse

Full GenAI UI

Session view

Free tier

Grafana + Tempo

Query by attributes

Custom dashboards

Free

No vendor lock-in. One set of attributes. Six places to visualize them.

## What you should do today

If you're tracing LLM calls — even with custom code — aligning with the spec now saves you pain later. The conventions are experimental, but the direction is locked in.

Quick checklist:

* Setgen_ai.operation.nameon every LLM span:chat,invoke_agent, orexecute_tool
* Format span names as{operation} {model_or_agent_name}
* Use official attributes:gen_ai.agent.name,gen_ai.tool.name,gen_ai.tool.type
* Put YOUR custom attributes under YOUR namespace — notgen_ai.*
* Don't record prompt/completion by default — make it opt-in
* Test your traces in at least 2 backends (Jaeger + one GenAI-specific like Phoenix)

Full spec:OpenTelemetry GenAI Semantic ConventionsAgent spans:GenAI Agent Spans

Previous articles:

* #1: My AI bot burned through my API budget overnight
* #2: I audited my tool, fixed 44 bugs — and it still didn't work

toad-eye— open-source LLM observability, OTel-native:GitHub·npm

🐸👁️

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (19 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse