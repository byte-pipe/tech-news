---
title: Announcing AWS Lambda Web Functions | AWS News Blog
url: https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere
site_name: tldr
content_file: tldr-announcing-aws-lambda-web-functions-aws-news-blog
fetched_at: '2026-10-15T21:58:10.634960'
original_url: https://aws.amazon.com/blogs/aws/announcing-aws-lambda-web-functions-for-fast-consistent-web-app-performance-anywhere
date: '2026-10-15'
published_date: '2026-10-12T15:34:47-07:00'
description: Announcing AWS Lambda Web Functions | AWS News Blog
tags:
- tldr
---

## AWS News Blog

# Announcing AWS Lambda Web Functions

Today, we’re announcingAWS Lambda Web Functions, a new form factor that lets you run standard HTTP web applications on Lambda without rewriting your code into an event handler. You can take a standard port-listening server built with Express, Hono, Fastify, Next.js, or any Node.js framework, deploy it with a single command, and Lambda automatically handles scaling, multi-region distribution, and active CPU billing. No adapters, no infrastructure to manage, and no framework lock-in.

With this launch, AWS Lambda now offers three distinct form factors, each built on the same Firecracker isolation technology and designed for a different programming model.

Lambda Event Functionsare what you already know as Lambda functions. They use the event-driven, single-concurrent handler model with wall-clock billing. We’re introducing the “Event Functions” name to highlight that programming model: your function receives an event, processes it, and returns a response. The event-driven programming model is ideal for event processing, queue consumers, and invocations triggered by other AWS services.

Lambda Web Functionsuse an HTTP-native programming model with multi-concurrent execution and active CPU billing. Your code listens on a port and handles standard HTTP requests. That programming model is ideal for web applications, API backends, and interactive HTTP workloads where multiple concurrent requests and I/O-heavy processing are the norm.

Lambda MicroVMsprovide isolated, stateful sandbox environments with customer-managed lifecycles for running untrusted or user-generated code.

The three complement each other. An application might use Event Functions for asynchronous backend processing, Web Functions for the user-facing API and server-side rendering layer, and MicroVMs for interactive code execution features, all within the same AWS account and sharing the same operational model.

Why Web FunctionsModern web applications need to serve global audiences with fast, consistent response times while giving developers the freedom to use standard frameworks and iterate quickly. Building this today typically requires assembling multiple infrastructure components, configuring multi-region deployments, setting up latency-based routing, and tuning billing models to avoid paying for I/O wait. Developers often find themselves adapting their application code to fit a specific compute model rather than deploying the HTTP server they already have.

Lambda Web Functions removes this complexity. Each execution environment handles multiple requests simultaneously (up to 128 concurrent requests per environment), which means a burst of incoming traffic can share warm environments instead of mapping each request to a new one. Web Functions meter the CPU time your code uses, so time spent waiting on a database query or an API call consumes little CPU. Memory is metered for as long as the execution environment exists. For I/O-heavy web workloads like server-side rendering, API backends, and AI inference endpoints streaming token responses, this can reduce compute costs.

Let’s try it outTo get started, I wrote a simple Express.js server. This is the same code I run locally withnode index.js, no Lambda-specific adapters or wrappers required.

import express from 'express';

const app = express();
const [host, port] = process.env.AWS_LAMBDA_HTTP_ENDPOINT.split(':');

app.get('/', (req, res) => {
 res.json({ message: 'Hello from Lambda Web Functions!' });
});

app.listen(port, host, () => {
 console.log(`Server running on port ${port}`);
});

The only difference from running locally is theAWS_LAMBDA_HTTP_ENDPOINTenvironment variable, which Lambda sets to the host and port your server must listen on. To run locally, set it yourself, for exampleAWS_LAMBDA_HTTP_ENDPOINT=127.0.0.1:3000 node index.js.

With my code ready, I deployed using theAWS Command Line Interface (AWS CLI):

aws lambda-web deploy --name my-web-app --code ./my-app

One command. No prior resource setup. The CLI bundled my source, created the Web Function, published its first revision, attached a Web Function endpoint, and returned a live HTTPS URL in under a minute.

A revision is an immutable snapshot of the code I deployed. The endpoint is the HTTPS URL that routes traffic to a revision, or splits traffic across revisions. Those are the resources I use to iterate and to control how traffic moves to new code.

I tested it immediately:

$ curl https://<domain-id>.<shard-id>.lambda-web.us-east-1.on.aws/
{"message":"Hello from Lambda Web Functions!"}

Next, I wanted my application to serve users in Europe and Asia with lower latency. I redeployed with multiple regions:

aws lambda-web deploy --name my-web-app --code ./my-app \
 --regions us-east-1,eu-west-1,ap-northeast-1

Lambda Web Functions replicated my code to all three regions and configured latency-based routing automatically. Each request now routes to the Region with the lowest latency for the caller, on a best-effort basis, through one global URL (<domain-id>.lambda-web.global.on.aws).

When I updated my code and ran the same deploy command again, the CLI detected the existing function, uploaded the new revision, and pointed the endpoint at it. Total turnaround from code change to live: seconds.

For production workflows that require a more gradual rollout, I can shift traffic between revisions with a single API call:

aws lambda-web update-web-function-endpoint \
 --function-name my-web-app \
 --endpoint-name dev \
 --auto-deployment-mode Disabled \
 --revision-weights '[{"revisionId": "<current-revision-id>", "weight": 90}, {"revisionId": "<new-revision-id>", "weight": 10}]'

This sends 90% of endpoint traffic to the current revision and 10% to the new one, giving me a canary deployment without additional tooling.

Better together with Amazon CloudFrontFor applications that combine static and dynamic content, Web Functions works well alongsideAmazon CloudFront. You can select a Web Function endpoint as the origin for your CloudFront distribution. Static assets are served from the cache while dynamic requests route to your Web Function, giving you CDN performance for static content with serverless compute for the dynamic parts.

Web Functions improves the private-origin experience with CloudFront. With this launch, you attach CloudFrontorigin access control (OAC)to a Web Function endpoint instead. CloudFront signs requests to the origin, and the endpoint allows only your distribution to invoke it. You get the same private-origin pattern CloudFront already provides forAmazon Simple Storage Service (Amazon S3), without exposing the endpoint or adding custom authorization to your app.

Now availableAWS Lambda Web Functions is available today in US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Tokyo), and Europe (Ireland). Web Functions run Node.js 24 (nodejs24.x) on Arm64 at launch and support Amazon Virtual Private Cloud (VPC) connectivity, allowing your function to access resources that exist within a VPC.

To get started, deploy your first Web Function in under a minute:

aws lambda-web deploy --name hello-world --hello-world

For pricing details, visit theAWS Lambda pricing page. To learn more, see theLambda Web Functions documentation.