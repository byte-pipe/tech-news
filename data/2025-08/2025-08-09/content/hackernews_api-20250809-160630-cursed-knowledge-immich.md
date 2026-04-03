---
title: Cursed Knowledge | Immich
url: https://immich.app/cursed-knowledge/
site_name: hackernews_api
fetched_at: '2025-08-09T16:06:30.318332'
original_url: https://immich.app/cursed-knowledge/
author: bqmjjx0kac
date: '2025-08-08'
description: Things we wish we didn't know
tags:
- hackernews
- trending
---

Skip to main content
⚠️ The project is under
very active
 development. Expect bugs and changes. Do not use it as
the only way
 to store your photos and videos!

# Cursed Knowledge

Cursed knowledge we have learned as a result of building Immich that we wish we never knew.

* 6/4/2025Zitadel Actions are cursedZitadel is cursed because its custom scripting feature is executed with a JS engine that doesn't support regex named capture groups.[Go JS engine]6/4/2025
* 5/30/2025Entra is cursedMicrosoft Entra supports PKCE, but doesn't include it in its OpenID discovery document. This leads to clients thinking PKCE isn't available.[#18725]5/30/2025
* 5/5/2025Image dimensions in EXIF metadata are cursedThe dimensions in EXIF metadata can be different from the actual dimensions of the image, causing issues with cropping and resizing.[#17974]5/5/2025
* 4/1/2025YAML whitespace is cursedYAML whitespaces are often handled in unintuitive ways.[#17309]4/1/2025
* 9/20/2024Hidden files in Windows are cursedHidden files in Windows cannot be opened with the "w" flag. That, combined with SMB option "hide dot files" leads to a lot of confusion.[#12812]9/20/2024
* 8/7/2024Carriage returns in bash scripts are cursedGit can be configured to automatically convert LF to CRLF on checkout and CRLF breaks bash scripts.[#11613]8/7/2024
* 8/7/2024Fetch inside Cloudflare Workers is cursedFetch requests in Cloudflare Workers use http by default, even if you explicitly specify https, which can often cause redirect loops.[Cloudflare]8/7/2024
* 7/21/2024GPS sharing on mobile is cursedSome phones will silently strip GPS data from images when apps without location permission try to access them.[#11268]7/21/2024
* 7/3/2024PostgreSQL NOTIFY is cursedPostgreSQL does everything in a transaction, including NOTIFY. This means using the socket.io postgres-adapter writes to WAL every 5 seconds.[#10801]7/3/2024
* 7/3/2024npm scripts are cursednpm scripts make a http call to the npm registry each time they run, which means they are a terrible way to execute a health check.[#10796]7/3/2024
* 6/28/202450 extra packages are cursedThere is a user in the JavaScript community who goes around adding "backwards compatibility" to projects. They do this by adding 50 extra package dependencies to your project, which are maintained by them.[#10690]6/28/2024
* 6/25/2024Long passwords are cursedThe bcrypt implementation only uses the first 72 bytes of a string. Any characters after that are ignored.6/25/2024
* 1/31/2024JavaScript Date objects are cursedJavaScript date objects are 1 indexed for years and days, but 0 indexed for months.[#6787]1/31/2024
* 1/9/2024ESM imports are cursedPrior to Node.js v20.8 using --experimental-vm-modules in a CommonJS project that imported an ES module that imported a CommonJS modules would create a segfault and crash Node.js[#6179]1/9/2024
* 12/28/2023PostgreSQL parameters are cursedPostgresSQL has a limit of 65,535 parameters, so bulk inserts can fail with large datasets.[#6034]12/28/2023
* 6/26/2023Secure contexts are cursedSome web features like the clipboard API only work in "secure contexts" (ie. https or localhost)[#2981]6/26/2023
* 2/23/2023TypeORM deletes are cursedThe remove implementation in TypeORM mutates the input, deleting the id property from the original object.[typeorm#6034]2/23/2023
