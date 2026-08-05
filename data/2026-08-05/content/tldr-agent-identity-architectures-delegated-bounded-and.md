---
title: 'Agent identity architectures: Delegated, bounded, and autonomous | 1Password'
url: https://1password.com/blog/ai-agent-identity-architectures
site_name: tldr
content_file: tldr-agent-identity-architectures-delegated-bounded-and
fetched_at: '2026-08-05T12:53:17.663031'
original_url: https://1password.com/blog/ai-agent-identity-architectures
date: '2026-08-05'
published_date: '2026-06-26T00:00:00.000Z'
description: '1Password maps AI into three authority models: delegated, bounded, and autonomous, with six identity architecture profiles to govern agentic access.'
tags:
- tldr
---

byWen Li

June 26, 2026- 17 min

## Related Categories

* AI
* Security

The agents running in your environment aren’t all the same and neither are the risks they carry. A CI/CD pipeline runner and a long-running autonomous coding agent have fundamentally different access needs, threat surfaces, and identity requirements. Traditional IAM has been successful at governing login for humans and machine workloads with predictable behavior, but controlling non-deterministic agentic systems require unique authority models that a single identity architecture cannot fully govern.

An agent that starts with access to a QA database may determine mid-task that it needs production access to complete its task, and the architecture governing it has to respond in real time without over-provisioning. That sort of dynamic authorization looks different depending on the type of agent that’s running, who authorized it, and what it has access to.

At 1Password, we’ve mapped the AI agent architectures we see in production into delegated, bounded, and autonomous authority models, each with variants for local and remote deployments. In this post, we’ll explore the distinct threat models and required controls to secure all six profiles at your organization.

## The three agent authority models

The authority model describeswho or whatthe agent is acting on behalf of, and what accountability chain that creates.

* Delegated authority: The agent acts on behalf of a named human. The human's identity is the delegation subject, and the agent's actions must be traceable back to it.
* Bounded authority: The agent acts on behalf of a system or workflow. No human subject is in the chain; instead, the agent is scoped to a defined operational boundary.
* Autonomous authority: The agent acts toward a goal with minimal or no human oversight. It may spawn sub-agents, evolve its access needs over time, and operate across systems its initiator did not explicitly plan for.

For each model, deployment in a developer's machine, a local sandbox, or an on-device browser, introduces a different set of attestation and threat challenges than in a remote environment like a Kubernetes cluster, a managed cloud sandbox, or a CI/CD platform. That distinction drives a significant portion of the protocol choices in each profile.

## Delegated authority

A delegated agent is an extension of a human, it inherits the human's permissions and intentions within an explicitly scoped boundary. The challenge is not just proving that the agent has authorization; it’s provingwhoseauthorization it has in a way that is cryptographically verifiable and auditable at the delegation level.

Every action a delegated agent takes must be traceable back to a human who authorized it and must be able to answer what scope was granted and the steps it took. Logging actions under a service account fails this requirement entirely.

Use cases include:

* IDE coding agents: Cursor, Claude Code, Codex, GitHub Copilot running in a developer's local environment, acting on behalf of the developer to read repositories, write code, and call external APIs.
* Browser copilots: Claude for Chrome, ChatGPT Atlas, and similar tools that act on behalf of a user within their browser session and SaaS applications.
* Workplace assistants: Sales, RevOps, and support agents that draft documents, schedule meetings, query CRM systems, and take actions within the user's existing SaaS permissions.

### Delegated / local

A local delegated agent is an AI agent running on a user’s own machine that acts on their behalf, where the human remains the authorizing principal but the agent executes autonomously within a delegated scope. Local delegated agents are the most common deployment pattern and carry the highest attestation risk profile.

When a coding agent runs in a developer's IDE, it executes under the same OS user account as the developer. Without additional controls, any other process running under that account could impersonate the agent. Malicious code, a compromised package, or an attacker payload injected via a prompt can all claim to be the legitimate agent when presenting credentials to an authorization server. This wasdocumented in a production environment, where indirect prompt injection turned a long-lived local agent session into an attack vector.

The Workload Identity Broker is an intermediary security service that replaces static API keys and passwords with ephemeral, policy-driven credentials. It’s common in cloud-hosted environments, such as CI/CD workloads, but typically isn’t available in local environments. In the context of local delegated agents, the WIB would be a code-signed local daemon that sits between the agent and the authorization server.

Before issuing any credential, the broker verifies the calling process against the OS code-signing subsystem like macOS Code Signing, Windows Authenticode, or Linux IMA. It holds an ephemeral key pair enrolled with the authorization server during device registration, and never exposes a long-lived credential to the agent process itself.

The protocol stack on top of this uses OAuth Token Exchange (RFC 8693) to express the delegation. The agent presents a subject token for the human and receives a delegated access token scoped to the specific role. The `act` claim in the resulting JWT carries the agent's workload identifier, making the delegation chain explicit and auditable end-to-end.

WebAuthn (W3C Level 3) provides step-up authentication for high-level actions like

pushing to a production branch, writing to a secrets vault, or making infrastructure changes. The agent triggers a user gesture, either with Touch ID, Windows Hello, or a hardware security key, to confirm explicit human intent before proceeding. This keeps humans in the loop on consequential actions and allows the agent to run without requiring approval for every low-risk operation.

The most important operational control for local delegated agents is session lifetime. Credentials must be rotated continuously throughout the session to maintain scope because a prompt-injection attack that succeeds mid-session inherits whatever is live at that moment. Longer sessions provide longer risk exposure. Development and production access must be separated at the policy level, a local coding agent should never hold credentials for production systems, regardless of what it requests.

### Delegated / remote

Remote delegated agents run in infrastructure the organization controls or contracts out, like a managed cloud service, a hosted browser policy, or a SaaS platform with an agent runtime. The delegation subject is still a human but the execution environment is controlled and attestable, meaning you can cryptographically verify where the agent is running and under whose authority.

When an agent runs on a local machine, there's no external party that can verify that it is what it claims to be, which is why the Workload Identity Broker exists. When the agent runs in the cloud, the platform already knows exactly what's running in it. It issues an OIDC token asserting the workload's identity, which gets exchanged via RFC 8693 for a delegated access token scoped to what the authorizing user approved. The platform takes the Workload Identity Broker's role, so the agent’s identity is verified before any access credential is issued..

With attestation managed by the platform, the primary challenge for delegated/remote agents is scope drift. Remote agents running in managed environments operate continuously and reliably, which creates pressure to provision them with broad, persistent permissions rather than issuing just-in-time credentials for each task. This is operationally tempting and architecturally wrong. The correct implementation re-establishes the delegation chain from the human principal at the start of each task, issues scoped tokens for that task window only, and expires them when the task completes.

WIMSE(Workload Identity in Multi-System Environments)is the key protocol for remote delegated agents that cross service boundaries. A workplace assistant that reads calendar details, sends emails, and queries a CRM in a single session might cross several service boundaries in a single session. Each of those systems has its own authorization rules and no pre-existing trust with the agent's home runtime. WIMSE provides a standard for expressing the workload identity portably across all three boundaries, in a format every system understands.

CAEP(Continuous Access Evaluation Profile)is a hard requirement at this profile. Remote delegated agents can act faster and across more systems than local agents. When a user's session is revoked, or their permissions change, or a security event is detected, that change must propagate immediately to every relying party the agent has an active session with, not at the next token expiry.

In enterprise environments where MCP clients and servers both support it, the Enterprise-Managed Authorization (EMA) extension for MCP offers an optional alternative path for how the initial delegation chain is established. Instead of the agent’s runtime exchanging directly with the MCP server’s authorization server, the organization’s identity provider (Okta, Azure AD, or similar) acts as an intermediary. The MCP client exchanges the user’s existing SSO identity for an Identity Assertion JWT Authorization Grant (ID-JAG), which is then presented to the MCP server’s authorization server in place of the standard token exchange. This means access policy and revocation for MCP servers are centralized at the IdP, alongside every other enterprise application, which is operationally attractive for large deployments.

## Bounded authority

Bounded agents act on behalf of a system or workflow, where there is no human delegation subject in the authorization chain. The agent's authority is derived from its operational scope defining the set of services, tools, and actions it is configured to use.

The identity challenge for agents with bounded authority is scope enforcement. The work these agents need to accomplish is often broad, and issuing fine-grained, per-task credentials have been expensive to implement historically. So organizations routinely take the shortcut and provision bounded agents with permissions far wider than any single run requires. That over-provisioning determines the blast radius when these credentials are compromised.

Use cases:

* CI/CD pipelines and review bots:GitHub Actions, GitLab CI, and Jenkins – automated build, test, and deploy workflows that need ephemeral, scoped access to source repositories, artifact stores, and deployment targets.
* Provisioning and lifecycle jobs:Joiner-mover-leaver workflows running off SCIM, HR automation agents that create, modify, and deprovision accounts across connected systems.
* Scheduled batch jobs:Compliance reporting, billing pipelines, ETL workflows, and webhook receivers that run on a schedule and interact with specific downstream APIs.

### Bounded / local

Local bounded agents often handle development automation and local webhook receivers. There is no human delegation chain to impersonate and although the agent's authority is derived from its configured role rather than a user's permissions, the workload identity still matters. A local automation process needs a verifiable identity to obtain credentials for the systems it touches.

For local bounded agents, the Workload Identity Broker only needs to verify the process and issue a scoped token. There’s no user delegation chain, no step-up authentication, no RFC 8693 token exchange. The broker verifies the process through  the OS code-signing subsystem and issues a WIMSE-compliant workload identity with a short-lived, scoped access token for the specific services it’s configured to reach.

The critical operational control is the same as in remote bounded case: each local automation run should receive a token scoped to that run only. A deploy script targeting a test environment and a deploy script targeting production should hold separate workload identities, authorized by separate policies, even when they are the same codebase. That’s the development-vs-production trust boundary that matters most for teams running automated deployment scripts locally.

### Bounded / remote

Remote bounded agents are the most common profile in enterprise environments today. Nearly every organization running automated pipelines has remote bounded agents, and most of them run on long-lived credentials that have never been rotated, scoped, or revoked, accounting for the largest, unaddressed source of non-human identity risk in the environment.

Controlling access for remote bounded agents starts with eliminating long-lived credentials at the source. Where platform OIDC is available, a short-lived OIDC token is issued for each workflow run, scoped to the specific repository, workflow, and run. That token is exchanged at the authorization server for credentials that cover only the resources the current stage requires. No long-lived secret is stored in the repository or secrets manager. The agent's workload identity is cryptographically tied to that specific run, not to a persistent, static credential.

For environments without native platform OIDC, SPIFFE/SPIRE can issue short-lived identity documents to workloads based on verifiable runtime attributes (pod labels in Kubernetes or instance metadata in cloud environments) and rotate them automatically. WIMSE provides the standard for expressing those identities across service and organizational boundaries in multi-environment deployments.

The unsolved problem for most teams implementing this profile is per-stage token scoping, i.e., the ability to issue a token for the build stage that cannot access deployment targets and a separate token for the deploy stage that cannot access the source repository.

OAuth Transaction Tokensare designed specifically for this. They carry the full context of a multi-step, cross-service transaction and allow each stage to receive only the authority it needs for that stage, while maintaining a tamper-evident chain linking the workflow back to its initial authorization.

CAEP subscription at this profile gives security teams something long-lived credentials can never offer: the ability to revoke a pipeline's access mid-run in response to a threat signal. Long-lived credentials stored in secrets managers are only checked at authentication time; by definition, they can't be stopped once a run has started.

## Autonomous authority

Autonomous agents pursue a goal over an extended time horizon with minimal or no human oversight. They adapt their behavior to new inputs, may spawn sub-agents for specific tasks, and frequently need access to systems their initiator didn’t explicitly anticipate. A human sets the goal, but the agent determines the execution path.

The identity challenge here is continuous authorization. Every step the agent takes must be authorized by a policy that is consistent with the original human intent, even when no human is available to approve it in real time. This places the highest demand on any architecture: real-time enforcement, revocation infrastructure, and a complete audit trail for the execution path.

Use cases:

* Long-running coding agents in managed sandboxes:Devin, Claude Code in autonomous mode, and similar systems running inside remote execution environments like Daytona to build and test software without a human in the loop for each step.
* Supply chain and operations agents:Agents that reroute orders, adjust inventory, or respond to infrastructure disruptions autonomously.
* Autonomous production remediation agents:Security or reliability agents that act quickly detect issues and take corrective action on live infrastructure.
* Continuous security agents:Threat hunting and posture management agents that run ongoing scans, correlate signals across systems, and surface findings.

### Autonomous / local

Local autonomous agents are currently rare, but the pattern is emerging. Local execution requires a level of trust in an agent’s reliability and sandboxing environments that are still maturing. While these boundaries are maturing, most teams running autonomous agents today deploy them in managed cloud environments. An example of an autonomous, locally run agent would be one that runs overnight on a developer’s machine, iterating across multiple repositories, installing dependencies, and calling external APIs to build a feature end-to-end.

The risk level here is high. A long-running process, operating without active human oversight, on hardware that may be shared or uncontrolled, allows an agent to accumulate access across systems over an extended session. A single successful prompt injection attack could redirect the agent's goal while it continues to operate under a valid credential.

The Workload Identity Broker here must implement continuous credential rotation. Instead of a single issuance at startup, a fresh token must be issued for each meaningful task transition. The broker must also monitor the calling process to detect if the agent's process signature changes during execution, a sign of compromise or injection, and stop credential issuance immediately.

A local autonomous agent running without human oversight has no natural stopping point, so CAEP subscription is important even at the local level. A revocation event from the authorization server must terminate the agent's active sessions across all local services it has touched. Without it, a compromised session persists until the next token expiry, which, for an autonomous agent, is an unacceptably large window.

A local autonomous agent must not hold credentials for production systems. Any artifact it produces should require an explicit human approval step and re-authorization before it touches production infrastructure.

### Autonomous / remote

Remote autonomous agents have the highest security risks and the highest operational complexity. Long-running agents in managed sandboxes, continuous production agents, and autonomous remediation agents all fall here.

Remote execution provides better attestation infrastructure, but autonomy introduces problems that platform attestation alone cannot address. The core issue is that the agent's access needs evolve mid-execution in ways the initial authorization policy did not anticipate.

Handling this without granting standing broad permissions requires just-in-time privilege escalation: a mechanism for the agent to request additional access at runtime. That request gets evaluated against current policy and the original authorization context, and the agent receives a scoped, short-lived credential for the specific step, without a human in the loop for routine escalations, and with explicit human approval required for escalations above a defined sensitivity threshold.

OAuth Transaction Tokens carry the entire authorization context of the original grant, subsequent escalations, and the policy decisions made at each step, in a tamper-evident chain. Consider an agent that starts a run with access to QA resources, runs a deployment test, and requests production access to proceed. The transaction token records the escalation request, the policy that evaluated it, and the credential issued in response, in a complete, unfalsifiable chain.

Sub-agent delegation is an open problem at this profile. An autonomous agent that spawns a sub-agent for a specific task must constrain the sub-agent's authority to a subset of its own. The sub-agent cannot inherit the full permission set.

WIMSE and the Agent Identity Management (AIMS) model provide the conceptual framework where the parent agent presents its workload identity plus a delegation scope when requesting a token for the sub-agent, and the authorization server issues a token bound to that scope. This is one of the areas where the community is most actively developing the specs.

CAEP at this profile must cover all downstream systems the agent has touched, including sub-agents. A revocation event for the top-level agent must cascade to every sub-agent spawned under its authority. Teams implementing this profile need to plan for revocation cascades at the system design stage and build them in from the start.

The development/production boundary is crucial for autonomous remote agents with production access. These are the highest-risk workload in this framework. Separate authorization policies, separate audit logs, and explicit human approval requirements for production-scope actions are required controls.

## Three security requirements to govern AI agent identity

The six profiles share three non-negotiable requirements:

1. No long-lived credentials on agent workloads.Local or remote, delegated or autonomous, agents receive short-lived, scoped tokens issued for a specific task window. The Workload Identity Broker (local) or the platform OIDC subsystem (remote) manages the credential lifecycle. The agent never holds a secret that survives the task.
2. Attribution-complete audit records.Every agent action traces to a specific workload identity. Every workload identity traces to either a human delegation subject or a bounded system authority. The delegation chain must be captured in the log, not reconstructed after the fact.
3. Development and production are separate trust domains.Writing software and running it on production systems carry fundamentally different threat models. Separate workload identities, separate authorization policies, and explicit human-in-the-loop controls for any promotion from development to production are a design requirement.

Each authority model and execution environment combination has a distinct identity architecture with its own protocols, attestation mechanisms, and operational controls. The next posts in this series will walk through each one in detail, covering what the use cases look like, what the architecture requires, and where the hard problems still live.

Explore Unified Access

See how 1Password Unified Access secures identity for humans, machines, and AI agents without long-lived credentials, attributable audit records, and clear dev/production boundaries.

Explore Unified Access Platform
 

## Continue Reading

April 8, 2026

## NIST and AI agents: 1Password’s approach to agent identity

Security
AI

June 15, 2026

## Introducing 1Password Credential Broker

Unified Access
AI