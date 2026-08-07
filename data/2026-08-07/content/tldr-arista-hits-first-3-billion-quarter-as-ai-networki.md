---
title: Arista hits first $3 billion quarter as AI networking momentum continues | Network World
url: https://www.networkworld.com/article/4205721/arista-hits-first-3b-quarter-as-ai-networking-demand-continues-and-supply-pressures-show-signs-of-improvement.html
site_name: tldr
content_file: tldr-arista-hits-first-3-billion-quarter-as-ai-networki
fetched_at: '2026-08-07T11:44:08.877507'
original_url: https://www.networkworld.com/article/4205721/arista-hits-first-3b-quarter-as-ai-networking-demand-continues-and-supply-pressures-show-signs-of-improvement.html
date: '2026-08-07'
description: Arista sees networking as the central nervous system for infrastructure, from the client to campus to AI data centers.
tags:
- tldr
---

by									
Michael Cooney

Senior Editor

# Arista hits first $3B quarter as AI networking demand continues and supply pressures show signs of improvement

News

Aug 5, 2026
7 mins

Arista Networks shared some good news about its earnings and future directions during its second-quarterearnings callthis week.

For starters, Arista reported its first-ever $3 billion quarter. The company logged revenue of $3.036 billion, an increase of 12.1% compared to the first quarter of 2026, and an increase of 37.7% from the second quarter of 2025. Just five years ago, Arista reported $2.9 billion in revenue for the entire 2021 year, noted CEO Jayshree Ullal.

“Customers seenetworkingas the central nervous system for infrastructure from the client to campus to data and AI centers,” Ullal said. “Our AI fabrics momentum with Etherlink switches now exceeds 100 cumulative customers from the initial four to five customers I spoke of in 2024.”

Ullal said the company is seeing growth in all sectors—from back-end AI fabrics to the core data-center front end, to adjacent campus and routing businesses. The scale-across switching and routing market is forecast to hit between $15 billion and $20 billion by 2030, for example, positioning Arista well for growth, Ullal said.

“We are now projecting 40% annual growth, which is an incremental $2.1 billion over our 2025 Analyst Day goal of $10.5 billion, and an incremental $1.1 billion over our recent projections of $11.5 billion in May of 2026,” Ullal said.

So what exactly is working? Arista highlighted a number of areas.

## Supply chain pressures beginning to ease

Just last quarter, Arista said supply-chain pressures on networking components—memory, chips, and wafers—were leading toongoing shortagesandrising costs.

With a lot of work, some of that pressure has eased, reportedTodd Nightingale, president and COO of Arista. “Arista has spent the last six months improving our supply chain to meet growing product demand, and we’re seeing significant improvements,” Nightingale said. “We’ve secured multiyear agreements with leading vendors of strategic components, qualified new suppliers in key areas to limit risk and built out supply chains for next gen AI technologies.”

“Relationships with our strategic silicon vendors continue to be strong, with really excellent collaboration in both supply chain and technical engagements,” Nightingale said. “Our memory supply has been secured for 2026, and we have extended visibility well into 2027 across DDR4, DDR5 and NAND memory. And importantly, we’ve increased our resiliency through optionality and expanded vendor qualification. For PCBs and optics, we’re now able to build capacity in a 12-month window and have strengthened our engagement and commitments from key suppliers. We’ve improved our lead times and inventory management of thousands of component SKUs, improving sub-component pipelining and multi-sourcing, and providing increased flexibility with reduced inventory risk,” Nightingale said.

Nightingale noted, too, that Arista has established a liquid-cooling supply chain “capable of driving and delivering the next generation of AI infrastructure. This includes cold plate, quick disconnect, and tubing vendors with capacity agreements for cutting-edge new AI technology.”

“By focusing on vendor stability and diversity, risk mitigation, and predictable delivery terms, innovation for new AI products, and capacity across our factories, we are making significant improvements and significant capacity increases across our supply chain,” Nightingale said.

Ullal kept things in perspective, however: “I don’t want you to believe that suddenly we waved a magic wand and all our problems have gone away,” she said. “The industry is going to have a two-year problem [with memory and other silicon availability challenges], and I don’t think we get out of it as an industry until 2028. But Arista is taking individually and specifically steps in the first half of this year that we believe will have results in the back half of this year.”

## EOS innovations

“I have never witnessed the combination of rapid innovation and scale deployment that we are seeing in AI networks,” saidKenneth Duda, president and CTO of Arista. He highlighted three technologies, all of which are part of the vendor’s EOS operating system, that are helping to drive and differentiate Arista gear: Smart System Upgrade (SSU), Multipath Reliable Connection (MRC), and Segment Routing (SRV6).

“SSU is the ability to upgrade switch software without any disruption. Frequent upgrades are a hard reality today, especially as AI both uncovers security vulnerabilities and creates tools to exploit them,” Duda said. “While many competing systems require a full reboot to address these issues, leading to expensive and disruptive downtime, Arista EOS handles these upgrades seamlessly.”

In order to maximize xPU utilization, customers need MRC, because in first-generation AI networks, every packet on an XPU-to-XPU flow has to take the same path. “That means if two flows hash to the same length, they both run at half speed. MRC enables senders to spray a single flow across many paths through the fabric, where receivers reassemble any data that arrives out of order, eliminating the performance hit from fabric cache collisions,” Duda said.

But how is the sender supposed to control which paths deploy or use? That’s where SRV6 comes in. “It’s not new, but using it toload balance an AIfabric, that’s the game changer,” Duda said. “The sender tags each packet with a stack of SRV6 segment IDs dictating the exact path the packet will take. The system then uses real-time congestion signaling to dynamically shift packets away from hotspots.”

“Because Arista EOS provides a single unified operating system, we support this SRv6 intelligence all the way from the scale-out fabric to the long-distance scale-across routing,” Duda said. “It gives our customers the combination of high-quality top performance and operational simplicity that Arista is known for.”

## The optics

Optical connection technology continues to move into the AI networking environment, and Ullal said Arista believes the majority of the market will continue using pluggable optics and copper through 2028-2029. “I think there’s very much a philosophy there [of] copper if you can, optics if you must,” Ullal said.

“I think you’re going to see a lot of copper in that two-meter, three-meter distance, well within a rack, that type of thing, and the importance of pluggable optics. But in some cases, there is a number of instances of proprietary implementations of traditional co-packaged optics (CPO) that’s been floating around,” Ullal said. “Arista is not a fan of five different proprietary implementations.”

Arista’s development team has been working to solve one aspect, which is an open CPO. “We don’t think open CPO is going to happen overnight, but the idea here is to use socketed optical engines, pigtail fibers, and allow these modules to be fully pretested. And whether they’re soldered on the board or nearby, the idea is to have a truly open interface that can operate with multiple vendors and multiple switch configurations,” Ullal said.

“Arista supports open, socketed optical engines rather than multiple proprietary solutions. And CPO/Near Packaged Optics (NPO) are expected to enter trials in 2027 but will remain a small portion near term,” Ullal said.

Arista recently unveiledextended pluggable optics (XPO), a form factor designed specifically for optics at high speed and assembled over 100 optics module suppliers as part of amulti-source agreementto build and support XPO.

Artificial Intelligence
Networking
Network Switches
Networking Devices
Enterprise Routers
 

 

														by 															

																Michael Cooney															

Senior Editor

1. Follow Michael Cooney on X
2. Follow Michael Cooney on LinkedIn

Michael is a senior editor with Network World focused on deciphering the strategies of many core high-tech vendors such as Cisco, Arista, Juniper, HPE and IBM. Michael has been writing about the industry for more than 33 years and has won coverage awards from ASBPE and FOLIO. He has a BA in Journalism and Technical Writing Certificate from The Pennsylvania State University.He can be reached atmichael_cooney@foundryco.com.

## More from this author

* news### Nvidia moves to accelerate storage access, boost industry cooperationAug 4, 20264 mins
* news### Dell, Nutanix combo expands virtualization, private cloud choicesJul 29, 20263 mins
* news### IBM: AI-driven attacks increased 56% last year, and data breach costs are up 12%Jul 29, 20265 mins
* news### Fortinet’s new FortiGate platform converges firewall, SASE technologiesJul 28, 20262 mins
* news### Cisco, AMD bring enterprise-level security, visibility to Ryzen AI Halo systemsJul 24, 20264 mins
* news### IBM keen on mainframe even after 42% revenue drop in Q2Jul 23, 20265 mins
* news### Arista debuts unified SD-WAN edge platformJul 21, 20265 mins
* news### IBM targets AI edge with Power server, software upgradesJul 15, 20265 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

news
 
 

### AMD to buy Taalas, maker of model-specific AI chips for enterprise inference

 
By Anirban Ghoshal
Aug 7, 2026
4 mins

Artificial Intelligence
CPUs and Processors
Data Center Design

news
 
 

### Agentic AI could force a rethink of enterprise AI server design, researchers say

 
By Gyana Swain
Aug 7, 2026
4 mins

Data Center
Servers

news
 
 

### Black Hat: NatJack exploits test NAT security assumptions

 
By Sean Michael Kerner
Aug 6, 2026
7 mins

Network Security
Networking
Security

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