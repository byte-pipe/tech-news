---
title: 'Complete silence is always hallucinated as "ترجمة نانسي قنقر" in Arabic which translates as "Translation by Nancy Qunqar" · openai/whisper · Discussion #2608 · GitHub'
url: https://github.com/openai/whisper/discussions/2608
site_name: hackernews_api
fetched_at: '2025-07-23T04:07:25.342766'
original_url: https://github.com/openai/whisper/discussions/2608
author: edent
date: '2025-07-22'
description: Complete silence is always hallucinated as "ترجمة نانسي قنقر" in Arabic which translates as "Translation by Nancy Qunqar"
tags:
- hackernews
- trending
---

openai



/

whisper

Public

* NotificationsYou must be signed in to change notification settings
* Fork10.4k
* Star85.3k

# Complete silence is always hallucinated as "ترجمة نانسي قنقر" in Arabic which translates as "Translation by Nancy Qunqar"#2608

 puthre



 started this conversation in

General

 Complete silence is always hallucinated as "ترجمة نانسي قنقر" in Arabic which translates as "Translation by Nancy Qunqar"


#2608

 puthre


Jun 13, 2025

·

 14 comments

·

 5 replies


Return to top



Discussion options



Quote reply

## puthreJun 13, 2025



-

If you generate complete silence in a wav file and run whisper on it, it will always hallucinate the same thing

ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 30 silence.wav

whisper ./silence.wav --language Arabic --model large-v3[00:00.000 --> 00:29.980] ترجمة نانسي قنقر

It seems that the model learned to interpret silence as ترجمة نانسي قنقر in arabicAny way to fix / circumvent this?

BetaWas this translation helpful?Give feedback.



19


You must be logged in to vote


😄

145



👀

1





All reactions

## Replies:14 comments·5 replies



Comment options



Quote reply

### misutonekoJun 14, 2025



-

VAD, probably.I've only tried the turbo one, but what I can say is that v3 isdifferentfrom the earlier models.It looks like it doesn't have the audio descriptions to fall back on and produces hallucinations instead.

The earlier models will also produce some miscellaneous crap when they encounter silence(they do this regardless of language), but there are more options for how to deal with that.

For example, these things can be effective for the small model (but not for v3):

* the suppress_tokens trick
* setting initial prompt to something like "."
* adjusting logprob_threshold to -0.4 (works for this empty audio, probably not good for general use)

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### Navanit-gitJul 8, 2025



-

is there any good arabic model you guys found which is better than large v3 ?@misutoneko@puthre

BetaWas this translation helpful?Give feedback.



0


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### moadel321Jul 22, 2025



-

Voxtral was released a few days ago and looks promising

BetaWas this translation helpful?Give feedback.


👍

1





All reactions



Comment options



Quote reply

### rjb729951Jul 17, 2025



-

I found a similar thing happens in German where it says"Untertitelung des ZDF für funk, 2017."

For both German and Arabic I found that this pretty much only happens at the very end of videos / when there is sustained silence.

BetaWas this translation helpful?Give feedback.



22


You must be logged in to vote


😄

30



❤️

1





All reactions

 0 replies




Comment options



Quote reply

### KillerXJul 22, 2025



-

Essentially this seems to be an artifact of the fact that Whisper was trained on (amongst other things) YouTube audio + available subtitles. Often subtitlers add their copyright notice onto the end of the subtitles, and the end of the videos are often credits with music, applause, or silence. Thus whisper learned that silence == "copyright notice".

See some research for the Norwegian example here:

https://medium.com/@lehandreassen/who-is-nicolai-winther-985409568201

BetaWas this translation helpful?Give feedback.



32


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### qpwoJul 22, 2025



-

In English there is always applause

BetaWas this translation helpful?Give feedback.



7


You must be logged in to vote


😄

25



🎉

3





All reactions

 0 replies




Comment options



Quote reply

### iodize6399Jul 22, 2025



-

this also happens when you don't speak into the voice mode, the transcript usually results in the same Arabic phrase

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### dharmabJul 22, 2025



-

I've also seen this happen a lot in English withSkyeye:

It also happens a lot with hallucinations saying stuff like "This is the end of the video, remember to like and subscribe"

BetaWas this translation helpful?Give feedback.



6


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### AhmedGMurtazaJul 22, 2025



-

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote


👎

124



😄

2



🚀

1





All reactions

 1 reply




Comment options



Quote reply

#### nyxierealJul 22, 2025



-

Ok? This doesn't have anything to do with the topic of this discussion

BetaWas this translation helpful?Give feedback.


👍

10





All reactions



Comment options



Quote reply

### ei23fxgJul 22, 2025



-

In german it's "Vielen Dank" (Thank you very much)

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### lloydjatkinsonJul 22, 2025



-

This has been a problem since at least February 2024:https://x.com/SheriefFYI/status/1756694995241951398

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### alentodorovJul 22, 2025



-

in romanian, i’ve noticed multiple instances where the transcripts ends with “nu uitati sa da-ti like si subscribe” which, as you might easily infer , translates to “don’t forget to like and subscribe”.

BetaWas this translation helpful?Give feedback.



6


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### andrewmccaffertyJul 22, 2025



-

BetaWas this translation helpful?Give feedback.


😄

17





All reactions



Comment options



Quote reply

### taf2Jul 22, 2025



-

Interesting google translates this into "Translated by Nancy Kangar"

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### rany2Jul 22, 2025



-

It gets it right if you set the source language to Arabic.

BetaWas this translation helpful?Give feedback.



All reactions



Comment options



Quote reply

### abdussamadbelloJul 22, 2025



-

You can either finetune the model or filter the response from whisper

text = "helo helo hello ."
target_phrase = "ترجمة نانسي قنقر"
replacement = ""

updated_text = text. Replace(target_phrase, replacement)

print(updated_text)

BetaWas this translation helpful?Give feedback.



1


You must be logged in to vote



All reactions

 0 replies




Comment options



Quote reply

### sheriefJul 22, 2025



-

ChatGPT voice mode is also affected by this fwiw:https://x.com/SheriefFYI/status/1929129956153377144

BetaWas this translation helpful?Give feedback.



2


You must be logged in to vote



All reactions

 1 reply




Comment options



Quote reply

#### abdussamadbelloJul 22, 2025



-

Other languages don't get as much support as English during the data annotation and fine-tuning stages of most models

BetaWas this translation helpful?Give feedback.



All reactions

Sign up for free

to join this conversation on GitHub
.
 Already have an account?

Sign in to comment
