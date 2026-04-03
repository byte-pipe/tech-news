---
title: AI Agent for Google Play Review Monitoring - DEV Community
url: https://dev.to/bridget_amana/ai-agent-for-google-play-review-monitoring-2p9b
site_name: devto
fetched_at: '2025-09-06T11:05:25.091800'
original_url: https://dev.to/bridget_amana/ai-agent-for-google-play-review-monitoring-2p9b
author: Bridget Amana
date: '2025-08-31'
description: This is a submission for the AI Agents Challenge powered by n8n and Bright Data What I... Tagged with devchallenge, n8nbrightdatachallenge, ai, webdev.
tags: '#devchallenge, #n8nbrightdatachallenge, #ai, #webdev'
---

n8n and Bright Challenge: Unstoppable Workflow

This is a submission for theAI Agents Challenge powered by n8n and Bright Data

## What I Built

I built a workflow that takes reviews of an app from Google Play, runs sentiment analysis on them, and routes them based on the results. Positive reviews get logged for tracking, while negative ones are flagged so they can be acted on. The whole point was to create an automated system that helps teams quickly understand how users feel about their app without going through hundreds of reviews manually. To make it practical, I used Temu as the app for testing

## Demo

### n8n Workflow

Github Gist

## Technical Implementation

I started by connecting Bright Data’s Web Scraper node in n8n to Google Play. My first challenge was figuring out the correct URL setup to fetch reviews. I realized I needed to scrape by the app’s URL and then create a dataset node to structure the review data.

Once the reviews came in, I needed a way to handle them individually. I used n8n’sSplit Out Itemsnode to break the dataset into separate review objects. At first, I struggled with which fields to split, but including only the review text solved the problem. Later on, I discovered a feature inside Bright Data’s actions:Split snapshots data to parts by snapshot id, which would have done exactly what I did with split out.

For sentiment analysis, I connected n8n’s AI Agent node withOpenAI GPT-4.1-MINI. The prompt I used was:

Given the following review {{ $json.review }}, return a JSON with: {sentiment: ..., summary: ..., key_issue: ...}

Enter fullscreen mode

Exit fullscreen mode

It worked, but I had to tweak the output handling to make sure it returned proper JSON that n8n could actually parse.

Next came the routing logic. I wanted negative reviews to go to the team for action and positive ones to just be logged. Using an IF node, I set the condition:

{{ $json["message"]["content"]["sentiment"] }} == "Negative"

Enter fullscreen mode

Exit fullscreen mode

At first I ran into false branches because I wasn’t using expressions correctly, but once I switched to using proper expressions, it started working as expected.

Finally, I logged everything into Google Sheets. Each row had the Sentiment, Summary, and Key Issue fields.

### Bright Data Verified Node

Bright Data’s verified node is what made this workflow possible. At first, I wasn’t fully clear on what Bright Data was or how to really use it. I joined the live demo session and got a few pointers, but I was still confused until I stumbled on a video that broke it all down. That video is what unlocked things for me, so if you’re new to Bright Data, I recommend watching it first.

Once I had the node running, it was straightforward to fetch reviews directly from the Google Play page. The dataset it produced was clean enough to connect with other parts of n8n, which made the later steps; splitting, analysis, and routing, much easier to manage.

## Journey

This was my first real attempt at using Bright Data with n8n, and it didn’t go perfectly at first. I spent time figuring out URL structures, how datasets worked, and how to properly handle outputs from AI. There were moments where I thought I had broken the workflow entirely, but each roadblock helped me learn how n8n’s nodes actually work in practice.

The biggest lightbulb moment was discovering Bright Data’s snapshot split feature, which made structuring data far simpler. Another one was realizing how much expressions matter inside n8n. Without setting them correctly, conditions and mappings just don’t behave the way you expect.

If I were to redo this, I’d start by setting up a proper schema for how I wanted the data to flow before building the workflow itself. That would have saved me a lot of time. Still, the process taught me how powerful Bright Data and n8n can be together when you use them right.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
