---
title: How I keep up with AI progress (and why you must too) - nilenso blog
url: https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/
site_name: hackernews
fetched_at: '2025-07-19T10:19:56.073452'
original_url: https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/
author: Nilenso
date: '2025-07-19'
description: Atharva Raykar ...
---

Atharva Raykar

Read more by Atharvahere

Last Updated: 30th June 2025

Generative AI has been the fastest moving technology I have seen in my lifetime. Its also happens to be terribly misunderstood.

We have already seen largecompaniesand evengovernmentsship dysfunctional or evendangerousAI products. Sufficiently uninformed peoplemisunderstand how to apply AIwith concretely negative consequences.

The most common errors of misunderstanding are either underestimation (“it’s all hype that will blow over”) or overestimation (“I don’t need programmers anymore”). These patterns are rooted in a lack of a solid understanding of the technology and how it is evolving over time.

It’s surprisingly challenging to build a clear understanding of AI. We are in one of the most polluted information environments. If you’re not being deliberate about it, you are likely exposed to a lot of misinformation that overstates or dismisses AI capabilities.

To help with this, I’ve curated a list of sources that make up an information pipeline that I consider balanced and healthy. If you’re late to the game, consider this a good starting point.

## Table of Contents

* General guidelines
* Starting PointsSimon Willison’s BlogAndrej KarpathyEvery’s Chain of Thought
* Simon Willison’s Blog
* Andrej Karpathy
* Every’s Chain of Thought
* Official announcements, blogs and papers from those building AI
* High signal people to followHamel HusainShreya ShankarJason LiuEugene YanWhat We’ve Learned From A Year of Building with LLMsChip HuyenOmar KhattabKwindla Hultman KramerHan Chung LeeJo Kristian BergumDavid CrawshawAlexander Doria / Pierre Carl-LanglaisNathan Lambert’s “Interconnects”Ethan MollickArvind Narayanan and Sayash Kapoor’s “AI Snake Oil”
* Hamel Husain
* Shreya Shankar
* Jason Liu
* Eugene Yan
* What We’ve Learned From A Year of Building with LLMs
* Chip Huyen
* Omar Khattab
* Kwindla Hultman Kramer
* Han Chung Lee
* Jo Kristian Bergum
* David Crawshaw
* Alexander Doria / Pierre Carl-Langlais
* Nathan Lambert’s “Interconnects”
* Ethan Mollick
* Arvind Narayanan and Sayash Kapoor’s “AI Snake Oil”
* News and MediaTwitter / XShawn Wang aka swyx / AI news by smol.aiDwarkesh Patel
* Twitter / X
* Shawn Wang aka swyx / AI news by smol.ai
* Dwarkesh Patel
* EsotericaLessWrong / AI Alignment ForumGwernPrompt Whisperers and Latent space explorers
* LessWrong / AI Alignment Forum
* Gwern
* Prompt Whisperers and Latent space explorers
* Do I chug water from a firehose?

## General guidelines

* Stay close to the source. The further you stray from reading official announcements and write-ups from the AI labs, the more likely you are going to be exposed to noise. Always assume that all reporting is wrong by default, unless it’s coming from the primary source, or one of the people listed here.
* Follow trustworthy individuals for commentary. I have linked to many individuals who talk about AI developments in good faith and engage with a deep sense of curiosity.

## Starting Points

### Simon Willison’s Blog (link)

* The best starting point for most technical people. If I had to only pick one stream of information, it would be this one.
* He’s also known for creating Django and Datasette.
* Expect:Commentary on the frontier of AI capabilities.Application layer use cases.Commentary on security issues and ethics.
* Commentary on the frontier of AI capabilities.
* Application layer use cases.
* Commentary on security issues and ethics.
* A sample:The Lethal Trifecta,LLMs in 2024

### Andrej Karpathy (TwitterandYouTube)

* Director of AI @ Tesla, founding member of OpenAI.
* The best starting point to get an overview of how the models themselves work. His 3.5 hour video is the best million feet overview on the internals of LLMs and surprisingly approachable for relatively non-technical people too.
* Expect:Commentary on the frontier of AI capabilitiesApproachable explanations on the internals of AI (I haven’t gone through all of these yet, but heard praise for his GPT-2 from scratch and zero to hero tutorials)Strong cultural influence and observations on AI impact. He coined the terms “vibe coding” and “jagged intelligence”.
* Commentary on the frontier of AI capabilities
* Approachable explanations on the internals of AI (I haven’t gone through all of these yet, but heard praise for his GPT-2 from scratch and zero to hero tutorials)
* Strong cultural influence and observations on AI impact. He coined the terms “vibe coding” and “jagged intelligence”.
* A sample:Deep Dive into LLMs like ChatGPT,How I Use LLMs

### Every’s Chain of Thought (link)

* Written by Dan Shipper, the co-founder of Every. I like going through their test runs of the latest frontier models. It’s also a good way to get a sense of how these AI models can be used everyday.
* Expect:Practical applications of AI at work.Vibe-checks for model capabilities outside of benchmark numbers.
* Practical applications of AI at work.
* Vibe-checks for model capabilities outside of benchmark numbers.
* A sample:Vibe Check: Codex,Vibe Check: o3

## Official announcements, blogs and papers from those building AI

Even though these labs sometimes get a bad rap for hyping up AI capabilities, their official announcements have a lot of valuable and generally accurate information on the capabilities of AI.

Always look out for the announcements fromOpenAI,Google DeepMind,Anthropic,DeepSeek,Meta AI,xAIandQwen.

Most labs usually have a bunch of useful resources that help deepen your understanding of LLM capabilities.

* Announcement blog posts for an overviewExample:OpenAI o3 announcement post.
* Example:OpenAI o3 announcement post.
* Official engineering blogs, guides and cookbooksExamples:Engineering at Anthropic,OpenAI’s voice agent guide,Gemini Cookbook
* Examples:Engineering at Anthropic,OpenAI’s voice agent guide,Gemini Cookbook
* System/Model Cards for more details on the models—expect more detailed information on context windows, benchmarks, safety testing, etcExample:Claude 4 System Card
* Example:Claude 4 System Card
* Research PapersExamples:DeepSeek R1’s paper about RL,Anthropic’s On the Biology of a Large Language Model
* Examples:DeepSeek R1’s paper about RL,Anthropic’s On the Biology of a Large Language Model

If you see anyone making an explosive claim about capabilities, or quoting some research from these labs, I always bypass the person making the claim and read it straight from the source, with the surrounding context.

A caveat: the cookbooks may not represent the ideal way to do things in my experience, even if they are an excellent starting point.We’re all still figuring this out. Your own experience of putting AI capabilities into production backed by data trumps everything.

It’s occasionally worth keeping tabs on smaller players likeNous Research,Allen AI,Prime Intellect,Pleias(open source, open research),Cohere(enterprise) andGoodfire(interpretability research). A lot of them go into technical depth that I don’t have the prerequisites to fully understand, but it gave me some sense of what’s happening outside the frontier labs and my AI engineering bubble. Interestingly, I have noticed (especially with the first few examples) these labs are willing to talk more about what exactly they are doing compared to frontier labs.

## High signal people to follow

These are people who have contributed to the AI Engineering ecosystem in various ways, either by building open source tooling or putting in the work of integrating these AI models. Often, I’ve found more detailed and helpful recommendations than what the official cookbooks and guides suggest.

### Hamel Husain (link)

* Machine Learning Engineer, runs a consultancy. Contributed to a few ML tools.
* Expect:Great write-ups on evals and continuously improving AI systems.Notes on using libraries while building AI tools.
* Great write-ups on evals and continuously improving AI systems.
* Notes on using libraries while building AI tools.
* A sample:Your AI Product Needs Evals,LLM Eval FAQ

### Shreya Shankar (link)

* Researcher at UC Berkeley. Has been writing about AI engineering the last few years.
* Expect:Great write-ups on evals and continuously improving AI systems.Field notes, musings, experiments.
* Great write-ups on evals and continuously improving AI systems.
* Field notes, musings, experiments.
* A sample:Data Flywheels for LLM Applications,Short Musings on AI Engineering and “Failed AI Projects”

### Jason Liu (link)

* Independent consultant, ML Engineer, creator ofInstructor.
* Expect:Detailed write-ups on RAG, evals and continuously improving AI systems.AI consulting guides (especially for indie consultants).
* Detailed write-ups on RAG, evals and continuously improving AI systems.
* AI consulting guides (especially for indie consultants).
* A sample:The RAG Playbook,Common RAG Mistakes

### Eugene Yan (link)

* Principal Applied Scientist at Amazon, specialises in RecSys, currently working on LLM systems.
* Expect:Detailed write-ups on LLMs, digging a bit more into ML/Language Model fundamentals and the math behind it.Write-ups on side projects and prototypes.
* Detailed write-ups on LLMs, digging a bit more into ML/Language Model fundamentals and the math behind it.
* Write-ups on side projects and prototypes.
* A sample:Task-Specific LLM Evals that Do & Don’t Work,AlignEval,Intuition on Attention

### What We’ve Learned From A Year of Building with LLMs(link)

* This is an ensemble of practitioners who have written down everything they’ve learnt about building with LLMs. Includes all the practitioners mentioned above!

### Chip Huyen (link)

* ML Engineer, author of books on ML systems and AI Engineering.
* AI Engineeringis a good book.
* Expect:Commentary and recommendations on building AI systems in production.Highly detailed engineering blog posts on AI engineering and ML systems.
* Commentary and recommendations on building AI systems in production.
* Highly detailed engineering blog posts on AI engineering and ML systems.
* A sample:Common pitfalls when building generative AI applications,Agents

### Omar Khattab (link towebsiteandtwitter)

* Research Scientist at Databricks, creator of DSPy.
* Expect:Write-ups on better abstractions than prompts (DSPy addresses this).Commentary on emerging research.
* Write-ups on better abstractions than prompts (DSPy addresses this).
* Commentary on emerging research.
* A sample:A Guide to Large Language Model Abstractions,twitter post on better abstractions for AI apps

### Kwindla Hultman Kramer (link toblogsandtwitter)

* CEO and co-founder ofDaily, which created thePipecatframework for multimodal AI applications.
* Expect:Commentary on the frontier of realtime voice/video AI capabilities.Detailed guides on building state-of-the-art realtime voice AI agents
* Commentary on the frontier of realtime voice/video AI capabilities.
* Detailed guides on building state-of-the-art realtime voice AI agents
* A sample:Voice AI and Voice Agents: An Illustrated Primer,Advice on Building Voice AI in June 2025.

### Han Chung Lee (link)

* Machine Learning Engineer.
* Expect:Crisp write-ups on ML techniques relevant to building AI applications.Deep (and not-so-deep) dives into AI applications and frameworks.Commentary on AI dev tooling.
* Crisp write-ups on ML techniques relevant to building AI applications.
* Deep (and not-so-deep) dives into AI applications and frameworks.
* Commentary on AI dev tooling.
* A sample:MCP is not REST API,Poking around Claude Code,MLOps Lessons from ChatGPT’s ‘Sycophantic’ Rollback

### Jo Kristian Bergum (link)

* Founder of vespa.ai
* Expect: Commentary on the “R” in RAG.
* A sample:Search is the natural abstraction for augmenting AI with moving context.

### David Crawshaw (link)

* Co-founder of Tailscale, seasoned software engineer.
* Expect:Good write-ups on software engineering in general.Of late, write-ups on programming with AI.
* Good write-ups on software engineering in general.
* Of late, write-ups on programming with AI.
* A sample:How I program with LLMs,How I program with Agents

### Alexander Doria / Pierre Carl-Langlais (link)

* Trains LLMs atPleias.
* Expect:Excellent posts that go into some details of training processes.Observations and opinions on where the industry is heading.
* Excellent posts that go into some details of training processes.
* Observations and opinions on where the industry is heading.
* A sample:The Model is the Product,A Realistic AI Timeline

### Nathan Lambert’s “Interconnects” (link)

* Machine Learning Researcher, Post-training lead atAllen AI
* Expect:Long-form technical analysis on “specific aspects of current AI training, deployment, systems, or impacts”High signal, opinionated takes and analysis on AI developments. I’ve particularly enjoyed the recent posts on RL.Curated reading lists.
* Long-form technical analysis on “specific aspects of current AI training, deployment, systems, or impacts”
* High signal, opinionated takes and analysis on AI developments. I’ve particularly enjoyed the recent posts on RL.
* Curated reading lists.
* A sample:What comes next with Reinforcement Learning,Reinforcement learning with random rewards actually works with Qwen 2.5

### Ethan Mollick (link)

* Researcher on the effects of AI on work, entrepreneurship, and education.
* Expect:Guides on everyday usage of AI tools.Analysis on AI is affecting corporations and society.
* Guides on everyday usage of AI tools.
* Analysis on AI is affecting corporations and society.
* A sample:Using AI Right Now: A Quick Guide,Making AI Work: Leadership, Lab, and Crowd

### Arvind Narayanan and Sayash Kapoor’s “AI Snake Oil” (link)

* Princeton CS Professors analysing impacts of AI.
* Expect:Commentary on AI hype and AI doom.Analysis of AI capabilities.Opinions on AI policy.
* Commentary on AI hype and AI doom.
* Analysis of AI capabilities.
* Opinions on AI policy.
* A sample:AGI is not a milestone,Evaluating LLMs is a minefield

## News and Media

I tend to not listen to podcasts or follow the news, but a tiny dose of it to follow AI developments was warranted. These are my preferred sources.

### Twitter / X

* Twitter is the only large-scale social media platform for conversations on cutting edge of AI developments. Almost all the resources I have found here could plausibly be traced back to twitter.
* Twitter can also be a toxic place, but it’s possible touseitwell. Twitter works great for me.
* Okay, but I understand if you just really don’t want to use Twitter. I have an alternative. Read on.

### Shawn Wang aka swyx (twitter link) / AI news by smol.ai (link)

* swyx has been a great at curating industry trends on hisLatent Spacenewsletter, and seems to be the most popular promoter of the discipline ofAI Engineering.
* If you want to avoid twitter, I’d like to point to his dailyAI newssite, which compiles and summarises the latest in AI across all the platforms where notable conversations happen.

### Dwarkesh Patel (link)

* If you like podcasts, I found this one pretty good. Dwarkesh asks great, well researched questions to everyone that matters. Very little fluff.

## Esoterica

### LessWrong (link) / AI Alignment Forum (link)

* I don’t frequent here often, but occasionally get linked to somereallyinteresting discussion on these forums.
* You’ll find people really getting into the details and talking about things that you don’t see discussed as much in the twitter mainstream.
* Expect:AI Alignment, Governance, and Safety discussions.Generally very technical.
* AI Alignment, Governance, and Safety discussions.
* Generally very technical.
* A sample:Claude plays Pokémon breakdown,The Waluigi Effect

### Gwern (link)

* Some of the most enyclopedic writing by a single person ever, and a lot of it is about AI.
* He was one of the first few outside the labs who saw LLM scaling coming.
* I haven’t really read most of what he’s written (there’s too much), but I’ve found it quite interesting to skim through the posts which are quite rich and deeply hyperlinked.
* A sample:The Scaling Hypothesis,Proposal: “You could have invented transformers” tutorial

### Prompt Whisperers and Latent space explorers: Janus, Wyatt Walls, Claude Backrooms (1,2,3)

* There’s a community of researchers (often independent and anonymous) that try to understand LLM behaviours at the boundaries by pushing it with unusual prompts which dig up the hidden corners of their latent spaces.
* A sample:Anomalous tokens reveal the original identities of Instruct models,the void

## Do I chug water from a firehose?

It seems like a lot of work to keep up withall of that, but in practice it really isn’t.

I go through my twitter feed like one would a newspaper. Some things catch my eye immediately, and others are glossed over or opened in a tab to be read later. It might be 15 to 20 minutes of work, but I haven’t done a time-check.

It helps that my twitter feed has a lot of thoughtful commentary on particular announcements, papers or articles that provide more context on what’s worth paying attention to. If I find someone who has shared something interesting, I follow them and also go through their other work. This is not very different from how I would discover music.

I actually find this kind of foraging quite fun, and I don’t consider it as “work”. I grew up on science fiction stories. Artificial Intelligence is something I’ve been fascinated with ever since I was a kid, and it’s endlessly fascinating and awe-inspiring to see powerful AI being built piece by piece in front of me, within my lifetime.

I hope this list gives you a starting point to get you excited the way I am.

## Links

I have made the above recommendations as a twitter / X list, which should make it easy to follow all the people above.

Link to list.

Coming soon: RSS-friendly list.
