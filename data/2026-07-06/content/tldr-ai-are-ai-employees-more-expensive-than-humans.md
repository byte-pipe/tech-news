---
title: 'AI: Are AI employees more expensive than humans?'
url: https://lex.substack.com/p/ai-tokens-are-cheaper-but-ai-bills
site_name: tldr
content_file: tldr-ai-are-ai-employees-more-expensive-than-humans
fetched_at: '2026-07-06T07:31:29.659066'
original_url: https://lex.substack.com/p/ai-tokens-are-cheaper-but-ai-bills
author: Luke Spill
date: '2026-07-06'
description: Finance departments need to have serious conversations around weighing costs of tokens against human payroll.
tags:
- tldr
---

# AI: Are AI employees more expensive than humans?

### Finance departments need to have serious conversations around weighing costs of tokens against human payroll.

Luke Spill
Jul 02, 2026
35
1
Share

Hi Fintech Futurists —

Today’s agenda is below.

1. AI:Per-token prices are collapsing, yet AI bills are exploding at the same time.
2. REPORT:The State of Finance for Marketers, and where Banks are beating Fintechs
3. PODCAST:Inside the $1B-a-Day Stablecoin Market Maker for 1,500 Institutions, with B2C2’s Cactus Raazi
4. CURATED UPDATES:Machine Models, AI Applications in Finance & Investment Outlook

To support this writing and access our full archive of newsletters, analyses, and guides to building in Fintech & DeFi, subscribe below (if you haven’t yet).

Subscribe

### 🤖🏦🧭 Our Ecosystem:

Generative Ventures|AI Research|Robot Money|Linkedin&Twitter|Sponsors

* 🚀 Lex is actively meeting teams building machine-native financial companies. If that’s you, reachout here.
* 🤖AI & Robotics Industry Encyclopedia:In this 100+ page report, we collate all the meaningful companies across public quities, private equity, and digital assets related to the machine economy. 👉Learn more here
* 🦄 In partnership with InterPrivate, we just launched a$200MM SPAClooking for targets in fintech, digital assets, and AI infrastructure. If you are a late-stage founder or have an idea to discuss, reply directly to this email.

### Cheaper tokens are NOT leading to cheaper AI bills

Nvidia has put its next data-centre platformVera Rubinintofull production.

The headline was the10x reductionin the cost of generating a token, achieved by tripling the memory bandwidth feeding each chip. By token, we mean the AI-inference kind of intelligence token, not digital assets.

Source

Jensen Huang called it “token factory economics”, and described the modern data centre as a machine whose output is measured in tokens per watt.

In the same few weeks, the buyers of that output were reaching a different conclusion. JPMorgan’s technology desk sent clients a note titled“AI Bills Are Out of Control”, reporting that some investment analysts were running personal token budgets into the tens of thousands of dollars, a handful past $100,000. Uber’s chief technology officer told The Information he hadburned throughthe company’s entire 2026 AI budget in four months... A four-person startup posted a$113,000monthly bill from a single model provider.

The gap between the cheapening of tokens and rising AI bills is where finance teams have to step in.

### The key numbers of Unit Price x Consumption

Most coverage of the cost of AI folds three numbers into one.

The first is unit price, which is falling fast. Andreessen Horowitz’s Guido Appenzeller measured atenfold annual declinein the cost of a given level of model performance, from $60 per million tokens in 2021 to $0.60 three years later.

Source

Epoch AI, working from benchmark data rather than list prices, found the cost of reaching a fixed performance levelhalving roughly every two months, with declines ranging from 9x to 900x a year depending on the task.

Source

On any measure, intelligence per dollar is getting cheaper faster than compute did during the personal-computer era.

The second number is consumption, and it is climbing at least as fast. Goldman Sachs Research, in a May report modelling the agentic economy from the bottom up, put token consumption on course tomultiply 24x timesby 2030, to 120 quadrillion tokens a month.

##### Estimated monthly token count for Agentic AI applications

An agent reads and re-reads context, calls tools, checks its own work across several rounds, and often runs without being asked. Goldman’s own worked example of a software-development agent gets through roughly 6M input tokens and 820K output tokens in a day.

The third number is the one a finance director reviews — that is the bill. It is the product of the other two, and because consumption is rising faster than prices fall, the bill is getting bigger each month.

### What sets the price, and where it goes

Generating a token is not, for the most part, an arithmetic problem. A model produces one token at a time, and for each one, it must read its weights and accumulated context out of memory. The calculation involved is small next to the cost of moving that data, so an accelerator running inference typically uses onlythirty to forty per centof its theoretical compute, and the rest of the time it waits for memory.

Inference is bound by memory bandwidth.

The store of context a model holds grows with the length of the exchange and the number of requests handled at once, and now routinelytakes more memory than the model’s own weights. Almost all of the engineering that has made tokens cheaper, from caching to quantisation to smarter batching, amounts to managing memory traffic.

This is why Nvidia’s tenfold claim for Vera Rubin rests on memory rather than maths. The platform triples per-chip bandwidth to 22 terabytes a second with HBM4. That change carries most of the savings, as memory is now the largest line in the price of an AI server, up more thanfour hundred per centover the previous generation.

Then comes energy usage. One peer-reviewed paper estimates a single frontier query at about a third of a watt-hour, if the reasoning is then stretched to 15x the tokens, then the energy risesroughly 13x. If you wrap the model in an agent that loops through tools and checks its own answers, one request can use60x to a 140xthe energy of a one-shot reply.

While each token becomes cheaper, the models are making each task consume more of them.

### The financial comparison

Arvind Jain, who runs the enterprise-search firm Glean, told CNBC this was the first time in his career that technology cost about the same as people, and that the choice between the two was being putdirectly to finance teams. Nvidia’s own Bryan Catanzaro said that for his deep-learning group, the cost of compute already ran farbeyond the cost of the employees.

However, Gartner’s forecast that a developer’s token spend will match or exceed a software engineer’s salary by 2028, rests on aglobal-average wage of $2,000 a month, not a Western one. In London or New York, token spend is not about to overtake a six-figure salary, but in Bangalore it may already match a mid-level engineer’s pay, because the token price does not vary by geography even though the wage does.

The dominant enterprise pattern is now the advisor model, in which a cheap open-weight models handle the bulk of the work and calls a frontier model only when stuck, capable of cutting bills by an order of magnitude through routing alone. Chinese open-weight models such asDeepSeek and Zhipunow land within a point or two of the Western frontier on Agentic benchmarks at a 1/5 of the cost or less.

### Key Takeaways

So what should we do with the information that AI may be ramping up costs as much as it is cutting them?

* Investors: Watch inference margin. The valuations floated for the model labs ahead of their listings assume pricing power. AI-native software carries 40% - 50% of revenue as inference cost, against 10% - 20% for classic SaaS models.
* Founders:Track cost per completed task, not per seat, and keep the model layer swappable. Context engineering is now a cost centre that needs human management.
* Operators: The cost implications are strongest where compliance overhead is heaviest, so price agents against the human cost, and build budgets on the assumption that frontier-reasoning unit cost may not fall in the future.

If the marginal token is increasingly priced by memory bandwidth and electricity rather than by the model itself, the cost advantage in AI-driven finance accrues to whoever controls power and routing, not to whoever trained the cleverest model. For an industry that has spent two years worrying about its dependence on a few model providers, price may be the tipping point.

Further, this creates opportunities for net new human jobs.

Source

Recent data from Ramp shows that companies that spend more on AI also increase their staff numbers across all jobs. Good news at last — we can be robot shepherds.

👑Related Coverage👑

#### AI: Ramp and Stripe Race to Bank the Bots

Laurence Smith
·
Mar 17
Read full story

#### AI: Could the next generation of OpenAI and Google AI Agents be financial?

Z.Z
·
May 21, 2024
Read full story

#### AI: Financial analysts will be replaced or augmented by LLMs, see $2.5B AlphaSense

Z.Z
·
June 17, 2024
Read full story

### Report: The State of Finance for Marketers, and where Banks are beating Fintechs (linkhere)

Today, we are excited to highlight AppsFlyer’sState of Finance for Marketers: Europe 2026 report.

It tracked 2.4 billion installs and roughly a billion dollars of spend to figure out where Europe’s finance marketing budget is actually going.

There are some pretty fascinating metrics in here, so let’s dig in. Or, if you want to just see the numbers, click below:

Read Report

### 🎙️Podcast: Inside the $1B-a-Day Stablecoin Market Maker for 1,500 Institutions, with B2C2’s Cactus Raazi (linkhere)

Hi Fintech Architects,

In this episode, Lex chats withCactus Raazi— CEO Americas at B2C2, one of the original and largest institutional market makers in digital assets, serving roughly 1,500 institutions and pricing across more than 40 exchanges globally.

They discuss what a market maker actually does, how balance sheet and signal generation underpin roughly $1 billion a day of stablecoin flow at B2C2, and why the two extremes of crypto market making - riskless principal aggregation versus proprietary alpha - produce very different client outcomes that buyers rarely understand.

Cactus explains B2C2’s 18-month bet that the Circle-versus-Tether debate would give way to a multi-issuer world, the launch of its PENNY product for instant zero-cost cross-stablecoin swaps, and they explore why programmability is the next frontier for digital dollars, why US capital markets have almost no structure for funding genuine risk-taking businesses, and whether the current combination of scale, speed, and complexity makes this the hardest investing environment Wall Street has ever faced.

Listen to Podcast

Fintech Blueprint 🤖🏦🧭 is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Subscribe

## Curated Updates

Here are the rest of the updates hitting our radar.

### Machine Models

Ethical and Bias Considerations in Artificial Intelligence/Machine Learning- Matthew G. Hanna & Liron Pantanowitz & Brian Jackson & Octavia Palmer & Shyam Visweswaran & Joshua Pantanowitz & Mustafa Deebajah & Hooman H. Rashidi

A Critical Field Guide for Working with Machine Learning Datasets- Sarah Ciston & Mike Ananny & Kate Crawford

### AI Applications in Finance

⭐AI-Driven Payment Systems: From Innovation To Market Success- Merve Ozkurt Bas

The Rise Of Generative Ai Agents In Finance: Operational Disruption And Strategic Evolution- Inesh Hettiarachchi

Financial Modeling in Corporate Strategy: A Review of AI Applications For Investment Optimization- Olufunmilayo Ogunwole & Ekene Cynthia Onukwulu & Micah Oghale Joel & Ejuma Martha Adaga & Augustine Ifeanyi Ibeh

### Investment Outlook

⭐Private Equity Outlook 2025: Is a Recovery Starting to Take Shape?- Bain & Company

⭐Global Venture Capital Outlook: The Latest Trends- Bain & Company

⭐Global Private Markets Report 2025: Braced for shifting weather- McKinsey & Company

## 🚀Postscript

* Sponsor the Fintech Blueprint and reach over 200,000 professionals.👉Reach out here.
* Check out our new AI products newsletter,Future Blueprint. (Don’t tell anyone)
* Read ourDisclaimer here— this newsletter does not provide investment advice
* Contributors:Lex,Laurence,Matt,Farhad,Daniel,Michiel,Luke
* For access to all our premium content and archives, consider supporting us with a subscription. In addition to receiving our free newsletters, you will get access to all Long Takes with a deep, comprehensive analysis of Fintech, Web3, and AI topics, and our archive of in-depth write-ups covering the hottest fintech and DeFi companies.

Upgrade to Premium

35
1
Share
Previous