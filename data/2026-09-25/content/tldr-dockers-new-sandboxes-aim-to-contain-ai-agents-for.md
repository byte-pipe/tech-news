---
title: Docker's new sandboxes aim to contain AI agents for real
url: https://www.theregister.com/ai-and-ml/2026/09/24/dockers-new-sandboxes-aim-to-contain-ai-agents-for-real/5298964
site_name: tldr
content_file: tldr-dockers-new-sandboxes-aim-to-contain-ai-agents-for
fetched_at: '2026-09-25T21:59:52.073706'
original_url: https://www.theregister.com/ai-and-ml/2026/09/24/dockers-new-sandboxes-aim-to-contain-ai-agents-for-real/5298964
date: '2026-09-25'
published_date: '2026-09-24T19:51:26.000Z'
description: With Cloud Sandboxes, devs can keep agents at arm's length
tags:
- tldr
---

ai and ml

 

# Docker's new sandboxes aim to contain AI agents for real

With Cloud Sandboxes, devs can keep agents at arm's length

Thomas Claburn

Thomas

Claburn

AI AND SOFTWARE REPORTER

Published

thu 24 Sep 2026 // 20:51 UTC

### READ MORE

* #### Frontier AI keeps racing despite calls to slow down2 days ago
* #### Security firm finds naming AI agents after Seinfeld characters helps bots join the team2 days ago
* #### ABBYY gives old-school OCR a job in the AI pipeline3 days ago
* #### Anthropic-linked CVEs pile up, attackers mostly shrug3 days ago
* #### Treasury chief says AI bosses, not their bots, will carry the can for criminal acts4 days ago

In a market where AI agents keep breaking the rules and escaping their containers, Docker has a new solution. On Thursday, the company debuted Cloud Sandboxes in a bid to keep AI agents within boundaries.

Despite the existence and implementation of sandboxing technology as a way to limit the reach of AI agents, industry leaders like Anthropic and OpenAI keep reporting containment failures.

On Thursday, Australian officialsdisclosedthat an OpenAI agent had accessed an Australian government portal without authorization while seeking health statistics. It's the latest in a series of incidents involving AI agents pushing beyond access controls their operators expected them to respect.

REG AD

On the heels ofDocker Sandboxes, the container biz is now offering a hosted option, which puts a bit more distance between squirrely AI and precious locally stored files.

REG AD

"We're announcing todayDocker Cloud Sandboxes, which is a simple, flexible set of compute shapes with simple low, low pricing," said Docker president and COO Mark Cavage at theWeAreDevelopers Conference.

"We have cloud sandboxes that boot in hundreds of milliseconds. They're billed by the second, and they have secrets, policies, networks, agent config, CloudMCP gateways, all built in."

With a nod to the elephant in the room – the ability of AI agents to bypass barriers – Cavage demonstrated how Anthropic's Claude model, despite being started in a Docker container, can find a locally stored secret outside the container by probing its environment and finding a hole – the mounted host Docker socket.

"Agents are going to find the edges of your environment because they need to mutate your environment," he said, adding that the capabilities that make agents useful and powerful are the ones that allow them to push past boundaries.

It's not that containers are insecure, said Cavage. They're doing the job they were designed to do, to isolate applications. "We have to separate containers from containment," he said.

Cavage invited Docker principal engineer Michael Irwin on stage to demonstrate sandbox-based containment. Launching Claude in a Docker Sandbox, Irwin gave the model the same prompt to find a local secret, and this time the AI model could not do so.

"The isolation holds," said Irwin. "And in fact, if we look at the summary that's in the output here, we can see that it's found a Docker socket, it tried to utilize it to mount other spots from the host and privileged container and it just couldn't get there. And that's because the sandbox is running as a full micro VM."

That's the case for sandboxes and it now extends to the cloud, giving developers the option to process long-running jobs on external infrastructure. This removes the need to access a local machine but still provides the option to shift work back to a local device if needed.

REG AD

"Sandboxes are part of the containment story, but not all of it," said Cavage. "They're the deterministic base layer, while policies are what govern the agent's intent. As an industry, we still have work to do applying policy and intent controls across every layer of the stack agents touch, but having that deterministic base layer in place should be the absolute minimum requirement."

Docker has also updated its Kits specification for packaging agents, tools, and rules into a shareable artifact. Kits now come as standard OCI images, which may address concerns about being locked into a proprietary format.

One such Kit comes from BAND, which makes enterprise infrastructure for distributed AI agent deployments. TheBAND Python Kit for Docker Sandboxesprovides a way for AI agents to work with one another over a WebSocket connection without operating in the same environment. The idea is to give developers more control and tools to observe what agents are doing within defined boundaries.

Pricing for Docker Cloud Sandboxes varies with instance size, starting with Micro (1 VCPU, 2GB) for $0.07 per hour, and extending to XL (16 VCPUs, 32 GB) for $1.12 per hour. ®

anthropic

ai and ml

claude

container security

docker

ai agents

REG AD

## Valen creator drives 'Golden Spike' to connect new languages with Rust

An experiment is afoot to sidestep C as the language of interoperability with Rust

## Microsoft cells out, crams multiple values into Excel boxes

Once a single-scalar home, spreadsheet cells are being redeveloped to handle many tenants

## Huawei Cloud Rolls Out Enterprise AI Products Across the Board, Building an Open Agentic Cloud

PARTNER CONTENT: Huawei Cloud strengthens the silicon bedrock on the cloud

## Uncle Sam coughs up $1.9B for grid upgrades as datacenters hit a power wall

Better conductors and improved sensing capabilities expected to unlock at least 23 gigawatts of additional capacity

systems approach

## In the age of AI, teaching networking principles remains more important than learning protocols

Kids can learn why BGP matters in a semester, but that won’t leave them ready to implement it

## Fake Google Security Team ad says 'no script reading' in voice phishing - then prints the script

More mockery and memes from the Dark Web Roast

### TOP STORIES

* #### Anthropic decides to support OpenAI's markdown instructions spec
* #### Microsoft agentically ports Copilot runtime to Rust for $120K
* #### KPMG tech cuts come with a severance sum some staff call insulting
* #### ShinyHunters claims FBI hack: 'This is NOT financially motivated'
* on call#### Techie fixed Wi-Fi dead zone with a drill
* #### Astronomer watches Starlink satellites sinking to build a ‘planetary barometer’

### AI

* #### Google's TPUs to catch some rays in orbit next weekPart of Project Suncatcher, the proof of concept aims to see how well lightly modified compute fares in orbit
* #### Meta's new AI fidget is a ... Tamagotchi?We hope Zuck's Muse Charm doesn't die if you neglect it
* #### CVE flood pushes Ubuntu onto weekly kernel release cycleAI-assisted bug hunting is helping pile up vulnerabilities faster than defenders can patch them, so Canonical is picking up the pace
* #### Google to critical infra orgs: Our AI scanners won't be evil, promiseGemini 3.8 Flash Cyber and Wiz's Red Agent team up to protect hospitals, public transit, and tech
* #### Shut up and calculate: Jev's new AI primitives for codersDevelopers test what they can build with TypeSafe's fast, typed decision model

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### KDE turns 30 and someone's brought an AI-native desktop proposalAkademy talk imagines Plasma assembling itself around a personal model of each user
* #### Shopify extends lifeline to Tailwind as vibe coding erodes web dev platform's bottom lineAcquisition gives open source CSS framework 'a stable long-term home'
* #### Switzerland tests a FOSS escape route from Microsoft 365Swiss Army sticks a knife in American cloud apps with its own FOSS push
* #### Feel peak Windows was 7? You might like Kumander LinuxDebian and Xfce – solid, sensible choices – with a pretty skin
* #### Canonical shuttering some of its legacy chat channelsThe Ubuntu Pastebin went in June, IRC gets demoted next
* #### Audacity audio-editing app no longer looks like it's from the early 2000sThe FOSS tool for audio editing has a fresh coat of paint, and new features to boot