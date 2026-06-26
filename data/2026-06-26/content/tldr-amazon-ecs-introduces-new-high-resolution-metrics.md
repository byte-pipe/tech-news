---
title: Amazon ECS introduces new high-resolution metrics for faster service auto scaling | AWS News Blog
url: https://aws.amazon.com/blogs/aws/amazon-ecs-introduces-new-high-resolution-metrics-for-faster-service-auto-scaling/
site_name: tldr
content_file: tldr-amazon-ecs-introduces-new-high-resolution-metrics
fetched_at: '2026-06-26T11:55:43.157363'
original_url: https://aws.amazon.com/blogs/aws/amazon-ecs-introduces-new-high-resolution-metrics-for-faster-service-auto-scaling/
date: '2026-06-26'
published_date: '2026-06-18T14:06:38-07:00'
description: Amazon ECS introduces new high-resolution metrics for faster service auto scaling (4 minute read)
tags:
- tldr
---

## AWS News Blog

# Amazon ECS introduces new high-resolution metrics for faster service auto scaling

Amazon Elastic Container Service (Amazon ECS) service auto scalingautomatically adjusts task counts to meet workload demand with comprehensive scaling policies, including predictive scaling for recurring traffic patterns, scheduled scaling for planned events, and target tracking to scale dynamically on real-time metrics.

You can choose proactive scaling by usingpredictive scaling(automatic) andscheduled scaling(customer-defined), or reactive scaling by usingtarget trackingwith just a target to scale on. Amazon ECS service auto scaling adjusts the number of tasks in an ECS service based onAmazon CloudWatchmetrics, such as average CPU/Memory usage, request count per target, a custom metric such as queue depth, or demand surges by using advanced machine learning (ML) algorithms.

With today’s launch, Amazon ECS service auto scaling now detects and responds to load changes faster with support for high resolution (20-second) metrics and metric publishing optimizations. In AWS benchmarking tests, time to trigger scale-out improved from 363 seconds to 86 seconds (76% faster, 4.2x), and total time to scale and provision new tasks improved from 386 seconds to 109 seconds (72% faster, 3.5x)

This launch delivers three key benefits for your applications:

* Improved performance and reliability: Faster scaling means, your application responds faster to demand surges, reducing latencies or failures for end users during demand surges.
* Right-size without compromise: Depending on the workload, you can reduce baseline task counts because scale-out now happens fast enough to handle traffic spikes without preemptive capacity padding. This directly reduces compute costs while maintaining application performance and availability.
* Simpler scaling configuration: Target tracking with high-resolution metrics delivers the aggressive scaling behavior that previously required custom scaling configurations, such as usage of step-scaling policies. One configuration change replaces custom engineering work.

How it worksTo use ECS faster service auto scaling, first enable high-resolution metrics for your ECS service, and then configure a target tracking scaling policy which uses high-resolution metrics. ECS faster service autoscaling works across all compute options on ECS:AWS Fargate,ECS Managed Instances, andAmazon Elastic Compute Cloud (Amazon EC2). You can enable these metrics when you create or update your ECS service in theAmazon ECS console, or usingAWS SDKs and tools, andAWS CloudFormation.

When you create a service in the console, add 20-seconds resolution metrics in theMonitoring configurationsection. These metrics incur additional CloudWatch costs while the standard resolution (60-seconds) is free.

In theService auto scalingsection, checkUse service auto scalingand chooseTarget Trackingfor the scaling policy type to use real-time data to scale the number of tasks that your service runs based on demand.

Then, choose aScaling policy typefor the target tracking. You can selectECSServiceAverageCPUUtilizationHighResolutionorECSServiceAverageMemoryUtilizationHighResolutionas new metrics.

That’s it. Your ECS service will use high resolution metrics for auto scaling.

To update an existing ECS service to use faster auto scaling, you first need to configure high resolution metrics viaUpdate Service. Once deployment completes, your service will generate high-resolution metrics. You can then go to theService and auto scalingtab from your service details to update scaling policy to use higher resolution metrics.

That’s all you need. Your ECS service now evaluates scaling decisions at 20-second intervals.

You can also use theAWS Command Line Interface (AWS CLI)to enable new metrics in your ECS service through Application Auto Scaling. To learn more, visit thefaster auto scaling documentation.

Now availableFaster service autoscaling with high-resolution metrics for Amazon ECS is available today. The feature itself has no additional cost, but high-resolution CloudWatch metrics introduce a new pricing dimension. For details, see theCloudWatch pricingpage.

Give it a try today and send feedback toAWS re:Post for ECSor through your usual AWS Support contacts.

—Channy