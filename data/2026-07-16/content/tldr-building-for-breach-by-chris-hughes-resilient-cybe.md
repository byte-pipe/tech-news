---
title: Building for Breach - by Chris Hughes - Resilient Cyber
url: https://www.resilientcyber.io/p/building-for-breach
site_name: tldr
content_file: tldr-building-for-breach-by-chris-hughes-resilient-cybe
fetched_at: '2026-07-16T11:35:00.711416'
original_url: https://www.resilientcyber.io/p/building-for-breach
author: Chris Hughes
date: '2026-07-16'
description: The Case for Containment in a World Where Prevention Has a Ceiling
tags:
- tldr
---

# Building for Breach

### The Case for Containment in a World Where Prevention Has a Ceiling

Chris Hughes
Jul 14, 2026
19
1
1
Share

I have spent the better part of my career trying to help organizations reduce risk through vulnerability management and application security.

I have written books on the subject, worked in AppSec programs, ran vulnerability management operations, and spent years in the federal government helping large enterprises operationalize zero trust.

I am a true believer in patching, in secure development, in shifting left, and I am telling you that none of it, individually or combined, is going to be enough to keep pace with where the threat and current landscape with AI’s convergence with cyber is heading.

The economics of offense changed underneath us, and most security programs are still budgeted as if they did not.

Thanks for reading the Resilient Cyber Newsletter! Subscribe for FREE and join 20,000+ readers to receive weekly updates with the latest news across AppSec, Leadership, AI, Supply Chain, and more for Cybersecurity.

Subscribe

## You Cannot Patch Your Way Out of This

The vulnerability discovery rate is now compounding on multiple independent curves.

The CVE ecosystem published over 40,000 vulnerabilities in 2025, and projections for 2026 range from 60,000 to as high as 100,000 depending on how aggressively you account for AI-assisted discovery, based on FIRST’s2026 mid-year projection.

As I covered inAI Is Winning the Cyber Arms Race, offense became a compute problem, and compute keeps getting cheaper and faster. Finding and exploiting a vulnerability is a search task. The cost per token has been deflating faster than Moore’s Law, and that is a structural shift rather than a handful of headline demos.

At the same time, the global codebase keeps expanding. AI-assisted development is accelerating the rate of new code, and every new function creates interaction surfaces with existing code. The growth isn’t trivial either, as I have discussed in theThe Attack Surface Exponential, GitHub alone is poised to go from 1 billion commits in 2025 to 14 billion in 2026.

Dependency chains amplify the problem further. The average enterprise application pulls in hundreds of open-source dependencies, each with its own transitive tree often five to seven levels deep, and a single flaw anywhere in that tree is a flaw in every application that imports it.

On the defense side, remediation has a hard ceiling.

TheQualys Threat Research Unit analyzedCISA’s Known Exploited Vulnerabilities program across 1.1 billion remediation records from more than 10,000 organizations over four years. What they found should concern every practitioner. Organizations that increased their remediation effort by a factor of 6.5 in a single year, closing 6.5 times more tickets, saw the percentage of critical vulnerabilities still unresolved at seven days actually worsen from 56% to 63%. Massive effort, negative marginal returns.

This happens because writing the fix is only about 10 to 15% of the enterprise remediation timeline. The rest is organizational work such as impact assessment, cross-team coordination, testing against dependent systems, scheduling deployment windows, deploying without breaking production, verifying the fix.

That bottleneck is organizational, not computational.

AI can help write patches faster, but a 10x improvement in fix-writing speed applied to 10 to 15% of the total timeline produces less than a 2x improvement end to end. That does not change the math when discovery has increased by orders of magnitude.

Meanwhile, the exploitation window has collapsed.

CrowdStrike’s 2026 Global Threat Report puts average breakout time at29 minutes, with the fastest observed breakout at27 seconds. The broader exploitation window compressed from 771 days in 2018 to just hours in recent years, as is well documented in theZero Day Clock.

For the class of vulnerabilities that actually determines whether an organization suffers a material breach, attackers are often discovering and weaponizing before defenders are even notified.

Patching remains necessary. It is a hygiene function that every organization must perform, but the ecosystem math means it can no longer serve as the sole strategy an organization relies on to prevent material breach. Discovery is compounding, remediation has a ceiling, and the gap between them is widening, not narrowing.

## A Practitioner’s History with Microsegmentation

The idea that you should limit lateral movement through network segmentation is not new. It has been a foundational security principle for decades. NIST has written about it extensively in publications such as 800-207. CISA’s Zero Trust Maturity Model explicitly includes network as a pillar, and the advanced maturity levels require microsegmentation with dynamic, identity-based policy enforcement.

Every serious security framework includes some version of this requirement.

The adoption numbers tell a different story. Gartner estimates that only 5 to 20% of enterprises have implemented microsegmentation in any form. In cloud specifically, only a small fraction of workloads have any perimeter network security at all. The vast majority of production environments are still running flat or near-flat architectures where compromising a single workload can give an attacker a path to nearly everything.

I lived this problem firsthand during my years helping large federal enterprises implement zero trust. The pattern repeated across agencies and programs. Security teams would identify microsegmentation as a priority. Leadership would agree in principle…then the project would stall.

The first reason was fear of breaking production.

Network policy changes carry real operational risk. In environments where uptime is measured against availability SLAs that carry political consequences, teams default to inaction rather than risk an outage. I watched programs where the security architecture was approved, funded, and staffed, and still never enforced because the operations team could not accept the risk of flipping the switch and potentially impacting business units.

The second reason was operational complexity.

Traditional microsegmentation required deep network engineering expertise, manual policy creation for every communication path, and constant policy maintenance as applications changed. Most organizations did not have the staff, the tooling, or the institutional patience for it. The policies grew stale, the exceptions multiplied, and eventually the segmentation existed on paper while production networks stayed flat.

The third reason, and perhaps the most fundamental, was that nobody actually knew what their applications needed to talk to.

You cannot write effective segmentation policies without a complete understanding of application communication patterns. In most environments I worked in, that understanding did not exist. Application teams knew their own service, but the full map of dependencies, especially transitive ones across shared infrastructure, was something nobody owned.

So the concept sat on architecture diagrams and compliance checklists while production environments stayed open, and every time an attacker got through, the blast radius was the entire environment because nothing constrained lateral movement or egress.

### Secure-by-Design Means Architecture, Not Just Code

The industry conversation around Secure-by-Design has focused heavily on how software is written. Memory-safe languages, secure coding practices, developer security education, secure defaults in libraries and frameworks.

All of that work matters and should continue, but Secure-by-Design should apply with equal force to how systems and environments are architected and deployed.

A perfectly written application deployed in a flat network with unrestricted egress and over-permissioned service identities is not secure by design. It is secure code sitting in an insecure architecture. When that application gets compromised, and given the vulnerability deficit it eventually will, the damage is determined not by the quality of the code but by the architecture surrounding it.

NIST and CISA included network segmentation in their publications and guidance because decades of breach data demonstrate that the presence or absence of architectural containment is a determining factor in whether an incident becomes a catastrophe.

That data continued to prove the point in 2026. CrowdStrike reports that 82% of intrusions now use valid credentials through legitimate channels, producing no anomalous signal. Attackers are logging in rather than hacking in. The identity layer sees no violation, the endpoint layer sees no malware, and the question of whether the attacker can move laterally and exfiltrate data comes down entirely to whether architectural constraints exist on those paths.

This is what I mean by building for resilience.

We need to accept that breaches will occur and orient our architecture around limiting the damage when they do. Patching tries to reduce the probability of breach. Detection tries to minimize the time an attacker operates. Architectural containment reduces the blast radius, and it is the only variable fully determined by design choices the defender makes before any incident occurs.

## Cloud Made the Problem Worse

On-premises environments, for all their limitations, developed with multiple defensive layers roughly in balance. The network pillar was pervasive, with perimeter firewalls, internal zones, VLAN segmentation, and routing-enforced separation. A compromised credential still had to traverse multiple layers before reaching anything of value.

Cloud inverted that posture. Identity became genuinely strong through AWS IAM, Azure Entra, and GCP IAM, but cloud providers left networking wide open because their economic engine is developer velocity, and network security reads as friction.

As Doug Merritt put it when we discussed this onResilient Cyber, “developer velocity and security is friction.” That incentive structure produced defaults where every major cloud provider ships allow-all outbound traffic and permits unrestricted communication between workloads in the same network. Kubernetes compounds the problem, with EKS, AKS, and GKE all permitting unrestricted pod-to-pod communication unless explicit network policies are applied.

The endpoint pillar became patchy in cloud at the same time. Containers, serverless functions, managed databases, and AI inference endpoints cannot host traditional agents. Much of the modern compute fabric lives for seconds. The workload types growing fastest are the types least compatible with agent-based security.

The practical result is that defense-in-depth in the cloud collapsed to a single pillar. That pillar, identity, is getting outsized focus, and rightfully so. It is also the pillar most easily bypassed when the attacker arrives with valid credentials, which is what happens in 82% of intrusions.

This is why, as I discussed with Doug Merritt onAviatrix’s In Progress podcast, the interesting question is never how they got in, it is always a lateral movement and egress problem.

## What Containment Looks Like in Cloud

The historic blocker to microsegmentation was cognitive load.

Writing and maintaining policies for tens of thousands of workloads across multiple clouds, regions, and compute models was more than most teams could sustain. That is the version of segmentation I watched fail repeatedly in federal environments.

What changed is AI.

AI is strong at the synthesis and pattern-matching that segmentation demands, specifically baselining application communication patterns, recommending policies based on observed behavior, and identifying anomalous flows against that baseline. The staged path of observe, baseline, monitor, and then enforce that was theoretically correct but practically unworkable a few years ago is becoming operationally realistic.

I recently walked through Aviatrix’s approach to this problem in a pair of detailed demos with their engineering team, and it maps well to what I always wished I had available during those federal zero trust implementation efforts.

The platform starts with visibility, onboarding cloud accounts in read-only mode to discover traffic flows and existing workloads across VMs, containers, Kubernetes clusters, and AI agents. This is the step that most segmentation projects skip or historically involved manual interviews and discussions with application teams, and it is the step whose absence causes everything downstream to fail.

You cannot write policies for communication patterns you do not understand.

From there, Aviatrix deploys lightweight enforcement points at the account level that govern both egress and east-west traffic without requiring global network modifications or changes to the underlying routing infrastructure.

Policy is expressed in terms of workload identity using existing cloud metadata and tags rather than IP addresses, which are meaningless in environments where workloads are constantly created and destroyed.

The enforcement model progresses through a lifecycle, from unprotected to monitored to partially protected to fully protected, giving teams the ability to validate policies against real traffic patterns before activating enforcement. If something breaks, reversal is a single action rather than an escalation path.

Two aspects of their approach address the failure modes I saw most often in practice.

The first is that the platform assumes brownfield environments. Most segmentation tools I’ve evaluated assumed some degree of greenfield architecture, and that assumption almost always wrong. Aviatrix works with whatever the customer has deployed today, as the network exists now, not as we wish it did.

The second is support for a dual-control operational model where a security team manages overarching guardrails and threat blocking through a centralized interface, while application teams manage their own specific policies through Terraform and CI/CD pipelines, in the formats and methodologies they are used to.

This aligns with how modern platform engineering teams actually work, and it distributes the operational burden of policy management across the people who best understand what each application needs.

The platform also extends containment to AI workloads, with the ability to detect communication with LLM endpoints and apply policy to AI agents.

Given that AI agents are rapidly becoming privileged non-human identities with broad cross-service access, and given real-world demonstrations like the GrafanaGhost attack where an AI assistant was weaponized to exfiltrate data through an authorized rendering channel with no anomalous signal, governing AI agent communication paths is not a theoretical future concern.

It is a current operational gap that most organizations have not begun to address.

Looking for a deeper dive for effective containment in the AI era? Grab the guide below!

-> Grab the Guide! <-

## Building for Resilience

I named my outlet and brand Resilient Cyber for a reason.

Resilience has always been the more honest framing for security. It does not pretend that prevention will succeed every time and instead, it accepts that incidents will occur and focuses on ensuring those failures are survivable.

Containment is the architectural expression of that principle.

It does not prevent the initial compromise, it prevents the initial compromise from propagating into the kind of lateral movement and data exfiltration that turns an incident into a headline. It holds whether or not the exploited vulnerability has been patched, whether or not the breach has been detected, and whether or not anyone on the security team is awake at 3 AM when the attacker moves.

The cybersecurity industry invested two decades primarily in prevention and detection. Both remain necessary, and both face structural headwinds that limit their effectiveness as standalone strategies.

The threat environment now demands at least equal investment in the architectural layer that governs what happens after prevention fails and before detection catches up. Blast radius should be a metric that CISOs, CIOs, and boards track deliberately and drive down over time, not a number they discover after an incident.

Organizations that treat it this way will be the ones who’s incidents stay local and recoverable, while everyone else is left explaining to leadership and regulators why a single compromised workload gave the attacker access to the entire environment.

Subscribe
19
1
1
Share