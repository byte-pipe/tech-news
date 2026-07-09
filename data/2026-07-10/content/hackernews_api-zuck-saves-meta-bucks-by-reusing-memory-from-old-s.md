---
title: Zuck saves Meta bucks by reusing memory from old servers with a custom CXL ASIC
url: https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483
site_name: hackernews_api
content_file: hackernews_api-zuck-saves-meta-bucks-by-reusing-memory-from-old-s
fetched_at: '2026-07-10T09:09:34.533043'
original_url: https://www.theregister.com/systems/2026/06/29/zuck-saves-meta-bucks-by-reusing-memory-from-old-servers-with-a-custom-cxl-asic/5263483
author: ihsw
date: '2026-07-04'
published_date: '2026-06-29T10:43:00.000Z'
description: In production on millions of boxes and the payoff is a 25% reduction in machines needed for some inference workloads
tags:
- hackernews
- trending
---

SYSTEMS

 

# Zuck saves Meta bucks by reusing memory from old servers with a custom CXL ASIC

In production on millions of boxes and the payoff is a 25% reduction in machines needed for some inference workloads

Simon Sharwood

Simon

Sharwood

APAC Editor

Published

mon 29 Jun 2026 // 11:43 UTC

Meta is recovering DDR4 memory from old servers, installing it in new machines, and using a custom Compute Express Link (CXL) ASIC to share the memory across applications – without encountering latency problems.

The social networking giant calls its tech "Vistara" and will present it at ISCA 2026 on Monday, butThe Registerfound the company's paper ahead of the talk. Our sister site,Blocks and Files, also happens to havereported on thison Friday.

The document opens with the admission that Meta can't increase the amount of memory in around 40 percent of its vast server fleet, meaning millions of servers can't handle some of its workloads. That's unfortunate because the expected service life of its servers is three to five years, but memory is useful for seven to ten years.

REG AD

Meta's response is to rip DDR4 DIMMs from old servers, put them into new machines that rely on DDR5, and turn it all into a pool of capacity – which in theory makes it possible to compose virtual servers that share resources across multiple physical hosts.

REG AD

The paper points out that CXL is hard to put into production because sharing memory across hosts can mean low bandwidth, high latency, and extra computing overheads to manage additional memory layers. Those problems can arise in systems that combine different memory technologies. Meta wanted to blend memory types in a single machine but found off-the-shelf CXL kit can't do the job.

"Most CXL solutions bundle DRAM with the controller – preventing DIMM reuse – and often omit DDR4 support, which is a requirement for repurposing older memory," the paper states. "Additionally, their high power consumption and high cost further limit their appeal."

To make CXL sing, Meta created a custom ASIC called "Vistara."

"At its core, the Vistara ASIC is designed to bridge DDR4 memory to host processors via a CXL 2.0/1.1-compliant PCIe Gen5 x16 interface," the paper explains. "Each Vistara ASIC integrates two independent 72-bit DDR4 memory channels, supporting speeds up to 3,200 MT/s and up to 256 GB per chip with 64 GB DIMMs."

A pair of custom RISC-V processors drive the ASICs.

Vistara hardware lives in devices Meta calls a "MemServer" powered by an AMD Turin processor packing 158 cores and running 316 threads. Each MemServer combines 768 GB of DDR5 memory alongside 256 GB of DDR4 connected through Vistara ASICs.

## MORE CONTEXT

* ### Memory godboxes could offer relief from the RAMpocalypse
* ### One vendor doesn't mind high RAM prices: VMware
* ### PCIe 7.0 first official draft lands, doubling bandwidth yet again
* ### Micron joins the CXL 2.0 party with a 256GB memory expander

"The Vistara CXL cards are installed in dedicated rear-accessible slots within each MemServer chassis," the paper reveals. "To manage the increased thermal load from high-density memory and CXL devices, the chassis employs directed airflow with high-capacity fans that channel cool air directly across the Vistara modules, for stable operation under heavy workloads."

The software side of Vistara sees the DDR4 presented to the OS "as a distinct, CPU-less NUMA node, separate from the local DRAM nodes directly attached to the processor." Meta's platforms first use all available local DDR4, then employ the CXL-enabled memory when needed.

REG AD

Zuck's house of hyperscale hypnotism makes this happen with custom tweaks to the Linux CXL driver. "All Linux kernel CXL driver code in use for Vistara is either present in the upstream kernel, or is on its way to being included in the upstream kernel," the paper states.

The paper says Meta has put this CXL stuff to work "in hyperscale infrastructure with millions of servers, across a variety of production workloads, including disaggregated ML inference (embedding tables in recommendation systems), big data processing, databases, distributed caches, and CI/CD build systems."

Some workloads, including big data tools such as Spark and Hive, use terabyte and petabyte-scale datasets, and need hundreds of gigabytes of memory per job. The paper says that if those workloads experience out-of-memory events, it can "disrupt critical business analytics and ML pipelines."

"The expanded memory headroom provided by CXL enhances system reliability," the paper explains. "By mitigating the risk of out-of-memory (OOM) events, CXL reduces the frequency of job failures and the associated overhead of job restarts and resource fragmentation by 33 percent."

Meta says the system also cuts infrastructure costs. "These deployments have demonstrated large benefits, such as reducing the server count by up to 25 percent for disaggregated inference," the paper states. And of course Meta is avoiding the sky-high memory prices caused by theRAMpocalypse. ®

systems

virtualization

memory

mark zuckerberg

cxl

compute express link cxl

server

meta

REG AD

CYBER-CRIME

## An unnamed US county – perhaps in Ohio – paid $1M extortion demand to cybercriminals

Leaked negotiations spill the tea

ai and ml

## AI slop writing has taken over the internet, particularly LinkedIn and X

One in four long-form social media posts appear entirely AI-generated, with nearly half of those on Microsoft's and Elon's platforms involving AI in some form

## Canonical Managed Kubeflow lands on Azure

PARTNER CONTENT: Why platform teams are swapping DIY Kubeflow for Canonical's managed service

ai and ml

## AI tool scours the web for job openings, preps your resume and cover letter

Searching for work sucks; AI combs the internet and sucks it all up. Combine the two and let 'er rip with this Python project

networks

## Media Over QUIC can scale real-time streaming and carry the world's vids

With the low latency of WebRTC and the scalability of DASH

SOFTWARE

## OpenMandriva claims disgruntled admin trashed repos after community bust-up

Linux distro accuses former contributor of deleting years of work and pushing a package that could have broken installs

### MOST POPULAR

* ai and ml#### Even banks and hyperscalers are now sounding the alarm about the AI bubble
* Security#### Hackers shoveled snow for company, were rewarded with network admin access
* OFFBEAT#### C programmers commit fresh crimes against readability
* AI AND ML#### New humanoid robots from China look like creepy pop star action figures – complete with slightly dodgy lip-synch
* software#### Court tosses Microsoft's appeal in pre-owned software licenses battle

### AI

* AI and ML#### OpenAI makes ChatGPT better at banterWith GPT-Live, talking, listening, and formulating answers all happen at once
* ai and ml#### The AI that spawned MechaHitler and deepfake porn puts on a suit to become legal advisor and Excel jockeyThe newly renamed SpaceXAI wants you to believe little ol' Grok is all grown up
* ai and ml#### Intel-backed AI chip startup SambaNova breathes new life into aging Nvidia GPUs in latest benchmarksThird-party testing shows heterogeneous compute platform combining H200s and SN50 RDUs churning out 763 tok/s in MiniMax M2.7
* ai and ML#### Former GitHub CEO launches competitor designed for the age of vibe codingAs GitHub struggles to manage AI load, challengers take aim
* AI and ML#### AI is becoming a bargain hunter's market, with a few luxury models on topInference is become a commodity except for frontier models

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### KDE Plasma users face a dire omen of change: 6.6.6 arrives6.7 is now current, and in 6.8 you're getting Wayland whether you like it or not
* #### Collabora releases CODE 26.04 as rivalry between FOSS cloudy office suites heats upNow with Markdown support and smarter formula error handling – plus integrated AI, though it's off by default
* #### Blast from the past as GIMP 0.54 is revived in Flatpak formRetro-computing fun for the nostalgic with first (and last) release to use Motif instead of GTK
* #### Bcachefs exits experimental status in new 'performance release'More Rust, but more trouble with AI slop, too
* #### France's digital sovereignty push is struggling to escape the Microsoft gravity wellNextcloud rollout shows locally controlled storage is one thing; getting users off Office is quite another
* #### History of CentOS: How a biochemist's Linux hobby project became the enterprise world's default operating systemWhen a community came together after Red Hat said Windows was 'probably the right product'