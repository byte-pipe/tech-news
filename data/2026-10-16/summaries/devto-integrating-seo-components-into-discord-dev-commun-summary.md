---
title: Integrating SEO Components into Discord - DEV Community
url: https://dev.to/thomasbnt/integrating-seo-components-into-discord-2d8g
date: 2026-10-13
site: devto
model: llama3.2:1b
summarized_at: 2026-10-16T15:13:16.019873
---

# Integrating SEO Components into Discord - DEV Community

**Replacing Open Graph Cards with Custom Previews**

Discord has introduced a new option to replace the default Open Graph card with a custom preview, featuring formatted text, an image gallery, and buttons. The process involves several steps to ensure proper functionality.

**Key Requirements**

* A site served over HTTPS
* Open Graph tags already present (required, even with an `embedcomponent` tag)
* Server-side rendering (HTML must contain tags in the response itself, not after a JavaScript script)
* Discordbot crawler allowed if a WAF, CDN, or rate limiter is in front of the site
* Embed component's JSON payload ready

**Default Behavior**

Without Open Graph tags, Discord generates a default card. The process works as follows:

1. Sends a request to the URL
2. Reads the HTML returned by the server
3. Looks for Open Graph tags in the `head` element
4. If found, a card is automatically generated

**Custom Preview**

To replace the default card with a custom preview:

1. Introduce required Open Graph tags in the `head` element (content, `og:title`, `og:description`, `og:image`, `og:url`, `name="twitter:card"`)
2. Set `og:url` to the desired URL
3. Add an embedded component to the HTML response (content, image size, etc.)
4. Ensure the crawler identifies itself with the user-agent `Mozilla/5.0` and allows Discordbot if blocked by a WAF or rate limiter
5. Cache the custom preview for approximately 30 minutes

**Optional Enhancements**

The custom preview can be enhanced by exploring more advanced Open Graph tags and additional metadata, such as:

* Description and keywords using `og:description` and `og keywords`
* Twitter Card tags for multimedia and interactive content
* Custom image sizes and formats using `og:image` with `srcset` and `sizes`

By following these steps, developers can create a seamless custom preview experience for their Discord channels, enhancing the user experience and content presentation.