---
title: I Verified My LinkedIn Identity. Here's What I Actually Handed Over. | THE LOCAL STACK
url: https://thelocalstack.eu/posts/linkedin-identity-verification-privacy/
site_name: hackernews_api
content_file: hackernews_api-i-verified-my-linkedin-identity-heres-what-i-actua
fetched_at: '2026-02-22T06:00:14.236913'
original_url: https://thelocalstack.eu/posts/linkedin-identity-verification-privacy/
author: ColinWright
date: '2026-02-21'
description: I wanted a blue badge on LinkedIn. To get it, I gave a US company my passport, my face, and my biometric data. Then I read the fine print.
tags:
- hackernews
- trending
---

# I Verified My LinkedIn Identity. Here's What I Actually Handed Over.

Feb 16, 2026

10 min read

privacy, linkedin, biometrics, gdpr, cloud-act, identity

I wanted the blue checkmark on LinkedIn. The one that says “this person is real.” In a sea of fake recruiters, bot accounts, and AI-generated headshots, it seemed like a smart thing to do.

So I tapped “verify.” I scanned my passport. I took a selfie. Three minutes later — done. Badge acquired. I felt a tiny dopamine hit of legitimacy.

Then I did what apparently nobody does. I went and read the privacy policy and terms of service.

Not LinkedIn’s. Theothercompany’s.

## Wait, What Other Company?

When you click “verify” on LinkedIn, you’re not giving your passport to LinkedIn. You get redirected to a company calledPersona. Full name: Persona Identities, Inc. Based in San Francisco, California.

LinkedIn is their client. You are the face being scanned.

I had never heard of Persona before this. Most people haven’t. That’s kind of the point — they sit invisibly between you and the platforms you trust.

So I downloaded their privacy policy (18 pages) and their terms of service (16 pages). Here’s what I found.

## Everything I Gave Them

For a three-minute identity check, this is what Persona collected:

* Myfull name— first, middle, last
* Mypassport photo— the full document, both sides, all data on the face of it
* Myselfie— a photo of my face taken in real-time
* Myfacial geometry— biometric data extracted from both images, used to match the selfie to the passport
* MyNFC chip data— the digital info stored on the chip inside my passport
* Mynational ID number
* Mynationality, sex, birthdate, age
* Myemail, phone number, postal address
* MyIP address, device type, MAC address, browser, OS version, language
* Mygeolocation— inferred from my IP

And then there’s the weird stuff:

* Hesitation detection— they tracked whether I paused during the process
* Copy and paste detection— they tracked whether I was pasting information instead of typing it

Behavioral biometrics. On top of the physical biometrics. For a LinkedIn badge.

## They Also Called Their Friends

Persona didn’t just use what I gave them. They went and cross-referenced me against what they call their “global network of trusted third-party data sources”:

* Government databases
* National ID registries
* Consumer credit agencies
* Utility companies
* Mobile network providers
* Postal address databases

I scanned my passport for a checkmark. They ran a background check.

## My Face Is Training Data

Here’s something I almost missed. Buried in a table on page 6 of the privacy policy, under “legitimate interests”:

They use uploaded images of identity documents — that’s my passport —to train their AI. They’re teaching their system to recognize what passports look like in different countries. They also use your selfie to “identify improvements in the Service.”

The legal basis? Not consent.Legitimate interest.Meaning they decided on their own that it’s fine. Under GDPR, they’re supposed to balance their “interest” against your fundamental rights. Whether feeding European passports into machine learning models passes that test — well, that’s a question worth asking.

I came for a badge. I stayed as training data.

## Where Does My Face Go?

Once Persona has your data, here’s who gets a copy:

LinkedIn receives:

* Your full name
* Your birth year
* Government ID type and issuing authority
* Verification result
* A blurred version of your ID (everything redacted except your name and portrait)

Also with access:

* Persona’s service providers— vendors working on their behalf
* Their “global network of data partners”— those third-party databases work both ways
* Affiliates and subsidiaries— related companies that share “common data systems”
* Anyone who buys Persona— in a merger, acquisition, or bankruptcy, your data goes with the deal
* Law enforcement— and this is where it gets really interesting

And then there’s the subprocessor list. Persona publishes who else touches your data. I wish I hadn’t looked.

## The 17 Companies That Touch Your Face

Persona maintains apublic list of subprocessors— third-party companies that process your personal data on their behalf. Here’s the full list:

Company

What They Do With Your Data

Location

Anthropic

Data Extraction and Analysis

San Francisco, USA

OpenAI

Data Extraction and Analysis

San Francisco, USA

Groqcloud

Data Extraction and Analysis

San Jose, USA

AWS

Infrastructure, Image Processing

Houston, USA

Google Cloud Platform

Infrastructure as a Service

Mountain View, USA

Resistant AI

Document Analysis

New York, USA

FingerprintJS

Device Analysis

Chicago, USA

MongoDB

Database Services

New York, USA

Snowflake

Database Services

Bozeman, USA

Elasticsearch

Search and Analytics Engine

Mountain View, USA

Confluent

ETL Services

Mountain View, USA

DBT

ETL Services

Philadelphia, USA

Sigma Computing

Data Analytics

San Francisco, USA

Tableau

Data Analytics

Seattle, USA

Stripe

Credit Card Processing

South San Francisco, USA

Twilio

Communication APIs (Phone, SMS)

Denver, USA

Persona Identities Canada

Customer Support & Development

Toronto, Canada

Count them.17 companies.16 in the United States. 1 in Canada.Zero in the EU.

Let that sink in. You scanned your European passport for a European professional network, and your data went exclusively to North American companies. Not a single EU-based subprocessor in the chain.

And look at who’s doing “Data Extraction and Analysis” —Anthropic, OpenAI, and Groqcloud.Three AI companies are processing your passport and selfie data. Your government-issued identity document is being fed through the same companies that build large language models and AI systems.

AWS handles “Image Processing.” That’s your face going through Amazon’s infrastructure. FingerprintJS — a company literally named after the thing it does — handles “Device Analysis.” They’re fingerprinting your device while Persona fingerprints your face.

Remember when the privacy policy said data is stored in the “United States and Germany”? The Germany part is technically true — maybe some data sits there. But every single company thatprocessesyour data is American. The CLOUD Act doesn’t just apply to Persona. It applies toall 16 of these US subprocessors too.

## The CLOUD Act: Why Frankfurt Doesn’t Protect You

Persona has data centers in theUnited States and Germany. If you’re in Europe, you might think: great, my data is probably sitting on a German server, protected by GDPR, safe from American reach.

It’s not.

Persona is a US company. Incorporated in California. This means they’re subject to theUS CLOUD Act— the Clarifying Lawful Overseas Use of Data Act, signed in 2018.

Here’s what the CLOUD Act does in plain language:it allows US law enforcement to force any US-based company to hand over data, even if that data is stored on a server outside the United States.

Your passport scan can be sitting in a data center in Frankfurt. A US court issues a warrant. Persona has to comply. The physical location of the server doesn’t matter. What matters is the legal location of the company.

And Persona’s privacy policy confirms it. Their exact words:

We will access, disclose, and preserve personal data when we believe doing so is necessary to comply with applicable law or respond to valid legal process, including fromlaw enforcement, national security, or other government agencies.

“National security.” Those two words do a lot of heavy lifting. Under US law, national security requests — like FISA court orders or National Security Letters — can come withgag orders. Persona couldn’t tell you they handed over your data even if they wanted to.

## “But There’s the Data Privacy Framework!”

Yes, Persona says they comply with theEU-US Data Privacy Framework(DPF). They certified with the US Department of Commerce. They follow the principles. It’s all very official.

Here’s the thing about the DPF: it’s the replacement forPrivacy Shield, which the European Court of Justice killed in 2020. The reason? US surveillance laws made it impossible to guarantee European data was safe.

The DPF exists because the US signed an Executive Order (14086) promising to behave better. But an Executive Order is not a law. It’s a presidential decision. It can be changed or revoked by any future president with a pen stroke.

Privacy activists — including noyb, the organization behind the original Schrems rulings — have already challenged the DPF. The legal foundation your data is “protected” by is, at best, temporary.

So the reality looks like this:

1. You scan your passport in Madrid, Berlin, or Dublin
2. Persona stores it — maybe in Germany, maybe in the US
3. The CLOUD Act gives US authorities access regardless of where it sits
4. The DPF is supposed to protect you, but it’s built on sand
5. A national security request could grab your biometric data without you ever knowing

Your European passport is one quiet subpoena away from a US government system.

## The Biometrics Time Bomb

Let me be clear about what “biometric data” means here.

Persona extracts themathematical geometry of your facefrom your selfie and from your passport photo. This isn’t just a picture — it’s a numerical map of the distances between your eyes, the shape of your jawline, the geometry of your features. It’s data that uniquely identifies you. And unlike a password,you can’t change your face if it gets compromised.

Their policy says this scan data is destroyed “upon completion of Verification or within six months of your last interaction.” Good.

But there’s an exception:“unless Persona is otherwise required by law or legal process to retain the data.”

That exception, combined with the CLOUD Act, means a US legal process could force Persona to keep your biometric data indefinitely. The six-month clock means nothing if a court says “hold onto this.”

## The $50 Safety Net

Now let’s talk about what happens if things go wrong. Say there’s a breach. Say your passport scan, your facial geometry, and your national ID number end up in the wrong hands.

Persona’s Terms of Service cap their liability at$50 USD.

Your passport. Your face. Your biometric data. Your national ID number. Fifty dollars.

They also includemandatory binding arbitration— no court, no jury, no class action. You can only bring claims individually. Through the American Arbitration Association. Even if you’re in Europe and the dispute is about European data.

For EU/EEA residents, the ToS says Irish law governs the contract. Which sounds better until you remember:Irish law governs the contract, but US law governs the company.The CLOUD Act doesn’t care what your contract says.

## What You Should Do

If you’ve already verified — like me — here’s what I’d recommend:

1. Request your data.Emailidv-privacy@withpersona.comorprivacy@withpersona.com. Under GDPR, they have 30 days to respond.

2. Request deletion.The verification is done. LinkedIn already has the result. There is no reason for Persona to keep your passport scan and facial geometry on their servers. Ask them to delete it.

3. Contact their DPO.dpo@withpersona.com— that’s their Data Protection Officer. If you want to object to them using your documents as AI training data under “legitimate interests,” this is where you do it.

4. Think twice before verifying.That blue badge might not be worth what you’re trading for it. A checkmark is cosmetic. Biometric data is forever.

## Three Minutes

The whole thing took three minutes. Scan, selfie, done.

Understanding what I actually agreed to took me an entire weekend reading 34 pages of legal documents.

I handed a US company my passport, my face, and the mathematical geometry of my skull. They cross-referenced me against credit agencies and government databases. They’ll use my documents to train their AI. And if the US government comes knocking, they’ll hand it all over — even if it’s stored in Europe, even if I’m European, and possibly without ever telling me.

All for a small blue checkmark on a professional networking site.

I’m not telling you to skip verification. But I am telling you to know what you’re trading. Because Persona does. LinkedIn does. The only person in the dark is the one holding their passport up to the camera.

Sources:

* Persona IDV Privacy Policy(Last Updated: May 8, 2025)
* Persona IDV Terms of Service(Last Updated: September 12, 2023)
* Persona Subprocessors(Last Updated: September 8, 2025)

privacy

linkedin

biometrics

gdpr

cloud-act

identity

← Previous

I Asked an AI Chatbot for My Data. I Didn't Expect a Psychological Profile.
