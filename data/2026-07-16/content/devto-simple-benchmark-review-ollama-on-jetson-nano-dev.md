---
title: 'Simple Benchmark Review: Ollama on Jetson Nano - DEV Community'
url: https://dev.to/annavi11arrea1/simple-benchmark-review-ollama-on-jetson-nano-5gee
site_name: devto
content_file: devto-simple-benchmark-review-ollama-on-jetson-nano-dev
fetched_at: '2026-07-16T03:36:59.366417'
original_url: https://dev.to/annavi11arrea1/simple-benchmark-review-ollama-on-jetson-nano-5gee
author: Anna Villarreal
date: '2026-07-12'
description: 'Previous Related Post: Part 1 This particular rabbit hole was created due to a previous... Tagged with ai, webdev, nvidia, productivity.'
tags: '#ai, #webdev, #nvidia, #productivity'
---

High accuracy at low quantization

Previous Related Post:Part 1

This particular rabbit hole was created due to a previous conversation I had here with another member on DEV about benchmarking and tests. Lot's of questions sparked:

* What's the best way to do them?
* How do we do them?
* What are good numbers?
* What information is actually important?

The truth is that it heavily depends on what you are doing and what is important to you, first and foremost. For me, and my little test generation app, my purpose seemed simple: create a simple app using ai, locally, for free, and take text I have and generate flashcards and quizzes from it so I can review. I can tell you by this point I have spent less time reviewing and more time digging into interesting tools.

On this particular journey, man - I did so much I'm having trouble knowing what to explain first. But I'll try to stick to testing. So basically, I wanted to see which model would run the best on my nano, you know without crashing it, because I did do that actually at one point. That's a tangent I'll save for later but I saved by conversation with claude in my techdocs if you want some entertainment. (techdocs--> then click jetson nano on the left. ) I did not have enough ram on my nano to handle the test run. This led me to create a swap file to accommodate for lack of ram in case of emergency. Just as a safety net - since I get into trouble.

Safety net in place, I create a quick quiz of the OSI model from a web page to use as source of truth - something to compare the results to. Thanks Vinicius Pereira for the ideas in our chat! So, I ran this test against each one of the models and varying 'quantizations' (is that a word yet?) to bring to light the mystery of this concept.

### The high level - if a model is heavily quantized, you lose quality. Brass tax.

I went to these great lengths and then only come to realize, sheesh, this is only for one specific use case. This would take a minute to map performance across many different use cases. I wonder, if you have nano, what have you used Ollama for on it? Not like I need another reason to hoard data. XD

Anyways, in case you don't feel like navigating away, here's a table:

Model

Quant

Accuracy

qwen2.5:3b-instruct

q4_K_M

100%

qwen2.5:3b-instruct

q5_K_M

100%

qwen2.5:3b-instruct

q8_0

100%

qwen3.5:2b

q4_K_M

0% (empty output)

qwen3.5:2b

q8_0

0% (empty output)

llama3.2:3b-instruct

q2_K

40%

llama3.2:3b-instruct

q4_K_M

90%

llama3.2:3b-instruct

q5_K_M

90%

llama3.2:3b-instruct

q8_0

90%

mistral:7b-instruct

q2_K

80%

mistral:7b-instruct

q4_K_M

100%

mistral:7b-instruct

q5_K_M

80%

Some cells above are empty because they would not fit on the gpu of the nano, so no point in running a test for a model that will never perform as needed due to hardware limitations.

The numbers are based on a pool of 10 questions, so this is why the numbers are so perfectly precise. Obviously this is simple high level test, but I wanted to work through this fully. Having gone through the motions, I know that the rabbit hole is deep and vast and this is barely the surface. But from simple test point of view for my use case of quiz generation, qwen2.5:3b-instruct takes the cake from the bakery to the house. Guess ima have a slice once I recombobulate my app, switching from llama3.2:3b-instruct to qwen ~ a task for another day.

I'm sure many of you reading this have seen other benchmarks elsewhere. I'd love to have some peer review here to tell me if I'm kind of on point here or if my data looks odd. Feel like I'm falling into a dark trap of testing things. I know others have done this and there is other information out there, but what kind of actual appreciation for the technology does that offer?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (30 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse