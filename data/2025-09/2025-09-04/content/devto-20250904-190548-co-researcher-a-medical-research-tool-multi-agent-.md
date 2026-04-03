---
title: Co-Researcher | A Medical Research tool | Multi-Agent and Real-time data - DEV Community
url: https://dev.to/ashiqsultan/co-researcher-accelerating-healthcare-research-with-multi-agent-ai-hjo
site_name: devto
fetched_at: '2025-09-04T19:05:48.249382'
original_url: https://dev.to/ashiqsultan/co-researcher-accelerating-healthcare-research-with-multi-agent-ai-hjo
author: Mohamed Ashiq Sultan
date: '2025-08-30'
description: This is a submission for the AI Agents Challenge powered by n8n and Bright Data What I... Tagged with devchallenge, n8nbrightdatachallenge, ai, webdev.
tags: '#devchallenge, #n8nbrightdatachallenge, #ai, #webdev'
---

n8n and Bright Challenge: Unstoppable Workflow

This is a submission for theAI Agents Challenge powered by n8n and Bright Data

## What I Built

I built a Co-Research app to help scientists in healthcare and medicine get their work done faster in drug discovery. It’s uses by multiple n8n AI Agent nodes each having brightdata as their tool to retrive real-time data from internet

Each agent takes care of a specific job, like pulling inClinical Trial data, checking literatures, analysis of safety concernsand then a final agent ties it all together into a neat summary with insights.

## Demo

Main WorkflowSub Workflow

Live AppYou can try the app in the below link.

https://co-researcher.vercel.app

### n8n Workflow

* Main Workflow JSON
* Sub-Workflow (BrightData) JSON

## Technical Implementation

I have created two workflows.

1. Main Workflow:This is where the actual research workflow happens. It uses multiple AI agents, with each agent handling a specific part of the research process.
2. Sub Workflow: To search the internet using BrightDataThink of this like a resuable helper function. It handles web searching tasks and isdesigned to work with any existing or new workflows. In this project, three different agents use this same sub workflow as their search tool.

LLM Model: Well, I used Gemini Flash due to their free tier.Memory: I used simple memory provided by n8nTools: Well, the BrightData search

This is simply the tech stack

* Next.js: Web app
* n8n: Research Automation
* BrightData: For Searching Web
* AirTable: Storage
* Gemini: LLM

### Bright Data Verified Node

I have used couple of bright data nodes

* Webscrapper Node with Google AI search
* Monitor Snapshot
* Download Snapshot

## Journey

This project is an inspiration fromJames Zoutalk onVirtual Lab of AI Scientists. Since this is just a hackathon project, I didn't capture his complete version, rather adapted the core ideas he outlined so credits to him.

Okay now about my actual journey

I'm completely new to both n8n and brightdata so had to watch some YouTube videos to get an overall understanding. Also as person who likes to avoid tooling and loves to code everything, this entire concept seemed too good to be true. What I personally liked is the easy integration with the various platforms with just API keys and also the orchestration of AI Agent tool, this is super cool coz If I had to code this I would easily sit at least a week on this.

I started experimenting with BrightData on n8n, and initially tried using it directly as a tool in an agent node. But that didn't really work for me cox the results would get stored in a BrightData snapshot, which made it pretty tricky to orchestrate the whole process properly.

So I had this idea to create a separate workflow instead and call that as a tool. Turns out this approach worked really well for me, What I ended up with wasthis reusable web searching workflow that I can basically plug in anywhere I need itI pretty much liked this neat solution.

Now all I needed is a place to store the records, I wanted to keep it simple and went with Airtable. Finally I created a Next.js app to make it accessible and view the results.

You can find the code along with n8n workflow jsons in the below GitHub repo.GitHub

If you have read it till here, a like would be great, thank you.

...

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
