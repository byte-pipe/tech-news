---
title: Slop Is Not Necessarily The Future | Greptile Blog
url: https://www.greptile.com/blog/ai-slopware-future
site_name: hnrss
content_file: hnrss-slop-is-not-necessarily-the-future-greptile-blog
fetched_at: '2026-04-01T11:24:29.875912'
original_url: https://www.greptile.com/blog/ai-slopware-future
date: '2026-03-31'
published_date: '2026-03-31T12:00:00'
description: Everyone's worried about slop, but good code will prevail, not only because we want it to, but because economic forces demand it.
tags:
- hackernews
- hnrss
---

# Slop Is Not Necessarily The Future

Soohoon Choi • Mar 31, 2026

Table of Contents

### Table of Contents

### Table of Contents

A couple of years ago, "slop" became the popular shorthand for unwanted, mindlessly generated AI content flooding the internet including images, text, and spam. Simon Willison helped popularize the term, though it had been circulating in engineering communities in the years prior.

At Greptile, we spend a lot of time thinking about questions like: Is slop the future? Are programming best practices now a thing of the past? Will there be any reason at all for AI coding tools to write what we call good code going forward?

I want to argue that AI models will write good code because of economic incentives. Good code is cheaper to generate and maintain. Competition is high between the AI models right now, and the ones that win will help developers ship reliable features fastest, which requires simple, maintainable code. Good code will prevail, not only because we want it to (though we do!), but because economic forces demand it. Markets will not reward slop in coding, in the long-term.

## What's Happening Now?

Software development is changing fast. A prominent recent example comes from Ryan Dahl, creator of Node.js, who wrote, "The era of humans writing code is over. Disturbing for those of us who identify as SWEs, but no less true."

Meanwhile, the complexity of the average piece of software is drastically increasing. In our 2025 State of AI Coding report[1], lines of code per developer grew from 4,450 to 7,839 as AI coding tools became standard practice. Median PR size increased 33% from March to November 2025, rising from 57 to 76 lines changed. Individual file changes became 20% larger and "denser."

The stats suggest that devs are shipping more code with coding agents. While this is exciting, like many other developers I am quite alarmed by this progression. The worry is that AI slop is being shipped into production systems at an ever increasing rate leading to mass distribution of bad software. The consequences may already be visible: analysis of vendor status pages[2]shows outages have steadily increased since 2022, suggesting software is becoming more brittle. Engineers understand this, Andrej Karpathy[3]describes: "agents bloat abstractions, have poor code aesthetics, are very prone to copy pasting code blocks and it's a mess, but at this point I stopped fighting it too hard and just moved on."

Collectively, software engineers are cranking out code at a high quantity. And there seems to be no reason for "good" code. Most users get what they asked for, model labs get paid per token, and developers get to ship without thinking too hard.

## Why "Good Code" Will Win

InA Philosophy of Software Design[4], John Ousterhout argues that complexity is the #1 enemy of well-designed software. Broadly he argues that good code is:

* Simple and easy to understand
* Easy to modify

Bad code is the opposite, needs lots of context and mental bandwidth to understand and is almost impossible to modify.

This principle applies the same for AI agents. AI will write good code because it is economically advantageous to do so. Per our definition of good code, good code is easy to understand and modify from the reduced complexity. This means it requires less context to understand a relevant piece of code and fewer lines of code to be written to achieve some change. Translating this to token economics, we can clearly see the parallels: it is more token efficient to write and maintain software with good code.

By contrast, complex code doesn't scale. It requires a lot of tokens and compute, and as codebases grow, it gets exponentially more expensive.

## What This Means

We're still early in the AI coding adoption curve. As the technology and competition matures, economic forces will drive AI models toward generating good, simpler, code because it will be cheaper overall.

The world right now is focused on getting AI to work in the first place, not on optimizing its abilities. We are going through a particularly messy phase of innovation. Once AI code generation becomes ubiquitous, I believe that economic incentives will start to take effect and AI models will be forced to generate good code to stay competitive amongst software developers and companies.

## References

[1]
State of AI Coding report
[2]
Analysis of vendor status pages
[3]
Andrej Karpathy
[4]
A Philosophy of Software Design

## Keep Reading

### Series A and Greptile v3

Announcing Greptile's $25M Series A led by Benchmark Capital and unveiling Greptile v3—our most advanced AI code reviewer that catches 3x more critical bugs.

Sep 23, 2025
•
Daksh Gupta

### How to Make LLMs Shut Up

Lessons learned from our challenges reducing LLM output: Discover everything that went wrong when trying to make our models say less.

Dec 18, 2024
•
Daksh Gupta

### Greptile's work culture

A from-the-source outline of our work culture, so potential teammates can self-assess their fit.

Sep 10, 2025
•
Daksh Gupta
Newsletter

### Subscribe to our blog

Get the latest posts and product updates delivered to your inbox

Subscribe
Demo

### See Greptile in action

Book a personalized demo to see how Greptile can help your team ship faster

Schedule Demo
