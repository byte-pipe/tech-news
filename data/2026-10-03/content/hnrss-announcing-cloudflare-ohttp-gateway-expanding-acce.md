---
title: Announcing Cloudflare OHTTP Gateway – expanding access to Cloudflare’s privacy-preserving infrastructure | Cloudflare Blog
url: https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/
site_name: hnrss
content_file: hnrss-announcing-cloudflare-ohttp-gateway-expanding-acce
fetched_at: '2026-10-03T22:00:44.634641'
original_url: https://blog.cloudflare.com/announcing-cloudflare-ohttp-gateway/
date: '2026-10-03'
published_date: '2026-10-02T13:00:00.000Z'
description: We’re announcing the closed beta of a self-serve Cloudflare OHTTP Gateway. We’re also renaming our Privacy Gateway to Cloudflare OHTTP Relay to better distinguish the two products.
tags:
- hackernews
- hnrss
---

Today, end users carry too much of the burden of online privacy. To avoid third-party trackers or targeted ads, users are instructed to use a VPN, disable cookies, or install adblockers. Meanwhile, some app developers end up knowing more about their users than they’d care to: a typical client-server exchange creates a trail of user data, like the client’s IP address or TLS fingerprint. This level of visibility can be a burden.

That’s why Cloudflare builds infrastructure that helps developers bake privacy into their apps. Oblivious HTTP (OHTTP) is anIETF standarddesigned to enable app backends to receive HTTP requests without seeing user IP addresses.

This fall, we’re launching the Cloudflare OHTTP Gateway. Customers will be able to enable our new OHTTP Gateway as a paid add-on to their zone and start receiving OHTTP traffic with just a few clicks. Register throughour formto join our waitlist. Read on to learn more.

## Expanding our OHTTP product suite

With OHTTP, requests travel through two independently-operated hops: a relay and a gateway. An OHTTP relay blindly forwards encrypted requests in order to hide client identifiers from app servers. An OHTTP gateway performs the cryptographic work of decapsulating encrypted requests and encapsulating responses such that app servers can handle OHTTP requests as if they were plain HTTP. The separation of trust between relay and gateway is critical: it ensures that no single party sees both client identifiers and request contents.

In 2022, we launched an OHTTP relay product,Privacy Gateway. Privacy Gateway enables our customers to offer more privacy-preserving experiences to their users. For example, Flo Health uses OHTTP for their app’sAnonymous Mode, and Apple’sPrivate Cloud Computeuses OHTTP to disassociate AI inference requests from user identities. But customers who are already protecting their servers behind Cloudflare can’t also use a Cloudflare-operated relay — they need an OHTTP gateway instead.

With the existing Cloudflare OHTTP Relay, customers must bring their own Gateway to preserve a separation of trust.

In our experience running OHTTP relays, we’ve seen how difficult it can be to build and operate a secure, performant OHTTP gateway at scale. Today, we’re launching the closed beta for our self-serve Cloudflare OHTTP Gateway. We’re also renaming our “Privacy Gateway” to “Cloudflare OHTTP Relay” to better distinguish the two products.

Now, customers who want an OHTTP architecture with the necessary separation of trust have two options:

1. Use Cloudflare’s OHTTP Relay (formerly Cloudflare Privacy Gateway) and run your gateway yourself. This is best if your application servers are hosted off Cloudflare, and you’re able to run your own OHTTP gateway.
2. Use Cloudflare’s new OHTTP Gateway with a third-party relay. This is best if your app servers are already behind Cloudflare (on our CDN or Workers, for example), if you’re accepting OHTTP requests from a third party (like Apple’sLiveCallerID), or if you want a managed gateway to minimize latency and operational overhead.

We’re working to raise the bar for privacy across the Internet, and we believe that protocols like OHTTP can help — if we make them easy enough to adopt. It’s always been our goal to expand our OHTTP product suite and make our trusted privacy infrastructure accessible to a broader swath of the Internet.

## Why we built the Cloudflare OHTTP Gateway

Since we launched our OHTTP Relay product, we’ve observed a few things.

First, we’ve seen that there's a growing appetite among developers for accessible, usable privacy infrastructure. Developers of privacy-oriented apps want to bake network privacy into their applications by default, but doing so remains harder than it should be.

Second, we’ve learned that building and operating an OHTTP gateway can be tough for customers. Any proxying architecture introduces some latency because requests must travel an extra hop or two around the Internet. Combine that with the cost to decrypt requests and encrypt responses, and the latency hit of a homegrown OHTTP setup can be significant. We’re well-positioned to solve this problem: the same building blocks that enable us to operate fast, reliable privacy infrastructure for products like1.1.1.1andiCloud Private Relaymake us a good home for an OHTTP gateway. Because of Cloudflare’sanycastapproach, our OHTTP Gateway will run on every server on Cloudflare’s global edge network, minimizing latency in relay-to-gateway hops. If you use our CDN, user requests can be decrypted by our Gateway and resolved by your app servers on the same Cloudflare metals, saving gateway-to-origin latency.

Finally, recall that OHTTP’sprivacy modelrequires that the relay and app server be operated by separate, non-colluding parties. We want to provide our customers with the best possible range of options for their privacy infrastructure. Before, developers who protected their app servers behind Cloudflare weren’t able to use our OHTTP Relay, because Cloudflare would see both client metadata and the decrypted contents of requests, breaking OHTTP’s privacy model. Now, developers can choose whether a Cloudflare OHTTP Relay or Gateway is a better fit for their architecture.

## A primer on OHTTP

A typical interaction between a client and application server reveals information about the client. When a client and app server talk to one another, the app server learns the client’s IP address because each packet in which data is sent is labeled with a source IP — similar to the “from” label on an envelope. App servers can also “fingerprint” a client based on attributes like supported TLS versions or cipher suites. These signals make it possible for app servers to link multiple requests back to the same user.

But what if I wanted to build an app that really doesn’t know much about my users? For example: Flo Health wanted to build anAnonymous Modeto enable users to access personal health data without it being linkable to possible user identifiers.

OHTTP introduces a proxy, called a “relay,” that forwards requests and responses between client and app server to obfuscate the client’s identity from the app server. The relay sees client identifiers like IP address and TLS fingerprint, but strips them before forwarding on requests. This prevents app servers from linking multiple requests back to the same user, and means that request contents can’t be associated with the user’s IP address.

For example, a regular client-server exchange might reveal the following information about a client:

- ipAddress: 192.0.2.33 # the client’s IP address 

- ASN: 7922

- tlsCipher: AEAD-CHACHA20-POLY1305-SHA256 # potentially unique

- tlsVersion: TLSv1.3

- Country: US

- Region: California # the client's location

- City: Campbell

A request first sent through an OHTTP relay would reveal only the relay’s information to the app server receiving the request:

- ipAddress: 128.62.37.13 # the relay's IP address & fingerprint 

- ASN: 18 

- tlsCipher: AEAD-AES-128-GCM-SHA256 

- tlsVersion: TLSv1.3 

- Country: US

- Region: Texas # the relay's location

- City: Austin

This means that for each request, the app server doesn’t learn the location and TLS fingerprint of the end user. Plus, if many different users are sending requests through the relay, the app server won’t be able to distinguish which requests are coming from whom, limiting their ability to trace app activity back to a single end user. This creates a strong privacy boundary.

What really differentiates OHTTP from a basic forwarding proxy, however, is the encryption of data between client and app server. Requests and responses are encapsulated using Hybrid Public Key Encryption (HPKE) such that only the client and app server can see plaintext, and the relay sees only a jumble of ciphertext. A “gateway” sits between the relay and app server to handle all of this cryptography — decapsulating requests, encapsulating responses — and the app server handles only plain HTTP.

This creates a “double-blind” privacy model: the relay sees only client identifiers; the gateway and app server see only request contents; no party sees both.

A diagram showing how requests flow from end users through the OHTTP Gateway to app servers. A response from app servers follows the same path in reverse to the end user. Note that with the Gateway, you can choose whether or not to put your servers behind Cloudflare.

## How we built the OHTTP Gateway

In building our OHTTP gateway-as-a-service, our goal is to bring our secure, performant privacy infrastructure to a broader swath of the Internet. Performance and easy onboarding are critical. So, we built our Gateway as a flexible service deployed across our global network. With just a couple of clicks, you can enable the Gateway on your zone and start sending OHTTP tohttps://your-zone.com/.well-known/ohttp-gateway. We’ll scale the service up and down automatically, so you don’t need to worry about capacity.

We had a few other user needs in mind, informed by the pain points we’d seen OHTTP Relay customers run into when operating their own OHTTP gateways.

First: We wanted to abstract away as much of the complexity of OHTTP as possible for your app servers. We wanted developers to be able to start receiving OHTTP while continuing to accept regular HTTP traffic if they chose. So, we designed the Gateway as a feature of your zone, where clients sendwell-formattedOHTTP requests to a/.well-known/ohttp-gatewayendpoint on your zone. We support both standard andchunked OHTTP— and we recommend using chunked OHTTP for better performance, because it enables us to process requests incrementally (in “chunks”).

Our Gateway service will intercept each request, decrypt it, issue a subrequest to your app server, and return an encrypted response to the client. All non-OHTTP requests will travel to your server without invoking the Gateway.

Binding your Gateway to your zone also enables us to protect your Gateway from abuse. A client sending requests to your zone `example.com` may send to `foo.example.com` or `bar.example.com`, but notwikipedia.com. Without you needing to worry about it, this prevents unauthorized clients from using your zone as a way to target other domains.

Second: Seamless key management is critical. Gateways need to maintain a public HPKE key configuration to enable clients to encrypt requests, but managing keys securely is a challenge. So, we designed the Gateway to fully manage all keys for customers, and to serve public keys as responses to GET requests to/.well-known/ohttp-gateway. For stronger privacy, clients can download keys over a different IP than they request the gateway.

Third: Gateways need to be able to authenticate relays. Because the Gateway (by design) knows very little about the client sending a given request, it places trust in the relay to authenticate clients and forward traffic responsibly. But how do you ensure that only trusted relays can send traffic to your gateway?

We designed the Gateway such thatCloudflare Access, Cloudflare’s zero trust network access product, runsbeforerequests are decrypted, enabling you to use any standard Accesspoliciesto authenticate incoming traffic and protect your Gateway from abuse. Options include mutual TLS, static service credentials, and custom external logic.

Finally: Mistakes happen, and we anticipated that customers might accidentally break OHTTP’s privacy model by running both their relay and gateway on Cloudflare. So, to preserve OHTTP’s separation of trust and ensure that Cloudflare never seesbothclient identities and decrypted inner requests, our Gateway will refuseto decrypt requests sent from Cloudflare Workers or from proxied hosts on Cloudflare.

## When is the OHTTP Gateway a better fit than the OHTTP Relay?

If you want to use Cloudflare’s OHTTP product suite, but you’re wondering why you’d pick Cloudflare’s OHTTP Gateway instead of the OHTTP Relay, here are a couple of considerations.

First, do you want your app servers on Cloudflare – behind our CDN or built on Workers, for example? If so, the OHTTP Gateway is a better fit to ensure adherence to OHTTP’s privacy model.

Second, what’s your use case? If you want to receive OHTTP requests from a third-party client and relay — to use Apple’sLiveCallerIDSDK, for example — then the OHTTP Gateway is likely the better solution for you.

## Getting started

If you have a feature request or would like to register for our waitlist, so we can notify you when the product launches,sign up here.

Then, you’ll need to implement an OHTTP client. Seeohttp.infoor oursample client libraryfor some examples to help you get started. One flag as you build the client: OHTTP provides privacy at the network level, and doesn’t touch the inner request body. So, to preserve user privacy, it’s up to you not to send identifying information (e.g. a user’s email address or username) in the request body.

Next, you’ll need to bring your own relay. Relays can run on any infrastructure provider, and they’re simple: here’s somesample code. The challenge and the reason you might want a dedicated OHTTP relay provider, is to verifiably promise to your users that you won’t inspect logs with client identifiers. Otherwise, you’d be able to correlate clients at the relay with decrypted requests at your app servers.

Finally, once your OHTTP deployment is live, check out ourpvcli clientto help with testing and debugging.We’re excited to bring accessible privacy infrastructure to developers everywhere.Reach out to usif you’d like to try out the new OHTTP Gateway and raise the bar for privacy online.

## Related tags

Birthday Week
Privacy
Protocols
Standards

Follow on Social Media

* Cloudflare
* Lara Schull

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.