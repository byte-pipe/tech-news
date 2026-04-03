---
title: Basic facts about GPUs | Damek Davis’ Website
url: https://damek.github.io/random/basic-facts-about-gpus/
site_name: hackernews
fetched_at: '2025-06-25T07:05:04.875907'
original_url: https://damek.github.io/random/basic-facts-about-gpus/
author: ibobev
date: '2025-06-25'
published_date: '2025-06-18T00:00:00+00:00'
description: Making sure I don’t forget what I read.
---

# Basic facts about GPUs

last updated:2025-06-18

I’ve been trying to get a better sense of how GPUs work. I’ve read a lot online, but the following posts were particularly helpful:

1. Making Deep Learning Go Brrrr From First Principles
2. What Shapes Do Matrix Multiplications Like?
3. How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance: a Worklog

This post collects various facts I learned from these resources.

Acknowledgements: Thanks toAlex McKinneyfor comments onindependent thread scheduling.

Table of Contents

* Compute and memory hierarchy
* Two Performance Regimes: Memory-Bound and Compute-Bound
* The Third Regime: Overhead
* Two basic strategies for increasing performance: Fusion and TilingOperator FusionTiling: Strategy for Compute-Bound KernelsThe Coalesced Load: HBM to SRAMSynchronizationThe On-Chip Hardware: Banks and WarpsThe Bank Conflict ProblemThe On-Chip Compute Phase: Increasing Arithmetic Intensity
* Operator Fusion
* Tiling: Strategy for Compute-Bound KernelsThe Coalesced Load: HBM to SRAMSynchronizationThe On-Chip Hardware: Banks and WarpsThe Bank Conflict ProblemThe On-Chip Compute Phase: Increasing Arithmetic Intensity
* The Coalesced Load: HBM to SRAM
* Synchronization
* The On-Chip Hardware: Banks and Warps
* The Bank Conflict Problem
* The On-Chip Compute Phase: Increasing Arithmetic Intensity
* Additional Performance ConsiderationsOccupancy and Latency HidingAvoiding Thread DivergenceQuantization
* Occupancy and Latency Hiding
* Avoiding Thread Divergence
* Quantization

## Compute and memory hierarchy

A GPU’s design creates an imbalance since it can compute much faster than it can access its main memory. An NVIDIA A100 GPU, for example, can perform 19.5 trillion 32-bit floating-point operations per second (TFLOPS), but its memory bandwidth is only about 1.5 terabytes per second (TB/s). In the time it takes to read a single 4-byte number, the GPU could have performed over 50 calculations.

Below is a diagram of the compute and memory hierarchy for an NVIDIA A100 GPU. The numbers I quote for flops/s and TB/s are exclusive to A100s.

+---------------------------------------------------------------------------------+
| Global Memory (VRAM) |
| (~40 GB, ~1.5 TB/s on A100) |
+----------------------------------------+----------------------------------------+
 | (Slow off-chip bus)
+----------------------------------------v----------------------------------------+
| Streaming Multiprocessor (SM) |
| (1 of 108 SMs on an A100, each ~(19.5/108) TFLOPS) |
| (2048 threads, 64 warps, 32 blocks) |
| +-----------------------------------------------------------------------------+ |
| | Shared Memory (SRAM) / L1 Cache |
| | (~192 KB on-chip workbench, 19.5 TB/s) |
| +-----------------------------------------------------------------------------+ |
| | Register File (~256 KB, ? TB/s) |
| +-----------------------------------------------------------------------------+ |
| | | |
| | //-- A "Block" of threads runs on one SM --// | |
| | +--------------------------+ +------------------------+ | |
| | | Warp 0 (32 thr) | | Warp 1 (32 thr) | ... (up to 32 warps)| |
| | | +----------------------+ | +----------------------+ | | |
| | | | Thread 0 Registers | | | Thread 32 Registers | | | |
| | | | [reg0: float] | | | [reg0: float] | | | |
| | | | [reg1: float] ... | | | [reg1: float] ... | | | |
| | | +----------------------+ | +----------------------+ | | |
| | +--------------------------+ +------------------------+ | |
| | | |
+---------------------------------------------------------------------------------+

This diagram shows the performance hierarchy.1Global Memory (VRAM)is the large, slow, off-chip memory pool where all data initially lives. AStreaming Multiprocessor (SM)is the GPU’s unit of computation. To work, it must fetch data over the slow bus. To mitigate this, each SM has fast, on-chipShared Memory(SRAM) with a bandwidth of 19.5 TB/s.2Programmers use this as a manually-managed cache.

Athreadis the smallest unit of execution. Each thread has a private set ofRegistersto hold values for immediate computation, with access speeds over ?? TB/s.3The hardware groups threads intoWarpsof 32. This post analyzes performance using the simplified model oflockstep execution, where all 32 threads in a warp execute the same instruction at the same time.4On an A100, an SM has an upper limit of 64 warps. A programmer groups threads into aBlock, a grid of threads that is guaranteed to run on a single SM. A block can be one, two, or three-dimensional. For simplicity, this post will focus on square two-dimensional blocks ofBLOCK_DIM x BLOCK_DIMthreads, where the total number of threads cannot exceed the hardware limit of 1024. All threads in a block share access to the same on-chip Shared Memory.

## The Two Performance Regimes

We analyze the performance of akernel, which is a function launched by the host (CPU) to be executed in parallel by many GPU threads. A kernel’s performance is limited by either its memory bandwidth or its compute throughput. These two limits define the performance regimes.

An operation ismemory-boundif its runtime is dictated by the speed of transferring data from Global Memory to the SM. For an operation like element-wise additiony = x + 1, the SM performs a trivial number of FLOPs for each element it reads. The SM spends most of its time idle, waiting for data.

An operation iscompute-boundif its runtime is dictated by the SM’s arithmetic speed. A large matrix multiplication is the canonical example. Once data is loaded into the SM, a massive number of computations are performed. The memory bus is idle while the SM is busy.

Arithmetic Intensity (AI)is the formal metric that determines the regime. It is the ratio of work to memory traffic.

Arithmetic Intensity = Total FLOPs / Total Bytes Accessed

For the Roofline model,Total Bytes Accessedspecifically counts the data transferred between Global Memory (HBM) and the on-chip SM. This is because the model evaluates a kernel’s performance against the primary bottleneck: the slow off-chip memory bus. On-chip traffic, such as from Shared Memory to registers, is not included in this calculation.

The Roofline Model plots a kernel’s achievable performance (in FLOPs per second) against its AI. The two “roofs” are the hard physical limits of the GPU.

 ^ Performance (TFLOPS)
 |
 | Memory-Bound Region ¦ Compute-Bound Region
 | ¦
 | /¦---------------------- <-- Peak Compute (~19.5 TFLOPS)
 | / ¦
 | / ¦
 | Peak Global /<--¦------ Inefficient Compute Roof (e.g., using scalar ops, transcendental functions)
 | Mem BW (~1.5 / ¦
 | TB/s) / ¦
 | / ¦
 +---------------------¦---------------------------> Arithmetic Intensity (FLOPs/Byte)
 ^
 ¦
 Hardware Ridge Point (~13)

The performance of a kernel is determined as follows:

* When memory-bound, the SMs are stalled waiting for data. The runtime is the time it takes to move that data:Runtime = Bytes_Accessed / Memory_Bandwidth. The kernel’s performance is thereforePerformance = Total_FLOPs / Runtime = AI * Memory_Bandwidth. On the log-log plot, this is the diagonal line.
* When compute-bound, the SMs are fully utilized. The performance is limited by their peak arithmetic throughput:Performance = Peak_Compute_FLOPs. This is the horizontal line.

A kernel’s actual performance is the minimum of these two values. Theridge pointis the AI where the two performance ceilings intersect. For the A100, this is19.5 TFLOPS / 1.5 TB/s ≈ 13 FLOPs/Byte. A kernel must exceed this AI to become compute-bound. A kernel with AI lower than 13 operates in the memory-bound region; a kernel with AI higher than 13 operates in the compute-bound region. The goal of optimization is to increase AI to move the kernel’s operating point to the right, pushing its performance up until it hits the compute roof.

The “Peak Compute” roof of 19.5 TFLOPS is an ideal, achievable only with highly optimized instructions like Tensor Core matrix multiplications and high enough power limits. An operation can be compute-bound but still perform far below this peak. For example, a kernel with high AI that is dominated by scalar arithmetic or complex transcendental functions (sin,exp) will be limited by the throughput of those specific, slower instructions. This creates a lower effective “roof” for that kernel, as shown in the diagram. Increasing AI is necessary, but not sufficient; the FLOPs must also be efficient.

The primary strategy to increase AI is to maximize the reuse of data once it has been loaded into the SM’s fast on-chip memory. The following is a simplified model where a thread reads data from Global Memory directly into its private registers. This analysis calculates theminimum requireddata transfer; actual memory traffic depends on access patterns, which we will discuss later.

Consider computingC = A@B, where all matrices areN x Nand use 4-byte floats.

Strategy 1: One thread computes one elementC[i,j]

* FLOPs:To computeC[i,j], the thread performs N multiply-add operations. This is2*NFLOPs.
* Bytes Accessed:The thread must read rowiof A (N floats) and columnjof B (N floats). This is a total of2*Nfloats, or8*Nbytes.
* Arithmetic Intensity:(2*N FLOPs) / (8*N Bytes) = 0.25 FLOPs/Byte.

This AI is low. The kernel will be memory-bound.

Strategy 2: One thread computes a2x2tile of CTo compute a2x2tile (C[i,j],C[i,j+1],C[i+1,j],C[i+1,j+1]), the thread must perform the computation for all four elements.

* FLOPs:4 elements * 2*N FLOPs/element = 8*NFLOPs.
* Bytes Accessed:The thread must read two rows from A (A[i,:],A[i+1,:]) and two columns from B (B[:,j],B[:,j+1]). This is2*N + 2*N = 4*Nfloats, or16*Nbytes.
* Arithmetic Intensity:(8*N FLOPs) / (16*N Bytes) = 0.5 FLOPs/Byte.

These AI values are far below the A100’s ridge point of ~13 FLOPs/Byte. This simple register-only model is insufficient to make matrix multiplication compute-bound.5The key to achieving high AI is for threads within a block to cooperate by loading a much larger tile of A and B into the shared, on-chip SRAM. By working together on this shared data, a block of 1024 threads can achieve an AI greater than 13. We will detail the mechanics of this in the section on Shared Memory.

## The Third Regime: Overhead

Performance can also be limited by host-side overhead. This is time the CPU (the host) spends preparing work for the GPU, for example, in the Python interpreter or a framework’s dispatch system.

An application is overhead-bound if its GPU kernels are too small or numerous. The GPU executes each small task quickly and then waits, idle, for the CPU to issue the next command. The runtime is dominated by the CPU’s inability to feed the GPU fast enough.

Modern frameworks use asynchronous execution to mitigate this. The host can queue a stream of commands for the GPU without waiting for each one to complete. If the individual GPU operations are sufficiently large, the host can “run ahead,” and the overhead of launching one kernel is hidden by the execution of the previous one.

For the remainder of this post, we assume our kernels are large enough that overhead is not the primary limiter, and focus instead on memory and compute.6

## Two basic strategies for increasing performance: Fusion and Tiling

With the kernel large enough to make launch overhead negligible, performance is governed by the two physical limits of the GPU: memory bandwidth and compute throughput. Increasing the performance of a kernel, therefore, means pushing its operating point on the Roofline model up and to the right. There are two basic strategies for achieving this.

* For a sequence of individually memory-bound operations, the strategy is tofusethem into a single kernel to eliminate intermediate memory traffic.
* For a single, complex operation with high potential arithmetic intensity (like matrix multiplication), the strategy is to usetilingto maximize data reuse within the SM’s fast memory.

We will address each strategy in turn.

### Operator Fusion

Chains of simple operations likey = relu(x + 1)are common. Each operation (add,relu) has a very low arithmetic intensity and is memory-bound. Executing them as separate, sequential GPU kernels is inefficient. The primary strategy to optimize these sequences isoperator fusion.

The problem is the intermediate memory traffic. Consider the unfused execution ofy = relu(x + 1):

1. Kernel 1 (add):Reads the entire tensorxfrom global memory. Computestmp = x + 1. Writes the entire intermediate tensortmpback to global memory.
2. Kernel 2 (relu):Reads the entire tensortmpfrom global memory. Computesy = relu(tmp). Writes the final tensoryback to global memory.

This approach is wasteful. It involves two separate kernel launch overheads and forces a round-trip to slow global memory for the intermediatetmptensor.

Fusion combines these steps into a single, more efficient GPU kernel. A JIT compiler like Triton ortorch.compile’s Inductor backend can perform this transformation automatically.

In the fused kernel:

1. A single thread reads one element ofxfrom global memory into its private registers.
2. It performs all computations, i.e.,tmp = x + 1, theny = relu(tmp), entirely within those fast registers.
3. It writes only the final resultyback to global memory.

# Unfused (Conceptual)

def

unfused_add_relu
(
x
):


tmp

=

torch
.
add
(
x
,

1
)

# Reads x from HBM, writes tmp to HBM


y

=

torch
.
relu
(
tmp
)

# Reads tmp from HBM, writes y to HBM


return

y

# Fused (Conceptual)

@
torch
.
compile

def

fused_add_relu
(
x
):


# The compiler fuses these into one kernel.


# The intermediate result of x+1 never touches HBM.


return

torch
.
relu
(
x

+

1
)

The intermediate tensortmpbecomes ephemeral, never materializing in global memory. This cuts the memory traffic in half (one read ofx, one write ofy) and eliminates the launch overhead of the second kernel.

### Tiling: Strategy for Compute-Bound Kernels

Our register-only model forC=A@Byielded an arithmetic intensity of 0.25 FLOPs/Byte, far below the A100’s ridge point of ~13. This is because a single thread reads2*Nvalues to perform2*NFLOPs; the data is used once and then discarded. To increase data reuse and become compute-bound, threads within a block must cooperate to load large tiles of the input matrices into the SM’s fast, on-chip Shared Memory.

The logic of this cooperation is based on decomposing the matrix product. The calculation for a single elementC[i,j]is a sum over thekdimension:C[i,j] = sum_k A[i,k] B[k,j]. This sum can be partitioned into a sum of partial sums over tiles. For square tiles, the innerkdimension is broken into tiles of sizeBLOCK_DIM, matching the outer dimensions. The formula becomes:`

\[C[i,j] = \sum_{t=0}^{\text{NUM_K_TILES}-1} \left( \sum_{k=t \cdot \text{BLOCK_DIM}}^{(t+1) \cdot \text{BLOCK_DIM} - 1} A[i,k] B[k,j] \right)\]

The tiling algorithm computes one term from the outer sum (one partial product) per iteration. A block of threads computes one outputC_tileby iterating through thekdimension, loading tiles of A and B, computing their product on-chip, and accumulating the result. This is achieved with a three-phase pattern:Load, Synchronize, and Compute.

# Conceptual algorithm for one thread block computing one output tile, C_tile.
# C_tile corresponds to, e.g., C[block_row_start:end, block_col_start:end].

# Each thread in the block holds a piece of C_tile in its registers. Initialize to zero.

thread_private_C_accumulator

=

zeros
(...)

# Loop over tiles of A and B along the k-dimension.
# Each iteration computes one partial product from the sum above.

for

k_tile_idx

in

range
(
NUM_K_TILES
):


# Phase 1: Load


# All threads in the block cooperate to load one tile of A and one tile of B


# from slow Global Memory into fast Shared Memory.


A_tile

=

load_A_tile_from_global_mem
(
k_tile_idx
)


B_tile

=

load_B_tile_from_global_mem
(
k_tile_idx
)


# Phase 2: Synchronize


# Wait for all threads to finish loading before any thread starts computing.


# This ensures A_tile and B_tile are fully populated.


__syncthreads
()


# Phase 3: Compute


# Each thread computes its piece of the on-chip matmul.


# The data in A_tile and B_tile is reused extensively from Shared Memory.


thread_private_C_accumulator

+=

on_chip_matmul_piece
(
A_tile
,

B_tile
)


# Wait for all threads to finish computing before loading the next tile.


__syncthreads
()

# After the loop, write the final accumulated result to Global Memory.

write_C_tile_to_global_mem
(
thread_private_C_accumulator
)

We now examine the mechanics of the three-phaseLoad, Synchronize, Computepattern.

### The Coalesced Load: HBM to SRAM

The first phase loads tiles of A and B from slow global memory (HBM) into fast on-chip Shared Memory (SRAM). The goal is to perform this transfer with the maximum possible memory bandwidth. This requirescoalesced memory access. A memory access is coalesced when all 32 threads in a warp access a single, contiguous 128-byte block of HBM in one transaction.

To achieve this, the kernel maps thread indices to memory addresses. For aBLOCK_DIM x BLOCK_DIMblock of threads loading a data tile of the same size, a common mapping is for thread(tx, ty)to be responsible for loadingA[global_row + ty, global_k + tx]intoA_tile[ty, tx]in Shared Memory. In this example,BLOCK_DIMis 32.

Consider a single warp of threads wheretyis fixed andtxranges from 0 to 31.

* Thread(0, ty)readsA[global_row + ty, global_k + 0].
* Thread(1, ty)readsA[global_row + ty, global_k + 1].
* …
* Thread(31, ty)readsA[global_row + ty, global_k + 31].

Assuming row-major storage, these threads access 32 consecutive 4-byte floats, a contiguous 128-byte segment. This is a perfect coalesced read. The entire32x32tile is loaded in 32 such coalesced reads, one for each warp in the block.

 Thread Block (32x32) Global Memory (HBM)
 (One row of A's tile)
 +--------------------+
 | Warp 0 (ty=0) | ----> [A_ij, A_i,j+1, ..., A_i,j+31] (128 bytes)
 | (tx = 0..31) | (One coalesced memory transaction)
 +--------------------+
 | Warp 1 (ty=1) | ----> [A_i+1,j, ..., A_i+1,j+31] (128 bytes)
 +--------------------+
 | ... |
 +--------------------+
 | Warp 31 (ty=31) | ----> [A_i+31,j, ..., A_i+31,j+31] (128 bytes)
 +--------------------+

This load can be made more efficient withvectorized access. The physical memory transaction for a coalesced read fetches the full 128 bytes from HBM regardless. The difference is how the SM requests this data.

With scalar loads, the warp must issue 32 separate 32-bit load instructions. With vectorized loads, it issues only 8 wider 128-bit load instructions. This is more efficient because the SM has a limited number of instruction issue slots per clock cycle. Requesting the data with 8 wide instructions consumes fewer of these hardware resources than requesting it with 32 narrow instructions. This ensures the memory controller is kept busy with a continuous stream of full-width requests, increasing theutilizedmemory bandwidth by reducing SM-side bottlenecks.

Vectorized access is enabled by casting pointers in device code (e.g., fromfloat*tofloat4*), promising the compiler that the memory is aligned to the vector size.

The efficiency of these vectorized loads relies onmemory alignment. A singlefloat4instruction loads a 16-byte vector. For a matrix of 4-byte floats, this vector contains 4 elements. The hardware executes this instruction efficiently only if the memory address is a multiple of 16. This means the matrix’s inner dimensionK(the number of columns) must be a multiple of 4. IfKis not a multiple of 4, the rows become misaligned with the 16-byte memory segments.

Consider a matrix of 4-byte floats and a memory system with 16-byte segments.

* Aligned (K=8, a multiple of 4):Memory: |<--- 16B --->|<--- 16B --->|
 [Seg 0 ][Seg 1 ]
Row 0: [e0 e1 e2 e3 | e4 e5 e6 e7] (A float4 load for e0-e3 is aligned)
Row 1: [e0 e1 e2 e3 | e4 e5 e6 e7] (A float4 load for e0-e3 is aligned)
* Unaligned (K=7):Memory: |<--- 16B --->|<--- 16B --->|<--- 16B --->|
 [Seg 0 ][Seg 1 ][Seg 2 ]
Row 0: [e0 e1 e2 e3 e4 e5 e6]
Row 1: [e0 e1 e2 e3 e4 e5 e6] (A float4 load for Row 1's e0-e3 spans Seg 0 and Seg 1)This misalignment forces the hardware to issue more complex, slower load operations, reducing memory bandwidth.7

Important:This row-wise strategy provides coalesced access for matrix A. For matrix B, the required access patterns are in opposition.

1. HBM Requirement:To maintain coalescing, the B tile must be read from HBM row-by-row.
2. Compute Requirement:The matrix multiplication itself requires access to columns of the B tile.

Loading columns directly from a row-major matrix is an uncoalesced, strided access that serializes HBM transactions. The solution is therefore to load the B tile using coalesced row-reads, but then rearrange the data as it is written into Shared Memory. The structure of this rearrangement is dictated by the physical, banked architecture of Shared Memory.

### Synchronization

The__syncthreads()call acts as a barrier. No thread in the block proceeds until all threads have reached this point. This ensures theA_tileandB_tileare fully loaded into Shared Memory before the compute phase begins.8:

### The On-Chip Hardware: Banks and Warps

Shared Memory is a physical resource located on the Streaming Multiprocessor (SM). When a thread block is scheduled to run on an SM, it is allocated a portion of that SM’s total Shared Memory for its exclusive use.

The Shared Memory is physically partitioned into 32 independent memory modules of equal size, calledbanks. These banks can service memory requests in parallel. This number is not arbitrary; it is matched to thewarp size. Recall that a warp consists of 32 threads that execute instructions in lockstep, and it is the fundamental unit of memory access. The 32 banks are designed to serve, in parallel, the 32 memory requests from a single warp in one clock cycle, provided those requests target different banks.

Addresses, representing 4-byte words, are interleaved across the banks.

bank 0: [word 0, word 32, word 64, ...]
bank 1: [word 1, word 33, word 65, ...]
...
bank 31: [word 31, word 63, word 95, ...]

The bank for a given word address is determined bybank_id = address % 32.

### The Bank Conflict Problem

To achieve the full bandwidth of Shared Memory, the 32 threads of a warp must access words that fall into 32 different banks. Abank conflictoccurs when multiple threads access different addresses that map to the same bank. The hardware resolves this by serializing the requests, reducing bandwidth. Abroadcast, where all threads read thesameaddress, is a fast, conflict-free operation.

This creates a problem for matrix multiplication. Consider aBLOCK_DIM x BLOCK_DIMtile stored in Shared Memory in a row-major layout, whereBLOCK_DIM=32. The address oftile[row, col]isrow * 32 + col.

* Row Access (A_tile):A warp accessesA_tile[fixed_row, t]fort = 0..31. The addresses arefixed_row * 32 + t. The bank for each threadtis(fixed_row * 32 + t) % 32 = t % 32. Sincetis unique for each thread, the threads access 32 unique banks. This is a conflict-free, full-bandwidth access.
* Column Access (B_tile):A warp accessesB_tile[t, fixed_col]fort = 0..31. The addresses aret * 32 + fixed_col. The bank for each threadtis(t * 32 + fixed_col) % 32 = fixed_col % 32. All 32 threads target the same bank. This causes a 32-way bank conflict, serializing the memory access.

The solution is to store theB_tilein a transposed layout within Shared Memory.

# Action for thread (tx, ty) during the load phase
# A is loaded directly, B is loaded and transposed on-the-fly

A_tile
[
ty
,

tx
]

=

A_global
[
global_row

+

ty
,

global_k

+

tx
]

B_tile
[
tx
,

ty
]

=

B_global
[
global_k

+

ty
,

global_j

+

tx
]

# Indices are swapped

This “load-and-transpose” maneuver alters the on-chip computation. The calculation for an element of the partial product is no longer a dot product between a row ofA_tileand a column ofB_tile. Instead, using the transposed on-chipB_tile, the formula becomes:

\[C_{\text{partial}}[i,j] = \sum_{k} A_{\text{tile}}[i,k] \cdot B_{\text{tile}}[j,k]\]

In this formulation, a warp of threads computing differentjvalues for a fixediwill access a row fromA_tileand a row from the on-chipB_tile. Both are conflict-free access patterns. This single strategy solves both the HBM coalescing requirement and the SRAM bank conflict problem.

 Load-and-Transpose Operation (Thread tx, ty)
 Reads row-wise from HBM, writes column-wise to SRAM

 Global Memory (HBM) Shared Memory (SRAM)
 +-------------------------+ +-----------------------+
 | B[k_base+ty, j_base+tx] | -----> | B_tile[tx, ty] |
 +-------------------------+ +-----------------------+

 Result: HBM reads are coalesced, SRAM reads are conflict-free.

### E. The On-Chip Compute Phase: Increasing Arithmetic Intensity

With data staged in Shared Memory, the block performs the computation. The goal is to maximize data reuse from this fast on-chip memory. We will analyze two strategies for structuring this on-chip computation.

Strategy 1: One thread computes one output

The simplest approach maps one output element to one thread. ABLOCK_DIM x BLOCK_DIMthread block computes aTILE_DIM x TILE_DIMdata tile, whereBLOCK_DIMandTILE_DIMare equal. This strategy is conceptually similar toKernel 3inBoehm’s post, which introduces Shared Memory caching.9The hardware limit of 1024 threads per block constrainsBLOCK_DIMto be at most 32. Thread(tx, ty)is responsible for a single output elementC_partial[ty, tx].

# Action for a single thread (tx, ty) where BLOCK_DIM = TILE_DIM

c_accumulator

=

0.0

for

k

in

range
(
TILE_DIM
):


c_accumulator

+=

A_tile
[
ty
,

k
]

*

B_tile
[
tx
,

k
]

The arithmetic intensity for this strategy isTILE_DIM / 4.

* Total FLOPs:The block performs2 * TILE_DIM^3FLOPs.
* Total Bytes Accessed (HBM):The block loads two data tiles, totaling8 * TILE_DIM^2bytes.
* Arithmetic Intensity (AI):(2 * TILE_DIM^3) / (8 * TILE_DIM^2) = TILE_DIM / 4FLOPs/Byte.

WithTILE_DIMlimited to 32, the maximum AI is32 / 4 = 8. This is insufficient to cross the A100’s ridge point of ~13. The kernel remains memory-bound.

Strategy 2: One thread computes multiple outputs

To increase AI, we must increaseTILE_DIMwithout increasing the number of threads. This requires decoupling the data tile size from the thread block size. We assign more work to each thread. This strategy corresponds to the goal ofKernel 5inBoehm’s post.

A16x16thread block (BLOCK_DIM = 16, 256 threads) can compute a64x64data tile (TILE_DIM = 64). Each thread now computes a4x4sub-tile of the output. This requiresTILE_DIM=64to not exceed Shared Memory capacity.10

# A thread computes a 4x4 output sub-tile
# TILE_DIM = 64, BLOCK_DIM = 16

c_regs

=

[[
0.0
]

*

4

for

_

in

range
(
4
)]

a_regs

=

[
0.0
]

*

4

b_regs

=

[
0.0
]

*

4

for

k

in

range
(
TILE_DIM
):


# Load a sliver of A_tile and B_tile into registers


for

i

in

range
(
4
):

a_regs
[
i
]

=

A_tile
[
thread_row
*
4

+

i
,

k
]


for

j

in

range
(
4
):

b_regs
[
j
]

=

B_tile
[
thread_col
*
4

+

j
,

k
]


# Compute outer product in registers, accumulating into c_regs


for

i

in

range
(
4
):


for

j

in

range
(
4
):


c_regs
[
i
][
j
]

+=

a_regs
[
i
]

*

b_regs
[
j
]

The AI calculation remainsTILE_DIM / 4. WithTILE_DIM = 64, the AI is64 / 4 = 16FLOPs/Byte. This exceeds the A100’s ridge point. The kernel is nowcompute-bound.

A compute-bound kernel’s runtime is limited by the SM’s arithmetic throughput. This does not guarantee high absolute performance. A kernel can be compute-bound but still be slow if its FLOPs are inefficient (e.g., using scalar FP32 math instead of specialized hardware like Tensor Cores11) or if the GPU operates below its peak clock speed due to power limits.

The inner loop in the code above can be further optimized. A thread loads four separatefloatvalues fromA_tileintoa_regs. It can instead issue a single instruction to load a 16-bytefloat4vector. This vectorized load from Shared Memory reduces the number of instructions issued for on-chip data movement, improving the efficiency of the compute phase. This corresponds to the on-chip vectorization refinement used inKernel 6ofBoehm’s post.

A Final Consideration: Tile Quantization

If matrix dimensions are not multiples of the tile size, the kernel launches extra blocks that perform wasted computation.

To cover anM x Nmatrix withTILE_M x TILE_Ntiles, the GPU launches a grid ofceil(M/TILE_M) x ceil(N/TILE_N)thread blocks. Tiling a 65x65 matrix with 32x32 tiles requires aceil(65/32) x ceil(65/32)= 3x3 grid of blocks. The kernel’s logic is fixed; each block is programmed to perform the arithmetic for a full 32x32 tile.

 Columns 0-31 Columns 32-63 Columns 64-95
 +-----------------+-----------------+-----------------+
R 0 | | | |
o-31| Block 0,0 | Block 0,1 | Block 0,2 |
w | (Full work) | (Full work) | (Wasted work) |
s | | | |
 +-----------------+-----------------+-----------------+
R 32| | | |
o-63| Block 1,0 | Block 1,1 | Block 1,2 |
w | (Full work) | (Full work) | (Wasted work) |
s | | | |
 +-----------------+-----------------+-----------------+
R 64| | | |
o-95| Block 2,0 | Block 2,1 | Block 2,2 |
w | (Wasted work) | (Wasted work) | (Wasted work) |
s | | | |
 +-----------------+-----------------+-----------------+

According to NVIDIA, “While libraries ensure that invalid memory accesses are not performed by any of the tiles, all tiles will perform the same amount of math.” My understanding of why this happens (I’m happy to be corrected): Boundary blocks perform wasted work because the kernel explicitly pads the data. Threads assigned to load elements from outside the matrix bounds are prevented from doing so by a guard condition. Instead, they write zero to their location in the on-chip Shared Memory tile. The arithmetic loops are not shortened. The kernel’s logic is uniform across the tile. All threads in a warp execute the same multiply-add instructions. A thread whose data corresponds to a padded zero still executes the instruction; it just performs a useless computation, such asC += A * 0. The hardware resources are used, but the work is discarded.

## Additional Performance Considerations

We have made our kernel compute-bound. Its performance is now limited by the speed of its on-chip arithmetic. However, the kernel can still be made faster by managing additional aspects of the hardware. The following are three such considerations. There are others, but I’m not quite advanced enough to write about them, yet. SeeBoehm’s postfor others.

### Occupancy and Latency Hiding

A warpstallswhen it executes a long-latency instruction, such as a read from Global Memory. It cannot execute its next instruction until the data arrives, which can take hundreds of clock cycles. During this time, the SM’s compute units would be idle if the stalled warp were the only work available.

The SM hides this latency by executing other work. It can hold multiple thread blocks concurrently, creating a pool of resident warps. When one warp stalls, the SM’s hardware scheduler instantly switches to a different warp from this pool that is ready to run. This mechanism is calledlatency hiding.

+-------------------------------------------------------------------+
| Streaming Multiprocessor (SM) |
| |
| [Block A] [Block B] |
| - Warp A1 (Ready) - Warp B1 (Ready) |
| - Warp A2 (Stalled -> waiting on HBM) |
| | | |
| +------------------v------------------+ |
| [ Pool of Ready-to-Run Warps ] |
| [ A1, B1 ] |
| | |
| +-------v-------+ |
| | SM Scheduler | --> [Execute instructions] |
| +---------------+ |
| |
+-------------------------------------------------------------------+

Occupancyis the ratio of active warps on an SM to the maximum number it can support. High occupancy gives the scheduler a larger pool of warps to choose from. This increases the likelihood that it can find a ready warp to execute at any given cycle, keeping the compute units active.

This leads to a trade-off between the resources used per block and the number of blocks that can reside on an SM. The two extremes can be visualized as follows:

+------------------------------------+ +----------------------------------------------+
| SM with High AI, Low Occupancy | | SM with Low AI, High Occupancy |
| | | |
| +--------------------------------+ | | +----------+ +-----------+ +-----------+ |
| | Block 0 (uses 64KB SMEM) | | | | Block 0 | | Block 1 | ... | Block N | |
| | TILE_DIM=128 -> High AI | | | | (8KB SMEM) | (8KB SMEM)| | (8KB SMEM)| |
| +--------------------------------+ | | +----------+ +-----------+ +-----------+ |
| | | |
| --> Low # of resident blocks. | | --> High # of resident blocks. |
| --> Small pool of warps for | | --> Large pool of warps for |
| latency hiding. | | latency hiding. |
+------------------------------------+ +----------------------------------------------+

We tune the kernel’s resource usage to balance the benefit of high AI against the necessity of sufficient occupancy. The primary levers for this tuning are the thread block dimensions (BLOCK_DIM), the amount of Shared Memory allocated per block (determined byTILE_DIM), and the number of registers used per thread.12

### Avoiding Thread Divergence

A conditional branch (if-else) where threads in a warp disagree on the outcome causesthread divergence.13When this occurs, the hardware resolves the divergence by executing the different code paths serially. First, threads that take theifpath execute it while the others are inactive. Then, the roles are reversed for theelsepath.

# A warp of 32 threads encounters an `if` statement:

if

(
thread_id

<

16
)


# Path A

else


# Path B

Execution

Timeline
:

Time

->

+------------------------------------------------------------------+

|

Warp

Execution

|

|

|

|

Cycle

1
:

Path

A

is

executed
.

|

|

-

Threads

0
-
15
:

Active
,

execute

Path

A

code
.

|

|

-

Threads

16
-
31
:

Inactive
,

masked

off
.

|

|

|

|

Cycle

2
:

Path

B

is

executed
.

|

|

-

Threads

0
-
15
:

Inactive
,

masked

off
.

|

|

-

Threads

16
-
31
:

Active
,

execute

Path

B

code
.

|

|

|

|

Result
:

Two

cycles

are

required

instead

of

one
.

|

|

Effective

throughput

is

halved
.

|

+------------------------------------------------------------------+

This serialization doubles the execution time of the divergent code, halving the warp’s effective throughput. We avoid this cost by writing branchless code in performance-critical sections, using primitives likeminandmaxinstead ofif-else.

### Quantization

Quantization reduces precision of elements of our tensor, from, say FP32 to FP16 or BFP16. This has two effects. First, it reduces the memory needed to store each element, for example, by 2. Thus, we can transfer twice as many elements per second from global memory to shared memory. This increases AI by 2.

Second, GPUs, such as the A100, can operate faster on lower precision elements. For example, on an A100, 312 TFLOPS are achievable for certain FP16 operations, whereas FP32 operations are limited to 19.5 TFLOPS. Thus, theoretically we can speedup computation by a factor of 16.

Quantization can therefore move us up and to the right on the Roofline plot.

1. I learned fromthis postthat one should take these “peak” numbers with a grain of salt, since power limits effect clock speed.↩
2. The (peak) 19.5 TB/s figure for shared memory is derived as follows: $32 \text{ banks} \times 4 \text{ bytes per bank cycle} \times 1.41 \text{ GHz clock} \times 108 \text{ SMs} = 19.5 \text{ TB/s}$. Note that read and write are on independent ports, so the bandwidth is doubled in some sense.↩
3. Apparently, these numbers are not released by NVIDIA. I didn’t bother tracking them down because the main point is that this is the fasted memory to read and write from.↩
4. Modern GPUs (e.g., A100s) actually haveIndependent Thread Scheduling(ITS). See page 14 and beyond ofthis documentfor a nice introduction to ITS. In particular, the authors write that in ITS, “[e]ach thread is given its own, individual program counter, meaning that theoretically, each thread can store its own unique instruction that it wants to perform next. The execution of threads still happens in warps, this has not changed. It is not possible for threads in a warp to perform different instructions in the same cycle. However, a warp may now bescheduled to progress at any of the different program counters that the threads within it are currently holding. Furthermore, ITS provides a“progress guarantee”: eventually, over a number of cycles, all individual program counters that the threads in a warp maintain will be visited. Thismeans that if, for instance, the execution has diverged and two branches, both are guaranteed to be executed sooner or later.” While ITS allows one to write correct branching code a bit more easily than in older architectures, one should still strive to write code where warps operate as much as possible in lockstep, so we can take advantage of the maximal number of parallel lanes.↩
5. This also assumes that we can load the entire column of the matrix into the set of registers belonging to a single thread. Since each SM has a register file of size 256 KB, this not possible for large matrices.↩
6. SeeMaking Deep Learning Go Brrrr From First Principlesfor more on overhead.↩
7. BTW aspointed out by Horace He), this effect explains whypadding a model’s vocabulary size can improve performance.↩
8. With Independent Thread Scheduling, we cannot rely on implicit synchronization between threads in a warp. Correctness requires an explicit barrier like__syncthreads()to guarantee that, for example, all data is written to Shared Memory before any thread reads it.↩
9. This post solves HBM coalescing (likeKernel 2) and SRAM bank conflicts (which Boehm addresses for matrix A inKernel 6) simultaneously by transposing the B tile on-chip. Therefore, this strategy is a bit more advanced than the one inBoehm’sKernel 3, which introduces Shared Memory but still suffers from bank conflicts.↩
10. Two64x64tiles of 4-byte floats require2 * 64 * 64 * 4 = 32768bytes (32 KB) of Shared Memory. This fits within the 48 KB available to a block on an A100 under default configuration. A kernel can request more (up to 100KB), but this reduces the number of thread blocks that can run concurrently on an SM, a trade-off with occupancy.↩
11. Tensor Coresare specialized hardware units on NVIDIA GPUs that execute matrix-multiply-accumulate (D = A@B + C) operations. On Ampere GPUs, they accelerateFP32inputs by first rounding them to theTensorFloat-32 (TF32)format. TF32 uses the same 8-bit exponent asFP32but only a 10-bit mantissa, matching the precision ofFP16. The internal accumulation is performed inFP32. This process is the default for some operations in deep learning frameworks, offering a speedup at the cost of lower precision. For maximum throughput, Tensor Cores also operate on formats likeFP16,BF16, andINT8. BTW how can they get away with calling TF32, TF32, when it is lossy!↩
12. The SM has a finite physical Register File (e.g., 65,536 32-bit registers on an A100). The total number of registers a block requires is(threads per block) * (registers per thread). The SM can only host as many concurrent blocks as can fit within its Register File and Shared Memory capacity. Therefore, using more registers per thread reduces the number of blocks that can be resident, lowering occupancy. The compiler allocates registers to warps in fixed-size chunks, so, e.g., a kernel requesting 33 registers per thread may be allocated 40, further impacting this resource calculation.↩
13. Independent Thread Scheduling does not eliminate the cost of divergence. While each thread has its own Program Counter (PC), a register pointing to the next instruction, the warp is still managed by a scheduler that can only issue an instruction from a single address per cycle. When PCs within a warp diverge, the scheduler must serially execute each unique path, leaving all other threads idle. The simplifiedif-elsemodel in the main text is thus still an accurate description of thread divergence since serialization diminishes the warp’s parallelism.↩
