---
title: Integrating SEO Components into Discord - DEV Community
url: https://dev.to/thomasbnt/integrating-seo-components-into-discord-2d8g
site_name: devto
content_file: devto-integrating-seo-components-into-discord-dev-commun
fetched_at: '2026-10-16T15:12:15.737111'
original_url: https://dev.to/thomasbnt/integrating-seo-components-into-discord-2d8g
author: Thomas Bonnet
date: '2026-10-13'
description: 'If you paste a link to your website in a Discord channel, a small card appears automatically: title,... Tagged with webdev, seo, html, discord.'
tags: '#webdev, #seo, #html, #discord'
---

Requires server-side Open Graph tags first

If you paste a link to your website in a Discord channel, a small card appears automatically: title, description, and an image. You didn’t have to write any special code for this, it’s the default behavior.

Discord has just added another option: to completely replace this card with a custom preview, featuring formatted text, an image gallery, and buttons.

I tested this on this blog, and here's how it works.

Here's what you need to have set up before you start:

* A site served over HTTPS
* Open Graph tags already present (required, even with anembedcomponent)
* Server-side rendering (the HTML must contain the tags in the response itself, not after a JavaScript script)
* The Discordbot crawler is allowed if a WAF, CDN, or rate limiter is in front of the site
* Theembedcomponent's JSON payload is ready (we'll get to that next)

## Default Behavior: Open Graph Tags

Without going into further detail, here's what happens: Discord sends a request to your URL, reads the HTML returned by the server, and looks for Open Graph tags in the<head>element.

If they're there, a card is automatically generated.

<meta
 
property=
"og:title"
 
content=
"Title of this page"
 
/>

<meta
 
property=
"og:description"
 
content=
"Description of this page"
 
/>

<meta
 
property=
"og:image"
 
content=
"https://example.com/og-image.png"
 
/>

<meta
 
property=
"og:url"
 
content=
"https://example.com/page"
 
/>

<meta
 
name=
"twitter:card"
 
content=
"summary_large_image"
 
/>

Enter fullscreen mode

Exit fullscreen mode

How it appears on Discord, based solely on these tags:

Here are three key points about how this works, because they’re important for what comes next as well:

* The tags must be in the HTMLsent by the server. Discord does not execute any JavaScript; a tag added later by client-side JS does not exist for Discord.
* The crawler identifies itself with the user-agentMozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com). If a WAF or rate limiter blocks bots, you must explicitly allowDiscordbotthrough.
* The preview is cached for about30 minutes. To force a refresh during testing, simply add?v=2to the URL.

I go into detail about these Open Graph tags (image sizes, Twitter Card tags, etc.) in "A Few Tips for Improving Your SEO" if you want to explore that topic further.

## The new format: component embeds

If there are no embed components on the page, Discord displays nothing more than the card shown above.

This is an addition, not a mandatory replacement: theog:*tags are still required in all cases. They serve as a fallback if the embed cannot be displayed (e.g., a context that doesn’t support it, an invalid payload, etc.).

On the crawler side, the process is the same as for the standard card, with one additional step:

1. A link to your page is posted in a Discord message.
2. Discord fetches the URL and reads the HTML.
3. It also looks for anembedcomponent tag. If it exists, it parses the JSON and retrieves the metadata for each image in the payload.
4. If the payload is valid, it replaces the Open Graph card with this custom rendering. Otherwise, it goes back to the previous step.

Two ways to display this JSON:

Option 1,inline, a<script>within the<head>:

<script 
id=
"discord:component-embed"
 
type=
"application/json"
>

 
{

 
"
component
"
:
 
{

 
"
type
"
:
 
17
,

 
"
components
"
:
 
[

 
{

 
"
type
"
:
 
10
,

 
"
content
"
:
 
"
# Patch Notes
\n
- Correction d'un bug d'affichage
"

 
}

 
]

 
}

 
}

</script>

Enter fullscreen mode

Exit fullscreen mode

Option 2,in external JSON, with a link pointing to a file on the same domain (or a subdomain):

<link

 
rel=
"discord:component-embed"

 
type=
"application/json"

 
href=
"https://exemple.com/embeds/article.json"

/>

Enter fullscreen mode

Exit fullscreen mode

This option has a strict limit:3,000 bytesfor the raw file. For an embed with an image gallery and buttons, the inline option allows for a larger size.

The rootcomponentmust be a *Container(type: 17).

It can contain up to40 componentsin total, from among those listed in the table below. Any other component type invalidates the entire payload:

Type

Component

Notes

1

Action Row

row of buttons

2

Button

link style only (
style: 5
), with 
label
 and/or 
emoji

9

Section

text + an element (thumbnail or button)

10

Text Display

Discord Markdown (headings, bold, lists, links...)

11

Thumbnail

small image attached to a Section

12

Media Gallery

up to several images/videos, in large format

14

Separator

separator line

17

Container

the root component

For images (thumbnails and Media Gallery), you only need to provide the URL; Discord will automatically retrieve the dimensions and file type:

{
 
“url”:
 
“https://exemple.com/images/hero.webp”
 
}

Enter fullscreen mode

Exit fullscreen mode

Supported formats: PNG, GIF, JPEG, WebP, AVIF, and for the Media Gallery, MP4/MOV/WebM as well.

## What I've set up on my blog

On every post onmy blog, in addition to the standard Open Graph tags (which are still there, hidden), I now include an embed component.

It’s built using the same data as the standard card: the title, description, cover image, and the post’s accent color.

The structure looks like this, simplified:

{

 
"component"
:
 
{

 
"type"
:
 
17
,

 
"accent_color"
:
 
5793266
,

 
"components"
:
 
[

 
{

 
"type"
:
 
10
,

 
"content"
:
 
"# [Title of the post](https://thomasbnt.dev/blog/...)
\n
Description."

 
},

 
{

 
"type"
:
 
12
,

 
"items"
:
 
[{
 
"media"
:
 
{
 
"url"
:
 
"https://thomasbnt.dev/.../index.png"
 
}
 
}]

 
},

 
{

 
"type"
:
 
1
,

 
"components"
:
 
[

 
{

 
"type"
:
 
2
,

 
"style"
:
 
5
,

 
"url"
:
 
"https://thomasbnt.dev/blog/..."
,

 
"label"
:
 
"Lire l'article"

 
},

 
{

 
"type"
:
 
2
,

 
"style"
:
 
5
,

 
"url"
:
 
"https://thomasbnt.dev/blog/"
,

 
"label"
:
 
"Blog"

 
}

 
]

 
}

 
]

 
}

}

Enter fullscreen mode

Exit fullscreen mode

The final result on Discord:

Some decisions made while building it:

* Media Gallery instead of Thumbnail: At first, I went with a Section + Thumbnail, but the image looked tiny next to the text. The Media Gallery displays the image in full size, like a real banner.
* No Separator: It visually broke up the embed for no reason between the text and the image.
* Two buttons: one to read the article, one to return to the blog. Simple, but it provides an additional entry point directly from Discord.
* accent_color: this is an integer, not a hexadecimal color. This blog already has a color associated with each article (backgroundColorin the frontmatter). I simply convert it to decimal (parseInt(hex.replace(“#”, “”), 16)) rather than managing a new one.

As with the OG tags, this script is generated on the server side during the build (the site is built with Astro, so everything is static), so there’s nothing to execute on the client side.

## Common issues to avoid

* A component not on the list, or an extra key on a button(id,custom_id...) invalidates the entire payload, not just the offending component.
* Removing OG tags because you think they’re no longer needed.They’re still essential: they serve as a fallback whenever the embed doesn’t display.
* The 30-minute cache.While testing, adding?v=2to the URL saves you from wondering for ten minutes why nothing is changing.
* The 10-second time limit.The entire fetch, including images, must be completed within this timeframe. With a Media Gallery that loads multiple images, this limit is reached faster than with a simpleog:image.

## How to Test

DiscordEmbed Debuggershows exactly how the crawler reads a URL: which tags it found, and which embed format it chose. This should be your first step before looking for a bug elsewhere.

## Conclusion

To summarize the logic: even without taking any action, Discord already displays a card based on theog:*tags.

Adding an embed component is an additional option, not a replacement. It only activates if the JSON payload is present and valid; otherwise, Discord automatically falls back to the default card.

On this blog, it’s a simple change: same title, same description, same image as the standard card, just presented differently with direct access to the rest of the blog.

## Resources

* Official documentation on component embeds: the complete spec, with all component types and their constraints.
* Embed Debugger: to see exactly how Discord reads a given URL.
* Some tips for improving your SEO: Open Graph tags, Core Web Vitals, and other technical basics.
* This blog’s Discord server: to test your links or discuss all of this.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (11 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse