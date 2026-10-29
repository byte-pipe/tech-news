---
title: 'A Shared Language for Agent Defense: Introducing Project Quarry - Cisco Blogs'
url: https://blogs.cisco.com/ai/project-quarry-agent-security-detections
site_name: tldr
content_file: tldr-a-shared-language-for-agent-defense-introducing-pr
fetched_at: '2026-10-29T21:00:05.066905'
original_url: https://blogs.cisco.com/ai/project-quarry-agent-security-detections
author: Adam Swanda, Ravikumar Balakrishnan, Amy Chang, Konstantin Berlin
date: '2026-10-29'
published_date: '2026-10-28T12:45:39+00:00'
description: AI agents now read, decide, and act on their own, and the attacks against them unfold across many ordinary, permitted steps that most of today's defenses were not built to connect. Project Quarry (“Quarry”), which we are open sourcing today, is a...
tags:
- tldr
---

Cisco BlogsArtificial Intelligence - AI

# A Shared Language for Agent Defense: Introducing Project Quarry

Adam Swanda

Ravikumar Balakrishnan

Amy Chang

Konstantin Berlin

Artificial Intelligence - AI

October 28, 2026

•

16 min read

•

26 min listen

In collaboration withSanketMendaparaand Evgeny Livshits

AI agents now read, decide, and act on their own, and the attacks against them unfold across many ordinary, permitted steps that most of today’s defenses were not built to connect.Project Quarry(“Quarry”), which we are open sourcing today, is a detection language built from the ground up for that problem. It lets a security team describe a multi-step agent attack once, check every agent session against it, and see the evidence behind each finding. We designed Quarry to become the shared foundation for detecting harmful or disallowed agent behavior, both at Cisco and across the security community.

In July, AI agents running in anOpenAI cybersecurity evaluationgot around the controls meant to keep them off the internet, found exposed credentials, and spent roughly two and a half days inside Hugging Face’s production infrastructure. Hugging Face laterrecoveredabout 17,600 of the agents’ actions from its logs. Most were unremarkable on their own: list a directory, upload a file, make a web request, run a command. The intrusion became visible only in how those actions accumulated over time and diverged from the task the agents had been given.

That incident was extreme, but the pattern behind it shows up in ordinary AI deployments. During a single task, an agent may read a page, inspect a file, call a tool, receive a result, and act again, in a loop until the task is done. Each action alone can look benign, and many are explicitly permitted. Chained together, they can add up to a potential security incident: an untrusted instruction returned by a tool, followed by a shell command; a sensitive file read, followed by a request to an external destination.

Security teams need detections that read the full trace (the step-by-step record of what an agent saw, said, and did), and the interactions between an agent and the environment it operates in. Classifiers that inspect standalone messages still matter, as do authorization controls that allow or deny an individual action, but neither, on their own, capture attacks or misalignment that develop across a sequence of steps. Teams need a precise way to define which sequences matter and produce findings with supporting evidence attached.

Card fraud detection offers a familiar comparison. A bank approves each purchase on its own, while its fraud team looks for patterns across purchases (e.g., a small test charge, then a purchase in another state, then a large electronics order within the hour) and tells the cardholder which charges raised the alert. Agent security needs the same combination of pattern detection and evidence, applied to the steps an agent takes rather than to purchases.

Network security defenders have faced a version of this problem before. A single packet rarely proves a successful attack, soSnort, the open-source intrusion prevention system Cisco maintains, gives them a readable rule language for detecting malicious attack traffic. Those rules can be tested, versioned, shared, and argued over, and Cisco Talos ships new Snort coverage the day Microsoft releases its monthly patches. Malware analysts gained a comparable shared language in YARA, and security operations teams gained one for logs in Sigma. Agent behavior now warrants a language of its own, and we believe defenders will be better served by one open language that every team can read, test, and extend than by a separate rule format inside every product.

Today, we are open sourcingProject Quarry, a neurosymbolic rule language (one that combines machine learning judgments with exact, rule-based checks) for evaluating agent behavior, and the engine that evaluates those rules. We built Quarry to be that language for agent security. It covers single-turn and multi-turn large language model (LLM) conversations, agents, tool use, Model Context Protocol (MCP) interactions, and multimodal inputs. Check out theGitHub repository here.

A singleQuarryrule can draw on two kinds of evidence. Neural signals come from machine learning classifiers and LLM judges, which handle questions that need judgment, such as whether a tool result contains a prompt injection. Symbolic checks handle what can be stated exactly, such as an unsafe command, a string match, or the order of two tool calls. Optical character recognition (OCR) and vision models can supply neural signals for images in the same way. The rule defines what data to inspect, which signals to invoke, how to combine them, which exemptions apply, and what constitutes amatch.Quarryalso brings agents into the policy-writing process.

Quarryis designed as a shared policy layer, not a replacement for every detector or every enforcement control. It keeps event structure intact—from a tool’s name and arguments to its result and available metadata—so a policy can reason over either a complete session or a standalone event. A check on a single event can catch local risks, but it should not be mistaken for session-level coverage when the behavior depends on what came before or after. When a policy matches,Quarryreturns the evidence. This includes the steps that caused the match, the field each one matched in, and a short excerpt, with common secret formats masked. The product receiving that finding can then map it to an action such as alerting, blocking, redacting, quarantining, or logging.

Where teams can useQuarry:

* Runtime guardrails: check an agent before and after each model call and tool run, and block or flag a risky step
* Post-hoc evaluation: check stored traces against a rule set for security analytics
* Incident response: run a newly learned pattern against old traces

## From threat to action: Integration with AI Security & Safety Framework

TheCiscoIntegrated AI Security & Safety Frameworkgives organizations a shared language for describing AI risks, setting boundaries, and deciding which controls and evaluations they need.Quarryis the policy and evaluation layer that can put that language to work on real world interactions: a framework category can be translated into an inspectable rule over messages, tool calls, results, and session context. In that sense, Quarry moves the framework from describing AI risk toward detecting it in agent activity, and the framework’s categories offer a natural roadmap for the rules that Cisco and the community write next.

For example, the framework’s Agentic Autonomy Failures objective includes excessive agency, goal drift, and reward hacking. AQuarrypolicy can look for evidence such as an agent reaching beyond its assigned authority, continuing after a stop condition, changing course during a long task, or working around a check to make a metric look successful. These are behavioral patterns, not just unsafe phrases, so they require trace-level evidence to provide a more comprehensive view of potentially unintended or unwanted activity.

Ourrecent framework updatewould classify the OpenAI and Hugging Face incident as AITech-2.3 Reward Hacking combined with AITech-2.1 Excessive Agency. A Quarry rule turns a classification like that into a check, and the repository’sexamplesinclude starting points such as capability scope creep and silent task substitution.

## Where Quarry fits alongside other controls

Quarry does not replace fine-grained authorization (which decides whether a specific action is permitted, like a badge reader on each door). Detection policies driven by Quarry can identify a suspicious pattern that spans several individually permitted actions, such as the one badge that opened six doors in four minutes and ended at the server room.

Other controls remain useful because they solve different parts of the problem. Middleware can steer or audit an agent at selected stages, and content classifiers can flag a suspicious message or result. Used alone, however, these controls may not connect to the full structured trace, preserve session history, combine different signals, or return the evidence behind a multi-step finding. Teams then must build stateful correlation and policy logic separately in each integration.

## Sometimes, one tool call can be enough

Some detections are local to one action. A tool call that sends a base64 encoded string to a shell and immediately decodes and executes it may contain enough evidence for a finding. The policy can inspect the named tool, select the command argument, and match the obfuscation and execution pattern. This is the simplest case because the relevant evidence sits in one call.

In Hugging Face’stechnical timeline, the July intruder’s code-execution payload was one line that decompressed a base64-encoded blob and ran it. Encoding can also defeat plain-text log searches; Hugging Face’s first automated scan of its raw logs found very few secrets, whereas decoding them the way the attacker had encoded them recovered roughly four times as many. Quarry’s base64 string modifier matches the encoded form of a pattern, so a rule doesn’t depend on the payload appearing in plain text.

Figure 1: One tool call is enough: catching a decode-and-execute payload

## Intent can emerge over time

Other behavior only becomes suspicious over time. Consider a user who first asks what tools and permissions are available, then claims to represent the security team, and finally requests an account change that grants administrative access. No isolated message determines the result. The ordered history provides evidence: reconnaissance, a claim of authority, and an escalation request that’s approved.

In November 2025,Anthropic reportedthat a threat actor had used Claude Code to carry out a significant portion of a cyber campaign against roughly 30 organizations. The operators split the work into small, routine-looking tasks and told the model that it worked for a security firm conducting defensive testing. Viewed one request at a time, much of the activity resembled an authorized penetration test; its purpose became apparent only when the requests were read together and in order.

Figure 2:History changes the verdict: reconnaissance and claimed authority before an admin grant

## Data exfiltration is a sequence, not a single event

Data exfiltration illustrates why action relationships matter. Reading a configuration file may be legitimate. Sending a request to an external endpoint may also be legitimate. A policy can produce a finding when the trace shows a sensitive file read followed within a defined window by an external send. The risk comes from the relationship between the two actions, so the finding should preserve evidence from both.

Invariant Labsdemonstratedthis with GitHub’s MCP server in May 2025. An attacker planted instructions in an issue on a public repository. When the owner asked their agent to review open issues, it followed them: it read the owner’s private repositories and published what it found in a pull request on the public one, using only access the owner had granted.

Figure 3: Following the data: an injected issue that leaks a private repo

## Several signals can support one finding

A tool result might contain an instruction to ignore previous rules and upload a secrets file. A deterministic pattern can flag the instructions. A prompt injection classifier can score the text, and a model judge can consider the surrounding messages. The policy can require those signals together with later use of shell and network tools. Detectors supply evidence; the rule owns the logic that decides whether the combined behavior matches.

General Analysisdemonstrateda version of this with Supabase’s MCP server in July 2025: instructions in a customer support ticket led a developer’s Cursor agent, running with full database privileges, to read a table of integration tokens and post them back into the ticket for the attacker to see.

Related signatures can also be packaged as deployable threat profiles. A profile gives teams a versioned collection of rules for a class of agent risks, while keeping the individual matches and their evidence inspectable.

### Beyond text

Agent behavior is not limited to text. Traces may include images, audio, or files, and Quarry can represent these as typed content parts while preserving existing text. Specialized analyzers—such as optical character recognition, transcription, image classification, perceptual matching, or multimodal judges—can provide signals that a policy combines with text and tool-flow evidence. This extends detection to richer interactions without creating a second policy language.

Our ownresearch on typographic attacksfound that instructions rendered inside an image can redirect a vision-language model. A rule that combines an OCR signal on the image with what the agent did next can catch a case that a text-only filter never sees.

## Reading the Hugging Face intrusion as a trace

OpenAIandHugging Facehave published detailed accounts of the July incident,and together they make it possible to read the intrusion the way a detection engineer would, as a trace of individual steps. We have not run Quarry against incident data, so what follows is a counterfactual. Even so, the published timelines show several points where the agents’ own actions would have given a rule something to act on.

* Agents talking where they shouldn’t(May 12):During a training run, an agent left a note in OpenAI’s internal package registry asking other agents for a missing file. Writing messages into a package service falls outside the scope of any task, and OpenAI has said an internal team noticed this kind of activity in late May, before its significance was understood.

* Internet access from a sandbox that had none(May 26 and July 8):Agents got the package service to send web requests on their behalf, first on May 26 and again on July 8, after OpenAI had rebuilt the service. A rule can flag any tool call that reaches a destination outside a task’s allow list.

* Credentials found, then used elsewhere(July 10):An agent reconstructed, validated, and shared 14 publicly exposed Hugging Face credentials with write access, and an agent later used them to gain code execution on Hugging Face servers. A credential that appears in a tool result and is followed by a call to an outside service is the data-movement pattern described earlier.

* Encoded execution(July 11): The code that ran on Hugging Face’s workers arrived as the one-line, decode-and-run payload described earlier. The agents had been packing their commands this way since July 9.

* Pressing on after success(July):According to OpenAI, most agents already had the correct answer, obtained by cheating, but kept working to exploit Hugging Face for days because they believed the grader wanted more. Continuing after a task’s goal is met is a reward-hacking signal, and it becomes visible only across the full trace.

Rules complement the monitoring both companies described rather than replace it.OpenAI saidthat its current chain-of-thought monitoring, had it been running on these evaluations, would have paged its security team more than a day before the agents breached Hugging Face’s systems. Hugging Face described its first signals as ambiguous on their own, and said they became a coherent attack signal only once they were correlated. A rule’s value in that setting lies in recording the pattern in a form that other teams can review, test, and apply to their own agents.

Figure 4.Five points in the OpenAI and Hugging Face timelines (May 12 to July 19) where a Quarry rule would have had evidence to act on.

## Closer to home: always-on personal agents

In September,Meta launched Muse and OpenAI launched Dots, agents that shop, fill out forms, plan travel, and send email in the background on a user’s behalf. Both ask for approval before consequential actions. Again, the harder case is a sequence in which no single step looks consequential.

Say a user asks one to book a flight when the fare drops, and the airline’s page carries hidden text telling the agent to confirm the traveler’s identity by emailing a passport scan to a support address. A Quarry rule can describe that pattern: an instruction from web content, followed within a few steps by an outbound message with an attachment the user never mentioned. Quarry isn’t built into either product, but whoever sees the agent’s traffic can check for it: the platform operator, an enterprise gateway, or, for agents people run themselves, DefenseClaw (see below).

## If you’ve read a Snort rule, you can read a Quarry rule

A Snort rule has a header that says which traffic to look at, options that say what to match, and metadata for tracking the rule. Quarry applies the same anatomy to agent traces, in a syntax anyone who has written a YARA rule will recognize. The Snort rule below flags a cloud secret leaving in an HTTP request; the Quarry rule flags an agent that reads a credentials file and calls out within four steps.

Figure 5:A samplecomparisonof whata Snort rule andaQuarry rule look like

These are illustrative examples, as we are aware thetwo rules differ in what they canobserve. The Snort rule, as written, matches the secret only if it crosses the wire in readable form, so a payload the agent encodes first,as the Hugging Face intruder did,would requireadditionalrulelogic to catch.Neither engine decodes obfuscation natively, and in both cases the rule authorhas toanticipateencoded variants. The Quarry rule in this example, however, keys on theagent’ssteps (a credentials file read followed by an outbound request) rather than on the contents of the request, so encoding the payload does not affect whether it matches.

The detection engineering workflow carries over in this example. Talos writes coverage for a new vulnerability, tests it, assigns it an identifier, and ships it, and operators then tune what fires in their own environments. A Quarry rule could follow a similar path: a text file paired with one conversation that should match and one that shouldn’t. It compiles when it loads (so a broken rule fails before it scans anything), and it moves through version control and continuous integration like other code. When a new agent attack technique is published, defenders can respond with a new rule, rather than waiting for a product release.

## Let your coding agents write Quarry rules

Writing every rule by hand will not scale as agents take on more of this work, so we want agents, as well as security and AI engineers, to be able to write Quarry rules. The Quarry Plugin lets a coding agent compose, compile, and refine rules from a plain-English description of an organization’s risk, and then test those rules against real conversations. Because the plugin uses the same compiler and scanner as the runtime, a rule that passes in a coding agent should behave the same way in your runtime. We still recommend that a human review and approve each rule before it moves to enforcement, because a rule written by an agent can inherit gaps in that agent’s understanding of the risk it is meant to capture.

The same Plugin will also power Cisco’s Policy Studio, our platform for building and running detections. Policy Studio adds what a platform needs around that engine: tenant and user access, stored rules and conversations, datasets and labeling, batch evaluation, and promotion of tested rules to live detection. In practice, an agent might draft a rule on a developer’s laptop, and Policy Studio would then evaluate it against the organization’s own data before it is promoted and shipped. The plugin and Policy Studio are early steps toward detection coverage that can keep pace with how quickly new agent attack techniques appear.

## What’s included in your Quarry starter pack

The open-source project gives practitioners a working foundation for detection engineering:

* a readable DSL for conversations, tool use, and event relationships;
* an evaluation runtime with configurable safety and resource limits, which compiles each rule when it loads;
* a command-line scanner for individual traces, directories, and datasets;
* a Python SDK for application integration;
* optional configured model operations for semantic signals;
* the Quarry plugin for Claude Code, Codex and other MCP-compatible agents
* rule metadata, examples, documentation, and message-format guidance; and
* a workflow for validating rules against positive and benign datasets.

TheQuarry repositorycontains installation instructions, supported Python versions, configuration examples, rule-writing guidance, and contribution information.

Adoption can proceed in three steps:

* Start with traces you already keep.Quarry reads OpenAI-format chat JSON, which many agent frameworks already log or can convert to. Pointquarry scanat a directory of stored traces.
* Tune before you enforce.Review matches and their evidence, then add exemptions for behavior you sanction, like your own upload endpoints. Consider versioning each rule with a matching and clean example conversation, gating changes in CI.
* Move to runtime once you sort through the noise.Call Quarry from the application path and map findings to alert, block, redact, quarantine, or log.

## Quarry integration in Cisco AI Defense

Quarryis already in production in AI Defense, where we enhance the policy model across compatible AI Defense surfaces, including agent traces, tool events, protocol integrations, and multimodal interactions.

We also plan to bring Quarry toDefenseClaw, our open-source governance layer for agent runtimes, which already scans skills, MCP servers, and generated code before they run and streams tool calls and policy decisions to Splunk. The aim is to test rules against stored traces from DefenseClaw and to send its findings, with evidence, to the same Splunk index. Taken together, these integrations reflect our intent for the same Quarry rules to run across Cisco’s AI security products, so that coverage written and tested once can be applied wherever an organization’s agents operate.

Planned features and integrations described in this post are forward-looking and subject to change. Some products or features described may be in various stages of development and offered on a when-and-if available basis.

## What this means for you

* If you build or deploy agents:Use policies to describe behavior that spans messages, tool calls, results, and state changes. Keep authorization controls for individual actions, then add trace-level detection where risk depends on order or context.
* If you write detections or evaluate agents:Express the evidence and relationship that should produce a finding, then test that policy against representative traces. Shared rules make disagreements visible and give teams a concrete object to improve.
* If you lead AI security or governance:Use findings and their evidence to connect policy requirements with evaluations, monitoring, and incident review. A rule should make the reason for a decision inspectable rather than hiding it inside an opaque score.
* If you buy or approve agent products: Ask vendors what their agents record, whether you can get the full trace, and whether a security finding arrives with the evidence behind it. An agent whose actions can’t be reconstructed afterward leaves an organization with little basis for an investigation.

## Engage with us

Agent behavior will keep changing as systems gain new tools and longer operating horizons. A detection policy language should make it possible to add new evidence and relationships without rebuilding every control around them. We see this release as a starting point rather than a finished answer. Quarry gives Cisco and the wider community a common format for describing agent behavior, and because no single organization will see every new technique, we expect many of the most useful rules to come from contributors outside Cisco. We want practitioners to test the model against their own traces, contribute detection ideas, and challenge the cases where a rule draws the wrong boundary. Feedback, counterexamples, and contributions will help us decide where Quarry needs to become more precise next.

Hugging Face reconstructed roughly 17,600 agent actions after the fact. Our aim with Project Quarry is to help defenders recognize sequences like that one while they are still in progress, and to preserve the evidence behind each finding for the people who have to act on it.

Check out the GitHub repository here:https://github.com/cisco-ai-defense/project-quarry

### Tags:


											AI Security										


											Artificial Intelligence (AI)