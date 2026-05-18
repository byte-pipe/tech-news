---
title: AI Didn't Make Software Engineering Easier. It Made the Hard Parts Harder. - DEV Community
url: https://dev.to/iampraveen/ai-didnt-make-software-engineering-easier-it-made-the-hard-parts-harder-39n4
site_name: devto
content_file: devto-ai-didnt-make-software-engineering-easier-it-made
fetched_at: '2026-05-18T12:11:41.982770'
original_url: https://dev.to/iampraveen/ai-didnt-make-software-engineering-easier-it-made-the-hard-parts-harder-39n4
author: Praveen Rajamani
date: '2026-05-14'
description: When I started using AI tools seriously across my side projects, I expected the work to get easier.... Tagged with discuss, ai, webdev, career.
tags: '#discuss, #ai, #webdev, #career'
---

The loss of low-intensity recovery time

When I started using AI tools seriously across my side projects, I expected the work to get easier. AI handles the boilerplate, I focus on the interesting parts. That was the promise.

It didn't get easier. The interesting parts got harder, more frequent, and more exhausting.

I am not alone in this. AGoogle Staff Engineer recently went viral for leaving the company- not for pay, not for perks, but because the work had become rushed and less meaningful. AI was being pushed into places it did not belong. He was getting paged at 2am. He wrote:"I don't want to be just another execution arm for someone else."

If this is happening at Google - one of the most technically capable organisations on the planet - it is worth asking what AI is actually doing to software engineering. Not in the press releases. In practice.

Here is what I think is really going on.

## The job used to be 80% execution, 20% thinking

For most of software engineering's history, the job broke down roughly like this:

The 80% - Execution

* Writing boilerplate code
* Fixing repetitive bugs
* Moving tickets and updating docs
* Setting up configs and environments
* Writing tests for known behaviour

The 20% - Deep Thinking

* Understanding the real problem
* Designing systems under constraints
* Debugging edge cases nobody predicted
* Making trade-offs with incomplete information
* Knowing what not to build

The 80% was the grunt work. Necessary, but learnable. The 20% was where experience actually mattered - where a senior engineer earned their title not by typing faster but by thinking clearer.

## AI ate the 80%. Now the 20% is the whole job.

Tools like Claude Code, Cursor, and GitHub Copilot are genuinely excellent at the execution layer. Boilerplate? Gone. Standard CRUD endpoints? Done in seconds. Repetitive tests? Generated before you finish your coffee.

The narrative was: this is great news. Engineers freed from boring work can focus on interesting problems.

And in one sense, that is true. But here is what nobody said out loud:

The 20% was hard precisely because it required sustained, deep focus. Now engineers are expected to live there permanently - and the human brain was not built for that.

The 20% has become the new 80%. And it is exhausting in a completely different way than the old 80% ever was.

Writing boilerplate for three hours is tedious - but your brain recovers. Spending three hours designing a distributed system's failure modes, making architectural trade-offs, and debugging a race condition that only appears under specific load - that is a different kind of tired. And AI is not reducing how often you have to do it. It is increasing it.

## Nobody is talking about the human context window

There is a conversation happening constantly in the AI world about context windows. How many tokens can the model hold? How do we optimise retrieval? How do we make sure the model has the right information at the right time?

It is a completely valid engineering problem. But there is another context window nobody is talking about.

⚠️ The human engineer's context window is not growing. It is the same brain it always was - now expected to hold more architectural complexity, make faster decisions under uncertainty, and context-switch between systems more frequently than ever before. Unlike the model, you cannot just upgrade to a longer context. You cannot add more RAM to your prefrontal cortex.

The Google engineer described being paged at 2am, unable to go back to sleep until 5-6am. That is not a productivity problem. That is a cognitive load problem. And it is becoming the norm, not the exception.

## I feel this every single day

I am not speaking theoretically. I work with these tools daily across my five side projects.

The productivity gains are real - I ship things faster than I ever have. But the cognitive load is also higher than it has ever been. Every hour I save on execution goes straight back into harder thinking. Last week I spent a full afternoon on a single architectural decision about how to handle shared state across five products in my monorepo. That decision used to take days because the execution work around it gave me natural thinking time. Now the execution is instant - and the thinking time has to be deliberately carved out or it simply does not happen.

I am not writing less code. I am making more decisions. And decisions are the expensive part.

## What this means practically

Protect your deep work time more than ever.When AI handles the shallow work, shallow interruptions become proportionally more damaging. A Slack notification that cost you ten minutes before now costs you an architectural decision. I now block two hours every morning before I open anything AI-related.

Get comfortable saying "I need to think about this."The speed AI enables creates pressure to decide faster. Resist it. Treating "let me think about this properly" as a professional response, not an admission of slowness, is one of the most underrated skills right now.

Treat cognitive recovery as part of the job.The old 80% gave your brain natural rest - switching from deep thinking to routine execution was recovery in disguise. That rest is gone. Deliberately ending deep work sessions with something low-stakes makes a real difference.

Know when not to use AI.Sometimes writing code slowly is what helps you understand the system. I once let AI generate an entire data-fetching layer for one of my products. It looked clean, it passed my quick review, and I shipped it. Three weeks later I hit a caching bug I could not debug - because I had never actually understood how the layer worked. I spent two days fixing something that would have taken two hours if I had written it myself. The comprehension debt is real and it shows up at the worst time.

## The honest question

The Google engineer said the work had become rushed and less meaningful. I do not think AI made it less meaningful - but the pace it enables can make it feel that way if you are not careful.

And here is the question I keep coming back to: the 20% that is left - system design, trade-offs, debugging under uncertainty, knowing what not to build - this used to take years to develop. Junior engineers built it gradually, on top of the foundation the 80% of execution work gave them. That foundation is now disappearing fast.

AI is not replacing engineers. It is compressing the timeline of everything an engineer has to do. Whether that is a gift or a burden depends entirely on how deliberately you manage what is left.

Are you finding the work more demanding since AI tools arrived, or genuinely easier? And what is happening to the junior engineers on your team - are they getting the foundation they need, or being thrown into the deep end before they are ready?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (32 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse