---
title: 'EmDash 1.0: the stable CMS with a secure plugin registry | Cloudflare Blog'
url: https://blog.cloudflare.com/emdash-cms-plugin-registry
site_name: tldr
content_file: tldr-emdash-10-the-stable-cms-with-a-secure-plugin-regi
fetched_at: '2026-09-28T23:42:07.311133'
original_url: https://blog.cloudflare.com/emdash-cms-plugin-registry
date: '2026-09-28'
published_date: '2026-09-28T13:00:00.000Z'
description: EmDash 1.0 is a stable, open source CMS built for Astro, with agent-friendly workflows, secure sandboxed plugins, and a decentralized registry that keeps publishers in control.
tags:
- tldr
---

When weintroduced EmDash on April 1as the “spiritual successor to WordPress”, the buzz was hard to ignore. Walking around a WordPress conference that month, we couldn’t walk far without hearing murmurs about EmDash from fellow attendees.

But alongside the excitement and curiosity has been a seed of doubt among some in the industry. Was this just an April Fools’ joke?

It was not. Today, we are releasing EmDash 1.0: a stable, free, and open source CMS built on Astro, ready to power a production website, your agency’s vibe-coding platform, or your hosting company’s site-building experience.

Developers build with Astro, editors manage content through the EmDash admin, and agents can work through the API, CLI, or built-in MCP server. EmDash 1.0 brings those pieces together with production-tested editorial, media, localization, migration, and deployment workflows.

We are also launching a decentralized plugin registry that lets developers publish without handing ownership of their identity or releases to a central marketplace, while site owners can discover and install their plugins directly from inside EmDash.

The EmDash post editor.

## The road to 1.0

Since EmDash's first beta, developers have launched real websites with it. Even so, we kept hearing a reasonable response: “This looks interesting. Let me know when it is 1.0.” Before relying on EmDash for their sites, they wanted confidence that it was stable, secure, that upgrades would protect their content, and that we are fully committed to maintaining it.

EmDash 1.0 is our answer to that. For the past five months, we have worked with contributors and production users on the parts of the CMS that every site depends upon: data safety, database migrations, editorial workflows, localization, plugin security, performance, and the reliability of the admin, API, MCP, and media experiences.

Real deployments shaped much of that work, uncovering edge cases and identifying needs that only show up when a site is serving real traffic and being used by real teams of editors.

As one example of this,Avuluxconverted a custom microsite to EmDash after dealing with the maintenance burden of WordPress for too long. Since EmDash is an agent’s best friend, using theEmDash Agent Skillshelped that transition take less than a day to complete.

“The site had to be fast to use and simple for our team to update,” says Greg Barbosa, Director of Innovation and Systems at Avulux. “WordPress had become the opposite of that. With EmDash, we now have a shared platform that developers can extend and marketers can edit content."

In August, wemigrated the Cloudflare Blog to EmDashas part of our “Customer Zero” approach. Working alongside our content engineering team provided actionable insights around localization, media management, the admin editor experience, and scaling. Comfortably handling the traffic load for the Cloudflare Blog meant being ready for millions of pageviews per week, spikes up to 5,000 requests per second (RPS) of legitimate traffic, or sporadic DDoS attacks. The optionalKV object caching,Hyperdrive database adapter, andWorkers Cache compatibilitywere all features spawned from our migration project that are widely available to all customers now.

## Built in public, open to everyone

A CMS sits at the heart of an organization’s web presence. It is trusted with its most important data, and is often used by dozens of editors every day. They need to be able to know they can rely on it, without fear of vendor lock-in or changing business priorities. For that reason, EmDash iscompletely free and open source, using the flexible and permissive MIT license.

EmDash 1.0 could not exist without its open-source development community. At the time of writing, more than 175 people have contributed to the project, across more than 1,800 commits. The rise of agentic coding tools has presented both challenges and opportunities to open-source projects, and we have deliberately built a project where the agents can help the human developers, rather than being overwhelmed by them.

We are particularly grateful to the core group of the most dedicated contributors, who between them have shipped hundreds of improvements to all areas of the project. They include@swissky,@danielmlr,@MA2153,@marcusbellamyshaw-cell, and dozens of others. Contributors have translated EmDash into 25 languages, from Arabic to Ukrainian.

Particular recognition is due to Noah Pham, who joined Cloudflare as an intern and became EmDash’s second maintainer alongside Matt. Noah contributed more than 80 changes, taking ownership of major parts of the media library, content editor, and admin interface. We have said thatinterns ship meaningful work at Cloudflare; Noah’s work is now at the heart of EmDash 1.0.

There is plenty more to build, and contributing does not have to mean writing code. If you want to help with code, translations, documentation, testing, design, issue triage, answering questions, or just welcoming new users,join over 800 others in the EmDash community on Discord.

## A growing ecosystem

A content management system thrives when the ecosystem around it is healthy and supported. We’ve been excited by the theme companies, plugin shops, agencies, and platforms who are creating new services and products using EmDash.

* Lexington Themesoffers 44 Astro themes with EmDash variants, giving teams a beautiful and functional starting point for their site, complete with reusable components and built-in content collections.
* Urumiis using their WooCommerce expertise to release EmDash’s first eCommerce plugin.
* Empressis launching a platform for multi-brand entities, offering the flexibility of managing a fleet of sites with natural language or a conventional CMS admin panel.

“Empress's delightful multisite experience would not be possible without the foundations EmDash has laid: sites that are fast, safe to extend, and easy for people and agents to read and act on,” says Raj Makker, Empress’s founder. “EmDash unlocks powerful control over a website, and Empress builds on it to give you complete control over as many sites as you want. We're excited to be part of this journey.”

## A plugin registry that does not own the ecosystem

The EmDash plugin registry

With EmDash 1.0, developers can publish sandboxed plugins and site owners can discover, inspect, and install them from theEmDash plugin registry.

Traditional plugin registries usually combine three roles: they provide the publisher’s account, hold the authoritative package record, and operate the catalog where users discover it. That is convenient, but it also makes one company the gatekeeper for both identity and distribution. If an account is suspended, a listing is removed, the rules change, or the service shuts down, publishers cannot take the same identity and release history somewhere else.

EmDash separates the plugin from the catalog. Publishers retain control of their packages and release history, while EmDash provides a convenient place for people to find and install them. Other services can index the same publications, build their own catalogs, and apply their own policies without requiring developers to start again.

The EmDash catalog applies default content moderation to the names, descriptions, links, and images it displays. Moderation can hide harmful or inappropriate material from this catalog, but it does not rewrite a release, take ownership of the plugin, or erase the underlying publication.

The registry is built onAT Protocol(atproto), a decentralized network protocol that powers Bluesky and a growing ecosystem of applications. Plugin authors publish with anAtmosphereaccount, the portable identity also used across these applications. The package and release records are signed by the publisher and stored in the publisher's own account.

EmDash hosts the default registry services so publishers and site owners can use them without running infrastructure themselves. We hope others will build new catalogs, moderation systems, publishing tools, and other services we have not imagined yet. To help this, we have released all of our services as open-source software, includingthe aggregatorthat powers the plugin registry,the labeler servicethat uses Workers AI to moderate package descriptions, and anAstro live content loaderto make it easy to include plugin listings in any Astro site. We are excited to see what the community will build with them!

There’s no centralized controller that can take over plugins or remove them on a whim. We believe the security of plugins and the registry should be baked into code, rather than trusting any central authority or code of conduct.

Decentralized publishing does not mean accepting unverified code. Atproto repositories use signed Merkle Search Trees, so an inclusion proof connects the exact release record to a signed commit from the publisher’s account. EmDash can therefore verify the record independently instead of trusting the catalog’s copy. It then checks the plugin’s checksum, package name, version, requested access, and any required build provenance, and confirms that the downloaded bundle matches the signed record.

The registry supports free plugins today, and we aim to add support for paid plugins in future, with the same decentralized model as now. We are watching theAtproto Spaces Alphawith interest. Anybody should be able to run a secure, paid plugin marketplace. We want publishers to be able to make money from their software.

For now, plugin authors can publish useful software without asking permission from EmDash — and site owners can understand exactly what that software is allowed to do before they run it.

## Plugins with clear boundaries

Plugins are the core of a CMS ecosystem. They save site developers from rebuilding the same integrations and workflows, while giving experts a way to share their best practices — and potentially build a software business.

Agents make that reuse even more valuable. An agent can build a one-off integration, but it still has to understand the problem, generate and test the code, and maintain it afterward. A plugin captures that work. Another agent can install and configure a proven solution instead of starting again from scratch.

That convenience creates a serious security concern: plugins are code you did not write, operating alongside valuable content and customer data. With WordPress, plugins run inside the same PHP process as the rest of the application, with direct access to its database, filesystem, and network. A contact-form plugin can technically read unpublished posts, modify another plugin, or send data anywhere. Site owners must trust that it will not — and that a future update will not change its behavior.

Sandboxed EmDash plugins use a different model. Each plugin runs in an isolated runtime with access to its own private storage, but not to the site’s content, media, users, secrets, environment, filesystem, or network. It gains additional abilities only when they are declared by the plugin and approved by the site administrator.

A comparison of the WordPress and EmDash runtime architecture.

Installing a sandboxed plugin therefore feels more like installing a mobile app than a traditional CMS plugin. EmDash shows what the plugin wants to do before it runs, and the runtime limits it to those approved abilities.

That lets plugins perform useful work without receiving unrelated access:

A plugin could…

It might need to…

It still cannot…

Index published articles for search

Read content and contact the search service

Edit articles or contact other hosts

Optimize uploaded images

Read and manage media

Read user content

Send publishing notifications

Observe publishing and send email

Change the content being published

Provide configurable webhooks

Read selected events and contact public destinations

Reach private networks or other plugins’ storage

The important part is that these abilities are independent. Giving a plugin access to media does not also expose users or unpublished content. Allowing it to contact one service does not open the rest of the network. These boundaries are enforced by the runtime, not left to the plugin author’s good intentions.

This isolation is not limited to Cloudflare deployments. On Cloudflare, EmDash runs each plugin as aDynamic Workerthrough the Worker Loader. On Node.js, EmDash startsworkerd— the open-source Workers runtime — as a separate process and runs each plugin as an isolated service inside it. Plugins use the same manifests and capability-gated APIs on either platform. See theplugin sandbox documentationfor setup and runtime differences.

Cloudflare Email Sending is one of many plugins available in the new EmDash plugin registry.

## From a single site to a website platform

EmDash can power an individual Astro site, but it is also designed for companies building website creation and hosting products.

Workers for Platformslets those companies run each customer’s site as a Worker on Cloudflare’s global network. They do not need to provision a server for every site or build the surrounding networking and deployment infrastructure themselves. That leaves them free to focus on the experience their customers use to create and manage a website.

EmDash provides the content layer for that experience. A platform can use the admin interface directly, build its own interface on the API and CLI, or put an agent in front of the built-in MCP server. A bakery owner could update opening hours by asking for the change in plain language; the platform’s agent would handle reading, updating, and saving the content.

The sandboxed plugin model also gives platforms a safer way to offer extensions across many customer sites. Plugins receive only approved access to content, media, users, email, or external services, rather than running with unrestricted access to the whole application. Platforms can run their own plugin marketplaces with access to the full registry — or curate a selection of pre-approved plugins.

We are always looking for additional hosting partners that want to join us in developing new agent-oriented CMS experiences.Reach out to usif you’d like to learn more about reinventing with EmDash.

## EmDash Build: an open source AI site builder

We are also releasing and open-sourcing an alpha of EmDash Build, an AI site builder that hosting providers, website builders, and platforms can run themselves and integrate with their own systems. Try the demo today atbuild.emdashcms.com, orexplore the code.

If you’re building a site today, for yourself or for a client, you won’t start in an IDE. You’re more likely going to start with a chat box, and describe to an agent what you want. But once you have something, you could find that changing simple things requires you to go back to that prompt box, and either roll the dice on the result, or burn credits for a one-line change.

EmDash Build creates an EmDash site instead, which brings the full stack: server-rendered Astro pages, a database, media storage, and an admin interface. The agent designs a content model from the brief, fills it in through EmDash's MCP server, and writes the pages that display it. After that, you or your customer can edit text right on the page, schedule posts, or let an agent do it for you.

In EmDash Build, each project gets its own Cloudflare Sandbox container, where the agent, built on the Agents SDK, verifies its own work. Artifacts tracks every change as a git commit. When the site is published, the content moves into a production EmDash site, and deploys to the host's Workers for Platforms namespace.

A website made in EmDash Build: started with a prompt, now living on the full stack.

## Get started and get involved

With the release of EmDash 1.0, now is a great time to migrate your company’s marketing site or have an agent spin up that side project you’ve been talking about.Try out the EmDash playground site here.

To create a new EmDash site locally, via the CLI, run:

npm create emdash@latest

Or you can do the same via the Cloudflare dashboard below:

If you’re ready to develop an EmDash plugin,our documentation has a step-by-step guidefor creating and publishing a plugin to the registry.

We also welcome you to join our growing community of contributors onDiscord. You don’t have to be an engineer to get involved — we welcome translators, issue triage managers, user experience designers, marketers, and all others who are excited about the future of content management systems.

## Related tags

Birthday Week
Cloudflare Workers
Developers
EmDash
Internship Experience
Open Source
Product News

Follow on Social Media

* Cloudflare
* Scott Buscemi
* Matt Kane
* Noah Pham

## Subscribe to receive notifications of new posts

Email address

We’ll never share your email address.

Subscribe

Thanks for subscribing! Check your inbox to confirm.