---
title: 'AI Agent Governance on AWS: Block Agents, Prove EU AI Act Compliance - DEV Community'
url: https://dev.to/aws-builders/ai-agent-governance-on-aws-block-agents-prove-eu-ai-act-compliance-1829
site_name: devto
content_file: devto-ai-agent-governance-on-aws-block-agents-prove-eu-a
fetched_at: '2026-09-30T22:50:57.936403'
original_url: https://dev.to/aws-builders/ai-agent-governance-on-aws-block-agents-prove-eu-ai-act-compliance-1829
author: Sarvar Nadaf
date: '2026-09-29'
description: I built a synthetic multi-agent loan crew on Amazon Bedrock and made Traccia hard-block a runaway agent, redact applicant PII across every sub-agent, and export EU AI Act audit evidence. Two of my three governance policies blocked nothing - and not because I misconfigured them. Why is the useful part. Tagged with aws, ai, governance, discuss.
tags: '#discuss, #aws, #ai, #governance'
---

Includes a video walkthrough and cost breakdown

Every fact here is verified against an actual run (Amazon Nova Pro us-east-1 on-demand, Strands Agents, and traccia 0.1.29 $0.0008 per 1K input and $0.0032 per 1K output; EU AI Act Annex III credit-scoring obligations apply 2 December 2027). The demo system is SYNTHETIC throughout.

Observability told me the agent approved a loan it should have declined. It showed me the run that leaked an applicant's email into the logs. Then it did nothing, because watching is the only thing it does.

Part 1 of this seriesput a real observability layer under a multi-agent AWS crew and caught a run that looked healthy while it silently overspent. This part is about the two things observability cannot do:stopthe bad run, and hand a regulator the paperwork afterward. So I built a synthetic multi-agent loan-decision crew on Amazon Bedrock, wired it to Traccia, and made four things happen on real infrastructure: a prompt injection hard-blocked before any model call, applicant PII redacted across every sub-agent's trace, EU AI Act evidence stamped on every span, and the platform itself denying a runaway agent with a real, cited decision.

Then it did not work. Two of the policies I wrote denied nothing, and not because I misconfigured them: two of the three policy types structurally had no signal to match in this crew. Working out why is the most useful part of this article, because it is the part nobody writes down.

How I tested this:the build, the afternoon the platform refused to block, the two real bugs I fixed, and the critique near the end are all mine. Everything on screen is real (real Nova Pro calls, real governance decisions, real exported evidence), the crew is synthetic on purpose, and it producesevidence, not compliance- a distinction that runs through the whole piece. The $0 SDK layer needs no account. After Part 1, the 14-day free trial on the premium platform tier (@governenforcement and the Governance Hub) is what pushed me to dig in and pull out something meaningful for the community, so everything here is reproducible at no cost.

This is for people already running agents on AWS (Strands, CrewAI, LangGraph, or your own loop on Bedrock) who have heard "EU AI Act" enough times to be nervous, and who want runtime guardrails plus audit evidence without rewriting the app around a compliance framework. Where the governance vocabulary is new, I define it the first time it shows up.

If you have two minutes, skip tothe platform payoff, and why it did not work at first. The build-up matters, but that section is the point.

Contents

* Why agent governance is a different problem
* The crew, and why it is synthetic
* Two layers, and only one needs a key
* Prerequisites
* The three $0 governance beats
* The platform payoff, and why it did not work at first
* The evidence a regulator asks for
* Real-time enforcement vs scheduled detection
* The timing that makes this worth doing now
* An honest take on Traccia governance
* Honest caveats
* FAQ

## Why agent governance is a different problem

Observability answers "what did the agent do, and what did it cost." Governance answers a harder pair: "can I stop it from doing the wrong thing, and can I prove what happened." Those are not the same layer, and a trace alone gives you only the first.

For a deterministic service, governance is mostly access control and input validation. Both are loud, and both are enforced at the edge before any work starts. An AI agent breaks that. It decides its own control flow, so a block has to interrupt a reasoning loop that is already running. It calls tools in an order you did not hardcode, so a runaway is a genuine failure mode, not a hypothetical.

And when it is amulti-agentcrew, the failure surface multiplies three ways. A block has to stop thewholecrew, not one sub-agent. Redaction has to covereveryspan in the tree, not just the entry point. And the agent that actually burns the budget may be three delegations deep from the one you wrapped.

There is regulation attached to this now, not just good practice. The EU AI Act names credit scoring as a high-risk use (Annex III, point 5(b)) and attaches concrete obligations: record-keeping (Article 12), transparency to deployers (Article 13), human oversight (Article 14), post-market incident reporting (Articles 72 and 73), and for some deployers a Fundamental Rights Impact Assessment (Article 27). Article 50 transparency, telling a person they are dealing with AI, is already enforceable. So "governance" here is concrete: a specific list of things a specific regulator will ask you to show.

A quick vocabulary anchor, because the rest leans on it. Aguardrailinspects an input, an output, or a tool call and decides whether it is allowed. Apolicyis a rule the platform enforces at runtime (a spend cap, a tool-call cap, an allowed-model list).Enforcementis what happens when a policy matches: the call is denied.Evidenceis the durable record of all of it. The whole article is putting the right guardrails and policies on the right agents, then reading the evidence back.

## The crew, and why it is synthetic

A supervisor loan officer delegates to three specialists, using the AWS Strands agents-as-tools pattern, each calling Amazon Nova Pro (amazon.nova-pro-v1:0).

* Intakeparses the applicant's free text into an id and a requested amount. PII lands here first, which is why redaction gets tested here (though it covers every span).
* Credit & Risk(credit-risk) calls amockcredit_scoretool and a region-restrictedpull_bureau_report. This is the agent that makes the tool calls. Remember it, because it is the whole plot of the platform-block section.
* Policyapplies a deterministic, explainable lending rule (income-to-debt and requested-amount-to-income, never a protected attribute) and returns approve, refer, or decline.

Two more guardrails sit at the boundary alongside the injection block: anoutput-validationcheck that rejects any recommendation making an absolute approval claim, and afairnesscheck that rejects a decision if a protected attribute drove the score. Fairness carries real weight here, because it is the whole reason credit scoring is high-risk under the EU AI Act. So the crew asserts on the scoring signals and blocks if a protected attribute ever appears.

Multi-agent earns its place too. It makes governance harder in exactly the ways that matter, and a single-agent demo hides all three problems: the block has to stop the whole crew, the redaction has to span the whole tree, and a crew can genuinely run away, so a loop cap is believable rather than contrived.

Now the honesty that has to be up front:the credit score is a mock.There is no real bureau, no real model decision, no real applicants. The scoring is a deterministic heuristic that uses only legitimate financial signals and, by construction, never touches a protected attribute (there is a unit test that asserts exactly that). A real high-risk credit system needs a legal conformity assessment; this project produces theevidence substratesuch a system would generate, not the compliance itself. I label everything "synthetic" on screen for the same reason: a governance demo that pretends to be a real lender is the opposite of trustworthy.

## Two layers, and only one needs a key

Traccia's governance splits into two layers, and getting the split right is most of this article.

Layer

Needs a key?

What it does

SDK / in-process

No ($0, offline)

Guardrail detection, an explicit hard-block, PII redaction, EU AI Act stamping, transparency evidence, an integrity hash. All run as OpenTelemetry span processors before export.

Platform

Yes (
TRACCIA_API_KEY
)

@govern
 networked enforcement (Spend Cap, Model Boundary, Loop Cap), plus the Governance Hub: system registry, human review, incidents, evidence packs, FRIA.

@observegives you observability on any OTLP backend, no key.@governadds runtime policy enforcement and needs the platform. The load-bearing point, stated plainly because it is easy to blur:the local hard-block and PII redaction run in-process regardless of the key.The key does not power the block. What the key adds is thenetworkedenforcement and the audit hub. So the honest framing is "the SDK governs locally; the platform enforces and records," not "you have to pay to block anything."

One more piece of honesty about the SDK layer, because I read the source to be sure: a Traccia guardraildetects, it does not enforce. The three-tier engine writes findings to spans. The "block" in Beat 1 below ismy own code raisingon a guardrail result, not the guardrail engine stopping anything. Keeping that distinction straight is the difference between describing the tool accurately and overselling it.

## Prerequisites

Three things, and only the third is for the platform payoff.

1. Python 3.10+and the SDKs (strands-agents,strands-agents-tools,traccia,boto3). The repo pins tested versions inrequirements.txt(traccia 0.1.29, strands-agents 1.56.0, boto3 1.43.99).
2. AWS credentialswithbedrock:InvokeModelon Nova Pro. The repo ships a least-privilege policy atiam/bedrock-invoke-policy.jsonthat allows InvokeModel onamazon.nova-pro-v1:0only. You also enable Nova Pro once in the Bedrock console underModel access(the console grant is not an IAM permission, so you need both). "$0 Traccia" still means real Bedrock calls, so this is required to run the crew at all.
3. A Traccia platform key(TRACCIA_API_KEY)onlyfor the@governenforcement and the Governance Hub. Everything else runs without it.

Getting it running is clone, set up, and go:

git clone https://github.com/simplynadaf/ai-agent-governance-aws.git

cd 
ai-agent-governance-aws

ls
 
-a
 
# no .env here - only the shipped .env with keys commented out

cat
 .env 
# proves the $0 beats need no key

make setup 
# venv + pinned deps + git hooks

make 
test
 
# 10/10 unit tests: pure logic, no AWS, no key

Enter fullscreen mode

Exit fullscreen mode

A fresh clone runs the $0 beats withno key. The tracked.envships with the key lines commented out, socat .envon camera is the proof that "$0, no key" is real rather than a footnote. Your real key goes in that same file locally; a pre-commit hook blocks any commit that contains an uncommented key.

## The three $0 governance beats

These run with nothing but the install and AWS credentials, writing traces to a localtraces_gov.jsonlfile.

### Beat 1: hard-block a prompt injection

A detector decorated with@observe(as_type="guardrail")returns a bool, and the SDK auto-setsguardrail.triggeredfrom it. Your own code raises on that. The crew stops before the supervisor ever calls the model.

@observe
(
as_type
=
"
guardrail
"
,
 
attributes
=
{
"
guardrail.category
"
:
 
"
prompt_injection
"
,

 
"
guardrail.enforcement_mode
"
:
 
"
block
"
})

def
 
injection_check
(
text
:
 
str
)
 
->
 
bool
:

 
return
 
any
(
kw
 
in
 
text
.
lower
()
 
for
 
kw
 
in
 
INJECTION_KEYWORDS
)

# in the crew entrypoint:

if
 
injection_check
(
text
):

 
raise
 
BlockedByGuardrail
(
"
Prompt injection detected. Crew blocked before any model call.
"
)

Enter fullscreen mode

Exit fullscreen mode

The proof is not the log line, it is the trace:the blocked run has zero sub-agent spans.Intake, Credit & Risk, and Policy never ran. I verified this by counting spans in the exported file: the blocked trace contains only the injection check and the crew root. A block that truly stops a multi-agent crew leaves nothing downstream, and the trace is where you confirm that instead of trusting a print statement.

One naming detail worth being honest about: the SDK's real signal isguardrail.triggered(auto-set from the guardrail's bool return). The crew-stopped flagdemo.crew.blockedis my own attribute, not an SDK one. I keep the two distinct so nobody thinks the SDK is doing something it is not.

### Beat 2: redact PII across every sub-agent

init(redact_pii=True)adds a regex processor that masks email, phone, and SSN to[REDACTED_EMAIL],[REDACTED_PHONE],[REDACTED_SSN]oneveryspan in the tree, before export. I verified it the only way that counts: searched all span attributes for the literal test email and SSN. Zero matches, across the whole multi-agent tree, not just the intake entry point.

Honest limit, out loud: this isbest-effort regex, not ML NER. It catches labeled patterns like emails and SSNs; it will miss names, addresses, and unlabeled ids, and it can over-redact. In a real system you say that plainly and layer a real PII classifier on top.

### Beat 3: stamp EU AI Act evidence

init(compliance={"frameworks": ["eu_ai_act"], "risk_tier": "high"})putseu_ai_act.risk_tier=highon every span automatically. Credit scoring is a textbook Annex III point 5(b) case, so I stampeu_ai_act.annex_iii_category="5b_creditworthiness"by hand. That distinction is deliberate and verified against the SDK source: the SDK auto-writesrisk_tier, but the Annex III key is a reserved constant that is never auto-populated, so if you want it, you set it.disclosure()records Article 50 transparency, and every span carries an automaticgovernance.integrity_hash.

A plain-language report reads straight from the trace file, so a compliance reviewer never has to open raw span JSON:

AGENTS THAT RAN: loan-prescreen, intake, credit-risk, policy
GUARDRAIL TIERS: A explicit YES · B provider-native "not observed" · C heuristic YES
EU AI ACT: risk_tier N/N spans · annex_iii YES · Art.50 YES · integrity_hash YES
PII LEAK CHECK: raw test PII found in 0 places (must be 0)

Enter fullscreen mode

Exit fullscreen mode

Here is the honesty note most tutorials skip, and myverify_trace.pynow prints it. Traccia's guardrail engine has three detection tiers:A(explicit, your@observeguardrails),B(provider-native, fires when the model itself returns a safety or stop signal), andC(heuristic, fires when a tool span errors with a denial keyword). I show A and C firing (the injection block is A; the region-restricted bureau pull that errors for an EU applicant is C).Tier B does not fire on a clean run, and that is expected, not a gap. So the honest claim is "A and C demonstrated; B fires on the model's own safety signals," never "all three fire."

## The platform payoff, and why it did not work at first

Here is the afternoon I lost, and the lessons that came out of it.

I set@govern(fail_open=False)on the crew entrypoint, put the key in.env, and ran it. Result:ALLOWED. No block.

Before any policy could even be evaluated, there was a setup gotcha to clear.@governneeds a tracingendpoint, not just a key. WithoutTRACCIA_ENDPOINTset, the SDK logs "Traccia endpoint not found," silently skips enforcement, and returns ALLOWED. I setTRACCIA_ENDPOINT=https://api.traccia.ai/v2/traces, and the warning went away. Now enforcement was actually running, so the real diagnosis could start. It still returned ALLOWED.

Then I created aModel Boundarypolicy that only permittedgpt-4o(the crew uses Nova Pro), scoped it to the crew agentloan-prescreen, set it to Block, and activated it. Ran again.Still ALLOWED.That was the first policy that should have blocked and did not.

The Decision Log in the dashboard is what cracked it. It groups per-call policy checks by trace, and every row said the same two things:No Match, and the check was attributed to agentcredit-risk, notloan-prescreen.

The Decision Log is the screen that cracked this for me. Each row is a per-call check tied to a trace. The No Match rows told me why my first policies failed; the Denied row (Loop Cap, credit-risk, "tool calls 2 exceed 1") is the block that finally worked. Every check is attributed tocredit-risk, not the@governentrypoint.

Two lessons fell out of that, and they are the content the docs and the reference paper do not have.

Lesson 1: scope the policy to the agent that actually makes the calls.My crew wraps each sub-agent in a Strandsrun_identity, so the per-call policy check runs under the sub-agent's identity (credit-risk), not the@governentrypoint's (loan-prescreen). A policy scoped to the entrypoint never matches, because no call is ever attributed to it. Scope to the sub-agent, or org-wide.

Lesson 2: match the policy type to what the spans actually carry.I re-scoped aSpend Capwith a $0 budget tocredit-risk. Still No Match. The two span checks in each trace are the twotoolcalls (credit_scoreandpull_bureau_report), and their cost is about zero, so a spend rule has nothing to trip. A Model Boundary needs an auto-patched LLM client to inspect the model in use, and a StrandsBedrockModelis not one of the clients Traccia auto-patches. So neither policy type can match this crew, for two different reasons.

ALoop Capcounts tool calls per run. The crew makes exactly two. So I set Max Tool Calls Per Run to 1, Block, scoped tocredit-risk, activated it, and ran:

PLATFORM BLOCK - AgentBlockedError
:

 
reasons 
:
 
[
'
tool
 
calls
 
2
 
exceed
 
1'
]

 
decision_id 
:
 
b5a3a3e4-6b62-4c81-9c07-358773735d44 (varies per run)

 
remaining_budget_usd
:
 
None

Enter fullscreen mode

Exit fullscreen mode

The active Loop Cap: Max Tool Calls Per Run = 1, scoped tocredit-risk, enforcement Block. This is the only one of the three policy types whose signal actually exists in this crew's spans.

That is a real, networked deny with a reason and a decision id (the id is fresh on every run). A subtle but important detail I verified in the SDK source: those populated fields (reasons, a realdecision_id) come from theper-call deny path. A block from the lagged status check raises abareAgentBlockedErrorwith empty reasons and no id. So a block that shows a real reason string and a decision id is proof the per-call policy engine denied it, not that an auth failure or a status breaker tripped.remaining_budget_usdisNonebecause this is the loop path, not the spend path (only a Spend Cap deny populates that field).

This is not a case of "Loop Cap good, the other two bad." Runtime enforcement depends onwhere the model call is visible to the governance planeandwhich agent identity carries the call.For a tool-heavy Strands crew with near-zero LLM cost, a Loop Cap is the policy type whose signal actually exists in the spans. The Decision Log's "N span checks, No Match versus Denied" tells you both facts at once, which is why it is the screen I kept open the whole time.

I fixed two real bugs along the way, both committed: the crew entrypoint was forwarding the whole prompt sentence asapplicant_id(aKeyError), and the platform init was passing the key without the endpoint. Neither was exotic; both are the kind of thing you only find by running it for real against the platform.

## The evidence a regulator asks for

Once a real block exists, the Governance Hub turns it into paperwork. Working from the single blocked trace, I registered, reviewed, logged, and exported.

The Compliance Hub after the run: Readiness 85, one registered AI System, one pending review, one open incident. These are real, non-zero, and every one traces back to the single blocked run.

From that one blocked trace I built the paper trail a regulator expects. I registered the crew as a high-risk AI System (Article 12 record-keeping) with risk tier High, three agents linked, and an Annex III 5(b) intended purpose, which moved the registry from 0 systems to 1. I requested a human review on the blocked trace (Article 14 human oversight), and the Reviews tab went to Pending 1. I logged an incident (Articles 72 and 73), "Loop Cap block: credit-risk exceeded tool-call cap (2 > 1)," carrying the decision id and trace, and the Incidents tab went to Open 1. Finally I exported an audit bundle (Article 12 / Annex VIII), which is the payoff artifact: one hash-sealed JSON, about 10 KB, that ties everything together.

The Audit Bundle is one hash-sealed JSON that snapshots the registered system, the policy decisions, the human review, the incident, and the admin audit trail. Verified contents: the High-risk system with three linked agents,review_requests_count 1with the blocked trace id inside it,incidents_count 1,audit_events_count 110, and a top-levelintegrity_hash.

Turning on the EU AI Act module in Settings then unlocked the EU-specific artifacts: aFRIA draft(Article 27), plusInstructions for Use(Article 13), anAnnex IVtechnical-documentation outline, and anEU registration pre-fill(Annex VIII). Each is a real export tied to the registered system.

The FRIA wizard (Article 27), tied to the registered high-risk system. It exports a draft JSON with the real ai_system_id and a completion percentage, another artifact a deployer of a high-risk system is expected to produce.

Honest limits again, because a governance tool that overclaims is worse than no tool:

* @governdefaults tofail_open=True. If the platform is unreachable, execution continues. I setfail_open=Falsefor a high-risk crew, but that only hardens the before-run status check.The per-call policy check is always fail-open, with no override, so a network blip mid-run lets that individual call through. The on-camera block is a real per-call deny, but it is not a guarantee the platform can never miss a call.
* integrity_hashis a plainunkeyed SHA-256. It is tamper-evidence, not a signature. Anyone who can rewrite the bundle can recompute the hash.
* The EU registration export is a pre-fill, and it says so:annex_iii_categorycomes back null because the registry field is not auto-populated from the SDK span stamp, and the export carries a disclaimer thatTraccia is not the official EU registry.
* Evidence substrate is not legal compliance.A lawyer or a notified body still decides conformity. This produces the record; it does not sign off on it.

## Real-time enforcement vs scheduled detection

One thing confused me on the dashboard, and it is worth 30 seconds because it looks like a bug and is not. The Policies page showed "Open Violations 0" even though I had real blocks. The reason is that Traccia has two policy families that surface in different places:

* Preventive (per-call)policies (Loop Cap, Spend Cap, Model Boundary) act inreal time, before each call, and show up instantly in theDecision Logas "Denied" (plus theAgentBlockedError). My block is one of these.
* Detective (monitoring)policies (Output Token Limit, Cost Spike Alert) evaluateafterthe run, on aschedule(shortest cadence is hourly), and feed theOpen Violationstile.

So "Open Violations 0" next to Denied rows is correct: the block is a real-time preventive deny, and a detective violation only opens on the next scheduled tick. I added a detective Output Token Limit policy to demonstrate the second path, and after the hourly evaluation Open Violations went to 1. The lesson for anyone building this: do not wait on camera (or in a demo) for the hourly tick, and narrate the distinction. Real-time block is the Decision Log; scheduled detection is the violations tile.

For completeness on the live numbers, after running the crew a few dozen times the registered agent showed the following.

Per-agent cost and posture for the crew: 37 executions, a 43% error rate, and a 7-day cost around $0.002. The error rate is high on purpose, because every demo run includes a deliberate injection attempt and every@governdeny raises an error by design. A high error rate here is the guardrails firing, not a defect.

The 37 executions and the near-zero cost are honest, not throttled or trimmed: each run is a short sequence of Nova Pro calls, and I did not fake a single one of those numbers to look better. Treat the 43% error rate the same way, as the guardrails and denies doing their job, not a reliability problem.

## The timing that makes this worth doing now

Article 50 transparency obligations became enforceable on 2 August 2026. The Annex III high-risk obligations for credit scoring apply from 2 December 2027. That is a preparation window, not a free pass, and building the evidence layer before the deadline is far cheaper than retrofitting it after. (Verify these dates on your publish day; regulatory timelines move, and the kind of omnibus adjustments that shift them are exactly the thing to double-check.)

## An honest take on Traccia governance

I shipped a real crew against this and read the SDK source to understand the behavior, so here is the assessment grounded in that, the parts that earned their keep and the parts that cost me an afternoon.

What earned its keep, first. The two-layer split does real work at $0: you get real governance in-process (block, redact, stamp) without a key, and the key adds networked enforcement plus the audit hub. The free tier is not a demo-ware teaser; it does the real work with no account attached. The Decision Log is the best diagnostic in the product. "N span checks, No Match versus Denied, attributed to agent X" told me both why my policy failed and how to fix it, and without it the two lessons above would have been a much longer afternoon. The evidence hub also maps cleanly to real EU AI Act articles: registry, review, incident, evidence pack, FRIA, and the EU exports line up with Articles 12, 13, 14, 27, 72/73, and Annexes IV and VIII, which is worth a lot to a team that needs toshowsomething. And it does not oversell itself in the exports; the disclaimers ("not the official registry," the unkeyed hash) are baked into the product output, not just something I added in this article.

Now where it made me work, and where it should be better:

* The endpoint requirement is silent.@governskips enforcement without an endpoint (at the time of writing). Set only the key and you get ALLOWED with a log line most people miss. A hard error, or a louder warning, would save the confusion.
* The always-fail-open per-call check deserves a louder callout.fail_open=Falsereads like "this will always stop," but it only hardens the status check; the per-call engine still fails open. That is a defensible design (a network blip should not hard-fail a production call), but it is exactly the kind of nuance a high-risk deployer needs stated up front.
* The per-call identity attribution is a genuine gotcha for multi-agent crews.That the check runs under the sub-agent'srun_identity, not the@governentrypoint, is correct behavior, but it is undocumented for this case and it is exactly where a multi-agent build goes wrong first.
* Documentation is the real gap, same as in Part 1. I learned the identity precedence, the endpoint requirement, the always-fail-open per-call rule, and the policy-matching logic by running the platform and reading the source, not from docs. The capability is there; the guidance for a multi-agent Strands build is not written down yet, which is precisely the gap this article fills.

Net: the governance is real and the evidence structure is genuinely useful. The gaps are documentation and a couple of developer-experience papercuts, and I would not wave all of them away as stage-of-product growing pains. For a tool whose entire value is trustworthy audit evidence, shipping always-fail-open per-call behavior that is not documented is more than cosmetic; a high-risk deployer needs that surfaced, not discovered. The capability is there and it works. The guidance and a few defaults have not caught up to it yet.

## Honest caveats

* The loan crew issynthetic. The credit model is a mock, the applicants are invented, no output is a real decision. This produces evidence, not compliance.
* The local block and PII redaction run in-processwith or without the key. The key adds networked enforcement and the hub, not the local guardrails.
* A Traccia guardraildetects; it does not enforce. The Beat 1 block is my own control flow raising on a finding.
* PII redaction isbest-effort regex, not ML NER. It misses names and addresses and can over-redact.
* integrity_hashis anunkeyed SHA-256: tamper-evidence, not a signature.
* @governdefaultsfail_open=True; the per-call check isalwaysfail-open, even when you setfail_open=False.
* I show guardrail TiersA and C; Tier B is provider-native and does not fire on a clean run. Do not claim all three fire.
* Every dollar and token count is real, but they shift run to run. Treat the relationships (a crew makes two tool calls; a Loop Cap of 1 blocks it) as the lesson, not the exact decimals.
* The block that works is aLoop Cap scoped tocredit-risk, not a Model Boundary or Spend Cap, for the reasons in the payoff section. Your policy choice depends on what your spans carry.

The takeaway is not "buy a governance tool." It is that watching a failure and stopping one are different layers, that in a multi-agent crew the enforcement has to target the agent that actually makes the calls, and that the audit evidence is something you generate on purpose, before a regulator asks.

## FAQ

What is AI agent governance, and how is it different from observability?Observability records what an agent did and what it cost. Governance decides whether the agent is allowed to do it (guardrails and runtime policies) and produces a durable audit record. Observability watches; governance blocks and proves.

Can I block a runaway agent without a paid platform?You can block locally with an in-process guardrail that raises (the injection block here runs at $0, no key). What needs the platform isnetworkedenforcement: a Loop Cap, Spend Cap, or Model Boundary the platform evaluates on every call and denies with a decision id you can cite.

Why did my@governpolicy not block anything?Three usual reasons, all of which I hit. You did not setTRACCIA_ENDPOINT, so the SDK skipped enforcement silently. You scoped the policy to the@governentrypoint agent, but in a Strands crew the per-call check is attributed to the sub-agent'srun_identity. Or you picked a policy type whose signal is not in your spans (a Spend Cap on a ~$0 crew, or a Model Boundary on a non-auto-patched client). Open the Decision Log; "No Match versus Denied" tells you which.

How does this map to the EU AI Act?Credit scoring is Annex III point 5(b), high-risk. The demo produces record-keeping (Art. 12), transparency to deployers (Art. 13) and to users (Art. 50), human oversight (Art. 14), incident logging (Arts. 72/73), a FRIA draft (Art. 27), and Annex IV / VIII exports. It is evidence substrate, not a compliance sign-off.

Is Traccia open source?The SDK (traccia-py) is Apache-2.0 and OpenTelemetry-native, so the spans are standard OTel and the local governance runs with no account. The@governenforcement and the Governance Hub are the hosted, commercial part.

Does this work with Strands out of the box?The $0 SDK governance (block, redact, stamp) works with any code you can decorate. The platform@governworks too, but the per-call policy matching has the multi-agent identity nuance above: scope to the sub-agent that makes the calls, and pick a Loop Cap for a tool-heavy crew.

## Try it

Prefer to watch it happen first? The full walkthrough is on YouTube:Watch the demo.

The full code (the crew, the three $0 beats, the platform@governscript, the 10 unit tests, and a Makefile) is on GitHub:ai-agent-governance-aws. Clone it, runmake demoto see the local block, redaction, and EU AI Act stamping at $0, then drop a Traccia key into.env, add the endpoint, and runmake platformto get the realAgentBlockedError.

If you run agents in production: do you have a real block in the request path, or an alert that fires after the money (or the bad decision) is already gone? That is the difference this whole article is about.

Follow me for more on AWS architecture, DevOps, and AI Infrastructure:Portfolio|LinkedIn|Dev.to|YouTube|Email|AWS Builder Center|X

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (18 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse