---
title: Revamped RSS Feed Imports - DEV Community
url: https://dev.to/devteam/revamped-rss-feed-imports-3j1e
site_name: devto
content_file: devto-revamped-rss-feed-imports-dev-community
fetched_at: '2026-03-10T11:15:47.904749'
original_url: https://dev.to/devteam/revamped-rss-feed-imports-3j1e
author: Jon Gottfried
date: '2026-03-09'
description: You can now add multiple RSS feed imports, monitor their status, and assign each one to different... Tagged with forem, devto, rss.
tags: '#forem, #devto, #rss'
---

You can now add multiple RSS feed imports, monitor their status, and assign each one to different default authors or organizations.

DEV (and Forem) have supported RSS feed imports for a long time. They are the primary way to automatically syndicate posts from an external blog into the DEV community, complete with proper canonical URL referencing to preserve your SEO ranking. Historically, each user was limited to one RSS feed that they could sync to DEV.

Let's check out the brand new upgraded functionality. If you head over to the RSS Import Feeds page under your Dashboard, you can add your first RSS feed from your (or your team's) external blog.

As part of the import process, you can set which organization on DEV these imported articles will be associated with. You can also set a default author. If the author of the imported post does not have an account on DEV, the article will be listed under your default author instead.

You still have the same two options as before, toMark the RSS source as canonical URL by default(which we recommend doing for SEO purposes, unless you are fully moving your blog to DEV and shutting down the old version). You can alsoReplace self-referential links with DEV Community-specific links- this option will update URLs inline to point to the imported version of an article on DEV instead of the original version. This is useful if you're migrating your entire blog onto DEV.

Once you've added your Feed Source, a background job gets queued up to import your posts. Just refresh the page a few minutes later to see the status. If it was successful, you'll see a list of imported drafts under your Import History. You can also see which articles were skipped or errored out. If there's no new articles at all, it will be shown under the routine checks dropdown at the bottom of the page.

Go through each edited article, edit the draft, and publish your post. In some situations you may need to publish it by modifying the markdownpublishedtag to be set totrueinstead of false. Saving it will then publish the post.

On published posts with canonical links, you'll see a linkback on the post author line.

We look forward to seeing y'all syndicate your blogs into the DEV community and to any feature feedback you have here!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
