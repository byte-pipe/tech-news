---
title: Digital Society | Posts | Migrating to Hetzner
url: https://digitalsociety.coop/posts/migrating-to-hetzner-cloud/
date: 2025-10-17
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-18T11:21:57.648276
screenshot: hackernews_api-digital-society-posts-migrating-to-hetzner.png
---

# Digital Society | Posts | Migrating to Hetzner

## Migrating from DigitalOcean to Hetzner: 76% Savings in Cloud Bills

We saved 76% on our cloud bills while migrating the development team's workload to Hetzner from AWS and DigitalOcean. This migration aimed to optimize the team's infrastructure needs and reduce operational costs.

### Background

* The project uses both AWS core hosting (as DNS and email services) and SaaS product tap, hosted on various AWS services.
* Prior to migration, we relied heavily on AWS for familiarity since it has been our preferred choice for nearly 15 years. However, tap became a data-intensive SaaS that required higher resources.

### Decision Factors

* Favoring reliability due to API stability concerns
* Automation of infrastructure management and desire for minimal manual effort
* Preferencing managed Kubernetes (DigitalOcean Kubernettes) over self-managed options like AWS ECS and RDS
* Initial use of DigitalOcean but later discovered that tapping into an AWS credit package could allow experimentation without costly upfront expenses

### Migration to Hetzner

* Initially used only DigitalOcean, leveraging the generous $1,000 AWS startup credit for data-intensive projects.
* Explored using AWS Fargate container runtime to manage scale according to usage needs.

### Performance and Costs

* Tap's performance requirements necessitated a high resource utilization (2x CPUs, 4 GiB RAM) which resulted in higher costs on AWS ($70/month per environment).
* Total costs for two environments increased to $4, underscoring the need for optimized infrastructure management.
* Aided by familiarity with the AWS ecosystem and automation of many tasks, the team successfully migrated their workload without substantial disruptions.
