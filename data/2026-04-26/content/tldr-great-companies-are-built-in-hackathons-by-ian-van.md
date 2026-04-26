---
title: Great companies are built in hackathons - by Ian Vanagas
url: https://newsletter.posthog.com/p/great-companies-are-built-in-hackathons
site_name: tldr
content_file: tldr-great-companies-are-built-in-hackathons-by-ian-van
fetched_at: '2026-04-26T19:44:52.567275'
original_url: https://newsletter.posthog.com/p/great-companies-are-built-in-hackathons
author: Ian Vanagas
date: '2026-04-26'
description: You should run more hackathons. Here’s how to do them well.
tags:
- tldr
---

# Great companies are built in hackathons

### You should run more hackathons. Here’s how to do them well.

Ian Vanagas
Apr 21, 2026
32
3
Share

PostHog hackathons have generated millions in revenue.Session Replay,Data Warehouse,Logs,Workflows, andPostHog AIwouldn’t exist without them.

We take multiple days out of every year to do them. They are days our team looks forward to all year. They’re an integral part of our culture.

Yet for many companies and people, hackathons are seen as a waste of time. A distraction from important “real work.” An act of performative participation.

This is because they think about and do hackathons wrong.

## Hackathons are an innovation engine, but only if separate from work

Hackathons fail when they’re not separate from regular work or used as cover to accelerate existing work. We have two simple rules to prevent this:

1. You should work on totally new things.Hackathons are for ambitious, weird ideas, trying new things, and learning new technologies. Pitching ideas on the roadmap is forbidden.
2. You should focus 100% on the hackathon.We protect people from regular work by running our hackathons duringoffsites, where we have dedicated time and coverage plans for support and incidents. DigitalOcean employswork embargoesfor hackathons run in an office.

These rules fuel the innovation engine because people are unconstrained by their day-to-day work, and have a safe space to work on ambitious bets without distractions.

We’ve seen first-hand how running hackathons like this can lead to transformative new products and features that influence the direction of the whole company.

In PostHog’s earliest days, an engineer decided to build Session Replay during a hackathon based on user feedback, despite co-CEO James arguing it would take too long and split the focus of the company.

It ended up being wildly popular, with over 50,000 daily active users, and led us to become the multi-product company we are today. As an early Facebook engineer noted,code wins argumentsand hackathons are a great venue for this to play out.

Remember this:Give permission and cover for your team to focus on the hackathon and ignore day-to-day work. Not doing so leads to low participation, burnout, and unambitious hackathon projects.

## Hackathons are for everyone

When you think about hackathons, you picture a bunch of engineers huddled around laptops, coding up a storm. This is mostly what our hackathons look like with one difference: they’re not just for engineers.

LLMs let anyone build software. When this is combined with specific domain expertise and a sprinkle of motivation, it leads to the dozens of hackathon projects our “non-technical” team members have built, including:

* Games like Three Button Dungeon, Awkwardness Avoider, and Flappy Hog forDeskHog, our open-source developer toy.
* Instagram Storiesfor PostHog showcasing our latest features in a format everyone’s familiar with.
* A DPA generatorthat automates and brings joy to an otherwise boring legal document.

Non-technical team members can require more encouragement to pitch projects and support to ensure they can contribute, but the cultural benefits of getting them involved are worth it.

Getting unfamiliar parts of the organization to work together breaks down silos between technical and non-technical teammates.DigitalOceanfinds “the teams that have created truly innovative products and addressed real, practical problems are cross-functional teams with members from all across the company.”Twilioactively discourages “lone wolf” ideas to make this happen, as do we.

Beyond the hackathon, getting non-technical people building opens their eyes to what’s possible and encourages them to explore more. Trying out new technologies often leads to adopting them in day-to-day work. That’s why companies likeJane,Uber, andVantaare all driving AI adoption with hackathons.

Ultimately, we agree withSlack, who found that “the more people participate, the better your outcomes” – both during the hackathon and beyond.

Remember this:Encourage everyone to participate in hackathons, including people who would never see themselves as hackathon participants. Give them the tools they need to succeed (like Claude Code) and create cross-functional teams.

Curious what a PostHog hackathon actually looks like? We filmed a behind-the-scenes documentary about one and you can watch it below:

## Demos aren’t optional

At our2024 hackathon, the “RealTimeHog 3000” team built a livestream service that displayed events as soon as they hit our ingestion Kafka topic using server-sent events.

It was cool when they showed this by getting people to click around on the demo site they built, it was even cooler when they had a “one more thing” moment and showed off a globe onposthog.comof all the events being captured worldwide into our US and EU Cloud services.

Requiring demos is a forcing function. You want to have something worth showing off, so initially ambitious plans quickly become more realistic to ship something real.

They’re also fun. When someone says “this is available now” or “we already have users using this,” there are always “ooohs” and “ahhhs.” People love a little showmanship and it’s fun to be in the spotlight.

While demos are mandatory, judging and prizes are optional and arguably undesirable.We hire peopleto “be the driver.” They don’t need artificial motivation like gift cards or merch to do that. We also don’t want people to only build projects they think will win, or what the bosses want to see.

When you give a self-motivated and autonomous team time and space to work on what they think is best, they’ll surprise and delight you with what they build. The results of our hackathons are proof of that.

Remember this:Let people know they’ll be demoing at the start and make sure everyone does. As a bonus, keep track of what people demo. It’s easy for these valuable ideas to get lost. Writing about what people built also makes forgreatblogcontent.

## The best hackathon projects ship

A common complaint about hackathons is that they are a waste of time. You spend a lot of time and effort that’s all lost after a few days, but it doesn’t have to be like that.

What does this look like in reality? OurLogsproduct can give you an idea:

1. By the end of the 2025 offsite hackathon, the team had built OTEL log capture into ClickHouse, a query API, and a basic frontend.
2. After the offsite, the team felt it was worth continuing as Frank was looking into an internal logging solution anyways. He thought it could be “good enough” within one sprint.
3. Two weeks later, it was! It had the features we needed: filtering, search, and speed.
4. Logs then went on the backburner, but Tim mentioned it as a product we wanted to build soon and customers requested it.
5. Four months later, Frank revisited it, which was made easier because the product had already shipped internally. Ahead of Q4 planning, Logs was identified as a priority, made its own team, and moved quickly towards a proper launch.

We don’t have a perfect hackathon-to-production pipeline. Instead we rely on aproduct engineer“being the driver,” pushing the project forward, and having the freedom to do so.

This wouldn’t have been possible without some slack after the hackathon to wrap up the project, ship what we’ve built, and make longer term plans. Doing this makes it easier to revisit and improve in the future.

Getting real customer demand was a big help, even if that customer was us. We looked at what Datadog would charge us for Logs and saw it was a minimum of $260,000 per month, providing a big incentive to work on it.

We don’t expect all projects to ship to production, deadend hackathon projects are part of the messy process of innovation, but everyone starts knowing that great projects can end up in production.

Remember this:Encourage people to “be the driver” to take their project as far as they can and give them some slack after the hackathon for them to do it.

## Make hackathons a tradition

Out of 17 projects from at our2025 hackathon in Mexico, 10 were shared in our#hackathon-ideasSlack channel in advance.

This is the power of making a hackathon a tradition. People are more likely to share ideas throughout the year when they have a space for it and know they might actually get worked on. Good ideas can come at any time and often sound like weird ideas.

This is not an original idea.Early Facebook hackathonsfeatured an internal wiki to share ideas. Some of their “most-loved products” started this way like Video, the Like button, Chat, Hip Hop for PHP, and even Timeline.

The added benefits of making your hackathon a tradition are:

* People are less restless working on things because they know they’ll have a chance to flex their other muscles at hackathons.
* Many hackathon ideas are just inspiration for features that should be built as part of a team’s day-to-day work. A roadmap often misses the ambitious ideas hackathons encourage.
* It’s a perk and cultural cornerstone. The hackathons show we value autonomy and give people the time to make the most of it. It also creates lore, like the time our AI chatbot was insistent PostHog’s mascot was a character named “Hoge.”

Making your hackathon a tradition turns them into a promise: that the company will keep making space for the weird and wonderful things they believe in, not just what’s on the roadmap. This is what really helps a hackathon turn into a foundation for building a great company.

Remember this:Start referring to your hackathon as your “annual hackathon.” Manifest it. Create a #hackathon-ideas Slack channel and post your random “we should build this” ideas in there.

Words byIan Vanagas, who has not forgotten about Hoge.

Subscribe for everything you need to crush your next hackathon

Subscribe

## 🦔 Jobs at PostHog

Join us at our next hackathon with this one easy trick (applying):

* Product Engineer
* Technical Account Manager
* Payroll Manager
* Backend Engineer - Ingestion
* BDR

## 🛋️ Late night reads to procrastinate to

* A beginner’s guide to testing AI agents- Radu Raicea
* You’re doing lifecycle emails wrong- Sara Miteva
* Untangling Tokio and Rayon in production: From 2s latency spikes to 94ms flat- Matheus Batista
* Hack Days- Alex Watt
* Software Bonkers- Craig Mod
32
3
Share
Previous