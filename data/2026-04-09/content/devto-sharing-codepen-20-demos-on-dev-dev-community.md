---
title: Sharing CodePen 2.0 demos on DEV - DEV Community
url: https://dev.to/alvaromontoro/sharing-codepen-20-demos-on-dev-273
site_name: devto
content_file: devto-sharing-codepen-20-demos-on-dev-dev-community
fetched_at: '2026-04-09T11:24:57.369858'
original_url: https://dev.to/alvaromontoro/sharing-codepen-20-demos-on-dev-273
author: Alvaro Montoro
date: '2026-04-07'
description: How to share CodePen 2.0 demos on DEV. Tagged with meta, dev.
tags: '#meta, #dev'
---

Workaround for the new URL format

If you've tried the new CodePen 2.0 editor, you may have noticed that the URL format has changed. And if you've tried sharing one of these demos here on DEV, you've probably also noticed that it doesn't work with the standard CodePen embed code:

{% codepen https://codepen.io/editor/alvaromontoro/pen/019d657e-d7bc-746a-9bc3-4df2244c97cc/24ac30a5aad27b2b927702d3557c6e70 %}

Enter fullscreen mode

Exit fullscreen mode

If you try adding that code to a DEV article, you'll get this error:

So, the new URL doesn't work yet... but what if you still want to include it in a DEV article? Good news: you can! You just need to use the hash for the CodePen demo instead. Here's how to find it:

1. Click on theShare iconin the top-right corner
2. Select "Embed"
3. A modal will open, make sure "HTML (recommended)" is selected
4. In the code, look fordata-slug-hashanddata-user
5. Copy those values.
6. Use them to generate a classic CodePen URL in the embed tag:{% codepen https://codepen.io/[USER]/pen/[SLUGH_HASH] %}
7. That's it!

In the screenshot above, the hash is "MYjBBrm" and the user is "alvaromontoro", that makes the URLhttps://codepen.io/alvaromontoro/pen/MYjBBrm, so the embed tag becomes:

{% codepen https://codepen.io/alvaromontoro/pen/MYjBBrm %}

Enter fullscreen mode

Exit fullscreen mode

Which works just fine (it will only show the preview, not the code):

To be fair, I expect the DEV team to fix this soon. But in the meantime, this is a simple workaround for sharing CodePen 2.0 demos.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse