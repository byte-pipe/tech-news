---
title: Choosing between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK | AWS DevOps & Developer Productivity Blog
url: https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/
site_name: tldr
content_file: tldr-choosing-between-amazon-ecs-bluegreen-native-or-aw
fetched_at: '2026-02-28T12:13:34.157820'
original_url: https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/
date: '2026-02-28'
published_date: '2026-02-11T11:59:00-07:00'
description: Choosing between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK (7 minute read)
tags:
- tldr
---

## AWS DevOps & Developer Productivity Blog

# Choosing between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK

Blue/green deployments onAmazon Elastic Container Service (Amazon ECS)have long been a go-to pattern for shipping zero-downtime deployments. Historically, the recommended approach in theAWS Cloud Development Kit (AWS CDK)was to wire ECS toAWS CodeDeployfor traffic shifting, lifecycle hooks, and tight integration with AWS CodePipeline.

In July 2025, Amazon ECS launched built-in blue/green deployments. This allows you to operate directly within the ECS service, without requiring the use of Amazon CodeDeploy.

This post explains what changed, how the new ECS-native blue/green model compares to CodeDeploy, and how to decide which path to take in your CDK projects.

Figure1: Amazon ECS blue/green deployment with AWS CodeDeploy

## Why blue/green on ECS, and what was launched in July 2025

In a blue/green deployment, two production environments are maintained: blue, the current environment, and green, the new environment. This strategy allows you to validate the new version of your environment before it receives production traffic.

The ECS service team saw an opportunity to simplify the deployment process by creating lifecycle hooks, bake time, and managed rollback directly within ECS. With this shift, the complexity of coordinating blue/green deployments through CodeDeploy is consolidated into a single service. This consolidation not only simplifies the deployment pipeline but also reduces the number of moving parts, making it easier to maintain and troubleshoot over time.

Conceptually, ECS-native blue/green provisions a replacement task set registered to a separate target group (blue target group in figure 2) behind your Elastic Load Balancing listener. When you approve the cutover, ECS performs an all-at-once traffic shift to the green revision (green target group in figure 2), then holds both revisions during a configurable bake period before retiring blue or rolling back if alarms or hooks fail.

Figure 2: Amazon ECS Native Blue Green Deployment

Unlike CodeDeploy, which requires fine-grained configuration of traffic shifting strategies, ECS native deployments are intentionally simpler, designed to cover the most common blue/green use cases without the operational overhead of managing a multi-phase canary.

## Two paths in CDK: ECS-native blue/green vs. CodeDeploy blue/green

With CDK, you now have two ways to achieve blue/green on ECS. One is the ECS-native path that keeps deployment configuration on theCDK ECS moduleand its related load balancer resources. You configure lifecycle hooks that invoke AWS Lambda functions at specific deployment stages, you set a bake time, and you optionally use a test listener or Amazon ECS Service Connect header rules to validate traffic to the green revision before production cutover. The CodeDeploy path creates a CodeDeploy application and deployment group bound to your ECS service and Application Load Balancer (ALB), lets you choose canary, linear, or all-at-once policies, and typically plugs into AWS CodePipeline for orchestration.

A key functional difference is how the traffic shifts. ECS-native blue/green performs an immediate all-at-once switch to green, followed by a bake period; CodeDeploy supports canary and linear shifting in addition to all-at-once. If you require progressive exposure by percentage, CodeDeploy remains the way to go. If you want a simpler, service-centric model with fewer moving parts, ECS-native is now the default choice.

Currently, the AWS CDK includes L2 support for ECS-native blue/green so that you can model these settings directly without custom CloudFormation or escape hatches. If your stack already uses the Deployment Controller Type. CODE_DEPLOY path, you can continue to do so; migration options exist (outlined later in this post).

Figure 3: Amazon CodeDeploy blue/green deployment traffic shift

## Decision guide: choosing the right path

AWS CodeDeploy offers more refined functionality for managing deployments through its integration with AWS CodePipeline to support multi-stage workflows across services, regions, and accounts, and provides a clear audit trail for change management. AWS CodeDeploy offers policies that can shift traffic in defined increments (for example, 5% or 10%) with automated metric checks and optional approvals. This deployment pattern supports coordinating multiple environments with formal governance, or teams that want data-driven promotions based on alarms and checkpoints. Because of its integration with AWS CodePipeline, you can have several stages for different services for ECS Blue/Green (CodeDeploy) and coordinate the deployment of multiple dependent services in a single release.

Utilize ECS-native to achieve a compact operational footprint by consolidating deployments and operations into a single service. The ECS service supports zero-downtime deployments through Blue/Green deployment (shifting the traffic all at one time) and enables quick rollbacks with configurable settings forminimumHealthyPercentandmaximumPercent. Application Load Balancer (ALB) draining and task health checks ensure a balance between speed and safety. Additionally, the built-in deployment circuit breaker automatically halts and reverts problematic rollouts, minimizing operational issues.

## How to implement in ECS native in CDK

To utilize ECS-native blue/green in CDK, start with an Amazon ECS service (Fargate or EC2), an Application Load Balancer, and two target groups managed by ECS during deployments. In your service definition, you’ll opt into the blue/green deployment type, set a bake time, and attach lifecycle hooks. Hooks can run Lambda functions at stages such as before scale-up or after production traffic shift, letting you run synthetic tests, warm caches, or gate on external checks. If you’re using Amazon ECS Service Connect, you can route “dark” test traffic to green by sending requests with a specific header during the pre-cutover phase.

const service = new ecs.FargateService(this, "Service", {
 cluster,
 taskDefinition,
 desiredCount: 3,
 securityGroups: [serviceSG],
 vpcSubnets: {
 subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
 },
 deploymentStrategy: ecs.DeploymentStrategy.BLUE_GREEN,
 bakeTime: Duration.minutes(30),
 propagateTags: ecs.PropagatedTagSource.SERVICE,
 deploymentAlarms: {
 alarmNames: [
 this.stackName + "-Http-500-Blue",
 this.stackName + "-Http-500-Green",
 "Synthetics-Alarm-trivia-game-" + props.stage,
 ],
 behavior: ecs.AlarmBehavior.ROLLBACK_ON_ALARM,
 },
 lifecycleHooks: [
 new ecs.DeploymentLifecycleLambdaTarget(
 preTrafficHook,
 "PreTrafficHook",
 {
 lifecycleStages: [
 ecs.DeploymentLifecycleStage.POST_TEST_TRAFFIC_SHIFT,
 ],
 }
 ),
 ],
 minHealthyPercent: 100,
 maxHealthyPercent: 200,
 });

Code Snipped: Amazon ECS service with AWS Fargate and AWS CodeDeploy

## Conclusion

Using ECS-native blue/green deployments is now the recommended default for most teams. This approach provides zero-downtime cutovers, lifecycle hooks, bake time, and rollback capabilities without requiring the management of an additional service.

Choose CodeDeploy only if you need advanced traffic shifting options, such as canary or linear deployments, or if you have other dependencies with AWS CodePipeline workflows.

Bring your ECS deployments to the next level by enabling Blue/Green deployment with the strategy that best fits for your use case. For step-by-step instructions for migrating from CodeDeploy to ECS-Native refer to thismigration guide.
