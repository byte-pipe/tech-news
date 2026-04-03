---
title: Infinite Pixels – Eric’s Archived Thoughts
url: https://meyerweb.com/eric/thoughts/2025/08/07/infinite-pixels/
site_name: hackernews
fetched_at: '2025-08-08T04:06:52.694224'
original_url: https://meyerweb.com/eric/thoughts/2025/08/07/infinite-pixels/
author: OuterVale
date: '2025-08-08'
---

I was on one of my rounds of social media trawling, just seeing what was floating through the aether, when I came acrossa toot by Andy Pthat said:

Fun #css trick:width: calc(infinity * 1px);height: calc(infinity * 1px);

…and I immediately thought,This is a perfect outer-limits probe!By which I mean, if I hand a browser values that are effectively infinite by way oftheinfinitykeyword, it will necessarily end up clamping to something finite, thus revealing how far it’s able or willing to go for that property.

The first thing I did was exactly what Andy proposed, with a few extras to zero out box model extras:

div {
	width: calc(infinity * 1px); 
	height: calc(infinity * 1px);
	margin: 0;
	padding: 0; }

<body>
  <div>I’m huge!</div>
</body>

Then I loaded the (fully valid HTML 5) test page in Firefox Nightly, Chrome stable, and Safari stable, all on macOS, and things pretty immediately got weird:

Element Size Results

Browser

Computed value

Layout value

Safari

33,554,428

33,554,428

Chrome

33,554,400

33,554,400

Firefox (Nightly)

19.2 / 17,895,700

19.2 / 8,947,840 †

† height / width

Chrome and Safari both getveryclose to 225-1 (33,554,431), with Safari backing off from that by just 3 pixels, and Chrome by 31.  I can’t even hazard a guess as to why this sort of value would be limited in that way; if there was a period of time where 24-bit values were in vogue, I must have missed it.  I assume this is somehow rooted in the pre-Blink-fork codebase, but who knows. (Seriously, who knows?  I want to talk to you.)

But the faint whiff of oddness there hasnothingon what’s happening in Firefox.  First off, the computed height is19.2px, which is the height of a line of text at default font size and line height.  If I explicitly gave itline-height: 1, the height of the<div>changes to 16px.  All this is despite my assigning a height of infinite pixels!  Which, to be fair, is not really possible to do, but does it make sense to just drop it on the floor rather than clamp to an upper bound?

Even if that can somehow be said to make sense, itonlyhappens with height.  The computed width value is, as indicated, nearly 17.9 million, which is not the content width and is also nowhere close to any power of two.  But the actual layout width, according to the diagram in the Layout tab, is just over 8.9 million pixels; or, put another way, one-half of 17,895,700minus 10.

This frankly makes my brain hurt.  I would truly love to understand the reasons for any of these oddities.  If you know from whence they arise, please, please leave a comment!  The more detail, the better.  I also accept trackbacks from blog posts if you want to get extra-detailed.

For the sake of my aching skullmeats, I almost called a halt there, but I decided to see what happened with font sizes.

div {
	width: calc(infinity * 1px); 
	height: calc(infinity * 1px);
	margin: 0;
	padding: 0;
	font-size: calc(infinity * 1px); }

My skullmeats did not thank me for this, because once again, things got… interesting.

Font Size Results

Browser

Computed value

Layout value

Safari

100,000

100,000

Chrome

10,000

10,000

Firefox (Nightly)

3.40282e38

2,400 / 17,895,700 †

† line height values ofnormal/1

Safari and Chrome have pretty clearly set hard limits, with Safari’s an order of magnitude larger than Chrome’s.  I get it: what are the odds of someone wanting their text to be any larger than, say, a viewport height, let alone ten or 100 times that height?  What intrigues me is the nature of the limits, which are so clearly base-ten numbers that someone typed in at some point, rather than being limited by setting a register size or variable length or something that would have coughed up a power of two.

And speaking of powers of two… ah, Firefox.  Your idiosyncrasy continues.  The computed value is a 32-bitsingle-precision floating-pointnumber.  It doesn’t get used in any of the actual rendering, but that’s what it is.  Instead, the actual font size of the text, as judged by the Box Model diagram on the Layout tab, is… 2,400 pixels.

Except, I can’t say that’s theactualactual font size being used: I suspect the actual value is 2,000 with a line height of 1.2, which is generally whatnormalline heights are in browsers. “So why didn’t you just setline-height: 1to verify that, genius?” I hear you asking.  I did!  And that’s when the layout height of the<div>bloomed to just over 8.9 million pixels, like it probably should have in the previous test!  And all the same stuff happened when I moved the styles from the<div>to the<body>!

I’ve started writing at least three different hypotheses for why this happens, and stopped halfway through each because each hypothesis self-evidently fell apart as I was writing it.  Maybe if I give my whimpering neurons a rest, I could come up with something.  Maybe not.  All I know is, I’d be much happier if someone just explained it to me; bonus points if their name is Clarissa.

Since setting line heights opened the door to madness in font sizing, I thought I’d try settingline-heightto infinite pixels and see what came out.  This time, things were (relatively speaking) more sane.

Line Height Results

Browser

Computed value

Layout value

Safari

33,554,428

33,554,428

Chrome

33,554,400

33,554,400

Firefox (Nightly)

17,895,700

8,947,840

Essentially, the results were the same as what happened with element widths in the first example: Safari and Chrome were very close to 225-1, and Firefox had its thing of a strange computed value and a rendering size notquitehalf the computed value.

I’m sure there’s a fair bit more to investigate about infinite-pixel values, or about infinite values in general, but I’m going to leave this here because my gray matter needs a rest and possibly a pressure washing.  Still, if you have ideas for infinitely fun things to jam into browser engines and see what comes out, let me know.  I’m already wondering what kind of shenanigans, other than inz-index, I can get up to withcalc(-infinity)…


* Infinite Pixelswas published onThursday, August 7th, 2025.
* It was assigned to theBrowsersandCSScategories.
* There have beenfive replies.

### Comments (5)

1. Wonderful article. Thank you for sharing. Had a tl;dr moment today
2. Today I learned why I like Safari over Firefox and Chrome (ew ads); thanks for sharing!
3. Small typo :)“andFirefoxChrome by 31″
4. @femtozer Ah, yep. Fixed!
5. Ah!Memories.There have always been limits :)

Name

E-mail(required but not displayed)

URI(optional)

Meyerweb dot com reserves the right to edit or remove any comment, especially when abusive or irrelevant to the topic at hand.

HTMLallowed:<a href="" title=""> <abbr title=""> <acronym title=""> <b> <blockquote cite=""> <cite> <code> <em> <i> <q cite=""> <s> <strong> <pre class=""> <kbd>

Your Comment
(
Markdown
 supported)

if you’re satisfied with it.

#### Comment Preview

Δ
