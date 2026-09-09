---
title: 'Remembering Why We Code: Dropping AI for Fundamental Learning - DEV Community'
url: https://dev.to/annavi11arrea1/remembering-why-we-code-dropping-ai-for-fundamental-learning-4868
site_name: devto
content_file: devto-remembering-why-we-code-dropping-ai-for-fundamenta
fetched_at: '2026-09-10T07:20:48.595793'
original_url: https://dev.to/annavi11arrea1/remembering-why-we-code-dropping-ai-for-fundamental-learning-4868
author: Anna Villarreal
date: '2026-09-06'
description: Excitement I wanted to share my excitement of forcing myself to build without using AI. I... Tagged with learning, beginners, programming, java.
tags: '#learning, #beginners, #programming, #java'
---

The rewarding rush of manual problem-solving

### Excitement

I wanted to share my excitement of forcing myself to build without using AI.

I would say I've been learning to code semi-consistently for roughly 3 years. Most recently, I started a class called Java 2. It builds on foundational concepts learned in the previous class. I feel I might be spread a bit thin, dabbling over here in Ruby, dabbling over there in Python, and then poking around at Java on Sunday afternoon. Good thing they share the overarching concepts or it would be utter confusion. ¯(°_o)/¯

As many of us have been leaning heavily into AI to build amazing things at lightspeed, I made the conscious decision to not open a single AI tool as I power through the first assignment of the class. I said to myself "No, I'm going to struggle because I want to understand." And I can tell you, after using AI constantly, this was a wakeup call to the real rewards that exist when you stop relying on AI.

I did google a few things, but that is allowed if you ask me. This is the internet, after all.

### Getting Things to Click Again

At some point in my assignment things started clicking again. That was an amazing moment. A class can have methods, we can call those in the main function, I can nest switch statements for nested menus, and I can debug in real life with minimal resources! Twice I got stuck, and twice I came out the other sided with that excited "**** yes, it's working!" moment - a feeling I have been missing for some time. The feeling that you struggled and powered through it and figured out what was seemingly impossible by yourself.

Here is the sub-menu I built today with a nested switch statement.

import
 
java.util.ArrayList
;

import
 
java.util.List
;

import
 
java.util.Scanner
;

// Runs a console program that lets the user add and analyze texts,

// then stores and prints the texts entered during the session.

public
 
class
 
Main
 
{

 
public
 
static
 
void
 
main
(
String
[]
 
args
)
 
{

 
Scanner
 
scanner
 
=
 
new
 
Scanner
(
System
.
in
);

 
List
<
String
>
 
texts
 
=
 
new
 
ArrayList
<>();

 
boolean
 
running
 
=
 
true
;

 
System
.
out
.
println
(
" --------------------------------"
);

 
System
.
out
.
println
(
"| Paragraph Parser |"
);

 
System
.
out
.
println
(
" --------------------------------"
);

 
System
.
out
.
println
();

 
while
 
(
running
)
 
{

 
System
.
out
.
println
(
"1. General Text Analysis"
);

 
System
.
out
.
println
(
"2. Do a specific text analysis"
);

 
System
.
out
.
println
(
"3. Display Texts"
);

 
System
.
out
.
println
(
"4. Exit"
);

 
int
 
choice
 
=
 
readInt
(
scanner
,
 
"Choose an option: "
);

 
switch
 
(
choice
)
 
{

 
case
 
1
:

 
Text
 
analysisResult
 
=
 
displayText
(
scanner
,
 
"Add text to analyze:\n"
);

 
System
.
out
.
println
(
analysisResult
);

 
break
;

 
case
 
2
:

 
// nested switch for sub-menu text analysis tools

 
Scanner
 
scannerNestedScanner
 
=
 
new
 
Scanner
(
System
.
in
);

 
boolean
 
extraTestRunning
 
=
 
true
;

 
while
 
(
extraTestRunning
)
 
{

 
System
.
out
.
println
(
"1. Word frequency finder"
);

 
System
.
out
.
println
(
"2. Find frequency of specific character"
);

 
System
.
out
.
println
(
"3. Find the number of unique words"
);

 
System
.
out
.
println
(
"4. Return to main menu"
);

 
int
 
extraChoice
 
=
 
readInt
(
scannerNestedScanner
,
 
"Choose text analysis tool (Enter number): "
);

 
switch
 
(
extraChoice
)
 
{

 
case
 
1
:

 
WordFrequency
 
wordFrequency
 
=
 
new
 
WordFrequency
(
displayText
(
scannerNestedScanner
,
 
"Enter the text to search through:\n"
).
content
.
toLowerCase
());

 
String
 
wordToFind
 
=
 
displayText
(
scannerNestedScanner
,
 
"Enter the word to find its frequency:\n"
).
content
;

 
wordToFind
 
=
 
wordToFind
.
replaceAll
(
"\\p{Punct}+"
,
 
""
);

 
//strip punctuation so it doesn't affect the word frequency count

 
System
.
out
.
println
(
"Word frequency analysis for: "
 
+
wordToFind
+
 
" -> "
 
+
 
wordFrequency
.
findWordFrequency
(
wordToFind
));

 
break
;

 
case
 
2
:

 
CharacterFrequency
 
charFrequency
 
=
 
new
 
CharacterFrequency
(
displayText
(
scannerNestedScanner
,
 
"Enter the text to analyze:\n"
).
content
);

 
System
.
out
.
println
(
"Character frequency analysis for: "
 
+
 
charFrequency
.
getCharacterFrequencyCount
(
displayText
(
scannerNestedScanner
,
 
"Which character are we looking for? Enter a character:\n"
).
content
.
charAt
(
0
)));

 
// Add your extra test logic here

 
break
;

 
case
 
3
:

 
UniqueWords
 
uniqueWords
 
=
 
new
 
UniqueWords
(
displayText
(
scannerNestedScanner
,
 
"Add text to count unique words:\n"
).
content
);

 
System
.
out
.
println
(
"Number of unique words: "
 
+
 
uniqueWords
.
getUniqueWordCount
());

 
break
;

 
case
 
4
:

 
extraTestRunning
 
=
 
false
;

 
break
;

 
default
:

 
System
.
out
.
println
(
"Invalid option for extra test."
);

 
}

 
}

 
break
;
 
// Add this break to prevent fall-through from case 2 to case 3 in the main switch.

 
case
 
3
:

 
System
.
out
.
println
();

 
displayTexts
(
texts
);

 
break
;

 
case
 
4
:

 
running
 
=
 
false
;

 
break
;

 
// Fall through to default case if needed.

 
default
:

 
System
.
out
.
println
(
"Invalid option. Please try again."
);

 
}

 
}

 
System
.
out
.
println
(
"\nFinal text list:"
);

 
displayTexts
(
texts
);

 
scanner
.
close
();

 
}

Enter fullscreen mode

Exit fullscreen mode

I discovered that having nested switch statements is both doable and useful. I heard somewhere that this is often used in games and it's nice to have an understanding of how one might incorporate that.

Guys I seriously encourage you, put down the AI just for a few hours and fight with something. Your old self, those feelings you have been missing, they will return! Instant youth, almost guaranteed. XD

Tell me, what have you recently challenged yourself to build without using AI?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse