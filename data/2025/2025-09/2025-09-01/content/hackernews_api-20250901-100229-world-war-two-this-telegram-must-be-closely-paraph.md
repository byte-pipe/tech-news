---
title: world war two - "This telegram must be closely paraphrased before being communicated to anyone." Why? - History Stack Exchange
url: https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone
site_name: hackernews_api
fetched_at: '2025-09-01T10:02:29.695969'
original_url: https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone
author: azeemba
date: '2025-08-31'
description: “This telegram must be closely paraphrased before being communicated to anyone”
tags:
- hackernews
- trending
---

70

Some historical documents from WWII have a notice on them stating

This telegram must be closely paraphrased before being communicated to anyone.

The documents I've found were received by the United States, and are part of the FDR Presidential Library and Museum. Here's a poorly-cropped photo of one:

and links toone dated 1939-09-01andanother dated 1940-01-07.

T.E.D. also found onefrom 1941 from Churchill to F.D.R..

The normal use of the word "paraphrase", as found in dictionaries, would not normallyneedto be doneclosely. If the idea is to deliberately be vague and not disclose information out of the message, then one would not want to paraphraseclosely; I imagine a "close" paraphrase would not be vague or inaccurate. If accuracy is paramount, an exact quote could be a better choice than a paraphrase: why choose to paraphrase, never mindrequireit?

So what did this phrase mean? Was it an instruction to rephrase every sentence in the message before distribution, because the messages in question had been sent encoded, so as not to leak plaintext (which might be used to help crack the cipher)? Or is this stock phrase using some other meanings of "must", "closely", or "paraphrase" than I'm expecting?

My web searches for "paraphrase" and "telegram" have found a few examples of this phrase, but I haven't found an explanation of it anywhere yet. I searched and skimmed some Wikipedia pages related to cryptography and World War II, but haven't found anything about measures to avoid leaking plaintext.

* world-war-two
* united-states
* communication

edited
2 days ago

Dan Getz

 asked
Aug 26 at 17:12

Dan Getz
Dan Getz

743
1
1 gold badge
5
5 silver badges
8
8 bronze badges

 New contributor

Dan Getz
 is a new contributor to this site. Take care in asking for clarification, commenting, and answering.
Check out our
Code of Conduct
.

3

## 2 Answers2

 Sorted by:


 Reset to default


 Highest score (default)


 Date modified (newest first)


 Date created (oldest first)


105

It appears that it was US military communications doctrine to not send the exact same message twice using different encryption ("none" counting as one type of encryption), and the term of art for changing a message to avoid that was indeed "paraphrase".

I managed to dig up a US Army document on Cryptology from roughly that era that appears to discuss paraphrasing. The document in question isDepartment of the Army Technical Manual TM 32-220(pdf), dated 1950, titled "BASIC CRYPTOGRAPHY". It apparently supersedes previous documents TM-484 from March 1945 and TM 11-485 from June 1944. It would probably be more ideal to look at them, since they are closer to the time you are interested in, but I was not able to find them online.

Here's what this declassified manual had to say about "paraphrasing", from Chapter 7, in the section Fundamental Rules of Cryptographic Security, section 84, subsection b, rule 3 (titled "Text of messages")

(a) Never repeat in the clear the identical text of a message once
sent in cryptographic form, or repeat in cryptographic form the text
of a message once sent in the clear. Anything which will enable an
alert enemy to compare a given piece of plain text with a cryptogram
that supposedly contains this plain text is highly dangerous to the
safety of the cryptographic system. Where information must be given
out for publicity, or where information is handled by many persons,
the plain text version should be very carefullyparaphrasedbefore
distribution, to minimize the data an enemy might obtain from an
accurate comparison of the cryptographic text with the equivalent,
original plain text.Toparaphrasea message means to rewrite it so
as to change its original wording as much as possible without
changing the meaning of the message. This is done by altering the
positions of sentences in the message, by altering the positions of
subject, predicate, and modifying phrases or clauses in the sentence,
and by altering as much as possible the diction by the use of
synonyms and synonymous expressions.In this process, deletion rather
than expansion of the wording of the message is preferable, because
if an ordinary message isparaphrasedsimply by expanding it along
its original lines, an expert can easily reduce theparaphrasedmessage to its lowest terms, and the resultant wording will be
practically the original message. It is very important to eliminate
repeated words or proper names, if at all possible, by the use of
carefully selected pronouns; by the use of the words "former,"
"latter," "first-mentioned," "second-mentioned"; or by other means.
After carefullyparaphrasing, the message can be sent in the other
key or code.

(b) Never send the literal plain text or aparaphrasedversion of the plain text of a message which has been or will be
transmitted in cryptographed form except as specifically provided in
appropriate regulations

(emphasis mine)

In fact the allies would have have known intimately about how this was possible, because this is one of the ways they ended updecrypting the stronger German Enigma cipher. Captured machines using simpler ciphers were used to break those simpler ciphers. The fact that the Germans were encrypting theexact same messagesin both ciphers meant the allies could know (for those messages) what both the unencrypted and encrypted messages were, which allowed them to decrypt the stronger cyphers as well, or quickly figure out what today's code was.

Though Enigma had some cryptographic weaknesses, in practice it was
German procedural flaws, operator mistakes, failure to systematically
introduce changes in encipherment procedures, and Allied capture of
key tables and hardware that, during the war, enabled Allied
cryptologists to succeed.

edited
Aug 28 at 23:24

 answered
Aug 28 at 14:38

T.E.D.
♦
T.E.D.

125k
17
17 gold badges
325
325 silver badges
497
497 bronze badges

3

0

I was able to find the manuals mentioned in the other comment, but can't reply bc new account:

RadioNerds-TM 11-485 (PDF) (33.22 MB) 4

Internet Archive-US Army Cryptography Manuals Collection (see "TM_11-485.pdf")

edited
38 mins ago

MCW
♦

35.2k
12
12 gold badges
112
112 silver badges
167
167 bronze badges

 answered
51 mins ago

Typpi
Typpi

1
1
1 bronze badge

 New contributor

Typpi
 is a new contributor to this site. Take care in asking for clarification, commenting, and answering.
Check out our
Code of Conduct
.

## Your Answer

Draft saved

Draft discarded

### Sign up orlog in

 Sign up using Google


 Sign up using Email and Password


Submit

### Post as a guest

Name

Email

Required, but never shown

### Post as a guest

Name

Email

Required, but never shown

 Post Your Answer


 Discard


By clicking “Post Your Answer”, you agree to ourterms of serviceand acknowledge you have read ourprivacy policy.

Start asking to get answers

Find the answer to your question by asking.

Ask question

Explore related questions

* world-war-two
* united-states
* communication

See similar questions with these tags.
