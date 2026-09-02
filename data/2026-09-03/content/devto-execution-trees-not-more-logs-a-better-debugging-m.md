---
title: 'Execution Trees, Not More Logs: A Better Debugging Model for AI Agents - DEV Community'
url: https://dev.to/raju_dandigam/execution-trees-not-more-logs-a-better-debugging-model-for-ai-agents-3d4g
site_name: devto
content_file: devto-execution-trees-not-more-logs-a-better-debugging-m
fetched_at: '2026-09-03T07:20:36.245110'
original_url: https://dev.to/raju_dandigam/execution-trees-not-more-logs-a-better-debugging-model-for-ai-agents-3d4g
author: Raju Dandigam
date: '2026-09-02'
description: A flat log can tell you that five things happened. It often cannot tell you which operation caused... Tagged with ai, typescript, debugging, opensource.
tags: '#ai, #typescript, #debugging, #opensource'
---

Mental timeline reconstruction fails at scale

A flat log can tell you that five things happened. It often cannot tell you which operation caused the next one, which failure triggered a fallback, or whether three tool calls were children of one planning step or unrelated work.

That distinction matters for AI agents because the path is part of the behavior.

I maintainAgentInspect, an open-source TypeScript toolkit for inspecting agent executions locally. This article explains why I chose execution trees as the primary debugging model, using synthetic fixtures verified againstagent-inspect@6.17.4.

## The problem with reading an agent run as a timeline

Consider a support agent that performs these operations:

09:00:00.000 plan started
09:00:00.020 inventory request started
09:00:00.060 inventory request failed: 503
09:00:00.061 inventory request started
09:00:00.120 inventory request succeeded
09:00:00.150 answer completed

Enter fullscreen mode

Exit fullscreen mode

This is enough to reconstruct a simple story, but the reconstruction is happening in your head. Add nested agents, parallel tools, reused operation names, and interleaved application logs, and timestamps stop being a reliable picture of causality.

An execution tree makes the relationship explicit:

support-agent
├── plan
├── fetch-inventory (failed: 503)
├── fetch-inventory (success)
└── draft-answer

Enter fullscreen mode

Exit fullscreen mode

The tree does not replace raw event data. It is a projection of that data for the question developers usually ask first:What path did this run take?

## Capture meaningful boundaries in TypeScript

AgentInspect provides wrappers for a run and for named steps. Here is a deliberately small example:

import
 
{
 
inspectRun
,
 
step
 
}
 
from
 
"
agent-inspect
"
;

await
 
inspectRun
(

 
"
travel-planner
"
,

 
async 
()
 
=>
 
{

 
const
 
plan
 
=
 
await
 
step
(
"
plan
"
,
 
async 
()
 
=>
 
({

 
destinations
:
 
[
"
SFO
"
,
 
"
SEA
"
],

 
}));

 
const
 
[
flights
,
 
hotels
]
 
=
 
await
 
Promise
.
all
([

 
step
.
tool
(
"
search-flights
"
,
 
async 
()
 
=>
 
[

 
{
 
id
:
 
"
F-101
"
,
 
price
:
 
220
 
},

 
]),

 
step
.
tool
(
"
search-hotels
"
,
 
async 
()
 
=>
 
[

 
{
 
id
:
 
"
H-202
"
,
 
nightly
:
 
180
 
},

 
]),

 
]);

 
return
 
step
.
llm
(
"
rank-options
"
,
 
async 
()
 
=>
 
({

 
plan
,

 
flights
,

 
hotels
,

 
}));

 
},

 
{
 
traceDir
:
 
"
./.agent-inspect
"
 
},

);

Enter fullscreen mode

Exit fullscreen mode

This is manual instrumentation. It does not claim that a wrapper can automatically discover every framework-internal operation. The purpose is to record the boundaries you care about: the run, its planning step, the two sibling tool calls, and the final model-facing step.

Then inspect the run locally:

npx agent-inspect view travel-planner 
\

 
--dir
 .agent-inspect 
\

 
--summary

Enter fullscreen mode

Exit fullscreen mode

## Four shapes that reveal different classes of bugs

### 1. Nested work exposes ownership

A three-level synthetic fixture renders like this:

Execution Tree:
✔ outer (120ms)
 ✔ middle (80ms)
 ✔ inner (50ms)

Enter fullscreen mode

Exit fullscreen mode

Those two spaces are not decoration. They tell us thatinnerbelongs tomiddle, which belongs toouter. Ifinnerfails, we know which higher-level operation owned it. With flat logs, matching IDs or surrounding timestamps would be required to infer the same structure.

Nesting is especially useful when one agent delegates to another, a tool performs several sub-operations, or a retrieval step owns both a query rewrite and a vector search.

### 2. Fallbacks expose recovery behavior

Now consider an error-recovery fixture:

Execution Tree:
✖ tool:primary-search (100ms)
 Error: primary search unavailable
✔ tool:fallback-search (200ms)
✔ handle-recovered-result (50ms)

Enter fullscreen mode

Exit fullscreen mode

The final run may still be successful. If we looked only at the answer, the failed primary search could disappear from the debugging story. The tree preserves both facts:

* the primary path failed;
* the recovery path completed.

That distinction can change the engineering decision. A successful answer produced by a fallback may be acceptable, but a sudden rise in fallback use could still indicate a degraded dependency or an expensive routing change.

### 3. Repeated siblings expose retries

Retries deserve their own visible shape:

Execution Tree:
✖ tool:fetch-inventory (40ms)
 Error: synthetic 503 from upstream
✖ tool:fetch-inventory (45ms)
 Error: synthetic 503 from upstream
✔ tool:fetch-inventory (60ms)
✔ handle-recovered-result (30ms)

Enter fullscreen mode

Exit fullscreen mode

A final success status would hide the cost of reaching success. The repeated tool name makes the retry sequence visible. It also gives a deterministic check something concrete to evaluate: for example, whetherfetch-inventoryexceeded an allowed call count.

The tree alone does not tell us whether the retry policy was correct. It gives us evidence that the policy was exercised.

### 4. Parallel siblings expose concurrency

A parallel fixture renders as sibling operations:

Execution Tree:
✔ tool:search-hotels (300ms)
✔ tool:search-flights (200ms)
✔ tool:search-cars (100ms)

Enter fullscreen mode

Exit fullscreen mode

The durations are not meant to be added. These steps are siblings, and may overlap. That protects us from a common timeline mistake: assuming each timestamped operation waited for the previous one.

The tree does not prove that concurrency was optimally implemented, but it accurately preserves the structural relationship needed to investigate it.

## Trees are a view, not the entire evidence model

It is tempting to turn a readable tree into the only stored artifact. I avoided that because a human-readable view necessarily compresses information.

The underlying trace may include identifiers, timestamps, status, inputs or outputs (subject to capture policy), observations, and metadata. Different questions need different projections:

structured trace
├── tree -> what path happened?
├── check -> did an invariant hold?
├── diff -> what changed between runs?
├── report -> what should a reviewer read?
└── bundle -> what evidence can be shared?

Enter fullscreen mode

Exit fullscreen mode

An execution tree is the fastest entry point, not a substitute for checks or analysis.

## Turn a suspicious shape into a deterministic check

Suppose the retry tree reveals that an inventory tool can run three times. If the intended policy permits at most two calls, encode that expectation rather than relying on future visual inspection.

At the CLI level, a trajectory check can require tools and fail on recorded observations:

npx agent-inspect check travel-planner 
\

 
--dir
 .agent-inspect 
\

 
--preset
 trajectory 
\

 
--required-tool
 search-flights 
\

 
--fail-on-observation
 failed

Enter fullscreen mode

Exit fullscreen mode

For richer rules, AgentInspect exposes an experimentalTraceContractAPI that can express tool requirements, forbidden tools, maximum calls, ordering, run status, duration, model allowlists, and token ceilings. Because that API is beta in the referenced release, pin the version and test the exact semantics before using it as a CI gate.

The important workflow is broader than one API:

1. inspect the tree;
2. identify a stable behavioral invariant;
3. encode it as a deterministic check;
4. keep human judgment for context-dependent questions.

## What the tree cannot tell you

A clean tree does not prove that an answer is correct. A required retrieval step may return irrelevant documents. A model call may produce unsupported claims. A tool can succeed technically while returning stale data.

Execution trees are strongest for structural questions:

* Which operations ran?
* Which operation owned a failure?
* Was a fallback or retry used?
* Which work happened as siblings?
* Where did a run stop?

Use semantic evaluators, domain tests, and human review for content quality. The most reliable agent debugging workflow combines these layers rather than asking one visualization to answer every question.

## Debug the path, not only the answer

The final response is what the user sees, but the execution path is what the engineer can improve. A tree turns that path from an inferred narrative into a concrete artifact.

That is the design principle behind AgentInspect’s local view: preserve causal structure, expose unsuccessful work even when recovery succeeds, and make suspicious patterns easy to convert into repeatable checks.

You can explore the exact release used here onGitHub. If you try it, start with a synthetic failure-and-fallback fixture. A perfect happy path is the least interesting test of a debugger.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (18 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse