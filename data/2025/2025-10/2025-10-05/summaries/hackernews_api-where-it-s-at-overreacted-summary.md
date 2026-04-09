---
title: "Where It's at:// — overreacted"
url: https://overreacted.io/where-its-at/
date: 2025-10-02
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-05T11:21:28.165104
screenshot: hackernews_api-where-it-s-at-overreacted.png
---

# Where It's at:// — overreacted

# Where It's at://

The AT protocol, also known as hyperlinked JSON (hJSON), is a unique way of representing online links in the internet protocol (TCP/IP) stack. At its core, hJSON allows multiple web servers to share information about an article when it is published on their sites.

### What is an at:// URI?

An at://URI is an address that points to multiple web servers that host similar articles or content. In this case, the provided examples show specific at://URIs:

*   **at://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z**
*   **at://danabra.mov/sh.tangled.feed.star/3m23ddgjpgn22**
*   **at://tessa.germnetwork.com/pub.leaflet.publication/3lzz6juivnc2d**

### Resolving an at:// URI

To find the corresponding JSON, you need to know how to interpret these URIs and navigate through them.

#### Using an SDK or Client App

The hJSON structure can be resolved using various client apps such as LSDs (Layered Storage Devices) for Android or Taproot for iOS. These apps act as intermediaries between your device and the internet, connecting your app to different servers within a network, allowing you to browse through multiple web pages. They provide an efficient way to access related content without having to visit each individual site individually.

#### The HJSON Structure

The provided example shows a JSON structure that could be obtained from an at://URI in hJSON format:

```json
{
    "uri": {
        "at://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z",
        "cid": "bafyreiae4ehmkk4rtajs5ncagjhrsv6rj3v6fggphlbpyfco4dzddp42nu"
    },
    "value": {
        "text": [
            "posting from did:web, like a boss"
        ],
        "type": "app.bsky.feed.post"
    },
    "langs": ["en"]
}
```

In this structured representation of hJSON:

-   The JSON object has two main parts: the `uri` and the `value`.
-   The `uri` section contains one or more addresses, referred to by their short names (e.g., `at://ruuuuu.de/app.bsky.feed.post/3lzy2ji4nms2z`).
-   The `value` part of the JSON object represents a piece of data containing text information.
-   The `lang` section lists the languages associated with this specific part of the data.

**Understanding the Purpose**

The AT protocol allows for easy access to various pieces of content across different servers and sources. This structure is particularly useful in situations where you need to find related materials or navigate through a larger network to discover new information.
