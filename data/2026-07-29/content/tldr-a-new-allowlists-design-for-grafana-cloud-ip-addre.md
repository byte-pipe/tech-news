---
title: 'A new allowlists design for Grafana Cloud IP addresses: What you need to know | Grafana Labs'
url: https://grafana.com/blog/a-new-allowlists-design-for-grafana-cloud-ip-addresses-what-you-need-to-know/
site_name: tldr
content_file: tldr-a-new-allowlists-design-for-grafana-cloud-ip-addre
fetched_at: '2026-07-29T19:31:40.336935'
original_url: https://grafana.com/blog/a-new-allowlists-design-for-grafana-cloud-ip-addresses-what-you-need-to-know/
date: '2026-07-29'
description: Grafana Cloud's source IP allowlists are moving to a single, structured JSON API. Here's what's changing, why, and what you need to do.
tags:
- tldr
---

# A new allowlists design for Grafana Cloud IP addresses: What you need to know

Pablo Angulo

•
2026-07-23
•
5 min

If your network restricts inbound or outbound traffic, you likelymaintain an allowlistof Grafana Cloud IP addresses so your systems and Grafana Cloud can talk to each other. Today we're introducing anew allowlists design: a single, structured API that replaces the collection of per-product lists we've published until now.

If you don't use IP allowlisting—or you connect to Grafana Cloud over private connectivity such as AWS PrivateLink—nothing changes for you, and no action is needed.

If you do use IP allowlisting, please read on to learn what’s changing, how to update your URLs, and how to test your automations for your migration. All the legacy per-product formats—the JSON lists, their.txtequivalents, and thesrc-ips.<product>.grafana.netDNS records—will continue to work and stay up to dateuntil January 31, 2027to allow for your teams to properly plan and execute your migration.

If you have any issues or questions about this update, please reach out to the Grafana Labs support team.

## What's changing

Until now, Grafana Cloud published source IP addresses through a patchwork of per-product endpoints and formats—a separate JSON list, plain-text list, and DNS record for each product (for example,https://grafana.com/api/hosted-metrics/source-ips, its.txtequivalent, and thesrc-ips.hosted-metrics.grafana.netDNS lookup). Keeping firewalls in sync meant polling several different lists and stitching them together yourself.

We're replacing all of them with a singleAllowlist APIthat serves the current IP addresses as structured JSON over HTTPS:

* Global: all services for all Grafana Cloud regions:https://allowlists.grafana.net/v1/
* Per region: all services for one region:https://allowlists.<your-region>.grafana.net/v1/
* Per service: a single service in one region:https://allowlists.<your-region>.grafana.net/v1/<service>

Each entry tells you the traffic direction and the IPv4 CIDR ranges to allow:

Copy
{
 "metadata": { "schemaVersion": "v1", "region": "prod-eu-west-2" },
 "services": {
 "metrics": {
 "direction": "ingress-to-grafana",
 "ipv4": ["198.51.100.10/32", "198.51.100.11/32"]
 },
 "grafana": {
 "direction": "egress-from-grafana",
 "ipv4": ["203.0.113.20/32"]
 }
 }
}

Valid service names aregrafana,metrics,logs,traces,profiles,otlp,alerts, andfleet-management.

## What you need to do

This isnot a drop-in URL change. The legacy endpoints return flat JSON arrays, plain-text lists, or DNS records, while the new API returns structured JSON containing CIDR ranges and traffic-direction metadata. You must update and test your automation as part of the migration:

1.Find every legacy allowlist reference: Check forgrafana.com/api/*/source-ips, their.txtvariants, andsrc-ips.*.grafana.netDNS records, includingGrafana Assistantrecords.

2.Choose the appropriate new endpoint:

* One service in one region:https://allowlists.<your-region>.grafana.net/v1/<service>
* All services in one region:https://allowlists.<your-region>.grafana.net/v1/
* All services across non-BYOC regions:https://allowlists.grafana.net/v1/

BYOCcustomers must use their regional endpoint because BYOC regions are excluded from the global endpoint.

3.Update your parser for the new response format: The API returns structured JSON and IPv4 CIDRs instead of a flat list of IP addresses. Update legacy service names such ashosted-metricstometrics;hosted-grafanaandgrafana-assistantmap tografana.

4.Test before removing the legacy configuration: Where possible, temporarily combine the addresses returned by the legacy and new systems. Validate telemetry delivery, queries, alert notifications, and other relevant connections before completing the cutover.

5.Fetch the API dynamically: IP addresses can change, so retrieve the current response on a regular schedule rather than copying individual addresses into long-lived firewall configuration.

6.Where possible, use private connectivity: Using private connectivity, such as AWS PrivateLink, GCP Private Service Connect, or Azure Private Link, removes the need for IP allowlisting altogether. You may still need an allowlist for traffic that continues over the public internet, such as connections from Grafana Cloud to external data sources or notification endpoints. Evaluate each traffic path separately.

You can find your stack's region on the instance details pages in your Grafana Cloud stack.

## Timeline

The new Allowlist API is available now. All the legacy per-product formats—the JSON lists, their.txtequivalents, and thesrc-ips.<product>.grafana.netDNS records—will continue to work and stay up to dateuntil January 31, 2027, after which they will be removed.

If any of your firewall automation resolves the oldsrc-ips.*.grafana.netDNS names, make sure to migrate those too. Please complete your migration tohttps://allowlists.grafana.net/before January 31, 2027.

## Why we're making this change

We have reworked how Grafana Cloud publishes its IP allowlists, moving from a mix of formats and global lists to a single, regionally aware JSON schema. The result is easier to automate against and clearer to reason about, whatever your product, region, or deployment model. Here's what changes for you:

* One format instead of many: A single JSON schema across all products and regions replaces the previous mix of JSON, text, and DNS lists.
* This single JSON schema is easierto parse, automate, and validate.
* Better granularity: Query exactly what you need, whether that’s all Grafana Cloud regions, a single region, or a single service in a region. No more filtering a global list to find the addresses that actually apply to your stack.
* Clear traffic direction: Each allowlist clearly states whether it coversingresstraffic (lists the public destination IP addresses your systems connect to when sending data to or querying Grafana Cloud services) oregresstraffic (lists the public source IP addresses Grafana Cloud uses when connecting to your systems, including for data source queries or alert notifications). No more guessing which list to apply on which side of your firewall.
* Support across deployment models: The regional design works for Grafana Cloud-managed regions and BYOC while preserving BYOC region isolation.

## Where to learn more

For full details, response schemas, and examples, see theList of source IP addresses to add to your allowlist. For further guidance, please reach out to the Grafana Labs support team.

Tags

Grafana Cloud