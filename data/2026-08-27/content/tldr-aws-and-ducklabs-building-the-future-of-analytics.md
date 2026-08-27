---
title: 'AWS and DuckLabs: Building the future of analytics together | AWS Big Data Blog'
url: https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/
site_name: tldr
content_file: tldr-aws-and-ducklabs-building-the-future-of-analytics
fetched_at: '2026-08-27T20:57:34.952448'
original_url: https://aws.amazon.com/blogs/big-data/aws-and-ducklabs-building-the-future-of-analytics-together/
date: '2026-08-27'
published_date: '2026-08-26T06:28:34-07:00'
description: AWS moves to acquire the company behind DuckDB (3 minute read)
tags:
- tldr
---

## AWS Big Data Blog

# AWS and DuckLabs: Building the future of analytics together

Today we are announcing thatAmazon has signed a definitive agreement to acquire DuckLabs, the Amsterdam-based company behind the open-source analytical database DuckDB. We expect the transaction to close shortly, subject to customary closing conditions. Hannes Mühleisen and Mark Raasveldt, who created DuckDB and co-founded DuckLabs, will continue leading the team and the open-source project’s technical direction as part of AWS. The DuckDB open-source project will also continue to be driven by the DuckLabs team, remain open source under the independent Foundation (the non-profit that oversees DuckDB), and available under the MIT license as it does today (seeDuckLabs blog).

Data has always been a core asset and differentiator for companies. That is true now more than ever, as organizations use their data to customize inference and build AI agents. For 20 years AWS has driven the frontier of data, starting with the launch of Amazon S3 to create data lakes for every business, the first cloud analytics service in Amazon EMR, the first cloud data warehouse with Amazon Redshift and the many capabilities that we have introduced with Athena, Glue ETL, etc. We continue innovating for AWS customers on the data frontier including providing Apache Iceberg capabilities directly in S3 Tables, vector storage in the data lake and our new optimized Graviton-based Redshift clusters.

DuckDB has also been at the forefront of changing how the world works with data. Hannes and Mark started DuckDB while at Centrum Wiskunde & Informatica (CWI), the national research institute in the Netherlands that also invented Python. The founders of DuckDB realized that older databases and analytics engines like Spark focused on performance for very large data processing but didn’t have an effective way to “scale down” to smaller size data queries that form the backbone of what most customers do with SQL analytics.

DuckDB set out to solve the problem of blazingly fast performance for the 90%+ of data queries in the world today, that often runs 1 terabyte of data or less as part of analysis and dashboarding. DuckDB’s architecture is based on that core premise of “make the everyday SQL query super fast” so DuckDB runs in-process to other applications which simplifies and speeds up data exchange with the application. DuckDB gets big performance gains from its vectorized execution because it does not require a heavy compiler to run simple statements likeSELECT * FROM table. And what works for everyday queries also (unsurprisingly) works very well for agents because agents behave a lot like people when interacting with data. They poke. They experiment. They run exploratory analysis on small data sets before figuring out what they really want to do. DuckDB ends up being naturally optimized for AI agents to use. What started as an academic project is now widely adopted across data engineering, data science, analytics, and now AI agents, for its simplicity of use and raw performance. We plan to combine the superpower of DuckDB at everyday queries of a terabyte or less with the proven exabyte-plus enterprise scale of S3 and our AWS analytics services of Redshift, Athena, EMR, Glue-ETL, and SageMaker platform which power analytics across hundreds of terabytes to petabytes of data. Andy Warfield, Distinguished Engineer at AWS, talks aboutDuckDB and the Changing Physics of Analyticsin Werner Vogel’s All Things Distributed blog.

Our customers use DuckDB today with AWS services and tell us how much they love it for its speed and simplicity. For example, DuckDB today executes SQL directly against external files, such as Parquet, CSV, and JSON, stored locally or on cloud storage like S3 for unparalleled performance and significantly lower cost.

David Feng, Executive Director, Scientific Computing at Allen Institute, said“The Allen Institute accelerates science for a healthier world by tackling the biggest questions in biology at a large scale, and that involves extensive analysis of large, multimodal data. We started using DuckDB to analyze terabytes of scientific data in 2025 and love it. We are storing data in S3 for realtime quality control and analysis of neurophysiology and behavior data, critical to driving the next data acquisition. Queries that took minutes now come back in less than a second, enabling completely new ways of interacting with data.” DuckDB can also run in-process to AWS Lambda functions.

We are excited to make DuckDB applications run best on AWS, and will continue to invest in deep integration between DuckDB and our building block services.

We are also using DuckDB in our own AWS infrastructure. When Amazon Quick wanted to augment the performance of their custom dashboarding engine, they picked DuckDB to query data in S3 Tables. The Quick team found that the DuckDB engine scales effortlessly with the number of CPUs, and its single library can easily plug into the internal Quick control plane subsystems. Since we launched Quick in October 2025, we have processed over 2.5B queries using our custom Quick query engine with the DuckDB integrations and optimizations. These DuckDB integrations and optimizations helped Amazon Quick reduce average query latency by 30%. We are going to look at how we can integrate DuckDB’s performance and simplicity in our other AWS services across data and analytics.

Stay tuned for more about how DuckLabs and AWS will reinvent the frontier of data together for applications, data engineers, and AI, meeting customers where they are today and giving them the benefits of DuckDB’s innovation within AWS.

## About the author