---
title: The $1,000 AWS mistake | Blog
url: https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/
site_name: hackernews
fetched_at: '2025-11-19T19:06:55.641205'
original_url: https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/
author: Dotsquare LLC
date: '2025-11-19'
description: A cautionary tale about AWS VPC networking, NAT Gateways, and how a missing VPC Endpoint turned our S3 data transfers into an expensive lesson.
---

November 18, 2025
By
Mathias Hansen

# The $1,000 AWS mistake

A cautionary tale about AWS VPC networking, NAT Gateways, and how a missing VPC Endpoint turned our S3 data transfers into an expensive lesson.

I've been using AWS since around 2007. Back then, EC2 storage was entirely ephemeral and stopping an instance meant losing all your data. The platform has come a long way since then.

Even after nearly two decades with the platform, there's always something new to learn. And sometimes those lessons come with a $1,000 price tag.

## The setup

We recently moved over to using S3 for mirroring some large internal data files for Geocodio. We're talking about geographic datasets (things like address points, boundary data, and census information) that range from a few gigabytes to hundreds of gigabytes each. Some of these files are updated almost daily with fresh data, while others are refreshed less frequently. They need to be synced regularly from our ETL platform (which is hosted with Hetzner) to our processing infrastructure on AWS.

AWS has notoriously high data transfer costs.Cloudflare has written extensively about this, and it's a common complaint across the industry. Corey Quinn from Last Week in AWS has alsocalled out the AWS Managed NAT Gatewayfor being particularly expensive. AWS charges $0.09 per GB for data transfer out to the internet from most regions, which adds up fast when you're moving terabytes of data.

So before starting this project, I did my homework. I carefully researched the costs involved and confirmed two critical things:

1. AWS still allows free transfer between EC2 instances and S3(as long as they're in the same region)
2. TransfersintoS3 are free(this was important since the data comes from our ETL platform hosted with Hetzner)

Great! I had a clear picture of the costs.

...Or so I thought.

## The surprise

A few days after deploying the new S3 sync process, I got a notification from AWS Cost Anomaly Detection. (Boy, was I happy that I had that enabled!)

The alert showed something alarming:20,167.32 GBof "NAT Gateway" data transfers in a single day, which amounted to$907.53.

Month to date, this had already surpassed $1,000.

I stared at the dashboard in disbelief. How could this be happening? I had specifically confirmed that EC2-to-S3 transfers were free!

## But why oh why?

After some frantic investigating (and a bit of panic), I discovered the culprit.

When you're using VPCs with a NAT Gateway (which most production AWS setups do), S3 transfersstill go through the NAT Gatewayby default. Even though you're making requests to an AWS service that's in the same region, the traffic is routed out through your NAT Gateway and back in, incurring data transfer charges at $0.045 per GB.

The solution?VPC Endpoints for S3, specifically what AWS calls a "Gateway Endpoint."

A Gateway Endpoint is a special type of VPC endpoint that allows you to privately route traffic to S3 without going through your NAT Gateway or Internet Gateway. It's essentially a direct pipe from your VPC to S3.

Even better, Gateway Endpoints for S3 arecompletely free. No hourly charges, no data transfer charges. Nothing.

## The fix

The solution is to create a VPC Gateway Endpoint for S3. This is a special type of VPC endpoint that creates a direct route from your VPC to S3, bypassing the NAT Gateway entirely.

In our case, we manage infrastructure with Terraform, so it was just a matter of adding the Gateway Endpoint resource and associating it with our route tables. AWS automatically handles the routing updates to direct S3 traffic through the endpoint instead of the NAT Gateway.

## The lesson

I've built countless VPCs, configured security groups, set up load balancers, and optimized costs in dozens of ways over the years. But somehow, VPC Endpoints for S3 had slipped through the cracks of my knowledge.

AWS's networking can be deceptively complex. Even when you think you've done your research and confirmed the costs, there are layers of configuration that can dramatically change your bill.

Don't make my mistake. Here are a few things I'd suggest checking to help you avoidyour ownsurprise $1,000 bill:

AWS Cost Anomaly Detection is worth setting up.It caught this issue within days, saving us from an even larger surprise at the end of the month. If you haven't enabled it yet,do itnow.

VPC Endpointsare your friend.If you're using S3 or DynamoDB from EC2 instances in a VPC with a NAT Gateway, you absolutely need Gateway Endpoints. There's literally no reason not to use them. They're free and improve performance.

Always validate your assumptions.I thought "EC2 to S3 is free" was enough. I should have tested with a small amount of data and monitored the costs before scaling up to terabytes.

The cloud is complicated.There's always more to learn, even after nearly two decades. And that's okay. It just means we need to be careful and vigilant.

And we're not alone in this. Just last year,Recall.ai discovered they were paying $1M annually in unexpected AWS WebSocket data processing fees. Even experienced teams hit these surprises.

## What's next

We've since audited our entire AWS infrastructure to make sure we have Gateway Endpoints configured for all VPCs that communicate with S3.

If you're using AWS and you haven't checked your VPC Endpoint configuration lately, I'd recommend taking a look. That $1,000 lesson doesn't need to be repeated.

TL;DR: NAT Gateways charge for ALL data processing, even for traffic to AWS services like S3 that have no data transfer fees. Use VPC Endpoints to bypass this.

## Additional Resources

* AWS VPC Endpoints for S3
* AWS Cost Anomaly Detection
* Save Cash by Avoiding The AWS NAT Gateway with Gateway Endpointsby Carmen Cincotti
* The AWS Managed NAT Gateway is Unpleasant and Not Recommendedby Corey Quinn
* Cloudflare's take on AWS egress costs
Engineering
Infrastructure
AWS

## Subscribe to Code and Coordinates

## Get the latest articles about software development, data science, and geospatial technology

Subscribe

### From Millions to Billions

How we solved request logging at scale by moving from MariaDB to ClickHouse, Kafka, and Vector after our deprecated database engine couldn't keep up with billions of monthly requests.
Read more

### How Geocodio keeps 300M addresses up to date

Working with address data requires continual updates. Our in-house ETL, built on Laravel and SQLite, helps us expand our address point data on a daily basis.
Read more

### Geocodio's Development Manifesto

We recently wrote down the development principles we've been following at Geocodio for the past 10+ years. Thought it might be interesting to share.
Read more
Copyright © 2014-
2025
 Dotsquare LLC, Norfolk, Virginia. All rights reserved.
