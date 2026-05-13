---
title: Amazon Redshift introduces AWS Graviton-based RG instances with an integrated data lake query engine | AWS News Blog
url: https://aws.amazon.com/blogs/aws/amazon-redshift-introduces-aws-graviton-based-rg-instances-with-an-integrated-data-lake-query-engine/
site_name: tldr
content_file: tldr-amazon-redshift-introduces-aws-graviton-based-rg-i
fetched_at: '2026-05-13T19:36:47.257002'
original_url: https://aws.amazon.com/blogs/aws/amazon-redshift-introduces-aws-graviton-based-rg-instances-with-an-integrated-data-lake-query-engine/
date: '2026-05-13'
published_date: '2026-05-12T09:05:12-07:00'
description: Amazon Redshift introduces AWS Graviton-based RG instances with an integrated data lake query engine (3 minute read)
tags:
- tldr
---

## AWS News Blog

# Amazon Redshift introduces AWS Graviton-based RG instances with an integrated data lake query engine

Since 2013,Amazon Redshifthas given the full power of a data warehouse in the cloud, at a fraction of the on-premises cost. Every architectural generation—from dense compute toAmazon RA3 instances, from provisioned toAmazon Redshift Serverless—has made each query cheaper, faster, and more efficient than the last.

For over a decade, as data volumes have grown and analytics requirements have evolved, organizations increasingly leverage both data warehouse tables for structured, frequently-accessed data and data lakes for cost-effective storage of diverse datasets. Add AI agents to the mix and they query your data warehouse at a scale that dwarfs typical human usage, leading to spiraling operational costs.

Amazon Redshift has doubled down on its core strengths to meet the demands of any workload — whether driven by humans or AI agents. For example, in March 2026, Amazon Redshift improved the performance of business intelligence (BI) dashboards and ETL workloads byspeeding up new queries by up to 7 times. This significantly improves the response times of low-latency SQL queries, such as those used in near-real-time analytics applications, BI dashboards, ETL pipelines, and autonomous, goal-seeking AI agents.

Today, we’re announcingAmazon Redshift RG instances, a new instance family powered byAWS Graviton. RG instances deliver better performance, running data warehouse workloads up to 2.2x as fast as RA3 instances at 30% lower price per vCPU. Their integrated data lake query engine lets you run SQL analytics across your data warehouse and data lake from a single engine with performance up to 2.4x as fast as RA3 forApache Icebergand up to 1.5x as fast as RA3 forApache Parquet. This blend of speed, cost efficiency, and an integrated data lake query engine makes Redshift RG instances well-suited to handle the high query volumes and low-latency requirements of today’s analytics and agentic AI workloads.

You can compare new RG instances and current RA3 instances:

Current RA3 Instance

Recommended RG instance

vCPU

Memory (GB)

Primary Use Case

ra3.xlplus

rg.xlarge

4

32

Small cluster departmental analytics

ra3.4xlarge

rg.4xlarge

12 → 16 (1.33:1)

96 GB → 128 GB (1.33:1)

Standard production workloads, medium data volumes

This approach reduces total analytics costs for customers running combined data warehouse and data lake workloads, while simplifying operations through a single system for querying both warehouse tables andAmazon Simple Storage Service (Amazon S3)data lakes. We recommend using theAWS Pricing Calculatorwith your specific workload patterns to estimate savings.

Getting started with Amazon Redshift RG instancesYou can launch new clusters or migrate existing clusters through theAWS Management Console,AWS Command Line Interface (AWS CLI),or AWS API. The integrated data lake query engine is enabled by default.

In the Amazon Redshift console, you can choose new RG instances when you create a cluster.

You can migrate previous-generation instances to RG instances with optimal paths based on your cluster configuration to estimate costs, validate compatibility, and automate execution.

* Elastic Resize—in-place migration with 10-15 minutes downtime for compatible configurations
* Snapshot and Restore—create a RG cluster from an RA3 snapshot. This is best for customers who want to make configuration changes during the migration

Your external tables, schemas, and query syntax—including existing Spectrum queries—remain unchanged. There is no need to recreate external tables or modify application code. To learn more, visit theRedshift Management Guide.

Amazon Redshift now executes data lake queries on cluster nodes—the same compute that processes data warehouse workloads. As a result,Amazon Redshift Spectrumis no longer required. Data lake queries stay within your VPC boundary, use existing IAM roles, and incur zero per-terabyte scanning charges. This removes the $5/TB Spectrum scanning fees that previously added to total Redshift costs.

Now availableAmazon Redshift RG instances are now available in the following AWS Regions: US East (N. Virginia, Ohio), US West (N. California, Oregon), Asia Pacific (Hong Kong, Hyderabad, Jakarta, Malaysia, Melbourne, Mumbai, Osaka, Seoul, Singapore, Sydney, Taiwan, Tokyo), Canada (Central), Europe (Frankfurt, Ireland, Milan, London, Paris, Spain, Stockholm), and South America (São Paulo). For Regional availability and a future roadmap, visit theAWS Capabilities by Region. For Redshift Provisioned, you can select On-Demand Instances with hourly billing and no commitments or choose Reserved Instances for cost savings. To learn more, visit theAmazon Redshift Pricing page.

Give RG instances a try in theRedshift consoleand send feedback toAWS re:Post for Amazon Redshiftor through your usual AWS Support contacts.

—Channy

 

Updated 5/12/26: Middle East (UAE) removed from available regions.