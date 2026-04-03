---
title: AWS CloudFormation 2025 Year In Review | AWS DevOps & Developer Productivity Blog
url: https://aws.amazon.com/blogs/devops/aws-cloudformation-2025-year-in-review/
site_name: tldr
content_file: tldr-aws-cloudformation-2025-year-in-review-aws-devops
fetched_at: '2026-02-10T11:23:47.336052'
original_url: https://aws.amazon.com/blogs/devops/aws-cloudformation-2025-year-in-review/
date: '2026-02-10'
published_date: '2026-01-27T18:08:08-07:00'
description: AWS CloudFormation 2025 Year In Review (5 minute read)
tags:
- tldr
---

## AWS DevOps & Developer Productivity Blog

# AWS CloudFormation 2025 Year In Review

AWS CloudFormationenables you to model and provision your cloud application infrastructure as code-base templates. Whether you prefer writing templates directly in JSON or YAML, or using programming languages like Python, Java, and TypeScript with theAWS Cloud Development Kit (CDK), CloudFormation and CDK provide the flexibility you need. For organizations adoptingmulti-account strategies, CloudFormationStackSetsoffers a powerful capability to deploy resources across multiple regions and accounts in parallel.

In 2025, we delivered a comprehensive set of major enhancements focused on three core areas: reducing dev-test cycle through early validation, improving deployment safety with improved configuration drift management, and integrating IaC context to AI-powered development tools.

These launches address common pain points in infrastructure development workflows, from catching deployment errors before resource provisioning to managing configuration drift systematically. The features span the entire development lifecycle, from template authoring in your IDE to multi-account deployments at scale.

This blog provides an overview of the key capabilities we launched in 2025 and how they improve your infrastructure development workflow.

# Accelerating Development Cycles

## Early Validation & Enhanced Troubleshooting: Pre-Deployment Error Detection

CloudFormation now validates your templates duringchange set(preview of infrastructure changes before deployment) creation, catching common deployment errors before resource provisioning begins. The validation checks for invalid property syntax, resource name conflicts with existing resources in your account, and S3 bucket emptiness constraints on delete operations.

Figure 1: Pre-deployment validations view

When validation fails, the change set status shows ‘FAILED’ with detailed information about each issue, including the property path where problems occur. This early feedback helps you fix issues faster rather than waiting for deployment failures.

Figure 2: Validation of Invalid ENUM value for nested property

## Improved Deployment troubleshooting

For runtime errors that occur during deployment, every stack operation now receives a unique operation ID. You can filter stack events by operation ID to quickly identify root causes, reducing troubleshooting time from minutes to seconds. The newdescribe-eventsAPI provides grouped access to events. You can query events for a specific operation, filter to FAILED status events, and extract the root cause without parsing through the entire stack event history.

Figure 3: New CloudFormation stack operation page

Figure 4: Filter operation failure root causes

Learn more:

* What’s New Post
* Detailed Blog Post

## CloudFormation IDE Experience: Language Server Protocol Integration

We launched theAWS CloudFormation Language Server, bringing end-to-end infrastructure development directly into your IDE. Available through the AWS Toolkit for Visual Studio Code, Kiro, and other compatible IDEs, this capability transforms how you author CloudFormation templates.

Figure 1: Initializing a CloudFormation project with environment configuration

The Language Server provides context-aware auto-completion that understands CloudFormation semantics. When you define resources, it suggests only required properties automatically, while optional properties appear on hover. Built-in validation catches issues before deployment integrating early validation capabilities, flagging invalid resource properties, missing IAM permissions, and security policy violations using CloudFormation Guard.

Figure 2: Hover information displaying optional properties and their documentation

The drift-aware deployment view highlights differences between your template and deployed infrastructure, helping you spot configuration changes made outside CloudFormation. The Language Server also provides semantic navigation features, go-to-definition for logical IDs, find-all-references for resource dependencies, and hover documentation that pulls from the CloudFormation resource specification. These features work across intrinsic functions like !Ref, !GetAtt, and !Sub, understanding the CloudFormation template structure. By integrating validation and real-time feedback directly into your authoring experience, the Language Server keeps you in flow state, reducing context switching between your IDE, AWS Console, and documentation.

Figure 3: Type-aware completions for intrinsic functions like !GetAtt & !Ref

Learn more:

* What’s New Post
* Detailed Blog Post

### Stack Refactoring: Adapt your infrastructure to your organization evolution

Stack Refactoring enables you to reorganize your CloudFormation and CDK infrastructure without disrupting deployed resources. You can move resources between stacks, rename logical IDs, and decompose monolithic stacks into focused components while maintaining resource stability and operational state.

Whether you’re modernizing legacy stacks, aligning infrastructure with evolving architectural patterns, or improving long-term maintainability, Stack Refactoring adapts your CloudFormation and CDK organization to changing requirements. The console and CDK experience, launched this year, extends the earlier CLI capability, making refactoring accessible through your preferred interface.

Learn more:–Blog Post – Refactor CloudFormation from Console–Blog Post – Refactor CDK

# Safer Deployments

## Drift-Aware Change Sets

Configuration drift occurs when infrastructure managed by CloudFormation is modified through the AWS Console, SDK, or CLI. Drift-aware change sets address this challenge by providing a three-way comparison between your new template, last-deployed template, and actual infrastructure state.

Figure 4: Examine the drift-aware change set to see the dangerous memory reduction that would occur

This capability helps you prevent unexpected overwrites of drift. If your change set preview shows unintended changes, you can update your template values and recreate the change set before deployment. During execution, CloudFormation matches resource properties with template values and recreates resources deleted outside of CloudFormation.

Drift-aware change sets enable you to systematically revert drift and keep infrastructure in sync with templates, strengthening reproducibility for testing and disaster recovery while maintaining your security posture.

Learn more:

* What’s New Post
* Detailed Blog Post

# Enforcing Proactive Controls

## CloudFormation Hooks: Control Catalog with Hooks

AWS CloudFormation Hooks now supports managed proactive controls, enabling customers to validate resource configurations against AWS best practices without writing custom Hooks logic. Customers can select controls from the AWS Control Tower Controls Catalog and apply them during CloudFormation operations. When using CloudFormation, customers can configure these controls to run in warn mode, allowing teams to test controls without blocking deployments and giving them the flexibility to evaluate control behavior before enforcing policies in production. This significantly reduces setup time, eliminates manual errors, and ensures comprehensive governance coverage across your infrastructure.

AWS also introduced a new Hooks Invocation Summary page in the CloudFormation console. This centralized view provides a complete historical record of Hooks activity, showing which controls were invoked, their execution details, and outcomes such as pass, warn, or fail. This simplifies compliance reporting issues faster.

With this launch, customers can now leverage AWS-managed controls as part of their provisioning workflows, eliminating the overhead of writing and maintaining custom logic. These controls are curated by AWS and aligned with industry best practices, helping teams enforce consistent policies across all environments. The new summary page delivers essential visibility into Hook invocation history, enabling faster issue resolution and streamlined compliance reporting.

Learn more:

* AWS CloudFormation Proactive Control Hooks

# Scaling Multi-Account Infrastructure

## StackSets Deployment Ordering

CloudFormation StackSets now supports deployment ordering for auto-deployment mode, enabling you to define the sequence in which stack instances automatically deploy across accounts and regions. This capability coordinates complex multi-stack deployments where foundational infrastructure must be provisioned before dependent application components.

When creating or updating a StackSet, you can specify up to 10 dependencies per stack instance using the DependsOn parameter in the AutoDeployment configuration. StackSets automatically orchestrates deployments based on your defined relationships. For example, you can ensure networking and security stack instances complete deployment before application stack instances begin, preventing deployment failures due to missing dependencies.

StackSets includes built-in cycle detection to prevent circular dependencies and provides error messages to help resolve configuration issues. This feature is available at no additional cost in all AWS Regions where CloudFormation StackSets is available.

Learn more:

* What’s New Post
* Detailed Blog Post

# AI-Powered Infrastructure Development

## AWS IaC Server

We introduced theAWS Infrastructure-as-Code (IaC) MCP Server, bridging AI assistants with your AWS infrastructure development workflow. Built on the Model Context Protocol (MCP), this server enables AI assistants likeKiro CLIto help you search CloudFormation and CDK documentation, validate templates, troubleshoot deployments, and follow best practices, all while maintaining the security of local execution.

Figure 1: Kiro-CLI with AWS IaC MCP server

The IaC MCP Server provides nine specialized tools organized into two categories. Remote documentation search tools connect to AWS knowledge bases to retrieve up-to-date information about CloudFormation resources, CDK APIs, and implementation guidance. Local validation and troubleshooting tools run entirely on your machine, performing syntax validation with cfn-lint, security checks with CloudFormation Guard, and deployment failure analysis with integrated CloudTrail events.

Figure 4: Validate my CloudFormation template with AWS IaC MCP Server

## Key Use Cases

1. Intelligent Documentation Assistant

Instead of manually searching through documentation, ask your AI assistant natural language questions:

“How do I create an S3 bucket with encryption enabled in CDK?”

The server searches CDK best practice and samples, returning relevant code examples and explanations.

2. Proactive Template Validation

Before deploying infrastructure changes:

User: “Validate my CloudFormation template and check for security issues”

AI Agent: [Uses validate_cloudformation_template and check_cloudformation_template_compliance]

“Found 2 issues: Missing encryption on EBS volumes,

and S3 bucket lacks public access block configuration”

3. Rapid Deployment Troubleshooting

When a stack deployment fails:

User: “My stack ‘stack_03’ in us-east-1 failed to deploy. What happened?”

AI Agent: [Uses troubleshoot_stack_deployment with CloudTrail integration]

“The deployment failed due to insufficient IAM permissions.

CloudTrail shows AccessDenied for ec2:CreateVpc.

You need to add VPC permissions to your deployment role.”

4. Learning and Exploration

New to AWS CDK? The server helps you discover constructs and patterns:

User: “Show me how to build a serverless API”

AI Agent: [Searches CDK constructs and samples]

“Here are three approaches using API Gateway + Lambda…”

Learn more:Detailed Blog Post

# Learn more

Here are some resources to help you get started learning and using CloudFormation to manage your cloud infrastructure:

* Watch our re:Invent 2025 session on CloudFormation and CDK
* AWS CloudFormation Workshop
* AWS CloudFormation Troubleshooting Guide

# Conclusion

As we begin 2026, our focus remains on making infrastructure deployment faster, safer, and more manageable. The launches in 2025 reflect our commitment to solving real customer challenges and improving the CloudFormation developer experience. From intelligent IDE integrations to AI-powered assistance, these capabilities help you build infrastructure with greater confidence and efficiency.

We encourage you to try these features and share your feedback. For detailed information about any of these launches, visit ourdocumentationor check out theAWS DevOps Blog.

## Blog Author Bio:
