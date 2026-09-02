---
title: Fine, I’ll build my own text editor! – David Bushell – Web Dev (UK)
url: https://dbushell.com/2026/09/01/text-editor/
site_name: hackernews_api
content_file: hackernews_api-fine-ill-build-my-own-text-editor-david-bushell-we
fetched_at: '2026-09-02T21:36:07.173704'
original_url: https://dbushell.com/2026/09/01/text-editor/
author: David Bushell
date: '2026-09-01'
description: The one where I build my own text editor (until I get bored).
tags:
- hackernews
- trending
---

# Fine, I’ll build my own text editor!

Tuesday

1Sept2026Play Synthesised Audio

“They don’t make ’em like Sublime Text anymore”resonated with a lot of folk. Software these days is garbage. That got me thinking; I’m good at building garbage!

Why can’t I build my own text editor?

VS Code is built uponMonaco Editorwhich is a<div>soup hellscape. I was late to the VS Code train because for years my Intel inside™ Mac was too slow. That issue was resolved when I bought Apple silicon. If that’s the standard I have a lot of room to make mistakes.

## Canvas

My first experiment renders everything on a<canvas>element.

 
 
 
 
 
 
 
 

You can’t tell, but your CPU is doing a lot of work to render that picture at 60–120 frames per second. Lack of interactivity is an obvious problem for a text editor.

I made a list of the “minimum viable” features and implemented them.

* Pointer down to position text cursor
* Arrow keys to move text cursor
* Highlight current line
* Type to enter text
* Fancy cursor animation

This next demo is interactive, click around and type.

 
 
 
 
 
 
 
 
 

Before you @ me about Vim bindings: shut up, I’ve got more pressing issues. Canvas gives me nothing for free. Amongst many desirable features, I’m missing:

* Text selection
* Undo/redo history
* Multi-line paste
* Overflow scrolling

That last one is critical. Life is too short to implement custom elastic scrollbars. I decided to cheat and use native browser overflow on a hidden element. A<div>is sized to match the canvas text and the scroll position is used to calculate render offsets on thecanvas.

 
 
 
 
 
 
 
 
 
 

I’m pleased with how that’s coming along but I’m also disheartened because<canvas>is entirely inaccessible. I could continue to add text selection and other features but I’m not solving the fundamental accessibility issue.

I had a better idea.

## Content editable

Instead of rendering text on the<canvas>I can just render it natively in the overflow<div>and make it editable with acontenteditableattribute. That attribute has aplaintext-onlyvalue that is perfect for code. All content remains within a single text node.

<
div

 
 
contenteditable
=
"
plaintext-only
"

 
 
autocapitalize
=
"
off
"

 
 
autocorrect
=
"
off
"

 
 
spellcheck
=
"
false
"

 
 
translate
=
"
no
"
>

 
 
<!--
 
text
 
goes
 
here
 
-->

</
div
>
Copy Code

Attributes likespellcheckmust be disabled to avoid input latency spikes. Want to guess how many days it took me to discover that fix?Days!

Usingcontenteditablegives native text selection and undo history etc. So much accessibility goodness is wired up for free by the browser.

 
 
 
 
 
 
 
 
 

TheSelection APIprovides metrics I use to continue rendering a custom text cursor.::selectionis available so I can style that too. I’ve set the nativecaret-colorinvisible, which is probably a no-no.

Thecontenteditabletechnique is promising but I’ve noticed strange performance issues beyond a certain character count. Chromium browsers perform worse than WebKit and whatever Firefox is now but it’s unpredictable.

## Textarea

Instead of plaintextcontenteditablewould a simple<textarea>be viable? In short: yes. Turns out a<textarea>is far more performant for longer text.

In this final demo I’ve added syntax highlighting too.

 
 
 
 
 
 
 
 
 
 

My original plan was to usecustom::highlighton thecontenteditableelement.<textarea>can’t use CSS highlights so a third layer was required. For demo purposes I added some<div>soup for the visible lines to applyMicroLighter.

Edit:I’m told the newOpaqueRange APIunlocks custom highlights for<textarea>— neat!

Edit 2:and theEditContext APIimproves<canvas>input.

Too many CSS highlights are another performance bottleneck. A more robust solution would be to useTree-sitterto generate a syntax tree and walk that to generate highlights for only visible lines. I was hoping to avoid virtualised scrolling entirely but I could improve it using theinverse sticky technique. Or I can go back tocontenteditablebecause the file sizes I’d be editing don’t hit the performance wall.

Anyway, looking good, right?

Looks like 90% of a text editor with 1% of the features. From here it’s pretty straight forward todraw the rest of the owl. I’m tempted to keep drawing but then I think about all the little things like tab indentation. Right now I just hijack the tab key to insert two spaces…

My demos above are unoptimised and far from perfectly accessible but at least I’m not starting from a losing position. Rendering on<canvas>would be a nightmare.

I’m filing this project away for a rainy day.

JavaScript strings and text ranges work with UTF-16 code units. It’s easy to naively introduce bugs. I’m sure my demos are full of them. I’ll leave with a code example to nerd snipe.

"
🍋‍🟩
"
.length;
 
//
 
5

[
...
"
🍋‍🟩
"
].length;
 
//
 
3

const
 
segmenter
 
=
 
new
 
Intl.
Segmenter
(
"
en
"
,
 
{granularity
:
 
"
grapheme
"
});

[
...
segmenter.
segment
(
"
🍋‍🟩
"
)].length;
 
//
 
1
Copy Code