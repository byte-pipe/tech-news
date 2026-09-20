---
title: ChatGPT now knows what you do on other websites via ad collector
url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
site_name: hackernews_api
content_file: hackernews_api-chatgpt-now-knows-what-you-do-on-other-websites-vi
fetched_at: '2026-09-20T21:11:11.578238'
original_url: https://www.buchodi.com/chatgpt-now-knows-what-you-do-on-other-websites-via-ad-collector/
author: lmbbuchodi
date: '2026-09-20'
published_date: '2026-09-20T15:17:49.000Z'
description: ChatGPT now knows what you do on other websites via ad collector
tags:
- hackernews
- trending
---

OpenAI's ad collector atbzr.openai.comsets a cookie called__obi, scoped to.openai.com. The value is while you are on ChatGPT and tied to your ChatGPT account.__obiis then sent to OpenAI from ordinary websites you visit.

Any company that buys ads on ChatGPT installs asmall piece of OpenAI codeon its own site, the same way retailers already install Meta and Google tracking code. Loading that code, sends__obito OpenAI along with data about the page you are browsing. This includes products you are searching for, articles you are reading, and purchase behaviors.

The bottom line is that OpenAI can connect what you do on those sites to your ChatGPT account.

I reproduced the full mechanism on my own phone, verified with two independent capture methods, and cross-checked against several months of observed traffic covering 936 distinct advertiser pixels across 1,029 hostnames.

## How it works

Step 1. ChatGPT creates an identifier and signs it.

Onchatgpt.com, the client generates 16 random bytes and callsPOST /backend-api/bazaar/obi/sync-token(or/backend-anon/when signed out). The backend returns an RS256 JWT:

{
 "iss": "chatgpt-wadi",
 "aud": "bzr.openai.com",
 "purpose": "obi_sync",
 "operation": "set",
 "consent_decision": "analytics_allowed",
 "consent_policy_version": "user_granular_consent_v1",
 "sub": "«redacted: 64-hex account subject»",
 "subject_type": "account_user",
 "obi": "«redacted: 22-char identifier»",
 "exp": "«iat + 60s»"
}

subis the account.obiis the identifier. The token binds them, is scoped to the collector, and expires in 60 seconds.bzrstands forbazaar, OpenAI's internal name for the ads platform;wadiis the issuing service.

Step 2. The identifier becomes a cookie on OpenAI's domain.

The client POSTs{"token": "«JWT»"}cross-site tobzr.openai.com/v1/obi/sync. The response:

Set-Cookie: __obi=«redacted»; Domain=.openai.com; HttpOnly;
 Max-Age=31536000; Path=/; SameSite=none; Secure

SameSite=nonewithSecureis the configuration a cookie needs to be sent on cross-site requests.Max-Ageis one year. Theobivalue in the JWT and the value in the cookie are identical.

Step 3. Advertiser sites send it back.

Three request classes go from an advertiser's page to OpenAI's hosts. On a phone with__obiin the jar, all three carried it:

Request

Carried 
__obi

Notes

GET bzrcdn.openai.com/sdk/oaiq.min.js

yes

the script load itself

POST bzr.openai.com/v1/sdk/events
 with 
obref

yes

conversion events

POST bzr.openai.com/v1/sdk/events
, bare body

yes

the SDK's "no credentials" path

GET bzrcdn.openai.com/pixel-config/…

no cookie header at all

control

The first row is particularly interesting. The pixel SDK has a code path that omits credentials, and it does not help: the browser attaches cookies to the<script src>request that loads the SDK before any of OpenAI's code runs. By the virtue of loading the tag the identifier is disclosed.

## What travels with it

The same SDK also collects identity from the advertiser's page. The payload separates four sources, labelled by OpenAI itself:infor values the advertiser passes deliberately, andfm,ht,jsfor values the SDK scrapes from form fields, rendered page text, and the tag-manager bus. In observed traffic, scraped identity outnumbered advertiser-supplied identity 685 events to 255.

The tag-manager bus is the largest source of email. The SDK replaceswindow.dataLayer.pushwith its own function, also readsadobeDataLayer, and locates renamed GTM layers by parsing thel=parameter off thegtm.jsscript tag. Current versions take email and phone from it. Version 0.1.31 also took names and geography before the scope was narrowed on 27 August.

Email, phone, first and last name are SHA-256 hashed before transmission. Country, region, city and postal code are sent in the clear. Postal code was the most-harvested form field, 100 events across 28 sites.

URLs are reduced to origin plus path before sending; none of 23,929 observed carried a query string. Paths survive, and paths reaching the collector included a medical condition, a debt-solutions funnel and a litigation intake form.

Automatic matching was enabled for 638 of 881 pixels with a known setting, including every credit and lending advertiser observed. It is controlled from OpenAI's Ads Manager. A denylist excludes passwords, one-time codes, card numbers, SSN, date of birth, medical history, diagnosis and court fields.

## The cookie is built to cross sites

On the same advertiser-page requests, every other OpenAI cookie was blocked by the browser:

Cookie

Outcome

oai-did
, 
oaicom-stable-id

blocked, 
SameSite=Lax

oai-client-auth-info
, session cookies

blocked, domain mismatch

__obi

sent

__obiis the only OpenAI identifier configured withSameSite=None.

## Observed reach

On my device, one__obivalue was sent to OpenAI from 12 commercial websites under 13 distinct pixel IDs, including Chewy, Wayfair, ThriftBooks, Eventbrite, HelloFresh, Coursera and SeatGeek. Every request was accepted with202.

In the broader traffic, 12 of 30 distinct__obivalues appeared under more than one advertiser, one under ten.

## It works when you are logged out

Across 932 decoded sync tokens, 736 carriedsubject_type: account_userand 196 carriedanonymous. The anonymous subject is as stable as the account subject: one per device, persisting at least 27 days.

## What OpenAI's cookie policy says

OpenAI'scookie policylists__obiunder Analytics cookies, one year, onchatgpt.comandopenai.com. It is the only entry in that section. The policy describes analytics cookies as helping OpenAI understand how its services perform and are used.

OpenAI runs analytics and marketing as two separate consent choices,oai_consent_analyticsandoai_consent_marketing, and every sync token I decoded carriedconsent_decision: analytics_allowed. Someone who allows analytics and refuses marketing gets this.

## OpenAI's response

I sent the mechanism and two questions topress@openai.comandprivacy@openai.comon 14 September: why__obiis classified as an analytics cookie, and whether a user who grants analytics consent and refuses marketing consent still receives it. The reply came from OpenAI Support. It acknowledged the inquiry, said the observations would be shared internally for review, and did not answer either question. The script-load observation above was made after the inquiry was sent. I will update this post if OpenAI responds.

## Limits

Browsers.Observed on Chrome for Android.Safari's Intelligent Tracking Preventionblocks all third-party cookies, and Chrome on iOS runs on WebKit, so the mechanism does not operate on any iOS browser. Desktop Chrome is untested.

Gating.Roughly one ChatGPT session in five produced a sync token. ChatGPT's mobile web client serves ads without syncing at all. Someone following the steps below may see the pixel fire with no cookie attached.

The join is not observed.202means the collector accepted the event with the cookie attached. That OpenAI resolves it to the account server-side follows from the design; I did not watch it happen.

Meta built the structural equivalent years ago.A logged-in account, third-party cookies on pixel fires, off-site conversions resolved to a profile. The mechanism is standard adtech. What has no precedent is running it on an AI chat product. People tell these products things they would not put on a social network, and these products increasingly act on their behalf.

The pixel's other cookie does not do this.__obrefis set on the advertiser's own domain. Each site gets a different value and no site can see another's. Of 2,860 values observed, 2,828 appeared under exactly one advertiser.

Advertisers cannot see this.__obibelongs to a domain their scripts cannot read. They installed a conversion pixel and have no way to know their visitors are being resolved to a ChatGPT identity.