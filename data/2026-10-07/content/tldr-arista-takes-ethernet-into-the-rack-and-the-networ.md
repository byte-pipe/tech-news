---
title: Arista takes Ethernet into the rack, and the network becomes the backplane - SiliconANGLE
url: https://siliconangle.com/2026/10/07/arista-takes-ethernet-rack-network-becomes-backplane
site_name: tldr
content_file: tldr-arista-takes-ethernet-into-the-rack-and-the-networ
fetched_at: '2026-10-07T23:28:46.958267'
original_url: https://siliconangle.com/2026/10/07/arista-takes-ethernet-rack-network-becomes-backplane
author: Zeus Kerravala
date: '2026-10-07'
published_date: '2026-10-07T20:02:05+00:00'
description: Arista takes Ethernet into the rack, and the network becomes the backplane - SiliconANGLE
tags:
- tldr
---

UPDATED 16:02 EDT / OCTOBER 07 2026

 
INFRA

### Arista takes Ethernet into the rack, and the network becomes the backplane

GUEST COLUMNbyZeus Kerravala

Since its founding in 2004, it’s arguable that no network vendor has made better switches thanArista Networks Inc. That was true then and remains true, as its prowess in this area helped it ride the cloud boom and the artificial intelligence wave.

That model is changing as AI scales. Today, ahead of next week’sOpen Compute ProjectGlobal Summit in San Jose, Arista announced an expansion of its AI network strategy from switches to rack scale.

Arista is launching an open Ethernet rack-scale portfolio covering both scale-up and scale-out AI fabrics, built with a large ecosystem of players such as Advanced Micro Devices Inc., Arm Ltd., Broadcom Inc., d-Matrix Corp., Meta Platforms Inc., Microsoft Corp. and Qualcomm Corp. The lead announcement isEtherlink SU-144, an Ethernet-based scale-up architecture that connects up to 144 accelerators, or XPUs, within a single-hop domain and up to 1,024 XPUs across racks. It is built on the Ethernet for Scale-Up Networking or ESUN initiative.

In the AI era, the network can no longer be thought of as an independent pipe moving data between servers. It has become a tightly integrated, rack-scale backplane, and how well it’s built determines how much value customers get from their compute. That’s a significant shift for a company whose identity has been built on the network as a distinct layer. But the network isn’t disappearing into the compute. Instead, the compute is being built around the network.

### What Arista announced

The scale-up piece comes in three physical form factors, each designed for different use cases. During an analyst briefing, Vijay Vusirikala, Arista’s distinguished lead for AI systems and networks, walked through each one.

* Orthogonal chassis.Servers sit in front, and full-height switch cards in the back connect directly, with no backplane or cabling, drawing on Arista’s modular chassis heritage. It supports 100 to 400 kilowatts of liquid cooling. This is the design for vendors focused on training workloads that need the largest possible scale-up domain.
* Cabled backplane.Switches sit in the middle of the rack and connect to servers via copper cable cartridges. It is less dense but more serviceable, and it lets operators split bandwidth between intra-rack and inter-rack connections.
* Cross-rack.A dedicated switch rack connects separate accelerator racks. It is the most flexible design and the fastest to market because it avoids long co-engineering cycles, but it adds interconnect cost and power. “Copper runs out of juice very quickly,” Vusirikala said, so anything beyond two racks needs optics.

On the scale-out side, Arista offers liquid-cooled rack reference designs in eight-, 12- and 16-switch configurations, built around its 7060EX7 switches. Each delivers 102.4 terabits per second, plus fiber patch panels, cooling manifolds, drip trays with active leak detection, rack management controllers and power shelves with battery backup. Integration partners build, test and deliver the configured racks. The fabric supports Ultra Ethernet Consortium specifications, Multipath Reliable Connection resiliency, multi-plane routing and dynamic and cluster load balancing.

Customers can run Arista EOS or an open network operating system on the common Netdi foundation. Arista also said next-generation optics, including its XPO pluggables and open co-packaged and near-packaged optics, will increase rack capacity from 1.6 petabits per second to 6.5 petabits, cutting the data center footprint by nearly half.

### Andy Bechtolsheim to present at OCP

The OCP Global Summit runs Oct. 12-15 in San Jose, and Arista will have a fully assembled liquid-cooled rack at its booth. This departs from the traditional engineering story at an Arista booth, focusing less on switching and more on manifolds, leak handling, fiber management and power. According toArista’s OCP event page, co-founder and industry visionary Andy Bechtolsheim will present at 1 p.m. Oct. 13 on “The Gigawatt AI Data Center Era.”

### Why this matters for Arista

Three takeaways emerged from the Arista announcement. First, Arista is targeting the one part of the AI network it hasn’t owned. It leads in scale-out and is pushing into scale-across, but scale-up has mirrored Nvidia’s NVLink market share. Arista was matter-of-fact that this won’t change for Nvidia-based systems anytime soon. “There is no near-term opportunity because that is proprietary,” Vusirikala told me.

The opportunity lies in non-Nvidia accelerators, and a partner list including AMD, Microsoft’s Maia, Qualcomm and d-Matrix shows that market is real. Arista is betting that heterogeneous compute will become the norm. This is wise for Arista, as there is plenty of opportunity for every vendor without trying to disrupt Nvidia’s seemingly undisruptable business.

Second, Arista is making the case for a single network stack across all three fabrics. These have historically been separate networks. Arista wants the same EOS, telemetry and diagnostics, regardless of whether the silicon underneath is shallow-buffer, deep-buffer, or low-latency. That’s a network-centric view rather than a compute-attached one, and it’s Arista’s strongest argument because fault isolation and predictive maintenance now extend into the most performance-sensitive part of the cluster.

Third, this is a reference architecture strategy, not a SKU launch, and it changes how infrastructure is delivered. Arista supplies the switches, software, designs and validation suites, while partners handle rack integration.

During the briefing, Arista Senior Product Line Manager Arihant Jain explained the importance of this. A 16-switch rack configuration can involve 2,000 fibers, and on-site cabling invites bend-radius violations, miswiring, signal-integrity problems, and dead optics. “The whole old approach of spare parts or things assembled at site has to change,” he said. Racks need to be integrated and tested upstream, then rolled into place. Liquid cooling forces the issue because switches, manifolds, and leak responses must be designed together.

Do you shut down a switch or a rack when a leak is detected, and does that decision tie into the building management system? These used to be facilities questions. They are now network questions.

The caution is that Nvidia’s turnkey stack remains Arista’s biggest obstacle and, in some ways, detracts from its Ethernet prowess. When customers buy a complete system, Ethernet doesn’t always come up. Open designs win on choice and economics, but they demand coordination among accelerator vendors, rack integrators and cooling suppliers.

Execution across that ecosystem will determine how quickly these land. Early buyers will be hyperscalers, neoclouds and AI infrastructure providers. Most enterprises will use these architectures through those providers rather than deploy them directly, at least for now.

### Advice for network engineers

* Learn liquid cooling now.Arista expects roughly a 50-50 split between air- and liquid-cooled deployments for its current 100-terabit switches next year. Vusirikala said liquid cooling becomes effectively mandatory at 200 terabits per second. Removing fans alone cuts switch power by about 10%. Engineers who understand manifolds, leak detection and thermal design will be in demand.
* Think in racks, not boxes.Acceptance testing, sparing and troubleshooting shift when the rack is the product. Request rack-level validation data.
* Get fluent in scale-up.Scale-up was the server team’s problem. As Ethernet moves into that domain, it becomes the network team’s problem. Study ESUN, UEC, and features such as link-level retry and credit-based flow control.
* Keep optics options open.Arista said its customers are roughly split between next-generation pluggables and open CPO. Decide based on serviceability, power and your operational model.
* Protect operational consistency.One operating model across scale-up, scale-out and scale-across is worth more than a marginal performance gain.
* Question your AI providers.If you consume AI capacity from a neocloud or cloud provider, ask how its scale-up domains are built and how quickly failed racks are isolated. That affects the accelerator time you pay for.

The InfiniBand-versus-Ethernet debate in scale-out is largely settled. Arista is betting that the same economics hold one layer down, inside the rack. The competition is no longer about port speeds. It’s about who can roll in a validated rack and put expensive accelerators to work fastest. As accelerators diversify, the network that ties everything together becomes the platform, and that is precisely where Arista wants to be.

Zeus Kerravala is a principal analyst at ZK Research, a division of Kerravala Consulting. He wrote this article for SiliconANGLE.

##### Photo: Arista

# A message from John Furrier, co-founder of SiliconANGLE:

Support our mission to keep content open and free by engaging with theCUBE community.Join theCUBE’s Alumni Trust Network, where technology leaders connect, share intelligence and create opportunities.

* 15M+ viewers of theCUBE videos, powering conversations across AI, cloud, cybersecurity and more
* 11.4k+ theCUBE alumni— Connect with more than 11,400 tech and business leaders shaping the future through a unique trusted-based network

### Are you an AWS customer?Support SiliconANGLE financially by buying your AWS services from ourMarketplace portal page and links:https://siliconangle.com/aws-marketplace/

 

##### About SiliconANGLE Media

SiliconANGLE Media is a recognized leader in digital media innovation, uniting breakthrough technology, strategic insights and real-time audience engagement. As the parent company of 
SiliconANGLE
, 
theCUBE Network
, 
theCUBE Research
, 
CUBE365
, 
theCUBE AI
 and theCUBE SuperStudios — with flagship locations in Silicon Valley and the New York Stock Exchange — SiliconANGLE Media operates at the intersection of media, technology and AI.

Founded by tech visionaries John Furrier and Dave Vellante, SiliconANGLE Media has built a dynamic ecosystem of industry-leading digital media brands that reach 15+ million elite tech professionals. Our new proprietary theCUBE AI Video Cloud is breaking ground in audience interaction, leveraging theCUBEai.com neural network to help technology companies make data-driven decisions and stay at the forefront of industry conversations.

##### LATEST STORIES

* US government, tech giants and Biohub commit $1.8B to AI biology initiative
* Anthropic releases Claude Haiku 5.5 small model and halves Sonnet 5.5 cache read prices
* OpenAI publishes 722 AI-generated math discoveries in major scientific milestone
* Cisco broadens agentic features in Webex collaboration platform
* Aston Martin puts back-end AI to work while keeping agents off its website
* Midwest Wheel builds toward AI agents that fix problems

##### LATEST STORIES

* US government, tech giants and Biohub commit $1.8B to AI biology initiativeEMERGING TECH- BYMARIA DEUTSCHER.27 MINUTES AGO
* Anthropic releases Claude Haiku 5.5 small model and halves Sonnet 5.5 cache read pricesAI- BYDUNCAN RILEY.46 MINUTES AGO
* OpenAI publishes 722 AI-generated math discoveries in major scientific milestoneAI- BYMARIA DEUTSCHER.3 HOURS AGO
* Cisco broadens agentic features in Webex collaboration platformAI- BYPAUL GILLIN.3 HOURS AGO
* Aston Martin puts back-end AI to work while keeping agents off its websiteAI- BYJONATHAN ANTHONY.3 HOURS AGO
* Midwest Wheel builds toward AI agents that fix problemsAI- BYSLOANE KALI FAYE.3 HOURS AGO