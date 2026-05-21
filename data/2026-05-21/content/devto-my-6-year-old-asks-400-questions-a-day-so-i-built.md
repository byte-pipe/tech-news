---
title: My 6-year-old asks 400 questions a day. So I built him a Gemma 4 AI tutor. - DEV Community
url: https://dev.to/sann3/my-6-year-old-asks-400-questions-a-day-so-i-built-him-a-gemma-4-ai-tutor-1e13
site_name: devto
content_file: devto-my-6-year-old-asks-400-questions-a-day-so-i-built
fetched_at: '2026-05-21T19:36:31.455270'
original_url: https://dev.to/sann3/my-6-year-old-asks-400-questions-a-day-so-i-built-him-a-gemma-4-ai-tutor-1e13
author: Santhoshkumar. P
date: '2026-05-20'
description: 'This is a submission for the Gemma 4 Challenge: Build with Gemma 4 My 6-year-old asks me four... Tagged with devchallenge, gemma, gemmachallenge.'
tags: '#devchallenge, #gemma, #gemmachallenge'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Build with Gemma 4

My 6-year-old asks me four hundred questions a day — about clouds, his shadow, whether ants have birthdays. I love it, but I can't always stop what I'm doing, and the usual fallbacks (Google, YouTube, a generic chatbot) are either too dense, too distracting, or too unsafe to hand a small child.Curio Kid is the app I built so my son can keep asking — and actually get warm, kid-friendly answers — without me worrying about what he sees next.

## What I Built

Curio Kidis a kid-safe Android app where a child asksanything— by typing, snapping a photo, attaching an image, or just talking — and gets a warm, age-appropriate answer fromLuna, an AI tutor powered byGemma 4. Answers are short on purpose: 2–5 sentences, an everyday analogy (Lego, swings, fruit), and a follow-up question to keep the curiosity loop running.

Designing it for my own kid forced some opinionated choices:

* He can't reliably read or type yet, but he can talk and point a camera.Voice and camera are first-class inputs, not afterthoughts.
* He will absolutely test the safety rails.Kids ask wild things ("what happens if I drink poison?","why do people fight in wars?") — Luna has to handle them gracefullyevery single time.
* I want to know what he's curious about, not spy on him.Hence theCuriosity Digest— a daily themed summary, not a chat log.

What makes it more than "yet another chatbot wrapper":

* Multimodal input— text, gallery image, live camera, on-device speech-to-text.
* Safety as a hard requirement— locked-down system prompt + Gemini safety thresholds pinned toLOW_AND_ABOVEacross harassment, hate, sexually explicit, and dangerous content; unsafe topics get a fixed redirect to "a trusted adult."
* Parent Dashboard— PIN-gated, with a one-tapCuriosity Digest: themes, highlights with quotes, dinner-table conversation starters, and an "anything to flag?" section.
* Privacy-first— API key + PIN inEncryptedSharedPreferences(AES-256); question history in a local Room DB, excluded from cloud backup; the only network call is to the model endpoint with the user's own key.
* Three interchangeable Gemma 4 back-ends— not every family phone can host a multi-gigabyte model on-device, soGoogle AI Studio(default, free tier, multimodal),OpenRouter, and a scaffoldedon-devicepath are all swappable from Settings.
* Output cleaning— Gemma 4 sometimes thinks out loud ("Final Polish:","Let me revise…"); a post-processor strips those leaks so the child only sees the final answer.

## Demo

https://raw.githubusercontent.com/sann3/curio-kid/main/demo/Home.pnghttps://raw.githubusercontent.com/sann3/curio-kid/main/demo/1i.pnghttps://raw.githubusercontent.com/sann3/curio-kid/main/demo/2i.pnghttps://raw.githubusercontent.com/sann3/curio-kid/main/demo/3i.pnghttps://raw.githubusercontent.com/sann3/curio-kid/main/demo/4i.pnghttps://raw.githubusercontent.com/sann3/curio-kid/main/demo/5i.pnghttps://raw.githubusercontent.com/sann3/curio-kid/main/demo/6i.png

https://raw.githubusercontent.com/sann3/curio-kid/main/demo/final.mp4

## Code

GitHub:github.com/sann3/curio-kid.

## How I Used Gemma 4

Curio Kid exposestwo Gemma 4 variantsin the model picker, and the choice is intentional.

### gemma-4-26b-a4b-it— 26B Mixture-of-Experts (default)

The daily driver. A kid-facing chat app needs three things at once:multimodal,fast first-token latency, andsmart enough to teach. MoE hits all three — only a slice of experts fires per token, so latency feels ~4B-class while depth stays 26B-class. In practice:

* A child holding up a beetle to the camera gets an answer in a couple of seconds, not ten.
* Streaming starts almost instantly, so chat bubbles fill in live (and incidentally dodge the Gemini SDK's hard-coded 80s socket timeout — Curio Kid usesgenerateContentStreamfor exactly this reason).
* The 256K context window means the whole day's history fits into a singleCuriosity Digestcall — no RAG, no summarisation tricks.
* Same model handles"Why is the sky blue?"anda photo of a moth.

Dense is overkill for "explain photosynthesis in three sentences"; E2B/E4B don't yet match 31B-class reasoning on the harder "why" questions kids love. MoE is the right middle.

### gemma-4-31b-it— 31B Dense (optional "thinker" mode)

For genuinely hard questions ("Why do mirrors flip left-and-right but not up-and-down?"). Slower and pricier per call, but noticeably better on multi-step or counterintuitive reasoning. Same persona, same safety, same UI — just a heavier brain when the curiosity warrants it.

### Why not E2B / E4B by default?

On-device is fully wired up via MediaPipe LLM Inference — Settings →On-devicedownloads a vision-capable Gemma 4.task(resumable, sha256-checked, metered-network aware) and runs it through a process-wideLlmInferencesingleton withaddImagefor the camera path. But cloud stays thedefaultbecause:

1. Not every phone can run Gemma 4 locally.Multi-GB models need RAM and storage the hand-me-down tablet a kid actually uses doesn't have. Gating first launch behind "Pixel 8 Pro + 1.6 GB cellular download" defeats the point.
2. Quality > offline for a six-year-old.Being told"the moon is made of cheese"by an under-cooked tiny model is worse than waiting two seconds over Wi-Fi.

So Google AI Studio is the zero-friction default, OpenRouter is the alt-cloud, and on-device is one Settings tap away for capable phones — sameLlmBackendinterface, same prompts, same cleaner.

### Where Gemma 4 actually does the work

1. The chat.Multimodal(image + history + question) → kid-friendly paragraph. The system prompt is strict (2–5 sentences, analogies, ≤2 emojis, one follow-up, no markdown) and Gemma 4 follows it remarkably well.
2. Safety reasoning.Instead of a blocklist, Lunareasonsabout whether a topic is age-appropriate and produces a fixed redirect line — Gemma 4 is instruction-faithful enough to honour a "ONLY reply with this exact sentence" clause while still engaging naturally with the 99% of fine questions.
3. The Curiosity Digest.Day's transcript → structured markdown summary (themes / highlights / conversation starters / flags) in one shot — long-context + structured-output, no orchestration framework.

### Bits I had to engineer around Gemma 4's quirks

* Chain-of-thought leakage.Gemma 4 occasionally emits"Final Polish:"/"Self-Correction:"/"Let me rewrite…"before its real answer.cleanLunaReply(LunaAI.kt) detects anchors, drops planning paragraphs, and strips markdown emphasis — without nuking legit phrases like"Let me think of a fun example!".
* MAX_TOKENSstops.The Gemini SDK throwsResponseStoppedExceptioninstead of returning partial text; I catch it on both one-shot and streaming paths and surface what already arrived.
* 80s socket timeout.Hard-coded in the Kotlin SDK with noRequestOptionsoverride. Streaming resets the read timer per chunk, so slow first-byte doesn't kill the request.
* Friendly errors.OnefriendlyError()mapper turns every 4xx/5xx/safety/quota/network failure into one short, kid-readable sentence ("Wow, so many questions today! Let's wait a minute and try again."), while logging the raw exception to a debug ring buffer.

Gemma 4 unlocked something I couldn't have shipped a year ago: amultimodal, instruction-faithful, locally-routablemodel smart enough to teach a six-year-old about black holes, safe enough to hand to that six-year-old, and efficient enough to be the default tier of a free app.

Thanks to the DEV team and Google for the challenge!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse