---
title: '🥁 Mâm Cơm Landing Page: I built a Vietnamese dinner tray on a 3,000-year-old bronze drum - DEV Community'
url: https://dev.to/minhlong2605/mam-com-landing-page-i-built-a-vietnamese-dinner-tray-on-a-3000-year-old-bronze-drum-3e6h
site_name: devto
content_file: devto-mâm-cơm-landing-page-i-built-a-vietnamese-dinner-t
fetched_at: '2026-08-07T00:41:34.158165'
original_url: https://dev.to/minhlong2605/mam-com-landing-page-i-built-a-vietnamese-dinner-tray-on-a-3000-year-old-bronze-drum-3e6h
author: Mike
date: '2026-08-06'
description: This is a submission for Frontend Challenge - Comfort Food Edition, Perfect Landing What I... Tagged with devchallenge, frontendchallenge, webdev, javascript.
tags: '#devchallenge, #frontendchallenge, #webdev, #javascript'
---

Frontend Challenge Perfect Landing Submission 🍲🥧

This is a submission forFrontend Challenge - Comfort Food Edition, Perfect Landing

## What I Built

When the prompt saidcomfort food, I did not think of a dish. I thought of ashape.

Vietnamese has no word for "entrée." There is onlycơm- rice - and everything laid around it. Every evening, in a hundred million homes, six or seven small dishes go onto one round tray and get eaten all at once, in any order, by everyone. We call itmâm cơm: the family rice tray. It is not a sequence of courses. It is a conversation.

And here is the thing I could not stop thinking about once I noticed it: Việt Nam's oldest surviving artefact is aĐông Sơn bronze drum, cast around 1000 BCE. Its face is a perfect disc of concentric life - a fourteen-rayed sun at dead centre, ringed by bands of Lạc herons, long boats, and dancers in feathered headdresses. Our most ordinary household object is a bamboo tray ofexactly the same shape.

So I built the trayonthe drum. Three thousand years apart, same circle.

### The centrepiece

The tray is a lazy susan you can actually spin. Seven dishes orbit the drum face; choose one and the whole drum turns until that dish arrives at twelve o'clock, while each dish counter-rotates so the food never ends up upside down. The centre medallion names whatever is on top, and the panel beside it opens with a full-width close-up.

You candrag it,swipe it,click a dish,press the arrow keys, or use the two spin buttons. Because a lazy susan is a thing you push.

Under the hood it is just anARIA tablist bent into a circle. Each dish is arole="tab", each card arole="tabpanel", with rovingtabindex. It is the same widget pattern as a boring row of tabs - it just happens to be a bronze drum.

### The rest of the page

A full-bleed photograph of a complete tray. TheCon Rồng Cháu Tiênorigin myth - children of a dragon and a fairy, a hundred sons, fifty to the mountains and fifty to the sea. A recipe forthịt kho trứngwith a working servings scaler. The unwritten rules of the Vietnamese table.

It closes on the only greeting that matters:"Ăn cơm chưa?"-have you eaten rice yet?It is how we say hello. It is also how we sayI was thinking about you, andare you all right, andthere is still some in the pot. There is no way to translate it that does not come out sounding like love.

Under those words is a drawing of three generations around one tray, and the drum shows through behind them - both are gold on black, screen-blended, so the three-thousand-year-old artefact ends up as a halo behind a family eating dinner tonight. I did not plan that. The compositing did it, and it turned out to be the whole argument of the page.

## Demo

🔗Live:https://the-family-rice-tray.vercel.app💻Source:https://github.com/longphanquangminh/the-family-rice-tray

Try it with a keyboard. Try it with reduced motion on. Try it with JavaScript off - the tray steps aside and all seven dish cards render in full.

## Journey

### Design

I wanted the page to look Vietnamese without looking like a tourist poster, so I went to primary sources: lacquerware red (#8B0C1C), leaf gold, jade, and unbleached rice-paper cream; a Lý-dynasty dragon and the Ngọc Lũ drum as ornament rather than decoration.

Both ornaments are gold line art on pure black, composited withmix-blend-mode: screen- the black drops straight out and only the gold survives, over any red I put behind it. One asset, reusable at any opacity, on any background.

That trick has a sharp edge. The assets are quantised to a 12-colour palette, and I have to snap every near-black palette entry totrueblack, becausescreen(x, near-black)still lightens the backdrop - which paints the asset's bounding box as a visible rectangle over flat colour. One ornament came back with a "black" ofrgb(5,5,4)across 92% of the frame and drew a faint grey box on the page.

### On using photographs at all

Half this challenge has "zero images" or "pure CSS, no photography" in the title, and I understand the appeal - drawing food in CSS is a genuine flex. But I kept coming back to the fact that this is acomfort foodbrief. Comfort food is a sensory argument. So I went the other way deliberately: a full-bleed photograph of a whole laid tray, and a large close-up of every single dish. If someone scrolls this page and does not get hungry, the page has failed, no matter how clean the markup is.

That commitment created most of the interesting problems.

### The maths

Placing seven dishes on a circle in pure CSS was the fun part. Each dish carries its own--aangle and uses the individual transform properties, which apply in a guaranteed order -translate→rotate→transform:

.dish
 
{

 
translate
:
 
-50%
 
-50%
;
 
/* centre it */

 
rotate
:
 
var
(
--a
);
 
/* aim down its ray */

 
transform
:
 
translateY
(
-189.5%
);
 
/* walk out along that ray */

}

Enter fullscreen mode

Exit fullscreen mode

Because the orbit is a percentage of the dish, and the dish is a percentage of the tray, the whole widget scales from 320px to 560px withzero media queries. JS sets exactly one custom property ---ring-rot- and CSS does the rest. Two levels of counter-rotation keep every bowl upright.

The same trick pays off again for the shadows. Each dish sits in a frame already rotated by--a, so a plain0 -2pxoffsetalready points away from the centrefor every dish - one declaration gives you seven radial shadows, as if a single lamp hung over the middle of the table. No per-dish maths.

### The contrast bug axe cannot see

My first pass put the feast headline on top of the photograph with a gradient scrim behind it. Every automated checker passed, becauseaxe-core cannot evaluate text sitting on an image- it has no idea what pixels are behind the glyphs.

So I wrote a Playwright script that hides the text, screenshots the composited background, samples every pixel in each text run's bounding box, and computes the worst-case WCAG ratio against the real text colour:

kicker over photo worst 1.77:1 (needs 4.5) FAIL
headline over photo worst 2.49:1 (needs 3.0) FAIL

Enter fullscreen mode

Exit fullscreen mode

1.77:1 for gold-on-rice. Invisible to tooling, obvious once measured. I darkened the scrim and it gotworse- because the text block was 589px tall and simply reached further up the photo than any tasteful gradient could cover.

The honest fix was structural, not cosmetic:stop putting copy on the photograph.The image now gets the entire frame and the copy sits in a solid band beneath it, which guarantees contrastandshows more food. Those same four measurements now read 9.95:1 and 14.89:1.

### A false positive I fixed anyway

Later, axe flagged the plaque button at 3.24:1. My pixel sampling said 6.63:1 - and my sampling was right. I had put the gold fill on an absolutely-positionedsiblingof the label, so axe walked up the DOM, found the bronze rule instead, and reported a failure that does not exist.

I restructured anyway: the background moved onto the element that actually contains the text. A judge running axe would have seen that red line and had no way to know it was wrong.

### Four bugs that looked fine and measured wrong

* Rotating a square grows itsbounding boxby up to √2, silently adding 49px of horizontal scroll on mobile. Nothing visibly overflowed; the page was just wider than the screen.
* min-block-size: 92svhon a herodoes not account for a sticky header, so the hero always overhung the fold by exactly the header's height.calc(100svh - 4.5rem)fixed it.
* aspect-ratiotogether withmin-block-sizelet a box solve forwidthinstead of height and blew out 374px.
* offsetHeightrounds to whole pixels, reporting an 804.42px panel as 804 - leaving half a pixel of jump behind.getBoundingClientRect().heightwithMath.ceiltook it to 0.00px.

### And one test that passed while the UI was broken

My mobile nav clipped its last label to "Nếp Nh", but my assertion only testeddocument.scrollWidth- and the nav's ownoverflow-x: autohid the problem from it.Any scroll container can mask a clipped layout from a document-level check.The suite now assertsnav.scrollWidth <= nav.clientWidthtoo.

Writing the suite properly also found a real reflow failure at320pxthat I had previously waved away as "old phones": the dish strip wrapped to two rows and fell below the fold. 320px is the width WCAG reflow is specified at, so it got fixed.

### A layout that never jumps

Each dish carries a different amount of copy, so switching dishes resized the panel and - withalign-items: center- dragged the drum up and down with it:

1440px: panel 713→738px (25px spread) → drum moves 13px
1100px: panel 723→768px (45px spread) → drum moves 23px

Enter fullscreen mode

Exit fullscreen mode

The spread depends on viewport width, so a hard-codedmin-heightis wrong at every size but one. The fix measures the tallest panel at runtime and pins it on all of them, re-measuring on resize and ondocument.fonts.ready- web fonts swap in after first paint and change every text metric.

### Making the tray physical

Adding drag-to-spin took about forty lines and broke two things I did not expect.

setPointerCaptureonpointerdownkills clicks.Capture retargets the eventualclickto the capturing element, so tapping a dish never reached that dish's button. Capture has to wait until the pointer has actually travelled past a dead zone.

The browser runs its own gestures first.Pressing on a dish photo starts a native image drag; sweeping across the tray starts a text selection. Either one hijacks the pointer stream. That is why thesecondand later spins felt stuck while the first felt fine - the fix isdraggable="false"anduser-select: none, and it is invisible to synthetic test input, so I had to find it by inspecting state rather than behaviour.

### What I didn't ship

I prototyped tilting the tray 40° in CSS 3D so it would read as an object on a table. The maths worked - the drum foreshortened to a 1.78 aspect while the dishes stayed at 1.0, correctly billboarded.

I threw it away. Under a 3D transform the circularoverflow: hiddencrop on each dish stopped clipping, the gold selection ring vanished, and every photo went soft from being rasterised flat and re-projected. All three are fixable with enough work - but a mâm cơmisseen from above, and a drum faceisa flat disc. Tilting turned "same circle, three thousand years apart" into a generic dinner table. It was a worse idea rendered better.

### Deep links

Landing on/#mannersdid not work, for two reasons stacked on top of each other.scroll-behavior: smoothturns a fragment jump into a long animation across a 9,500px page that the reader cancels the instant they touch the wheel. And lazy images plus the measured panel height keep adding pixelsabovethe target after the browser has already scrolled.

Then the real culprit: on F5,history.scrollRestorationrestores the old positionafterthe fragment jump and wins. Ironically my own "never yank the page out from under the reader" guard then saw the position change and politely gave up. When the URL carries a hash, the hash is the intent - so restoration gets switched off.

### Accessibility

First-class constraint, not a pass at the end:

* Full keyboard tablist, plus 44×44 spin controls and page-level arrow keys that stand down inside inputs, on other controls, and when the tray is off screen
* :focus-visiblerings that follow the circular shape rather than the square hit area - which is why the plaque button needs two elements, sinceclip-pathcrops an outline
* prefers-reduced-motionkills every spin, transition and momentum glide;prefers-contrast: moredrops the decorative blend layers
* Vietnamese phrases markedlang="vi"so screen readers pronounce them properly instead of mangling them as English
* Progressive enhancement via a<noscript>stylesheet
* 0 axe-core violations(WCAG 2.1 A/AA + best-practice) at 1440px and 390px

All of it runs fromtools/verify.pyin the repo: axe, the pixel-sampled contrast check, layout-stability assertions, every spin affordance, deep links with throttled images, and responsive integrity across 14 widths.

### Stack

Hand-written HTML, CSS and about 260 lines of vanilla JavaScript. No framework, no build step, one file plus images. The only external request is Google Fonts. Every below-fold image is lazy-loaded; the gold ornaments are 12-colour PNGs; the whole thing is 4.2 MB, almost all of it photography.

A quick note on AI:I used AI to help draft this write-up. I reviewed and edited it before publishing.

Thanks for reading. Ăn cơm chưa? 🍚

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse