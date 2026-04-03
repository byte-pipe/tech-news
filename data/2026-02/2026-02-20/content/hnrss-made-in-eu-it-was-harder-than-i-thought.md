---
title: '"Made in EU" - it was harder than I thought.'
url: https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/
site_name: hnrss
content_file: hnrss-made-in-eu-it-was-harder-than-i-thought
fetched_at: '2026-02-20T11:15:16.744813'
original_url: https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/
date: '2026-02-20'
published_date: '2026-02-20T09:00:27.000Z'
description: I tried building my startup entirely on European infrastructure. Here's the stack I landed on, what was harder than expected, and what you still can't avoid.
tags:
- hackernews
- hnrss
---

When I decided to build my startup on European infrastructure, I thought it would be a straightforward swap. Ditch AWS, pick some EU providers, done. How hard could it be?

Turns out: harder than expected. Not impossible, I did it, but nobody talks about the weird friction points you hit along the way. This is that post.

## Why bother?

Data sovereignty, GDPR simplicity, not having your entire business dependent on three American hyperscalers, and honestly, a bit of stubbornness. I wanted to prove it could be done. The EU has real infrastructure companies building serious products. They deserve the traffic.

## The stack

Here's what I landed on after a lot of trial, error, and migration headaches.

Hetznerhandles the core compute. Load balancers, VMs, and S3-compatible object storage. The pricing is almost absurdly good compared to AWS, and the performance is solid. If you've never spun up a Hetzner box, you're overpaying for cloud compute.

Scalewayfills the gaps Hetzner doesn't cover. I use their Transactional Email (TEM) service, Container Registry, a second S3 bucket for specific workloads, their observability stack, and even their domain registrar. One provider, multiple services, it simplifies billing if nothing else.

Bunny.netis the unsung hero of this stack. CDN with distributed storage, DNS, image optimization, WAF, and DDoS protection, all from a company headquartered in Slovenia. Their edge network is genuinely impressive and their dashboard is a joy to use. Coming from Cloudflare, I felt at home rather quickly.

Nebiuspowers our AI inference. If you need GPU compute in Europe without sending requests tous-east-1, they're one of the few real options.

Hankohandles authentication and identity. A German provider that gives you passkeys, social logins, and user management without reaching for Auth0 or Clerk. More on this in the "can't avoid" section — it doesn't eliminate American dependencies entirely, but it keeps the auth layer European.

## Self-hosting: Rancher, my beloved

This is where things get fun... and time-consuming. I self-host a surprising amount:

* Giteafor source control
* Plausiblefor privacy-friendly analytics
* Twenty CRMfor customer management
* Infisicalfor secrets management
* Bugsinkfor error tracking

All running on Kubernetes, with Rancher as the glue keeping the whole cluster sane.

Is self-hosting more work than SaaS? Obviously. But it means my data stays exactly where I put it, and I'm not at the mercy of a provider's pricing changes or acquisition drama.

For email,Tutanotakeeps things encrypted and European.UptimeRobotwatches the monitors so I can sleep.

## The parts that were extra hard

Transactional email with competitive pricing.This one surprised me. Sendgrid, Postmark, Mailgun, they all make it trivially easy and reasonably cheap.The EU options exist, but finding one that matches on deliverability, pricing, and developer experience took real effort. Scaleway's TEM works, but the ecosystem is thinner. Fewer templates, fewer integrations, less community knowledge to lean on when something goes wrong.

Leaving GitHub.If you live in GitHub's ecosystem Actions, Issues, code review workflows, the social graph... walking away feels like leaving a city you've lived in for a decade. You know where everything is. Gitea is actually excellent, and I'd recommend it without hesitation for the core git experience. But you'll miss the ecosystem. CI/CD pipelines need to be rebuilt. Integrations you took for granted don't exist. The muscle memory ofgh pr createtakes a while to unwire.

Domain TLD pricing.This one is just baffling. Certain TLDs cost significantly more when purchased through European registrars. I'm talking 2-3x markups on extensions that are cheap everywhere else. I never got a satisfying explanation for why. If anyone knows, I'm genuinely curious.

## What you realistically can't avoid

Here's the honest part. Some things are American and you just have to accept it:

Google Ads and Apple's Developer Program.If you want to acquire users and distribute a mobile app, you're paying the toll to Mountain View and Cupertino. There is no European alternative to the App Store or Play Store. This is just the cost of doing business.

Social logins.Your users expect "Sign in with Google" and "Sign in with Apple."You can add email/password and passkeys, but removing social logins entirely is a conversion killer. Every one of those auth flows hits American servers. The silver lining: Hanko, a German identity provider, handles the auth layer itself, so at least your user management and session handling stay in Europe, even if the OAuth flow touches Google or Apple.

AI.If you want Claude, and I very much want Claude, that's Anthropic, that's the US.The EU AI ecosystem is growing, but for frontier models, the options are mostly American. You can run open-weight models on European inference providers, but if you want Claude, you're making a transatlantic API call.

## Was it worth it?

Yes, with caveats. My infrastructure costs are lower than they'd be on AWS. My data residency story is clean. I understand my stack deeply because I had to ... there's no "just click the AWS button" escape hatch.

But it took longer than I expected. Every service I self-host is a service I maintain.Every EU provider I chose has a smaller community, thinner docs, and fewer Stack Overflow (or Claude) answers when things break at 2 AM.

If you're thinking about doing this: go in with your eyes open. The EU infrastructure ecosystem is real and maturing fast. But "Made in EU" is still a choice you have to actively make, not one you can passively fall into. The defaults of the tech industry pull you west across the Atlantic, and swimming against that current takes effort.

It's effort worth spending. But it is effort.

If you curious to see the finished product, here it is:hank.parts.
