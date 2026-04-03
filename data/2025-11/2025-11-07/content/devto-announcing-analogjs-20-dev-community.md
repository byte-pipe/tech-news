---
title: Announcing AnalogJS 2.0 ⚡️ - DEV Community
url: https://dev.to/analogjs/announcing-analogjs-20-348d
site_name: devto
fetched_at: '2025-11-07T11:08:19.993968'
original_url: https://dev.to/analogjs/announcing-analogjs-20-348d
author: Brandon Roberts
date: '2025-11-03'
description: We're excited to announce the 2.0 release of AnalogJS! This release includes many features that help... Tagged with webdev, angular.
tags: '#webdev, #angular'
---

We're excited to announce the 2.0 release of AnalogJS! This release includes many features that help developers ship websites and applications, faster, with Angular.

This release marks the second major release of Analog, providing developers many new features and improvements to build with Analog.

## Features ⭐️

Analog is the meta-framework built on top of Angular, powered byVite, a next generation open-source build tool, andNitro, an open-source server engine framework. Here are some of its features, including:

* First-class support for the Vite ecosystem (Vitest, Playwright, Storybook, and more)
* Filesystem-based routing
* Support for markdownpages and blogs
* Support for API/server routes
* HybridSSR/SSGwith sitemap and RSS feed support
* Supports Angular CLI/Nx workspaces
* Server and deployment support
* And more!

## What's New

Analog 2.0 contains many new features including content resources, smaller install and bundle size optimizations, and Vite ecosystem upgrades.

### Content Resources 📜

As Angular continues to evolve with the introduction of Resources, Analog now also includes resources for displaying content lists and content files.

Content Files resources are used to display lists of loaded content.

import

{

Component

}

from

'
@angular/core
'
;

import

{

contentFilesResource

}

from

'
@analogjs/content/resources
'
;

import

{

PostsComponent

}

from

'
../../components/posts
'
;

import

{

Post

}

from

'
../../data/posts
'
;

@
Component
({


selector
:

'
blog-posts
'
,


imports
:

[
Posts
],


template
:

`
 @defer(hydrate on hover) {
 <posts [posts]="postsResource.value()"></posts>
 }
 `

})

export

default

class

Blog

{


readonly

postsResource

=

contentFilesResource
<
Post
>
();

}

Enter fullscreen mode

Exit fullscreen mode

Content file resources retrieve content as a signal, integrating with Angular's latest primitives for reactivity.

import

{

Component

}

from

'
@angular/core
'
;

import

{

MarkdownComponent

}

from

'
@analogjs/content
'
;

import

{

contentFileResource

}

from

'
@analogjs/content/resources
'
;

import

{

RouteMeta

}

from

'
@analogjs/router
'
;

import

{

Post

}

from

'
../../data/posts
'
;

import

{

postMetaResolver
,

postTitleResolver

}

from

'
./resolvers
'
;

export

const

routeMeta
:

RouteMeta

=

{


title
:

postTitleResolver
,


meta
:

postMetaResolver
,

};

@
Component
({


selector
:

'
post
'
,


imports
:

[
MarkdownComponent
],


template
:

`
 @let post = postResource.value();

 @if (post) {
 <div class="flex flex-grow justify-center min-h-screen">
 <article class="w-screen max-w-4xl p-8">
 <h2 class="text-gray-600 text-2xl">{{ post.attributes.title }}</h2>

 <span class="font-light text-sm">
 {{ post.attributes.publishedDate }} -
 {{ post.content }} min read
 </span>

 <analog-markdown [content]="post.content"></analog-markdown>
 </article>
 </div>
 }
 `

})

export

default

class

BlogPost

{


readonly

postResource

=

contentFileResource
<
Post
>
();

}

Enter fullscreen mode

Exit fullscreen mode

As Resources are still experimental in Angular, there will be future updates, and we're looking to further support these new APIs in Analog.

### Installation and Bundle Size Optimizations 📦

We've continued to improve Analog projects, including installing project dependencies and optimizing bundle sizes. A few changes include:

* Smaller install footprint for Angular CLI workspaces without any Webpack dependencies.
* All Angular builders are shipped as ESM.
* Replacing packages with smaller equivalents, such as usingtinyglobbyinstead offast-glob.
* Direct usage of the Vite CLI for serve/build in addition tong serve
* Direct usage of the Vitest CLI for testing in addition tong test
* Generated bundle output size reduction of 100Kb+ for full-stack projects.

These optimizations decrease the installation time of Analog projects in development, and reduce the amount of code built and shipped.

### Vite Ecosystem Upgrades ⚡️

Analog continues to integrate and support many Vite ecosystem integrations:

* Angular v17-v20 with upcoming support for Angular v21
* Vite 6.x and 7.x, including support for the latest Rolldown-Vite releases
* Vitest 3.x and 4.x including support for the Vitest VSCode extension
* Nx 22.x
* Storybook 10.x, including support forcomponent testing with Vitest
* Astro 5.x

### Angular support for Vitest 🧪

In Angular v21, stable support for Vitest directly through the Angular CLI was introduced for new Angular projects. While both Analog and Angular support running tests with Vitest, there are some similarities and key differences.

The table below shows the features available across both choices.

Vitest

Analog

Angular

Angular Versions

v17+

v21+

Vitest Versions

2.0+

4.0+

Support

Community

Angular Team

Builders

✅

✅

Schematics

✅

✅

Migrations

✅

✅

Fully Configurable

✅

⚠️

Vitest CLI

✅

❌

Vitest Workpsaces

✅

❌

Custom Environments

✅

❌

Custom Providers

✅

❌

IDE extensions

✅

❌

Buildable Libs

✅

❌

Module Mocking/Graph

✅

❌

Plugins/Types

✅

❌

The table above is not to compare the two solutions, but to provide the information on what features are supported by each implementation. Choose the solution that best fits your needs and priorities.

Check out our guide on how you canadd Vitestto any existing Angular project.

## Contributions and Community 🤓

AnalogJS would not be where it is without a team of core contributors and collaborators.

Robin GoetzMarko StanimirovićLuis CastroChau TranJoshua MoronyAndrés Villanueva

Also, thanks to the150+ contributorsto the project, whether through code, documentation, tests, or even just trying out the project.

The project already has nearly 3000 stars onGitHub, 1000+ members onDiscord, 1000+ followers onTwitter/X, and was accepted into the firstGitHub Accelerator Cohort.

## Partner with Analog 🤝

Continued development of Analog would not be possible without our partners and community. Thanks to our official deployment partnerZeropsand longtime supportersSnyder Technologies,Nx, andHouse of Angular, and many other backers of the project.

Find out more information on ourpartnership opportunitiesor reach out directly to partnerships[at]analogjs.org.

## Join the Community 🥇

* Visit and Star theGitHub Repo
* Join theDiscord
* Follow us onTwitter

If you enjoyed this post, click the ❤️ so other people will see it. FollowAnalogJSandmeon Twitter/X, and subscribe to myYouTube Channelfor more content!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments have been hidden by the post's author -find out more

For further actions, you may consider blocking this person and/orreporting abuse
