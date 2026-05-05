---
title: 'Migrating from Astro 5 to Astro 6: A Real-World Breakdown 📖 - DEV Community'
url: https://dev.to/harshil1712/migrating-from-astro-5-to-astro-6-a-real-world-breakdown-2d0c
site_name: devto
content_file: devto-migrating-from-astro-5-to-astro-6-a-real-world-bre
fetched_at: '2026-05-05T11:59:36.955302'
original_url: https://dev.to/harshil1712/migrating-from-astro-5-to-astro-6-a-real-world-breakdown-2d0c
author: Harshil Agrawal
date: '2026-05-03'
description: I have been meaning to upgrade my personal site to Astro 6 for a while. The release notes sat in my... Tagged with ai, devjournal, javascript, webdev.
tags: '#ai, #devjournal, #javascript, #webdev'
---

I have been meaning to upgrademy personal sitetoAstro6 for a while. The release notes sat in my open tabs for weeks, and every time I sat down to do it, I found an excuse to work on something else. This week, I finally ran out of excuses. I carved out an afternoon, rannpx @astrojs/upgrade, crossed my fingers, and expected a smooth ride.

The dev server crashed immediately with a cryptic error about a missingtailwindcsspackage.

I stared at the error for a minute. Then I did what any reasonable developer would do in 2026 — I looped in an AI coding agent and told it to help me fix everything.

This post is the field guide I wish I had, and also a reminder that AI agents are incredibly helpful but dangerously confident. You still need to know what you're doing.

## What I started with

* Astro 5.x (various patch releases)
* @astrojs/cloudflarev12.x
* @astrojs/tailwindv5.x
* Legacy content collections (src/content/config.ts,type: 'content'/'data')
* astro-expressive-codev0.38.x
* astro-iconv1.1.5

## What I ended up with

* Astro 6.2
* @astrojs/cloudflarev13
* Tailwind CSS v4 (@tailwindcss/vite)
* astro-expressive-codev0.41.7
* A custom inline-SVG icon component (replacingastro-icon)

## Error 1:Cannot find package 'tailwindcss'

Cannot find package 
'tailwindcss'
 imported from
.../node_modules/@astrojs/tailwind/dist/index.js

Enter fullscreen mode

Exit fullscreen mode

### What happened

@astrojs/tailwindv6 was installed by the upgrade command, but itspackage.jsononly liststailwindcssas apeer dependency— it does not bundle it. Sincetailwindcsswasn't in mydependencies, Node couldn't resolve it.

### The agent's diagnosis

I pasted the error into the agent and asked what was going on. It diagnosed the peer dependency issue immediately and confidently moved to PostCSS. It addedpostcss.config.mjs,autoprefixedand the@tailwinddirectives. The site was functional again, but the apporach was completely off.

I had to ask the agent to stick with TailwindCSS and migrate to PostCSS. I asked the agent to check the Astro docs instead of guessing. The agent then used the tools and came up with two options:

Option A: Stay on Tailwind 3 (simplest)

Installtailwindcss@3alongside the integration and keep everything as-is:

npm 
install 
tailwindcss@3

Enter fullscreen mode

Exit fullscreen mode

Yourastro.config.mjsstays the same:

import
 
tailwind
 
from
 
'
@astrojs/tailwind
'
;

// ...

integrations
:
 
[
tailwind
()]

Enter fullscreen mode

Exit fullscreen mode

This is the path Astro docs recommend for legacy Tailwind 3 projects.

Option B: Upgrade to Tailwind 4

Astro 5.2+ includes anastro add tailwindcommand that installs the official Vite plugin (@tailwindcss/vite), which is the new recommended way to use Tailwind 4 in Astro.

npx astro add tailwind

Enter fullscreen mode

Exit fullscreen mode

This sets up:

1. @tailwindcss/vitein your Vite plugins (viaastro.config.mjs)
2. src/styles/global.csswith@import "tailwindcss";
3. Removes the need fortailwind.config.mjs— v4 uses CSS-based configuration instead

If you go this route, you can then remove@astrojs/tailwindentirely and followTailwind's v4 upgrade guideto migrate your custom theme to CSS variables.

### What happened next: The correct apporach

I instructed the agent to proceed withOption B, runningnpx astro add tailwindto get the proper Vite plugin set up, then migrated the custom theme into the new@themeblock inglobal.css:

@import
 
"tailwindcss"
;

@theme
 
{

 
--color-primary
:
 
#f97316
;

 
--color-hover
:
 
#ea580c
;

 
--color-light
:
 
rgba
(
249
,
 
115
,
 
22
,
 
0.15
);

 
--color-secondary
:
 
#fdba74
;

}

@variant
 
dark
 
(
&
:
where
(.
dark
,
 
.
dark
 
*
));

Enter fullscreen mode

Exit fullscreen mode

If you want to keep Tailwind 3:use Option A above and let@astrojs/tailwinddo the work.

If you want Tailwind 4:use Option B and the official Vite plugin. Don't manually wire PostCSS.

## Error 2:LegacyContentConfigError

With Tailwind sorted, I restarted the dev server feeling optimistic. Then the next error hit.

[LegacyContentConfigError] Found legacy content config file in
"src/content/config.ts". Please move this file to
"src/content.config.ts" and ensure each collection has a loader defined.

Enter fullscreen mode

Exit fullscreen mode

### What happened

Astro 5 introduced theContent Layer API, but kept automatic backwards compatibility for old collections. Astro 6 removed that safety net entirely. Mysrc/content/config.tswithtype: 'content'andtype: 'data'was no longer valid.

### The fix

The agent handled this migration competently. It moved the file, rewrote the imports, and configured the loaders:

Before:

import
 
{
 
defineCollection
,
 
z
 
}
 
from
 
'
astro:content
'
;

const
 
writings
 
=
 
defineCollection
({

 
type
:
 
'
content
'
,

 
schema
:
 
z
.
object
({
 
...
 
})

});

const
 
projects
 
=
 
defineCollection
({

 
type
:
 
'
data
'
,

 
schema
:
 
z
.
array
(
z
.
object
({
 
...
 
}))

});

export
 
const
 
collections
 
=
 
{
 
writings
,
 
projects
 
};

Enter fullscreen mode

Exit fullscreen mode

After:

import
 
{
 
defineCollection
 
}
 
from
 
'
astro:content
'
;

import
 
{
 
glob
,
 
file
 
}
 
from
 
'
astro/loaders
'
;

import
 
{
 
z
 
}
 
from
 
'
astro/zod
'
;

const
 
writings
 
=
 
defineCollection
({

 
loader
:
 
glob
({
 
pattern
:
 
'
**/[^_]*.mdx
'
,
 
base
:
 
'
./src/content/writings
'
 
}),

 
schema
:
 
z
.
object
({
 
...
 
})

});

const
 
projects
 
=
 
defineCollection
({

 
loader
:
 
file
(
'
src/content/projects/projects.json
'
),

 
schema
:
 
z
.
object
({
 
...
 
})
 
// not z.array(...)

});

export
 
const
 
collections
 
=
 
{
 
writings
,
 
projects
 
};

Enter fullscreen mode

Exit fullscreen mode

Key changes:

* File location:src/content/config.ts→src/content.config.ts(project root insidesrc/).
* zimport:astro:content→astro/zod.
* typeremoved:No moretype: 'content'ortype: 'data'. You explicitly declare aloader.
* Data collections:If you were usingtype: 'data'with a JSON file, the newfile()loader returns one entry per top-level object. The schema should bez.object(...)(one item), notz.array(...)(the whole file).
* slug→id:In the old API,entry.slugwas auto-derived. In the new API,entry.idis the identifier. My URLs needed updating:

// Before
href={`/writings/${post.slug}`}
// After
href={`/writings/${post.id}`}

Enter fullscreen mode

Exit fullscreen mode

Here's where the agent overstepped. It told me that since my posts live infolder/index.mdxstructures,glob()would generate IDs from file paths, producing something likemigrating-astro-5-to-astro-6/index. It suggested I strip the suffix:

href={`/writings/${post.id.replace(/\/index$/, '')}`}

Enter fullscreen mode

Exit fullscreen mode

Something about that felt off. Every post in mywritingscollection already has aslugfield in its frontmatter, and I had a hunch Astro would use that as the entryid. I pushed back and asked the agent to verify against Astro's documentation.

After checking the docs, it couldn't actually confirm that/indexgets appended whenslugis present in frontmatter. And in practice,post.idwas alreadymigrating-astro-5-to-astro-6and nevermigrating-astro-5-to-astro-6/index. The.replace()was unnecessary for my setup, and the simplepost.idworks perfectly.

Note:always verify agent output against your own code and build output. The agent is fast, but you are the one who has to ship it.

So far, so good. The agent was saving me hours. Then it got cocky.

## Error 3:Property 'runtime' does not exist on type 'Locals'

Content collections were fixed. I was ready to see the site render. But the Cloudflare adapter had other plans.

ts
(
2339
):
 
Property
 
'
runtime
'
 
does
 
not
 
exist
 
on
 
type
 
'
Locals
'
.

Enter fullscreen mode

Exit fullscreen mode

### What happened

@astrojs/cloudflarev13 removedAstro.locals.runtimeentirely. The new documented approach is:

import
 
{
 
env
 
}
 
from
 
'
cloudflare:workers
'
;

const
 
kv
 
=
 
env
.
MY_KV
;

Enter fullscreen mode

Exit fullscreen mode

I migrated my API routes to this pattern. But then I hit a runtime error in dev:

module
 
is
 
not
 
defined

Enter fullscreen mode

Exit fullscreen mode

originating from the Cloudflare Vite plugin's worker runner.

The agent spent a while suggesting random fixes — clearing caches, reordering imports, checking Vite config — none of which worked. I ended up tracing it myself:@astrojs/cloudflarev13's dev server runs insideworkerd, and it has an incompatibility with theastro-iconintegration. Whenastro-icon's<Icon>component was first rendered, the workerd module runner would crash with that crypticmodule is not definederror, breaking every route on the site.

At this point, the was frustrated. It had already spent more time on this than it planned. It downgraded back to@astrojs/cloudflarev12 just to get something working.

But we didn't stop there. The agent suggested replacingastro-iconentirely with a tiny custom component that inlines SVG paths from@iconify-json/mdi. Thirty lines of code. No virtual modules. Noworkerdcompatibility issues. We tried it, switched back to v13, and that was the unlock.

### The fix: finish the v13 migration properly

First, updatewrangler.tomlto use the v13 entrypoint:

main
 
=
 
"@astrojs/cloudflare/entrypoints/server"

Enter fullscreen mode

Exit fullscreen mode

Then migrate all code fromAstro.locals.runtime.envtoimport { env } from 'cloudflare:workers':

Before:

const
 
{
 
env
 
}
 
=
 
Astro
.
locals
.
runtime
;

const
 
kv
 
=
 
env
.
VOTES
;

Enter fullscreen mode

Exit fullscreen mode

After:

import
 
{
 
env
 
}
 
from
 
'
cloudflare:workers
'
;

const
 
kv
 
=
 
env
.
VOTES
;

Enter fullscreen mode

Exit fullscreen mode

For TypeScript, I also had to augmentCloudflare.Envinsrc/env.d.tswith secrets that aren't declared inwrangler.toml(likeYOUTUBE_API_KEYandGITHUB_TOKEN):

declare
 
namespace
 
Cloudflare
 
{

 
interface
 
Env
 
{

 
YOUTUBE_API_KEY
:
 
string
;

 
PLAYLIST_ID
:
 
string
;

 
GITHUB_TOKEN
:
 
string
;

 
}

}

Enter fullscreen mode

Exit fullscreen mode

Note:The agent didn't know about thewrangler typescommand. This command generates the types, which would have prevented the manual addition.

This is required becauseimport { env } from 'cloudflare:workers'is typed against the globalCloudflare.Envinterface, not the project-levelEnvthatwrangler typesgenerates.

Finally, removeastro-iconfrompackage.jsonandastro.config.mjs, and replace<Icon name="mdi:github" />usages with the custom component. Problem solved.

## Error 4:astro-expressive-codepeer dependency mismatch

That was the biggest battle. I thought I was in the clear. Thennpm run buildreminded me that integrations have their own timelines.

peer astro@"^4.0.0-beta || ^5.0.0-beta || ^3.3.0" from astro-expressive-code@0.38.3

Enter fullscreen mode

Exit fullscreen mode

### What happened

The upgrade command didn't bumpastro-expressive-code, so it still had a peer dependency range that excluded Astro 6.

### The fix

npm 
install 
astro-expressive-code@0.41.7

Enter fullscreen mode

Exit fullscreen mode

v0.41.7 officially supports Astro 6.

This one the agent got right on the first try. I take the wins where I can get them.

## Error 5:Buffer<ArrayBufferLike>' is not assignable to parameter of type 'BodyInit'

Just when I thought the dependency wars were over, TypeScript had one more surprise for me.

In my OG image generation endpoint, I had:

const
 
screenshot
 
=
 
await
 
page
.
screenshot
({
 
...
 
});

return
 
new
 
Response
(
screenshot
,
 
{
 
...
 
});

Enter fullscreen mode

Exit fullscreen mode

After the upgrades, TypeScript started rejectingBufferas aResponsebody. This wasn't a runtime issue —Puppeteerstill returns aBuffer— butastro check(and thereforenpm run build) flags it.

### The fix

Converted toUint8Arraybefore passing toResponse:

return
 
new
 
Response
(
new
 
Uint8Array
(
screenshot
),
 
{
 
...
 
});

Enter fullscreen mode

Exit fullscreen mode

This satisfies both the Workers runtime types and TypeScript's strict checks.

## Final checklist

Command

Status

npm install

✅ (no 
--legacy-peer-deps
)

npm run dev

✅ All routes render in 
workerd

npm run build

✅

npm run preview

✅

## What I learned

* npx @astrojs/upgradehandles the Astro core bump, but integrations often have their own timeline.Always checknpm lsfor peer dependency warnings after upgrading.
* Content collections migration is unavoidable in v6.Astro 5 gave you a grace period. Astro 6 does not. The newloaderAPI is actually clearer once you get used to it.
* Adapter upgrades are the riskiest part.@astrojs/cloudflarev13 made major changes to how env bindings work and moved the dev server intoworkerd. The upside is your dev environment is now nearly identical to production. The downside is that some integrations (likeastro-icon) aren't yet compatible withworkerd's module loading.
* Build != dev.My site built successfully long before the dev server worked. The v13 Cloudflare adapter broke only in dev (astro dev) because of how it runs code insideworkerd. Always test both.
* When an integration breaks, check the official docs before inventing a workaround.I had already pulled@astrojs/tailwindand installedtailwindcssdirectly, but the agent pointed me to@tailwindcss/vite— the proper Vite plugin for Tailwind CSS v4. Astro'snpx astro add tailwindcommand sets this up automatically for v4, which is the supported path.
* import { env } from 'cloudflare:workers'is the new standard.It replacesAstro.locals.runtime.envcompletely. If you're on v13, embrace it — just remember thatwrangler typesgenerates theEnvinterface, butcloudflare:workersreads fromCloudflare.Env, so you may need to augment the namespace for secrets.
* AI agents are great teammates, but bad team leads.They will suggest wrong approaches confidently, miss root causes, and hallucinate migration details. You need to know enough to push back, verify claims, and direct the strategy.

## Summary

Upgrading from Astro 5 to 6 is not a single command. The core bump is smooth, but the integrations around it — Tailwind, Cloudflare, expressive-code — each carry their own breaking changes. If I were doing this again, I would:

1. Start with the content collections migration (src/content/config.ts→src/content.config.ts).
2. Decide on Tailwind 3 vs. 4 before running the upgrade. Usenpx astro add tailwindfor v4, or installtailwindcss@3for legacy v3.
3. Go straight to@astrojs/cloudflarev13. TheAstro.locals.runtime→import { env } from 'cloudflare:workers'migration is mechanical.
4. Testnpm run dev, not justnpm run build.workerdis stricter than Node.

Theworkerddev server in v13 is a net positive — my local environment now behaves almost exactly like production — but it is unforgiving. If you hitmodule is not definedor similar low-level errors, trace which integration is triggering them. Replacingastro-iconwith a custom 30-line SVG component removed an entire class of compatibility issues for me.

## Further reading

* Astro 6.0 migration guide
* Content Layer API documentation
* Cloudflare adapter for Astro
* Tailwind CSS v4 upgrade guide

If you're planning this migration yourself, I'd love to hear how it goes. Feel free to hit me up onX/Twitterif you hit a wall I didn't cover, or if you found a cleaner fix for any of these errors. Stay tuned for more write-ups like this.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse