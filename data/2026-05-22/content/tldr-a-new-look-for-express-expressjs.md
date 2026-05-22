---
title: A New Look for Express · Express.js
url: https://expressjs.com/en/blog/2026-05-18-a-new-look-for-express/
site_name: tldr
content_file: tldr-a-new-look-for-express-expressjs
fetched_at: '2026-05-22T19:34:53.084654'
original_url: https://expressjs.com/en/blog/2026-05-18-a-new-look-for-express/
date: '2026-05-22'
description: Discover the redesigned Express.js website and our brand-new logo, built from the ground up with Astro.
tags:
- tldr
---

Edit on GitHub 
 
 
 
 
 
 announcements 
 
 

# A New Look for Express

 
 
 
 
 
 
 Sebastian Beltran 
 
 May 18, 2026 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

Express has been one of the most important frameworks in the Node.js ecosystem for over a decade. Millions of developers have built their first API, their first web app, or even their first startup with Express. Yet, while the framework kept evolving, the website remained largely the same for years.

In 2024, the Express project went through amajor reboot. A new team, a fresh vision for the framework, and a clear path forward. That momentum inspired me to start contributing to Express with a simple goal: improve the documentation experience. Good documentation helps everyone, from beginners building their first server to experienced developers looking for the right API detail, or even those building frameworks on top of Express. In early 2025, that goal started to become a reality when theredesign of the Express documentationofficially kicked off. What began as a documentation effort eventually grew into something much bigger, a complete redesign of the website and a brand-new logo for Express.

In short: we rebuilt the Express website, improved the documentation experience, and introduced a new logo and visual identity to match where the project is headed.

## A New Website

Rebuilding the Express website was not only a visual refresh. It was also an opportunity to rethink the foundations of how the documentation is organized, generated, and maintained.

Under the hood, we moved from Jekyll toAstro, chosen after a longcommunity discussionweighing tradeoffs and long-term maintenance. It gave us the flexibility we needed for content-heavy pages, strong performance, solid i18n support, and a component model that doesn’t lock us into a single UI framework.

### What’s New in the Documentation

The redesign was also a chance to bring long-requested improvements to how the documentation works.

* Improved versioning.Documentation pages now support multiple versions of Express side by side. You can read the docs for the version you’re actually running, and the content stays stable as new versions are released. The previous site didn’t make this easy to achieve, which often led to confusion between versions. This is especially helpful now that Express 5 is the latest stable release and many projects are still on Express 4.
* AI-powered search.The new search is built on top ofOramaand goes beyond keyword matching. You can ask questions in natural language and get contextual answers drawn directly from the documentation, which makes finding the right API or concept much faster.
* llms.txtsupport.Every section of the documentation is now available through anllms.txtendpoint, following thellms.txtconvention. This makes it much easier for language models, AI assistants, and other tools to access accurate, up-to-date Express documentation.

### What’s Next for the Documentation

Launching the new site is just the start. The next phase of this effort is focused on the documentation itself, closing the gaps that have built up over the years and bringing every Express API up to the standard the framework deserves.

A few of the things ahead:

* Closing content gaps.Many guides and API references still need fresh examples, clearer explanations, or rewrites that reflect how Express is used today, especially with Express 5.
* Better translations.The site has solid i18n foundations, but most translations are incomplete or out of date. The goal is to make translating Express docs a simple contribution for any native speaker.
* Keeping docs aligned with releases.New Express versions should ship with documentation that’s already ready, not catch up months later.

The new site is designed to make contributing easier than ever. If you spot something that could be better, an unclear explanation, a missing example, or a translation that needs love, pleaseopen an issue or a pull request.

## A New Logo

One of the most visible changes is the brand-new Express logo. This wasn’t something we designed in isolation. It came out of a collaborative workshop with theOramateam, where community members and the Express Technical Committee came together to define who Express is today and where it’s heading. The entire process was handled publicly, so anyone in the community could participate and share their voice.

Before jumping into the visual identity, we worked together on the foundations that would guide every design decision.

### Vision and Mission

We started by asking ourselves two simple questions: what is Express today, and where do we want it to go? The answers became the vision and mission that now guide every decision, from the framework itself to the documentation and the new visual identity.

### Brand Values

With the vision and mission in place, we distilled them into three values that describe how Express shows up for its users. They anchor the new identity and set the tone for everything the project communicates.

### The Logo

With that foundation in place, the design work was led byAngela AngeliniandDavide Spazianifrom the Orama team. Over several months, multiple logo proposals were shared with the community for feedback. You can still explore all of them in theoriginal discussion.

After gathering feedback from the community, both on the OpenJS FoundationSlackand across social media, we landed on the logo and favicon you see today:

It represents a fresh chapter for Express while staying true to the minimalism and clarity that have always defined the framework.

## Built by the Community

The redesign was not a solo effort. Dozens of people from across the Express community contributed code, design, reviews, and feedback over more than a year.

The effort was led bySebastian Beltran, withFrancesca Gianninodriving much of the design and UI work across the new site, andAngela AngeliniandDavide Spazianileading the brand workshop that shaped the new visual identity.

A huge thank you goes to theOramateam for sponsoringFrancesca Giannino,Angela Angelini,Michele Riva, andDavide Spaziani, and for the design, feedback, and support they brought to every stage of the project.

From the Express side, the redesign was shaped by many hands:Ulises Gascón,Rand McKinney,Jon Church,Shubham Oulkar, the rest of theExpress Technical Committee, and everyone who contributed reviews, issues, or comments along the way. The full history, including every PR that made it into the redesign, lives inthe main pull request.

More than a year of work went into this launch. In open source, progress is rarely fast: decisions take discussion, design takes iteration, and reviews take time. But step by step, a community can build something it’s proud of, and this is one of those steps.

Thank you to everyone who has written code with Express over the years, to the people who helped build this new site, and to the broader community that keeps the project alive. We can’t wait to see what you build next.

 
 
 
 

## More from Express

 
 
 
 
 
 announcements 
 
 

## Spring Cleaning in Express.js: Deprecations and the Path Ahead

 
 
 
 
 
 
 
 Express Technical Committee 
 
 May 16, 2025 
 
 
 
 
 
 
 
 
 
 announcements 
 
 

## [email protected]: Now the Default on npm with LTS Timeline

 
 
 
 
 
 
 
 Express Technical Committee 
 
 March 31, 2025 
 
 
 
 
 
 
 
 
 
 announcements 
 
 

## A New Chapter for Express.js: Triumphs of 2024 and an ambitious 2025

 
 
 
 
 
 
 
 Express Technical Committee 
 
 January 9, 2025 
 
 
 
 
 
 

### Interested in writing a post? 
 Check out our guidelines to get started.

 
 Read the guidelines