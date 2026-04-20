---
title: Vercel confirms breach as hackers claim to be selling stolen data
url: https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/
site_name: hackernews_api
content_file: hackernews_api-vercel-confirms-breach-as-hackers-claim-to-be-sell
fetched_at: '2026-04-20T12:02:59.285571'
original_url: https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/
author: colesantiago
date: '2026-04-19'
description: Cloud development platform Vercel has disclosed a security incident after threat actors claimed to have breached its systems and are attempting to sell stolen data.
tags:
- hackernews
- trending
---

# Vercel confirms breach as hackers claim to be selling stolen data

 By 

###### Lawrence Abrams

* April 19, 2026
* 01:32 PM
* 0

Update 4/19/26: Added additional information from Vercel that was disclosed after publishing.

Cloud development platform Vercel has disclosed a security incident after threat actors claimed to have breached its systems and are attempting to sell stolen data.

Vercel is a cloud platform that provides hosting and deployment infrastructure for developers, with a strong focus on JavaScript frameworks.

The company is known for developing Next.js, a widely used React framework, and for offering services such as serverless functions, edge computing, and CI/CD pipelines that enable developers to build, preview, and deploy applications.

In a security bulletin published today, the company said a limited subset of customers was affected by a security breach.

"We've identified a security incident that involved unauthorized access to certain internal Vercel systems,"warns Vercel.

"We are actively investigating, and we have engaged incident response experts to help investigate and remediate. We have notified law enforcement and will update this page as the investigation progresses."

The company says its services have not been impacted and that it is working with impacted customers.

Vercel says it is taking steps to protect its customers, advising them toreview environment variables, use itssensitive environment variable feature, and to rotate secrets if needed.

After publishing this story, Vercel updated its advisory to state that the breach stemmed from the compromise of a third-party AI tool's Google Workspace OAuth application.

Vercel is advising Google Workspace administrators and Google account owners to check for the following application:



OAuth App: 110671459871-30f1spbu0hptbs60cb4vsmv79i7bbvqj.apps.googleusercontent.com

Vercel CEO Guillermo Rauch later shared additional detailson X, stating that the initial access occurred after a Vercel employee's Google Workspace account was compromised via a breach at the AI platform Context.ai.

According to Rauch, the attacker then escalated access from the compromised account into Vercel environments, where they were able to access environment variables that were not marked as sensitive and therefore not encrypted at rest.

While intended to contain non-sensitive information, the attacker gained further access after enumerating these variables.

"Vercel stores all customer environment variables fully encrypted at rest. We have numerous defense-in-depth mechanisms to protect core systems and customer data," Rauch said.

"We do have a capability, however, to designate environment variables as 'non-sensitive.' Unfortunately, the attacker got further access through their enumeration."

The company's investigation has confirmed that Next.js, Turbopack, and its other open-source projects remain safe.

Vercel has also rolled out updates to its dashboard, including an overview page of environment variables and an improved interface for managing sensitive environment variables.

Customers are strongly advised to review environment variables for sensitive information and enable the sensitive variable feature to ensure they are encrypted at rest.

If you have any information regarding this incident or other undisclosed attacks, you can contact us confidentially via Signal at 646-961-3731 or at tips@bleepingcomputer.com.

## Hacker claims to be selling stolen Vercel data

The disclosure comes after a threat actor claiming to be "ShinyHunters" posted on a hacking forum that they had breached Vercel and were selling access to company data.

It should be noted that while the hacker claims to be part of the ShinyHunters group, threat actors linked to recent attacks attributed to the ShinyHunters extortion gang have denied to BleepingComputer that they are involved in this incident.

In the forum post, the hacker claimed to be selling access keys, source code, and database data allegedly stolen from Vercel, along with access to internal deployments and API keys.

"This is just from Linear as proof, but the access I'm about to give you includes multiple employee accounts with access to several internal deployments, API keys (including some NPM tokens and some GitHub tokens)," reads the forum post.

A screenshot of a forum post shared by the threat actor on Telegram

The attacker also shared a text file containing Vercel employee information, which consists of 580 data records containing names, Vercel email addresses, account status, and activity timestamps. They also shared a screenshot of what appears to be an internal Vercel Enterprise dashboard.

BleepingComputer has not been able to independently confirm if the data or screenshot is authentic.

In messages shared on Telegram, the threat actor also claimed they were in contact with Vercel regarding the incident and that they discussed an alleged ransom demand of $2 million.

BleepingComputer contacted Vercel with additional questions about the breach, including whether any sensitive data or credentials were exposed and if they are negotiating with the attackers, and will update this story if we receive a response.

Update 4/19/26 6:14 PM ET: Updated article to add further information disclosed by Vercel.Update 4/19/26 7:21 PM ET: Updated article with additional information from Vercel's CEO.

## 99% of What Mythos Found Is Still Unpatched.

AI chained four zero-days into one exploit that bypassed both renderer and OS sandboxes. A wave of new exploits is coming.

At the Autonomous Validation Summit (May 12 & 14), see how autonomous, context-rich validation finds what's exploitable, proves controls hold, and closes the remediation loop.

Claim Your Spot

### Related Articles:

Data breach at edtech giant McGraw Hill affects 13.5 million accounts

McGraw-Hill confirms data breach following extortion threat

Stolen Rockstar Games analytics data leaked by extortion gang

Hims & Hers warns of data breach after Zendesk support ticket breach

CERT-EU: European Commission hack exposes data of 30 EU entities