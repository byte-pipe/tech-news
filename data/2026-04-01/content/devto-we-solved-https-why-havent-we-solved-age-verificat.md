---
title: We Solved HTTPS. Why Haven’t We Solved Age Verification? - DEV Community
url: https://dev.to/kevinbridges/we-solved-https-why-havent-we-solved-age-verification-2g9o
site_name: devto
content_file: devto-we-solved-https-why-havent-we-solved-age-verificat
fetched_at: '2026-04-01T19:28:08.021355'
original_url: https://dev.to/kevinbridges/we-solved-https-why-havent-we-solved-age-verification-2g9o
author: Kevin Bridges
date: '2026-03-26'
description: We Solved HTTPS. Why Haven’t We Solved Age Verification? There’s something fundamentally... Tagged with webdev, dis, architecture, security.
tags: '#webdev, #dis, #architecture, #security'
---

Comments challenge the HTTPS analogy.

# We Solved HTTPS. Why Haven’t We Solved Age Verification?

There’s something fundamentally broken about how the internet handles age verification.

Right now, most websites rely on a system that looks like this:

“Are you 18?” →Click yes→ full access

That’s not a safeguard. It’s a checkbox with zero enforcement.

At the same time, social media companies and online platforms are increasingly being held responsible for protecting minors from harmful content, addictive design, and inappropriate interactions. The expectation is rising—but the infrastructure to support it hasn’t kept up.

We’re asking platforms to solve a hard, global identity problem… individually.

That’s the real issue.

## The Wrong Problem

Most debates around age verification focus on edge cases:

* What if a kid lies?
* What if they use a parent’s account?
* What about privacy?
* What about global access?

These are valid concerns—but they miss the bigger picture.

The goal should not be:

“Make it impossible for minors to access restricted content”

That’s unrealistic.

Instead, the goal should be:

“Replace fake safeguards with real, reasonable friction—and give platforms a standard way to enforce it.”

We already accept this model in the physical world:

* ID checks for alcohol
* Age restrictions for movies
* Gambling regulations

None are perfect. All are still worth doing.

## The Real Problem: No Shared Infrastructure

Think about how the internet solved other hard problems:

* Payments→ Stripe, PayPal, Visa
* Authentication→ Google, Apple, OAuth
* Security→ TLS certificates (DigiCert, GoDaddy)

We don’t expect every website to:

* Build its own payment processor
* Create its own encryption standard
* Design its own login system

We createdshared infrastructure layersinstead.

But for age verification?

Every platform is improvising.

## A Better Model: Age Tokens as Infrastructure

What if age verification worked more like HTTPS?

Instead of every website collecting IDs or guessing ages, we introduce:

Age Tokens— simple, verifiable credentials that prove a user meets an age requirement (e.g., “18+”) without revealing identity.

### How it would work:

1. A user verifies their age with a trusted provider

* PayPal, Google, a bank, telecom, or government system

1. The provider issues a signed credential

* “This user is over 18”

1. A website requests proof when needed

* e.g., accessing adult content or certain features

1. The user shares a token

* The site verifies the signature—not the identity

## The PKI Analogy (Why This Scales)

This model mirrors how HTTPS works today:

HTTPS

Age Verification

Certificate Authorities (DigiCert, GoDaddy)

Age Providers (PayPal, Google, governments)

SSL Certificates

Age Tokens

Browsers trust a list of CAs

Platforms trust a list of providers

A website doesn’t need to knowwho you are—only that:

A trusted authority vouches for a specific property.

In this case:

“This user is over 18.”

## Why This Approach Works

### 1. No Reinventing the Wheel

Platforms don’t need to build their own verification systems. They integrate once.

### 2. Better Privacy (at the Platform Level)

Websites don’t collect:

* IDs
* birthdates
* biometric data

They only receive a yes/no assertion.

### 3. Global Flexibility

Different regions can use different methods:

* U.S. → private providers (Google, PayPal)
* EU → privacy-focused digital identity wallets
* China → state-backed systems
* Developing regions → telecom-based verification

The platform doesn’t care how verification happens—only that the token is valid.

### 4. Clearer Accountability

Responsibility becomes shared and defined:

* Providers→ verify age correctly
* Platforms→ enforce access using tokens

### 5. Realistic Enforcement

This doesn’t eliminate bypassing—and it doesn’t need to.

It:

* Removes trivial access (“just click yes”)
* Adds friction
* Creates enforceable standards

## The Core Critique (And It’s Valid)

A common and important pushback is:

“You’re still asking users to trust a provider—Google, a bank, a telecom, or a government.”

That’s true.

Even in this model:

* Theplatform doesn’t know who you are
* But theprovider does

Which raises the real issue:

Have we actually solved the privacy problem—or just moved it?

## Why Technology Alone Isn’t Enough

Even with strong cryptography (signed tokens, zero-knowledge proofs), one issue remains:

The entity issuing the age credential still sees—and verifies—your identity.

That means they could:

* Store more data than necessary
* Correlate activity across services
* Monetize or misuse that data

So while theplatform risk is reduced, theprovider risk remains.

This is where a second layer is needed.

## A Proposed Layer: Age Assurance Compliance Framework (AACF)

To address this, we can introduce:

Age Assurance Compliance Framework (AACF)

AACF would function similarly to PCI—but tailored for identity and age verification.

Instead of asking:

“Can you securely process credit card data?”

AACF asks:

“Can you verify age while minimizing, protecting, and restricting the use of identity data?”

## What AACF Would Enforce

### 1. Data Minimization

* Only collect what is required to verify age
* Prefer derived attributes (e.g., “18+”) over storing birthdates
* Prohibit unnecessary retention of raw identity data

### 2. Purpose Limitation

* Data can only be used for:age verificationfraud prevention
* age verification
* fraud prevention
* Explicitly prohibited:advertising useresalebehavioral profiling
* advertising use
* resale
* behavioral profiling

### 3. Token Design Requirements

* Short-lived or one-time-use tokens
* No persistent cross-site identifiers
* Encouragement of privacy-preserving techniques

### 4. Audit & Certification

* Independent third-party audits conducted regularly
* Verification of data minimization practices
* Review of storage, retention, and deletion policies
* Inspection of technical controls (token handling, anti-tracking safeguards)
* Evaluation of internal access controls and monitoring systems
* Financial and operational audits to ensure compliance with data usage restrictions, including review of records to detect any sale or unauthorized sharing of user data with third parties (similar in rigor to an IRS-style audit)

Certification would be required to act as atrusted provider, with:

* Required remediation for violations
* Suspension for significant issues
* Revocation for severe or repeated non-compliance

### 5. Assurance Levels

Not all providers are equal. AACF could define tiers:

* Level 1:Self-asserted / low confidence
* Level 2:Behavioral / heuristic-based
* Level 3:Verified (KYC, ID-backed)

Platforms could require different levels depending on risk.

## How AACF Compares to PCI and HIPAA

Framework

Scope

Goal

Key Limitation

PCI DSS

Payment card data

Prevent fraud and breaches

Does not regulate broader data use

HIPAA

Health information

Protect sensitive medical data

Applies only to healthcare

AACF (proposed)

Age/identity attributes

Minimize and constrain identity usage

Requires trust and enforcement

### Key Differences

PCI DSS

* Focus:security
* Question: “Can you protect this data?”

HIPAA

* Focus:privacy + regulation
* Question: “Are you allowed to use this data this way?”

AACF

* Focus:minimal disclosure + controlled trust
* Question:

“Can you verify age without becoming a data exploitation point?”

## What This Solves (and What It Doesn’t)

### What it improves:

* Reduces data sprawl across platforms
* Limits misuse by verification providers
* Creates enforceable standards
* Builds trust through audits

### What it does NOT solve:

* Eliminates trust entirely ❌
* Prevents all misuse ❌
* Resolves global political differences ❌

## The Bigger Picture

If we combine everything:

* Age Tokens→ how verification works
* Trust Framework (PKI-style)→ who is trusted
* AACF (compliance layer)→ how they must behave

We move from:

fragmented, inconsistent, and opaque systems

to:

a structured, auditable, and interoperable model

## Final Thought

The internet didn’t become secure because we told websites to “be careful.”

It became secure because we built:

* protocols (TLS)
* trust systems (certificate authorities)
* enforcement mechanisms

Age verification will likely follow the same path.

Not perfect.

But significantly better than a checkbox that says:

“Yes, I’m 18.”

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
