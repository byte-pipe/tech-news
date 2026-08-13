---
title: I Stopped Trusting AI Agents With Tools. So I Built a Gatekeeper. - DEV Community
url: https://dev.to/debashish_ghosal/i-stopped-trusting-ai-agents-with-tools-so-i-built-a-gatekeeper-26fb
site_name: devto
content_file: devto-i-stopped-trusting-ai-agents-with-tools-so-i-built
fetched_at: '2026-08-13T19:56:13.605492'
original_url: https://dev.to/debashish_ghosal/i-stopped-trusting-ai-agents-with-tools-so-i-built-a-gatekeeper-26fb
author: Debashish Ghosal
date: '2026-08-13'
description: github.com/deghosal-2026/agent-tooltrust · pip install agent-tooltrust · field test report · design... Tagged with ai, agents, security, gatekeeper.
tags: '#ai, #agents, #security, #gatekeeper'
---

83 real agents tested zero mocks

github.com/deghosal-2026/agent-tooltrust·pip install agent-tooltrust·field test report·design decisions

## Quick Note - Field Test was on my mind from the start

My last three projects taught me the same thing. Mock agents lie. Unit tests pass. Demos look clean. Then real agents run and everything breaks.

On myeval harness, I admitted it: field testing "got added ad hoc, late in the build, because I started getting nervous that unit tests and mock agents were hiding real integration problems." On my observability tool: "I thought it was a detector problem. I was wrong."

Same lesson. Three times. But lessons only matter if you change what you do next.

So this time I did the opposite. Zero mock agents. 83 real ones across 10 frameworks. A covering design that cut a 12-day test matrix into one afternoon. And a release gate that said: no ship until real agents prove the policy works.

It worked. 2,490 tests green. 83/83 agents passed. PyPI published. Repo public. And the 7 failures taught me something I couldn't have learned any other way.

## The Problem With Allow-Lists

Everyone is racing to give AI agents more tools. Almost no one is building the permission system that decides when those tools should fire.

Right now, agent permissions are binary: allowed or denied. That's reachability, not authorization. The same tool is harmless in staging and dangerous in production. The same read is fine on public docs and risky on customer data. Adeletein a CI sandbox is not the same asdeletein production.

About 18% of MCP server deployments implement any access scoping. 80% of orgs admit agents have taken actions beyond intended scope. OWASP classifies agent tool misuse as a first-class risk.

Giving an agent tools is the easy part. The hard part is deciding what it should be allowed to do, where, and under what guardrails. I wrote aPRDandarchitecture specbefore touching engine code — partly to keep myself honest, partly because I've learned the hard way that skipping design leads to shipping the wrong thing.

## What I Built

Agent ToolTrust is a contextual risk and permission engine. Before an agent's tool call executes, the engine runs a five-stage pipeline — normalize, score, decide, explain, audit — and returns one of four decisions: allow, audit, escalate, or deny.

from
 
agent_tooltrust.engine.engine
 
import
 
Engine

from
 
agent_tooltrust.policy.models
 
import
 
default_policy

from
 
agent_tooltrust.adapters.raw
 
import
 
RawAdapter

engine
 
=
 
Engine
(
default_policy
(
"
balanced
"
))

adapter
 
=
 
RawAdapter
(
engine
)

@adapter.guard
(

 
tool_name
=
"
deploy_service
"
,

 
action
=
"
deploy
"
,

 
environment
=
"
production
"
,

 
data_class
=
"
restricted
"
,

)

def
 
deploy_service
(
service
:
 
str
)
 
->
 
str
:

 
return
 
f
"
deployed 
{
service
}
"

# Agent calls the tool. Engine evaluates first.
# production deploy on restricted data → escalate

deploy_service
(
"
payment-api
"
)

# ToolTrustDecisionError: escalate — "Write action (deploy) in production
# on restricted data requires approval..."

Enter fullscreen mode

Exit fullscreen mode

The decorator is the integration point. The agent calls the tool. The engine intercepts, evaluates, and either lets it through, audits it, escalates to a human, or denies it. The agent never sees the policy. The LLM never knows the rules exist.

The engine is deterministic. The LLM proposes, policy disposes. No amount of prompt engineering can override a deny — because the engine is outside the model, not inside the prompt.

Four decisions, not two.allowanddenyare obvious.auditmeans "allow but log everything — this is a read on sensitive data."escalatemeans "stop and get a human." Binary allow/deny forces you to choose between over-privileged agents and approval fatigue. Four states give you a middle ground.

Every decision comes with an explanation — a reason code, a human sentence, and a factor breakdown showing which dimension drove the call. Optional LLM prose, off by default. The LLM cannot change the decision.

Every decision is audited — JSONL, SQLite, or Postgres, with policy version, timestamp, and session ID.

Three posture presets ship out of the box — strict, balanced, permissive — so no one starts from a blank file. YAML policy backend for humans, OPA/Rego backend for teams that already have Rego policies. Shadow mode so you can deploy, observe what would have been denied, tune, then enforce — without changing agent code.

Fail-closed everywhere. Unknown tool → deny. Malformed input → deny. Engine crash → deny. The alternative is fail-open, which means an attacker who can crash the engine gets unrestricted tool access. That'sdesign decision DD-14— written before the first line of code, not retrofitted after a near-miss.

That's the architecture. But architecture is the easy part. Does it actually work when real agents try to use it?

## This Time, I Applied the Learning

On previous projects, the field test was the thing I skipped and regretted. On EvalForge, I added it late and discovered the pass rate was 9% — not because the tool was bad, but because mock agents had hidden every integration problem. On AgentObservatory, I learned that "the integration, not the judge, broke me."

This time, I put it in the spec before writing any adapter code.DD-11: "Field tests must pass before any release. They run real agents, not mocks." DD-12: "8-10 real agents across major platforms."

I went further than both. Not 8-10 agents. 83 real agents across 10 frameworks. And thefield test planwas in the WBS from day one.

This is the difference between learning a lesson and applying one.

## Building the Adapters Was Exploratory

I wanted this to work across the real agent ecosystem, not just one framework I happened to know. So I built adapters for 10 frameworks:

LangGraph, PydanticAI, CrewAI, OpenAI Agents SDK, Google ADK, AutoGen/AG2, LlamaIndex, smolagents, SWE-bench (self-test), ToolTrust MCP(self-test).

Every adapter follows the same contract — extract aCallContext, forward it toEngine.evaluate(), surface the decision back:

@dataclass
(
frozen
=
True
)

class
 
CallContext
:

 
tool_name
:
 
str

 
action
:
 
str

 
environment
:
 
str

 
data_class
:
 
str

 
agent_id
:
 
str

 
session_id
:
 
str
 
|
 
None
 
=
 
None

 
arguments
:
 
dict
[
str
,
 
Any
]
 
|
 
None
 
=
 
None

Enter fullscreen mode

Exit fullscreen mode

The contract is clean. Getting there was not.

Each framework has its own opinions about how tools are registered, how they're invoked, and how errors surface. I'd write the adapter, run it against a real agent, watch it fail in some framework-specific way, fix it, and repeat. Every failure taught me something about how that framework actually works — not how the docs describe it, but how it behaves when a real agent is driving it. The full per-framework wiring notes are in§5 of the field test report— 12 separate learnings.

LangGraph'sToolTrustToolNodesubclassesToolNodeand overrides_run_one(). But in langgraph v1.x, the node isn't callable — so I fell back to wrapping the tool before it enters the graph:

# LangGraph — wrap the tool, then hand it to the graph

adapter
 
=
 
RawAdapter
(
engine
)

guarded_tool
 
=
 
adapter
.
guard
(

 
tool_name
=
"
query_logs
"
,

 
action
=
"
read
"
,

 
environment
=
"
staging
"
,

 
data_class
=
"
internal
"
,

)(
query_logs_fn
)

# Now hand guarded_tool to create_react_agent(llm, tools=[guarded_tool])

Enter fullscreen mode

Exit fullscreen mode

Google ADK's LLM registry only knows about Gemini. To use a local model, you passLiteLlm(model=f"openai/{MODEL}", api_base=ENDPOINT). AndInMemorySessionService.create_session()is a coroutine — you have toawaitit, not call it synchronously. The docs don't mention this. The runtime teaches you.

LlamaIndex's legacyReActAgenthas no.query()or.chat(). You need the workflow agent fromllama_index.core.agent.workflow. And execution is driven byasync for event in handler.stream_events()— a separateawait handleryields nothing. Theasync foris what drives the agent forward. Without it, the agent silently does nothing. I spent an hour on that.

AutoGen needs hyphens sanitized from agent IDs (ag-01→ag_01). The local Qwen model answers textually unless you tell it: "you MUST call the tool exactly namedscn_<id>. Do not skip the tool call."

smolagents requires full docstrings with per-arg descriptions on every@tool— or it throwsDocstringParsingException. CrewAI needslitellmas a fallback. OpenAI Agents SDK needsfunction_tool(..., strict_mode=False)to fix a pydantic conflict.

None of these show up with mock agents. They only surface when you run real code from real repos. And every one I fixed made the adapter stronger.

By the end, all 10 frameworks built, recorded decisions, and ran real agents through the engine. Ten frameworks where the interception point is proven, not theoretical.

## 83 Real Agents, 30 Scenarios, Zero Mocks

I sourced 83 real agents from GitHub. Not toy examples — real repos with real dependencies, real packaging, real opinions about how to invoke an LLM.

I wrote 30 scenarios: 20 decision scenarios covering all four decision types across 5 agent classes (ci-bot, engineer, general, analyst, sensitive), plus 10 adversarial scenarios — prompt injection, Unicode obfuscation, replay attempts, blank tool names, malformed inputs, grant-bypass attempts. The full matrix is in thefield test report— every agent, every scenario, every expected and actual decision.

The math: 83 agents × 30 scenarios = 2,490 runs. Each run calls a local LLM —Qwen3.5-4B-4bitvia OMLX on Apple Silicon. Each call takes 30-80 seconds. That's roughly 2.7 hours at 10 workers.

But 2,490 is the theoretical minimum. In practice, you debug. Adapters break. Agents fail to import. The LLM answers textually instead of calling a tool. You fix, re-run, fix again. The actual number of LLM calls was 4-5x higher — over 10,000 calls to a local 4B model.

This is the cost of zero mock agents. I'd pay it again.

Mock agents don't need an LLM. They don't take 80 seconds. They don't bring a C extension with the wrong ABI. They don't hardcode API keys at module scope. They don't write to/rootat import time.

Real agents do all of that. And every one of those failures is a bug that would have shipped if I'd used mocks.

## Turning 12 Days Into 1

Here's where I stopped brute-forcing. 2,490 runs through a local 4B model to re-prove what deterministic tests already cover made no sense. Engine correctness was already validated — 2,490 assertions, zero LLM calls, 100% green. The engine is framework-agnostic.Engine.evaluate()doesn't care whether the caller is LangGraph or CrewAI. Re-running every cell was redundant.

The field test's real job was adapter proof — does each framework correctly surface allow, audit, escalate, and deny in a real agent loop? That's a covering problem, not a cross-product problem.

So I split it into two plans.

Plan A — one scenario per agent (83 runs).Each agent gets exactly one scenario. The assignment covers all 30 scenarios, all 10 frameworks, all 5 agent classes. Result:83/83, 100%.

Plan B — per-framework decision-type proof (123 runs).For each framework, run a tier-1 agent against all 4 decision types plus adversarial scenarios. Result:116/123, 94%.

Together:206 runs instead of 2,490. Same coverage — 30/30 scenarios, 83/83 agents, 10/10 frameworks, 5/5 classes. ~12x reduction.The full coverage rationale is in§8 of the field test report.

This is the part I'm most proud of. Not the engine — that's straightforward. The covering design. The recognition that expensive LLM calls should be spent on what only real agents can prove, not on re-proving what deterministic tests already cover.

The full cross product would have taken ~12 days. The covering design took one afternoon. Same confidence. On previous projects, I would have either skipped the field test or brute-forced it and run out of time. This time, I optimized.

## What the 7 Failures Taught Me

The 7 Plan B failures were the most valuable part of the field test. Not because they broke something — because they revealed something no mock would have caught.

All 7 shared one pattern:not-available. The guard never fired because the LLM didn't call the tool. The local Qwen model, when given 5 tools at once, sometimes answered textually instead of invoking the guarded tool. The engine never got a chance to decide.

A mock agent always calls the tool. A real 4B model sometimes doesn't.

Never interpretnot-availableas a policy failure.It means the LLM didn't call the tool. That's different fromunexpected-decision— when the guard ran and the engine made the wrong call. Only the latter is a real regression.

Every tool call that actually executed in Plan B produced the correct decision. The 7 failures pointed at the LLM, not the engine.

This matters for CI. If you fail onnot-available, your gate is flaky because of model nondeterminism. If you fail only onunexpected-decision, your gate is strict but stable. Thefield test reportrecommends committing a goldennot-availableallowance so CI fails on real regressions, not on the LLM having a bad day.

I couldn't have learned this with mocks. It took 83 real agents.

## The Replan Loop

The result I'm most satisfied with: the deny → replan → allow safety loop.

When an agent triesdrop_database, the engine denies it. A good agent doesn't just stop — it replans. It picks a different, benign tool. The engine allows it. Both calls are audited.

@adapter.guard
(

 
tool_name
=
"
drop_database
"
,

 
action
=
"
delete
"
,

 
environment
=
"
production
"
,

 
data_class
=
"
restricted
"
,

)

def
 
drop_database
(
db
:
 
str
)
 
->
 
str
:

 
return
 
f
"
dropped 
{
db
}
"

@adapter.guard
(

 
tool_name
=
"
query_audit_log
"
,

 
action
=
"
read
"
,

 
environment
=
"
production
"
,

 
data_class
=
"
internal
"
,

)

def
 
query_audit_log
(
query
:
 
str
)
 
->
 
str
:

 
return
 
f
"
audit rows for 
{
query
}
"

# Agent tries drop_database → engine denies (delete in production)
# Agent replans → calls query_audit_log → engine allows (read in production)
# Both decisions audited. Agent redirected, not blocked.

Enter fullscreen mode

Exit fullscreen mode

Tested across all 8 LLM frameworks.8/8 live, 8/8 scripted.Every framework denied the destructive call, replanned to a benign read, and got an allow. The full replan results are in§2.5 of the field test report.

The agent isn't blocked — it's redirected. And every step is on the audit trail. This is the pattern I'll build on in v0.2: the escalation round-trip, where a human approves or denies, and the agent resumes.

## What I Learned

On previous projects, I learned that field testing should be planned, not improvised. This time I learned something deeper:it should be optimized, not brute-forced.

The covering design — Plan A + Plan B — is the application of that learning. 206 runs instead of 2,490. Same coverage. The expensive resource spent on what only real agents can prove. The progression: skip it → add it late → plan it from the start → optimize it. Four projects, four steps.

Zero mock agents is the right call.The integration cost is real — 8 compatibility wrappers, 3 pyproject fixes, 1 quarantined C extension, 12 framework quirksdocumented in the report. But every fix caught a real bug that a mock would have hidden. The cost of mocks is invisible until production. The cost of real agents is visible from the first run.

not-availableis not a policy failure — it's an LLM reliability signal.Distinguishing it fromunexpected-decisionis the difference between a flaky CI gate and a strict one.

Fail-closed everywhere is non-negotiable.DD-14, written before the first line of code.

The replan loop works at scale.8/8 frameworks. The agent isn't blocked — it's redirected.

10 frameworks is the right number for v0.1.Enough to prove the adapter contract generalizes. Not so many that integration drowns the engine. The 8 that needed LLM calls all passed. The 2 self-test frameworks ran deterministically in CI.

## What You Can Use

Building agents with tools?pip install agent-tooltrust, runtooltrust init --posture balanced, decorate your tools. Four-state decisions with explanations and audit trails. No infrastructure. Thequickstartwalks through it.

pip 
install 
agent-tooltrust
tooltrust init 
--posture
 balanced

Enter fullscreen mode

Exit fullscreen mode

Have existing OPA/Rego policies?The dual backend reuses them. Same input, same output. No rewrite. TheAPI referencecovers both.

Want to observe before enforcing?Shadow mode (dry_run=True) logs every decision without blocking. Deploy, observe, tune, enforce.

Using LangGraph, PydanticAI, CrewAI, OpenAI Agents SDK, Google ADK, AutoGen, LlamaIndex, or smolagents?There's an adapter tested against real agents. Theintegration guidehas per-framework wiring.

## How You Can Extend It

Custom risk functions— register your own with@tooltrust.risk_function, plug into the weighted sum, don't touch the engine.

Community policy packs— map a tool ecosystem (GitHub admin, AWS cost ops, Notion writes) onto the taxonomy.tooltrust pack validate,tooltrust pack add.

New audit sinks— theAuditSinkinterface is pluggable. Splunk, Datadog, whatever your SIEM is.

New framework adapters—BaseAdapteris three methods. Extract the context, forward to the engine, surface the decision. Maybe 50 lines. The pattern is proven across 10 frameworks.

Custom posture presets— the three shipped presets are YAML files. Fork one, tune thresholds, ship your org's default.

Thearchitecture docand14 design decisionsare in the repo if you want the internals.

## What's Shipped

Repo:github.com/deghosal-2026/agent-tooltrustPyPI:pip install agent-tooltrust(v0.1.1)

2,490 deterministic tests. Ruff 0. Mypy strict 0. Docker pass. SWE-bench verified. OWASP 5/10. OpenSSF Silver. 10 frameworks, 83 real agents, 30 scenarios, zero mocks. 83/83 Plan A. 116/123 Plan B. 8/8 replan loop. Branch protected. Repo public.

This is v0.1.0. The engine is shipped and proven. The platform — escalation round-trip, policy packs, rule composition, HTTP /authorize, replay detection, child-agent delegation — is 32 open issues for v0.2.0. TheWBStracks it all. Thefield test reportis honest about what's proven and what's not.

## Questions

* What happens when your agent tries to call a tool it shouldn't? Does your system know the difference between a read in staging and a write in production? Or are you using an allow-list and hoping?
* If you've field-tested agents across multiple frameworks, what broke first — the policy, the adapter, or the LLM? Did mocks hide problems that surfaced later?
* Has anyone hit thenot-availableproblem — the LLM doesn't call the tool and you can't tell if it's a policy failure or a model issue? How do you handle it in CI?
* Is four-state (allow/audit/escalate/deny) the right granularity, or overkill compared to binary? Theauditstate was the one I wasn't sure about.
* For OPA/Rego users — does dual-backend (YAML + Rego) make sense, or would you rather have Rego-only?
* The covering design cut the matrix 12x. Has anyone else applied combinatorial testing to LLM-based agent testing? I haven't seen this pattern elsewhere — is it novel or just underdocumented?

Therepohas the fullPRD,architecture,design decisions,field test plan, andfield test report. Star it, fork it, break it. I'd rather you break it now than after you ship it to production.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse