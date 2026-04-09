---
title: CORS Almost Broke Me But Preflight Saved the Day - DEV Community
url: https://dev.to/techwithhari/cors-almost-broke-me-but-preflight-saved-the-day-21mk
date: 2025-10-14
site: devto
model: llama3.2:1b
summarized_at: 2025-10-18T11:15:27.677170
screenshot: devto-cors-almost-broke-me-but-preflight-saved-the-day-d.png
---

# CORS Almost Broke Me But Preflight Saved the Day - DEV Community

# CORS: The Browser's Refusal to Play Nice

## Introduction

Initially, a frontend application hosted on S3, powered by Apollo GraphQL, and using API Gateways to manage requests. However, every request made from the frontend to the backend suddenly failed with an "Access to fetch at 'https://api.mybackend.com/graphql' ... has been blocked" error.

## Conclusion

The issue was not a bug but rather a misunderstanding of the browser's CORS policy. The client-side browser made the following assumptions:

* The server would always accept the request from another domain (myfrontend.com).
* The allowed HTTP methods for requests to this domain were limited to GET, POST, etc.
* Any requested headers were allowed or disallowed.

## Problem Breakdown

1. Handling preflight at API Gateway
2. Backend trust and permission
3. Correct responses from API Gateway and backend

## Solution

### Handle Preflight at API Gateway

Ensuring the OPTIONS request was correctly handled by the API Gateway and responding with the correct options allowed the browser to proceed.

### Backend Trust and Permission

Allowing requests from the frontend domain dynamically on the Apollo server, and passing the frontend URL as an environment variable made it safe for deployments without hardcoded or accidental errors.

### Lessons Learned

* Preflight is crucial.
* API Gateway must respond correctly to OPTIONS requests.
* Background domains still require permission by the backend.
* Always manage allowed origins through environment variables.
* Test preflight in the Network tab, not your GraphQL query itself.
