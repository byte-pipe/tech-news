---
title: The Node.js Mistake That Cost My Client $3,000 in AWS Bills - DEV Community
url: https://dev.to/manolito99/the-nodejs-mistake-that-cost-my-client-3000-in-aws-bills-30a5
site_name: devto
content_file: devto-the-nodejs-mistake-that-cost-my-client-3000-in-aws
fetched_at: '2026-06-26T11:55:40.320600'
original_url: https://dev.to/manolito99/the-nodejs-mistake-that-cost-my-client-3000-in-aws-bills-30a5
author: Lolo
date: '2026-06-23'
description: Last year I was asked to investigate a startup's AWS bill. It had jumped from roughly $200/month to... Tagged with node, javascript, aws, webdev.
tags: '#node, #javascript, #aws, #webdev'
---

Tight loops and missing backoff logic

Last year I was asked to investigate a startup's AWS bill.

It had jumped from roughly $200/month to over $3,000 in a few weeks.

Nobody knew why.

After digging through logs, metrics, and database traffic, I found the culprit: a polling loop with no backoff strategy.

The code looked harmless:

async
 
function
 
processQueue
()
 
{

 
const
 
jobs
 
=
 
await
 
getJobs
()

 
for 
(
const
 
job
 
of
 
jobs
)
 
{

 
await
 
processFile
(
job
)

 
}

 
processQueue
()

}

processQueue
()

Enter fullscreen mode

Exit fullscreen mode

At first glance, this seems reasonable. Process all available jobs, then check again.

The problem appears when the queue is empty.

WhengetJobs()returned no work, the loop immediately queried the database again. And again. And again.

There was no delay, no backoff, and no event-driven trigger.

As a result, the service continuously hammered the database looking for work that didn't exist.

Each iteration generated:

* A database query
* Network traffic
* CPU usage
* Logging overhead
* Additional infrastructure load

Individually, each operation was cheap.

Executed hundreds of thousands of times per day, they became expensive.

The fix was simple:

async
 
function
 
processQueue
()
 
{

 
while 
(
true
)
 
{

 
const
 
jobs
 
=
 
await
 
getJobs
()

 
for 
(
const
 
job
 
of
 
jobs
)
 
{

 
await
 
processFile
(
job
)

 
}

 
await
 
new
 
Promise
(
resolve
 
=>
 
setTimeout
(
resolve
,
 
5000
))

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Even better would have been replacing polling entirely with an event-driven design using a message queue.

What this incident taught me:

1. Empty queues are production workloads.

Many engineers optimize for peak traffic and forget about idle traffic. Systems often spend more time idle than busy.

2. Polling needs backoff.

If you're polling, always define what happens when no work is found.

3. Cost bugs rarely look like bugs.

Nothing crashed. No exceptions were thrown. The system was technically working exactly as written.

It was just doing useless work 24/7.

4. Always monitor cost alongside performance.

CPU, latency, and error rates looked normal.

The AWS bill was the first real alert.

One question I ask during reviews now:

"What does this code do when there's nothing to do?"

That single question has caught more production issues than many architecture discussions ever did.

What's the most expensive bug you've ever seen in production?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse