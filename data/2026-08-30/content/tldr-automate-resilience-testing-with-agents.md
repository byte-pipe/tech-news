---
title: Automate Resilience Testing with Agents
url: https://www.harness.io/blog/find-resilience-risks-automatically-then-confirm-them
site_name: tldr
content_file: tldr-automate-resilience-testing-with-agents
fetched_at: '2026-08-30T21:52:53.573761'
original_url: https://www.harness.io/blog/find-resilience-risks-automatically-then-confirm-them
date: '2026-08-30'
published_date: '2026-08-24T00:00:00Z'
description: RT Agents detect resilience risk in your CD pipelines and Kubernetes workloads, then generate and run chaos experiments or load tests to confirm it. | Blog
tags:
- tldr
---

What is a Kubernetes Container?

GraphQL: Harness Your Way

CI/CD Pipeline: Everything You Need to Know

CI/CD Testing: The Complete Guide for Modern Software Delivery

Your First Harness CI Installation, Build, and Publish

IT Audits - How Continuous Delivery can Help

Blue-Green Deployments With Kubernetes and Harness

How We Cut Cloud Logging Costs by $140k: A Step-by-Step Breakdown

6 Actionable GitOps Best Practices to Help You Get Started

An Introduction to Artificial Intelligence and Machine Learning

Applying AI/ML to CI/CD Pipelines

Comparing Helm vs Kustomize

Continuous Integration Testing: Types, Best Practices, and Tools

Accelerates AWS Cloud Migration

What is O11Y? Observability Demystified with Chris Riley from Splunk

Kubernetes CI/CD Best Practices for Scalable, Secure Deployments

Tutorial: How to Use the New Vault Agent Integration Method With Harness

Pipeline Patterns for CI/CD Pipelines

Feature Flags: Should I Build or Buy?

Measuring and Improving Developer Productivity: A Practical Guide for DevOps Teams

4 Best CI/CD Tools for DevOps

How To Turn Your GitHub Repository Into an Automated Helm Chart Repo

Harness the Power of AWS EKS-Anywhere

Test Intelligence™: Move Fast, Don’t Break Things

What Are Audit Trails & Why You Need Them in CD

5 Feature Flag Use Cases You May Not Have Thought Of

The Benefits of Feature Flags in Software Delivery

Feature Flags With Python

Intelligent & Automated Feature Flags With Harness

Find and Fix Vulnerabilities in Your Pipeline With Snyk and Harness

What Is Testing in Production & How to Avoid The Risks

GitHub Actions Support in Harness CI

How Feature Flags Help With Trunk-Based Development

Feature Flags Best Practices

Micro-Frontend Architecture in the Harness Software Delivery Platform

What Is Split.io? What is Harness Feature Management and Experimentation? A Look at Features and Use Cases

Kubernetes Mistakes: A Beginner’s Guide to Avoiding Common Pitfalls

In-Depth: Harness Feature Flags Relay Proxy

Announcing: Public APIs for Feature Flags

The Git Sync Experience in Harness

Git Branching in Harness

Source Code Management in DevOps

Harness Security Testing Orchestration (STO) - Key Capabilities

Quality vs Reliability

Build System vs CI System: What's the Difference and Why Does it Matter?

The Best Open Source CI Tools

Benefits of GitOps & Why GitOps Is Important

What Are GitOps Principles?

GitOps Tools for Kubernetes: Best Platforms to Scale Continuous Delivery

Kubernetes Services Explained

Harness CI and Harness CD - Your First True CI/CD Pipeline

Continuous Delivery vs. Continuous Deployment: What’s the Difference?

How Value Stream Mapping Optimizes Your Software Delivery Process

How to Build CI Pipelines with GitHub Actions and Deploy to Kubernetes with Harness

What is PaaS (Platform-as-a-Service)?

Declarative Continuous Delivery for Kubernetes: A Closer Look at Argo CD

What Is a CI/CD Platform and Why Should I Care?

The Dependency and Plugin Hell That is Jenkins

Build a Canary Deployment in 4 Mins with Harness CD

Comparing Harness and Jenkins

Harness Extends Continuous Verification To Dynatrace

10 Signs You Don't Do Continuous Delivery

Harness Continuous Delivery for Red Hat OpenShift

A Time Series Machine Learning Model for Canary Deployments

JFrog Artifactory & Harness - Don’t Get Bogged Down With Continuous Delivery

Harness CI/CD Pipelines for .NET and Azure

ServiceNow for CI/CD Pipelines

Vulnerability Scanning in your CI/CD Pipeline - Part Two

The DevOps Tools Lifecycle Mesh for 2021

Intro to Deployment Strategies: Blue-Green, Canary, and More

Continuous Verification - Machine Learning to Safeguard Your Deployments

Discover Azure DevOps Alternatives

Top 8 Cloud Cost Management Tools

What Is GitOps? Learn About Benefits, Challenges, and More

The Importance of Continuous Verification

Best Argo CD Alternatives & Competitors

Best Spinnaker Alternatives to Consider

Continuous Delivery Tools to Consider

How DORA Metrics Improve DevOps Performance

The Software Development Life Cycle: A Complete Guide to Each Phase

A Snapshot of DevOps

What are Feature Flags and How Do We Use Them?

What Is Role-Based Access Control (RBAC)?

How to Prioritize the Developer Experience and Improve Output

SRE vs. DevOps: Key Differences, Roles, and How They Work Together

User & Role Management in the Harness Software Delivery Platform

How We Built Event-Driven Architecture with Redis Streams at Harness

Service Accounts: A Path to CI/CD Automation

Harness YAML Editor - Code Away Your CI/CD Pipelines!

What Is an Artifact Repository?

Simplify test maintenance with the builder factory pattern

Modern Software Delivery Best Practices & Software Delivery Management

Managing the 'Git' in 'GitOps': 4 Ways to Structure Code in Your GitOps Repos

Top 10 Best Practices for DevSecOps

What is CircleCI? A Look at Features and Use Cases

Kubernetes Application Deployment Strategies

The Basics of GitOps Secrets Management

Harness Chaos Engineering (CE) Key Capabilities

What is ArgoCD?

Introducing Harness CI/CD Plugin for Backstage

Next

# Find Resilience Risks Automatically, Then Confirm Them| Harness Blog

RT Agents detect resilience risk in your CD pipelines and Kubernetes workloads, then generate and run chaos experiments or load tests to confirm it.

Resilience Testing

Published: 
August 24, 2026

Last updated: 
2026-08-27
By
Uma Mukkara
Time to Read
Table of Contents
+
Link

Resilience Testing (RT) Agents scan your CD pipelines and Kubernetes workloads for resilience risk before it reaches production, then generate and run the chaos experiments or load tests needed to confirm it.

## What We're Announcing

We're announcing a major update to ourResilience Testingcalled RT Agents. Instead of handing you a testing tool and a blank page, our agents now do the first part of the work, often the hardest part, for you. They continuously analyze your deployment pipelines and infrastructure to predict where resilience risks are hiding, tell you exactly what kind of testing is needed to prove it, and recommend next steps. From there, you decide where to take action. When you do, the agents help you get there: generating the chaos experiments and load tests, running them, and reading the results, so you don't have to start from scratch.

Resilience Testing no longer has to start from zero. Harness finds the risk and helps you act on it, directly in your existing pipeline.

## Key Features

### Passive risk detection in your Harness Continuous Delivery (CD) pipelines

If you're aHarness CDuser, this shows up as Agentic Resilience inside the pipeline you already run. RT Agents continuously read your deployment configuration, manifests, and pipeline history to flag resilience risk as it's introduced, before it reaches production. There's nothing to instrument and nothing to run. Detection happens automatically as part of your existing CD workflow, so risk gets caught at the moment it's created instead of months later during an incident.

### Simplified onboarding for Kubernetes apps

Getting resilience insight into your Kubernetes workloads no longer requires a lengthychaos experimentor load test setup process. Onboard your applications through a streamlined flow that connects to your existing cluster and infrastructure metadata, and the agents start surfacing the resilience risks specific to your environment right away. No faults injected, nothing touched in production.

### In-product dashboards for Resilience Insights

Every risk the agents detect rolls up into dashboards built for tracking resilience posture over time, not just point-in-time results. You get a consolidated view of risk across services and pipelines, so teams and leadership can see whether resilience is trending in the right direction.

### Resilience Scores for your Load Tests

Load testing results now come with a Resilience Score: a single, trackable number that reflects how your services hold up under load, beyond raw throughput and latency numbers. It's built to make load test outcomes easier to compare over time and easier to explain to stakeholders who don't work with performance data day to day.

### Java, JavaScript, and Python support for Load Test scripting

You can now writeLoad Testscripts in the language your team already uses. That removes a common barrier to adoption: teams don't need to learn a new scripting language just to write a load test, so load testing fits more naturally into how your engineers already work.

## Free Plan: Try It Out

You don't need to take our word for it. Harness offers a free plan for resilience testing, so you can put it to work in your own environment before committing to anything. It includes a hosted experience with the core capabilities you'd expect: an extensive fault library, a centralized control plane, native integration with Harness pipelines, and enterprise features likeRBACand hosted logging, all at no cost. It's a way to validate the resilience of your own services without the limits of a typical trial account.

If you're new toResilience Testing, this is the easiest way to see what RT Agents find in your own pipelines. Sign up, connect your infrastructure, and let the agents show you where your risk actually is.

Signup for free.

‍

## FAQ

### Does RT AI Agents touch production or inject faults during detection?

No. Detection is passive: the agents read your existing deployment configuration, manifests, and pipeline history. Nothing is instrumented and nothing runs against your services until you choose to generate and run a chaos experiment or load test.

### Do I need to set up a chaos experiment or load test before RT Agents can find risk?

No. The agents analyze your CD pipelines and Kubernetes workloads on their own and tell you what kind of test would confirm the risk. You only run a test once you decide to act on what they find.

### What's included in the free plan for Resilience Testing?

A hosted experience with the full fault library, a centralized control plane, native Harness pipeline integration, and enterprise features like RBAC and hosted logging, all at no cost.

### Which languages can I use to write load test scripts?

Java, JavaScript, and Python, alongside Harness's existing load testing options. Use whichever your team already works in instead of learning a new scripting language.

### What is a Resilience Score?

A single, trackable number attached to each load test that reflects how a service holds up under load, beyond raw throughput and latency numbers, so teams can compare results over time and report them to stakeholders.

### Uma Mukkara

All this author's posts →

Uma Mukkara is Head of Chaos Engineering at Harness, where he helps teams improve reliability by safely testing how systems behave during real-world failures. Earlier, Mukkara co-founded MayaData and helped build cloud-native technologies such as OpenEBS.

← Previous:
Next: →
‍

## Related Resources

Building for Resilience: An Engineering Guide to the Mythos Era

Harness Platform

### Building for Resilience: An Engineering Guide to the Mythos Era

April 29, 2026

Adam Arellano

+ more
Time to Read

The release ofAnthropic Mythos and Project Glasswingmarks an exciting and pivotal new chapter in software development. As the industry advances, the speed and economics of vulnerability exploitation have fundamentally shifted. What once took weeks of manual reconnaissance can now be scaled rapidly through automated models.

However, this is not just a security problem to solve. It is a massive engineering opportunity to build cleaner, more robust systems. By leaning into AI-accelerated defense, engineering teams are uniquely positioned to lead the charge and redesign the landscape of modern software architecture.

### Breaking Down Silos and Establishing Shared Accountability

To succeed in this new era, the traditional silos separating security and engineering must fall. Defense at machine speed requires a unified front.

* Organizations need a shared roadmap and accountability model across Engineering, Infrastructure, and Security.
* These roadmaps must be crafted jointly with clear responsibility assigned per action item.
* Every executive and their corresponding team will be affected and accountable for changing the way work is done.
* Preparations for these improvements should be treated exactly like new product features.
* Savvy customers will start to pay attention to companies who are responding to Mythos, turning your proactive resilience into a highly visible competitive advantage.

### Core Engineering Imperatives

The foundation of AI-accelerated defense relies on sound, proactive engineering practices. Developers must take ownership of architectural hygiene from the ground up.

* Accelerate velocity:Teams must focus heavily on shortening patch and change cycles (such as with HarnessCIandCD). The single most important metric is how quickly you can safely make changes.
* Shift left completely:You must find bugs before you ship code. Achieve this by integratingSAST,SCA, and auto-pen testing into a secure pipeline, and prefer using memory safe code languages.
* Design for resilience:Always build with breach assumed. In practice, this means implementingzero-trust, isolating services by identity, and using short lived tokens by default.
* Simplify the architecture:As you engineer and build for resilience and simplicity , take time to audit your current code base to reduce dependencies and standardize on known good services and libraries. Additionally, actively reduce and inventory what you expose.
* Pay attention runtime: Aside from bugs, engineering teams haven’t traditionally paid attention to therun-time securityof their applications. Aside from the functional insights developers can glean from runtime security tools, understanding how a system is attacked can help you make better architectural and functionality decisions.

### Planning for the Unexpected

Even with the best architecture, unexpected friction will occur. Resilient engineering means planning comprehensively for your ecosystem.

* Ensure youknow your software dependenciesand precisely who to contact in emergencies.
* Engineering teams should build technical work-arounds for times when providers or internal systems experience issues.
* Organizations must establish a surge defense capability. When faced with a severe situation, have a SWAT team established with pre-approved authority, budget, and standard operating procedures across domains and outside help.
* At the company level, pre-position high-visibility incident response. This includes having pre-approved and crafted messaging triggered by established conditions.

### Security as an AI-Powered Partner

To keep pace with the increased velocity of engineering teams, Security teams must also evolve their operational models.

* Security needs to leverage AI to de-toil high calorie activities.
* Practical applications include putting a model in front of your alert queue and testing it regularly.
* AI should also handle the triage and prioritization of scan findings alongside ticket ops automation.
* It is crucial to automate the technical incident response pipeline.
* By automating the bookkeeping around incidents, human decisions should be made with assistance at most.
* The ultimate goal is to find places to leverage AI and accelerate the time between incident and resolution.

### Leading the Charge

Engineering leaders and developers are in the perfect position to navigate this industry inflection point. By taking ownership of these structural changes today, you ensure the long-term viability of your products and the enduring strength of your codebase. Bring your security, infrastructure, and engineering teams together into the same room and start building your shared roadmap today.

AI-Powered Resilience Testing with Harness MCP Server and Windsurf

Resilience Testing

### AI-Powered Resilience Testing with Harness MCP Server and Windsurf

September 15, 2025

Ashutosh Bhadauriya

+ more
Time to Read

The complexity of modern distributed systems demands proactive resilience testing, yet the old-school chaos engineering often presents a steep learning curve that can slow adoption across teams. What if you could perform chaos experiments using simple, natural language conversations directly within your development environment?

The integration of HarnessChaos Engineeringwith Windsurf through the Model Context Protocol (MCP) makes this vision a reality. This powerful combination enables DevOps, QA, and SRE teams to discover, execute, and analyze chaos experiments without deep vendor-specific knowledge, accelerating your organization's journey toward building a resilience testing culture.

## Simplifying Chaos Engineering

Chaos engineering has proven its value in identifying system weaknesses before they impact production. However, traditional implementations face common challenges:

Technical Complexity: Setting up experiments requires deep understanding of fault injection mechanisms, blast radius calculations, and monitoring configurations.

Learning Curve: Teams need extensive training on vendor-specific tools and chaos engineering principles before becoming productive.

Context Switching: Engineers constantly move between documentation, experiment configuration interfaces, and result analysis tools.

Skill Scaling: Organizations struggle to democratize chaos engineering beyond specialized reliability teams.

The Harness MCP integration changes this landscape by bringing chaos engineering capabilities directly into your AI-powered development workflow.

## Understanding Harness Chaos Engineering MCP Tools

The Harness Chaos Engineering MCP server provides six specialized tools that cover the complete chaos engineering lifecycle:

### Core Experiment Tools

chaos_experiments_list: Discover all available chaos experiments in your project. Perfect for understanding your resilience testing capabilities and finding experiments relevant to specific services.

chaos_experiment_describe: Get details about any experiment, including its purpose, target infrastructure, expected impact, and success criteria.

chaos_experiment_run: Execute chaos experiments with intelligent parameter detection and automatic configuration, removing the complexity of manual setup.

chaos_experiment_run_result: Retrieve detailed results including resilience scores, performance impact analysis, and actionable recommendations for improvement.

### Advanced Monitoring Tools

chaos_probes_list: Discover all available monitoring probes that validate system health during experiments, giving you visibility into your monitoring capabilities.

chaos_probe_describe: Get detailed information about specific probes, including their validation criteria, monitoring setup, and configuration parameters.

## Setting Up Harness MCP Server with Windsurf

### Prerequisites

Before beginning the setup, ensure you have:

* Windsurf IDEinstalled
* Harness Platform accesswith Chaos Engineering enabled
* Harness API keywith appropriate permissions
* Go 1.23+(to build from source)

### Step 1: Build the Harness MCP Server Binary

You have multiple installation options. Choose the one that best fits your environment:

#### Building from Source

For advanced users who prefer building from source:

1. Clone the Repository:

git clone https://github.com/harness/mcp-server
cd mcp-server

‍

1. Build the Binary:

go build -o cmd/harness-mcp-server/harness-mcp-server ./cmd/harness-mcp-server

### Step 2: Configure the Harness MCP Server in Windsurf

1. Navigate to yourWindsurf Settings,click onCascade,thenManage MCPs.
1. Click onView raw configtoopen yourmcp_config.jsonfile

‍

1. Add the below configuration to the file

{
 "mcpServers": {
 "harness": {
 "command": "/path/to/harness-mcp-server",
 "args": ["stdio"],
 "env": {
 "HARNESS_API_KEY": "your-api-key-here",
 "HARNESS_DEFAULT_ORG_ID": "your-org-id",
 "HARNESS_DEFAULT_PROJECT_ID": "your-project-id",
 "HARNESS_BASE_URL": "https://app.harness.io"
 }
 }
 }
}

‍

### Step 3: Add the Path of your Binary and Harness Credentials

Gather the following information, add it to the placeholders and save themcp_config.jsonfile.

* Command:Path to your built harness-mcp-server binary
* API Key: Generate from your Harness account settings (Profile > My API Keys)
* Organization ID: Found in your Harness URL or organization settings
* Project ID: The project containing your chaos experiments
* Base URL: Your Harness instance URL (typicallyhttps://app.harness.io)

### Step 4: Verify Installation

1. Restart Windsurf: Close and reopen Windsurf to load the new configuration
2. Go back toMange MCPs, you should see a list of tools available
1. Test Connection: Try a simple prompt like:

"List all chaos experiments available in my project"

‍

If successful, you should see chaos-related tools with the "chaos" prefix and receive a response with your experiment list.

## AI-Powered Chaos Engineering in Action

With your setup complete, let's explore how to leverage these tools effectively through natural language interactions.

‍

### Discovery and Learning Phase

Service-Specific Exploration:

"I am interested in catalog service resilience. Can you tell me what chaos experiments are available?"

‍

Expected Output: Filtered list of experiments targeting your catalog service, categorized by fault type (network, compute, storage).

‍

Deep-Dive Analysis:

"Describe briefly what the pod deletion experiment does and what services it targets"

‍

Expected Output: Technical details about the experiment, including fault injection mechanism, expected impact, target selection criteria, and success metrics.

‍

Understanding Resilience Metrics:

"Describe the resilience score calculation details for the network latency experiment"

‍

Expected Output: Detailed explanation of scoring methodology, performance thresholds, and interpretation guidelines.

‍

### Experiment Execution Phase

Targeted Experiment Execution:

"Can you run the pod deletion experiment on my payment service?"

‍

Expected Output: Automatic parameter detection, experiment configuration, execution initiation, and real-time monitoring setup.

Structured Overview Creation:

"Can you list the network chaos experiments and the corresponding services targeted? Tabulate if possible."

‍

Expected Output: Well-organized table showing experiment names, target services, fault types, and current status.

Monitoring Probe Discovery:

"Show me all available chaos probes and describe how they work"

‍

Expected Output: Complete catalog of available probes with their monitoring capabilities, validation criteria, and configuration details.

‍

### Analysis and Reporting Phase

Result Interpretation:

"Summarise the result of the database connection timeout experiment"

‍

Expected Output: Comprehensive analysis including performance impact, resilience score, business implications, and specific recommendations for improvement.

Probe Configuration Details:

"Describe the HTTP probe used in the catalog service experiment"

‍

Expected Output: Detailed probe configuration, validation criteria, success/failure thresholds, and monitoring setup instructions.

Comprehensive Resilience Assessment:

"Scan the experiments that were run against the payment service in the last week and summarise the resilience posture for me"

‍

Expected Output: Executive-level resilience report with trend analysis, critical findings, and actionable improvement recommendations.

## The Road Ahead

The convergence of AI and chaos engineering represents more than a technological advancement, it's a fundamental shift toward more accessible, and intelligent resilience testing. By embracing this approach with Harness and Windsurf, you're not just testing your systems' resilience, you're building the foundation for reliable, battle-tested applications that can withstand the unexpected challenges of production environments.

Start yourAI-powered chaos engineeringjourney today and discover how natural language can transform the way your organization approaches system reliability.

‍

Resilience Testing Is Non-Negotiable in the Enterprise SDLC

Resilience Testing

### Resilience Testing Is Non-Negotiable in the Enterprise SDLC

March 18, 2026

Dewan Ahmed

+ more
Time to Read

Modern software delivery has dramatically accelerated. AI-assisted development, automatedCI/CDpipelines, and cloud-native architectures have made it possible for teams to deploy software dozens of times per day.

But speed alone does not guarantee reliability.

AtConf42 Site Reliability Engineering (SRE) 2026,Uma Mukkara,Head of Resilience Testing at Harnessand co-creator of LitmusChaos, delivered a clear message:outages are inevitable. In modern distributed systems, assuming your design will always work is not just optimistic—it’s risky.

In fact, as Uma put it,failure in distributed systems is a mathematical certainty.

That’s whyresilience testingmust become acore, continuous practice in the Software Development Life Cycle (SDLC).

## The Reality of Inevitable Outages

Even the most reliable cloud providers experience outages.

Uma illustrated this with examples that highlight how unpredictable failures can be:

* Physical disruptionsuch as drone strikes affecting AWS Middle East data centers
* Policy or configuration errorsthat triggered cascading outages on cloud platforms like Azure
* Retry storms and load spikeswhere services collapse under unexpected demand

These incidents demonstrate an important reality:the types of failures constantly evolve.

A system validated during design may not be resilient against tomorrow’s failure scenarios. Architecture may stay the same, butthe failure patterns surrounding it continuously change.

This is why resilience cannot rely on assumptions.

Hope is not a strategy—verification is.

‍

For a deeper look at thisbroader approach to resilience, see howchaos engineering, load testing, and disaster recovery testing work together.

## What Resilience Really Means

Resilience is often misunderstood as simply keeping systems online.

But uptime alone does not make a system resilient.

Uma defines resilience more precisely:

Resilience is the grace with which systems handle failure and return to an active state.

In practice, a resilient system must handlethree categories of disruption:

### 1. System Failures

Pod crashes, node failures, infrastructure disruptions, or network faults.

### 2. Load Conditions

Traffic spikes or sudden demand that pushes systems to their limits.

### 3. Disasters

Regional outages, multi-AZ failures, or infrastructure loss that require recovery mechanisms.

If teams test only one of these dimensions, they leave significant risks undiscovered.

True resilience requiresverifying how systems behave across all three scenarios.

## Continuous Verification in the SDLC

One of the biggest challenges Uma highlighted is how organizations treat resilience.

Many teams still see it as a“day-two problem”—something SREs will handle after systems are deployed.

Others assume that once resilience has been validated during system design, the problem is solved.

In reality, resilience must becontinuously verified.

As systems evolve with each release, so do their failure modes. The most effective strategy is to:

* Test resilience continuously
* Verify resilience with every delivery
* Document results across releases

This approach shifts resilience testing into theouter loop of the SDLC, alongside functional and performance testing.

Instead of waiting for production incidents, teams proactively identify weaknesses before customers experience them.

## Understanding Resilience Debt

Uma introduced an important concept:resilience debt.

Resilience debt is similar totechnical debt. When teams postpone resilience validation, they leave hidden risks unresolved in the system.

Over time, that debt accumulates.

And when failure eventually occurs—which it inevitably will—thebusiness impact grows proportionally to the resilience debt that was ignored.

The only way to reduce this risk is to steadily increaseresilience testingcoverage over time.

As testing matures across multiple quarters, organizations gain better feedback about system behavior, uncover more risks earlier, and continuously reduce the likelihood of severe outages.

## A Holistic Approach to Resilience Testing

Another key takeaway from Uma’s session is that resilience testing should not happen in silos.

Many organizations treat chaos testing, load testing, and disaster recovery validation as separate initiatives owned by different teams.

But the most meaningful risks often appear when these scenarios intersect.

For example:

* A resource bottleneck might only appear whenhigh traffic coincides with a service failure.
* Chaos experiments developed for reliability testing can also be reused indisaster recovery workflows.
* Combining chaos and load tests helps teams observe system behaviorat failure limits under real-world conditions.

That’s why resilience testing must be approached as aholistic practicecombining:

* Chaos Engineering
* Load Testing
* Disaster Recovery (DR) Validation

You can explore the fundamentals of resilience testing in theHarness documentation.

## Collaboration Across Teams

Resilience testing also requires collaboration across multiple roles.

Developers, QA engineers, SREs, and platform teams all contribute to validating system reliability.

Uma pointed out that many organizations already share infrastructure for testing but run different experiments independently. By coordinating these efforts, teams can:

* reuse testing environments
* share chaos experiments across testing scenarios
* validate DR workflows more frequently
* improve testing efficiency across teams

Resilience becomes significantly stronger whenpersonas, environments, and test assets are shared rather than siloed.

## The Role of AI in Resilience Testing

As systems become more complex, another challenge emerges:knowing what to test and when.

Large organizations may have hundreds of potential experiments, making it difficult to prioritize testing effectively.

Uma described howagentic AI systemscan help address this challenge.

By analyzing internal knowledge sources such as:

* incident data
* CI/CD pipelinehistory
* infrastructure configuration
* operational documentation

AI systems can recommend:

* the most relevant chaos experiments
* appropriate load testing scenarios
* disaster recovery tests that should run at a given time

These recommendations allow teams to runthe right tests at the right moment, improving resilience coverage without overwhelming engineering teams.

## A Unified Platform for Resilience Testing

To support this holistic approach, Harness has expanded its original Chaos Engineering capabilities into a broader platform:Harness Resilience Testing.

The platform integrates multiple testing disciplines in a single environment, enabling teams to:

* design chaos experiments
* run load tests
* validate disaster recovery workflows
* observe system risk patterns in one place

By combining these capabilities, teams gain asingle pane of glass for identifying resilience risks across the SDLC.

This unified view allows organizations to track trends in system reliability and proactively address weaknesses before they turn into production incidents.

## Resilience Is a Core Practice for Modern SRE Teams

Uma closed the session with a clear conclusion.Resilience testing is not optional.

Outages will happen. Infrastructure will fail. Traffic patterns will change. Dependencies will break.

What matters is whether organizations havecontinuously validated how their systems behave when those failures occur.

The more resilience testing coverage teams build over time, the more feedback they receive—and the lower the potential business impact becomes.

In modern software delivery, resilience is no longer just a reliability practice.

It is acore discipline of the enterprise SDLC.

Ready to start validating your system’s resilience?

Explore Harness Resilience Testing andstart validating reliability across your SDLC.

Get Started

## Get Started with Harness AI

Try the full platform free. No module restrictions, no credit card.

Try Harness AI Free
See Harness AI Demo
Uma Mukkara
Head of Chaos Engineering
Uma Mukkara is Head of Chaos Engineering at Harness, where he helps teams improve reliability by safely testing how systems behave during real-world failures. Earlier, Mukkara co-founded MayaData and helped build cloud-native technologies such as OpenEBS.
uma-mukkara
https://www.linkedin.com/in/uma-mukkara/