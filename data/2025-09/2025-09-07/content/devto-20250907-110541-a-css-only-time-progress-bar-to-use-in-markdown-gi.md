---
title: A CSS only time progress bar to use in markdown / GitHub Pages - DEV Community
url: https://dev.to/codepo8/a-css-only-time-progress-bar-to-use-in-markdown-github-pages-465f
site_name: devto
fetched_at: '2025-09-07T11:05:41.162708'
original_url: https://dev.to/codepo8/a-css-only-time-progress-bar-to-use-in-markdown-github-pages-465f
author: Christian Heilmann
date: '2025-09-05'
description: A way to display time inside markdown files published as HTML pages on github. Tagged with css, markdown, githubpages.
tags: '#css, #markdown, #githubpages'
---

For our weeklyWeAreDevelopers Live ShowI wanted to have a way to include a time progress bar into thepage we show. The problem there was that these are markdown files using GitHub Pages and whilst I do use some scripting in them, I wanted to make sure that I could have this functionality in pure CSS so that it can be used on GitHub without having to create an html template. And here we are.

You can check out thedemo page to see the effect in actionwith the liquid source code or play with the few lines of CSS inthis codepen. Fork this repo to use it in your pages or just copy the_includesfolder.

## Using the CSS time progress bar

You can use as many bars as you want to in a single page. The syntax to include a bar is the following:

{​% include cssbar.html duration="2s" id="guesttopic" styleblock="yes" %​}

Enter fullscreen mode

Exit fullscreen mode

* Thedurationvariable defines how long the progress should take
* Theidvariable is necessary to and has to be unique to make the functionality work
* If thestyleblockis set, the include will add astylewith the necessarycss rulesso you don't have to add them to the main site styles. You only need to do that in one of the includes.

## Using the bar in HTML documents

You can of course also use the bar in pure HTML documents, as shown inthe codepen. The syntax is:

<div

class=
"progressbar"

style=
"--duration: 2s;"
>


<input

type=
"checkbox"

id=
"progress"
>


<label

for=
"progress"
>
start
</label>

</div>

Enter fullscreen mode

Exit fullscreen mode

Don't forget to set a unique id both in the checkbox and the label and define the duration in the inline style.

## Drawbacks

* This is a bit of a hack as it is not accessible to non-visual users and abuses checkboxes to keep it CSS only. It is keyboard accessible though.
* In a better world, I'd have used an HTMLprogresselement and styled that one…

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
