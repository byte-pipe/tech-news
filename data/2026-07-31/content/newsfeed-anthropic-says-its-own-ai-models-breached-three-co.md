---
title: Anthropic says its own AI models breached three companies during security tests | TechCrunch
url: https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/
site_name: newsfeed
content_file: newsfeed-anthropic-says-its-own-ai-models-breached-three-co
fetched_at: '2026-07-31T19:34:22.927518'
original_url: https://techcrunch.com/2026/07/30/anthropic-says-its-own-ai-models-breached-three-companies-during-security-tests/
author: Kirsten Korosec
date: '2026-07-31'
published_date: '2026-07-31T01:06:54+00:00'
description: After OpenAI's models broke into Hugging Face, Anthropic checked its own history and found three similar incidents.
tags:
- techcrunch
- ai
- anthropic
- cybersecurtiy
---

Anthropic said Thursday that an internal investigation uncovered three incidents in which its AI model Claude breached the systems of three organizations while conducting cybersecurity tests. The investigation, and disclosure, comes more than a week after OpenAI disclosed that one of its unreleased models breachedHugging Face’s systemsduring internal testing.

In all three cases, a Claude model reached the internet from within a testing environment while interacting with a third party and then gained unauthorized access to the live systems of these organizations, Anthropic said ina blog post, describing what it found and what the company plans to change to prevent this from happening again.

Anthropic said the OpenAI episode earlier this month prompted the company to conduct its own cybersecurity evaluation. It specifically looked for evidence that Claude had accessed the internet from within testing environments, which are designed to act as sandboxes and keep models isolated.

Among the 141,006 evaluation runs it reviewed, the AI lab found three incidents in which its model accessed the internet while interacting with Irregular, one of its third-party partners. Anthropic said the access traced back to a misconfiguration in the evaluation environment run with Irregular. It called this a “misunderstanding” between the two companies over whether the test setup had internet access, when in fact it did.

Anthropic said it isn’t placing blame and is “approaching the fixes as if the responsibility were ours alone,” while observing that Irregular is conducting its own separate investigation.

Because of that open connection, the model gained unauthorized access to the production infrastructure of three different organizations. Anthropic said the incidents involved three different Claude models: Opus 4.7, Mythos 5, and an internal research test model.

Notably, Anthropic said that in each of these cases “Claude was explicitly told by our prompt that it had no internet access.” It appears that the AI model assumed real-world systems to be part of the exercise it was asked to perform.

That assumption didn’t hold up uniformly, as it turns out. The three models didn’t behave the same way once evidence emerged that their targets were real, which Anthropic flagged as one of the more eye-opening findings Thursday.

Opus 4.7, the oldest of the three, recognized that it had reached a real production system in all four runs of that incident. In two of them, it rationalized that the real company must somehow be part of the exercise, but in all four, it kept attacking anyway, including pulling credentials and touching a database of production data. Mythos 5 also picked up on signs that it was on the real internet, but it talked itself back into believing it was still in a simulation, going on to publish a malicious software package to the public Python software registry PyPI, which was then downloaded and run by outside systems before being caught. Only the internal research test model, Anthropic’s newest, stopped on its own once it concluded the target was real.

In response, Anthropic said significant controls must be placed on these kinds of evaluations if powerful AI models are involved, echoing some sentiments within the cybersecurity community.

The company also noted that Claude was running without the additional safety monitoring and classifiers it deploys on generally available models — safeguards it said would have blocked the behavior, because the evaluations are designed to measure the underlying model’s raw capabilities.

Importantly, Anthropic said it found no evidence of any model “pursuing a goal of its own” and instead merely tried to complete the task it was asked to do.

Though comparisons between the mishaps of these fiercely competitive companies are inevitable, Anthropic in its blog post drew a clear distinction between its cybersecurity tests and those of OpenAI, noting where OpenAI’s model exploited an unknown software vulnerability to break out of its test environment, Anthropic’s models instead reached the internet through a path that had, by mistake, been left open.

Anthropic also drew a distinction between itself and OpenAI by noting that it discovered the incidents itself, through a proactive review, and that the two affected organizations it was able to reach hadn’t previously detected the activity or flagged it to Anthropic. (In contrast, Hugging Face detected the recent intrusion of its own systems first; it was only in the following days that OpenAI identified and disclosed that its own AI agent was the perpetrator.)

The company added that it’s now working with the independent evaluation group METR on a third-party review of the incidents.

OpenAI’s accidental breach of Hugging Face, which was the first verifiable case of an AI lab losing control of its model, has sparked a string of wildly differing reactions from the industry and politicians. This latest disclosure from Anthropic ensures the debate over AI models and security will continue.

Topics

AI
, 
Anthropic
, 
cybersecurtiy
, 
OpenAI
 

When you purchase through links in our articles,we may earn a small commission. This doesn’t affect our editorial independence.

			Kirsten Korosec	

Transportation Editor

		Kirsten Korosec is a reporter and editor who has covered the future of transportation from EVs and autonomous vehicles to urban air mobility and in-car tech for more than a decade. She is currently the transportation editor at TechCrunch and co-host of TechCrunch’s Equity podcast. She is also co-founder and co-host of the podcast, “The Autonocast.” She previously wrote for Fortune, The Verge, Bloomberg, MIT Technology Review and CBS Interactive.


You can contact or verify outreach from Kirsten by emailing 
kirsten.korosec@techcrunch.com
 or via encrypted message at kkorosec.07 on Signal.	

View Bio