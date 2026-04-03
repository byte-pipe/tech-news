---
title: 'Introducing pay per crawl: enabling content owners to charge AI crawlers for access'
url: https://blog.cloudflare.com/introducing-pay-per-crawl/
site_name: hackernews
fetched_at: '2025-07-02T01:05:38.624616'
original_url: https://blog.cloudflare.com/introducing-pay-per-crawl/
author: scotchmi_st
date: '2025-07-02'
published_date: 2025-07-01T11:00+01:00
description: Pay per crawl is a new feature to allow content creators to charge AI crawlers for access to their content.
---

# Introducing pay per crawl: enabling content owners to charge AI crawlers for access

2025-07-01

* Will Allen
* Simon Newton
5 min read

## A changing landscape of consumption

Many publishers, content creators and website owners currently feel like they have a binary choice — either leave the front door wide open for AI to consume everything they create, or create their own walled garden. But what if there was another way?

At Cloudflare, we started from a simple principle: we wanted content creators to have control over who accesses their work. If a creator wants to block all AI crawlers from their content, they should be able to do so. If a creator wants to allow some or all AI crawlers full access to their content for free, they should be able to do that, too. Creators should be in the driver’s seat.

After hundreds of conversations with news organizations, publishers, and large-scale social media platforms, we heard a consistent desire for a third path: They’d like to allow AI crawlers to access their content, but they’d like to get compensated. Currently, that requires knowing the right individual and striking a one-off deal, which is an insurmountable challenge if you don’t have scale and leverage.

## What if I could charge a crawler?

We believe your choice need not be binary — there should be a third, more nuanced option:You can charge for access.Instead of a blanket block or uncompensated open access, we want to empower content owners to monetize their content at Internet scale.

We’re excited to help dust off a mostly forgotten piece of the web:HTTP response code 402.

## Introducing pay per crawl

Pay per crawl, in private beta, is our first experiment in this area.

Pay per crawl integrates with existing web infrastructure, leveraging HTTP status codes and established authentication mechanisms to create a framework for paid content access.

Each time an AI crawler requests content, they either present payment intent via request headers for successful access (HTTP response code 200), or receive a402 Payment Requiredresponse with pricing. Cloudflare acts as the Merchant of Record for pay per crawl and also provides the underlying technical infrastructure.

### Publisher controls and pricing

Pay per crawl grants domain owners full control over their monetization strategy. They can define a flat, per-request price across their entire site. Publishers will then have three distinct options for a crawler:

* Allow:Grant the crawler free access to content.
* Charge:Require payment at the configured, domain-wide price.
* Block:Deny access entirely, with no option to pay.

An important mechanism here is that even if a crawler doesn’t have a billing relationship with Cloudflare, and thus couldn’t be charged for access, a publisher can still choose to ‘charge’ them. This is the functional equivalent of a network level block (an HTTP403 Forbiddenresponse where no content is returned) — but with the added benefit of telling the crawler there could be a relationship in the future.

While publishers currently can define a flat price across their entire site, they retain the flexibility to bypass charges for specific crawlers as needed. This is particularly helpful if you want to allow a certain crawler through for free, or if you want to negotiate and execute a content partnership outside the pay per crawl feature.

To ensure integration with each publisher’s existing security posture, Cloudflare enforces Allow or Charge decisions via a rules engine that operates only after existing WAF policies and bot management or bot blocking features have been applied.

### Payment headers and access

As we were building the system, we knew we had to solve an incredibly important technical challenge: ensuring we could charge a specific crawler, but prevent anyone from spoofing that crawler. Thankfully, there’s a way to do this usingWeb Bot Authproposals.

For crawlers,this involves:

* Generating an Ed25519 key pair, and making theJWK-formatted public key available in a hosted directory
* Registering with Cloudflare to provide the URL of your key directory and user agent information.
* Configuring your crawler to useHTTP Message Signatureswith each request.

Once registration is accepted, crawler requests should always includesignature-agent,signature-input, andsignatureheaders to identify your crawler and discover paid resources.

GET /example.html
Signature-Agent: "https://signature-agent.example.com"
Signature-Input: sig2=("@authority" "signature-agent")
 ;created=1735689600
 ;keyid="poqkLGiymh_W0uP6PZFw-dvez3QJT5SolqXBCW38r0U"
 ;alg="ed25519"
 ;expires=1735693200
;nonce="e8N7S2MFd/qrd6T2R3tdfAuuANngKI7LFtKYI/vowzk4lAZYadIX6wW25MwG7DCT9RUKAJ0qVkU0mEeLElW1qg=="
 ;tag="web-bot-auth"
Signature: sig2=:jdq0SqOwHdyHr9+r5jw3iYZH6aNGKijYp/EstF4RQTQdi5N5YYKrD+mCT1HA1nZDsi6nJKuHxUi/5Syp3rLWBA==:

### Accessing paid content

Once a crawler is set up, determination of whether content requires payment can happen via two flows:

#### Reactive (discovery-first)

Should a crawler request a paid URL, Cloudflare returns anHTTP 402 Payment Requiredresponse, accompanied by acrawler-priceheader. This signals that payment is required for the requested resource.

HTTP 402 Payment Required
crawler-price: USD XX.XX

The crawler can then decide to retry the request, this time including acrawler-exact-priceheader to indicate agreement to pay the configured price.

GET /example.html
crawler-exact-price: USD XX.XX

#### Proactive (intent-first)

Alternatively, a crawler can preemptively include acrawler-max-priceheader in its initial request.

GET /example.html
crawler-max-price: USD XX.XX

If the price configured for a resource is equal to or below this specified limit, the request proceeds, and the content is served with a successfulHTTP 200 OKresponse, confirming the charge:

HTTP 200 OK
crawler-charged: USD XX.XX
server: cloudflare

If the amount in acrawler-max-pricerequest is greater than the content owner’s configured price, only the configured price is charged. However, if the resource’s configured price exceeds the maximum price offered by the crawler, anHTTP402 Payment Requiredresponse is returned, indicating the specified cost.  Only a single price declaration header,crawler-exact-priceorcrawler-max-price, may be used per request.

Thecrawler-exact-priceorcrawler-max-priceheaders explicitly declare the crawler's willingness to pay. If all checks pass, the content is served, and the crawl event is logged. If any aspect of the request is invalid, the edge returns anHTTP 402 Payment Requiredresponse.

### Financial settlement

Crawler operators and content owners must configure pay per crawl payment details in their Cloudflare account. Billing events are recorded each time a crawler makes an authenticated request with payment intent and receives an HTTP 200-level response with acrawler-chargedheader. Cloudflare then aggregates all the events, charges the crawler, and distributes the earnings to the publisher.

## Content for crawlers today, agents tomorrow

At its core, pay per crawl begins a technical shift in how content is controlled online. By providing creators with a robust, programmatic mechanism for valuing and controlling their digital assets, we empower them to continue creating the rich, diverse content that makes the Internet invaluable.

We expect pay per crawl to evolve significantly. It’s very early: we believe many different types of interactions and marketplaces can and should develop simultaneously. We are excited to support these various efforts and open standards.

For example, a publisher or new organization might want to charge different rates for different paths or content types. How do you introduce dynamic pricing based not only upon demand, but also how many users your AI application has? How do you introduce granular licenses at internet scale, whether for training, inference, search, or something entirely new?

The true potential of pay per crawl may emerge in an agentic world. What if an agentic paywall could operate entirely programmatically? Imagine asking your favorite deep research program to help you synthesize the latest cancer research or a legal brief, or just help you find the best restaurant in Soho — and then giving that agent a budget to spend to acquire the best and most relevant content. By anchoring our first solution onHTTP response code 402, we enable a future where intelligent agents can programmatically negotiate access to digital resources.

## Getting started

Pay per crawl is currently in private beta. We’d love to hear from you if you’re either a crawler interested in paying to access content or a content creator interested in charging for access. You can reach out to us athttp://www.cloudflare.com/paypercrawl-signup/or contact your Account Executive if you’re an existing Enterprise customer.

Cloudflare's connectivity cloud protects
entire corporate networks
, helps customers build
Internet-scale applications efficiently
, accelerates any
website or Internet application
,
wards off DDoS attacks
, keeps
hackers at bay
, and can help you on
your journey to Zero Trust
.
Visit
1.1.1.1
 from any device to get started with our free app that makes your Internet faster and safer.
To learn more about our mission to help build a better Internet,
start here
. If you're looking for a new career direction, check out
our open positions
.
Discuss on Hacker News
AI Bots
Bots
AI
Bot Management
