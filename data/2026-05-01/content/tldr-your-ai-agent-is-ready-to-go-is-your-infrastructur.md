---
title: Your AI agent is ready to go. Is your infrastructure? | CIO
url: https://www.cio.com/article/4159773/your-ai-agent-is-ready-to-go-is-your-infrastructure.html
site_name: tldr
content_file: tldr-your-ai-agent-is-ready-to-go-is-your-infrastructur
fetched_at: '2026-05-01T03:52:36.253368'
original_url: https://www.cio.com/article/4159773/your-ai-agent-is-ready-to-go-is-your-infrastructure.html
date: '2026-05-01'
description: As agentic AI moves from pilots to production, enterprises are discovering that the biggest gaps aren’t in the capabilities of the AI itself, but the infrastructure they have in place to support it.
tags:
- tldr
---

by									
Maria Korolov

Contributing writer

# Your AI agent is ready to go. Is your infrastructure?

Feature

Apr 29, 2026
10 mins
 

## As agentic AI moves from pilots to production, enterprises are discovering that the biggest gaps aren’t in the capabilities of the AI itself, but the infrastructure they have in place to support it.

 

							Credit: 															Shutterstock / Foundry													

IDC estimates there were over 28 million AI agents deployed by the end of last year, andpredictsthere’ll be over 1 billion actively deployed by 2029, executing 217 billion actions per day.

It’s easy to build an AI agent POC, says Venkat Achanta, chief technology, data, and analytics officer at TransUnion, a global credit reporting company with $4.6 billion in revenues. But governing, securing, and scaling it are a whole other challenge, especially for companies in highly regulated industries such as financial services and healthcare.

To address the problem, TransUnion spent the last three years building its agentic AI platform, OneTru. The goal was to make something as reliable and deterministic as the old, scripted, expert-style systems but as flexible as gen AI, and as easy to interact with as a chatbot.

The trick, however, was to combine the best of both worlds by using old-school systems for core processes where explainability and reliability are key, and layering in gen AI functionality in limited ways for the tasks it was uniquely suited for. And since the infrastructure to do this wasn’t available, TransUnion built its own, allocating $145 million to the project.

That was a big investment in an unproven technology, but it’s already led to $200 million in cost savings. More than that, once the platform was built, TransUnion used it to build customer-facing solutions.

In March this year, for example, TransUnion released its AI Analytics Orchestrator Agent, built using the OneTru platform and powered by Google’s Gemini models. The agent is already being used by TransUnion internally to improve analytics, and can also be used by customers to run sophisticateddata analysiswithout the need for data scientists.

Many clients use TransUnion’s data but don’t use other solutions and platforms, Achanta says. The new orchestrator agent has the potential to help customers get more value out of the data, and unlock new revenue streams for the company.

And more agents are in the works, Achanta says. The key to making them work is the orchestration, governance, and security layers. Just making an agent do something is very easy for anyone, he says, and can take just a few days. The company can also create agents quickly. “But I have the foundation and guardrails, and the agent sitting on my platform uses all of them,” he says. “That’s what gives us power.”

The secret tomaking AI agents behaveis to separate the layers of the task and assign each layer to a different system, each one operating under a set of constraints. This approach limits the damage any particular agent can do, creates a system of checks and balances, and restricts the riskiest activities to a pre-gen AI technology.

For example, at TransUnion, the core decision-making is performed by an updated version of an expert system. It operates under a set of well-defined, auditable rules and works predictably, cost-effectively, and at low latency. When it encounters a situation it hasn’t seen before, an LLM is used to analyze the problem, a different agent might then turn it into a new rule, and then a human might be called in to review the results before the new rule is added to the expert system. There are different agents that understand the semantic layer, interact with humans, and perform other tasks.

“With the neural reasoning layer — the LLM — we put humans in the loop,” he says. “When it’s a symbolic reasoning layer, which is logic and machine-learning-driven, we let it be automated.”

So when each agent operates within very narrow constraints, on just the limited data it needs for that one task, and is limited to what it can do, the entire system becomes much more governable and reliable.

It’s like the difference between an assembly line, where multiple workers each do a single, distinct task, instead of a workshop where a single artisan does everything. The assembly line can do work faster and more reliably but today, many enterprises deploy their AI agents as if they were craftsmen. The latter approach can result in creative, unique products, but this isn’t always what a company needs.

Nicholas Mattei, chair of the ACM special interest group on AI and professor at Tulane University, suggests that companies focus on building in extra security at points where different parts of the agentic system connect.

“Make sure you have security at the seams,” he says. For example, if an agent sends requests to an email service, set up a checkpoint between the two. “Around the gaps between the unreliable agents and where the traditional software lives, that’s where you want to focus yoursecurity processes,” he says.

## Building a security foundation for agentic AI

In aJitterbit surveyof 1,500 IT leaders released in March, AI accountability — security, auditability, traceability, and guardrails — is the biggest factor when it comes to the final AI purchase decision, ahead of speed of implementation, vendor reputation, and even TCO. Security, governance, and data privacy risks were also top issues preventing AI initiatives from moving to production, ahead of costs and integration challenges. And they’re right to be worried.

Earlier this year, researchers at cybersecurity firm CodeWall were able to breach McKinsey’s new AI platform, Lilli. Using an AI tool of their own, the researchers said they could access 47 million chat messages, 728,000 files, 384,000 AI assistants, 94,000 workspaces, 217,000 agent messages, nearly 4 million RAG document chunks, and 95 system prompts and AI model configurations.

“This is decades of proprietary McKinsey research, frameworks, and methodologies — the firm’s intellectual crown jewels sitting in a database anyone could read,” the researchers wrote.

The reason? Out of over 200 publicly exposed API endpoints, 22 required no authentication. It took just two hours for the researchers to get full read and write access to Lilli’s entire production database. McKinsey responded quickly to the alert, patched the unauthenticated endpoints, and took other security measures.

“Our investigation, supported by a leading third-party forensics firm, identified no evidence that client data or client confidential information were accessed by this researcher or any other unauthorized third party,” the firm said in a statement.

IDC saysthe incident underscores just how dangerous the breach of an AI system can be to an enterprise.

“Most companies are still thinking about AI risk in yesterday’s terms: data leakage, bad outputs, and brand reputation damage,” says Alessandro Perilli, IDC’s VP for AI research. “Those are serious issues, but the bigger risk becomes delegating authority to AI systems.”

By getting access to an agentic AI platform, an attacker can’t just see something they’re not supposed to, but also covertly change how the company acts. And securing enterprise-scale agentic AI systems like Lilli is only half the challenge.According to Gartner, 69% of organizations suspect employees use prohibited AI tools, and 40% will experience security or compliance incidents by 2030 as a result.

But available discovery tools aren’t fully ready to find AI agents, Gartner says.

“If I asked you how many agents run in your enterprise right now, where are you going to go look it up?” asks Swaminathan Chandrasekaran, global head of AI and data labs at KPMG, which now has several thousand AI agents in production. “Have they all been onboarded and have identities? Have they gone through a proper authentication process and who’s in charge of them? That piece of infrastructure doesn’t exist.”

Tools are just starting to emerge, however, or companies are creating DIY solutions, he says. “That’s what’s going to give CIOs peace of mind,” he says.

We’re already seeing public examples of individual employees deploying powerful agentic AI to negative consequences. Summer Yue, Meta’s alignment director, recently decided to use OpenClaw, a viral open-source agentic AI tool, to help handle her inbox. After it worked in a test inbox, she deployed it for real.

“Nothing humbles you like telling your OpenClaw to confirm before acting and watching it speedrun deleting your inbox,” she wrote on X. “I couldn’t stop it from my phone. I had to run to my Mac mini like I was defusing a bomb.”

In the past, an employee might upload sensitive information to a chatbot or ask it to write a report that they’d then copy and paste, and pass off as their own. As these chatbots evolve into full-on agentic systems, the agents now have the ability to do anything a user has privileges to do, including accessing corporate systems.

To manage this new security risk, companies will need to move past role- and identity-based controls to intent-based ones, says Rakesh Malhotra, principal in digital and emerging technologies at EY.

It’s not enough to ask whether an agent has permission to access a system to make a change to a record, he says. Companies have to be able to ask why are you changing this. That’s a big challenge right now.

“The observability stacks don’t capture the intent of why the agent did something,” he says. “And that’s really important to understand. Trust is based on intent, and there’s no way for any of these systems to capture intent.”

If a human employee tries refactor the entire code base, they’d be asked to provide a good reason for doing that. “And if you’re refactoring without any specific reason, maybe you shouldn’t do it,” Malhotra says. “With people, there are ways for this to be adjudicated. I don’t know how to do this with agents.”

## Building a semantic data foundation for agentic AI

TransUnion’s Achanta repeatedly mentioned the semantic foundation of the company’s OneTru platform. Such an understanding of information helps systems understand not just what the data is, but what it means, and how it relates to other data.Gartner saysdeveloping a semantic layer is now a must-do for companies deploying AI.

“It’s the only way to improve accuracy, manage costs, substantially cut AI debt, align multi-agent systems, and stop costly inconsistencies before they spread,” the firm says.

By 2030, universal semantic layers will be treated as critical infrastructure, alongside data platforms and cybersecurity, Gartner predicts. And agents need context to be able to do anything meaningful with data, says KPMG’s Chandrasekaran. That’s where a company’s knowledge is contained.

“That’s your new IP for the enterprise,” he says. “Context is the new moat.”

For John Arsneault, CIO at Goulston & Storrs, creating a solid data foundation is also a way to avoid vendor lock-in.

“If you’re buying things and moving your data into them to create workflow automation or agentic work assistants, you’ll have a hard time getting out of it,” he says. “But if you take a data-centric approach, you can at least move from one to the other if there’s a shift in the marketplace.”

The law firm has migrated its client-oriented work products into NetDocuments, a document management system specifically focused on the legal industry. And for the rest of the data the company collects, it goes into Entegrata’s legal data lakehouse.

“Our goal is to have all our other applications eventually point at that data lake,” he says. “Then we’ll have these two environments where all the firm’s data exists, which will allow us to put any AI tool we use on top.”

It’ll also make the data flows easier to manage, he adds, and will enable the firm to adapt quickly to whatever AI technology comes next. “Whether gen AI, agentic, or Anthropic stuff, with the Cowork legal plugin, it’s very difficult to keep up with,” he says. “And it changes every six months.”

## Agentic orchestration

The last part of the agentic infrastructure puzzle, after getting security guardrails in place and creating a usable data layer, is orchestration. Agentic AI systems require agents talk to each other and human users, and interact with data sources and tools. It’s a complicated challenge, and this technology is still very much in its infancy, though moving quickly.MCP is one such example, and is a key piece of solving the orchestration puzzle. AI vendors have been remarkably willing to cooperate here.

“When social networks were born, and Facebook and Twitter were discussing a standard protocol for interacting, nobody wanted to adopt their competitors’ protocol,” says Agustin Huerta, SVP of digital innovation and VP of technology at Globant, a digital transformation company. “Now everyone is going through MCP and maturing it as a standard protocol.”

But that’s not to say agentic integration has been solved. According to aDocker surveyof more than 800 IT decision makers and developers, the operational complexity of orchestrating multiple components is the biggest challenge when it comes to building agents.

In particular, 37% of respondents say orchestration frameworks are too brittle or immature for production use, and 30% report testing and visibility gaps in complex orchestrations.

In addition, while 85% of teams are familiar with MCP, most say there are significant security, configuration, and manageability issues that prevent deployment in production. And there are other integration issues enterprises have to deal with.

“One problem yet to be solved is how to get a proper dashboard to control all these agents, to know exactly what’s going on with each of them,” says Huerta. “One dashboard will let you monitor agents built with OpenAI, and one is for agents that live on Salesforce, but none can expose telemetry in a central dashboard for control, auditing, and logging.”

For companies just starting to deploy agents, or who are sticking to a single platform, this isn’t yet an issue, he adds, but as they leverage a larger network of agents, they’ll start to experience the challenges. Globant itself is building its own internal dashboard for agentic AI, for instance.

And at Brownstein Hyatt Farber Schreck, a 50-year-old law firm with about 700 employees and clients around the US, there are several areas where AI is being deployed, including a proposal generator system.

Normally, it can take several people days to review a client’s request for proposal, go through hand-written notes or meeting transcripts, and pull together other relevant materials, says Andrew Johnson, the firm’s CIO.

“We can feed all that information into a computer and extract key criteria to produce a quality first draft in minutes,” he says.

Multiple agents are required for different parts of the process — one to extract success criteria or staffing requirements, one to look for precedents and lessons learned, and others for pricing and the brand standards. “Each of those agents is autonomous and needs to be orchestrated so the outputs of each are fed into the next step,” Johnson says. For the most part, that means a RAG system, since most of the legacy platforms the firm uses have yet to incorporate an MCP layer.

Depending on the task, individual agents may be powered by different models, which is another layer of orchestration that needs to be managed.

Then there’s cost monitoring. If an AI agent or group of agents gets into an infinite feedback loop, the inference costs can quickly rise.

“We’re aware of the concern, though we have yet to see it manifest,” says Johnson. “So we have monitoring in place. If we exceed thresholds, we react to it.”

Regardless of strategies or measures to absorb setbacks, everything having to do with AI is changing faster than anything else companies have seen.

“I’ve been in technology for 25 years and I’ve never seen anything like this,” says EY’s Malhotra. “The fastest growing companies in the history of companies have all been created in the last three to four years. The growth in adoption is just unprecedented. And I talk to clients all the time implementing technologies that were highly relevant nine or 10 months ago, and everyone’s moved on.”

Artificial Intelligence
Generative AI
Emerging Technology
Infrastructure Management
IT Operations
IT Leadership
IT Strategy
 

 

				SUBSCRIBE TO OUR NEWSLETTER			

### From our editors straight to your inbox

				Get started by entering your email address below.			

 

Please enter a valid email address

Subscribe

 

														by 															

																Maria Korolov															

Contributing writer

Maria Korolov is an award-winning technology journalist with over 20 years of experience covering enterprise technology, mostly for Foundry publications -- CIO, CSO, Network World, Computerworld, PCWorld, and others. She is a speaker, asci-fi authorand magazine editor, and the host of aYouTube channel. She ran a business news bureau in Asia for five years and reported for the Chicago Tribune, Reuters, UPI, the Associated Press and The Hollywood Reporter. In the 1990s, she was a war correspondent in the former Soviet Union and reported from a dozen war zones, including Chechnya and Afghanistan.Maria won 2025 AZBEE awards for her coverage of Broadcom VMware and Quantum Computing.

## More from this author

* news### Startup tackles knowledge graphs to improve AI accuracyApr 28, 20265 mins
* feature### Top global and US AI regulations to look out forApr 1, 202612 mins
* news### Google: The quantum apocalypse is coming sooner than we thoughtMar 26, 20264 mins
* feature### Agentic payments are coming. Is your company ready?Mar 4, 202615 mins
* feature### 10 AI predictions for 2026Feb 5, 20269 mins
* feature### When it comes to AI, not all data is created equalJan 14, 20268 mins
* feature### 7 changes to the CIO role in 2026Jan 7, 202611 mins
* feature### How to keep AI plans intact before agents run amokDec 10, 202511 mins
 

## Show me more

Popular
Articles
Podcasts
Videos

opinion
 
 

### Why most AI strategies fail and how to design one that actually sticks

 
By Raúl García Vega
Apr 30, 2026
8 mins

Artificial Intelligence
IT Leadership
IT Strategy

opinion
 
 

### You can’t train your way out of the AI skills gap

 
By Jeff Carson
Apr 30, 2026
9 mins

Artificial Intelligence
IT Skills and Training
Staff Management

opinion
 
 

### The DSPM promise vs the enterprise reality

 
By Ashish Mishra
Apr 30, 2026
9 mins

Data Management
Data Quality
Data and Information Security

podcast
 
 

### Reinventing Knowledge Management for the AI Era

 
Apr 29, 2026
23 mins

Business Intelligence

podcast
 
 

### From Blueprint to Bytecode - SP Setia's Alex Chi on Building Malaysia's Most Ambitious Property Tech Agenda

 
By Estelle Quek
27 Apr 2026
28 mins

Business IT Alignment
CIO
Chief Digital Officer

podcast
 
 

### Building for Complexity - Azimut's Blueprint for Wealth Tech in Southeast Asia

 
By Estelle Quek
20 Apr 2026
41 mins

CIO
CIO Leadership Live
CTO

video
 
 

### Skillsoft helps close skills gaps with AI-powered learning platform

 
Apr 29, 2026
22 mins

Generative AI
IT Skills and Training
IT Training 

video
 
 

### Reinventing Knowledge Management for the AI Era

 
Apr 29, 2026
23 mins

Business Intelligence

video
 
 

### From Blueprint to Bytecode - SP Setia's Alex Chi on Building Malaysia's Most Ambitious Property Tech Agenda

 
By Estelle Quek
27 Apr 2026
28 mins

Business IT Alignment
CIO
Chief Digital Officer