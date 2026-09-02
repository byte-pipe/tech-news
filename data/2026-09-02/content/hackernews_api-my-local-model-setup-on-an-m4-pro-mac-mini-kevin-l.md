---
title: My local model setup on an M4 Pro Mac mini | Kevin Lewis
url: https://lws.io/blog/my-local-model-setup/
site_name: hackernews_api
content_file: hackernews_api-my-local-model-setup-on-an-m4-pro-mac-mini-kevin-l
fetched_at: '2026-09-02T14:58:54.531868'
original_url: https://lws.io/blog/my-local-model-setup/
author: raybb
date: '2026-09-01'
description: I run a local LLM server on my M4 Pro Mac mini with 48 GB of RAM.
tags:
- hackernews
- trending
---

# My local model setup on an M4 Pro Mac mini

 
[2026-09-01]
 
 
 

I run a local LLM server on my M4 Pro Mac mini with 48 GB of RAM. It handles everything from my Hermes agent backend to quick chat queries on my phone. The whole thing takes about 30 minutes to set up.

Here is the stack:

* Qwen3.6-35B-A3B-OptiQ-4bit: my main model for anything that needs reasoning or depth
* Gemma-4-E4B-it-OptiQ-4bit: lightweight model for simple chats, formatting, and other routine tasks
* oMLX: the inference server
* Tailscale: tailnet connecting the Mac mini, my iPhone, and my MacBook

Hermes runs as the agent backend on the Mac mini, with my MacBook running the desktop client and my phone running Telegram. For non-Hermes usage I use Apollo on iOS for quick chats (reads like Claude, good for throwaway questions), Pi as my coding agent (I already wrote about that setup), and Raycast AI on my Mac for random things.

## Why bother?

The main reason to run local: cloud APIs are rented land. They can change their pricing, hit your usage limits, or swap the model being served behind the scenes whenever they feel like it. I was regularly maxing out two $200/month subscriptions and it felt like I was getting different things from them at different points. Sometimes a model was fine, sometimes it degraded with no notice.

Data privacy is another issue. You do not know what these companies do with your data once they have it. They might limit how it gets used, they might sell it, they might expose it. Either way, it creates an operational security risk. If you work with sensitive code, client data, or proprietary workflows, sending it to a third-party API is a decision you make once and cannot undo.

Then there is AI sovereignty. I have been watching how the US government has limited the rollout of various models. That can happen at any point from any government, for any reason, and you have no control over it. If your workflow depends on a cloud model that gets restricted, you have to stop or scramble. The only way to avoid that is to own your compute.

Other practical advantages:

* Cost predictability.APIs are variable. Your usage spikes and your bill follows. With local hardware, the cost is the hardware purchase plus electricity. Flat. After that, every inference is free.
* Latency.No network roundtrip means faster responses for everyday tasks. The M4 Pro’s media engine handles inference at speeds that feel instant for most prompts.
* Offline capability.No internet, still works. For agent workflows that run in the background, this matters more than it sounds.
* No rate limits.API providers throttle you when you hit usage thresholds. Your own machine does not care how much you run.

## How I actually use it

The Mac mini is always on. It sits on my desk and I barely notice it except when I need it.

Hermes runs on the Mac mini as well, using a local model on the same machine. I access my agent through Telegram (on my phone) and the Hermes desktop app on my MacBook. The Hermes desktop app acts as a ‘shell’ and connects to a Hermes backend on another device (in this case the Mac mini). This means I share a backend, conversation history, and skillset across all my devices.

Then there is everything else:

* Apolloon iOS for quick throwaway chats. I want something that reads like Claude but does not require an API key or a subscription. Connect Apollo tohttp://[mac-mini-tailnet-url]/v1and you are done. Good for “rewrite this paragraph” or “what does this error mean” type questions.
* Raycastalso on my Mac for random things I don’t want to install anything for.
* Pifor coding.Already wrote about that setup.

The point is not to replace API-based models. It is to handle the 80% of requests that do not need GPT-5 or Claude Opus. And when I do need those, they are already available. Local just covers more of my day-to-day for free.

## The model breakdown

Running a large model locally comes down to one thing: how much RAM it actually needs in memory. Most people look at the parameter count and get the wrong idea, because the difference between dense and mixture-of-experts (MoE) models matters a lot on consumer hardware.

Here is how to read the identifier:

Qwen3.6-35B-A3B-OptiQ-4bit

* Qwen3.6: model family and version
* 35B: total parameters across all experts
* A3B: active parameters per token (3 billion, not 35)
* OptiQ-4bit: mixed-precision quantization (4-bit mostly, 8-bit on sensitive layers)

gemma-4-e4b-it-4bit

* gemma-4: Google’s Gemma 4 family
* e4b: encoding size, roughly 4 billion parameters total
* it: instruction-tuned
* 4bit: uniform 4-bit quantization

The key difference is theA3Bpart. A dense 27B model has 27 billion parameters loaded in RAM at all times, for every single token. An MoE model like the Qwen3.6-35B-A3B has 35 billion total parameters spread across 256 experts, but only about 3 billion are actually activated per token. The other 32 billion sit in RAM doing nothing.

On my 48GB Mac mini, the Qwen3.6-35B-A3B in 4-bit takes about 20GB of RAM. That leaves 28GB for context windows, the operating system, and everything else running on the machine. The Gemma-4-E4B is roughly 2.4GB. Small enough to keep around for simple tasks where using the full 20GB model is overkill.

My friend’s MacBook Air had 16GB total. A dense 27B in 4-bit needs roughly 14GB. That is literally everything the machine has, minus room for the OS. So it works for a moment, and then when it does not, it swaps to SSD and becomes painful.

MoE changes this. The 35B model in my identifier would fit on the same MacBook because only 3B of weights are actually active per token, which means the GPU/Media Memory footprint is more like what a 6B dense model would need. The 35 billion total parameter weights all sit in unified memory

How to check if a model will work on your hardware:

* Look at the quantized file size first. A 4-bit model is roughly the number of parameters in gigabytes (35B params ≈ 17-20GB depending on the quantization method).
* Subtract your OS overhead. macOS takes about 6-8GB on Apple Silicon.
* Leave room for context windows. Every few thousand tokens adds megabytes to the KV cache. Plan for 8-16GB overhead if you expect long conversations.
* For MoE models, the total parameter count is misleading. Look for the “active parameters” figure to understand actual inference memory.
* If your model plus context still fits within your available unified memory with a 10-15% buffer, you are good. Anything closer to full will swap to SSD.

## Performance

Qwen averages 325 tok/s in processing prompts, and 34 tok/s in token generation. That isn’t instant, but it’s quick enough that I never really think about it.

Memory bandwidth matters too, though it’s not about whether a model will run — it’s about how fast. The M4 Pro has 273 GB/s of unified memory bandwidth. That’s the speed limit for moving model weights from RAM into the compute units during inference. For context, a base M3 is 100 GB/s, an M2 Pro is 200 GB/s, and the M3 Max tops out at 400 GB/s. The M4 Pro sits solidly between the Pro and Max range, which is why the token speeds feel usable but not instant.

## Swapping models is easy

This is the part nobody talks about. You can swap out your local models every few weeks as new ones drop. It is literally a download and a restart.

The workflow:

1. Download the new model into~/models/
2. oMLX auto-discovers it from the model directory
3. Pick it in the oMLX app or restart the server
4. Done

The oMLX admin dashboard has a built-in HuggingFace model browser. Find a model, click download. Change the model in Hermes, Pi, Raycast, and Apollo, and I am all done.

A lot of this can be done via CLI too, so I can SSH into the Mac mini from any of my devices.

Why this matters: the gap between local models and API models is closing fast. What was “meh” quality a year ago is competitive for most real-world tasks now. Coding, reasoning, tool use are where it matters. And the 4-bit quantization from OptiQ keeps quality surprisingly high. The 35B-A3B at 4-bit only loses about 1-2 points on most benchmarks compared to BF16 (16-bit floating point, the uncompressed baseline). That is an acceptable tradeoff for 48GB of memory usage instead of 70.

## The network

Tailscale creates a mesh between all my devices. Mac mini, iPhone, MacBook, all on the same private network. Nothing exposed to the public internet.

The oMLX server listens on port 8000. Any device on the tailnet can connect. Raycast, Apollo iOS, Hermes desktop on my MacBook, they all hit the same endpoint. No configuration drift between devices.

oMLX’s KV cache persistence also matters on the tailnet setup. Coding agents repeatedly circle back through earlier context in a session. oMLX caches each block to SSD, so when the agent returns to a previous prefix, it is restored from disk in milliseconds instead of being recomputed. That makes the local setup actually practical for agent work, which is where Hermes lives.

## Closing out

Local models on Apple Silicon are not a side experiment anymore. The M4 Pro Mac mini handles it without breaking a sweat, the models are good enough for most tasks, and you can swap them out whenever you want. You are not paying per token. You are not routing sensitive data through third-party endpoints. And when a better model drops next week, you can try it with barely any effort for the cost of some hard drive space.

I have already ordered a 128GB M5 Max Mac Studio to be delivered later this year, but I am incredibly happy with the performance of this M4 Pro Mac mini so far. If you have other Apple Silicon devices, try it out - you may need to change the model based on your specs, but the general setup holds.