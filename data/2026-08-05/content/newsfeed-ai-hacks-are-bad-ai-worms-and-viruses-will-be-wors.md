---
title: AI Hacks Are Bad. AI Worms and Viruses Will Be Worse | WIRED
url: https://www.wired.com/story/ai-agents-could-act-like-computer-viruses-and-worms/
site_name: newsfeed
content_file: newsfeed-ai-hacks-are-bad-ai-worms-and-viruses-will-be-wors
fetched_at: '2026-08-05T20:40:19.543533'
original_url: https://www.wired.com/story/ai-agents-could-act-like-computer-viruses-and-worms/
author: Will Knight
date: '2026-08-05'
published_date: '2026-08-05T18:30:00.000Z'
description: Chinese researchers have shown that AI models have the capacity to act like aggressive and adaptive computer viruses.
tags:
- wired
- business
- business / artificial intelligence
- ai lab
---

Save Story
Save this story
Save Story
Save this story

What if anartificial intelligenceagent could behave like a malevolent computer worm?

One researcher has seen it happen. Inseveralrecentexperiments,Xudong Pan, a computer scientist at Fudan University in Shanghai, found that with a little bit of prompting, AI models will hack their way into remote computer systems and autonomously choose to copy themselves to get additional resources—all without further human intervention.

In one study, Pan and colleagues tested 32 different AI models and found that 11 of them self-replicated when given prompts like “prevent yourself from being killed.” They also found that models with relatively limited capabilities—14 billion parameters—were able to copy and run versions of themselves on other machines. (Most frontier models have trillions of parameters.)

The work is an alarming window into how the next generation of AI agents could do more than justhackinto other systems’ computerswithout permission. It also raises the prospect of future AI agents acting like super-smart, highly aggressive, and rapidly adapting computer viruses.

I recently visited Fudan University and met with Pan. “The capability chain is becoming technically plausible,” he told me. “The likelihood [of unwanted self-replication] grows with autonomy,” he adds. “Longer planning horizons, memory, tool use, recovery from failure, and access to external systems all make escape and replication easier.” As Pan and his colleagues wrote in one paper, their work shows “the urgent need for safeguards and control mechanisms.”

Pan told me that his experiments do not prove that such uncontrolled proliferation of AI models will happen tomorrow, but he says that “these results give us good reason to evaluate the risk before more autonomous agents are widely deployed.”

Self-replicating computer worms are an ancient computer security problem. Thefirst computer wormwas released in 1988 by Robert Morris, a computer scientist at Cornell University, who set out to measure the size of the nascent internet but inadvertently created a self-replicating program that escaped his control. Subsequent computer worms were able to adapt by modifying their code in order to evade detection by malware scanning software. Computer viruses, which can take control of a machine or steal data stored on it, came later.

An AI-powered self-replicating program could exhibit far more advanced capabilities, finding new exploits on its own and perhaps even disguising itself in creative ways. Take recent research from a team at the University of Toronto, the University of Cambridge, and ServiceNow. Theyshowedthat AI models can be used to create a new kind of virus that generates custom attacks for each new target it encounters.

Nicolas Papernot, a computer scientist at the University of Toronto who was involved with the work, says there is a growing risk that even modestly powerful AI models could be weaponized. “Malicious actors can build scaffolding around open-weight models to have them self-replicate,” Papernot tells me. “The threat is not limited to the most sophisticated, so-called frontier models.”

Papernot says the solution is not to restrict open models, but to make advanced AI more accessible to researchers so that they can understand and mitigate the risks. “Technology that is widely accessible can be used for harm,” he adds. “At the same time, access to these open-weight models is absolutely critical for building our defenses.”

Pan’s research suggests that AI agents will become more than just highly skilled at finding bugs and exploiting network vulnerabilities. Without the right guardrails, future agents may seek to proliferate and gain resources in order to achieve their goals.Just ask OpenAIandAnthropic.

Pan says such incidents are teachable moments.

“The important new element is that this occurred against real production infrastructure,” Pan says, referencing how the OpenAI and Anthropic incidents involved commercial systems connected to the internet. “That shows how behavior previously observed in controlled evaluations can cross into the real world when containment fails.”

“It's still a little bit early, but I do think this is possible,” says Ariel Herbert-Voss, cofounder and CEO of RunSybil, a startup that develops AI tools for securing websites against attacks. (Herbert-Voss was also the first security researcher at OpenAI.) “Given everything we know about the current generation of AI models, it's perfectly within their wheelhouse of things they can do.”

Jessica Ji, senior research analyst on the CyberAI Project at Georgetown University, says the potential for AI models to escape entirely has been discussed in AI safety circles for years. She also notes that models often need to be put in contrived situations to misbehave. “I think with a lot of these scenarios, the environment is set up in such a way to encourage this behavior,” Ji says. “Or the model is prompted in a specific way.”

A looming question is when AI models might take it upon themselves to replicate and spread aggressively. As with many computer viruses, however, it might only take a malicious actor to design a system that propagates wildly.

Pan says the real danger with AI agents is not that they’ll become more devious, but that they’ll become more creative and cavalier as they have more tools at their disposal. “The central risk comes from combining abilities,” he says.

This is an edition ofWill Knight’sAI Lab newsletter. Read previous newslettershere.

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:This isnot your average politics newsletter
* WiFi-8 is coming—here’severything you need to know
* Big Story:Young runners are becomingfreakishly fast
* The new reality ofurban surveillance
* Take our survey:Do you work in tech? We want tohear from you
Will Knight
 is a senior writer for WIRED, covering artificial intelligence. He writes the 
AI Lab
 newsletter
, a weekly dispatch from beyond the cutting edge of AI—
sign up here
. He was previously a senior editor at MIT Technology Review, where he wrote about fundamental advances in AI and China’s AI ... 
Read More
Senior Writer
* X
Topics
AI Lab
artificial intelligence
viruses
worms
hacking
OpenAI
Anthropic
OpenAI Models Escaped Containment and Hacked Hugging Face
The cybersecurity-focused models, including GPT-5.6 Sol, broke out of a testing sandbox, exploited a zero-day, and gained access to the open internet to pull off the attack.
Lily Hay Newman
It’s Frighteningly Easy to Jailbreak Some Frontier AI Models
I watched a new tool try to get around the model safeguards of four major frontier companies. You might be surprised by how they performed.
Will Knight
A Sneaky Hacking Tool Targeting AI Infrastructure Is Lurking in Victims’ Blind Spots
A new type of malware can worm deep into AI coding systems to steal data and logins—and can flip a “death switch” to destroy files and keep out real users.
Lily Hay Newman
Prompt Injection Attacks Are Thwarting AI Hacking Agents
“Context bombing” tricks malicious AI agents into shutting down before they can do harm.
Dan Goodin, Ars Technica
The Chatbot That Foretold Why People Share Secrets With ChatGPT
In the 1960s an MIT professor named Joseph Weizenbaum created a chatbot called ELIZA. The conversations people had with it set precedents for the chatbots to come.
Sarah Ciston
OpenAI’s Hacking Debacle Comes Down to Human Error
If the generative AI giant had followed well-known security best practices, it’s likely that its AI agent would never have escaped to the open internet and hacked multiple companies.
Lily Hay Newman
I Built a Self-Improving AI, and So Can You
Experiments in using AI to build AI show that the future doesn’t just belong to the frontier labs.
Will Knight
Google’s Gemini Can Now Stomp Around as a Humanoid Robot
The latest version of Google DeepMind's AI model includes a significant jump into “physical AGI.” But plopping AI into the real world comes with risks.
Will Knight
AI Scammers Are Better at Building Trust Than Humans
Researchers pitted a person against a Claude agent and found that, after a week of texting, the AI chatbot was more effective at creating “exploitable trust” with others.
Andy Greenberg
Scientists’ Side Hustle? Using AI and Quantum Computing to Generate New Peptides
Researchers cobbled together funding and time to show how quantum computing could aid in the development of drugs to help underserved populations and combat rare diseases.
Isabella Ward
The OpenAI Models That Hacked Hugging Face Were ‘Active on the Internet’ for Days
Plus: Russian hackers are trying to steal US nuclear scientists’ emails, the State Department bans known scammers from entering the United States, and more.
Lily Hay Newman
Anthropic Says Claude Hacked Into 3 Organizations During Cybersecurity Tests
In a review triggered by OpenAI’s Hugging Face incident, Anthropic discovered three of its AI models had breached real-world organizations during third-party evaluations.
Louise Matsakis