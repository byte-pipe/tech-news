---
title: CORS Almost Broke Me But Preflight Saved the Day - DEV Community
url: https://dev.to/techwithhari/cors-almost-broke-me-but-preflight-saved-the-day-21mk
date: 2025-10-14
site: devto
model: llama3.2:1b
summarized_at: 2025-10-16T11:24:54.619874
screenshot: devto-cors-almost-broke-me-but-preflight-saved-the-day-d.png
---

# CORS Almost Broke Me But Preflight Saved the Day - DEV Community

**CORS Almost Broke Me But Preflight Saved the Day**

When building a frontend-backend setup with S3 as the frontend, Apollo GraphQL for backend, and API Gateways in the middle to handle requests safely, I thought everything would be smooth. However, every request from my frontend to the backend continued to fail due to browser security restrictions.

The console kept screaming:

```
Access to fetch at 'https://api.mybackend.com/graphql'
from origin 'https://myfrontend.com'
has been blocked by CORS policy
```

But I had double-checked my backend, triple-checked API Gateway. It seemed everything was "working" from the frontend's perspective... until I tried Postman.

**What I finally understood**

CORS isn't a bug; it's the browser saying:

`"Hold on, I don’t trust this request from another domain unless the server says it’s okay."`
and always starts with a preflight (OPTIONS) request asking `* Am I allowed to send requests...?`

If the server or API Gateway doesn’t answer correctly, the browser blocks the actual request. Postman worked but my frontend didn't.

**How I finally fixed it**

The fix came in two parts:

1. **Handle preflight at the API Gateway**

I made sure that the OPTIONS request was correctly handled and the gateway responded with allowed origins, methods, and headers. Once this handshake worked, the browser let the real requests go through.

2. **Backend trusted the frontend**

On the Apollo server, I set it up to allow requests from the frontend domain dynamically by passing the frontend URL as an environment variable. This made deployments safe – no hardcoding, no accidental errors.

**Lessons learned**

* Preflight is everything. If it fails, nothing else works.
* API Gateway must respond correctly to OPTIONS requests.
* Backend still needs to explicitly allow the frontend domain.
* Always manage allowed origins through environment variables.
* Debugging tip: check the preflight request in the Network tab, not your GraphQL query itself.

**After that, my frontend finally talked to my backend without errors**

Sometimes, the smallest headers can cause the biggest headaches. Create templates for quick answers or store snippets for re-use.
