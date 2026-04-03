---
title: You Can Now Disable All AI Features in Zed — Zed's Blog
url: https://zed.dev/blog/disable-ai-features
site_name: hackernews_api
fetched_at: '2025-07-25T01:05:36.083071'
original_url: https://zed.dev/blog/disable-ai-features
author: meetpateltech
date: '2025-07-24'
published_date: 07/23/2025
description: 'From the Zed Blog: If you don’t want AI in your workflow, it won’t be there.'
tags:
- hackernews
- trending
---

← Back to Blog

# You Can Now Disable All AI Features in Zed

Our goal at Zed has always been to build the world’s best code editor.

For many, the best editing experience must include first-class agentic AI.
That’s why we’ve made Zedthe world’s fastest AI code editorand launched theAgentic Engineeringseries to explore how programmers can use AI effectively.

But we’ve heard from others on GitHubdiscussionsandissueswho either cannot or would prefer not to use Zed's AI features.
We’re here for you, too. You’re now able add a global setting to disable Zed AI to yoursettings.jsonfile:

{

 "disable_ai"
:
true

}

This change hits Preview today and will be in our Stable release next week.

And soon new users can also disable all AI features in Zed with a single switch during onboarding.

The disable AI switch during onboarding.

## Why disable AI?

Some developers have fundamental objections to AI in their coding process—whether it's concerns about training data, environmental impact, or philosophical reasons about machine-generated code.
You may prefer the predictability and control that comes with traditional development tools, without any AI suggestions interfering with your workflow.

Many organizations restrict AI tool usage, especially when working with proprietary code, and legal teams may require AI-free development environments.
Other companies have approved specific AI vendors that aren't available in Zed yet, or in editors generally.

We've heard these concerns from our users, and we agree these are valid engineering decisions.
Zed is built to respect your intent. If you don’t want AI in your workflow, it won’t be there.

## Privacy-first alternatives to disabling AI

If your concerns are only about data privacy, we offer several ways to stay secure:

* Bring your own keys:Easily connect to AI providersyou trust using your own API keys, giving you direct control over the vendor relationship.
* Keep it local: Zed also supportslocal AI modelsthat keep your code completely on your machine, so nothing ever leaves your development environment.

When you use our Zed AI service, your code and prompts are discarded after each request, never stored persistently, and never used for training.
We also maintain zero-retention agreements with Anthropic to ensure your code stays private.

## For the skeptics

We understand the apprehension around AI tools. They can be overhyped and inconsistent, and sometimes create questionable results.

You don't have to love it. But understanding it (so you can use it effectively, or choose not to) is becoming part of the craft.
That's why we launched ourAgentic Engineeringseries.
We're hoping to create a space for us to discuss and learn about practical techniques for maintaining craftsmanship while leveraging AI.

Even if you're skeptical, these tools are quickly becoming part of how software gets built.
Understanding them helps you make informed decisions about when and how to use them—or not use them.

## Your editor, your choice

Zed is built for engineers who care about their tools.
That means giving you control over your development environment, including the choice to work without AI if that's what works best for you.
Zed is also open-source underthe GPL license, so if you'd like to customize it even further, you are completely empowered to do so!

We'll continue to work towards our goal of making Zed the world's best code editor.
This meansadding support for Windows, improving our AI experience, and continuing to improve our experience for those who won't be using AI at all.
