---
title: Introducing Web Search API · Changelog
url: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/
date: 2026-10-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:48:58.004487
---

# Introducing Web Search API · Changelog

# Introducing Web Search API

## Overview
- The Web Search API is now available in beta.
- It enables AI agents and applications to perform live Internet searches and base their responses on current information.
- Replaces reliance on guessed URLs or the model’s training cutoff.

## Search Providers
- Three providers are supported at launch: Ceramic.ai, Exa, and Linkup.
- All providers offer Zero Data Retention for requests routed through Cloudflare.
- Each provider adheres to Cloudflare’s verified bot‑crawling standards.

## Billing & Integration
- The API operates through AI Gateway, so each search request appears in gateway logs.
- Charges are applied to AI Gateway credits at the provider’s listed API price, with no extra markup.
- Users may also supply their own provider API key.

## Usage Examples
### REST API (cURL)
```bash
curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
  --request POST \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{
    "query": "What are some fun things to do in Salt Lake City as fall approaches?",
    "provider": "ceramic",
    "limit": 5,
    "options": { "gateway": { "id": "default" } }
  }'
```

### Worker with AI Binding (JavaScript)
```javascript
const response = await env.AI.websearch({
  gatewayId: "default",
  query: "What are some fun things to do in Salt Lake City as fall approaches?",
  provider: "exa",
  limit: 5,
});

const results = await response.json();
```

## Getting Started
- Refer to the “How to use Web Search API” documentation for detailed setup instructions.