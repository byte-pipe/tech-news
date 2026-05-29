---
title: 'Your Inbox Knows Too Much: Parsli for the Privacy Paranoid - DEV Community'
url: https://dev.to/olgabraginskaya/your-inbox-knows-too-much-parsli-for-the-privacy-paranoid-7ah
site_name: devto
content_file: devto-your-inbox-knows-too-much-parsli-for-the-privacy-p
fetched_at: '2026-05-30T06:00:25.402392'
original_url: https://dev.to/olgabraginskaya/your-inbox-knows-too-much-parsli-for-the-privacy-paranoid-7ah
author: Olga Braginskaya
date: '2026-05-24'
description: 'This is a submission for the Gemma 4 Challenge: Build with Gemma 4 What I Built Every few... Tagged with devchallenge, gemmachallenge, gemma.'
tags: '#devchallenge, #gemmachallenge, #gemma'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Build with Gemma 4

## What I Built

Every few weeks there is another story about leaked customer data or a breached SaaS platform. At the same time people keep happily connecting their Gmail accounts to random AI products just to answer one question: "Where is my package?"

Parsli is a local-first AI assistant that answers that question without sending your inbox into somebody else's cloud.

It connects to Gmail locally, parses shipment-related emails, extracts tracking information, classifies shipment events and builds timelines from the mess of marketplaces, carriers, pickup points, customs notifications and random stores that still send emails like it is 2009.

Shipment emails are a surprisingly intimate dataset once you look at them closely. They quietly reveal where you shop, what pharmacies you use, what expensive things you buy, when you travel, and sometimes when you are not even home. I did not want to hand that stream of personal behavior to yet another startup with a "we take your privacy seriously" page.

Parsli is still an early prototype but it is one I genuinely plan to keep working on. I order from different countries through different marketplaces and shipment tracking quickly turns into chaos across carriers, languages and notification formats. This started as an experiment around local AI workflows but gradually became something I actually want to use myself. Next steps include adding SMS, screenshots and voice messages as input sources - shipment updates are scattered across channels, not just email.

I also wanted the system to be observable rather than becoming another "black box" AI agent. Besides storing shipment events, Parsli persists rule matches, model decisions, confidence levels, extracted entities, processing timings, token usage and classification reasoning. Email parsing turns into edge case hell almost immediately once you leave happy-path demos, so having a full decision trail made debugging significantly easier.

## Demo

## Code

https://github.com/olgazju/parsli

## How I Used Gemma 4

Parsli uses Gemma 4 as the reasoning layer on top of a deterministic extraction pipeline.

A lot of shipment emails do not need an LLM at all. Amazon, UPS, Israel Post and half the internet keep sending the same templates over and over, so things like HTML cleanup, tracking number extraction, invoice filtering and obvious shipment updates are handled through deterministic rules and language packs. Wasting model calls on every single email would be slow and pointless.

But once emails start drifting away from standard templates - a multilingual customs notice, a pickup point notification with tracking buried in prose, a marketplace that formats everything differently - deterministic rules alone stop being enough. That is where Gemma comes in as both a shipment classifier and an auditing layer on top of the rules.

The pipeline first extracts structured candidates deterministically and then sends the ambiguous cases to the model for validation, confidence estimation, shipment state classification and general "does this actually make sense" checking before the result gets persisted.

I store the whole decision trail: which rules fired, model outputs, confidence scores, token usage, timings and whether the final answer came from rules or the model. On my real mailbox out of 48 relevant emails 55% were resolved by rules with the model just agreeing as a cheap audit, 38% the model actually corrected what the rules got wrong and the rest split between edge cases. Rules alone would get you maybe 60% of the way there. The model alone could handle everything but would be slow and wasteful. Together they cover each other's blind spots.

For local inference I used google/gemma-4-e4b running on an M2 MacBook Pro through LM Studio in headless mode. That model size ended up being more than enough for this workload. Shipment tracking is a narrow structured problem once you strip away the HTML garbage and email chaos - you are classifying into a finite set of states, not writing poetry. E4B gave me the reasoning quality I needed while staying fast enough to run locally without a dedicated GPU server, which was the whole point.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse