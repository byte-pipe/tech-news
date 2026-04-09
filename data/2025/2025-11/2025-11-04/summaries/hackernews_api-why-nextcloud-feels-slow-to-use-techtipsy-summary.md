---
title: Why Nextcloud feels slow to use :: ./techtipsy
url: https://ounapuu.ee/posts/2025/11/03/nextcloud-slow/
date: 2025-11-03
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-04T11:14:56.545761
screenshot: hackernews_api-why-nextcloud-feels-slow-to-use-techtipsy.png
---

# Why Nextcloud feels slow to use :: ./techtipsy

# Why Nextcloud Feels Slow To Use

## Introduction

Nextcloud offers a feature-rich platform for self-hosting various applications under one roof. However, despite its attractive features and ability to replace multiple services in one instance, I find it difficult to use the platform. This article discusses the issues I've encountered with nextcloud.

## Issues With Nextcloud Resources

*   **Large JavaScript Loading Times**: The initial page load for a clean instance will take around 15-20 MB of JavaScript files downloaded and compressed.
*   **Bundling Common Libraries**: The core-common.jsbundle, which provides common functionality across different apps, contributes to the heavy JavaScript sizes at various stages of loading.

## Core Components Contributing to Slow Loading Times

### NotificationsApp Chunk.mjs


*   1.06 MB: The NotificationsApp chunk contains 2 small files included for basic functionalities.


### App-Specific Views (`Nextcloud Calendar app`, `Files app`)

### Notes App Basic Editor Main.js


*   4.36 MB: This chunk includes the code for the editor and other main functionality within Notes.app.



## Summary

Overall, my issues with nextcloud stem from its architecture, specifically how it bundles large JavaScript files without optimizing their compression ratios effectively. The core-common.jsbundle significantly contributes to large initial page loads, necessitating a significant amount of browser resources. This highlights several design trade-offs related to resource management, potentially contributing to the platform's noticeable performance shortcomings despite its promising features.
