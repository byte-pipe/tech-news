---
title: Andy Pavlo joins ClickHouse to establish ClickHouse Labs | ClickHouse
url: https://clickhouse.com/blog/andy-pavlo-joins-clickhouse
site_name: hnrss
content_file: hnrss-andy-pavlo-joins-clickhouse-to-establish-clickhous
fetched_at: '2026-08-03T19:33:31.490580'
original_url: https://clickhouse.com/blog/andy-pavlo-joins-clickhouse
date: '2026-08-03'
description: I am excited to announce that I am joining ClickHouse, Inc. to establish and lead a new research team at ClickHouse Labs.
tags:
- hackernews
- hnrss
---

->
Scroll to top
<-
Back
* Blog
* /
* Company and culture
Copy page
Copied!
More actions
* View as MarkdownOpen this page in Markdown
* Open in ChatGPTAsk questions about this page
* Open in ClaudeAsk questions about this page
* Open in v0Ask questions about this page

# Andy Pavlo joins ClickHouse to establish ClickHouse Labs

Andy Pavlo
Aug 3, 2026 · 5 minutes read

I am excited to announce that I am joining ClickHouse to establish and lead a new research team calledClickHouse Labs. I want to share how it came about and what we plan to do.

## How It Started#

I started as a professor in the Computer Science Department at Carnegie Mellon University in 2013. I have spent my career seeking to understand the science of modern database management system (DBMS) internals. I make it a priority totrack every new systemthat comes along, both in industry and academia, to understand their implementations.

I have known about the ClickHouse DBMS since it wasfirst announced as open-source softwarein June 2016. My initial reaction to this news was that it had to be vaporware because it seemed too good to be true. ClickHouse had features that at the time were only found in a handful of closed-source, commercial analytical DBMSs. For example, ClickHouse was written in C++ and supported vectorized query execution using SIMD in 2016. Most prominent open-source analytical DBMSs in 2016 were JVM-based and did not support SIMD optimizations until years later.

Since then, I have followed ClickHouse's development closely. It has always been a leading system that was highly relevant to our academic research projects. You can even see me wearing my original ClickHouse shirt inmy first remote lectures in 2020, when the pandemic forced us to move our database courses online.

Given this history, I was honored when the ClickHouse co-founders invited me to establish this new research group at ClickHouse. The chance to work with one of the strongest engineering teams on the next generation of database technology was an opportunity that I could not pass up. This will be a next-level collaboration like whenKiller Mike hooked up with El-Pto create a hip-hop supergroup.

## What Is ClickHouse Labs?#

The goal of ClickHouse Labs is to establish a best-in-class industry research organization focused on databases. It will not operate as an isolated research organization that throws ideas over the wall to engineering. Instead, we will work closely with ClickHouse engineers, customers, collaborators, and industry partners to develop and disseminate new ideas that keep ClickHouse at the bleeding edge.

We will also work with ClickHouse's PostgreSQL team to help establish its burgeoning managed service as a market leader in performance and reliability. PostgreSQL and ClickHouse serve different workload requirements, but the combination gives us a broad foundation for investigating both transactional and analytical database problems.

Our objective is straightforward but ambitious: conduct research with scientific value and then help transform the best ideas into technology that matters to users. I want to achieve the same level of impact associated with pioneering industry research organizations, such asIBM ResearchandMicrosoft Research. Those groups demonstrated that industry laboratories can simultaneously advance fundamental computer science, influence commercial products, and train generations of database researchers. That is the tradition we want to continue.

## What is Next?#

The ClickHouse team already has an exceptional record of publishing deep technical material about its work. Since the establishment of the company in 2021, its engineers have produceddetailed articlesthat explain the DBMS's implementation. There is also the2024 VLDB paperthat describes ClickHouse's core architecture. These works are so thorough that I assign them as readings to my students at Carnegie Mellon. At the same time, there is a backlog of interesting ideas and optimizations that the ClickHouse engineering team has explored but has not yet had the time to validate fully and push into production. One of my immediate priorities is to help accelerate this process. We will then use that as a springboard to explore new ideas that push ClickHouse even further.

One larger question we will investigate is how DBMSs like ClickHouse and PostgreSQL fit into emerging AI and agentic technologies. There are two sides to this problem. The first is determining what a DBMS should look like to better support agents. The second side is determining how agents can improve and automate the development of DBMSs themselves. Everything is on the table: new hardware, new algorithms, new data structures, new execution strategies, and new ways of building and operating DBMS software. Although I do not have answers to these problems yet (this is why it is research), the one thing I am certain about is that ClickHouse's solid relational model foundation positions it well to evolve alongside these data-intensive workloads.

I have spent my career studying how database systems are built and helping train the people who build them. With ClickHouse Labs, we now have the opportunity to create an organization devoted to advancing both.

Share this post

* Copy URL

### Subscribe to our newsletter

Stay informed on feature releases, product roadmap, support, and cloud offerings!

## Recent posts

View all Blogs
Company and culture

### ClickHouse launches ClickHouse Labs with Andy Pavlo as VP of Database Research

ClickHouse · Aug 3, 2026
Engineering

### I created a playground for 110 database systems

Alexey Milovidov · Aug 3, 2026
Product

### What's new in clickhousectl v0.4.0

Al Brown · Jul 31, 2026
Company and culture

### ClickHouse joins the Open Secure AI Alliance

ClickHouse · Jul 30, 2026
View all Blogs