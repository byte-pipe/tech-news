---
title: Configuring Storybook for TypeScript and Tailwind, with Astro 🚀😡 - DEV Community
url: https://dev.to/ingosteinke/rediscovering-storybook-with-typescript-and-tailwind-m8h
site_name: devto
fetched_at: '2025-09-08T11:06:04.340302'
original_url: https://dev.to/ingosteinke/rediscovering-storybook-with-typescript-and-tailwind-m8h
author: Ingo Steinke, web developer
date: '2025-09-02'
description: I have worked with Storybook in the past and I loved its pragmatic, standalone, and interactive... Tagged with astro, typescript, react, webdev.
tags: '#astro, #typescript, #react, #webdev'
---

I have worked with Storybook in the past and I loved its pragmatic, standalone, and interactive preview functionality in a React application.

Fast forward six years, Storybook is still there! Storyknobs are deprecated, and so are several other add-ons that I came and go while I was mostly working with JAMStack (SSG) and LAMP stack (PHP-based frameworks like Symfony and WordPress). Welcome to Vite and Vitest making everything work much smoother now. Not?

## Integrating Astro 5, Storybook 9, Vite 7, and Tailwind 3 🐇🕳️

### Ingo Steinke, web developer ・ Aug 8

#webdev

#discuss

#tailwindcss

#vite

Maybe I shouldn't write this kind of blog posts. They might underminde the illusion of senior mastery and doubtless confidence as a 10x developer or whatever who always keeps calm and enjoys figuring out awkward configuration details and cobble them together, and I shouldn't give away my learnings for free without earning some StackOverflow reputation at least.

Maybe I've just got an unlucky talent to spot rare errors and edge cases everywhere. Documentations don't cover my specific use case, conflicting peer dependencies make me spend days to set up a new project, and AI fails to vibe-code my projects, like Claude freezes and crashes my browser before I even have a chance to use up all my AI tokens.

Only with Storybook does the pesky, detailed configuration with incomprehensible error messages and misleading AI responses really make you angry again.

However, I'm just exaggerating to tell a story for the sake of learning. We will see...

## TypeScript in Storybook, with Astro

Creating stories is easy. Just add some boilerplate code that imports a React component and, optionally, add testable behavior.

Although Storybook doesn't support Astro, as Fantinel points out in hisStorybook + Astro + Svelte tutorial, we can write components in React (or Svelte, Solid, Vue, ...) even for static elements, and those can be tested in Storybook.

The code below is correct but incomplete. We must define every content property (defined in Astro'scontent.config.ts, imported inBook.tsx, in turn imported inBook.stories.ts, the file below).

import

type

{

Meta
,

StoryObj

}

from

'
@storybook/react-vite
'
;

import

Book

from

'
./Book.tsx
'
;

const

meta

=

{


component
:

Book
,

}

satisfies

Meta
<
typeof

Book
>
;

export

default

meta
;

type

Story

=

StoryObj
<
typeof

meta
>
;

export

const

Primary
:

Story

=

{


args
:

{


title
:

'
my title
'
,


description
:

'
my description
'
,


},

};

Enter fullscreen mode

Exit fullscreen mode

Surprise, surprise, if I copy the file and replaceBookbySearchInput, why does it fail atconst meta = { component: SearchInputwithTS2322: Type Element is not assignable to type ComponentType<Element> | undefined?

That's most probably because mySearchInputcomponent isn't ready yet and includes no explicit type definitions and doesn't even import React explicitly? Then why isSearchInput.tsxsupposed to be error-free?

const

SearchInput

=

(


<
label

...
>


<
/label
>

);

export

default

SearchInput
;

Enter fullscreen mode

Exit fullscreen mode

The minimal code above proves that it's it generally not necessary to import React in TSX files when using React 17 or newer with the modern JSX transform enabled in your TypeScript configuration:


"compilerOptions"
:

{


"jsx"
:

"react-jsx"

Enter fullscreen mode

Exit fullscreen mode

The first examples in theofficial React TypeScript introductioncause an editor warningTS7005: variable ... implicitly has an any type, when working in strict mode.

The following code is better.

interface

SearchInputProps

{}

const

SearchInput
:

React
.
FC
<
SearchInputProps
>

=

(
props
)

=>

{

Enter fullscreen mode

Exit fullscreen mode

Now Storybook should be happy, and we can add properties and their types later when we proceed to develop. Only that it isn't happy yet.SearchInput.stories.tsfails because[plugin:vite:import-analysis] Failed to resolve import "astro:content" from "src/components/Book.tsx". Does the file exist?/home/ingo/PhpstormProjects/bookstack-reading-list-app/src/components/Book.tsx:2:18

What's this? How are both components related?

Thanks to Storybook, we can see the same errors from a different perspective in different syntax highlighting colors.

I don't even mention "book" anywhere in my search input component file, except as part of "storybook". This makes no sense and, according to Google and AI assistants, never happens. Nevermind.

Somewhere in the middle of the huge, verbose, warning text is a helpful hidden hint like "property author is missing in type". Addingauthorto myBooksstory removed the error message in theSearchInputstory.

Books still fail for other reasons, while neither my IDE, noreslint, nor my Astro/Vite build process show any errors, so this is truly Storybook-specific.

### Rolling the Dice: AI Advice 🎲

Have you tried turning it off an on again? Deleting node_modules? Clearing your Storybook cache?Sometimes, caching is the issue, you know?

Ormaybeyou needsome specific tweaksto your configiguration or your paths cause MIME type mismatches? Just roll the dice and change your code randomly until it eventually works.

Seriously, let's read the error message details before asking AI.Sure itmaylikelymake sensesometimes?

Failed to fetch dynamically imported module:http://localhost:6006/src/components/Book.stories.ts?t=1756739306131The component failed to render properly,likelydue to a configuration issue in Storybook. Here are some common causes and how you can address them:

Missing Context/Providers:You can use decorators to supply specific contexts or providers, which aresometimesnecessary for components to render correctly. For detailed instructions on using decorators, please visit the Decorators documentation.Misconfigured Webpack or Vite:Verify that Storybook picks up all necessary settings for loaders, plugins, and other relevant parameters. You can find step-by-step guides for configuring Webpack or Vite with Storybook.Missing Environment Variables:Your Storybookmayrequire specific environment variables to function as intended. You can set up custom environment variables as outlined in the Environment Variables documentation.

If any of the above was true, why wouldn't the static SearchInput story fail as well? And how wouldfetchingfail if the implicit import was based on an existing file name? I double-checked, the URL returnsBook.stories.ts, and I know it used to work, before I refactored the typing from an interface to inferred from another Zod file that's imported by theBooks, but not by the simplerSearchInputcomponent.

import

ToggleButton

from

'
./ToggleButton
'
;

// this works

import

{

bookSchema

}

from

'
../content.config
'
;

// this doesn't?

Enter fullscreen mode

Exit fullscreen mode

Mosty likely,..is unreachable for Storybook, so "addingsome specific tweaksto my configuration" is really the correct solution for fixing my story files.

### Alias Paths and Configuration Confusion

Relative paths are considered hard to read, and using an alias like@schemasis considered best practice both for Astro and for Storybook. However, Astro allegedly always expectssrc/content.config.tsat that very unchangeable spot, so we must split that file and import our schema from an aliased schema directory, just to make sure things get not complicated, but orderly enough so that all parts of my tech stack can collaborate without failing due to their own little opinionated expectations.

If you happen to be a maintainer of the Astro or Storybook documentation, you might consider adding a note, just in case. However, the docs often seem complete in hindsight.

Astro supports import aliases

also known as TypeScript path aliases. To keep our code DRY and don't define them redundantly both for Astro/TypeScript and for Storybook, there isTsconfigPathsPluginortsconfigPathsthat should work both with a classic Webpack or a modern Vite configuration when applied in theviteFinalfunction in Storybook's configuration and define the actual paths nowhere else but in thetsconfig.jsonfile consistently throughout the entire project.

// .storybook/main.ts

import

type

{

StorybookConfig

}

from

'
@storybook/react-vite
'
;

import

{

mergeConfig

}

from

'
vite
'
;

import

tsconfigPaths

from

'
vite-tsconfig-paths
'
;

const

config
:

StorybookConfig

=

{


async

viteFinal
(
config
)

{


return

mergeConfig
(
config
,

{


base
:

'
../src/
'
,


plugins
:

[


tsconfigPaths
(),


],

Enter fullscreen mode

Exit fullscreen mode

Note thattsconfigPaths()is imported and executed as a Vite plugin, while the postCSS plugins use require module syntax within the same Vite configuration section:


async

viteFinal
(
config
)

{


return

mergeConfig
(
config
,

{


css
:

{


postcss
:

{


plugins
:

[


require
(
'
tailwindcss
'
),


require
(
'
autoprefixer
'
),

Enter fullscreen mode

Exit fullscreen mode

We can use tsconfigPaths in Astro's Vite configuration or in a standalonevite.config.tsconfiguration.

Now we're nearly there.

import

{

defineConfig

}

from

'
astro/config
'
;

import

react

from

'
@astrojs/react
'
;

import

tailwind

from

'
@astrojs/tailwind
'
;

import

sitemap

from

'
@astrojs/sitemap
'
;

import

tsconfigPaths

from

'
vite-tsconfig-paths
'
;

import

type

{

Plugin

}

from

'
vite
'
;

export

default

defineConfig
({


integrations
:

[
react
(),

tailwind
(),

sitemap
()],


vite
:

{


plugins
:

[
tsconfigPaths
()

as

Plugin
]

Enter fullscreen mode

Exit fullscreen mode

TS2322: Type Plugin$1 is not assignable to type PluginOptionType Plugin$1 is not assignable to type PluginTypes of property hotUpdate are incompatible.

Unless we're preparing for an academic TypeScript exam, at this point I'd just write

plugins: [tsconfigPaths() as any]

and save my precious time for solving real problems.

The actual paths are defined explicitly or with a global pattern like in the first line, once and for all, without repetition, only intsconfig.json:

//

tsconfig.json

{


"compilerOptions"
:

{


"paths"
:

{


"paths"
:

{


"@/*"
:

[
"src/*"
],


"@components/*"
:

[
"src/components/*"
],


"@content/*"
:

[
"src/content/*"
],


"@schemas/*"
:

[
"src/schemas/*"
],


"@styles/*"
:

[
"src/styles/*"
]


}

Enter fullscreen mode

Exit fullscreen mode

Note thatpathsis acompilerOption.

Use these aliases everywhere, so that

import

{

bookSchema

}

from

'
../content.config
'
;

// becomes

import

{

bookSchema

}

from

'
@schemas/bookSchema
'
;

Enter fullscreen mode

Exit fullscreen mode

Inside our schema file, don'timport { z } from 'astro:content'butimport { z } from 'zod'so that Storybook can find it, too.

Irepeat myself, but none of this configuration fiddling is what I understand by "frontend web development". Why, after abadoning Webpack for good and supporting modern JS and CSS in most browsers, do we still spend hours to match imports and packages to each other, knowing that our fragile harmony will eventually break after the next major update or deprecation?

## Coding in the Age of Constant Deprecation?

### Ingo Steinke, web developer ・ Aug 7

#webdev

#discuss

#programming

#productivity

After fixing all the little errors that could never upset me, can finally proceed with my components' storyies' styling, please?

## Tailwind and Daisy in Storybook, with Astro

After setting up Tailwind in a Vite-based project, everything should work out of the box. Even when, due to Astro, they're not the latest versions. Even without adding daisyUI.

And it does.

## Conclusion

These are some public notes (and rants) in case someone, like my future self, might find them useful.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
