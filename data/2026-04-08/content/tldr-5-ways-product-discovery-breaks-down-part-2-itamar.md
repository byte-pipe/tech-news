---
title: 5 Ways Product Discovery Breaks Down (Part 2) - Itamar Gilad
url: https://itamargilad.com/discovery-problems2/
site_name: tldr
content_file: tldr-5-ways-product-discovery-breaks-down-part-2-itamar
fetched_at: '2026-04-08T11:23:55.295268'
original_url: https://itamargilad.com/discovery-problems2/
author: Itamar Gilad
date: '2026-04-08'
published_date: '2026-04-06T09:52:56+00:00'
description: Why lack of infrastructure, partial validation, and no learning are hurting your product discovery efforts, and what to do about it.
tags:
- tldr
---

Why is product discovery — the practice of identifying the right things to buildbeforeswitching to delivery — so hard to implement? In myprevious articleI described two systemic problems:must-have featuresandweak goals. In this article I’ll focus on three key challenges that the are down to the product org itself.

## 1. Missing Infrastructure

As I teach product discovery, these challenges keep coming up:

* We can’t measure these metrics
* We don’t have an experimentation platform
* We don’t have user researchers or data analysts
* We launch only twice a quarter

These are objectively hard problems which, in my experience, product people often use as an excuse not to do product discovery. But these are also technical challenges that the product org is best positioned to address.

### Why is This Happening?

The most common reason is that product discovery is simply not a top priority — not for management and often not for the engineering team. The focus of both groups is on output — building and shipping stuff and discovery is left an orphan child.

### What Can You Do About It?

Make It a Top Priority

The infrastructure limitations mentioned above are objectively hurting the business. Without proper data you don’t know if what you’ve developed is making a difference or not (revenue is rarely a good product metric as it’s affected by many factors and slow to change). Without user researchers and data analysts you can’t know what your users are doing and why. Slow release cycles makes the company less responsive, dissatisfying customers and giving more agile competitors an edge.

Set Meta-Goals, Aim For Continuous Improvement

I often advise product leaders to set explicit goals for infrastructure improvements. Here’s a sample quarterly OKR:

O: Launch frequently and make evidence-guided decisions

* KR1: Double launch frequency from once a month to once every two weeks
* KR2: Validate at least 5 ideas using user interviews and surveys
* KR3: Run at least two A/B experiments that lead to pivot/persever/park decisions

The objective can persist for many quarters. The key results should reflect ambitious-yet-achievable targets for this quarter. Aim for continuous improvements rather than a few big leaps. If you were able to run just two experiments last quarter, aim to run 4.  If you’ve spent no time reviewing ideas with users last quarter, try to run 2 ideas in 6 user interviews. Don’t even wait a whole quarter to see if you made progress — set monthly improvement cycles and hold retrospectives at the end of each.

 
 

Join my newsletter to get articles like thisplus exclusive eBooks and templates by email

 
 
 
 
 
 
JOIN
 
 
 
 
 

Be Scrappy

Even if you work in a large company, chances are that your discovery infrastructure project will be underfunded and understaffed. This means you need to act more like a startup than an enterprise. As you’re developing for internal users, you can be scrappy and iterate through partial solutions and rough MVPs. This is especially true when you build yourdata system, as I’ve written before:

“Consider that even in data-driven companies many data projects are started bottom-up at the initiative of product teams. Don’t wait for permission and funding. Today there are many affordable off-the-shelf tools and open source solutions to get your started. If you’re just starting, I’d recommend against launching a massive data project that is likely to stretch from quarters to years. Instead start with measuring the things you really need to know now, and extend your data infrastructure and analysis over time.”

## 2. Partial Validation

I often meet teams that underdo the most important part of product discovery: idea validation — the iterative phase where you test the key assumptions underlying the ideaThese are common anti-patterns:

* Overly relying on validation techniques that generate weak evidence. For example launching a big new feature based solely on usability tests.
* Delaying validation until a very late stage where the new product change is mostly implemented (often called an “MVP test”). Due to the sunk-cost fallacy it’s very hard to pivot or park a bad idea at this stage, and the team is missing a lot of learnings it could have gained earlier at lower cost.

### Why Is This Happening?

Under-validation stems from a few core challenges:

* Time pressure — trying to cut the validation phase short so not to delay delivery. With AI-coding the pressure has become even more acute.
* Problem-focus — Some assume that product discovery is mostly about mapping out  the “problem space”; once that is done, validating the solutions is secondary. In reality it’s quite the opposite. There may be many ideas attached to a certain problem/opportunity/need, but only a few will work. Also some of the most important ideasdon’t come from opportunity mapping.
* Prioritization-focus — Some leaders and PMs are banking on a great prioritization process to tell them which ideas are the best. In practice no prioritization method (Ireviewedthemall) can predict which ideas will work and which will not. I’ve written before about this fallacy:“if you test your ideas rigorously, accurate prioritization is of far lower importance. You could pull ideas from a hat and still do OK.”

### What Can You Do About It?

Carve out Time and Resources for Validation

Here’s a fact that’s that most of your colleagues and managers don’t know: taking the time to experiment can5x-10x the valuethe product org creates for the business and for the users, while significantly shortening time-to-outcome. In other words it’s a crazy-good investment.

Here’s the contract you should establish with your colleagues: whatever the idea — even if it comes from an important customer or stakeholder —  the team is allowed to validate the key assumptions before switching to delivery. Discovery should be time-boxed, but rarely skipped.

Ideally you want to land on a plan that’s shaped like this:

A 
goal lifecycle
 that includes product discovery 

If your company uses some type of output roadmap (launches on a timeline, Now/Next/Later), start by prepending product discovery to each idea, and give the team the right to come back with contradicting evidence and alternative ideas.

Use the Concept of Confidence

My regular readers will be familiar with the Confidence Meter (free downloadhere) — a tool that estimates your level of confidence in an idea based on the evidence you’ve collected. Ideas that have only opinions and sparse data going for them get a low confidence score. Ideas that went through successful tests score much higher.

The Confidence Meter (free download 
here
)

Over the years I’ve gotten consistent feedback that the Confidence Meter is very effective in communicating to managers, stakeholders, and team that there’s simply not enough evidence to go by and that more validation is needed. I would go further and establish a rule that no idea goes into delivery unless it has beensufficiently validated.

## 3. No Learning

Experimenting alone is not enough. You need to interpret the results and take appropriate action.  Unfortunately that’s something many product companies still don’t do well:

* Interpreting results in an overly positive way (akamoving the goal posts): usually done by overly optimistic PMs and managers who are unwilling to admit that their pet idea is not working.
* Interpreting the results in overly negative way — Judging mixed results as failure (often done by engineers). Even good ideas need iteration, and less-than-perfect results are normal and often an opportunity for improvement.
* Not taking action — Not parking or pivoting ideas that don’t work. The temptation is to take the idea through one more test (or to rerun the last test), hoping that something will change for the better.

### Why Is This Happening?

Almost all product teams come from a legacy of plan-and-execute where modifying or canceling a project midway is considered failure. Similarly, many leaders and PMs are used to evangelizing their ideas, getting funding, and pushing them through at all costs. Admitting that the idea you were passionate about does not work was a big no-no in the past. I encounter also lack of know-how and experience in analyzing and interpreting results.

### What To Do About It?

Build the knowledge

This can be achieved by hiring people with experience in experimentation from companies that are good at it, andtraining. Some data and experimentation products help build better practices, and an early AI products are showing a lot of promise as well.

Define success criteria in advance

To avoid moving the goal posts at the end of the experiment it’s useful to determine what would be considered success (note: it’s a guess that sometimes may be adjusted down in hindsight). For example:

* At least 8 out of 10 participants will be able to complete task X
* Conversion rates will improve by at least 0.4% statistically significant.

Analyze with experts that have no skin in the game

* It’s a good idea to analyze experiment results with a user researcher or a data analyst (depending on the type of experiment).
* Seasoned product people may be able to help too. For example, Netflix holds weekly experiment analysis sessions where anyone can bring their data, and experienced practitioners help interpret it.
* AI is increasingly becoming good at results analysis, but as always, proper context and prompting make a big difference.

Ask the 3 questions:

In my eBookTesting Product IdeaI suggest asking these questions at the end of each experiment:

* Q1: Are the results positive, neutral or negative?That’s always a matter of interpretation.
* Q2: How strong is this evidence?Use the Confidence Meter to answer this one.
* Q3: What is the right next step?See the table below:

## Discovery is an Immediate Need

AI coding is making it easier to launch slop features and products. Performing research, evaluating ideas, and validating them has never been more important. AI can also help you introduce better product discovery by automating some of the hard parts and lowering costs (I plan to write a lot more on this topic —subscribe to my newsletterto get future articles), but the bigger challenges I listed have to be solved by humans. If you feel your organization needs to improve its product discovery, share this article broadly as a catalyst for discussion and action. If you’re interested in building your knowledge, consider joining one of my publicworkshopsor booking a workshop for your company.

Upcoming Workshops

Practice hands-on the modern methods of product management, product discovery, and product strategy.Secure your ticket for the nextpublic workshopor book aprivate workshoporkeynotefor your team or company.

My Book Evidence-GuidedisNow Available

“The grand unified theory of product management”“Best practical product management guide”“Top 5 business books I’ve read”

## Related Articles

* Think Learning, Not Experiments
* Why The Impact Effort Prioritization Matrix Doesn’t Work
* ICE Scores – All You Need to Know
Share with a friend or colleague