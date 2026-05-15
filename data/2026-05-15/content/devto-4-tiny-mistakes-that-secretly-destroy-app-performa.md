---
title: 4 Tiny Mistakes That Secretly Destroy App Performance - DEV Community
url: https://dev.to/sylwia-lask/4-tiny-mistakes-that-secretly-destroy-app-performance-3cgo
site_name: devto
content_file: devto-4-tiny-mistakes-that-secretly-destroy-app-performa
fetched_at: '2026-05-15T11:42:18.722672'
original_url: https://dev.to/sylwia-lask/4-tiny-mistakes-that-secretly-destroy-app-performance-3cgo
author: Sylwia Laskowska
date: '2026-05-14'
description: Ok, I’m back from my short vacation and returning with some useful content 😄 As you know, from time... Tagged with javascript, angular, react, frontend.
tags: '#javascript, #angular, #react, #frontend'
---

Real-world cases and energy-saving impacts

Ok, I’m back from my short vacation and returning with some useful content 😄 As you know, from time to time I write posts for you in the style of articles likeStop Installing Libraries: 10 Browser APIs That Already Solve Your Problems— which I honestly love writing, and I know you enjoy them too 🙂

Today I want to approach the topic from a slightly different angle. I’m going to show you a few interesting things that might accidentally be making your appmuchslower, even though they often look completely innocent at first glance. And the best part? Some of them can be fixed surprisingly quickly. Also, these are the kinds of issues Claude Code or Codex probably won’t immediately point out when you ask them “why is my app slow” 😅

Usually, we develop our applications on powerful machines with fast CPUs, plenty of RAM, and fast internet. Unfortunately, real users often live in a completely different reality. Some of them absolutely have modern hardware, but there willalwaysbe somebody using an old laptop, a cheap Android phone, weak WiFi, or mobile internet from the depths of hell 😅

And suddenly it turns out your app is painfully slow for 10–30% of users.

And that’s where the war for milliseconds begins 😀

Every example in this article is something I either personally encountered in a real project or heard about from another developer, so these are definitely not hypothetical scenarios. Check whether some of these things are secretly happening in your own application 👀

Meanwhile, I’m slowly preparing for my JSNation conference talk. If you want to support me (or just see me awkwardly talking in my garden 😄), you can give me a likehere. And if you want to watch my full talk completely FOR FREE, you can grab a free badgehere. HOW COOL IS THAT 😄

But enough self-promotion, let’s get to the point!

## 1. Custom headers → preflight requests

This is exactly why it’s worth attending conferences. Sometimes you hear about problems there that you would probably never randomly google yourself 😀

One of my colleagues talked about this issue during his presentation. His team was trying to understand why their application felt slow for some users. Naturally, the backend was blamed first. Poor backend, as always 😅

But eventually they noticed something interesting in the network tab:OPTIONSrequests appearing before almost every API call. Some of them were taking hundreds of milliseconds.

So what exactly is happening here?

This is related to CORS. Browsers sometimes send an additionalOPTIONSrequest before the actual API call. This is called a preflight request and usually happens for “non-simple” requests — for example when using methods likePUTorDELETE, but also when adding custom headers.

And yes, even a completely innocentGETrequest can suddenly becometwonetwork calls because somebody addedX-Feature-Whateverthree years ago 😅

In their case, the funniest part was that the custom header wasn’t even used anymore. It was some ancient historical leftover from years earlier. Nobody knew why it existed. Nobody questioned it. It simply survived every refactor like an immortal enterprise relic 😀

If you’re curious, I actually prepared (together with Claude Code 😅) a small repo showing this behavior here:https://github.com/sylwia-lask/preflight-options

Let's see the screens (please appreciate my high graphic skills!):

GET request without custom header:

GET request with custom header:

And honestly, this kind of thing happensall the timein large projects. Somebody adds a custom header for feature flags, debugging, localization, analytics, or “temporary” metadata… and then the header survives for the next four years.

Of course, sometimes custom headers are completely justified. But if you only use them for frontend-only logic, there are often better alternatives like query params, cookies, local state, or configuration endpoints fetched once during startup.

Individually, one extra request may not look catastrophic. But if your app performs dozens of calls during startup, especially on slower mobile connections, this suddenly becomes very noticeable.

## 2. Code splitting that does absolutely nothing

Sometimes the problem isn’t the network itself but the gigantic JavaScript bundle we load during startup. And this is usually the moment where everybody says:

“But how? We’re already doing code splitting! We use lazy loading everywhere!”

Yeah… about that 😄

I once audited an Angular application that looked very well structured at first glance. It had modules everywhere, lazy loading, proper architecture, all the “best practices.”

And yet the application loaded painfully slowly.

Fortunately, we have tools likewebpack-bundle-analyzer,source-map-explorer,rollup-plugin-visualizer, or@next/bundle-analyzerthat allow us to see what’sactuallyhappening inside our bundles.

And what did we discover?

Yes, the application was split into modules…

…except each module was like 2 KB 😅

Because almost everything important lived inside one gigantic shared module that was imported absolutely everywhere, meaning most of the application still ended up inside the main bundle anyway 😀

Congratulations, your app is now split into 400 beautifully separated files that all load at startup.

This is also not the only weird case I’ve seen. I’ve already encountered situations where the app technically “lazy loaded” modules while still downloading almost the entire application every single time 😄

For example, something like this looks perfectly fine:

{

 
path
:
 
'
admin
'
,

 
loadChildren
:
 
()
 
=>

 
import
(
'
./admin/admin.module
'
).
then
(
m
 
=>
 
m
.
AdminModule
)

}

Enter fullscreen mode

Exit fullscreen mode

Looks clean. Looks modern. Looks optimized.

Until you discover thatAdminModuleimports a massive shared module containing half the application 😅

So yeah — just because you useimport()or lazy modules doesnotautomatically mean your bundles are healthy. Always check what is actually being downloaded by the browser.

## 3. Unnecessary runtime dependencies

This is another extremely common problem, especially in projects where nobody really controls what npm packages people install 😅

In my current project, importing a new dependency is practically treated like a sacred ritual that requires approval from the wisest architects of the kingdom (which basically means me and two or three coworkers 😀). But in many projects, people install libraries completely thoughtlessly.

And then suddenly your application contains:

* three analytics SDKs,
* two date libraries,
* all Moment.js locales,
* the entire Lodash package because somebody needed one utility function,
* Firebase imported globally,
* three icon packs,
* and some “tiny lightweight helper package” that quietly imports half the internet 😀

I once saw an application loading three different date libraries at the same time. The funniest part? The app barely even handled dates 😅 Apparently every developer simply had their own preferred religion.

Another classic example is importing Lodash like this:

import
 
_
 
from
 
'
lodash
'
;

Enter fullscreen mode

Exit fullscreen mode

instead of:

import
 
debounce
 
from
 
'
lodash/debounce
'
;

Enter fullscreen mode

Exit fullscreen mode

The difference may look small, but over time these things accumulatea lot. Especially in enterprise applications that grow for years.

And unfortunately, tree shaking is not magic 😅

## 4. Huge background images

This one sounds almost too obvious, right?

Everybody already knows giant images are bad.

…except people still keep shipping giant images 😄

Recently, during the WeAreDevelopers podcast, we discussed which government websites loaded the fastest. Surprisingly, the UK completely dominated everybody else. Why? I’ll probably write a separate article about this later, but generally speaking, the site was just extremely simple. Very little visual noise, lots of informational text, simple layout, SSR, minimal unnecessary assets.

The second fastest was the US government website.

It followed almost exactly the same principles… except it loaded a fancy large image during startup 😅

And suddenly the large contentful paint became noticeably worse.

The funny thing about large background images is that they often look harmless on developer hardware with fast internet. But on slower devices they can absolutely destroy perceived performance.

Fortunately, there are many ways to improve this: use AVIF or WebP, compress aggressively, avoid massive hero images above the fold, lazy load non-critical visuals, and preload only truly critical assets.

And honestly?

Sometimes the fastest image is simply… no image 😀

## Final thought

Application optimization is obviously an endless topic, and this article only scratches the surface. But I think one of the most important things to understand is that performance problems are often death by a thousand cuts.

One unnecessary header.

One oversized dependency.

One “temporary” shared module.

One background image nobody questioned.

Individually, none of these things look catastrophic. Together, they create an application that feels sluggish — especially on older devices or slower mobile networks.

And the really scary part?

Most of these decisions looked perfectly reasonable when they were originally introduced 😅

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (34 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse