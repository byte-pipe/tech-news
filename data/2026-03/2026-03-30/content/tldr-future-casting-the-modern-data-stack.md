---
title: Future Casting the Modern Data Stack
url: https://motherduck.com/blog/future-casting-the-modern-data-stack
site_name: tldr
content_file: tldr-future-casting-the-modern-data-stack
fetched_at: '2026-03-30T11:26:04.455073'
original_url: https://motherduck.com/blog/future-casting-the-modern-data-stack
author: MotherDuck
date: '2026-03-30'
published_date: '2026-03-23T19:35:25.892Z'
description: If the Modern Data Stack isn't yet dead, it's at least incredibly sleepy. AI is bringing the "long run" closer than ever — here's what might come next for ETL, BI, data warehouses, and the role of data engineers.
tags:
- tldr
---

GO BACK TO
BLOG

# Future Casting the Modern Data Stack

2026/03/23-20min read

BY
Jordan Tigani

“In the long run, we’re all dead” – John Maynard Keynes (dead person)

After writing an article a few years ago called “Big Data is Dead,” it feels a bit clichéd to call things “dead.” So I won’t say any such thing about the Modern Data Stack. It does, however, appear very, very sleepy. Someone should go and poke it with a stick.

The Modern Data Stack - deceased or just drowsy?

While we’re all dead in the long run, one thing that is different now is that AI is bringing the “long run” a lot closer than it has ever been. In the last couple of years, AI has forever changed a number of professions that were once thought to be safe from disruption. From art to software engineering, AI is changing how people get things done, and changing things much faster than you’d expect.

Those of us on the data side of things somewhat smugly looked on and said, “AI isn’t going to impact me, because of [reasons].” I was one of those people. There is too much context in people’s heads! SQL is going to be harder for LLMs to write! No one is going to trust the output of an LLM in their decision making! It turns out that these were just short run thinking.

How quickly things change. As Joe Reis pointed out in his recentpost, “the reckoning is already here.” Once you have an existence proof, it is hard to hang onto your rationales that such a thing is impossible. It has only been roughly 3 months since Anthropic’s 4.5 models came out, and that has already changed the way many data people do their jobs.

It has also brought tons of new folks into the fold, people who had wanted to get insights from data but used to be stuck waiting for others to prepare their dashboards. Now they can figure things out on their own.

The interesting question to me is, “What comes next?” If we assume models continue to get better, companies capitalize on the opportunities, things get tied together in a nice bow, what does the world look like? What could it look like? Let’s start with what we know.

## The Immovable Objects

“I very frequently get the question: 'What's going to change in the next 10 years?'... I almost never get the question: 'What's not going to change in the next 10 years?' And I submit to you that that second question is actually the more important of the two.” – Jeff Bezos

When trying to understand the future, it is often more useful to figure out what isn’t going to change than what is. That is, if you focus on things that are in flux, it can be very hard to predict where they’re going to land. However, if there is something that is true today and will be true in 10 years, whatever new equilibrium we end up with will have to accommodate that fact.

What are some things that we know won’t change?

The end goal of data is insight.This may sound obvious, but it is worth starting with as an anchor: The reason that data has value is because it is needed to help people gain insight and make decisions. The types of data might change, the types of people who are able to interact with their data might change, and the sources of data might change. But people will still have a need to answer questions that can only be found in the data. Absent the robots taking over or other apocalyptic scenarios, it is hard to imagine a future in which that isn’t true.

Data is always changing, and its value decays over time.If we just cared about static data sets, the job of a data engineer would be easy. The vast majority of the complexity of data systems is dealing with change. Schemas change, values of data change, new sources arrive, new metrics need to be created, new features need to be tracked, bugs exist, companies merge, tools get migrated. In order to get the value out of data, you need to be able to handle all of the ways that it changes.

Context is Critical.In order to efficiently get from stored data to higher-level concepts, you need some sort of map. That map might contain the definitions of metrics for the organizations (e.g., “this is how we calculate ARR”) or specific semantic information (“the customer_id field is a UUID and to get a name you need to join with the organizations table on the org_id field”). Because this context is organization-specific, this information will not be something that the LLM can infer.

Analytics is computationally intensive.Unlike a lot of other infrastructure tools, an analytical query engine like a data warehouse benefits from increased resources. If you throw more memory and more CPU, and more network bandwidth at the problem, you can get the answer faster. While engines are getting faster all the time, if you want to get answers from your data, you need to pay a computational tax either on the preparation side or at query time.

## The Inexorable Forces

“This is the Worst LLMs are ever going to be.” – Ethan Mollick

The next piece of the puzzle is figuring out the forces afoot that are going to drive changes to the status quo. These are important to understand because they are things that can enable us to make high quality predictions.

The cost of building is going to zero.Anything that can be vibe-coded will be vibe-coded. The delta to being able to describe what you want and getting what you want will continually be reduced. LLMs are already very good at coding and writing SQL, and will continue to get much better. However, infrastructure is and will be the most resistant to vibe-coding.

Fight the LLMs at your peril.Each generation of LLMs has made entire classes of businesses unnecessary. You can think of them like a tidal wave. You can’t outrun them, you can’t swim through them. If you are very, very good you cansurf them, and they’ll take you very far very fast. But you’d best not fall.

Consolidation is good for customers.The un-bundling of the modern data stack created a flourishing of innovation, but once that settled down, customers want predictability, and each new vendor they have to work with is a tax. There has been a trend towards consolidation in the last year or two, but AI is going to accelerate this by blurring some of the traditional lines between the swim lanes of the MDS ecosystem.

Feedback Loops.One of the most powerful forces in nature is the feedback loop. This is, after all, what is behind both natural selection as well as LLM training and reinforcement learning. The best data solutions will be the ones that can incorporate feedback loops so they continue to get better as LLMs get better. Positive feedback loops help accelerate change, negative feedback loops help create a stable equilibrium.

## The State of the World at Time Zero

“We were somewhere around Barstow on the edge of the desert when the drugs began to take hold.” – Hunter S Thompson

To figure out where you can go, you need to know where you are. Here are some things that are happening right now with LLMs and the modern data stack that can be useful to understand before making predictions.

LLMs are writing SQL.LLMs are already very good at writing SQL and will continue to get much better. Pre-November of 2025, this might not have been the case, but these days, if you give one of the latest models a question that can be answered by the data, there is a very good chance it will be able to write high-quality SQL to get you the result you were looking for.

LLMs aren’t picky about formats.LLMs are good at understanding things that they have seen a lot of in their training sets, but generally aren’t sticklers about formats. While a lot of energy has been invested into creating highly structured context layers, LLMs don’t really care about the structure, as long as the format is comprehensible. Moreover, as LLMs are getting better at keeping more context, this is likely going to continue into the future.

LLMs can draw.LLMs are very good at data visualizations. From a simple prompt, they can already build a nicer looking chart than virtually any BI tool. They can add custom themes, and make other API calls. While there is more to BI than dashboards and reports, it is hard to see the current wave of BI tools surviving in their current form.

ETL is highly vibe-codeable.Extract-Transform-Load or Extract-Load-Transform pipelines generally contain fairly straightforward code that will be easy for an LLM to generate. There are good open source connectors, and even if they were not, LLMs can consume documentation for an API and build a connector fairly easily.  The transformations themselves are typically relatively straightforward, and can usually be specified in SQL. The ingestion and transformation side of the modern data stack would also seem ripe for disruption.

Open Data Formats are taking over.The trend towards storing data in engine-agnostic formats like Iceberg, Delta, and DuckLake is going to accelerate in a world where AI is driving a lot of the analytics. This is because you’ll have more tools that need to read and write the data, and locking it up in a data warehouse doesn’t make sense.

Computers can ask more questions faster than humans.Humans are typically limited by how fast they can write SQL or how quickly they can come up with new questions, whereas a computer, or an agent, can fire off a lot more queries in a short period of time. An agent will be faster at writing the SQL, but will also likely be able to try a lot more different ideas because the “cost” of writing a query and executing it will be small.

## What Does the Future Hold?

“Computers in the future may weigh no more than 1.5 tons.” – Popular Mechanics

Now that we’re properly oriented, let’s take the change drivers above and iterate them out a bit. What are some predictions we can make about the future?

Humans will write only a very small percentage of SQL.Unlike say, C++, where there is an art and craft to proper software design (the right layers of abstraction, modularity, naming, dependency management), SQL is typically more utilitarian: Does this answer the question I’m trying to pose? As such, hand-written SQL is likely going to plummet and become very niche.

If I were to look at the amount of hand-written SQL vs AI-written SQL amongst employees at MotherDuck over the past few months since we released the MCP server, the usage of the web ui to write queries has plummeted, while the amount of AI-written SQL has increased. At the same time, the amount of usage of our BI tool has also decreased significantly. Even our head of finance is using AI-generated analytics for budgeting purposes.

Context is at the heart of the new data stack.If humans aren’t writing SQL, context becomes very important. That is, if you asked your human analyst to compute your ARR over the last two quarters, they’d have a bunch of context in their heads such as where are the relevant fields in the relevant tables, which fields in which tables are joinable, what you mean by ARR, and what your fiscal quarters are.

Natural languages like English (or Portuguese, or Urdu) will be as good or better to provide context than any of the structured metrics layer languages like MetricsFlow, Cube, LookML, or Malloy. One reason is that there is a bootstrapping problem; there aren’t enough of these languages in the training sets for the LLMs to really know how to read and write these super well. On the other hand, there is a ton of natural language in the training corpus.

Furthermore, to an LLM, a simple natural language statement saying that two fields are joinable is just as comprehensible as the same thing in a structured language. And from the perspective of maintenance, English is going to be easier for human reviewers to both ensure that the information correct and inject their own rules on the system.

In the process of answering questions, LLMs find out a lot of information. They try a join and realize that it doesn’t work. They look at a table that seems promising but doesn’t have any data more recent than December 2024. They will  probe a table and realize that the region codes are all three-letter airport codes. However, without a context layer, they have to figure the same thing out every time, which is highly inefficient, as well as error prone.

This is where the feedback loops come in. Even though humans are not great at keeping documentation up to date, an LLM should be able to write the vast majority of the context layer documentation. On the ingestion side, LLMs know where data came from and can trace lineage on their own. On the query side, they glean information by trying things and also through prompts. The LLM can take whatever it learns and commit it back to the context. Some care needs to be taken to ensure that it doesn’t get polluted with false finding, but that is relatively straightforward.

The context feedback loop: each query makes the next one smarter.

For the past few months, I have been using Claude + an MCP server that talks to our MotherDuck data warehouse instead of writing SQL. I recently asked Claude to use my chat history to generate a markdown doc describing the metrics we used internally, as well as information about the tables and fields we have. The resulting doc was quite comprehensive and high quality. To me, this was evidence that LLMs will not need explicit human-generated context.

Data Modeling will be even more important.If you want the query side agents to work well, the data model needs to be clean and understandable. If there are a bunch of vestigial tables with broken data that is infrequently updated, that’s going to confound your favorite LLM. Of course, a good context model can point the way, but if there aren’t clean abstractions, the job is way harder, and the chances of a hallucination go way up.

In an era where computers can do everything, creating a clean abstraction boundary is going to enable them to do things better. Data sources tend to be set up for transactional workloads instead of analytics. They change their schema without worrying about all the downstream effects, or end up losing history by changing data in place. Data warehousing techniques like star and snowflake schemas or even “one-big-table” are still going to be useful.

It is likely, however, that computers are going to be able to help generate these models. While data-engineers are likely going to be the best architects of a good data model, they will likely do so with LLM-driven assistance. An LLM can suggest a star schema and build the pipeline to match.

The job of a data engineer will be to manage change (and agents).The most underrated task of a data engineer is dealing with change. If you can vibe-code a data pipeline, that’s great, but what happens when a data type changes? What about when new data sources arrive? When one of your sources gets blocked? When a field starts getting filled with nulls?

Agents will almost certainly help out here, but humans are going to need to provide judgment and keep things moving smoothly. Just like the job of a software engineer is likely going to change to be a conductor for an orchestra of agents, a data engineer is also likely going to have their own fleet of agents to coordinate.

Most likely, this will mean that a data engineer will need to take on more responsibility for a broader cross-section of tools. They’ll need to make sure the context is up to date, the data sources are flowing smoothly, and they have alerts that can help them know when something has changed or is wrong.

A significant part of data engineering will be writing evals that are like unit tests for the data. These will be constraints for the LLM-generated code and pipelines, and can help test when something has gone wrong. They can test for logical impossibilities, validate internal assumptions, and accumulate wisdom over time.

We’re likely to see a Text-to-SQL scandal in 2026, but it won’t slow down adoption.First we said, “No one will trust vibe-coded analytics to make a business decision.” Then it was that they wouldn't trust it to put in their board slides. Then it was they wouldn’t trust it to put in their SEC filings. But, they will anyway. It is too easy to use, and it is mostly always mostly right unless it is subtly or horribly wrong. Someone is going to trust it a little bit too much and get something important embarrassingly wrong. But that’s ok, by the time the next model comes out it will be all forgotten.

## The Tolling of the Bells for the Modern Data Stack

“Hadoop seems to have solidified its position as the cornerstone of the entire ecosystem.” – Matt Turck, 2014

If we take these priors and iterate them out a bit, what do we think is going to happen to the good ol’ modern data stack?

The MDS circa 2023 - how times have changed.

Vibe-Coded ETL Pipelines are coming, but will take off more slowly than people expect.On one hand, Claude Code can build you a data pipeline that will read from hubspot, transform the schema to something sane, and write it to snowflake every 10 minutes. So from that perspective, it seems like it would spell doom and gloom for the ingestion, orchestration, and transformation pillars of the modern data stack.

Not so fast, however. Even if you can vibe-code your way to a working data pipeline, the hard part, as always, is change management. What happens when a new field shows up? Or a schema changes? Or there was a bug somewhere and you need to backfill? Oh and by the way, you don’t want to break any existing dashboards.

One of the ways that we’ll be able to deal with change is to add agents to the mix. Agents will monitor data for changes and be able to react to changes automatically. This will allow some problems to be corrected automatically, and others to notify a human engineer and provide them context.

BI Vendors will need to adapt or become irrelevant.Much of what BI tools currently do will be replaced with custom visualizations. Claude et al are already very good at building visualizations, and they will continue to get even better. With a brief prompt, you can make interactive dashboards, add themes, and even use other APIs turning them into full-blown apps.

One way that BI tools can stay relevant is to leverage their semantic models for context for AI. After all, if someone has spent a lot of energy encoding their data model into LookML, that information is going to allow an LLM to write better queries.

Data Warehouse vendors will survive but be commoditized.Infrastructure is more resistant to AI than a lot of other software. AI tends to use infrastructure vs try to rebuild it. I am a founder of a data warehouse company, so of course I think that of all the categories in the modern data stack we’re in the best shape.

Analytics is very resource intensive, and is a CPU, memory, and network hog. It can go from zero to using pretty much all of the resources you throw at it in a very short amount of time. Agents will typically run in a resource-constrained environment; most of the jobs that they do don’t need a lot of memory or CPU. These two things taken together mean that in order to do analytics, agents will want to call out to a service somewhere.

Of course, in the distant future even the query engine may be vibe-codeable. Researchers haveshownthat you can get order of magnitude improvements to query speeds by basically hard-coding the data model into the database. Right now it is pretty impractical, but if LLMs get much better, part of the data pipeline may be generating a custom query engine.

The data gravity that data warehouse vendors once had, and their stickiness, is already starting to erode and will do so further. AI will accelerate the trend towards moving data from the data warehouse-managed storage to open data formats. This will give agents the ability to interact with the data directly.

Data warehouse vendors will also need to adapt in order to stay relevant. How do you work well with agents? How do you store and provide access to context? Cost and ease of use will be important, and the large margins seen by the industry will likely be eroded.

The swim-lanes of the Modern Data Stack will be generally abolished.If you can vibe-code a data connector, orchestration, and the data transformation pipeline, is there a reason those all need to come from different vendors? This is likely going to turn into a free-for-all. The larger players like Fivetran+dbt, Snowflake, and Databricks will have a distribution advantage. Smaller startups will have a nimbleness advantage.

When it all shakes out, my bet is that there ends up being one form factor that people settle on. It will consist of an agent swarm for data management backed by a query engine for doing the actual analytics. Agents can handle change and adapt the system in real time. They can prepare insights directly for users.

To provide an existence proof, this is basically what OpenAI’sdataagent does, so I’m not exactly going out on a limb with this prediction.

## Conclusion

“You’re still here? It’s over. Go home!” – Ferris Bueller

A couple of years ago I talked to a founder and asked him what AI was going to do to his business. He said that previously, he felt like he could see a long road stretching out in front of him and he could see exactly what he was going to encounter far ahead to the horizon. But with AI, it was like a fog bank had rolled in; you can’t really see further than a few feet in front of your nose.

What makes it worse is that the AI world is moving so fast that if you slow down to wait and see how things work out you get lapped. So you pick a path and aim for it, but you have to be ready to turn super quickly if you realize you’re running off the road.

Writing these predictions have been helpful to me in figuring out exactly what I think; hopefully they’re interesting or useful to you. If they are, please share your feedback.

Start using MotherDuck now!

Try 7 Days Free
Get Started

## Subscribe to motherduck blog

Subscribe to other MotherDuck Updates
Submit

## PREVIOUS POSTS

2026/03/13 - Simon Späti

### DuckDB Ecosystem Newsletter – March 2026

SQL Transpilers, VS Code Extensions, Dives and more

2026/03/19 - Garrett O'Brien

### Claudeception: Inside the Mind of an Analytics Agent

More tool calls, more schema exploration, more verification — does it help, or hurt? We dug into the chain-of-thought traces behind one of the hardest text-to-SQL benchmarks to understand how analytics agents actually think.

View all
