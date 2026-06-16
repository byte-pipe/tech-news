---
title: 'How We Saved Big and Simplified Our Image Pipeline: Adopting bunny.net on DEV - DEV Community'
url: https://dev.to/devteam/how-we-saved-big-and-simplified-our-image-pipeline-adopting-bunnynet-on-dev-3d53
site_name: devto
content_file: devto-how-we-saved-big-and-simplified-our-image-pipeline
fetched_at: '2026-06-17T06:00:20.739320'
original_url: https://dev.to/devteam/how-we-saved-big-and-simplified-our-image-pipeline-adopting-bunnynet-on-dev-3d53
author: Ben Halpern
date: '2026-06-16'
description: Hey everyone, Ben here. If you’ve been following the journey of DEV and our open source project... Tagged with performance, webdev, design, bunny.
tags: '#performance, #webdev, #design, #bunny'
---

Hey everyone, Ben here.

If you’ve been following the journey of DEV and our open source projectForem, you know we’ve always been obsessed with web performance. Way back in the day, I spoke at Codeland about how to make your website so fast it goes viral in Japan, diving into the mechanics of edge caching and how we kept our page loads nearly instant.

Our core philosophy has always been simple: keep the architecture as lean as possible, cache aggressively at the edge, and let the Rails monolith (Forem) focus on what it does best. For years, Fastly has handled our HTML edge caching brilliantly—most of your page requests never even have to touch our Puma servers, which keeps our RAM usage low and our response times in the milliseconds. Fastly continues to be how all the document content on DEV is served.

But while edge-caching static HTML is a well-understood problem, user-uploaded media is a completely different beast.

As DEV grew, we found ourselves drowning in images. Every post cover, user avatar, comment screenshot, and challenge banner is a high-res asset uploaded by our community. Serving billions of these images globally, while keeping page sizes lightweight, eventually led us into a silent scaling trap: a tangled, multi-CDN media pipeline, massive cloud egress fees, and eye-watering monthly bills.

Here is the story of how we ended the multi-CDN chaos, simplified our media architecture, saved a small fortune, and used edge scripting to build a smarter, faster image-serving pipeline withbunny.net.

## The Chaos of Multi-CDN and the Billing Reality Check

To understand why we made the switch, you have to look at what our image pipeline used to look like.

For a long time, our media stack was a bit of a patchwork. We had different CDNs handling different parts of the platform, an image proxying service for dynamic resizing, and raw assets sitting in cloud storage (like AWS S3).

When a user uploads a 10MB JPEG as an article cover, our Rails app doesn't pre-process it into dozens of different dimensions. Instead, we rely on on-the-fly image transformation. In theory, this is great: the browser requestsimage.jpg?width=800, and a dynamic image optimizer resizes it, converts it to WebP or AVIF, and serves it.

In practice, the economics and mechanics of this setup at scale are brutal, especially when you factor in the realities of modern web traffic:

* The Scraper & Traffic Tax:On the open web, you aren't just serving human users. You are constantly being hit by RSS readers, search crawlers, and high-frequency scrapers. Traditional setups simply weren't smart enough to handle this gracefully. A wave of aggressive scrapers requesting un-cached variations or bypassing standard query parameters would force our pipeline to repeatedly re-fetch and re-process assets, sending computing costs into the stratosphere.
* Egress Fees:Every single time an image optimizer had to fetch a raw image from our cloud storage origin because of a cache miss (often induced by the traffic patterns mentioned above), we paid steep cloud egress fees.
* Transformation Pricing:Many premium image CDNs charge "per thousand images processed" or utilize complex, punitive usage tiers. When you have millions of active posts and users scrolling feeds with hundreds of custom-sized avatars, those transformation counts skyrocket.
* Multi-CDN Friction:Running separate providers for HTML caching and image delivery/optimization created massive operational overhead. We had complex header configurations, CORS issues, and routing rules scattered across different YAML files and dashboards.

Our media bills were ballooning, it was incredibly expensive, and we were spending way too much time debugging why our pipeline wasn't smart enough to handle volatile traffic spikes smoothly. We needed a solution that was fast, reliable, highly configurable, and above all, economically sustainable.

## Why We Hopped Over to bunny.net

I’ve actually been using bunny.net for years across many of my personal projects. Whether spinning up a quick side application or testing out a new concept, I always found myself returning to it because it is an incredibly well-designed platform with sensible, intuitive products. It lacks the dense, enterprise bloat of traditional cloud vendors; instead, it provides clean developer ergonomics that just work. Because of that first-hand experience, I knew it was a platform we could trust to scale seamlessly with DEV.

What really sold us for Forem wasn't just the raw bandwidth savings (though slashing our bandwidth bills to a fraction of what premium enterprise CDNs charge was a massive win). It was how beautifully their product ecosystem handled our specific architectural pain points through the combination ofBunny OptimizerandEdge Scripting.

### 1. Bunny Optimizer and Perma-Cache

Bunny Optimizer acts as a fully managed, dynamic image transformation API. We could easily plug it in, append simple URL query parameters (like?width=600&height=300&crop=1:1), and let Optimizer handle the resizing, cropping, and automatic compression on-the-fly. It automatically negotiates next-gen formats like WebP or AVIF based on the browser'sAcceptheaders, reducing file sizes by up to 80% without any visible quality loss.

But the real magic ingredient—and our ultimate weapon against scraper traffic—isPerma-Cache.

Normally, when a CDN edge server evicts an infrequently accessed image variant, the next request has to go all the way back to the origin (our cloud storage) to fetch and re-optimize it, triggering more egress fees. Perma-Cache solves this by permanently replicating the optimized image variants to Bunny Storage.

Once an image is processed once, it is stored at the edge forever. It never has to hit our AWS origin again, shielding our backend from erratic traffic and virtually eliminated our cloud storage egress fees overnight.

### 2. Edge Scripting: TypeScript-Native Control

While Bunny Optimizer gave us the raw power to resize images, we needed fine-grained control over how we served them. We didn't want to pollute our Rails views with complicated URL-building logic, and we wanted to prevent users (or bots) from downloading massive raw images.

This is where Edge Scripting came in.

Built on Deno and V8, Edge Scripting runs JavaScript and TypeScript directly at the edge, allowing us to write lightweight, type-safe middleware that executes in milliseconds. It completely replaced the need for custom image proxies or complex Rails controller routing.

## Under the Hood: Forem’s Pluggable Images::Optimizer Service

If you look into Forem's codebase, you’ll see that we’ve always designed our image pipeline to be pluggable. We didn't want to hardcode our views to use a specific CDN's query parameters. If a template wants to render a post cover image, it calls a unified helper that delegates to ourImages::Optimizerservice:

# app/views/layouts/application.html.erb

<%=
 
Images
::
Optimizer
.
call
(
Settings
::
General
.
favicon_url
,
 
width: 
32
)
 
%>

Enter fullscreen mode

Exit fullscreen mode

Insideapp/services/images/optimizer.rb, we use a simple strategy pattern. TheOptimizerclass acts as a router that maps standardized parameters (likewidth,height,fit,gravity) to the specific URL format required by the active CDN provider.

Historically, Forem has supported providers like Fastly, Cloudflare, and Cloudinary and adding bunny.net was incredibly straightforward. Here is a look at how our Rails service handles this multi-CDN routing:

# app/services/images/optimizer.rb

module
 
Images

 
class
 
Optimizer

 
def
 
self
.
call
(
url
,
 
options
 
=
 
{})

 
return
 
url
 
if
 
url
.
blank?

 
# Select the provider strategy based on our environment configuration

 
case
 
provider

 
when
 
:bunny

 
BunnyProvider
.
call
(
url
,
 
options
)

 
when
 
:cloudflare

 
CloudflareProvider
.
call
(
url
,
 
options
)

 
when
 
:fastly

 
FastlyProvider
.
call
(
url
,
 
options
)

 
else

 
url

 
end

 
end

 
def
 
self
.
provider

 
ENV
.
fetch
(
"IMAGE_OPTIMIZATION_PROVIDER"
,
 
"bunny"
).
to_sym

 
end

 
end

end

Enter fullscreen mode

Exit fullscreen mode

Each provider implements its own URL rewriting strategy. For example, our bunny.net provider simply builds standard query strings that Bunny Optimizer parses:

# app/services/images/bunny_provider.rb

module
 
Images

 
class
 
BunnyProvider

 
def
 
self
.
call
(
url
,
 
options
 
=
 
{})

 
uri
 
=
 
URI
.
parse
(
url
)

 
query_params
 
=
 
[]

 
query_params
 
<<
 
"width=
#{
options
[
:width
]
}
"
 
if
 
options
[
:width
]

 
query_params
 
<<
 
"height=
#{
options
[
:height
]
}
"
 
if
 
options
[
:height
]

 
query_params
 
<<
 
"crop=
#{
options
[
:crop
]
}
"
 
if
 
options
[
:crop
]

 
query_params
 
<<
 
"auto=format"

 
uri
.
query
 
=
 
[
uri
.
query
,
 
query_params
.
join
(
"&"
)].
compact
.
join
(
"&"
)

 
uri
.
to_s

 
end

 
end

end

Enter fullscreen mode

Exit fullscreen mode

This decoupled architecture is fantastic for an open-source project like Forem. Different self-hosted communities can configure their own CDN of choice by simply changing theIMAGE_OPTIMIZATION_PROVIDERenvironment variable.

However, while the Rails app generates these optimized URLs, we ran into an interesting operational challenge: what happens when a template forgets to pass a width parameter, or a legacy post contains raw external URLs?

If we relied only on Rails-side URL building, any fallback or unparsed URL would still trigger a heavy, unoptimized image load. This is where our Edge Scripting strategy stepped in—to act as a global safety net right at the network boundary.

## Deep Highlight: Smart Downsizing at the Edge

With Edge Scripting, we can intercept image requests right at the CDN layer and apply custom business logic before the request even reaches the optimizer or storage.

For example, we wanted to ensure that user profile avatars and feed thumbnails are never served larger than they actually need to be, regardless of what the original upload was or what query parameters were requested. If a client requests a raw, un-optimized avatar URL, our edge script automatically intercepts it, checks the context, and rewrites the request to enforce a strict maximum width and apply WebP compression.

Here's a simplified example

// A lightweight middleware script running on bunny.net's Edge

export
 
default
 
async
 
function
 
handleRequest
(
request
:
 
Request
)
 
{

 
const
 
url
 
=
 
new
 
URL
(
request
.
url
);

 
// Intercept requests to our user-uploaded uploads path

 
if 
(
url
.
pathname
.
startsWith
(
'
/uploads/
'
))
 
{

 
const
 
isAvatar
 
=
 
url
.
pathname
.
includes
(
'
/avatars/
'
);

 
const
 
isThumbnail
 
=
 
url
.
pathname
.
includes
(
'
/thumbnails/
'
);

 
// Check if the request already has optimization parameters

 
const
 
hasWidth
 
=
 
url
.
searchParams
.
has
(
'
width
'
);

 
if 
(
isAvatar
 
&&
 
!
hasWidth
)
 
{

 
// Dedicatedly downsize all avatar requests to a max of 150px

 
url
.
searchParams
.
set
(
'
width
'
,
 
'
150
'
);

 
url
.
searchParams
.
set
(
'
height
'
,
 
'
150
'
);

 
url
.
searchParams
.
set
(
'
crop
'
,
 
'
1:1
'
);

 
}
 
else
 
if 
(
isThumbnail
 
&&
 
!
hasWidth
)
 
{

 
// Enforce a strict mobile-friendly limit on thumbnails

 
url
.
searchParams
.
set
(
'
width
'
,
 
'
400
'
);

 
}

 
// Ensure automatic next-gen format negotiation (WebP/AVIF) is active

 
url
.
searchParams
.
set
(
'
auto
'
,
 
'
format
'
);

 
// Fetch the optimized asset from bunny.net's CDN pipeline

 
return
 
fetch
(
url
.
toString
(),
 
request
);

 
}

 
return
 
fetch
(
request
);

}

Enter fullscreen mode

Exit fullscreen mode

This is incredibly powerful because it offloads the "computational thinking" of image delivery entirely to the edge. Our Rails application doesn't have to keep track of responsive image breakpoints or generate heavy, complex markup. We just request the logical asset URL, and our edge script dynamically handles the rest based on client headers and context.

Even better, we’ve integrated this into our standard development workflows. We use GitHub Actions combined with fine-grained personal access tokens to manage and deploy these edge scripts automatically. When we want to adjust our optimization rules or add support for a new layout—like optimizing billboard images or adjusting resolutions on challenge pages—we just push a commit, our CI runs, and the new edge logic is live globally in seconds.

## Graceful Failures: Smart Fallbacks Over Plain Broken Images

Beyond routing and sizing, running code at the edge unlocked a massive UX victory: the ability to handle missing or broken assets gracefully.

In a massive community ecosystem, edge cases happen. A user might delete an external image they linked to, an old upload path might break during a migration, or a malformed request could slide through. Traditionally, when an image fails to load or returns a 404/500, the browser drops a jarring, ugly "broken image" icon that disrupts the layout and makes the entire site look broken.

With Edge Scripting, we can catch these failures mid-flight. If our origin or storage returns an error status code, the edge script intercepts the response and seamlessly rewrites it to serve a beautifully styled, custom placeholder image that says"Image not available"or matches our UI theme.

Instead of writing complex, heavy JavaScript event listeners (onError) into every single<img>tag across the Rails application, we handle it natively at the network layer. The application layer never has to think about fallback logic, and our users get a consistent, unbroken visual experience no matter what happens behind the scenes.

## Future considerations

Stabilizing and optimizing our image pipeline was just phase one. As we look ahead to how DEV and Forem will continue to evolve, video is the next logical horizon.

Video delivery is notoriously complex—requiring adaptive bitrate streaming (HLS/DASH), multi-resolution transcoding, specialized storage, and optimized video players. In legacy architectures, this usually means spinning up another fragmented set of expensive third-party video processors and complex integrations.

Given our success with their media infrastructure, bunny.net is our definitive first choice for how we are thinking about video moving forward. Their unified platform approach extends directly into video streaming with products that match the same sensible, developer-first philosophy as their image optimizer. Because we can trust their infrastructure to scale predictably without predatory data transfer costs, expanding our edge architecture to handle next-generation rich media feels like a natural progression rather than a daunting infrastructure overhaul.

## Final Thoughts

As developers, we often focus on optimizing our database queries, refactoring Ruby code, or fine-tuning our server configurations. But sometimes, the biggest wins are sitting right there in your network tab.

Egress fees and bloated media delivery are a silent tax on growing platforms. By moving to an edge-native, developer-friendly platform like bunny.net, we were able to simplify our architecture, speed up our page loads, and save a lot of money in the process.

If you’re running a media-heavy platform or building open-source community software like Forem, do yourself a favor: look closely at your CDN bills, check your cloud storage egress, and see if you can offload some of that weight to a platform built to grow with you. Your budget (and your users) will thank you.

Happy coding ❤️

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse