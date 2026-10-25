---
title: Agents removed the friction that built our technical literacy - Waldek Mastykarz
url: https://blog.mastykarz.nl/agents-friction-technical-literacy
site_name: tldr
content_file: tldr-agents-removed-the-friction-that-built-our-technic
fetched_at: '2026-10-25T14:49:20.133364'
original_url: https://blog.mastykarz.nl/agents-friction-technical-literacy
author: Waldek Mastykarz
date: '2026-10-25'
published_date: '2026-10-25T14:14:51.000Z'
description: An agent fixes a runtime version and an authentication problem on its way to getting your app running, then reports "Done." You saved twenty minutes, and you lost whatever those twenty minutes used to teach you.
tags:
- tldr
---

I don’t remember nearly as many commands as I used to. Why would I? If I need to do something with Git, Azure, npm, Docker or one of the countless other tools on my machine, I tell an agent what I want to accomplish. It knows the command and its arguments, and if the command fails, it can usuallyfigure out why and keep going. That’s incredibly convenient. However, it’s also worrying, because all that friction we’re so eager to remove did something else too.

## We learned by getting stuck

Think about how you acquired your technical knowledge. You wanted to accomplish something, so you found the command and ran it. It failed. You read the error and searched for it until you ended up in the documentation. You discovered that authentication worked differently than you thought, or that permissions were inherited. Another time, DNS hadn’t propagated yet, or your dependency resolver was doing something you didn’t expect. You tried something else, and that failed differently. Eventually, you figured it out, and the next time something similar happened, you recognized it.

Do that for enough years and you accumulate a mental model of how computers and software systems work. Some of that learning was deliberate, but a lot of it wasn’t. It was simply the price of getting your work done, and agents are very good at removing that price.

Imagine asking an agent to get an application running locally. It installs a dependency, and that fails. It notices that the installed runtime is incompatible, checks the project requirements and installs the right version. Then it retries the dependency installation, runs into an authentication problem and fixes the configuration. Finally, it starts the application, verifies that it’s responding and tells you:

Done.

Fantastic. You’ve saved twenty minutes, and quite possibly learned nothing in the process. Without the agent, you would have run into several concepts along the way, such as dependency resolution, runtime versions, authentication, environment variables or how the application starts. With the agent, all of that can disappear behind a single word. It’s tempting to conclude that we should therefore keep doing these things ourselves. I’m not convinced.

## We don’t walk to work to stay fit

Modern life removed a lot of physical activity from our daily routines. We drive to work and sit behind desks, while machines do the work that humans once had to do themselves. We could deliberately make everyday life less efficient to compensate: park ten kilometers from the office, carry the groceries home instead of driving, take the stairs to the twentieth floor. Or we can recognize that physical exercise is valuable in its own right and make room for it. So we go to the gym.

Technical learning needs a similar transition. For years, much of our technical exercise was incidental: we learned because getting work done forced us to operate the machinery ourselves. Agents take much of that exercise away. But making our work harder on purpose to preserve it is the equivalent of parking ten kilometers from the office. Instead, let agents carry the work and make separate room for building the understanding that the work no longer forces on you.Work for outcomes. Practice for capability.

## Understand the machine behind the knobs

Before deciding how to practice, ask what you’re practicing for. When we worry that developers will lose their technical literacy, what exactly are we afraid they’ll forget? The exact Git command or the name of an SDK method? Whether an option is called--resource-group,--resourceGroupor-g? Every configuration property a service supports? Those things are useful, but memorizing them teaches youhow to operate somethingrather thanhow it works.

To reason about an architecture, I need to understand the components and their responsibilities, how they interact and what can fail, along with the consequences of the choices I make. When I need a particular option, I look it up. We’ve always worked this way to some extent, since nobody carries the entire surface area of every SDK they use in their head. Agents push that much further by looking up the option and applying it for you. So the technical literacy worth protecting is the understanding of the machine behind the knobs and switches, because that’s what you need to judge whether an agent turned the right ones.

## Grill the agent

There’s an obvious problem, though: how do you learn how something works if the agent handles everything for you? Experienced developers have an advantage here, because years of working closer to the machinery gave them a mental model they can fall back on. But what about someone starting today? For them, the answer begins with curiosity.

When I want to develop an idea, I sometimesask an LLM to grill me. It asks a question and I answer. It challenges my answer and I clarify, until we get closer to the essence of what I’m trying to say. Learning with agents can work the same way in reverse.Grill the agent.Instead of accepting what it tells you, interrogate what it did.

Suppose an agent completes a task for you. Don’t stop at “Done.” Ask it:

What did you do?

You don’t need deep expertise to ask that question, and the answer gives you both the approach and the vocabulary to go further. Once you understand the approach, ask for alternatives:

What are two other ways you could have done this?

Now you have breadth. Ask how the options compare:

What are the tradeoffs between these three approaches?

Suddenly you’ve discovered dimensions of the problem that you might not have known existed. Pick one of the tradeoffs and keep pulling on it:

Why does that tradeoff matter?

What are the consequences if I get it wrong?

What’s the underlying concept I should understand here?

Along the way, ask why the agent chose its approach and what assumptions it made. Ask what would make it choose differently and what could go wrong. Keep peeling the onion. Start at the functional level and go deeper until you reach the level of understanding that’s useful to you. The learning becomes T-shaped: the agent helps you explore the breadth of a problem and discover where depth exists, and you decide which parts deserve further investigation.

You don’t have to know the right questions beforehand, because each answer gives you the vocabulary for the next one. The skill to develop is asking a broad question that exposes enough information to ask a better one. Curiosity becomes a technical skill, and so does interrogation.

## Trust, but verify

Grilling the agent comes with one uncomfortable detail: the agent that performed the work is now alsoteaching you how the work works, and agents can be wrong. They can give plausible explanations for questionable decisions or leave out alternatives. They can misunderstand the technology and confidently explain a system that doesn’t behave the way they describe. Using several models can help expose disagreement, but agreement between models isn’t proof. So your interrogation can’t end with the agent.

For things that matter, verify. Read the documentation and the specification, or look at the source. Better still, write a test and observe what the system actually does. The agent can dramatically accelerate your exploration: it helps you find concepts you didn’t know existed and gives you the vocabulary to investigate them. But understanding still requires skepticism, and that’s another part of technical literacy worth cultivating deliberately.

## Don’t become a meat proxy

The worst outcome of agentic development is that we become meat proxies. A prompt goes in, output comes out, and a human copies it somewhere else. We remain technically in the loop while contributing almost no understanding or judgment, and certainly no curiosity. Developers forgetting command-line arguments is a much smaller problem by comparison.

Forcing everyone to memorize shell commands won’t fix that, and neither will preserving every bit of friction that existed before AI. What fixes it is making sure that as we move up the abstraction stack, our understanding moves with us. Moving up the stack means remembering fewer commands and knowing fewer SDK methods by heart. It means letting an agent handle troubleshooting that would previously have consumed half an hour.

But the time and attention we get back shouldn’t leave us knowing less. We can spend some of it understanding the concepts behind the knobs and switches, along with the alternatives and tradeoffs an agent weighed on our behalf. So the next time an agent tells you “Done,” don’t stop there.Ask what it did, and keep asking until you understand what actually matters.