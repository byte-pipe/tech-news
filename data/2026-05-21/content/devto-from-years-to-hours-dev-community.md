---
title: From Years to Hours - DEV Community
url: https://dev.to/annaspies/from-years-to-hours-joe
site_name: devto
content_file: devto-from-years-to-hours-dev-community
fetched_at: '2026-05-21T19:36:31.225941'
original_url: https://dev.to/annaspies/from-years-to-hours-joe
author: Anna
date: '2026-05-21'
description: It's not a brag for me to say "I've been visualizing infrastructure since 2018" - it's the actual... Tagged with ai, stripe, cli, agents.
tags: '#ai, #stripe, #cli, #agents'
---

It's not a brag for me to say "I've been visualizing infrastructure since 2018" - it's the actual truth. That was the year I joined a lovely Portland-based startup calledStackery, which took infrastructure as code (IaC for those familiar) and generated an architecture diagram that looked like this:

The secret sauce was that it went both ways: drag and drop resources, get IaC back that you can then deploy. Though the startup has not existed since 2021, you can actually still play with thelive editor;)

Why am I bringing up ancient history? Well, Stackery went on to be acquired by AWS (something I can say now that I'm no longer employed by them) and becameAWS Infrastructure Composer(née Application Composer), which takes infrastructure as code and generates an architecture diagram that looks like this:

And it also works both ways: drag and drop resources, get a Cloudformation template that you can then deploy. More importantly though, it's a powerful way to visually understand the distributed systems that make up serverless services and how they interact with each other.

## Modern times

Today I'm at Stripe, which is not a cloud provider, so one would think there's no use case for visualizing IaC at my new job.

That was true until last month, whenStripe Projectswas released and suddenly the Stripe CLI became a means to buildinganything!

With Projects, anyone can use the Stripe CLI to provision services from a quickly-expandingcatalogof providers for hosting, auth, AI, databases, and so on - just about anything a hobby or real-world application may need. More commonly though, users are setting up their agents with the CLI and saying "build me an app that does X" and the agent can figure out that this use case requires a database and provision it straight from the CLI, as the gods intended.

So now we have an application composed of multiple services with increasing complexity that the developer may not fully understand - sound familiar for anyone around in the #believeinserverless days?

## Visualizing Projects

I used Projects recently to build a transcription app for my team and wrote about the process here:From init to deploy. Even though that application is fairly simple and uses just two providers, Vercel and OpenRouter, I still thought a visualization would be useful for any of my teammates wanting to contribute to it, so I built astripe-projects-visualizerapp in a somewhat manic single afternoon.

This app looks at a project's.projects/state.jsonfile, which is the source of truth for its provisioned services, analyzes how provider environment variables are used throughout the codebase, and comes up with an architecture diagram showing how your provisioned services connect and how data flows between them.

For example, here's the generated diagram for my transcription app:

## From years to hours

Is this tool cool and useful? Sure, I'd like to think so. Is it missing features? Of course, but not as many as one would think for the time spent on it. My biggest takeaway from building it in one afternoon is thatI could.

Stackery took six engineers many, many years to build and maintain. Infrastructure Composer started with five engineers, then expanded to nearly a dozen plus a UX team, but even the initial preview version launched at re:Invent 2022 took over 9 months of intense building. Then, my former team spent another year re-architecting the canvas part of it to be more portable and extensible.

The Stripe Projects Visualizer tookone person one afternoonto build. I could probably launch a web app version of it tomorrow. This is an entirely different paradigm than I was in eight years ago. It's entirely different from eight months ago, when I was still fumbling while trying to use Kiro and Claude Code to improve the underlying canvas tech of Infrastructure Composer.

I almost titled this post "The Terrifying Reality of Years to Hours" because in some aspects (the ones where I would very much like to stay employed), this is terrifying. Security aspects as well, for that matter, though my adversarial agent assures me there are no security gaps in my repo (whew!).

But this is also exciting, because projects that would have taken years or never gotten off the ground now have a chance to at least exist in a rough state that a team can polish and maintain.

So I guess I'm along for the terrifyingly awesome ride.

If you want to be as well, give Stripe Projects a try:

brew 
install 
stripe/stripe-cli/stripe 
&&
 stripe plugin 
install 
projects

Enter fullscreen mode

Exit fullscreen mode

then visualize your terrifyingly awesome creation with:

npx stripe-projects-visualizer visualize

Enter fullscreen mode

Exit fullscreen mode

Let's see what you come up with!

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse