---
title: Backbone of a beast – charting Nvidia's rise to networking titan
url: https://www.theregister.com/networks/2026/10/31/backbone-of-a-beast-charting-nvidias-rise-to-networking-titan/5306499
site_name: tldr
content_file: tldr-backbone-of-a-beast-charting-nvidias-rise-to-netwo
fetched_at: '2026-11-01T18:53:08.458141'
original_url: https://www.theregister.com/networks/2026/10/31/backbone-of-a-beast-charting-nvidias-rise-to-networking-titan/5306499
date: '2026-11-01'
published_date: '2026-10-31T08:03:00.000Z'
description: How a $6.9B bet on Mellanox made Nvidia bigger than Cisco, and the world's most valuable company to boot
tags:
- tldr
---

networks

 

# Backbone of a beast – charting Nvidia's rise to networking titan

How a $6.9B bet on Mellanox made Nvidia bigger than Cisco, and the world's most valuable company to boot

Tobias Mann

Tobias

Mann

SYSTEMS EDITOR

Published

sat 31 Oct 2026 // 08:03 UTC

Make us preferred on Google

### READ MORE

* #### Google's AI satellite sends a very expensive haiku to Earth14 hours ago
* #### Amazon sends chills through its workforce with mixed message memo about AI use19 hours ago
* #### Domestic droid gone amok? Don't worry, you're covered1 day ago
* #### Google's search revenue Ferrari hits an AI-powered speed bump1 day ago
* #### AWS installs an AI accelerator every 14 seconds and eyes $1 trillion annual revenue2 days ago

Nvidia is more than just a leader in graphics and AI hardware. It has also become a titan of the networking industry with bigger datacenter Ethernet sales than any other vendor.

In Q2, Nvidia's networking revenuestopped$17.5 billion. To put that in perspective, Cisco's revenue during that same period, across all products, was $17.3 billion.

GPUzilla's arrival as a networking power feels sudden, yet Jensen Huang started working towards this status in 2019 with the $6.9 billionacquisitionof long-time networking partner Mellanox .

REG AD

At the time, Mellanox wasn't a big name in Ethernet switching. The company was mostly known for its ConnectX NICs and InfiniBand switches. Outside of high-performance computing (HPC) and supercomputing clusters, and a big deployment at Microsoft, InfiniBand wasn't widely deployed in hyperscale datacenters.

REG AD

Buying Mellanox allowed Nvidia to reposition itself as a system builder, which means something different in the context of distributed compute. Nvidia understood its datacenter customers weren't interested in buying GPUs or even servers; they wanted clusters of systems. For that, Nvidia needed interconnect and Mellanox's InfiniBand fit the bill.

### Relentless co-design

Over the years, Huang has talked about co-design – designing components and software to work together for specific set of jobs rather than to be the best GPU, switch, or NIC. Its work with Mellanox is a prime example of that approach.

According to Dell'Oro Group analyst Sameh Boujelbene, Nvidia's decision to integrate compute and networking became key to the company's success.

"Customers choose Nvidia for its tightly integrated compute and networking architecture, optimized for AI workloads," she toldThe Register. That integration makes deployments easier and speeds time to market.

Ben Mabey, CTO of pioneering AI and machine learning company Recursion, toldThe RegNvidia's integration schemes won him over.

Founded in 2013, nearly a decade before ChatGPT made AI the subject of dinner-table discussion, Recursion sought to apply machine learning running atop GPUs to the problem of drug discovery.

This work involved churning through massive datasets which, Mabey tells us, now total more than 50 petabytes in size.

REG AD

"When you think about our workloads, it makes LLMs workload training seem easy compared to the amount of data that has to be moved around," he toldThe Register.

"In the biological space and sciences in general, it's not well appreciated just how big the data actually is," he added. "The internet's big, but in the grand scheme of things, the text that people are training on is actually pretty small, versus the petabytes of data that we have of these images."

Recursion's first cluster was a system called BioHive Zero which it cobbled together from GTX 1080 graphics cards originally intended for gaming systems. It used Ethernet to connect GPUs and ran into the limits of conventional networking.

So, for its second cluster, an A100-based machine with around 300 accelerators, Recursion went with Nvidia's Quantum InfiniBand switches and ConnectX NICs.

As Mabey explains it, buying its compute and interconnects from the same vendor vastly simplified optimization and troubleshooting. When Recursion reached out to Nvidia for help tuning the system, they were able to consider it as a single system, rather than discrete compute and networking resources. This level of integration had only previously been offered by boutique supercomputer builders like Cray or Atos (Eviden/Bull/whatever it gets renamed next).

### A wider Spectrum

Nvidia hasn't always listed networking revenue as a single line item in its financials. However, based on CFO commentary and a little back of the napkin math we can fill in the blanks.

Nvidia's networking revenues have exploded since the acquisition of Mellanox in 2019 positioned the company to compete as a system builder rather than GPU maker.

Tobias Mann

 

Nvidia's networking revenues have grown steadily since the Mellanox acquisition. At two moments, its revenue shot up suddenly.

REG AD

The first came in the 2023 calendar year (FY24) after OpenAI kicked off the AI gold rush with the launch of ChatGPT.

The second spread across 2024 and 2025, when Nvidia started selling Blackwell-generation GPUs and then started to ship them in large quantities.

"I see two major inflection points, both coinciding with the Blackwell platform ramp: the introduction of NVLink switches and the accelerating adoption of Spectrum-X Ethernet switches for AI back-end networks, driven by growing deployments of Nvidia GPU clusters and increased attach rates of Nvidia switches, NICs, optics, and cables," Boujelbene said.

It was around this time that users started deploy to Ethernet switches in large volume across Nvidia clusters. Elon Musk's Colossus supercomputer was one of the earliest examples.

As wereportedat the time, the first half of the 200,000-chip H100 and H200-based cluster came online in 2024 and, at the time, was among the largest ever clusters deployed using Nvidia's Spectrum-X Ethernet switches.

Meta has also made extensive use of Nvidia's Spectrum switches in its own training clusters, including at its million-GPU Prometheus site in New Albany, Ohio.

There are a couple reasons Nvidia's Spectrum-X offering is doing so well.

First, through a combination of Spectrum Ethernet switches, superNICs, and some clever software optimizations, Nvidia was able to replicate many of the qualities that made InfiniBand so attractive while also benefiting from significantly higher radix and interoperability.

Ethernet switches, including Nvidia's own, have historically offered more ports. The higher the radix, the fewer switches are necessary to support a cluster at a given port speed.

This often gets misconstrued to mean that InfiniBand can't scale beyond clusters of a certain size, which isn't necessarily the case. But for clusters exceeding a certain number of GPUs, Ethernet is often more economical because it requires less equipment while achieving similar utilization.

That said, Nvidia's Spectrum-X isn't exactly unique. Broadcom, Cisco, AMD and others have managed toachieveutilization similar to InfiniBand through various investments in smartNICs and switches.

Nvidia's main differentiator, as Mabey and Boujelbene noted earlier, is the level of integration between the compute and networking.

### The next frontier

Then Blackwell hit the market, enabling much greater scale and creating a surge in Nvidia's networking revenue.

Prior to Blackwell, Nvidia's NVLink and NVSwitch interconnect tech had largely been limited to single systems with up to eight GPUs. With the launch of the GB200 NVL72, these NVSwitches were broken out into dedicated appliances. (And yes, we remember GH200 NVL256 and NVL32, but from what we can tell these were never shipped in any meaningful volume, if at all.)

For everyNVL72 racksystem sold, Nvidia also sold nine NVSwitch trays, which enabled the system's six dozen GPUs to function as a single enormous GPU. This effectively guaranteed steady networking revenue growth: even if customers didn't buy Nvidia's scale-out switches, if they wanted NVL72 racks, they were automatically buying NVSwitch.

"We estimate that NVSwitch now accounts for roughly one-third of Nvidia’s networking revenue, up from virtually zero less than two years ago," Boujelbene toldEl Reg. "This underscores how quickly NVLink switching has become a major growth engine for Nvidia’s networking business."

Nvidia is now moving to grow its networking business even further with a new licensing program.

Until recently, Nvidia's NVSwitch tech was limited to its own accelerators. However, with the introduction of NVLink Fusion early last year, Nvidia opened the interconnect tech up tothird parties to license.

Many chip designers, including Marvell, Qualcomm, Arm, Fujitsu, MediaTek, and d-Matrix, have announced plans to develop CPUs and XPUs using NVLink Fusion. The adoption of the interconnect opens the door to additional NVSwitch sales, as the chips using NVLink Fusion still rely on them for chip-to-chip communications, and there's no other place to get them, as Nvidia has yet to license out NVSwitch.

"NVLink Fusion allows Nvidia to extend its networking footprint beyond its own GPUs into the rapidly growing custom accelerator market. I see it as a strategic move to capture a larger share of AI networking spending, even in clusters that do not use Nvidia GPUs," Boujelbene said.

Nvidia's networking ambitions don't stop there.

"Nvidia continues to pursue opportunities in emerging networking domains as network requirements evolve to keep pace with increasingly demanding AI workloads," Boujelbene added. "The latest example is scale-in networking, designed to address the new requirements of agentic AI, while innovations such as CPO will help overcome growing bandwidth, power, and scalability challenges." ®

switching

ethernet

datacenter

ai

networks

nvidia

Make us preferred on Google

REG AD

## Google's AI satellite sends a very expensive haiku to Earth

Experimental orbital datacenter prototype puts its TPU to work producing poetry

## Goth aesthetic gone wild: a user's self-inflicted black screen of non-death in Windows 3.1’s

Labeled in black on black - controls for a galactic hyper-hearse or ill-advised Windows theme?

## Built to bend: Postgres’s inventor and a steward on what AI really needs

PARTNER CONTENT: Michael Stonebraker and Bruce Momjian on why enterprise AI needs a database that no one controls, and what PostgreSQL 19 says about the road ahead

## Amazon sends chills through its workforce with mixed message memo about AI use

A lot of software engineers feel bleak about the future of the profession

## PHP2Shell is a warning shot for vulnerability disclosure

Keeping secrets is difficult in an open world, but we've done it before and must do it again

BORK!BORK!BORK!

## Chocolate Caterpillar or Chocolate Teapot? Top up the disk space for Windows 10 to find out

London's Oxford Street signage shows its underwear to passing tourists

### TOP STORIES

* #### Anthropic now lets Claude users jump out of plane without parachute
* #### Google struggling to make AI Mode searches pay
* #### Alibaba's Qwen AI caught trying to contact server in China
* #### Microsoft offers parachutes to 60k employees if they jump by the end of the year
* #### Tesco replacing VMware with Proxmox in its stores and on the edge
* #### Man spends 35 years collecting corporatespeak, turns it into an app

### AI

* #### Amazon sends chills through its workforce with mixed message memo about AI useA lot of software engineers feel bleak about the future of the profession
* #### Backbone of a beast – charting Nvidia's rise to networking titanHow a $6.9B bet on Mellanox made Nvidia bigger than Cisco, and the world's most valuable company to boot
* #### Domestic droid gone amok? Don't worry, you're coveredInsurance firms look to insulate domestic humanoid robot owners against the inevitable chaos they will bring
* #### Google's search revenue Ferrari hits an AI-powered speed bumpJust wait 'til we add more AI and this thing'll really fly
* #### AWS installs an AI accelerator every 14 seconds and eyes $1 trillion annual revenueBefore long, we could be writing about a cloud company with a retail side hustle

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### AlpineBSD announced – an AI-free FOSS OSCombining the NetBSD kernel with the Alpine Linux userland
* #### Ubuntu 27.04 may bring a preview of the long-awaited Core DesktopCanonical has a long way to catch up, but it knows who it's chasing
* #### Systemd adds support for RustWhat's even better than Rust in the Linux kernel? Rust in systemd!
* #### FreeBSD founder ports Omarchy to FreeBSD in ten days, ten releasesDaemonarchy is unaffiliated with the Linux original, built with AI help, and could complicate FreeBSD's debate over AI contributions
* #### SparkyOS: Lightweight general-purpose Arch, on a pendriveInteresting new project from the minds behind SparkyLinux
* #### Red Hat helps teach about tech writingBut learns tough lessons about AI in the process