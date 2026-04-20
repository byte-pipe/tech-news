---
title: 'AI Evals in the Real World: Human Judging, LLM Judges, and the Gaps Between'
url: https://datasciencexai.substack.com/p/ai-evals-in-the-real-world-human
site_name: tldr
content_file: tldr-ai-evals-in-the-real-world-human-judging-llm-judge
fetched_at: '2026-03-07T06:00:37.145861'
original_url: https://datasciencexai.substack.com/p/ai-evals-in-the-real-world-human
author: Stella Liu
date: '2026-03-07'
description: The Hidden Complexity of Evaluating AI Customer Service Chatbots
tags:
- tldr
---

# AI Evals in the Real World: Human Judging, LLM Judges, and the Gaps Between

### The Hidden Complexity of Evaluating AI Customer Service Chatbots

Stella Liu
Mar 02, 2026
12
1
4
Share

This week I’m excited to share a guest post fromYe Yuan.

Ye brings a rare mix of academic rigor and shipped-product pragmatism to AI evals. She holds a PhD in Applied Linguistics and Education, and has spent years studying how humans learn and use language. She’s also applied that lens directly to GenAI product development.

In the post below, she shares how her team at a leading tech firm in China, evaluated a sophisticated customer support system using a hybrid approach, combining human judgment with automated evaluation, and the real-world constraints they ran into along the way.

The AI evals space is moving fast. The only way we keep up is by learning from each other’s wins, failures, and the messy in-between.

Subscribe

## Context: what we built and what “success” meant

As an AI Product Manager, I previously led conversational optimization for an AI-powered customer service system at a large tech company. Our chatbot handled high-volume inbound traffic from search engine ads across diverse verticals: travel, healthcare, education, legal services, and more.

The business objective was not only to answer user questions, but also to sustain engagement and capture contact information for downstream human sales follow-up. In this post, I’ll share the evaluation framework we developed, the hybrid approach we adopted, and the challenges we encountered along the way.

## Why traditional NLP metrics didn’t work

Traditional NLP metrics were insufficient for our use case. They could not capture whether the AI sustained multi-turn interactions, handled intent shifts, or progressively uncovered user needs in a way that moved the conversation forward.

So we designed a task-specific evaluation framework benchmarked against high-performing human sales and support interactions.

## Our rubric: three dimensions of quality

Our rubric centered on three core dimensions, each broken down into fine-grained criteria with anchored rating scales:

1. Resolution capabilityDid the system correctly infer user intent and provide accurate, relevant answers?
2. Commercial effectivenessCould the system maintain engagement, probe deeper into user needs, and gradually guide the user toward leaving contact information when appropriate?
3. Conversational naturalnessDid the dialogue feel pragmatically human, in terms of discourse coherence, logical structure, appropriate follow-ups, and conversational flow?

## Our workflow: human evaluation + LLM-as-a-judge

Our evaluation process adopted a hybrid framework combining human evaluation with LLM-as-a-judge. In general, subjective evaluation remained primarily human-led, while objective evaluation was more often automated using LLMs.

LLM-as-a-judge in our setup relied on two approaches: prompt-based general-purpose LLMs and task-specific fine-tuned models. When evaluation criteria could be clearly defined and operationalized, well-designed prompts enabled LLMs to deliver reasonably reliable assessments at scale. However, when the criteria were ambiguous or difficult to formalize, we incorporated human-annotated data to train specialized judge models for more consistent and precise evaluation.

At a high level, the loop looked like this:

1. Run automated evaluations at scale
2. Retain human spot-checking for quality assurance
3. Manually review all low-scoring dialogues for error analysis
4. Feed identified failure patterns into the next iteration of conversation design

This semi-automated loop helped us balance scale with oversight, but it also introduced new challenges.

## What broke in practice: three bottlenecks

#### Bottleneck 1: annotation capacity and calibration

One major bottleneck was annotation capacity. To build a gold dataset, we invested heavily in annotator training and repeated calibration rounds to ensure intercoder reliability. Vertical-specific product managers reviewed annotated samples before admitting them into the gold dataset.

This process produced high-quality labels, but it was expensive and time-consuming.

#### Bottleneck 2: gold data scarcity and synthetic data mismatch

Even with significant investment, the resulting gold dataset was often too small to meet the data demands of model training and evaluation.

To augment limited gold data, we generated synthetic conversations using LLMs. However, these conversations often failed to reflect the ambiguity and emotional or topical shifts seen in real user traffic. Models trained or evaluated on synthetic data could easily overestimate performance, especially when deployed to real-world edge cases.

#### Bottleneck 3: judge-model instability on pragmatics

Judge-model stability posed another challenge. In particular, LLM-based judges struggled with pragmatic subtleties, implicit meanings, and user silence. Score variance across runs could be significant.

At the same time, scaling human evaluation to real-time production volumes was operationally infeasible. This created a practical tension: automated judging was necessary for scale, but it was least reliable precisely where conversational quality became most nuanced.

## The hardest question: what does “human-like” mean?

The most conceptually difficult part of evaluating AI conversations was defining “human-likeness.”

Operationalizing human-like conversation requires grappling with context sensitivity, turn-taking dynamics, empathy modeling, discourse-level coherence, and more. It also forces deeper questions: what level of human equivalence should current AI systems be expected to achieve?

This is why AI evaluation is not just a technical measurement problem. It reflects product positioning and calibration of expectations. And when quality criteria involve complex or ambiguous values, alignment across stakeholders becomes essential.

## What I learned: the structural constraints underneath it all

Reflecting on these challenges, I’ve come to see them as symptoms of three structural constraints: model capability, human resources, and scope.

First, if we want to move toward more automated evaluation, LLMs need to become more reliable in pragmatic reasoning.

Second, a professionally trained annotation workforce is critical for maintaining evaluation quality and consistency.

Finally, evaluation cannot be owned by a single function. It requires cross-functional collaboration to build a more comprehensive, less biased understanding of quality and to align on what “good” means.

The AI Evals space is evolving fast, and I’m eager to keep comparing notes with practitioners, learning from what works, and being honest about what doesn’t. If this resonates, I’d love to connect on LinkedIn and continue the conversation.

Ye is a learner in ourAI Evals & Analytics Playbookcourse. If you want to learn the latest in AI evals, sharpen best practices, and connect with builders who are actually deploying evals in the wild, come hang with us in an upcoming cohort.

12
1
4
Share
