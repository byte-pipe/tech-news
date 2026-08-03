---
title: Code Review (As We Know It) Must Die - Alex Looney
url: https://alexlooney.substack.com/p/code-review-as-we-know-it-must-die
site_name: tldr
content_file: tldr-code-review-as-we-know-it-must-die-alex-looney
fetched_at: '2026-08-03T20:02:46.246443'
original_url: https://alexlooney.substack.com/p/code-review-as-we-know-it-must-die
author: Alex Looney
date: '2026-08-03'
description: A twenty-year-old process is failing at its own goals and throttling how fast product teams can move.
tags:
- tldr
---

# Code Review (As We Know It) Must Die

### A twenty-year-old process is failing at its own goals and throttling how fast product teams can move.

Alex Looney
Jul 28, 2026
2
Share

As AI continues to disrupt how companies execute, the teams on the frontier are rapidly rethinking how product, design, and engineering actually work, chasing the velocity AI makes possible. Whether that means treating evals as the new PRD, designing directly in code, or building a full software factory, the gains all hit the same ceiling: code review.

The symptoms show up early and get worse as velocity increases:

* The velocity gains made possible by AI are being capped by slow human reviews.
* The untenable volume of code reviews is leading to degradations in codebase quality and a resultant increase in production outages.
* Engineers are burning out on this cognitively draining work, and are becoming demoralized and losing faith in the future of what the role looks like.

These aren’t growing pains that better tooling will smooth over. The process itself is the problem.

Async, diff-centric code review hardened into orthodoxy ~20 years ago, in an engineering context that no longer exists. Applied to agent-led software engineering, the process fails in three key ways:

* Writing code got cheap and reviewing it did not.Code review was designed in a world where writing code was slow and expensive, and reviewing it was relatively cheap. With agents, writing is exceptionally cheap while human review is slow and expensive.
* Diffs communicate at the wrong abstraction level.A diff is just raw lines: no intent, no design, no surrounding system, so the reviewer has to reconstruct all of it before judging any of it. That reconstruction used to be cheap, because the process assumes reviewers already have context on the line-by-line implementation, and they did. With agents writing code no human has that context on, every review starts from zero, and the reconstruction is the tax.
* Every change gets the same ceremony regardless of risk.A copy tweak and a payment logic change get identical process and identical human attention. At factory volume, risky changes get less scrutiny than they need while trivial ones clog the queue.

Those failures tell you the process is broken. They don’t tell you what to build instead. For that you need to know what jobs code review was doing, because those jobs don’t go away. Three are well known:

* Catch defects before they ship.A second set of eyes finds the bugs, logic errors, and security issues the author missed.
* Keep the codebase maintainable and consistent.Enforce standards and design norms so code stays readable and changeable by people other than the author.
* Spread knowledge across the team.More than one person understands each part of the system, silos get broken, and juniors learn by review. This happens by force: review makes a second person load the code into their head, and it’s often the only thing guaranteeing anyone besides the author ever reads the code.

Those three were never the whole story. Two more jobs get less attention, but the process does them just as reliably:

* It’s a control and authorization gate.Nobody changes the system without a second person signing off. Approval distributes accountability and satisfies compliance.
* It’s how norms get enforced.Review is where the team’s taste gets imposed: naming, patterns, “how we do things here.”

Every one of those jobs was met by the same act: a person reading a diff. Agents don’t eliminate any of the jobs. They break that bundling, so each one now has to be met on its own terms:

* Catching defects moves to automated checks before production.Tests not written by the authoring agent, with a human verifying the tests make sense. Independent AI review. A human or agent manually testing the change. The human validates the change to the product, not the code.
* Maintainability splits into two things moving in opposite directions.Line-level readability matters much less when AI can explain any code instantly. Architectural quality matters more than ever, because it’s what agents actively erode.
* Knowledge sharing moves up an abstraction level.The reviewer gets intent, design, and surrounding context communicated up front, with the code packaged alongside rather than serving as the explanation. And when someone does need to understand the code itself, comprehension is pull-based: ask AI, get answers, no forced reading at merge time.
* Norm enforcement moves upstream.Into specs, linters, and agent skills, enforced by construction instead of by comment.
* Control survives intact: the merge gate, deciding what code is allowed into the codebase.A human still owns the change and a second human still approves it, and approval still vouches for the whole thing, lines included. What changes is how you earn that confidence: you review a level up and trust the agents, the testing, and the automated verification to carry it down into the lines.

What’s left is the work that didn’t move: the jobs where human attention is worth the most:

* Verify the change an abstraction level up.The reviewer confirms two things: that the intended change is worth making, and that the implementation actually delivers it. Reading the lines was one way to get there, and never a cheap one. Now the review has to supply it directly: intent, context, design decisions, and evidence that the implementation matches them.
* Don’t bottleneck agent velocity.The process has a speed requirement it never had. Human reading time doesn’t scale to agent volume, so any process whose default path ends in a person reading a line-by-line diff fails this.
* Steer the system.With agents writing, review becomes the main point where humans inject taste and course-correct architecture. Less inspection, more steering.

So what does a process built to hit all three actually look like?

* Align on the design before the code exists.The decisions are the hard part: what to build, how it should work, how it fits the system. That’s where human judgment and creativity actually change the outcome, so that’s where review starts. Once those decisions are settled, generating the implementation is cheap.
* Surface the change, don’t make the reviewer reconstruct it.The review artifact carries the decisions that were already aligned on, plus a description of the implementation at the level a human can judge, with the code packaged alongside rather than standing in for the explanation. The reviewer shouldn’t have to go hunting for intent or rebuild the design from the lines.
* Run the adversarial pass before a human looks.Independent AI reviewers hunting for what the coding agent missed, with loops that fix findings first.
* Show the evidence.The reviewer gets proof the change was tested, and a fast way to check it themselves, in whatever form fits the change.
* Route by risk.Low-risk changes auto-approved on automated checks alone. Human attention concentrated where a mistake could actually hurt the business.
* Absorb mistakes in the system.Staged rollouts, fast rollbacks, monitoring routed back into the factory. Individual changes are less vetted, so the system has to be safe for that, with a named human owning the merge.

That last piece is the one people balk at. The human on the merge approves a change they didn’t read line by line, and still vouches for all of it. That holds because the confidence now comes from reviewing the decisions and the logical change, where the expensive mistakes live: what got built, and how it fits the system. Underneath that, the lines are covered by the adversarial pass that hunts what the coding agent missed, the evidence that the change does what it was meant to, and the risk routing that puts human attention where a mistake could actually hurt. Approval still covers the whole change. Only the path to it moved.

That’s the whole process, described at once. In practice it’s showing up in pieces, with different teams working out one component at a time:

* Align on the design: HumanLayer.Spec, architecture, and program design reviewed before the agent writes code, so PR review shrinks to confirmation.
* Surface the change: Linear Diffs.Guided reviews, glue code split out, the originating issue attached, agents fixing feedback inline. Baz goes further: it infers the intent of a change first, then investigates the code against it.
* Route by risk: Meta RADAR.A risk-scoring funnel that auto-approves low-risk diffs through layered checks, cutting median time-to-close by over 330%. Uber’s Code Inbox similarly estimates risk per change and directs reviewer attention to the risky ones.
* Run the adversarial pass: the most developed of these pieces.A whole market of independent AI reviewers has emerged (Cursor’s BugBot, CodeRabbit, Greptile, Claude Code Review), and big companies are building their own: Uber’s uReview covers over 90% of its ~65,000 weekly diffs, and Cloudflare gave its AI reviewer authority to block merges.

There are costs: individual changes will be less vetted, and some bugs will ship that old review would have caught. The winners will accept that and build systems that absorb mistakes rather than trying to avoid them.

None of this evolution is easy, but it’s worth it. The companies that successfully cast off processes built for a world that’s gone, and rebuild around how software actually gets made now, will win because of the operating speed it gives them. Velocity that compounds, where the bottleneck moves from “can we build it” to “what should we build,” and more shots on goal iterate you toward the right answer faster than competitors can plan their way there. And engineers freed to do the creative, high-leverage work they signed up for: designing systems, shaping products, steering agents, instead of grinding through review queues.

Code review was built for a world where humans wrote code slowly and reading the lines was how you earned confidence in a change. That world is gone. Reading isn’t obsolete, but it’s no longer how that confidence gets earned. The companies that evolve will lap the ones still paying a human-review tax on every change, and their engineers will be building the future while everyone else’s are stuck reading PRs.

2
Share