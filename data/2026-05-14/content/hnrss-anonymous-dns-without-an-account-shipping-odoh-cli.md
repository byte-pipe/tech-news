---
title: 'Anonymous DNS without an account: shipping ODoH client + relay in one Rust binary — Numa'
url: https://numa.rs/blog/posts/odoh-anonymous-dns-without-an-account.html
site_name: hnrss
content_file: hnrss-anonymous-dns-without-an-account-shipping-odoh-cli
fetched_at: '2026-05-14T19:35:13.932630'
original_url: https://numa.rs/blog/posts/odoh-anonymous-dns-without-an-account.html
date: '2026-05-14'
description: Every existing anonymous-DNS option (Apple Private Relay, NextDNS, Cloudflare Families) requires signing up. ODoH (RFC 9230) is the protocol that splits ‘who you are’ from ‘what you asked’ across two independent operators. Numa v0.14 ships the client, the relay, and a public deployment in one MIT-licensed binary. Here’s what the protocol actually does, what it doesn’t fix, and what it took to deploy the second public relay in the ecosystem.
tags:
- hackernews
- hnrss
---

If you run Pi-hole, AdGuard Home, or any forwarding resolver, every
one of your queries goes through one operator who sees both your IP
address and the question. If you switch to a recursive resolver like
Unbound, your IP gets exposed to every authoritative nameserver instead
-.comlearns you exist,google.comlearns you
exist, and so does every CDN edge in the chain. DoH and DoT encrypt thetransport; they don’t changewho learns what.

Apple’s iCloud Private Relay solved this for Apple users by splitting
the path: an ingress proxy sees your IP but not the request, an egress
proxy sees the request but not your IP. DNS gets anonymized system-wide,
but only with iCloud+ ($0.99/mo), only on iOS/macOS, and only through
Apple-curated egress partners. NextDNS, Cloudflare for Families, Quad9 -
all the privacy-focused DNS services - require accounts, telemetry, or
both. The self-hosted audience effectively had no anonymous-DNS option
without an account or a platform lock-in.

Hops that see {your IP, your question}

{1, 1} → {disjoint}

relay sees IP, target sees question

Crypto primitives

all audited

odoh-rs (HPKE) · rustls (TLS) — zero custom

Account required

none

single binary, MIT, default config works

ODoH (RFC 9230, “Oblivious DNS over HTTPS”) is the IETF protocol that
does this for DNS. Numa v0.14 ships a client, a relay, and a public
deployment in one binary. This post is what it does, what it doesn’t
fix, and what it took to deploy the second public relay in the
ecosystem.

## How it works

INDEPENDENT
OPERATORS - MUST NOT
COLLUDE
[encrypted]
A
example.com?
93.184.216.34
[encrypted]
YOU
NUMA
RELAY
CLOUDFLARE
AUTHORITATIVE

You
Encrypts the query under target’s HPKE pubkey.
Includes a symmetric key for the response.

Numa relay
Sees your IP. Sees only ciphertext, in both
directions.

Cloudflare target
Decrypts the question. Sees no IP -
just relay’s.

Authoritative
Standard DNS recursion. Cloudflare’s job,
not yours.

Return
Cloudflare encrypts the answer with the symmetric
key you supplied and sends it back along the same path. Relay still sees
only ciphertext. Same privacy property, opposite direction.

Encryption uses HPKE (RFC 9180) - the same primitive as TLS Encrypted
ClientHello. Cloudflare publishesodoh-rsfor the
seal/open operations and I used it. Numa’s hand-rolling principle isno DNS libraries; HPKE is a different thing, and hand-rolling
crypto is the kind of decision where every hour of “I want full control”
buys ten of audit anxiety.

## What it took to build

ODoH client mode plugs into Numa’s existing forwarding pipeline as a
fourth transport (alongside UDP, DoH, DoT). The relay is a separate mode
(numa relay [PORT]) - same binary, different entry point,
onlyPOST /relayandGET /healthexposed. Two
things in the relay needed more attention than expected:

SSRF-hardened hostname validator.The relay opens an
outbound connection to a target named in the request URL. Without
validation that’s textbook SSRF - a malicious client could ask it to
“forward” to169.254.169.254and exfiltrate cloud metadata.
The validator is regex-strict (RFC 1035 ASCII labels, no IDN, no IP
literals, no non-443 port).

eTLD+1 same-operator check.ODoH’s guarantee depends
on relay and target being run bydifferentorganizations. If
they share an eTLD+1, one operator can join IP and question across both
legs and the whole construction is theatre. Numa rejects same-operator
configs by default (intentional same-operator setups still possible)

odoh-relay.numa.rsruns in docker-compose on a Hetzner
VPS with Caddy in front for TLS. Default Numa config pairs it withodoh.cloudflare-dns.com- two independent operators in the
path out of the box, no shared eTLD+1. The probe scripttests/probe-odoh-ecosystem.shchecks the whole public
ecosystem in one run.

## What it doesn’t fix

* The target sees the question.ODoH moves trust, it
doesn’t eliminate it. If Cloudflare wants to log every ODoH query they
receive, they can, and there’s no cryptographic protection against that.
The protection is operational: the target doesn’t know who you are, so
the question is unattributed.
* Recursive mode still leaks at the target’s egress.If your target operates in recursive mode, the walk to
root/TLD/authoritative is plaintext UDP/TCP. ODoH protects the
client→target hop; everything past the target is the target’s problem,
not the protocol’s.
* Traffic analysis is possible against small relays.A relay handling few queries leaks correlations: if your IP is the only
one talking to relay A, and Cloudflare receives exactly one query right
after, the timing alone re-identifies you. The defense is volume - more
users on the same relay, more padding traffic, a wider anonymity set.
This is why a single-user self-hosted relay isworsefor
privacy than a busy public one.
* The pubkey distribution is centralized.The client
fetches the target’s HPKE config over plain HTTPS from the target’s own
well-known endpoint. If you don’t trust the WebPKI to deliver the right
config, you don’t trust ODoH. Pkarr-published target keys are an obvious
next step but aren’t shipped yet.
* DNSSEC is orthogonal.ODoH protects the path;
DNSSEC protects the answer’s authenticity. You still want both, and
Numa’s recursive mode does both - encrypted to the target, validated
against the IANA root key.

## The public ecosystem

DNSCrypt’scurated
list(v3/odoh-relays.md, last updated September 2025)
carries one relay entry, with the upstream README noting“odohrelay-crypto-sx seems to be the only ODoH relay left.”Frank Denis runs the well-known public relay atodoh-relay.edgecompute.appon Fastly Compute - it’s the
default indnscrypt-proxy, the only widely-used open-source
ODoH client. Numa adds the second well-known operator atodoh-relay.numa.rsand ships a client that can speak to
either.

This isn’t a product - it’s infrastructure I maintain because Numa
needed it and the existing ecosystem was thin.I’d love to see
other people stand up relays.Same binary Numa users already
run; flip the mode torelay, point Caddy at it, done in a
Sunday afternoon (docker-compose
receipt). The protocol’s privacy properties scale with operator
diversity.

## What’s next

For anonymous DNS today:cargo install numa, setmode = "odoh"innuma.toml, your queries route
through two independent organizations - both open source, both
inspectable. Docker users: there’s aturnkey
compose recipepreconfigured with ODoH mode.

Numa is a DNS resolver that runs on your laptop or phone. ODoH client
+ self-hosted relay, recursive resolution from root with DNSSEC, ad
blocking,.numalocal domains with auto-TLS, a REST API,
and a live dashboard.github.com/razvandimescu/numa.

Discussion:GitHub Issues·Hacker
News.