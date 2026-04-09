---
title: Today is when Amazon brain drain finally caught up with AWS • The Register
url: https://www.theregister.com/2025/10/20/aws_outage_amazon_brain_drain_corey_quinn/
site_name: hackernews_api
fetched_at: '2025-10-21T11:08:27.148786'
original_url: https://www.theregister.com/2025/10/20/aws_outage_amazon_brain_drain_corey_quinn/
author: raw_anon_1111
date: '2025-10-20'
description: Today is when the Amazon brain drain sent AWS down the spout
tags:
- hackernews
- trending
---

#### PaaS + IaaS

# Today is when the Amazon brain drain finally sent AWS down the spout



## When your best engineers log off for good, don’t be surprised when the cloud forgets how DNS works

column"It's always DNS" is a long-standing sysadmin saw, and with good reason: a disproportionate number of outages are at their heart DNS issues. And so today, as AWS is still repairing its downed cloud as this article goes to press, it becomes clear that the culprit is once again DNS. But if you or I know this, AWS certainly does.

And so, a quiet suspicion starts to circulate: where have the senior AWS engineers who've been to this dance before gone? And the answer increasingly is that they've left the building — taking decades of hard-won institutional knowledge about how AWS's systems work at scale right along with them.

### What happened?

AWS reports that on October 20, at 12:11 AM PDT, it began investigating “increased error rates and latencies for multiple AWS services in the US-EAST-1 Region.” About an hour later, at 1:26 AM, the company confirmed “significant error rates for requests made to the DynamoDB endpoint” in that region. By 2:01 AM, engineers had identifiedDNS resolution of the DynamoDB API endpointfor US-EAST-1 as the likely root cause, which led to cascading failures for most other things in that region. DynamoDB is a "foundational service" upon which a whole mess of other AWS services rely, so the blast radius for an outage touching this thing can be huge.

As a result,much of the internet stopped working: banking, gaming, social media, government services, buying things I don't need on Amazon.com itself, etc.

AWS has given increasing levels of detail, as is their tradition, when outages strike, and as new information comes to light. Reading through it, one really gets the sense that it took them 75 minutes to go from "things are breaking" to "we've narrowed it down to a single service endpoint, but are still researching," which is something of a bitter pill to swallow. To be clear: I've seen zero signs that this stems from a lack of transparency, and every indication that they legitimately did not know what was breaking for a patently absurd length of time.

Note that for those 75 minutes, visitors to the AWS status page (reasonably wondering why their websites and other workloads had just burned down and crashed into the sea) were met with an "all is well!" default response. Ah well, it's not as if AWS hadpreviously called out slow outage notification timesas an area for improvement.Multiple timeseven. We cankeep doing thisif you'd like.

### The prophecy

AWS is very, very good at infrastructure. You can tell this is a true statement by the fact that a single one of their 38 regions going down (albeit a very important region!) causes this kind of attention, as opposed to it being "just another Monday outage." At AWS's scale, all of their issues are complex; this isn't going to be a simple issue that someone should have caught, just because they've already hit similar issues years ago and ironed out the kinks in their resilience story.

Once you reach a certain point of scale, there are no simple problems left. What's more concerning to me is the way it seems AWS has been flailing all day trying to run this one to ground. Suddenly, I'm reminded of something I had tried very hard to forget.

At the end of 2023, Justin Garrison left AWS androasted them on his way out the door. He stated that AWS had seen an increase in Large Scale Events (or LSEs), and predicted significant outages in 2024. It would seem that he discounted the power of inertia, but the pace of senior AWS departures certainly hasn't slowed — and now, with an outage like this, one is forced to wonder whether those departures are themselves a contributing factor.

You can hire a bunch of very smart people who will explain how DNS works at a deep technical level (or you can hire me, who will incorrect you by explaining that it's a database), but the one thing you can't hire for is the person who remembers that when DNS starts getting wonky, check that seemingly unrelated system in the corner, because it has historically played a contributing role to some outages of yesteryear.

When that tribal knowledge departs, you're left having to reinvent an awful lot of in-house expertise that didn't want to participate in your RTO games, or play Layoff Roulette yet again this cycle. This doesn't impact your service reliability — until one day it very much does, in spectacular fashion. I suspect that day is today.

* AWS outage exposes Achilles heel: central control plane
* Major AWS outage across US-East region breaks half the internet
* Amazon spills plan to nuke Washington...with X-Energy mini-reactors
* Amazon turns James Bond into the Man Without the Golden Gun

### The talent drain evidence

This isThe Register, a respected journalistic outlet. As a result, I know that if I publish this piece as it stands now, an AWS PR flak will appear as if by magic, waving their hands, insisting that "there is no talent exodus at AWS," a la Baghdad Bob. Therefore, let me forestall that time-wasting enterprise with some data.

* It is a fact that there have been27,000+ Amazonians impacted by layoffsbetween 2022 and 2024, continuing into 2025. It's hard to know how many of these were AWS versus other parts of its Amazon parent, because the company is notoriously tight-lipped about staffing issues.
* Internal documents reportedly say that Amazonsuffers from 69 percent to 81 percent regretted attritionacross all employment levels. In other words, "people quitting who we wish didn't."
* The internet is full of anecdata of senior Amazonians lamenting the hamfisted approach of their Return to Office initiative;experts have weighed inciting similar concerns.

If you were one of the early employees who built these systems, the world is your oyster. There's little reason to remain at a company that increasingly demonstrates apparent disdain for your expertise.

### My take

This is a tipping point moment. Increasingly, it seems that the talent who understood the deep failure modes is gone. The new, leaner, presumably less expensive teams lack the institutional knowledge needed to, if not prevent these outages in the first place, significantly reduce the time to detection and recovery. Remember, there was a time when Amazon's "Frugality" leadership principle meant doing more with less, not doing everything with basically nothing. AWS's operational strength was built on redundant, experienced people, and when you cut to the bone, basic things start breaking.

I want to be very clear on one last point. This isn't about the technology being old. It's about the people maintaining it being new. If I had to guess what happens next, the market will forgive AWS this time, but the pattern will continue.

AWS will almost certainly say this was an "isolated incident," but when you've hollowed out your engineering ranks, every incident becomes more likely. The next outage is already brewing. It's just a matter of which understaffed team trips over which edge case first, because the chickens are coming home to roost. ®



Get our

Tech Resources

Share

#### More about

* Amazon
* AWS
* Layoff

More like these

×

### More about

* Amazon
* AWS
* Layoff
* Outage

### Narrower topics

* Amazon Bedrock
* AWS Graviton
* Ebook
* EC2
* Kindle
* S3

### Broader topics

* Cloud Computing
* Employment
* Jeff Bezos

#### More about

Share

#### More about

* Amazon
* AWS
* Layoff

More like these

×

### More about

* Amazon
* AWS
* Layoff
* Outage

### Narrower topics

* Amazon Bedrock
* AWS Graviton
* Ebook
* EC2
* Kindle
* S3

### Broader topics

* Cloud Computing
* Employment
* Jeff Bezos

#### TIP US OFF

Send us news
