---
title: I Built a New Tab Extension for DEV - DEV Community
url: https://dev.to/sizzlebop/i-built-a-new-tab-extension-for-dev-4kmm
site_name: devto
content_file: devto-i-built-a-new-tab-extension-for-dev-dev-community
fetched_at: '2026-10-21T15:51:36.082904'
original_url: https://dev.to/sizzlebop/i-built-a-new-tab-extension-for-dev-4kmm
author: Jessica Doering
date: '2026-10-18'
description: I spend a lot of time on DEV these days. Reading posts, finding interesting projects, participating... Tagged with showdev, webdev, opensource, javascript.
tags: '#showdev, #webdev, #opensource, #javascript'
---

Includes tag filters and offline caching details

I spend a lot of time on DEV these days. Reading posts, finding interesting projects, participating in challenges, and occasionally writing something myself.

I also like daily.dev. Having a feed of developer content right there whenever I open a new tab is pretty convenient.

So naturally, I started thinking... what if I had something like that, but just for DEV?

And because apparently I can't have an idea without turning it into another project, I built one.

It's calledDEV Tab, and it's a free, open-source browser extension that replaces your new tab page with a feed of posts from DEV.

It's now available on the Chrome Web Store.

Install DEV Tab for Chrome

Firefox support is built too, and the add-on is currently awaiting review. I'll update this post with the link once it's approved.

## A little more than just a feed

The original idea was pretty simple. Open a new tab, see what's happening on DEV, and click through to anything interesting.

But, as usual, I kept thinking of things to add.

You can browse posts from Today, This Week, Rising, and Latest, along with dedicated sections for trends, events, podcasts, and videos.

There are also tag filters, so you can quickly jump between subjects you're interested in. You can save your favorite tags, hide tags you'd rather not see, and follow posts from specific DEV organizations.

A few other things I added:

* Search directly from the new tab page.
* Keyboard navigation using arrow keys and Enter.
* A compact view if you'd rather see more posts and fewer images.
* Reaction counts and previews of the three newest comments.
* A shortcut to create a new DEV post.
* Feed caching, so opening a new tab doesn't mean waiting for everything to load again.

Nothing particularly revolutionary here. I just wanted a convenient way to explore DEV without having to go looking for things.

## Then I decided it needed a dashboard

This part wasn't in my original plan, but I spend enough time writing on DEV that I thought having a better overview of my own activity would be useful.

If you add your DEV API key in the extension settings, you unlock some additional features, including a personal dashboard.

The dashboard includes your follower count, views, reactions, comments, and new followers, with options to look at the last 7, 30, or 90 days.

There's also a daily views chart, an activity heatmap that lets you browse previous years, and a list of your published posts and drafts.

You can see recent followers, top supporters, and where your readers are coming from, too.

I particularly like having the activity heatmap and post statistics together. It's interesting to look back and see when I was active and how different posts performed.

The dashboard screenshot above uses fictional example data, by the way.

## Connecting your DEV account is completely optional

You don't need an account or API key to use the extension. The public feeds, search, filters, and other browsing features work without one.

But if you do connect your DEV account, you also get access to your personal feed based on the tags you follow, your reading list, and semantic search.

You can generate an API key from yourDEV settings.

The extension doesn't have a backend, analytics, or tracking. Your API key stays in your browser's local extension storage and is only sent to DEV for authenticated API requests.

I wanted to keep it simple and avoid introducing a separate service just to display information DEV already makes available.

## A few limitations

There are a couple of things I would have liked to include but couldn't because of the DEV API.

For example, you can't directly react to posts, leave comments, or save articles to your reading list from the extension.

You can view reaction counts and preview comments, but interacting with a post opens it on DEV itself.

I'd love to have those actions directly in the feed someday, but for now, that's a limitation of what's available through the API.

## Built with WXT, React, and TypeScript

I usedWXTfor the extension framework, along with React and TypeScript.

This was my first time using WXT, and I really liked being able to build for Chrome and Firefox from the same codebase.

One thing I spent some time on was making sure the feed wouldn't constantly refetch everything whenever a new tab opened. The first page of each feed gets cached for ten minutes, and previously loaded posts can still appear if you're offline.

It's a small thing, but when you're replacing something as frequently used as the new tab page, I think it matters.

## Give it a try!

DEV Tab is open source, so you can take a look at the code, report bugs, suggest features, or contribute if you'd like.

Chrome Web Store

GitHub

The Firefox version is currently awaiting approval, and I'll add the link here when it's published.

This started as one of those little "wouldn't it be nice if..." ideas, and somehow turned into a full browser extension with a personal analytics dashboard.

I guess that's what happens when you keep finding things you want to build.

If you use DEV regularly, I'd love to hear what you think! And if there's something you'd find useful in a future version, let me know.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (35 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse