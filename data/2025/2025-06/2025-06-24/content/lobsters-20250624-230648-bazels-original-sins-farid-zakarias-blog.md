---
title: Bazel’s Original Sins | Farid Zakaria’s Blog
url: https://fzakaria.com/2025/06/22/bazel-s-original-sins
site_name: lobsters
fetched_at: '2025-06-24T23:06:48.405462'
original_url: https://fzakaria.com/2025/06/22/bazel-s-original-sins
date: '2025-06-24'
published_date: '2025-06-22T15:12:00-07:00'
description: I have always enjoyed build systems. I enjoy the craft of software engineering and I geek out about building software in the same way chefs do about their knives.
tags: programming
---

I have always enjoyed build systems. I enjoy the craft of software engineering and I geek out about building software in the same way chefs do about their knives.

My passion for this subject even led me to defend my PhD at University of California Santa Cruz, where I researched how to improve building software given the rise of stability [YouTube video] 👨‍🎓.

Bazelhas always intrigued me. I remember attending the first BazelCon in 2017 even though I was working at Oracle and we were not even using it. There was so much hype about how it was designed by Google and the size of their repository.

Fast forward a few years, I find myself working at Google and I had a lot more first-hand experience about howblaze(internal version of Bazel) works and more specifically, why it is successful. I have also been actively involved in theNixOScommunity which has shown me what a completely hermetic approach to building software could look like.

After having spent a full-year on a large migration to Bazel, the challenges and hurdles are starkly contrasted with the successful idioms I observed within Google.

## Sin #1:/is mounted into the sandbox

Bazel gives a convincing pitch abouthermiticityand the promise of reproducibilcity Valhalla. Unfortunately, you are quickly thrown into a quagmire of subtle differences and rebuilds.

The crux of the problem, or the most glaring one, is that the root/is mountedread-onlyby default into the sandbox. This makes it incredibly easy to accidentally depend on a shared system library, binary or toolchain.

This was never a problem at Google because there was complete control and parity over the underlying hosts; known impurities could be centrally managed or tolerated. It was easier to pick up certain impurities from the system rather than model them in Bazel such ascoreutils.

I spent more time than I care to admit tracking down a bug that turned out to be a difference between GNU & BSDdiff. These types of problems are not worth it. 😩

## Sin #2: Windows support

Google (Alphabet) has 180,000 employees with maybe an estimate of 100,000 of those are engineers. Despite this massive work-force,blazedid not support Windows.

I don’t even remember it working on MacOS and all development had to occur on Linux.

Open-source projects however are often subject to scope creep in an attempt to capture the largest user-base and as a result Bazel added support for MacOS and more challenging, Windows.

Support for Windows is somewhat problematic because it deviates or does not support many common Unix-isms. For instance, there are no symlinks in Windows. Bazel on Unix makes heavy use of symlinks to construct therunfiles treehowever in order to support Windows alternative mechanisms (i.e. manifests) must be used which complicates the code that would like to access these files.

## Sin #3: Reinventing dependency management

Google’s monorepo is well known to also house all third-party code within it as well in//third_party. This was partly due to the codebase predating the existence of many modern package-manage tools and the rise of semantic versioning.

The end result however was an incredibly curated source of dependencies, free from the satisfiability problems often inherent in semantic versioning algorithms (e.g, minimum version selection, etc…).

While the ergonomics of package-managers (i.e.bzlmod) are clearly superior to hand-curating and importing source-code the end result is we are back to square-one with many of the dependency management problems we sought to eschew through the adoption of Bazel.

There is a compelling case to be made for a single curated public//third_partyfor all Bazel users to adopt, similar to the popularity ofnixpkgsthat has made Nix so successful.

It’s difficult to advocate for a tool to take a stance that is worse ergonomically in the short term or one that seeks to reject a userbase (i.e. Windows). However, I’m always leery of tools that promise to be thesilver bulletor the everything tool. There is beauty in software that is well-purposed and designed to fit its requirements.

Less is more.
