---
title: GPUHammer
url: https://gpuhammer.com/
site_name: hackernews
fetched_at: '2025-07-17T07:05:05.076038'
original_url: https://gpuhammer.com/
author: jonbaer
date: '2025-07-17'
---

## GPUHammer: Rowhammer Attacks on GPU Memories are Practical#

Chris (Shaopeng) Lin†, Joyce Qu†, Gururaj Saileshwar,from University of Toronto

Published atUSENIX Security 2025(link topaper). Artifact available onGitHubandZenodo.†equal contribution

## TL;DR#

GPUHammeris the first attack to showRowhammer bit flips on GPU memories, specifically on aGDDR6 memory in an NVIDIA A6000 GPU. Our attacksinduce bit flips across all tested DRAM banks, despite in-DRAM defenses like TRR, using user-level CUDA code. These bit flips allow a malicious GPU user totamper with another user’s data on the GPUin shared, time-sliced environments. In a proof-of-concept, we use these bit flips to tamper with a victim’s DNN models anddegrade model accuracy from 80% to 0.1%, using a single bit flip. Enabling Error Correction Codes (ECC) can mitigate this risk, but ECC can introduce up to a 10% slowdown for ML inference workloads on an A6000 GPU.

## 🔍 What’s New in Rowhammer for GPUs?#

Rowhammeris a hardware vulnerability where rapidly activating a memory row introduces bit flips in adjacent memory rows.
Since 2014, this vulnerability has been widely studied in CPUs and in CPU-based memories like DDR3, DDR4, and LPDDR4.
However, with critical AI and ML workloads now running on discrete GPUs in the cloud, it is vital to assess the vulnerability of GPU memories to Rowhammer attacks.

Rowhammer is uniquely more challenging on GPU-based GDDR memories for the following reasons:

* ⏱️ GDDR6 has higher latency and faster refresh than CPU-based DDR4, making hammering harder.
* 🧩 Unknown DRAM address mappings in GDDR memories complicate crafting effective patterns.
* 🛡️ In-DRAM mitigations in GDDR are opaque and undocumented.

Despite this, GPUHammer overcomes these barriers and launches successful attacks on GDDR6.

### Step 1: Reverse Engineering GPU DRAM Mappings#

To craft effective Rowhammer attacks, we first need to identify memory addresses that map to the same DRAM bank on an NVIDIA GPU. Unlike CPUs, NVIDIA GPUs do not expose the physical addresses to user-level CUDA code, making it challenging to identify and hammer DRAM rows in the same bank. However, observing that the NVIDIA GPU driver consistently maps virtual memory to the same physical memory, we reverse engineer the virtual memory offsets to DRAM bank mappings. Inspired by theDRAMAtechnique, we use timing differences between memory accesses to the same bank vs. different banks.

One key obstacle, as shown inFig. 1, is theNon-Uniform Memory Access (NUMA)effect in memory access latencies for addresses accessed in pairs, which makes it hard to pinpoint same-bank addresses. Based on the insight that addresses in the same DRAM bank must have similar latency when accessed in isolation, we filter out such addresses contributing to the NUMA effects and clearly identify addresses mapping to the same DRAM bank (seeFig. 2). This accurately identifies same-bank address pairs needed for crafting Rowhammer patterns.

Fig. 1:Naively accessing pairs of addresses: different-bank latencies (320-370ns) overlap with same-bank latencies (370-380ns) due to NUMA effects.

Fig 2:After filtering addresses with different latencies when accessed in isolation, same and different bank address pairs are distinguishable.

### Step-2: Maximizing Hammering Intensity#

GPU memory accesses are up to4× slowerslower than CPUs, making it hard to reach the activation rate needed for Rowhammer attacks using naive,single-threadedhammering like in CPUs (Fig. 3, green line). To overcome this, we exploit the GPU’sSIMT parallelism, launching multiple threads and warps in parallel. Thismulti-threaded, multi-warp approach(Fig. 3, orange line) eliminates idle time in the memory controller and reaches the maximum possible hammering rate.Fig. 4shows how these strategies maximize memory controller utilization.

Fig. 3:Number of activations in a single refresh period (tREFW) for single-thread, multi-thread, and multi-warp hammering.

Fig. 4:Memory controller utilization with (a) single-thread,
(b) multi-thread, and (c) multi-warp hammering. Multi-warp
hammering minimizes idle time, maximizing activation rates.

### Step-3: Synchronizing to Refreshes, Defeating Mitigations#

Prior works likeSMASHandBlackSmithshow that synchronizing hammering to refreshes (REF) is key to bypassing in-DRAM defenses.
However, CUDA’s synchronization primitives (like__syncthreads()) used to synchronize threads can reorder warp execution. Instead, we use implicit per-warp delays, aligned such that REF commands overlap with our inserted delays, to align our hammering with refreshes and defeat in-DRAM mitigations like TRR while preserving warp execution order.

Fig. 5:Per-warp delays inserted usingaddsfor synchronizing
to REF. When the delays overlap, the REF
is inserted in alignment with the hammering pattern.

## 💥 What Did We Break?#

We ran GPUHammer on anNVIDIA RTX A6000 (48 GB GDDR6)across four DRAM banks and observed8 distinct single-bit flips, and bit-flipsacross all tested banks(see Fig. 6). Theminimum activation count ( TRH)to induce a flip was ~12K, consistent with prior DDR4 findings.

Using these flips, we performed thefirst ML accuracy degradation attack using Rowhammer on a GPU.Prior workshows thatflipping the most significant bit of a floating-point exponentin FP16 model weights can drastically reduce model accuracy. Based on this insight, we show that in a time-shared GPU setup, an attacker can position victim data into vulnerable DRAM rows via memory massaging and force the bit flips at such locations.

In our proof-of-concept (Fig. 7), with justa single bit flip, the accuracy of an ML model isdegraded below 1%for all five tested ImageNet DNN models, resulting in up to80% accuracy loss.

Fig. 6:Number of bit-flips in 4 banks on RTX A6000 with GDDR6. We observed bit-flips on each bank.

Fig. 7:Accuracy degradation attack on ImageNet models on NVIDIA A6000 GPU. We report the top-1 / top-5 accuracy without (Base Acc) and with (Degraded Acc) the bit-flip, and the Relative Accuracy Drop (RAD) for the top-1 accuracy.

## ❓ FAQs#

#### What GPUs are vulnerable? Am I affected?#

We confirmed Rowhammer bit flips onNVIDIA A6000 GPUs with GDDR6memory. Other GDDR6 GPUs, such as theRTX 3080, did not show bit flips in our tests, possibly due to variations in DRAM vendor, chip characteristics, or operating conditions like temperature. We also observedno flips on an A100GPU with HBM memory.

#### Why test so few GPUs? Isn’t that a small sample size?#

Unlike CPUs, where DRAM modules can be easily swapped out for testing,GPU DRAM is soldered in, making large-scale testing expensive (GPUs can cost thousands of dollars). Our attack code isextensible to other Ampere GPUs and beyond, and we encourage future work to expand the test coverage.

#### How can GPUHammer be mitigated?#

Admins can mitigate GPUHammer byenabling ECCvianvidia-smi -e 1(followed by a reboot). All observed bit flips so far aresingle-bit, which ECC can correct. However, enabling ECC mayreduce performance by up to 10%andmemory capacity by 6.25%on the A6000. Still, this doesn’t eliminate the root cause, a hardware flaw, which would require redesigning GDDR6 with principled mitigations likePRAC, which has been proposed for DDR5 and beyond, or probabilistic mitigations likePRIDE.

#### Are newer GPUs like the H100 or RTX 5090 affected?#

Currently,no. H100 (HBM3) and RTX 5090 (GDDR7) featureon-die ECC, which likely masks single-bit flips. However, future Rowhammer patterns causing multi-bit flips may bypass such ECC, as shown in attacks likeECCploit.

#### Did you disclose this to NVIDIA? What was their response?#

Yes. Weresponsibly disclosedGPUHammer to NVIDIA onJanuary 15, 2025, and also to major cloud service providers (AWS, Azure, GCP, etc.). NVIDIA confirmed the issue and recommended enabling ECC as a mitigation.

## Further Information#

Please refer to ourpaper, which appears atUSENIX Security 2025. The artifacts are available onGitHubandZenodo.

To cite our paper, please use:

@inproceedings
{
lin2025gpuhammer
,


author

=

{Chris S. Lin and Joyce Qu and Gururaj Saileshwar}
,


title

=

{GPUHammer: Rowhammer Attacks on GPU Memories are Practical}
,


publisher

=

{USENIX Association}
,


booktitle

=

{Proceedings of the 34th USENIX Conference on Security Symposium}
,


year

=

{2025}
,


series

=

{SEC '25}
,


address

=

{USA}
,


location

=

{Seattle, WA, USA}
,

}

### Acknowledgements#

This research was supported by Natural Sciences and Engineering Research Council of Canada (NSERC) under funding reference number RGPIN-2023-04796, and an NSERC-CSE Research Communities Grant under funding reference number ALLRP-588144-23.
Any research, opinions, or positions expressed in this work are solely those of the authors and do not represent the official views of NSERC, the Communications Security Establishment Canada, or the Government of Canada.

 ↑
