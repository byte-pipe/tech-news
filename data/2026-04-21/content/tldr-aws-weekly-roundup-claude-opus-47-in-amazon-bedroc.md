---
title: 'AWS Weekly Roundup: Claude Opus 4.7 in Amazon Bedrock, AWS Interconnect GA, and more (April 20, 2026) | AWS News Blog'
url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-opus-4-7-in-amazon-bedrock-aws-interconnect-ga-and-more-april-20-2026
site_name: tldr
content_file: tldr-aws-weekly-roundup-claude-opus-47-in-amazon-bedroc
fetched_at: '2026-04-21T20:02:35.116021'
original_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-claude-opus-4-7-in-amazon-bedrock-aws-interconnect-ga-and-more-april-20-2026
date: '2026-04-21'
published_date: '2026-04-20T08:53:21-07:00'
description: AWS Pushes Bedrock Forward (2 minute read)
tags:
- tldr
---

## AWS News Blog

# AWS Weekly Roundup: Claude Opus 4.7 in Amazon Bedrock, AWS Interconnect GA, and more (April 20, 2026)

Last week I had the honor of delivering a commencement speech at theUniversity of Namur(uNamur) for their 2025 graduation ceremony.

Standing in front of freshly minted computer science graduates, I talked about the future of software development in the age of AI. My message to them was simple: AI will not make you obsolete. We’ve seen tools evolve over the decades, from punch cards to IDEs to AI-assisted coding, but the work remains yours, not the tool’s. The developers who will thrive are those who stay curious, think in systems, communicate with precision, and take ownership of what they build. The world needsmorepeople with coding skills, not fewer. AI raises the bar on what we can accomplish, and that’s a good thing.

Now, let’s get into this week’s AWS news.

HeadlinesAnthropic’s Claude Opus 4.7 is now available in Amazon Bedrock– Anthropic’s most intelligent Opus model is now available in Amazon Bedrock, with improved performance across coding, long-running agents, and professional knowledge work. Claude Opus 4.7 scores 64.3% on SWE-bench Pro and 87.6% on SWE-bench Verified, extending its lead in agentic coding with stronger long-horizon autonomy and complex code reasoning. It also does better on knowledge work tasks like document creation, financial analysis, and multi-step research.

The model runs on Bedrock’s next-generation inference engine with dynamic capacity allocation, adaptive thinking (letting Claude allocate thinking token budgets based on request complexity), and the full 1M token context window. It also adds high-resolution image support for better accuracy on charts, dense documents, and screen UIs. Claude Opus 4.7 is available at launch in US East (N. Virginia), Asia Pacific (Tokyo), Europe (Ireland), and Europe (Stockholm), with up to 10,000 requests per minute per account per Region.

AWS Interconnect is now generally available with a new option to simplify last-mile connectivity– AWS Interconnect brings two managed private connectivity capabilities to general availability. The first,AWS Interconnect – Multicloud, provides Layer 3 private connections between AWS VPCs and other cloud providers (Google Cloud available now, Azure and OCI coming later in 2026). Traffic flows over the AWS global backbone and the partner cloud’s private network, never over the public internet, with built-in MACsec encryption, multi-facility resiliency, and CloudWatch monitoring. AWS published the underlying specification on GitHub under Apache 2.0 so any cloud provider can become an Interconnect partner.

The second capability,AWS Interconnect – Last Mile, simplifies high-speed private connections from branch offices, data centers, and remote locations to AWS through existing network providers. It provisions 4 redundant connections across 2 physical locations automatically, configures BGP routing, activates MACsec encryption and Jumbo Frames by default, and offers bandwidth from 1 Gbps to 100 Gbps adjustable from the console without reprovisioning. Last Mile launches in US East (N. Virginia) with Lumen as the initial partner.

Last week’s launchesHere are some launches and updates from this past week that caught my attention:

