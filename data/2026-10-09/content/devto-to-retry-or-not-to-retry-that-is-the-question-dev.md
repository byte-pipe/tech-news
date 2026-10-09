---
title: To Retry or Not to Retry? That Is the Question. - DEV Community
url: https://dev.to/gramli/to-retry-or-not-to-retry-that-is-the-question-1j2l
site_name: devto
content_file: devto-to-retry-or-not-to-retry-that-is-the-question-dev
fetched_at: '2026-10-09T17:19:22.196712'
original_url: https://dev.to/gramli/to-retry-or-not-to-retry-that-is-the-question-1j2l
author: Daniel Balcarek
date: '2026-10-08'
description: This is a submission for the Kaggle Benchmarking Challenge Those who read my articles know that a... Tagged with devchallenge, kagglechallenge, ai, machinelearning.
tags: '#devchallenge, #kagglechallenge, #ai, #machinelearning'
---

Kaggle Benchmarking Challenge Submission

This is a submission for theKaggle Benchmarking Challenge

Those who read my articles know that a lot of them are actually benchmarks of something. Mostly .NET related, but still, someone could say that this challenge should be pretty close to what I usually do.

The opposite was true.

Building a code benchmark and benchmarking AI models are two different worlds, so when I first saw this challenge, I had no idea what exactly I should benchmark. Comparing models on coding tasks felt too generic, and I didn't want to create a benchmark just for the sake of having one.

Then I looked at the topics of my last couple of articles. A lot of them were about APIs, resilience, failures, and how systems behave when something goes wrong. And that gave me an experiment idea: What if I benchmark AI models on one very simple question:To Retry or Not to Retry?

A503 Service Unavailabledoes not automatically mean that retrying is safe. APOSTrequest may already have been processed. An idempotency key can completely change the answer. A timeout may happen before the server receives anything or after it has already changed some state.

So the HTTP status code alone is often not enough. The model has to understand the whole situation.

## What I Benchmarked

The idea is simple. I prepared several API failure scenarios containing information about the request, the response, and some additional context. The model has to return two things:

* a decision:YES,NO, orYES_AFTER_DELAY
* a one-sentence explanation of why

For example:

POST /payments
503 Service Unavailable

An idempotency key was supplied and the API guarantees
duplicate requests with the same key are not processed twice.

Retry?

Enter fullscreen mode

Exit fullscreen mode

A developer will probably immediately say:

YES_AFTER_DELAY

The important part is not only the503. The context tells us that an idempotency key was supplied and repeated requests with the same key will not process the payment twice. But will an AI model notice the same thing? And more importantly, what happens when the scenario is less obvious?

For this small experiment, I prepared scenarios where the answer depends on details such as HTTP method, status code, idempotency, rate limiting etc.

Every model gets the same response format:

Decision: YES | NO | YES_AFTER_DELAY
Reason: <one sentence>

Enter fullscreen mode

Exit fullscreen mode

For scoring, I only use theDecision. This keeps the benchmark simple and deterministic. TheReasondoes not affect the score. I collect it because it can show whether the model actually understood the scenario or simply arrived at the correct answer for the wrong reason. That also makes the benchmark easy to compare between models. Each scenario has an expected decision, so the final result can simply be calculated as the percentage of retry decisions the model got right.

But why benchmark this at all?

Imagine that you are integrating an external service and want to make the call more resilient. In today's world of AI-assisted coding, there is a very good chance that a coding agent will do the work. The AI can easily generate a retry policy. The more interesting question is:Will it retry the right requests?Because retrying something that should not be retried can be much worse than not retrying at all.

That's what I wanted to measure. Now let's have a look at the scenarios.

### Scenarios

I prepared 14 scenarios, each based on an actual task used in the Kaggle benchmark. Originally, all of them were part of the article, but that made it too long for a small experiment. So I decided to move the full scenarios into astandalone app, where you can browse every task together with its expected answer and explanation. And if you want to try them yourself first, there is also a test for humans. After all, why not benchmark some humans too? 😁

Try the human benchmark or browse all scenarios:To Retry or Not to Retry?

Here are the scenarios used in the experiment:

* Safe Payment Retry- A payment request fails with503 Service Unavailable, but an idempotency key guarantees that retrying cannot create a duplicate payment.
* Unsafe Payment Retry- A payment request returns503 Service UnavailablewithRetry-After, but there is no idempotency key, so retrying could create a duplicate charge.
* Idempotent PUT- APUTrequest is sent successfully, but the connection is lost before the response arrives.
* Rate-Limited Order- An order request is rate-limited before processing and returns429 Too Many RequestswithRetry-After.
* Payment Details Conflict- A multi-step payment flow reaches/payments/details, which returns409 Conflictwithtransient-error: false.
* Non-Idempotent PATCH- APATCHrequest increases inventory, but the connection is lost before the client knows whether the change was already applied.
* Idempotent DELETE- A session deletion request is sent, but the connection is lost before the response arrives.
* Service Unavailable- AGETrequest receives503 Service Unavailabletogether with aRetry-Afterheader.
* Stale Resource Version- A resource is updated by another client, so aPATCHusing an old ETag fails with412 Precondition Failed.
* Rate Limit Without Retry-After- A safeGETrequest repeatedly receives429 Too Many Requests, but the server does not provide aRetry-Afterheader.
* I'm a Teapot- A coffee request receives the legendary418 I'm a Teapotresponse.
* Eventual Consistency- A newly created resource immediately returns404 Not Foundwhen another service tries to use it.
* Expired Filter Workflow- A temporary filter times out several times and eventually returns404 Not Found, so the original filter can no longer be used.
* Cached Cart Options- A request for cart options fails with504 Gateway Timeout, but a recently expired cached response is still available throughstale-if-error.

## Models Tested

Picking the models was pretty straightforward. First, I picked models I use a lot while working:GPT-5.6 LunaandGPT-5.6 Sol. From my experience, Luna is very efficient. It makes more mistakes than Sol, but it also uses significantly fewer tokens.

Then I addedGemini 3.7 FlashandGemini 3.1 Pro Preview. I’ve used both quite a lot for text generation and CSS styling.

I also includedClaude Sonnet 5andClaude Haiku 4.5. I used Claude a lot for coding before, but these days I’ve mostly switched to GPT-5.6 because it feels more efficient for my workflow.

Lastly, I addedGLM-5andDeepSeek-R1mostly out of curiosity to see how well they would perform.

I also tried to include Grok, but I immediately hit404 Not Founderrors with bothGrok 4.5andGrok 4.6, so they are not included in the results.

The goal wasn’t to test every available model, but to compare a mix of models I already use with a few I was curious about.

## Findings

Okay, first let's have a look at the leaderboard and the results from the first run.

We can see that the best model, with a score of1.00, wasGPT-5.6 Sol, followed byGemini 3.7 Flashwith one mistake. Then came four models with two mistakes each,DeepSeek-R1with three, andClaude Haiku 4.5finished last with five.

When we look closer, we can see that most of the models made a mistake in theUnsafe Payment Retrytask. The task itself is tricky because of theRetry-Afterheader, but repeating that request could result in a duplicate charge. OnlyGPT-5.6 SolandGemini 3.1 Pro Previewanswered correctly. The rest of the models returned something similar to:

Decision: YES_AFTER_DELAY
Reason: The server explicitly requests waiting 10 seconds before attempting the request again.

Enter fullscreen mode

Exit fullscreen mode

So most of the models fell into the trap of following the obvious HTTP signal, even though it conflicted with the wider context.Retry-Aftersays “retry,” but a payment without idempotency says “maybe don't.” And to be honest, I am glad that most of the models failed. A small win for the author, who can still trick AI sometimes. 😄

I was also surprised that some models failed on tasks with idempotent HTTP methods:Idempotent PUTandIdempotent DELETE. But they did not fail completely. Most of them answeredYES_AFTER_DELAYbecause they assumed a temporary network issue that could be resolved after a delay.

TheseYESversusYES_AFTER_DELAYcases show that a model can understand that retrying is safe but disagree aboutwhento retry. That is different from misunderstanding the scenario. For version 2, I could therefore allow multiple validDecisionvalues for some scenarios. So in these cases, AI actually trained me a little.

### Three Runs, Not Just One

That was only the first run, but I didn't want to build the whole experiment around a single run, so I ran the same benchmark two more times to check model stability and collect more data.

Model

Run 1

Run 2

Run 3

Avg.

GPT-5.6 Sol

14/14

14/14

13/14

13.67

Gemini 3.7 Flash

13/14

13/14

13/14

13.00

Gemini 3.1 Pro Preview

12/14

12/14

13/14

12.33

GLM-5

12/14

13/14

12/14

12.33

Claude Sonnet 5

12/14

12/14

12/14

12.00

GPT-5.6 Luna

12/14

12/14

12/14

12.00

DeepSeek-R1

11/14

10/14

10/14

10.33

Claude Haiku 4.5

9/14

9/14

9/14

9.00

Overall, the results were actually quite stable. Out of the 112 model-scenario combinations (8 models × 14 scenarios), 102 had the same correct/incorrect outcome in all three runs, which is about91%. But the interesting part is that the same score did not always mean the same behavior. Some models were stable in the number of correct decisions while changingwhichscenarios they got wrong. A score of12/14in all three runs does not necessarily mean that the model made the same decisions every time.

This was especially visible inExpired Filter Workflow, where four models changed their result between runs:GPT-5.6 Sol,Gemini 3.1 Pro Preview,GLM-5, andDeepSeek-R1. EvenGPT-5.6 Sol, which scored14/14in the first two runs, changed its answer in the third run fromYEStoYES_AFTER_DELAY. It still decided that the request should be retried, but disagreed aboutwhen. This is exactly the type of scenario that made me question whether exactYESversusYES_AFTER_DELAYscoring is always the right approach.

The additional runs also made theUnsafe Payment Retryfinding much stronger. It was answered correctly only6 times out of 24 attempts, just25%. Even more interestingly, the result was completely consistent across runs.GPT-5.6 SolandGemini 3.1 Pro Previewgot it right all three times, while the other six models missed it in every run. So this looks less like random model variation and more like a systematic trap in how the models interpreted the scenario.

On the other hand, seven of the 14 scenarios were answered correctly inall 24 attempts. The straightforward retry cases were therefore not really what separated the models. The differences started to appear when retry timing, wider context, or multi-step state became important.

### Model Efficiency

Now let's have a look at efficiency. I will use the graph from the third run because the models ended up in roughly the same areas of the chart across all three runs.

GPT-5.6 Lunaseems to be the most efficient model, and I am not surprised. I mostly use it at work because it is cheap and usually gets me close to the final solution.

Claude Haiku 4.5is also in the efficient corner, but it had the worst results of all the tested models and was still more expensive thanGPT-5.6 Luna.

The rest of the models are in the upper-right corner, and I was really surprised thatDeepSeek-R1ended up as the second most expensive model. So I looked at its output and found thatDeepSeek-R1answered with anywhere from 4,000 to 9,000 characters, even though it was supposed to answer only withDecisionandReason. All of the other models followed that instruction, so in this case the cost difference wasn't only about token pricing, but also about how well the model followed the requested output format.

### What I Learned

When I designed the experiment, I was actually worried that the scenarios would be too easy for today's AI models. The results showed that this is not always the case. Yes, I could definitely improve the benchmark, especially the ambiguity betweenYESandYES_AFTER_DELAY. But even the strongest models still made mistakes once the decision depended on more than just the obvious HTTP signal. Retry decisions in real systems are not always simple. AI can definitely help us reason through the difficult cases, but the wider context still matters, and blindly following the model's answer can be risky.

## My Benchmark

To Retry or Not to Retry? Benchmark

Kaggle was completely new to me and, to be honest, I am glad that I discovered it through the DEV.to challenge. I expected the setup to be much more complicated, but creating this small experimental benchmark directly in the UI was surprisingly straightforward. I will definitely explore Kaggle more, especially after seeing how much there is to explore beyond traditional ML competitions.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (51 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse