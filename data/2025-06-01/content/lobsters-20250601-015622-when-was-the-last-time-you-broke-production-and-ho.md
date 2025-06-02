---
title: When was the last time you broke production and how? | Lobsters
url: |
  https://lobste.rs/s/ytefme/when_was_last_time_you_broke_production
site_name: lobsters
fetched_at: |
  2025-06-01T01:56:22.775760
original_url: |
  https://lobste.rs/s/ytefme/when_was_last_time_you_broke_production
date: 2025-06-01
description: ☶
tags: ask, practices
---



In 2020, I tried to remove capabilities from a privileged UI context in Firefox. This context can request arbitrary URLs (ignoring the Same-Origin Policy) and do a lot of dangerous stuff. It has wide access to user data and settings. I removed everything I could but also made more my block permissive for tests in CI, because they would often do complicated stuff with these APIs.

Anyway, at some point I had a successful CI run that blocked A LOT of stuff. Including downloading things with privileges. Basically everything that wasnât part of the browser build. In the end, I could block all access to http and https URL schemes. And it was green in CI. Perfect!

At some point, I requested reviews and got it landed in our repository.

Next thing I know is Firefox Nightly doesnât have favicons and the update check stops workingâ¦

Why was this not caught in tests? Well, because I made it more permissive.

And this is why you should (almost) never write code that behaves differently in production than in tests.
