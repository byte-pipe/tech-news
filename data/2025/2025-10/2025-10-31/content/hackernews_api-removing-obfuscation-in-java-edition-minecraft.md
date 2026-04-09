---
title: Removing obfuscation in Java Edition | Minecraft
url: https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition
site_name: hackernews_api
fetched_at: '2025-10-31T11:10:10.114418'
original_url: https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition
author: SteveHawk27
date: '2025-10-29'
published_date: '2025-10-29T16:00:00Z'
description: 'For a long time, Java Edition has used obfuscation (hiding parts of the code) – a common practice in the gaming industry. Now we’re changing how we ship Minecraft: Java Edition to remove obfuscation completely. Find out more in this article!'
tags:
- hackernews
- trending
---

News

Written By

Staff

Published

10/29/25

# Removing obfuscation in Java Edition

What this means for our modding community

Do you like to mod Java, tinker with builds, or take deep dives into Minecraft’s code? Then this article is for you!

For a long time, Java Edition has used obfuscation (hiding parts of the code) – a common practice in the gaming industry. Now we’re changing how we ship Minecraft: Java Edition to remove obfuscation completely. We hope that, with this change, we can pave a future for Minecraft: Java Edition where it’s easier to create, update, and debug mods.

 

## An obfuscated history

Minecraft: Java Edition has been obfuscated since its release. This obfuscation meant that people couldn’t see our source code. Instead, everything was scrambled – and those who wanted to mod Java Edition had to try and piece together what every class and function in the code did.

But we encourage people to get creative both in Minecraft and with Minecraft – so in 2019 we tried to make this tedious process a little easier by releasing “obfuscation mappings”. These mappings were essentially a long list that allowed people to match the obfuscated terms to un-obfuscated terms. This alleviated the issue a little, as modders didn’t need to puzzle out what everything did, or what it should be called anymore. But why stop there?

 

## Removing obfuscation in Java Edition

To make things even easier – and remove these intermediary steps – we’re removing obfuscation altogether! Starting with the first snapshot following the complete Mounts of Mayhem launch, we will no longer obfuscate Minecraft: Java Edition. This means that this build (and all future builds) will have all of our original names* – now with variable names and other names – included by default to make modding even easier.



*Names in this context refers to technical names of elements of the code, including variables, fields, methods, classes, etc.

HANDY GUIDE

## What this means for modders

We know that this change may pose challenges for existing modding tools, which are typically designed for obfuscated code, and we’re going to help modders prepare for this change. Starting with the next snapshot we will provide un-obfuscated “experimental release” versions alongside obfuscated ones. Modders will be able to use these to test their tools and workflows before we transition fully to non-obfuscated versions.

The first snapshot following the complete Mounts of Mayhem launch will be the first version without obfuscation.

 

## Why are we doing this?

Modding is at the heart of Java Edition – and obfuscation makes modding harder. We're excited about this change to remove obfuscation, as it should make it quicker and easier for modders to create and improve mods. Now you won’t have to untangle tricky code or deal with unclear names. What’s more, de-bugging will become more straightforward, and crash logs will actually be readable!

 

## No changes to EULA

 

Just a quick reminder: these changes don’t affect ourMinecraft End User License AgreementandMinecraft Usage Guidelines. Both still apply to Minecraft: Java Edition and any mods, so please keep them in mind. For extra transparency, you’ll now find a LICENSE file inside the jar that links directly to the EULA.

Here’s what modders can expect in upcoming releases and snapshots:

 

* No more obfuscation maps in version .jsons – as they’re no longer needed
* The client and server .jar files won’t be obfuscated
* Each .jar now includes a new LICENSE file

 

As with all of our releases, we’ll want your feedback on this change – especially as we transition from an obfuscated past into our new, more transparent future!

## Share this story

## Newest News



 Catch up on the latest Minecraft news & game updates!
