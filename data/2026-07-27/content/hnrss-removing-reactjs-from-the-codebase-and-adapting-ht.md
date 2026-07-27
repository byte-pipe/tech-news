---
title: Removing React.js from the codebase and adapting HTMX for UI interactivity | Roadmap | Misago Forums
url: https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/
site_name: hnrss
content_file: hnrss-removing-reactjs-from-the-codebase-and-adapting-ht
fetched_at: '2026-07-27T19:33:07.475425'
original_url: https://misago-project.org/t/removing-reactjs-from-the-codebase-and-adapting-htmx-for-ui-interactivity/1267/
date: '2026-07-27'
tags:
- hackernews
- hnrss
---

Here's how Misago works currently:

1. You requesthttps://misago-project.org.
2. Django view gathers data to render list of threads.
3. Django view renders template that contains almost complete HTML with list of threads, but also includes a JSON with same data used to render this HTML. And there is no interactivity because forms are disabled.
4. JavaScript downloads.
5. JavaScript runs, reads JSON embedded in the page's body and replaces most of HTML rendered from Django templates with HTML fromReact.jscomponents. Buttons become active, and timestamps in UI swap.

This approach has some problems:

* A lot of pages in Misago are implemented twice: as Django templates andReact.jscomponents.
* People who start customizing HTML get burned because they edit Django templates and see their changes flash for a second on a site before being replaced byReact.jsHTML which they didn't know they also need to customize.
* Every view accessible to both users and guests needs to be done twice: as Django view with templates, and asReact.jsroute with components. It also requires an API and JSON serializers to power data fetching.
* JSON serialization to pre-bake data forReact.jsapp slows down response generation.
* A large part of translation messages is duplicated, living in bothdjango.poanddjangojs.pofiles. JavaScript translation files also increase the initial download size.
* Lots of JavaScript can kill performance, especially on older and slower mobile devices.
* Enabling plugins to replace or inject custom HTML to the page requires for those plugins to implement both Django templates andReact.jscomponents. And Misago will need to implement a JavaScript build step as part of site build inmisago-docker. Plugin devs need to know both.

I've considered two solutions to this problem:

1. Drop Django views and templates, only keep those in minimal versions to keep search engine bots happy. Focus on implementing an API and having all UI asReact.jsapp.
2. Reduce Django to API and use JavaScript framework with serverside rendering, eg.Next.jsorRemix.run.

But here's a thing: there's a lot of forum software out there that still does the old way of rendering as much as possible on the server and using some JavaScript on client to improve its interactivity here and there. And people arehappy with that. And this approach hasnoneof the above issues.

Internet forum software has plenty of interactivity, but this interactivity is isolated to specific places on the page. Moderation actions, watching a thread, writing a reply, seeing last notifications, voting in a poll. All this stuff can be achieved withoutReact.jsand was achieved without it for years before we've decided that full page reload is something that needs to be avoided.

Now, what's HTMX?HTMXis a tiny library that lets developers specify parts of HTML as dynamic islands that can be swapped by new server-rendered HTML on interaction. For example, list of actual threads is one such (large) island. With little bit of HTMX included in Django template, changing current category on threads list could pull new HTML from Django only for new threads list for selected category, while keeping rest of the page's HTMX (eg. already loaded search results in navbar) unchanged. Misago's backend code would only need to be changed to return only the HTML for this island when request comes from HTMX, instead of full page. There's no need to do any JSON serialization or write dedicated JavaScript orReact.js.

HTMX is declarative way of doing$.get("url", "#outlet")we've did in jQuery 20 years ago. Or Rails Turbolinks. I can't believe I am writing this, but this is the way for forum software if you hate endless scrolling or want to keep things simple otherwise.