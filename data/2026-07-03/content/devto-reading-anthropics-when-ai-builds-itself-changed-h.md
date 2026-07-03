---
title: Reading Anthropic's "When AI Builds Itself" Changed How I Think About AI and Software Engineering - DEV Community
url: https://dev.to/hemapriya_kanagala/reading-anthropics-when-ai-builds-itself-changed-how-i-think-about-ai-and-software-engineering-3eh
site_name: devto
content_file: devto-reading-anthropics-when-ai-builds-itself-changed-h
fetched_at: '2026-07-03T11:49:43.477479'
original_url: https://dev.to/hemapriya_kanagala/reading-anthropics-when-ai-builds-itself-changed-how-i-think-about-ai-and-software-engineering-3eh
author: Hemapriya Kanagala
date: '2026-06-30'
description: TL;DR Anthropic recently published When AI Builds Itself, an essay explaining how AI is... Tagged with discuss, ai, developers, softwareengineering.
tags: '#discuss, #ai, #developers, #softwareengineering'
---

80% of Anthropic's code is now AI-written

TL;DR

Anthropic recently publishedWhen AI Builds Itself, an essay explaining how AI is increasingly helping build the next generation of AI. Today, more than 80% of Anthropic's production code is written by Claude, and engineers are shipping around eight times more code than they were in 2024.

I went into the essay carrying the same quiet anxiety I think many developers have right now. I came out feeling less scared.

Not because the numbers are small. They aren't.

It's because after reading the entire essay, I realized the thing AI is getting better at is not the thing that makes developers valuable. Execution is getting faster and cheaper. Judgment, the ability to decide what's worth building, whether a result actually makes sense, and when to question an answer instead of accepting it, is not. That distinction gets lost in most of the conversations happening online, and once you see it, the whole essay reads differently.

If you'd like to read the original essay before reading my thoughts, here's the link:When AI Builds Itself by Anthropic.

## Table of Contents

* I Want to Start With Something Honest
* How It Started and How Fast It Moved
* The Numbers, Because They Matter
* The Difference Between Execution and Judgment
* What I Think About This as Someone Early in My Career
* Three Ways This Could GoThe trend slows downHumans stay in the loop, but the way we work changesRecursive self-improvement
* The trend slows down
* Humans stay in the loop, but the way we work changes
* Recursive self-improvement
* My Honest Takeaway
* I Would Love to Hear Your Thoughts
* References
* 🤝 Stay in Touch

## I Want to Start With Something Honest

Over the last few months, I have probably read hundreds of posts about AI replacing developers.

Some were thoughtful. Some were obviously written just to get clicks. But after a while, they all started blending together, and I noticed something interesting.

The loudest opinions almost never came from people discussing the original source material. They came from summaries of summaries, screenshots of tweets, or headlines that focused on a single statistic while leaving out everything around it.

So when Anthropic publishedWhen AI Builds Itself, I decided to read the whole thing instead of waiting for someone else to explain it.

I expected to come away more worried. Instead, I came away thinking the conversation online had become much more dramatic than the essay itself.

The numbers are real. The pace is real. The changes happening inside companies like Anthropic are real. None of that should be ignored. That doesn't mean the essay is reassuring on its own. Some of the numbers are genuinely astonishing. But the overall picture is much more nuanced than the internet often makes it sound.

This isn't meant to summarize every page. It's simply how reading the essay changed the way I think about the conversation around AI and software engineering.

One piece of context is worth mentioning before getting into it. Anthropic didn't publish this essay as a prediction about what software engineering might look like someday. They wrote it to explain what they were already seeing inside their own engineering and research teams as AI became a much larger part of their development process. That distinction matters. The essay is mostly describing changes they have already observed, not changes they simply hope will happen.

## How It Started and How Fast It Moved

One thing I wasn't expecting was how little time the essay spends making predictions about the future. Instead, it starts by looking backward.

The authors walk through how AI gradually became part of Anthropic's own engineering workflow, and that context matters because it changes the way you read everything that comes after it. The essay isn't saying "this is what might happen one day." It's saying "this is how we got here."

In the early years, around 2021 to 2023, things looked much like they would at any other software company. Engineers wrote code, reviewed pull requests, fixed bugs, and made technical decisions. AI wasn't really part of the development process yet.

Then it started helping with smaller tasks. At first, it looked a lot like how many of us use AI today. Generate a function. Explain a piece of code. Suggest a refactor. The engineer was still driving every step, while AI acted more like another tool sitting beside the editor.

Around 2025, that relationship began to change. Instead of only suggesting code, Claude started handling much larger parts of the workflow. It could write files, run them, inspect the output, fix errors, and repeat that cycle several times before a person needed to step in again. The role of the engineer wasn't disappearing, but the amount of hands-on implementation they needed to do was already changing.

By 2026, according to the essay, those workflows had become even more autonomous. AI agents were capable of working for much longer periods of time and, in some cases, coordinating work with other agents.

One example from the essay makes that progression much easier to picture. A routine software upgrade unexpectedly caused tens of thousands of AI training jobs to fail. An engineer gave Claude access to the environment along with some context about the problem. Within roughly two hours, Claude identified an obscure configuration flag that was responsible for the failures, verified the fix, and resolved the issue. According to the authors, the same investigation would likely have taken an experienced engineer two or three days.

Stories like that are impressive on their own, but they're still just one example. What convinced me was that the essay backs them up with data. The numbers suggest this wasn't a one-off success but part of a much broader shift inside the company.

## The Numbers, Because They Matter

Before talking about what all of this means, it's worth looking at the numbers themselves. They're easy to exaggerate. They're also easy to dismiss. Neither reaction is particularly helpful.

The headline statistic is the one that has probably already made its way around social media. As of May 2026, Anthropic says that more than 80% of the code merged into its production codebase was authored by Claude. Before Claude Code launched in early 2025, that figure was only in the low single digits.

The effect shows up in productivity too. Engineers are now merging roughly eight times more code than they were in 2024. According to the essay, that happened in two noticeable jumps. The first came when Claude moved beyond simply suggesting code and started running it. The second happened when AI agents became capable of working autonomously over much longer periods.

The research side tells a similar story. Anthropic shared results from an internal survey of around 130 researchers. The median response was that people felt they were producing roughly four times as much output when using AI compared to working without it.

The capability benchmarks have also moved quickly. One benchmark measures whether an AI system can successfully reproduce the results of published research papers. Success rates reportedly increased from around 20% in 2024 to nearly saturating the benchmark only fifteen months later. Another measure estimates how long AI can reliably complete real-world tasks on its own, and according to the essay, that window has been doubling roughly every four months, growing from tasks that took only a few minutes to tasks lasting around twelve hours.

Those numbers are impressive. What gave me more confidence in them was how openly the authors discussed their limitations. They repeatedly point out the gaps in their own measurements. Lines of code are an imperfect productivity metric. Survey responses can overestimate real productivity gains. Benchmarks don't always capture what happens in real engineering work.

That actually made the data more convincing. It felt less like marketing and more like a team trying to explain what they're genuinely seeing inside their own organization.

## The Difference Between Execution and Judgment

The most important part of the essay comes after all the numbers. After reading through them, I found myself asking a much simpler question.

If Claude is writing most of the code, what are the engineers doing?

The answer, at least from how I read the essay, is that the work developers do isn't disappearing. It's changing.

Claude has become exceptionally good at execution. Give it a clearly defined task, enough context, and the right tools, and it can move through implementation remarkably quickly. It can write code, run experiments, debug issues, test different approaches, and iterate far faster than a person could on repetitive engineering work.

But software engineering has never been only about writing code.

Someone still has to decide which problems are worth solving. Someone has to recognize when an experiment is answering the wrong question, even if it technically succeeds. Someone has to look at a result that seems correct and ask whether it actually makes sense within the larger system. Those decisions are much harder to measure than lines of code or benchmark scores, but the essay suggests they remain an important part of where engineers create value.

The authors even tried to measure part of this. They looked at real research sessions where a human made a decision that later turned out to be inefficient or simply wrong. They then showed Claude everything up to that point and asked what it would do next. Their best model improved from choosing the better next step about 51% of the time in late 2025 to around 64% only a few months later.

That is meaningful progress. At the same time, it also means the model was still not choosing the better direction in every situation. On more open-ended decisions, there is still a noticeable gap.

One comparison in the essay helped put that into perspective. The authors describe how responsibilities change as engineers gain experience. Early in a career, much of the work involves implementing tasks that someone else has already defined. With experience comes more responsibility for deciding how those tasks should be approached, and eventually which problems deserve attention in the first place.

I don't think that comparison means AI is simply replacing junior engineers while senior engineers stay untouched. Software engineering doesn't work that neatly, and neither does AI. What it suggests is that as implementation becomes easier, the skills around understanding systems, evaluating trade-offs, reviewing work, and making good decisions become even more valuable.

That ended up being my biggest takeaway from the essay.

I don't think the discussion is really about whether developers become unnecessary. It's about how the balance of the job changes as one part of software engineering becomes dramatically faster. That's a much more useful way to think about what's happening than reducing the conversation to "AI writes most of the code."

## What I Think About This as Someone Early in My Career

I know a lot of people around me who are genuinely worried about AI. Sometimes that worry comes from social media, sometimes from conference talks, and sometimes simply from seeing how quickly these tools are improving. When you read that more than 80% of the production code inside one of the world's leading AI companies is now written by AI, it is difficult not to wonder where that leaves everyone else.

I have had those thoughts too. Reading the essay did not make those questions disappear, but it did change the way I think about them.

The biggest difference for me was that I stopped focusing on the number itself. 80 percent sounds enormous until you start asking what that eighty percent actually represents. The essay made me realize I had been measuring software engineering mostly by the amount of code being written, when in reality some of the most valuable work happens long before anyone opens an editor. That shift in perspective made the essay feel much less like a story about replacement and much more like a story about changing workflows.

The more I thought about that, the more it reminded me why we spend so much time learning computer science fundamentals. When you are studying operating systems, networking, databases, algorithms, or distributed systems, it is easy to wonder when you will ever use some of those ideas. They can feel abstract compared to building an application or shipping a feature. But those subjects are not only teaching syntax or APIs. They teach you how to reason about systems. They teach you how to think about trade-offs, understand complexity, identify bottlenecks, and explain why something behaves the way it does. Those skills become more valuable as implementation becomes easier, because they are the skills that help you evaluate whether the implementation is actually correct.

That was the point where my perspective really changed. The fear that developers are being replaced often comes from imagining that writing code is the entire job. Software engineering has never really worked that way. Writing code is important, but so is understanding the problem, designing the system, reviewing solutions, communicating with other engineers, and making decisions when there is no obvious answer.

I am still early in my career, and I know people with much more experience will have different perspectives on this. That is perfectly reasonable. This is simply the conclusion I reached after reading the essay carefully instead of reacting to the headlines surrounding it.

## Three Ways This Could Go

The essay avoids something I see a lot in AI discussions. The internet often talks about AI as though there are only two possibilities: either everything changes overnight, or nothing really changes at all. The essay takes a much more measured approach. It lays out several possible directions and is honest that nobody knows with certainty which one we are heading toward.

### The trend slows down

The first possibility is that today's rapid progress eventually begins to slow. Every technology reaches limits somewhere, whether they come from hardware, energy, data, research challenges, or simply the fact that the remaining problems become much harder to solve. Anthropic acknowledges that possibility, but based on the evidence they currently have, they do not think they are seeing those limits yet. Across the different capability measurements they track, the curves are still moving in the same direction. That does not mean progress continues forever at the same pace. It simply means they have not yet seen convincing signs that the improvements are flattening out.

### Humans stay in the loop, but the way we work changes

This is the scenario that felt the most believable to me, partly because it doesn't require a dramatic leap from where we already are today. The essay doesn't argue that developers suddenly disappear or that AI takes over software engineering overnight. It describes a future where AI gradually becomes a bigger part of the workflow while people continue making the decisions that require context, experience, and responsibility.

Over the last couple of years, AI has become another tool in many developers' workflows. We use it to explain unfamiliar code, write tests, generate boilerplate, debug issues, or help us think through a problem from a different angle. None of that has removed the need for developers. If anything, it has changed where we spend our time. We've seen this kind of shift before too. High-level programming languages didn't eliminate programmers, they just moved the work up a level. AI handling more of the repetitive implementation work looks like the same kind of shift, not a different one.

### Recursive self-improvement

The final possibility is the one that attracts the most attention. This is the idea that AI eventually becomes capable of contributing so much to AI research that each new generation helps create an even better one with very little human involvement. Progress starts depending less on human research effort and more on available compute, infrastructure, and resources.

The essay discusses this possibility seriously, but it is careful not to present it as an inevitable outcome. There are still many unknowns, and the authors openly acknowledge that they do not know when, or even if, this point is reached. I think that honesty makes the essay much more credible. It is easy to write bold predictions about technology. It is much harder to admit where uncertainty still exists.

## My Honest Takeaway

When I started readingWhen AI Builds Itself, I thought I was trying to answer one question. Is AI really replacing developers?

By the time I reached the end of the essay, I realized I had started asking a completely different question instead. How is software engineering changing as AI becomes part of the development process itself?

Those are very different conversations. One is mostly driven by fear. The other is driven by curiosity. That shift in perspective is probably the biggest thing I took away from reading the essay.

The numbers Anthropic shares are real, and they are difficult to ignore. More than 80% of their production code is now written by Claude. Engineers are shipping significantly more code than they were only a couple of years ago. AI systems are becoming capable of working independently for much longer periods of time. None of that feels like hype.

But neither does the essay read like the internet often talks about it. Throughout the article, the authors repeatedly acknowledge uncertainty. They talk about the limitations of their own measurements. They discuss multiple possible futures instead of presenting one inevitable outcome. They are surprisingly careful about separating what they have observed from what they think might happen next.

Before reading the essay, I had mostly been reacting to headlines, short clips, and posts that focused on a single statistic without much context. Reading the original source did not make every concern disappear, but it replaced a lot of vague anxiety with a clearer understanding of what is actually changing and what is still very much uncertain.

I am still early in my career, so I am not pretending to have all the answers. Maybe five years from now I will look back and realize I underestimated how much AI would change software engineering. Maybe I will realize I worried more than I needed to. Right now, I honestly do not know.

What I do know is that reading the original source felt very different from reading everyone else's interpretation of it. And if there is one sentence that sums up what I took away from the essay, it is this: the thing being automated is not the skill I am trying to become better at.

## I Would Love to Hear Your Thoughts

Writing this article forced me to slow down and think about where a lot of my own anxiety was coming from. For me, it was not really the technology itself. It was the constant stream of headlines telling me what the technology supposedly meant without encouraging me to read the original source.

After reading the essay, I feel like I have a much clearer picture of both the opportunities and the uncertainties. I am still excited about AI. I am still cautious about where it is going. But I no longer think those two feelings have to contradict each other.

I would love to hear what you think. If you have read the essay yourself, did you come away with the same conclusions, or did something completely different stand out to you? If you are also early in your career, has AI changed the way you think about becoming a software engineer? And if you have been in this industry for much longer, I would be especially interested in hearing how you see these changes from your perspective.

Drop a comment below. I read every one, and I would love to continue the conversation.

## References

* Anthropic,When AI Builds Itself

## 🤝 Stay in Touch

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

Transparency note:The banner image for this article was generated using DEV Community's built-in AI image generation feature. I wrote the prompt, generated multiple variations, and selected the final image used in this post.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (56 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse