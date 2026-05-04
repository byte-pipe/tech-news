---
title: How Monero’s proof of work works · Technical Blog · Alcazar Security
url: https://blog.alcazarsec.com/tech/posts/how-moneros-proof-of-work-works
site_name: hnrss
content_file: hnrss-how-moneros-proof-of-work-works-technical-blog-alc
fetched_at: '2026-05-04T20:14:22.417440'
original_url: https://blog.alcazarsec.com/tech/posts/how-moneros-proof-of-work-works
date: '2026-05-04'
published_date: '2026-04-27'
description: Monero does not use a simple fixed hash like Bitcoin. Its proof of work, RandomX, turns mining into running random CPU-friendly programs over a large memory dataset, which is why it behaves so differently from ASIC-first systems.
tags:
- hackernews
- hnrss
---

Published Apr 27, 2026

 

# How Monero’s proof of work works

 
Ask AI
 
 
ChatGPT
 
ChatGPT
 
Claude
 
Claude
 
Gemini
 
Gemini
 
Perplexity
 
Perplexity
 
Grok
 
Grok
 
Duck.ai
 
Duck.ai
 

Monero’s proof of work is calledRandomX.

 

Monero doesnotask miners to run the same tiny hash function over and over. It asks them to run a small random program on a virtual machine, hit memory hard while doing it, and then hash the result.

 

Bitcoin’s proof of work is great for specialized chips because the work never changes. RandomX was built to do the opposite. It tries to make efficient mining look as much like a normal CPU workload as possible.

 

## Short version

 

Here is the shortest useful summary:

 
1. Monero takes the candidate block header plus a nonce.
2. It also uses an older block hash as a medium-term key.
3. That key builds a large shared memory dataset.
4. The candidate block input is hashed to create a seed for a special virtual machine.
5. The VM runs integer math, floating-point math, branches, and lots of memory accesses across8 chained programs.
6. The final machine state is hashed into a 256-bit output.
7. If that output is below the network target, the block is valid.
 

The interesting part is not the yes-or-no rule at the end. Every proof-of-work system has that. The interesting part is how Monero makes each hash attempt expensive in the exact ways normal CPUs are good at and custom chips hate.

 

## Why Monero does not use a simple hash

 

If your proof of work is just “run this fixed function on new inputs until you get a lucky output,” hardware designers have a clear job: build silicon that runs that exact function as cheaply and as fast as possible.

 

That is what happened to Bitcoin with SHA-256 ASICs.

 

Monero did not want that path. Long before RandomX, the project was explicit that specialized mining hardware creates centralization pressure. Fewer manufacturers matter more. Large farms matter more. Ordinary users matter less.

 

Monero’s earlier answer was theCryptoNightfamily. Later, in late2019, Monero switched toRandomX, which its own release notes described as a new proof of work “based on random instructions, adapted to CPUs.”

 

So the design target changed frommake memory mattertomake a whole CPU matter.

 

## The core idea behind RandomX

 

RandomX starts from one observation: CPUs are not just arithmetic boxes. They are flexible machines built to run changing code and juggle a lot of hardware features at once.

 

A modern CPU has:

 
* multiple cache levels
* integer units
* floating-point units
* branch handling
* out-of-order execution
* speculative execution
* memory controllers
 

Normal cryptographic hashes do not use much of that variety. They mostly push data through a fixed pipeline.

 

RandomX tries to bind proof of work to those broader CPU strengths. Its design document says the work must bedynamic. That means the miner is not just feeding in new data. The miner is also getting new code to run.

 

That is why RandomX is based onrandom code execution.

 

## What a miner is actually computing

 

At the Monero level, RandomX takes two important inputs:

 
* akeyK
* ahashing inputH
 

For Monero,Kcomes from an older block hash, called thekey block. The RandomX reference README recommends changing this key every2048 blockswith a64-block delay, and that is how Monero wires it in.

 

That detail matters because miners donotrebuild the heavy shared memory structures for every nonce. They rebuild them only when the key changes, roughly every2.8days.

 

His the candidate block hashing blob with a chosen nonce. That is the part miners keep changing over and over.

 

So you can think of Monero mining like this:

 
* the network gives you a medium-term environment throughK
* your candidate block gives you a per-attempt input throughH
 

The environment changes slowly. The attempt changes constantly.

 

## Step 1: build the cache from the key

 

RandomX first takes the keyKand runsArgon2don it.

 

Argon2d is better known as a password-hashing and key-derivation function. It is useful here for the same reason it is useful there: it ismemory-hard. It forces the machine to touch a lot of memory in a way that is annoying to cheat.

 

In the default RandomX parameters, this produces a256 MiB cache.

 

That cache is the smaller of the two big memory structures in RandomX. It is not the structure miners want to use directly for maximum speed. It is the structure used to build the bigger one.

 

## Step 2: expand the cache into the dataset

 

From that 256 MiB cache, RandomX builds thedataset.

 

The default dataset size is:

 
* 2,147,483,648bytes base size
* 33,554,368bytes extra size
 

Together that is about2080 MiB, a little over2 GiB.

 

This odd-looking size is deliberate. It is big enough to spill out of on-chip memory and into DRAM, and the extra non-power-of-two tail makes life more annoying for hardware designers.

 

The dataset is read-only during hashing. RandomX uses it to force regular DRAM traffic. The design doc says each program iteration reads one 64-byte dataset item, and across a whole hash result that becomes16,384 dataset reads.

 

That gives RandomX one of its main bottlenecks: memory access, not just arithmetic.

 

## Step 3: initialize the scratchpad from the block input

 

Now RandomX turns to the per-hash inputH.

 

It computesHash512(H)usingBlake2b. That 64-byte result seeds an AES-based generator, which fills thescratchpad.

 

The scratchpad is the VM’s working memory. Unlike the large dataset, it is meant to live in CPU cache, not DRAM.

 

Its default size is2 MiB, split to mimic CPU cache levels:

 
* 16 KiBL1
* 256 KiBL2
* 2 MiBL3
 

This is one of the smartest parts of RandomX. It uses two very different memory structures at once:

 
* abig datasetto hit DRAM
* asmaller scratchpadto behave like cache-heavy code
 

That lets it pressure both the memory subsystem and the CPU core.

 

## Step 4: generate a random program

 

After the scratchpad is ready, RandomX generates a program for its virtual machine.

 

This is not a C program or a JavaScript program. It is a compact VM program with its own instruction set.

 

Two details matter a lot:

 
1. Every instruction is8 byteslong.
2. Any 8-byte word is a valid instruction.
 

That second choice is a big deal. It means RandomX can generate programs by just filling a buffer with random bytes. There is no slow parser and no complicated syntax checking.

 

Each program contains256 instructions.

 

Those instructions are chosen to look like work real CPUs are built for:

 
* integer math
* 64-bit multiplies
* floating-point operations
* 128-bit vector operations
* memory loads and stores
* occasional branches
 

The floating-point side is not cosmetic. RandomX uses IEEE 754 double precision operations, including division and square root, and it uses all four standard rounding modes. That makes the VM harder to collapse into a tiny “mostly integer” custom design.

 

## Step 5: run the program loop

 

The VM executes the 256-instruction program in a loop for2048 iterations.

 

During each iteration it:

 
* reads and writes scratchpad memory
* prefetches and loads dataset items
* mixes integer and floating-point register state
* takes a low-probability branch when the condition says so
 

The design doc says an average iteration reads about504 bytesfrom memory and writes about256 bytes.

 

That number is a clue to what RandomX is really doing. It is not “a hash with extra steps.” It is trying to behave like messy, mixed, real software.

 

## Why the branches are there

 

Branches are easy to overlook, but they matter.

 

If the code were fully straight-line, specialized hardware could optimize away more of it. Branches make static simplification harder.

 

RandomX uses branches sparingly. A branch is taken with probability about1/256, and the design intentionally makes these branches usually predict as “not taken.” That means they are cheap on CPUs most of the time, while still getting in the way of over-optimized hardware shortcuts.

 

The important point is not that RandomX found some magic branch predictor trick. It did not. The point is that even a little real control flow makes the workload look more like actual code and less like a clean hardware pipeline.

 

## Why there are 8 chained programs per hash

 

One random program is not enough.

 

If miners only had to run a single random program, a dishonest miner could try to inspect the program first and skip “bad” ones. Or a custom chip designer could support only the subset of programs that are easy for their hardware.

 

RandomX blocks that by chaining8 programstogether.

 

The output state of one program becomes the seed for the next. So once you start, you cannot know the whole chain in advance. You either finish the chain or throw away work you already paid for.

 

This is one of the cleanest ideas in RandomX. It turns “maybe I will only do the easy jobs” into a bad strategy.

 

## Step 6: collapse the final state into a hash

 

After the last of the 8 programs finishes, RandomX still has to turn all that machine state into one final digest.

 

It does two things:

 
1. It fingerprints the whole scratchpad with an AES-based hash.
2. It combines that with the VM register file and runs a finalBlake2b-based 256-bit hash.
 

That final 256-bit result is the RandomX output.

 

At the Monero level, the miner checks whether that result is below the current difficulty target. If yes, the block wins. If no, the miner changes the nonce and tries again.

 

## Fast mode and light mode

 

RandomX has two modes:

 
* fast mode, which uses the full2080 MiBdataset
* light mode, which uses only the256 MiBcache and computes dataset items on the fly
 

Both modes give thesame answer.

 

Verification has to agree with mining, but the two modes do not cost the same amount of work.

 

Fast mode is for mining. Light mode is for verification. The reference README says exactly that, and this split is one of RandomX’s best design choices.

 

If every verifier needed more than2 GiBjust to check one proof of work, that would be ugly. If light mode were cheap enough to mine competitively, that would also be ugly. RandomX tries to stay in the middle: verification should be practical, but not attractive as a mining shortcut.

 

The design document explicitly aims for light mode to lose on the memory-time tradeoff. In plain English, if you save memory, you should pay back that advantage in extra work.

 

## Why this is CPU-friendly

 

“CPU-friendly” can sound like marketing, so it is worth being specific.

 

RandomX favors CPUs because it leans on the things good CPUs already have:

 
* large caches
* decent DRAM bandwidth
* hardware AES
* fast 64-bit math
* floating-point hardware
* out-of-order execution
* dynamic code generation
 

The reference implementation even includes JIT compilers forx86-64,ARM64, andRISCV64, so the VM programs can be translated into native machine code on the fly instead of being interpreted instruction by instruction.

 

That does not make ASICs impossible forever. Nothing honest should claim that. What it does is make the custom-chip job much uglier. A good RandomX ASIC starts looking less like a neat fixed-function hash engine and more like “build a weird expensive CPU with a lot of memory attached.” That shrinks the advantage.

 

## What RandomX is trying to buy Monero

 

RandomX is not mainly about raw speed. It is abouthardware economics.

 

Monero wants proof of work that:

 
* keeps mining more open to ordinary hardware
* reduces the edge from fixed-function ASICs
* avoids tying consensus to a few hardware vendors
* stays reasonably cheap to verify
 

That is why RandomX looks so strange if you expect a normal mining hash.

 

It is not trying to be elegant in the Bitcoin sense. It is trying to be awkward for specialization.

 

## The simplest way to think about it

 

If Bitcoin mining is “run this one small machine forever,” Monero mining is “keep generating little CPU-flavored workloads and survive the memory traffic.”

 

That is the shortest mental model I know that is still true.

 

Under the hood, RandomX is a stack of careful choices:

 
* Argon2d to build a cache
* a 2 GiB-plus dataset to force DRAM access
* a cache-sized scratchpad to exercise local memory
* a VM with random programs
* integer, floating-point, vector, and branch instructions
* 8 chained programs to stop easy-program filtering
* a fast mode for miners and a light mode for verifiers
 

Put those together and you get Monero’s proof of work today.

 

It is not simple. But the point is simple:make mining look like general-purpose computing, so specialized hardware gets less room to run away with the network.

 
← Back to Tech Log
 

Leave the right message behind

 

Set up encrypted messages, files, and instructions for the people who would need
 them most if something happened to you.

 
 
See the dead man's switch