---
title: 'GitHub - cilium/cilium: eBPF-based Networking, Security, and Observability · GitHub'
url: https://github.com/cilium/cilium
site_name: github
content_file: github-github-ciliumcilium-ebpf-based-networking-security
fetched_at: '2026-09-17T15:26:49.510674'
original_url: https://github.com/cilium/cilium
author: cilium
description: eBPF-based Networking, Security, and Observability - cilium/cilium
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 cilium

 

/

cilium

Public

* NotificationsYou must be signed in to change notification settings
* Fork4.1k
* Star25.3k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

44,642 Commits
44,642 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.devcontainer
.devcontainer
 
 
.github
.github
 
 
.nvim
.nvim
 
 
.vscode
.vscode
 
 
Documentation
Documentation
 
 
api/
v1
api/
v1
 
 
bpf
bpf
 
 
bugtool
bugtool
 
 
cilium-cli
cilium-cli
 
 
cilium-dbg
cilium-dbg
 
 
cilium-health
cilium-health
 
 
clustermesh-apiserver
clustermesh-apiserver
 
 
contrib
contrib
 
 
daemon
daemon
 
 
examples
examples
 
 
hack
hack
 
 
hubble-relay
hubble-relay
 
 
hubble
hubble
 
 
images
images
 
 
install/
kubernetes
install/
kubernetes
 
 
operator
operator
 
 
pkg
pkg
 
 
plugins
plugins
 
 
standalone-dns-proxy
standalone-dns-proxy
 
 
test
test
 
 
tools
tools
 
 
vendor
vendor
 
 
.authors.aux
.authors.aux
 
 
.clang-format
.clang-format
 
 
.clomonitor.yml
.clomonitor.yml
 
 
.custom-gcl.yaml
.custom-gcl.yaml
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.golangci.yaml
.golangci.yaml
 
 
.mailmap
.mailmap
 
 
AUTHORS
AUTHORS
 
 
CODEOWNERS
CODEOWNERS
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
MAINTAINERS.md
MAINTAINERS.md
 
 
Makefile
Makefile
 
 
Makefile.defs
Makefile.defs
 
 
Makefile.docker
Makefile.docker
 
 
Makefile.kind
Makefile.kind
 
 
Makefile.quiet
Makefile.quiet
 
 
README.rst
README.rst
 
 
SECURITY-INSIGHTS.yml
SECURITY-INSIGHTS.yml
 
 
SECURITY.md
SECURITY.md
 
 
USERS.md
USERS.md
 
 
VERSION
VERSION
 
 
go.mod
go.mod
 
 
go.sum
go.sum
 
 
netlify.toml
netlify.toml
 
 
stable.txt
stable.txt
 
 
View all files

## Repository files navigation

 
 
 
 
 

 
 

 

 

 
 
 

Cilium is a networking, observability, and security solution with an eBPF-based
dataplane. It provides a simple flat Layer 3 network with the ability to span
multiple clusters in either a native routing or overlay mode. It is L7-protocol
aware and can enforce network policies on L3-L7 using an identity-based security
model that is decoupled from network addressing.

Cilium implements distributed load balancing for traffic between pods and to
external services, and is able to fully replace kube-proxy, using efficient
hash tables in eBPF, allowing for almost unlimited scale. It also supports
advanced functionality like integrated ingress and egress gateways, bandwidth
management, and service mesh, and provides deep network and security visibility and monitoring.

A new Linux kernel technology calledeBPFis at the foundation of Cilium. It
supports dynamic insertion of eBPF bytecode into the Linux kernel at various
integration points such as: network IO, application sockets, and tracepoints to
implement security, networking, and visibility logic. eBPF is highly efficient
and flexible. To learn more about eBPF, visiteBPF.io.

## Stable Releases

The Cilium community maintains minor stable releases for the last three minor
Cilium versions. Older Cilium stable versions from minor releases prior to that
are considered EOL.

For upgrades to new minor releases, please consult theCilium Upgrade Guide.

Listed below are the actively maintained release branches along with their latest
patch release, corresponding image pull tags and their release notes:

v1.20

2026-09-15

quay.io/cilium/cilium:v1.20.2

Release Notes

v1.19

2026-09-15

quay.io/cilium/cilium:v1.19.8

Release Notes

v1.18

2026-09-15

quay.io/cilium/cilium:v1.18.14

Release Notes

### Architectures

Cilium images are distributed for AMD64 and AArch64 architectures.

### Software Bill of Materials

Starting with Cilium version 1.13.0, all images include a Software Bill of
Materials (SBOM). The SBOM is generated inSPDXformat. More information
on this is available onCilium SBOM.

## Development

For development and testing purposes, the Cilium community publishes snapshots,
early release candidates (RC) and CI container images built from themain
branch. These images are
not for use in production.

For testing upgrades to new development releases, please consult the latest
development build of theCilium Upgrade Guide.

Listed below are branches for testing along with their snapshots or RC releases,
corresponding image pull tags and their release notes where applicable:

main

daily

quay.io/cilium/cilium-ci:latest

N/A

v1.21.0-pre.2

2026-09-09

quay.io/cilium/cilium:v1.21.0-pre.2

Release Notes

## Functionality Overview

### CNI (Container Network Interface)

Cilium as a CNI pluginprovides a
fast, scalable, and secure networking layer for Kubernetes clusters. Built
on eBPF, it offers several deployment options:

* Overlay networking:an encapsulation-based virtual network spanning all
hosts with support for VXLAN and Geneve. It works on almost any network
infrastructure as the only requirement is IP connectivity between hosts
which is typically already given.
* Native routing mode:Use of the regular routing table of the Linux
host. The network must be capable of routing the IP addresses
of the application containers. It integrates with cloud routers, routing
daemons, and IPv6-native infrastructure.
* Flexible routing options:Cilium can automate route learning and
advertisement in common topologies such as using L2 neighbor discovery
when nodes share a layer 2 domain, or BGP when routing across layer 3
boundaries.

Each mode is designed for maximum interoperability with existing
infrastructure while minimizing operational burden.

### Load Balancing

Cilium implements distributed load balancing for traffic between application
containers and to/from external services. The load balancing is implemented
in eBPF using efficient hash tables, enabling high service density and low
latency at scale.

* East-west load balancingrewrites service connections at the socket
level (connect()), avoiding the overhead of per-packet NAT and fullyreplacing kube-proxy.
* North-south load balancingsupports XDP for high-throughput scenarios
andlayer 4 load balancingincluding Direct Server Return (DSR), and Maglev consistent hashing.

### Cluster Mesh

CiliumCluster Meshenables
secure, seamless connectivity across multiple Kubernetes clusters. For
operators running hybrid or multi-cloud environments, Cluster Mesh ensures
a consistent security and connectivity experience.

* Global service discovery: Workloads across clusters can discover and
connect to services as if they were local. This enables fault tolerance,
like automatically failing over to backends in another cluster, and
exposes shared services like logging, auth, or databases across
environments.
* Unified identity model:Security policies are enforced based on
identity, not IP address, across all clusters.

### Network Policy

CiliumNetwork Policyprovides identity-aware enforcement across L3-L7. Typical container
firewalls secure workloads by filtering on source IP addresses and
destination ports. This concept requires the firewalls on all servers to be
manipulated whenever a container is started anywhere in the cluster.

In order to avoid this situation which limits scale, Cilium assigns a
security identity to groups of application containers which share identical
security policies. The identity is then associated with all network packets
emitted by the application containers, allowing the identity to be validated
at the receiving node.

* Identity-based securityremoves reliance on brittle IP addresses.
* L3/L4 policiesrestrict traffic based on labels, protocols, and ports.
* DNS-based policies:Allow or deny traffic to FQDNs or wildcard domains(e.g.,api.example.com,*.trusted.com). This is especially useful
for securing egress traffic to third-party services.
* L7-aware policiesallow filtering by HTTP method, URL path, gRPC call,
and more:Example: Allow only GET requests to/public/.*.Enforce the presence of headers likeX-Token: [0-9]+.
* Example: Allow only GET requests to/public/.*.
* Enforce the presence of headers likeX-Token: [0-9]+.

CIDR-based egress and ingress policies are also supported for controlling
access to external IPs, ideal for integrating with legacy systems or
regulatory boundaries.

### Service Mesh

With CiliumService Mesh,
operators gain the benefits of fine-grained traffic control, encryption, observability,
and access control without the cost and complexity of traditional proxy-based
designs. Key features include:

* Mutual authenticationwith automatic identity-based encryption between
workloads using IPSec or WireGuard.
* L7-aware policy enforcementfor security and compliance.
* Deep integration with the Kubernetes Gateway API:Acts as aGateway APIcompliant data
plane, allowing you to declaratively manage ingress, traffic splitting, and
routing behavior using Kubernetes-native CRDs.

### Observability and Troubleshooting

Observability is built into Cilium from the ground up, providing rich
visibility that helps operators diagnose and understand system behavior
including:

* Hubble: A fully integrated observability platform that offers
real-time service maps, flow visibility with identity and label metadata,
and DNS-aware filtering and protocol-specific insights
* Metrics and alerting: Integration with Prometheus, Grafana, and other
monitoring systems.
* Drop reasons and audit trails: Get actionable insights into why traffic
was dropped, including policy or port violations and issues like failed
DNS lookups.

## Getting Started

* Why Cilium?
* Getting Started
* Architecture and Concepts
* Installing Cilium
* Frequently Asked Questions
* Contributing

## Community

### Slack

Join the CiliumSlack channelto chat with
Cilium developers and other Cilium users. This is a good place to learn about
Cilium, ask questions, and share your experiences.

### Special Interest Groups (SIG)

SeeSpecial Interest Groupsfor a list of all SIGs and their meeting times.

### Developer meetings

The Cilium developer community hangs out on Zoom to chat. Everyone is welcome.

* Weekly, Wednesday,
5:00 pmEurope/Zurich time(CET/CEST),
usually equivalent to 8:00 am PT, or 11:00 am ET.Meeting Notes and Zoom Info
* Third Wednesday of each month, 1:30 pmJapan time(JST).APAC Meeting Notes and Zoom Info

### eBPF & Cilium Office Hours livestream

We host a weekly communityYouTube livestream called eCHOwhich (very loosely!) stands for eBPF & Cilium Office Hours. Join us live, catch up with past episodes, or head over to theeCHO repoand let us know your ideas for topics we should cover.

### Governance

The Cilium project is governed by a group ofMaintainers and Committers.
How they are selected and govern is outlined in ourgovernance document.

### Adopters

A list of adopters of the Cilium project who are deploying it in production, and of their use cases,
can be found in fileUSERS.md.

## License

The Cilium user space components are licensed under theApache License, Version 2.0.
The BPF code templates are dual-licensed under theGeneral Public License, Version 2.0 (only)and the2-Clause BSD License(you can use the terms of either license, at your option).