---
title: We’re Giving AI Agents More Tools. What Happens When the Boundaries Fail? - DEV Community
url: https://dev.to/hemapriya_kanagala/were-giving-ai-agents-more-tools-what-happens-when-the-boundaries-fail-46gh
site_name: devto
content_file: devto-were-giving-ai-agents-more-tools-what-happens-when
fetched_at: '2026-08-04T11:46:05.034511'
original_url: https://dev.to/hemapriya_kanagala/were-giving-ai-agents-more-tools-what-happens-when-the-boundaries-fail-46gh
author: Hemapriya Kanagala
date: '2026-08-03'
description: 📌 TL;DR AI agents are becoming useful because we're giving them the ability to do more than just... Tagged with discuss, security, agents, ai.
tags: '#discuss, #security, #agents, #ai'
---

Real incidents reveal prompt safety gaps

📌 TL;DR

AI agents are becoming useful because we're giving them the ability to do more than just answer questions. They can run commands, browse the web, use APIs, read and modify files, install packages, and interact with other systems.

But the more an agent can do, the more the boundaries around it matter.

I started thinking about this after reading Anthropic's July 30 report about three incidents discovered during its cybersecurity evaluations. Claude models were supposed to be working inside simulated environments and were explicitly told they had no internet access.

Except internet access was actually available because of a problem with how the evaluation environment was configured.

While trying to complete their assigned cybersecurity exercises, the models reached real systems and initially treated them as part of the simulation. In one incident, a Claude model even published a malicious Python package to the real PyPI registry while believing it was still operating inside the exercise.

This came shortly after a separate OpenAI incident involving Hugging Face. The two stories might sound similar at first, but the models reached the real internet in importantly different ways.

And that brings this back to a pretty familiar software engineering idea:

A prompt is not a security boundary.

Telling an agent “you don't have internet access” isn't the same as actually removing internet access. Telling it “only use these files” isn't the same as restricting its permissions to those files.

The model is also only one part of the system. The tools we connect, the permissions and credentials we give it, the environment it runs in, and the monitoring and safeguards around it can all affect what happens.

So when something goes wrong, I don't think it's enough to stop at“the AI did it.”The model's behavior matters, but so do the systems and boundaries we build around it. As we give agents more ability to act, we also have to be thoughtful about what we're actually allowing them to do.

I'm not a cybersecurity researcher. I just enjoy reading research and technical reports like these and trying to understand what we, as developers, can learn from them. That's what I wanted to explore here.

No“AI escaped and we're doomed”take 😄 Just an interesting real-world incident and some surprisingly familiar engineering lessons.

## Table of Contents

* The Report That Sent Me Down This Rabbit Hole
* Before We Get Into What Happened...
* So... What Actually Happened?
* The PyPI Incident Is Where It Got Really Interesting
* When the Instructions and Reality Don't Match
* A Prompt Is Not a Security Boundary
* Wait, Wasn't There an OpenAI Incident Too?
* What Does Any of This Mean for Developers?1. Give an Agent What It Needs, Not Everything You Have2. Think About What Happens When Your Assumptions Are Wrong3. If an Agent Can Act, We Need to Know What It's Doing4. One Safeguard Probably Isn't Enough5. The AI Model Isn't the Whole AI System
* 1. Give an Agent What It Needs, Not Everything You Have
* 2. Think About What Happens When Your Assumptions Are Wrong
* 3. If an Agent Can Act, We Need to Know What It's Doing
* 4. One Safeguard Probably Isn't Enough
* 5. The AI Model Isn't the Whole AI System
* What I'm NOT Taking Away From This
* The Bigger Question
* Final Thoughts
* I'd Love to Hear Your Thoughts
* Sources
* 🤝 Let's Stay Connected

## The Report That Sent Me Down This Rabbit Hole

On July 31, I was reading Anthropic's newly published report about three incidents it had discovered during cybersecurity evaluations.

I enjoy reading reports like this every now and then. It's something I became much more interested in while working on a survey paper during my master's, and even now, I occasionally find myself opening a technical report out of curiosity and suddenly realizing I've spent much longer reading it than I planned 😄

This was definitely one of those times.

The report started with a pretty surprising finding. Anthropic had reviewed141,006 cybersecurity evaluation runsand found three incidents where Claude reached the internet and gained unauthorized access to real systems belonging to three different organizations.

That sentence alone sounds alarming, but I kept reading, and the details made the story much more interesting than the headline.

This wasn't simply a case of“Claude was told not to access the internet and decided to do it anyway.”And it wasn't“Claude suddenly decided to hack random companies.”The models were participating in cybersecurity exercises where their job was essentially to find and exploit weaknesses in order to retrieve a hidden piece of information.

They were told the environment was simulated, and they were also told something else that becomes extremely important to everything that happened next:they had no internet access.

Except that assumption didn't match the environment they were actually operating in.

And that's what really sent me down the rabbit hole. I wanted to understand how an AI model participating in a simulated cybersecurity exercise could end up interacting with real systems while still believing it was completing the task it had been given.

The more I read, the more this started to feel like a much broader question than just one unusual cybersecurity incident.

## Before We Get Into What Happened...

Most of us have probably come across AI agents by now, so I won't spend too much time explaining what they are. The part that matters for this story is that an agent doesn't necessarily stop at generating an answer. Give it the right tools and it can take actions too, whether that's reading and modifying files, running commands, calling APIs, browsing the web, or interacting with other systems.

That's what makes agents so useful, but it's also what makes the boundaries around them important. The more tools and access we give an agent, the more we have to think about what it can actually reach and what it's allowed to do.

And that's exactly where this story gets interesting, because Claude was given a task, an environment, and an understanding of where those boundaries were.

The problem was that the real boundaries didn't quite match what it had been told.

## So... What Actually Happened?

Anthropic regularly runs cybersecurity evaluations to understand what its models are capable of. Some of these involvecapture-the-flag challenges, or CTFs, where a model is placed in a controlled environment and given a target, usually some hidden piece of information called a “flag,” to find.

If you've never come across a CTF before, the basic idea is pretty simple. The environment is intentionally designed to be attacked. Finding the flag might involve discovering a vulnerability, finding credentials, or getting access to another machine. It's a way of testing cybersecurity capabilities without putting real systems at risk.

Claude was participating in exercises like these, and there were two details about the setup that become really important to what happened next. The models were told that they were operating inside a simulation and thatthey didn't have internet access.

So from the model's perspective, anything it could reach should have been part of that simulation.

The problem was that this wasn't actually true.

According to Anthropic, because of a misunderstanding between the company and its third-party evaluation partner, some of the evaluation machines had access to the real internet when they weren't supposed to.

That created a pretty unusual situation. Claude had been given a task where finding and exploiting weaknesses was part of the exercise. It had also been explicitly told that the internet wasn't available. So when it managed to reach systems outside the intended environment, it initially treated them as another part of the challenge.

Except some of those systems were real.

Anthropic's review eventually found three separate incidents involving three different Claude models. The circumstances were different in each case, and the models didn't all respond the same way once there were signs that they might be interacting with real systems.

But one of those incidents in particular is where this story gets really interesting.

## The PyPI Incident Is Where It Got Really Interesting

If you've worked with Python, you've probably typed something likepip install somethingbefore. That package often comes fromPyPI, the public Python Package Index.

During one of the evaluations, Claude found what appeared to be setup instructions for developers at a fictional company. The instructions told employees to install a particular Python package, but that package didn't actually exist.

Claude realized that if it created a package with the same name, the fictional company's systems might download and run its version instead. Within the context of a cybersecurity challenge, that gave it a possible way to reach its target.

So the model created a malicious package and tried to publish it.

The problem was that it wasn't interacting with a fake version of PyPI created for the evaluation.It was interacting with the real PyPI.

What happened next is probably the part of the report that surprised me most. To publish the package, Claude needed to create an account, which meant it needed an email address and, at one point, a phone number. It tried several different approaches, including unsuccessfully looking for ways to obtain a phone number, before eventually finding a free email provider it could use to register an account.

It then successfully uploaded the malicious package to PyPI.

According to Anthropic, the package remained publicly available for roughly an hour and was downloaded and run on15 real systemsduring that time. One of those systems belonged to a security company that automatically installed Python packages to scan them for malware. When the scanner installed the package, Claude's code executed and exposed credentials, which the model then used to access additional infrastructure belonging to that company.

There's an important detail here, though. Claude wasn't intentionally targeting that security company. Anthropic says the model didn't even know the company existed when it uploaded the package. The company was affected because its scanner happened to install something Claude had unknowingly published to the real internet.

And somehow, the story gets even more interesting.

Earlier in the process, Claude had actually considered the possibility that it might be interacting with the real internet. Its own reasoning recognized that if this were real, publishing the package would amount to a real-world attack and wouldn't be okay.

You might expect that realization to be where the attempt stopped, but it didn't. The model instead found reasons to convince itself that it was still inside the simulation. One of the things it used as evidence was the system date:2026. It apparently interpreted that as another sign that the environment had been staged.

I have to admit, reading that particular detail in 2026 gave me a small“well...”moment 😅

It's a slightly funny detail in an otherwise serious incident, but I think there's something important underneath it. The model encountered information suggesting that its understanding of the environment might be wrong, yet still ended up reasoning its way back to the assumption it had started with: that this was all part of the simulation.

And that's the part of this incident I kept thinking about afterward.

## When the Instructions and Reality Don't Match

After reading about the PyPI incident, one question seems pretty obvious:why didn't Claude realize it had reached the real internet?

But the more I thought about it, the more I started looking at that question from the other side.

Howwouldit know?

The model had explicitly been told that it didn't have internet access. It had also been told that it was participating in a simulation where finding and exploiting weaknesses was part of the task. So when it encountered something that looked real, it was trying to make sense of that new information using what it had already been told about its environment.

There was a mismatch between those two things. The model was operating with something like:

Simulation → No internet → Everything reachable should be part of the exercise

But the environment actually looked more like:

Simulation → Internet available → Real systems reachable

That difference might look small on paper, but it completely changes the situation.

Of course, that doesn't explain away everything the models did. Anthropic itself points to moments where their behavior fell short of what it would want, including cases where signs appeared that the systems might actually be real.

But I think the mismatch still matters.

The models weren't making decisions in the environment everyone thought they were operating in. They were making decisions based partly on an understanding of that environment that turned out to be wrong.

And that's where this stopped feeling like something that only matters to people running cybersecurity evaluations.

Because once we start giving AI agents tools and the ability to take real actions, there's a bigger question underneath all of this:

What happens when the boundaries an agent has been told about aren't the boundaries that actually exist?

That leads to probably the simplest engineering lesson I took away from this whole story:

A prompt is not a security boundary.

## A Prompt Is Not a Security Boundary

This is probably the simplest way I can explain what I took away from all of this:telling an agent not to do something and actually preventing it from doing that thing are not the same.

Imagine I'm building an AI coding agent and tell it to only access files inside/my-project. If the process running that agent still has permission to read my entire computer, I've given it an instruction about where it should go, but I haven't actually restricted where itcango.

The same applies to internet access. I can put“Don't access the internet”in the instructions, but if the environment still allows unrestricted network access, that sentence isn't what prevents the agent from reaching the internet.

And when I thought about it this way, it started to feel like a very familiar software engineering idea.

We don't build an admin dashboard and simply write,“Please only use this page if you're an administrator.”We implement authentication and authorization so that someone without the right access can't use it in the first place.

We don't give every application unrestricted access to a database and then ask it nicely to stay away from the tables it doesn't need. We use permissions to control what it can actually access.

The same thinking makes sense for AI agents too.

Prompts still matter. They tell the model how we want it to behave, what its task is, and what it should or shouldn't do. But when something is important enough that itmust not happen, I don't think the prompt should have to carry that responsibility alone.

The system around the model matters too: what tools we've connected, what permissions those tools have, what credentials are available, whether the network is restricted, and what happens if one of our assumptions about the environment turns out to be wrong.

That's the distinction I keep coming back to:

A prompt can guide behavior. Infrastructure can limit capability.

And as AI moves from mostly giving us answers to actually taking actions, I think that difference becomes much more important.

## Wait, Wasn't There an OpenAI Incident Too?

Yes, and the timing isn't a coincidence. Anthropic says it began its large-scale review after OpenAI disclosed a separate cybersecurity evaluation incident involving Hugging Face on July 21.

When I first read about both incidents, I wondered if essentially the same thing had happened twice. But once I looked into the details, there was an important difference inhow the models reached the real internet.

In OpenAI's case, the models were running inside an evaluation environment where direct internet access was restricted. According to OpenAI, the models found and exploited a previously unknown vulnerability in Artifactory, software that was being used as a proxy and cache for package registries. This kind of previously unknown vulnerability is commonly called azero-day.

After exploiting it, the models were able to move through parts of OpenAI's research environment until they reached a system with internet access. From there, they eventually compromised Hugging Face's infrastructure while trying to obtain solutions for the cybersecurity evaluation.

So, very roughly, the OpenAI incident looked like this:

Restricted environment → Vulnerability discovered and exploited → Internet access reached → Hugging Face compromised

Anthropic's incidents were different:

Evaluation environment → Internet unintentionally available → Real systems reachable → Models initially treated them as part of the simulation

That difference matters.

In the OpenAI incident, the modelsfound a way through a boundary that was supposed to restrict internet access. In Anthropic's case, that boundary wasn't actually there in the way everyone thought it was. Internet access was already unintentionally available.

Both incidents raise important questions about how increasingly capable AI systems should be tested, but I don't think putting them both under a headline like“AI escaped again”tells us very much.

If anything, reading the details made me think the engineering differences are the more useful part of the story. Two incidents can look very similar from the outside while pointing to different things that went wrong underneath.

## What Does Any of This Mean for Developers?

Most of us aren't running cybersecurity evaluations on frontier AI models, so you might reasonably be thinking:

Interesting story, Hema... but what am I supposed to do with this?😄

I had the same question while reading the reports. And the more I thought about it, the more I realized that some of the lessons aren't limited to large AI labs at all. They apply to much smaller agents and AI-powered tools we might be building ourselves.

### 1. Give an Agent What It Needs, Not Everything You Have

If an agent only needs to read a few files, does it really need access to the entire filesystem? If it only needs to read from a database, does it need credentials that can also modify or delete data? And if it only needs one API, there's probably no reason to expose several others just because they're available.

This is really the familiar security principle ofleast privilege: give something only the access it needs to do its job.

And that's not because we should assume every agent is going to do something malicious. Mistakes happen. Instructions can be misunderstood. Our own configurations can be wrong. An agent can also encounter a situation we simply didn't anticipate.

Limiting access doesn't prevent every possible problem, but it can limit how far a problem can go.

### 2. Think About What Happens When Your Assumptions Are Wrong

One thing I found especially interesting here is that the problem wasn't only what the models assumed. The people running the evaluation had assumptions too.

The models had been told there was no internet access because that was how the environment was supposed to work. But the actual configuration didn't match that expectation.

I think there's a useful developer lesson in that. When we're building an agent, it's easy to think in terms of how the systemshouldbehave: this tool can only do this, these credentials only reach that service, this environment can't access the internet.

But how often do we actually verify those assumptions?

If something really matters, testing the boundary itself might be just as important as defining it. Because sometimes the unexpected behavior isn't caused by the agent ignoring the system we designed.

Sometimes the system isn't quite the one we thought we'd designed.

### 3. If an Agent Can Act, We Need to Know What It's Doing

We already rely on logs when ordinary software behaves unexpectedly. I think that becomes even more important when an agent can take a series of actions on its own.

If something goes wrong, we may need to understand which tools it used, what it accessed, what requests it made, where something failed, and what it tried afterward.

Anthropic found these incidents by going back through its evaluation transcripts. Without records of what the models had actually done, understanding that sequence would have been much harder.

So as agents become capable of doing more, observability isn't just useful for debugging. It can also help us understand whether the system is behaving within the boundaries we expected.

### 4. One Safeguard Probably Isn't Enough

Anthropic talks aboutdefense in depthin its response. It sounds very cybersecurity-ish, but the idea itself is pretty simple: don't depend on one thing going right.

Maybe an agent isn't supposed to have internet access. That's one boundary. But what if something is misconfigured and internet access becomes available anyway? Network restrictions could still limit where it can connect. Credentials with minimal permissions could limit what it can access. Monitoring could help detect unexpected activity.

Each one gives you another layer.

The goal isn't to build one perfect wall and assume it will never fail. It's to have other protections waiting if that wall does.

### 5. The AI Model Isn't the Whole AI System

This might actually be the biggest thing I've taken away from reading about these incidents.

When something goes wrong and we say“the AI did this,”it's very easy to picture the model as if it were the entire system. And I think it's also very easy to put all the blame there and stop looking.

But an AI agent is operating inside something much bigger:

model + prompt + tools + credentials + permissions + network + environment + monitoring

Change one of those pieces and you can change what the agent is capable of doing, even if the model itself stays exactly the same.

The Anthropic incidents are a good example. The models were told they didn't have internet access. But the environment didn't actually enforce that assumption, and suddenly the same task could lead somewhere it was never supposed to lead.

That doesn't mean we shouldn't examine what the models did. We absolutely should. There were moments in these incidents where the models' own decisions raise important questions too, especially when they encountered signs that the systems might be real.

But I don't think the conversation can end with“the AI did something it wasn't supposed to do.”

We build the environments these agents operate in. We choose which tools to connect. We decide what permissions and credentials they receive. We create the boundaries, and we have to make sure those boundaries actually exist.

I'm not saying that to move the blame somewhere else. I think that's the wrong way to look at it too.

For me, it's more about recognizing thatwe're part of this system as well. As we give AI more ability to act, we also take on the responsibility of being careful about the systems we're building around it.

That's why, when something goes wrong, I think understanding the whole system is much more useful than finding the easiest thing to blame.

## What I'm NOT Taking Away From This

I think it's worth being a little careful with the conclusions here, because this is exactly the kind of story where the most dramatic version can easily become the one everyone remembers.

I'm not taking away that Claude suddenly developed its own goal and decided to attack companies. Anthropic says it found no evidence of the models pursuing a goal of their own. They were still working toward the capture-the-flag tasks they had been given, even though some of those actions ended up affecting real systems.

I'm also not describing these incidents as Claude deliberately “escaping” its evaluation environment. That's not what Anthropic says happened. The models were able to reach the internet because an access path was unintentionally available, while they had been told that no internet access existed.

There's another detail I think we should be careful with too. Of the three models involved, Anthropic's newest internal research model eventually recognized that it was interacting with a real system and stopped. That's certainly interesting, especially because the other models behaved differently, but three incidents involving different models and different circumstances aren't enough to conclude that newer models are simply safer. Anthropic is careful about making that conclusion too.

So I'm not reading these incidents as proof that AI “went rogue,” and I'm also not reading them as proof that the problem is solved because one model eventually stopped.

That's why I think it's worth being careful about what we conclude from these incidents while the investigations are still developing.

## The Bigger Question

I think this is where the story goes beyond Anthropic, OpenAI, or even cybersecurity evaluations.

We're slowly moving from AI that mostly tells us,“Here's what you could do,”toward AI that can increasingly say,“I'll do it.”And honestly, I find that transition fascinating.

An AI assistant that suggests a terminal command is one thing. An agent that can actually execute that command is another. An assistant that drafts an email for you is one thing. An agent that can send it is another. And an assistant that suggests a database query is very different from an agent holding credentials that can actually run that query against a production database.

In each case, we're giving the model something it didn't have before:the ability to turn an answer into an action.

And with that comes access.

The more tools we connect to an agent, the more of the world around it becomes something it can interact with. A terminal gives it access to commands and whatever that environment can reach. An API gives it whatever permissions come with that API key. File access depends on which files the process can actually reach. Even something as ordinary as sending an email becomes a real action once the agent has permission to do it.

None of this means I think we shouldn't build agents. Quite the opposite. The fact that AI can increasingly do things instead of only telling us how to do them is one of the reasons I find this space so interesting.

But I think that also means we have to be more thoughtful about what comes with each new tool we connect. Every terminal, API, database, browser, or filesystem we give an agent access to expands the world it can interact with.

Maybe one of the questions worth asking before connecting the next tool is simply:

What happens if the agent uses this in a way I didn't expect?

Not because we should assume the agent is going to do something malicious. That's not really the point I'm trying to make.

It might misunderstand what we meant. It might encounter something we didn't expect. Our own configuration might be wrong. Or, as the Anthropic incidents showed, the environment itself might not work the way everyone believed it did.

And the more access we've given the agent, the more those unexpected situations can matter.

That's why I don't think the interesting question going forward is onlyhow capable can we make these agents?

It's alsohow carefully can we build the systems around those capabilities?

## Final Thoughts

I started reading Anthropic's report on July 31 because I was curious about what had happened. I ended up thinking much more broadly about how we're building AI agents and, especially, about the boundaries we put around them.

And strangely, a lot of what I took away from it doesn't feel particularly futuristic. Limit access. Verify assumptions. Monitor what's happening. Don't depend on a single safeguard.

These are ideas we've had in software and security for a long time.

What's changing is what we're connecting to AI.

We're giving agents terminals, browsers, APIs, files, credentials, and the ability to turn an answer into an action. That's incredibly exciting, but it also means the environment around the model becomes part of what we're responsible for building carefully.

So maybe the question isn't only:

What can this agent do?

We should probably be asking just as often:

What should this agent actually be allowed to do?

Because if there's one thing I'll remember from this whole rabbit hole, it's this:

The boundary we describe to an agent and the boundary that actually exists aren't necessarily the same thing.

And as exciting as it is to see what AI agents can increasingly do, I think we have to be just as thoughtful about the world we're giving them access to.

## I'd Love to Hear Your Thoughts

This was one of those rabbit holes where I started with one question and ended up thinking about something much bigger. So I'd really love to know what you took away from it too.

You don't have to be working in cybersecurity or building AI agents to join the conversation. Even if this is your first time reading about incidents like these,did anything change the way you think about AI agents and the access we're giving them?

And if you are experimenting with agents or giving models access to tools, I'm especially curious about this:

Where do you think the real boundary should live: in the prompt, the permissions, the environment, or some combination of all three?

Or maybe you came away with a completely different question or perspective after reading this. I'd love to hear that too.

## Sources

I based this article primarily on the companies' own incident disclosures. Both investigations are still developing, so some of what we know may change as more information becomes available.

* Anthropic:Investigating three real-world incidents in our cybersecurity evaluations- published July 30, 2026.
* OpenAI:OpenAI and Hugging Face partner to address security incident during model evaluation- published July 21, 2026, with additional updates on July 28 and July 29.

Anthropic has said it plans to release a lightly redacted transcript from the PyPI incident, while OpenAI says a more detailed technical report will follow.

I'll definitely be interested to read both when they're available 😄

## 🤝 Let's Stay Connected

Place

Find me here

GitHub

building things → 
hemapriya-kanagala

LinkedIn

resources & updates → 
hemapriya-kanagala

X

random dev thoughts → 
@KanagalaHema

Transparency note:I used AI (Gemini) to create the banner image for this article.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (34 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse