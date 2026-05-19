---
title: Amazon Bedrock introduces new advanced prompt optimization and migration tool | AWS News Blog
url: https://aws.amazon.com/blogs/aws/amazon-bedrock-introduces-new-advanced-prompt-optimization-and-migration-tool/
date: 2026-05-20
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-20T06:02:43.794091
---

# Amazon Bedrock introduces new advanced prompt optimization and migration tool | AWS News Blog

# Amazon Bedrock introduces new advanced prompt optimization and migration tool

## Overview
- Announces **Amazon Bedrock Advanced Prompt Optimization**, a tool to improve and migrate prompts across up to 5 Bedrock models simultaneously.  
- Enables testing for regressions, performance gains, and under‑performing tasks.

## How the optimizer works
- Accepts a prompt template, example inputs, ground‑truth answers, and an evaluation metric.  
- Supports multimodal inputs (png, jpg, pdf) for document and image analysis.  
- Uses a metric‑driven feedback loop to rewrite prompts, producing original and optimized templates with scores, cost estimates, and latency.

## Using the tool
- Access via **Create prompt optimization** on the Advanced Prompt Optimization page in the Bedrock console.  
- Select up to 5 inference models (current model as baseline plus up to 4 others).  
- Prepare prompt templates in JSONL format, each line containing:
  - version, templateId, promptTemplate, optional steeringCriteria, evaluation settings, and evaluationSamples with inputVariables and optional multimodal data.  
- Upload files directly or import from Amazon S3; specify an S3 output location for results.  
- Click **Create optimization** to start the process.

## Evaluation options
- **Lambda function** – custom Python scoring logic (accuracy, F1, JSON match, etc.).  
- **LLM‑as‑a‑Judge** – rubric‑based scoring using a judge model (default Claude Sonnet 4.6, others selectable).  
- **Steering criteria** – free‑form natural‑language qualities (brand voice, safety, format) evaluated by a default judge model.  
- One method per prompt template; multiple templates can use different methods in the same job.

## Availability and pricing
- Available in US East (N. Virginia, Ohio), US West (Oregon), Asia Pacific (Mumbai, Seoul, Singapore, Sydney, Tokyo), Canada (Central), Europe (Frankfurt, Ireland, London, Zurich), and South America (São Paulo).  
- Charged based on Bedrock model‑inference tokens consumed during optimization, at regular per‑token rates.

## Getting started
- Try the feature in the Amazon Bedrock console or via the **CreateAdvancedPromptOptimizationJob** API.  
- Provide feedback through AWS re:Post for Amazon Bedrock or standard AWS Support channels.