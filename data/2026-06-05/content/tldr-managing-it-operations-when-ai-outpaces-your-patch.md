---
title: Managing IT Operations when AI outpaces your patching cycle
url: https://www.redhat.com/en/blog/managing-it-operations-when-ai-outpaces-your-patching-cycle
site_name: tldr
content_file: tldr-managing-it-operations-when-ai-outpaces-your-patch
fetched_at: '2026-06-05T19:36:44.349596'
original_url: https://www.redhat.com/en/blog/managing-it-operations-when-ai-outpaces-your-patching-cycle
date: '2026-06-05'
description: Learn how Red Hat Ansible Automation Platform's Event-Driven Ansible feature can help organizations shift from waiting on scheduled maintenance windows to an active, real-time response for vulnerability management, reducing the exposure window and improving security posture.
tags:
- tldr
---

# Managing IT Operations when AI outpaces your patching cycle

June 4, 2026
3
-minute read
 

Automation and management
 

 Richard Henshall
 

 Head of product management for Ansible
 

It’s no surprise that AI has altered the technology landscape and added more complexity for IT teams. And when it comes to vulnerability management and patching, scheduled security is now outpaced by AI-detected vulnerabilities. This new complexity means our traditional, time-bound routines have become a liability—creating a lag time between threat discovery, containment, and remediation.

Anthropic’s recent Project Glasswing update proves what security teams have known for a while: The traditional patch cycle simply doesn't work when exposures are discovered at machine speed. Anthropic stated its Claude Mythos Preview model discovered over10,000 high- or critical-severity vulnerabilitiesacross major enterprise software in just weeks.

While AI has made identifying vulnerabilities near-instantaneous, finding them is only half the battle. The true challenge for IT leaders lies in the operational delay that follows—the critical gap between discovering a threat and enforcing the necessary containment or remediation before it can be exploited.

## The real risk: Time between discovery and enforcement

Automating a deployment script misses the real operational bottleneck. In a hybrid environment, safely deploying a patch or rolling out a new build takes time, which requires testing, change approvals, and staged maintenance windows to protect and coordinate system uptime.

The delay between discovering vulnerabilities and addressing them becomes the risk. Relying on scheduled, periodic cycles creates three clear issues:

* The exposure window:Even mature pipelines require hours or days to test and deploy a fix safely. Attackers exploit this exact window, moving minutes after a vulnerability goes public.
* Predictable routines:Security postures that are only checked on a rigid schedule become highly predictable and create a false sense of security.  Malicious actors use automated bots and tooling to scan for vulnerabilities, they don't wait for schedules or routines.
* Human-gated delays:While final deployments can be automated, the surrounding governance, such as architectural sign-offs and compliance reviews, remains human-bound, leaving exposures open at runtime.

Defending against automated threats means teams cannot leave systems exposed while waiting for a complete development cycle.

## Shrinking the containment window from days to minutes

To defend against machine-speed threats, organizations must shift away from waiting on the next scheduled maintenance window. Security enforcement needs to become an active, real-time response that contains threats the moment they are detected.

By automating these immediate containment steps, teams can shrink a typical multi-day or multi-week remediation cycle down to a near-instantaneous automated response. This doesn't replace the thorough testing required for a permanent software patch or an immutable build; rather, it safely buys the enterprise the time it needs to deploy those permanent fixes without leaving systems wide open to exploitation.

This is whereEvent-Driven Ansible, included in Red Hat Ansible Automation Platform, changes the operational dynamic. Instead of relying on a human engineer to manually triage a ticket and log into a console, Event-Driven Ansible acts as an automated circuit breaker. When a high-signal security tool identifies a critical exposure, Event-Driven Ansible can instantly trigger targeted, pre-approved playbooks to isolate the affected asset, tweak a security group, or temporarily revoke a compromised credential, supported with human-in-the-loop approval steps for higher risk actions.

## Protecting uptime and restoring baselines

The next step in this evolution is combining event-driven execution with AI intelligence. Shifting to an orchestration model delivers operational benefits that go far beyond basic vulnerability patching:

* Continuous compliance:Security baselines are enforced continuously at runtime. This turns compliance from a stressful, point-in-time audit into a natural byproduct of daily operations.
* Uptime-aware remediation:The platform monitors system health during execution. If a containment action or configuration change disrupts production, the system can automatically rollback to protect uptime while instantly elevating the alert to SecOps. This human-in-the-loop guardrail allows engineers to step in and deploy alternative mitigations, such as tightening perimeter security or modifying firewall rules, rather than leaving an exposure unprotected.
* Breaking the exploit chain:Automated orchestration can continuously correct things such as configuration errors and drift. But what about watching for things you don’t know about? Attackers will leverage lateral pathways they need to move through your network in unknown or new unpredictable ways. The recently announcedautomation orchestratoris designed to turn isolated automated responses into a continuous, guarded security loop that handles both software flaws and configuration issues. The resulting workflows combine contextual analysis and human-in-the-loop governance to execute and scale across fleets.

## The bottom line

AI is making vulnerability management more complex. IT operations leaders must evolve from time-bound routines using automation to continuous and event-driven results minimizing lag time between threat discovery and containment allowing teams to reduce risks in minutes and restore systems to a secure baseline more efficiently.

## Next steps

To close the velocity gap and move your enterprise from scheduled patching to continuous, event-driven enforcement, check out these resources:

* Review the architecture in action:Watch our executive-level framework onAutomated CVE Triage and Remediation with Red Hat Lightspeed and Ansible Automation Platformto see how agentic security loops operate under strict corporate governance.
* Schedule an executive briefing:Ready to transition your estate from reactive patching to continuous enforcement?Contact the Red Hat Enterprise Sales Teamto schedule a dedicated strategic consultation with an Automation Architect.

Resource

## 5 steps to automate your business

This e-book explores how Red Hat Services can help you adopt enterprise-ready automation to unify teams, standardize processes, and transform your IT.

Get the resource
 

### About the author

 

### Richard Henshall

Head of product management for Ansible

 

Richard is responsible for the Ansible Automation Platform strategy. With more than 16 years of experience in Financial Services IT across a range or operational, design and Architecture roles. As well as being an Ansible customer before joining the Red Hat team, he brings a customer focused viewpoint to compliment the strong engineering capabilities of one of the most popular open source projects.

 

More from this author
 

Enter keywords here to search blogs

UI_Icon-Red_Hat-Close-A-Black-RGB

 Search 

## More like this

 

 Blog post

 
 

### Build security into ITOps from the start with automation

 

 Blog post

 
 

### Stop managing, start orchestrating: Streamlining catalyst operations with Red Hat Ansible Automation Platform

 

 Original podcast

 
 

### Operating System Management | Compiler

 

 Original podcast

 
 

### Technically Speaking | Taming AI agents with observability

## Keep exploring

* The automated enterpriseE-book
* Try Red Hat Ansible Automation Platform with self-paced, hands-on labsInteractive lab
* Red Hat Ansible Automation Platform: A beginner’s guideE-book

## Browse by channel

Explore all channels
 

### Automation

The latest on IT automation for tech, teams, and environments

### Artificial intelligence

Updates on the platforms that free customers to run AI workloads anywhere

### Open hybrid cloud

Explore how we build a more flexible future with hybrid cloud

### Security

The latest on how we reduce risks across environments and technologies

### Edge computing

Updates on the platforms that simplify operations at the edge

### Infrastructure

The latest on the world’s leading enterprise Linux platform

### Applications

Inside our solutions to the toughest application challenges

### Virtualization

The future of enterprise virtualization for your workloads on-premise or across clouds