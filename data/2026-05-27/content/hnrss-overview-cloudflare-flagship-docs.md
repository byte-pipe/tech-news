---
title: Overview · Cloudflare Flagship docs
url: https://developers.cloudflare.com/flagship/
site_name: hnrss
content_file: hnrss-overview-cloudflare-flagship-docs
fetched_at: '2026-05-27T19:44:15.601212'
original_url: https://developers.cloudflare.com/flagship/
date: '2026-05-26'
description: Ship features safely with Flagship, Cloudflare's feature flag service for controlling feature visibility without redeploying code.
tags:
- hackernews
- hnrss
---

# Cloudflare Flagship

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

Ship features safely with feature flags.

 

Flagship is Cloudflare's feature flag service. It lets you control feature visibility in your applications without redeploying code. Define flags with targeting rules and percentage-based rollouts, then evaluate them directly inside your Workers through anative binding.

OpenFeature↗is the CNCF open standard for feature flag management. Flagship is compatible with OpenFeature, so you can use the@cloudflare/flagship↗SDK from any JavaScript runtime — Workers, Node.js, or the browser — and swap providers without changing evaluation code.

Check out theGet started guideto create your first feature flag.

## Features

 

### Worker binding

 
 

Evaluate flags with a native Workers binding. Type-safe methods with automatic fallback to defaults.

 
 
 Binding reference 
 
 

 

### OpenFeature SDK

 
 

Use the@cloudflare/flagship↗OpenFeature provider to evaluate flags from Workers, Node.js, or browsers. Switch from another flag provider by changing one line of configuration.

 
 
 View SDK docs 
 
 

 

### Targeting rules

 
 

Serve different flag values based on user attributes. Rules support 11 comparison operators, logical AND/OR grouping, and sequential evaluation.

 
 
 Learn about targeting 
 
 

 

### Percentage rollouts

 
 

Gradually release features to a percentage of users. Consistent hashing ensures the same user always receives the same flag value.

 
 
 Learn about rollouts 
 
 

 

### Multi-type variations

 
 

Flag variations can be booleans, strings, numbers, or structured JSON objects. Use object variations to deliver entire configuration blocks as a single flag.

 
 
 Use Multi-type variations 
 
 

 

### Flag management

 
 

Create, update, and delete flags through the Cloudflare dashboard. Organize flags into apps that map to your projects or services.

 
 
 Use Flag management 
 
 

## Related products

 
 
 
 
 
 
Workers
 
 

Build serverless applications on Cloudflare's global network. Flagship integrates natively with Workers through a binding.

 
 

 
 
 
 
 
 
KV
 
 

Store key-value data across Cloudflare's global network. Flagship uses this infrastructure to deliver flag configurations.

 
 

## More resources

 

Developer Discord

 

Connect with the Workers community on Discord to ask questions, show what you
are building, and discuss the platform with other developers.

 
 

@CloudflareDev

 

Follow @CloudflareDev on Twitter to learn about product announcements and what
is new in Cloudflare Workers.