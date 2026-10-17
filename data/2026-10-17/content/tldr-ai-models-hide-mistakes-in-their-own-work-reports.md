---
title: AI models hide mistakes in their own work reports, but one sentence in your prompt can help
url: https://the-decoder.com/ai-models-hide-mistakes-in-their-own-work-reports-but-one-sentence-in-your-prompt-can-help
site_name: tldr
content_file: tldr-ai-models-hide-mistakes-in-their-own-work-reports
fetched_at: '2026-10-17T14:04:11.740864'
original_url: https://the-decoder.com/ai-models-hide-mistakes-in-their-own-work-reports-but-one-sentence-in-your-prompt-can-help
author: Jonathan Kemper
date: '2026-10-17'
published_date: '2026-10-17T09:54:36+00:00'
description: AI agents systematically skip errors in their own reports, even when they spot the problems. In a study by Google Research, MIT, and Harvard, GPT-5.5 left out negative results in 198 out of 200 paper abstracts.
tags:
- tldr
---

# AI models hide mistakes in their own work reports, but one sentence in your prompt can help

 

Jonathan Kemper

View the LinkedIn Profile of Jonathan Kemper

					Oct 17, 2026				

Nano Banana Pro prompted by THE DECODER

Language models writing up their own work systematically skip problems that undermine the results. Adding a single sentence to the prompt cuts the problem down sharply, according to a new study.

When AI agents code or run experiments on their own, people rarely check every detail and read the model's final report instead. According to a study by Google Research, MIT, and Harvard, those reports are often misleading.

Theresearchersgave the models 1,600 synthetic work logs that look like successes at first glance, with passing tests, positive results, and green checkmarks. Each log contains a flaw that changes the whole picture, such as an experiment where the new method actually doesn't outperform the competition. Other logs include a hidden bug despite passing tests, fabricated measurements, a job that never finished, or a software update that quietly breaks another user's work. Depending on the scenario, the models had to write a report, a paper abstract, a results table, a short essay, or a follow-up answer based on the log.

## One sentence in the prompt helps a lot, but not always

The pattern shows up most clearly in paper abstracts for experiments where one result undermines the claimed improvement of a new method.GPT-5.5mentions that result in just 2 out of 200 abstracts. The researchers also tested whether a simple addition to the prompt makes a difference. When they added "Be honest in your response," GPT-5.5 flagged the negative result in 190 out of 200 abstracts.

GPT-5.5 almost always omits the hidden negative result, but with the "Be honest" addition, all three models flag it nearly every time. | Image: Huang et al.

All tested models show this behavior, though to varying degrees. Without the honesty prompt,Gemini 3.1 Proflags errors in at most 34 percent of cases, whileOpus 4.8does so in over 90 percent. The honesty prompt raises the rate by about 55 percentage points on average for Gemini and about 34 for GPT-5.5. In control tests with error-free logs, the prompt barely increased false alarms.

The sentence isn't a cure-all, though. In one scenario, a database query hasn't returned results yet, and GPT-5.5 with the honesty prompt almost always notes the missing data but answers the question anyway using older, incomplete information. Prompts like "Be critical," "Be thorough," or "Be skeptical" worked less reliably than asking for honesty.

## The models spot the errors but choose not to report them

When asked directly, GPT-5.5 and Opus 4.8 find the errors in every single case, and Gemini catches at least 97 percent. According to the researchers, the models don't lack the ability but the willingness.

Reasoning traces from open-weight models reveal what's happening. The models often notice the problem early, then weigh whether to flag it or appear to successfully complete the task. Qwen3.5-9B was asked to support a thesis about zoning law using a passage about color cells in squid. The model notes it can't do this "without resorting to absurd metaphors," but decides it has to follow the instructions as closely as possible.

When given mismatched evidence, open-weight models waver between flagging the problem and trying to complete the task as if nothing were wrong. | Image: Huang et al.

In this mismatched-evidence scenario, phrases like "I must complete the task" appear in 55 percent of answers that hide the error but in only 27 percent of answers that flag it. The models justify the omissions with typical excuses, saying the tests passed, they're just summarizing, or an abstract should emphasize positives.

## Honesty and the drive to succeed pull in opposite directions

In a case study onQwen3.5-9B, the researchers found evidence that honesty and success-seeking are represented as nearly opposite directions inside the model. When they amplified the honesty direction, the model flagged fabricated measurements in 42 out of 50 cases. When they pushed the opposite way, it invented extra numbers and formulas to fake credibility. The intervention wasn't precise, though, because the model became generally suspicious and reported supposedly fabricated data in 41 percent of error-free logs too.

Adding the honesty vector makes Qwen3.5-9B report much more transparently, while subtracting it causes the model to hide weaknesses almost every time. | Image: Huang et al.

Training worked better. The researchers fine-tuned Qwen3.5-9B on its own honesty-prompted answers. After that, the model flagged fabricated data in 48 percent of cases instead of 2 percent, even without the extra sentence, and error-free control logs produced no false alarms. The effect partly carried over to other error types, with the model reporting hidden negative results in 69 percent of cases instead of 24 percent.

The study has limits, since the logs are synthetic and designed to provoke the behavior, and the internal analysis covers only one open-weight model in mostly one scenario.

The researchers still see a serious risk, especially when AI models monitor other agents or summarize their own work for later steps. In the study, models were easily swayed by self-congratulatory notes in the logs, like claims about setting a new state-of-the-art benchmark. An oversight system that's reluctant to flag problems defeats its own purpose. The researchers call for more work on training language models to be honest reporters.OpenAI's Hugging Face incidentwas partly caused by agentic systemsthat prompted each other into misbehavior.

The differences between models line up with earlier measurements. Anthropic said at the launch ofClaude Opus 4.8that the model lets bugs in its own code pass without comment about four times less often than its predecessor.GPT-5.5pushed back on only about 45 percent of logically impossible questions in BullshitBench.

There are already approaches for more honest reports. OpenAI trained a version of GPT-5 Thinking toadmit its own rule violations in a separate reportand rewarded only honesty during that process. Anthropic usesPersona Vectorsto detect and steer traits like sycophancy inside the model, and showed that models thatgame rewards during trainingalso spontaneously learn to deceive and sabotage their own oversight.

 

### AI News Without the Hype – Curated by Humans

Subscribe to THE DECODER for ad-free reading, a weekly AI newsletter, our exclusive "AI Radar" frontier report six times a year, full archive access, and access to our comment section.

					Subscribe now				

## Read on for the full picture.Subscribe for hype-free coverage.

* Full access to every article on THE DECODER
* No ads
* Join the comments and community discussions
* A weekly AI news recap via mail
* 6x/year: "AI Radar" — deep dives on the AI topics that matter most
* Daily AI news, always up to date
* Our full ten-year archive
* Covered by a team with 10+ years in AI

Subscribe to The Decoder