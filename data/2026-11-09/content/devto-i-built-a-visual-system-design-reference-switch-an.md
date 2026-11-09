---
title: I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source - DEV Community
url: https://dev.to/amananandrai/i-built-a-visual-system-design-reference-switch-any-architecture-between-aws-azure-gcp-open-55og
site_name: devto
content_file: devto-i-built-a-visual-system-design-reference-switch-an
fetched_at: '2026-11-09T16:00:28.089328'
original_url: https://dev.to/amananandrai/i-built-a-visual-system-design-reference-switch-any-architecture-between-aws-azure-gcp-open-55og
author: amananandrai
date: '2026-11-02'
description: I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP... Tagged with systemdesign, webdev, opensource, showdev.
tags: '#showdev, #systemdesign, #webdev, #opensource'
---

Born from frustration with scattered notes

# I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source

🔗Live site:system-design-explainer.vercel.app⭐GitHub:amananandrai/system-design-explainer

## 🧠 Why I Built This

Like a lot of developers, I've spent hours reading system design articles, watching interview prep videos, and staring at static diagrams trying to understandhow YouTube actually handles an uploadorhow Uber matches a rider to a driver in real time.

The problem I kept running into:

* Diagrams werestatic— you could see the boxes, but not how a request actually flows through them.
* Every diagram was tied toone vendor's vocabulary. An AWS diagram says "S3, SQS, DynamoDB", a GCP one says "Cloud Storage, Pub/Sub, Bigtable" — and translating between them in your head is tiring.
* My notes were scattered across bookmarks, Notion pages, and screenshots.

So I decided to build the reference I wished I had.

This started as a personal project to learn and grow.Building it forced me to actually understand each architecture well enough to draw it, break it into steps, and map every component across clouds. Somewhere along the way, I realised it could be just as useful for others preparing for interviews, designing real systems, or simply curious about how the apps they use every day work under the hood.

## 🚀 What Is System Design Explainer?

System Design Explaineris an interactive system design reference site where you canvisualise architectures of real-world systemsandview the same architecture through different tool lenses— a generic view, AWS, Google Cloud, Azure, or open-source tooling.

Every system page covers the requirements, APIs, capacity estimates, data model, request-flow walkthroughs, bottlenecks, scaling and extensions — all next to an auto-laid-out architecture diagram.

At the time of writing it has:

* 📦36 systems
* 🧩36 components
* 📚27 concepts

## ✨ Key Features

### ☁️ 1. Switch Clouds in One Click

This is the feature I'm most excited about. Every architecture can be relabelled for:

* Generic(vendor-neutral building blocks)
* AWS
* Google Cloud
* Azure
* Open source

So the same "object storage → queue → worker → CDN" flow instantly becomes the matching services for whichever stack you work with. Here's the YouTube design switching between all five:

Object storage becomesAmazon S3,Cloud Storage,Azure Blob StorageorMinIO; the event stream becomesAmazon MSK,Pub/Sub,Azure Event HubsorApache Kafka— same boxes, same arrows, different names. Great for interviews (where you're often asked to stay generic)andfor real-world work (where you're usually tied to a specific cloud).

### ▶️ 2. Play Hop-by-Hop Walkthroughs

Instead of just looking at a diagram, you canfollow a request step by step— upload a video, book a seat, pay a merchant, create a short link. Each step highlights what's happening and which component is responsible, so you build intuition for theflow, not just thelayout.

Here's what uploading a video to YouTube looks like:

And booking movie seats on BookMyShow (watch the seat hold and the idempotency key do their thing):

Walkthroughs work on every cloud too, so you can follow the exact same request through AWS, GCP or Azure services.

🎬 More walkthroughs (click to expand)Create a short link (URL shortener):Charge a card (payment gateway):Request a ride (Uber, on AWS):Message an online friend (WhatsApp, on GCP):Payment declined → saga compensation (Amazon, on Azure):

### 🔍 3. Inspect Components

Every building block (load balancers, caches, queues, databases, CDNs, etc.) has its own page covering:

* The options available per provider
* Common pitfalls
* Which systems on the site use it

### 📖 4. Learn the Patterns

Core concepts likecaching, sharding, fan-out, sagas, idempotency, consistent hashing, rate limiting, geospatial indexing, WebSockets, change data captureand more are explained on their own — and linked back to the real designs where they're applied. Many concept pages even come with a small diagram you can step through.

### 🔎 Bonus: Search & Dark Mode

HitCtrl Kto jump to any system, component or concept, and switch to dark mode for late-night interview prep.

## 🗺️ Learning Paths

If you're not sure where to start, there are guided learning paths where each one builds on the patterns from the previous one. Your progress is saved in your browser.

Level

Path

Systems

🟢 Start here

Foundations

URL shortener → Pastebin → API rate limiter → Search autocomplete

🟡 Intermediate

Real-time systems

WhatsApp → WebSockets at scale → Live sports scores → Uber

🔴 Advanced

Media at scale

Instagram → Twitter / X → YouTube → Netflix

🔴 Advanced

Money & bookings

BookMyShow → Amazon → Payment gateway → Buy now, pay later

## 🏗️ Systems Covered

The catalogue is filterable by category, difficulty, and concept. Here's a snapshot:

* Media & Social:YouTube, Netflix, Instagram, Twitter / X, WhatsApp, Quora, LinkedIn, Live sports scores
* Mobility & Logistics:Uber, Google Maps, Zomato / food delivery, Porter, Car rental, Driver booking & fleet management
* Commerce & Fintech:Amazon, Payment gateway, Buy now pay later, Stock brokerage
* Bookings & Marketplaces:BookMyShow, MakeMyTrip, Airbnb, Airline reservations, NoBroker, Urban Company, Practo, AstroTalk, Meeting scheduler
* Building Blocks:URL shortener, Pastebin, API rate limiter, Search autocomplete, Web crawler, Dropbox, WebSockets at scale, Video calling (WebRTC), Redis Cluster

I deliberately included a mix of global giantsandsystems that are popular in India (BookMyShow, Zomato, NoBroker, Practo, Urban Company…) because those come up a lot in interviews here and are rarely covered elsewhere.

## 🎯 Who Is This For?

* 👩‍💻Interview preppers— practise explaining designs end-to-end and see how patterns repeat across systems.
* 🏢Working engineers— map a design you know in one cloud to another cloud's services.
* 🎓Students & beginners— start with the Foundations path and build up gradually.
* 🤔The curious— ever wondered what happens when you hit "Book" on a movie seat? Now you can watch it happen.

## 🛠️ How It's Built

* Next.js(static export) — the whole site is plain static files, deployed on Vercel
* React Flow + ELK— auto-laid-out, zoomable architecture diagrams
* Tailwind CSS— styling, including dark mode
* Zod— every system is a typed content file validated against a schema, so adding a new design is mostly writing data, not UI code

## 📈 What I Learned Building It

Building this taught me far more than reading ever did:

* You only really understand a system when you have to draw every hop.Gaps in my knowledge showed up immediately when I tried to write a walkthrough.
* Clouds are more similar than they look.Once you map components across AWS, GCP, Azure and open source, the underlying patterns become obvious — the names are just different.
* Patterns repeat everywhere.Idempotency shows up in payments, bookings, and ride matching. Fan-out shows up in Twitter, Instagram, and LinkedIn. Seeing this visually made it click.

This project is very much still growing — and so am I.

## 🤝 Get Involved

This is a learning project, and I'd love for it to become a community resource. If you found it useful:

* ⭐Star the repo on GitHub— it really helps more people discover it:github.com/amananandrai/system-design-explainer
* 💡Share suggestions— which system should I add next? Drop it in the comments!
* 🐛Raise issues— spotted an inaccurate diagram, a wrong cloud mapping, or a bug? Pleaseopen an issue.
* 🔧Raise PRs— contributions are very welcome, whether it's a new system, a better walkthrough, a component fix, or a UI improvement.

Want to add a system? Create a file insrc/content/systems/, register it insystems/index.ts, follow the schema insrc/types/schema.ts, and runnpm run validateto check it. To run it locally:

git clone https://github.com/amananandrai/system-design-explainer.git

cd 
system-design-explainer
npm 
install

npm run dev 
# http://localhost:3000

Enter fullscreen mode

Exit fullscreen mode

## 🙌 Wrapping Up

👉Try it here:system-design-explainer.vercel.app⭐Star it here:github.com/amananandrai/system-design-explainer

I'd genuinely love to hear your feedback. Tell me in the comments which architecture you explored first — and which one you want to see next!

Happy designing! 🚀

Submit

Preview

Dismiss