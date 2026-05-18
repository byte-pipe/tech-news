---
title: 'AWS Outage May 2026: Lessons for Database Disaster Recovery'
url: https://www.singlestore.com/blog/aws-outage-may-2026-cross-region-disaster-recovery/
site_name: tldr
content_file: tldr-aws-outage-may-2026-lessons-for-database-disaster
fetched_at: '2026-05-19T06:00:35.430655'
original_url: https://www.singlestore.com/blog/aws-outage-may-2026-cross-region-disaster-recovery/
date: '2026-05-19'
published_date: '2026-05-14T13:37:11Z'
description: Coinbase, FanDuel and CME went dark after an AWS data centre overheated. What happened, what it cost, and what cross-region DR really looks like.
tags:
- tldr
---

At 23:50 UTC on Thursday, 7 May 2026, a room in an Amazon data centre in Northern Virginia overheated. Multiple cooling units in availability zone use1-az4 failed. Within minutes, EC2 instances and EBS volumes on the affected racks were losing power. Within the hour, traders trying to close positions onCoinbase, bettors trying to cash out during Game 2 of theLakers and Thunder Western Conference semifinal on FanDuel, and institutional users on CME Direct were staring at error screens.

For most of those users, the next several hours were the operational definition of helplessness. There was no failover button. There was no secondary region to switch to. They could only refresh.

If you run a mission-critical workload on a single AWS region, this post is for you.SingleStore Smart DRprovides cross-region replication with a target RPO of up to 10 minutes and no idle compute cost in the secondary region until you fail over.

## Key takeaways

* A single-zonethermal event in AWS US-EAST-1caused multi-hour outages at Coinbase, FanDuel and CME Group on 7–8 May 2026.
* Coinbase was offline for approximately seven hours. AWS recovery extended into the following afternoon.
* The standard AWS service credit covers about 10% of monthly compute spend on impacted instances. It does not cover lost revenue, regulatory exposure or customer trust.
* Multi-AZ high availability did not save Coinbase, because their latency-sensitive matching engine ran in a single zone by design. Multi-region disaster recovery is a different problem.
 

## What happened on 7–8 May 2026

Thethermal eventbegan at approximately 17:25 PDT on Thursday, 7 May. Cooling capacity in a single data centre hall dropped, triggering a power loss that physically damaged EC2 instances and EBS volumes on affected racks. AWS shifted traffic away from the affected zone, but recovery depended on physically restoring cooling capacity before damaged hardware could safely return to service. Coolingwas stabilised at pre-event levels at 13:50 PT on Friday, 8 May, more than 20 hours after the incident began. Most affected instances and volumes were restored at that point.

The root cause matters. This was not a software bug or a misconfiguration. It was a building that got too hot. Software orchestration cannot automatically reroute around physical hardware damage. That is why the rest of this post is about cross-region disaster recovery rather than high availability.

## Who was impacted

Coinbasewas offline for approximately seven hours. Trading, exchange access, balance updates, Prime, the international venue and the derivatives exchange all went dark. The disruption arrived at the end of an already difficult week for the company: on Monday, Coinbase had announceda 14% workforce reduction of around 700 employees. On Thursday afternoon, hours before the outage began, the companyreported a Q1 net loss of $394 millionand a 31% year-on-year revenue decline.

CEO Brian Armstrong was unusually direct about what went wrong. Ina public statement on X, he wrote that the outage was "never acceptable", and acknowledged that while most Coinbase systems are designed to tolerate the failure of a single AWS availability zone, the centralised exchange did not. Coinbase's Head of Platform Rob Witoff later confirmed that the primary exchange systems run in a single zone to minimise latency, and that backup systems "did not work as expected during the incident, extending the outage and forcing engineers to manually execute disaster recovery procedures".

FanDuelwent offline at approximately 21:00 ET, just as Game 2 of the Lakers and Thunder semifinal tipped off. This is, by some margin, the worst possible window for a US sportsbook to fail. Live bets could not be cashed out. Users posted screenshots demanding refunds and bonuses, some threatening legal action.FanDuel acknowledged "technical difficulties prohibiting users from accessing our platform"before confirming the AWS link about two hours later.

CME Groupreported login and latency issues on CME Direct, its institutional trading platform. For a regulated derivatives exchange, even short outages create aregulatory and operational risk management question, not just a technical one.

These are the three companies whose outages made the news. The actual downstream was much wider. Any business with production workloads in US-EAST-1 that depended on EC2 instances or EBS volumes in availability zone use1-az4 may have experienced impairments. That includes some SingleStore Helios customers running on AWS. (Helios is our fully managed cloud database service.) Many had architectures that absorbed the disruption cleanly. Others felt it directly. The companies in the press are visible because public markets oblige them to file statements. The teams who quietly spent the night on a bridge call do not show up in headlines, but the impact on their business is no less real.

## The hidden cost: SLA credits versus reality

AWS will compensate affected customers under the standard EC2 service level agreement. The credit is typically 10% of monthly compute spend on impacted instances. There is no compensation for lost revenue, lost customer trust or regulatory exposure. Independent research consistently puts the real cost much higher: the2024 ITIC Hourly Cost of Downtime surveyfound that 90% of mid-size and large enterprises lose more than $300,000 per hour during an outage, and 41% lose between $1 million and $5 million per hour. In finance and trading the losses run higher still.

The cloud SLA is not your business continuity plan. It is a small refund.

## High availability and disaster recovery solve different problems

The temptation, after an event like this, is to conclude that multi-AZ is the answer. Two things complicate that conclusion.

First, Coinbase already had multi-AZ for most workloads. Their statement made this explicit: "Coinbase systems are designed to be resilient to a single zone outage. In this case, we observed failures impacting multiple AWS zones." The exchange itself ran in a single zone by design, optimised for latency and customer co-location. If you run a real-time operational workload that is genuinely latency-sensitive, you have probably made similar trade-offs.

Second, even where multi-AZ is in place, it does nothing for a region-level event. AWS treats availability zones as the failure domain for high availability. Disaster recovery is about regions, and regions are independent on purpose. A thermal event in US-EAST-1 will not move your data to US-WEST-2 unless you have explicitly arranged for it to do so.

The distinction matters. High availability protects you from a bad day in one rack or one zone. Disaster recovery protects you from a bad day in one region. Most production workloads need both.

## A note to our customers

We want to be straightforward with the Helios customers reading this. Some of you run mission-critical, real-time workloads on Helios in AWS US-EAST-1. Not all of you have Smart DR enabled. If you spent Thursday night on a bridge call or watching the dashboards with a knot in your stomach, we understand. Operations leadership rarely gets credit for resilience investments until the moment the building gets too hot, and at that point the conversation is no longer about budget; it is about how fast you can recover.

The honest reality is that this will happen again. US-EAST-1 has been the source of repeated significant outages over the past several years, and the underlying cause this time was a physical one that no amount of software design eliminates. The next regional event is not a question of if; it is a question of when, and which of your workloads is sitting on the affected hardware when it happens. We would rather have the conversation with you now, while the dashboards are green, than during the next incident.

If you are a SingleStore customer and you do not have a cross-region disaster recovery posture today, please reach out to your account team or your customer success contact. We will work through your current architecture with you, your application-level failover requirements, what a secondary region would actually need to do for you, and whetherSmart DRis the right fit. Sometimes it is not, and we will say so. The point is to make sure you walk out of that conversation with a plan you trust, before the next outage forces the conversation for you.

## What SingleStore Smart DR does

SingleStore Helios Smart DRis our cross-region disaster recovery service for Helios. It is supported on AWS, GCP, and Azure. In one sentence, it maintains a continuous asynchronous replica of your database in a geographically separate region, with failover and failback driven from the portal or the API. The substance:

* RPO of up to 10 minutes.Asynchronous database replication runs continuously between the primary and secondary region. In the event of a regional outage, you lose at most the data that had not yet been replicated.
* No idle compute by default.You pay only for storage and data transfer until you fail over. Traditional active-passive disaster recovery doubles your infrastructure bill. Smart DR does not, unless you explicitly enable Hot Standby.
* Full topology replication.It is not just data. Smart DR replicates workspace configuration, users, roles and permissions, firewall policies, ingest pipelines and metadata. After failover, the secondary region looks like the primary, with a new connection string.
* Failover and failback in a few clicks.From the Smart DR configuration page in the portal, click Failover, confirm, and the system provisions workspaces, attaches databases and emits a connection string. Failback follows the same pattern, with incremental sync rather than a full reload.
* Hot Standby for faster RTO.Enable Hot Standby to keep compute warm in the secondary region, configure private endpoints in advance, and test DR behaviour without disrupting production. With Hot Standby, target RTO is approximately 20 minutes. A DR plan that has never been exercised is a hypothesis.
* Works alongside Point-in-Time Recovery.PITRoperates independently. The combination protects you against both regional outages and logical errors such as a bad deployment or a destructive query.

## Where Smart DR stops and your DR plan begins

We are being honest about the constraints. Smart DR protects the database recovery path. It does not remove the need for an end-to-end application disaster recovery plan.

You still need to think through application behaviour during failover, networking, private endpoints, DNS or connection management, operational ownership and runbooks. Who makes the failover decision. How the application reconnects. How you validate correctness in the target region. How you test the process regularly. These are questions Smart DR does not answer for you, and we would rather say so than pretend otherwise.

Replication is asynchronous, which is the right trade-off for an operational database but means it is not a synchronous multi-region active-active topology. The 10-minute RPO is a ceiling, not a guarantee; actual RPO depends on workload characteristics and replication lag at the moment of failure.

## Three things to do this week

Whether or not you are a SingleStore customer, three things are worth doing in the next seven days.

1. Map your region affinities.For each tier of your application (presentation, API, application logic, primary database, cache, message bus, object storage, analytics), write down the AWS region and, where applicable, the availability zone. You will probably find at least one tier you assumed was multi-region and is not.
2. Stress-test your assumed RTO.Sit with your engineering lead and walk through what it would actually take to restore service if US-EAST-1 went offline for six hours starting now. Be specific. Who runs the runbook. Where is the runbook. When was it last exercised. What is the connection string for the secondary region. What does DNS look like.
3. Decide what you are buying.Cross-region disaster recovery is an insurance product. The premium is database replication cost. The payout is everything you do not lose when the chillers fail. Set a number for what an hour of downtime costs your business. Compare it to the replication cost. The decision usually becomes obvious in one direction or the other.

For SingleStore customers ready to enable Smart DR, thedocumentation walks through setup, and ouroriginal Smart DR product blogcovers the design philosophy in more depth. Your account team can scope a pilot and a readiness test against your current workload.

## Closing

The internet still runs in buildings, and buildings can overheat. That is the part of the story no architecture diagram makes visible. The teams at Coinbase, FanDuel, CME and the other affected platforms responded well to a hard situation, and we have a great deal of sympathy for the engineers who spent Thursday night and Friday morning on a recovery call.

The lesson we take from May 2026 is not that AWS is unreliable. AWS is, on the whole, extremely reliable, and the engineering response during this event was professional. The lesson is that being on a reliable provider is not the same as being resilient. Resilience is something you own. It lives in the choices you make about where your data is, how often it replicates, and how quickly you can run your application in a different region. Smart DR is one option for that. There are others. The only choice that is not available is to not make a choice.