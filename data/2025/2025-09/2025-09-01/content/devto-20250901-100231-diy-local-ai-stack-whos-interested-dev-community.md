---
title: 'DIY Local AI Stack: Who’s Interested? - DEV Community'
url: https://dev.to/ghotet/diy-local-ai-stack-whos-interested-48bc
site_name: devto
fetched_at: '2025-09-01T10:02:31.478603'
original_url: https://dev.to/ghotet/diy-local-ai-stack-whos-interested-48bc
author: Jay
date: '2025-08-29'
description: 'Building a Fully Offline AI Stack: A Proposal Hey folks, this one''s going to be short and... Tagged with ai, opensource, linux.'
tags: '#ai, #opensource, #linux'
---

# Building a Fully Offline AI Stack: A Proposal

Hey folks, this one's going to be short and simple. No fancy formatting or morbid humor this time—just a quick check-in to gauge if there's any interest in a potential write-up.

## A Quick Recap: The "Franken-stack" AI Setup

A lot of people seemed to like my previous post about building a fully local AI stack, which I dubbed myFranken-stack. The goal was to replicate the functionality of ChatGPT with a complete set of features, including:

* Chat
* Image Generation
* Voice Interaction
* Web Search
* Connectivity with personal domains/websites

This entire system operates offline, is open-source, and costs youzerodollars. Everything works through a unified front end, so you can access it all through a single interface, just like you would with ChatGPT.

## Is It for You? Here's What You Need to Know

While I won't be writing a full tutorial just yet, I wanted to gauge interest in a breakdown of the setup. If you're curious, I'd be happy to list the various software components needed to build this stack. Be warned, though, it's a bit GPU-heavy and can tax your CPU at times, so there are someminimum system requirementsto consider.

It should run on Windows, but since I primarily useLinux Mint, there might be small caveats on the Windows side. However, I suspect setting it up on Windows might actually be easier than on Linux.

### Key Considerations:

* CPU & GPU Requirements: The system can be pretty demanding on both the CPU and GPU. You’ll need a solid setup to ensure smooth performance, especially if you plan on running the stack with multiple features (like Image Generation and Web Search combined with the dmands of an LLM) at the same time. There are ways to run it with less resources which I will outline however generally speaking, reducing GPU load requires running lower tier LLM's so there is a performance sacrifice involved.
* Storage Considerations: This setup does take up a significant amount of disk space, so make sure you have enough room before getting started. I will outline how much space you will need as a baseline. Docker may be an option however due to my Linux use case and some edge case issues regarding the API domain logic I was unable to get it working using Docker containers. As far as I know this is a Linux specific issue with how it appends docker to the domain address by default.
* Cross-platform Support: I’m working toward making it cross-platform, so it will work across both Linux and Windows. However, this will take some time and testing.

## What’s Missing?

Currently, the stack is feature-rich but has one limitation:Speech to Text(STT). I’ve implementedText to Speech (TTS)already, so it can speak to you, but you can’t speak to it yet. However by the time you have it set up I'm sure you would have the skills and knowledge to be able to simply add it in yourself I just don't have a specific software in mind for this aspect yet.

## Extra Thoughts: Personal Website Integration

I’ve already set up the stack to be hosted through my personal domain, enabling remote access anytime/anywhere. Would anyone be interested in learning how to do this as well? It’s a bit of extra effort, but definitely doable.This part will cost a few dollars as you would need to purchase a domain to use for it. You could also probably just link it to a new page through an existing domain if you have one.

### A Word of Caution:

There are many tools available to accomplish these tasks, but the stack I’ve built uses very specific tools that work well together. You’re welcome to experiment with alternatives, but I can’t promise I’ll be able to assist you much if you go down a different route.

### Future Plans:

* Speech to Text: I aim to integrate this feature soon, but I’m currently busy and don't have an exact timeline.
* Personal Website Integration: I already have the stack linked to my personal domain for online use. If you're interested in this functionality for your own setup, I can walk you through that too.
* More Platforms: Once everything's running smoothly, I plan to support setups forLinux,Windows, andDocker, and will make sure to include Speech-to-Text in the setup when I get around to doing a full tutorial.

## Interested? Here’s How to Let Me Know

If you're interested in me laying out the tools, specs, and requirements for setting up your own fully offline, fully featured AI stack (aside from STT), just leave a reaction and drop a comment. If I get enough traction, I'll write up a detailed guide.

Also, if you have any specific questions, feel free to ask them in the comments. I’ll do my best to answer them!

If there’s enough interest, I’ll go ahead and dive deeper into the technical details and start building the full write-up. Thanks for reading!

Side note:I ask for comments because, with a growing number of followers, I can’t go through each one individually to see who to follow back. A comment lets me know you’re active, that you’re following (thank you!), and helps me engage with the people who make writing these articles worthwhile.

I’m not monetizing this, I’m not advertising anything, and it’s just me—a chaotic solo dev—trying to carve out a space to share experiences with like-minded people. I’m happy to support fellow devs and help genuine insights reach a wider audience, but I can’t do that if I don’t know who’s genuinely contributing and who’s just posting AI-generated clickbait.

I want to help build a real, supportive community here. Personally, I find more value in authentic stories of trial and error than in “top 10” lists you could get from AI that still somehow get 180 reactions. I know opinions differ, but I’d rather highlight those real experiences than watch them get buried under viral but generic content. We all love AI, but let's take a moment to be human, shall we?

//Ghotet

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)


For further actions, you may consider blocking this person and/orreporting abuse
