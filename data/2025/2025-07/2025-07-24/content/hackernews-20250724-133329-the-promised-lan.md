---
title: 🖧 The Promised LAN
url: https://tpl.house/
site_name: hackernews
fetched_at: '2025-07-24T13:33:29.706452'
original_url: https://tpl.house/
author: Bogdanp
date: '2025-07-24'
---

# 🖧 The Promised LAN

The Promised LAN is a closed, membership only network of friends that operate
a 24/7 always-on LAN party, running since 2021. The vast majority of
documentation is maintained on the LAN, but this website serves to give
interested folks, prospective members or friends an idea of what the Promised
LAN is, and how it works.

## A Manifesto for The Promised LAN

For background on why we started the lan, what we hope to achieve, and how we
approach the social-technical dynamics, we haveposted a Manifestoto encourage more
similarly structured LANs.It is worth reading this before moving on.
The social and technical aspects are intertwined here.

## Backbone Network

Each Promised LAN segment connects to the Backbone network, since each LAN
connecting to every other LAN quickly becomes unmaintainable, even with a small
number of segments -- individual dynamic IPs change, keying material exchanges,
negotiating a cipher suite; it gets hard! As a result, we have all LANs connect
to the closest backbone node, and traffic is routed through the backbone network.

The network is made up of independently operated and heterogeneous nodes
(currently three nodes, a mix of Debian usingstrongSwanand
OpenBSD usingiked), which peer over IPSec links. We've decided on
a set of common algorithms which appear to be the best tradeoff of speed,
security and support for our existing backbone nodes.

AlgorithmsIKE SA AuthHMAC SHA2 512IKE SA EncryptionAES 256IKE SA DHCurve25519Child SA EncryptionChaCha20 Poly1305Child SA DHCurve25519

The Backbone network operates in a dedicated /24 allocation, where individual
backbones are issued an IP based on its "Node ID". Each backbone is only
hardcoded with the routes for each directly connected backbone via its IPSec
connection. This network of nodes operates as The Promised LAN'sDefault Free Zone (DFZ).
Once the IP links are established, backbones communicate using BGP (currentlybirdon Debian andbgpdon OpenBSD) in order to advertise directly connected user LANs to the rest of
the backbone network.

## DNS

We're using our own non-standard and possibly ill-advised TLD, which is.tpl— short for The Promised LAN. Each LAN gets a domain
automatically when it joins the LAN — and folks can request new domains
for whatever they want after joining. There are a set of root DNS servers
(ns1.tpl,ns2.tpl,ns3.tpl) which are
hosted on three different LANs which are each connected to a different backbone
node, in the event of network outages. We strive to keep core services
running, even if a node is completely disconnected from all others. Eachauthoritative nameserveris running annsd, with a config replicated by pulling a centralgitrepo on a cron.

By convention (mostly to avoid managing a bunch ofglue records),
we expect that each LAN runs their own authoritative nameserver at the fixed
IP ofx.x.x.254. This allows us to automate and template the
configurations when LANs join, at a pretty minor cost.

Since each LAN doesn't really need to know all the roots themselves (unless
they want), we run arecursive resolveron ananycastedIP block (x.x.0.1),
running local on the backbones themselves. This is generally runningunbound.

## PKI

Even though everything here is already secure enough for us, deploying services
that useTLSmakes using existing/modern tools a lot easier. On
the whole PKI is way more work than it's worth here, but we decided to engineer
this properly.

We operate a set of root x509 Certificate Authorities, each with a three year
lifetime. The first year allows us to distribute the roots across the LAN and
let the roots update along with the cadence of routine system maintenance. The
second year is that root's "operational" year, where all x509 certificates are
issued by that root, and finally, the last year is the transition year to allow
issued certs to expire naturally without the CA being invalid.

Currently, we issue roots using theECDSA P-384key type,
withSHA384signatures. Additionally, each CA containsX509v3 Name Constraints(markedcritical) which
limit validity toDNS:.tplandemail:.tpl.

Finally, we figured we'd use our existingDNSfor managing
our x509 certificate issuance — so we don't have to sendCSRs
around and wait for human action. Deploying something likeACMEis overkill (for now) and a maintenance nightmare. We wrote something fairly
basic instead, since we can easily constrain our problem space and rules.
Every LAN may set DNSTXTrecords named_pkifor a given domain, which contains an OpenSSH public key. Signing a new
certificate is done over SSH -- where a CSR is signed by checking the requested
SAN is against the key used to authenticate to the CA against the PKI DNS records
to make an issuance decision.
