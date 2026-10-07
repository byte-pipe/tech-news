---
title: AWS launches open-source AI agent sandbox to prevent YOLO mode disasters
url: https://www.theregister.com/ai-and-ml/2026/10/07/aws-launches-open-source-ai-agent-sandbox-to-prevent-yolo-mode-disasters/5301687
site_name: tldr
content_file: tldr-aws-launches-open-source-ai-agent-sandbox-to-preve
fetched_at: '2026-10-07T23:28:46.337943'
original_url: https://www.theregister.com/ai-and-ml/2026/10/07/aws-launches-open-source-ai-agent-sandbox-to-prevent-yolo-mode-disasters/5301687
date: '2026-10-07'
published_date: '2026-10-07T17:42:06.000Z'
description: Strands Box is the latest open source AI control tool from the cloud giant; like its predecessors, it promises tighter reins on autonomous agents
tags:
- tldr
---

ai and ml

 

# AWS launches open-source AI agent sandbox to prevent YOLO mode disasters

Strands Box is the latest open source AI control tool from the cloud giant; like its predecessors, it promises tighter reins on autonomous agents

Brandon Vigliarolo

Brandon

Vigliarolo

GOVERNMENT AND IT NEWS REPORTER

Published

wed 7 Oct 2026 // 18:42 UTC

Make us preferred on Google

### READ MORE

* #### OpenAI dots inspire open source imitators amid technical difficulties1 hour ago
* #### Attackers hijacked top-level domains, minted fake security certs for Google and other orgs2 hours ago
* #### US states sue popular kitmaker TP-Link over China risks4 hours ago
* #### Poetry is the new AI security threat as PoeLLM malware infects 3K+ servers6 hours ago
* #### FortiBleed still a bleeding nuisance as FBI confirms ongoing attacks11 hours ago

AWS has offered multiple open-source strategies for holding AI agents accountable, and now it’s adding a full-on sandbox to this stack.

DubbedStrands Box, the new solution uses OS-level isolation and some of AWS’ other recent open-source AI control tools to, ostensibly, retain greater control over autonomous AI agents’ behavior.

“Agents increasingly run in ‘YOLO mode,’ approving every action without human review,” the AWS team explained in its announcement. “The usual solution to this problem is a sandbox … but access is only part of what we want to control.”

REG AD

The problem with containers and microVMs typically used to isolate AI agents, as AWS explains it, is that their strong isolation doesn’t come with contextual rule enforcement. In other words, when a containerized or virtualized agent gets hold of a tool, there may be no stopping it from doing whatever it wants - like deleting a production database, or gaining access to the internet and doingdog knows what.

REG AD

That’s where the other open-source tools inside Strands Box come in: It uses theDogwood Local Engineto give the policy engine in Box temporal awareness, so tool calls can be checked against not only what the agent wants to do, but what it’s already done.

As one example, AWS noted that an agent could be allowed to post status updates to Slack, but no more than three times every ten minutes to prevent it from spamming its human operators. An AWS spokesperson further explained that Box could be used to control when an agent can perform a Git push, or it could be used toput a cap on API callsthat could end up costing a small fortune.

Additionally, Strands Box includes Strands Shell and Monty for Python, which expose shell and Python operations to the same Dogwood policy engine and event history, making agentic actions clearer to developers and allowing policies to account for what an agent is trying to do.

AWS VP and distinguished engineerMarc Brooker, one of the folks behind Dogwood and Strands Box, explained toThe Registerthat the interpreters are a key part of making agentic behavior more intelligible, which allows for devs to write more precise policies to prevent agents from taking bad actions.

“Box’s Shell and Python interpreters expose operations such as file deletions, while its gateways expose API requests and tool calls,” Brooker told us in an email. “Policies can then account for the action being attempted and earlier activity.”

Box, Brooker added, enforces those rules without trusting or relying on agents to actually follow instructions, which should ideally prevent them from running roughshod over their operators’ wishes.

As for the reason behind AWS’ push to develop open-source tools like Dogwood, the Dogwood Local Engine, and Strands Box, Brooker said that AWS wants to find the right balance between boundaries and policies that prevent agentic AI disasters of the kind we regularly report.

“Box enforces the policies developers configure, deterministically, and the agent can't talk its way around these rules,” Brooker explained, though he added that, even with properly configured permissions, an agentic action can still produce an unwanted result.

REG AD

“Developers remain responsible for deciding what access to grant and where human review is needed,” Brooker added - in other words, don’t let your YOLO mode go too YOLO. A bit of human oversight is still necessary.

“Agent safety is an area where the industry still has significant work to do, and we're committed to continuing to invest in it, both inside the AWS cloud and in open source,” Brooker said.

Strands Box supports any agent or harness one wants to confine within its walls and isavailableon GitHub now, though only for macOS for the time being. Linux support is in development, and AWS told us a Windows client is “on our radar,” but neither has a planned release date. Deployment to platforms like AgentCore, ECS, and Kubernetes is also planned. ®

agentic ai

security

open source

aws

ai and ml

Make us preferred on Google

REG AD

## Microsoft is about to let Copilot loose on your file system

But don't worry, it's totally safe because the agents and models will (probably) be running locally. Routers never break right?

## OpenAI dots inspire open source imitators amid technical difficulties

Persistent agents appeal to AI companies, but demand isn't obvious

## The VMware exit is a protection upgrade

PARTNER CONTENT: VergeIO says an exit is also an opportunity

## Argonne scientists create chatty X-ray microscope that zooms in where you tell it to

Talking to an X-ray nanoprobe beamline is far better than talking to a toaster, we assume

OPINION

## Brighter isn't better and more is less. The AI slowdown is nigh, no matter who says what

Meta isn’t helping — or perhaps it is

## Microsoft N1Xes Intel in favor of Nvidia's shiny new SoCs in Surface Laptop Ultra

Poverty-spec model starts at $2,599 with 24 GB of RAM and 512GB of storage with 128 GB models topping $5,899

### TOP STORIES

* #### AI models keep posting screenshots showing sensitive data from inside tech companies
* #### Stanford prof is beating the drum for a new protocol to replace TCP
* #### Teen suspected of running KillSec ransomware group as cops seize servers, arrest three
* #### Games Workshop seeks IT leader to summon the legions in epic saga battling the forces of ERP
* #### Microsoft makes Windows settings backup the default in 26H2
* #### Nvidia debuts $4,999 DGX Spark with half the RAM and storage, amid memory crunch

### AI

* #### Microsoft is about to let Copilot loose on your file systemBut don't worry, it's totally safe because the agents and models will (probably) be running locally. Routers never break right?
* #### Microsoft N1Xes Intel in favor of Nvidia's shiny new SoCs in Surface Laptop UltraPoverty-spec model starts at $2,599 with 24 GB of RAM and 512GB of storage with 128 GB models topping $5,899
* #### Rails originator roasted over Rust boosterismDavid Heinemeier Hansson's agent-coded bakeoff produced curious results
* #### Google teams with nuclear power giant to give reactors a tune-upUpgraded turbines, generators, and digital controls are expected to unlock an addition 890MW of capacity
* #### Schneider Electric drops $22.6B on PTC as datacenter boom rains money on infra companiesPart of a bigger play for smarter power infra

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### OpenAI dots inspire open source imitators amid technical difficultiesPersistent agents appeal to AI companies, but demand isn't obvious
* #### Ubuntu 'Stonking Stingray' beta swims out: Deeper Rust 'oxidization' plus LLM speech-to-textGNOME 51 is here, and Ubuntu interim releases are getting interesting again
* #### Revive Raskin's 3 laws of software with humane work that considers a dev's duty of careAll this, and angry NeoVim users
* #### Firefox 157: Could bold new look be just what Mozilla needs?*Yet another new version of Firefox, with a significant reskin
* #### KDE turns 30 and someone's brought an AI-native desktop proposalAkademy talk imagines Plasma assembling itself around a personal model of each user
* #### Shopify extends lifeline to Tailwind as vibe coding erodes web dev platform's bottom lineAcquisition gives open source CSS framework 'a stable long-term home'