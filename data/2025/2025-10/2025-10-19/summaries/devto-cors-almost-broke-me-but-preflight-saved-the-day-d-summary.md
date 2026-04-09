---
title: CORS Almost Broke Me But Preflight Saved the Day - DEV Community
url: https://dev.to/techwithhari/cors-almost-broke-me-but-preflight-saved-the-day-21mk
date: 2025-10-14
site: devto
model: llama3.2:1b
summarized_at: 2025-10-19T11:18:55.287600
screenshot: devto-cors-almost-broke-me-but-preflight-saved-the-day-d.png
---

# CORS Almost Broke Me But Preflight Saved the Day - DEV Community

Here is a concise and informative summary of the article:

**Summary**

The author built a frontend-backend setup using S3 as the front end and Apollo GraphQL as the backend. However, they encountered frequent failures when making requests from their frontend to the backend due to CORS policy restrictions on certain domains. The author's browser blocked these requests without error, preventing their application from functioning correctly.

**Key Points**

* CORS is not a problem itself, but rather a warning from the browser indicating that it does not trust requests from different origins (domains).
* The issue lies in the preflight request sent by the browser to check for allowed domains and HTTP methods.
* To resolve this, the author:
	+ Modified API Gateway to respond correctly to OPTIONS requests with the correct allowed origins, methods, and headers.
	+ Configured Apollo server to allow incoming requests from the frontend domain dynamically, using environment variables.

**Lessons Learned**

* Preflight is a critical step that should be taken to resolve CORS issues.
* Ensuring API Gateway responds correctly is essential for making requests successfully.
* Explicitly configuring the backend to receive requests from the frontend domain is necessary for resolving CORS policy errors
* Using templates for FAQs and storing snippets can help with re-use and debugging.

**Template Example**

Here's a basic template example of how you could implement a simple FAQ template:
```markdown
# FAQs

## Q: How do I set up CORS on my backend?
A: Configure your API Gateway to allow requests from the frontend domain dynamically using environment variables.
```
You can then use this template to answer frequently asked questions and store snippets for re-use.
