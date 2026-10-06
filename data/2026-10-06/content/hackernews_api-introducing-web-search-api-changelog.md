---
title: Introducing Web Search API · Changelog
url: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/
site_name: hackernews_api
content_file: hackernews_api-introducing-web-search-api-changelog
fetched_at: '2026-10-06T16:47:52.849797'
original_url: https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/
author: tosh
date: '2026-10-05'
description: Search the web from your AI agents and applications through AI Gateway with Ceramic.ai, Exa, and Linkup.
tags:
- hackernews
- trending
---

View RSS feeds
		

			Subscribe to RSS
		
Back to all posts
October 2, 2026

## Introducing Web Search API

AI Gateway
Web Search API
Copy as Markdown
|
View as Markdown
|
Agent setup

Web Search APIis now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers:Ceramic.ai, Exa, and Linkup. All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare'sverified botcrawling standards.

Web Search API runs throughAI Gateway, so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:

curl
 https://api.cloudflare.com/client/v4/accounts/
$CLOUDFLARE_ACCOUNT_ID
/ai/websearch/
 \

 --request
 POST
 \

 --header
 "Authorization: Bearer 
$CLOUDFLARE_API_TOKEN
"
 \

 --header
 "Content-Type: application/json"
 \

 --data
 '{

 "query": "What are some fun things to do in Salt Lake City as fall approaches?",

 "provider": "ceramic",

 "limit": 5,

 "options": { "gateway": { "id": "default" } }

 }'

Or from a Worker with the AI binding:

const
 response
 =
 await
 env.
AI
.
websearch
({

	gatewayId: 
"default"
,

	query: 
"What are some fun things to do in Salt Lake City as fall approaches?"
,

	provider: 
"exa"
,

	limit: 
5
,

});

const
 results
 =
 await
 response.
json
();

To get started, refer toHow to use Web Search API.