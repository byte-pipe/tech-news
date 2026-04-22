---
title: Agentic coordination, Human delivery - Dont Dos
url: https://dontdos.substack.com/p/what-if-the-robots-came-for-the-org
site_name: tldr
content_file: tldr-agentic-coordination-human-delivery-dont-dos
fetched_at: '2026-04-23T09:44:33.394011'
original_url: https://dontdos.substack.com/p/what-if-the-robots-came-for-the-org
author: Dont Dos
date: '2026-04-23'
description: Posted anonymously by a CTO who'd rather not turn a difficult year into a marketing exercise. About nine minutes, if you read at a civilised pace.
tags:
- tldr
---

# Agentic coordination, Human delivery

### Posted anonymously by a CTO who'd rather not turn a difficult year into a marketing exercise. About nine minutes, if you read at a civilised pace.

Dont Dos
Apr 17, 2026
7
1
Share

### TL;DR

* We’re a profitable B2B SaaS outfit. I’m not going to name us as this isn’t an ad, and I have no intention of joining the growing club of founders who have turned a round of layoffs into a personal brand. The people I’m about to describe deserve better than being a line in somebody else’s LinkedIn victory lap. Including mine.
* The coordination work that used to sit in the middle of our org (meeting minutes, roadmap drafting, prioritization, acceptance criteria, release readiness..) is now handled by a small crew of agents running on LangGraph, with Claude Sonnet and Opus doing the thinking and Notion playing the part of the shared brain.
* This turned out to be the single most underpriced trade in the AI industry: coordination work is cheap to automate, because the worst-case output is an awkward paragraph in a Notion doc rather than a smoking crater where your API used to be (not to mention token usage).
* The hard problems (performance reviews, career growth, two people who cannot be in the same room) still want humans. For now.

### I.

The first time I clocked that something was properly wrong, I was reading our quarterly engineering survey in a coffee shop in Lisbon. One of our backend engineers, a man I’d trust to hold my wallet and my laptop at the same time, had written, in the free text field:“I found out about the Acme deal from a customer on a support call.”

Acme was a seven-figure contract. It had been the headline topic of a leadership offsite two months earlier. The engineer in question was about to spend the better part of his next quarter building the thing Acme had signed for. And he heard about it from the customer.

I read it twice. Closed the laptop. Paid for my coffee. Went for a walk.

### II.

Here is the shape of the company: about forty people; observability software for a particular flavour of infrastructure I am not going to describe in any detail, because I would rather this post be useful than googleable; six years old; profitable, which in this market apparently qualifies as breaking news.

Three of us at the top. Roughly twenty people on the making side: engineers, designers, a handful of QA and support. And, as of last summer, nine people sitting in the space between us and them. Product managers, one of whom doubled as a product owner for the platform squad. Engineering managers. A design lead. A QA lead.

Every one of those nine had been hired on a specific Tuesday to solve a specific problem that existed on that specific Tuesday. Every one of them was, individually, a good call. And for roughly eighteen months, they did exactly what good middle-of-the-company people do: they absorbed chaos from above, dispatched clarity below, and made everybody’s Monday morning marginally less feral.

### III.

Then I read that survey in Lisbon and I started paying attention to what was actually happening between the top floor and the shop floor.

I’d say something in a Monday leadership meeting. A PM would hear it and repeat it, correctly, in planning on Wednesday. An engineering manager would hear the PM and repeat it, correctly, in standup on Thursday. A senior engineer would hear the EM and write a ticket. By the time the ticket got picked up, the thing being built was not the thing I’d said on Monday. Not the opposite. Just a little bit duller. A little bit safer. A little bit morereasonable. Every handoff a person, in good faith, trying to make what they’d heard make sense inside their own head. Every handoff a small, well-meaning, lossy compression.

We had rather a lot of handoffs. A sort of corporate Chinese whispers, only with quarterly bonuses.

Meanwhile, my engineers were finding out about seven-figure deals from support tickets.

That was the diagnosis: not that anyone was doing their job badly, but that the geometry of a forty-person company with people in its middle produces, as a matter of physics, a version of the strategy that reaches the engineers ten days late and two degrees off axis. And physics, unlike people, does not respond to a firm word over coffee.

### IV.

The thing that unlocked it, the thing that stopped me lying awake wondering whether I’d gone round the bend, was a small and rather obvious observation about failure modes.

The worst thing a bad coordinator can do is produce a misaligned team. The worst thing a bad engineer can do is put a bug into production. One of those you sort out on Tuesday morning with a slice of cake and a good-humoured apology. The other ends up on the front page of Hacker News, and possibly in a solicitor’s letter. These are not the same category of risk. We had been treating them as though they were.

We had been quietly assuming, without ever saying it aloud, that letting a model near our company required the same paranoid choreography as letting a model near our production systems. But the model wasn’t going to ship anything. The model was going to write a briefing. A human was going to read the briefing. A human was going to decide whether to act on it. A human was going to write the code, merge the code, own the code. The worst-case output of a badly behaved agent, in the system I was starting to sketch, was an awkward paragraph in a Notion doc, the sort of problem a civilised man can live with.

Once I’d seen it, I couldn’t unsee it. The entire AI industry had spent two years staring, very hard, at the wrong question. Everybody wanted to know how to let agents write code, which — and I want to be precise here, because most of the discourse isn’t, also forgive the em dashes — is not actually the hard part. Drafting code is something current models do perfectly well on a Tuesday afternoon. The hard part, the part that needs the paranoid choreography and the retry loops and the committee of reviewer agents, isshipping code to production and taking ownership of it when it breaks at three in the morning. That is a different animal entirely. That is the part where the cost of a mistake is a real bug in a real system that a real customer is paying real money for, and where somebody’s name has to be on the merge, and where that somebody has to be in a position to be woken up about it. Nobody has worked out how to put an agent on a pager rota, and I suspect nobody will for some time.

Meanwhile, the people in my company who were most expensive per head were spending their days writing meeting minutes, drafting acceptance criteria, rewriting Jira tickets, arguing about the priorities. Work where a mistake costs you an afternoon of mild annoyance, where nobody gets woken up, and where nobody’s job is to carry a pager. Work that current models are, frankly, embarrassingly good at. Work you can run for roughly the price of a pint.

Coordination is cheap to automate. Shipping code and owning it in production is expensive to automate. This, I think, is the single distinction I would most want another founder to carry away from this post, so I am going to repeat it and then continue.

Coordination is cheap to automate. Shipping and owning production is expensive to automate.

Right. Onwards.

### V.

I spent a couple of months last year finding out whether the models were actually up to it. Built a prototype at weekends. It was ugly, it lived in a Docker container on my personal laptop, and it did precisely one thing: read the transcripts of our Monday leadership meetings and produce a weekly briefing fit to put in front of an engineer.

The first briefings were rubbish. The fourth was better than what our PMs were writing. I showed it to my co-founder. His reaction cannot be reprinted in a respectable blog post, but I took it as encouragement.

We spent another month turning the prototype into something real, and over the course of the summer the shape of the middle of our company changed. Six of the nine roles in that layer moved on to other things (some to other companies, one into a senior engineering seat here, one into a customer-facing role that badly wanted him). Three stayed: one EM, who now runs the human side of engineering full-time; one senior PM, who owns the customer-facing parts of product strategy; and the design lead, because designing things is not a coordination problem. The three of them are, without exaggeration, doing the most rewarding work of their careers, because the tedium has been stripped out from underneath them.

I will not pretend this was painless, but the headline is not really about the people who left. The headline is that we discovered, by accident, that a forty-person company does not need lots of people in its middle. It needs few, and a small set of draft-writing machines, and a great deal more honesty flowing up and down the vertical.

### VI.

Here is what a week looks like now.

Monday morning, the three of us at the top have our strategy meeting. We quarrel about customer signal and sales pipeline and what we want to lean on this quarter. The meeting is recorded.

Separately (and of all the moving parts, this is the one doing the most work) every sales call and every customer success call from the previous week has also been recorded and transcribed. The raw conversations, unfiltered, with the customers’ own words still warm in them, are sitting in a bucket by Sunday night. Nobody has to write a summary. Nobody has to remember to file anything. The customer is already in the building.

A first agent, which I privately call thestenographerthough the code calls it something more dignified, reads the lot. Monday’s meeting, the sales calls, the CS calls, any async notes we dropped into a dedicated Notion space during the week. It writes a weekly briefing into Notion. Same shape every time: what customers are asking for, what sales is seeing in the pipeline, what’s slipping, what leadership said it wanted, and where those four things are quietly at war with each other. Everybody in the company can read it. Plenty of them do. It was a small change, and the quietest thing we did, and it turned out to matter most, because for the first time since we were fifteen people, our engineers can read what our customers actually said last week, in the customer’s own words, with nobody in the middle doing the translating.

A second agent reads the briefing, reads the current roadmap, reads the actual measured velocity of our squads over the last few sprints, and writes a proposal.Given what the customers said last week, and given what the squads are really shipping, here is what the roadmap probably ought to look like instead. Here are the tradeoffs. Here is what you’d be giving up.We read it Tuesday morning over coffee, quarrel about it for half an hour, and decide. Once we’ve decided, a third agent walks the changes into Jira. Epics created, closed, reshuffled, each one carrying a link back to the exact paragraph in the briefing that justified it. A chain of attribution from every line in every ticket back to a sentence somebody said in a meeting.

A fourth agent walks the new epics. Proposes dates, drafts acceptance criteria, breaks epics into candidate stories. A fifth agent watches every merged PR and every epic in flight and keeps a living list of what wants testing before we cut a release. Two human QA engineers work through that list and decide what ships. The agent does not. It never has. A handful of senior engineers keep a loose eye on the agent outputs — perhaps two hours a week between them, which may be the cheapest insurance policy ever sold in western Europe.

And then the fourth agent hands its story breakdowns to the engineers. The scoping sessions are run by humans, for humans. The agent’s proposal is the opening move, not the final word. I say the same thing at every one of these sessions: your job in this room is to push back. If the estimate is wrong, say so. If the acceptance criteria miss a case, say so. If the approach is daft, say so. Use whatever AI tools you fancy to think through the complexity (I could not possibly care less) but the estimate on the ticket is yours, and your name is on the date. There is no PM to blame when it slips. There is no EM to play peacekeeper. There is you, your team, and the work.

### VII.

The effect I did not see coming, and which in the end matters more than the money, is this: when the agent drafts and the humans argue, the humans end up understanding the workbetter, not worse.

Last month one of our engineers (call her Priya) spent forty minutes in a scoping session insisting that the agent’s three-day estimate on a migration ticket was complete fiction, because it hadn’t accounted for a legacy auth path nobody had bothered to document and the agent had no earthly way of knowing about. She rewrote the estimate at eight days, acceptance criteria to match. Six weeks later, when that ticket hit a snag nobody had predicted, Priya walked into the room already knowing every assumption baked into it, for the simple reason that she was the one who had baked them in.

The Priya of a year ago would have been handed the same ticket by a PM, nodded politely, and forgotten it existed until the sprint started. The agent produces a draft. The humans produce theunderstanding. That is the precise opposite of what a more automated company is supposed to feel like, and it is the single thing another founder ought to believe before trying any of this.

One of our engineers (the same man from the Lisbon survey) told me in a 1:1 recently that it was the first time in eighteen months he’d understood why we were building what we were building. I did not know what to say to that, so I said thank you, and changed the subject.

### VIII. The stack, briefly

For those of a more mechanical disposition.

The backbone is LangGraph running as a small Python service. I wanted the state transitions explicit rather than emergent out of a chatty multi-agent loop — I’ve seen what happens when you let agents hold a committee meeting, and it is not a thing one bills a customer for. Claude Sonnet 4.6 for most nodes. Opus 4.6 for the weekly roadmap proposal, where I am happy to pay for the extra reasoning once a week. Long-lived context in Postgres with pgvector. The knowledge base is just Notion, reindexed into the vector store every night.

Each agent is defined as a set of skills. A skill is a folder containing a prompt, a description of when to use it, a few worked examples from our own history, and a list of tools that skill is allowed to touch. It is the single most important design decision we made, because it means non-engineers (including our CEO) can change how an agent behaves by editing a markdown file. She has done so several times. It felt deeply strange at first.

We leaned on what already exists for tool access: Atlassian’s first-party Jira integration, the Notion API, the GitHub API. We built precisely one small internal service, exposing our analytics warehouse as a read-only query tool, because nobody else was going to wrap our data for us. Transcription is Fireflies, dumping structured JSON into S3. Observability is Langfuse. The whole operation runs as four containers on the same ECS cluster that runs our product. Roughly four thousand lines of Python, most of which is prompt scaffolding and skill definitions rather than orchestration logic. Two engineers could have built it in a quarter. One engineer built the prototype at weekends. When I look at the Langfuse dashboard I still feel vaguely as though I am getting away with something. The entire apparatus costs less per month in tokens than one senior engineer costs per week.

### IX.

A few more things.

The agents are more objective about strategy than we were, which surprised me and really shouldn’t have. A human sitting in the middle of an org has career incentives and political preferences and pet projects and a soft spot for the one engineer they’d quite like to protect from a painful ticket. A model has none of these charming encumbrances. When theroadmapagentrecommends killing a feature, it has no memory of whose clever idea the feature was six months ago, and no particular interest in being invited to the leaver’s drinks.

Our mistakes, mercifully, have all been survivable. Once, the roadmap agent proposed deprioritising a compliance feature because it wasn’t generating customer excitement in the briefings. The reason it wasn’t generating excitement was that compliance features don’t generate excitement, they generate renewals. And the agent had not yet learnt the difference. A senior engineer caught it before Tuesday. We updated the skill with a note on how to think about compliance work. Cost us an afternoon.

The hard problems are still the human ones. Performance reviews. Career conversations. Two people who cannot work together. A designer who is quietly miserable. Our surviving EM handles those, there is no plan to automate them, and there may never be. That will be its own post.

### X.

The coordination work inside a software company has always been a kind of tax: the cost of getting a group of clever people to point, more or less, in the same direction. That tax is collapsing now, and what it reveals underneath is the part of the work that was always supposed to be the point: engineers building things, designers shaping them, QA making sure they’re real, leadership deciding what to bet the company on. Everybody still on the payroll, including the three who used to sit in the middle, is doing more of the work they came here to do and less of the work that was about keeping the machine running.

There is a version of this story where the moral isthe middle of the company is dead. That is not the moral. The moral is that a forty-person company does not need a middle that looks like a hundred-and-forty-person company, and that we had quietly been running the wrong shape for about eighteen months before anybody noticed. The people who used to hold the middle together were not wrong to have held it together. The shape was wrong. The shape is changing now, for us and — one more em dash — for every company built after ours.

I shall let you know what I learn next.

Next in this series: how the Notion knowledge base is actually structured, and why it, not the agents, is the real unlock. And a harder post about what happens to performance reviews when most of the coordination work has moved into software.

7
1
Share