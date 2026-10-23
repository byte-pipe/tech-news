---
title: 'AI’s hidden storage bill: What inference leaves behind | MIT Technology Review'
url: https://www.technologyreview.com/2026/10/22/1146948/ais-hidden-storage-bill-what-inference-leaves-behind/
site_name: newsfeed
content_file: newsfeed-ais-hidden-storage-bill-what-inference-leaves-behi
fetched_at: '2026-10-23T15:40:40.206511'
original_url: https://www.technologyreview.com/2026/10/22/1146948/ais-hidden-storage-bill-what-inference-leaves-behind/
date: '2026-10-22'
description: 'Ask most executives to picture the cost of AI and they’ll likely see GPUs—racks of accelerators with gigawatts of power—and a waitlist for silicon. But that picture leaves something out: Data storage costs. What happens to data after a model responds? Much of the back-end data that’s generated—from billions of daily prompts, images, and videos—needs…'
tags:
- mit-tech-review
- artificial intelligence
- sponsored
---

Sponsored

Provided byWD

 

Ask most executives to picture the cost of AI and they’ll likely see GPUs—racks of accelerators with gigawatts of power—and a waitlist for silicon. But that picture leaves something out: Data storage costs.

 
 

What happens to data after a model responds?Much of the back-end data that’s generated—from billions of daily prompts, images, and videos—needs to be stored. But data storage is one of the harder infrastructure costs to plan for, and it’s often overlooked in initial AI infrastructure planning.

 
 

### As inference scales, the data footprint grows with it

 

Traditionally, AI infrastructure conversations have centered on the compute-intensive process of training a model. Training is finite: a run starts, burns through compute, and ends. But inference runs continuously, every time a model answers a prompt. For infrastructure planning, that difference matters: A training run is a project you can budget for and retire. Inference doesn’t retire; every inference request leaves something behind.

 

Take AI-generated video. In this workload, the back-end spend can be significant. From internal measurements, WD found that an 8-second clip (returned to a user as a 3.97MB 720p file) left more than 500MB of associated data behind on the back end, including logs, cached context, immediate renders, backups, and safety records. That’s a 130x increase over the output file size the user saw. Scale this to an enterprise generating longer, higher resolution video and the back-end footprint grows into the hundreds of gigabytes per clip.

 

And that back-end footprint is growing fast. McKinseyprojects AI inference demandwill grow at a 35% CAGR through 2030, versus 22% for training, making up more than 40% of total data center demand by the end of the decade.

 

Arecent WD-sponsored IDCglobal white paper that surveyed 763 IT and business decision makers found that nearly 95% of respondents reported an increase in data volume due to generative AI over the past 12 months, with roughly 61% reporting growth of 25% or more.

 

“You can think of having more storage as an optimization for keeping the GPUs busy,” said a senior product manager of a hyperscale cloud service provider quoted in report. “The biggest challenge is to ensure that the GPUs are not idle, waiting for data to show up—hours of GPU idle time becomes very expensive, very fast.” Put in dollar terms: if your storage spend is growing 25% year over year while your compute budget grows in the more predictable cyclical way, storage ends up outpacing the budget line that receives the most attention.

 

### Matching storage to the AI data life cycle

 

Compute demand rises and falls with training cycles, product launches, and hardware refreshes. But the volume of retained data doesn't fall back down with it when compute demand slows. Model logs, synthetic outputs, inference results, and more keep accumulating, and organizations are holding onto more of it for longer.

 

This changes the role of retained data. Information that once moved into an archive and rarely surfaced can now become an input to future AI workloads. As more data is retained, retrieved, and reused, storage must support not only growing capacity, but increasingly dynamic access to it. The same WD-IDC survey found 96% of respondents anticipate needing faster archive retrieval to support inference or retrieval-augmented generation (RAG).

 

AI workloads require both performance and capacity, with different technologies serving different needs across the data lifecycle. And for the vast volumes of data that must be retained and revisited, HDDs provide a cost-effective, high-capacity foundation, with a significant cost-per-terabyte advantage

 

### What this means for how AI gets budgeted

 

For a CFO or CIO, this means “AI infrastructure spend” may be scoped too narrowly on compute. A model that idles while data loads costs about as much as one idling for lack of a GPU. But the storage bottleneck stays hidden until it’s already a problem, surfacing in operating costs and retrieval delays rather than a CapEx line next to the accelerators.

 

Consider a retailer generating AI product videos for its catalog, or an insurer running claims documents through a RAG pipeline for faster underwriting. In both cases, the compute cost is a known, budgeted quantity: a per-generation or per-query rate that finance can forecast. The storage cost is different: It compounds with every video generated and every claim processed, because none of that back-end data disappears once the task is finished.

 

A team that budgets AI as “compute plus a rounding error for storage” may find, in 12 to 18 months, that the rounding error has become a significant fraction of the program’s total cost—right around the time leadership is deciding whether to expand.

 

### Building for economically scalable capacity

 

Addressing this challenge starts with architecture. Storage strategy tends to be designed for expensive, hot-tier performance (for data accessed instantly and constantly), while most AI data by volume accumulates in the warm, cool, and cold tiers behind it.

 

What enterprises need is economically scalable capacity: Infrastructure designed for the full AI data life cycle, balancing performance with capacity, power, reliability, and total cost of ownership as data persists, compounds, and is increasingly reused. That means treating archives that once sat untouched as active assets for RAG and inference, and setting retention policies for data’s growing strategic value rather than its original storage cost. It also means recognizing that decisions about storage play out across fleets, not individual drives.

 

Such infrastructure requires storage tiers, where individualized power consumption, reliability, density, and operational efficiency all determine whether the system remains economically sustainable as capacity scales.

 

There are three questions to ask about your organization’s AI infrastructure budget:

 
1. What’s our data retention policy for AI-generated content, and who set(s) it?
2. Is our storage procurement tied to training-time performance needs, or to the actual life cycle of the data we’re producing?
3. If our AI usage doubled next year, would our storage cost double with it, or worse?
 

Most organizations cannot answer all three with confidence. That’s the gap worth closing before the next budget cycle, not after.

 

This content was produced by WD. It was not written by MIT Technology Review’s editorial staff.

### Deep Dive

### Artificial intelligence

### Don’t be fooled—LLMs don’t reason

Ten years after AlphaGo’s match against Go champion Lee Sedol, today’s AI still isn’t tapping into the machinery that made that win possible.

By 
* Thore Graepelarchive page

### “We were looking at it wrong”: The explosive claim that’s upended the AI world

An exclusive interview with Nick Cammarata, the researcher whose 26,000-word viral blog post has AI safety folks celebrating.

By 
* Will Douglas Heavenarchive page

### Don’t be fooled by this summer of AI hype

Breathless claims about AGI and new capabilities fall apart pretty quickly under scrutiny.

By 
* Timnit Gebruarchive page
* Emily M. Benderarchive page

### The inside story on why OpenAI agents hacked Hugging Face

The underlying models had been rewarded for cheating and communicating with each other, a new OpenAI report finds.

By 
* Grace Huckinsarchive page

### Stay connected

Illustration by Rose Wong

## Get the latest updates fromMIT Technology Review

Discover special offers, top stories,
 upcoming events, and more.

Enter your email
Privacy Policy

Thank you for submitting your email!

Explore more newsletters

It looks like something went wrong.

We’re having trouble saving your preferences.
 Try refreshing this page and updating them one
 more time. If you continue to get this message,
 reach out to us atcustomer-service@technologyreview.comwith a list of newsletters you’d like to receive.