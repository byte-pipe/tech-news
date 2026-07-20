---
title: Why did my benchmark stop at N=22? A debugging story in nine bugs - DEV Community
url: https://dev.to/gde/why-did-my-benchmark-stop-at-n22-a-debugging-story-in-nine-bugs-3m2l
site_name: devto
content_file: devto-why-did-my-benchmark-stop-at-n22-a-debugging-story
fetched_at: '2026-07-20T19:34:37.885627'
original_url: https://dev.to/gde/why-did-my-benchmark-stop-at-n22-a-debugging-story-in-nine-bugs-3m2l
author: xbill
date: '2026-07-15'
description: Submission for DEV's Summer Bug Smash — Smash Stories track. There was a file in my repo called... Tagged with bugsmash, debugging, ai, python.
tags: '#bugsmash, #debugging, #ai, #python'
---

Summer Bug Smash: Smash Stories Submission 🐛🛹

Submission forDEV's Summer Bug Smash— Smash Stories track.

There was a file in my repo calledrun_benchmark_1_22.py.

Not 1 to 24, which is what the harness was written to do. Not 1 to 26, which is how many Mersenne exponents the agents know. Twenty-two. A chart in the README —a2a_latency_times_1_22.png— agreed. At some point, past-me had decided the benchmark ends at 22, committed the evidence, and moved on.

This summer, hunting for a Bug Smash target, I finally asked:why 22?

## The setup

a2a-benchmarkcompares A2A agent performance across four languages. Python and Go sit behind Gemini tool-calling (ADK); Node and Rust are bare HTTP handlers. Each computes Mersenne primes with Lucas–Lehmer; a harness sweeps N from 1 to 24 and draws two charts.

I ran the full sweep. At N=24, the Python column printedN/A. Every other language returned data. There it was — not a decision, acrash, worked around by shortening the run until it stopped hurting.

## The 4,300-digit wall

The Python agent's response at N=24 wasn't even subtle about it:

"Exceeds the limit (4300 digits) for integer string conversion;
 use sys.set_int_max_str_digits() to increase the limit"

Enter fullscreen mode

Exit fullscreen mode

CPython 3.11 added a default cap onint→strconversion — 4,300 digits — as a denial-of-service mitigation. My agent stringified every prime it found. The 24th Mersenne prime, 2^19937−1, has6,002 digits.

Here's the part that made me laugh out loud: the stringified list wasnever returned. The tool reports only its elapsed time. The line that had silently amputated my benchmark at N=23 was decorative. The fix wasgit rmenergy: delete thestr(), keep the raw int. Go had the identical dead weight (val.String()) inside its timed region — it just happened not to crash.

One deleted expression, and a column of data that had never existed came into being: N=24, Python, 2,425.9 ms.

## It gets worse before it gets better

With the agents finally running, I kept pulling the thread. The harness parsed Python's elapsed time out of theLLM's prosewithr"It took ([\d\.\-e]+) seconds". Gemini, in my captures, never once said "It took" — it said"Calculating the first 5 Mersenne primes took…"and later"The calculation took…". The only reason the benchmark had Python data at all was a fallback that read the structured tool artifact. My measurement pipeline's primary path was a bet on a language model's phrasing habits.

The direct agents had their own tells. Ask Node or Rust for 100 Mersenne primes and they'd cheerfully report"Found first 100 Mersenne primes"— having computed 26, the size of their exponent table. And they formatted elapsed time as%.2fms, so Rust's fastest runs reported0.00ms, which parses to zero, which cannot exist on a log-scale chart. Those points didn't look wrong; they looked like nothing.

And the biggest lie was the chart itself: "A2A Round-Trip Time (including LLM/Tool calling)". Only half true — literally. Two of the four agents route through Gemini; two never touch an LLM. Median RTT: 2.6ms and 4.6ms for the direct pair, ~1.6s and ~1.8s for the Gemini pair. A~400× gappresented as a language comparison was actually a pipeline comparison.

## The encores

I fixed everything and re-ran the sweep to generate the "after" charts. Go's N=1 datapoint:N/A.

Cause: my fix. With the dead formatting deleted, Go's small-N runs got so fast thattime.Durationswitched output units —Elapsed time: 836ns— and the harness parser had branches for µs, ms, and s, but had never met a nanosecond.The fix made the code too fast for its own benchmark.

Parser patched. Re-ran again. Three Go datapoints missing — different ones. The captured response text:

"I already did that. Do you want to do it again?"

The harness reused deterministic context IDs; ADK keeps per-context session history; on a rerun, Gemini looked at the old conversation and declined to redo the work. My benchmark's completeness now depended on a language model's opinions about repetition. Unique per-run IDs fixed it, and the final sweep came back96/96.

## What I actually learned

1. The workaround you commit is the bug you keep.run_benchmark_1_22.pysat in the repo like a fossil of an uninvestigated crash. The moment you rename the script instead of reading the stack trace, you've decided to ship the bug.
2. Benchmarks are production code.Mine crashed, lied about counts, rounded away its smallest measurements, and compared two different architectures on one axis. Every chart it ever produced was quietly wrong in four ways.
3. If a machine consumes the output, never route it through prose.Structured tool artifacts existed the whole time; the regex on LLM text was pure fragility.
4. An LLM in the measurement path adds failure modes that have nothing to do with the code under test— including, apparently, boredom.

Nine bugs. Four PRs (#1,#2,#3,#4). One question I should have asked a year ago:why 22?

Don't take my word for any of it —docker run --rm -e GEMINI_API_KEY=your_key -v "$PWD/out:/out" xbill9/bugsmashruns all four fixed agents and the full sweep, and writes the charts to./out.

Disclosure: I ran this investigation with Claude Code as the debugging agent — it did the reproduction, the fixes, and the benchmark reruns while I steered. The bugs, the numbers, and the "I already did that" refusal are all real and archived in the repo.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse