---
title: Meet Alice. Alice is impatient. - Marc's Blog
url: https://brooker.co.za/blog/2026/06/19/waiting.html
site_name: hnrss
content_file: hnrss-meet-alice-alice-is-impatient-marcs-blog
fetched_at: '2026-06-22T00:53:19.137218'
original_url: https://brooker.co.za/blog/2026/06/19/waiting.html
author: Marc Brooker
date: '2026-06-20'
description: Alice is impatient
tags:
- hackernews
- hnrss
---

# Marc's Blog

# About Me

 My name is Marc Brooker. I like to build things that work, and do cool stuff. I like building big things. I also dabble in machining, welding, cooking, and skiing.

 I am an engineer at Amazon Web Services (AWS) in Seattle, where I work on agentic AI, especially safety and policy for agentic AI. Before that, I worked on EC2, EBS, databases, serverless, and serverless databases.

All opinions are my own.
 

# Links

My Publications and Videos

@marcbrooker on Mastodon

@MarcJBrooker on Twitter

Is this blog written by AI?

# Meet Alice. Alice is impatient.

What do you mean?

Meet Alice. Alice uses your web service. Alice, like most humans, measures her time in seconds and minutes. Alice says your service is slow. You tell Alice that the mean request to your service completes in 100ms, but Alice says that her mean wait time is 1s.

You’re both right.

Meet Alex. Alex uses your web service. Alex, like most humans, measures his time in seconds and minutes. Alex says that when you have outages, they last a long time and he gets really annoyed. You tell Alex that your MTTR is less than 1 minute. Alex says that he sees the mean outage lasting 1 hour.

Again, you’re both right.

What’s going on? What’s going on is that you’re measuring time in requests, or in outages, and Alex and Alice are measuring time in seconds and minutes. When you have a long request or a long outage, Alex and Alice count that as a long time, with a heavy weight. But you only count that as one.

More technically, what’s going on here is theinspection paradox. Alex and Alice don’t experience your latency distribution $f(t)$, they experience a t-weighted version of it. If you have a MTTR or mean request time of $\mathbb{E}[X]$, Alex and Alice experience $\mathbb{E}_a[X] = \frac{\mathbb{E}[X^2]}{\mathbb{E}[X]} = \mathbb{E}[X] + \frac{\mathrm{Var}(X)}{\mathbb{E}[X]}$.

Most of the time they’re waiting, they’re waiting for things that take a long time. This is (roughly) how humans experience time.

Let’s play with this with a little simulation. Plug in your median latency (or recovery time), and 99th percentile latency (or recovery time), we’ll fit a log-normal distribution to it, and then plot both what your service metrics see and what your customers see.

Median:ms
   
 p99:ms

What your service sees (mean):–ms.
 What your customers experience (mean):–ms.

For example, put in 30 as the median (let’s ignore the milliseconds and pretend these are minutes for now) for a 30 minute Median TTR (i.e. in half of your postmortems you see a recovery time of $\leq 30$ minutes), and 600 in as the p99 (one in every 100 events, recovery takes 10 hours). Your MTTR is just over an hour. Your customers experience a mean time to recovery of around 6 hours!

There are many arguments for why tail latency (and long recovery times) are so important to understand (e.g.multiple samples), but this is the one that I think is the least widely understood. For service times, timeout-and-retry can hide this latency some of the time (as long as the running request doesn’t hold locks or other exclusive resources). But, for recovery time, no such hiding is possible. The heaviness if the tail matters a great deal. This is also one of the reasons I don’t like trimmed measurements (like trimmed means) as a way of thinking about service latency or recovery time. They throw out some really critical context about the shape of the right tail that dominates the customer experience (the other reason is related to Little’s Law and capacity usage,which I’ve written about before).

A note on log-normal:I chose log-normal here for numerical convenience. It has the nice property that $\mathrm{lognormal}(\mu, \sigma^2)$ becomes $\mathrm{lognormal}(\mu + \sigma^2, \sigma^2)$. Also it’s well-behaved around 0. I don’t believe that log-normal is a particularly good choice of distribution for latency or recovery time metrics, and generally would approach these problems entirely non-parametrically.

 « 
Back to the blog index

#### Similar Posts

* 06 Aug 2020»Surprising Economics of Load-Balanced Systems
* 19 Apr 2021»Tail Latency Might Matter More Than You Think
* 05 Aug 2021»Latency Sneaks Up On You

#### Something Completely Different

* 18 Jun 2026»Is this blog written by AI?

Marc BrookerThe opinions on this site are my own. They do not necessarily represent those of my employer.marcbrooker@gmail.com

RSSAtom

 This work is licensed under a 
Creative Commons Attribution 4.0 International License
.