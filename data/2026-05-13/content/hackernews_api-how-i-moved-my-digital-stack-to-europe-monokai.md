---
title: How I Moved My Digital Stack to Europe — Monokai
url: https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/
site_name: hackernews_api
content_file: hackernews_api-how-i-moved-my-digital-stack-to-europe-monokai
fetched_at: '2026-05-13T19:36:37.148019'
original_url: https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/
author: Monokai
date: '2026-05-13'
description: On digital sovereignty, and why European cloud is better than you think
tags:
- hackernews
- trending
---

# How I Moved My Digital Stack to Europe

 

## On digital sovereignty, and why European cloud is better than you think

 

April 29, 202610 min.Digital SovereigntyDigital InfrastructureDigital AutonomyEuropean CloudEurope

 
 
 
 
 
100% accurate European digital infrastructure, AI generated
 

There’s a version of this post that starts with a spreadsheet and ends with a quiet sense of satisfaction. That’s mostly how it went. But underneath the practical exercise of swapping one SaaS tool for another was something that felt more urgent, a growing discomfort with how much of my digital infrastructure sat on servers I didn’t control, in a jurisdiction increasingly prone to unpredictability, operated by companies whose incentives don’t always align with mine.

 
 

Digital sovereigntysounds like a buzzword until you think carefully about what it means. It means knowing where your data lives. It means not being one policy change, one acquisition, or one executive’s bad mood away from losing access to tools your business depends on. It means choosing infrastructure based on values, not just convenience.

 
 

So I started migrating.

 
 
 

## Analytics

 
 
 
 
 
 
 
Google Analytics
 
 
 
 
 
 
 
 
 
Matomo
 
 
 

Google Analytics was the obvious first target. It’s the canonical example of a service that’s free becauseyouare the product, your visitors’ behavior funneled back into Google’s advertising machinery.

 
 

Self-hostingMatomosolved this cleanly. The data stays on myown serverI had to instantiate a new small server for this, which is cheap, but not free., and I’m fully GDPR-compliant without the cookie consent theater that Google Analytics typically requires. The reporting is comprehensive, the interface is familiar enough, and I own everything.

 
 

The main downside is maintenance overhead. You’re now responsible for updates, backups, and keeping the server healthy. For most setups this is low-friction, but it’s not zero friction.

 
 
 

## Email

 
 
 
 
 
 
 
Google Workspace
 
 
 
 
 
 
 
 
 
Proton Mail
 
 
 

Proton Mailis based in Switzerland, not EU territory, but Swiss privacy law is closely aligned with GDPR and arguably stronger in some respects. Proton builds its business model around privacy rather than advertising, and end-to-end encryption is baked in at the protocol level rather than bolted on. The email client is solid, the calendar works well, and for anyone moving away from US-based services, it sits comfortably in the same spirit as the rest of this stack.

 
 

One adjustment is getting used to Proton’s filter system, which is a bit more limited than Gmail’s. Gmail lets you write filters against virtually anything, including the full body of the message. Proton doesn’t support filtering on email content at all. So if you’ve built a workflow around catching specific phrases or keywords in message bodies, you’ll have to rethink it. For most people this won’t be a dealbreaker, but it’s worth knowing before you migrate.

 
 

There’s also a practical limitation worth flagging: Proton caps custom domains at three, even on the Duo plan. If you run several domains, like separate addresses for different projects or businesses, you’ll hit that ceiling quickly and need to rethink how you route and send mail. I ended up consolidating, which was probably overdue anyway, but it wasn’t a choice I made entirely freely.

 
 

Proton isn’t free and charges a substantial fee compared to other options. You’ll get access to a whole suite of Proton apps though.

 
 
 

## Password Management

 
 
 
 
 
 
 
1Password
 
 
 
 
 
 
 
 
 
Proton Pass
 
 
 

Once I was in the Proton ecosystem, moving password management there as well made sense.Proton Passis end-to-end encrypted, open source, and benefits from the same Swiss jurisdiction as the rest of Proton’s stack.

 
 

1Password is a genuinely great product and this was a lateral move more than an upgrade. The interface is simple, the browser extension works reliably, and having passwords, email, and calendar under one encrypted roof has a certain satisfying coherence to it.

 
 
 

## Compute

 
 
 
 
 
 
 
DigitalOcean
 
 
 
 
 
 
 
 
 
Scaleway
 
 
 

DigitalOcean has earned its reputation by doing one thing exceptionally well: getting out of your way. The UI is clean, the mental model is simple, and spinning up infrastructure never feels like a chore. It’s the platform that proved developer experience could be a competitive moat.

 
 

Scalewaywas a pleasant surprise. I expected a capable-but-rough European alternative, but what I found was a platform that’s genuinely well thought out. Servers spun up quickly inside a private network of my own configuration, the control panel is clean, and the options available matched everything I actually needed. Scaleway displays projectedCO₂ emissionsThis actually made me host most of my infrastructure in Paris, where Compute consumes the least energy.alongside server location choices, a nice touch.

 
 
 

## Object Storage

 
 
 
 
 
 
 
Amazon Web Services
 
 
 
 
 
 
 
 
 
Scaleway
 
 
 

Scaleway’s object storage is S3-compatible, which makes migration mechanical rather than painful, update your endpoint and credentials and existing code works unchanged.

 
 

I used a tool calledrcloneto sync my old AWS S3 storage buckets to the new Scaleway S3 buckets. This took a little more than a week of constant syncing, as these buckets were quite large.

 
 
 

## Offsite Backups

 
 
 
 
 
 
 
Backblaze
 
 
 
 
 
 
 
 
 
OVHcloud
 
 
 

OVHis the largest European cloud provider and brings the reliability and pricing you’d expect at that scale. Their object storage works well as a backup destination and ends up cheaper than Backblaze B2 once you configure lifecycle rules to move older backups to the cold storage class.

 
 

Getting there, however, requires some patience. The OVHcloud control panel is a labyrinth: the lifecycle rule configuration is buried somewhere in the documentation, and it involves some work in the terminal. Once it’s set up, it works reliably and the cost difference is meaningful.

 
 
 

## Transactional Emails

 
 
 
 
 
 
 
Twilio SendGrid
 
 
 
 
 
 
 
 
 
Lettermint
 
 
 

Lettermintis a European transactional email service that does the job without the bloat. Deliverability is solid, the API is clean, and it hasstraightforward pricingI cut some costs with this move, as I had two separate SendGrid accounts which I could now merge into one..

 
 

Compared to SendGrid, the analytics are leaner and the ecosystem integrations are fewer. SendGrid has years of tooling, documentation, and community answers behind it. Lettermint is newer and smaller. For most transactional sending use cases (password resets, notifications, receipts) that doesn’t matter much. But if you’re doing complex multi-stream email infrastructure, you’ll want to audit the feature set carefully first.

 
 
 

## Error Tracking

 
 
 
 
 
 
 
Sentry
 
 
 
 
 
 
 
 
 
Bugsink
 
 
 

Bugsinkis a self-hosted error tracking tool that accepts Sentry’s SDK, which means the migration path is almost frictionless, change one line of configuration and you’re done.

 
 

To be honest: Bugsink is bare-bones. There’s no performance monitoring, no session replays, no advanced alerting. It’s not a Sentry replacement for teams that use Sentry properly. For me, it’s a simple remote error log, when something breaks in production I get a stack trace and that’s enough. Sentry’s cloud product is genuinely excellent if you need the full feature set, and for larger engineering teams the breadth almost certainly justifies the cost. But if your use case is “tell me when something broke and show me the stack trace”, self-hosted Bugsink does exactly that with no data leaving your infrastructure.

 
 
 

## AI API integration

 
 
 
 
 
 
 
OpenAI
 
 
 
 
 
 
 
 
 
Mistral
 
 
 

For my AI API integrations, I switched from OpenAI to Mistral. It worked out perfectly as I was mostly using simpler models anyway.

 
 

Mistralis headquartered in Paris and has published compelling open-weight models alongside its API offering. The API is clean, the models are fast and capable, and there’s something coherent about a European AI provider that leans into openness rather than away from it. For my inference workloads, the switch was lateral in quality and meaningfully better in terms of where the money goes.

 
 
 

## CDN

 

### Exception № 1

 
 
 
 
 
 
 
Cloudflare
 
 
 

Not everything moved.Cloudflareis a US company, I still use it, and I’m at peace with that.

 
 

Here’s the reasoning: Cloudflare sits in front of my public-facing websites. Its job is to cache, protect against DDoS attacks, and make content load fast for visitors around the world. The data flowing through it is already public by definition. I’m not routing private communications or sensitive application data through Cloudflare; I’m using it to serve pages that anyone on the internet can read. The sovereignty calculus is different when the thing you’re protecting is already public.

 
 

I did tryBunny CDN, which is European-based and has a great reputation. For straightforward CDN use it’s excellent. But Cloudflare’s feature set (security rules, Workers platform, breadth of configuration options) wasn’t matched closely enough to justify the switch for my specific needs. Sometimes the pragmatic answer wins.

 
 
 

## Payments

 

### Exception № 2

 
 
 
 
 
 
 
Stripe
 
 
 
 
 
 
 
 
 
Mollie
 
 
 

Stripe is one of the few services I haven’t moved yet, even though payment infrastructure is exactly the kind of thing I care about having in a jurisdiction I trust.Mollieis a Dutch payment processor with full EU incorporation, strong GDPR compliance by design, and a product that has matured considerably in recent years. The API has converged toward parity for most common payment flows, and for a European business the regional payment method coverage (iDEAL, Bancontact, SEPA) is arguably better.

 
 

The migration is on the list. It’s just not a trivial one. Payment integrations touch billing logic, webhooks, tax invoicing and customer-facing flows in ways that require careful testing and a good moment to cut over. It’s also more expensive than Stripe for my usecase.

 
 
 

## AI Code assistance

 

### Exception № 3

 
 
 
 
 
 
 
OpenAI
 
 
 
 
 
 
 
 
 
Claude Code
 
 
 
 
 
 
 
 
 
Qwen
 
 
 

This one felt overdue. OpenAI works fine, but the company’s trajectory doesn’t align with my own views anymore. After a period of deliberate drift, I felt the need to switch. Ideally I wanted to useMistral Vibehere, but it just didn’t make the cut as it couldn’t compete with Claude.

 
 

Claude Codeis now my day-to-day AI assistant for coding. The reasoning quality is strong, the context handling is genuinely impressive, and Anthropic’s approach to safety and transparency feels more structurally grounded.

 
 

Anthropic is a US company, so this doesn’t satisfy the jurisdictional criterion I applied elsewhere. But it satisfies something else, the sense that the organization building the thing has given serious thought to what it’s building and why.

 
 

It’s also worth noting that local models are becoming increasingly viable.Qwen, Alibaba’s open-weight model family, is a strong example: capable enough for many real workloads, running entirely on your own hardware, with no data leaving your machine. The gap between frontier API models and what you can run locally is narrowing faster than most people realize.

 
 

Not everything is ideal. Most data centers still sit outside Europe, and “open” means different things to different organizations. But the direction is right. A world where capable AI runs on your own hardware, with published weights and transparent training, is a much better world for digital autonomy than one where all inference routes through a handful of closed API providers. We’re not there yet, but the trajectory is encouraging.

 
 
 

## Git Version Control

 

### Exception № 4

 
 
 
 
 
 
 
GitHub
 
 
 
 
 
 
 
 
 
GitLab
 
 
 

GitLabalso remains for now. GitLab is headquartered in the US but offers self-hosted options, and the company has long had a strong commitment to transparency and open source. A self-hosted instance is on the roadmap, but moving source control is a more significant undertaking than most of these migrations.

 
 

GitHubstays in the picture for one specific purpose: public-facingNPM packagesand issue tracking for open source software. When you publish a package or maintain public tooling, GitHub is where developers expect to find it. The network effects are real, it’s where the forks, stars, and issue reports come from. For the public-facing surface of open source work, there’s no meaningful sovereignty concern and a lot of practical upside.

 
 
 

## Was it worth it?

 

The practical friction was real but manageable. Most migrations were an afternoon of work: update a credential here, point a DNS record there, export and import some data. A few took longer. None were catastrophic. All in all it took longer than expected, but most time was spent in researching and planning when to do what. Two months in, everything is running without incident. No fires, no regrets.

 
 

Digital sovereignty isn’t about paranoia. It’s about being conscious about your infrastructure, where you decide who holds your data, who can reach it, and what happens when politics shift. The tools are there. The ecosystem is mostly mature. The only thing that was stopping me was inertia. It’s entirely possible to run a reliable, capable, professional digital stack mostly from European infrastructure. This migration was proof of that.

 
 

## Monoco — squircle shapes for HTML elements

 

NPM package available for vanilla JavaScript, React and Svelte.

 

## Monokai Pro: beautiful functionality for professional developers

 

Creating the ideal coding environment in Sublime Text