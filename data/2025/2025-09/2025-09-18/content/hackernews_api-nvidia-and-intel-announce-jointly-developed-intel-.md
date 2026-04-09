---
title: Nvidia and Intel announce jointly developed 'Intel x86 RTX SOCs' for PCs with Nvidia graphics, also custom Nvidia data center x86 processors — Nvidia buys $5 billion in Intel stock in seismic deal | Tom's Hardware
url: https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal
site_name: hackernews_api
fetched_at: '2025-09-18T19:05:59.836958'
original_url: https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal
author: stycznik
date: '2025-09-18'
published_date: '2025-09-18T11:00:11Z'
description: Nvidia and Intel announced today that the companies would jointly develop multiple new generations of products together. The products include x86 Intel CPUs tightly fused with an Nvidia RTX graphics chiplet for the consumer gaming PC market, and custom-built Intel x86 CPUs for Nvidia’s AI products for hyperscale and enterprise customers.
tags:
- hackernews
- trending
---

(Image credit: Nvidia)

In a surprise announcement that finds two long-time rivals working together, Nvidia and Intel announced today that the companies will jointly develop multiple new generations of x86 products together — a seismic shift with profound implications for the entire world of technology. Before the news broke, Tom's Hardware spoke with Nvidia representatives to learn more details about the company’s plans.

The products include x86 Intel CPUs tightly fused with an Nvidia RTX graphics chiplet for the consumer gaming PC market, named the ‘Intel x86 RTX SOCs.’ Nvidia will also have Intel build custom x86 data center CPUs for its AI products for hyperscale and enterprise customers. Additionally, Nvidia will buy $5 billion in Intel common stock at $23.28 per share, representing a roughly 5% ownership stake in Intel. (Intel stock is now up 33% in premarket trading.)

The partnership between the two companies is in the very early stages, Nvidia told us, so the timeline for product releases along with any product specifications will be disclosed at a later, unspecified date. (Given the traditionally long lead-times for new processors, it is rational to expect these products will take at least a year, and likely longer, to come to market.)

Nvidia emphasized that the companies are committed to multi-generation roadmaps for the co-developed products, which represents a strong investment in the x86 ecosystem. But representatives tells us it also remains fully committed to other announced product roadmaps and architectures, including the company's Arm-basedGB10 Grace Blackwell processors for workstationsand theNvidia GraceCPUs for data centers, as well as the next-genVera CPUs. Nvidia says it also remains committed to products on its internal roadmaps that haven’t been publicly disclosed yet, indicating that the new roadmap with Intel will merely be additive to existing initiatives.

The chip giant hasn’t disclosed whether it will use Intel Foundry to produce any of these products yet. However, while Intel has used TSMC to manufacture some recent products, its goal is to bring production of most high-performance products back into its own foundries.

Some products never left. For instance, Intel’s existingGranite Rapidsdata center processors use the ‘Intel 3’ node, and the upcomingClearwater Forest Xeonswill use Intel’s own 18A process node for compute. This suggests that at least some of the Nvidia-custom x86 silicon, particularly for the data center,could be fabbed on Intel nodes. Intel also uses TSMC to fabricate many of its client x86 processors, however, so we won’t know for sure until official announcements are made — particularly for the RTX GPU chiplet.

In either case, Nvidia has beenmulling using Intel Foundry since 2022, hasfabbed test chipsthere, and participates in the U.S. Defense Dept.'sRAMP-C projectwith Intel. The DoD project involves Nvidia alreadymaking chips on Intel's 18A process node, so it wouldn't be a total surprise.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

While the two companies have engaged in heated competition in some market segments, Intel and Nvidia have partnered for decades, ensuring interoperability between their hardware and software for products spanning both the client and data center markets. And the PCIe interface has long been used to connect Intel CPUs and Nvidia GPUs. The new partnership will find tighter integration using theNVLink interface for CPU-to-GPU communication, which affords up to 14 times more bandwidth along with lower latency than PCIe, thus granting the new x86 products access to the highest performance possible when paired with GPUs. Let’s dive into the details we’ve learned so far.

## Intel x86 RTX SOCs for the PC gaming market

For the PC market, the Intel x86 RTX SoC chips will come with an x86 CPU chiplet tightly connected with an Nvidia RTX GPU chiplet via the NVLink interface. This type of processor will have both CPU and GPU units merged into one compact chip package that externally looks much like a standard CPU, rivaling AMD’s competing APU products.

This type of tight integration packs all the gaming prowess into one package without an external discrete GPU, providing power and footprint advantages. As such, these chips will be heavily focused on thin-and-light gaming laptops and small form-factor PCs, much like today’s APUs from AMD. However, it’s possible the new Nvidia/Intel chips could come in multiple flavors and permeate further into the Intel stack over time.

Intel has worked on a similar type of chip before with AMD; there is at least one significant technical difference between these initiatives, however. Intel launched itsKaby Lake-G chip in 2017with an Intel processor fused into the same package as an AMD Radeon GPU chiplet, much the same as the description of the new Nvidia/Intel chips. You can see an image of the Intel/AMD chip below.

Image
1
 of
5
An RTX GPU chiplet connected to an Intel CPU chiplet via the fast and efficient NVLink interface.

This SoC had a CPU at one end connected via a PCIe connection to the separate AMD GPU chiplet, which is flanked by a small, dedicated memory package. This separate memory package was only usable by the GPU. The Nvidia/Intel products will have an RTX GPU chiplet connected to the CPU chiplet via the faster and more efficient NVLink interface, and we’re told it will have uniform memory access (UMA), meaning both the CPU and GPU will be able to access the same pool of memory.

Intel notoriouslyaxed the Kaby Lake-G products in 2019, and the existing systems wereleft without proper driver supportforquite some time, in part because Intel was responsible for validating the drivers, and then finger-pointing ensued. We’re told that both Intel and Nvidia will be responsible for their respective drivers for the new models, with Nvidia naturally providing its own GPU drivers. However, Intel will build and sell the consumer processors.

We haven’t spoken with Intel yet, but the limited scope of this project means that Intel’s proprietary Xe graphics architecture will most assuredly live on as the primary integrated GPU (iGPU) for its mass-market products.

Intel's new x86 RTX CPUs will compete directly with AMD's APUs. For AMD, that means it faces intensifying competition from a company with the leading market share in notebook CPUs (Intel ships ~79% of laptop chips worldwide) that's now armed with GPU tech from Nvidia, whichships 92% of the world's gaming GPUs.

## Nvidia's first x86 data center CPUs

Intel will fabricate custom x86 data center CPUs for Nvidia, which Nvidia will then sell as its own products to enterprise and data center customers. However, the entirety and extent of the modification are currently unknown. We do know that Nvidia will employ its NVLink interface, which tells us the chips could leverage Nvidia’s newNVLink Fusiontech that enables custom CPUs and accelerators to enable faster, more efficient communication with Nvidia’s GPUs than found with the PCIe interface.



(Image credit: Nvidia)

Intel has long offered custom Xeons to its customers, primarily hyperscalers, often with relatively minor tweaks to clock rates, cache capacities, and other specifications. In fact, these mostly slightly-modified custom Xeon models once comprised more than 50% of Intel’s Xeon shipments. Intel has endured several years of market share erosion due to AMD’s advances, most acutely in the hyperscale market. Therefore, it is unclear if the 50% number still holds true, as hyperscalers were the primary customers for custom models.

Intel haslong said that it will design completely custom x86 chips for customersas part of its IDM 2.0 strategy. However, aside from a recent announcement ofcustom AWS chipsthat sound like the slightly modified Xeons mentioned above, we haven’t heard of any large-scale uptake for significantly modified custom x86 processors. Intelannounced a new custom chip design unit just two weeks ago, so it will be interesting to learn the extent of the customization for Nvidia’s x86 data center CPUs.

Nvidia already uses Intel’s Xeons in several of its systems, like the Nvidia DGX B300, but these systems still use the PCIe interface to communicate with the CPU. Intel’s new collaboration with Nvidia will obviously open up new opportunities, given the tighter integration with NVLink and all the advantages it brings with it.

The likelihood of AMD adopting NVLink Fusion is somewhere around zero, as the company is heavily invested in its ownInfinity Fabric (XGMI)andUltra Accelerator Link (UALink)initiatives, which aim to provide an open-standard interconnect to rival NVLink and democratize rack-scale interconnect technologies. Intel is also a member of UALink, which uses AMD’s Infinity Fabric protocol as the foundation.

## Dollar and Cents, Geopolitics

Nvidia’s $5 billion purchase of Intel common stock will come at $23.28 a share, roughly 6% below the current market value, but several aspects of this investment remain unclear. Nvidia hasn’t stated whether it will have a seat on the board (which is unlikely) or how it will vote on matters requiring shareholder approval. It is also unclear if Intel will issue new stock (primary issuance) for Nvidia to purchase, as it did when the U.S. government recently became an Intel shareholder (that is likely). Naturally, the investment is subject to approval from regulators.

Nvidia’s buy-in comes on the heels of theU.S government buying $10 billion of newly-created Intel stock, granting the country a 9.9% ownership stake at $20.47 per share. The U.S. government won’t have a seat on the board and agreed to vote with Intel’s board on matters requiring shareholder approval “with limited exceptions.”Softbank has also recently purchased $2 billion worth of primary issuance Intel stockat $23 per share.

Swipe to scroll horizontally
Purchases of Intel Stock
Row 0 - Cell 0

Total

Share Price

Stake in Intel

Nvidia

$5 Billion

$23.28

~5%

U.S. Government

$9 Billion

$20.47

~9.9%

Softbank

$2 Billion

$23

Row 3 - Cell 3

The U.S. government says it invested in Intel with the goal of bolstering US technology, manufacturing, and national security, and the investments from the private sector also help solidify the struggling Intel. Altogether, these investments represent a significant cash influx for Intel as it attempts to maintain the heavy cap-ex investments required to compete with TSMC, all while struggling with a negative amount of free cash flow.

“AI is powering a new industrial revolution and reinventing every layer of the computing stack — from silicon to systems to software. At the heart of this reinvention is Nvidia’s CUDA architecture,” said Nvidia CEO Jensen Huang. “This historic collaboration tightly couples NVIDIA’s AI and accelerated computing stack with Intel’s CPUs and the vast x86 ecosystem—a fusion of two world-class platforms. Together, we will expand our ecosystems and lay the foundation for the next era of computing.”

“Intel’s x86 architecture has been foundational to modern computing for decades – and we are innovating across our portfolio to enable the workloads of the future,” said Intel CEO Lip-Bu Tan. “Intel’s leading data center and client computing platforms, combined with our process technology, manufacturing and advanced packaging capabilities, will complement Nvidia's AI and accelerated computing leadership to enable new breakthroughs for the industry. We appreciate the confidence Jensen and the Nvidia team have placed in us with their investment and look forward to the work ahead as we innovate for customers and grow our business.”

We’ll learn more details of the new partnership later today when Nvidia CEO Jensen Huang and Intel CEO Lip-Bu Tan hold awebcast press conference at 10 am PT.

This is breaking news…more to come.

FollowTom's Hardware on Google News, oradd us as a preferred source, to get our up-to-date news, analysis, and reviews in your feeds. Make sure to click the Follow button!

See more CPUs News

TOPICS

Paul Alcorn
Editor-in-Chief

Paul Alcorn is the Editor-in-Chief for Tom's Hardware US. He also writes news and reviews on CPUs, storage, and enterprise hardware.
