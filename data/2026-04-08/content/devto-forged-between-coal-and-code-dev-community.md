---
title: Forged Between Coal and Code - DEV Community
url: https://dev.to/anchildress1/forged-between-coal-and-code-phi
site_name: devto
content_file: devto-forged-between-coal-and-code-dev-community
fetched_at: '2026-04-08T11:23:52.389187'
original_url: https://dev.to/anchildress1/forged-between-coal-and-code-phi
author: Ashley Childress
date: '2026-04-03'
description: A backend engineer builds an immersive narrated web experience with Canvas, WebGL, layered audio, and her own Appalachian voiceover. No frameworks. 13 ADRs. Tagged with wecoded, devchallenge, frontend, css.
tags: '#wecoded, #devchallenge, #frontend, #css'
---

WeCoded 2026: Frontend Art 💜

This is a submission for the2026 WeCoded Challenge: Frontend Art

## Show us your Art

Carbon Traceis an immersive memoir that I designed, wrote, narrated, and produced. I used my native Appalachian accent throughout since the origin story starts at home in a small coal town in Southwest Virginia.

For the full experience, visit my website athttps://carbon-trace.anchildress1.devand be sure to turn on your sound.

Pay attention to the ambient audio shifting between scenes. Watch the circuit traces grow from barely visible to full coverage. The ghost-drift text is intentionally out of sync with the narration—it's not a subtitle, it's a feeling.

Built with Canvas 2D, WebGL displacement effects, GSAP timelines, layered Howler.js audio, and accessibility-first interaction design—no frameworks, no shortcuts.

💡 This submission reflects thev1.0.1release used for the competition build.

## Inspiration

### Origins ofCarbon Trace🪨

When I first saw this challenge, I felt what I wanted to draw almost immediately. The first obstacle was figuring out how to translate that feeling into code.

I wasn't inspired by any one thing. I was inspired byeverything. To accurately convey the depth of gender roles in my life, I had to start at the beginning in the small Appalachian coal town where I grew up. Life there has clear binary boundaries: men work in the mines and women take care of the home. I've been pushing back on this ideal for as long as I can remember—starting with the toy kitchen gift I had zero interest in as a toddler.

Carbon Traceisn't another generic idea of equality. It's the fight I went through to be treated as an equal in a male dominated world. The diamond is a metaphor for my life and moves through its own journey in pictures as I tell you mine. I wrote and narrated the script in the exact same dialect I grew up speaking. Each scene has independent ambient audio designed to embody a specific emotion. There are small animations throughout that help bring the static images alive. Each individual component adds a layer of depth to the overall story.

Every image builds off of the previous version as the narrative progresses and follows the same constraints: circuitry begins barely perceptible and grows every frame until it covers the entire frame. The diamond starts black and covered in coal and shines brighter until its full power in the end. Strategic lighting throughout obscures faces to keep the focus on the diamond as the primary character and prevent this from being about any one person—it's designed to be about women in the industry as a whole because my experience is not unique. It's one of many.

So the diamond is my story zoomed out and abstracted so every individual can feel themselves inside the experience while I tell you about mine.

### The Numbers Haven't Changed 📉

Even though we have grown from ideas like the ones I grew up with—where women belong in the kitchen, not in the coal mines—the inequality is still glaringly apparent in the tech space.

In college I served as president of theCS WoWclub that aims to improve visibility of tech-related careers for young grade school girls through community outreach. Even with programs like this throughout the US, only one woman earns a CS degree for every 4 men (NCES, 2021–22).

In tech and more specifically engineering, men currently outnumber women 4 to 1 (BLS, CPS Table 39). The women who do work these jobs earn approximately 12% less on average than their male counterparts (BLS, Highlights of Women's Earnings 2023). I builtCarbon Traceas a long-lasting impact piece. It maintains the state of truth in 2026 the same as these statistics do. I didn't build it to raise awareness. I builtCarbon Traceto make you feel what these numbers can't.

### Why It Had to Be Immersive 🌊

I imagine there's at least one person reading this and wondering why I needed a full scale production to tell a story that I just as easily could have written about. My answer is becauseI needed you to feel it.

Every technical layer inCarbon Traceexists to carry a piece of that feeling. The ambient audio shifts between scenes to set an emotional tone that words alone can't establish—mine dust settling, water running, wind through an empty room. The ghost-drift text floats fragments of thought across the screen like the things you almost say out loud but don't. The circuit trace shimmer starts nearly invisible and grows brighter every scene because the potential was always there—it just needed the right conditions to be seen. The PixiJS displacement effects make the world around the diamond physically respond: water flows, heat rises, and the diamond glows with increasing intensity. None of these layers are decorative. Each one is a narrative instrument, andCarbon Traceis what happens when they all play at once.

## My Code

## anchildress1/carbon-trace

### Deterministic scene engine for an interactive narrative experience using GSAP, Howler, Canvas 2D and PixiJS. Built for WeCoded 2026 Frontend Art.

# Carbon Trace: An Immersive Art Experience

 
 
 
 

An immersive visual narrative told from the awareness of a diamond trapped in a coal seam—12 painted scenes with ghost-drift text, narrated audio, and pixel-level visual effects. Built forWeCoded 2026 DEV ChallengeFrontend Art.

Experience it live:https://carbon-trace.anchildress1.dev

## The Story 💎

A diamond wakes up inside a coal seam. It doesn't know what it is yet—just pressure, darkness, and the sense that something isn't right. Over 12 scenes it moves through tunnels, furnaces, pockets, sinks, and silence. It gets carried, stored, forgotten, and found again. By the end, it isn't just a diamond anymore. It's a circuit. It's music. It's light.

The narrative follows a carbon cycle that isn't chemistry—it's personal. Coal to diamond to circuit to light. Each scene is a painted image (Leonardo AI, Flux 2 Pro) with narration I recorded, ambient textures, ghost-drift text that pours in and blows out…

View on GitHub

⚖️ This project is licensed underPolyform Shield 1.0.0.

### What I Am Not 🔧

I am not a frontend developer.I'm a backend-focused engineer who had never heard of Canvas 2D, Howler.js, PixiJS, or GSAP before this project. I spent just as much time learning what these tools do as I did designing the system around them. AI helped me learn what each tool did and gave me alternatives. I decided what to do with it from there.

I'm also not an artist. I usedLeonardo.aito generate all images and dusted off some old GIMP skills to build the image layer masks by hand. Everything you see inCarbon Tracewas built by someone who doesn't do this every day—which is exactly why it took a full production pipeline, 13 ADRs, and four competing AI reviewers to ship it.

What I am is a backend engineer who brought backend discipline to a frontend art project. The ADR process, the adversarial review gauntlet, the CI/CD pipeline, 685 unit tests, 220 E2E tests—that's what happens when someone who builds production systems decides to build something meaningful instead.

### The Voice You Can't Generate 🎙️

I wrote and narrated the script myself because real Appalachian is something that AI is incapable of—even with the list of words it's allowed to use in reference to the area I still call home. Words like "holler" (hollow) or "sangle" (single) and phrases like "ain't got a pot to piss in" (little financial means) are all authentic from the Southwestern Virginia and Eastern Kentucky regions.

I know enough about recording to know I never wanted to learn it myself. However,Carbon Tracecould not exist without quality recordings that you don't get from QuickTime. So, I taught myself enough of GarageBand to record all tracks and no, that wasn't very much fun. I got in and out with the basics and then usedffmpegto help slice the ambient sounds fromFreeSound.org. AI was in the background to help me iterate ideas until I was happy with the end result.

### How I Wrangled the Robots 🦾

Since this project lives entirely outside my usual stack, I leaned heavily on my AI friends to get the job done, but this was not a prompt-and-go solution.

#### The Review Gauntlet ⚔️

My primary workflow was Claude Code as implementer, Codex and Antigravity performed adversarial code reviews for every branch to identify inconsistencies and bugs, and Copilot had the final review sign off for all changes. Sonar and Trivy ran for every PR along with a suite of tests, including Playwright and Lighthouse.

This is just one of many examples of why this works overall—one LLM is never good at everything and putting them in competition with each other helps to increase code quality.

The adversarial reviews were critical to the final build, because no single AI was allowed to operate unchecked in a repo where I didn't plan to personally review the code. Beyond architecture bugs, the gauntlet caught frontend-specific issues—a mask processing loop that was freezing the page during scene loads, and repeated layout calculations that caused animation stutter. It also proved to be a pain because every time I thought I was done with a feature, there would be another hour or more of AI wrangling I had to do. The back and forth continued until all of my helper reviewers agreed on the ultimate solution and only then was the branch merged.

#### From Design Doc to Decision Records 🗂️

I started with a simple design document in markdown that was converted into anAGENTS.mdfile and wired to each AI individually. By the time I made it to version 5 of the "simple" design, I decided I needed something with a bit more structure. That's when I started writing architecture decision records instead and I added them to the repo for tracking. I ended up with 13 ADRs, most of which were updated after one or more decisions I made proved impossible given the constraints I defined. This forced every major technical decision to be intentional instead of experimental.

Alongside the repo work, ChatGPT and Claude Cowork helped me with image generation prompts and gave me all the info I needed about GSAP, Howler.js, PixiJS, and Canvas 2D to be able to make design decisions. They had competing reviews between them, as well, just to make sure all the pertinent information was available to me when I needed it.

💡 For a full breakdown of every architectural decision made during the build,the ADRsare available in the repo.

### Hundreds of Wrong Diamonds 🔮

Leonardo wasn't very easy to wrangle either, as I generated literally hundreds of images to perfect each scene. ChatGPT and Claude often helped with wording, so both had their own best-practice instructions generated from research, covering several different image flows across models including Flux Pro 2.0, Nano Banana, and GPT Image 1.5.

I had several hilarious outtakes during image generation, too. I learned that specific words like "rough faceted" or "silhouette" did not mix well with some models. I ended up with a somewhat extensive set of rules for prompt generation to ensure the diamond's story was properly told through each picture.

Here's a couple of my favorite outtake images:

### Under the Hood ⚙️

Application architecture:Vanilla JS (no framework), 14 ES modules orchestrated by a 5-state machine (Loading → Paused → Scene Active → Transitioning → Credits). My goal was to make this a production-level application without over-engineering or introducing abstraction where it doesn't belong. This is a static single page, one-flow-only application and the entire flow for each scene is controlled byscenes.json—every frame's image, narration lines, ambient audio, audio cues, effects, and transition config lives in one file for easy edits that don't interfere with code structure. Every scene difference is expressed as configuration, not logic, which means adding a new per-scene behavior is adding a config key, not an if-block.

The state machine isn't just a label—it controls how every subsystem behaves at any given moment. When a user pauses, audio, canvas transitions, PixiJS effects, shimmer dots, GSAP timelines, and auto-advance timers all freeze in sync. When they resume, everything restarts from exactly where it left off. An unconditional auto-advance timer fires regardless of whether the narrationendevent arrives, eliminating a race condition where scenes could stall if the browser swallowed the event. Every timer in the system is pause-aware through a sharedPausableTimerutility so nothing leaks across scene boundaries.

The audio system is the most complex piece.I wanted to include different emotional ambient tracks for each scene designed to play just under the narration layer. I sourced all tracks fromFreeSound.org, but no two sound effects have the same volume, which meant I needed the ability to mix on demand from the backend in addition to fade controls and delayed timing. Two independent Howler.js channels are responsible for running each track concurrently:

Channel

Format

What it does

Ambient

m4a, looped

Crossfades between scenes (800ms), pauses with all channels during nav

Narration

m4a, one-shot

Per-scene voiceover with configurable delay, pre-buffers next scene's audio during current playback

I also implemented buffer recovery escalation through three distinct stages: nudge (no-op seek to force browser re-eval), reload (preserve position → reset source → restore), exhaustion (log warning, clear state, prevent UI lockup). All timers use unified pause/resume logic to prevent cross-scene leakage. The final scene layers in a licensed track from Bridge City Sinners that fades in before the narration ends, then boosts in volume with a 3-second fade once the voiceover completes—a cinematic handoff from story to music.

Rendering architecture:The visual stack is four layers composited on top of each other—a Canvas 2D scene layer for images, a PixiJS/WebGL canvas for displacement effects, a separate Canvas 2D overlay for the shimmer trace dots, and a DOM layer on top for text, captions, and controls. Each layer has its own render loop and pauses independently with the state machine.

PixiJS visual effects:A separate WebGL-powered canvas handles pixel-level scene animations—water displacement, heat distortion, glow, and shockwave—each confined to mask-based regions so only targeted areas of the image animate. Effect parameters modulate in real time from audio frequency data via a Web Audio AnalyserNode. The entire PixiJS bundle (~330 KB) is lazy-loaded after the initial paint so it never blocks the first screen the user sees, and if WebGL fails entirely, the experience degrades gracefully to static images.

Circuit trace overlays:The circuit traces aren't just static images—they're a live shimmer overlay rendered on a dedicated canvas. Each scene loads a hand-authored PNG mask that I drew in GIMP, where dark pixels define walkable paths.shimmer.jsspawns glowing dots that navigate those paths using 8-directional pathfinding, pulsing in warm amber tones that shift per scene. The opacity ramps from 5% in the opening to full coverage by the finale—the circuitry was always there, it just needed the right conditions to be seen.

The first design couldn't produce what I had in mind, so I deferred it, rewrote the ADR, and came back with a completely different approach that would get the job done.

GSAP timeline orchestration:The ghost-drift text was designed to keep the audience engaged in the narration in real time. I set up positioning as a percentage value relative to the container and originally allowed for alignment options. Later, I decided that was unnecessary and removed the extra noise from the codebase.

All captions sync directly into the GSAP timeline via callbacks instead of independent timers. That way when the user pauses or resumes any scene, the captions are automatically included.

The credits overlay has its own ADR and runs a GSAP-driven scroll with touch, wheel, and keyboard input, focus management for links, and full reduced-motion support.

Accessibility (WCAG AA):Any time I do any front-end work, accessibility is top of mind. This project was no different. I made sure all standard best practices were followed after AI helped to research what that looks like in 2026, including:

* aria-live="polite"region to announce full narration text on scene change
* Roving tabindex for the scene progress bar
* Standard media keyboard nav: Space (play/pause), Enter/Arrow (advance), Escape (pause)
* Screen reader narration separate from visual ghost-drift text (aria-hidden="true"on visual elements to prevent duplication)
* A persistent caption toggle via localStorage
* Reduced motion is fully supported—prefers-reduced-motiondisables all canvas effects, freezes shimmer dots, cuts transitions instantly, and responds to live preference changes mid-session

I used AI to research and implement accessibility standards, then tested the final result and orchestrated changes to prevent repo chaos.

### Shipping It 🚢

Underneath the story is a production-grade engineering process. Since I already have a pretty solid workflow with Release Please and Cloud Run, I provided the examples to AI and had the full CI/CD pipeline configured early on. That allowed me to track each shippable feature as a new deployed version for the final round of testing.

The setup for me was minimal, but it was the last piece of turning this fancy art project into a small scale production build. The final build is ~5,500 lines of code (LOC) backed by ~14,500 LOC of tests across 685 unit tests and 220 E2E tests. Five CI workflows cover linting, automated tests, Lighthouse CI for both mobile and desktop performance, security scanning via Trivy and CodeQL, static analysis through SonarCloud, and release automation.

## What the Diamond Knows Now 💎

I took an unconventional path to get here, but looking back, I was always going to end up exactly where I am. The circuit traces in every scene ofCarbon Tracedidn't appear out of nowhere—they were there from the start, just waiting to be seen. That's my story too. I was made to solve problems, even when nobody around me expected that from a girl growing up in a poor coal town.

It's not always easy. But I've never been afraid of hard work to get the job done. The end result is a full circuit—built from pressure, time, and a refusal to stay small.

The fact that I'm a female engineer shouldn't matter. It only matters that I'm a good one.

## Ashley ChildressFollow

Distributed backend specialist. Perfectly happy playing second fiddle—it means I get to chase fun ideas, dodge meetings, and break things no one told me to touch, all without anyone questioning it. 😇

### 🛡️ Pressure-Tested by More Than One Brain

This post was written by me with collaborative editing from Claude, ChatGPT, and Gemini. The code forCarbon Tracewas built using Claude Code, Codex, Antigravity, and Copilot, and it was directed by a human who refused to let any of them off easy. All images were generated with Leonardo.ai under my art direction. All narration is my actual voice. No AI was harmed in the making of this post, but all were argued with repeatedly and extensively.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse