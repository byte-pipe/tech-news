---
title: I Analyzed 100 B2B Marketing Teams with Claude Code. Here's the full report.
url: https://newsletter.mkt1.co/p/state-of-marketing-report-teams-part-1
site_name: tldr
content_file: tldr-i-analyzed-100-b2b-marketing-teams-with-claude-cod
fetched_at: '2026-04-27T06:00:31.829271'
original_url: https://newsletter.mkt1.co/p/state-of-marketing-report-teams-part-1
author: Emily Kramer
date: '2026-04-27'
description: 'A research report on marketing teams at 100 B2B companies: team size, hiring, CMO titles, and what the ''top'' startups are actually doing in 2026.'
tags:
- tldr
---

# I Analyzed 100 B2B Marketing Teams with Claude Code. Here's the full report.

### 19 graphs covering everything from marketing team size, to tool mentions in job descriptions, to the prevalence of CMOs vs CROs. Part 1 of a 3-part series.

Emily Kramer
Apr 21, 2026
86
2
Share

👋 This is a monthly free edition of MKT1 Newsletter—a deep dive into a B2B startup marketing topic, brought to youbySoftr,Attio, and42 Agency.Upgrade to a paid subscription for:Full access to our newMKT1 MCP Server|100+ templates & resources|Post toMKT1 Job Board|MKT1 Newsletter Archive|$40K+ in discounts in theMKT1 Perk Stack

Subscribe

Iaccidentallyembarked on my first big research report using Claude Code over the past week. The result: a 3-part newsletter on the State of Marketing based on my research of 100 B2B companies from seed-stage to recently public.

Part 1 covers the State of Marketing Teams, Part 2 will cover the State of Marketing Activities (some sneak preview stats from part 2 below), and Part 3 will cover how to make—and even distribute—these reports in Claude Code.

Let’s back up, here’s how this report started. An advisee asked me a simple question: “If we want to start a newsletter for our B2B startup, what platform should we use?” Usually, my brain goes blank thinking of relevant companies to look at when marketers ask me questions like this.

Then I realized with Claude Code I could create and save a list of 100 fast-growing, forward-thinking B2B companies of various sizes, stages, and industries.So I built the list and made a skill to research all 100 companies at once. And then I couldn’t stop. I ended up researching over 90 data points for those companies. I blew past the $100 Claude plan into the $200 plan. I still had to spot-check data and correct graphs manually many times over, but now I can add a company or a data point and re-run the skill for fast answers. And I have about 30 graphs to share with you all.

If you're thinking "how is this different than just using Claude Chat for research?"—reading this series will show you.Specifically, part 3 will cover the details of building a report like this, saving it as a skill, and releasing it via an MCP Server. In other words, I'll explain exactly how to produce researched work, not AI slop.

Subscribe so you don’t miss part 2 and 3 over the next 2 weeks.

Subscribe

## Recommended products & agencies

We only include sponsors we’d recommend personally to our community. If you are interested in sponsoring our newsletter, email us atsponsorships@mkt1.co.

Softr: Vibe coding is great until you need to build a database, multiple pages, logins & permissions, and hosting. Softr’s new AI Co-Builder handles all of it. Build any internal marketing tool yourself: an influencer CRM, advisory board app, enablement library, etc.🔓Offer:Use code MKT1-50 for 50% off the Business Planfor 3 months (expires 12/31/26).—Attiois the AI native CRM with built-in enrichment, flexible workflows, and fast set up. Their new “Ask Attio” agent has changed how I personally CRM: it can update fields, do company research, and more with a single AI prompt.🔓Offer:MKT1 subscribersget 15% off your first year.—

42 Agencyis a MOPs & paid media agency that kicks off differently. They start with a Revenue Opportunity Analysis that digs into your ad accounts, CRM, and closed-lost deals to find where revenue is leaking. Then they fix it.🔓Offer:First 5 companies to redeemget 15% offa revenue opportunity analysis.

## In this newsletter:

* Part 1 - This newsletter:State of Marketing Teams, 19 graphs, each with additional analysis you can read or scroll right past
* Part 2 - In your inbox in a few days:State of Marketing Activities, with an emphasis on social and webPart 3 - Coming end of April:Claude Code researching and reporting lessons and takeaways based on creating these newsletters
* Next Buildathon:There will be a buildathon related to researching companies in Claude Code, date TBD. In the meantimesee the recap and replay of our first Buildathon on building a marketing-strategy skill in Claude Code here ➜

Bonus for paid subscribers—2 new skills related to this research & Report inour MCP Server:

1. /state-of-b2b-marketingQuery the full dataset behind this report: 100 high-growth B2B startups, 90+ data points each, covering GTM motion, team composition, social, ads, homepages, CMS, conversion, and AEO readiness.
2. /high-growth-b2b-company-listMy curated list of 150 high-growth B2B companies ready as a reference set. Run quick research across a solid list of companies instead of starting from scratch every time.

# The State of B2B Marketing, Part 1: Marketing Teams

##### *Based on what Claude Code can research with Emily Kramer’s prompting

## Methodology

Before I show you all thebeautifulcharts and graphs me, Claude, and Figma made together, some notes on methodology:

* I chose 100 B2B startups, mostly venture-backed, from seed to IPO, concentrated in growth-stage. I targeted companies with recent funding rounds, high-growth trajectories, that are referenced as a startup to watch, or are default B2B tools we all know. Claude helped me pull this list together, of course.
* I tried to include a range of GTM motions, audiences, categories, and stages. But it’s concentrated in AI,which is where so much of the fundraising is going right now.This is a curated list, not a random sample. It’s biased and not statistically significant (for example, since I chose “hot” companies, more are hiring than the average startup).
* Categorizing companies into clean buckets is a bit of a fool’s errand.You might have grouped them differently, but I did my best to group companies based on the audiences they target. (See the diagram above for the 8 buckets I used and the companies in them.)
* I pulled and analyzed data via Claude Code using MCP servers(Figma, Clay, Attio, Airtable, and theMKT1 MCP Server). Claude scraped LinkedIn, web pages, ad libraries, and pulled in other sources to validate.
* This report is meant to give you reference points and examples,and show you what the “top” B2B companies are doing in marketing. Despite my best efforts,it may have mistakes. No one’s perfect…not even me or Claude.

### How does this sample break down by GTM motion?

I categorized a lot of the data in this report by GTM motion and category, in addition to total funding. Why? Most marketers benchmark against “companies our size.” But there are other “cuts” that dramatically shape what marketing does: GTM motion (how people buy) and category (what you sell).

Quick definitions:

* Self-serve:You can buy without talking to sales. (Some call this PLG. Close but not the same, but that’s a different newsletter.)
* Sales-led:Most buyers go through a rep. You’re getting a demo whether you want one or not.
* Hybrid:A combination of the two, you can sign up or buy without talking to sales or you can buy through a rep, depending on your deal size, use cases, etc.

Two things worth calling out:

1. Certain categories default to certain GTM motions. Vertical-focused startups like Harvey (legal-tech) and Abridge (health-tech) go sales-led because the TAM is narrower and the buyers expect a relationship.
2. I see a lot of marketers try to run a self-serve or PLG playbook at a sales-led company (or vice versa) and fail.Throughout this report, you’ll see how yourGTM motionchanges what happens in marketing.

## The state of marketing team size

🎯 MY FAVORITE STATCompanies selling to marketers have bigger marketing teams as a % of headcount,with an 8.3% median (8.1% mean). That's more than 2x the rest of the sample. Sample size of 8 is small, but way to practice what you preach.

Let’s start with what’s going on with marketing teams. Obviously, the composition of teams are shifting, agents and AI are doing things humans once did, and we all feel a bit anxious about the situation.But the fast-growing startups in this sample are hiring marketers in large numbers.These companies realize that at a time when it’s easier than ever to build products, marketing, distribution and brand just might be the moat.

Quick caveat/reminder: I scraped data from web, usingClay, and spot checking many careers pages and LinkedIn searches, but this data isn’t perfect, its meant to be directional and a snapshot of what’s going on. It’s not statistically significant.

### How big are marketing teams right now?

➜ The median marketing team size is 13; the mean is 44

As a refresher: Median is the middle value in an ordered dataset, and mean is the average. My team made me put this math lesson in.

* I use median as the main measure of the “middle” throughout this report, since the big companies on the list pull the average up substantially.Canva and HubSpot have hundreds of marketers each!
* Team size data on its own isn’t particularly interesting unless you slice it against other datapoints, so let’s slice and dice this data.

➜ Marketing is ~4% of company headcount

* Looking at the above team size charts, I immediately wanted to know what % of headcount sits on the marketing team.
* I’ve long thought5% was a good benchmark for marketing as a share of headcount(or higher depending on GTM motion and stage), and I’ve fought for that headcount when I’ve led marketing. But, the median in this sample is4%(mean 4.4%), a bit lower than I expected.
* Marketing team sizes may get smaller in the future (thanks AI), but so will other teams in the org.So, I expect this ratio to stay roughly steady.Maybe I’ll run this skill again in 6 months and see if that holds.

### How does marketing team % shift by stage, category, and GTM motion?

When you slice marketing team size, things get more interesting. A few stats stand out:

➜Below 250 headcount, marketing teams are 5%+ of total headcount.

* Above 250, marketing is consistently 2-4%. As headcount grows, the team size grows, but % of total headcount shrinks.
* Note: It may look like a massive jump in median marketing team size from 500-1K employees (18 marketers) to 1K+ employees (71 marketers). But the 1K+ bucket is a wide range, covering companies from 1,000 people to 15,000.

➜ Companies selling to marketers hire the most marketers.

* The 8 companies building products for marketers have a median marketing team of 8.3% of headcount. The other companies combined median is just 3.8%. It’s a small sample, but clearly having more marketers on the team when you target marketers is beneficial.
* Companies selling to sales teams don’t hire as many marketers. The 6 companies in that bucket run marketing at just 2.9% of headcount.Maybe their sales teams pick up the marketing slack?

➜Self-serve companies have the biggest marketing teams.

* I expected companies with hybrid GTM motions to have the biggest marketing teams since they have the widest range of channels and content types, plus more ops complexity.
* Butself-serve “wins”, with marketing as 5.6% of headcount. Marketers compensate for the lack of a sales team.
* And if you have any self-serve motion (hybrid + pure self-serve) the median is 4.3% vs. the23 pure sales-led companies with a 3.2% median.

🥤 TAKEAWAY:Marketing team sizes are a bit all over the place. I love a tidy benchmark, and2-4% of total headcount is the typical range. But GTM motion, category, and founder preferences shape the actual number a lot.

Brief intermission:Don’t hold another marketing meeting without Granola. It’s now in the MKT1 Perk Stack, which totals $40K+ in exclusive discounts for annual paid subscribers, including Framer, Typeform, Primer, PhantomBuster, and Storylane.Go to the Perk Stack ➜

## The state of marketing leadership

🎯 MY FAVORITE STATOnly companies with $50M+ in total funding had someone with a “CMO” titlein our sample of 100 companies. So don’t expect the C-level title, even if you’re doing the job, until there’s more money in the bank!

Next up let’s look at who’s leading these teams. In my experience, companies that do marketing leadership well have one person owning the whole function with the right title and real scope. Otherwise you end up with silos, gaps, andrandom acts of marketing.

### What titles do we give marketing leaders running the whole team?

Note: These graphs only count the senior-most marketing title per company. A company with a CMO, likely also has VPs too, they just aren’t represented here.

➜ 68% of companies have someone leading all of marketing, but with a mix of Head of, VP, and CMO titles

* Early-stage teams often have no one leading all of marketing.40% of companies with less than $50M raised don’t have a unified marketing leader;53% have someone with a “Head of” title.
* That doesn’t mean they have no marketers.Half (3 companies) have someone running a sub-function like content or demand gen.The other half (3 companies) have no marketing hires yet.
* Only 2 companies with under $100M raised have CMOs: Puzzle andWispr Flow(and given Wispr’s marketing, I think this is a great call, it’s so good!)
* By$500M+ raised, 81% of companies have a unified marketing leader,and 45% have a CMO.

➜ It’s hard to get a CMO title, we found only 27 CMOs across 100 fast-growing companies

* If you have the title, you’re an anomaly not the norm. This bums me out (and without the title you are often under-leveled on compensation too).
* As fundraising goes up so do C-level titles, which does make sense, but still why so low? So let’s compare this to CROs at the same companies to see if they have more seats at the table.

### Are there more CMOs or CROs? Or more companies with no C-level GTM leaders?

➜ 59 of 100 companies have no CMO or CRO.

* Three-quarters of those 59 companies have raised less than $500M,meaning C-suite GTM titles are mostly a late-stage phenomenon.
* On the flip side,15 companies have both a CRO and CMO, all late-stage and mature: Benchling, Chainguard, Datadog, Figma, etc.

➜CMOs and CROs are basically tied

* 29 companies have a CRO. 27 have a CMO. 59 have nieither.This was suprising to me, I thought CROs would be in much higher numbers than CMO.
* CRO-only companies (14) skew AI infra and sales-led,like Cohere, Rippling, ServiceTitan, etc.

🥤 TAKEAWAY:Plenty of B2B companies are growing fast without a CMO. Would they grow faster with one?I think yes, but the data can’t prove it. Do marketers deserve more senior titles and the same seat at the table as a C-level sales leader? I also think yes.

## The state of marketing hiring

🎯 MY FAVORITE STAT(s)

* 100% of companies with more than $500M raised are hiring marketers.
* ~1/3 of open marketing roles are in ecosystem and events-related functions.These channels are doing the heavy lifting while inbound and outbound both struggle.

Despite fears of AI taking marketing jobs, companies are still hiring in big numbers (at least at the fast-growing startups in this sample). This is likely because so much funding is flowing into AI-era B2B companies right now. I hope it lasts. In the meantime, learn those AI skills!

### Are there open roles out there?

➜ Yes, companies are hiring marketers. 87 of the 100 in our sample have open roles, many with more than 1

* Across those 87 companies, there are 507 total open marketing roles. That’s an average of ~6 per company.
* But,85% of the open roles are at companies with $250M+ raised.
* The 13% not hiring skew small and early:Paper, Obsidian, Navattic, etc.

➜ 100% of companies with more than $500M in funding are hiring marketers right now

* All 42 late-stage companies($500M-1B, $1B+, pre-IPO, and public) on our list have at least one open marketing role.
* Most open roles are from companies you’d expect: Anthropic, OpenAI, Stripe, Deel, Datadog, and Rippling all have more than 20 roles open each.

### How does sales hiring compare to marketing hiring?

➜ 78% of companies are hiring for both marketing and sales right now

* This makes sense, if you are growing fast, you are hiring for both teams, but there was more overlap than I even expected.
* 87 companies are hiring marketing,84 are hiring sales,7 aren’t hiring for either.

➜ There are more than 3x as many sales roles open compared to marketing, but most of this is due to a few companies hiring A LOT of sales people

* Rippling alone has hundreds of open sales roles (yes, hundreds). Datadog and HubSpot have over 100 each.Remove those three outliers and the ratio of marketing to sales roles drops to ~1.5x.
* Sales open roles counts are often misleading. Some companies list 1 role for “AE” when they are actually hiring 5. In the other direction, some companies include regional variants for potentially just 1 role. Given this, I think the number of companies hiring for either function in general is more interesting.

Looking for a new role?Inspired by the Claude Code skill I built to scrape roles for this report, we created a new and improved job board. It now has more roles, new filters, and an easier way for paid subscribers to submit jobs for approval.Go to the job board ➜

### What marketing functions are companies hiring for most?

➜ No surprise, Growth and Product Marketing are by far the biggest buckets

* Growth / Demand Gen / Paid leads with 99 open roles. Product Marketing is right behind at 90.
* Together they make up 37% of all open marketing roles.

➜ Events and ecosystem hiring point to what actually works in 2026

* 34% of open marketing roles are in ecosystem and events-related functions(partner, field/events, community, DevRel, and PR). I’ve been saying this for a while, with inbound declining, outbound saturated, and AI slop, human interactions and recommendations matter.
* Field / Eventsis the #3 bucket with 60 open roles. 5 years ago during peak-Covid times we never could have imagined this!
* Ecosystem marketingroles add up: Partner (16) + Social/Community (44) + DevRel/Advocacy (28) + Comms/PR (23) = just over 100 roles. Companies are hiring marketers to orchestrate relationships with partners, creators, communities, and media to piggyback on trust and credibility.

### What do marketing job descriptions say in the AI era?

➜ If you don’t mention AI in your JD, you’re in the minority

* 84% of JDs mention “AI,” 18% mention “agent” or “agentic,” 6% mention “LLM.” Clearly, you need to use AI in today’s marketing roles, but we knew that already.
* Some of the companies that don’t mention AI in their JDs (like Framer and Railway) are very AI-forward. Maybe it’s so obvious it doesn’t need to be said?

➜ The evolution of “cringe”

Cringe is subjective, but here’s what‘s cringe to me just for fun…

* I was expecting “ninja,” “rockstar,” and “hacker” to show up, but I guess we’ve finally moved on (thankfully).
* Instead we have new candidates for cringe like “passionate” (26%), “grit” (3%), and “hungry” (1% - not in chart). It’s giving “Let’s all drink protein-shakes together" vibes.
* You might disagree with me here, but I put “storyteller” in the cringe bucket. It was theWSJ articlethat did me in.

### And what tools do they mention?

➜ Figma and Notion at #1 and #2 was a surprise. Stripe at #6 has an explanation.

* I’m surprised Figma clocks in at #1 (16%), especially given how many marketers prefer Canva. (For the record, all of the graphs in this report were made with the Figma MCP in Claude Code + my obsessive editing.)
* But a caveat for this whole chart: anytime a well-branded tech company shows up in JDs, some of those mentions are name-drops (social proof customer lists, shared investor callouts), not actual tool requirements.Stripe at #6 is the cleanest example — almost all customer name-drops, not actual usage. Figma’s 16% is partly that too: Notion, Hex, and Sanity all name-drop them.

➜ AI tools have taken over, but Marketo is still hanging on

* OpenAI (10%), Claude (7%), Anthropic (6%), and ChatGPT (5%) all show up at meaningful rates. Each one shows up roughly as often as HubSpot (8%) or Salesforce (11%).Lump them together and “AI labs” is the most-mentioned tool category in marketing JDs.
* AI-native tools also show up:Clay(6%), Cursor (5%),Replit(4%),Lovable(4%),Gamma(3%). Honestly less than I expected for Clay and Lovable.
* Meanwhile, Marketo (4%) is still hanging on at roughly the same frequency as Slack and GitHub. Not dead yet.

### What are the marketing roles of the future?

I’ve been talking a lot about theGen Marketer skillsetover the last 9 months. So with the job scraping skill I made for this report, I pulled some roles that reflect the need for marketing generalists, who can execute cross-channel campaigns, and work efficiently with AI and agents. Here are some that I found:

* Ramp — Agentic Operator, Growth Marketing:Asks for familiarity with agentic AI, MCP, and evals; if you’d showed me this 12 months ago I would have been very confused!
* Cursor — Marketing Systems Lead:Systems thinker meets marketing ops. Cursor pitching marketing as a systems architecture job is on-brand for an AI coding tool.
* Clay — Chief of Staff, Marketing:I’ve long been a proponent of a CoS in marketing(when leading marketing teams, I called the role something else to get the headcount!). And it’s a perfect role for a Gen Marketer skillset.Lovable also has this role.
* Airtable — Program Manager, AI Programs:Dedicated marketing role for AI-specific programs. Sounds like a Gen Marketer is needed here too.
* Lovable — Field Marketing Lead, Hackathon:Events role written specifically for builder / developer hackathons. A new field-marketing archetype for the AI era.
* Gamma — Product Evangelist:This “Evangelist” role is a mix of a product marketing, content, and DevRel role. Anthropic and Lovable are hiring for "Evangelist" titles too. These PLG, AI-first companies need to educate the market, and this is a new way to do it.

🥤TAKEAWAY:There are marketing jobs out there. And yes,you do need AI skills to get them.

Companies are asking for people with broad skillsets and loading the JDs with AI tools and AI buzzwords. But the job titles haven't caught up yet; companies are still mostly hiring for specialist roles. The next time I run this report, I expect to see more generalist, campaign lead, and marketing chief-of-staff titles, and fewer narrow sub-function JDs.

### But what’s interesting in this report isn’t just the data…

It’s what this means for how marketers research and distribute content…

It’s now possible to run your own research in Claude, then ship what you learnback to your customersin Claude, where it becomes immediately actionable.

That’s what I did with this report.Claude both co-created thefuel and is the engine for distribution.The research lives as two skills in our MKT1 MCP Server. Now you can use them to benchmark yourself against 150 companies in B2B, or answer the kinds of questions I get asked as an advisor all the time.

### 2 new research skills on the MKT1 MCP Server

1. /state-of-b2b-marketingQuery the full dataset behind this report: 100 high-growth B2B startups, 90+ data points each, covering GTM motion, team composition, social, ads, homepages, CMS, conversion, and AEO readiness.
2. /high-growth-b2b-company-listMy curated list of 150 high-growth B2B companies ready as a reference set. Run quick research across a known-good list instead of starting from scratch every time.

Add the MKT1 MCP Server

### Loving our MCP Server, want to talk about it?

Good news, we’re launching a Slack just for talking about using Claude Code or Cowork and/or our MCP Server. It’s invite-only for paid subscribers using the MKT1 MCP Server users.Get on the list ➜

### New to MCP Servers and Claude Code?

We hosted a Buildathon that will help you get up to speed.Watch the replay ➜

## Reminder: Parts 2 and 3 coming in the next 2 weeks

I’m increasing the newsletter cadence temporarily because what was supposed to be one newsletter turned into three. More graphs, more stats, and more about how I used Claude Code to pull this report together, coming very soon. After that we’ll go back to our normal 2x/month cadence at MKT1,unless I get carried away in Claude Code again for days on end…

## Even more from MKT1

🙏 Brought to you by:Softr, an AI platform for business apps;Attio, the AI CRM for modern businesses; and42 Agency, a Demand Gen and MOPs agency.All 3 companies have offers for MKT1 subscribers!

🤖 MKT1 MCP Server:Add MKT1 to Claude Code, Chat, and Cowork.Paid subscribers get our full library of skills and templates, including the 2 new research skills from this newsletter.

👩‍💻MKT1 Buildathons: Missed our first Buildathon?Watch the replayto see how to build a /marketing-strategy-skill in Claude Code. Want in on the next one?Get on the waitlist.

📦 MKT1 Unboxing:Watch our video series to see Kramer (that’s me) unboxMutiny,Wistia,Luma AI, &Attio.

🥞 MKT1 Perk Stack - New Perk:Exclusive discounts worth $40K+on our favorite GTM tools. For annual & superfan paid subscribers only.We just added 3 months free of Granola, check it out!

🧰 MKT1 template library:We have100+ templates and resourcesavailable to paid subscribers in our template & tool library.

🧑‍🚀MKT1 job board - new & improved:Jobs from the MKT1 community(it’s free to post as a paid subscriber). Andour candidate formif you’re looking for a new role (option to remain anonymous included!).

86
2
Share
Previous