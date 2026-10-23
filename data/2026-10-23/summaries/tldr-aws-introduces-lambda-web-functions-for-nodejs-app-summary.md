---
title: AWS Introduces Lambda Web Functions for Node.js Applications - InfoQ
url: https://www.infoq.com/news/2026/10/aws-lambda-web-functions
date: 2026-10-23
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-23T15:46:37.239662
---

# AWS Introduces Lambda Web Functions for Node.js Applications - InfoQ

**AWS Introduces Lambda Web Functions for Node.js Applications**

**Key Points:**

* AWS Lambda Web Functions allow developers to run Node.js web applications directly on Lambda with concurrent requests and streaming response support.
* These functions charge for active CPU time and memory, whereas traditional Lambda functions charge for CPU time spent waiting for downstream services.
* Lambda Web Functions support multi-region routing and single warm execution environments to reduce cold starts.

**Maintaining Original Perspective and Language:**

* The article remains in the same narrative style and point of view as the original text.
* Grammar, sentence structure, and vocabulary are preserved.
* Mixed-language sections retain their original meaning and context.

**Summary in Markdown:**

# AWS Introduces Lambda Web Functions for Node.js Applications

* **What**: AWS Lambda Web Functions allow developers to run Node.js web applications directly on Lambda with concurrent requests and streaming response support.
* **Benefits**:
 + Charges for active CPU time and memory, reducing costs.
 + Supports multi-region routing to optimize performance.
 + Supports single warm execution environment for reduced cold starts.
 + Optimizes resource usage through scaling, routing, and billing.
* **Target Workloads**:
 + Full-stack web applications
 + REST and GraphQL APIs
 + Independently scaling microservices
 + Server-side rendering and streaming responses
* **Lambda Web Functions**:
 + Currently available for Node.js only
 + Supports other languages through traditional Lambda functions
* **Example Use Case**:
 + Sample application built using a standard Node.js HTTP server
 + Deployment with CloudFormation or one command
 + Scalable, pay-per-use HTTPS endpoint with global reach
* **Key Takeaway**:
 + AWS Lambda Web Functions offer a serverless operating model for Node.js web applications without adapter layers.