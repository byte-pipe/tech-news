---
title: AI coding has outgrown the laptop - Islo
url: https://islo.dev/blog/ai-coding-has-outgrown-the-laptop
site_name: tldr
content_file: tldr-ai-coding-has-outgrown-the-laptop-islo
fetched_at: '2026-09-14T22:17:02.501453'
original_url: https://islo.dev/blog/ai-coding-has-outgrown-the-laptop
date: '2026-09-14'
published_date: '2026-09-14T00:00:00.000Z'
description: AI coding began on developer laptops. Autonomous work needs shared, persistent, observable and governable cloud environments.
tags:
- tldr
---

Almost every engineering team I talk to is using AI coding tools, but most are still using them exactly like they used their IDE: one developer, one laptop, one agent session.

That made sense as a starting point. The laptop already had the repository, credentials, compiler, internal certificates, databases, and all the other things nobody had documented properly. Installing Claude Code or Cursor there was the quickest way to find out whether the models were useful.

They are useful. Now the limitations of running them locally are becoming much harder to ignore.

An agent working on somebody’s laptop inherits that person’s access, disappears when the machine goes offline, and leaves most of its reasoning in a private terminal or chat history. Nobody really knows what a bug fix cost, how many approaches failed before the final one, or whether another model would have completed it with fewer retries. The rest of the team sees the pull request, but not much of the work that produced it.

That is fine while the agent is an assistant and the developer is watching it. It breaks down when agents start working for hours, taking several tasks in parallel, waiting for CI, responding to review comments, or calling external systems on the company’s behalf.

At that point, an agent is no longer just a feature inside an editor. It is a workload, and workloads need somewhere proper to run.

## Development is collaborative; local agent sessions are not

When an engineer asks an agent to investigate a bug, the final patch is only part of the useful output. The failed reproduction attempts matter, as do the logs it inspected, the assumptions it made, the tests it ran, and the point where it got stuck.

Most of that disappears inside a local session. If somebody else joins the investigation, they usually get a summary along the lines of “I tried a few things and this seems to work,” then repeat some of the same work because the actual environment and history are sitting on another person’s laptop.

Running the task in a shared cloud environment means another engineer can open the same workspace, inspect the services and logs, understand what the agent has already tried, and continue from there. A reviewer can look beyond the diff and see the evidence behind it, while a security engineer can see which external services the agent contacted and which credentials it used.

I don’t mean recording every developer keystroke or turning engineering tools into employee surveillance. I mean that work delegated to a company-operated agent should be inspectable by the company, just as source code lives in a shared repository and builds run in a shared CI system.

It is strange that we centralized almost every important part of software delivery, then allowed autonomous work to happen in one of the least observable places available.

## Real engineering work survives the session

A developer can usually recover after a laptop restart because they remember why three services were running, which command failed, and what they planned to try next. An agent returning to a clean checkout knows only what somebody managed to preserve in its prompt.

This matters because real work rarely fits into one uninterrupted session. Tests take time, CI fails, reviewers reply the next morning, dependencies land in the wrong order, and product or security decisions can pause a task for days. A migration may touch several repositories and move through multiple people before it is finished.

Keeping a laptop awake overnight is not a good answer to any of this.

A persistent environment can preserve the code, services, artifacts, logs, and task history while the work waits, then let the same agent, a different agent, or a human continue from a known state. This becomes essential when one engineer is supervising several tasks, each with its own branch and dependencies, instead of trying to run all of them locally through a mess of worktrees, ports, containers, and credentials.

I think the unit of development is going to shift from a developer machine to a task environment. Every task will receive the code, compute, tools, identity, policy, and lifetime it needs, and the environment will disappear when the task is actually complete.

## We need better metrics for AI development

Ask most engineering leaders how much they spend on AI coding and they can probably give you the price of the licenses or the total model bill. Ask what it cost to investigate a specific bug and the answer is usually impossible to find.

That distinction is going to matter a lot more as agents do more work. We need to know how much model usage, compute, build time, test time, retries, and human intervention went into an actual outcome. Otherwise, we are measuring input and calling it productivity.

I want to be able to answer questions such as:

* Was this dependency upgrade economical to delegate?
* Why did this feature require six agent attempts before the tests passed?
* Is the cheaper model still cheaper after retries and review time?
* Which repositories spend more time preparing environments than making changes?
* Are we reducing engineering work, or generating more pull requests for humans to repair?

This is an internal weekly view of human and agent-authored output. The trailing four-week average increased from 23,046 to 41,943 lines per week, while merged pull requests rose from 19 to 102; the September bar is a partial week. By late August, the agent account was authoring most of the added lines.

I find the direction exciting, but the chart also shows why counting code and pull requests is not enough. It tells us that output increased; it does not tell us whether the changes were valuable, how much they cost, how much human review they required, or how many survived production without creating more work.

We need a new scoreboard built around completed work rather than generated code:

* Time to verified outcome:How long did it take to move from an issue to a change that passed the required checks?
* Cost per accepted outcome:What did we spend on models, compute, tests, retries, and human review for a change that was actually accepted?
* Autonomous completion rate:What percentage of tasks reached review without an engineer rescuing the agent or rebuilding its environment?
* Human attention per change:How many minutes did engineers spend prompting, unblocking, reviewing, and repairing the result?
* Rework and escape rate:How often was the change reverted, substantially rewritten, or connected to a later defect?
* Waiting versus working time:How much of the run was lost to environment setup, queues, builds, tests, or external approvals?

No single metric is safe on its own. Optimizing for autonomous completion can produce trivial tasks, optimizing for cost can reward weak models that create more review work, and optimizing for speed can reduce quality. The useful view combines outcome, cost, human attention, and what happened after merge.

Those numbers are difficult to connect when the agent runs locally, the tests run somewhere else, and the model usage arrives as one aggregate invoice. A cloud task can tie those events to the same run, which makes it possible to compare the real cost of a flaky-test fix with a migration or a small feature.

Some of the results will be uncomfortable. We will find agent-generated changes that cost more to produce and review than doing them manually, along with repositories where broken setup and slow verification consume far more money than model tokens. That is useful information. AI development should be managed as an engineering system, not defended as a belief.

## The security argument is really about control

Cloud environments are not automatically more secure. A badly isolated remote VM with broad credentials and unrestricted network access may be worse than a laptop.

The problem is that the common local setup is not particularly reassuring either. We give an autonomous process the developer’s permissions, which may include SSH keys, cloud credentials, browser sessions, environment files, unrelated source code, and access to internal systems, then rely on that process behaving like the person whose identity it borrowed.

Moving execution into a controlled environment gives us a chance to do better. Each task can receive its own identity, short-lived credentials, limited network access, isolated compute, and an approval requirement before it merges code, changes infrastructure, or performs a destructive action. When the task finishes, its access and environment can expire with it.

More importantly, the policy is consistent. Security can answer what the agent was allowed to reach, what it actually did, and which human approved the sensitive actions without reconstructing an incident from a developer’s shell history.

That is the security benefit I care about. Not “cloud is secure,” which is obviously too broad to be true, but that cloud execution makes agent access governable in a way that ad hoc processes on hundreds of laptops are not.

## Cloud development environments failed for good reasons

None of this is a new idea. Companies have tried for years to move development into remote containers, VMs, and browser IDEs, usually promising reproducible environments, instant onboarding, tighter security, and the ability to work from anywhere.

For most developers, the laptop still won.

Latency was part of it. A delay that nobody notices in a dashboard becomes irritating when it appears after every keystroke, terminal command, or editor action. Remote terminals stuttered, language servers lagged, port forwarding was awkward, and anything involving graphics, mobile devices, large files, or unusual hardware made the distance from the machine obvious.Experimental research on delayed IDE responseconfirms that developers notice and react to slowdowns in interactive development tools, even though tolerance varies by task and delay pattern.

The harder problem was setup. That supposedly reproducible environment had to capture years of undocumented local state: private registries, certificates, licensed tools, VPN routes, databases, test data, background services, and scripts that quietly depended on one operating system. Platform teams had to build all of this and then keep it current, often to give developers an experience that still felt slower than the laptops they already owned.

That trade-off was not compelling enough for many teams, and saying “cloud development failed” is a little too simple because it worked well in some organizations and workflows, but it clearly did not replace local development as the default. Where teams did make the investment, the later payoff could be substantial:GitHub’s npm engineering team reportedreducing environment setup from hours to minutes and cross-team access from days to minutes after moving the workflow to Codespaces. That is a GitHub case study about a GitHub product, so I would not treat it as a universal benchmark, but it shows how the upfront setup cost can be amortized.

Agents change the equation because they do not care about input latency. An agent does not get annoyed because its editor redraws in 120 milliseconds instead of 20; a human gives it a task and comes back later. The biggest experiential disadvantage of remote development matters much less when the primary worker is software.

At the same time, the old benefits have gone from nice to have to necessary. Agents need environments that can be created through an API, reproduced reliably, observed centrally, isolated from one another, left running without a laptop, and removed when the work ends. If ten agents are working in parallel, letting all of them borrow a developer’s machine is not a workable architecture.

This does not make environment setup easier. It makes the work impossible to avoid.

The private registries, services, initialization steps, network rules, secrets, test data, and verification commands hidden across developer laptops now have to become explicit. I see that less as new overhead created by agents and more as infrastructure debt that agents finally force us to address.

Teams that solve it will get more than faster onboarding. They will have the execution layer required to run autonomous engineering safely and at scale. Teams that don’t will keep powerful agents trapped inside fragile personal setups.

## Cloud development has real downsides

I am obviously making the case for cloud development, but it would be dishonest to present it as the same workflow running in a better location. Teams take on real costs and risks when they move agent work away from developer laptops.

The setup takes longer, especially at the beginning.A developer can often get a repository working locally through a combination of old credentials, manual fixes, and knowledge they have forgotten they possess. A cloud environment forces the team to document all of that before the first task runs successfully. The investment should pay back through repeatability and faster setup later, but the initial migration can be substantial, and some unusual environments may never become completely portable.

More autonomy requires more verification.When a developer watches an agent locally, they are continuously applying judgment even if they do not notice themselves doing it. An asynchronous cloud agent can take the wrong assumption much further, much faster, and several agents can produce several wrong changes at once. Moving execution to the cloud therefore needs stronger tests, deterministic checks, retry limits, and approval boundaries. A remote agent that can run for six hours without supervision but cannot prove its work is not an improvement.

The infrastructure costs are real.Cloud machines, storage, snapshots, network traffic, builds, tests, and idle environments all cost money. Parallel agents can increase that bill very quickly, particularly in repositories with large builds or expensive test suites. Some of this spending replaces developer hardware and waiting time, but not all of it, which is why task-level cost visibility, automatic shutdown, reuse of build outputs, and explicit budgets need to be part of the platform rather than added after the invoice arrives.

Source code and development data become a privacy concern.A cloud environment may contain proprietary code, customer data used for testing, credentials, logs, and prompts that reveal internal architecture. Teams need to know where that data is processed, how long it is retained, whether it is used by model providers, who can access snapshots and logs, and which jurisdictions it enters. For some organizations, the right answer may be a private cloud, regional deployment, hybrid architecture, or keeping certain classes of work local.

These are not minor implementation details, and cloud development should not be the default for every repository simply because agents are involved. The case for it is that the benefits become necessary as agent work grows more autonomous and parallel—not that the trade-offs disappear.

## Local execution should be the exception

Local development still has obvious advantages for humans: immediate interaction, offline access, direct control, familiar tools, and compatibility with every strange dependency a developer has collected over time. None of those advantages makes a laptop the right place to operate autonomous workloads.

If an agent task can run in a cloud environment, it should. Personal preference and easier initial setup are not strong enough reasons to make company work dependent on one person’s machine.

Keep execution local when the workload genuinely cannot handle the cloud: it depends on specialized hardware or USB devices, must work offline or inside an air-gapped network, is blocked by a legal or data-residency requirement, or cannot yet be reproduced faithfully in a remote environment. Even then, the constraint should be explicit rather than turning every developer laptop into the permanent exception.

Developers can still use whichever editor helps them think. The execution behind delegated, long-running, parallel, privileged, or business-critical work belongs in an environment the organization can share, persist, measure, and control. If the company expects to rely on the result, the company should be able to understand how it was produced.

## What engineering leaders should ask now

Whether a team prefers Cursor, Claude Code, or another coding agent matters much less than where the work runs. Models and interfaces will keep changing, while the underlying requirements are becoming fairly clear:

1. Can another engineer inspect and continue the task?
2. Does its state survive interruptions, CI failures, and approval waits?
3. Can cost be attributed to a bug, feature, or migration?
4. Which identity, credentials, and network access does it receive?
5. Which actions require tests, policy checks, or human approval?
6. What evidence remains when the work is complete?

If every answer depends on the developer who started the session and the laptop sitting in front of them, the team has adopted AI tools, but it has not built an operating model for AI development.

Source control moved from local history into shared systems, builds moved into CI, and production debugging moved into centralized observability. Local tools remained useful through every transition, but they stopped being the place where the organization kept and operated the work.

AI development will move the same way, driven by parallelism, longer-running tasks, shared ownership, and the need to understand what agents are actually doing. The direction is already visible in the products:Cursor Cloud Agentsrun in dedicated VMs, whileClaude Code on the webruns each session in a fresh managed VM that persists independently of the laptop. These are vendor descriptions rather than independent evidence of outcomes, but competing tools arriving at remote, isolated execution is a meaningful signal about where the architecture is going.

An assistant can live in an editor; an autonomous agent needs an identity, a budget, an environment, telemetry, and an owner.

AtIslo, this is the transition we are building for: agents running in secure environments, connected to the tools they need to finish real engineering work. The goal is not to remove developers from the process, but to stop pretending that a personal laptop is sufficient infrastructure for the work they can now delegate.