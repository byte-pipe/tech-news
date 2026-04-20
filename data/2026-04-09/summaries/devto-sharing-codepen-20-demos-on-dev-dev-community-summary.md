---
title: Sharing CodePen 2.0 demos on DEV - DEV Community
url: https://dev.to/alvaromontoro/sharing-codepen-20-demos-on-dev-273
date: 2026-04-07
site: devto
model: llama3.2:1b
summarized_at: 2026-04-09T11:32:03.075318
---

# Sharing CodePen 2.0 demos on DEV - DEV Community

**Sharing CodePen 2.0 Demos on DEV: A Workaround**
=====================================================

If you have tried the new CodePen 2.0 editor but encountered issues with sharing demos, you are not alone. Unfortunately, it seems like the URL format has changed.

To work around this limitation, you can use a workaround that is accepted by DEV: using the hash in the codepen embed tag instead of the base URL.

**Finding the Hash**
--------------------

Here's how to find your hash:

1. Click on the Share icon in the top-right corner
2. Select "Embed"
3. A modal will open, make sure "HTML (recommended)" is selected
4. In the code, look for `data-slug-hash` and `data-user`.
5. Copy those values.

**Generating a Classic CodePen URL**
-------------------------------------

Once you have found your hash, use it to generate a classic CodePen URL in the embed tag:

```markdown
{% codepen https://codepen.io/[USER]/pen/[SLUGH_HASH] %}
```

In this case:

* `[USER]` is replaced with the actual username from the Share modal
* `[SLUGH_HASH]` is left as it is, containing your hash

This should now work correctly and display only the preview of your CodePen demo.

**Why This Works**
------------------

This workaround allows DEV to still share your CodePen 2.0 demos even if they cannot use the new base URL format out-of-the-box. By using the hash, you are essentially creating a link that has been validated by DEV and will work as expected.

While this is not an official fix from DEV, it works surprisingly well in practice. We hope this helps alleviate any inconvenience caused by this change!
