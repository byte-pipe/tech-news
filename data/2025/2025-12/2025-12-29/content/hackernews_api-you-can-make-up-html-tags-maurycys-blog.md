---
title: 'You can make up HTML tags: (Maurycy''s blog)'
url: https://maurycyz.com/misc/make-up-tags/
site_name: hackernews_api
fetched_at: '2025-12-29T19:06:59.709267'
original_url: https://maurycyz.com/misc/make-up-tags/
author: todsacerdoti
date: '2025-12-29'
description: You can make up HTML tags
tags:
- hackernews
- trending
---

# You can make up HTML tags:

Aug 2, 2025

(
Programming
)

Instead of writing HTML like this:

<
div

class
=
cool-thing
>

Hello, World!

</
div
>

… you can write HTML like this:

<
cool-thing
>

Hello, World!

</
cool-thing
>

… and CSS like this:

cool-thing
 {


display
:
block
;


font-weight
:
bold
;


text-align
:
center
;


filter
: drop-shadow(
0

0

0.5
em

#ff0
);


color
:
#ff0
;

}

Hello, World!

For those using RSS, click
here
 to see it in action.

Browsers handle unrecognized tags by treating them as a generic element, with no effect beyond what’s specified in the CSS.
This isn’t just a weird quirk, but isstandardized behavior.
If you include hyphens in the name, you can guarantee that your tag won’t appear in any future versions of HTML.

While you should use descriptive built-in tags if they exist, if it’s a choice between <div> and <span>,
making up your own tag provides better readability then using a bunch of class names.

As an example, if you have a bunch of nested tags:

<
div

class
=
article
>

<
div

class
=
article-header
>

<
div

class
=
article-quote
>

<
div

class
=
quote-body
>

... a bunch more HTML ...

</
div
>

</
div
>

</
div
>

</
div
>

Good luck trying to insert something inside of “article-heading” but after “article-quote” on the first try.
This problem vanishes if you use descriptive tag names — no </div> counting required:

<
main-article
>

<
article-header
>

<
article-quote
>

<
quote-body
>

... a bunch more HTML ...

</
quote-body
>

</
article-quote
>

<!-- here! -->

</
article-header
>

</
main-article
>
