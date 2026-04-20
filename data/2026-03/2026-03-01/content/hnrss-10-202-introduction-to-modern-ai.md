---
title: '10-202: Introduction to Modern AI'
url: https://modernaicourse.org
site_name: hnrss
content_file: hnrss-10-202-introduction-to-modern-ai
fetched_at: '2026-03-01T19:09:23.282329'
original_url: https://modernaicourse.org
date: '2026-03-01'
description: '10-202: Introduction to Modern AI (CMU)'
tags:
- hackernews
- hnrss
---

# 10-202: Introduction to Modern AI

## Logistics

* Course Instructor:Zico Kolter
* Lectures:MW[F] 9:30–10:50 Tepper 1403 (note: Friday lectures will only be used for review sessions or makeup lectures when needed)

## Online Course

 A minimal free version of this course will be offered online, simultaneous to the CMU offering, starting on 1/26 (with a two-week delay from the CMU course). This means that
all content
 (lecture videos, assignments available on mugrade, etc) will be available to the online course
two weeks
 after the dates indicated in the schedule below. By this, we mean that anyone will be able to watch lecture videos for the course, and submit (autograded) assignments (though not quizzes or midterms/final).
Enroll here
 to receive emails on lectures and homeworks once they are available. Note that information here about TAs, office hours, grading, prerequisites, etc, are for the CMU version, not the online offering.



## Syllabus Overview

This course provides an introduction to how modern AI systems work. By “modern AI”, we specifically mean the machine learning methods and large language models (LLMs) behind systems like ChatGPT, Gemini, and Claude.[Note]In most academic settings, the term “Artificial Intelligence” refers to techniques much broader than machine learning and LLMs. However, in modern usage the term often refers to these kind of AI systems like chatbots that many of us use every day, and for this course we’ll use this common-usage sense.Despite their seemingly amazing generality, the basic techniques that underlie these AI models are surprisingly simple: a minimal LLM implementation leverages a fairly small set of machine learning methods and architectures, and can be written in a few hundred lines of code.

This course will guide you through the basic methods that will let you implement a basic AI chatbot. You will learn the basics of supervised machine learning, large language models, and post-training. By the end of the course you will be able to write the code that runs an open source LLM from scratch, as well as train these models based upon a corpus of data. The material we cover will include:

* A brief history of AI
* Supervised machine learningLinear modelsLoss functions and optimizationNeural networks
* Linear models
* Loss functions and optimization
* Neural networks
* Large language modelsSelf attention and transformersTokenizersEfficient inference
* Self attention and transformers
* Tokenizers
* Efficient inference
* Post-trainingSupervised fine tuningAlignment and instruction tuningReasoning models and reinforcement learningSafety and security of AI systems
* Supervised fine tuning
* Alignment and instruction tuning
* Reasoning models and reinforcement learning
* Safety and security of AI systems

The topics above are a general framing of what the course will cover. However, as this course is being offered for the first time in Spring 2026, some elements are likely to change over the first offering.

## Grading

* 20% - Homework and Programming Assignments
* 40% - Homework Quizzes
* 40% - Midterms and Final (10% each midterm, 20% final)

## Prerequisites

* Programming:15-112 or 15-122. You must be proficient in basic Python programming, including object oriented methods.
* Math:21-111 or 21-120. The course will use basic methods from differential calculus, including computing derivatives. Some familiarity with linear algebra and probability is also beneficial, but these topics will be covered to the extent needed for the course.

## Homework and Programming Assignments

A major component of the course will be the development of a minimal AI chatbot through a series of programming assignments. Homeworks are submitted usingmugradesystem (tutorial video). Some assignments build on previous ones, though for the in-class CMu version we'll distribute solutions to help you work through any errors that may have cropped up in previous assignments (for the online version, we'd suggest talking to others who were able to complete the assignment). In addition to the (main) programming aspect, some homeworks may contain shorter written portion that works out some of the mathematical details behind the approach.

All homeworks are released as Colab notebooks, at the links below. We are also releasingMarimonotebook versions. The mugrade version of the online assignment will be available two weeks after the release dates for the CMU course.

* Homework 0: Autograding and programming basics(marimo)
* Homework 1: Introduction to linear algebra and PyTorch(marimo)
* Homework 2: Automatic differentiation and training a linear model(marimo)
* Homework 3: Training a neural network
* Homework 4: Implementing a Transformer
* Homework 5: Implementing an minimal LLM
* Homework 6: Supervised finetuning and chat training
* Homework 7: Reinforcement Learning

Each homework will be accompanied by an in-class (15 minute) quiz that assesses basic questions based upon the assignment. This will include replicating (at a high level) some of the code you wrote for the assignment, or answering conceptual questions about the assignment. All quizzes are closed book and closed notes.

## Midterm and Final

In addition to the homework quizzes, there will be 3 in-person exams, two midterms and a final (during finals period). The midterms will focus on material only covered during that section of the courses, while the final will be cumulative (but with an emphasis on the last third of the course). All midterms and final and closed book and closed notes.

## Lectures

Lecture schedule is tentative and will be updated over the course of semester. All materials will be available to the online course two weeks after the dates here.

Date

Lecture

Homework

1/12
Class logistics and a brief history of AI (
video 1
,
video 2
)
HW0 Out

1/14
Intro to supervised learning (
video
)

1/19
MLK Day - no class

1/21
Linear algebra and PyTorch (
video
)
HW0 Due

1/28
Linear models (
video
)
HW1 Out

1/30
Loss functions and probability (
video
)

2/2
Optimization and gradient descent (
video
)

2/4
(moved to 2/6)
HW1 Due

2/6
Putting it together: Training a linear model (
video
)/td>
HW2 Out

2/9
Neural networks models (
video
)

2/11
Neural network implementation
HW2 Due

2/16
Midterm 1 - Supervised machine learning
HW3 Out

2/18
Sequence models: handling sets of inputs

2/23
Self attention and positional embeddings

2/25
Transformer models
HW3 Due, HW4 Out

3/2
Spring break - no class

3/4
Spring break - no class

3/9
Tokenizers

3/11
Efficient inference and key-value caching
HW4 Due

3/16
Putting it together: your first LLM
HW5 Out

3/18
Midterm 2 - Large Language Models

3/23
Supervised fine tuning

3/25
Alignment and instruction/chat tuning

3/30
Guest lecture
HW5 Due, HW6 Out

4/1
Guest lecture

4/6
Reinforcement learning basics
HW6 Due

4/8
RL for LLMs

4/13
Reasoning models
HW 7 Out

4/15
AI Safety and security

4/20
The future: AGI and beyond
HW7 Due

4/22
Instructor Q&A

TBD
Final

## AI Policy for the AI course

Students are permitted to use AI assistants for all homework and programming assignments (especially as a reference for understanding any topics that seem confusing), but we strongly encourage you to complete your final submitted version of your assignment without AI. You cannot use any such assistants, or any external materials, during in-class evaluations (both the homework quizzes and the midterms and final).

The rationale behind this policy is a simple one: AI can be extremely helpful as a learning tool (and to be clear, as an actual implementation tool), but over-reliance on these systems can currently be a detriment to learning in many cases. Youabsolutelyneed to learn how to code and do other tasks using AI tools, but turning in AI-generated solutions for the relatively short assignments we give you can (at least in our current experience) ultimately lead to substantially less understanding of the material. The choice is yours on assignments, but we believe that you will ultimately perform much better on the in-class quizzes and exams if you do work through your final submitted homework solutions yourself.
