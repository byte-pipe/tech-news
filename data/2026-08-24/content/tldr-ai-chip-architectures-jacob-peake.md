---
title: AI Chip Architectures - Jacob Peake
url: https://www.jepeake.com/ai-chip-architectures
site_name: tldr
content_file: tldr-ai-chip-architectures-jacob-peake
fetched_at: '2026-08-24T19:27:17.823476'
original_url: https://www.jepeake.com/ai-chip-architectures
date: '2026-08-24'
description: A look at AI Chip Architectures. NVIDIA, AMD, TPUs, Trainium, Groq, Cerebras.
tags:
- tldr
---

At the 2018International Symposium on Computer Architecture,John HennessyandDavid Pattersondelivered theirTuringLecture:"A New Golden Age for Computer Architecture".

In the 1980s, whenHennessyandPattersondid their Turing Award-winning research,single-threaded CPU performance grew 52% a year. By 2018, with the end ofMoore's LawandDennard Scaling, the rate was 3%.

There was a need fordomain-specific architectures(DSAs). Their worked example was Google'sTPU v1, already in production: 29× the throughput of a CPU on neural-network inference, at 80× better energy efficiency. The closing prediction:"the next decade will see a Cambrian explosion of novel computer architectures."

This prediction came true. Today, we now have dozens of architectures in serious development.GPUs,TPUs,LPUs,NPUs,DPUs,ASICs,wafer-scale engines,reconfigurable dataflow,neuromorphic,photonic,analog. Particularly, these architectures focus on compute forAI.

The architectures that have won real deployment so far:GPUs(NVIDIA, AMD),systolic-array accelerators(TPU, Trainium), theCerebras Wafer-Scale Engine, and theGroq LPU.

NVIDIAis the clear frontrunner;AMDfollows, with 6 GW commitments from bothOpenAIandMeta.TPUstrain Gemini and willserve Anthropic with up to a million chips; Anthropic also runs Claude onover a millionTrainiumchips.Cerebrasnow serves OpenAI inference; theGroq LPUwasfolded into NVIDIA via a $20B acquihire.

This post aims to survey these varying approaches - theirphilosophy,architecture,scaling methods (scale-up and scale-out), andsoftware stack (how you program the chip).

### The Problem

AI compute is dominated bymatrix multiplication. A transformer is a sequence of matmuls:Q/K/V projection,attention,output projection,FFN- interleaved with element-wise ops: normalisation, activation, residual adds.Traininga frontier model performs102510^{25}1025multiply-accumulate operations (matmuls are a sequence of multiply-accumulates).

Theshapeof those matmuls depends on the workload.Trainingpushes a batch of sequences forward through every layer, backpropagates the loss, and updates the weights, with thousands of tokens flowing through the same weight matrix at once.Prefillis the prompt-ingestion phase of inference: the full input sequence projected through the model in a single pass, before the first output token has been produced. Both training & prefill stack many tokens against the same weight matrix, so each layer's math is a largematrix-matrixmultiply (GEMM), with higharithmetic intensity(compute-bound).Decodeis autoregressive: the model emits one token at a time, each conditioned on every token before it, and tokenN+1cannot begin until tokenNhas been produced. Only one token gets projected per step, so every matmul becomes amatrix-vectorproduct (GEMV). Producing one token requires a full pass over every weight in the model, plus a full read of theKV Cachefor attention. Arithmetic intensity drops by orders of magnitude versusprefill.

Inference systems recover some of that intensity by batching tokens to promote those GEMVs back to GEMMs:continuous batchingstacks many users'decodesteps,speculative decodingstacks K drafted tokens per request and verifies them in one pass, andmulti-token predictionfolds the same trick inside the model itself. This achieves higher utilisation of the matmul units, and pushes up the Ops/B. For continuous batching, each user's request still reads its ownKV Cache, so long-context decode shifts from weight-bandwidth-bound to KV-bandwidth-bound.

The architecture problem here ismoving the numbersto where the matmuls happens fast enough. This is known as thememory wall: compute has scaled exponentially, memory bandwidth has not.

Each architecture proposes a different strategy for winning the data-movement game. Understanding a chip reduces to four questions:where does datalive, how does itmoveto the compute units, what do thecompute unitslook like, and how do chips talk to each other atscale.

### NVIDIA GPU

The NVIDIA GPU is amassively parallel processor. The philosophy is that a programmable chip with thousands of threads, orchestrated by a host CPU and exposed throughCUDA, is the right machine to runparallelisableworkloads. Each generation adds acceleration primitives onto programmableStreaming Multiprocessorswithout changing the programming model. The same chip trains transformers, serves inference, renders graphics, and runs scientific simulation (accelerated computing).

#### Genealogy

2006
Tesla
G80
The first CUDA-capable GPU; 
unified shaders
 and the 
SIMT execution model
.

2010
Fermi
GF100
First true compute architecture: unified L1/L2 caches, dual 
warp schedulers
, IEEE-754 
FP64
.

2012
Kepler
K20
, 
K40
SMX
, 
dynamic parallelism
, 
Hyper-Q
; the GPU can launch its own work.

2014
Maxwell
M40
Redesigned SM with ~2× perf-per-watt over Kepler.

2016
Pascal
P100
NVLink
 1.0, 
HBM2
, native 
FP16
 throughput; the first GPU designed explicitly for deep learning.

2017
Volta
V100
First 
Tensor Cores
; 
independent thread scheduling
.

2018
Turing
T4
2nd-gen 
Tensor Cores
 with 
INT8
/
INT4
; first 
RT Cores
.

2020
Ampere
A100
3rd-gen 
Tensor Cores
 with 
TF32
 and 
structured sparsity
; 
Multi-Instance GPU
 partitioning.

2022
Hopper
H100
, 
H200
, 
GH200
4th-gen 
Tensor Cores
, 
FP8
, 
Transformer Engine
; 
HBM3
, 
TMA
, thread block clusters, async 
wgmma
.

2024
Blackwell
B100
, 
B200
, 
GB200
5th-gen 
Tensor Cores
 with 
FP4
, 
Tensor Memory (TMEM)
, 
two-die chiplet GPU
, 
NVLink 5
.

2025
Blackwell Ultra
B300
, 
GB300
Mid-cycle refresh: ~1.5× 
FP4
 throughput, 288 GB 
HBM3e
. Tuned for long-context reasoning.

2026
Rubin
Rubin
, 
VR200
, 
Rubin CPX
HBM4
, 3rd-gen 
Transformer Engine
, 
Vera CPU
 pairing, disaggregated 
prefill
 via 
Rubin CPX
.

2027
Rubin Ultra
Rubin Ultra
4-die GPU package, 1 TB 
HBM4
e per package. Deployed in 600 kW NVL576 Kyber racks at 100 PetaFLOPS 
FP4
 per GPU.

#### Architecture

An NVIDIA GPU is a group ofthroughput-oriented cores, a deep memory hierarchy to keep them fed, + just enough scheduling silicon to keep thousands of threads in flight. The cores areStreaming Multiprocessors, replicated 100+ times per package: 80 onV100, 108 onA100, 132 onH100, 148 onB200, 160 onB300, 224 onRubin. Inside every SM sits the same recipe: fourSM Sub-Partitions, each with its ownwarp scheduler,dispatch unit, 16k×32-bitregister file, scalarCUDA Corelanes, aSpecial Function Unitfor transcendentals, and a private port into the SM'sTensor Cores. The four partitions share anL1/shared-memoryblock, and theTMA. Threads are grouped intowarpsof 32 that execute inSIMTlock-step; dozens of resident warps per partition let the scheduler hide memory/arithmetic stalls by switching between them.

##### Compute

CUDA Coresare the original compute throughput, and for AI they still own everything that isn't a matmul: activations, residual adds, normalization, address arithmetic. But, a transformer block is ~99% matmul FLOPs, so the overwhelming compute throughput comes from theTensor Cores.

These cores executefused matrix multiply-accumulateon small matrix tiles,D=A⋅B+CD = A \cdot B + CD=A⋅B+CThe full matmul is broken into output tiles: to produce one output tile, a kernel walks the shared inner dimensionKKK, drawingAAAfrom a row-strip of the left input matrix andBBBfrom a column-strip of the right, and folds each partial product into a running accumulator.CCCholds the partial sum so far,DDDis the updated value carried into the next step. After the inner loop completes,DDDis one finished tile of the full output matrix; the whole matmul is built from many of these tileMMAs.

Tile shapes are writtenM × N × K,M×NM \times NM×Nis the output tile size, andKKKis how much of the inner dimension the instruction contracts over in one fire; the rest of the matmul'sKKKaxis is walked by the kernel's inner loop. The accumulator is sticky across that loop: each MMA's outputDDDbecomes the next MMA's inputCCC, so the equation is reallyC←A⋅B+CC \leftarrow A \cdot B + CC←A⋅B+Cin place: successive instructions fold their partial products into the same storage until the K-axis is fully walked.

V100's first-gen unit (8 per SM) ran a warp-level 16×16×16 FP16MMA.A100's 3rd-gen unit addedTF32,BF16, FP64 matmul, and 2:4structured sparsity.H100's 4th-gen unit added nativeFP8and pulled the abstraction up from a warp to awarp group: 128 cooperating threads firing an asynchronouswgmmaat 64×256×16 shape that runs in the background while the issuing warps load the next tile.B200's 5th-gen unit went further still: atwo-SM MMAof 256×256×16 with operands split across a pair of SMs, nativeFP4, and a dedicated 256 KBTensor Memory (TMEM)scratchpad per SM that holds accumulator tiles instead of bleeding into the register file.Rubin's 6th-gen unit extends FP4 throughput, adds native FP6, and pairs with a 3rd-genTransformer Enginethat does adaptiveNVFP4micro-block scaling in hardware, keeping the per-tile quantization metadata on theTensor Corepath, rather than through theCUDA Cores.

What stays constant across all six generations is that the matmul lives inside thethread/warp hierarchy, but the number of threads it takes toissueone has shrunk, and the issue itself has decoupled from execution.Volta'smma.syncis warp-collectiveand synchronous: all 32 threads in awarpexecute it together, each lane holding register fragments of A, B,and the accumulator D, and the warp blocks until it completes.Hopper'swgmma.mma_asyncwidens the issuer to awarp-groupof 128 threads, moves B into ashared-memory descriptor(A becomes optional: either registersora descriptor, kernel's choice), andreturns immediately: the matmul runs in the background while the warp-group queues the next tile, with completion tracked viawgmma.commit_group/wgmma.wait_group.

Blackwell'stcgen05.mmacompletes the migration:A joins Binshared-memory descriptors(or A comes fromTMEMdirectly), and the accumulatorD lands in TMEMrather than the register file. With every operand off the lanes, there is no per-thread state for an issue to coordinate, so asingle threadfires the instruction andreturns immediately, with completion signalled by anmbarrierthe consumer warp waits on. The rest of the warp, and the issuing thread itself, is free for other work in the meantime. ACTA-pair variantscales the same model across two SMs: one thread on each SM in a paired cluster issues coordinatedMMAsthat share operands across the pair, composing the256×256×16 two-SM tileunder the same async/mbarriercompletion, just promoted to a cluster-level barrier so the pair stays in step.

The matmul has grown bigger and lighter on the issuing threads at the same time: an instruction that started as 32 lanes acting in lockstep is now closer to a singledescriptor-driven command, dispatched from inside the warp model but no longer executed by it.

That decoupling is what makes transformer attention kernels efficient on a GPU. The warp can run softmax, apply a mask, or pre-load the next tile while the matmul is in flight; the overlap of matmul and the surrounding element-wise work is the structure of every modern attention kernel (FlashAttention-3, FA4), and it depends on the matrix instruction not blocking the warp.

##### Memory

The on-chip hierarchy ishardware-managed caches at every level, with software hints layered on top. Off-chip isHBM: 32 GBHBM2on V100, 80 GBHBM3on H100, 192 GBHBM3eon B200, 288 GB on B300, 288 GBHBM4on Rubin. A chip-levelL2 Cachesits between HBM and the SMs: 6 MB on V100, 40 MB on A100, 50 MB on H100, 60 MB on B200 (split into two 30 MB banks across thetwo-die package, with locality-awareresidency controlsso that hot tiles can be pinned to the near die). Inside each SM, 256 KB of unifiedL1/SMEMis partitioned at kernel launch between hardware-managed L1 and a programmer-controlled scratchpad. The register file is another ~256 KB per SM, sliced four ways across the partitions.

Blackwell adds a fifth tier:TMEM, 256 KB per SM dedicated toMMAaccumulators and addressed only by the Tensor Core, pulling the operand-residency pressure out of the general register file.

Movement between tiers has been progressively decoupled from the warp. Pre-Ampere, loading a tile was synchronous: each thread issued its own global load, the warp blocked until every fragment landed in registers, and a second pass copied them to shared memory; every tile burned warp lanes on address arithmetic and on the wait.Ampereintroducedcp.async: per-thread async copies HBM → SMEM that bypass registers entirely, with the warp committing groups of in-flight copies and waiting only when the consumer needs the data.Hopperreplaced that with theTMA, a dedicated DMA engine: one thread submits a multi-dimensional tile descriptor (base address, leading dimension, swizzle), the engine handles all the address arithmetic and writes into shared memory, and completion is signalled by anmbarrier. The whole warp is freed from load issue and address math; the kernel just queues descriptors. TMA also supportscluster-level multicast: one HBM read fans out to every SM in athread-block cluster, turning what used to be N separate loads into one.Blackwellextends TMA again: direct loads intoTMEM, so accumulator tiles stream in without staging through SMEM. The trajectory is one less thing the warp has to do per tile, generation after generation.

##### Warp Specialisation

The Hopper-era programming idiom iswarp specialisation: inside one block, some warps act asproducersthat issue back-to-backTMAloads; others act asconsumersthat firewgmmaon freshly-arrived tiles. Synchronisation between them is no longer the old SM-wide__syncthreads()barrier; it ismbarrier(memory barriers in shared memory) and asynchronous transaction barriers attached to TMA completions, allowing fine-grained producer/consumer handshakes at warp granularity rather than block granularity. The pattern that has become the reference for every modern attention kernel (FlashAttention-3,CUTLASSping-pong GEMMs, the BlackwellFA4kernel) is the same recipe: a TMA-driven producer pipeline feeds a wgmma consumer pipeline through shared memory and TMEM, with mbarrier handshakes andthread-block clusters(Hopper+) tying multiple SMs into one cooperative compute unit so that the two-SM MMA of Blackwell composes naturally on top.

##### Numerics

FP32was the historical default; Volta broughtFP16with FP32 accumulate and theloss-scalingtricks that made it trainable; Ampere addedTF32(FP32 range, FP16 mantissa, drop-in for FP32 matmul),BF16, and 2:4structured sparsitythat doubles effective throughput on pruned weights. Hopper introduced nativeFP8in bothE4M3andE5M2, paired with theTransformer Enginewhich auto-scales activations layer-by-layer to keep them inside FP8 dynamic range. Blackwell halved precision again withFP4and shippedmicroscaling MX formats(block-level shared exponents that recover most of the accuracy lost at FP4), together with a 2nd-gen Transformer Engine that retargets the auto-scaling pipeline to FP4. Rubin's 3rd-gen Transformer Engine addsNVFP4(NVIDIA's tightened FP4 variant) and nativeFP6with more aggressive sparsity. The chip layout itself is now part of the numerics story: B100/B200/B300 aretwo reticle-limit diesstitched by a ~10 TB/sNV-HBIlink and presented to software as one logical GPU, with 8 HBM stacks on the package; Rubin extends the chiplet recipe to dual-die at ~336 B transistors with 8 HBM4 stacks. Every generation buys roughly 2× per-watt throughput by cutting bits in half and restoring accuracy with a finer-grained scaling scheme, and increasingly, by bonding more silicon into the package.

##### Bets

* Bet 1: Programmability.The workload is a moving target (attention variants, novel model architectures), so keep every block programmable and let the developer writeCUDA. Even the specialised units are exposedthroughthat model rather than as fixed-function blocks.
* Bet 2: Hide Latency with Massive Multithreading.Latency is unpredictable and data-dependent, so hide it not with a static schedule but with massive thread overcommit, up to 64 resident warps per SM, with the hardwarewarp schedulerpicking a ready warp every cycle.
* Bet 3: Warp-wrapped Matmul.The matrix unit is the overwhelming compute throughput, but it must live behind the same warp/thread abstraction that everything else uses, so wrap it inmma.sync→wgmma→tcgen05.mma- rather than expose it as a fixed-function pipe. This enables a single kernel to fuse matmul, softmax, and element-wise ops in one pass.
* Bet 4: Async Memory Hierarchy.Make the memory hierarchyexplicitandprogrammer-managedrather thanimplicitandcompiler-scheduled. Keep theL2 cache, but exposeSMEMandTMEMas named scratchpads, and layer async machinery on top:TMAfor bulk copies,TMEMfor the matmul accumulator,mbarrierfor the producer/consumer handshake. The hierarchy issoftware-pipelinedinside a programmable kernel, not statically scheduled by a compiler against a known-latency scratchpad.
* Bet 5: Amortised SIMT Tax.Every transistor spent on a warp scheduler, register-file, or coherent cache is a transistor not spent on aMAC; accept the tax, and pay it down two ways: a Tensor Core now big enough that the SIMT machinery is amortised across a much larger MAC count, and units like TMEM trading away some general-purpose flexibility for MAC density.

#### Scaling

There are two regimes for scaling:scale-upandscale-out.

Scale-up
Bind several GPUs into one coherent memory domain. Any GPU can load or store any other GPU's 
HBM
 directly over 
NVLink
 at nanosecond latencies: one address space, no explicit transfers.

Scale-out
Network those domains together at the 
rack
 and 
cluster
 level. Data crosses via explicit 
RDMA
 at microsecond latencies: separate address spaces, but tens of thousands of chips per 
cluster
.

AI infrastructure uses both: bandwidth-hungrycollectives(tensor parallelism,MoE expert routing) stay inside the scale-up domain;data parallelismandpipeline parallelismcross the scale-out fabric.

##### Scale-up

The scale-up stack isNVLinkplusNVSwitch.NVLinkimplements acache-coherent fabricbetween GPUs, so a load or store on one GPU can target another GPU'sHBMwith the hardware handling address translation and coherence. ButNVLinkby itself is point-to-point: one link connects exactly two chips.NVSwitchis a dedicatedcrossbarchip that every GPU connects to, routing traffic so every GPU can simultaneously communicate with every other at fullNVLinkbandwidth,non-blockingandall-to-all.

Together they defined theHGX8-GPU baseboard, pairing eightH100SXMmodules withx86hosts (AMD EPYCorIntel Xeon) overPCIe Gen5. Hopper also shipped aGrace-paired form: theGH200 Grace Hopper Superchipbonded oneGraceARM CPU to oneH100overNVLink-C2Cat 900 GB/s, eliminating thePCIehost-device hop. Modules scaled up intoGH200NVL2pairs and rack-levelGH200NVL32. Blackwell makes the pairing the default. TheGB200module fuses oneGracewith two B200s overNVLink-C2C, andNVL72stitches 36 of them into a single liquid-cooled scale-up domain: 72 GPUs, 36GraceCPUs, 13.5 TB ofHBMand 17 TB ofLPDDR5Xas one flat, coherent address space. Rubin steps this in two.NVL144ships in 2026 as a Rubin-generation refresh inside the sameOberon-class rack: 72 Rubin packages, badged as 144 GPUs under NVIDIA's new die-counting convention, withHBM4and NVLink 6 doubling per-package bandwidth. The actual rack-scale jump is Rubin Ultra in 2027:NVL576packs 144 four-die Rubin Ultra packages into the newKyberchassis for 576 GPU dies in one coherent domain.

That density is held together bypassive copper. NVL72's NVLink fabric runs over 5,184 cables blind-mated through a backplane (~2 miles of cabling per rack, noin-cable retimers, theSerDesliving on the GPU andswitch ASICsthemselves), carrying ~130 TB/s ofall-to-allbandwidth across the 72 GPUs. NVIDIA estimates the copper choice saves roughly 20 kW per rack against an optical equivalent that would have neededpluggable transceiverson every link. Copper is what makesrack as one GPUeconomically practical: at sub-2-metre runs it still wins on power, cost, and signal integrity per dollar; beyond that, the bits have to go on glass.

NVL144 stays inside Oberon and copper continues to work because the package count (72) is unchanged from NVL72; the cabling doesn't have to lengthen, just transmit faster on Gen 6 SerDes.Rubin Ultra's NVL576 holds the same copper line by reshaping the rack: the newKyberform factor is roughly twice the height of Oberon and packs all 576 GPU dies into one enclosure, sized specifically so every NVLink path stays within passive-copper reach even at 144 four-die packages and tens of thousands of cables.

##### Scale-out

The scale-out stack comes from their acquisition ofMellanox. UnlikeNVLink, scale-out fabrics arenot coherent: nodes keep separate address spaces, and data crosses only via explicitRDMAinitiated by software, typically wrapped inNCCLcollectives likeall-reduceorall-to-all. The referenceclusteris theDGX SuperPOD: eight NVL72 racks stitched together overQuantum-X800InfiniBandyield 576 Blackwell GPUs under a single scheduler, and training clusters scale further by tiling SuperPODs. Rubin SuperPODs in 2026 keep the same 8-rack pattern with NVL144 (yielding 1,152 GPUs per SuperPOD instead of 576). Rubin Ultra in 2027 scales the recipe up an order of magnitude: Kyber racks of 576 GPU dies each, stitched together overQuantum-X PhotonicsCPO, putting thousands of GPUs under one scheduler.

Every GPU has its ownConnectXNICinto that fabric. Blackwell nodes run ConnectX-8 at 800 Gbps per GPU, an order of magnitude less bandwidth than per-GPUNVLink, and latencies climb from nanoseconds to microseconds. Rubin moves to ConnectX-9 at 1.6 Tbps per GPU, doubling the per-GPU scale-out bandwidth as the per-rack scale-up domain grows from 72 to 576 GPUs. Alongside each NIC sits aBlueField DPU, adding ARM cores and accelerators to offload storage, networking, and security from the host CPU. For customers who prefer Ethernet toInfiniBand,Spectrum-Xis a lossless-Ethernet alternative tuned for AI traffic.

The crossover from copper to glass happens at the rack boundary. Inside the NVL72 the spine is copper; once a link has to cross racks at 800 Gbps it isoptical. Passive copper DAC tops out at roughly 1.5–2 metres at 200 G/lane, well short of cross-rack reach, so today's SuperPOD spine rides overOSFP-RHSpluggable transceivers, each module carrying its own laser, modulator, photodetector, and DSP. A SuperPOD spine fanning out to thousands of GPUs is, in optical terms, tens of thousands ofpluggablesdrawing tens of kilowatts on transceiver lasers alone.

With Rubin, that optical layer collapses into theswitch ASIC.Quantum-X Photonics(InfiniBand) andSpectrum-X Photonics(Ethernet) replace the pluggables withco-packaged optics: lasers, modulators, and photodetectors bonded onto the switch package via TSMC COUPE. NVIDIA claims ~4× fewer lasers and ~3.5× lower link power than the OSFP-pluggable equivalent. The chiplet logic that turned the GPU into a two-die package and stacked HBM next to it is now showing up at the network layer: vertical integration of compute, memory,andphotonics on one substrate.

NVLinkFusionrecently opened the scale-up fabric itself: third-party CPUs andXPUscan now joinNVLinkdomains, letting hyperscalers build semi-custom racks around NVIDIA's interconnect without designing their own coherent fabric from scratch.

#### Software

CUDAis the natural programming model for amassively parallelprocessor. You write a kernel (one piece of code executed once per thread) and launch it across thousands of threads organised into blocks and warps; the programmer decides what they share, when they synchronise, and which piece of the problem each one handles. That is why the abstraction has barely changed in eighteen years, and why every CUDA kernel written since 2007 would still compile and run on Blackwell.

That continuity is both the moat and the constraint. Each new generation introduces new hardware (Tensor Cores,TMA,TMEM) onto the same kernel-and-warps model, exposed as intrinsics inPTXandSASS:mma.sync,wgmma.mma_async, and so on. NVIDIA cannot radically rethink the SM because too much code depends on it; in return, every investment in CUDA software compounds across generations.

On top of PTX sits a stack constructed over two decades.cuBLASandcuDNNfor math and DNN primitives;CUTLASS, encoding decades of GEMM expertise in templated C++;TensorRT-LLMfor paged attention, in-flight batching, and speculative decoding; framework bindings throughPyTorch,Triton, andJAX.

FlashAttention, one of the most important algorithmic rewrites in modern AI, tiles attention to avoid materialising theO(N2)O(N^2)O(N2)matrix. Its four generations (FA1 through FA4) have each been hand-optimised for the latest NVIDIA silicon (FA3 for Hopper's async pipelines, FA4 for Blackwell), with ports to other hardware trailing by months or years.

Most of this stack is written by people NVIDIA does not pay. The moat is not CUDA itself; it is two decades of third-party kernels, libraries, and tooling, and the millions of developers who have learned the API along the way.

NVIDIA also ships human expertise alongside the silicon. They embed dozens of their own engineers inside frontier labs and hyperscaler teams, writing kernels for each new model architecture and tuning them to each new silicon generation. Whatever a lab wants to train next month tends to run well on NVIDIA much faster than other platforms. Switching off NVIDIA is therefore not just rewriting the kernels and libraries. It is re-training the mental models of an entire engineering workforce, and losing the NVIDIA engineers who today sit inside the building.

### Google TPU

TheTPUis amatrix multiplication machine. The philosophy is, rather than a programmable chip that can run any massively-parallel workload, focus on a single primitive (dense matrix-multiplication on a largesystolic array) and let theXLAcompiler plan every cycle and every byte of memory ahead of time. No hardware scheduler, no cache, no threads/warps. Each generation grows thepod, with thousands of chips wired through theICIinterconnect into one coherent machine. A TPU has no ambition to render graphics or run scientific simulation; it exists to train and serve Google's workloads (search, translation, recommendation, Gemini) more efficiently per watt than any general-purpose alternative.

#### Genealogy

2015
TPU v1
v1
First production deep-learning ASIC; 
INT8
 inference only over 
PCIe
.

2017
TPU v2
v2
First training-capable TPU; switched the 
MXU
 from 
INT8
 to 
BF16
, established dual-
TensorCore
 + 
HBM

2018
TPU v3
v3
First liquid-cooled TPU; doubled 
MXUs
 and 
HBM
 versus v2; 1,024-chip pods.

2020
TPU v4
v4
, 
v4i
First reconfigurable 
optical circuit switches
 (
Palomar
); 
SparseCores
; both 
BF16
 & 
INT8
; 4,096-chip pods.

2023
TPU v5
v5e
, 
v5p
v5e for efficiency, v5p for performance; v5p has 3.3× INT8 FLOPs & 2.2× HBM BW of v4, 8,960-chip pods.

2024
Trillium
v6e
First 256×256 
MXU
; 4.7× v5e peak FLOPS at similar power; trained 
Gemini 2.0
.

2025
Ironwood
v7
Built for inference of reasoning models; adds native 
FP8
; 9,216-chip superpods at 
42.5 ExaFLOPS FP8
.

2026
TPU v8
8t
, 
8i
 8t for training, 8i for inference; adds native 
FP4
; 9,600-chip superpods at 
121 ExaFLOPS FP4
 (8t).

#### Architecture

A TPU chip is amatmul engine wrapped in just enough silicon to keep it fed. The unit of compute is theTensorCore: flagship chips fromv2onward carry two per package; efficiency-tuned chips (v4i,v5e,v6e) carry one. Inside every TensorCore sits the same five-component recipe: one or moreMXUsfor matrix math, aVPUforelement-wise math, aScalar Unitthat runs the show, anXLUfor cross-lane reductions, and an attachedTranspose/Permute Unit, plus accumulator queues feeding and draining the MXU. Fromv4onward each chip also carries dedicatedSparseCoredataflow engines outside the TensorCore (4 per chip onv4,v5p, andIronwood; 2 per chip onTrillium), explicitly carved out to absorb theembedding-lookupworkload the systolic array was the wrong shape for. Every block sits on a singleVLIWissue plane driven by aCore Sequencerthat fills all eight functional slots of a 322-bit bundle every cycle. There is no instruction cache miss, nowarp scheduler, no out-of-order engine, nobranch predictor: the compiler is the scheduler, and the silicon area saved is spent on moreMACs.

##### TensorCore

TheMXUis the systolic array.v1shipped one 256×256 INT8 inference array;v2was the first training-capable TPU and introduced 128×128 cells doingBF16multiply withFP32accumulate (INT8 came back to the MXU atv4onwards at equivalent throughput). Cell counts per TensorCore grew from there: 1 MXU onv2→ 2 onv3→ 4 onv4/v5e/v5p.Trilliumwent back to 256×256 (65,536 multiply-accumulate cells per array per cycle), andIronwood,8t, and8iall kept the 256×256 shape.

To computeC=A×BC = A \times BC=A×B, matrix B's values are pre-loaded one weight per cell:weight-stationarydataflow, the choice that distinguishes TPUs fromoutput-stationaryarrays elsewhere. Activations enter from the left edge, propagate one column per cycle, multiply against the resident weight at every cell, and partial sums flow downward intoaccumulator queuesat the bottom. Once data enters the array no memory access occurs: each weight is reused for every activation that passes through, each activation is reused 128 (or 256) times across the row. Data reuse is wired into the silicon, not arbitrated by a cache. The dominant cost in computing is not the multiplication itself (a few picojoules) but reading and writing memory at 100–1000× more energy per access; the systolic array deletes that cost by construction. The trade-off isunderfill: a 128×128 matmul on a 256×256 array wastes 75% of the silicon, soXLAtiles,pads, andschedulesdimensions to multiples of 128 (or 256 on v6e+) and the model code is written with those quanta in mind.

TheVPUis the second-fiddle compute engine but is in many ways the more interesting microarchitectural object: every TPU is a 2D vector machine, not a 1D SIMD machine. The VPU's register file holds 2DVREGs. Onv4/v5pthe shape is(8, 128): 128laneswide, 8sublanesdeep, 32 (v4) or 64 (v5p) registers per core, with 4 independent floating-point ALUs per (lane, sublane). The lane axis matches the systolic array's input width, so the lane count presumably widened to 256 alongside the MXU onTrilliumandIronwood; Google has not published post-v5p VPU dimensions. The sublane axis lets the VPU stream tiles through the MXU at one matmul per X clocks (where X is the sublane dimension). Most of the speedup in modern TPU programs comes fromVPU/MXU overlap: quantisation, layernorm, softmax, activation, and bias-add all run on the VPU in the same cycles the MXU is running the matmul behind them. Cross-lane reductions (the awkward case for any 2D vector ISA) are handled by theXLU: slow, expensive, and a known compiler hot spot. Layout transforms that misalign with the 2D shape are absorbed by the dedicatedTranspose/Permute Unit, sparing a round-trip through memory.

TheScalar Unitis the smallest block and arguably the most consequential: a single-threaded, dual-issue integer ALU with 32 32-bit registers and 4 KiB ofSMEMfor control state, paired with an Imem holding the program. It is the only block that does instruction fetch; every cycle it pulls a 322-bit VLIW bundle, executes its own two scalar slots locally (address arithmetic, loop counters, branches, sync-register checks), and dispatches the remaining six slots to the rest of the chip: 2 vector ALU (VPU), 2 vector load/store (HBM↔VMEMDMA), 2 matrix (push/pop the MXU queue). Synchronisation between blocks is explicit:sync flagstrack when MXU and VPU pipelines are busy, and the compiler inserts barrier checks rather than the hardware tracking dependencies. The Scalar Unit is what makes the rest of the TensorCore look like fixed-function dataflow: every cycle, one place decides what eight things happen, and there is no dynamicreorder bufferto undo a bad decision.

##### Memory

The on-chip memory hierarchy is the same idea as the compute side:there are no caches, every level is software-managed. Off-chip isHBM(16 GB on v2/v5e, 32 GB on v3/v4/v6e, 95 GB on v5p, 192 GB on Ironwood, 216–288 GB on the v8 generation), and on-chip is a hand-stacked tier of explicitly-addressable scratchpads. Closest to compute isVMEM, the vector scratchpad feeding both the VPU and the MXU input queues, sized 32 MiB on v4, 128 MiB on v5e, and stretched to 384 MiB on the inference-tunedv8iprecisely to hold an entireKV cacheon chip. Above it sitsCMEM, introduced withv4at 128 MiB: a slower, larger SRAM staging area between HBM and VMEM that absorbsfused-opintermediates. TheScalar Unithas its ownSMEM(~10 MiB for control state on v4) and a tiny scalar register file. Every tensor in the program is pinned to one tier at compile time; XLA'sbuffer-assignmentpass schedulesDMAsacross tiers so that data arrives just before the cycle that consumes it. The hardware does no prefetching, no eviction, nocoherence; when the compiler gets it right, the array never stalls; when it gets it wrong, there is no fallback path.

##### SparseCore

The block outside the TensorCore that breaks the systolic mould isSparseCore, introduced withv4.Recommenderand ranking models live onembedding lookups(billions of indices into vast tables), and the access pattern is the inverse of dense matmul:irregular,indirect,all-to-all. A 256×256 systolic array is exactly the wrong shape. SparseCore is adataflow processorwith 16 compute tiles and dedicatedSPMEMscratchpads, sitting alongside the TensorCore and absorbingscatter,gather, andsegmented-reduceprimitives plus the data-dependentall-to-alltraffic that shardedembeddingtables generate. This achieves 5–7× speedup onembedding-heavy models for ~5% of die area and power.v4shipped 4 SparseCores per chip,v5pkept that count,Trilliumdropped to 2, andIronwoodwent back to 4 (2 per chiplet on its dual-die layout). Thev8i (Zebrafish)inference chip removes SparseCore entirely and replaces it with aCAE (Collectives Acceleration Engine)on the I/O chiplet: different problem (collectivereductionsduringautoregressive decode), same idea (carve a small accelerator off the main core to absorb a workload the systolic array is the wrong shape for).

##### Numerics

TPUv1wasINT8-only inference;v2switched this forBF16as the canonical training format: same dynamic range asFP32, half the memory, noloss-scalingtricks.v4reintroduced native INT8 support.Ironwoodthen added nativeFP8support (both E4M3 and E5M2) for ~2× the throughput of BF16 in the same area. v8 adds nativeFP4plusblock-scale multiplicationinside the MXU itself, which deletes the VPU dequant overhead that Ironwood still paid.Stochastic roundingis hardware-supported on every modern TensorCore: rounding decisions made by the lower mantissa bits acting as a probability, which preserves the expected value of low-precision accumulations across long training runs and is one of the small details that lets BF16/FP8 close the accuracy gap to FP32.

At the chip boundary sit theICIports themselves (4 ports on the2D-toruschips v2/v3/v5e/v6e, 6 on the3D-torusflagships v4/v5p/v7/8t), and theDCNNIC for scale-out. From a chip-level perspective the ICI ports look like just another set ofDMAengines theCore Sequencercan target inside a VLIW bundle: a remote-tensor send is the same instruction class as a VMEM-to-HBM transfer, and the compiler treatscollectivesas part of the same overallscheduleit builds for compute and local memory.

##### Bets

* Bet 1: Systolic array.Matmul dominates the workload, so spend the silicon on a systolic array.
* Bet 2: Software scratchpads.Compute is cheap and memory is expensive, so reuse data in the wires of the array and replace caches with software-managed scratchpads.
* Bet 3: Compiler scheduling.The workload is statically predictable, so move scheduling into the compiler: VLIW issue, nospeculation, no out-of-order, nodynamic scheduler.
* Bet 4: MAC-only silicon.Power matters more than peak, so delete every transistor that does notmultiply-add: every cache tag, every branch predictor, every reorder buffer.
* Bet 5: Dedicated off-array engines.The dense matmul array is the wrong shape for some real workloads (embeddings,collectives), so carve out small dedicated engines (SparseCore, CAE) rather than warp the main core to fit them.

#### Scaling

The TPU's scale-up story is the inverse of NVIDIA's. WhereNVLink+NVSwitchmake every other GPU'sHBMlook like local memory (a hardware-managed coherent address space), Google'sICIismessage-passing. There is noremote-load semantics, nocache coherence, nocrossbar. Every multi-chip operation is an explicitcollectivecompiled byXLA. The scale-up domain is tied together not by a switch fabric but by atorus(chips wired directly to their neighbours withedge wrap) and stitched at the rack boundary byoptical circuit switches.

Scale-up
Wire chips directly to one another in a 
2D
 or 
3D torus
 over 
ICI
. XLA emits 
SPMD
 collectives that tightly choreograph thousands of TPUs as one program. No coherence, but huge 
bisection bandwidth
 at low latency.

Scale-out
Network 
pods
 together over the datacenter fabric: many more chips than fit in one 
ICI
 domain, at lower per-chip bandwidth. Today: 
Virgo
 handles east-west TPU traffic (v8t+), 
Jupiter
 handles north-south. 
Multislice
 + 
Pathways
 orchestrate 
SPMD
 across pods.

##### Scale-up

ICIlinks come straight out of the TPU die: high-speedserial lanes,direct-attach copperinside a 64-chip cube (a 4×4×4 arrangement that lives in one liquid-cooled rack), optical between cubes. Per-chip aggregateICIbandwidth has scaled from ~250 GB/s onv2to1.2 TB/s bidirectional onIronwood, and2×that onv8t. Topology alternates by generation:2D toruson the efficiency-tuned chips (v2,v3,v5e,v6e),3D toruson the flagships (v4,v5p,v7,v8t).

The piece with no NVIDIA analogue is thePalomar OCS: a3D-MEMSoptical circuit switchthat sits between cubes. Tiny mirrors physically rotate to map any input fibre to any output. Av4superpoduses 48 Palomar switches to wire 64 cubes (4,096 chips) into one 3D torus;v5pandIronwoodscale the same scheme up. Reconfiguration is millisecond-class, not nanosecond, but that's fine, becauseOCSiscircuit-switched: pick a topology at job start, run it for a week, then reconfigure for the next workload. Three problems collapse into one component: topology reconfiguration per workload (twisted torigive up to 70% betterbisection), sub-podslicingon demand, andfault tolerance(when a chip dies, theOCSoptically swaps in a spare cube and the run continues without losing theICIdomain).

This makes thesuperpodthe unit of scale-up: equivalent in role to NVIDIA's NVL72, two orders of magnitude bigger.v4was 4,096 chips;v5p, 8,960;Ironwood (TPU v7)is 9,216 chips arranged as 144 cubes of 64, presenting1.77 PB ofHBM(~68 PB/s) and 42.5 ExaFLOPSFP8as one coherentICIdomain.

TPU 8t (Sunfish)stretches this to9,600 chips, 2 PB ofHBM(~62 PB/s), and 121 ExaFLOPS FP4.TPU 8i (Zebrafish)has1,024 chips, ~295 TB ofHBM(8.8 PB/s), and ~10 ExaFLOPS FP4. 8i replaces torus with a new hierarchicalhigh-radixtopology calledBoardfly(4-chip ring → 8-board group → up to 36 groups linked byOCS), cuttingall-to-alllatency in half. This is designed forMoEinference. A 3D torus excels whencollectivesare nearest-neighbour (ring all-reduceuses every link every cycle), butMoE expert routingis the opposite pattern,all-to-all: every chip ships unique fragments to every other, and round-trip latency is bounded by the longest-hop pair. A 1,024-chip 3D torus has a 16-hop diameter;Boardfly's ring → group → OCS hierarchy compresses that to 7.

##### Scale-out

ThroughTPU v7, scale-out ran over a single fabric:Jupiter,all-optical at the spine since 2022viaApollo OCS, the same 3D-MEMS family asPalomar, scaled across the building. Google uses the same primitive (optical circuit switching) at every layer from rack to datacenter spine; that is the architectural signature nobody else has.Jupitertoday carries 13 Pb/s ofbisectionper building.

WithTPU 8t, scale-out split into two fabrics. East-west TPU-to-TPU traffic moved toVirgo, a dedicated accelerator fabric;Jupiterretained thenorth-southrole: storage access, general compute, and inter-site scaling.Virgois aflat,two-layer,non-blockingtopology built onhigh-radixswitches: every TPU is at most two switches from any other. OneVirgocluster links 134,000+TPU 8ts at 47 Pb/s ofbisection(4× the per-chip bandwidth and 40% lowerunloaded latencythan the priorDCNgeneration), withmulti-planar fault isolationandsub-millisecond telemetrythat lets the scheduler kill stragglers before they wreck a step. The architectural payoff is that each layer can now evolve independently: scale-up, east-west scale-out, and front-end can iterate on different cadences without rewiring the others.

Per-chip scale-out bandwidth is on the order of100 Gbps onIronwood, and4×that onv8t, but still two orders of magnitude less than per-chipICI. This bandwidth gap dictates partitioning:tensor parallelismandMoE expert routingstay insideICI;data parallelismandpipeline parallelismcross the scale-out fabric.

Google'sMultisliceframework, plumbed intoXLA, lets a singleSPMDprogram span multipleslicesin differentpods; the compiler emits hierarchicalcollectives(ring all-reduceinside each slice,higher-level reduceacross). The structure is exactly the trick for hiding theICI/DCNbandwidth gap: as much work as possible stays inside the slice over fast ICI, leaving only the cross-slice residual to pay the slow-fabric cost.

Above this sitsPathways. WhereNCCL+Slurm+Megatron-styleschedulersdriveSPMDfrom many controllers,Pathwaysdrives the entire job fromoneclient andvirtualisesmultiple "islands" (podswith their ownICIdomains) connected overDCN. It doesgang scheduling,elastic training(when a slice fails,OCSreshapes the topology andPathwaysresumes from the last checkpoint on the new shape), andcross-region orchestration.Gemini Ultrawas the first frontier model trained across multiple datacenters;Pathwaysstitches them into one synchronousSPMDjob.

The philosophy:the compiler is the scheduler, the torus is the topology, and the optical switch is the universal reconfigurable substrate, at every layer from rack to datacenter.

#### Software

The TPU stack iscompiler-drivenwhere CUDA iskernel-driven. On a GPU, the developer writes the kernel and theframeworkstrings kernels together; thecompiler's job is mostlylocal. On a TPU, the developer writes a numerical program inJAXandXLAis responsible for everything below it: which operationsfuse, where each tensorlives, how it islaid outacross the 2D vector registers, whenDMAsfromHBMtoVMEMissue, how the 322-bitVLIWbundles arescheduled, how the programshardsacross thousands of chips. There is no hardware fallback: nowarp scheduler, no cache, no out-of-order engine to paper over a badschedule. Thecompileris the system. The trade-off is the central one of the architecture:XLA gets closer to the theoreticalceilingwithout hand-tuning, butclosing the remaining gapis harder.

The compilation path isJAX→JAXpr→StableHLO→HLO→LLO→VLIW bundles.JAXtraces a Python function into atypedfunctionalIR(JAXpr) underjit, lowers it toStableHLO(theOpenXLA-standardised,versionedop-setof ~100statically-shaped primitivesthat allfront-endsnowemit), which XLAingestsasHLOand runs through its pass pipeline:operation fusion(collapsepointwise+reduction+matmulinto one kernel so intermediates never hit HBM),layout assignment(decide the2D tilingof every tensor so itstreamsinto theMXUwithout atranspose: substantially harder than on1D SIMD machinesbecause both the registers and the systolic inputs are 2D),buffer assignment(every tensor pinned to either VMEM, CMEM, or HBM withoverlap windowspre-computed),SPMD partitioning, and finally a VLIWschedulerthat fills all eight slots of every bundle.HLOlowers toLLO(Low-Level Optimizer), the TPU-specificIR, and LLOemitsthe final VLIW stream. A well-compiled program overlapsMXUsystolic execution, VPUelement-wise math, and HBM↔VMEM DMA in the same bundle every cycle.

Multi-chip execution isSPMD: one program, sharded data, hierarchicalcollectives,emittedbyGSPMD(now being replaced byShardy, anMLIR-native successor that lands as the default in early 2026). The user expresses shardingdeclarativelywithMesh+PartitionSpecannotations on a few key tensors; thecompilerpropagates shardings through the rest of thegraphand insertsall-reduces,all-gathers, andreduce-scatterswhere the layout changes. When thecompilerpicks a wrong collective,shard_mapdrops the user intomanual SPMD(per-device code with explicit local shapes and explicitcollectives), composable insidejitso a single kernel can be hand-partitioned without giving up auto-partitioning everywhere else. This is the inverse of the PyTorch idiom:FSDPandDeepSpeedwrap the model in a runtime that issuescollectivesat module boundaries; GSPMD/Shardy partitions the wholegraphas acompilerproblem.

Pallasis the escape hatch: JAX's kernel-writing language, broadly the TPU equivalent ofTritonon GPUs. Pallas kernels are written in JAX-flavoured Python, lowered throughMosaic(theMLIR-based TPU backend) to LLO, and embedded back into HLO as a custom op. It exists because XLA cannot always synthesise the optimum for novel attention variants, fused MoE dispatch, or anything that demands manual VMEM tiling and DMA scheduling: aFlashAttention-classoptimisation, where the win is in thescheduleand not the algebra.Pallas:Mosaic-GPUtargets H100/Blackwell with the same front-end, so a kernel author can write once and lower to either substrate. The library tier above this is uniformly JAX-native:Flax NNXfor modules,Optaxfor optimisers,Orbaxfor asynchronous distributed checkpointing,Grainfor input pipelines,Tunixfor post-training/RL,Qwixfor quantisation. Google's reference training stacks (MaxTextfor LLMs including DeepSeek-V3-class MoE, andMaxDiffusionfor Flux, Wan 2.1) sit at the top, in pure JAX;Pathwayssits beneath, exposed to the user aspathwaysutils, so a single Python client can drive a job across thousands of chips and several pod-islands without giving up the JAX programming model.

The PyTorch path is real but second-class.torch_xlauses aLazyTensormechanism: every PyTorch op records into an HLOgraphthat compiles on the next barrier, with the compiled artifact cached by graph-shape hash. PyTorch/XLA 2.x addedGSPMD-style sharding annotations,torch.compileintegrationthrough an XLA backend, aJAX bridge, and (PyTorch/XLA 2.7) C++11-ABI builds with materially faster tracing. The gap to JAX is real (JAX's primitives map more cleanly toStableHLO, and complex parallelism strategies are better-covered), which is whyvLLM TPU(powered by thetpu-inferenceplugin announced at Cloud Next 2025) lowerseverymodel, JAX-defined or PyTorch-defined, through aunified JAX→XLA path.TorchTPU, announced April 2026, is Google's response: a native PyTorch experience with eager mode,torch.distributed, andtorch.compileover XLA, on track to replace torch_xla.

Compared to CUDA, the TPU ecosystem iscentralised, not sprawling. Almost everything below the framework (XLA, JAX, Flax, Optax, Pallas, MaxText, Pathways, Shardy, Mosaic) is open-sourced by Google itself, evolving in lockstep with the silicon. There are far fewer third-party kernels than CUDA's decades of accumulation; the moat is thinner where the workload looks weird, deeper where the workload looks like Gemini. The recentIronwood (v7) "codesigned AI stack"language is the explicit framing: chip, ICI fabric, OCS, XLA, Pathways, Pallas, MaxText, vLLM, and Pathways co-released as one product, with v8t/v8i continuing the same model under a single tpu-inference lowering path.Tritonandtorch.compilenarrow the gap on the NVIDIA side (kernel-driven and compiler-driven are converging), but the philosophical poles are still real:on TPU thecompileris the only interface that matters; on GPU thecompileris one of several.

### AMD GPU

TheAMD InstinctGPUsare built on a different bet from NVIDIA: where NVIDIA each generation expands what each SM cando, AMD has held theCompute Unitconservative sinceGCN(2012) and reinvested into the package: matched or beat the contemporary NVIDIA flagship onHBMcapacity every generation since 2021; the first3D-stackeddatacenter GPU (CDNA 3); the first coherentCPU+GPUAPU(MI300A); and anopen ecosystem(ROCm,HIP, OCP MX,UALink).

#### Genealogy

2018
Vega 20
MI50
, 
MI60
First 7 nm GPU; 1:2 
FP64
 vector throughput. Last GCN-family Instinct before the 
CDNA
 / RDNA.

2020
CDNA
MI100
First 
MFMA
 matrix cores; graphics fixed-function silicon dropped entirely. Native 
BF16
.

2021
CDNA 2
MI210
, 
MI250
, 
MI250X
First MCM Instinct via dual-GCD package; full-rate 
FP64
 matrix

2023
CDNA 3
MI300A
, 
MI300X
First 3D-stacked chiplet GPU: 
XCDs
 hybrid-bonded onto 
IODs
 via 
TSV
; 
FP8
; 
Infinity Cache
; coherent CPU+GPU 
APU
 on MI300A; powered 
El Capitan
.

2024
CDNA 3 refresh
MI325X
Same compute, 
HBM3E
 refresh: 256 GB at 6.0 TB/s.

2025
CDNA 4
MI350X
, 
MI355X
Native 
FP4
 / FP6 with OCP MX microscaling; per-CU 
FP64
 cut roughly in half; first generation tilted toward AI density over HPC.

2026
CDNA Next
MI430X
, 
MI440X
, 
MI455X
HBM4
; the 
Helios
 rack (72-GPU 
MI455X
 flagship over 
UALoE
 at launch, native 
UALink
 from 2027): AMD's first answer to NVL72.

#### Architecture

Terminology

AMD
NVIDIA

Compute Unit (CU)
Streaming Multiprocessor (SM)

SIMD
SM Sub-Partition

SIMD Lane
CUDA Core (FP32 ALU)

Wavefront (wave64)
Warp (warp32)

Matrix Core
Tensor Core

MFMA
mma.sync / wgmma / tcgen05.mma

VGPR / SGPR
Register File

LDS (Local Data Share)
SMEM (Shared Memory)

Infinity Fabric
NVLink

Where NVIDIA's architectural ambition livesinsideeach SM (new tensor primitives, new async machinery, new operand stores each generation), AMD's livesbetweentheCUs, in how many of them can be bonded into a single coherent package. The CU itself is conservative: four 16-laneSIMDs, one shared scalar unit, a 64 KBLocal Data Share, an L1 vector cache, a per-SIMDVGPRfile with a CU-sharedSGPRpool, and (since CDNA 1) aMatrix CorerunningMFMA. The shape hasn't meaningfully changed sinceGCNin 2012; what scales is the count (120 CUs onMI100, 220 onMI250X, 304 onMI300X, 256 onMI355X) and the packaging that bonds them. Awavefrontof 64 threads streams across the 16 SIMD lanes over 4 cycles, with many wavefronts resident per SIMD that the scheduler switches between to hide stalls. There's nothing exotic in here; what's interesting about CDNA is everythingoutsidethe CU.

##### Compute

Inside the CU, the SIMDs and the Matrix Core run side by side. The fourSIMDshandle everything element-wise: activations, normalization, residuals, address arithmetic. TheMatrix Corehandles the matmul. The split is the same as NVIDIA'sCUDA Cores/Tensor Coressplit, but the matrix abstraction has evolved on a very different curve.

NVIDIA's Tensor Core climbed the thread hierarchy: a 32-threadwarponVolta, a 128-threadwarp-grouponHopper, a single thread plus an optionaltwo-SM clusteronBlackwell. AMD's Matrix Core stayed put. Every generation ofMFMA(from MI100 in 2020 through MI355X in 2025) is wavefront-scoped: onewave64issues a single matrix op (V_MFMA_*), the four SIMDs cooperate to drive it, and operands come from the wavefront's register file: A and B fromVGPRs, C and D usually from the dedicatedAGPRfile. The instruction got faster and the format set widened, but the issuer and the scope did not. The one feeder-side concession came with CDNA 4: a dedicatedMFMA transpose-load from LDSthat hands operands to the Matrix Core already in the layout it wants, small in spirit to NVIDIA's TMA, but the matrix op itself stayed wave-issued.

The throughput numbers tell the format story directly. CDNA 1 launched in 2020 with FP32 / FP16 /BF16/ INT8 at 256 / 1024 / 512 / 1024 FLOPs per CU per cycle, with nativeBF16support alongsideA100. CDNA 2 doubled theFP64path to a full-rate matrix at 256 FLOPs/CU/cycle: uniquely AMD, the bet that put MI250X intoFrontier. CDNA 3 reached parity withH100onFP8at 4,096 FLOPs (E4M3 + E5M2), added 2:4structured sparsity, and added aTF32-equivalent path that runs FP32 matmul at the FP64-matrix rate by truncating mantissas. CDNA 4 doubled again toFP4at 16,384 FLOPs and FP6 withOCP MX block-scaling, and added mixable A/B precision in one MFMA: FP8 × FP4, for example. The same generation halved per-CU FP64 throughput, the first AMD chip to trade HPC density for AI density rather than ship both.

The wavefront-scope decision shows up in two costs.

Divergence.A half-emptywave64wastes 32 lanes where a half-empty warp32 wastes 16. For workloads with mostly-uniform control flow this is a small price; for irregular workloads it hurts.

Overlap.NVIDIA's asynchronous, descriptor-driven matmul decouples issue from execution: the issuing thread fires the instruction and moves on; the Tensor Core runs in the background; the warp can run softmax, apply a mask, or pre-load the next tile while the previous matmul is still in flight. AMD's wavefront-collective MFMA gives the wave no equivalent: the same wave that issued the matmul can't simultaneously do meaningful vector work while it's pending. Overlap is possible acrossseparatewavefronts, but has to be staged in software with explicit wavefront barriers, which is more fragile and consumes more wave slots and registers.

How much this matters depends on the workload.Pure dense GEMM(DGEMM, the inner loop of large-batch training) has nothing useful to do during the matmul; both engines saturate; async buys little. These are exactly the workloads where AMD has historically led at exascale HPC (Frontieron MI250X,El Capitanon MI300A).Transformer attention(FlashAttention-3, FA4) interleaves matmul with softmax, masking, and KV-cache reads, and the async overlap is the whole structure of those kernels. AMD has to recreate the pipeline by hand, which lags NVIDIA's hardware-level support.MoE dispatch, paged attention, speculative decodesit in the same camp: address-irregular work that wants to run alongside the matmul.

NVIDIA's matrix-instruction abstraction has moved further across generations (warp → warp-group → single-thread async + cluster), and AMD hasn't followed.

##### Memory

AMD's memory hierarchy hasfewergeneral-purpose tiers than NVIDIA's, with one giant cache that NVIDIA does not have at all. From the CU outward: a 64 KBLDSscratchpad (software-managed, 32-bank, AMD's analog of NVIDIA'sSMEM), a vector L1 (16 KB on early CDNA, 32 KB fromMI300Xonward), a per-XCDL2 of a few MB. The L2 isn't coherent across XCDs, though; coherence happens one tier above L2.

That tier is theInfinity Cache: 256 MB on MI300X, distributed across the fourIODs, 16-way set-associative, ~12 TB/s measured, more than twice MI300X's 5.3 TB/s ofHBM3. It originated on RDNA gaming GPUs to compensate for narrow GDDR buses; AMD reused the IP for AI on CDNA 3, where attention KV reuse and weight reuse fit a large LLC unusually well. NVIDIA bet on bigger HBM bandwidth instead (8 TB/s onB200, scaling withHBM4onRubin), and AMD bet on the cache.

Off-chip, the HBM capacity grows aggressively: 32 → 64 → 128 → 192 → 256 → 288 GB acrossMI100/MI210/MI250X/MI300X/MI325X/MI350X, matching or exceeding the contemporary NVIDIA flagship in every generation from 2021 onward. The bet is that inference workloads are increasingly capacity-bound, and that the chip with more memory wins.

##### Numerics

The format trajectory tracks the precision-halving pattern that everyone in AI silicon shares: FP32 → FP16 → FP8 → FP4, restoring accuracy each step with finer-grained scaling. The AMD-specific axis isopenness. CDNA 4'sFP4and FP6 useOCP MXblock-scale multiplication: the same numeric format asBlackwell's MXFP4 and TPU v8's MXU, but specified by an open consortium (AMD, NVIDIA, Intel, Meta, Microsoft, Qualcomm, ARM) that AMD helped found, rather than by any single vendor. The format that ships in MI355X is identical to what ships in B200 and TPU v8.

The CDNA 4 inflection deserves its own line: per-CU FP64 throughput halved.MI300Xserved training, HPC, and inference together;MI355Xis an AI chip first. The full-rate FP64-matrix bet that poweredFrontierhasn't been killed, but it's no longer carrying the weight.

##### Chiplets

The packaging is where CDNA stops looking like NVIDIA and starts being something else.

CDNA 1'sMI100was monolithic 7 nm. CDNA 2'sMI250Xwas AMD's first multi-chip GPU: twoAldebaranGCDs side-by-side on a 2.5D EFB organic substrate, joined by 4 in-packageInfinity Fabriclinks at 400 GB/s aggregate, but presented to software as two separate GPUs.

CDNA 3 is the move that changed everything. EightXCDs(TSMC N5, ~115 mm² each) are stacked in 3D viaTSMC SoIChybrid bonding (sub-micron-pitchTSVs, no microbumps) onto fourI/O dies(TSMC N6) below. The IODs carry theInfinity Cache, theHBM3PHYs, the Infinity Fabric links, andPCIe Gen 5; each IOD hosts two XCDs above and two HBM stacks beside. The four IODs are stitched byInfinity Fabric APat 4.8 TB/s bisection, so the 153-billion-transistor package looks like one GPU to the kernel: cache and address space unified at the IOD layer. NVIDIA stayed monolithic throughH100and only went to two reticle-limit dies onB200via 2.5DCoWoS-L. AMD got to 3D stacking a generation earlier, at smaller per-die area: different bets on the same packaging frontier.

TheMI300AAPUpushed the bet further. Replace 2 of the 8 XCDs with three Zen 4CCDs, leave HBM and Infinity Cache and the IODs intact, and let CPU and GPU share one physical address space backed by HBM3 with hardware coherence. There is no host-device copy. There is no pinned memory. There is no PCIe in the path. Zen 4 cores and CDNA 3 XCDs read from the same pages. NVIDIA'sGrace-Hopperbridgestwopackages overNVLink-C2C; MI300A isone.El Capitan(11,039 nodes of 4× MI300A) is the deployment that justified it.

On CDNA 4'sMI355X, eightXCDsare still 3D-stacked viaSoIConto base dies below, but the XCDs move to TSMC N3P with 32 active CUs apiece (256 total, vs 304 onMI300X; the per-XCD count dropped to free area for biggerMatrix Coresand a 160 KBLDS). The four MI300XIODscollapse to two, each twice as wide on TSMC N6, hosting four XCDs above and fourHBM3Estacks beside. Each IOD now carries its own 128 MB slice of the 256 MBInfinity Cache, half the HBM PHYs, its share of theInfinity Fabriclinks, andPCIe Gen 5.Infinity Fabric APbetween the two IODs runs at 5.5 TB/s bisection (~15% above CDNA 3), and the eight stacks shift to 12-Hi HBM3E for 288 GB at 8 TB/s, 50% more capacity than MI300X on the same pin count. The package totals 185 billion transistors and still presents as one GPU to the kernel.

##### Bets

* Bet 1: HPC then AI.HPC and AI are the same betuntil they aren't: ship full-rate FP64 matrix from CDNA 2 through CDNA 3, then bifurcate at CDNA 4 once inference economics decisively favour low precision.
* Bet 2: Memory capacity.Match or beat the contemporary NVIDIA flagship on HBM capacity every generation since 2021, and add a 256 MB last-levelInfinity Cachethat absorbs the reuse H100 must hit HBM for.
* Bet 3: Early 3D-stacking.3D-stack compute on cache and I/O before NVIDIA does: TSMCSoIChybrid-bonded XCDs on IODs in 2023, while NVIDIA stayed monolithic until 2025.
* Bet 4: Coherent CPU+GPU.TheMI300AAPU is the most chiplet-aggressive product ever shipped, and theEl Capitandeployment is the proof.
* Bet 5: Open scale-up fabric.UALinkand OCP MX overNVLinkand proprietary FP4.

#### Scaling

The memory bet has a scaling consequence: when 8MI300Xchips hold 1.5 TB of HBM and 8MI350Xchips hold 2.3 TB, you can fit a 405B-parameter model inFP8inside a single 8-GPU box (weights, KV cache, and headroom for longer contexts and bigger batches), where the same model on 8×H100(640 GB) requires careful sharding. For inference workloads through 2024–2025, AMD's scale-up didn't need to match NVL72 at the rack to be competitive at the box. Fortrainingat the frontier, it did, and AMD didn't have an answer until 2026.

Scale-up
Bind GPUs into one coherent memory domain over 
Infinity Fabric
. Through 
MI355X
 this stops at the 8-GPU 
OAM
 box (896 GB/s mesh per GPU). 
Helios
 extends to a 72-GPU rack via 
UALink
, tunnelled over Ethernet at launch (
UALoE
) and native from 2027.

Scale-out
Network those domains over Ethernet. No 
InfiniBand
. 
Pensando
 NICs (
Pollara 400
, 
Vulcano 800
) implement the 
Ultra Ethernet Consortium
's 
UET
 
RDMA
 transport; 
Broadcom Tomahawk 6
 supplies the 
switch ASIC
 and 
CPO
.

##### Scale-up

Through MI355X, AMD's scale-up means an8-GPUOAMplatformoverInfinity Fabric. EachMI300Xhas 7 IF links (one to every peer in the box) at 128 GB/s bidirectional, giving 896 GB/s of per-GPU mesh bandwidth in a fully-connected all-to-all topology.MI350Xbumps each link to 153.6 GB/s (~1,075 GB/s per GPU) but keeps the 8-GPU shape. The platform conforms to OCP's UBB 2.0: the same mechanical socket as an NVIDIA HGX baseboard, so server vendors can ship AMD or NVIDIA on the same chassis without redesigning the system.

What AMD didn't ship through MI355X was a rack-scale equivalent of NVL72. Customers running larger models on MI300X clusters scaled across multiple 8-GPU boxes via Ethernet, paying scale-out latency for what NVIDIA users could keep inside scale-up. This was the gap that mattered for training, and the gap thatHeliosis built to close.

Helios is AMD's first rack-scale scale-up domain, shipping in 2H 2026 alongsideMI455X. 72 GPUs per rack, ~31 TBHBM4, 1.4 PB/s aggregate HBM bandwidth, 2.9 ExaFLOPS FP4 / 1.4 ExaFLOPS FP8, 260 TB/s of scale-up bandwidth, 43 TB/s of scale-out. The form factor isOpen Rack Wide (ORW)(Meta's 2025 OCP submission, double-wide and liquid-cooled), not an AMD-proprietary chassis. Building on Meta's reference design rather than designing a rack from scratch is a deliberate AMD bet: any hyperscaler standardised on ORW can deploy Helios without bespoke datacenter facilities work.

The fabric isUALink: Ultra Accelerator Link, an open consortium standard AMD helped found alongside Apple, AWS, Cisco, Google, HPE, Intel, Meta, Microsoft, and Synopsys. UALink 200G 1.0 (April 2025) defines a 200 GT/s lane and 800 Gbps per direction, with switched topologies scaling to 1,024 accelerators per pod. The promise is a cache-coherent interconnect comparable to NVLink but unowned: any vendor can build a UALink switch, any accelerator can talk UALink, the standard belongs to the consortium rather than to the strongest seller.

The catch:native UALink switching silicon won't ship in volume until 2027. Astera Labs' Scorpio, plus competing parts from Auradine, Enfabrica, and Xconn, are all targeting late-2026 / 2027 deployment. Helios at launch usesUALoE(Infinity Fabric tunnelled over standard Ethernet) as a stopgap, preserving the programming model while waiting for native UALink fabric. Native UALink switching arrives with MI500 in 2027. At launch, Helios is closer to a fast Ethernet-tunnelled coherent cluster than to NVL72's true cache-coherent NVLink domain: a real concession on the timeline, paid in exchange for hitting 2H 2026 with a competitive product.

##### Scale-out

AMD does not shipInfiniBand. The whole scale-out stack is Ethernet, anchored on a different open standard: theUltra Ethernet Consortium (UEC).

UEC 1.0 (released June 2025) definesUltra Ethernet Transport (UET): a new RDMA transport over standard Ethernet, with packet spraying, SACK-based selective retransmit, and modern congestion control. UET is not RoCEv2 (which encapsulates InfiniBand transport in Ethernet frames); it's a clean redesign of RDMA semantics for scale-out AI fabrics. AMD is a founding member alongside Broadcom, Cisco, Meta, and Microsoft. Same play as UALink: own the standard, not the implementation.

The NIC isPensando, the networking startup AMD acquired in 2022.Pollara 400is the current AI NIC: 400 GbE, P4-programmable, UEC-ready, PCIe Gen 5, paired with MI300X / MI355X.Vulcano 800ships in 2026 alongside MI455X: UEC 1.0 compliant, PCIe Gen 6, native UALink interfaces, 8× the per-GPU scale-out bandwidth of Pollara.Salina 400is the front-end DPU (16× Arm Neoverse-N1, dual 400 GbE) for storage / SDN / firewall, equivalent to NVIDIA'sBlueField, distinct from the AI back-end NIC.

The switch silicon, though, isn't AMD's. Helios's 43 TB/s scale-out fabric runs throughBroadcom Tomahawk 6: a 102.4 Tbps Ethernet switch ASIC with co-packaged optics ("Davisson"). AMD has no in-houseCPOand no in-house switch ASIC; the optical layer is partner silicon. NVIDIA owns its entire stack: InfiniBand, Spectrum-X Ethernet, ConnectX, BlueField, Quantum-X Photonics CPO, all in-house. AMD owns one tier (NIC + DPU via Pensando) and bets that open standards plus best-of-breed partner silicon will outpace vertical integration.

The industry has moved AMD's way. Dell'Oro reports Ethernet handled more than twice the AI scale-out fabric volume of InfiniBand in 2025; AWS, Microsoft, Meta, Oracle, and xAI have all standardised on Ethernet for their AMD-based AI clusters. The remaining question isn't whether Ethernet can match InfiniBand on RDMA semantics (UEC closes that gap) but whether Helios can close therack-scalegap with NVL72 fast enough to win frontier training workloads that today default to NVIDIA.

#### Software

ROCmis the open-source counterpoint toCUDA. Where NVIDIA's stack is proprietary and vertically integrated (cuBLAS, cuDNN, TensorRT-LLM ship as binary blobs maintained by NVIDIA alone), ROCm is GitHub-native and bets on open standards (PyTorch, Triton, vLLM, OCP MX) rather than a walled-garden library set. The software gap with NVIDIA is real, but AMD's strategy is to close it through the open community rather than build a parallel CUDA stack from scratch.

The bottom of the stack isHIP, AMD's CUDA-compatible C++ runtime.hipifytranslates CUDA source to HIP automatically. Bulk HPC code (HACC, Laghos, QMCPack) ports at 80–95% out of the box: the CORAL-2 number. Modern AI kernels port worse: anything that reaches for Hopper- or Blackwell-specific primitives (TMAdescriptors,wgmma,tcgen05.mma) has no clean ROCm analog and has to be rewritten by hand.

Above HIP sits a library tier structured to mirror NVIDIA's, one-to-one by name:rocBLASfor cuBLAS;hipBLASLtfor cuBLASLt;MIOpenfor cuDNN;RCCLfor NCCL;Composable Kernel(and its modernck-tileDSL) for CUTLASS; rocprofv3 / rocprof-sys / rocprof-compute for the Nsight family. There is no first-party analog of TensorRT-LLM, though. AMD's answer is to backvLLMas the open-source serving engine and ship AMD-specific operators (AITER) that plug into it; the dedicated ROCm CI for vLLM took test-pass rate from 37% to 93% across early 2026.

The PyTorch path is first-class. Eager-mode PyTorch has run on ROCm since 2018;torch.compilelowers through Triton, and Triton's ROCm backend (withAOTritonfor ahead-of-time math kernels) is upstream. There is no XLA-style intermediate IR; ROCm compiles direct to HIP / Triton / CK. As Triton becomes the default kernel path in PyTorch, much of the porting cost evaporates: a kernel that runs throughtorch.compileworks on both CUDA and ROCm without source change. This is the architectural bet beneath AMD's open strategy: Triton's Python DSL becomes the cross-vendor lingua franca that sidesteps the need for a CUDA-equivalent kernel ecosystem.

FlashAttentionis the load-bearing case.FA2is production on MI300X via Composable Kernel; PyTorch defaults to CK or AOTriton on ROCm.FA3(Hopper-tuned) is partially supported via AITER + CK, but Dao-AILab's canonical implementation remains CUDA-only.FA4(Blackwell, March 2026) has no ROCm port at all.HipKittens, Hazy Research's MI355X port of ThunderKittens (November 2025), claims forward-pass parity with hand-tuned AITER in ~500 lines. The pattern: open-source academic kernels close the AMD tail months after NVIDIA's, not years.

Production deployment has validated the strategy. Microsoft Azure'sND MI300X v5instances went GA in May 2024; OpenAI runs GPT inference on them. Meta ships Llama 3 / Llama 4 inference on MI300X via the Grand Teton platform. Oracle OCI'sBM.GPU.MI300X.8went GA in September 2024, with MI355X following in 2026. These are real serving fleets at hyperscaler scale, not pilots.

The honest gap is still real. Independent benchmarks (Phoronix, March 2026) put ROCm 7.2 at10–25% slower than equivalent CUDAon standard PyTorch / vLLM / SGLang workloads, at equivalent precision on equivalent silicon. ROCm 7 reachedfeature paritybut notperf parity. The FlashAttention-4 tail (research code that exploits Blackwell's newest primitives) is where NVIDIA's moat remains most durable; it has no clean ROCm analog and waits for a hand-written AITER kernel or HipKittens-class community port. NVIDIA ships engineers inside frontier labs; AMD ships kernels through GitHub. The strategies converge on common workloads (Llama inference, attention, dense transformer training) but the long tail of novel research code still costs MI300X / MI355X deployments engineering time NVIDIA users don't pay.

### Cerebras WSE

Cerebrasbuilds thelargest chip ever shipped. The philosophy: thememory wallis a consequence of cutting the wafer. A fab prints dozens of dies onto 300 mm of silicon and saws them apart; the industry then spends its most exotic engineering (HBM,NVLink,CoWoS, 5,184 copper cables per rack) wiring the pieces back together at a small fraction of on-die bandwidth. Cerebras skips the saw. TheWafer-Scale Engineis one piece of silicon: 84reticle fields, 46,225 mm², 900,000 dataflow cores, and every byte of on-chip memory inSRAMone cycle from a compute unit.

#### Genealogy

2019
WSE-1
CS-1
First shipped wafer-scale processor: 1.2T transistors, 400,000 cores, 18 GB on-wafer SRAM.

2021
WSE-2
CS-2
7 nm: 850,000 cores, 40 GB SRAM. 
Weight streaming
 moves weights off-wafer into 
MemoryX
.

2023
Condor Galaxy
CG-1
64-system clusters built with 
G42
; trained the 
Jais
 Arabic LLM family.

2024
WSE-3
CS-3
5 nm: 4T transistors, 900,000 cores, 44 GB SRAM; per-core FP16 SIMD doubled to 8-wide; clusters specified to 2,048 systems.

2024
Inference
Weights parked in SRAM instead of streamed: the fastest independently measured decode in the industry, and the pivot that now defines the company.

#### Architecture

A GPU is a hierarchy: threads insidewarpsinside SMs, dies inside packages inside racks, each boundary with its own bandwidth, its own latency, its own programming construct; every accelerator built from dies inherits some version of it. The WSE is aflat plane: 900,000 identical cores tiled edge-to-edge in a 2D mesh, with no shared cache, no global memory, and no boundary of any kind between one core and the other 899,999. Each core is tiny, ~38,000 µm² onWSE-2, roughly half SRAM and half logic, peaking at 30 mW: 48 kB of local SRAM, sixteen general-purpose registers, a six-stage pipeline, a 4-wide FP16FMACSIMD (8-wide onWSE-3), and a five-port router into the fabric. Execution isdataflow: a core sits idle until awaveletarrives, control bits in the wavelet select which handler task fires, and eight hardwaremicrothreadsswitch cycle-by-cycle as tensor operands arrive and drain. No warps, nowarp schedulers, no caches to miss, no reorder buffer:the arrival of data is the schedule.

##### The Wafer

A stepper exposes a wafer onereticleat a time, ~850 mm² per shot, which is why every conventional chip lives under that ceiling (and why B200 becametwo diesthe moment NVIDIA pressed against it). Cerebras prints the same ~550 mm² die 84 times in a 12×7 grid, like any other customer of TSMC, and then, in a process co-developed with TSMC, lays extra high-level metal across the <1 mmscribe lineswhere the saw would normally run. The mesh crosses each seam on a source-synchronous parallel interface (2,880 GB/s per die on WSE-3), and the entire inter-die layer costs ~97 W. To software the seams do not exist: one uniform mesh, one chip.

Wafer-scale has been tried before and it failed on yield: a single defect in a monolithic wafer-computer kills the whole wafer, which is what buriedthe ideain the 1980s. Cerebras's answer is granularity. A defect on an H100 disables an entire ~6 mm² SM; the same defect on a WSE disables one 0.05 mm² core. WSE-3 fabricates ~970,000 cores and ships 900,000: the ~7% spare pool, plus redundant fabric links, lets the hardware remap around every defect and restore a full logical mesh.

##### The Core

The unusual part of the core is not the datapath; it is what an instructionis. Alongside the sixteen general-purpose registers sit44data-structure registers(DSRs), each holding a tensor descriptor:base address,extent, andstride, up to four dimensions. Instructions name their operands by DSR, so a single FMAC instruction saysmultiply the arriving stream against this resident tensor and accumulate into that one, and the hardware streams elements for as long as the tensor lasts. There is no software loop around the multiply and no instruction fetch per element; the loop lives in the descriptor. NVIDIA spent five Tensor Core generations walking the matmul toward a singledescriptor-driven command; on a WSE core, a tensor instruction has no other form.

Sequencing is the fabric's job. Acoloris a statically routed virtual channel with a handler task bound to it at compile time, so sending a wavelet on a colorisinvoking code on the destination core: the 16 control bits are the call, the 16 data bits the argument. Thetask schedulerholds the in-flight tensor operations on the core's eight microthreads and switches among them every cycle by operand availability. It is the same stall-hiding job awarp schedulerdoes with 64 resident warps, done with eight contexts, because the latency being hidden is a busy SRAM bank or a neighbour hop, not an HBM round trip.

The 48 kB of local SRAM is organised for the datapath rather than for locality: eight single-ported 6 kB banks deliver two 64-bit reads and one 64-bit write every cycle, exactly two 4-element FP16 operands in and one result out, the width of the WSE-2 FMAC. A 256-byte software-managed cache (512 B on WSE-3) keeps the hottest values beside the pipeline. This is the machine's thesis in miniature: per core, memory bandwidth and compute are matched exactly, and the wafer inherits that balance 900,000 times over.

##### Compute

There is no matrix unit on the wafer. NVIDIA, Google, and AMD all concentrate their FLOPs in a dedicated matmul engine (Tensor Core,MXU,Matrix Core) and differ mainly in how that engine is fed; Cerebras assembles matmul out of the fabric. A GEMM runs as a wafer-wide choreography: each arriving weight is broadcast along a row of cores holding activations, every core fires a multiply-accumulate against its resident slice (anAXPYper weight), and partial sums reduce across the mesh. The data reuse a Tensor Core gets from a register tile and an MXU gets from its wiring, the WSE gets from geometry: activations never move, so the only operand in flight is the one being multiplied.

The FLOPs ledger needs care, because the number Cerebras prints is not the number to compare. WSE-3's headline125 PFLOPS is sparse FP16: it assumes the hardware's roughly 8× zero-skipping payoff on ideally sparse tensors. Dense is roughly15.8 PFLOPS FP16(derived: 900,000 cores × 8-wide FMAC × 1.1 GHz; Cerebras publishes no official dense figure). That is real compute, but it is not the point: per watt, dense FLOPs on the wafer lose to every contemporary GPU. The wafer was never a FLOPs machine. It is abandwidth machine, and the FLOPs exist to keep up with the SRAM.

Zero-skipping is where dataflow earns its keep. Because computation is triggered by arriving data, a zero never triggers anything:zeros are filtered at the sender, and the receiving core never sees them and never spends the cycle. This is unstructured, element-granular sparsity, the general case that NVIDIA's 2:4structured sparsityonly samples. It is also, so far, an unexercised option. Cerebras's own sparse-pretraining results (SPDF: 75% sparsity at 1.3B parameters; a follow-up at 6.7B) are vendor-authored and sub-7B, and no flagship customer model has been disclosed as sparse-trained:Jais 2, the biggest run on the hardware, is dense. The only silicon that can harvest unstructured sparsity has yet to ship a headline model that uses it.

##### Memory

The hierarchy is one tier:44 GB of SRAM in 48 kB slices inside the cores, and nothing else on the wafer. No HBM, no L2, no eviction policy; every byte is one cycle from an FMAC. The quoted bandwidth is 21 PB/s, and the number deserves its flag: it is thesumof 900,000 local SRAM ports, an on-wafer aggregate, not a point-to-point link, and not comparable to an HBM figure. The honest comparison is bytes per FLOP: the wafer can feed ~1.3 bytes per dense FP16 FLOP, where aB200gets ~0.002 from HBM. On that axis every GPU and TPU is starved; the WSE is the only machine in balance.Decode, the phase that is a pure bandwidth problem (one full read of the weights per token), is the phase the wafer turns out to be shaped for.

The other side of the tier is the edge of it. The wafer's connection to everything else is 12×100 GbE:1.2 Tb/s, barely more than the singleConnectX-8NIC attached to one Blackwell GPU. Between on-wafer SRAM and off-wafer Ethernet sitfive orders of magnitude. NVIDIA's hierarchy descends gradually, each tier a few times slower than the last; the WSE has two tiers with a cliff between them. The wafer is an island, and the island's superpower and its cage are the same fact.

And the island is not growing. SRAM density has effectively stopped scaling on leading nodes: WSE-3 carries just 10% more SRAM than WSE-2 despite a full node shrink and a 54% jump in transistor count. Logic keeps shrinking; the six-transistor SRAM cell does not. The architecture's scarcest resource is the one thing the next process node no longer buys.

##### Weight Streaming

Training on the wafer inverts the flow everyone else takes for granted: on a GPU or TPU, weights are resident and activations stream through; on a WSE,activations are resident and weights stream through. Master weights live inMemoryX, a DRAM-and-flash appliance beside the cluster. Layer by layer, weights stream across the wafer, trigger multiply-accumulates against the activations pinned in SRAM, and leave; gradients stream back out on the backward pass, and the optimizer step runs inside MemoryX on CPUs (a weight update is O(parameters) of element-wise work with no reuse, so CPU-class compute keeps pace). The wafer never stores weights, "not even temporarily" (Cerebras's phrase). Model size is bounded by MemoryX, not by the 44 GB; the 44 GB bounds activations and batch.

What this buys is the programming model. One wafer holds a full layer's activations, so there is notensor parallelism, nopipeline parallelism, noFSDPsharding: a 70B model is written as a single-device program, and multi-system scaling ispuredata parallelismthroughSwarmX, a broadcast/reduce tree that fans one weight stream out to N wafers and sums their gradients on the way home. The parallelism-strategy spreadsheet that dominates GPU training simply has no Cerebras page.

What it costs is scale, in the market's own revealed preference. The spec sheet says 2,048 CS-3s; the largest cluster ever disclosed is 64 (Condor Galaxy 3). The largest from-scratch model ever disclosed on the platform isJais 2 at 70B parameters and 2.6T tokens, trained by anchor customerG42with Cerebras engineers embedded. Nothing above 70B, from anyone, in the seven years since CS-1. And utilisation (MFU), the number GPU labs publish as a matter of course at 35–45%, has never been disclosed for any Cerebras run.

##### Numerics

The numerics fit in a sentence:FP16 and BF16 with FP32 accumulate, plus (from WSE-3) a 16-wide 8-bit integer path that the Hot Chips disclosure labels fixed-point. No FP8, no FP4, no microscaling. While every other vendor halves precision each generation and buys the accuracy back with block scaling, Cerebras still computes in 16-bit and markets it as a quality differentiator ("the original 16-bit weights"). The tension is obvious: SRAM capacity is the architecture's scarcest resource, and 8-bit weights would halve the number of wafers a model needs. Whether 16-bit-only is numerical conviction or a datapath roadmap gap is an open question; no primary Cerebras source shows floating-point 8 anywhere on the wafer.

##### Bets

* Bet 1: Don't cut the wafer.The die boundary is the tax the rest of the industry pays: SerDes, interposers, HBM stacks, cables, switches. Stitch 84 reticle fields in metal and the highest-bandwidth boundary in rival systems does not exist at all.
* Bet 2: SRAM is the only memory.Trade capacity for bandwidth at the steepest ratio in the industry: 44 GB at an on-wafer aggregate 21 PB/s. Balance the machine instead of hiding imbalance behind a hierarchy.
* Bet 3: Dataflow cores, no matrix unit.900,000 tiny cores triggered by arriving wavelets, with matmul assembled from broadcast, FMAC, and mesh reduction: skipping a zero is free rather than a special mode.
* Bet 4: Weights move, activations stay.Weight streaming decouples model size (MemoryX) from wafer memory (44 GB) and collapses cluster scaling to pure data parallelism.
* Bet 5: Sell latency, not throughput.The wafer re-reads an entire model per token faster than anything built on HBM; price that speed as a premium product instead of competing on cost per token.

#### Scaling

Scale-up and scale-out mean something different here. NVIDIA's scale-up problem (make 72 packages behave like one device) is solved on the WSE by lithography: the coherent domain ships from the fab in one piece. What remains is everything past the wafer's edge, and no other machine hits its edge as hard or as early.

Scale-up
The wafer. 900,000 cores on one 2D mesh: 32-bit links, single-cycle hops, statically routed over 24 
colors
, native broadcast, 214 Pbit/s aggregate fabric bandwidth. Fixed at 46,225 mm² by the size of a 300 mm wafer.

Scale-out
Ethernet, immediately: 12×100 GbE (1.2 Tb/s) per system. Training scales through 
SwarmX
 (data-parallel broadcast/reduce over 
RoCE
); inference shards models across systems at layer boundaries, pipeline-parallel.

##### Scale-up

The wafer's internal fabric has noSerDes, no cables, no transceivers, and no marginal cost per link: routing is compiled, each hop is one cycle, and a broadcast is a native fabric primitive rather than a switch feature. Where NVL72 spends 5,184 copper cables and a tray ofNVSwitchASICs to give 72 GPUs 130 TB/s of all-to-all, the WSE's equivalent domain is a single lithographic object. The catch is that the domain size is a constant. NVIDIA's scale-up domain grows every generation (NVL72 to NVL576 across three years); the wafer has been 46,225 mm² since 2019 and will stay there. 300 mm is the largest wafer the industry runs (the 450 mm transition died a decade ago), so Cerebras's scale-up roadmap is whatever the next node yields in density: there is no more area to be had.

##### Scale-out

Training scale-out isSwarmX, and it only does one thing: replicate. Broadcast the weight stream to N wafers, reduce their gradients on the return path; batch grows with system count, model size does not. The claimed ceiling of 2,048 systems ("256 exaFLOPS", sparse) has never been built; 64 has.

Inference abandons weight streaming entirely; the arithmetic is fatal. Streaming a 70B model's 140 GB from MemoryX for every decoded token over a ~150 GB/s pipe would cost roughly a second per token. So inferenceparks the weights in SRAMand shards the model across wafers at layer boundaries: Llama 70B on "as few as four" CS-3s, pipeline-parallel over Ethernet, each additional wafer contributing 44 GB of weight-plus-KVcapacity and 23 kW of load.

The speeds are real, and independently verified.Artificial Analysismeasured 1,850 tokens/s on Llama 3.1 8B and 446 on 70B at the August 2024 launch, 969 on Llama 405B (240 ms to first token), and 2,522 on Llama 4 Maverick in 2025, ~2.4× the best published Blackwell number of the time. Vendor-quoted peaks run higher (2,100 on 70B withspeculative decoding; 3,000 on GPT-OSS-120B, where the live independent measurement sits nearer 2,000). No GPU provider comes close on per-user decode speed.

The economics are the sharp edge. Forty-four GB per wafer means a frontier-scale model consumes fleets:SemiAnalysisestimates ~24 CS-3s for a 1.6T-parameter-class model that fits in a handful of GPU racks, each system an analyst-estimated ~$450k bill of materials selling at a list price around $2–3M (never officially disclosed). During decode the wafer's enormous FLOPs mostly idle; Cerebras has declined to disclose batch sizes and has never published per-system throughput. Per-token API pricing runs roughly 3–5× GPU-based providers for the same open models, and Llama 405B was quietly dropped from the API, which SemiAnalysis reads as serving economics that didn't clear. Fixed SRAM also prices context: KV cache lives in the same 44 GB as weights, so long contexts steal capacity and force more systems per replica; the API caps at 131K tokens while frontier providers serve 256K–1M.MoEis served (Qwen3-235B at ~1,500 tokens/s, vendor-quoted) but is the format's worst case: a huge parameter footprint touched a few experts at a time, held in the most expensive memory.

The market has priced this honestly. Mistral's Le Chat (~1,100 tokens/s), Perplexity Sonar, and Meta's Llama API all pay for the latency; in January 2026 OpenAI signed for750 MW of CS-3 capacity through 2028,reported above $10Bat signing andsince grown past $20B, the largest endorsement wafer-scale has ever received. The first flagship to ship on that capacity isGPT-5.6 Sol, launched July 2026 at a quoted 750 tokens/s.

#### Software

The stack is compiler-driven like the TPU's, but through a much narrower aperture: the Cerebras compiler is akernel matcher, not a general code generator.cerebras.pytorchtraces the training step through lazy tensors into Torch-MLIR and a graph IR, then matches subgraphs against a library of hand-written kernels, falling back to slower auto-generated ones for ops with no match. Thedocumented constraintsare stark by GPU standards: static graphs only, no dynamic shapes, no data-dependent control flow, no eager tensor access mid-step, and a PyTorch version pinned behind upstream. The best independent practitioner account (SURF, the Dutch national compute centre) reports unsupported layer types and no 1:1 porting path for standard PyTorch code.

And there is no kernel escape hatch. CUDA's answer to a novel attention variant iswrite a kernel; the TPU's isPallas; ROCm's isTriton. The Cerebras ML stack has no user kernel path at all: when the matcher misses badly, the fix is a Cerebras engineer. A separate SDK language,CSL, exposes the raw machine (tasks, wavelets, colors) and has produced striking HPC results (aTotalEnergies stencil codeat ~228× an A100, a Gordon Bell finalist on 48 CS-2s), but it is a separate world, unconnected to the PyTorch flow. Every flagship model on the platform (Jais, BTLM, Med42) was co-developed with embedded Cerebras staff.

There is a strange immunity in this.FlashAttention, the defining kernel lineage of the GPU era, is a scheme for tiling attention through a memory hierarchy, and the WSE has no hierarchy to tile against: the optimisation class that costs AMD years of porting lag simply does not apply. But the immunity and the poverty are the same fact. The third-party kernel ecosystem that compounds on CUDA has no surface to attach to here; every kernel improvement in the platform's history has one author.

Where does that leave the wafer? Owning a real niche, honestly won: batch-one decode speed, independently verified, paid for by customers who price latency above cost. Around the niche, hard walls: 3–5× per-token pricing, a 70B training ceiling seven years in, revenue still ~86% concentrated in two Abu-Dhabi-linked customers in 2025 (per the S-1 filings around its May 2026 IPO), and a scarcest resource, SRAM density, that stopped scaling just as models kept growing. Hennessy and Patterson promised a Cambrian explosion; the WSE is its most extreme body plan, the one that decided the memory wall was a packaging choice and spent 46,225 mm² of silicon refusing to make it.

### AWS Trainium

Annapurna Labs, the team behind AWS'sNitrocards andGravitonCPUs, builtTrainiumas afast-follower. The compute core takes the TPU's proven playbook (a 128×128weight-stationarysystolic array, software-managed scratchpads, whole-program compilation) down to sharing Google'sXLAcompiler outright. The scale-out fabric is theNitro-offloaded network that already carries the rest of AWS. What is genuinely Amazon's is narrow and deliberate: dedicated collective-communication silicon bolted onto the borrowed core, and the vertical integration to price a chip that only has to beat NVIDIAinside AWS.

#### Genealogy

2015
Annapurna Labs
Amazon acquires the Israeli chip startup for ~$350M; it becomes AWS's in-house silicon team.

2018
Graviton
 + 
Nitro
Arm server CPUs and the 
DPU
 offload fabric.

2019
Inferentia
NeuronCore-v1
First AWS ML chip, inference-only: 4 NeuronCores, 8 GB DRAM, three fixed engines.

2022
Trainium1
Trn1
, 
v2
First training chip: 2 NeuronCore-v2, a programmable 
GPSIMD
 engine, 32 GB HBM, NeuronLink 2D torus.

2023
Inferentia2
v2
Shares NeuronCore-v2 with Trn1: the inference and training lineages converge on one microarchitecture.

2024
Trainium2
Trn2
, 
v3
8 NeuronCore-v3, first real 
FP8
 acceleration, 96 GB 
HBM3
; the 64-chip 
UltraServer
. Powers 
Project Rainier
.

2025
Trainium3
Trn3
, 
v4
First 3 nm AWS chip (TSMC N3P); OCP 
MXFP8/MXFP4
; the 
NeuronSwitch
 all-to-all fabric replaces the torus. 144-chip UltraServer.

#### Architecture

The other captive-silicon story belongs to Google, and Trainium is best read as the TPU's thesis rebuilt inside a different cloud. The bets underneath are the same (asystolic arrayfed from software-managedSRAM, scheduled ahead of time by a compiler, with no caches and no thread scheduler), but the unit is assembled differently. A Trainium chip carries asmallnumber ofNeuronCores(2 onTrn1, 8 onTrn2andTrn3), and each NeuronCore is not one monolithic matmul engine but acluster of decoupled, specialised engines: aTensor Engine(the 128×128 systolic array), aVector Enginefor reductions, aScalar Enginefor pointwise math, and a programmableGPSIMD Engineof eight 512-bit vector processors for whatever fits none of the other three. Around them sit the data-movers: 128DMA engines, aSync Enginethat sequences transfers, and (from Trn2) dedicatedCC-Coresfor collectives. There are no warps and no wavefronts; the engines run as a statically-scheduled dataflow pipeline, and the load-bearing design decisions are about what surrounds the systolic array, not the array itself.

##### Compute

TheTensor Engineowns the matmul FLOPs; the other three engines own everything else. It is a 128×128 grid of processing elements (16,384MACs) runweight-stationary: one operand tile is loaded into the array and held in place (LoadStationary), the other streams through it (MultiplyMoving), and partial sums land inPSUM, a small accumulator SRAM the engine can read-add-write so a contraction longer than 128 folds into place along theKKKaxis. This is the sameD=A⋅B+CD = A \cdot B + CD=A⋅B+CtileMMAat the heart of every matmul accelerator; but where NVIDIA wraps it in the warp hierarchy and Google issues it from aVLIWbundle, Trainium exposes it as a pair of explicit instructions against a named scratchpad.

The array is physically fixed at 128×128 across all three generations; what changes is how many products it packs per cell.Trn1's NeuronCore-v2 ranBF16/FP16 withFP32accumulate and offeredFP8only at the BF16 rate (no speedup).Trn2's v3 double-pumps FP8 to present an effective 256×128 array, the first Trainium with a real 2× on 8-bit.Trn3's v4 packsmicroscalingoperands to present an effective 512×128 at 4× the BF16 rate. The count of physical multiply-add cells never moves; the datapath just feeds them narrower numbers.

The other three engines are what keep the array busy. TheVector Enginehandles cross-element reductions (layernorm, softmax, pooling); theScalar Enginehandles one-in-one-out pointwise ops (activations, GELU); theGPSIMD Engine, eight fully-programmable vector processors running C, absorbs anything that maps to none of them. A well-compiled step overlaps all four: the Tensor Engine grinds a matmul while the Vector Engine runs the previous tile's softmax and the DMA engines stage the next, the same producer/consumer overlap that makes TPU and GPU attention kernels efficient, expressed here as separate physical engines rather than separate warps or VLIW slots. The design pays off when a layer decomposes cleanly onto the four engine types, which transformers largely do. It pays a tax at the edges: an operator that fits none of the specialised engines falls to the programmableGPSIMDpath, slower, and the part of the machine most likely to bottleneck a novel architecture. It is Trainium's version of the long-tail cost every non-GPU accelerator carries.

##### Memory

The memory hierarchy is the compute philosophy applied to storage:three tiers, all software-managed, no hardware cache anywhere. AWS's own documentation draws the contrast, noting that unlike a CPU or GPU the NeuronCore has no cache and that "all memory movement is explicit in the program itself." Off-chip isHBM(32 GB on Trn1, 96 GBHBM3on Trn2, 144 GBHBM3eon Trn3). On-chip, closest to the engines, is theState Buffer (SBUF): the main scratchpad, roughly 20× HBM bandwidth, organised in 128 partitions and sized per NeuronCore at 24 MiB (v2), 28 MiB (v3), 32 MiB (v4). Between the array and SBUF sitsPSUM, a 2 MiB accumulator dedicated to matmul outputs. Data moves HBM → SBUF → Tensor Engine → PSUM → SBUF, every hop issued by the compiler; nothing is prefetched or evicted by hardware.

This is exactly Google'sVMEMbet, an explicit scratchpad the compiler must schedule perfectly with no cache to paper over a mistake, and the opposite of NVIDIA's hardware-managedL2andL1. Trainium inherits both the ceiling and the fragility that come with it: when the schedule is right the engines never stall, and when it is wrong there is no fallback path. The design runs a generousHBMbudget against modest peak FLOPs, so per unit of compute Trainium carries more memory than a comparable NVIDIA part. Onabsolutecapacity, though, it trails: Trn2's 96 GB sits below theH200andB200, and Trn3's 144 GB (2025) sits below the 192 GBB200and 288 GBB300it ships against. So the lever AWS actually pulls when it argues the economics of serving a large model is not memory leadership butprice: cost per unit of compute and HBM, on silicon it builds and rents itself.

##### Numerics

Trainium tracks the same precision-halving curve as everyone else (FP32 → BF16 → FP8 → FP4), with two Trainium-specific wrinkles. The first isconfigurable FP8: rather than fixE4M3andE5M2like Hopper, the Tensor Engine takes an adjustable exponent bias and supports E5M2, E4M3, and E3M4, letting the compiler trade range for precision per tensor. The second is thatTrn3'sFP4buysno extra throughput: OCPMXFP4operands are up-converted to MXFP8 before they reach the array, so FP4 runs at the FP8 rate and saves only memory and bandwidth, not compute. Both generations lean on the industry's accuracy-recovery tricks:microscalingblock exponents from Trn3, and hardwarestochastic roundingon every generation. The one figure to distrust is the sparse peak: AWS headlines a 4× FP8 number that its own architecture pages put at 2× over dense FP8 (the 4× is relative to dense BF16), so the marketed acceleration and the datapath do not quite agree.

##### Collectives in Silicon

The block with no clean analogue on a GPU is thecollective-communication core. Distributed training and inference spend a large fraction of their wall-clock incollectives: every gradient step is anall-reduce, everyMoElayer anall-to-all. On a GPU those collectives run asNCCLkernels on the same SMs doing the math, so communication and compute contend for the same silicon and the overlap has to be won in software. Trainium carves the function out into dedicated hardware: 20CC-Coresper Trn2 chip, wired straight to theNeuronLinkports, executing all-reduce, all-gather, reduce-scatter, and all-to-all while the Tensor and Vector engines keep running. It is the same move Google made withSparseCoreand Cerebras made with its off-core zero filter: find a workload the main engine is the wrong shape for, and spend a little area on a purpose-built block beside it rather than steal cycles from the core. Communication becomes something the chip doesconcurrently, not something it pauses to do.

##### Bets

* Bet 1: The cloud is the product, the chip is a component.Annapurna designs chip, server, rack,Nitronetwork, and cloud API as one stack, so Trainium only has to win on price-performance inside AWS, never on a merchant-silicon spec sheet.
* Bet 2: Borrow the compute thesis, don't reinvent it.A 128×128weight-stationaryarray, software-managedSBUF/PSUMscratchpads, and whole-program compilation are the TPU's bets, reused down to sharing Google'sOpenXLA. The effort saved goes into the network and the rack.
* Bet 3: Collectives belong in silicon.DedicatedCC-Coresoverlapall-reduceandall-to-allwith compute in hardware, instead of running them as kernels that steal FLOPs from the matmul units.
* Bet 4: Reuse the cloud's own network.Scale-out isEFAwith theSRDtransport: the sameNitro-offloaded, packet-sprayedRDMAthat already runs the rest of AWS. NoInfiniBand.
* Bet 5: Move the topology to the workload.Trn1 and Trn2 copied the TPU'storus; Trn3'sNeuronSwitchreplaces it with a switchedall-to-allfabric asMoEtraffic outgrew nearest-neighbour. Honestly, this is following the playbook: first Google's, now NVIDIA's.

#### Scaling

Trainium's scaling inherits its split from the rest of AWS: a tightly-coupledNeuronLinkdomain for the chips that must act as one, and the cloud's general-purposeEFAfabric for everything beyond it. The scale-up domain is not cache-coherent shared memory the wayNVLinkis; AWS markets theUltraServeras a pooled multi-terabyte memory, but underneath it is message-passing over point-to-point links, closer in spirit to the TPU'sICIthan to anNVSwitchcrossbar.

Scale-up
NeuronLink
 binds chips into one 
UltraServer
. Through Trn2 the topology is a 
torus
 (16 chips per instance in a 4×4 2D torus, 64 per UltraServer in a 4×4×4 3D torus); Trn3 replaces it with the 
NeuronSwitch
 all-to-all fabric. Message-passing, not coherent load/store.

Scale-out
Elastic Fabric Adapter
 over Ethernet, offloaded to 
Nitro
. The 
SRD
 transport sprays each flow across many paths and delivers reliably but out-of-order; 
UltraClusters
 reach hundreds of thousands of chips over the 
10p10u
 fabric.

##### Scale-up

NeuronLink is Trainium's chip-to-chip fabric, the roleNVLinkplays for NVIDIA andICIfor the TPU. Through Trn2 it wires chips into atorus, exactly the TPU's choice: a singletrn2instance is 16 chips in a 4×4 2D torus at ~1.28 TB/s per chip, and theTrn2 UltraServerjoins four instances into 64 chips on a 4×4×4 3D torus, presenting 83 denseFP8PetaFLOPS and ~6 TB ofHBMas one scale-up domain. The third torus axis is deliberately thin (the inter-instance ring runs at ~256 GB/s per chip against 1.28 TB/s inside an instance), which is the torus's characteristic trade: cheap wiring and huge nearest-neighbour bandwidth, at the cost of many hops across the diameter. AWS positions the 64-chip UltraServer against NVIDIA's 72-GPUNVL72; the aggregate compute is in the same league, but a torus is not acrossbar, and the two behave very differently on traffic that is not nearest-neighbour.

That trade is why Trn3 abandons the torus.NeuronSwitch-v1is a switchedall-to-allfabric that roughly doubles inter-chip bandwidth and, more importantly, flattens the diameter so any chip reaches any other in one switched hop. The Trn3 UltraServer scales to 144 chips for 362 dense FP8 PetaFLOPS and 20.7 TB ofHBM3e. The motivation is the one that also pushed Google toward high-radix topologies forMoEinference:expert routingis all-to-all, the worst case for a torus, and a switch turns the longest-hop pair into a single crossing. Trainium's interconnect roadmap is a compressed re-run of the industry's: adopt the torus while the workload is nearest-neighbour, switch to a crossbar when it is not.

##### Scale-out

Scale-out is not bespoke; it is the same fabric AWS already runs. Every Trainium instance carries anElastic Fabric AdapterNICinto the datacenter network (3.2 Tbps per Trn2 instance), and the transport isSRD (Scalable Reliable Datagram), offloaded to theNitrocards rather than run on the accelerator. SRD is AWS's clean-sheet answer toRDMA: instead of the single ordered flow ofRoCEorInfiniBand, it sprays each message across up to 64 parallel paths and delivers reliably but out-of-order, pushing reassembly up to the collective library and sidestepping the head-of-line blocking a single congested path would cause. It is the transport AWS built for its cloud generally, repurposed for the accelerator fabric.

At the top of the hierarchy is theUltraCluster, stitched together by the10p10unetwork (AWS's shorthand for ~10 petabits/s of bandwidth at under 10 microseconds of latency across a datacenter) and scaling to hundreds of thousands of chips. The proof point isProject Rainier: roughly half a million Trainium2 chips across multiple US datacenters, brought online forAnthropicin late 2025; by early 2026 Claude was running on over a million chips, the largest commitment any external lab has made to a non-NVIDIA training platform. It exists because the economics close end to end. AWS claims Trainium2 delivers 30–40% better price-performance than itsHopper-class GPU instances (an AWS figure, measured against last-generation NVIDIA rather thanBlackwell), and because Amazon owns every layer from theNitrocard to the API, that margin is Amazon's to set.

#### Software

Trainium's software makes the borrowing explicit: theNeuron SDKis acompiler-first stack built on the sameOpenXLAfoundation as the TPU. The Neuron compiler (neuronx-cc) ingestsXLA HLOgraphs and lowers them to aNEFFbinary that the Neuron runtime loads onto the NeuronCores; the front-end IR is Google's, and Google's own OpenXLA announcements list Trainium as a first-classPJRTdevice alongside the TPU.torch-neuronxruns PyTorch throughPyTorch/XLA'sLazyTensortracing (record ops, compile the graph at a step boundary), andjax-neuronxlowers JAX throughStableHLO. On the spectrum from kernel-drivenCUDAat one pole to whole-programXLAat the other, Trainium sits almost on top of the TPU: the compiler is the system, and it is largely the same compiler.

Where it diverges is the escape hatch. XLA alone cannot always synthesise the optimum for a novel attention variant or a fused MoE dispatch, so Neuron shipsNKI (Neuron Kernel Interface), a Python, tile-level kernel language that exposes the four engines and theSBUF/PSUMscratchpads directly. It is Trainium'sPallas(or itsTriton): the same idea of a tile DSL that drops beneath the whole-program compiler when a kernel's win is in theschedule, not the algebra. Below it, acollective-communication librarymapsall-reduceandall-to-allonto theCC-Coresand the NeuronLink topology (theNCCLanalogue), andNeuronX Distributedprovides the sharded-training layer.

The gap to CUDA (and even to the TPU's stack) is maturity, not design. NKI, the JAX path, and the distributed library were all still in beta through late 2024; a ported model runs only on AWS, with no cross-vendor fallback; and thevLLMbackend trails the upstream project. The clearest tell is how the anchor tenant works:Anthropicdoes not simply target Trainium through PyTorch, it embeds with Annapurna, writes its own low-levelNKIkernels, and upstreams fixes into the Neuron stack. Trainium is production-viable at the frontier, but at the frontier it is co-engineered, not turnkey: the compiler is inherited and excellent, but the surrounding ecosystem is young.

### Groq LPU

TheGroqLPUis adeterministicmachine. Every other chip spends silicon tolerating uncertainty: caches to hide memory latency, schedulers to fill stalls, arbiters to resolve contention it cannot predict. The LPU deletes all of it. Strip out everyreactivecomponent (no cache, no branch predictor, no arbiter, no reorder buffer, not even an on-chip crossbar) and hand the entire scheduling problem to the compiler, which places every instruction and every byte on an exact cycle. What is left is a chip whose latency is known before it runs. Where theTPUmoved scheduling into the compiler but keptHBMand a dynamic network, Groq removed the last sources of nondeterminism: memory is allSRAM, and the network is scheduled too, so hundreds of chips run as one clock-exact program.

#### Genealogy

2016
Founding
Jonathan Ross
, who started Google's 
TPU
 as a 20% project, leaves to build a deterministic inference chip.

2020
TSP
GroqChip 1
First silicon (
ISCA
 2020, 
Think Fast
): a single 
functional-slice
 core, 14 nm, no 
HBM
, no caches.

2022
Multiprocessor
ISCA
 2022: 
software-scheduled networking
 extends the deterministic schedule across thousands of chips via a compiled 
Dragonfly
.

2023
Samsung 4 nm
Second-gen LPU announced on Samsung 
SF4X
; it never shipped (a reported failed tapeout).

2024
LPU / GroqCloud
The TSP is rebranded the 
Language Processing Unit
; the company pivots from selling cards to selling tokens, on record decode speeds.

2025
NVIDIA License
NVIDIA takes a 
non-exclusive license
 to the LPU technology and hires Ross and much of the team.

2026
NVIDIA Groq 3 LPU
LP30 / LPX
The technology reappears at 
GTC
 2026 as a latency co-processor beside 
Rubin
 NVL72, via 
Attention-FFN disaggregation
.

#### Architecture

The rest of the field is built from areplicated core: tile oneSM,TensorCore,CU, or dataflow core across the die and farm work out to the copies. The LPU is built the other way. It takes a single conventional core andpulls it apart: instruction control, the vector ALUs, the matrix units, the memory, and the network each become afunctional slice, a full-height column of identical hardware, and the columns stand side by side across the die. Homogeneous down each slice, heterogeneous across the chip. Data does not sit in a register file waiting to be issued onto a unit; itstreamshorizontally through the slices like parts down an assembly line, East and West, one register hop per cycle, whileVLIWinstructions issue Northward from the control slices to meet it. Nothing in the datapath reacts: the compiler knows where every operand is on every cycle, and the hardware just turns the clock. The streaming is the identity: this design launched as theTensor Streaming Processor(TSP), and carried that name until the 2024 rebrand toLanguage Processing Unit.

The vertical axis is SIMD width. The chip is 320 lanes tall, organised as 20superlanesof 16 lanes each (a 21st is a spare, fused out for yield and invisible to software), and every slice acts on all 320 lanes at once. The horizontal axis is time. There are 64 logicalstream registersper lane, 32 flowing East and 32 West, and on every tick each stream advances one slice in its direction until it is consumed or falls off the edge of the die. A slice reads operands off the passing streams, computes, and writes results back onto streams bound for the next slice. The die is mirrored into two hemispheres around a central vector unit, so a value produced once can be consumed by slices on either side.

##### Compute

The LPU keeps the same division of labour as everything else, matrix work on dedicated units and the rest on a vector engine, but arranges both as slices in the stream. The matrix path is theMXM: four independent 320×320 multiply-accumulate planes (two per hemisphere), 409,600 multipliers in all, taking INT8 or FP16 operands into INT32 or FP32 accumulators. Weights install across a plane (all of them in under 40 cycles), then activations stream through and products accumulate. At 900 MHz that is roughly750 INT8 TOPS and 188 FP16 TFLOPS, and, unusually, the number carries no sparsity asterisk: the TSP refuses to skip zeros at all, because a data-dependent skip would make execution time data-dependent, and determinism is the one property it will not trade.

The vector path is theVXMin the centre of the die: 16 ALUs per lane arranged as a 4×4 mesh, 5,120 32-bit ALUs, running activations, normalisation, quantisation, and residual adds. Because compute isspatialrather than issued to a shared unit, an operand can march through a chain of VXM ALUs and straight into an MXM plane on consecutive cycles without touching memory: the operator fusion a GPU kernel builds by hand is here just the physical order of the slices. A third slice type, theSXM, handles the movement the straight-line stream cannot express: lane shifts, a 320-lane permute, transposes, and the chip-to-chip links all live here, so rearranging data across lanes is a first-class operation rather than a round-trip through SRAM.

##### Memory

There is no HBM, no DRAM, and no cache. On-chip is theMEMslices: 230 MB of SRAM in 88 slices (44 per hemisphere), every byte a single cycle from a compute slice, ~80 TB/s aggregate. That is the whole hierarchy: one tier, flat, software-addressed, with none of the eviction, prefetch, or coherence machinery that would introduce a variable-latency access.

The consequence is the defining constraint of the architecture. 230 MB does not hold a model. Llama-2 70B in FP16 is 140 GB, so it has to besharded across hundreds of chips, its weights spread over the aggregate SRAM of a whole rack or more: the deployed configuration was ~576 LPUs. Where a GPU parks the model in HBM on a handful of packages and streams tokens past it, the LPU spreads the model in SRAM across a cluster and streams tokens through the cluster. The chip count is set by capacity, not compute: the weights have to fit. It is the same trade Cerebras makes (SRAM only, no HBM), reached from the opposite direction: Cerebras keeps one enormous die and gives up capacity per wafer; Groq keeps a normal-sized die and gives up ever fitting a model on one.

##### Numerics

The numerics are the road not taken. Every other vendor here has been halving precision each generation,FP16toFP8toFP4with block scaling to buy the accuracy back. The TSP stayed atFP16 and INT8with FP32 accumulate and never shipped FP8 or FP4 in silicon. Its one numeric idea isTruePoint: a 320-element dot product fused into a single rounding step with FP32 accumulation, so an FP16 multiplier array lands close to FP32 accuracy on the reduction (Groq reports ~0.05% max error against an FP32 baseline).

Whether 16-bit was conviction or a datapath that never got its low-precision refresh is hard to separate from the fact that the second-generation chip never shipped. SRAM capacity is the architecture's scarcest resource, and 8-bit weights would halve the chips a model needs; a machine this capacity-bound had every reason to want FP8 and did not get it on silicon. It is the same open question that hangs over Cerebras's 16-bit-only datapath, and the same tension: the vendor most starved for capacity computing at the widest precision.

##### Determinism

Every other accelerator hides latency; the LPUexposesit. The ISA carries the execution latency of each instruction, the datapaths are fixed-latency by construction, and so the compiler computes ahead of time the exact cycle on which every result appears. Nothing in the hardware can disturb that schedule: no cache to miss, no arbiter to stall on, no branch to mispredict, no speculation to unwind. Groq's own measurement is the proof: 24,240 runs of BERT-Large returned inside a ~75 µs band, and the compiler's predicted latency sat within 2% of measured.

This is the TPU's instinct (move scheduling into the compiler, delete the hardware that second-guesses it) taken one step further. The TPU compiler schedules a chip; the LPU compiler schedules asystem, because the determinism holds across the network too. And it is the exact inverse of Cerebras, whose cores aredataflow, firing whenever an operand happens to arrive: the WSE reacts to data, the LPU is timed to it. Both machines delete the scheduler; one replaces it with arrival, the other with a clock.

##### Bets

* Bet 1: Determinism over tolerance.Delete every reactive component (caches, arbiters, predictors, reorder buffers) and let the compiler own every cycle.
* Bet 2: Spatial functional slices.Disaggregate the core into slices and stream operands through them, so fusion is the floorplan and data reuse lives in the wires, not a register-file dance.
* Bet 3: SRAM is the only memory.No HBM, at any capacity cost. Trade the ability to hold a model on-chip for single-cycle, fixed-latency access, accept models must span hundreds of chips.
* Bet 4: Schedule the network too.Make the chips their own routers and compile the communication cycle-by-cycle, so a thousand-chip cluster is one deterministic program with no switches and no congestion.
* Bet 5: Sell latency, not throughput.Optimise for tokens per second per user at batch 1, the regime GPUs are worst at, and price that speed as the product rather than competing on cost per token.

#### Scaling

Scaling an LPU is unlike anything else here, because there is no separate scale-up fabric to build: the chip is already a switch. Each LPU carries up to 16 chip-to-chipRealScalelinks (11 exposed on the card) and acts simultaneously as a compute endpoint and a router. Wire the chips directly to each other and the cluster is aglueless multiprocessor: noNICs, noswitch ASICs, no top-of-rack switch. And because determinism holds across those links, the entire cluster runs on one compile-time schedule.

Scale-up
The node: 8 LPUs fully connected over 
RealScale
 C2C, forming one 
Dragonfly
 group that presents as a single high-radix virtual router. Software-scheduled, switchless, no coherence.

Scale-out
The same fabric, extended. A 
Dragonfly
 of nodes: 9 per rack (72 chips, one node a hot spare), scaling to a spec'd 10,440 chips, every hop still on a compiled, deterministic schedule.

##### Scale-up

The node is 8 LPUs, fully connected: 7 of each chip's links wire it to the other seven, so every chip in the node is one hop from every other. The remaining four links on each chip (32 across the node) bundle into what the ISCA paper calls a 32-port virtual router, the node's uplink into the larger fabric. There is no baseboard switch and no coherent address space; a remote operand is not loaded, it isscheduledto arrive, injected by the source chip on a cycle the compiler chose and consumed by the destination on the cycle it lands.

##### Scale-out

Beyond the node, nodes wire into aDragonfly: 9 nodes make a 72-chip rack (the ninth a hot spare, so 64 active), and the topology scales to a specified 10,440 chips with any two under six hops apart. The fabric issoftware-scheduled: routing and flow control move to compile time, and the paper's framing is blunt,scheduled, not routed. There is no back-pressure and no dynamic arbitration, because the compiler has already proven the receiver is ready; links carryforward error correctioninstead of retransmission, because a retry would perturb the schedule. Keeping a rack of independently-clocked chips in lockstep is its own problem: the links areplesiochronous, and the fabric maintains a global consensus time withHardware-Aligned Countersexchanged every 256 cycles over a spanning tree, with periodic deskew instructions stalling each chip back into alignment. The payoff Groq reports is that an 8-wayall-reducematches anA100/NVSwitchnode on large tensors and beats it on small ones, where a scheduled fabric pays none of the handshake latency a dynamic one does.

The cost is written into the physics of the memory bet. A model replica is not a box, it is a rack (or eight): Llama-2 70B on ~576 chips carried, by one analysis, 144 host CPUs and 144 TB of host RAM alongside the LPUs, against two CPUs for an 8-GPU server. The wafer under each chip is cheap (14 nm GlobalFoundries, reportedly under $6k, against ~$16k for an H100-class part), but you need hundreds of them, and during decode most of their enormous compute sits idle while the SRAM does the work.SemiAnalysisput it plainly: the LPU wins the bill of materials per token when you optimise for latency, and loses to GPUs by roughly an order of magnitude on throughput per dollar once you batch. The architecture is not competing on cost. It is competing on speed.

#### Software

The programming model is the purest expression ofthe compiler is the machine. There areno kernels. You hand the Groq compiler a model fromPyTorch, TensorFlow, orONNX; it lowers to a small tensor op set and statically schedules every instruction, every stream, and every chip-to-chip transfer. Nobody writes awgmmaor hand-tunes a tile, because there is no dynamic hardware to hand-tune against. Groq's demonstration was bringing up LLaMA in four days with a team of under ten, against the months of hand-kernel work the same model took to tune on a GPU. The stack around the compiler (a profiler, a runtime, theGroqFlowbring-up path) is small and closed, andGroqFlowwas archived in 2025 as the company stopped selling cards and started selling tokens.

That pivot is the tell about what the architecture is for. The LPU isinference-onlyby construction (Ross's framing is that training is a local game and inference a global one), and it is unbeaten at a single thing: single-user decode latency. Independent measurement backs the claim, withArtificial Analysisclocking Groq among the fastest token-per-second providers on open models. It is badly matched to the rest: a model that will not fit in a rack of SRAM, a workload that wants big batches for throughput-per-dollar, or dynamic control flow a static schedule cannot express.MoEis served, but its data-dependent expert routing sits awkwardly against a compiler that wants to know everything in advance, and Groq has published little on how it reconciles the two.

The epilogue is that the buyer of all this was NVIDIA. In December 2025 NVIDIA took anon-exclusive licenseto the LPU technology and hired Ross and much of the team. It was not an acquisition: no products, customer contracts, or equity changed hands, per NVIDIA's own 10-K, though the roughly $13B paid at closing led the press to call it one. AtGTC2026 the technology reappeared as theNVIDIA Groq 3 LPU, a rack of 256 SRAM-only inference chips sitting besideRubinNVL72 and splitting the transformer between them: the GPUs runattention, the LPUs run the feed-forward and MoE layers, withDynamoorchestrating the hand-off. The most deterministic architecture in AI ended up as a latency co-processor inside the most programmable one. GroqCloud, meanwhile, still serves tokens on the original 14 nm silicon.

### Comparison

All arithmetic figures are peak values at the stated precision; entries are dense unless the vendor does not publish the basis. Memory bandwidth is the native tier shown: HBM for GPUs, TPUs, and Trainium; aggregate on-chip SRAM for Cerebras and Groq. Those numbers are not directly comparable. Scale-up bandwidth follows each vendor's convention and can mean per-chip aggregate, rack aggregate, or true bisection.

##### Per-chip

Company
Year
Chip
Accelerator memory
Memory BW
Flagship dense FLOPs
TDP
Scale-up BW

2023
H100 SXM5
80 GB HBM3
3.4 TB/s
1.98 PetaFLOPS FP8
700 W
900 GB/s

2024
H200 SXM
141 GB HBM3e
4.8 TB/s
1.98 PetaFLOPS FP8
700 W
900 GB/s

2024
B200
192 GB HBM3e
8 TB/s
4.5 PetaFLOPS FP8 / 9 PetaFLOPS FP4
1,000 W
1.8 TB/s

2025
B300
288 GB HBM3e
8 TB/s
7.5 PetaFLOPS FP8 / 15 PetaFLOPS FP4
1,400 W
1.8 TB/s

2026
Rubin
288 GB HBM4*
~13 TB/s*
~17 PetaFLOPS FP8* / ~50 PetaFLOPS FP4*
~1,500 W*
3.6 TB/s

2027
Rubin Ultra
1 TB HBM4e*
~32 TB/s*
~33 PetaFLOPS FP8* / ~100 PetaFLOPS FP4*
~1,800 W*
3.6 TB/s

2023
TPU v5p
95 GB HBM2e
2.8 TB/s
0.46 PetaFLOPS BF16
n/d
1.2 TB/s

2025
TPU Ironwood (v7)
192 GB HBM3e
7.4 TB/s
4.6 PetaFLOPS FP8
n/d
1.2 TB/s

2026
TPU v8t Sunfish
216 GB HBM3e
6.5 TB/s
12.6 PetaFLOPS FP4
n/d
n/d

2023
MI300X
192 GB HBM3
5.3 TB/s
2.6 PetaFLOPS FP8
750 W
896 GB/s

2024
MI325X
256 GB HBM3e
6.0 TB/s
2.6 PetaFLOPS FP8
1,000 W
896 GB/s

2025
MI355X
288 GB HBM3e
8 TB/s
10 PetaFLOPS FP8 / 20 PetaFLOPS FP4
1,400 W
1,075 GB/s

2026
MI455X
TBD
TBD
~40 PetaFLOPS FP4*
TBD
n/d

2021
WSE-2
40 GB SRAM (on-wafer)
20 PB/s (aggregate)
7.5 PetaFLOPS FP16
23 kW (system)
(domain = the wafer)

2024
WSE-3
44 GB SRAM (on-wafer)
21 PB/s (aggregate)
~15.8 PetaFLOPS FP16*
23 kW (system)
(domain = the wafer)

2022
Trainium1
32 GB HBM2e*
820 GB/s
0.19 PetaFLOPS BF16/FP8
n/d
n/d

2024
Trainium2
96 GB HBM3
2.9 TB/s
1.3 PetaFLOPS FP8
~500 W*
1.28 TB/s

2025
Trainium3
144 GB HBM3e
4.9 TB/s
2.5 PetaFLOPS FP8
n/d
n/d

2020
GroqChip (1st-gen TSP/LPU)
230 MB SRAM
80 TB/s (on-chip aggregate)
0.188 PetaFLOPS FP16
215 W
330 GB/s (11-link card)

2026
NVIDIA Groq 3 LP30
500 MB SRAM
150 TB/s (on-chip aggregate)
~1.2 PetaFLOPS FP8*
n/d
2.5 TB/s

##### Per-rack / pod

Company
Year
System
Chips
Aggregate dense FLOPs
Accelerator memory total
Scale-up fabric BW
Per-chip NIC
Power
Cooling

2023
HGX H100
8
16 PetaFLOPS FP8
640 GB
7.2 TB/s
400 Gbps (CX-7)
~10 kW
Air

2024
HGX H200
8
16 PetaFLOPS FP8
1.1 TB
7.2 TB/s
400 Gbps
~10 kW
Air

2024
GB200 NVL72
72
360 PetaFLOPS FP8 / 720 PetaFLOPS FP4
13.4 TB
130 TB/s
800 Gbps (CX-8)
~120 kW
Liquid

2025
GB300 NVL72
72
540 PetaFLOPS FP8 / 1,100 PetaFLOPS FP4
20.7 TB
130 TB/s
800 Gbps
~120 kW
Liquid

2026
NVL144
144
~1.2 ExaFLOPS FP8 / ~3.6 ExaFLOPS FP4
~21 TB
~260 TB/s*
1.6 Tbps (CX-9)
~200 kW*
Liquid

2027
NVL576 (Kyber)
576
~5 ExaFLOPS FP8 / ~15 ExaFLOPS FP4
~144 TB
n/d
1.6 Tbps
~600 kW*
Liquid

2023
TPU v5p pod
8,960
4.1 ExaFLOPS BF16
852 TB
(3D torus)
(ICI = scale-up + scale-out)
n/d
Liquid

2025
TPU Ironwood pod
9,216
42.5 ExaFLOPS FP8
1.77 PB
(3D torus)
optical OCS
~10 MW*
Liquid

2026
TPU v8t Sunfish pod
9,600
121 ExaFLOPS FP4
~2 PB
(Boardfly)
optical OCS
n/d
Liquid

2023
MI300X 8-GPU OAM
8
21 PetaFLOPS FP8
1.5 TB
7.2 TB/s
400 Gbps
~10 kW
Air

2024
MI325X 8-GPU OAM
8
21 PetaFLOPS FP8
2.0 TB
7.2 TB/s
400 Gbps
~12 kW*
Air

2025
MI355X 8-GPU OAM
8
80 PetaFLOPS FP8 / 160 PetaFLOPS FP4
2.3 TB
8.6 TB/s
400 Gbps
~16 kW*
Liquid

2026
Helios (MI455X)
72
1.4 ExaFLOPS FP8 / 2.9 ExaFLOPS FP4
31 TB
260 TB/s
n/d
n/d
Liquid

2024
Condor Galaxy 3
64 wafers
~1 ExaFLOPS FP16*
2.8 TB SRAM + MemoryX
(Ethernet tree)
1.2 Tb/s Ethernet
~1.5 MW*
Liquid

2022
Trn1 instance
16
3 PetaFLOPS BF16
512 GB
(2D torus)
~50 Gbps (EFA)
n/d
Air

2024
Trn2 UltraServer
64
83 PetaFLOPS FP8
6.1 TB
(3D torus)
200 Gbps (EFAv3)
n/d
Air

2025
Trn3 UltraServer
144
362 PetaFLOPS FP8
20.7 TB
(NeuronSwitch)
n/d
n/d
Liquid

2022
GroqRack
64 active (72 installed)
12 PetaFLOPS FP16
14 GB SRAM
3.2 TB/s bisection
(RealScale; no per-chip NIC)
n/d
Air

2026
NVIDIA Groq 3 LPX
256
315 PetaFLOPS FP8
128 GB SRAM + 12 TB DDR5
n/d (640 TB/s aggregate C2C)
n/d
n/d
Liquid

*marks analyst-derived, era-inferred, or vendor-aggregate-derived figures;n/dmarks specs the vendor has not disclosed.

##### What this shows

* Per-chip FP8 has converged.B200 (4.5 PF), Ironwood (4.6 PF), and MI355X (10 PF) sit within ~2× of each other. The per-chip arms race is close; the rack and pod are where the architectures diverge.
* HBM capacity is AMD's persistent win.192 → 256 → 288 GB across 2023–2025 has matched or beaten NVIDIA every generation. NVIDIA caught up at 288 GB only with B300 (late 2025); Rubin Ultra retakes the lead at 1 TB / package in 2026.
* Rack-scale scale-up is NVIDIA's win until 2026.GB200 / GB300 NVL72 was the only coherent rack-scale domain shipping in 2024–2025; AMD scaled up at the box and didn't reach rack scale until Helios. The TPU sidesteps the question: its torus is the rack and the cluster at once.
* TPU pods dwarf any NVIDIA rack in chip count.Ironwood pod = 9,216 chips for 42.5 ExaFLOPS FP8; NVL576 = 576 GPUs for ~5 ExaFLOPS FP8. The TPU's flat-rate-per-chip × massive-pod recipe yields more aggregate compute per system, at the cost of per-chip bandwidth.
* Power per chip is rising fast.700 W (Hopper) → 1,000 W (Blackwell, MI325X) → 1,400 W (B300, MI355X) → ~1,800 W (Rubin Ultra, analyst). Liquid cooling becomes mandatory above ~1,000 W; air cooling effectively ends with Hopper.
* Scale-out NIC bandwidth doubles each NVIDIA generation.400 Gbps (CX-7, Hopper) → 800 Gbps (CX-8, Blackwell) → 1.6 Tbps (CX-9, Rubin). AMD lags one generation (Pollara 400 → Vulcano 800), reflecting Pensando's smaller install base and later integration.
* Cerebras breaks the table's axes.No HBM at all: 44 GB of on-wafer SRAM at an aggregate 21 PB/s, ~1.3 bytes per dense FLOP where the GPU rows sit near 0.002. The cost is visible in the same row: less total memory than a single H200, dense FLOPs per watt behind every contemporary GPU, and an empty scale-up column because the coherent domain is the wafer itself.
* Trainium competes on economics, not the spec sheet.Per-chip it trails (Trn2's 1.3 PF FP8 is roughly a quarter of MI355X), but the Trn2 UltraServer reached 64-chip rack-scale scale-up in 2024 alongside NVL72, as a message-passing torus rather than a coherent crossbar, and Trn3 pivots to the switched NeuronSwitch fabric. AWS owns every layer from the Nitro card to the API, and one anchor tenant (Anthropic, over a million Trainium2 chips) validates it at frontier scale.
* Groq trades capacity for SRAM bandwidth, then scales the memory pool with chip count.The first GroqRack exposes only 14 GB across 64 active chips; Groq 3 LPX grows that to 128 GB across 256 chips at 40 PB/s aggregate SRAM bandwidth. Its 12 TB DDR5 tier and pairing with Rubin show that the LPU complements, rather than replaces, a large-memory GPU rack.