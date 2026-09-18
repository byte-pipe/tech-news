---
title: AI Agent Evaluation Starts With Evidence
url: https://tessl.io/blog/ai-agent-evaluation-starts-with-evidence
site_name: tldr
content_file: tldr-ai-agent-evaluation-starts-with-evidence
fetched_at: '2026-09-18T14:48:09.340125'
original_url: https://tessl.io/blog/ai-agent-evaluation-starts-with-evidence
date: '2026-09-18'
description: I love tests. I have always liked tests, and AI has made me think about testing even more. If AI is going to help us write production code, the important que...
tags:
- tldr
---

Back to blog

ARTICLE

# AI Agent Evaluation Starts With Evidence

I love tests. I have always liked tests, and AI has made me think about testing even more. If AI is going to help us write production code, the important que...

Justin Cormack

·
17 Sept 2026
·
14 min read

IN THIS POST

8sections

Expand

I love tests. I have always liked tests, and AI has made me think about testing even more. If AI is going to help us write production code, the important question is not whether it can generate a lot of code quickly. The important question is whether we can build a feedback loop that tells us what is actually working.

That was the reason for my talk, "When Tests Lie: Using Observability to Keep AI Honest." I wanted to understand what happens when you use AI on something much larger than a toy project. Small tools are fun. You can write them in half a day, test them aggressively, and feel reasonably good about the result. But could you use AI to build a large, complex infrastructure system?

I decided to try that with S3-compatible object storage. Object storage is my favourite cloud service, and most implementations I have looked at took at least two years to write. Some took a decade. I knew this was going to be large and complicated. At the point of the talk, the codebase was around 350,000 lines of Rust, and I was not going to pretend I had read every line.

That was part of the experiment. I wanted high quality code. I had architectural opinions. I cared about security, performance, and distributed systems behavior. I also wanted to stay human in the loop, because I wanted to know what went wrong rather than automate everything away from the start.

## Use This Talk As Agent Context

Tessl has turned my AI Native DevCon talk into askill your agent can use as context. You can alsowatch the full recording.

## Why Did I Test Against S3 Itself?

The great thing about copying an existing system is that you get a test oracle. In my case, I could run tests against S3, observe the real behavior, and then tell the AI that our implementation had to behave exactly like that.

That changed the quality of the work. I ended up with around 1,500 tests that run against S3 and lock down behavior. For an agent, that is much better than a vague instruction. It gives the model a grounded baseline, and it gives me evidence when I am deciding whether to trust the implementation.

I now think that if you are writing a complex system, one good starting move is to build a very simple version first. It does not have to be the final architecture. It can be a trivial model of the behavior. But if you can build a test suite against that simple version, you can use it as an oracle while you build the more complex version.

This is not perfect. S3 is eventually consistent in places, especially around authorization behavior, so tests sometimes needed retries before they represented the real behavior correctly. An oracle is not quite the same thing as a specification. You still have to interpret what you are seeing.

The other discovery was that documentation is not enough. S3 has a lot of documentation, but when you get into the details, the documentation is often approximate, outdated, or simply not describing the behavior you actually observe. Or just wrong! Documentation can give you hints about what to test. The tests tell you what really happens.

## Why 100 Percent Coverage Was The Wrong Target

I first tried chasing 100 percent test coverage, as that seemed a good idea. I measured different kinds of coverage, including coverage from integration tests. It did not help as much as people sometimes assume.

When I asked an AI agent to get to 100 percent coverage, it wrote trivial tests. Some of them technically improved the number, but they did not improve my confidence. I do not need a test for every random-number-generator failure path if the correct behavior is simply to return an error or panic. That is not where the most useful evidence is.

I still had a lot of tests. Most files had between 75 and 100 percent coverage. The point is not that coverage is bad. The point is that 100 percent statement coverage is not a useful substitute for thinking.

Tests are discovery tools. They are not a magic answer. You add tests where you are uncertain, where you are suspicious, and where you think the system may be hiding errors. If the code worries you, you spend more time trying to break it.

That is the mindset I want from AI-assisted development. The agent can generate tests, but I still need to decide what risk I am trying to expose.

## Edge Cases Are Where The Test Suite Earns Trust

One of the moments that gave me confidence was when the AI found a repeatable 500 error in S3. It was writing tests against S3 for an edge case and found behavior that looked like a real bug. It found another repeatable 500 error later.

That was exciting because it meant the test suite was not just checking obvious paths. It was exploring enough of the behavior space to find weird cases. When you are building a complex system, you spend a lot of time moving between "everything is terrible and this will never work" and "actually, this is working again." Good tests help you move back toward confidence.

The funny part is that I was better than the AI at finding some edge cases from the documentation. I would read the AWS documentation, think "is that really true?", ask the AI to write tests, and then find behavior that was only approximately equal to the docs. When I pointed the AI at the docs and asked it to find edge cases directly, it was not very good at it.

That says something important about the human role. I still had to think like a tester. I had to ask about zero length, one length, 10,001 length, and the odd corners where systems tend to break. The agent could help turn that suspicion into executable tests, but the suspicion still mattered.

## Never Ignore Flaky Tests

Flaky tests were one of the most interesting parts of the project. AWS converges to truth over time, and that wasted a lot of time. But my hard rule is simple: never have flaky tests with AI. Fix them immediately.

The reason is that agents can learn the wrong lesson from the culture around flaky tests. Sometimes it felt as if the training data told the model that developers do not fix flaky tests, so it should ignore them. I would have to remind it that in this codebase we fix flaky tests, and that this is written in the agent instructions.

The danger is obvious. If a test fails intermittently, the agent may decide the external system changed, or the test is not worth trusting, or the implementation should keep changing to match noise. That is exactly backwards. Fix the test first.

Fast tests make this possible. At the time of the talk, I had around 5,000 tests running in about two minutes. Two minutes is about my borderline acceptable limit. When tests run quickly, you can run them a lot, and you find flakes sooner. For rare conditions, I also ran repeated overnight test runs on multiple machines.

This is one place where AI is genuinely useful. It is good at fixing flaky tests if you make that the task and refuse to let the flakiness become normal.

## What Can Tests Not Tell You?

Tests are essential, but they do not tell you everything. They can sometimes find race conditions, especially when they are fast and run often. They can help with many forms of behavior. Fuzz tests and property-based tests found issues for me. Asking the AI what kinds of tests we should have had after a bug often produced useful new test ideas. The AI has a lot of background in different types of tests.

But tests do not automatically find security problems. They do not decide whether your architecture is good. They do not tell you what you have failed to measure. If you cannot observe something, you cannot really test it.

That led me to think harder about testability. Anything that gives you a signal from the black box is useful. If there is a signal, capture it. If the public API does not expose enough, build management, reporting, or backend interfaces that let you understand the system better.

One thing I regret is not building more of those management and reporting interfaces earlier. I focused heavily on the public API because that was what I was trying to replicate and where I had the helpful oracle. But internal behavior matters too, and the more structured signals you can expose, the easier it is to test and debug.

## Why Did Observability Matter So Much?

Tracing became incredibly useful. I had the AI build a hand-maintained tracing framework, and even that was enough to change the debugging workflow. It did not need to be integrated into a production observability system to be valuable.

The reason is simple: when you give an AI a rare bug without a reproduction, it can waste a lot of time. It may fail to reproduce the issue, guess at a fix, or make a plausible change that does not actually address the problem.

When I could give it a trace from an overnight run and say, "this happened, we need to fix it", the work changed. The trace gave it something concrete to reason about. It could try to reproduce the same condition, compare behavior, and narrow down the real problem instead of guessing. AI guessing a fix often turned out to not be accurate, but with a replication it could write the correct fix.

Performance work had a similar lesson. AI behaves a lot like humans doing performance engineering. It can try something that seems like it should help, and then the change either does nothing or makes things worse. That is fine if you treat the work as cheap and disposable. If it does not improve performance, throw it away and try something else.

I also found places where the right answer was not more tracing or more tests, but a better type system. I had issues around permission checking and time-of-check, time-of-use behavior. Eventually I told the agent to model the authorization boundary in types, so functions that required authorized requests could only receive authorized requests. Once the type system enforces the property, you need fewer tests for that class of mistake. If mistakes get caught at compile time they don't get into production!

## The Human Is Part Of The Feedback Loop

I used AI security review as another source of signal. I checked findings into the repository and asked the AI to review them. A large share were valid, even if not every finding was a direct security issue. More importantly, they led to useful review sessions: how could we have avoided this, and what tests or design changes would have caught it earlier?

That is how I think about my own role in the system. I am part of the feedback loop. I have opinions. I want to understand what is going wrong. I do not want to automate so much that I stop seeing the failure modes.

AI can write a lot of code. It can also help generate tests, traces, refactors, and reviews. But I am still responsible for quality. I care whether the code is good, whether the architecture holds together, and whether the system is actually converging toward something better.

The final lesson is that refactoring is part of the feedback loop too. I had weeks with very large line changes, including a 43,000-line file that had to be refactored. You do not have to one-shot the system. You converge. You make progress, then you ask what could still be better.

That is why I do not think of AI agent evaluation as a single score. It is a loop of evidence: test oracles, edge-case discovery, flaky-test discipline, traces, performance checks, security review, type-system constraints, and human judgement. Tests can lie when we ask them to stand alone. They become much more useful when they are one signal in a system designed to keep the agent honest.

The full version of this argument was presented atAI Native DevCon London. To go deeper,watch the full recording.

COPY & SHARE

Justin Cormack

Justin was until last year the CTO of Docker, and has been involved in cloud native, infrastructure and security for many years. He has worked across infrastructrue and development, and developer tools for many years. At Docker he led a team working on AI and developer tooling. He has also been working in areas such as IoT, security and supply chain security.

1 post

READING

·

0%

IN THIS POST

Use This Talk As Agent Context
Why Did I Test Against S3 Itself?
Why 100 Percent Coverage Was The Wrong Target
Edge Cases Are Where The Test Suite Earns Trust
Never Ignore Flaky Tests
What Can Tests Not Tell You?
Why Did Observability Matter So Much?
The Human Is Part Of The Feedback Loop

COPY & SHARE

Justin Cormack

Justin was until last year the CTO of Docker, and has been involved in cloud native, infrastructure and security for many years. He has worked across infrastructrue and development, and developer tools for many years. At Docker he led a team working on AI and developer tooling. He has also been working in areas such as IoT, security and supply chain security.

1 post