---
title: 10 Months Ago, We Were Barely Using Salesforce. Now It’s Our AI Agent Hub. | SaaStr
url: https://www.saastr.com/10-months-ago-we-were-barely-using-salesforce-now-its-our-ai-agent-hub/
site_name: tldr
content_file: tldr-10-months-ago-we-were-barely-using-salesforce-now
fetched_at: '2026-03-03T06:01:03.667824'
original_url: https://www.saastr.com/10-months-ago-we-were-barely-using-salesforce-now-its-our-ai-agent-hub/
date: '2026-03-03'
published_date: '2026-02-28T15:08:11+00:00'
description: 10 Months Ago We Were Barely Using Salesforce, Now It's Our AI Agent Hub (7 minute read)
tags:
- tldr
---

# 10 Months Ago, We Were Barely Using Salesforce. Now It’s Our AI Agent Hub.

byJason Lemkin|Artificial Intelligence (AI),Blog Posts,SaaStr.Ai

#### Here’s what no one tells you about deploying 20 AI agents across your business: they all need somewhere to live.

Ten months ago—Salesforce had almost become shelfware for us.  Even though I’ve been a customer for 20 (!) years.  Why? Our sales team had dwindled to 3 people. Two of them wouldn’t even log into Salesforce at all.  Even when we literally paid them $200 a month to do so.

We were paying for a system nobody was using.

When we added Momentum—the AI tool that automatically logs every sales call to Salesforce without reps lifting a finger, which Salesforce just acquired—one of our reps quit. Quit. Not because the job got harder. Because the idea of their activity being automatically captured and logged was a dealbreaker.

There was almost no point 10 months in logging into Salesforce anymore.  The data was stale, since the reps wouldn’t input any fo it.  We had such a tiny team that we had to operate on vibes and Slack and tribal knowledge and random spreadsheets.  It wasn’t great.

Then we went all-in on AI agents.

#### And suddenly Salesforce became the most important piece of software we run — again.

## Salesforce is Now How Our AI Agents All Talk to Each Other.  And Where All our Data Goes In.  And Out.

When you deploy your first AI agent, it’s exciting. It works. It books meetings, sends emails, scores leads, summarizes calls. Magic.

Deploy your second agent—same thing.

But by the time you have 5, 10, 15 agents all running autonomously across different parts of your business, you hit a wall if you haven’t mapped it all out.

Where does all that data go? How do your agents talk to each other? When they conflict, who wins?

Four AI SDR instances reaching out to six different customer segments. An AI that handles inbound qualification. Another that auto-fills CRM from every sales call. Another managing sponsorship pipeline. Another handling customer support tickets.  Another managing attendance to our global events.

All of them generating signals. All of them learning. All of them making decisions.

Without a hub, you get chaos. Agents stepping on each other. Duplicate outreach. Conflicting data. The left hand has no idea what the right hand is doing—and neither does the left AI agent.

Salesforce became that hub. Not because we planned it that way (although we would if we started from scratch today). Because it was the only system capable of handling it.

## How the Stack Actually Works Now

Let me be concrete about what “Salesforce as hub” actually means in practice.

* Momentumauto-transcribes and summarizes every sales call, then pushes structured data directly into Salesforce. Next steps. Objections. Competitor mentions. Decision-maker signals. No rep ever touches it. The AI captures it, structures it, and it lands in CRM automatically.
* Attentionlayers on top—more call intelligence, more signals, more context on every deal.
* We now run four AI SDRs, all syncing back to Salesforce
* Artisanruns three separate campaigns — ticket sales to past attendees, sponsorship outreach to warm relationships, and VIP reactivation for dormant community members. 15,000 messages in 100 days, 5-7% response rates.
* Monaco— Our latest AI GTM agent handles a fourth campaign for true outbound and has been booking meetings with some of the biggest names in AI. Not after weeks of setup. From Day 1 after go-live.

* And then there’sQualified for inbound— which you may have heard about because Salesforce just acquired them. Qualified powers our inbound AI agent, the “digital Amelia,” on saastr.com. It has full context on every visitor from Salesforce: whether you’ve attended before, your engagement history, your company, your fit against our ICP. That context is what makes it different from a chatbot. It’s not asking the same qualification questions a hundred times a day — it knows who it’s talking to.

(See a pattern? Salesforce acquired Qualified. Salesforce acquired Momentum. They’re buying the best agents in the stack and pulling them in-house. More on that below.)

* And then there’sAgentforce itself from Salesforce — which handles our win-backs.After SaaStr AI 2025, WE audited our Salesforce and found roughly 1,000 people who had filled out our “I’m interested in sponsoring” form, been automatically routed to a sales rep, and then received zero human follow-up. Ever. Warm, inbound, high-intent leads. Just… ghosted by our own team.

This is the perfect Agentforce use case, and here’s why: these people were already in Salesforce with full interaction history. Agentforce knows their past event attendance, previous sponsorship levels, every interaction with our team, their company info, their engagement patterns. When it reaches out, the email doesn’t feel like “recovered lead” outreach. It feels like a natural continuation of a relationship.

The results have been unlike anything else in our stack:

* 72% open rate.Not a typo. 72%. The emails get opened because they’re personal, contextual, and relevant — not because of a clever subject line trick.
* 10%+ response rateon contacts that were considered completely dead.
* ~3,000 emails sentto previously ghosted leads, already closing deals from people who got zero follow-up six months ago.

For comparison, cold email averages 2-4% open rates. Our Artisan outbound gets strong results at 5-7% response rates. Agentforce on warm CRM contacts at 72% open rates is a different category entirely.

The reason is simple and worth internalizing: Agentforce isn’t doing cold outreach. It’s doinginformedoutreach with full relationship context. The AI knows things about these prospects that even our human reps didn’t remember. That’s what native Salesforce integration actually means in practice.

The digital Ameliahandles inbound qualification in real-time via Agentforce — video, text, audio, however a prospect wants to engage. Qualifies sponsorship leads, answers attendee questions, routes conversations appropriately. Since we deployed, it’s handled hundreds of thousands of sessions, qualified over a thousand prospects, and contributed over $1M in closed sponsorship revenue — with another $2.5M in pipeline. 71% of our closed-won sponsorship deals in one recent month came from Agentforce-qualified leads. Our historic inbound average? 29-34%.

#### All of it logs back to Salesforce.

## The Pattern You Should Notice

Here’s something that tells you everything about where this is going:

Salesforce acquiredMomentum— the tool that auto-logs every sales call to CRM without reps touching anything. The same tool one of our reps quit over.

Salesforce acquiredQualified— the inbound AI agent that powers our digital Amelia.

They’re not building all of this from scratch. They’re buying the best agents in the market and pulling them into the platform. Agentforce is the umbrella. The acquisitions fill in the gaps.

What does that tell you? The CRM companies that survive the next five years aren’t the ones with just the best database. They’re the ones that become the hub for AI agents. Salesforce sees it clearly. That’s why they have 2,000 people working on Agentforce. That’s why they’re acquiring.

The uncomfortable corollary for us as operators: we now pay more for our individual agents than we pay for Salesforce itself. The agents are where the value is being extracted. Salesforce is providing the infrastructure. That’s the existential bet they’re making — that being the hub is worth more than being the database.

So far, for us, it’s working.

That’s the insight. When you go AI-first, the CRM doesn’t become less important. It becomes the operating system.

## What Changed (And What We Got Wrong Initially)

We made a classic mistake early on. With a lean team and a startup-speed culture, we assumed we could operate without CRM discipline. Slack, spreadsheets, tribal knowledge—it worked fine when humans were doing everything.

AI agents need structured data. They’re not good at reading a Slack thread to understand where a deal stands. They need clean records. Defined fields. Consistent data entry. All the CRM hygiene we’d deprioritized? Suddenly it mattered enormously.

The other thing we got wrong: we underestimated how much agents need to share context. Your AI SDR shouldn’t be reaching out to someone who just had a bad customer support interaction. Your inbound qualification agent should know that a prospect already had an outreach sequence. Your sponsorship agent should know a company’s full history with SaaStr before sending a “reconnect” email.

None of that coordination happens without a central hub.

## The Practical Takeaways

If you’re deploying AI agents—or planning to—here’s what I’d build for:

* Plan for a data hub from day one.Whether it’s Salesforce, HubSpot, or something else, decide early where your agents’ outputs will live and share context. Don’t retrofit this.
* Every agent takes 30 days to train.We reviewed the first 1,000 outputs of every agent manually. Every single one. The ones that “don’t work” are the ones nobody trained. Budget for this.
* The value of Salesforce isn’t Salesforce—it’s the shared data layer.We’re not using 80% of Salesforce’s features. We’re using it as a reliable, integration-rich data store that all our agents can read from and write to. That’s what we’re paying for now.
* Inbound is still the easiest win.There is no excuse today for prospects not getting instant answers. If someone visits your site and wants to know if they’re a fit for your product, an AI should tell them in real-time—not route them to a discovery call that happens three days later.
* The agents are only as smart as your data.Garbage in, garbage out. The irony of going AI-first is that it made us more disciplined about data hygiene than we ever were as a human team. Because the agents depend on it.

## Salesforce Matters More To Us Now Literally Than Ever.  The Age of AI Agents Has Re-Anchored it For Us

Ten months ago, Salesforce felt like legacy software we hadn’t gotten around to cutting.

Today, it’s the nervous system of our entire operation. Every agent connects to it. Every signal flows through it. Every decision gets logged in it.

The technology changed. But it was our deployment of AI agents that made us finally use our CRM the way it was always meant to be used.

#### If you’re building an AI-first B2B operation in 2026+, don’t underinvest in the hub. Your agents need somewhere to live.

### And Come Meet ALL of Them AtSaaStr AI 2026 (May 12-14)!  Agentforce, Artisan, Monaco, Qualified, Momentum, Attentive, Aurasell, Vivun, People.ai, Larridin and so many more AI GTM Agents and Leaders!!

May 12-14 in SF Bay!!