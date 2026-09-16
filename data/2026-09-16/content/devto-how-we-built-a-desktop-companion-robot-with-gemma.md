---
title: How we built a desktop companion robot with Gemma 4 and Raspberry Pi - DEV Community
url: https://dev.to/googleai/how-we-built-a-desktop-companion-robot-with-gemma-4-and-raspberry-pi-2oke
site_name: devto
content_file: devto-how-we-built-a-desktop-companion-robot-with-gemma
fetched_at: '2026-09-16T15:21:44.991888'
original_url: https://dev.to/googleai/how-we-built-a-desktop-companion-robot-with-gemma-4-and-raspberry-pi-2oke
author: bebechien
date: '2026-09-16'
description: The behind-the-scenes story of how we built DinoDesk AI—a privacy-first, LEGO dino companion robot powered by a hybrid Local Gemma 4 and Cloud Gemini architecture. Tagged with raspberrypi, gemma, gemini, robotics.
tags: '#raspberrypi, #gemma, #gemini, #robotics'
---

Have you ever wished for a little desk companion—something with the tactile charm of a retro game character that could chat with you, keep track of your desk timers, or talk you through a tricky bug—without a camera staring at you all day?

That question sparkedDinoDesk AI: our LEGO Dino AI Companion Robot.

I and my colleague Shama set out to build a smart, low-power desk robot that combines the nostalgia of 8-bit audio-visuals and LEGO Technic mechanics with a modernHybrid LLM Switching Architecture (Local ↔ Cloud). By pairing aRaspberry Pion the desk with a local PC gateway runningGemma 4alongsideGemini Flash, we created a companion that offers100% visual privacy (no camera), instantaneous zero-cost local chat, and deep cloud reasoning on demand.

Here is the full behind-the-scenes story of how we designed, wired, and programmed DinoDesk AI from the ground up.

# 1. The Hybrid Brain: Local Gemma 4 ↔ Cloud Gemini

One of the biggest dilemmas when building an AI hardware companion is choosing where the brain lives. If everything runs in the cloud, every casual"What time is it?"costs API tokens, adds network latency, and sends your voice data over the internet. On the other hand, if you strictly limit yourself to a small on-device model, the robot struggles the moment you ask it to create a new feature in your gigantic codebase, or explain a complex topic.

So we decided to build aHybrid LLM Architecture, with aUnified LLM Gateway (Router)hosted on the user's main PC. The Raspberry Pi on your desk sends identical OpenAI-compatible requests over Wi-Fi regardless of which engine is active:

 ┌─────────────────────────────────────────────────┐
 │ [ Main PC / Local Gateway ] │
 │ │
 │ ┌─────────────────────────────────────────┐ │
 │ │ Dynamic Model Router / Switch │ │
 │ └────────────────────┬────────────────────┘ │
 │ │ │
 │ ┌──────────────────┴──────────────────┐ │
 │ v v │
 │ [ LOCAL ENGINE ] [ CLOUD ENGINE ] │
 │ LM Studio / Gemma 4 Gemini Flash / │
 │ (Zero Latency, Private) Gemini Live │
 └────────────────────────┬────────────────────────┘
 │
 │ Wi-Fi (Unified OpenAI-Compatible Stream)
 v
 ┌─────────────────────────────────────────────────┐
 │ [ DinoDesk AI (RPi) ] │
 │ - Pirate Audio LCD & I2S Beep Speaker │
 │ - Push Button & Optional Sensors │
 └─────────────────────────────────────────────────┘

Enter fullscreen mode

Exit fullscreen mode

### Three Modes of Intelligence

Mode

Active Model

Strengths & Primary Use Case

How to Switch

🟢 Local Mode
 
(Default)

Gemma 4
 (via LM Studio)

Zero-cost, offline, 100% private.
 Delivers ~200 ms first-token latency for casual chats, desk timers, and quick status checks.

Double-click 
Pirate Audio Button X
, 3s long-press on Capacitive Touch sensor, or voice command (
"Switch to Cloud Mode"
)

🟡 Cloud Mode

Gemini Flash / Gemini Live

High reasoning & complex problem solving.
 Ideal for coding help, complex math, deep explanations, or language tutoring (~800 ms first token).

Same as above

⚡ Auto-Hybrid Mode

Automatic Routing

Defaults to 
Gemma 4 locally
. When the complexity classifier detects multi-step reasoning keywords (
"explain"
, 
"compare"
, 
"write code"
), it transparently escalates the prompt to 
Gemini Flash
.

Automatic System Routing

When Auto-Hybrid Mode escalates a question to the cloud, the robot's indicator temporarily shifts from🟢 steady greento🟡 steady goldfor the duration of the response, then returns to green—so you always know at a glance which brain is answering.

# 2. Hardware & Tactile Mechanics: LEGO Meets Pirate Audio

We wanted DinoDesk AI to feel like a physical toy rather than a cold smart speaker. Instead of 3D-printing a sealed plastic shell, we built the body out ofbasic LEGO bricks and Technic lever mechanismsso anyone can customize or repair it.

### Core Bill of Materials (BOM)

1. Main Controller:Raspberry Pi + 32GB MicroSD
2. Display & Audio Shield:Pimoroni Pirate Audio Speaker(1.3" 240×240 ST7789 IPS LCD + I2S 1W Speaker + 4 tactile buttons)
3. The Red Button:A mini push button switch that gives you a satisfying tactile click to start or stop voice capture
4. Audio Input:Compact USB Mini Microphone
5. Motion System:Motors driving Neck movements and Tail wagging

Before building the full body, I first prototyped the logic using a Raspberry Pi and a simple LEGO set.

### Physical Button Controls

Even with voice and sensor triggers, dedicated hardware buttons feel good for instant physical control:

* Button A (GPIO 5) — Cancel / Mute:Immediately stops the active response stream, silences audio, and returns the robot toIdle.
* Button B (GPIO 6) — Home Re-Center:Resets all servos to their neutral center position without interrupting the current state.
* Button X (GPIO 16) — Expression & Engine Switch:Single-click cycles facial expressions manually; double-click togglesLocal ↔ Cloud Mode.
* Button Y (GPIO 24) — Tail Test & Volume:Single-press fires a tail-wagging sequence to verify mechanical alignment; a 2-second long-press cycles beep volume (Low → Medium → High → Mute).

# 3. Bringing the Dino to Life: The 5-State Finite State Machine

A companion robot only feels alive when its eyes, voice, and body move together. We designed a 5-stageFinite State Machine (FSM)that coordinates the 240×240 LCD eye expressions, 8-bit beeps, and motor movements:

┌──────────┐ button ┌───────────┐ release ┌──────────┐ stream ┌──────────┐
│ Sleeping │──────────> │ Idle │────────────>│Listening │─────────> │ Thinking │
└──────────┘ (wake) └───────────┘ (trigger) └──────────┘ (send) └──────────┘
 ^ │
 │ ┌──────────┐ │
 └──────────────│ Speaking │<───────────────────────┘
 (done) └──────────┘ (tokens arrive)

Enter fullscreen mode

Exit fullscreen mode

State

Entry Condition

Pirate Audio LCD Expression

8-Bit Audio Feedback

Motor Action (Neck / Tail)

1. Sleeping

Inactive for 3 mins OR room dark

(
- _ -
)
Closed eyes + 
zzz

Silent (or optional soft snore)

Motors relaxed; head tilted slightly down

2. Idle

Default standby

(
• •
)
Autonomous blinking

Occasional wake/blink chime

Head centers; neck sways slowly

3. Listening

Button click OR sensor trigger

(
O O
)
Eyes widen bright

"Beep-Boop!"
 rising tone

Head tilts 15° toward the user

4. Thinking

Audio sent; router inferring

(
º º
)
Spinning pupils + mode badge

Irregular processing ticks (
tick-teek-poh
)

Neck sways slowly side-to-side

5. Speaking

Receiving SSE token stream

Expressive blinking + scrolling subtitles

8-bit typewriter beep per token

Tail wags in sync with text length

Building DinoDesk AI reminded us that AI doesn't have to stay locked inside a browser tab or a cloud data center. When you give an open model likeGemma 4a pair of pixel eyes, an 8-bit voice, a wiggling LEGO tail, and the ability to call onGeminiwhen things get heavy, your desk suddenly feels a whole lot more lively. 🦖✨

It's still a work in progress and not quite perfect yet, but I'll be back soon with fully implemented voice chat capabilities! Until then, please enjoy the fun little 8-bit sound effects every time you press the button. Beep-Boop!

Clone the repo here :https://github.com/google-gemma/dinodesk-ai-companion/

And drop a comment to share what you're planning to create.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse