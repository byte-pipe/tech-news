---
title: A Simple ECS + ECR Project for Beginners - DEV Community
url: https://dev.to/aws-builders/a-simple-ecs-ecr-project-for-beginners-4gc0
site_name: devto
fetched_at: '2025-06-23T01:04:40.591277'
original_url: https://dev.to/aws-builders/a-simple-ecs-ecr-project-for-beginners-4gc0
author: Venkata Pavan Vishnu Rachapudi
date: '2025-06-15'
description: Are you new to AWS and trying to understand how ECS and ECR work together to deploy your... Tagged with aws, docker, terraform, cdn.
tags: '#aws, #docker, #terraform, #cdn'
---

Are you new to AWS and trying to understand how ECS and ECR work together to deploy your applications? This post is for you! In this simple walkthrough, we’ll learn how to containerize an app, store the image in Amazon ECR, and run it on ECS with Terraform.

## ✅ Prerequisites

Before you begin, ensure you have the following installed and configured:

* ✅ AWS CLI (with credentials configured)
* ✅ Terraform
* ✅ Docker
* ✅ An existing ECR repository (or Terraform will create one for you)

## 🧰 Services Used in This Project (with Terraform)

1. Amazon ECR (Elastic Container Registry)

🗃️ A fully managed Docker container registry to store and manage your container images.

* Used to store the Docker image built from your app.
* Terraform automates the creation (or reuse) of an ECR repository.
* The ECS service pulls the image directly from ECR at runtime.

2. Amazon ECS (Elastic Container Service) with Fargate

🚢 A container orchestration service that allows you to run and scale containerized applications.

* We use Fargate, a serverless compute engine, which removes the need to manage EC2 instances.
* ECS takes care of deploying, scaling, and managing the container lifecycle.
* One or more ECS tasks (containers) are run inside an ECS service backed by a cluster.

3. Amazon VPC (Virtual Private Cloud)

🌐 Isolated network environment where all AWS resources are deployed.

* A custom VPC is provisioned with public subnets for ECS services and ALB.
* Includes internet gateway, route tables, and security groups.
* Provides secure and organized networking boundaries for your app.

4. Application Load Balancer (ALB)

⚖️ Distributes incoming traffic across ECS tasks running in different availability zones.

* Exposes your application publicly over HTTP.
* Automatically distributes traffic to available ECS containers (targets).
* Integrates with CloudFront as the origin.

5. Amazon CloudFront (Content Delivery Network)

🚀 Delivers your content securely and quickly across the globe.

* Sits in front of ALB and caches static and dynamic content.
* Provides HTTPS by default using an AWS-managed SSL certificate.
* Integrates with S3 for storing access logs and with CloudWatch for monitoring.

6. Amazon S3 (Simple Storage Service)

💾 Secure, durable object storage for any kind of data.

* Used to store CloudFront access logs, giving visibility into who accessed what, when, and how.
* A dedicated bucket is automatically created to collect logs.
* Useful for debugging, auditing, and traffic analysis.

7. Amazon CloudWatch

📈 Monitoring and observability platform for AWS resources and applications.

* Tracks key CloudFront metrics like request count, 4xx/5xx error rates, and latency.
* Used to trigger alarms and analyze performance trends.
* Can also log custom application or ECS-level logs if configured.

8. Amazon SNS (Simple Notification Service)

🔔 A messaging service used to send notifications based on monitoring triggers.

* Connected to CloudWatch alarms to send email notifications.
* Alerts you when thresholds are breached (e.g., too many 5xx errors from CloudFront).
* Ensures you're immediately notified about potential issues or traffic spikes.

9. Terraform

🛠️ Infrastructure as Code tool used to automate and manage all cloud resources.

* Defines, provisions, and destroys infrastructure consistently across environments.
* Enables full automation of the VPC, ECS, ALB, CloudFront, S3, CloudWatch, and SNS setup.
* Makes your deployments repeatable, version-controlled, and easy to maintain.

## 🛠️ Deployment Steps

Step 1: Initialize TerraformSet up Terraform in your working directory.

terraform init

Enter fullscreen mode

Exit fullscreen mode

Step 2: Format the Terraform CodeClean up the Terraform files (optional but recommended):

terraform fmt

Enter fullscreen mode

Exit fullscreen mode

Step 3: Prepare the Docker Image and Push to ECRIf you haven’t pushed your app image to ECR yet, Check forecr_push.shin scripts folder and run the commandsThis script will:

* Build the Docker image
* Tag it with your ECR repo URL
* Push the image to ECR

⚠️ Already have an image in ECR? You can skip this step.

✅ Final Checks Before You Deploy🔍 1. Double-check Terraform Variable ConfigurationEnsure the following are correctly defined and populated:

In variables.tf:

* Region
* ECR repo name
* S3 log bucket name (optional default or dynamic name)
* CloudFront price class or alias config (if any)
* email for SNS Topic Subscription
* Restrict access to specific IP addresses for security (Check in VPC module main.tf)
* ECS Tasks memory,CPU and number of tasks
* log retention period

Step 4: Review the Terraform PlanPreview what Terraform will create:

terraform plan -out=tfplan

Enter fullscreen mode

Exit fullscreen mode

ignore 1 to destroy

Step 5: Apply the Terraform ConfigurationDeploy the infrastructure:

terraform apply tfplan

Enter fullscreen mode

Exit fullscreen mode

Or simply:

if you don’t use -out=tfplan in terraform plan command

terraform apply

Enter fullscreen mode

Exit fullscreen mode

During the run , you will get a subscribe mail which i used in the sns topic.Click and confirm the subscription

The deployment may take a few minutes since Terraform is provisioning several resources like ECS tasks, services, ALB, and CloudFront.By default, Terraform automatically understands the order in which resources should be created by analyzing their dependencies using its internal dependency graph.However, if needed, we can explicitly control the order using the depends_on attribute.

You can safely ignore this message—Terraform is attempting to recreate the ECR image, but since it already exists, it's not necessary. To avoid this in the future, you can use a Terraform lifecycle rule withignore_changesto prevent updates to the image configuration.

✅ Step 6: Access Your ApplicationAfter Terraform finishes creating all the resources, it will automatically generate an outputs.txt file containing the key access information for your deployment.

Thanks to null_resources block in main.tf

This file includes:

- VPC ID
- ECR Repository URL
- ECS Cluster Name
- Load Balancer DNS
- CloudFront Domain Name
- CloudWatch Dashboard Name
- S3 Logs Bucket Name
- SNS Topic ARN

Enter fullscreen mode

Exit fullscreen mode

⚠️ Make sure outputs.txt is not committed to version control if it contains sensitive data in real projects.

or else run command

terraform output

Enter fullscreen mode

Exit fullscreen mode

Use either URL to access your web app.

🔗 Application URLs:

* CloudFront (Global HTTPS): Recommended for production use
* ALB DNS (Direct HTTP): Useful for internal testing or quick validation

Step 7: Clean Up ResourcesWhen done, destroy all created AWS resources to avoid costs:

terraform destroy

Enter fullscreen mode

Exit fullscreen mode

⚠️ Note on Destroying ResourcesDuring terraform destroy, most AWS resources will be deleted automatically. However, you may see errors like this:

ECR Repository not empty – cannot delete
S3 Bucket not empty – cannot delete

Enter fullscreen mode

Exit fullscreen mode

This is because:

* Amazon ECR will not allow deletion if it still contains images.
* Amazon S3 will not allow deletion if it contains objects/logs.

✅ Solutions🔹 Option 1: Delete Manually via AWS ConsoleGo to ECR → Select your repository → Delete all images.

Go to S3 → Select the bucket → Empty the bucket → Then delete it.

🔹 Option 2: Use AWS CLIDelete all ECR images:

aws ecr batch-delete-image \
 --repository-name ecs-ecr-demo \
 --image-ids $(aws ecr list-images --repository-name ecs-ecr-demo --query 'imageIds[*]' --output json)

Enter fullscreen mode

Exit fullscreen mode

Empty and delete the S3 bucket:

aws s3 rm s3://ecs-ecr-demo-logs-<your-bucket-id> --recursive
aws s3 rb s3://ecs-ecr-demo-logs-<your-bucket-id>

Enter fullscreen mode

Exit fullscreen mode

Once these are cleared, re-run:

terraform destroy

Enter fullscreen mode

Exit fullscreen mode

## 🔁 Flow Summary

* User sends request → CloudFront receives it over HTTPS.
* CloudFront checks cache; if miss, forwards to ALB.
* ALB forwards request to one of the ECS tasks (Fargate).
* ECS Task (running NGINX) returns the response.
* CloudFront caches and sends the response back to the user.
* Logs go to S3; metrics go to CloudWatch; alerts (if any) go via SNS.

## 🎨 Design Choices

Modular Terraform Structure:

* Each component (VPC, ECS, ECR, ALB, CloudFront) in its own module.
* Easy to scale, maintain, or reuse.
* Stateless Web App:
* Simple NGINX-based static page for demo purposes.
* Security:
* Public subnets used for quick demo access.
* Security groups restrict traffic to ports 80 and 443 only.

Outputs File:

A null_resource writes important info (e.g., URLs, VPC ID) into outputs.txt.

## 🔧 How to Customize

* 📝 Change docker/index.html to update the website content
* 🏗️ Edit main.tf to modify infrastructure behavior
* 🔁 Update ECS module to change container settings

## 💡Tips

* Add lifecycle { ignore_changes = [...] } in ECR module to avoid re-creation issues.
* Use depends_on when you want to manually control resource order.
* For real-world apps, consider using private subnets, HTTPS on ALB, and custom domains.

## 🚀 Try out now

📦 GitHub Repository:https://github.com/aquavis12/ecs-ecr-demo

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
