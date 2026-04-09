---
title: 'Show HN: OverType – A Markdown WYSIWYG editor that''s just a textarea | Hacker News'
url: https://news.ycombinator.com/item?id=44932651
site_name: hackernews
fetched_at: '2025-08-18T22:01:45.889620'
original_url: https://news.ycombinator.com/item?id=44932651
author: panphora
date: '2025-08-18'
---

Hacker News
new
 |
past
 |
comments
 |
ask
 |
show
 |
jobs
 |
submit
login
Show HN: OverType – A Markdown WYSIWYG editor that's just a textarea
368 points
 by
panphora

17 hours ago

 |
hide
 |
past
 |
favorite
 |
88 comments
Hi HN! I got so frustrated with modern WYSIWYG editors that I started to play around with building my own.

The problem I had was simple: I wanted a low-tech way to type styled text, but I didn't want to load a complex 500KB library, especially if I was going to initialize it dozens of times on the same page.Markdown in a plain <textarea> was the best alternative to a full WYSIWYG, but its main drawback is how ugly it looks without any formatting. I can handle it, but my clients certainly can't.I went down the ContentEditable rabbit hole for a few years, but always came to realize others had solved it better than I ever could.I kept coming back to this problem: why can't I have a simple, performant, beautiful markdown editor? The best solution I ever saw was Ghost's split-screen editor: markdown on the left, preview on the right, with synchronized scrolling.Then, about a year ago, an idea popped into my head: what if we layered a preview pane behind a <textarea>? If we aligned them perfectly, then even though you were only editing plain text, it would look and feel like you were editing rich text!Of course, there would be downsides: you'd have to use a monospace font, all content would have to have the same font size, and all the markdown markup would have to be displayed in the final preview.But those were tradeoffs I could live with.Anyways, version 1 didn't go so well... it turns out it's harder to keep a textarea and a rendered preview in alignment than I thought. Here's what I discovered:- Lists were hard to align - bullet points threw off character alignment. Solved with HTML entities (• for bullets) that maintain monospace width- Not all monospace fonts are truly monospace - bold and italic text can have different widths even in "monospace" fonts, breaking the perfect overlay- Embedding was a nightmare - any inherited CSS from parent pages (margin, padding, line-height) would shift alignment. Even a 1px shift completely broke the illusionThe solution was obsessive normalization:// The entire trick: a transparent textarea over a preview div
 layerElements(textarea, preview)
 applyIdenticalSpacing(textarea, preview)

 // Make textarea invisible but keep the cursor
 textarea.style.background = 'transparent'
 textarea.style.color = 'transparent'
 textarea.style.caretColor = 'black'

 // Keep them in sync
 textarea.addEventListener('input', () => {
 preview.innerHTML = parseMarkdown(textarea.value)
 syncScroll(textarea, preview)
 })A week ago I started playing with version 2 and discovered GitHub's <markdown-toolbar> element, which handles markdown formatting in a plain <textarea> really well.That experiment turned into OverType (https://overtype.dev), which I'm showing to you today -- it's a rich markdown editor that's really just a <textarea>. The key insight was that once you solve the alignment challenges, you get everything native textareas provide for free: undo/redo, mobile keyboard, accessibility, and native performance.So far it works surprisingly well across browsers and mobile. I get performant rich text editing in one small package (45KB total). It's kind of a dumb idea, but it works! I'm planning to use it in all my projects and I'd like to keep it simple and minimal.I would love it if you would kick the tires and let me know what you think of it. Happy editing!---Demo & docs:https://overtype.devGitHub:https://github.com/panphora/overtype

pedrovhb

13 hours ago

 |
next

[–]

Nice! Seems very useful if you can drop in and have everything work.

Nitpicking a bit: it's not as much _rendering_ markdown as it's _syntax highlighting_ it. Another interesting approach there could be to use the CSS Custom Highlight API [0]. Then it wouldn't need the preview div, and perhaps it'd even be possible to have non-mono fonts and varying size text for headers.[0]https://developer.mozilla.org/en-US/docs/Web/API/CSS_Custom_...

reply

pspeter3

9 hours ago

 |
parent
 |
next

[–]

Can you use highlights on text area contents?

reply

lifthrasiir

4 hours ago

 |
root
 |
parent
 |
next

[–]

You can't mainly because <textarea> separately tracks its own selection, AFAIK.

reply

scottfr

1 hour ago

 |
root
 |
parent
 |
next

[–]

There is a proposal to add support for this:

https://github.com/MicrosoftEdge/MSEdgeExplainers/blob/main/...

reply

jagged-chisel

11 hours ago

 |
parent
 |
prev
 |
next

[–]

The animated exploded demo definitely shows formatting differently from plain text (bold is bold, hyphens replaced with bullets.)

reply

franga2000

4 hours ago

 |
root
 |
parent
 |
next

[–]

Fair, but so do many syntax highlighters (at least bold, italic, titles...).

reply

4b11b4

11 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Ya that's true

reply

vmurthy

9 hours ago

 |
prev
 |
next

[–]

Went down the rabbit hole which is the overtype.dev website (nice work btw!) and found and even nicer rabbit hole -
https://hyperclay.com/
 Single HTML apps :). Enjoy!

reply

pavlov

6 hours ago

 |
parent
 |
next

[–]

This is coming close to WWW's original vision because the very first web browser was also an editor. Tim Berners-Lee's application on the NeXT was basically a wrapper for the operating system's built-in rich text editing class named TextView. (It later became NSTextView on Apple's Mac OS X and still powers the TextEdit app on Mac.)

We lost editing for two reasons:1) The HTTP PUT method didn't exist yet, so edited HTML files could only be saved locally.2) Mosaic built a cross-platform web browser that defined what the WWW was for 99% of users, and they didn't include editing because that would have been too complex to build from scratch in their multi-platform code base.

reply

dcreater

8 hours ago

 |
parent
 |
prev
 |
next

[–]

I don't say this often or lightly: my mind is blown.

Why is this not catching fire? Especially in the day of vibe coding this is a far better and far more effective route to app building

reply

runako

8 hours ago

 |
parent
 |
prev
 |
next

[–]

This reminds me of some of the better experiments in mid-aughts Web dev, and is exactly the kind of project that helps push standards & user expectations forward.

reply

dchest

14 hours ago

 |
prev
 |
next

[–]

Looks good!

Some links I've collected in the past that describe this approach:-https://css-tricks.com/creating-an-editable-textarea-that-su...-https://github.com/WebCoder49/code-inputI believehttps://grugnotes.comalso does this for markdown.

reply

kaboomshebang

13 minutes ago

 |
prev
 |
next

[–]

Very cool and useful!! Thanks for OSS this :)

reply

mmastrac

13 hours ago

 |
prev
 |
next

[–]

This is pretty nice, though I'd suggest you call it a transparent syntax highlighter.

Forhttps://grack.com/demos/adventure/, I used a hidden <input text> for something similar. I wanted to take advantage of paste/selection and all the other goodies of text, but with fully-integrated styling.Like you, I found that standard text input boxes were far more interesting than contentEditable because they're just so simple overall.I think there's probably an interesting middle ground here where you render real markdown with the textarea effectively fully hidden (but still with focus), emulate the selection events of the rendered markup into the textarea, and basically get a beautiful editor with all the textarea solidness.

reply

rockwotj

8 hours ago

 |
parent
 |
next

[–]

Fun fact: this is how github adds syntax highlighting in its search bar. A while back I built the same syntax highlighting in Shortwave (an email client) using the same “view on top of a transparent input” trick. Pair it all with the following blog, for a top notch search UX

https://blog.superhuman.com/delightful-search-more-than-meet...

reply

phonon

11 hours ago

 |
prev
 |
next

[–]

912 bytes....

https://sylvainpolletvillard.github.io/spell/demo.html

reply

Imustaskforhelp

5 hours ago

 |
parent
 |
next

[–]

what is this tom foolery. I am so amazed by it, this also seems to be a WYSIWYG but though it doesn't support markdown exactly per se but it has way more features than overtype (no offense to overtype which is also a really really cool project)

My mind is utterly blown with what you can do with 912 bytes.I imagine that I can create a really simple blog post that can load under 14 kb so that it can be sent in a (single request?) while still having comment feature with this one while also being super fast..So good that words can't explain lol

reply

WA

5 hours ago

 |
root
 |
parent
 |
next

[–]

It uses queryCommandState(), which is a deprecated browser feature [1]. It's quite common in many simpler WYSIWYG editors. Thing is, it might be so widespread that some people claim that it will never be truly deprecated.

OverType doesn't use this and the result is that you gotta build all the features in JS.[1]:https://developer.mozilla.org/en-US/docs/Web/API/Document/qu...

reply

janwilmake

16 hours ago

 |
prev
 |
next

[–]

Really cool! I just love the simplicity of it: has no drawbacks compared to regular textarea, but has lots of benefits. you basically improved textarea, by a lot!

I also made a similar thing a while ago called contextarea.com, maybe, I should add overtype!

reply

ikurei

14 hours ago

 |
parent
 |
next

[–]

Having to use a monospaced font is a pretty big drawback. To me, it means I wouldn't use this for a product that wasn't intended for a techie programmer audience.

Not that it isn't a really cool project! I'm only saying it has clear drawbacks.

reply

splitbrain

2 hours ago

 |
prev
 |
next

[–]

> Embedding was a nightmare - any inherited CSS from parent pages (margin, padding, line-height) would shift alignment.

This seems to be the perfect use case for a web component and its shadow DOM. Instead of using a div.editor, this component could wrap around a textarea and it would progressively enhance the textarea experience.

reply

garbageoverflow

15 hours ago

 |
prev
 |
next

[–]

If it were a WYSIWYG editor, there'd be previews for images. But it seems like it's just syntax highlighting for textareas. Nice project either way, but false advertising.

reply

ricardobeat

2 hours ago

 |
parent
 |
next

[–]

Indeed it is a misuse of the term. An actual WYSIWYG editor would not show any of the formatting markers.

By definition a “Markdown editor” cannot be WYSIWYG - you can have a WYSIWYG editor that is powered by markdown underneath though, which this is not.

reply

calmworm

12 hours ago

 |
parent
 |
prev
 |
next

[–]

I didn’t see an option for images. Am I missing something?

reply

macintux

12 hours ago

 |
root
 |
parent
 |
next

[–]

I assume that was the point. The parent commenter feels "WYSIWYG" by definition includes images.

reply

WA

5 hours ago

 |
parent
 |
prev
 |
next

[–]

I can type text, mark it, click "B" for bold and it works. This is WYSIWYG minus images.

reply

clippyplz

7 minutes ago

 |
root
 |
parent
 |
next

[–]

WYSIWYG does not refer to the icons in the toolbar, but rather the text itself. This is not WYSIWYG because when I make something bold, I see a bunch of asterisks around it.

Still a cool project, but someone who does not understand markdown would wonder why pressing the heading button makes my text into a hashtag instead of making it bigger.

reply

reactordev

13 hours ago

 |
prev
 |
next

[–]

This is actually really clever. Just don’t let it balloon out to be a 500kb full fledged WYSIWYG editor, just keep it simple like you do.

reply

rendaw

9 hours ago

 |
prev
 |
next

[–]

I made something similar!
https://github.com/andrewbaxter/malarkdowney
 - The main difference (I think) is that mine applies h* style changes and isn't visually separated from the rest of the page. I.e. it's not just syntax highlighting, it's a more fully-blown output preview.

The text overlay approach doesn't work if you want width-affecting/height style changes (I assume) since that'd cause the overlay to stop matching. The downside is contenteditable cursor movement is broken for inexplicable reasons.

reply

gethly

4 hours ago

 |
prev
 |
next

[–]

Syntax highlighting for markdown input is a good idea. I too have a markdown input and i have two modes for render - either the github style where you manually toggle between editing and rendering or i have two columns with editing on one side and live render on the other.

I too was close to making my own wysiwyg, trello for example has a md wysiwyg, so i knew it was doable with contenteditabe. But after talking with the dev community I was constantly warned by people who took the path before to not do it. So in the end i did not as i did not want to invest more time than i wanted to commit to the project.Good for you, that you did and you made it to the finish line.

reply

bloppe

11 hours ago

 |
prev
 |
next

[–]

This isn't really WYSIWYG because it keeps the formatting symbols like * or # etc.

reply

lifthrasiir

10 hours ago

 |
parent
 |
next

[–]

Still, what you see is what you get (plus some formatting symbols). It's marginally WYSIWYG.

reply

Jonovono

15 hours ago

 |
prev
 |
next

[–]

Nice, I was playing around with Milkdown. it's pretty cool:
https://milkdown.dev/playground
. It's like a block editor like notion for markdown so you don't need the split pane markdown/preview either

reply

mosselman

15 hours ago

 |
prev
 |
next

[–]

Very cool! So simple, I love it.

One thing that would be great is a bit better support for lists (todos, unordered and ordered) where when you press enter once it will add another `-` or `- [ ]`, etc item and when you press it a second time it becomes a blank line.

reply

nbbaier

8 hours ago

 |
prev
 |
next

[–]

Isn't this just syntax highlighting and not wysiwyg?

reply

zoom6628

4 hours ago

 |
prev
 |
next

[–]

This is great. I was a huge fan of typora for writing docs a few an ago and now do all in obsidian. In both the editing is plaintext but the visible text is rendered inline with formatting.

Love what you have done and will use in a project next week.Especially applaud your avoidance of npm, dependencies, and the usual ubiquitous JavaScript deluge.

reply

tomsmeding

14 hours ago

 |
prev
 |
next

[–]

In Firefox on Android, the bold font is wider than the upright and italic fonts, breaking alignment.

(It works fine in Chrome on the same Android phone. Android 16, Firefox 141.0.3)

reply

lifthrasiir

10 hours ago

 |
parent
 |
next

[–]

In fact, depending on font-synthesis [1] and the exact choice of fonts (even when they are monospaced), the alignment can be easily off. That's why this approach only works to some extent and not universal. One possible remedy is to wrap each grapheme into a cell that contains both fonts, where the visible one is bolden and the invisible one affects the advance width. But then you lose ligatures. (Personally I don't like ligatures in coding fonts so it's plus for me, though.)

[1]https://developer.mozilla.org/en-US/docs/Web/CSS/font-synthe...

reply

WA

5 hours ago

 |
prev
 |
next

[–]

Great project! I was looking into this area too for a while. Any reasons you didn't turn this into a web component? Seems like a no-brainer if I can basically use it like `<overtype-textarea>` or something like that.

reply

TeddyDD

3 hours ago

 |
prev
 |
next

[–]

Have you considered wrapping this in web component so it can be used without the div + constructor call ceremony?

reply

SamInTheShell

13 hours ago

 |
prev
 |
next

[–]

This is a nifty little project. If I wasn't already neck deep in blocknote adoption in a small experiment I'm doing, I'd be taking this for a spin.

I noticed on the site the really cool animation you got has a 1px solid border on one of the overlays in firefox. Figure you might care since it's clearly supposed to be flashy.

reply

jona777than

7 hours ago

 |
prev
 |
next

[–]

Love the simplicity. These sort of “less is more” solutions should become more prevalent as average code volume continues to rapidly increase

reply

holler

6 hours ago

 |
prev
 |
next

[–]

Looks nice! I like how simple/clean it is. I spent 3+ months building a contenteditable component from scratch for
https://sqwok.im
, learned a lot and was fun but oh my did it get challenging, especially with cross-browser issues.

reply

ingigauti

16 hours ago

 |
prev
 |
next

[–]

Great idea & solution

I noticed toolbar is missing from options doc, reason I went looking was if I could add my own custom button to the toolbar

reply

aschelch

17 hours ago

 |
prev
 |
next

[–]

Looks awesome. Like the simplicity. I'll keep that in mind for future project ;)

(Btw, there might be a typo on the landing page on the set up part. There is 2 times de <div> instead of the textarea i guess;))Edit: and the link to the Github is brocken

reply

panphora

16 hours ago

 |
parent
 |
next

[–]

The idea is that two instances of overtype would be initialized inside those divs!

reply

Tmpod

13 hours ago

 |
prev
 |
next

[–]

As it is, and without the toolbar, this really reminds me of how this[0] neovim plugin renders Markdown in the terminal. One of its nice features is doing syntax highlighting inside fenced code blocks (through tree-sitter I believe).

[0]:https://github.com/MeanderingProgrammer/render-markdown.nvim

reply

wesz

13 hours ago

 |
prev
 |
next

[–]

I used exactly the same approach years ago working on code editor with js evaluation -
http://labs.onether.com/javascript-sandbox/
 (this is some old version only with whitespace characters, it also had syntax highlighting but i couldn't find it).

Anyway, nice work mate.

reply

rakag

3 hours ago

 |
prev
 |
next

[–]

This is exactly what I need for my project :)

reply

pyromaker

11 hours ago

 |
prev
 |
next

[–]

I also got frustrated with text editors and decided to build something for myself too, so I don't have to repeat the process over and over.

https://www.texteditors.dev

reply

dcreater

3 hours ago

 |
parent
 |
next

[–]

Why do I have to sign up?

reply

jv22222

12 hours ago

 |
prev
 |
next

[–]

Smart! I’ve been working with contenteditable for 3 years. You found a great shortcut!

reply

philo23

14 hours ago

 |
prev
 |
next

[–]

The first time I saw this technique was while trying to figure out how GitHub styled the keyword:value tokens in their search box. It's a very cool technique, and you've done a very nice job of integrating it with a markdown parser!

Only down side to it is that you cant apply any padding to the styled inline elements.

reply

uonr

9 hours ago

 |
prev
 |
next

[–]

https://github.com/inokawa/rich-textarea

reply

indigodaddy

12 hours ago

 |
prev
 |
next

[–]

This is pretty awesome. Now I’m just a dumbo sysadmin with limited webdev/JS skills, so is there a high level way to integrate this into a site so that it could create MD files that could be saved server side?

reply

small_scombrus

12 hours ago

 |
parent
 |
next

[–]

Most JS/TS runtimes have filesystem modules, at it's simplest/least secure you could implement it with client-side fetch and:

On get request - find matching .MD file and returnOn put request - write to given location

reply

Imustaskforhelp

5 hours ago

 |
prev
 |
next

[–]

This is a really good project, kudos!

What I am wondering is if I can modify the project enough so that lets say when I do # test, then it can automatically modify it to be enlarged instead of just colored/ basically i think that this is how reddit comments work..Image support would be really preferred too, but honestly, this is seriously so cool that I can iamgine using this right now, but someone here mentioned spell/pellhttps://github.com/sylvainpolletvillard/spellandhttps://github.com/jaredreich/pelland so they are in the size of 1kb-2kb, even bytes and this is 40kb iirc, so why is there such a big size difference and how are those guys being so small.Once again, amazing project, my mind is truly blown by how simple it is, I will try to integrate this or spell or just anything whenever I can!

reply

victorbjorklund

3 hours ago

 |
prev
 |
next

[–]

This is nice. Just want I wanted.

reply

rafram

9 hours ago

 |
prev
 |
next

[–]

The scroll syncing in the demo doesn’t seem to work well on iOS Safari. I can’t scroll all the way to the bottom.

reply

ForceBru

12 hours ago

 |
prev
 |
next

[–]

I thought it should be extremely portable ("everything just works, it's native"), but it doesn't work on iOS 9.3.6. It doesn't even let me input text into the textarea...

A natural extension seems to be a source code editor with syntax highlighting, like those used inhttps://marimo.io/, Jupyter,https://plutojl.org/and other notebook-like Web editors.

reply

acherion

12 hours ago

 |
parent
 |
next

[–]

I'm not sure why you are testing in iOS 9.3.6. (which was released in 2015), when the documentation says support for Safari is for versions 16 and above.

reply

ForceBru

3 hours ago

 |
root
 |
parent
 |
next

[–]

Well, as I said, I thought this should work everywhere because it's just a textarea, so I didn't read the docs and rushed to test my hypothesis on an old and widely unsupported device

reply

zazaulola

10 hours ago

 |
prev
 |
next

[–]

2kb

https://medv.io/codejar/

reply

skyzouwdev

13 hours ago

 |
prev
 |
next

[–]

This is honestly brilliant. I love how you leaned into the constraints instead of trying to hide them, and the transparent textarea trick is such a clever hack. The fact that you got it down to 45KB while keeping undo/redo, mobile keyboard, and accessibility makes it feel like a breath of fresh air compared to bloated editors. Definitely bookmarking this for my next project.

reply

nm980

16 hours ago

 |
prev
 |
next

[–]

Can you send the GitHub link again?

And how does this handle rendering larger documents?

reply

neilv

13 hours ago

 |
prev
 |
next

[–]

Am I doing it wrong?

The animation shows variable-pitch fonts, but the demo seems to be all the same fixed-pitch font for me. (On Firefox ESR and Chromium.)

reply

drob518

12 hours ago

 |
prev
 |
next

[–]

This is cool (and amazingly simple). Would be even cooler than it already is if it would syntax highlight code in code blocks, too.

reply

ZYbCRq22HbJ2y7

8 hours ago

 |
prev
 |
next

[–]

That is not just a textarea, but it is a pattern seen in many other projects

reply

maz1b

14 hours ago

 |
prev
 |
next

[–]

Nice job. How is this different than marked on npm?

reply

bullen

11 hours ago

 |
prev
 |
next

[–]

Anyone knows a good in browser coding editor widget?

That supports color coding for different languages?

reply

farley13

10 hours ago

 |
parent
 |
next

[–]

Codemirror is pretty decent. Last time I looked for this (6+ years ago) it's what we landed on for an internal tool. Things may have changed tho!

reply

walterlw

13 hours ago

 |
prev
 |
next

[–]

would absolutely love this for a personal note-taking project, but having image support and some sort of auto-completion for commands, lists, tags etc is crucial for something i'd use every day on desktop and mobile.
Still love seeing more options for different purposes.

reply

jackbridger

11 hours ago

 |
prev
 |
next

[–]

12 pages of docs vs it’s a textarea. Great job, gonna try it out.

reply

albert_e

8 hours ago

 |
prev
 |
next

[–]

Minor typo:

> A PEAK UNDER THE HOODI think you meant "PEEK"

reply

cchance

15 hours ago

 |
prev
 |
next

[–]

is there a way to show the rendered preview (not with the markdown characters)

reply

jerpint

14 hours ago

 |
prev
 |
next

[–]

This is great! Gonna try this on my next project

reply

grigio

4 hours ago

 |
prev
 |
next

[–]

what about tables?

reply

octobereleven

16 hours ago

 |
prev
 |
next

[–]

Love this. Pretty much markdown on steroids!

reply

sdairs

13 hours ago

 |
prev
 |
next

[–]

This is really nice

reply

nodesocket

16 hours ago

 |
prev
 |
next

[–]

Very cool. I’m gonna implement into my hobby project today and see how it goes.

reply

breakfastduck

16 hours ago

 |
prev
 |
next

[–]

I really like the simplicity of this.

I have a couple projects I could see this being really useful in, at least as an option instead of pure plain text. I still feel like consumers don't like markdown though, it's frustrating.One thing I noticed, when doing a list (bullet, numbered etc) it would be great if the list continued on barrage return (enter) - most general users would expect that I think.

reply

knoopx

14 hours ago

 |
prev
 |
next

[–]

very nice!

reply

Bengalilol

16 hours ago

 |
prev

[–]

> That's it. No npm. No build. No config.

That's it, I am loving it.

reply

sitkack

14 hours ago

 |
parent

[–]

If it doesn't have an NPM build, it isn't a serious project. Not using anything w/o a build.

reply

neilv

13 hours ago

 |
root
 |
parent
 |
next

[–]

If it doesn't work with crack pipes, it's not a serious pharmaceutical.

reply

vid

13 hours ago

 |
root
 |
parent
 |
prev

[–]

I agree with sitkack. npm (packaged software) is really handle to bundle code and keep a repo up to date. But I guess if you just want a markdown editor on a page, this is fine.

reply

3836293648

12 hours ago

 |
root
 |
parent

[–]

You are arguing two (subtly) different points. Not requiring npm or any build step is great. Always.

Having it available to simplify integration into larger projects is also great.These two things are entirely orthogonal, even if this only does the first one.

reply

vid

8 hours ago

 |
root
 |
parent

[–]

It's fine that the points are different.

If you need to use npm in the rest of the project, which can be helpful for any project that uses front end Javascript, having one library (essentially) that uses a different mechanism is not great.I have built many projects and while I swore at convoluted bundlers in the past, they are pretty nice these days.

reply

Guidelines
 |
FAQ
 |
Lists
 |
API
 |
Security
 |
Legal
 |
Apply to YC
 |
Contact

Search:
