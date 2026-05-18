---
title: How Superset built the IDE for AI agents on Vercel - Vercel
url: https://vercel.com/blog/how-superset-built-the-ide-for-ai-agents-on-vercel
site_name: tldr
content_file: tldr-how-superset-built-the-ide-for-ai-agents-on-vercel
fetched_at: '2026-05-18T12:11:45.663436'
original_url: https://vercel.com/blog/how-superset-built-the-ide-for-ai-agents-on-vercel
date: '2026-05-18'
description: How Superset built the IDE for AI coding agents on Vercel, running a dozen parallel agents per developer and 600 preview deployments a day.
tags:
- tldr
---

4minread

Copy URL
May 10, 2026

Superset on Vercel

* 1,000–1,400 deployments per week
* ~600 preview deployments per day
* ~30 second average build time
* 57–64% week-over-week DAU growth

Software development with AI started as a single engineer chatting with a single agent about a local repo. Today, developers direct fleets of agents in the cloud, but traditional tools were built for the old shape of the job: IDEs, terminals, and review systems designed for one developer moving one ticket at a time.

Co-founders Kiet Ho, Satya Patel, and Avi Peltz, all former CTOs at YC-backed companies, builtSupersetas the IDE for multi-agent development. It runs up to 10 coding agents in parallel, each in its own isolated workspace. Developers use it to direct teams of agents generating code across multiple branches simultaneously.

Running a team of agents in parallel changes what the platform underneath has to do. The product Superset offers its users only feels parallel because nothing on the platform forces the work to wait. If any layer slows down, even briefly, the parallelism on top collapses with it.

“
Vercel uptime isn't something we plan around. It's a given.
Vercel uptime isn't something we plan around. It's a given.
Vercel uptime isn't something we plan around. It's a given.
”
Kiet Ho
, 
 Co-Founder and CEO

## Link to headingParallel agents need parallel infrastructure

This workflow has a dependency that's invisible from the product surface. Every agent thread needs its own isolated environment, every branch needs a live URL, and every change needs a safe place to run.

Without instant provisioning, parallel agents stop being parallel. CI pipelines have to be configured per branch, preview environments have to be managed by hand, and deploys back up behind one another. For a team running a dozen agents at once, that serialization is what breaks the product. Twelve workflows collapse into one queue, and a task that should take minutes takes hours. The developer is back to waiting, which is the exact problem Superset exists to solve.

## Link to headingSix Next.js projects, no platform team

Vercel was the default choice from the start, as all three founders had built on it at previous companies. From day one, Superset ran sixNext.jsprojects on Vercel: the web app, marketing site, docs, and three supporting services. The team skipped platform engineering entirely and stayed focused on the product.

Every branch a Superset developer or agent creates becomes apreview deploymentautomatically, often spinning up multiple services. At its peak, Superset generates roughly 600 preview deployments a day internally. Every branch gets a live URL, and the team never waits on a deploy queue.

## Link to headingOne AI stack for every workload

Superset's AIstack grew with the product, and each piece of the Vercel platform was pulled in to solve a specific problem as functionality was added.

Orchestration and model routing

* AI SDKandAI Elementsrun the agent orchestration itself, giving Superset a single interface for multi-model, multi-agent workflows.
* AI Gatewayhandles model routing without custom routing logic.

Storage and compute

* Vercel Blobstores artifacts from agents and users, no object storage to manage.
* Fluid computeabsorbs parallel tasks as agents fan out, scaling underneath without forcing the team to rearchitect.Active CPU pricingmeans cost is only incurred on actual compute, not round-trip time waiting on model responses.

Operational controls

* Cron Jobsprevent parallel environments from piling up.
* BotIDfilters bots during high traffic periods, no custom middleware needed.

As Superset has expanded into new product areas, the entire stack has stayed on Vercel. There's no second cloud to glue in, no orchestration layer to maintain, and no platform engineering team to keep it glued together. New surface areas gets built on the same primitives that handled the old surface area, which is what frees the team to keep moving on product instead of plumbing.

## Link to headingSuperset is its own super user

The most credible proof how the Superset team uses Superset themselves. GitHub issues flow into Superset and get split across parallel workspaces, and Satya has tuned the team's setup to run up to a dozen instances at once. Multiple efforts move forward without anyone waiting on serial decisions. Compared to their previous dev workflows, Superset's commit graph looks exponential.

## Link to headingScaling through a Hacker News spike

During aHacker News "Show HN" launch, user counts tripled overnight. Superset absorbed the spike without anyone provisioning infrastructure mid-flight.

That extends to incidents. If a customer reports an issue to Superset, their agents can spin up, write the fix, generate a preview, and merge the code in under thirty minutes. If the fix makes things worse,rollbacks are instant, so the cost of a bad deploy drops to near zero.

## Link to heading"Almost no time to deploy" as the bar

For Superset, immediate deployment matters because it keeps the loop between writing code, previewing it, and shipping it short enough that velocity never stalls, even across dozens of parallel workstreams. Build time averages around 30 seconds, and deployment volume runs between 1,000 and 1,400 a week.

“
When you're using Vercel, it's almost no time to deploy.
When you're using Vercel, it's almost no time to deploy.
When you're using Vercel, it's almost no time to deploy.
”
Satya Patel
, 
 Co-Founder and CTO

## Link to headingWhat's next

The pattern for success is already clear: a product built for parallelism, by a team that works in parallel, onagentic infrastructurethat doesn't force them back into a queue. Every new agent capability they ship to customers gets stress-tested first by their own engineers running a dozen at once. The dozen will become two dozen, and the infrastructure underneath was built to expect it.

About Superset:Supersetis built by a team of three ex-YC CTOs and its the IDE for the AI agents era, letting developers run multiple coding agents in parallel.