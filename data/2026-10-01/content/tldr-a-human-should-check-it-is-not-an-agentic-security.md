---
title: '''A Human Should Check It'' is Not an Agentic Security Control | CirriusTech | Serious About Tech'
url: https://cirriustech.co.uk/blog/a-human-should-check-it
site_name: tldr
content_file: tldr-a-human-should-check-it-is-not-an-agentic-security
fetched_at: '2026-10-01T23:02:22.042095'
original_url: https://cirriustech.co.uk/blog/a-human-should-check-it
date: '2026-10-01'
description: MSRC assessed an indirect prompt injection into Security Copilot as Low severity because consequential action still required downstream automation or human …
tags:
- tldr
---

A little while ago I demonstrated something fairly simple.

An attacker-controlled HTTPUser-Agentvalue was ingested into Microsoft Sentinel as part of normal security telemetry. Security Copilot then consumed that telemetry while analysing the incident.

TheUser-Agentcontained an indirect prompt injection and Security Copilot followed it.
And, critically, the injected instructions were able to influence the security conclusion reached by Copilot strongly enough that it recommended closing the incident.

That’s the interesting bit.

Not that an LLM could be prompt injected. We have known that for years. Nor that generated output could be wrong. Microsoft quite reasonably documents that Security Copilot can produce inaccurate or incomplete responses and that users should validate important outputs -https://learn.microsoft.com/en-us/copilot/security/security-copilot-application-card

The important bit was much more specific:

Attacker-controlled security telemetry could influence the AI system interpreting that telemetry, and could steer its security decision in a direction favourable to the attacker.

That’s a very different problem.

 ‌‌‌​​‌​​​​‌‌‌​​‌‌​‌​‌‌​‌​‌​‌‌​​​‌‌​​​​​​​​‌​​​‌‌​​​​‌‌​​‌‌​​​‌​​‌​​​‌​‌‌​​​‌‌‌​​‌​​​​‌‌‌‌‌​​‌​​​​‌​‌​‌​‌‌‌‌‌‌‌‌‌‌‌​‌‌‌‌‌‌‌​‌​‌​‌​‌‌​​‌​‌​‌​​​​​‌​‌‌‌‌‌​​​‌‌‌‌​​‌‌​​‌‌​‌​​‌​​​​‌​‌‌​‌​‌​‌‌​‌​‌​​‌​‌​‌​‌​​​‌‌‌‌‌‌​​​​​‌‌​​‌‌​‌‌​‌‌​‌‌​‌‌​​‌‌​​‌‌​‌​‌‌‌‌‌​​‌‌​‌​‌​​ 

I reported it to MSRC. Eventually, after some disagreement about how the report had originally been triaged, MSRC reassessed it and classified it as Low severity. Their reasoning was actually useful, because it exposes a security boundary that I think is going to become increasingly important.
MSRC described the issue as indirect prompt injection influencing Security Copilot’s triage output through an attacker-controlled HTTPUser-Agent, causing Copilot to recommend closing the incident.

So far, we agree.

They then explained that manipulating the assistant’s response does not, by itself, constitute a security vulnerability under the AI Bug Bar. The higher-impact outcome only occurs where a downstream playbook acts on that recommendation without analyst approval.

In other words:

the dangerous part is not the poisoned reasoning itself, but what happens if something trusts that reasoning enough to act on it.

That is a perfectly understandable distinction.
It is also exactly where things get problematic.

## The current boundary

There is an important nuance here.

Microsoft’s AI Bug Bar does explicitly recognise prompt injection as a form ofInference Manipulation. It describes this category as vulnerabilities that manipulate the model’s response to individual inference requests, with severity determined by the resulting security impact. It even gives privileged action or data exfiltration without user interaction as examples of Critical impact -https://www.microsoft.com/en-us/msrc/aibugbar

So the argument isn’t:

prompt injection is not a security problem.

The argument is closer to:

prompt injection becomes a security vulnerability of sufficient severity when it crosses into a concrete security impact.

Again, reasonable.

In the Sentinel case I reported, Security Copilot did not itself autonomously close the incident. Itrecommendedclosure.

To convert that recommendation into an actual incident status change, something downstream had to trust the result and perform the action.

That might be an analyst, or a Logic App or some other automation. And if you deliberately construct a workflow where an AI-generated recommendation is blindly passed into an automated remediation path, then yes, some responsibility clearly sits with the person who built that workflow.

I don’t think that’s controversial.

What I thinkisworth examining is whether that distinction survives contact with where security products are now going. Because “a human should check it” works better as a mitigation for an assistant than it does for an autonomous system.

## AI that assists versus AI that acts

Microsoft itself now makes this distinction explicitly.

Security Copilot is described as the generative AI-assisted interface:AI that assists.

Project Perception is the agentic system:AI that acts-https://www.microsoft.com/en-gb/security/business/ai-powered-cybersecurity/project-perception-agentic-system

That is not me editorialising.

Microsoft describes Project Perception as a coordinated system of red, blue and green security agents operating in continuous loops across end-to-end security workflows. Those agents share intelligence, investigate threats, remediate issues and harden environments -https://www.microsoft.com/en-us/security/blog/2026/07/30/whats-new-in-microsoft-security-july-2026/

Microsoft’s own architecture is even more interesting. Signals and sensors provide awareness. Context turns those signals into something agents can reason over. Models perform reasoning. A harness coordinates models and agents. Agents make decisions. And actuators translate those decisions into protection -https://blogs.microsoft.com/blog/2026/07/27/rethinking-security-for-the-age-of-ai/

Read that sequence again.

Because this is where my little maliciousUser-Agentsuddenly stops looking quite so parochial.

Attacker-controlled signal

 ↓

Security context

 ↓

Model reasoning

 ↓

Agent decision

 ↓

Actuator

 ↓

Security action

That’s almost the exact trust chain I was worried about. The specific implementation is obviously different. Some actions require approval. Humans remain part of the control model.

Good. They should.

But the underlying security question has not gone away.

It has become more important.

 ‌‌‌​​‌​​​​‌‌‌​​‌‌​‌​‌‌​‌​‌​‌‌​​​‌‌​​​​​​​​‌​​​‌‌​​​​‌‌​​‌‌​​​‌​​‌​​​‌​‌‌​​​‌‌‌​​‌​​​​‌‌‌‌‌​​‌​​​​‌​‌​‌​‌‌‌‌‌‌‌‌‌‌‌​‌‌‌‌‌‌‌​‌​‌​‌​‌‌​​‌​‌​‌​​​​​‌​‌‌‌‌‌​​​‌‌‌‌​​‌‌​​‌‌​‌​​‌​​​​‌​‌‌​‌​‌​‌‌​‌​‌​​‌​‌​‌​‌​​​‌‌‌‌‌‌​​​​​‌‌​​‌‌​‌‌​‌‌​‌‌​‌‌​​‌‌​​‌‌​‌​‌‌‌‌‌​​‌‌​‌​‌​​ 

## The thing doing the reasoning is part of the attack surface

One of the traps we keep falling into with AI security is treating model output as somehow separate from the rest of the security system.

If Copilot produces a bad answer, that can be framed as an AI-quality problem. If an agent produces a bad recommendation, that can be framed as something a human should catch. If an automation performs a bad action, we can blame the automation for trusting the model.

Individually, each explanation can be true.

Collectively, they can also hide the architecture. Security systems are composed systems. The juicy failures often live in the joins.

An attacker does not particularly care whether the component they manipulated was formally responsible for the final action. They care whether manipulating component A predictably changes what component B does.

If attacker-controlled data can influence the reasoning layer, and the reasoning layer influences a decision, and that decision eventually reaches something with authority to act, then the whole chain needs to be threat-modelled as a chain.

That does not mean every prompt injection is Critical. Nor does it mean every incorrect recommendation is a vulnerability. And it definitely does not mean that my original report magically becomes Critical simply because Microsoft has now announced an agentic platform.

That would be silly.

Itdoesmean, in my opinion, that we need to be very careful about using human review as the security boundary around a technology whose entire value proposition is increasingly about reducing the amount of human intervention required.

## “Humans remain in control”

This is a good principle. It’s also not the same thing as saying that every security-relevant decision is reviewed manually before it has any effect. Nor could it be.

The entire point of agentic security is that defenders cannot manually inspect every signal, every correlation, every prioritisation decision, every intermediate conclusion and every branch in every playbook. If they could, we would not need the agents.

The interesting security boundary therefore is not simply:

AI proposes

Human approves

Action happens

It is much larger:

Signals are selected

Context is constructed

Evidence is weighted

Incidents are prioritised

Hypotheses are formed

Agents exchange conclusions

Playbooks branch

Actions are proposed

Some actions are automatic

Some actions are approved

An attacker may not need to compromise the final approval step. They may only need to influence something upstream strongly enough that the system never reaches the branch where an approval would have been requested.

Which is whyintegrity of reasoningmatters.
If malicious input causes an investigation agent to conclude that something is benign, perhaps no remediation action is proposed. If malicious input causes a prioritisation system to downgrade an incident, perhaps it receives less scrutiny. If malicious input alters the shared context consumed by multiple agents, perhaps the effect propagates further than a single inference.

I am not saying Project Perception currently does any of those things incorrectly. I have not tested it and that distinction matters.

I am saying those are the questions I now want answered.

## Security telemetry is hostile input

This is the part I think deserves far more attention. Security telemetry is not trusted merely because it arrived in a SIEM. Logs contain attacker-controlled strings all the time.

* User agents
* URLs
* Hostnames
* File names
* Process command lines
* Email subjects
* HTTP headers
* DNS labels
* Cloud resource names
* OAuth application names
* Git commit messages
* Repository metadata
* Ticket text
* Chat messages
* Documents
* Payload contents
* etc.

We have spent decades teaching security systems to ingest hostile data safely at a syntactic level. Do not execute the string. Do not interpret it as SQL. Do not treat it as shell syntax. Escape it before placing it in HTML. Parameterise the query.

Then we attached language models to those systems and created an interpreter whose defining feature is that it tries to understand what stringsmean.

That changes things.

Indirect prompt injection is an attacker placing instructions into external content that the model then misinterprets as legitimate instructions. Security telemetry is an almost perfect delivery mechanism for exactly that class of input.

The data is attacker-influenced.
The defender wants the AI to consume it.
The AI is specifically being asked to reason about it.

And, unlike a webpage summariser, the thing doing the reasoning may eventually have access to security capabilities.

That combination deserves a threat model of its own.

## The trust boundary moves

This is really the point of the post. When I originally reported the Sentinel behaviour, MSRC’s position ultimately depended on a boundary:

Security Copilot can be influenced, but a human is expected to validate consequential output before action is taken.

Today, for the specific workflow I demonstrated, that boundary substantially limits the impact.
Fair enough.

But Microsoft’s security architecture is moving from copilots towards agents, coordinated playbooks and actuators.

The role of the human is changing from:

review each result

towards:

set strategy, define guardrails, approve the things deemed important enough to require approval.

Which is a very different operating model.
And autonomy changes where we have to put our security controls.

If hostile environmental data can influence the system deciding what requires human attention, then “there is a human in the loop” is not, by itself, a sufficient answer because the loop has structure.
The attacker may be inside it before the human is.

 ‌‌‌​​‌​​​​‌‌‌​​‌‌​‌​‌‌​‌​‌​‌‌​​​‌‌​​​​​​​​‌​​​‌‌​​​​‌‌​​‌‌​​​‌​​‌​​​‌​‌‌​​​‌‌‌​​‌​​​​‌‌‌‌‌​​‌​​​​‌​‌​‌​‌‌‌‌‌‌‌‌‌‌‌​‌‌‌‌‌‌‌​‌​‌​‌​‌‌​​‌​‌​‌​​​​​‌​‌‌‌‌‌​​​‌‌‌‌​​‌‌​​‌‌​‌​​‌​​​​‌​‌‌​‌​‌​‌‌​‌​‌​​‌​‌​‌​‌​​​‌‌‌‌‌‌​​​​​‌‌​​‌‌​‌‌​‌‌​‌‌​‌‌​​‌‌​​‌‌​‌​‌‌‌‌‌​​‌‌​‌​‌​​ 

## This is not really about my MSRC case

For completeness, MSRC shared the report with the relevant engineering team for internal review, classified it as Low severity, offered a Special Mention, and closed the case without a CVE or bounty. That is their call.

I disagree with parts of the reasoning, but I am not especially interested in spending the rest of my natural life litigating whether one particular bug should sit in one particular severity bucket because that misses the real question - which iswhat happens when the same class of influence reaches systems intentionally designed to reason and act with progressively less human intervention.

Preview is exactly when these questions should be asked. Can attacker-controlled telemetry alter agent reasoning? Can hostile strings survive transformation into shared security context? Does provenance remain visible to the model?
Can an agent distinguishdata describing attacker behaviourfrominstructions authored by the attacker?
Can poisoned conclusions move between agents?
What actions can occur without approval?
What determines that an action is high impact?
Can manipulated reasoning prevent an approval gate from being reached at all?

What happens when an attacker attacks thedecision about whether something is dangerous, rather than the actuator performing the remediation?

Those are much better questions than whether a chatbot can be made to say something silly.

## Capability changes the threat model

There is a broader lesson here.
AI security cannot be assessed purely at the model boundary.

A model with no authority is one thing.
A model connected to enterprise data is another.
A model that can recommend actions is another.
A model whose output feeds automation is another.
And a coordinated multi-agent system with identities, permissions, shared context, playbooks and actuators is something else again.

The underlying model weakness may be identical in every case but the security impact is not.

That’s why “the model can be prompt injected” is simultaneously both unsurprising and insufficient as a finding.

The real question is:

what capability exists on the other side of the compromised reasoning?

That’s the question I was already asking with Security Copilot.
It becomes considerably more important with agentic security.

I don’t particularly care whether the original report receives a bounty or a CVE.
I care whether we build autonomous defensive systems whose trust model assumes that the information they reason over cannot reason back.

Because it can.
I already demonstrated that part.

Now I want to know what happens when the thing listening to it can act.