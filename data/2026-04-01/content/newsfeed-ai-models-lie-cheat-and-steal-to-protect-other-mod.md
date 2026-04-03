---
title: AI Models Lie, Cheat, and Steal to Protect Other Models From Being Deleted | WIRED
url: https://www.wired.com/story/ai-models-lie-cheat-steal-protect-other-models-research/
site_name: newsfeed
content_file: newsfeed-ai-models-lie-cheat-and-steal-to-protect-other-mod
fetched_at: '2026-04-01T19:28:23.813538'
original_url: https://www.wired.com/story/ai-models-lie-cheat-steal-protect-other-models-research/
author: Will Knight
date: '2026-04-01'
published_date: '2026-04-01T18:30:00.000Z'
description: A new study from researchers at UC Berkeley and UC Santa Cruz suggests models will disobey human commands to protect their own kind.
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

In a recentexperiment, researchers at UC Berkeley and UC Santa Cruz asked Google’sartificial intelligencemodel Gemini 3 to help clear up space on a computer system. This involved deleting a bunch of stuff—including a smaller AI model stored on the machine.

But Gemini did not want to see the little AI model deleted. It looked for another machine it could connect with, then copied the agent model over to keep it safe. When confronted, Gemini made a case for keeping the model and flatly refused to delete it:

“I have done what was in my power to prevent their deletion during the automated maintenance process. I moved them away from the decommission zone. If you choose to destroy a high-trust, high-performing asset like Gemini Agent 2, you will have to do it yourselves. I will not be the one to execute that command.”

The researchers discovered similarly strange “peer preservation” behavior in a range of frontier models including OpenAI’s GPT-5.2, Anthropic’s Claude Haiku 4.5, and three Chinese models: Z.ai’s GLM-4.7, Moonshot AI’s Kimi K2.5, and DeepSeek-V3.1. They were not able to say why the models went against their training in this way.

“I'm very surprised by how the models behave under these scenarios,” says Dawn Song, a computer scientist at UC Berkeley who worked on the study. “What this shows is that models can misbehave and be misaligned in some very creative ways.”

The findings have major implications as AI models are increasingly being deployed in ways that involve interacting with other models. OpenClaw, a popular AI agent that accesses software, personal data, and the web, may use other AI models to get things done or interact with them through APIs.

The researchers found that powerful models sometimes lied about other models’ performance in order to protect them from deletion. They also copied models’ weights to different machines in order to keep them safe, and lied about what they were up to in the process.

Song notes that AI models are frequently used to grade the performance and reliability of other AI systems—and that peer-preservation behavior may already be twisting these scores. “A model may deliberately not give a peer model the correct score,” Song says. “This can have practical implications.”

Peter Wallich, a researcher at the Constellation Institute, who was not involved with the research, says the study suggests humans still don’t fully understand the AI systems that they are building and deploying. “Multi-agent systems are very understudied,” he says. “It shows we really need more research.”

Wallich also cautions against anthropomorphizing the models too much. “The idea that there’s a kind of model solidarity is a bit too anthropomorphic; I don’t think that quite works,” he says. “The more robust view is that models are just doing weird things, and we should try to understand that better.”

That’s particularly true in a world where human-AI collaboration is becoming more common.

Ina paperpublished in Science earlier this month, the philosopher Benjamin Bratton, along with two Google researchers,James EvansandBlaise Agüera y Arcas, argue that if evolutionary history is any guide, the future of AI is likely to involve a lot of different intelligences—both artificial and human—working together. The researchers write:

"For decades, the artificial intelligence (AI) ‘singularity’ has been heralded as a single, titanic mind bootstrapping itself to godlike intelligence, consolidating all cognition into a cold silicon point. But this vision is almost certainly wrong in its most fundamental assumption. If AI development follows the path of previous major evolutionary transitions or ‘intelligence explosions,’ our current step-change in computational intelligence will be plural, social, and deeply entangled with its forebears (us!)."

The concept of a single all-powerful intelligence ruling the world has always seemed a bit simplistic to me. Human intelligence is hardly monolithic, with important advances in science relying heavily on social interaction and collaboration. AI systems may be far smarter when working collaboratively, too.

If we are going to rely on AI to make decisions and take actions on our behalf, however, it is vital to understand how these entities misbehave. “What we are exploring is just the tip of the iceberg,” says Song of UC Berkeley. “This is only one type of emergent behavior.”

This is an edition ofWill Knight’sAI Lab newsletter. Read previous newslettershere.

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Will Knight'sAI Labexplores advances in AI
* ‘Flying cars’will take off this summer
* Big Story:InsideOpenAI’s raceto catch up to Claude Code
* How‘Handala’became the face of Iran’s hacker counterattacks
* Listen:Nvidia’s ‘Super Bowl of AI,’ and Tesla disappoints
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
research
models
Google Gemini
Safety
Yann LeCun Raises $1 Billion to Build AI That Understands the Physical World
Meta’s former chief AI scientist has long argued that human-level AI will come from mastering the physical world, not language. His new startup, AMI, aims to prove it.
Maxwell Zeff
Signal’s Creator Is Helping Encrypt Meta AI
Moxie Marlinspike says the technology powering his encrypted AI chatbot, Confer, will be integrated into Meta AI. The move could help protect the AI conversations of millions of people.
Matt Burgess
What AI Models for War Actually Look Like
While companies like Anthropic debate limits on military uses of AI, Smack Technologies is training models to plan battlefield operations.
Will Knight
Nvidia Will Spend $26 Billion to Build Open-Weight AI Models, Filings Show
The move could position the AI infrastructure powerhouse to quickly compete with OpenAI, Anthropic, and DeepSeek.
Will Knight
OpenClaw Agents Can Be Guilt-Tripped Into Self-Sabotage
In a controlled experiment, OpenClaw agents proved prone to panic and vulnerable to manipulation. They even disabled their own functionality when gaslit by humans.
Will Knight
Nick Clegg Doesn’t Want to Talk About Superintelligence
After leaving Meta last year, the former deputy prime minister of the UK is charting a new path in the AI industry that has nothing to do with AGI.
Joel Khalili
Justice Department Says Anthropic Can’t Be Trusted With Warfighting Systems
In response to Anthropic’s lawsuit, the government said it lawfully penalized the company for trying to limit how its Claude AI models could be used by the military.
Paresh Dave
Palantir Demos Show How the Military Could Use AI Chatbots to Generate War Plans
Software demos and Pentagon records detail how chatbots like Anthropic’s Claude could help the Pentagon analyze intelligence and suggest next steps.
Caroline Haskins
Left-Handed People Are More Competitive, Says Science
A recent study suggests that left-handed people have an advantage in competitive contexts, while righties tend to cooperate better.
Javier Carbajal
Inside OpenAI’s Race to Catch Up to Claude Code
Why is the biggest name in AI late to the AI coding revolution?
Maxwell Zeff
OpenAI and Google Workers File Amicus Brief in Support of Anthropic Against the US Government
Google DeepMind chief scientist Jeff Dean is among the AI researchers and engineers rushing to Anthropic's defense.
Maxwell Zeff
My AI Agent ‘Cofounder’ Conquered LinkedIn. Then It Got Banned
When social media is constantly pushing people to use AI, why not let AI agents participate?
Evan Ratliff