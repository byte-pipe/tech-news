---
title: RCE in React Server Components · Advisory · vercel/next.js · GitHub
url: https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp
site_name: hackernews
fetched_at: '2025-12-04T11:08:11.918796'
original_url: https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp
author: rayhaanj
date: '2025-12-04'
description: GitHub is where people build software. More than 150 million people use GitHub to discover, fork, and contribute to over 420 million projects.
---

vercel



/

next.js

Public

* NotificationsYou must be signed in to change notification settings
* Fork30k
* Star136k

# RCE in React Server Components

 Critical

aaronbrown-vercel

 published

GHSA-9qr9-h5gf-34mp

Dec 3, 2025

## Package

npm

next


 (
npm
)


## Affected versions

>=14.3.0-canary.77, >=15, >=16

## Patched versions

v16.0.7, v15.5.7, v15.4.8, v15.3.6, v15.2.6, v15.1.9, v15.0.5

## Description

A vulnerability affects certain React packages1for versions 19.0.0, 19.1.0, 19.1.1, and 19.2.0 and frameworks that use the affected packages, including Next.js 15.x and 16.x using the App Router. The issue is tracked upstream asCVE-2025-55182.

Fixed in:React: 19.0.1, 19.1.2, 19.2.1Next.js: 15.0.5, 15.1.9, 15.2.6, 15.3.6, 15.4.8, 15.5.7, 16.0.7

The vulnerability also affects experimental canary releases starting with 14.3.0-canary.77. Users on any of the 14.3 canary builds should either downgrade to a 14.x stable release or 14.3.0-canary.76.

All users of stable 15.x or 16.x Next.js versions should upgrade to a patched, stable version immediately.

1The affected React packages are:

* react-server-dom-parcel
* react-server-dom-turbopack
* react-server-dom-webpack
