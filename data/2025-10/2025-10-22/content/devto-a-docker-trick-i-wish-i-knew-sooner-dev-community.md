---
title: A Docker Trick I Wish I Knew Sooner - DEV Community
url: https://dev.to/joybtw/a-docker-trick-i-wish-i-knew-sooner-23of
site_name: devto
fetched_at: '2025-10-22T11:16:58.491883'
original_url: https://dev.to/joybtw/a-docker-trick-i-wish-i-knew-sooner-23of
author: Joy Biswas
date: '2025-10-16'
description: While building a Docker image recently, I needed to download a file using curl. My first instinct was... Tagged with docker, devops, productivity.
tags: '#docker, #devops, #productivity'
---

While building a Docker image recently, I needed to download a file usingcurl. My first instinct was to installcurlin the container, make the request, and move on. But then I discovered Docker has a built-in way to handle this, and it's cleaner.

## The Old Way: Installing curl

Here's what I was doing initially:

FROM
 alpine:latest

WORKDIR
 /app

RUN
apk add
--no-cache
 curl

RUN
curl
-sS
 https://example.com/somefile.txt
-o
 /app/somefile.txt

EXPOSE
 8080

Enter fullscreen mode

Exit fullscreen mode

This works, but it adds unnecessary bloat. You're installingcurljust to download a file, increasing your image size and adding an extra dependency you don't really need at runtime.

## The Better Way: Using Docker's ADD Instruction

Docker'sADDinstruction can fetch remote files directly without requiringcurlorwget:

FROM
 alpine:latest

WORKDIR
 /app

ADD
 https://example.com/anotherfile.json /app/anotherfile.json

EXPOSE
 8080

Enter fullscreen mode

Exit fullscreen mode

Much simpler. No extra packages, no additional layers, and the intent is clearer.ADDpulls the file at build time and places it exactly where you need it.

## Why This Matters

### Smaller Image Size

Every package you install adds megabytes to your final image. Skippingcurlkeeps things lean, especially important when you're optimizing for production or working with constrained environments.

### Fewer Dependencies

Less tooling means fewer potential security vulnerabilities and a simpler dependency tree. Your container only contains what it actually needs.

### Cleaner Dockerfiles

Using built-in instructions makes your Dockerfile more readable and idiomatic. Other developers (or future you) will immediately understand what's happening.

## When to Use Each Approach

UseADDwhen:

* You're downloading a single file from a URL
* The file doesn't require authentication
* You want to keep your image minimal

Stick withcurlorwgetwhen:

* You need more control over the download (headers, authentication, retries)
* You're fetching multiple files in a complex workflow
* You need to process or validate the downloaded content before using it

Have you usedADDfor remote files before, or do you have other Docker tricks worth sharing?Let me know in the comments! 😊

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
