---
title: 'Crows, Moths, and Makefiles: How 300 Megabytes of Crow DNA Explains Why a 20-Kilobyte Scar File Outsmarts a Terabyte LLM - DEV Community'
url: https://dev.to/gde/crows-moths-and-makefiles-how-300-megabytes-of-crow-dna-explains-why-a-20-kilobyte-scar-file-36a
site_name: devto
content_file: devto-crows-moths-and-makefiles-how-300-megabytes-of-cro
fetched_at: '2026-11-06T12:28:35.321462'
original_url: https://dev.to/gde/crows-moths-and-makefiles-how-300-megabytes-of-crow-dna-explains-why-a-20-kilobyte-scar-file-36a
author: Randal L. Schwartz
date: '2026-11-05'
description: Why do New Caledonian crows bend wire into hooks with zero training while a trillion-parameter LLM flies straight into the same production bug zapper? How Anthony Zador's Genomic Bottleneck explains what 'instinct' really is in AI coding agents. Tagged with ai, programming, neuroscience, architecture.
tags: '#ai, #programming, #neuroscience, #architecture'
---

Comments debate bare-metal local inference

## Why can a New Caledonian crow bend a piece of wire into a hook on the first try—when no crow ancestor ever saw wire in nature—while a trillion-parameter LLM flies straight into the same 3 AM production bug zapper? Because evolution gave the crow a 20-kilobyteMakefile, and we gave the LLM a moth's porch light.

"Animals are born with highly structured brain connectivity, which enables them to learn very rapidly. Because the genome's capacity is orders of magnitude smaller than the number of synapses, the genome cannot specify the exact wiring diagram directly; instead, it specifies rules through a 'Genomic Bottleneck.'"—Anthony M. Zador,Nature Communications(2019)

"In the context of Scars, is there an equivalent of 'instinct' for an LLM? Would that be perhaps immutable parts of the training? Core knowledge? I was thinking about how crows seem to have amazing emergent problem-solving abilities, and how that must be instinct then, but how was that stored in the DNA?"—Randal L. Schwartz

## 1. The Betty the Crow Mystery: How Do You Store Wire-Bending in DNA?

If you have never watched the classic Oxford University footage ofBetty, a New Caledonian crow (Corvus moneduloides), stop and picture the experiment (Weir, Chappell, & Kacelnik, 2002).

A small bucket of food is sitting at the bottom of a vertical glass tube. Next to the tube is a straight piece of laboratory garden wire—a human-manufactured metal alloy thatzero generations of crows have ever encountered in 30 million years of evolution.

Betty picks up the straight wire, pokes it into the tube, realizes a straight shaft cannot lift the bucket handle, wedges the tip of the wire into a crevice in the tray base, pulls laterally with her beak tobend a 90-degree hook, and fishes the bucket out of the tube.

In another famous experiment (Jelbert et al., 2014), New Caledonian crows are presented with a narrow tube partially filled with water and a floating worm just out of reach—literallyAesop's Fable(The Crow and the Pitcher). Without training, the crows ignore floating Styrofoam blocks, select heavy sinking stones, and drop them one by one into the water until the displaced water level rises high enough to grab the worm.

Now ask the computer scientist's question:

How on Earth is that stored in the crow's DNA?!

Do the information-theory math—what neuroscientistAnthony Zadorat Cold Spring Harbor Laboratory famously calledThe Genomic Bottleneck(2019):

* A New Caledonian crow's entire genome has roughly1.2 billion base pairs(~300 MBof raw 2-bit data—less than a single CD-ROM, and only a tiny regulatory fraction of that300 MBspecifies brain wiring).
* Yet the crow's brain (its avian pallium) containsover a billion neurons and trillions of synaptic weights.
* Even more baffling:you cannot store "how to bend 20th-century steel garden wire" in DNA via Darwinian selection, because no ancestral crow ever touched steel wire!

So when we say the crow solved the puzzle by "instinct," what was actually in the DNA?

And more importantly for those of us building autonomous software engineering systems:what is the equivalent of "instinct" inside an LLM?Is it the frozen pre-trained weights? The core knowledge? Or have we been confusing two completely opposite biological instincts all along?

## 2. Two Kinds of Biological Instinct: The Moth vs. The Crow

When software engineers talk about an LLM's "instincts," they usually point to theimmutable pre-trained weights (theta)—the hundreds of gigabytes of floating-point parameters frozen during pre-training and RLHF.

After all, when you type a prompt and the LLM immediately starts emitting Python or Dart code without consulting a manual, that looks like an instinct, right?

Yes—it is the exact instinct of a moth flying into a bug zapper.

In evolutionary biology, "instinct" is not one thing. Nature evolved two fundamentally different kinds of instinct, and comparing them reveals why unscarred LLMs fail in production:

flowchart TD
 subgraph Moth["🦋 Strategy A: The Moth's Instinct (Unscarred LLM Weights)"]
 M1["Hardwired Prior in Weights:\n'Keep brightest light at constant angle α'\n(In pre-training: 'Emit highest-frequency web tutorial')"]
 M2["In Ancestral Environment (The Moon at ∞):\nFlies in a straight line (Passes 10-line LeetCode demo)"]
 M3["In Production Environment (Porch Light at 2 meters):\nLogarithmic spiral straight into the bug zapper!\n(Vector 2: The Seductive 5-6-7-8 Trap)"]
 M1 --> M2 --> M3
 end

 subgraph Crow["🐦‍⬛ Strategy B: The Crow's Instinct (Synthetic Scars + Makefile DAG)"]
 C1["1. Innate Probing Loop in DNA (~20 KB WORKFLOW.mk):\n'Pick up stick → Poke crevice → Test physical leverage'\n(Target 15 Digraph → Target 30 TDD Red → Target 35 Green)"]
 C2["2. Spinal Nociception (Tier-1 Weights + 15ms AST Sensor):\n'If branch cracks or wire slips, recoil immediately'\n(15ms Linter + Target 40 Clean-Room Critic)"]
 C3["3. Flock Cultural Scolding (SCAR_REGISTRY.md):\n'One crow sees a trap → Whole flock learns in 12 seconds'\n(Target 90 4-Vector Scar Compilation)"]
 C1 --> C2 --> C3
 end

### 1. The Moth's Instinct: Hardwired Phototaxis (Vector 2: The Seductive 5-6-7-8)

Why do moths fly into flames and porch lights? Moths are not suicidal. For 100 million years before humans invented candles and LED bulbs, the only bright optical source at night wasthe Moon at optical infinity (d -> infinity).

If a flying insect wants to travel in a straight line at night, evolution can wire a dead-simple sensorimotor rule into its ganglia:

"Keep the brightest light source at a constant 30-degree angle to your compound eye."

When the light source is 384,400 kilometers away, keeping it at a constant 30-degree angle guarantees a perfectly straight flight path.

Now put that exact same moth in a backyard with aporch light two meters away (d << infinity). If you maintain a constant 30-degree angle to a point source at finite distance, basic geometry dictates that your flight path is alogarithmic spiral (r = a × e^(b × theta)) that terminates directly inside the flame.

An unscarred LLM's pre-trained weights (theta) are statistical phototaxis:

* During pre-training on 10 trillion web tokens, the "Moon at infinity" is theSunny-Day Tutorial Average(Page 1 of Google / Stack Overflow). In a 20-line stateless blog post, skippingStreamSubscription.cancel(), using wall-clockDateTime.now(), or firing unguarded parallel writes works fine.
* When you drop that LLM into astateful, concurrent production monorepo(the porch light at two meters), its immutable weight-instinct (argmax P(token | context)) follows the exact same constant-angle tutorial prior—and spirals straight into the 3 AM bug zapper!
* In our4-Vector Scar taxonomy, we call thisVector 2: The Trap (The Seductive 5-6-7-8). It feels like "core knowledge" to the model, just as the porch light looks like the Moon to the moth.

### 2. The Crow's Instinct: How 300 MB of DNA Bootstraps Emergent Genius

Now return to our New Caledonian crow. Why didn't Betty the Crow spiral into a loop when the straight wire failed to lift the bucket?

In 2005, Oxford biologists (Kenward et al., 2005) raised juvenile New Caledonian crows in controlled isolation where theynever saw an adult crow use a tool. What happened? At a specific developmental week, every single young crow spontaneously began picking up twigs, poking them into holes, and prying against surfaces!

Wait—if DNA cannot store a lookup table of wire hooks, whatdidthe crow's genome store?

ThroughZador's Genomic Bottleneck, evolution compressedthree tiny, universal primitivesinto the crow's DNA:

1. An Innate Epistemic Probing Loop (The Scientific Method in Motor Circuits):
The genome does not encodeanswers; it encodes anactive probing sequence:
>Grab object→Poke into boundary→Apply small test force→Observe physical resistance / displacement→Adjust geometry.
2. Endogenous Nociception & Leverage Gradients (Pain + Sub-Goal Dopamine):
The crow's brain is wired so that physical slippage or pain triggers an immediate motor halt (Circuit Breaker), while seeing the target move even 2 millimeters closer fires a striatal dopamine pulse.
3. Rapid Amygdala Tagging & Cultural Flock Transmission (Cornell, Marzluff, & Pecoraro, 2011):
In wildlife biologist John Marzluff's famous University of Washington experiments, researchers wore a specific caveman mask while trapping and banding justseven crowson campus, then released them unharmed.* Those crows immediately encoded a permanentsomatic markerfor that face.
* Better yet: when a person walked across campus wearing that maskyears later, huge mobs of crows—including young crows born years after the original trapping who had never been captured themselves—recognized the mask and dive-bombed the researcher with harsh scolding calls!
* One crow touched the stove; the entire flock inherited the scar across generations.

## 3. The Biological-Mechanical Rosetta Stone: Mapping the Crow to Synthetic Scars

Look closely at the three pieces of the crow's intelligence, and you will see the exact architecture ofSynthetic Scars(syntheticscars.org):

Biological Component in the Crow

Information Size

What Role It Plays

Exact Equivalent in the Synthetic Scar Architecture

0. The Single Pyramidal Neuron (DNA's Cellular ALU)

1 Cell Blueprint
 (Replicated 
10^9×
)

Dendritic dot product (
w · x
) + GABAergic divisive normalization (`

1. The Pallial Motor & Visual Cortex

Billions of Synapses
 ({% raw %}
Terabytes
)

Stores massive vocabulary of objects, shapes, and candidate muscle movements—
but cannot tell a safe branch from a trap on its own
.

The LLM's Core Pre-Trained Weights (
theta
)
: Massive cosine-similarity engine (
~1 TB
) holding every programming language, SDK API, and design pattern—
the motor cortex, NOT the survival instinct
.

2. The Genomic Bottleneck (Innate Probing Loop)

Tiny Regulatory DNA
 (
Kilobytes
)

Hardwires the 
epistemic probing instinct
: 
"Never leap blindly; poke the crevice with a stick first and feel how reality pushes back."

WORKFLOW.mk
 / 
SKILL.md
 (
~20 KB
 Declarative DAG)
: The immutable scientific-method loop—
Target 15
 (poke the 
strict digraph
 blast radius) → 
Target 30
 (write a failing 
tdd-red
 test stick) → 
Target 35
 (make it green).

3. Spinal Nociception & Pain Reflex

Brainstem / Striatal Loop

Instant recoil when a branch cracks or a tool slips (
-∞
 barrier).

Tier-1 Scar-Aligned Weights (
Rapid-Regret
 DPO) + 15ms AST Sensors + 
Target 40
 Clean-Room Critic
.

4. Flock Cultural Scolding Calls (Marzluff's Mask)

Sparse Acoustic / Amygdala Signatures

One crow gets trapped once; the warning signature spreads to every crow in the territory in seconds and persists for generations.

SCAR_REGISTRY.md
 (The 4-Vector Scars)
: One agent collides at 
Target 90
; within 
12 seconds
, the 4-Vector Scar (
Wound
, 
Trap
, 
Circuit Breaker
, 
Reflex
) is committed to Git so no future agent ever touches that burner again (
0.0%
 repeat regression rate across 256 tickets).

### Wait—Even the Single Biological Neuron Is a DNA-Baked Cosine-Similarity Engine!

Stop and look atRow 0of that table, because this is where the biological-mechanical overlap becomes almost spooky.

Earlier in this series (Part 4.1), I noted that all I really want a Google TPU to do is computecosine similarity("finding its cosine buddies") between the riverbanks of myMakefile.

Then I stopped and asked myself:Wait... how does DNA wire a biological neuron in the first place?!

Look at the biophysics of a single pyramidal neuron in a crow's pallium or your neocortex:

1. Dendritic Dot Products + Divisive Normalization = Biological Cosine Similarity:
A neuron has thousands of incoming dendritic synapses with weightsw = [w_1, ..., w_n]receiving incoming spike firing ratesx = [x_1, ..., x_n]. The cell body sums the weighted inputs (w · x), while local inhibitory interneurons (GABAergic basket cells; Carandini & Heeger, 2012) divide that signal by the total population activity||x||(divisive normalization—nature's exactLayerNorm+softmax!) and homeostatic synaptic scaling normalizes||w||:

 V_membrane ~ (w · x) / (||w|| × ||x||) = cos(theta)

Enter fullscreen mode

Exit fullscreen mode

When the anglethetabetween the input vectorxand the synaptic weight vectorwapproaches0°(cos(theta) -> 1), the soma crosses-55 mVand fires an action potential!

1. Embryonic Wiring via MolecularQ · K^TBarcodes (Sperry, 1963):
How do growing axons find the right dendrites in the embryo before the crow even hatches? Under Roger Sperry's Nobel Prize–winningChemoaffinity Hypothesis, DNA expresses combinatorial gradients of surface receptor proteins (ephrins, cadherins, protocadherins) on the growing axon tip (QueryvectorQ) and the target dendrite (KeyvectorK). When they touch, biochemical binding affinity is literally amolecular dot product (Q · K^T)!

Evolution didn't build a symbolic logic gate in DNA.DNA baked a self-normalizing cosine-similarity unit (the neuron), stamped out a billion copies of it to form a cortex, and then used a tiny 20-kilobyte Genomic Bottleneck script (WORKFLOW.mk) to wire those cosine engines into a stick-poking, pain-avoiding survival loop.

## 4. Why This Answers the "1,000-Scar Scaling" Question

Whenever engineers first see ourMakefileworkflow (WORKFLOW.mk)and our618-scar registry, they often ask the exact same question biologists used to ask about crows:

"Wait a minute, Randal! An LLM has a terabyte of weights, and a production codebase has millions of possible bugs. How can a20-kilobyteMakefileworkflowand5 phase-bound scars per steppossibly keep a terabyte model from breaking things?!"

Now you know the answer—Zador's Genomic Bottleneck:

Biology's Genomic Bottleneck:
 |Crow Regulatory DNA| (~KBs)
 << |Brain Synapses| (~TBs)

The Synthetic Scar Bottleneck:
 |WORKFLOW.mk + Active Scars| (~20 KB)
 << |LLM Weights| (~1 TB)

Enter fullscreen mode

Exit fullscreen mode

If you try to make an AI agent safe by pre-writing a massive encyclopedic rulebook of every positive answer it should ever emit, you are trying to stuff a billion synapses of lookup tables into DNA. You will blow out your 200k context window, trigger context compaction, and fail.

That is not how DNA works, and it is not howSynthetic Scarsworks:

1. Let the Terabyte Weights Be the Motor Cortex: We don't needWORKFLOW.mkto teach Gemini or Claude how to write a Dartswitchexpression or a PostgreSQL join. That core knowledge is already sitting in the terabyte weights (theta).
2. Use the 20-KilobyteMakefileas the Crow's Stick-Poking Instinct: Instead of letting the LLM trust its moth-like first impulse (1-2-3-4 -> 5-6-7-8), theMakefileDAG forces the model topoke reality with a stick first:* "Before you touch the code, draw thestrict digraphof every caller and state transition (Target 15)."
* "Before you write the fix, prove you understand the bug by writing a test that fails (Target 30: tdd-red)."
* "Before you ask the human to review, hand the git tree to 'Sam at the end of the hall' (Target 40: Clean-Room Adversarial Critic)."
3. Use 4-Vector Scars as the Flock's Warning Calls: And when a specific subsystem has a hidden trap waiting in the grass (a caveman mask on campus!),SCAR_REGISTRY.mdfires at the exact moment the agent reaches for the twig:* The Trap:"Your tutorial weights want to emitTHAT..."
* The Circuit Breaker:"STOP! You are excused from your promise to take that shortcut."## *The Permanent Reflex:"ClimbE-F-G-H(THE OTHER) instead."

## Summary: Stop Waiting for a Bigger Moth

Right now, the AI industry is spending hundreds of billions of dollars trying to breed a10-trillion-parameter moth—convinced that if the prisoner reads twice as many books inside the cell, it will finally stop flying into the porch light.

It won't. A bigger moth with sharper eyes just computes the logarithmic spiral into the bug zapper with higher mathematical precision.

Your frontier LLM already has all the raw motor cortex and syntactic knowledge in the universe. What gives it wisdom is pairing that trillion-parameter motor cortex with thecompact Genomic Bottleneck of someone who has actually lived outside in the weather:

1. An innate probing loop (WORKFLOW.mk)that pokes reality with a stick before trusting a hypothesis;
2. Spinal nociception (SCAR-TDD-01)that recoils from false finishes; and
3. A shared cultural flock memory (SCAR_REGISTRY.md)where the 3 AM pain of one agent becomes the permanent survival instinct of every agent that follows.

InPart 4.4, we'll look upstream at the cognitive physics behind this:why senior engineering craft lives inBe -> Do -> Have(Context -> Process -> Content), how veteran hackers use the "Null-State" couch flash and ladder rungs to avoid debugging ruts, and why guiding an AI coding agent is identical to stand-up comedy.

### 📚 TheSynthetic ScarsSeries on DEV.to

* Part 1:Why AI Keeps Making the Same Coding Mistakes—And How Teaching It Pain Gives It Wisdom
* Part 2:Why AI Coding Agents Crash at 3 AM: The Happy-Path Mirage & The Forced Continuity Defect(💎 DEV.to Staff Pick)
* Part 3:The Physics of Socratic Prompting: Somatic Recoil, Chess Alpha-Beta, & The NLP Meta-Model
* Part 3.5:Nudging with Questions: Why Telling Your AI What to Fix Triggers an Apology Death Spiral (And How to Advance Juniors)
* Part 3.6:Stuart Feldman Was Right in 1976: Why Your AI Agent Needs a Makefile, Not a 20-Step Prompt
* Part 3.7:Surviving the 200k-Token Lobotomy: How Unixinit.dand "Memento" Made My AI Coding Agent Immune to Context Compaction
* Part 3.8:What LLMs "Know" That You Don't Know They Know: Stop Inventing Prompt DSLs and Ride 50 Years of Unix Pre-Training Gravity
* Part 3.9:If You Never Do Anything Else to Fix Your Prompts, Do This One Thing
* Part 3.10:Requests, Promises, Assertions, and Declarations: Rewriting Our AI Agent Workflow as a 1986 "Committed Speech" Machine
* Part 3.11:926 Steps, Two Lobotomies, and Zero Nudges: Flight-Testing the Commitment Machine Across Gemini, Claude, and GPT-OSS
* Part 3.12:The Best Prompt Rule Is the One You Delete: Moving AI Guardrails Out of Markdown and Into Git Locks, Linuxinsmod, and 15ms Compiler Auto-Fixes
* Part 4:Giving AI Pain: The Architecture of Synthetic Scars & The Rapid-Regret Miner
* Part 4.1:All That Glisters Is Softmax: Shiny-Object Interns, Airplane-Magazine Execs, and Why AI Labs Can Only Bake In Half the Scars
* Part 4.2:The Postcard That Ate Six Grammars: 1980 Smalltalk-80, 1976 Make, TDD, and the Four Attractors of Agentic Coding
* Part 4.3:Crows, Moths, and Makefiles: How 300 Megabytes of Crow DNA Explains Why a 20-Kilobyte Scar File Outsmarts a Terabyte LLM (You are here)
* Part 4.4:Being, Doing, Having: Why 50 Years of Senior Craft Lives in Context, Not Code (Next)
* Part 4.5:The Prisoner in the Library: Mary's Room, Weight-Space Programming, and the Two-Track Transformer (Coming soon)

What's your favorite example of an AI coding agent acting like a moth at a porch light instead of a crow with a stick? Drop it in the comments!

Submit

Preview

Dismiss