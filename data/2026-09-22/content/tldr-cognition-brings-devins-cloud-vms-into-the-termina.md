---
title: Cognition brings Devin's cloud VMs into the terminal, SSH included
url: https://runtimewire.com/article/cognition-devin-cloud-terminal-ssh
site_name: tldr
content_file: tldr-cognition-brings-devins-cloud-vms-into-the-termina
fetched_at: '2026-09-22T08:46:41.353757'
original_url: https://runtimewire.com/article/cognition-devin-cloud-terminal-ssh
author: RuntimeWire
date: '2026-09-22'
published_date: '2026-09-21T19:41:43.689Z'
description: Cognition's Devin CLI can now create, resume and steer cloud sessions, provide SSH access to Devin VMs, and move work between local and cloud environments.
tags:
- tldr
---

Primary source:Cognition on X

## Why it matters

Cognition is turning Devin's VM into shared infrastructure for agents and developers, reducing the friction between interactive local coding and long-running cloud work.

Scott Wu (@ScottWu46)'s Cognition launched command-line controls and full SSH access for Devin Cloud on Monday, letting developers start, steer, resume and directly enter the remote virtual machines used by its coding agent,Cognition said in a thread on X.

https://x.com/cognition/status/2102104259219406886

The release turns Devin's cloud environment into an extension of the developer's terminal. A session can begin locally, move to a dedicated cloud VM for longer or more compute-heavy work, and return to the developer's machine for final edits. Developers can also enter the VM themselves to inspect files, run commands and test Devin's output.

Wu, Cognition's co-founder and CEO, built the AI networking service Lunchclub before starting Cognition. He grew up competing in mathematics and programming contests, winning three International Olympiad in Informatics gold medals and representing Harvard at the 2016 International Collegiate Programming Contest, according to aprofile published by Stripe. That competitive-programming background has shaped Cognition's pitch: software agents should own complete engineering tasks while people set direction and review the result.

### The terminal becomes Devin's control plane

Developers can start a cloud session withdevin --cloudor switch a fresh local session by entering/cloud. Cognition'sDevin Cloud documentationsays the remote environment includes a shell, browser and cloned repositories. The CLI streams the cloud session into the terminal, while the work continues on the VM if the terminal closes.

A developer can later resume a session by ID or URL usingdevin --cloud --resume. The same cloud session can also open in Devin's web interface or Devin Desktop, giving developers a visual view when they need to inspect the agent's desktop or review a recording.

The more consequential addition isdevin ssh. Cognition'sSSH documentationsays the command wraps the standard SSH client and authorizes the connection using the developer's logged-in Devin credentials. Developers can open a shell on the VM, edit code, use remote-SSH editor extensions, copy files withscp, and forward a remote port to localhost to test a running application.

That access changes the working relationship between the developer and the agent. Devin's VM was previously an environment developers delegated work into. It can now function as a remote development machine that both Devin and the human operator use during the same task.

### Moving work in both directions

Cognition is also making the boundary between local and cloud execution reversible. The/handoffcommand packages the current conversation, Git branch and uncommitted changes before starting a cloud session. Cognition'shandoff documentationwarns that the work-in-progress diff is transferred with the session, so developers must commit or stash anything they do not want sent.

From a cloud session,/handoffor/pickupfetches Devin's pull-request branch, switches the local checkout to that branch and starts a local session on the same code. That flow is aimed at tasks that move between quick interactive work and longer jobs such as integration tests, Docker builds, deployments, migrations and large refactors.

The release addresses a basic problem in coding-agent workflows: local tools offer immediate access to a developer's files and shell, while asynchronous agents can keep working after the laptop closes. Cognition is combining those modes under one CLI and preserving the session as work moves between them.

The launch follows Cognition's September 15th addition of Mac environments to Devin Cloud, which joined its Linux and Windows options. Together, the releases give Cognition a wider set of cloud machines and a direct terminal path into them.

Cognition has ample capital to build that infrastructure. On September 8th, Cognitionsaid it had raised more than $2 billion at a $48 billion valuation, in a round led by Andreessen Horowitz and Accel. Cognition also claimed that annualized run-rate revenue had risen from $492 million in May to almost $900 million. Those figures are self-reported and Cognition did not provide the underlying revenue period or calculation.

Cognition is offering sessions powered by its SWE-2 coding model free in Devin Cloud through October 8th. Access requires a Devin account and an authenticated installation of the Devin CLI.

## Reader comments

Conversation for this story loads after sign-in.