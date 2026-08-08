---
title: A requiem for Optane, Intel's KV cache killer that could have eased the RAM price crunch
url: https://www.theregister.com/storage/2026/07/29/a-requiem-for-optane-intels-kv-cache-killer-that-could-have-eased-the-ram-price-crunch/5280063
site_name: tldr
content_file: tldr-a-requiem-for-optane-intels-kv-cache-killer-that-c
fetched_at: '2026-08-08T19:27:44.412197'
original_url: https://www.theregister.com/storage/2026/07/29/a-requiem-for-optane-intels-kv-cache-killer-that-could-have-eased-the-ram-price-crunch/5280063
date: '2026-08-08'
published_date: '2026-07-28T23:27:59.000Z'
description: With microscopic latencies and otherworldly write endurance, it was perfect for today's AI workloads – but gone before they arrived
tags:
- tldr
---

Storage

 

# A requiem for Optane, Intel's KV cache killer that could have eased the RAM price crunch

With microscopic latencies and otherworldly write endurance, it was perfect for today's AI workloads – but gone before they arrived

Tobias Mann

Tobias

Mann

SYSTEMS EDITOR

Published

wed 29 Jul 2026 // 00:27 UTC

History is littered with the corpses of technologies that were ahead of their time, and Intel’s Optane storage and memory products are certainly among them.

Expensive, badly misunderstood, and awkwardly priced, the technology struggled to find a place in the market, surviving just five years before Chipzilla pulled the plug.

Things might have been different if it were launched today. The shift from AI training to inference has driven tremendous demand for DRAM and NAND flash. In fact, the same properties that made Optane a niche product a few years ago would have made it ideally suited to these write intensive AI workloads.

REG AD

### The rise and fall of Optane

REG AD

Intel and Micron co-developed Optane – or more specifically, 3D XPoint memory – and unveiled it in 2015. It promised to bridge the gap between conventional NAND flash used in SSDs and DRAM used in DDR4 and (later) DDR5.

Like NAND, 3D XPoint was non-volatile, which means data persists when unpowered, making it appropriate for storage applications.

But unlike NAND, 3D XPoint didn’t store data using trapped electrons and instead relied on a phase change material that was both extremely fast, achieving sub-10-microsecond latencies (even lower for later PMem modules), and absurdly write-endurant.

Intel’spenultimateOptane SSDs boasted endurance of 100 drive writes a day and a mean time between failures of two million hours — specs that remain unrivaled today.

Those figures are of course extrapolated, based on what we know about how 3D XPoint reads and writes data. But if anything, we suspect Intel was probably being conservative with its claims.

This one-two punch of endurance and latency, particularly for random reads and writes meant that it could be used as a second tier of system memory. Optane SSDs are really, really low latency for storage-class memory, but they’re still orders of magnitude less responsive than DRAM which can hit 100 nanoseconds or lower. We should note Intel’s PMem DIMMs were capable of latencies of roughly350 nanoseconds.

Intel’s Optane persistent memory also had the benefit of capacities up to 512 GB per DIMM, at a time when the most you could expect out of DDR4 was about 128 GB – and only if you had deep pockets.

These persistent memory DIMMs could be made to behave like main memory, with standard DDR4 functioning as a massive L4 cache when enabled; as a storage pool; or in an application-aware memory mode, which exposed the Optane memory directly to select applications.

REG AD

Despite Optane’s many strengths, it was rather awkwardly priced. For the same memory density, 3D XPoint was consistently more expensive than NAND and, while cheaper than DRAM, significantly less performant.

As a result, there was rarely a scenario in which users were better off with Optane than they would be just buying more NAND or fewer, bigger DIMMs.

## MORE CONTEXT

* ### AI is storage’s biggest opportunity - and biggest threat
* ### IBM insists AI didn't kill software deals, just delayed them
* ### Unexpected Windows bloat is due to bug, not by design
* ### Micron locks in historically high memory prices for five years

To make matters worse, as the boffins at TechInsightsnotedat the time, while 3D XPoint had its merits, it wasn’t improving quickly enough to keep up with NAND flash on bit density.

By 2021, Micron had had enough. The memory vendor announced it would end development of 3D XPoint products. With no source of new silicon for its SSD and persistent memory products, the writing was on the wall for Optane.

Intel's then-CEO Pat Gelsinger officiallypulled the plugin 2022, ending development of new products under the Optane banner. The P5810X and P5811X, the final Optane products to roll off the assembly line, launched in late 2022.

### Ahead of its time

The same year Intel pulled the plug on Optane, a new workload was emerging that would completely turn the datacenter on its head, and might very well have been the killer app to justify 3D XPoint’s continued development.

In November 2022, OpenAI, then a relatively obscure AI startup, lifted the curtain on ChatGPT, kicking off an AI arms race and sparking a massive influx of money into the tech sector.

REG AD

Large language models are among the most resource-intensive workloads in the world. But until 2025, most of that compute was dedicated to training bigger, smarter, and less hallucination-prone models.

The arrival of DeepSeek early in that year signaled the shift toward inference, a workload that needs plenty of compute, memory, and storage.

Modern inference engines are tuned to maximize efficiency. One way is by caching the key value pairs used to track model state.

Chatbots and agents are inherently iterative. For multi-turn sessions, every prompt contains not only new information, but also every request and response that came before it. Recomputing all of that every time a new request is made is wasteful, so instead that information is computed, cached, and reused.

The problem is at large context sizes and high concurrency, these KV caches can get rather large. A single 64,000-token sequence in a model like DeepSeek R1 can chew up four gigabytes of GPU memory. Multiply that across hundreds or thousands of users and it adds up quickly.

Modern GPUs don’t have much memory, and what they do have is usually tied up hosting model weights. Many inference engines therefore support KV cache offloading, either natively or through plugins. Once GPU memory is exhausted or chat sessions stale, older chats are ejected to system memory.

But DRAM is expensive, in short supply, and may not even be enough. In fact, Nvidia isreportedlycutting the amount of LPDDR5X shipped as part of its Vera Rubin platform.

Because of this, KV caches where, for example, a user has walked away and the session has been idle for an hour or more, may be offloaded to flash storage arrays for longer-term storage.

The problem is that KV caching is a write-intensive workload and NAND has a finite number of writes it can make before it’s shot. There's a lot of work being done to mitigate this, but the fact remains that if you write enough data to NVMe storage, eventually it wears out.

Optane’s otherworldly write endurance and low latency, particularly when concerning small random writes which dominate KV-caching, would have made it a perfect choice for this workload.

### Optane’s successors

One of the nails in Optane’s coffin was thatCompute Express Link(CXL) was already on the horizon. If the primary reason for adopting Optane was to get your hands on a large pool of reasonably fast DRAM-like memory, then CXL offered all the benefits and none of the compromises. In effect, early CXL implementations were essentially a remote memory controller to which you could attach your choice of memory, DDR4 or DDR .

Need more memory than your CPU supports? Just plug a CXL memory expander into a free PCIe slot and you were off to the races. Later revisions of the memory coherent protocol added support for pooling, and later sharing.

However, CXL hasn’t changed the fact that DDR5 is expensive at the best of times, and we are currently living in the worst of times for DRAM prices. (With that said, while your CPU may only support DDR5, the CXL controller might still be able to use DDR4. This is exactly what Meta is doing toboost the memory capacityof its systems on the cheap.)

In the absence of Optane, memory vendors have attempted to fill the void with write-optimized NAND of their own.

Kioxia’sXL-Flashis one such example of storage class memory (SCM) that promises many of the same benefits as Optane, including advertised write latencies under 10 microseconds, and endurance up to 60 drive writes a day, through the use of SLC (1-bit per cell) memory.

There’s also a crossover with CXL here. XL-Flash can be exposed as a CXL device to simplify memory tiering.

Samsung also attempted to replicate many of Optane's qualities with itsZ-NAND tech, but the tech still falls well short of 3D XPoint. Samsung is reportedly revamping the tech and aiming for a 15x performance increase over conventional NAND.

Alas, neither quite lives up to Optane’s legacy. The tech was simply too far ahead of its time. Had Intel and Micron waited just a few years longer, it might have ridden the AI wave all the way to victory. ®

ai

intel

optane

cxl

state of storage 2026

storage

REG AD

AI and ML

## Devs to Anthropic, OpenAI, Cursor, and friends: Make security and privacy the default

Researchers scour social media to measure developer concerns about AI coding tools

science

## South Korean satellite spots SpaceX lunar impact

Before and after shots of Elon's ejecta snapped by Danuri

devops

## Platform Engineering 2.0: your platform was built for a different era. AI just exposed it

PARTNER CONTENT: Platform engineering won the argument. Now it has to grow up fast and evolve for the AI era.

AI and ML

## OpenAI pledges to add Astra security as Anthropic loosens Fable's leash

Or how I learned to stop worrying and love dangerous AI

COLUMNISTS

## Adding an API to networking hardware doesn’t solve management challenges

This is why cloud-inspired networks win: virtual switches are all consistent

Security

## Water system controllers don't belong on the internet, says ex-NSA chief after suspected Iran attacks

Calling all defenders

### MOST POPULAR

* SECURITY#### IT department put sticky notes on the laptops to help employees log in
* AI and ML#### AMD acquires AI chip startup Taalas to boost inference performance by etching models into silicon
* Security#### London cops handed victim's new address and number to her stalker, watchdog says
* saas#### Double trouble for Microsoft as pre-owned software license claims converge
* AI AND ML#### Microsoft tells engineers to curb their token-burning enthusiasm

### AI

* AI and ML#### OpenAI pledges to add Astra security as Anthropic loosens Fable's leashOr how I learned to stop worrying and love dangerous AI
* AI and ML#### AI titans to tidy agent frontier with plugin prescriptionAgent Plugins 1.0 defines a write-once-run-anywhere container for passing tools and skills across different agent platforms
* AI and ML#### How the famed USENIX Security conf is managing a flood of papers in the AI eraAI usage is evident but isn't yet a serious problem
* AI and ML#### AMD acquires AI chip startup Taalas to boost inference performance by etching models into siliconEarly tech demos show model-specific integrated circuits churning out up to 17,000 tokens a second
* AI and ML#### AI struggles to patch vulns without adult supervisionLeft alone, autonomous fixes often fail to fully remediate flaws

### Infosec

* Security#### Russians are posing as Signal support to launch phishing attacksPLUS: US takes down Iranian propaganda sites; Marketing company asks 'Why Do We Have Your Information?' And more!
* Security#### Microsoft patches failed to fix on-prem SharePoint, which is now under zero-day attackPLUS: China upgrades smartphone surveillance tools; Ring eases anti-snooping stance; and more
* Black Hat and DEF CON#### DEF CON Franklin project enlists hackers to harden critical infrastructureVoting village reports have been so successful, says Jeff Moss, that the whole of DEF CON will now be included
* Security#### EQT buys majority share in Swiss cybersecurity biz AcronisWent at equivalent of $3.5B+ valuation for entire firm, though portion sold not specified
* Malware Month#### Ten years since the first corp ransomware, Mikko Hyppönen sees no end in sightOn the plus side, infosec's a good bet for a long, stable career

### FOSS

* #### FOSS smashed one Microsoft monopoly. After 20 years of failure, it's time to smash anotherWord up
* #### GNOME can look like Windows – and Flashback can do it without extensionsNew 'Simple-taskbar' is an option, but there's a simpler, stabler way
* #### A moment of silence, please, for the final release of Debian on x86-32New Debian versions hit FOSSland in the form of 13.6 and 12.15
* #### Baddies caught exploiting extensions bugs with perfect 10 scores on vulnerable Joomla websitesFlaws in iCagenda, Balbooa Forms extensions can impact open source CMS that powers a million sites worldwide
* #### Frame: A new X11 server – implemented directly in assemblyJoins yserver, Phoenix, and of course XLibre – and outlier Arcan
* #### Cinnamon 6.8 will support Wayland – if you want itNext version of Linux Mint’s desktop has both kinds of display server