---
title: How I use Obsidian — Steph Ango
url: https://stephango.com/vault
site_name: hackernews_api
content_file: hackernews_api-how-i-use-obsidian-steph-ango
fetched_at: '2026-02-19T06:00:17.762069'
original_url: https://stephango.com/vault
author: Steph Ango
date: '2026-02-18'
description: My personal Obsidian vault template. A bottom-up approach to note-taking and organizing things I am interested in.
tags:
- hackernews
- trending
---

# How I use Obsidian

I useObsidianto think, take notes, write essays, and publish this site. This is my bottom-up approach to note-taking and organizing things I am interested in. It embraces chaos and laziness to create emergent structure.

In Obsidian, a “vault” is simply a folder of files. This is important because it adheres to myfile over appphilosophy. If you want to create digital artifacts that last, they must be files you can control, in formats that are easy to retrieve and read. Obsidian gives you that freedom.

The following is in no way dogmatic, just one example of how you can use Obsidian. Take the parts you like.

## Vault template

1. Download my vaultor clone it fromthe Github repo.
2. Unzip the.zipfile to a folder of your choosing.
3. In Obsidian open the folder as a vault.

## Theme and related tools

* My themeMinimalwith theFlexokicolor scheme.
* Obsidian Web Clipperto save articles and pages from the web, see myclipper templatesfor specific sites I clip from.
* Obsidian Syncto sync notes between my desktop, phone and tablet.
* Obsidian Basesto view notes by category.
* Obsidian Mapsfor maps used in some of my templates.

## Personal rules

Rules I follow in my personal vault:

* Avoid splitting content into multiple vaults.
* Avoid folders for organization.
* Avoid non-standard Markdown.
* Always pluralize categories and tags.
* Use internal links profusely.
* UseYYYY-MM-DDdates everywhere.
* Use the 7-point scale for ratings.
* Keepa single to-do listper week.

Having aconsistent stylecollapses hundreds of future decisions into one, and gives me focus. For example, I always pluralize tags so I never have to wonder what to name new tags. Choose rules that feel comfortable to you and write them down. Make your own style guide. You can always change your rules later.

## Folders and organization

I use very few folders. I avoid folders because many of my entries belong to more than one area of thought. My system is oriented towards speed and laziness. I don’t want the overhead of having to consider where something should go.

I do not use nested sub-folders. I do not use the file explorer much for navigation. I mostly navigate using the quick switcher, backlinks, or links within a note.

My notes are primarily organized using thecategoriesproperty. Categories display an overview of related notes, using thebasesfeature in Obsidian.

Most of my notes are in the root of the vault, not a folder. This where I write about my personal world: journal entries, essays,evergreennotes, and other personal notes. If a note is in the root, I know it’s something I wrote, or relates directly to me.

Two reference folders I use:

* Referenceswhere I write about things that exist outside my world. Books, movies, places, people, podcasts, etc. Always named using the title e.g.Book title.mdorMovie title.md.
* Clippingswhere I save things other people wrote, mostly essays and articles.

Three admin folders exist so that their contents don’t show up in the file navigation:

* Attachmentsfor images, audio, videos, PDFs, etc.
* Dailyfor my daily notes, all namedYYYY-MM-DD.md. I do not write anything in daily notes, they exist solely to be linked to from other entries.
* Templatesfor templates.

Two folders are present in the downloadable version of my vault for the sake of clarity. In my personal vault, these notes would be in the root, not a folder.

* Categoriescontains top-level overviews of notes per category (e.g. Books, Movies, Podcasts, etc).
* Notescontains example notes.

## Links

I use internal links profusely throughout my notes. I try to always link the first mention of something. My journal entries are often a stream of consciousness cataloging recent events, finding connections between things. Often the link isunresolved, meaning that the note for that link isn’t created yet. Unresolved links are important because they are breadcrumbs for future connections between things.

A journal entry in therootof my vault might look something like this:

I went to see the movie [[Perfect Days]] with [[Aisha]] at [[Vidiots]] and had Filipino food at [[Little Ongpin]]. I loved this quote from Perfect Days: [[Next time is next time, now is now]]. It reminds me of the essay ...

The movie, movie theater, and restaurant each link to entries in myReferencesfolder. In these reference notes I capture properties, my rating, and thoughts about that thing. I useWeb Clipperto help populate properties from databases like IMDB. The quote was meaningful to me, so it became anevergreen notein my root folder. The essay I mention is in myClippingsfolder, because I didn’t write it myself.

This heavy linking style becomes more useful as time goes on, because I can trace how ideas emerged, and the branching paths these ideas created.

## Fractal journaling and random revisit

Fractal journaling and randomization are how I tame the wilderness that a knowledge base can grow into.

Throughout the day I use Obsidian’sunique notehotkey to write individual thoughts as they come up. This shortcut automatically creates a note with the prefixYYYY-MM-DD HHmmto which I may add a title that describes the idea.

Every few days I review these journal fragments and compile the salient thoughts. I then review those reviews monthly, and review the monthly reviews yearly (usingthis template). The result is a fractal web of my life that I can zoom in and out of at varying degrees of detail. I can trace back where individual thoughts came from, and how they bubbled up into bigger themes.

Every few months I set aside time for a “random revisit”. I use therandom notehotkey to quickly travel randomly through my vault. I often use the local graph at shallow depth to see related notes. This helps me revisit old ideas, create missing links, and find inspiration in past thoughts. It’s also an opportunity to do maintenance, like fix formatting based on new rules in my personal style guide.

People have asked me if this could be automated with language models but I do not care to do so. I enjoy this process. Doing this maintenance helps me understand my own patterns.Don’t delegate understanding.

## Properties and templates

Almost every note I create starts from atemplate. I use templates heavily because they allow me to lazily add information that will help me find the note later. I have a template for every category withpropertiesat the top, to capture data such as:

* Dates— created, start, end, published
* People— author, director, artist, cast, host, guests
* Themes— grouping by genre, type, topic, related notes
* Locations— neighborhood, city, coordinates
* Ratings— more on this below

A few rules I follow for properties:

* Property names and values should aim to be reusable across categories. This allows me to find things across categories, e.g.genreis shared across all media types, which means I can see an archive ofSci-fibooks, movies and shows in one place.
* Templates should aim to be composable, e.g.PersonandAuthorare two different templates that can be added to the same note.
* Short property names are faster to type, e.g.startinstead ofstart‑date.
* Default tolisttype properties instead oftextif there is any chance it might contain more than one link or value in the future.

The.obsidian/types.jsonfile lists which properties are assigned to which types (i.e.date,number,text, etc).

## Rating system

Anything with aratinguses an integer from 1 to 7:

* 7 —Perfect, must try, life-changing, go out of your way to seek this out
* 6 —Excellent, worth repeating
* 5 —Good, don’t go out of your way, but enjoyable
* 4 —Passable, works in a pinch
* 3 —Bad, don’t do this if you can
* 2 —Atrocious, actively avoid, repulsive
* 1 —Evil, life-changing in a bad way

Why this scale? I like rating out of 7 better than 4 or 5 because I need more granularity at the top, for the good experiences, and 10 is too granular.

## Publishing to the web

This site is written, edited, and published directly from Obsidian. To do this, I break one of my rules listed above — I have a separate vault for my site. I use astatic site generatorcalledJekyllto automatically compile my notes into a website and convert them from Markdown to HTML.

My publishing flow is easy to use, but a bit technical to set up. This is because I like to have full control over every aspect of my site’s layout. If you don’t need full control you might considerObsidian Publishwhich is more user-friendly, and what I use for myMinimal documentation site.

For this site, I push notes from Obsidian to a GitHub repo using theObsidian Gitplugin. The notes are then automatically compiled usingJekyllwith my web hostNetlify. I also use myPermalink Openerplugin to quickly open notes in the browser so I can compare the draft and live versions.

The color palette isFlexoki, which I created for this site. My Jekyll template is not public, but you can get similar results fromthis templateby Maxime Vaillancourt. There are also many alternatives to Jekyll you can use to compile your site such asQuartz,Astro,Eleventy, andHugo.

## Related writing

* File over app
* Concise explanations accelerate progress
* Evergreen notes turn ideas into objects that you can manipulate
* 40 questions to ask yourself every year
* 40 questions to ask yourself every decade
* How I do my to-dos
