---
title: Design for Churn - DEV Community
url: https://dev.to/dailycontext/design-for-churn-5c6h
site_name: devto
content_file: devto-design-for-churn-dev-community
fetched_at: '2026-10-15T15:30:43.831025'
original_url: https://dev.to/dailycontext/design-for-churn-5c6h
author: Ben Halpern
date: '2026-10-14'
description: The biggest design shift of the AI era isn’t about who writes the code. It’s about how long the code... Tagged with aie, design, churn, ai.
tags: '#aie, #design, #churn, #ai'
---

The biggest design shift of the AI era isn’t about who writes the code. It’s about how long the code is expected to live.

Churn has always been a dirty word in software. Microsoft researchersshowed years agothat relative code churn predicts defect density. Adam Tornhill wrote a whole book calledYour Code as a Crime Scene, where frequently changed, complex files are the first suspects.GitClear’s researchprojected that AI assistants would double the share of code rewritten within two weeks of being written, and framed that as downward pressure on quality. The instinct runs deep: code that keeps changing is code that was wrong.

But that instinct comes from a world where writing code was expensive. Durability was how you got your money’s worth. When a feature costs an afternoon instead of a sprint, the math flips. Rewriting something is often cheaper than carefully preserving it, and that’s only going to become more true.

## Codebases are gardens now

We’ve always described software in building terms: architecture, foundations, scaffolding, load-bearing walls. Buildings are supposed to stand still.

I think codebases are becoming more like gardens. Specifically, gardens full of annuals. A gardener replants annuals every season, and nobody calls a tomato plant technical debt because it dies in October. The gardener’s real investment goes into whatdoesn’tturn over: the soil, the beds, the irrigation, the oak tree in the corner. Good structure is exactly what makes replanting cheap.

Code that churns a lot is essentially disposable, and disposable doesn’t have to mean sloppy. It can still be well made. It just isn’t made to last. Quality for an annual means it does its job, it’s tested at its edges, and it can come out without tearing up everything around it.

The problem is that we don’t have a picture of what high-quality churn looks like yet. Our mental model of quality is tangled up with longevity. We brag about code that has run untouched for six years. So churn happens anyway, but implicitly, and it lands wherever is most convenient.

## Where churn actually lands

I looked at the last six months ofForem: 563 commits. The most-churned file isapp/models/article.rb, touched in 37 of them.

Our spam handler is up there too, at 13. That one I’m happy about. Spam is a seasonal crop. Spammers change tactics constantly, and our code should churn right along with them.

article.rbis the oak tree. When the oak gets dug up every week, it means new features are rooting themselves in the core model because that was the easiest place to plant them. That’s the structural compromise. Churn isn’t the problem. Unplanned churn in load-bearing places is.

## Designing for it

A few ideas for making churn explicit instead of accidental:

Name the layers.Say out loud what’s an annual and what’s a perennial. OurAGENTS.mdalready does a crude version of this by telling AI assistants to tread carefully around core auth, feed sorting, and cache pipelines. That should be more than a warning label. It should be the shape of the codebase.

Put contracts at the edges of the beds.Interfaces, schemas, API specs, and tests that pin behavior rather than implementation are the perennials. Whatever sits behind them can be rewritten freely, by a person or an agent.

Make removal cheap.The test of a good annual is whether you can pull it out without disturbing the bed. If something is meant to churn, it shouldn’t have tendrils in everything.

Measure churn by layer.High churn in the fast layer is a sign of health. Churn in the slow layer is the alarm.

## Churn is a design input

Churn is going to happen either way. AI has made it the default rate of change for most of what we build. We can keep treating it as a symptom, or we can treat it as a design input and build the structure that lets us replant with confidence.

I will acknowledge that I have always been more of the perspective that churn is more acceptable than conventional wisdom of software design has implied. I’ve never seen the avoidance of churn as being a good thing in my practical experience. I used to see both sides of the argument, now I am staunchly in the camp that churn is positively associated with the quality and rigidity of our codebases and our systems.

I’d rather tend the garden than pretend it’s a building.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse