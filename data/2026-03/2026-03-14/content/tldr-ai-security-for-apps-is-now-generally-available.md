---
title: AI Security for Apps is now generally available
url: https://blog.cloudflare.com/ai-security-for-apps-ga/
site_name: tldr
content_file: tldr-ai-security-for-apps-is-now-generally-available
fetched_at: '2026-03-14T06:00:35.222217'
original_url: https://blog.cloudflare.com/ai-security-for-apps-ga/
date: '2026-03-14'
published_date: 2026-03-11T13:00+00:00
description: Cloudflare AI Security for Apps is now generally available, providing a security layer to discover and protect AI-powered applications, regardless of the model or hosting provider. We are also making AI discovery free for all plans, to help teams find and secure shadow AI deployments.
tags:
- tldr
---

# AI Security for Apps is now generally available

2026-03-11

* Liam Reese
* Zhiyuan Zheng
* Catherine Newcomb
5 min read
This post is also available in
한국어
.

Cloudflare’sAI Security for Appsdetects and mitigates threats to AI-powered applications. Today, we're announcing that it is generally available.

We’re shipping with new capabilities like detection for custom topics, and we're making AI endpoint discovery free for every Cloudflare customer—including those on Free, Pro, and Business plans—to give everyone visibility into where AI is deployed across their Internet-facing apps.

We're also announcing an expanded collaboration with IBM, which has chosen Cloudflare to deliver AI security to its cloud customers. And we’re partnering with Wiz to give mutual customers a unified view of their AI security posture.

## A new kind of attack surface

Traditional web applications have defined operations: check a bank balance, make a transfer. You can write deterministic rules to secure those interactions.

AI-powered applications and agents are different. They accept natural language and generate unpredictable responses. There's no fixed set of operations to allow or deny, because the inputs and outputs are probabilistic. Attackers can manipulate large language models to take unauthorized actions or leak sensitive data. Prompt injection, sensitive information disclosure, and unbounded consumption are just a few of the risks cataloged in theOWASP Top 10 for LLM Applications.

These risks escalate as AI applications become agents. When an AI gains access to tool calls—processing refunds, modifying accounts, providing discounts, or accessing customer data—a single malicious prompt becomes an immediate security incident.

Customers tell us what they’re up against. "Most of Newfold Digital's teams are putting in their own Generative AI safeguards, but everybody is innovating so quickly that there are inevitably going to be some gaps eventually,” says Rick Radinger, Principal Systems Architect at Newfold Digital, which operates Bluehost, HostGator, and Domain.com.

## What AI Security for Apps does

We built AI Security for Apps to address this. It sits in front of your AI-powered applications, whether you're using a third-party model or hosting your own, as part of Cloudflare'sreverse proxy. It helps you (1) discover AI-powered apps across your web property, (2) detect malicious or off-policy behavior to those endpoints, and (3) mitigate threats via the familiar WAF rule builder.

### Discovery — now free for everyone

Before you can protect your LLM-powered applications, you need to know where they're being used. We often hear from security teams who don’t have a complete picture of AI deployments across their apps, especially as the LLM market evolves and developers swap out models and providers.

AI Security for Apps automatically identifies LLM-powered endpoints across your web properties, regardless of where they’re hosted or what the model is. Starting today, this capability is free for every Cloudflare customer, including Free, Pro, and Business plans.

Cloudflare’s dashboard page of web assets, showing 2 example endpoints labelled ascf-llm

Discovering these endpoints automatically requires more than matching common path patterns like/chat/completions. Many AI-powered applications don't have a chat interface: think product search, property valuation tools, or recommendation engines. We built adetection system that looks at how endpoints behave, not what they're called. To confidently identify AI-powered endpoints,sufficient valid trafficis required.

AI-powered endpoints that have been discovered will be visible underSecurity → Web Assets, labeled ascf-llm. For customers on a Free plan, endpoint discovery is initiated when you first navigate to theDiscovery page. For customers on a paid plan, discovery occurs automatically in the background on a recurring basis. If your AI-powered endpoints have been discovered, you can review them immediately.

### Detection

AI Security for Apps detections follow thealways-on approachfor traffic to your AI-powered endpoints. Each prompt is run through multiple detection modules for prompt injection, PII exposure, and sensitive or toxic topics. The results—whether the prompt was malicious or not—are attached as metadata you can use in custom WAF rules to enforce your policies. We are continuously exploring ways to leverage our global network, which sees traffic from roughly20% of the web, to identify new attack patterns across millions of sites before they reach yours.

#### New in GA: Custom topics detection

The product ships with built-in detection for common threats: prompt injections,PII extraction, andtoxic topics. But every business has its own definition of what's off-limits. A financial services company might need to detect discussions of specific securities. A healthcare company might need to flag conversations that touch on patient data. A retailer might want to know when customers are asking about competitor products.

The new custom topics feature lets you define these categories. You specify the topic, we inspect the prompt and output a relevance score that you can use to log, block, or handle however you decide. Our goal is to build an extensible tool that flexes to your use cases.

Prompt relevance score inside of AI Security for Apps

#### New in GA: Custom prompt extraction

AI Security for Apps enforces guardrails before unsafe prompts can reach your infrastructure. To run detections accurately and provide real-time protection, we first need to identify the prompt within the request payload. Prompts can live anywhere in a request body, and different LLM providers structure their APIs differently. OpenAI and most providers use$.messages[*].contentfor chat completions. Anthropic's batch API nests prompts inside$.requests[*].params.messages[*].content. Your custom property valuation tool might use$.property_description.

Out of the box, we support the standard formats used by OpenAI, Anthropic, Google Gemini, Mistral, Cohere, xAI, DeepSeek, and others. When we can't match a known pattern, we apply a default-secure posture and run detection on the entire request body. This can introduce false positives when the payload contains fields that are sensitive but don't feed directly to an AI model, for example, a$.customer_namefield alongside the actual prompt might trigger PII detection unnecessarily.

Soon, you'll be able to define your own JSONPath expressions to tell us exactly where to find the prompt. This will reduce false positives and lead to more accurate detections. We're also building a prompt-learning capability that will automatically adapt to your application's structure over time.

### Mitigation

Once a threat is identified and scored, you can block it, log it, or deliver custom responses, using the same WAF rules engine you already use for the rest of your application security. The power of Cloudflare’s shared platform is that you can combine AI-specific signals with everything else we know about a request, represented byhundreds of fieldsavailable in the WAF. A prompt injection attempt is suspicious. A prompt injection attempt from an IP that’s been probing your login page, using a browser fingerprint associated with previous attacks, and rotating through a botnet is a different story. Point solutions that only see the AI layer can’t make these connections.

This unified security layer is exactly what they need at Newfold Digital to discover, label, and protect AI endpoints, says Radinger: “We look forward to using it across all these projects to serve as a fail-safe."

## Growing ecosystem

AI Security for Applications will also be available through Cloudflare's growing ecosystem, including through integration with IBM Cloud. ThroughIBM Cloud Internet Services (CIS), end users can already procure advanced application security solutions and manage them directly through their IBM Cloud account.

We're also partnering with Wiz to connect AI Security for Applications withWiz AI Security, giving mutual customers a unified view of their AI security posture, from model and agent discovery in the cloud to application-layer guardrails at the edge.

## How to get started

AI Security for Apps is available now for Cloudflare’s Enterprise customers. Contact your account team to get started, or see the product in action with aself-guided tour.

If you're on a Free, Pro, or Business plan, you can use AI endpoint discovery today. Log in to your dashboard and navigate toSecurity → Web Assetsto see which endpoints we've identified. Keep an eye out — we plan to make all AI Security for Apps capabilities available for customers on all plans soon.

For configuration details, see ourdocumentation.

Cloudflare's connectivity cloud protects
entire corporate networks
, helps customers build
Internet-scale applications efficiently
, accelerates any
website or Internet application
,
wards off DDoS attacks
, keeps
hackers at bay
, and can help you on
your journey to Zero Trust
.
Visit
1.1.1.1
 from any device to get started with our free app that makes your Internet faster and safer.
To learn more about our mission to help build a better Internet,
start here
. If you're looking for a new career direction, check out
our open positions
.


Product News
AI
WAF
Security
Application Security
Application Services
