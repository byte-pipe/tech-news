---
title: 13-hour AWS outage reportedly caused by Amazon's own AI tools
url: https://www.engadget.com/ai/13-hour-aws-outage-reportedly-caused-by-amazons-own-ai-tools-170930190.html
site_name: tldr
content_file: tldr-13-hour-aws-outage-reportedly-caused-by-amazons-ow
fetched_at: '2026-03-17T11:21:45.698315'
original_url: https://www.engadget.com/ai/13-hour-aws-outage-reportedly-caused-by-amazons-own-ai-tools-170930190.html
date: '2026-03-17'
published_date: '2026-02-20T17:09:30.000Z'
description: A recent Amazon Web Services outage was reportedly caused by the company's own AI agent. Employees have also noted related outages due to AI error.
tags:
- tldr
---

Advertisement
Advertisement
Advertisement
NurPhoto via Getty Images

A recent Amazon Web Services (AWS) outage that lasted 13 hours was reportedly caused by one of its own AI tools,according to reporting byFinancial Times. This happened in December after engineers deployed the Kiro AI coding tool to make certain changes, say four people familiar with the matter.

Kiro is an agentic tool, meaning it can take autonomous actions on behalf of users. In this case, the bot reportedly determined that it needed to "delete and recreate the environment." This is what allegedly led to the lengthy outage that primarily impacted China.

Amazon says it was merely a "coincidence that AI tools were involved" and that "the same issue could occur with any developer tool or manual action." The company blamed the outage on "user error, not AI error." It said that by default the Kiro tool “requests authorization before taking any action” but that the staffer involved in the December incident had "broader permissions than expected — a user access control issue, not an AI autonomy issue."

Advertisement
Advertisement
Advertisement

Multiple Amazon employees spoke toFinancial Timesand noted that this was "at least" the second occasion in recent months in which the company's AI tools were at the center of a service disruption. "The outages were small but entirely foreseeable," said one senior AWS employee.

The companylaunched Kiro in Julyand has sincepushed employees into using the tool. Leadership set an 80 percent weekly use goal and has been closely tracking adoption rates. Amazon also sells access to the agentic tool for a monthly subscription fee.

These recent outages follow a more serious event from October, in which a15-hour AWS outage disrupted serviceslike Alexa, Snapchat,Fortniteand Venmo, among others. The companyblamed a bug in its automation softwarefor that one.

However, Amazon disagrees with the characterization of certain products and services being unavailable as an outage. In response to theFinancial Timesreport, the company shared the followingstatement, which it also published on its news blog:

Advertisement
Advertisement
Advertisement

We want to address the inaccuracies in theFinancial Times' reportingyesterday. The brief service interruption they reported on was the result of user error—specifically misconfigured access controls—not AI as the story claims.

The disruption was an extremely limited event last December affecting a single service (AWS Cost Explorer—which helps customers visualize, understand, and manage AWS costs and usage over time) in one of our 39 Geographic Regions around the world. It did not impact compute, storage, database, AI technologies, or any other of the hundreds of services that we run. The issue stemmed from a misconfigured role—the same issue that could occur with any developer tool (AI powered or not) or manual action. We did not receive any customer inquiries regarding the interruption. We implemented numerous safeguards to prevent this from happening again—not because the event had a big impact (it didn't), but because we insist on learning from our operational experience to improve our security and resilience. Additional safeguards include mandatory peer review for production access. While operational incidents involving misconfigured access controls can occur with any developer tool—AI-powered or not—we think it is important to learn from these experiences. The Financial Times' claim that a second event impacted AWS is entirely false.

For more than two decades, Amazon has achieved high operational excellence with our Correction of Error (COE) process. We review these together so that we can learn from any incident, irrespective of customer impact, to address issues before their potential impact grows larger.

Update, February 21 2026, 11:58AM ET:This story has been updated to include Amazon's full statement in response to the Financial Times report.

* About our ads
Advertisement
Advertisement