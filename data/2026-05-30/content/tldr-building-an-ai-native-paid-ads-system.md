---
title: Building an AI-Native Paid Ads System
url: https://jon4growth.substack.com/p/the-ai-native-paid-ads-system
site_name: tldr
content_file: tldr-building-an-ai-native-paid-ads-system
fetched_at: '2026-05-30T06:00:35.943150'
original_url: https://jon4growth.substack.com/p/the-ai-native-paid-ads-system
author: Jonathan Martinez
date: '2026-05-30'
description: How to run your ads inside of Claude
tags:
- tldr
---

# Building an AI-Native Paid Ads System

### How to run your ads inside of Claude

Jonathan Martinez
May 26, 2026
13
5
2
Share

I remember being on the early Postmates growth team in 2018.We were running hundreds of campaigns across channels, testing thousands of creative assets. We used Smartly (a Facebook Marketing Partner) to manage the chaos in one dashboard.

It was still a nightmare to track everything while optimizing and creating reports. Tons of back and forth between tools and dashboards.

Over the last couple of months, I’ve been experimenting heavily with Claude (hence Claude Marketers video academy) and I’ve created what I call “The AI-Native Paid Ads System.”

Before I explain it, here’s an overview graphic:

Let’s start with the first layer, and work our way down.

Share

Layer 1: Connectors & data sources

As many have seen firsthand, Anthropic became a powerhouse because of “connectors” which allow you to hook many of your current tools up to Claude. Meta’s recentannouncementis what really shows us what’s possible on running paid ads inside of a chat window.

Where this gets powerful is with Higgsfield, which is an image/video generator that uses all the best models (e.g., Nano Banana) to create high quality assets. You don’t need this connector if you’d rather keep the design in human hands. I do think AI creative is useful to validate copy and concepts at a much faster clip. Still not 100%, and I trust a designer much more for top tier creative assets but it’s a nice preview into the future.

Along with Meta and Higgsfield connectors, this system will continuously get stronger with:

* Actual campaign data from Meta
* Scheduled tasks competitive research

The campaign data will flow from the Meta MCP, so you don’t really need to do much there other than run regular analyses.

If you’d like to automate your campaign analyses along with competitive research, use Claude’s scheduled tasks to build this out.

I currently have a scheduled task that analyzes all of my competitor websites weekly and updates a database inside Notion with any changes (e.g., pricing, copy). This could feed creative angles and action items for new paid tests.

Layer 2: Claude skills and claude.md file

Having a claude.md file loaded into Claude will provide context on your brand ICP, design preferences and overall vibe. Every prompt will automatically get a “pre-read” of your brand.

Then you’ll want to add a specific Claude skill for paid ad management. This’ll get called anytime you ask Claude to work on paid ads, and will essentially feed it the brain of a Meta mastermind. To build the skill, you can prompt Claude with something like:

I’d like to build a skill for optimizing and managing paid social ads on Meta. Research the best 
minds on paid social and add all their best practices into this skill. This skill will be used
whenever I’m building ad dashboards, creating ads, optimizing campaigns, etc.

Running the account audit

Once you have your connectors, claude.md file and Claude skills loaded, you can run the audit on your Meta account with this prompt:

You’re auditing my Meta ad account. Use the Meta Ads MCP to pull live data directly. Don’t ask me to paste numbers or screenshots.

**Step 1: Confirm the account.**

List my ad accounts and confirm which one you’re auditing. If only one is connected, use it and move on.

**Step 2: Pull the data.** For the last 30 days and 90 days, get:

- Account-level performance trends (spend, CPM, CTR, CPC, CPA, ROAS, frequency)

- Campaign and ad set breakdowns, top and bottom performers by spend

- Top 10 ads by spend with creative-level metrics, plus any fatigue signals (rising CPM, falling CTR, frequency >3)

- Dataset / pixel quality, event match quality, and tracking errors

- Industry benchmarks for my vertical and objective

- Meta’s opportunity score and any diagnostic flags or auction warnings

**Step 3: Write the audit.** Structure it like this:

1. **Verdict** One paragraph. What’s actually going on in this account. Be blunt.

2. **Account health** Pixel, CAPI, event match quality, dataset issues, tracking gaps.

3. **Performance** How spend is pacing. What’s working, what’s bleeding money. Cite the numbers.

4. **Creative** What’s winning. What’s fatigued. Patterns I should double down on or kill.

5. **Structure & targeting** Campaign architecture, audience overlap, CBO/ABO setup, budget allocation problems.

6. **Benchmarks** How I compare to industry on the metrics that matter. Where I’m ahead. Where I’m behind.

7. **Top 5 actions this week** Specific, prioritized by impact. “Test more creative” doesn’t count. Tell me exactly what to test, in which ad set, and why.

**Rules:**

- Cite real numbers from the data. No vague claims.

- If data is missing, broken, or looks off, call it out.

- Skip corporate hedging. If something is broken, say so.

- End with the 5 actions. That’s what I’ll actually do on Monday.

Higgsfield in the loop

I still think we’re in the first inning of AI creative, and I wouldn’t trust Higgsfield for creative autopilot but it’s very cool to see. Here are some static assets I created for GrowthPair:

It's crazy to think the account audit and these static assets all happened inside of Claude. I was feeling a bit fancy so I asked Claude to animate a static asset into a short video:

You might be thinking these assets are super generic, and you're right. These were quick demos. The next set used a more detailed prompt for the GrowthPair brand and our target customer.

Create an ad using the growthpair.com look (colors, typography etc) and add some imagery 
so it’s not solely plain text on a background. Take inspo from ad libraries from our 
competitors on Meta like MarketerHire and best practices around Meta ad creative.

Much better. The fix took 15 extra seconds.

Layer 3: Claude’s live artifacts and tasks

Since Meta is connected to Claude, you can use all of the data to create beautiful dashboards using live artifacts. I wrote a morein-depth essayabout how to build these dashboards in minutes so I won't go into details. Here's an example of a dashboard I built for thethought leader adswe run on LinkedIn.

Layer 4: Learning loop with GitHub

The layer that pulls this all together is feeding your campaign learnings into ashared GitHub reposo your entire team and Claude have context on historical performance.

Source of truth — it never forgets how one of your tests performed.

To build out this layer, you’ll need to be using Claude Code so you can upload all this information into GitHub. Here’s how:

1. Create a folder on your desktop and connect it to Claude Code
2. Prompt Claude Code with something like this:I want to start running my paid ads on GitHub/ Claude Code. The idea is to house our campaign learnings here so that the entire team and Claude know what’s worked and what hasn’t. The entire team will update the folders with their tests. Can you ask any questions necessary and help me set this up so that we have the right foundation to get this kicked off?
3. Claude Code will ask questions and guide the setup for your folder structure
4. Create a repo on GitHub (important: make it private)
5. Give Claude Code the GitHub repo link and it’ll create your initial commit
6. Add your teammates to repo in GitHub (Repo Settings > Collaborators > add their GitHub usernames)
7. Using GitHub Desktop, click “Add Local Repository” and navigate to your marketing team folder that Claude Code created
8. It’ll detect the existing repo, and then you can hit “Push origin”

I believe that even outside of "The AI-Native Paid Ads System," all marketing functions will run their teams out of a GitHub repo. If you start with this, you can always add the files from this GitHub repo into a larger marketing org repo.

TLDR — how to action on this

1. Set up your connectors: Install Meta and Higgsfield connectors in Claude. It takes 2 minutes.
2. Buildclaude.mdand skills: Having these files loaded into Claude will make it much stronger every single time you prompt it.
3. Run your first AI audit: Use my exact prompt above on your biggest ad account. See what it catches that you missed.
4. Test one creative angle: Take the audit’s creative recommendations and spin up 3 new ad variants.
5. Build a simple dashboard: Use Claude’s artifacts to create a live performance dashboard for your campaigns.
6. Schedule weekly competitor research: Set up one automated task to track your top 3 competitors’ ad changes.
7. GitHub repo: Create a repo on Github and ask Claude to share learnings on a weekly cadence.

Until the next one,

Jonathan

Share

13
5
2
Share