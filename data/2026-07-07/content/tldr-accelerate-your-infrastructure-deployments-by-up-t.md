---
title: Accelerate your infrastructure deployments by up to 4x with AWS CloudFormation Express mode | AWS News Blog
url: https://aws.amazon.com/blogs/aws/accelerate-your-infrastructure-deployments-by-up-to-4x-with-aws-cloudformation-express-mode/
site_name: tldr
content_file: tldr-accelerate-your-infrastructure-deployments-by-up-t
fetched_at: '2026-07-07T12:02:32.057341'
original_url: https://aws.amazon.com/blogs/aws/accelerate-your-infrastructure-deployments-by-up-to-4x-with-aws-cloudformation-express-mode/
date: '2026-07-07'
published_date: '2026-06-30T14:30:33-07:00'
description: Accelerate your infrastructure deployments by up to 4x with AWS CloudFormation Express mode (4 minute read)
tags:
- tldr
---

## AWS News Blog

# Accelerate your infrastructure deployments by up to 4x with AWS CloudFormation Express mode

Today, we’re announcingAWS CloudFormationExpress mode, a new deployment mode that accelerates deployments for developers and AI tools iterating on infrastructure. Express mode accelerates deployments by completing when CloudFormation confirms resource configuration is applied, rather than waiting for extended stabilization checks. This reduces deployment time by up to 4 times for iterative development workflows and production scenarios.

How it worksEvery CloudFormation deployment performs stabilization checks after resource configuration is applied. These checks serve an important purpose when you need to confirm resources can serve traffic before shifting load.

However, many workflows do not require full stabilization to proceed. Express mode benefits two primary use cases: iterative development workflows and production scenarios where you are comfortable with eventual stabilization. These use cases include iterating on infrastructure configurations during development, testing individual components of your application, and AI-assisted infrastructure development that benefits from sub-minute feedback loops.

With Express mode, CloudFormation completes deployments when resource configuration is applied, without waiting for stabilization checks. Resources continue becoming operational in the background. CloudFormation automatically retries dependent resources that encounter transient failures during provisioning within the same stack, without requiring any customer intervention. This built-in resilience handles timing issues between resources as they stabilize. Express mode changeswhenthe deployment completes, nothowresources are provisioned.

For example, when I create anAmazon Simple Queue Service (SQS)queue with a dead letter queue (DLQ), Standard mode takes 64 seconds, but Express mode completes in up to 10 seconds. In the case of deleting anAWS Lambdafunction with network interface attachment, Standard mode takes 20–30 minutes, but Express mode completes in up to 10 seconds based on my benchmarking test.

Get started with CloudFormation Express modeWhen you create a CloudFormation stack in theAWS Management Console, chooseEnablein theExpress modeunderStack deployment options.

You can also useAWS Command Line Interface (AWS CLI),AWS SDKs, or IaC tools likeAWS Cloud Development Kit (CDK), and AI tools such asKiro.

Activate Express mode by setting the--deployment-configparameter toEXPRESSwhen creating, updating, or deleting stacks. No template changes are required. Express mode disables rollback by default for the fastest iteration experience. To re-enable rollback, setdisableRollbacktofalsein thedeployment-configfor production environments, or implement monitoring/cleanup mechanisms for failed deployments.

aws cloudformation create-stack \ 
 --stack-name my-app \ 
 --template-body file://template.yaml \ 
 --deployment-config '{"mode": "EXPRESS", "disableRollback": true}' \

For example, use the Express mode when you build infrastructure incrementally, adding resources one at a time. Ensure your IAM role templates follow the principle of least privilege.

# Iteration 1: Deploy IAM role
aws cloudformation create-stack \
--stack-name my-microservice \
--template-body file://iteration1-iam.yaml \
--deployment-config '{"mode": "EXPRESS"}' \
--capabilities CAPABILITY_IAM
--role-arn arn:aws:iam::123456789012:role/CloudFormationDeployRole

# Iteration 2: Add Lambda function
aws cloudformation update-stack \
--stack-name my-microservice \
--template-body file://iteration2-lambda.yaml \
--deployment-config '{"mode": "EXPRESS"}' \
--capabilities CAPABILITY_IAM
--role-arn arn:aws:iam::123456789012:role/CloudFormationDeployRole

# Iteration 3: Add SQS queue and event source mapping
aws cloudformation update-stack \
--stack-name my-microservice \
--template-body file://iteration3-sqs.yaml \
--deployment-config '{"mode": "EXPRESS"}' \
--capabilities CAPABILITY_IAM
--role-arn arn:aws:iam::123456789012:role/CloudFormationDeployRole

For AWS CDK, activate Express mode with thecdk deploy --expresscommand when you deploy your CDK stack. This command retrieves your generated CloudFormation template and deploys it through the CloudFormation Express mode, which provisions your resources as part of a CloudFormation stack.

Express mode works with all existing CloudFormation templates and supports all CloudFormation features including change sets and nested stacks. When you enable Express mode on a parent stack, all nested stacks also use Express mode. If you need resources to be fully operational before proceeding with traffic or testing, continue using the default deployment behavior, which performs stabilization checks before completing.

Now availableAWS CloudFormation Express mode is available today in all AWS commercial Regions at no additional cost. For Regional availability and a future roadmap, visit theAWS Capabilities by Region. If you want to call APIs, search documentation, find regional availability, and check troubleshooting about this new feature, try using theAWS MCP Serverandpluginswith your preferred AI tool. To learn more, visit theCloudFormation documentation.

Start accelerating your deployments today, and send feedback toAWS re:Post for AWS CloudFormationor through your usual AWS Support contacts.

—Channy