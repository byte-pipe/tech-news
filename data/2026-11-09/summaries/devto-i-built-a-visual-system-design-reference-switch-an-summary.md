---
title: I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source - DEV Community
url: https://dev.to/amananandrai/i-built-a-visual-system-design-reference-switch-any-architecture-between-aws-azure-gcp-open-55og
date: 2026-11-02
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:01:57.503420
---

# I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source - DEV Community

# I Built a Visual System Design Reference — Switch Any Architecture Between AWS, Azure, GCP & Open Source

## Why I Built This
- I was frustrated by static diagrams that showed only boxes, not request flows.  
- Every diagram used a single vendor’s terminology, making mental translation to other clouds tiring.  
- My notes were scattered across bookmarks, Notion, and screenshots.  
- I started the project as a personal learning exercise and realized it could help interview prep, real‑world design, and curiosity about everyday apps.

## What Is System Design Explainer?
- An interactive reference site that visualises real‑world system architectures.  
- Each system page includes requirements, APIs, capacity estimates, data model, request‑flow walkthroughs, bottlenecks, scaling, extensions, and an auto‑laid‑out diagram.  
- Current stats: 36 systems, 36 components, 27 concepts.

## Key Features
### Switch Clouds in One Click
- Views can be toggled between generic (vendor‑neutral), AWS, Google Cloud, Azure, and open‑source equivalents.  
- Example: the “object storage → queue → worker → CDN” flow maps to S3/Cloud Storage/Blob Storage/MinIO, MSK/Pub/Sub/Event Hubs/Kafka, etc.  

### Play Hop‑by‑Hop Walkthroughs
- Step‑by‑step request simulations (e.g., video upload, seat booking, payment, URL shortener).  
- Highlights the component handling each step and works across all cloud views.

### Inspect Components
- Dedicated pages for each building block (load balancer, cache, queue, database, CDN, etc.).  
- Lists provider options, common pitfalls, and which systems use the component.

### Learn the Patterns
- Concept pages explain caching, sharding, fan‑out, sagas, idempotency, consistent hashing, rate limiting, geospatial indexing, WebSockets, change data capture, and more.  
- Each concept links back to real designs where it is applied and often includes a small interactive diagram.

### Bonus Features
- Global search (Ctrl K) for systems, components, or concepts.  
- Dark mode for night‑time study.

## Learning Paths
- Guided paths save progress in the browser and build on previously introduced patterns.  
- **Foundations (Start here)** – URL shortener → Pastebin → API rate limiter → Search autocomplete.  
- **Intermediate** – Real‑time systems: WhatsApp → WebSockets at scale → Live sports scores → Uber.  
- **Advanced – Media at scale** – Instagram → Twitter/X → YouTube → Netflix.  
- **Advanced – Money & bookings** – BookMyShow → Amazon → Payment gateway → Buy now, pay later.

## Systems Covered
- **Media & Social:** YouTube, Netflix, Instagram, Twitter/X, WhatsApp, Quora, LinkedIn, live sports scores.  
- **Mobility & Logistics:** Uber, Google Maps, Zomato, Porter, car rental, fleet management.  
- **Commerce & Fintech:** Amazon, payment gateway, buy‑now‑pay‑later, stock brokerage.  
- **Bookings & Marketplaces:** BookMyShow, MakeMyTrip, Airbnb, airline reservations, NoBroker, Urban Company, Practo, AstroTalk, meeting scheduler.  
- **Building Blocks:** URL shortener, Pastebin, API rate limiter, search autocomplete, web crawler, Dropbox, WebSockets at scale, video calling (WebRTC), Redis Cluster.  
- Includes both global giants and India‑focused services that are common in local interviews.

## Who Is This For?
- Interview preppers who need end‑to‑end design explanations and pattern repetition.  
- Working engineers mapping designs across different cloud providers.  
- Students and beginners starting with the Foundations path.  
- The curious who want to see what happens behind actions like booking a movie seat.

## How It’s Built
- Next.js static export, hosted on Vercel.  
- React Flow + ELK for auto‑laid‑out, zoomable diagrams.  
- Tailwind CSS for styling and dark mode.  
- Zod validates typed content files, making new designs a matter of data entry rather than UI code.

## What I Learned Building It
- True understanding comes from drawing every hop; gaps appear instantly when writing walkthroughs.  
- Cloud providers are more similar than they appear; mapping reveals underlying common patterns.  
- Design patterns repeat across domains (e.g., idempotency in payments, bookings, ride matching; fan‑out in social feeds).  

## Get Involved
- Star the GitHub repo (github.com/amananandrai/system-design-explainer).  
- Suggest new systems in the comments.  
- Report issues for inaccurate diagrams, wrong cloud mappings, or bugs.  
- Submit pull requests for new systems, better walkthroughs, component fixes, or UI improvements.  

### Contributing Quick Start
```bash
git clone https://github.com/amananandrai/system-design-explainer.git
cd system-design-explainer
npm install
npm run dev
```