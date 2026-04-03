---
title: Simplifying Vulkan One Subsystem at a Time
url: https://www.khronos.org/blog/simplifying-vulkan-one-subsystem-at-a-time
site_name: hackernews_api
content_file: hackernews_api-simplifying-vulkan-one-subsystem-at-a-time
fetched_at: '2026-02-12T06:00:13.020038'
original_url: https://www.khronos.org/blog/simplifying-vulkan-one-subsystem-at-a-time
author: amazari
date: '2026-02-11'
published_date: '2026-02-05T06:00:00-08:00'
description: 'When those of us in the Vulkan® working group want to modify the API—whether it’s a new hardware feature to expose, a new use case we want to address, or even just a gap in the spec we want to address—we have one invaluable tool that we make heavy use of: extensions! Extensions are a wonderful way for us to get improvements to the Vulkan API out to developers without waiting for a new core version. They let vendors expose novel functionali'
tags:
- hackernews
- trending
---

# Simplifying Vulkan One Subsystem at a Time

 February 5, 2026

 by
Tobias Hector - AMD Software Architect / Vulkan Strategy Officer

vulkan

When those of us in the Vulkan® working group want to modify the API—whether it’s a new hardware feature to expose, a new use case we want to address, or even just a gap in the spec we want to address—we have one invaluable tool that we make heavy use of: extensions!

Extensions are a wonderful way for us to get improvements to the Vulkan API out to developers without waiting for a new core version. They let vendors expose novel functionality and enable us to gather community feedback on new features before we firm them up into a core specification.

Amazing! So we get new functionality out to developers quickly—what’s not to love!? Well…

## The Extension Explosion Problem 💥

Having access to this much extensibility comes at a cost. As we add more extensions to the API, we sometimes inadvertently obscure the simplest way to use it. What functionality can you rely on always being there? How many ways are there to do what you want to do? Which of those ways will give the best performance? How many paths through the API can you reasonably support in one application?

We sometimeslovinglyrefer to this as the “extension explosion problem” due to thenumber of extensions we have now—andhow many existed in OpenGL/ES™ beforehand. The more we add, the more they chain off of and interact with each other, adding combinatorically to the decision space for developers.

This is a persistent challenge that we’ve heard loud and clear from Vulkan’s developer base, but until now we haven’t had a good solution.

When we produced Vulkan 1.0, it gave us a clean slate moving from OpenGL® , but now 10 years into Vulkan we are facing the same problem again. So, what’s the answer? Should we rebuild the entire API from scratch every few years?

No—believe it or not,we add more extensions!

…🤨?

## Subsystem Replacement

Counterintuitive as it may seem, adding more extensions is one way we can improve the situation. However, thiscannotjust be business as usual. Wehaveto take a different approach.

Rather than incrementally adding or changing the API and increasing complexity, we want to revise whole API subsystems, producing whole-cloth replacements that let you ignore whatever came before, with supporting tooling and industry backing to make sure the new approach ships everywhere.

VK_EXT_descriptor_heapis the first concrete attempt at this approach,totally replacingthe existing descriptor set subsystem in Vulkan. Members of the Vulkan working group have poured everything into this, and it’s had the kind of attention we’ve only historically seen with major API revisions (e.g. Vulkan 1.0). While it’s shipping as an EXT for now, it’s very much on a path to becoming future core functionality.

We previously attempted to fix up the descriptor model withVK_EXT_descriptor_buffer, which developers have had some success with, but we used incremental (if large!) improvements to the existing descriptor set functionality, making it necessary to check for a variety of descriptor set extensions. This incremental approach also didn’t attract wide industry backing, resulting in cross-vendor portability issues. We knew we had the core of something important, but it needed a rethink to make it stick. So we took the lessons learned from VK_EXT_descriptor_buffer, and designed a completely new subsystem.

The new VK_EXT_descriptor_heap extension does not interact with the previous descriptor set API, including layouts, push descriptors, or descriptor buffers inany way—it fully replaces it all. Instead of just trying to tidy up the API a little, this extension fundamentally changes how Vulkan applications interact with descriptors. Descriptors are no longer some opaque thing that you manage through a series of awkward API commands and restrictive shader bindings. Descriptor heaps are just memory, descriptors are just data, and you can domore or lesswhatever you want with them. There aresomerestrictions, but it’s a lot closer to what you might expect on a console than in a portable API.

This extension has also had contributions from a huge swathe of the industry, much more than our typical extensions. Feel free to look at thecontributor list—it’sextensive. This extension has had meaningful input from virtually everyone in the Vulkan Working Group. Together we’ve spent the better part of the past three years iterating on and refining this, ensuring it not only works but workswell.

## If this has so much buy-in, why isn’t it a KHR?

We want to make sure we have buy-in from you, too.

With something this big, we want to make sure we get it right. We’re confident that what we’ve built is already a huge improvement and an excellent feature, but by releasing it as an EXT, we’re giving the wider community a chance to try it out, figure out its intricacies, and perhaps suggest ways it can be even better.

The EXT is not going to change, so you can use it in shipping apps today; when we do eventually ship a KHR version, we’re aiming for the transition to be as straightforward as possible if you choose to use it.

If you do find anything in the new extension that you think could be simpler or improved, we will consider any feedback as we finalize the KHR specification. By doing so, we will work to get everything as polished as possible and avoid additional extensions to fix things later.

While we can’t make any guarantees about when the eventual KHR will materialize, getting feedback within the next 9 months will give us the best opportunity to incorporate your input.

Pleaseuse this extension andlet us know how it goes!

## Cool. You did something about descriptors. What about <insert feature>?

Developer needs are at the center of our roadmap planning, and we're committed to addressing the requests we've been hearing.There’s a very good chancewe’re already working on the thing you are after.

If we don’t have your problem logged somewhere, or if you think it’s not getting enough attention, we encourage you tojump on our Discordorfile an issue on GitHubto let us know about it!

In order to replace subsystems like this, we have a lot of considerations to balance - developer needs, ecosystem needs, vendor roadmaps, future direction, and upcoming hardware and software releases, among other things. Taking care of all of those needs takes care to try and get it right the first time. That doesn’t mean any of this needs to be slow though! We are actively working on how to use this methodology to upgrade key parts of the Vulkan API, with strong industry buy-in.

One of our top priorities right now is to make the Vulkan API a joy to use. We know we still have a long way to go, but we hope that well-considered subsystem replacements like this are a major positive step in that direction. Please do let us know what you think of this approach—we’d love to hear from you!
