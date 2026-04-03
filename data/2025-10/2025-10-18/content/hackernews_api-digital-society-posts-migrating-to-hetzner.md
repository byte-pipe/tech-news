---
title: Digital Society | Posts | Migrating to Hetzner
url: https://digitalsociety.coop/posts/migrating-to-hetzner-cloud/
site_name: hackernews_api
fetched_at: '2025-10-18T11:07:22.096538'
original_url: https://digitalsociety.coop/posts/migrating-to-hetzner-cloud/
author: pingoo101010
date: '2025-10-17'
description: We saved 76% on our cloud bills while tripling our capacity by migrating to Hetzner from AWS and DigitalOcean. Digital Society is a not-for-profit cooperative helping you get your projects off the ground and realise the value of your data.
tags:
- hackernews
- trending
---

# Migrating to Hetzner

02/10/2025

We saved 76% on our cloud bills while tripling our capacity by migrating to Hetzner from AWS and DigitalOcean.

## Background

All the software we build atDigitalSocietyruns in the cloud. Prior to the migration we ran workloads on two platforms:

* We use AWS for some of our core hosting needs (DNS viaRoute53and sending emails viaSES).We also chose AWS to hosttap, our first SaaS product, using a variety of AWS services (ECSfor container orchestration,RDSfor relational databases,ALBfor ingress, and a long tail of peripheral services, as is the AWS way).We chose AWS for familiarity since we have worked with it for nearly 15 years. We also prize their reliability, particularly when it comes to API stability. We automate as much of our infrastructure management as possible, and don't want to spend time chasing API breaking changes.
* We usedDigitalOcean Kubernetesto host several lightweight services, such asepcdata.scot, and monitoring services (Umamifor web analytics,OpenObservefor telemetry, andUptime Kumafor availability monitoring).We chose DigitalOcean for its relatively simple and cost-effective managed Kubernetes offering, where you pay for the cluster's resources (nodes, block storage, load balancers) but the controlplane is free.We chose Kubernetes for familiarity since we have worked with it for nearly 10 years. Although it requires a lot ofboilerplate configuration, once it has been set up Kubernetes enables a frictionless developer experience for deploying applications quickly.

Why two cloud providers? Initially we used only DigitalOcean, but a data intensive SaaS like tap needs a lot of cloud resources and AWS have a generous$1,000 creditpackage for self-funded startups. Building tap with AWS credits let us experiment with our infrastructure needs without worrying about the cost.

## Credits don't last forever

In the spirit of minimising our operational costs we opted to use AWS' serverless container runtime,Fargate. This lets us pay per-second for the CPU and memory used by our application. Fargate's monthly pricing scales down fairly well, with a minimal workload (0.25 CPU, 0.5 GiB RAM) costing around $10/month.

However, tap is a data-intensive SaaS that needs to be able to execute complex queries over gigabytes of data in seconds. Even though we use the blazingly fastRustprogramming language and modern, efficient data technologies likeApache ArrowandDataFusion, we have found the minimum resource requirements for good performance to be around 2x CPUs and 4 GiB RAM – ideally even more to get a good experience for demanding queries.

How much does a 2x CPU, 4 GiB RAM container cost on AWS Fargate? Just over $70/month. We run two worker instances, which need these higher resources, along with smaller web instances and all the other infrastructure needed to host an application on AWS (load balancer, relational DB, NAT gateway, ...). All together, our total costs for two environments of tap grew to$449.50/month.

In the end we used up our free credits in less than 6 months, and as a bootstrapped startup absorbing that kind of running cost is painful.

## Investigating alternatives

Faced with these high running costs we started to investigate alternative cloud providers. Around the same time, tariff wars and the growth of AI-powered technofeudalism made us look specifically forUK or EU basedcloud providers.

We quickly came acrossHetzner, and while their offering is geared towards self-managed VPS, meaning additional maintenance compared to managed solutions, we were sold on their pricing (more detail later). So much so that we decided to migrate our DigitalOcean infrastructure as well.

Since most of our services were already running in Kubernetes, and tap was already container-based, we decided we would run Kubernetes. Having operated Kubernetes clusters before this wasn't a decision taken lightly, but we discoveredTalos Linuxwhich promised to simplify the cluster setup and maintenance.

Our existing Kubernetes clusters in DigitalOcean used aruntimethat we created to cover basic infrastructure needs for web applications. Combined with Kubernetes' native container orchestration features, these covered all the functionality we were using in AWS and DigitalOcean except for managed PostgreSQL databases. Given that these are critical pieces of infrastructure, we wanted a robust solution that included detailed monitoring, automated failover, seamless upgrades, and scheduled backups. We foundCloudNativePGwhich ticks all our boxes.

## The new stack

Altogether, this is the stack we landed on:

* Hetzneras the core infrastructure provider. We use their ARM shared vCPU cloud servers, block storage volumes, load balancers, networks, firewalls, and S3-compatible object storage.
* Talos Linuxas the operating system for cloud servers. Talos lets you manage Kubernetes nodes in a similar way to Kubernetes resources, by applying declarative configuration from which the OS figures out the actual changes (if any) to make on the node.
* CloudNativePGfills the role of a managed database service (e.g. RDS) for the cluster. PostgreSQL clusters can be declared in Kubernetes manifests alongside the workload(s) using them, and can be configured with scheduled backups, failover replicas, configuration overrides, etc.
* Ingress NGINX Controllerfills the role of a managed load balancer or API gateway for the cluster, consolidating and making available the ingress routes declared by workloads.
* ExternalDNSallows DNS names to be associated with ingress resources. Roughly, Ingress NGINX Controller manages HTTP routinginthe cluster while ExternalDNS handles routingtothe cluster.
* cert-managercreates TLS certificates to secure workload routes with HTTPS.

All infrastructure is codified usingTerraformandHelmwith deployments automated throughGitHub Actions.

## What a savings

It's not easy to do a strictly apples-to-apples comparison between cloud providers since they tend to differ in features (technical or contractual, e.g. SLAs), but an easy point of comparison is our monthly bill:

AWS and DigitalOcean*

$559.36

Hetzner

$132.96-76%

* Based on peak invoice amount. Technically DigitalOcean peaked in July ($109.86) before we started our migration. AWS peaked in August ($449.50) since we migrated tap later.

We get a lot more capacity for this price as well:

AWS and DigitalOcean

12vCPUs

24 GiBRAM

Hetzner*

44vCPUs+367%

88 GiBRAM+367%

* This is just the capacity available for workloads, with controlplanes excluded (an additional 6 vCPUs and 12 GiB RAM).

## Challenges

So much for the upsides, but the migration wasn't always straightforward. Our cloud estate is small in the grand scheme of things but inevitably there were challenges.

Hetzner's network zones are not equivalent to AWS' availability zones.

AWS's topology is based onregions and availability zones. Typically your infrastructure will live in a single region, but be split across availability zones for fault tolerance. Notably, private networking is region-wide (i.e. servers in different availability zones can easily communicate over private networks).

Hetzner's topology is based onlocations and network zones. There is only one EU network zone,eu-central, which has 3 locations. Since servers in different locations in the same network zone can communicate over private networks, we equivalated them to AWS' availability zones.

In reality, there is significant latency between Hetzner locations that make running multi-location workloads challenging, and potentially harmful to performance as we discovered through our post-deployment monitoring.

Instead, we opted to use a single location (Nuremberg) and useplacement groupsto improve resilience. Placement groups ensure that virtual servers in the same group run on different physical servers, significantly reducing the likelihood that they will fail together.

A service being docker-based doesn't mean it will be trivial to migrate.

On AWS we deployed our SaaS product, tap, to the Elastic Container Service (ECS) container runtime. This meant we were already building and push containers as part of the automated build and we had expected that migrating the rest of the configuration from ECS CloudFormation to Kubernetes manifests wouldn't be too laborious.

Unfortunately hadn't considered the deployment automation around the configuration. In particular, we had scripts to gather the right configuration from GitHub and pass it along to CloudFormation. The difficulty wasn't in adapting the scripts to Kubernetes, but rather that we hadn't anticipated the work and so that part of the migration took longer than we expected.

In the end we usedKustomizeas the glue between sensitive configuration in GitHub and our Kubernetes manifests. We moved our non-sensitive configuration out of GitHub settings and into config files in the repo itself since this works more easily with Kustomize. It also makes tracking and reviewing changes to these settings easier, so we are happy with the result.

## Conclusions

Hetzner is an incredibly cost-effective cloud provider. While their offerings are less expansive and hands-off than AWS or DigitalOcean's, it's possible to mitigate this with your stack if you don't mind getting your hands dirty.

We're particularly happy that this will allow us to keeptaprunning cheaply and performantly while we develop and launch it.
