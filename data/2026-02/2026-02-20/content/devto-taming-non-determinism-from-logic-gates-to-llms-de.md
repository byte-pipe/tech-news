---
title: 'Taming non-determinism: from logic gates to LLMs - DEV Community'
url: https://dev.to/leandronsp/taming-non-determinism-from-logic-gates-to-llms-3mf0
site_name: devto
content_file: devto-taming-non-determinism-from-logic-gates-to-llms-de
fetched_at: '2026-02-20T19:19:26.361036'
original_url: https://dev.to/leandronsp/taming-non-determinism-from-logic-gates-to-llms-3mf0
author: Leandro Proença
date: '2026-02-19'
description: 'Or: how engineering keeps turning chaos into reliable computation. And why agentic AI still hasn''t... Tagged with ai, llm, ann.'
tags: '#ai, #llm, #ann'
---

Or:how engineering keeps turning chaos into reliable computation. And why agentic AI still hasn't solved this.

There's a pattern that repeats across the entire history of computing: we take something fundamentallynon-deterministicand engineer enough layers on top of it until it behaves deterministically. Logic gates did it. Artificial neural networks (ANNs) replicated it at some level. LLMs are the next frontier, and the hardest one yet.

In this article, we'll explore how engineering is crucial to facing non-determinism, and analyse the current state of the art for LLMs.

## Agenda

* Part I - The lie inside a logic gateNoise marginsThe CPU clock
* Noise margins
* The CPU clock
* Part II - Aspirina: teaching non-determinism to behaveWhere the chaos livesComposition does the restThe cost compared
* Where the chaos lives
* Composition does the rest
* The cost compared
* Part III - LLMs and the "Unresolved Problem"Tests as noise marginsThe agentic loop as clockThe type system and compilerWhat's missing: timing analysisHow to mitigate that?
* Tests as noise margins
* The agentic loop as clock
* The type system and compiler
* What's missing: timing analysis
* How to mitigate that?
* Conclusion

## Part I - The lie inside a logic gate

Alogic gateis taught in school as a simple binary machine. You give it 0s and 1s, you get 0s and 1s back.

AND, OR and XOR are example of logic gates. They are clean, mathematical, deterministic. And that's a usefulfiction.

At the physical level, a gate is a transistor (or a few of them) through which electrons flow. Electrons don't care about yourBoolean algebra. The voltage on a wire is a continuous, analog value that fluctuates due to thermal noise, manufacturing variance, electromagnetic interference, and even cosmic radiation flipping bits in memory.

Fun fact: in May 2003, in Belgium, an electronic voting machine gave a candidateexactly 4096 extra votes. More than she could possibly have received. After investigation, the error was attributed to thespontaneous creation of a 13th bit in the memory of the computer. The leading explanation: a cosmic ray flipped a single bit, turning a 0 into a 1 at position 2^12, adding exactly 4096 to the candidate count.

Ok, but how does the industry get determinism out of this mess?

### Noise margins

Engineers define voltage thresholds: anything below 0.8V is a0, anything above 2.0V is a1. The zone between those values is declared "forbidden". The circuit is designed to never operate stably there. This isn't physics; it's an engineering contract. (More on noise margins)

### The CPU clock

A CPU clock isn't just a metronome. It's also asampling strategy. You let the signal propagate through the gate (which takes time, calledpropagation delay), and only read the value at a specific moment: theclock edge. By then, the signal has had time to cross the threshold and stabilise. Timing is calculated to guarantee this.

But when timing fails, things may get weird. If a signal is sampled while it's still in the forbidden zone, a flip-flop can entermetastability, which is an unstable equilibrium where the output isn't quite0or1and can oscillate for an indeterminate time. This may cause real crashes in real systems.

Think of metastability as what happens when two clocks on a wall are unsynchronized. Each showing a slightly different time. "What time is it right now?", one may ask. The answer depends on which clock you look at, but you can't decide which one is right.

Inside the CPU, when facing a forbidden zone, the flip-flop faces the same dilemma. It can't decide if it's a0or a1, which can corrupt the system state. Engineers mitigate this with synchronizer chains, but never eliminate it entirely.

It's the non-determinism of physics leaking through the engineering abstraction!

The key insight: the determinism of digital computing is not a property of nature. It's anengineering achievement. It's paid with noise margins, timing analysis and careful design.

Yes, it's all aboutengineering.

## Part II - Aspirina: teaching non-determinism to behave

Aspirinais my personal project that builds a complete CPU entirely from artificial neural networks (ANNs) trained to behave as logic gates, written in Rust.

Actually I created thevery first versionalmost 10 years ago in Elixir, when I was learning about ANNs and Elixir. Recently I decided to write a Rust version while I was learning Rust.

The inversion from Part I brings the beauty: instead of physical electrons that need to be tamed into bits, here we have ANNs -systems whose weights are initialised randomly and whose outputs are continuous floating-point numbers- that need to be tamed into0and1too.

The non-determinism here is introduced deliberately, and then engineered away. Bear with me.

### Where the chaos lives - unleash the madness

A neural network starts with random weights. Its output for any input is whatever the math happens to produce. Not0, not1, but something like0.6312. In case you missed, I already have an article in my blog aboutneural networks.

Backpropagation is the engineering response. It's the algorithm that adjusts the weights iteratively, measuring how wrong the output is (theloss) and leading weights in the direction that reduces the error. Run this for 10,000 epochs - 10,000 passes over the training data - and the network converges to weights that produce0.002for inputs that should be0, and0.997for inputs that should be1.

Thesigmoid function(a.k.a thelogistic curve) does in Aspirina what noise margins do in hardware: it squashes any continuous value into the range0..1. It doesn't give you exact binary outputs, but it pushes values toward the extremes.

And that's exactly what we need

Combined with a threshold decision - below0.5we could consider0, above0.5we consider1-, we get in Aspirina the same effect: a circuit thatbehaves deterministicallyeven though its internals are continuous and learned.

### Composition does the rest

Once gates are trained, they're composed to:

XOR + AND => Half Adder => Full Adder => 4-bit ALU => Memory => Registers => CPU => Assembler => Interpreter

Enter fullscreen mode

Exit fullscreen mode

Each layer treats the layer below as if it were perfectly deterministic, which isexactly the abstraction hierarchyof real hardware.

The non-determinism was contained at the lowest level (training), and every layer above it benefits from the illusion of determinism.

Yes,determinism is an illusion. Deal with it.

### The cost compared

Compute time during training. Just as chip fabrication invests energy upfront to create reliable silicon, Aspirina invests 10,000 epochs upfront to create reliable logic. After that, inference is cheap and stable.

Now,enter LLMs.

## Part III - LLMs and the "Unresolved Problem"

Alarge language model(LLM) is non-deterministic in a deeper and more stubborn way than either of the above.

Its weights are the result of a stochastic training process over vast data. Its output is sampled probabilistically (even withtemperature=0), and there's pseudo-randomness baked in. And crucially, unlike a neural network trained on a clean truth table, an LLM's "correct output" for most inputs isfundamentally ambiguous.

Yet we're building agentic systems (Claude Code, Codex, Cursor etc) that use LLMs to write, run and iterate on code autonomously.How do we tame this?

The pattern repeats, but the engineering is particularlymessieron LLM's.

### Tests as noise margins

A test suite could behave as a binary verdict on the LLM's output:green or red. It doesn't matter if the model generated three different valid implementations in three runs: if all tests pass, they're equivalent from the system's perspective. The non-determinism of the model iscontainedbelow the threshold of "passes tests". This works, but only as well as the tests themselves. And unlike voltage thresholds, test coverage is always incomplete.

### The agentic loop as clock

An agentic system like Claude Code doesn't generate once and deliver. It reads state (files, compiler output, test results), acts, observes the new state, and repeats. This feedback loop is structurally similar to thefetch-decode-executecycle of a CPU or the iterative of Aspirina. Each iteration constrains the space of valid next actions. Errors are observable, and the agent can correct.

### The type system and compiler as low-level validators

In a Rust project like Aspirina, the borrow checkerrejects invalid outputs before tests even run.The LLM can generate wrong code and hallucinate, the compiler then refuses it, the agent observes the error message, and iterates.

This is a lower-level noise margin: just a formal filter beneath the test layer and type system.

And that's why I think that languages with strict compilers like Rust will thrive in the agentic era. Let's see.

### What's missing: the equivalent of timing analysis

In hardware, engineers canprovethat a circuit will work at a given clock frequency. They run static timing analysis and guarantee that every signal stabilises before every clock edge. There's no equivalent for agentic LLM systems.

We don't know how many iterations an agent will need. We can't bound the convergence time. We can't guarantee termination. An agent can loop indefinitely, or enter what I'd call "agentic metastability": making and undoing the same change repeatedly, unable to reach a stable state.

Anyone who has used Claude Code or Codex for long enough has seen this - the model oscillates between two approaches, each creating a problem that motivates reverting to the other.

Despite we can retry, add guardrails, skills, and set token budgets, in the end, we can't prove termination the way a hardware engineer proves timing closure on metastability

### How to mitigate that?

In hardware, the fix for metastability isdesign. In agentic systems, the analog fix isclearer context, more granular tests, explicit checkpoints and tighter feedback loops; which can be described with the following practical list of skills I created and have been using on a daily basis for every project in production:

* PO (product owner): agent receives a prompt and outputs a well-scoped task based on initial requirements and prior knowledge on the codebase. Clearer context.
* TDD (test-driven development): the developer agent outputs the code, guided by TDD - red, green, refactor. Granular tests as noise margins.
* Review: agent and human checks before merging. Explicit checkpoint.
* Small PRs: small PR's enable development and testing with reviewable increments. Tighter feedback loops.

Yes, that'ssoftware engineering practicesall the way down (and they are not new). Yet we don't have the formal toolsto provethese fixes work. It's totally empirical.

## Conclusion

At least for me, what's interesting is that each level's "solved" status depends onbounded, well-defined tasks. Logic gates are deterministic for Boolean logic. Aspirina's networks converge reliably because truth tables are finite and exact. LLMs work well on narrow, testable tasks with earlier and good feedback.

The frontier is:what does it take to engineer reliable agentic behaviour on open-ended, ambiguous, long-horizon tasks?The answer probably looks like what came before: more layers of verification, better sampling strategies (the clock), formal specifications (the truth table), and tools that can analyse convergence before execution.We just don't have those yet.

Non-determinism doesn't go away. It never has. We just keep finding better ways to push it where it can't hurt us. From voltage thresholds to synchronizer chains to temperature tuning. Every generation of computing has faced the same enemy and responded with the same weapon:engineering. Besides hype, LLMs are no different. We're just earlier in the cycle.

## References

https://en.wikipedia.org/wiki/Logic_gatehttps://en.wikipedia.org/wiki/Electronic_voting_in_Belgiumhttps://en.wikipedia.org/wiki/Noise_marginhttps://en.wikipedia.org/wiki/Metastability_(electronics)https://en.wikipedia.org/wiki/Sigmoid_functionhttps://en.wikipedia.org/wiki/Large_language_modelhttps://en.wikipedia.org/wiki/Backpropagationhttps://en.wikipedia.org/wiki/Static_timing_analysishttps://github.com/leandronsp/aspirinahttps://github.com/leandronsp/morphinehttps://leandronsp.com/articles/ai-ruby-an-introduction-to-neural-networks-23f3

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
