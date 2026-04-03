---
title: CORS Almost Broke Me But Preflight Saved the Day - DEV Community
url: https://dev.to/techwithhari/cors-almost-broke-me-but-preflight-saved-the-day-21mk
site_name: devto
fetched_at: '2025-10-17T11:08:15.572139'
original_url: https://dev.to/techwithhari/cors-almost-broke-me-but-preflight-saved-the-day-21mk
author: Haripriya Veluchamy
date: '2025-10-14'
description: When I first built my frontend-backend setup, I thought everything would be smooth. Frontend hosted... Tagged with ai, fullstack, aws, web.
tags: '#ai, #fullstack, #aws, #web'
---

When I first built my frontend-backend setup, I thought everything would be smooth. Frontend hosted onS3, backend runningApollo GraphQL, andAPI Gatewaysitting in the middle to handle requests safely. Sounds simple, right?

Well… browsers had other plans.

Every request I made from the frontend to the backend kept failing.The console kept screaming:

Access to fetch at 'https://api.mybackend.com/graphql'
from origin 'https://myfrontend.com' has been blocked by CORS policy

Enter fullscreen mode

Exit fullscreen mode

I triple-checked my backend, triple-checked API Gateway. Everything was “working”… but the browser refused to cooperate.

### What I finally understood

CORS isn’t a bug. It’s the browser saying:

“Hold on, I don’t trust this request from another domain unless the server says it’s okay.”

And the browseralways starts with a preflight requestanOPTIONS requestthat asks the server:

* Am I allowed to send requests from this origin?
* Which HTTP methods can I use (GET, POST, etc.)?
* Which headers can I include?

If the server or the API Gateway doesn’t answer correctly, the browser blocks the actual request.That’s why Postman worked but the frontend didn’t.

### How I finally fixed it

The fix came in two parts:

1️⃣Handle preflight at the API GatewayI made sure that the OPTIONS request was correctly handled and that the gateway responded with the allowed origins, methods, and headers. Once this handshake worked, the browser let the real requests go through.

2️⃣Backend trusted the frontendOn the Apollo server, I set it up to allow requests from the frontend domain dynamically. Passing the frontend URL as an environment variable made deployments safe — no hardcoding, no accidental errors.

### Lessons learned

* Preflight is everything. If it fails, nothing else works.
* API Gateway must respond correctly to OPTIONS requests.
* Backend still needs to explicitly allow the frontend domain.
* Always manage allowed origins through environment variables.
* Debugging tip: check thepreflight request in the Network tab, not your GraphQL query itself.

After that, my frontend finally talked to my backend without errors — no more random CORS headaches or temporary hacks.

Sometimes thesmallest headerscause the biggest headaches 🥲.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
