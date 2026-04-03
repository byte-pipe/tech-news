---
title: 'tazjin''s blog: Trying Guix: A Nixer''s Impressions'
url: https://tazj.in/blog/trying-guix
site_name: hackernews
fetched_at: '2025-07-19T16:06:31.845590'
original_url: https://tazj.in/blog/trying-guix
author: todsacerdoti
date: '2025-07-19'
description: tazjin's blog
---

## Trying Guix: A Nixer's Impressions

People occasionally ask me how I think Guix compares to Nix. Let me set the stage: I've been using Nix for many years, have large projects using Nix, used to be very active in the Nix community, and even wrotemultipleNix language interpreters, so I'd say that I'm at leastfairly comfortablewith Nix.

I'm also one of those people who live in Emacs. I'm no stranger to Lisps (although my experience with Scheme is limited) and am very fond of them. It feels natural that people ask me about my views on Guix.

The thing is: I haven't actually ever used Guix, so I just don'tknow. But there's an easy way to find out: let's try it! So that's what I did this weekend.

Here are a few things I ran into and found noteworthy. My goal was to take myUnchartevicelaptop with its strange Zhaoxin x86_64-compatible CPU and see if I could get all the way to my standardniridesktop. There's no overarching point here, just observations a user of one or the other system might find interesting.

Spoiler:I didn't manage, but I saw a lot of interesting stuff. Knowing myself, I'll probably keep trying when some free time shows up.

A quick note before we begin: Technically, Guix uses a fork of the Nix daemon for the low-level primitives of functional package management (theNixGuix Store, derivations, substitutions, and all that stuff arebasicallythe same). The projects forked a long time ago, and development has diverged significantly since then. The similarities end here, however: Guix is not "just" Nix with Scheme — it's a complete alternative ecosystem built in parallel on top of the same foundational infrastructure. A mental model of "Nix with Lisp syntax" willnotwork in practice when approaching Guix.

Anyway, here we go.

## nonguix

The very first thing I ran into is more political, but I must mention it, as almost everyone trying the Guix System will face this immediately.Skipthis if you want to get straight into the technical stuff.

Guix is the GNU system, and as such takes software freedoms very seriously. Guix does not recommend and does not ship the proprietary blobs needed for most modern hardware. The FSF hasa websitethat lists laptops that work without them, but it isverylimited. Themajorityof Guix System users use something callednonguixthat adds these blobs, giving you access to things such as wireless internet.

I don't want to make this post about the political side of software freedoms, but I had to usenonguixto get internet working on the machine, which had very immediate technical effects that bring me to:

## Architectural Differences

A major and immediate difference between Guix and Nix is that they layer things differently. Nix works like this:

[ nix-daemon ] <-> [ Nix CLI ] <- [ Nix code ]

The brackets here are intended to signifyindependence: You can mix (to some extent) separately built nix-daemons and Nix CLIs, and you can use almost any version of Nix from the last 8 years or so to evaluate almost any Nix code (let's, please, not get intowhy flakes are nonsensewhy this is only "almost" true).

The Nix CLI knows nothing1about nixpkgs. In most Nix code, something, somewhere willimporta commit of nixpkgs, which yields an enormous data structure lazily containing all Nix packages, and then use bits of this structure. Importing multiple nixpkgs commits is no problem—it just means that you havetwolarge data structures now. In effect, this means that you can mix and match nixpkgs commits (or other Nix config) freelywithin the language, and Nix always evaluates the entire thing.

In fact, in TVLwe mix nixpkgs commitsall the time, because we track unstable releases and occasionally need to pick software from an older stable commit.

Guix doesn't work like this, and I found it very confusing at first. That's not to say it's bad — it's just different:

[ guix-daemon ] <-> [ guix CLI + profile ] <- [ Guix user code ]

As in Nix, the Guix daemon converses with the CLI over an RPC interface. The difference is that the Guix CLI runs in a fixed profile that hasallof the packages and modules from all channelsbaked in. In contrast to Nix, the Guix package/service set is not one big data structure, but a namespaced hierarchy of Scheme modules. The Guix CLI is a Scheme environment in which packages, services and so on are available for import in user code.

This means that to change the Guix version (i.e., commit in theirmonorepo, which is the implementation of the CLIandof the package set, as ifNixOS/nixandNixOS/nixpkgswere one) you essentiallyrebuild Guix. In Guix land, this happens through a command calledguix pull, which ultimately yields (as I understand it) a newguixbinary with a hardcoded profile.

This has two effects that were noticeable to me:

1. Switching between versions is always at least a two-step process: Rebuild Guix, then rebuild your config. You can't easily2, as in Nix, just import a different Guix commit in your code.
2. Runningguix pullis slow, and this makes the initial bootstrapping experience very frustrating. It's super-easy to build a configuration from some Guix commit, then run the wrong command and cache-bust everything as the commit changed (which, due to nonguix, often leads to a full Linux kernel rebuild—something you donotwant to do on a Zhaoxin KX-6640MA!).

There isn't a right-or-wrong here: Guix uses a different model from Nix. For me, Nix's feels more natural, but this might just be bias due to familiarity.

For what it's worth, Liam from the#guixIRC channel pointed metowards a methodfor handling Guix "pins" in a better way, but I haven't tried it out yet.

Another thing that seems architecturally different is profile-wide installs of packages. In Guix they seem to be preferred over the Nix approach of creating isolated environments for specific programs with helpers. The most noticeable one for me was Emacs: People usually install Emacs packages right into their system or user profile from which Emacs loads them, whereas Nix hasemacs.withPackagesthat takes a list of packages and builds a full Emacs with these packages baked in.

I haven't figured out if there is an equivalent to Nix'semacs.withPackages. Maybe I didn't look at the right people's configs? If there isn't, this kind of design makes some experimentation harder than on Nix: It's seemingly more difficult to try out packages without affecting the global namespace.

## Documentation & Onboarding

Guix's community has a much more focused culture. The Nix community is currently a bit of a mess of different corporate interests pulling in different directions with little ideology and direction.

Guix's clear focus allows to get some stuff done that I think would be difficult to organize in Nix. An area where this is noticeable is documentation: Guix's is many times better than Nix's. It is structured logically, available ininfo, all the Scheme constructs needed are documented like any other Scheme code, and so on.

The thing is, I'm not actually sure if Guix's better documentation helps smooth the onboarding in any way because you have to already know Scheme, which is a more complex language than Nix. On the other hand, the skill of knowing Scheme translates to other domains, so you might argue that learning Scheme is an investment that pays off more than learning the Nix language.

Another thing that complicates onboarding is the whole nonguix situation: There are no recent ISO images for installers with unfree firmware, and there's only a handful of posts strewn across the internet that will help you get up-and-running.

Maybe the documentation in both cases (Nix and Guix) isn't really going to help beginners, but it helps confident users more effectively use the system. Guix does this better.

## Performance

Guix is noticeably slower than Nix. We complain about NixOS evaluation with C++ Nix taking a long time, but Guix feels an order of magnitude slower.

On this laptop, aguix pull(remember, this is the equivalent to updating your nixpkgs pin on Nix) can easily take 30-50 minutes. After that you still need to evaluate the system config, check for substitutes, build it, and so on. Sure, this is a laptop with a CPU broadly equivalent to old Intel Atom CPUs, but on this same machine Nix performs much better (evaluating and switching to a new system config in 5-10 minutes).

Apparently once the system is stable, and commits don't keep changing much, performance improves - but I haven't reached that state yet, and getting there is hard.

Due to the kernel rebuilds I ended up installing Guix onnevsky, the powerful TVL build server, and building the system config there (the Guix package manager runs well on NixOS, and vice-versa). I couldn't figure out an easy way to get the system closure from there to the laptop though, asguix copy --from=...doesn't seem to work for HTTP substitution. It seems like evaluating the config locally is unavoidable.

I'm curious why this is: The Guile interpreter has a JIT, and Guix has a more imperative evaluation model which should (unintuitively) be able to avoid some of the work happening in Nix's magic recursive fixpoint sets. Maybe there are some low-hanging fruits and performance just hasn't been a priority? I don't know, but I'd be interested in finding out.

Of course, a CPU with these performance characteristics is an outlier in 2025, but it makes the difference more noticeable.

## Shepherd vs. systemd

The Guix system does not usesystemd. This is great—I'verantedbefore (in Russian) about how much I dislike the current state ofsystemd, and there are muchmore detailedposts about why systemd, albeit being an improvement over what came before it, is not very good.

Guix instead usesShepherd, an init system written in Scheme. I don't have much to say about it yet, but it seems fairly straightforward and has excellent documentation. Once I continue with my experiment, I'll take a look again.

## Conclusion

Where I ended up after hacking on this for the weekend:

I've got Guix running on the laptop, however without a graphical UI. Some hardware configuration bits are missing, and as there doesn't seem to be an equivalent tonixos-generate-configI still have to invest some time in guessingwhichbits. I failed to configure the same channels that I used during installation on the machine itself, so now I have to go through at least one more extremely slowguix pullcycle to evaluate and be able to substitute the next config generation, which is already built onnevsky. Feels like I'm doing something wrong, but that is learning.

Despite the problems I ran into, Guix is still intriguing: Lisp is a big plus, and the Guix ecosystem feels a lot more coherent than Nix. Would Guix be able to give me anything that Nix doesn't? I don't know. My first milestone would be just getting something equivalent to my NixOS desktop config running there, and figuring out a quicker way to iterate. The rest comes later.

1. If you send me a comment saying thattechnicallythe Nix CLI knows about the magic nixpkgs channel syntax in NIX_PATH entries I will force you to run Ubuntu in production.↩
2. Yes, I know about Guix inferiors.↩
