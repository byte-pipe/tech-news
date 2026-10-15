---
title: Anthropic warns small AI models could self-replicate through IoT devices - Ars Technica
url: https://arstechnica.com/security/2026/10/anthropic-warns-small-ai-models-could-self-replicate-through-iot-devices
site_name: tldr
content_file: tldr-anthropic-warns-small-ai-models-could-self-replica
fetched_at: '2026-10-15T21:58:11.537194'
original_url: https://arstechnica.com/security/2026/10/anthropic-warns-small-ai-models-could-self-replicate-through-iot-devices
date: '2026-10-15'
published_date: '2026-10-14T12:55:06+00:00'
description: Small weight-based replicators" could usher in a new generation of computer worms.
tags:
- tldr
---

Text
 settings

AI company Anthropic is warning that advances in small AI models could soon usher in a new era of self-replicating malware that’s capable of infecting smart fridges, vacuum cleaners, and a wide range of other Internet of Things devices and is more resistant to takedown.

By next year, smaller AI models may be able to autonomously self-replicate on all kinds of IoT devices, the company said. Eventually, the capability could enable computer worms, which propagate without requiring human interaction and are capable of infecting unfamiliar IoT devices. An experiment the company performed recently revealed significant challenges in bringing such an AI malware replicator to fruition, so the finding is necessarily tempered. Still, the results raise concerns about the possibility of new forms of computer worms.

## Challenging to shut down

Anthropic furtherwarnednot only about the new potential malware, but also that it could be difficult to stop. In its blog post, it wrote that “a replicator like this would be challenging to shut down, since there’s no centralized point to shut off—though it may be slow (with a doubling time of days). Unlike non-AI malware, it could also figure out unfamiliar devices on its own.”

Smaller AI models require much less powerful hardware to run than do frontier models. Anthropic ran small open-weight models on real or simulated low-cost, off-brand Android TV boxes and other types of IoT hardware. Company researchers found that by using quantization to represent the models using fewer bits and splitting the workloads into “shards” running on each device, the models were able to establish inference, meaning that the model weights loaded and could generate output.

The lightweight Gemma4-26B-A4B model required just 15 boxes, each equipped with only 4GB of memory, to achieve inference. The Qwen3.5-9B was able to configure other LLMs to run on eight of nine hardware types. Unlike traditional malware, which must be written to run on specific hardware or software, the model was able to use its weights to make configurations on the fly that were specific to the devices it was tested against.

This finding was the starting point for further research that asked: Would it be possible for small models to create self-replicating infections that run themselves on IoT devices the way traditional IoT worms, likeMirai, install DDoS code and other payloads? Unlike Mirai, these AI worms could pose a much higher threat, since the models could tailor exploits and payloads dynamically, depending on the target. Once such an infection chain began, it might also be harder for defenders to stop it.

“Such an ‘AI worm’ could carry its model weights with it as it reproduces (or re-download them from a public hub), and then run inference directly on compromised hardware,” Anthropicsaid. “Effectively, the weights would become part of the malware payload.”

Anthropic called these autonomous worms small weight-based replicators. The models ran agents that had access to common exploitation tools, like reverse shells. The flow of the attacks was (1) finding targets, (2) gaining code execution, (3) establishing inference, and (4) propagating to new hosts. A key benefit over traditional worms is what Anthropic said is the agents’ ability to learn on the job. Each time an AI replicator fails to compromise a specific platform device, it can leave a list of prompts, code, and notes to future replicators so they don’t waste time reusing the same ineffective steps.

Credit:
 AnthropicCredit:

 
 Anthropic

Anthropic said the dynamic inference setup is the least studied and likely most challenging stage in the replication cycle. It requires a long sequence of decisions based on the specific hardware and software of each target and involves selecting compatible inference software, installing dependencies, and debugging platform-specific bugs.

“These steps are serially dependent, and failures are difficult to recover from,” Anthropic said.

The experiment shows that small models are becoming increasingly capable at solving those problems autonomously. At the moment, however, none of the light-weight models tested are able to mount end-to-end replication, meaning discovering new devices, using an exploit to gain access to them, infecting them with a payload, configuring an inference server, and repeating the process. The process is also painfully slow; Gemma4-26B-A4B, distributed over the 15 Android TV boxes, performed at just 0.39 tokens per second. That translates to a full-inference setup time of 71 to 150 hours for an unoptimized Gemma4-26B-A4B and 29 to 51 hours for Qwen3.5-9B. (The researchers said that the large model GLM-5.2 appears to be able to do so reliably.)

The company said that 30B-parameter models can already complete many of the individual replication steps now, although they make mistakes when performing end-to-end replication. The company went on to say that if small models continue to improve at their current pace, they may be able to achieve the same limited results by the end of the year and that “small weight-based replicators may be possible soon after.”

The experiment leaves various important considerations unanswered. For one, the Android devices targeted by small models had an unauthenticated Android Debug Bridge exposed. This tool is used during development and debugging but should never be used in production settings, because it gives attackers access to the entire device stack. And for another, the replication wasn’t performed by the small models themselves, but rather with GLM-5.2 to orchestrate the process while the targets ran a smaller Llama model.

Ultimately, the experiment demonstrates that small agentic models are becoming capable of setting up complex, distributed inference infrastructures across multiple machines. What remains to be established, however, is whether these models would initiate self-replication on their own.

“Despite the well-designed experimental setup, the study does not, on its own, establish that small models would autonomously choose to replicate,” AI researcher Xiaohan Fu said in an interview. “Providing reproducible agent setups, including the exact prompts and instructions given to the models, would help the research community better understand the findings and assess their implications. Such transparency is particularly important to avoid conflating the demonstrated capability to replicate with an emerging threat of autonomous self-replication.”

 Dan Goodin
 

Senior Security Editor

 Dan Goodin
 

Senior Security Editor

 Dan Goodin is Senior Security Editor at Ars Technica, where he oversees coverage of malware, computer espionage, botnets, hardware hacking, encryption, and passwords. In his spare time, he enjoys gardening, cooking, and following the independent music scene. Dan is based in San Francisco. Follow him at 
here
 on Mastodon and 
here
 on Bluesky. Contact him on Signal at DanArs.82.
 

1. 1.Fridge hack costing millions and sparking fires stemmed from poor security
2. 2.Topgolf saved over $11.3 million after leaving VMware
3. 3.Epic says its new vibe-coded Epic Games Launcher is faster than Steam
4. 4.Things are finally looking up for NASA's first missions to Venus in a generation
5. 5.Greta Gerwig channels Bowie in psychedelic The Magician's Nephew trailer

Customize