* Amazon ECR pull through cache now supports referrer discovery and sync— ECR’s pull through cache now automatically discovers and syncs OCI referrers (image signatures, SBOMs, attestations) from upstream registries into your private repositories. This means end-to-end image signature verification and SBOM discovery workflows work without client-side workarounds.
* AWS Transform is now available in Kiro and VS Code— AWS Transform, the agentic migration and modernization factory, is now accessible via Kiro (as a Power) and VS Code (as an extension). You can run custom transformations for common patterns like Java/Python/Node.js version upgrades and AWS SDK migrations directly from your IDE, with job state shared across the web console, CLI, and IDE.
* Aurora DSQL launches connector for PHP— A new Aurora DSQL Connector for PHP (PDO_PGSQL) simplifies building PHP applications on Aurora DSQL by automatically generating IAM tokens, handling SSL configuration, managing connection pooling, and providing opt-in optimistic concurrency control retry with exponential backoff.
* Amazon Q supports document-level access controls for Google Drive— Amazon Q now enforces document-level access controls for Google Drive knowledge bases, combining indexed ACL replication for fast pre-retrieval filtering with real-time permission checks against Google Drive at query time.
* AWS Secrets Manager now supports hybrid post-quantum TLS— Secrets Manager now supports hybrid post-quantum key exchange using ML-KEM to protect secrets against both current and future quantum computing threats. This is automatically enabled in Secrets Manager Agent 2.0.0+, Lambda Extension v19+, and the CSI Driver 2.0.0+.
* Amazon EC2 C8in and C8ib instances are now generally available— Powered by custom 6th-gen Intel Xeon Scalable processors and 6th-gen AWS Nitro cards, these instances deliver up to 43% higher performance over C6in. C8in offers 600 Gbps network bandwidth (highest among enhanced networking EC2 instances), while C8ib delivers up to 300 Gbps EBS bandwidth (highest among non-accelerated compute instances), scaling up to 384 vCPUs.

For a full list of AWS announcements, be sure to keep an eye on theWhat’s New with AWSpage.

Other AWS newsHere are some additional posts and resources that you might find interesting:

* Navigating enterprise networking challenges with Amazon EKS Auto Mode— This post explains how EKS Auto Mode automates Kubernetes networking infrastructure including VPC CNI configuration, load balancer provisioning, and DNS management, reducing operational overhead while preserving enterprise security controls.
* Introducing granular cost attribution for Amazon Bedrock— My colleague Micah talked about this feature last week already, but the blog post came out after last week’s roundup. Amazon Bedrock now automatically attributes inference costs to the specific IAM principal that made each API call, with results flowing into AWS Cost and Usage Reports (CUR 2.0). You can aggregate costs by team, project, or cost center using IAM principal tags and session tags.
* Accelerate development workflows with Amazon EBS Volume Clones— EBS Volume Clones let you create instant, point-in-time copies of EBS volumes that are immediately usable without waiting for data transfer. The post highlights use cases including dev/test environment refreshes, disaster recovery testing, and CI/CD pipeline acceleration.
* Modernize VB6 applications at scale with AWS Transform Custom— A walkthrough of using AWS Transform Custom’s agentic AI capabilities to convert legacy Visual Basic 6.0 applications to modern C# ASP.NET Core web applications, addressing challenges like COM dependencies, ADO-to-Entity Framework migration, and VB6 forms-to-Blazor UI conversion.
* Migrating and decomposing APIs with zero-downtime using CloudFront— A zero-downtime API migration strategy using CloudFront Functions with CloudFront KeyValueStore for intelligent, user-aware traffic routing based on the Strangler Fig pattern. This is similar to whatAWS Migration Hub Refactor Spacesoffers, but implemented with just CloudFront and edge functions.

Upcoming AWS eventsCheck your calendar and sign up for upcoming AWS events:

* AWS Events— Browse upcoming AWS-led in-person and virtual events, startup events, and developer-focused events near you.
* AWS Power Hour— Weekly live training sessions on Twitch covering various AWS topics.
* Community.aws— Find community-led events, meetups, and user groups in your area.

That’s all for this week. Check back next Monday for another Weekly Roundup!

— seb