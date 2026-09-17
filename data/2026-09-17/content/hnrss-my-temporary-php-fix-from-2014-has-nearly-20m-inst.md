---
title: My temporary PHP fix from 2014 has nearly 20M installs. Today I'm deprecating it. — Jake A. Smith
url: https://jakeasmith.com/blog/http-build-url/
site_name: hnrss
content_file: hnrss-my-temporary-php-fix-from-2014-has-nearly-20m-inst
fetched_at: '2026-09-17T15:27:04.402527'
original_url: https://jakeasmith.com/blog/http-build-url/
date: '2026-09-15'
description: In 2014 I wrote http_build_url, a temporary PHP polyfill for AOL's CMS. Twelve years and nearly 20 million installs later, I'm deprecating it.
tags:
- hackernews
- hnrss
---

← All posts

 
 
 

Twelve years ago, I wrote174 lines of PHPas a stopgap for AOL’s content management system. I put it on Packagist in case anyone else needed the same patch, and somehow it’s been installed nearly 20 million times since. Today I marked it deprecated.

## A temporary shim

In 2014, we were in the middle of upgrading AOL’s CMS from PHP 5.2 to 5.3. Part of that upgrade was dropping version 1 of thepecl_httpextension, which gave us a function calledhttp_build_url(). A CMS deals with a lot of URLs, and ours called that function in dozens of places. I wasn’t touching those. The function seemed straightforward enough to reproduce, so I wrote my ownhttp_build_url(), defined only if the real one didn’t already exist. The old code never knew anything had changed.

Composer was just taking off at the time, which made sharing it easy. I figured it would earn its keep for a year or two, until the PHP community moved on to something better.

## That’s a lot of installs

Well, it wasn’t temporary. It’s been installed from Packagist nearly 20 million times, and it still picks up over 400,000 installs a month.

And it turns out Composer is only part of the picture.WPML, the market-leading multilingual plugin for WordPress, bundles the polyfill directly in its codebase, and WPML says it’s installed on over 1.5 million sites. The domain-name libraryidna-convertdepends on it too, which is how it ships insidethe source of SPIP, a French content management system, and how it ended uppackaged in Debianand Ubuntu. Between all of them, there’s a pretty good chance you’ve visited a website that is still running my code.

I never imagined it would go this far.

## Coming back to it

I didn’t grasp how far it had spread until a few months ago, when I looked at the package for the first time in years. I knew it had users. By 2021 I’d been out of PHP for a while, and the downloads were surprising enough that Iasked for a new maintainer. Three people offered. Shortly after I asked, we lost a family member unexpectedly, and it turned our world upside down for a while. I never followed up, and that’s on me. By the time things settled, other goals had taken over, and I forgot about the package for years.

Along with the numbers, there were a handful of GitHub issues, including one where joining a path onto a URL with a trailing slash strips every letter “a” out of the path. So much for straightforward. Under a comment that reads// Workaround for trailing slashes, my code tacks an “a” onto the path so there’s always a last segment to cut off, then cuts it off with a find-and-replace. When the path ends in a slash, that last segment is just the “a”, and the find-and-replace takes every other “a” in the path with it. I can’t believe the bug went unnoticed for as long as it did.

So I had a decision to make. I could dive back into PHP after almost a decade away, hand the package to one of the people who’d offered, or let it keep sitting there.

## None of the above

It was always meant to be temporary, so I’m retiring it.The PHP League’s URI libraryhas been the community’s answer for years, andPHP 8.5now shipsa standards-compliant URI API in the language itself(thanks tojawirafor pointing me at it). Both are better than a 174-line shim from 2014. Maintaining the package would only delay the move everyone should be making, and handing it over would add a risk on top of that. I don’t doubt anyone who offered, andozhhas kepta forkgoing for YOURLS. But a widely installed package with a new maintainer nobody downstream has vetted is exactly what attackers look for.Veritasium’s video on the xz Utils backdooris the best telling I’ve seen of how that plays out.

The package will keep installing, but it won’t get new fixes, including for the missing-”a” bug. After this long without a change, even a one-line fix could have unintended consequences for someone, with no one around to support it.The READMEshows how to switch.

I wrote this code to ease a painful migration, for myself and anyone else going through the same one. Thank you to everyone who sent a pull request or offered to take it over, and to the people who kept filing issues long after I’d stopped reading them. It was a good run for a temporary fix.

P.S. We never migrated AOL’s CMS off the “temporary” polyfill. It ran there until the whole platform was shut down around 2020.