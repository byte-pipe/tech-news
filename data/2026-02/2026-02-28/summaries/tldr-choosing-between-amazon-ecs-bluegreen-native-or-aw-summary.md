---
title: Choosing between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK | AWS DevOps & Developer Productivity Blog
url: https://aws.amazon.com/blogs/devops/choosing-between-amazon-ecs-blue-green-native-or-aws-codedeploy-in-aws-cdk/
date: 2026-02-28
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-02-28T12:14:13.497244
---

# Choosing between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK | AWS DevOps & Developer Productivity Blog

# Choosing between Amazon ECS Blue/Green Native or AWS CodeDeploy in AWS CDK

## Background
- Blue/green deployments on Amazon ECS have been used for zero‑downtime releases.
- Historically, CDK projects wired ECS to AWS CodeDeploy for traffic shifting, lifecycle hooks, and integration with CodePipeline.
- In July 2025 Amazon ECS introduced built‑in blue/green deployment, removing the need for a separate CodeDeploy service.

## What the ECS‑native blue/green model adds
- Lifecycle hooks, bake time, and managed rollback are now handled directly by the ECS service.
- Deployment configuration is consolidated into a single service, reducing pipeline complexity and the number of moving parts.
- The model creates a replacement task set attached to a separate target group; an all‑at‑once traffic shift moves traffic to the green revision, followed by a configurable bake period before retiring or rolling back.

## Two CDK paths
- **ECS‑native blue/green**
  - Configured via the CDK ECS module and related load balancer resources.
  - Supports lifecycle hooks (Lambda), bake time, optional test listener or Service Connect header rules.
  - Traffic shift is immediate (all‑at‑once) with a post‑shift bake period.
- **CodeDeploy blue/green**
  - Creates a CodeDeploy application and deployment group bound to the ECS service and ALB.
  - Offers canary, linear, or all‑at‑once traffic shifting policies.
  - Typically integrated with CodePipeline for multi‑stage orchestration and cross‑region/account workflows.

## Decision guide
- Choose **CodeDeploy** when you need:
  - Progressive traffic exposure (e.g., 5 % increments).
  - Complex multi‑stage pipelines, cross‑service coordination, or formal governance.
  - Detailed audit trails and metric‑driven promotions.
- Choose **ECS‑native** when you prefer:
  - Simpler, service‑centric deployment with fewer components.
  - Immediate cutover with configurable bake time and automatic rollback.
  - Consolidated operational footprint and built‑in circuit breaker.

## Implementing ECS‑native blue/green in CDK
- Define an ECS service (Fargate or EC2) with an ALB and two target groups.
- Opt into `DeploymentStrategy.BLUE_GREEN`.
- Set `bakeTime`, `deploymentAlarms`, and `lifecycleHooks` (e.g., Lambda functions for pre‑traffic or post‑traffic actions).
- Example snippet:

```ts
const service = new ecs.FargateService(this, "Service", {
  cluster,
  taskDefinition,
  desiredCount: 3,
  securityGroups: [serviceSG],
  vpcSubnets: { subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS },
  deploymentStrategy: ecs.DeploymentStrategy.BLUE_GREEN,
  bakeTime: Duration.minutes(30),
  propagateTags: ecs.PropagatedTagSource.SERVICE,
  deploymentAlarms: {
    alarmNames: [
      `${this.stackName}-Http-500-Blue`,
      `${this.stackName}-Http-500-Green`,
      `Synthetics-Alarm-trivia-game-${props.stage}`,
    ],
    behavior: ecs.AlarmBehavior.ROLLBACK_ON_ALARM,
  },
  lifecycleHooks: [
    new ecs.DeploymentLifecycleLambdaTarget(preTrafficHook, "PreTrafficHook", {
      lifecycleStages: [ecs.DeploymentLifecycleStage.POST_TEST_TRAFFIC_SHIFT],
    }),
  ],
  minHealthyPercent: 100,
  maxHealthyPercent: 200,
});
```

## Conclusion
- ECS‑native blue/green deployments are now the recommended default for most teams, offering zero‑downtime cutovers, lifecycle hooks, bake time, and automatic rollback without an extra service.
- Opt for CodeDeploy only when advanced traffic‑shifting strategies (canary/linear) or extensive CodePipeline integrations are required.
- Follow the migration guide for step‑by‑step instructions to move existing CodeDeploy setups to the ECS‑native model.
