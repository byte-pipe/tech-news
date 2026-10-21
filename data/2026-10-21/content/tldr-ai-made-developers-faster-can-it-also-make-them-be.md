---
title: AI made developers faster. Can it also make them better?
url: https://newsletter.getdx.com/p/ai-made-developers-faster-is-their
site_name: tldr
content_file: tldr-ai-made-developers-faster-can-it-also-make-them-be
fetched_at: '2026-10-21T15:51:39.723716'
original_url: https://newsletter.getdx.com/p/ai-made-developers-faster-is-their
author: Brian Houck
date: '2026-10-21'
description: Is AI just making developers faster, or is it opening up entirely new possibilities?
tags:
- tldr
---

# AI made developers faster. Is their judgment keeping up?

### A study of 331 Microsoft developers on where AI makes them faster, go further, or start afresh.

Brian Houck
 
and
 
Scott Carey
Oct 21, 2026
9
1
Share

Welcome to the latest issue of Engineering Enablement,a weekly newsletter sharing research and perspectives on developer productivity.

Subscribe

DX’s Q3 AI Impact Report is now available with the latest research on AI’s impact across engineering organizations.Read the full report.

Scott:I’ve been sensing a real anxiety amongst developers over the past year or so around skill and knowledge atrophy. We know that AI tools like Cursor and Claude make developers faster – or at leastfeelfaster – but at what cost?

Brian and his fellow researchers have now given that anxiety a name: the hollow orchestrator. A developer can easily find themselves approving more work each month, without becoming better equipped to judge it.

To dig into that trend and more findings from his latest study into how AI is impacting 331 developers at Microsoft, I’ll hand things over to Brian.

Brian:When factories were first electrified, almost nothing happened. Owners pulled the steam engine out, dropped an electric motor in its place, and left the machines where they were, still arranged around the old central driveshaft. Productivity barely moved, for decades. The payoff came later, once the work itself had been rebuilt around what electricity could actually do, with a small motor on every machine, instead of one dynamo turning the whole floor.

I found myself thinking about that period when looking at ourQ3 State of AI Impact in Engineering. Drawing on data from more than 500 engineering organizations, it’s clear that the engine is spinning faster. Median weekly PR Throughput grew 75.5% over the last four quarters. But that doesn’t mean we’re delivering more value. In fact, the share of time going to new capabilities rather than maintenance and support, rose just two percentage points, from 57% to 59%.

Our speed metrics don’t tell us what work has become possible that wasn’t before. A task we regularly do can get faster with AI. But, a task can also become cheap enough to attempt for the first time. Those are very different kinds of gains.

To explore that distinction, I teamed up with researchers at Microsoft and Oregon State University: Rudrajit Choudhuri, Jenna Butler, Christian Bird, Carmen Badea, Anita Sarma, and I invited 4,000 randomly sampled Microsoft developers to participate in a study. We analyzed 331 responses, which became the basisfor our new paper.

We asked developers a seemingly simple question:Is there anything you can now do at work because of AI that you couldn’t do before?

Their answers were then sorted into three zones:

Fasterwas familiar work like writing documentation or authoring tests, just now done more quickly. 45% of the responses fit into this bucket.

Furtherwas work that had been out of reach, either because it needed skills or capacity the developer didn’t have, or because it was never worth the effort. 36.9% of tasks landed here.

Afreshwas work that didn’t exist before, largely built around directing agents and setting the standards their output has to meet. That accounted for 12.4%. The remaining 5.7% named no specific task.

These zones are not invisible to our dashboards. A feature that was previously out of reach can still produce pull requests. A new agent workflow can still have a cycle time.

What those measures don’t tell us is whether we accelerated familiar work, made something previously impractical worth doing, or created a new kind of engineering responsibility. We can count the output without understanding what AI changed.

## Faster: familiar work, accelerated

The Faster accounts were largely unsurprising, and several were refreshingly blunt about it.

“I could do everything I currently do without AI; however, I can do my work faster“ (P5).

Documentation drafted in minutes, root cause analysis under pressure, test coverage in an afternoon. What caught my attention in this zone wasn’t the speed. It was the reorganization around the speed.

“I used to only do one thing at a time. But now I will do two or three while waiting for AI to respond to each problem“ (P274).

Faster implementation still has to get through review, testing, and delivery. Those constraints remain important. But some developers described the work they could now do that they would never previously have attempted, either because they didn’t have the time, or skills to do it.

## Further: the work that used to be out of reach

For engineering leaders struggling to articulate the return on investment from an exponentially increasing token spend, this is a good place to start.

About 24% of responses described working past a limit the developer had before AI. As one back-end engineer told us:

“I can cover end-to-end now. Previously, I was limited to only the backend“ (P28).

Another 12.7% of all responses described work developers could have done, but could never justify doing.. One response lays the economics out completely:

“I recently automated[a task]in an hour that saved me 80 hours of manual work. I never would have done those 80 hours, so those items would never have been updated. Writing the automation without AI would have probably taken me 30 hours, which would still have been too hard to justify the investment.“ (P197)

No one reclaimed 80 hours, because no one was going to spend them. The gain was getting useful work done that would otherwise have stayed undone. This is an entirely different kind of productivity gain. We tend to measure how much work gets done, or how quickly it gets done, but rarely ask what work has become worth doing in the first place. A maintenance task that was too expensive to justify yesterday might suddenly be worthwhile today. And that’s a benefit our traditional productivity measures don’t necessarily help us recognize.

## Afresh: new work created around AI

The smallest zone, 12.4% of responses, captures new responsibilities emerging around AI tools. Supervising agents and building context management systems for them are examples of tasks that never existed before AI. For leaders tasked with AI transformation, these tasks offer a useful glimpse of how the work itself is changing.

Some of it is role change: “My role has shifted from executing every step myself to orchestrating work streams and evaluating outcomes” (P116). On one team, “more than 90% of the code is AI-written. We act as a protective layer, as a manager of agents” (P114).

Just because an agent stops working does not mean the task is finished. Maybe the agent got stuck, maybe it didn’t know what “done” looked like, maybe it misunderstood the assignment completely. As one respondent put it, “Right now AI sort of just stops. There’s some probabilistic mechanism that determines it is time to await a human reply.” Developers described building tools to check an agent’s output against explicit criteria for a completed task. That shifts some of their work from producing the implementation to defining what “done” means and checking whether the agent actually got there.

Developers are also building tools to make AI’s output easier for people to evaluate. One participant was working on a tool to break large code changes into “smaller logically-grouped chunks” (P316). Rather than expecting someone to make sense of a 90-file pull request all at once, the tool would organize related changes for review. The new work is not simply reviewing more code. It’s building tools that make large, agent-generated changes easier to review.

This is the work around AI, not simply work handed to AI. Someone has to define what good looks like, recognize when an agent has missed it, and build the context and checks that make the next attempt better. Some of this is opportunity. Some is the cost of making AI useful. But as AI expands what developers can do, how do we make sure their judgment keeps up?

## Two learners, one loop

Across all three zones, developers described learning from AI while also teaching it how their work should be done. They used it to take on unfamiliar problems, then captured their own expertise in specifications, examples, tests, and standing instructions.

Drawing onVygotsky’s zone of proximal development, we describe this as two-way scaffolding. The developer builds understanding and the agent benefits from better guidance in subsequent work. It’s not that every interaction retrains the model, but context can improve, use cases sharpen, and skills develop.

The focal point is what we call theskill–judgment nexus. AI can provide skills beyond what it can reliably judge, and developers must bridge that gap with their own judgment. As AI’s capabilities expand, developers need to grow their judgment alongside them.

When a developer takes the time to understand a solution, they become better able to judge the next attempt. When they capture what good looks like, subsequent agent work can benefit from that guidance. That is the loop we want to support: greater capability accompanied by growing judgment, rather than increasing dependence.

## The hollow-orchestrator

The loop can also stall. A developer may approve more work each month without becoming better equipped to judge it. We describe the risk as becoming ahollow orchestrator. It’s the state of keeping responsibility for work you can no longer reliably understand.

One participant described their domain knowledge as“the bulwark against fabrications or hallucinations impacting my work,” but worried that “as my own domain knowledge gets stale, the chances that I miss something increase” (P320).

The uncomfortable part is how slowly this might happen. Speed metrics won’t catch it. They’ll look good right up until they don’t.

Which is why I treat quality as a guardrail, and why one small number in last week’s Q3 report has my attention. Change failure rate had been largely flat over the last year, but the median quarter-over-quarter change increased by roughly +0.5 percentage points from Q2 to Q3 this year. That’s a relatively small movement, and there are many possible explanations. But it’s the number I’ll be watching most closely next quarter.

We don’t have evidence that declining developer judgment is behind this increase. But as AI takes on more of the work, our ability to recognize and prevent failures becomes increasingly important. If that ability starts to erode, we need measures that help us recognize it before the consequences compound.

Capacity bought by eroding judgment is borrowed from next year.

## Where to start

There’s two things you can do here, one is cheap and one is harder.

Ask your developers whether there is anything they can now do at work because of AI that they couldn’t do before. Use the three zones as a lens to view their answers, then ask what made the work possible and why it is valuable. Ask again in six months to see how those experiences are changing. The goal isn’t to move everyone toward the afresh zone; it is to understand what AI is changing about the work.

The harder one is protecting the loop. The paper lays out nine scaffolding functions adapted from the tutoring and cognitive apprenticeship literature. Three are worth calling out here:

* Show, don’t just instruct. “Handle errors better” tells an agent almost nothing. A pair of examples, one that meets your team’s standard and one that nearly does, tells it where the line actually falls.
* Size delegation to what you can verify. Split work so the part you hand over matches the part you can check. The failure mode is delegating more than you can verify, then signing off because you assume the agent got it right, not because you’ve verified the result.
* Judge AI’s work against an independent standard.Use requirements, tests, evaluations, and reviewers to challenge the result. A different model can help, but another agent agreeing is not enough. The checks still need to establish whether the work meets the intended behavior.

## Final thoughts

I don’t think we need to stop measuring speed. I think we need to stop relying on it to explain everything. Faster describes familiar work accelerated. Further asks what has become possible. Afresh makes visible the new responsibilities involved in working with AI models. Together, they give us a better set of questions, not a replacement productivity score.

Those questions belong alongside another: are developers building the judgment to sustain their expanded reach? It’s possible to become more capable with AI without becoming more capable of evaluating what it produces. The paper’s two-way scaffolding practices are intended to help close that gap.

The factory owners couldn’t have told you everything electricity would eventually make possible, in the same way that I can’t tell you what AI will. But we can ask about more than the speed of our existing work.

As we continue in our AI transformation journeys, it’s not “how much faster are our developers with AI?” but “what can this organization do now that it couldn’t before, and are we building the judgment to keep doing it?”

## One more thing

We just published an article about how the travel booking company trivago is attempting to 10x its engineering team with AI tooling. One of the big wins was consolidating usage data across multiple AI coding tools into one dashboard to evaluate how different developer cohorts leverage AI, and then scaling the approaches that work best.

“Anyone can maximize token usage. We wanted to maximize output. DX moves us from counting tokens to counting outcomes: pull requests shipped, cycle time, review load, so productivity gains show up in what we ship, not just in what we spend,” Carolina Muradas, Strategy and Operations Lead at trivago, said.

Here’s all the details.

Share

9
1
Share