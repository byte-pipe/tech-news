---
title: 'Email obfuscation: What works in 2026?'
url: https://spencermortensen.com/articles/email-obfuscation/
site_name: hackernews_api
content_file: hackernews_api-email-obfuscation-what-works-in-2026
fetched_at: '2026-04-03T01:01:14.957985'
original_url: https://spencermortensen.com/articles/email-obfuscation/
author: jaden
date: '2026-04-02'
description: 'Email obfuscation: What works in 2026?'
tags:
- hackernews
- trending
---

# Email obfuscation: What works in 2026?

Last updated:

January 30, 2026

Here are some of the best techniques for keeping email addresses hidden from spammers—along with the statistics on how likely they are to be broken.

## 1 Plain text

These techniques protect an email address written out in plain text (e.g. “email@example.com”).

Ideally, you should be using multiple techniques in combination, by splitting the email address into segments, where each segment is protected by a different technique.

### 1.1 No protection

Blocked 0% of 318 spammers

aa
@email
.spencer
mortensen
.com

aa@email.spencermortensen.com

### 1.2HTMLEntities

Blocked 95% of 318 spammers

&#97;
&#98;
&#64;
&#101;
&#109;
&#97;
&#105;
&#108;
&#46;
&#115;
&#112;
&#101;
&#110;
&#99;
&#101;
&#114;
&#109;
&#111;
&#114;
&#116;
&#101;
&#110;
&#115;
&#101;
&#110;
&#46;
&#99;
&#111;
&#109;

ab@email.spencermortensen.com

HTML entities are often decoded automatically by server-side libraries, which means that even the most basic harvesters can get your email addresses without any special effort.
This technique should be worthless—and, yet, it still stops most harvesters.

### 1.3HTMLComments

Blocked 98% of 318 spammers

ac
@email
.spencermortensen
<!--
.example
-->
.com

ac@email.spencermortensen
.com

This will stop only the most basic harvesters that struggle with HTML tags.
It offers minimal protection—and, yet, still manages to stop most harvesters (since most harvesters are basic).

### 1.4HTMLSVG

Blocked 100% of 318 spammers

<
object

class
=
"email"

width
=
"130"

height
=
"24"

data
=
"email.svg"

type
=
"image/svg+xml"
></
object
>

<
svg

viewBox
=
"0 0 130 24"

xmlns
=
"http://
www.w3.org
/2000
/svg"
>

<
style
>
@
import

url
(
'https://
fonts
.googleapis
.com
/css2
?family=
Indie
+Flower
&amp;display=
swap'
);

text
 {

dominant-baseline
:
middle
;

fill
:
#000
;

font-family
:
'Indie Flower'
;

font-size
:
16px
;

text-anchor
:
middle
;
}
</
style
>

<
text

x
=
"50%"

y
=
"50%"
>
email
@example
.com
</
text
>

</
svg
>

object
.
email
 {

height
:
2em
;

margin
:
-1em 0
;

vertical-align
:
middle
;
}

Inspiration:rouninmedia.github.io

This hides the email address in an unusual place where most harvesters won’t think to look.
However, the email address is stored there in plain text.

This technique is accessible to all users, including those who depend on a screen reader.
But youmustuse an object element for this to work:
an img element would give you an image that is non-interactive,
and inline SVG would put the email address in the source code where harvesters would find it easily.

The “width” and the “height” attributes help prevent layout shifts while the page is loading.
Because the dimensions depend on the font, the SVG file has to explicitly specify a web font to prevent rendering issues.

### 1.5CSSDisplay none

Blocked 100% of 318 spammers

<
div

class
=
"email"
>
ad
@<
span
>email.</
span
>
spencermortensen.
<
span
>example.</
span
>
com
</
div
>

div
.
email
 >
span
:
nth-child
(
2
) {

display
:
none
;
}

ad@
email.
spencermortensen.
example.
com

Most harvesters are unable to apply style rules, so this is one of the absolute best techniques.
Be sure to vary the decoy tags so the harvester won’t know which parts to omit.

This is fully accessible to everyone, including those who depend on a screen reader.
But youmustuse “display: none” to hide the text:
if you use any visual-only technique (such as shrinking the font size, or repositioning the text off screen), then you’ll break accessibility.

### 1.6JSConcatenation

Blocked 100% of 318 spammers

<
script
>document.write(
'a'
+'i'
+'@'
+'e'
+'m'
+'a'
+'i'
+'l'
+'.'
+'s'
+'p'
+'e'
+'n'
+'c'
+'e'
+'r'
+'m'
+'o'
+'r'
+'t'
+'e'
+'n'
+'s'
+'e'
+'n'
+'.'
+'c'
+'o'
+'m'
);
</
script
>

This is convenient because it has no external dependencies, and yet still manages to block most harvesters.
However, the full email address appears directly in the HTML source code, so this technique cannot be considered safe.

### 1.7JSRot18

Blocked 100% of 318 spammers

<
span

class
=
"email"
>
nw
@rznvy
.fcraprezbegrafra
.pbz
</
span
>

<
head
>
	<
script

src
=
"
text-rot18.js
"

defer
>
</
script
>
</
head
>

nw@rznvy.fcraprezbegrafra.pbz

This technique can be undone by basic harvesters that don’t interpret JavaScript.
At the very least, you should rotate your letters by something other than 13, and rotate your numbers by something other than 5.

### 1.8JSConversion

Blocked 100% of 318 spammers

<
span

id
=
"text-conversion"
>
zibby example com
</
span
>

<
head
>
	<
script

src
=
"
text-conversion.js
"

defer
>
</
script
>
</
head
>

zibby example com

In this technique, the HTML source code contains gibberish, and you write a custom function that converts the gibberish into a working email address.

Most harvesters can only access the HTML source code—and the source code contains nothing of value.
The only practical way to restore the email address is to run your custom conversion function in a web client with DOM and JavaScript support.
This is not possible for most harvesters.

You can write a custom function for each email address, or you can write a single function and apply it to all of the email addresses on the page.

Despite beingfrighteninglysimple, this is expected to be one of the very best techniques.

### 1.9JSAES encryption

Blocked 100% of 318 spammers

<
span

class
=
"email"
>
K
r
e
u
z
2
x
a
6
x
B
8
F
p
j
a
a
0
l
F
g
A
C
N
L
O
6
n
_
A
u
u
1
C
G
j
c
G
8
z
_
E
c
</
span
>

<
head
>
	<
script

src
=
"
text-aes.js
"

defer
>
</
script
>
</
head
>

Kreuz2xa6xB8Fpjaa0lFgACNLO6n_Auu1CGjcG8z_Ec

This technique uses AES 256 to encrypt the email address.
(AES is the only publicly-available cipher approved by the NSA for top secret information.)
The email address cannot be recovered without the JavaScript file—which most harvesters cannot access or run.
This implementation uses the browser’s own built-in cryptography library, so it will not run outside of the browser, even in JavaScript-capable environments.

The cryptography library,SubtleCrypto, is only available insecure contexts(such as over https or on localhost)—which could be a blocker if you’re using http.
You must upgrade to https before you can use this technique!

### 1.10JSUser interaction

Blocked 100% of 318 spammers

<
span

id
=
"text-interaction"
>
whose baby example com
</
span
>

<
head
>
	<
script

src
=
"
text-interaction.js
"

defer
>
</
script
>
</
head
>

whose baby example com

This technique keeps the email address hidden until the user interacts with the page; onlythenis the email address revealed.
This raises the bar for harvesters: they not only need to run a full web client, theyalsoneed to interact with it.

This technique can be used to trigger other techniques.

### 1.11HTMLSymbol substitution

Blocked 97% of 318 spammers

ag AT email DOT spencermortensen DOT com

ag AT email DOT spencermortensen DOT com

This technique is well known, and easily reversible, so it cannot be considered safe.

Breaks usability.This forces the user to undo every substitution before they can send their email.

### 1.12HTMLInstructions

Blocked 100% of 318 spammers

au.fluff@email.spencermortensen.com (remove the “.fluff” before writing to me)

au.fluff@email.spencermortensen.com
(remove the “.fluff” before writing to me)

In general, only a human or an AI can break this.
It’s mainly useful for when you need to publish your email address on an untrusted site.

This isat minimuminconvenient for your users, and may prevent them from reaching you at all.

Breaks usability.The user has to understand and follow the instructions perfectly, or they will be unable to reach you.

### 1.13HTMLImage

Blocked 100% of 318 spammers

<
img

src
=
"
email.jpg
"

width
=
"216"

height
=
"18"

alt
=
"email address"
>

This is inconvenient or inaccessible for every one of your users.

Breaks usability.Sighted users are forced to type out the full email address by hand.
The remaining users have no way to reach you.

### 1.14CSSContent

Blocked 100% of 318 spammers

<
span

class
=
"email"

data-user
=
"af"

data-domain
=
"email.
spencer
mortensen.
com"
>
</
span
>

span
.
email
::
after
 {

content
:
attr
(
data-user
)
'@'

attr
(
data-domain
);
}

This breaks basic usability (e.g. the text can be seen, but not copied), so it is worthless.

It is possible for harvesters to recover the full email address from the HTML alone, without interpreting the CSS, so this cannot be considered safe.

Breaks usability.The email address can be seen, but not selected. This is very frustrating! Eventually, the user is forced to give up or type out the full email address by hand.

### 1.15CSSText direction

Blocked 100% of 318 spammers

<
span

class
=
"email"
>
moc
.nesnetromrecneps
.liame
@ea
</
span
>

span
.
email
 {

unicode-bidi
:
bidi-override
;

direction
:
rtl
;
}

moc.nesnetromrecneps.liame@ea

This technique breaks usability, and can be undone by basic harvesters that don’t interpret CSS, so it is useless.

Breaks usability.The email address can be copied, but the text is reversed. Eventually, the user is forced to give up or type out the full email address by hand.

## 2 Clickable link

These techniques protect a clickable link that will open the user’s mail client (e.g.email).
Note that only the href “mailto:” attribute is protected.
If the link textalsocontains the email address, then the email address is additionally exposed as plain text, and you’ll need to layer on at least one of theplain-textobfuscation techniques.

### 2.1 No protection

Blocked 0% of 299 spammers

<
a

href
=
"mailto:
am
@email
.spencermortensen
.com"
>
email
</
a
>

email

### 2.2 HTML entities

Blocked 100% of 299 spammers

<
a

href
=
"&#109;
&#97;
&#105;
&#108;
&#116;
&#111;
&#58;
&#97;
&#110;
&#64;
&#101;
&#109;
&#97;
&#105;
&#108;
&#46;
&#115;
&#112;
&#101;
&#110;
&#99;
&#101;
&#114;
&#109;
&#111;
&#114;
&#116;
&#101;
&#110;
&#115;
&#101;
&#110;
&#46;
&#99;
&#111;
&#109;"
>
email
</
a
>

email

HTML entities are often decoded automatically by server-side libraries, which means that even the most basic harvesters can get your email addresses without any special effort.
This technique should be worthless—and, yet, it still stops most harvesters.

### 2.3 URL encoding

Blocked 96% of 299 spammers

<
a

href
=
"mailto:
%61
%6f
%40
%65
%6d
%61
%69
%6c
%2e
%73
%70
%65
%6e
%63
%65
%72
%6d
%6f
%72
%74
%65
%6e
%73
%65
%6e
%2e
%63
%6f
%6d"
>
email
</
a
>

email

Server-side libraries make it trivial to undo URL encoding, so this technique is essentially worthless—and, yet, it still stops most harvesters.

### 2.4 HTTP redirect

Blocked 100% of 299 spammers

<
a

rel
=
"nofollow, noindex"

href
=
"email/"
>email</
a
>

RewriteEngine

On

RewriteRule

^email/$

'mailto:
email
@example
.com'

[R=302,L]

RewriteEngine

On

RewriteRule

^email/$

'mailto:
email
@example
.com
?subject
=Hi'

[R=302,QSA,L]

email

This technique turns a “mailto:” link into a regular link, without breaking its mail capability, and hides it among the other links on the page.

If you’re planning to fill out any of the fields of the email, then you should use the second form of the “.htaccess” file (with the QSA flag included) to ensure that the query string is preserved.

Because the link doesn’t lead to an actual webpage, search engines might report this to you as a broken link.
The “nofollow, noindex” tags prevent this by instructing search engines not to follow and index the link.

When you’re fully satisfied with the redirect, you may wish to switch from a temporary (302) redirect to a permanent (301) redirect.
After you’ve loaded a permanent (301) redirect, your browser will ignore any further changes that you make.
This makes further testing more difficult, but it can make the redirect faster.

### 2.5HTMLSVG

Blocked 100% of 299 spammers

<
object

class
=
"email"

width
=
"33"

height
=
"24"

data
=
"email
.svg"

type
=
"image/svg+xml"
></
object
>

<
svg

viewBox
=
"0 0 33 24"

xmlns
=
"http://
www.w3.org
/2000
/svg"
>

<
style
>
@
import

url
(
'https://
fonts
.googleapis
.com
/css2
?family=
Indie
+Flower
&amp;display=
swap'
);

text
 {

dominant-baseline
:
middle
;

fill
:
#000
;

font-family
:
'Indie Flower'
;

font-size
:
16px
;

text-anchor
:
middle
;
}
</
style
>

<
a

href
=
"mailto:
email
@example
.com"
>
	<
text

x
=
"50%"

y
=
"50%"
>
email
</
text
>
</
a
>

</
svg
>

object
.
email
 {

height
:
2em
;

margin
:
-1em 0
;

vertical-align
:
middle
;
}

Inspiration:rouninmedia.github.io

This hides the email address in an unusual place where most harvesters won’t think to look.
However, the email address is stored there in plain text.

This technique is accessible to all users, including those who depend on a screen reader.
But youmustuse an object element for this to work:
an img element would give you an image that is non-interactive,
and inline SVG would put the email address in the source code where harvesters would find it easily.

The “width” and the “height” attributes help prevent layout shifts while the page is loading.
Because the dimensions depend on the font, the SVG file has to explicitly specify a web font to prevent rendering issues.

### 2.6 ConcatenationJS

Blocked 100% of 299 spammers

<
script
>
document
.write(
'<a href="mailto:'
+'a'
+'p'
+'@'
+'e'
+'m'
+'a'
+'i'
+'l'
+'.'
+'s'
+'p'
+'e'
+'n'
+'c'
+'e'
+'r'
+'m'
+'o'
+'r'
+'t'
+'e'
+'n'
+'s'
+'e'
+'n'
+'.'
+'c'
+'o'
+'m'
+'">email</a>'
);
</
script
>

This is convenient because it has no external dependencies, and yet still manages to block most harvesters. However, the full email address appears directly in the HTML, so this technique cannot be considered safe.

### 2.7 Rot18JS

Blocked 100% of 299 spammers

<
a

class
=
"email"

href
=
"znvygb:
nd
@rznvy
.fcraprezbegrafra
.pbz"
>
email
</
a
>

<
head
>
	<
script

src
=
"
link-rot18.js
"

defer
>
</
script
>
</
head
>

email

This technique can be undone by basic harvesters that don’t interpret JavaScript.
At the very least, you should rotate your letters by something other than 13, and rotate your numbers by something other than 5.

### 2.8 ConversionJS

Blocked 100% of 299 spammers

<
a

id
=
"link-conversion"

rel
=
"nofollow, noindex"

href
=
"to-
email-
spencer/"
>
email
</
a
>

<
head
>
	<
script

src
=
"
link-conversion.js
"

defer
>
</
script
>
</
head
>

email

In this technique, the HTML source code contains a decoy link, and you write a custom function that converts that decoy link into a working “mailto” link.

Most harvesters can only access the HTML source code—and the source code contains nothing of value.
The only practical way to restore the “mailto” link is to run your custom conversion function in a web client with DOM and JavaScript support.
This is not possible for most harvesters.

You can write a custom function for each email address, or you can write a single function and apply it to all of the email addresses on the page.

Despite beingfrighteninglysimple, this is expected to be one of the very best techniques.

### 2.9JSAES encryption

Blocked 100% of 299 spammers

<
a

class
=
"email"

rel
=
"nofollow, noindex"

href
=
"x
d
7
L
-
A
O
A
9
Q
c
k
l
5
R
X
b
F
u
F
w
8
L
x
u
i
P
Z
P
k
3
v
z
y
P
S
5
5
-
K
l
D
-
a
7
8
c
0
0
r
n
g"
>
email
</
a
>

<
head
>
	<
script

src
=
"
link-aes.js
"

defer
>
</
script
>
</
head
>

email

This technique uses AES 256 to encrypt the email address.
(AES is the only publicly-available cipher approved by the NSA for top secret information.)
The email address cannot be recovered without the JavaScript file—which most harvesters cannot access or run.
This implementation uses the browser’s own built-in cryptography library, so it will not run outside of the browser, even in JavaScript-capable environments.

The cryptography library,SubtleCrypto, is only available insecure contexts(such as over https or on localhost)—which could be a blocker if you’re using http.
You must upgrade to https before you can use this technique!

### 2.10 User interactionJS

Blocked 100% of 299 spammers

<
a

id
=
"link-interaction"

rel
=
"nofollow, noindex"

href
=
"to-
email-
spencer/"
>
email
</
a
>

<
head
>
	<
script

src
=
"
link-interaction.js
"

defer
>
</
script
>
</
head
>

email

This technique keeps the email address hidden until the user interacts with the page; onlythenis the email address revealed.
This raises the bar for harvesters: they not only need to run a full web client, theyalsoneed to interact with it.

This technique can be used to trigger other techniques.

## 3 Observations

### Most harvesters are easily defeated

Every obfuscation technique can be broken, so some people assume that there is no point to obfuscation.
Nothing could be further from the truth!
Most harvesters are unsophisticated, and even the simplest techniques are unreasonably effective at defeating them.

### Harvesters follow leads more than links

Harvesters often jump straight to the high-traffic pages, ignoring low-traffic pages and links.
As a result, some pages are very rarely or never seen by harvesters, which can lead people to falsely believe thatnopageseverneed protection.
This is false, and dangerous, since a page can suddenly go viral.

## 4 Methodology

This article is not only an article for human readers, it’s also a honeypot for harvesters.
Each technique is protecting an email address:
When that address receives spam, I know which technique was broken.
I make a list of which addresses each spammer knows, and I use that list to build up the statistics.

In order toreliablycollect statistics, I’ve had to disable spam filtering at every step along the way.
The big mail providers filter out a huge amount amount of spam that never reaches their users (some of it appears in the Spam folder, and some of it is silently deleted and never shown).
Desktop mail clients often do something similar.
As a result, I’ve set up my own mail server and client.

I deduplicate messages as best I can, so the statistics won’t be distorted by arbitrary details like the volume of email that a spammer sends.
I keep track of which email addresses the spammer knows, and nothing else.
This is a lot harder than it looks, because spammers often try to conceal their identities!

Harvesters generally don’t target both plain-text address and clickable links, so I keep those statistics independently:
That’s why the total spammer counts are different for text-based and link-based obfuscation techniques.

There is some uncertainty in the statistics because the sample sizes are still relatively small.
(Small, but growing.)
The more people link to this article, the better these statistics will become!
