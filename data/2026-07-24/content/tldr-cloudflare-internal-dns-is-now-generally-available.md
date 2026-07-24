---
title: Cloudflare Internal DNS is now generally available | The Cloudflare Blog
url: https://blog.cloudflare.com/internal-dns/
site_name: tldr
content_file: tldr-cloudflare-internal-dns-is-now-generally-available
fetched_at: '2026-07-24T19:32:44.880182'
original_url: https://blog.cloudflare.com/internal-dns/
date: '2026-07-24'
published_date: '2026-07-20T20:59:31.072Z'
description: Cloudflare Internal DNS brings authoritative and recursive DNS for private networks to the same global network and control plane that runs Cloudflare's Zero Trust, networking, and public DNS.
tags:
- tldr
---

Starting today, Cloudflare Internal DNS is generally available. Cloudflare Internal DNS provides authoritative and recursive DNS for private networks on the same global network and control plane customers already use for public DNS, Zero Trust, networking, and application services.

Internal DNS — sometimes also referred to as private DNS — is one of the last pieces of enterprise infrastructure still managed separately from the rest of the network. Many organizations operate one platform for public DNS, another for internal DNS, and use cloud-native DNS services inside each cloud environment with separate security policies layered on top. None of these systems share a common control plane. Split-horizon DNS adds another layer of complexity, often requiring multiple DNS environments to remain synchronized so internal and external users receive different answers for the same hostname. When those systems drift, outages follow.

With Cloudflare Internal DNS, you get a single platform to manage public and private DNS resources, enforcingDNS policiesand gaining visibility across your entire DNS stack. For Enterprise customers, this is included withCloudflare Gatewaywithout any additional charge.

## Why customers are adopting Internal DNS

Consolidate DNS operations. Public and private DNS run on one platform, with one API, one audit trail, and one place to set policy. The appliance refresh cycle and the scaling bottlenecks that came with legacy DNS go away.

Simplify split-horizon DNS. Internal and external resolution are defined as separate views over shared zones, managed from a single control plane. There are no parallel systems to keep in sync, so there's no drift to chase down.

Extend Zero Trust to DNS. Resolver policies decide which users and devices resolve against which view, enforced by the same Cloudflare Gateway that already governs the rest of your traffic. Private name resolution stops being the gap in an otherwise Zero Trust architecture.

Modernize legacy infrastructure. Retire hardware appliances, legacy DNS servers, and cloud-locked resolvers. Cloudflare Internal DNS runs on the infrastructure behind 1.1.1.1, with no hardware to rack and no capacity to provision.

## What we built

Cloudflare Internal DNS consists of two components:Gateway ResolverandInternal Authoritative DNS. Authoritatively managing zones is a different job from enforcing DNS security and routing policies.

The Gateway Resolver handles recursive resolution and policy evaluation.Launched in 2020and powered by 1.1.1.1 for public resolution, it comes with a built-in policy engine that can filter DNS queries and redirect queries to different upstream sources — all based onflexible expressions, with comprehensive logging and audits feeding a single pane of glass.

Internal Authoritative DNS serves records for internal zones built on the same authoritative platform Cloudflare has operated for over a decade and thatserves more domainsthan any other provider.

There are three primary objects customers work with:

* Internal Zoneshold the authoritative records for private resources: environment-specific apps, service endpoints, databases.
* DNS Viewsgroup zones into the resolution context a given set of users or devices should see. This is what makes split-horizon work without parallel systems.
* Resolver Policiessit in Gateway and route matching queries to a specific view.

Zone references let administrators reuse a shared zone across multiple views rather than copying its records into each one. A common zone like intranet.local is defined once and referenced everywhere it's needed, which is the difference between a Don't-Repeat-Yourself configuration and the duplicated, drift-prone setup that split-horizon usually forces.

### How a query resolves

A DNS query from a client first hits the Gateway Resolver, where policy is evaluated. From there, one of three things happens. If a resolver policy matches and points at an internal view, the query is routed to Internal Authoritative DNS and answered from the matching view's zones. If policy blocks the query, it is dropped at the resolver. Otherwise, the query follows the public path, with 1.1.1.1 resolving it against the public DNS hierarchy. Views can also fall back to public resolution when a name isn't found internally, so a single resolver can serve both private and public names without the client needing to know which is which.

### How a change propagates

Record changes follow a predictable, high-speed path from input to edge.

Every change enters through the same DNS Records API, whether it originates in the dashboard, in Terraform, or in a direct API call. That unified ingress means there is exactly one write path to reason about and audit, regardless of how the change was made. The change is persisted in Cloudflare's core data centers for durability and validated before it propagates.

From there, changes replicate across Cloudflare's global network and affected cached entries are invalidated as the updates arrive, so edited records take effect in seconds rather than waiting on TTL expiry.

### Getting started

If you're an Enterprise customer using Cloudflare Gateway, you have access to Internal DNS today. Open the Cloudflare dashboard, navigate to Networking, thenInternal DNS.

Setting up Internal DNS typically takes three steps: create a zone, create a view, and define a resolver policy that determines which users and devices should resolve against that view.

Create an internal zone and your first internal record:

POST https:
//api.cloudflare.com/client/v4/accounts/zones

{

  "account"
: {

    "id"
: 
"{account_id}"

  },

  "name"
: 
"corp.internal"
,

  "type"
: 
"internal"

}

POST https:
//api.cloudflare.com/client/v4/zones/{zone_id}/dns_records

{

  "type"
: 
"A"
,

  "name"
: 
"db.corp.internal"
,

  "content"
: 
"10.0.1.50"
,

  "ttl"
: 
300

}

Then create a DNS view and link your zone to it:

POST https:
//api.cloudflare.com/client/v4/accounts/{account_id}/internal_dns/views

{

  "name"
: 
"production-view"
,

  "zones"
: [
"{zone_id}"
]

}

Finally,create a Gateway resolver policyin theZero Trust dashboardthat routes matching traffic to your view.Create a Gateway location, set your conditions, select Internal DNS View as the resolution method, and choose your view. That's it. Queries matching your policy now resolve against your internal zones.

Terraform support is available, and because Terraform writes through the same DNS Records API as everything else, infrastructure-as-code changes follow the identical ingestion and propagation path. Full documentation and end-to-end configuration examples are available inour developer documentation.

### Internal DNS as part of the Connectivity Cloud

Internal DNS works with any Cloudflare connectivity method that routes DNS traffic through the Gateway Resolver, including the Cloudflare One Client (formerly WARP), DNS over HTTPS (DoH), DNS over TLS (DoT), standard DNS on port 53, PAC file deployments, and Cloudflare WAN.

For organizations running Cloudflare WAN, every device on the connected network can resolve internal hostnames through Cloudflare without requiring the Cloudflare One Client on individual devices. The result is a consistent DNS experience across remote users, branch offices, data centers, and cloud environments using a single control plane.

More importantly, Internal DNS is not a standalone DNS service. It extends the same Connectivity Cloud platform that organizations already use to secure users with Zero Trust, connect networks with Cloudflare WAN, accelerate applications, and protect Internet-facing services.

Bringing private DNS onto the same global network as everything else is just the starting point. Tighter integration across DNS, networking, and Zero Trust policy is where this goes next — so resolving an internal hostname, reaching the service behind it, and enforcing who is allowed to access it become decisions made through a single platform, rather than multiple disconnected systems.

Ready to consolidate your DNS? Open the dashboard, head to Networking, thenInternal DNS, and create your first zone today. Questions or want to compare notes with other operators? Join the conversation in theCloudflare Community.

## Related tags

Cloudflare Gateway
DNS
General Availability
Internal DNS
Networking
Product News
SASE
Zero Trust

Follow on Social Media

* Cloudflare
* Hannes Gerhart

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.