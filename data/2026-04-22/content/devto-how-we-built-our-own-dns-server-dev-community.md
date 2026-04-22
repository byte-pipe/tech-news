---
title: How We Built Our Own DNS Server - DEV Community
url: https://dev.to/code42cate/how-we-built-our-own-dns-server-4d3k
site_name: devto
content_file: devto-how-we-built-our-own-dns-server-dev-community
fetched_at: '2026-04-22T20:04:34.053405'
original_url: https://dev.to/code42cate/how-we-built-our-own-dns-server-4d3k
author: Jonas Scholz
date: '2026-04-17'
description: We wrote a production DNS server in ~1000 lines of Go, migrated thousands of records off Hetzner DNS,... Tagged with cloud, devops, docker, webdev.
tags: '#cloud, #devops, #docker, #webdev'
---

90-minute propagation cut to seconds

We wrote a production DNS server in ~1000 lines of Go, migrated thousands of records off Hetzner DNS, and dropped propagation time from "up to 90 minutes" to a few seconds. It uses the hidden primary pattern, Postgres as the event bus, and AXFR + IXFR to push zones to public secondaries. Here's how and why we did it!

## Why Hetzner DNS Stopped Working for Us

Every service on Sliplane gets a managed subdomain like my-app-abc123.sliplane.app. That means an A and AAAA record for every running service, pointing at the server IP where the container lives. Records scale linearly with the platform.

We started with Hetzner DNS because it was free and we already ran most of our infra there. That worked fine for a while, but after 2 years we hit two walls:

Record limits: Hetzner DNS has a hard cap per zone. Originally 500, they bumped it to 10k for us (genuinely appreciate that), but at our growth rate we'd blow through that within weeks. Apparently we're one of their biggest DNS users by record count :D

Speed: After creating a record via the API, it could take up to 90 minutes before Hetzner's own nameservers actually returned it. For a PaaS where someone just deployed a service and wants to visit the URL, that's a rough experience. Although this wasn't consistently that bad, everytime that happened it directly affected the user experience. It simply looked like our platform was broken (which in that case it was!).

## Why Not Just Use Another Managed Provider?

Fair question. For most people, a managed DNS provider is the right answer. But once you start shopping around at our "scale" and constraints, things get annoying fast:

"Contact sales" pricing.A lot of the providers that could comfortably handle our record count sit behind "talk to sales" forms. I hate that. Just tell me what it costs.

Per-record or per-query billing.The ones that do publish pricing often charge per record or per query. We have no idea how many DNS queries we actually serve, so migrating to an unknown pricing model felt like signing a blank check.

EU-only.We're based in the EU and wanted to keep DNS there too. That narrows the field a lot.

And honestly, it sounded fun.I'm a bit of a controlfreak and writing a DNS server is the kind of thing you daydream about. A thousand lines of Go felt worth the freedom. In the end, building the thing took less time than getting a meeting with a managed provider would have 😵‍💫

So we built it ourselves, which brings us to the pattern that made it surprisingly simple.

## The Hidden Primary Pattern

The reason why this is all way simpler than I initially thought: our DNS server never answers a single public query.

In DNS, a zone's primary nameserver holds the authoritative records. Secondaries pull copies usingAXFR(basically a full zone dump over TCP) and answer public queries just like the primary would. When the primary changes, it sends a NOTIFY to the secondaries, and they pull a fresh copy.

Ahidden primarytakes this one step further, the primary isn't public at all. It only exists to push zone data to secondaries. The public nameservers, the ones listed at your registrar, are all secondaries.

This means we can run our DNS server wherever we want, use any secondary provider that supportsAXFR, and swap providers without changing our server. No lock-in because AXFR and NOTIFY are standard protocols, any compliant secondary will work.

No anycast, no super redundant ddos protected DNS servers deployed across the globe. Just a few instances of our primary hidden server.

## The Architecture

The setup is pretty minimal:

Postgres is the source of truth.We install triggers that callpg_notify('dns_zone_changed', '')whenever a service is created, updated, or deleted. No message queue, no webhooks. Postgresisthe event bus.

Why not Redis, NATS, or a proper queue? Two reasons. We already run Postgres as our primary database, soLISTEN/NOTIFYis "free" (no free lunch, but as free as it gets) infrastructure, nothing new to operate, monitor, or pay for. And the volume is tiny. Zone changes happen a few times per minute at peak, which is laughably low for anything queue-shaped. Reaching for Kafka here would be like renting a shipping container to mail a postcard.

sliplane-dnsis a small Go server (~1000 lines, built onmiekg/dns) that subscribes viaLISTEN, queries Postgres for all managed domains and their IPs, builds the DNS zone, and serves it via AXFR.

To avoid unnecessary work, we hash all records. If the hash matches the previous zone, nothing happens, no serial bump, no NOTIFY. When the zone actually changes, we bump the SOA serial and send DNS NOTIFY to Hetzner's three secondary IPs. They pull the new zone, and records are live.

To see what a zone transfer actually looks like, here's a minimal DNS server that only speaks AXFR. It serves a hardcoded zone forexample.comwith a single A record (full code on GitHub):

package
 
main

import
 
(

 
"context"

 
"log"

 
"net/netip"

 
"codeberg.org/miekg/dns"

 
"codeberg.org/miekg/dns/rdata"

)

func
 
main
()
 
{

 
soa
 
:=
 
&
dns
.
SOA
{

 
Hdr
:
 
dns
.
Header
{
Name
:
 
"example.com."
,
 
TTL
:
 
3600
,
 
Class
:
 
dns
.
ClassINET
},

 
SOA
:
 
rdata
.
SOA
{
Ns
:
 
"ns1.example.com."
,
 
Mbox
:
 
"admin.example.com."
,
 
Serial
:
 
1
},

 
}

 
records
 
:=
 
[]
dns
.
RR
{

 
soa
,

 
&
dns
.
A
{

 
Hdr
:
 
dns
.
Header
{
Name
:
 
"app.example.com."
,
 
TTL
:
 
300
,
 
Class
:
 
dns
.
ClassINET
},

 
A
:
 
rdata
.
A
{
Addr
:
 
netip
.
MustParseAddr
(
"1.2.3.4"
)},

 
},

 
soa
,

 
}

 
mux
 
:=
 
dns
.
NewServeMux
()

 
mux
.
HandleFunc
(
"example.com."
,
 
func
(
_
 
context
.
Context
,
 
w
 
dns
.
ResponseWriter
,
 
r
 
*
dns
.
Msg
)
 
{

 
r
.
Unpack
()

 
w
.
Hijack
()

 
env
 
:=
 
make
(
chan
 
*
dns
.
Envelope
,
 
len
(
records
))

 
for
 
_
,
 
rr
 
:=
 
range
 
records
 
{

 
env
 
<-
 
&
dns
.
Envelope
{
Answer
:
 
[]
dns
.
RR
{
rr
}}

 
}

 
close
(
env
)

 
dns
.
NewClient
()
.
TransferOut
(
w
,
 
r
,
 
env
)

 
w
.
Close
()

 
})

 
srv
 
:=
 
dns
.
NewServer
()

 
srv
.
Addr
 
=
 
":5553"

 
srv
.
Net
 
=
 
"tcp"

 
srv
.
Handler
 
=
 
mux

 
log
.
Fatal
(
srv
.
ListenAndServe
())

}

Enter fullscreen mode

Exit fullscreen mode

Run it and pull the zone with dig:

dig @localhost 
-p
 5553 example.com AXFR

Enter fullscreen mode

Exit fullscreen mode

example
.
com
. 
3600
 
IN
 
SOA
 
ns1
.
example
.
com
. 
admin
.
example
.
com
. 
1
 
0
 
0
 
0
 
0

app
.
example
.
com
. 
300
 
IN
 
A
 
1
.
2
.
3
.
4

example
.
com
. 
3600
 
IN
 
SOA
 
ns1
.
example
.
com
. 
admin
.
example
.
com
. 
1
 
0
 
0
 
0
 
0

Enter fullscreen mode

Exit fullscreen mode

The full zone transfer is just SOA, all records, SOA again. This is roughly what Hetzner's secondaries pull from our production server, just with a few thousand more records in between the two SOAs.

## Saturday Night DNS Surgery

You can't gradually migrate DNS nameservers. The NS records at the registrar point to either the old set or the new set. There's a cutover window, no way around it.

We had to switch from Hetzner's nameservers (hydrogen.ns.hetzner.com,oxygen.ns.hetzner.com,helium.ns.hetzner.de) to Hetzner Robot's secondary nameservers (ns1.first-ns.de,robotns2.second-ns.de,robotns3.second-ns.com).

During the transition, resolvers with cached old NS records would still ask the old servers and get stale data until TTL expired. Two things made this manageable: the NS delegation TTL was 5 minutes, and onlynewservices deployed during that window were affected. Existing A/AAAA records were identical on both sets of nameservers.

We did it on a Saturday night when platform activity was lowest. It went smooth, no users complained!

## The One Thing That Bit Us: IXFR

I went into this thinking AXFR was enough. It's the protocol every tutorial shows, every example uses, and it's what I built first. Full zone dump, SOA at the start, SOA at the end, done.

Turns out Hetzner Robot's secondaries don't just do AXFR. When they already have a zone and see a new SOA serial via NOTIFY, they ask for anincrementalzone transfer first (IXFR, RFC 1995), a diff of only the records that changed since the old serial. If the primary doesn't speak IXFR, a well-behaved secondary falls back to AXFR. Hetzner Robot apparently doesn't fall back cleanly in every case, so zones weren't updating reliably until we implemented IXFR too.

IXFR isn't hard, you just keep a small history of recent zone versions and, on request, return the delta between the client's serial and the current one. But it's the kind of thing you'd only discover by actually shipping it against a real secondary. Cheers to whoever wrote that RFC.

## Was It Worth It?

So far, 100%. Propagation went from "up to 90 minutes" to however long it takes to do a zone transfer, which for our zone size is practically instant. The zone grows with the platform without hitting any record ceilings, and we also have full observability baked in.

## Should You Do This?

Probably not. Use Cloudflare DNS, Route 53, or whatever managed DNS your provider offers. They're fast, they work, and you don't have to think about them.

But if youdoend up hitting the limits of a managed DNS provider, the hidden primary pattern is worth knowing about. Your primary doesn't need to be public, you can use any AXFR-compatible secondary, and you can swap providers without touching your server.

Cheers,

Jonas, Co-Foundersliplane.io

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (21 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse