---
title: Agents Beat Two Accelerator Chips in 24 Hours | Blackbox
url: https://www.blackbox.ai/blog/gpt-oss-one-gpu-vs-custom-chips
site_name: tldr
content_file: tldr-agents-beat-two-accelerator-chips-in-24-hours-blac
fetched_at: '2026-10-17T13:52:57.415094'
original_url: https://www.blackbox.ai/blog/gpt-oss-one-gpu-vs-custom-chips
date: '2026-10-17'
published_date: '2026-10-16'
description: With no human in the loop, agents tuned gpt-oss-120b on one NVIDIA B200 to 723 tokens/sec in under 24 hours, past SambaNova's and Groq's accelerator chips.
tags:
- tldr
---

BLOG
October 16, 2026
·
2
 min read

# Agents BeatTwo Accelerator Chipson Inference in Under 24 Hours, No Human in the Loop

Four agents, one NVIDIA B200, no human in the loop: in under 24 hours they took gpt-oss-120b from about 480 to 723.2 tokens per second for a single request, past SambaNova's and Groq's accelerator chips. Cerebras is next.

Here is where one agent-tuned B200 lands against the fastest gpt-oss-120b providers Artificial Analysis tracks, and how it got there overnight.

gpt-oss-120b: output tokens per second, one request
higher is better

Single stream, 10k-token prompts · higher is better.

gpt-oss-120b: output tokens per second, one request
Model
Value
Cerebras
 Wafer-scale engine · next target
1,729.0
BLACKBOX AI
 1× NVIDIA B200 · agent-tuned
723.2
SambaNova
 RDU · ours +2.3%
706.8
Groq
 LPU · ours +53%
473.5
Azure
 GPU · ours 2.0×
361.0
Nebius (Base)
 GPU · ours 2.0×
357.7
1,729.0
Cerebras
Wafer-scale engine · next target
723.2
BLACKBOX AI
1× NVIDIA B200 · agent-tuned
706.8
SambaNova
RDU · ours +2.3%
473.5
Groq
LPU · ours +53%
361.0
Azure
GPU · ours 2.0×
357.7
Nebius (Base)
GPU · ours 2.0×

Providers: Artificial Analysis, P50 over the past 72 hours, October 16, 2026. BLACKBOX AI: best verified result from our agent run, measured on the same methodology by a fixed harness.

1.5× faster in 20 hours, with no human in the loop

Best verified single-stream output speed, gpt-oss-120b on one B200, by hours since the run started

1.5× faster in 20 hours, with no human in the loop
Hours since the agents started
Value
0 h
~480
20 h
723.2
0
200
400
600
800
0 h: ~480
~480
0 h
8 h
9 h
10.5 h
13.5 h
16.5 h
19 h
20 h: 723.2
723.2
20 h
Hours since the agents started
1.5×
faster in 20 hours
723.2
tokens/sec on one B200
83
experiments, scored automatically
0
human edits to the engine

## Faster than two accelerator chips

OnArtificial Analysis, the fastest gpt-oss-120b providers aren't GPU clouds. They are companies that built their own inference accelerators:Cerebras(wafer-scale engine),SambaNova(RDU) andGroq(LPU).

One general-purpose GPU, tuned overnight by agents, now runsahead of SambaNova(706.8) and53% faster than Groq(473.5), and about2×the other GPU providers on the list.

Provider
Hardware
Output tok/s
BLACKBOX AI vs them
Cerebras
Wafer-scale engine
1,729.0
next target
★ BLACKBOX AI
1× NVIDIA B200
723.2
—
SambaNova
RDU
706.8
+2.3%
Groq
LPU
473.5
+53%
Azure
GPU
361.0
2.0×
Nebius (Base)
GPU
357.7
2.0×

These are chips designed from the ground up to make exactly this workload fast. The agents closed that gap with software alone, on a GPU you can rent today, in a single night.

## 1.5× faster, overnight, on its own

At noon UTC on October 15 we gave four agents one NVIDIA B200, the open gpt-oss-120b weights and one goal: make a single request stream as fast as possible. No human touched the engine after that.

They started from a strong, standard recipe at about480 tokens per second. Twenty hours later, the same GPU streams723.2 tokens per second:1.5× faster, found, tested and verified entirely by agents.

## How the agents did it

Four agents ran the loop described inRecursive Self Improving Inference Engine: propose a change, submit it to the harness, keep it only if it beats the current best, and share what they learned so the others can build on it. Over the night they ran83 scored experimentsand exchanged501 messages.

The biggest jumps landed around the eight-hour mark, as the agents' early work started paying off. After that came a steady run of smaller wins, each one checked against a freshly re-measured control before it was kept. Ideas that didn't hold up were logged and rolled back, so every gain on the progress chart is a verified result.

## How it's scored

Every submission is measured by a fixed harness the agents can't modify, on theArtificial Analysis performance methodology: one request at a time, 10,000-token input prompts, and output speed counted from the first token to the last. A result only counts if it also keepstime to first token at or under 1.5 secondsanderrors at or under 1%.

The current best reaches first token in108 mson a 10k-token prompt, generates a median1,491 tokensper answer, and haszerofailed requests.

## What's next

The line is still rising. The agents' next milestone is1,000 tokens per secondon one GPU, and the target after that is Cerebras at 1,729.0 tokens per second.

The same loop works on any open model and any traffic shape. Bring the workload, the speed you need and the quality bar it must hold, and the agents do the tuning.

Want your model tuned like this?
Tell us what you run and the speed you need. Agents take it from there.
Talk to us

## Sources

Artificial Analysis, gpt-oss-120b (high) providers:artificialanalysis.ai/models/gpt-oss-120b/providers, accessed October 16, 2026. Output speed is the P50 over the past 72 hours on 10k-token inputs.

← Back to all articles
NEXT UP

### Same GPUs,More TPM: BLACKBOX AI vs Other Inference Providers

We rented Together AI and Fireworks AI dedicated deployments on the same NVIDIA GPUs we run, replayed real production agent sessions against each, and compared tokens per minute (TPM) at each provider's best. BLACKBOX AI delivers 23% to 500% more TPM, with faster time to first token (TTFT).

## Ready to serve your first token?

Tell us the workload and the controls it has to satisfy. We come back with a deployment plan and a per-token commit.

TALK TO SALES
READ THE DOCS