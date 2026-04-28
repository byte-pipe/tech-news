---
title: AI Is Becoming Infrastructure - DEV Community
url: https://dev.to/jonoherrington/ai-is-becoming-infrastructure-47pd
site_name: devto
content_file: devto-ai-is-becoming-infrastructure-dev-community
fetched_at: '2026-04-28T12:26:17.744670'
original_url: https://dev.to/jonoherrington/ai-is-becoming-infrastructure-47pd
author: Jono Herrington
date: '2026-04-25'
description: We stopped talking about DevOps. Now everything uses it. AI is slowly crossing that same threshold. Tagged with ai, leadership.
tags: '#ai, #leadership'
---

I was talking to a tech lead a couple of months ago, over drinks. Someone who's been shipping production code for over twenty years. I asked him, almost as an afterthought, when was the last time he wrote a line of code without AI assistance.

He paused. Actually paused. "Over a year," he said. "Maybe longer."

The number wasn't the surprising part. It was the realization in his voice. He hadn't noticed the transition. It just ... happened.

I've been thinking about that conversation ever since. Not because it's unusual, but because it's becoming the norm. The principal engineers I talk to, the ones running platforms at scale, are quietly shifting how they work. Not announcing it. Not debating it. Just ... doing it.

This is how infrastructure arrives. Not with a press release. With a shrug.

This is how infrastructure arrives. Not with a press release. With a shrug.

## The Pattern We Keep Repeating

I remember when Docker was controversial.

Two senior engineers I worked with got into an actual argument about it. Virtual machines versus containers. Resource overhead versus isolation guarantees. One of them was convinced Docker was a toy for startups. The other thought VMs were dinosaurs.

I didn't understand the intensity at the time. I was too busy playing with the new tool to notice the religious war forming around it. But looking back, I see what was happening. People were trying to apply Docker in places where it didn't fit yet. Companies with three engineers treating containerization like they were Google. The tool was right, but the context was wrong.

Then CI/CD was a "nice to have." Then Kubernetes was "overkill." Every infrastructure shift starts as controversy before it becomes furniture.

The pattern is consistent. First comes the debate ... should we use this? Then comes the adoption ... how do we use this? Then, eventually, comes the invisibility ... we use this.

We're somewhere between adoption and invisibility now.

## The Christmas Tree Problem

Don't get me wrong. AI is not fully infrastructure yet.

Look at Claude's status page on any given Tuesday. Green dots, yellow dots, red dots. Systems failing, recovering, failing again. It's less like reliable plumbing and more like a Christmas tree lighting up in sequence. We're failing, but we're failing fast. We're learning in public at scale.

The flakiness is part of the transition. Early CI/CD pipelines broke constantly. Early container orchestration ate memory and crashed nodes. Infrastructure doesn't arrive fully formed. It arrives with bruises.

But here's what I'm noticing. The conversations are changing.

A VP at a lifestyle brand told me his engineering teams are still asking ... "Should we use AI?" Three months ago, it became ... "How do we govern AI?" Now I'm hearing ... "How do we orchestrate agents through our existing pipeline?"

The question moved from permission to plumbing. That's the signal.

The question moved from permission to plumbing. That's the signal.

## What Infrastructure Actually Looks Like

Infrastructure has a specific quality ... you stop talking about it.

Nobody holds meetings about DNS. Nobody writes strategy documents about load balancers. These things just ... are. They're assumed. They're the medium, not the message.

AI is getting there. Not because the tools are perfect. Because the workflows are embedding.

On my team, agents are part of the SDLC now. Not alongside it. Inside it. Code reviews don't separate "AI-assisted" from "manual" anymore. They review the output. Deployment pipelines don't ask who wrote the code. They validate that it meets standards. The distinction between "using AI" and "not using AI" is becoming as irrelevant as "using an IDE" versus "using a text editor."

It's not a specific workflow. It's all the workflows. Not a specific integration point. All the integration points.

This is what people miss when they ask ... "Is AI ready for production?" The question assumes AI is a thing you adopt or don't adopt. But infrastructure doesn't work that way. You don't adopt plumbing. You build houses, and the plumbing is just ... there.

## The FOMO Trap

There's a counter-narrative I need to address. Every infrastructure shift creates this tension.

Large companies need orchestration at scale. They have thousands of services, complex dependency graphs, teams that can't possibly understand every system they touch. Kubernetes makes sense for them.

Smaller companies see the success stories and want the same. They have twelve engineers and three services, but they're standing up a full Kubernetes cluster because ... "that's what the big players do." They're applying infrastructure to problems that don't need it yet.

AI has the same trap. I see teams with straightforward CRUD applications trying to build agent orchestration frameworks. I see companies with simple deployment pipelines adding complexity they can't maintain because "AI is the future."

The future arrives unevenly. Not every team needs agents orchestrated through their pipeline. Not every problem benefits from AI automation. The infrastructure shift is real, but that doesn't mean you should front-run it.

Know your context. Know your scale. Know what problem you're actually solving.

## Six Months From Now

I'll make a prediction I'm reasonably confident about.

Six months from now, asking an engineer if they "use AI" will feel as strange as asking if they "use Git." The question assumes a choice that no longer exists as a meaningful distinction.

The teams that thrive won't be the ones with the best AI policies. They'll be the ones where AI has become invisible. Where agents run through pipelines without fanfare. Where the conversation shifted from "should we" to ... "how do we make this reliable."

The revolution isn't coming. It's quietly becoming the status quo.

Blockchain faded because it never became infrastructure. It stayed specialized, stayed controversial, stayed a solution looking for problems that fit it. Every use case felt forced because the infrastructure never integrated.

AI is different. It's integrating. Messily, imperfectly, with status pages that look like Christmas trees. But integrating nonetheless.

We're not fully there. But I can see the transition from here. I've watched it happen enough times to recognize the pattern.

Infrastructure doesn't make headlines. It just enables everything that does.

One email a week from The Builder's Leader. The frameworks, the blind spots, and the conversations most leaders avoid.Subscribe for free.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse