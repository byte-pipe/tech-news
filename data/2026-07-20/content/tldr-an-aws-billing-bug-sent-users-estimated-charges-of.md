---
title: An AWS billing bug sent users estimated charges of up to $2.5 trillion
url: https://thenextweb.com/news/aws-billing-bug-billion-dollar-estimates
site_name: tldr
content_file: tldr-an-aws-billing-bug-sent-users-estimated-charges-of
fetched_at: '2026-07-20T19:34:41.391437'
original_url: https://thenextweb.com/news/aws-billing-bug-billion-dollar-estimates
author: Cristian Dina
date: '2026-07-20'
published_date: '2026-07-17 18:21:09'
description: A unit pricing error in AWS Cost Explorer emailed users bills ranging from billions to $2.5 trillion. One user with $0.19 in charges got a $2.5 billion estimate.
tags:
- tldr
---

Image by: Tony Webster from Minneapolis, Minnesota, United States

#### TL;DR

An AWS billing bug sent users estimated bills in the billions and trillions. Amazon confirmed it was a unit pricing error and is recomputing all estimates.

AWS users woke up Friday to find estimated billing emails showing chargesranging from hundreds of millions to $2.5 trillion. A unit pricing error in the AWS Billing Console’s estimated billing computation subsystem was the cause, Amazon confirmed. One Reddit user whose charges totalled $0.19 last month received an estimated bill of nearly $2.5 billion. Others reported estimated monthly charges between $126,000 and $2.5 trillion.

“The displayed billing estimates do not reflect actual usage and charges,” AWS said. The company identified the root cause within 90 minutes, describing it as “an issue with unit pricing within the estimated billing computation subsystem.” AWS paused estimated bill updates so the inflated figures would not increase further, and said it has begun recomputing all billing data. Corrected amounts should appear by Saturday, July 18 at noon Pacific time.

The bug triggered panic before users realisedit was an error. “I nearly had a heart attack when my two S3 buckets with a few MBs of data generated a half-billion-dollar forecast,” one Reddit user wrote. Another posted: “Needless to say, I panicked and destroyed everything on this account.”AWS committed $1 billion to forward-deployed AI engineers last week, and the billing bug is an unwelcome reminder that the infrastructure running AI workloads worth billions per month is also capable of generating billing errors of the same magnitude.

The incident comes a day after a separate AWS CloudFront outage served errors instead of websites.Cloud infrastructure is handling unprecedented spending volumesas AI demand pushes monthly compute bills into the hundreds of millions for individual customers, making billing system reliability a higher-stakes problem than it was when the largest bills were measured in thousands.

## Get the TNW newsletter

Get the most important tech news in your inbox each week.