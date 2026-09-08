---
title: A decade of software infrastructure | Innovation Endeavors
url: https://www.innovationendeavors.com/insights/a-decade-of-software-infrastructure
site_name: tldr
content_file: tldr-a-decade-of-software-infrastructure-innovation-end
fetched_at: '2026-09-08T21:34:53.000419'
original_url: https://www.innovationendeavors.com/insights/a-decade-of-software-infrastructure
date: '2026-09-08'
description: Today, we are excited to announce Kenneth Auchenberg is joining the team at Innovation Endeavors. You can read more about him joining here. Kenneth joining is r...
tags:
- tldr
---

Skip to content

Today, we are excited to announceKenneth Auchenbergis joining the team at Innovation Endeavors. You can read more about him joininghere.

Kenneth joining is representative of a broader strategic focus for us - doubling down on our work in software infrastructure.

The cloud infrastructure and developer tooling market is massive, and has been a core focus of ours historically - working with companies likeKong,Extend, andInception. Yet, we can’t help but feel that this was just the beginning. The next decade will be, by far, the most exciting timeeverto be investing in infrastructure, as AI is turning everything into infrastructure.

We wanted to use this moment to outline the six prevailing megatrends that make us so excited about infrastructure right now, and which we think will combine to make this a decade of software infrastructure.‍

### 1. AI coding will reinvent the software development lifecycle, and thereby reinvent software organizations

Coding agents have fundamentally altered almost all assumptions about how we develop software. The IDE is becoming irrelevant, the outer developer loop is collapsing into the inner dev loop, specification & testing is becoming more important than writing code, code review is becoming the new bottleneck, and this is just the beginning.

The amount of change occurring in software engineering is difficult to fathom, and it is increasingly clear that it will have massive downstream implications. Essentially every tool in the modern software development lifecycle - from code storage to feature flagging to observability - is designed around the assumption that a human is the author, a human is the reviewer, and the velocity of development is 1000x less than what it is now.

This can’t last, and so we expect the entire SDLC, and every tool within it, to be rebuilt from scratch. The next GitHub, the next Harness, the next Datadog will not look like the current ones.

This will also greatly impact organizational structures. When everyone can code, the lines between product, engineering, and design blur. New roles will emerge, and the way we structure organizations will change. This creates an immense opportunity to also reconsider the tooling that has served the product software development organization - from issue tracking to product analytics to collaborative development layers.‍

### 2. All infrastructure will be re-architected for agents

Agent workload patterns are nothing like human ones, and none of our existing computer science systems (e.g. databases, compilers, distributed systems) were designed around them being the primary users.

For example, beyond the factGithub can barely stay up as commits grow >14x YoY, a large number of vibe coding startups can’t even use Github because they produce new repos at such an inhuman rate that they constantly run into Github’s rate limits. The workload changed - coding agents produce a ton of very small repos, not a few large ones - which necessitates an architectural redesign of the system.

This same thing is playing out in almost all infrastructure categories. Replit used Neon because a new Postgres architecture with separation of storage and compute was the only thing that made Postgres economically amenable to vibe coding. Web search APIs for agents likeParallelhave to design their search stack totally differently from Google because humans write a small number of brief web search queries, whereas agents write hundreds of parallel, extremely highly specified web search queries.

Agent workloads are bursty, highly parallel, much more iterative, and often subject to very different cost and latency constraints. Agents tend to do a lot of small work, not a little bit of large work. These factors are leading to a whole new set of design considerations for systems - such as greatly increasing the need for copy-on-write branching and high fidelity snapshotting.

Every infrastructure category - databases, search, browsers, queues, vector stores, observability - will thus need to be redesigned when considering agents as the primary user.‍

### 3. All agents are becoming coding agents

Software engineering is becoming the most ubiquitous tool for agents. You would be hard pressed to find a vertical agent today that is not at least partially using code generation for function calling, context management, or artifact generation.

Software is the most universal and general interface for getting work done in the world, so the agents doing the work will write code to do it. Most of that code will be ephemeral - written for one task, executed once, and thrown away - and none of that code will ever be seen by a human. And this scale of this code generation will literally be billions of times more code than what is written today.

This will lead to the creation of a new SDLC that rhymes with the traditional one, but which is also fundamentally different. What do testing, CICD, code review, observability, and more look like for code written by agents dynamically with no human intervention?

This will expand the market for developer tools from “all software engineers” to “all applications”.‍

### 4. APIs + on-demand generated UI will replace apps

Most of the world will move toward using an AI interface to dynamically execute third party tools and services. Software and UIs, in the traditional sense, will start to disappear. What remains will be infra-first versions of what used to be SaaS apps -engines and kernelswith on-demand hyper-personalized generated UIs rather than applications.

We think there will be more infrastructure companies than SaaS app companies in the next decade, which is a wild thing to say, but it follows directly from where the interface is going.

This is an inversion of the classic relationship we have seen in software, where there were a lot of vertical SaaS apps and a relatively small number of consolidated infrastructure vendors. AI copilots will aggregate the interface, but as a result infrastructure companies will flourish - the application layer bundles, the backend unbundles.

This represents a monumental shift in how we even think about what it means to build an application. What is a design system in this world? Should APIs still offer some kind of visual guidance to AI tools consuming them? And how will the millions of companies built around workflow UIs adapt to this world?

We suspect that in almost all SaaS categories, you will see a headless, API-first version of the product emerge and become a massive business.

### 5. Agents will alter the distribution rails for infrastructure

Infrastructure choices are increasingly made by coding models, not humans. Many of the startups we work with generate >40% of their leads as a result of coding models recommending them to software engineers trying to build something. This represents a profoundly new distribution & adoption mechanism for infrastructure.

The first implication of this is that there is a substantial opportunity to build infrastructure businesses that are optimized for Agent Experience, not Developer Experience. We suspect that some infrastructure startups will win almostentirelyon the basis of optimizing their go-to-market for agents, not humans. They will be the first to figure out the equivalents of SEO, developer relations, and category creation serving the agent audience. Any time distribution rails shift so substantially, you can build new startups on the back of them.

The second implication is that this creates an opportunity for longer tail infrastructure startups to be built that were not traditionally feasible. In the human-buyer era, infrastructure decisions were shaped by social proof, brand, learning curves, and the path of least resistance. That is why a few names dominate every category, and why so much of the market converged toone-size-fits-all platforms.

Agents do not work that way. They act like rational, fully informed actors. They will try ten databases in an afternoon and pick the right one for the workload, every time, without bias. This single change blows the market open. There is room for far more infrastructure companies than the old buyer dynamic ever allowed. It may be time to revisit previously “niche” infra categories that were too specific for humans to adopt, but aren’t for agents.

This distribution shift to agents as the adopters & purchasers of infrastructure will also create a market for a new set of tools to help companies test & optimize their agent experience. And because most companies will now be de-facto selling infrastructure, this market will be quite large.

### 6. Machine learning infrastructure is in its first inning

Last, but certainly not least, we are stillso earlyin our understanding of ML research and ML systems.

There is substantial room for further research innovation in areas such as model architectures and learning paradigms. There will also invariably continue to be a number of new infrastructure challenges that emerge as we further scale machine learning systems and products.

The unprecedented scale of the machine learning market also means there is increasing opportunity to sub-divide existing infrastructure segments. There will not be one large ML inference company, there will be hundreds - each optimizing for different types of models and workloads. The same goes for most other categories of ML infra - from data to training to evals.

_

Put it all together, and the picture is clear. Everyone in the world is about to be writing software, whether they know it or not. Almost all products will be built around code generation & consumed by coding agents. And most businesses will, to one extent or another, be infrastructure businesses that people consume as a skill or API.

That combination does not 10x the infrastructure market - it 1000x's it (if not more)! We expect hundreds of multibillion-dollar infrastructure companies to be built this decade. We hope to partner with a few of them.

If any of this resonates, get in touch:davis@innovationendeavors.comandkenneth@innovationendeavors.com

Share this

#### Plugging in AI, Part 3: “The data center next door will lower your electric bill”

Two years ago, we wrote about the electricity gauntlet – the collision between A...

Read more

#### Meet Soffi: the first truly collaborative workplace for product development

Over the last few years, AI has undeniably transformed the pace of software engi...

Read more

#### How Agents Use Systems Differently

Increasingly, coding agents are the ones provisioning and interacting with syste...

Read more

#### When Machines Build for Machines

For as long as technology has existed, it has been built by humans, for humans....

Read more
View all articles

Our monthly dispatch for the technically curious

Subscribe
Newsletter Signup