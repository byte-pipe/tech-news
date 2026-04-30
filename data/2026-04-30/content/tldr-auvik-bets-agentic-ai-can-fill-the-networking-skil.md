---
title: Auvik bets agentic AI can fill the networking skills gap | Network World
url: https://www.networkworld.com/article/4165098/auvik-bets-agentic-ai-can-fill-the-networking-skills-gap.html
site_name: tldr
content_file: tldr-auvik-bets-agentic-ai-can-fill-the-networking-skil
fetched_at: '2026-04-30T20:09:05.805222'
original_url: https://www.networkworld.com/article/4165098/auvik-bets-agentic-ai-can-fill-the-networking-skills-gap.html
date: '2026-04-30'
description: Auvik Bets on Agentic AI to Fix Network Ops Skills Gap (6 minute read)
tags:
- tldr
---

by									
Sean Michael Kerner

Contributing Writer

# Auvik bets agentic AI can fill the networking skills gap

News

Apr 29, 2026
6 mins
 

## Auvik is bringing agentic AI to network and IT operations with its Aurora platform.

 

							Credit: 															Gorodenkoff / Shutterstock													

IT teams managing multi-vendor networks are dealing with a growing volume of alerts and a shrinking pool of engineers with the expertise to act on them. AI, and more specifically agentic AI, is increasingly being positioned as the approach to solve that challenge.

The latest vendor to embrace agentic AI isAuvik,which has been building out a cloud-based IT and network management platform for the past 15 years. The company was founded with a straightforward mission: bring network management to organizations that couldn’t afford the complexity of traditional on-premises tooling, and do it across whatever mix of vendors they happened to run.

This week the company is launching Aurora, an agentic AI platform designed to push beyond alerting and into automated remediation. The direction was shaped by customers who had grown impatient with AI that doesn’t translate into action.

“Our customers have been very clear, and our customer advisory boards, when you come out with something, it has to be something that solves real world problems, and not just AI or agentic, for the sake of AI,” Doug Murray, CEO of Auvik, toldNetwork World.“We expect you to provide us with an experience that is going to help me automate and simplify things. That’s what we care about. We don’t care about some fancy AI nomenclature.”

## What Aurora does differently to simplify network operations

Before Aurora, the platform told IT teams there was a problem. Aurora is designed to tell them exactly what to do about it and, over time, do it for them.

* Alert prioritization.Rather than a flat alert feed, the platform ranks incoming alerts by impact in a red/yellow/green view. An MSP technician arriving to 20 alerts sees the three that matter first.
* Device lifecycle management.Aurora surfaces EOL and end-of-support status for managed devices in a ranked dashboard. A customer managing 100 devices gets a notification identifying exactly which SonicWall Gen 7 firewalls need to be rolled back and the scope of the exposure, not just that a problem exists.
* CVE monitoring (beta).Agents scan managed devices against known vulnerabilities proactively, surfacing exposure before reactive ticketing forces the issue.
* Scripting assistance.A technician unfamiliar with a device’s CLI can ask Aurora how to remediate an issue in natural language and receive a generated script to execute directly.

The longer-term direction is fully automated remediation. Aurora represents what Auvik calls the “Do” phase of a framework the company’s founders put on a whiteboard in its earliest days: See, Tell, Do. See is about visibility — knowing what’s in your infrastructure. Tell is alerting and prescriptive notification, telling teams what’s happening and what needs attention. Do is where Aurora comes in, moving the platform from surfacing problems to acting on them.“People will call it self driving, if you will,” Murray said. “But it’s really taking all of that and driving more into automation.”

## How it works

What separates Aurora from a generic AI layer bolted onto a network management platform is what’s underneath it. Aurora’s recommendations are grounded in live network context pulled from Auvik’s own infrastructure, not general training data, built up through years of on-network data collection across thousands of customer environments.

* The collector.Auvik’s on-network collector agent continuously pulls device state, topology, configuration and performance data from every managed device and sends it to a central cloud repository. That live data stream is the foundation Aurora operates against.
* The data foundation.Over 15 years of SaaS-based network management, Auvik has accumulated more than 300 million device configuration backups and 2.2 billion CLI command executions across hundreds of supported vendors. The platform currently manages more than 10 million devices daily. Aurora’s recommendations are grounded in that history, not generic training data.
* The agentic layer.Murray described the architecture as primarily contextual. The agents don’t rely on fine-tuning or traditional retrieval-augmented generation. They operate against the live context of a specific customer’s network, drawing on both real-time collector data and patterns from the broader dataset to surface recommendations specific to that environment. Getting there required significant data preparation work. “When we actually started taking all of that data about four years ago and worked through it, it wasn’t very clean,” Murray said. “It was basically, literally, just reams of data that we were trying to figure out architecturally, how to turn it into action.”
* The AI stack.The platform is built on proprietary infrastructure but uses Claude as its predominant LLM, with OpenAI models applied to specific functions. Murray said the shift to agentic AI tooling over the past two years made it substantially easier to mine Auvik’s historical dataset than the proprietary ML approach the company had been pursuing earlier.

## The talent gap

Fundamentally there is a structural problem that underpins the whole Aurora thesis as to why more automation is needed.

“There aren’t a lot of kids that are coming out of university today that are studying Cisco CLI or deep networking oriented expertise,” Murray said. “And so because of that, you have a lot of people that know infrastructure in the IT segment that will be retiring in the next five to 10 years.”

Aurora’s scripting assistance and push toward auto-remediation are both direct responses to that gap.

“Being able to create this in a way where we try to make it such that you don’t need to be a networking person to run the networking infrastructure is really the vision of where we’re trying to take this,” Murray said. “So the more we can automate and simplify and help people with auto remediation, the more powerful the platform becomes.”

Network Management Software
Networking
Artificial Intelligence
 

 

				SUBSCRIBE TO OUR NEWSLETTER			

### From our editors straight to your inbox

				Get started by entering your email address below.			

 

Please enter a valid email address

Subscribe

														by 															

																Sean Michael Kerner															

Contributing Writer

1. Follow Sean Michael Kerner on X

Sean Michael Kerner is an IT consultant, technology enthusiast and tinkerer, and has been known to spend his spare time immersed in the study of the Klingon language and satellite pictures of Area 51. He has pulled Token Ring, configured NetWare and has been known to compile his own Linux kernel. He consults to industry and media organizations on technology issues.Sean's writing has appeared inVentureBeat,InternetNews,TechTarget,ITPro Today,Data Center Knowledge, andTechCrunch, among other outlets.

## More from this author

* news### How Zero Networks is closing the network enforcement gap for AI agentsApr 21, 20265 mins
* news### Cloudflare wants to rebuild the network for the age of AI agentsApr 20, 20266 mins
* news### Linux 7.0 debuts with some big changes for networkingApr 13, 20265 mins
* news analysis### Lumen: Upstream network visibility is enterprise security’s new front lineApr 9, 20269 mins
* news### Aria Networks raises $125M and debuts its approach for AI-optimized networksApr 8, 20266 mins
* news### OpenStack Gazpacho is a dish best served cold for hot cloud networksApr 1, 20266 mins
* news analysis### How Lumen is dismantling decades of network complexityMar 30, 20267 mins
* news### Meshery 1.0 debuts, offering new layer of control for cloud-native infrastructureMar 25, 20267 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

news
 
 

### IT certification pay surges as noncertified skills slump

 
By Denise Dubie
Apr 30, 2026
4 mins

Careers
Certifications
IT Jobs

news
 
 

### QuEra claims quantum error correction breakthrough with 2-to-1 qubit ratio

 
By Maria Korolov
Apr 30, 2026
4 mins

Data Center
High-Performance Computing

feature
 
 

### Deconstructing the data center: A massive (and massively liberating) project

 
By Esther Shein
Apr 30, 2026
14 mins

Cloud Computing
Data Center
Data Center Management

podcast
 
 

### Has the hype around ‘Internet of Things’ paid off? | Ep. 145

 
Apr 18, 2024
36 mins

IoT Platforms
IoT Security

podcast
 
 

### Episode 1: Understanding Cisco’s Converged SDN Transport

 
Sep 24, 2021
20 mins

Cisco Systems
Internet
Networking

podcast
 
 

### Episode 2: Pluggable Optics and the Internet for the Future

 
Sep 23, 2021
17 mins

Cisco Systems
Computers and Peripherals
Internet

video
 
 

### Master Linux Math with the bc Command | Easy CLI Calculations Explained!

 
Jun 23, 2025
1 mins

Operating Systems

video
 
 

### Master Linux Math in Seconds: How to Use the expr Command Like a Pro

 
Jun 17, 2025
1 mins

Operating Systems

video
 
 

### How to Do Math in the Command Line Using Double Parentheses

 
Jun 6, 2025
1 mins

Operating Systems