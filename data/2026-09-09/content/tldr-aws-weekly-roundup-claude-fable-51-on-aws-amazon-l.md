---
title: 'AWS Weekly Roundup: Claude Fable 5.1 on AWS, Amazon Linux 2027 preview, AWS Certified AI Business Strategist, and more (September 7, 2026) | AWS News Blog'
url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-fable-5-1-on-aws-amazon-linux-2027-preview-aws-certified-ai-business-strategist-and-more-september-7-2026/
site_name: tldr
content_file: tldr-aws-weekly-roundup-claude-fable-51-on-aws-amazon-l
fetched_at: '2026-09-09T15:29:59.022453'
original_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-fable-5-1-on-aws-amazon-linux-2027-preview-aws-certified-ai-business-strategist-and-more-september-7-2026/
date: '2026-09-09'
published_date: '2026-09-07T07:24:08-07:00'
description: Claude Fable 5.1 on AWS comes with new data controls (5 minute read)
tags:
- tldr
---

## AWS News Blog

# AWS Weekly Roundup: Claude Fable 5.1 on AWS, Amazon Linux 2027 preview, AWS Certified AI Business Strategist, and more (September 7, 2026)

Last week,Claude Fable 5.1 became available on AWS. According to Anthropic, Claude Fable 5.1 delivers frontier intelligence for ambitious tasks across coding, scientific research, and enterprise workflows. Claude Fable 5.1 is built for long-running, high-stakes work that runs for hours and spans many applications. It can own more of a software project on its own, handling features across an entire codebase, code review, and performance work over extended sessions.

Anthropic has designated Fable 5.1 aCovered Model, a category of Claude models that carry additional data retention, safety review, and access policies wherever they’re offered. Claude Fable 5.1 is subject to data retention for up to 30 days and human review by Amazon personnel, with a newaws_reviewdata retention mode. In this mode, AWS retains your prompts and outputs for human safety review within the AWS boundary. Theprovider_data_sharemode is legacy, and Amazon Bedrock does not share your data with the model provider. In addition,Enterprise Frontier Safeguards (EFS), built in partnership between AWS and Anthropic, will let eligible customers use Covered Models while keeping their data in a cloud environment they control.

You have two ways to access Claude Fable 5.1: Amazon Bedrock and Claude Platform on AWS. To learn more, see theClaude Fable 5.1 model card on Amazon BedrockandClaude Platform on AWS.

Last week’s launchesHere are some launches that got my attention:

* Amazon Linux 2027 (AL2027) in public preview: AL2027 is the next version of the Amazon Linux operating system. It runs on kernel 7.1+, purpose-built for cloud-native workloads on AWS with performance, scale, and security in mind. Built on AL2023’s baseline, AL2027 is designed for customers who need a secure, stable, and AWS-native operating system running web applications, databases, containerized microservices, AI/ML workloads, and large-scale infrastructure.
* Amazon EC2 R9g and R9gd memory-optimized instances: These instances are powered by AWS Graviton5 processors, delivering the best price performance for memory-intensive workloads running on Amazon EC2. R9g and R9gd instances deliver up to 25% better compute performance compared to AWS Graviton4-based R8g and R8gd instances. They are up to 30% faster for databases, up to 35% faster for web applications, and up to 35% faster for machine learning. To learn more, readDaniel’s blog post.
* AWS Lambda SnapStart for container image functions: Lambda SnapStart is an opt-in capability that makes it easier for you to build highly responsive and scalable applications without provisioning resources or implementing complex performance optimizations. Previously, SnapStart was only supported for managed runtimes (Python, .NET, and Java). You can now use SnapStart for container images to reduce startup times from several seconds to as low as sub-second for latency-sensitive workloads such as ML inference and interactive APIs.
* AWS Agent Registry now generally available: AWS Agent Registry provides a private, governed catalog and discovery layer for agents, tools, skills, MCP servers, and custom resources within your organization. In addition to the capabilities launched in preview (manual and URL-based record creation, approval workflows, semantic and keyword search, and AWS CloudTrail audit trails), Registry now adds new enterprise features. To learn more, visit theAI Blog post.
* Amazon Redshift now supports Apache Iceberg v3 tables: You can read from and write to Apache Iceberg v3 tables in your data lake of Amazon Redshift. With this launch, Amazon Redshift introduces support for default column values, row lineage, and deletion vectors. Amazon Redshift’s Graviton based provisioned and serverless clusters support the new v3 format. To learn more, visitApache Iceberg v3 features in Redshift.

For a full list of AWS announcements, be sure to keep an eye on theWhat’s New with AWSpage.

Other AWS newsHere are some additional projects and news items you may find interesting:

* AWS named a Leader in the 2026 Gartner Magic Quadrant for Strategic Cloud Platform Services: For the 16th consecutive year, Gartner has recognized AWS as a Leader in the 2026 Gartner Magic Quadrant for Strategic Cloud Platform Services, and once again placed AWS highest on the Ability to Execute axis. We believe this recognition reflects our commitment to delivering the broadest and deepest set of cloud capabilities from infrastructure and AI to security and operations, so you can build, innovate, and scale with confidence.
* AWS Certified AI Business Strategist: This new certification targets professionals who evaluate, champion, and scale AI initiatives in their organizations: line-of-business leaders driving adoption across their teams, sales professionals articulating AI value to customers, consultants guiding client strategy from experimentation through production, program managers aligning AI investments to business outcomes. Beta exam registration opened September 1, 2026, with exam delivery beginning September 29.
* Agentic Security: Detection and Response at Machine Speed: We believe security should evolve ahead of AI adoption, not behind it. That belief drove our team to collaborate with the SANS Institute on a new chapter in the 2026 Cloud Security Exchange eBook, where we lay out a practical framework for securing agentic workloads at enterprise scale. Our chapter goes deeper on securing agentic workloads, with specific architectural patterns, implementation guidance, and frameworks for security teams at every stage of agentic AI maturity, whether you’re evaluating, piloting, or operating at scale.

For a full list of AWS blog posts, be sure to keep an eye on theAWS Blogspage.

Learn more about AWS, browse and join upcomingAWS-led in-person and virtual events,startup events, anddeveloper-focused eventsincludingAWS re:Invent,AWS Summits, andAWS Community Days. Join theAWS Builder Centerto connect with builders, share solutions, and access content that supports your development.

That is all for this week. Check back next Monday for another Weekly Roundup!

—Channy