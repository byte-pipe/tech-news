---
title: Netflix, Meta, IBM speakers discuss AI and their workdays • The Register
url: https://www.theregister.com/2026/04/04/all_things_ai_conference/
site_name: tldr
content_file: tldr-netflix-meta-ibm-speakers-discuss-ai-and-their-wor
fetched_at: '2026-04-10T11:22:02.105247'
original_url: https://www.theregister.com/2026/04/04/all_things_ai_conference/
date: '2026-04-10'
description: AI will make anyone a 10x programmer, but with 10x the cleanup (3 minute read)
tags:
- tldr
---

#### AI + ML

# AI will make anyone a 10x programmer, but with 10x the cleanup



## Agents to check the work of the agents

All Things AIAI is easy to use, but not quite as easy as just barking "Alexa! Make me an e-commerce site." And, no, adding "DON'T HALLUCINATE" to the instruction loop won't help.

More to the point, optimal AI results favor the well-fortified agent, according to speakers from IBM, Meta, and Netflix – among others – at theAll Things AIconference in Durham, North Carolina.

The more you want AI to do your bidding, the more preparatory chores you'll need to do, they advised.

Numerous talks evoked theJevons Paradox, where the more efficient a resource becomes, the more it's used. The paradox is often used to explain why AI won't take everyone's jobs. In fact, it will create more jobs, the argument goes.

Currently, AI is certainly creating more work for its users, requiring time to prepare context and check outcomes. Claude will make anyone a 10x programmer, but they'll need to clean up 10x the results.

Or, in the most apocalyptic terms, before the singularity can enslave humankind as energy pods à la The Matrix, it will require some assistance from us meat sacks to get around.

### The sorcerer's apprentice

How is AI keeping the folks at Netflix busy? In a talk, Netflix UI architectBen Ilegboduexplained how as soon as you create an agent to automate some task, you will need a second agent to evaluate the work done.

Ilegbodu sometimes even breaks the job into multiple agents that specialize in different parts of the code review. He calls this approach "adversarial code review."

Oh, you'll also need a third agent to orchestrate the actions between the first two, he said.

Ilegbodu's workday is the Jevons Paradox incarnate. Once he sets off one agent to implement some new feature, he tasks another agent to do the preliminary work for the next task he has in mind. In effect, he is "parallelizing himself so the work is always happening."

AI has allowed Ilegbodu to code in languages he doesn't yet know, such as Python, Bash, and Groovy.

But this context switching can get wearisome, he admitted. "At the end of the day, I'm actually kind of tired, because effectively, I spent the whole day talking to something."

### The insatiable intern

Many coders think about AI like an eager junior developer on the team: enthusiastic but naive. But unlike a junior dev, an AI won't "get overwhelmed," said Meta Developer AdvocateJustin Jeffress, in his talk.

You can just keep shoveling more information to the AI, and it will take it all in (for as many tokens as you can afford).

Such bottomless hunger leads to what Jeffress called "context rot."

"Over time, as you interact with your AI agent, the more stuff it has to calculate to provide an answer, the more there is vying for its attention and the less likely it's going to do the right thing," he said.

Vague instructions lead to diffuse results, he told the audience. Clearly thinking about what information you are giving to the agent is the work of context engineering, which, in the short time of agentic AI, has become an art form, if not quite a proper discipline yet.

With context engineering, "you're building a set of rules, tools, skills and other things that the AI agent at its moment of need can refer to in order to solve the problem," he said. He even recommended going one step further with "prompt chaining," or listing the specific tasks it needs to do step by step. More work at the beginning means less to worry about during runtime, allowing the developer to nip away for a pint.

Just kidding. It gives them time to refine the process even further by running multiple agents in parallel. Become the conductor of your own orchestra of agents, Jeffress said. Be sure also to create a markdown file to track progress to help keep the agent from forgetting its mission.

Jeffress noted that AI can usually do 80 percent of a given job, leaving the last 20 percent to be finished by a human. When Jeffress tackled the remaining 20 percent of the work, he found that 80 percent of that work could be done by the bots. And so on, like some fractalPareto principleof never-ending cleanup duties.

### Wishful prompting

The fact that the AI doesn't do exactly what you want it to do is not a problem with the AI. It's a problem with your lack of "decomposition" skills, posited Luis Lastras, IBM director of language and multimodal technologies, in his talk.

Wishful prompting is just typing "I must insist, do not hallucinate. My career depends on it, please, please, please." It's like casting a spell and hoping it'll work, he said.

Instead, developers should be thinking about how to break the work up into smaller, more bite-sized portions for the agent.

* AI recruiting biz Mercor says it was 'one of thousands' hit in LiteLLM supply-chain attack
* Google's TurboQuant saves memory, but won't save us from DRAM-pricing hell
* 'Uncle Larry's biggest fan' cut by email in early morning Oracle layoff spree
* Claude Code bypasses safety rule if given too many commands

This sort of "decomposition" is in fact Engineering 101, he said. It is "the art of taking a very complex system, identifying what are the key piece parts, modularizing them, and then designing those things, and even assigning specialists to design those pieces."

When you build your agent, don't just randomly throw information at the LLM, but define specific functions to help the agent execute the task. IBM's recently releasedmellea.aiis an open source library of what Lastras calls key patterns – functions that give LLMs specific Python-encoded instructions. They can be used to add requirements to LLM calls, detect harmful outputs, structure outputs in schemas, and more.

Big Blue is also working on the capability for agents to switch LLMs for specialized tasks, or "switch brains," Lastras said. In its research, IBM has found that a smaller, domain-specific model, given more time for inference, will outperform larger models.

### Pay the prep tax

"Implicit assumptions are tech debt," further explained Justin Chau, a senior developer at Intuit. What is obvious to us may not be obvious to the machine. "We have to be very, very specific in what we want as an outcome."

One piece of advice from Chau: give your agents constraints, not instructions. An LLM will disregard an instruction if it finds what it assumes is a better way to complete the task. Constraints are hard nos and more difficult for the AI brain to disregard. If you tell the agent that under no circumstances should it use HTML, then it will honor that request.

But even stronger than constraints is the lack of permissions. "If I don't give it access to GitHub, I know for sure it will never touch GitHub," Chau said.

Aficionados ofThe Hitchhiker's Guide to the Galaxywill remember the paradox of "Deep Thought," the world's most powerful computer. Like AI itself, Deep Thought was built to deliver the answer to Life, Universe, and Everything. But after centuries of calculation, it only delivered the inscrutable answer (42), and the human race then needed an  even larger computer just to figure out what the actual question was.

Perhaps, with AI, we find ourselves in Adams' world. Far from doing all the work for us, AI sets us down a path of endless preparation. ®



Get our

Tech Resources

Share

#### More about

* AI
* IBM
* Meta

More like these

×

### More about

* AI
* IBM
* Meta
* Netflix
* Tech Jobs

### Narrower topics

* AIOps
* AIX
* DeepSeek
* Facebook
* Gemini
* Google AI
* GPT-3
* GPT-4
* IBM Power
* IBM Watson
* IBM Z
* i OS
* Large Language Model
* Machine Learning
* MCubed
* Neural Networks
* NLP
* Open Compute Project
* OS/2
* Retrieval Augmented Generation
* Star Wars
* Tensor Processing Unit
* TOPS
* WhatsApp

### Broader topics

* Andrew McCollum
* Chris Hughes
* Dustin Moskovitz
* Eduardo Saverin
* Marc Randolph
* Mark Zuckerberg
* Reed Hastings
* Self-driving Car

#### More about

Share

#### More about

* AI
* IBM
* Meta

More like these

×

### More about

* AI
* IBM
* Meta
* Netflix
* Tech Jobs

### Narrower topics

* AIOps
* AIX
* DeepSeek
* Facebook
* Gemini
* Google AI
* GPT-3
* GPT-4
* IBM Power
* IBM Watson
* IBM Z
* i OS
* Large Language Model
* Machine Learning
* MCubed
* Neural Networks
* NLP
* Open Compute Project
* OS/2
* Retrieval Augmented Generation
* Star Wars
* Tensor Processing Unit
* TOPS
* WhatsApp

### Broader topics

* Andrew McCollum
* Chris Hughes
* Dustin Moskovitz
* Eduardo Saverin
* Marc Randolph
* Mark Zuckerberg
* Reed Hastings
* Self-driving Car

#### TIP US OFF

Send us news
