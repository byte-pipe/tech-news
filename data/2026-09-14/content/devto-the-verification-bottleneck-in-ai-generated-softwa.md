---
title: The Verification Bottleneck in AI-Generated Software - DEV Community
url: https://dev.to/kenwalger/the-verification-bottleneck-in-ai-generated-software-3p7l
site_name: devto
content_file: devto-the-verification-bottleneck-in-ai-generated-softwa
fetched_at: '2026-09-14T16:47:27.921961'
original_url: https://dev.to/kenwalger/the-verification-bottleneck-in-ai-generated-software-3p7l
author: Ken W Alger
date: '2026-09-09'
description: AI can generate code faster than ever. That doesn't mean we're shipping correct software... Tagged with ai, testing, programming, devtools.
tags: '#ai, #testing, #programming, #devtools'
---

Tacit assumptions cause hidden agent bugs

AI can generate code faster than ever. That doesn't mean we're shipping correct software faster.

Recently, I asked a coding agent to build a password reset flow. It produced the route, the token handling, the email integration, and the UI in about five minutes.

The implementation had a bug. The reset link worked more than once. Use it to set a new password, then open the same link again, and it still worked.

The feature request hadn't explicitly said that a reset link should be single use. It wasn't in the feature request, because it's the kind of thing that goes without saying right up until the moment it doesn't. Every path a person would click through by hand worked perfectly. A code review might have caught it. A demo would not have.

That gap is what I want to talk about.

## Code generation is no longer the expensive part

Traditional software development has an obvious constraint: humans have to write the software. We think about the requirement, design the implementation, write the code, run it, discover that it doesn't work, debug it, and repeat until we're sufficiently convinced.

AI coding agents compress parts of that loop dramatically. The agent can often produce an implementation faster than I can thoroughly review what it generated, which creates an inversion. For a long time, writing code was expensive and checking it was comparatively cheap. What happens when writing becomes cheap?

Verification becomes proportionally more valuable.

Suppose an agent implements a feature in five minutes, but determining whether the implementation is correct requires another 45 minutes of manual testing and code review. We haven't created a five-minute development process. We've created a 50-minute development process with a very fast implementation stage.

And the verification half is harder than it used to be, because you're now auditing code you didn't write.

Generating more code doesn't solve that. We need a better feedback loop.

## The specification is becoming the durable artifact

Here's the shift I think matters most, and it goes well beyond testing.

If an agent can rewrite a component cheaply, we become less attached to any particular implementation. Implementations are becoming disposable. Six months from now the routes change, the framework changes, the DOM changes, the internal architecture changes.

The user requirement doesn't:

 A user who resets their password must subsequently be able to authenticate with the new password, must no longer be able to authenticate with the old one, and must not be able to reuse the reset link.

In an era of inexpensive code generation, the thing worth maintaining is increasingly the specification rather than the implementation. Which means it's worth writing the specification first, deliberately, as an artifact in its own right rather than as documentation of something already built.

## Start with behavior, not implementation

I tested this with asmall web application,Claude Code, andtestRigor.

The application was deliberately ordinary: authentication, user accounts, login behavior, the kind of functionality in countless business applications. I wasn't interested in whether an agent could produce something visually impressive. I wanted to answer a different question. Can we define expected behavior first, let an agent implement it, and use independent end to end verification to determine whether the agent actually succeeded?

Consider the password reset feature. The implementation involves a route, form handling, token generation, validation, password hashing, database updates, session behavior, error handling, and UI changes. An agent generates all of it quickly.

None of those implementation details are what the user cares about. The user cares whether they can request a reset, receive the email, set a new password, log in with it, and whether the old password and the used link both stop working.

Those are observable outcomes. That makes them a useful boundary between what we asked the agent to build and what the agent actually built.

## Executable specifications

This is where testRigor became interesting to me.

testRigor expresses tests as English-like behavioral instructions rather than requiring the test author to work primarily in selectors and automation code. A test describes what a user does and what they expect to see.

That creates an opportunity when combined with AI-assisted development, because the behavioral test can function as an executable specification.

Instead of telling an agent to "add password reset," we provide a behavioral contract. The application must email a reset link. The link must lead to a form. The new password must work afterward. The link must not work a second time.

Now there are two artifacts with two responsibilities. The coding agent is responsible for figuring out how to implement the behavior. The behavioral test is responsible for determining whether the behavior exists.

That separation is the point.

## Don't let the student grade the exam

AI coding tools are increasingly capable of generating their own tests, and that's useful. I use it. But there's a problem when the same system interprets the requirement, creates the implementation, creates the test for that implementation, and then announces that everything passes.

The system can make the same mistaken assumption in multiple places. If the agent misunderstands the requirement, it produces code consistent with that misunderstanding and tests that validate the same misunderstanding.

Everything is green, and everything is also wrong.

This is exactly what happened with the reset link. An agent asked to write its own tests for the feature it just built would have tested the happy path, because the happy path is what it understood the requirement to be. It would have passed.

The single use check existed only because a specification written before the code asked a question the feature request never raised. That's the whole value: not that the test is in English, but that it was written by someone thinking about the requirement rather than about the implementation.

Independent behavioral verification asks a different question:

Regardless of how you implemented this, does the software exhibit the behavior we specified?

That's closer to the question a user actually cares about.

## Closing the loop

The part of this that interests me most isn't the testing tool. It's the feedback loop.

Once an end to end test produces a deterministic pass or failure, that result becomes input to the coding agent. The agent implements the feature, the behavioral test runs, and if the test fails, the failure returns to the agent. The agent examines the implementation, makes another change, and verification runs again.

In my case the full cycle ran three times. Red against the baseline, because the feature didn't exist yet. Red again after generation, on the reused link. Green after the failure text went back to the agent as context. About twenty minutes of wall clock end to end, most of it unattended.

The failure text mattered more than I expected. It wasn't a stack trace. It was a step in the behavior, in plain English, that didn't happen. That's readable by a person and readable by an agent, which is what let the loop close without me translating between them.

The agent now has something more useful than "try again." It has evidence that a specific expected behavior was not observed.

Spec-First Verification for AI-Generated Code

The video is rough around the edges, which is probably appropriate for an experiment. The interesting part isn't production quality. It's watching the loop operate.

## Generation and authority are different jobs

This reinforced something I've been thinking about more broadly in AI system design. Probabilistic systems are extraordinarily useful for proposing things: generate this implementation, interpret this requirement, suggest a fix, explain this failure, determine which files probably need to change.

But there are places where I want something else to have authority. Did the build succeed? Did the API return the expected response? Does the database contain the expected state? Can the user complete the specified workflow? Did the test pass?

Those questions can be answered deterministically, which gives a useful architectural separation:

AI proposes. Deterministic systems verify.

It doesn't eliminate mistakes. A badly written test verifies the wrong thing. An incomplete specification leaves important behavior uncovered. A test environment can differ from production. Verification itself needs engineering.

But separating generation from verification means we stop treating the model's confidence as evidence that the implementation is correct.

## Behavioral tests aren't magic

Working with an English-like testing system reinforced another lesson: plain English does not mean no learning required.

Tools still have semantics. You need to understand how the system identifies elements, interprets instructions, manages state, handles authentication, and responds when the application doesn't behave as expected. There were several moments where I had to learn testRigor's particular vocabulary before a seemingly obvious instruction did what I expected. My spec assumed the application would land on a login form after a successful reset. It didn't. That's a gap in my specification, not a bug in the application, and finding it took a run I hadn't budgeted for.

That isn't a flaw unique to testRigor. Abstractions don't eliminate complexity. They move it.

SQL didn't eliminate the need to understand databases. High level languages didn't eliminate the need to understand software. Natural language testing doesn't eliminate the need to understand testing.

What changes is who can express the behavior, and how tightly that behavior is coupled to implementation details. That part is genuinely interesting.

## What we should be optimizing

Much of the excitement around AI-assisted development has focused on productivity. How much faster can developers write code? How many tasks can an agent complete? How many tokens did it use?

Those metrics aren't useless, but they aren't the outcome. Software exists to behave correctly enough to solve a problem.

If an agent generates 10,000 lines in ten minutes and we spend the rest of the day figuring out whether any of it works, those lines aren't evidence of productivity. They're inventory awaiting inspection.

The metric worth tracking is correct functionality delivered per unit of time. That includes generation, but it also includes verification. As generation approaches zero marginal effort, the second half is where the remaining cost lives.

Coding agents are going to get better. They'll generate larger changes, operate longer without supervision, understand more complex repositories, and handle more of the implementation process autonomously. That makes verification more important, not less. Greater autonomy without independent evaluation doesn't produce a better development system. It produces a faster source of unverified output.

The opportunity is to build verification into the architecture rather than bolting it on afterward. The specification defines the destination. The coding agent proposes a route. Verification tells us whether we actually arrived.

Not generating code faster. Shipping working software faster.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (54 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse