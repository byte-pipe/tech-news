---
title: A Docker Trick I Wish I Knew Sooner - DEV Community
url: https://dev.to/joybtw/a-docker-trick-i-wish-i-knew-sooner-23of
date: 2025-10-16
site: devto
model: llama3.2:1b
summarized_at: 2025-10-21T11:14:42.314471
screenshot: devto-a-docker-trick-i-wish-i-knew-sooner-dev-community.png
---

# A Docker Trick I Wish I Knew Sooner - DEV Community

# Docker Trick I Wish I Knew Sooner - DEV Community
=====================================================

**The Old Way: Installing curl**

When building a Docker image, it's easy to download a file using `curl` and make another request. However, installing all the dependencies required by `curl` in the container can be unnecessary.

### The Better Way: Using Docker's ADD Instruction

Docker provides an `[ADD]` instruction that allows you to fetch remote files directly without requiring `curl` or other external tools.

## why this matters
### Smaller Image Size

By using `[ADD]`, we reduce the size of our Docker image. This is especially important in production environments where every kilobyte counts.

### Fewer Dependencies

Since we're using `[ADD]`, fewer dependencies are added to the container, which also reduces its "bloat".

### Cleaner Dockerfiles

Using `[ADD]` makes it simpler to read and understand your Dockerfile. It's more idiomatic and clear-cut.

## When to Use Each Approach
### Use [ADD] when:
* You're downloading a single file from a URL
* The file doesn't require authentication
* You want to keep your image minimal

```dockerfile
FROM alpine:latest

WORKDIR /app

ADD http://example.com/anotherfile.json /app/anotherfile.json

EXPOSE 8080

CMD ["echo", " downloading..."]
```

### Stick with [curl] or wget when:
* You need more control over the download (headers, authentication, retries)
* You're fetching multiple files in a complex workflow
* You need to process or validate the downloaded content before using it
