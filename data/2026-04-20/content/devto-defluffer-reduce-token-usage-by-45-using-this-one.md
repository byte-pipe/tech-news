---
title: Defluffer - reduce token usage 📉 by 45% using this one simple trick! [Earthday challenge] - DEV Community
url: https://dev.to/grahamthedev/defluffer-reduce-token-usage-by-45-26jj
site_name: devto
content_file: devto-defluffer-reduce-token-usage-by-45-using-this-one
fetched_at: '2026-04-20T12:03:01.614669'
original_url: https://dev.to/grahamthedev/defluffer-reduce-token-usage-by-45-26jj
author: GrahamTheDev
date: '2026-04-18'
description: 'This is a submission for Weekend Challenge: Earth Day Edition Fluffer: someone who helps people "get... Tagged with devchallenge, weekendchallenge, javascript, ai.'
tags: '#devchallenge, #weekendchallenge, #javascript, #ai'
---

DEV Weekend Challenge: Earth Day

This is a submission forWeekend Challenge: Earth Day Edition

Fluffer:someone who helps people "get ready for work" in the adult film industryDefluffer:a simple script that removes "fluff" and "filler" from your prompts! Could save over a million trees worth of CO2 a year (but probably not).

Don't worry, this article is about the latter and is my silly submission (but with a real message and principles that can have massive environmental impact) for the Earth Day challenge!

## What I Built

I built Defluffer - a text length reduction tool to keep your prompts nice and short!

Save an average of 45% tokens of your prompt text
with near zero compute!!!!

Every token you can save in a prompt means hundreds of tokens saved in a full conversation with a LLM due to how the whole context is loaded at each step (simplified explanation).

Defluffer is inspired byCaveman- except it uses code to reduce the payload size as using a LLM...to save tokens sent to a LLM, well...it uses tokens...and that just seemed silly!

Is it a serious project?Absolutely not, don't use it in production for the love of all that is mighty!

Are the principles useful to think about?Absolutely!

Fewer tokens = fewer Megawatts = less pollution / water / reduces the need for rare resources for GPUs etc. etc.

It also saves you money when using the APIs vs subscriptions!

In theory, if you "sured up" this script, and every developer in the world used it, we could save over60 Gigawatts a year(fluffed numbers from Gemini based on 40 mil devs using AI, 30 prompts a day and saving 135 tokens per prompt.)

Or:

* 🏡 5600 Homes Powered for a YEAR!
* 📱 3.94 billion Phone Charges
* 🌳 1.12 million Tree CO2 absorption Equivalence!

NowTHATis how we save the planet!

## Demo

There is a box at the top where you can enter a prompt and see how many tokens / words you can save when it is "defluffed"!

Here is a demo prompt you can copy paste in to try it!:

Hello there! I would really appreciate it if you could act as a senior backend developer. I am trying to figure out how to write a python script that connects to the database and retrieves all of the information from the user repository. 

Make sure that the results are filtered so that the retry count is greater than or equal to 5, and the active status is strictly equals to true. Due to the fact that the application is currently in the production environment, it is required that you utilize the environment configurations instead of hardcoding the parameters into the functions.

Also, I have a question about the following snippet. Could you please refactor this code without using any external libraries? 

` `
 
`javascript
function calculateMaximum(array) {
 if (array === null) return 0;
 return Math.max(...array);
}
`
 
` `

Take into consideration that the output should be formatted as a standard JSON object. If you don't mind, please provide a step by step guide on how to deploy this microservice to the kubernetes cluster at the very end. Thank you so much!

Enter fullscreen mode

Exit fullscreen mode

You can also see some sliders to see potential yearly savings in CO2 / power below that in the "impact calculator" tab.

You can also see the test suite size reduction results using Defluffer on a few sample prompts in the "test results" tab!

### Codepen Demo, make sure to scroll down!!!

## Code

The core code is really simple.

The hard part was the list of phrases to "compress" (which is essentially just a list of phrases that we do a replace on, or remove).

You canView The Code and Replace List in Codepen

Below is the entire class though!

class
 
Defluffer
 
{

 
constructor
(
dictionaries
)
 
{

 
this
.
phrasesAndLogic
 
=
 
{
 
...
dictionaries
.
phrases
,
 
...
dictionaries
.
logic
 
};

 
this
.
synonyms
 
=
 
dictionaries
.
synonyms
 
||
 
{};

 
this
.
blacklist
 
=
 
new
 
Set
(
dictionaries
.
blacklist
 
||
 
[]);

 
}

 
compress
(
prompt
)
 
{

 
let
 
text
 
=
 
prompt
;

 
let
 
protectedItems
 
=
 
[];

 
// 1. Extract and protect code blocks

 
text
 
=
 
text
.
replace
(
/
(
``
`

{
%
 
endraw
 
%
}

[
\
s
\
S
]
*
?

{
%
 
raw
 
%
}

```|`
[
^
`]+`
)
/
g
,
 
(
match
)
 
=>
 
{

 
protectedItems
.
push
(
match
);

 
return
 
`PROT
${
protectedItems
.
length
 
-
 
1
}
PROT`
;

 
});

 
// 2. Strip multi-word blacklist entries

 
for 
(
const
 
entry
 
of
 
this
.
blacklist
)
 
{

 
if 
(
!
entry
.
includes
(
'
 
'
))
 
continue
;

 
const
 
escaped
 
=
 
entry
.
replace
(
/
[
.*+?^${}()|[
\]\\]
/g
,
 
'
\\
$&
'
);

 
text
 
=
 
text
.
replace
(
new
 
RegExp
(
`
\\
b
${
escaped
}
\\
b`
,
 
'
gi
'
),
 
''
);

 
}

 
// 3. Phrase and logic collapsing

 
for 
(
const
 
[
phrase
,
 
replacement
]
 
of
 
Object
.
entries
(
this
.
phrasesAndLogic
))
 
{

 
if 
(
!
phrase
)
 
continue
;

 
const
 
escaped
 
=
 
phrase
.
replace
(
/
[
.*+?^${}()|[
\]\\]
/g
,
 
'
\\
$&
'
);

 
const
 
regex
 
=
 
new
 
RegExp
(
`
\\
b
${
escaped
}
\\
b`
,
 
'
gi
'
);

 
text
 
=
 
text
.
replace
(
regex
,
 
()
 
=>
 
{

 
if 
(
!
replacement
 
||
 
replacement
.
trim
()
 
===
 
''
)
 
return
 
'
 
'
;

 
protectedItems
.
push
(
replacement
);

 
return
 
`PROT
${
protectedItems
.
length
 
-
 
1
}
PROT`
;

 
});

 
}

 
// 4. Tokenize

 
let
 
tokens
 
=
 
text
.
split
(
/
(\b[
a-zA-Z0-9_'-
]
+
\b)
/
);

 
// 5. Apply single-word blacklist and synonyms

 
tokens
 
=
 
tokens
.
map
(
token
 
=>
 
{

 
if 
(
!
/^
[
a-zA-Z0-9_'-
]
+$/
.
test
(
token
))
 
return
 
token
;

 
if 
(
/^PROT
\d
+PROT$/
.
test
(
token
))
 
return
 
token
;

 
const
 
lower
 
=
 
token
.
toLowerCase
();

 
if 
(
this
.
blacklist
.
has
(
lower
))
 
return
 
''
;

 
if 
(
this
.
synonyms
[
lower
])
 
return
 
this
.
synonyms
[
lower
];

 
return
 
token
;

 
});

 
// 6. Rejoin and clean

 
text
 
=
 
tokens
.
join
(
''
)

 
.
replace
(
/
\s
+/g
,
 
'
 
'
)

 
.
replace
(
/
\s
+
([
.,?!;:
])
/g
,
 
'
$1
'
)

 
.
trim
();

 
// 7. Restore protected items

 
protectedItems
.
forEach
((
item
,
 
index
)
 
=>
 
{

 
const
 
placeholder
 
=
 
`PROT
${
index
}
PROT`
;

 
while 
(
text
.
includes
(
placeholder
))
 
{

 
text
 
=
 
text
.
replace
(
placeholder
,
 
item
);

 
}

 
});

 
// 8. Final cleanup

 
return
 
text

 
.
replace
(
/
\s
+/g
,
 
'
 
'
)

 
.
replace
(
/
\s
+
([
.,?!;:
])
/g
,
 
'
$1
'
)

 
.
trim
();

 
}

}

Enter fullscreen mode

Exit fullscreen mode

## How I Built It

Vibe coded with Google Gemini!

I essentially:

* mapped out the problem space and the inspiration.
* went though provided options (which included NLP libraries and other things I dismissed) until we came up with the core principles:Whitespace Reduction:Pure regex changing tabs, double spaces etc to single spaces.Phrase Collapsing:Dictionary lookup or phrases and their replacements.Fluff Blacklist:Hash set lookup of words to just remove (a, it etc.).Symbolic Logic:Dictionary lookup and replace ("not" becomes!)Stemming/Synonyms:Dictionary lookup and replace ("application" becomes "app")
* Whitespace Reduction:Pure regex changing tabs, double spaces etc to single spaces.
* Phrase Collapsing:Dictionary lookup or phrases and their replacements.
* Fluff Blacklist:Hash set lookup of words to just remove (a, it etc.).
* Symbolic Logic:Dictionary lookup and replace ("not" becomes!)
* Stemming/Synonyms:Dictionary lookup and replace ("application" becomes "app")
* Got Gemini to write the code and create the dictionary
* Asked for more dictionary items
* Asked for even more
* Gave up and asked Claude as it isn't stingy with message length
* added basic code exclusion (we dont want to removeias a var, so we leave code intact) and key phrases exclusion "act as a" to "be", but then make sure "be" is protected so we don't remove it later.
* got Gemini to write some test phrases.
* got Gemini to add a pretty UI and some basic "equivalant CO2 savings" at the bottom.

## Prize Categories

Best Use of Google Gemini???!???...even though I had to use Claude as it just won't do long messages?

I mean I am asking a LLM to write code to reduce it's own token usage so the irony of wanting a long message is not lost on me sotechincallyGemini was better than Claude here? haha

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse