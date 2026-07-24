---
title: Characterizing Metastable Faults and Failures
url: https://muratbuffalo.blogspot.com/2026/07/characterizing-metastable-faults-and.html
site_name: tldr
content_file: tldr-characterizing-metastable-faults-and-failures
fetched_at: '2026-07-24T11:35:03.232083'
original_url: https://muratbuffalo.blogspot.com/2026/07/characterizing-metastable-faults-and.html
date: '2026-07-24'
description: Characterizing Metastable Faults and Failures (8 minute read)
tags:
- tldr
---

### Characterizing Metastable Faults and Failures

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

-

July 22, 2026

Metastabilityhas been studied in previous work as a self-sustaining degradation in goodput that persists even after the trigger is gone. The degraded state loiters on entirely due to the system's own internal feedback loops (retries, queues), and there is no simple reset button to press in distributed systems. So this is not a rare exotic problem. Since production systems would have already been hardened to handle the obvious failures, what remains is these hard-to-detect emergent failures.The "Metastable Failures in the Wild" paper (OSDI'22)reports 22 incidents across 11 organizations. Four of the 15 major AWS outages in a decade were metastable failures, with durations ranging from 1.5 to 73 hours.

This paper (June 2026)argues that the systems community has treated metastability phenomenologically, which led people to chase symptoms rather than causes. The paper sets out to give the first analytical causal account of these failures. This framing leads to two connections I found delightful. The first casts a metastable failure asa sin of compositionamong self-stabilizing systems. The second ties the healing mechanism to scheduling. Since I have worked on self-stabilizing systems for a long time (between 1998-2010), and thought hard about how they compose, these two connections really excite me.

I do have some reservations, though, which I will get to in my review. The paper overlooks prior work on the composition of stabilizing systems. It also pulls a bit of a sleight-of-hand in its formalization to argue that the metastable fault tolerance (MFT) design can be done via local pairwise reasoning between components. I don't buy that as I explain below.

These reservations do not dampen how much I enjoyed this paper. This is an idea paper, and it has been a while since I saw one of these in distributed systems. Moreover, the author list includes two of my all-time favorite distributed systems researchers: Robbert Van Renesse and Lorenzo Alvisi.

So let's dive in.

## Sins of Composition and Self-Stabilization

The authors give formal definitions of ametastable faultand ametastable failure, and they draw a distinction between the two.

A metastable fault is what they beautifully call asin of composition. (I am guessing this is Lorenzo being poetic.) Loosely speaking, the metastable fault appears when two or more components that are perfectly stable on their own get wired together into a cyclic interference/destruction loop. When a shock (say overload or loss of cache) then triggers the system, each component runs its local corrective action to stabilize itself, and in doing so it destabilizes its neighbor.

Let me back up and explainself-stabilization. Aself-stabilizing systemcan start in any state and, with no outside intervention, converge on its own to a legitimate state and stay there. It lays outan elegant unified frameworkto tolerate any transient fault: A transient fault just leaves the system in some arbitrary state, and stabilization gradually heals it from there.

The paper leans hard on this stabilization theory going back to the 1980s. It defines apotential function(also called a variant or metric function) $f$ for each component, measuring how far the component is from a good state. A component is stabilizing if it eventually drives $f$ to zero, provided it runs inside a well-behaved "environment" $E$.

To formulate composition of stabilizing components, they add a compatibility check: if component A can stabilize when B is stable, and B can stabilize when A is stable, the two are compatible. But compatibility is not enough for guaranteeing composition of stabilization. Right after a shock, neither component is stable, so they hit a bootstrapping problem. Each waits for the other to recover first, and they get stuck in mutual destabilization, as their actions during recovery interfere with each other's healing progress.

This "sin of composition" is defined as the metastable fault. The fault turns into a failure only when the shock lands and the system'sschedulerkeeps favoring the locally stabilizing but globally destabilizing interactions over the stabilizing ones.

None of this surprises a stabilization researcher. Stabilization is famously hard to compose, precisely because the recovery strategies of the components interfere with each other. The challenge is to keep the components from corrupting each other during recovery. One clean way is layered composition: let the lower layer stabilize first (the higher layer can read it but not write to it), and let recovery flow upward. In general, though, when you compose systems you have to design the correction actions deliberately, check that they don't interfere, and prove they stabilize together.

## Overreaching for Local Reasoning

The paper's theoretical framework defines metastability nicely, however, I disagree with the claim that finding and fixing the fault is a local pairwise activity. That claim rests on the developer guessing the right potential function $f$ and the right environment predicate $E$. And it is not possible to derive a good potential function without reasoning about the system globally.

It is also worthwhile to discuss about the environment predicate $E$. In the classical stabilization literature, $E$ is usually trivial or vacuous, because a self-stabilizing system is supposed to recover from any state. The paper improves on this for compositionality by defining $E$ to capture the assumption that a component's neighbors behave well. But this generalization punts the hard parts to the developer: which environment predicate actually holds for the composed components, and which potential function is right for each component. These are questions that require global reasoning. Assuming a benevolent environment predicate $E$ in which everything else behaves perfectly ignores the reality that in a distributed system the "environment" is the other components, which are just as likely to be failing. Note that both the  Definition 3 (compatibility) and Definition 4 (destabilizing action) quantify over a single global environment predicate E for the whole composition.

So the paper gets handwavy and overreaches when it claims MFT is decompositional. Section 4.3 states that locating a metastable fault "does not require a global analysis" and "replaces reasoning about the entire composition with local, decompositional reasoning about pairs of components."

## Use the Graph to Fix, Not Just to Flag

The authors extract a composition blueprint, a directed graph ofwrites-torelations among components, which they search for cycles of destabilizing actions. But they use the graph only defensively, to flag faults. Once a fault is found, the proposed fix is to hand-inject ad-hoc timers that delay the destabilizing actions.

This leaves the constructive side of self-stabilization on the table. Leal and Arora's "Scalable self-stabilization via composition" (ICDCS 2004) showed you can enforce correct composition by leveraging this graph directly. The motivation for Leal (my academic brother) and Arora (my advisor) was to address the interference problem between actions which forces global reasoning over the whole system, and that reasoning explodes as systems grow. The key idea in their framework was to make two relations explicit: for each component, which other components it can corrupt, and which components must be corrected first before it can correct itself. Given per-component stabilizers (detectors and correctors), they offer several ways to coordinate correction depending on what you actually know about the corruption and correction relations. This framework aims to reduce design and reasoning to local activity between a component and its neighbors in order to allow local recovery and avoid blocking of components and distributed reset as much as possible. In other words, it proposed atopologicalanswer to the sins of composition. Instead of guessed empirical timers and tentative scheduling, you use the direction of the edges to enforce the scheduling discipline.

I ran into a similar problem in my own work, "A hierarchy-based fault-local stabilizing algorithm for tracking in sensor networks". There we used layered/hierarchical healing, and tuned the timing of the corrective actions: we deliberately delayed the propagation waves of correction to higher levels of the hierarchy, so that more recent waves from lower levels could catch up. That delay gave us fault-local stabilization instead of a global cascade of corruption.

## Scheduling as a First-Class Citizen

The paper also introduces Nyx, a DSL that forces you to model queues and resources explicitly and promotes the scheduler to a first-class citizen. The goal is to defer destabilizing interactions until stabilizing ones have achieved global stability. I like the intuition, but I think the paper reaches too far, and assumes a "God scheduler" that can serialize and control all concurrent actions from above. A central coordinator like that does not scale, and is not feasible to have in distributed systems. But the good news is that once you have framed the problem as a scheduling problem, you may not need a God scheduler to fix it. You can implement the fix with locally tuned timers. You don't have to be perfect; you only have to rig the odds toward stabilization.

Reading this paper gave me a concrete next step for MESSI, the metastability simulator tool Aleksey Charapko had developed to catch failures that hide in the seams between system components. We introduced MESSI in our recent paper, "A Case for Simulation-Driven Resilience in Agentic Data Systems". It models any subsystem as a graph of Logic Nodes (which express policy: where does this work go next?) and Processors (which express resource constraints, via delays for both service time and queuing time). Runs are deterministic and replayable, with full internal state captured every tick, and the runtime is scriptable, so you can inject failures, slowdowns, and config changes mid-run. The premise here is that production is too complex to tune by trial and error, so we need to trace how overload propagates before we deploy. To explore the effects of scheduling in MESSI,  we can add a ~SendAt()~ method, that allows delaying a potentially destabilizing message by a prescribed amount.

In sum, this is a thought-provoking paper. It correctly reframes metastability: not a mere symptom of overload, but a fundamental failure of recovery to compose across distributed boundaries. A metastable fault becomes a failure only under destructive interference among components. I think the paper's formal verification framework demands too much subjective guesswork to be practical, and its bet on the scheduler as a central coordinator may not be feasible. But the diagnosis of metastability is really a good one. Once you can name the interference (the sin of composition), accounting for it becomes a much more tractable problem.

Finally, I am adding a link to mymarked up copy of the paper. Even with the availability of LLMs, I still believe indeepmanualreading, and illustratingone's thought-processesto teach/train others.

metastability

paper-review

stabilization

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Popular posts from this blog

### Hints for Distributed Systems Design

-

October 02, 2023

This is with apologies to Butler Lampson, who published the " Hints for computer system design " paper 40 years ago in SOSP'83. I don't claim to match that work of course. I just thought I could draft this post to organize my thinking about designing distributed systems and get feedback from others. I start with the same  disclaimer Lampson gave. These hints are not novel, not foolproof recipes, not laws of design, not precisely formulated, and not always appropriate. They are just hints.  They are context dependent, and some of them may be controversial. That being said, I have seen these hints successfully applied in distributed systems design throughout my 25 years in the field, starting from the theory of distributed systems (98-01), immersing into the practice of wireless sensor networks (01-11), and working on cloud computing systems both in the academia and industry ever since. These heuristic principles have been applied knowingly or unknowingly and has proven...

Read more >>

### Chess invariants

-

May 21, 2026

Chess is a lot trickier than it looks. It has so many rules: castling, en passant, pawn promotion, pinning, the discovered check, and the deadlock case of stalemate. It is a concurrent system, but with a very specific kind of concurrency: interleaved execution. More specifically, taking turns: white, then black, then white. You know what we do with concurrent systems here? Here we model them, and we distill their invariants. Here is some setup definitions first. In a CS or math paper, if you write "Section 2: Model and Problem" well enough, the rest of the paper writes itself. With this setup you can sort of see what the actions will be. In fact, forget about the actions. Let's look at some invariants. Invariants When deriving invariants we ask: what must always be true? I find it useful to split the safety invariants into two camps: state invariants (which are predicates over a single state) and transition invariants (which are predicates over a step). The transition inv...

Read more >>

### The Agentic Self: Parallels Between AI and Self-Improvement

-

January 02, 2026

2025 was the year of the agent. The goalposts for AGI shifted; we stopped asking AI to merely "talk" and demanded that it "act". As an outsider looking at the architecture of these new agents and agentic system, I noticed something strange. The engineering tricks used to make AI smarter felt oddly familiar. They read less like computer science and more like … self-help advice . The secret to agentic intelligence seems to lie in three very human habits: writing things down, talking to yourself, and pretending to be someone else. They are almost too simple. The Unreasonable Effectiveness of Writing One of the most profound pieces of advice I ever read as a PhD student came from Prof. Manuel Blum, a Turing Award winner. In his essay "Advice to a Beginning Graduate Student", he wrote: "Without writing, you are reduced to a finite automaton. With writing you have the extraordinary power of a Turing machine." If you try to hold a complex argument enti...

Read more >>

### Learning about distributed systems: where to start?

-

June 10, 2020

This is definitely not a "learn distributed systems in 21 days" post. I recommend a principled, from the foundations-up, studying of distributed systems, which will take a good three months in the first pass, and many more months to build competence after that. If you are practical and coding oriented you may not like my advice much. You may object saying, "Shouldn't I learn distributed systems with coding and hands on? Why can I not get started by deploying a Hadoop cluster, or studying the Raft code." I think that is the wrong way to go about learning distributed systems, because seeing similar code and programming language constructs will make you think this is familiar territory, and will give you a false sense of security. But, nothing can be further from the truth. Distributed systems need radically different software than centralized systems do.  --A. Tannenbaum This quotation is literally the first sentence in my distributed systems syllabus. Inst...

Read more >>

### 5 Lessons at 50

-

June 24, 2026

Looking at my peak male physique, and my Keanu Reeves baby face, you would never suspect it, but I recently turned 50. As is the tradition, I thought about writing a post titled "50 Lessons at 50". Unfortunately, I don't have that kind of wisdom. The thing is, I still feel like I'm 18, same age as my son. Turns out this is the secret old guys have been hiding from us all along. You get older only on the outside, but inside you still see yourself as the same young lad. Still, fifty years should count for something. So what did I actually learn? How am I mentally different than my 18-year-old self. Here is my attempt to tally it up.  1. Caution is warranted I finally understand my parents. As you age, you accumulate battle scars, and the scars turn into habits. Anything that can go wrong will go wrong. You forget the cooktop on once, and suddenly you check it three times before leaving the house. True story. You stop diving head-first into a pile of leaves, because ther...

Read more >>

### Foundational distributed systems papers

-

February 27, 2021

I talked about the importance of reading foundational papers last week. To followup, here is my compilation of foundational papers in the distributed systems area. (I focused on the core distributed systems area, and did not cover networking, security, distributed ledgers, verification work etc. I even left out distributed transactions, I hope to cover them at a later date.)  I classified the papers by subject, and listed them in chronological order. I also listed expository papers and blog posts at the end of each section. Time and State in Distributed Systems Time, Clocks, and the Ordering of Events in a Distributed System. Leslie Lamport, Commn. of the ACM,  1978. Distributed Snapshots: Determining Global States of a Distributed System. K. Mani Chandy Leslie Lamport, ACM Transactions on Computer Systems, 1985. Virtual Time and Global States of Distributed Systems.  Mattern, F. 1988. Practical uses of synchronized clocks in distributed systems. B. Liskov, 1991. Exp...

Read more >>

### Building a Database on S3

-

March 04, 2026

Hold your horses, though. I'm not unveiling a new S3-native database. This paper is from 2008. Many of its protocols feel clunky today. Yet it nails the core idea that defines modern cloud-native databases: separate storage from compute. The authors propose a shared-disk design over Amazon S3, with stateless clients executing transactions. The paper provides a blueprint for serverless before the term existed. SQS as WAL and S3 as Pagestore The 2008 S3 was painfully slow, and 100 ms reads weren't unusual. To hide that latency, the database separates "commit" from "apply". Clients write small, idempotent redo logs to Amazon Simple Queue Service (SQS) instead of touching S3 directly. An asynchronous checkpoint by a client applies those logs to B-tree pages on S3 later. This design shows strong parallels to modern disaggregated architectures . SQS becomes the write-ahead log (WAL) and logstore. S3 becomes the pagestore. Modern Aurora follows a similar logic : t...

Read more >>

### Cloudspecs: Cloud Hardware Evolution Through the Looking Glass

-

January 09, 2026

This paper (CIDR'26) presents a comprehensive analysis of cloud hardware trends from 2015 to 2025, focusing on AWS and comparing it with other clouds and on-premise hardware. TL;DR: While network bandwidth per dollar improved by one order of magnitude (10x), CPU and DRAM gains (again in performance per dollar terms) have been much more modest. Most surprisingly, NVMe storage performance in the cloud has stagnated since 2016. Check out the NVMe SSD discussion below for data on this anomaly. CPU Trends Multi-core parallelism has skyrocketed in the cloud. Maximum core counts have increased by an order of magnitude over the last decade. The largest AWS instance u7in now boasts 448 cores. However, simply adding cores hasn't translated linearly into value. To measure real evolution, the authors normalized benchmarks (SPECint, TPC-H, TPC-C) by instance cost. SPECint benchmarking shows that cost-performance improved roughly 3x over ten years. A huge chunk of that gain comes from AWS G...

Read more >>

### TLA+ modeling tips

-

December 15, 2025

Model minimalistically Start from a tiny core, and always keep a working model as you extend. Your default should be omission. Add a component only when you can explain why leaving it out would not work. Most models are about a slice of behavior, not the whole system in full glory: E.g., Leader election, repair, reconfiguration. Cut entire layers and components if they do not affect that slice. Abstraction is the art of knowing what to cut . Deleting should spark joy.  Model specification, not implementation Write declaratively. State what must hold, not how it is achieved. If your spec mirrors control flow, loops, or helper functions, you are simulating code. Cut it out. Every variable must earn its keep. Extra variables multiply the state space (model checking time) and hide bugs. Ask yourself repeatedly: can I derive this instead of storing it? For example, you do not need to maintain a WholeSet variable if you can define it as a state function of existing variables: WholeSet =...

Read more >>

### Supporting our AI overlords: Redesigning data systems to be Agent-first

-

September 17, 2025

This Berkeley systems group paper opens with the thesis that LLM agents will soon dominate data system workloads. These agents, acting on behalf of users, do not query like human analysts or even like the applications written by them. Instead, the LLM agents bombard databases with a storm of exploratory requests: schema inspections, partial aggregates, speculative joins, rollback-heavy what-if updates. The authors calls this behavior agentic speculation . Agentic speculation is positioned as both the problem and the opportunity. The problem is that traditional DBMSs are built for exact intermittent workloads and cannot handle the high-throughput redundant and inefficient querying of LLM agents. The opportunity also lies here. Agentic speculation has recognizable properties and features that invite new designs. Databases should adapt by offering approximate answers, sharing computation across repeated subplans, caching grounding information in an agentic memory store, and even steering...

Read more >>