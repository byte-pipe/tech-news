---
title: What To Do If Your Project Was Affected By The Vercel Breach - DEV Community
url: https://dev.to/dumebii/vercel-got-breached-heres-exactly-what-to-do-if-you-use-it-2026-guide-2k76
site_name: devto
content_file: devto-what-to-do-if-your-project-was-affected-by-the-ver
fetched_at: '2026-04-23T20:05:59.159608'
original_url: https://dev.to/dumebii/vercel-got-breached-heres-exactly-what-to-do-if-you-use-it-2026-guide-2k76
author: Dumebi Okolo
date: '2026-04-21'
description: Vercel confirmed a security incident on April 19, 2026 affecting customer environment variables.... Tagged with webdev, security, tutorial, beginners.
tags: '#webdev, #security, #tutorial, #beginners'
---

Vercel confirmed a security incident on April 19, 2026 affecting customer environment variables. Here's what happened in plain English, whether you're affected, and the exact steps to secure your account. No security expertise required.

TL;DR:On April 19, 2026, Vercel disclosed a security incident. Attackers compromised a third-party AI tool called Context.ai, used that access to take over a Vercel employee's Google Workspace account, and reached environment variables that weren't marked as "sensitive." If you deploy on Vercel — especially if any of your API keys, database URLs, or tokens weren't explicitly marked sensitive — you need to rotate them. This guide walks through exactly what to do, in order, without assuming any security background.

If you've deployed any app on Vercel, chances are that you have been compromised!

You've probably seen the news over the last 48 hours and felt that particular kind of low-grade panic where you're not sure if you should be doing something right now or not. The short answer is yes, you probably should. The longer answer, which is what this guide is for, is that the required actions are straightforward, don't take long, and don't require you to be a DevOps engineer or a security researcher.

This is a practical walk-through for developers, solo founders, small teams, and anyone who builds or has built on Vercel and is now wondering what "rotate your keys" actually means. Let's start with what actually happened.

## What Happened in the Vercel Breach (Plain English)

On April 19, 2026, Vercelpublished a security bulletindisclosing that attackers had accessed parts of their internal systems. The attack didn't start at Vercel. It started somewhere smaller, and that's actually the most interesting part of the story.

Here's how the breach actually happened, step by step:

A Vercel employee had signed up for a productivity tool calledContext.ai, an AI-powered office suite, using their Vercel Google Workspace account. When they signed up, they granted the app broad permissions into their Google account.

Context.ai itself got compromised. According toCyberScoop's reporting, the initial infection started in February 2026 when a Context.ai employee's computer was hit with Lumma Stealer malware after searching for Roblox game exploits. That malware harvested credentials including OAuth tokens.

The attackers used the compromised OAuth token to get into the Vercel employee's Google Workspace account. This bypassed multi-factor authentication entirely, because once an OAuth token is issued, it doesn't require re-authentication.

From that Google account, the attackers moved laterally into Vercel's internal systems: admin tools, issue trackers, internal environments. Once inside, they were able to read customer environment variables that weren't marked as "sensitive" in Vercel's dashboard.

A threat actor claiming to be part of the ShinyHunters groupposted on a cybercrime forumtrying to sell the stolen data for $2 million. Vercel has engaged Mandiant, CrowdStrike, and law enforcement.

The key detail most people are missing:this isn't about Vercel being insecure.Vercel encrypts sensitive environment variables at rest and those are confirmed safe. What got exposed are variables that weren't explicitly marked sensitive, meaning plaintext values the attacker could read once inside. If you ever added an API key, database URL, or token to Vercel without ticking the sensitive flag, it's potentially in the wrong hands.

## Am I Affected by the Vercel Breach?

Short answer: you're probably fine, but assume worst case and act accordingly.

Vercel stated the breach affected "a limited subset of customers" and said they've directly contacted those customers. If you haven't received an email from Vercel about this, you're likely not in the confirmed-affected group.

However — and this is important — there are two reasons to treat your credentials as potentially exposed anyway:

The investigation is ongoing. Vercel said they "continue to investigate whether and what data was exfiltrated" and will contact customers if more evidence emerges.

OAuth trust chains are deep. According toTrend Micro's technical analysis, the attack leveraged OAuth tokens issued around June 2024 and only detected in April 2026, meaning there may have been access for months before disclosure.

The practical rule: if you have environment variables in Vercel that were not explicitly marked "sensitive" and contain real credentials, rotate them. The cost of rotation is low. The cost of not rotating a compromised key is potentially catastrophic.

## How To Secure Your Vercel Account Right Now (In Order)

These are the actions to take today, in priority order. If you get through the first four, you've covered 80% of the risk.

### 1. Open Vercel and identify every environment variable not marked "sensitive"

Go to your Vercel dashboard, open each project, and review the Environment Variables tab. Any variable that doesn't have the "Sensitive" flag set should be treated as exposed.

Vercel has alsorolled out a dashboard updatethat gives you an overview page of all environment variables across projects. Use it to audit faster.

### 2. How To Rotate Your Keys To Be Safe

This is the step that trips people up. Rotating a credential means generating a new one at the service that issued it, then updating Vercel to use the new one. Do not just delete the variable in Vercel and assume the old credential is dead or disabled. It's still valid at the service until you explicitly revoke it.

The order of operations:

* Log in to the service that issued the credential (AWS, OpenAI, Supabase, GitHub, Stripe, whatever)
* Generate a new key
* Update the Vercel environment variable with the new value
* Mark the variable as "Sensitive" this time
* Redeploy your project to pick up the new value
* Go back to the issuing service and revoke the old key

### 3. Prioritise by blast radius

You probably have dozens of credentials. Rotate them in this order based on what they unlock:

Tier 1(critical):cloud provider keys (AWS access keys, GCP service accounts, Azure tokens), database credentials (Supabase service role keys, Postgres URLs, MongoDB connection strings), payment keys (Stripe, payment processors), source control tokens (GitHub PATs, deploy keys).

Tier 2(high):third-party SaaS API keys (OpenAI, Anthropic, Firecrawl, SendGrid, Resend, analytics tools), email signing keys, webhook secrets.

Tier 3(medium):internal service tokens, feature flags, non-credential configuration values.

The reasoning: a Stripe secret key in the wrong hands can drain accounts. A feature flag value can't. Triage accordingly.

### 4. Check activity logs for anything suspicious

In each service, look at the access logs for the past 30 days. You're looking for:

* API calls from IP addresses you don't recognise
* Activity from countries where nobody on your team is located
* Resource creation or deletion you didn't authorise
* New webhooks, deploy keys, or OAuth applications that you didn't add

For AWS, checkCloudTrail. For GCP, checkAudit Logs. For GitHub, check theorganization audit log. For Vercel itself, check the activity log in the dashboard.

### 5. Revoke any third-party AI or SaaS apps connected to your Google or Microsoft account

This is the specific vector that caused the breach. Go toGoogle Account → Security → Your connections to third-party appsand review every app that has access. Revoke anything you don't actively use, especially anything with broad permissions ("Allow All" is a red flag).

Do the same for Microsoft 365 if you use it, and for your GitHub account's OAuth applications.

### 6. Turn on passkeys or an authenticator app for Vercel (and everywhere else important)

Vercel supports passkeys and authenticator app MFA. If you're still using SMS-based 2FA, that's a weaker setup. SMS can be SIM-swapped. A hardware key or authenticator app is meaningfully better.

This won't protect you against OAuth-token-based attacks (which is what happened here), but it raises the cost of every other category of attack.

### 7. Use the "Sensitive" flag for every new environment variable going forward

Going forward, treat the Sensitive flag as mandatory, not optional. PerVercel's documentation, sensitive variables are encrypted at rest and cannot be read back through the dashboard after they're set. This is precisely the protection that the exposed variables in this breach didn't have.

Vercel has also announced they're updating the default to make new variables sensitive automatically, but until that rolls out, do it manually.

## Why This Matters Even If You Weren't Directly Hit

The reason this story is getting extended coverage:TechCrunch,The Hacker News,Help Net Security, Hacker News front page, etc, signals that the attack pattern is a template for what's coming.

What the breach did is that it exploited the fact that modern software teams connect a web of third-party tools to their identity providers, and each connection is a potential breach path.

The same attack shape could hit any platform. The affected parties in this case used Context.ai, an AI productivity tool. Next month it could be a different AI tool, a different note-taking app, a different calendar plugin. If any employee on your team has granted broad OAuth permissions to a small third-party app using their corporate Google or Microsoft account, you have the same exposure surface Vercel did.

## Best Practices To Keep Your System Safe

The defensive posture is the same one that's been best-practice for years but most teams don't enforce rigorously:

* Treat every third-party OAuth app as a potential attacker
* Grant the narrowest permissions that let the app work, never "Allow All"
* Review and revoke unused app connections quarterly
* Rotate credentials regularly. Every 90 days at minimum for production keys, 30 days for the highest-stakes ones
* Encrypt at rest, always. Mark every credential as sensitive
* Monitor access logs for anything you didn't do

## How Ozigi Responded To The Vercel breach (Because We Were Affected Too)

A quick note, since we deploy Ozigi on Vercel. Yes, we were in the group of affected customers. Here's what we did in the first 24 hours after disclosure, roughly matching the sequence above:

We rotated every credential in our Vercel environment, starting with our Supabase service role keys, our Google Cloud Vertex AI credentials, and our Dodo Payments keys. All of them are now marked sensitive.

We audited our Google Workspace connections and revoked every third-party app we weren't actively using, including two we'd forgotten were connected.

We checked our activity logs across Supabase, Vercel, and GCP for anomalies. Nothing suspicious so far, but we're continuing to monitor.

We're in the process of moving longer-lived credentials intoDopplerfor centralised management and automated rotation, rather than managing them directly in Vercel's dashboard.

Like a lot of small teams, our security posture wasn't as tight as it should have been.The honest truth is that "it hasn't happened yet" is the reason most small teams haven't invested in secrets management properly. This incident was the trigger to fix it.

## Frequently Asked Questions

### Does rotating my keys actually help if they've already been stolen?

Yes, and it's the single most important thing you can do. Stolen credentials only have value while they're valid. The moment you rotate and revoke the old key at the source service, the stolen one is useless. Every hour you wait is an hour the attacker could be using it.

### What does "mark as sensitive" mean in Vercel?

It's a flag on each environment variable that tells Vercel to encrypt the value at rest in a way that prevents it from being read back through the dashboard or API. Once marked sensitive, you can update the variable or delete it, but you can't see what the current value is. This is the flag that would have prevented the affected variables from being readable in this breach.

### Do I need to rotate everything, or just keys on Vercel?

Focus on Vercel first. Keys stored elsewhere (in a separate secrets manager, in a different hosting platform, in your local.envfiles) aren't affected by this specific incident. That said, this is a good prompt to review credential hygiene everywhere — many teams discover they haven't rotated core credentials in years.

### How often should I rotate API keys going forward?

Industry standardis every 30-90 days for production keys, depending on sensitivity. Payment and cloud provider keys should be closer to 30 days. Third-party SaaS keys can be 90 days. Internal service tokens should ideally be short-lived credentials with 1-24 hour TTLs, generated dynamically by a tool like HashiCorp Vault.

### Is there a tool that automates this?

Yes, several.DopplerandInfisicalare the most accessible for small teams and solo founders.HashiCorp VaultandAWS Secrets Managerare the enterprise-grade options but have a steeper setup cost.GitGuardianscans your repos for exposed secrets and can trigger automated rotation workflows.

### What's the difference between an OAuth token and an API key?

An API key is a static credential you generate once and use directly. An OAuth token is issued by an identity provider (Google, Microsoft) after a user authorises a third-party app, and represents delegated access to that user's account. The Vercel breach specifically exploited OAuth tokens. That's what allowed the attackers to bypass MFA, since OAuth tokens don't require re-authentication once issued.

### Should I stop using AI productivity tools?

No, but you should audit them carefully. The problem isn't AI tools specifically, it's any third-party app that gets broad permissions into your corporate identity systems. Apply the same scrutiny to a calendar plugin, a CRM integration, or an analytics connector that you would to an AI tool.

### How do I know if my credentials are being sold on the dark web?

You typically won't know directly. Some services (GitHub, AWS) have automated monitoring that flags exposed credentials if they appear in known sources. Tools likeHave I Been Pwnedmonitor email addresses, and enterprise security tools likeHudson Rocktrack infostealer-compromised credentials. For small teams, the honest answer is you rotate proactively and assume the worst, rather than trying to detect after the fact.

### What should I ask my team or vendors in the next 48 hours?

Three questions: Which of our third-party tools have OAuth access to our Google/Microsoft workspace? Which of our production credentials were stored in Vercel and not marked sensitive? Do we have a secrets rotation schedule, and when did we last rotate our highest-risk keys? If the answer to any of those is "I don't know," that's your starting point.

## Feedback and Community

If you went through the Vercel rotation this week, I'd genuinely like to hear how it went: what you found, what tripped you up, what tools you reached for. I'mDumebi on LinkedInand always open to comparing notes with other founders navigating the same incidents.

If you're rebuilding your stack and thinking about content tooling along with the rest,Ozigiis what we've been building: an AI content engine specifically designed not to sound like AI. It's free to try and we're in the middle of tightening everything in response to this breach, so you're getting it at its most security-conscious state.

Stay safe out there. This won't be the last supply chain attack of 2026, but knowing how to respond means the next one will take you hours to handle instead of days.

This article is based on publicly disclosed information as of April 21, 2026. The situation is unfolding. Refer toVercel's official security bulletinfor the latest updates.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse