---
title: AWS raises GPU prices 15% on a Saturday • The Register
url: https://www.theregister.com/2026/01/05/aws_price_increase/
site_name: hackernews_api
fetched_at: '2026-01-06T19:06:59.421337'
original_url: https://www.theregister.com/2026/01/05/aws_price_increase/
author: Brajeshwar
date: '2026-01-06'
description: AWS raises GPU prices 15% on a Saturday, hopes you weren't paying attention
tags:
- hackernews
- trending
---

#### PaaS + IaaS

# AWS raises GPU prices 15% on a Saturday, hopes you weren't paying attention



## An anomaly or the beginning of a new trend? My bet's on the latter

I've been trackingAWSfor a long time, with a specific emphasis on pricing. "What happens if AWS hikes prices" has always been something of a boogeyman, trotted out as a hypothetical to urge folks to avoid taking dependencies on a given provider.

Over the weekend - on a Saturday, no less - that hypothetical became real.

AWS hasquietly raised priceson its EC2 Capacity Blocks for ML by approximately 15 percent. The p5e.48xlarge instance – eight NVIDIA H200 accelerators in a trenchcoat – jumped from $34.61 to $39.80 per hour across most regions, while the p5en.48xlarge climbed from $36.18 to $41.61. Customers in US West (N. California) face steeper hikes, with p5e rates rising from $43.26 to $49.75. The change had been telegraphed: AWS's pricing page noted (and bizarrely, still does) that "current prices are scheduled to be updated in January, 2026," though the company neglected to mention which direction.

This comes about seven months after AWS trumpeted "up to 45% price reductions" for GPU instances - though that announcement covered On-Demand and Savings Plans rather than Capacity Blocks. Funny how that works.

For the uninitiated, Capacity Blocks are AWS's answer to "I need guaranteed GPU capacity for my ML training job next Tuesday." You reserve specific GPU instances for a defined time window – anywhere from a day to a few weeks out – and pay up front at a locked-in rate. It's popular with companies doing serious ML work who can't afford to have a training run interrupted because spot capacity evaporated. The pricing should make it abundantly clear that the people using this aren't hobbyists; these are teams with budgets measured in millions.

An Amazon spox told us via email, "EC2 Capacity Blocks for ML pricing vary based on supply and demand patterns, as described on the product detail page. This price adjustment reflects the supply/demand patterns we expect this quarter."

To be clear, AWS has raised prices before, but rarely as a straight increase to a line item. The company prefers to change pricing dimensions entirely, oftenspinning this as a price reduction for most customers– a claim I'd characterize as "creative." Historical straight-up price increases have been tied to regulatory actions: per-SMS charges in certain markets and the like. This is different.

The timing is curious for another reason: it hands Azure and GCP a talking point on a silver platter. Both have been aggressively courting ML workloads, and "AWS just raised GPU prices 15%" is exactly the kind of ammunition enterprise sales teams dream about. Whether the competitors can actually absorb the demand is another question – GPU constraints are hardly unique to AWS – but perception matters in enterprise deals.

For companies with Enterprise Discount Programs or other negotiated agreements, this raises uncomfortable questions. EDPs typically guarantee discounts off public pricing – so if public pricing goes up 15 percent, your "discounted" rate just got more expensive in absolute terms, even if the percentage held steady. I expect some pointed conversations between AWS account teams and their larger customers in the coming weeks.

### Why are they doing this?

It's hard not to see this as a bellwether. GPUs are increasingly constrained globally as the world pivots to generating slop-as-a-service in every conceivable domain. The question is what this means for other resource types down the road. Does theglobal RAM crunchmean RAM-centric services are next? You can ignore ML Capacity Block pricing if you're not running machine learning workloads – which describes north of 95 percent of most companies' cloud spend – but RAM touches every service AWS offers. Well, possibly excepting their support function, though that'srapidly becoming "AI-Powered"too, so give it time.

* Deploying to Amazon's cloud is a pain in the AWS younger devs won't tolerate
* AWS adds hybrid cloud storage support for Nutanix's AHV hypervisor
* Jassy taps 27-year Amazon veteran to run AGI org, which is now definitely a thing that exists
* Smartphones face a memory cost crunch – and buyers aren't in the mood

The canary-in-the-coal-mine concern here isn't GPUs specifically, but rather the precedent it establishes. AWS has spent two decades conditioning customers to expect prices only ever go down. That expectation is now broken. Once you've raised prices on one service and the world doesn't end, the second increase becomes easier. And the third. The playbook has changed.

Keep an eye on services where AWS faces genuine supply constraints or where their costs have materially increased. Graviton instances have been priced aggressively to drive adoption – what happens when ARM chip supply tightens? Data transfer costs have been a cash cow for years, but they've also been stable; are those next? I don't have inside information, but I do have pattern recognition, and the pattern just shifted.

AWS has long benefited from the assumption that cloud pricing only trends in one direction. That assumption died on a Saturday in January, with all the fanfare of a Terms of Service update. The question isn't whether this matters – it does. The question is whether it's an anomaly or the new normal. My money's on the latter. ®



Get our

Tech Resources

Share

#### More about

* Amazon
* AWS
* AWS Graviton

More like these

×

### More about

* Amazon
* AWS
* AWS Graviton

### Narrower topics

* Amazon Bedrock
* Aurora
* Ebook
* EC2
* Kindle
* S3

### Broader topics

* Arm
* Cloud Computing
* Jeff Bezos
* Microprocessor

#### More about

Share

#### More about

* Amazon
* AWS
* AWS Graviton

More like these

×

### More about

* Amazon
* AWS
* AWS Graviton

### Narrower topics

* Amazon Bedrock
* Aurora
* Ebook
* EC2
* Kindle
* S3

### Broader topics

* Arm
* Cloud Computing
* Jeff Bezos
* Microprocessor

#### TIP US OFF

Send us news
