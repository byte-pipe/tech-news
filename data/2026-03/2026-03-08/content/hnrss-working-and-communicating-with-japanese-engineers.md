---
title: Working and Communicating with Japanese Engineers | TokyoDev
url: https://www.tokyodev.com/articles/working-and-communicating-with-japanese-engineers
site_name: hnrss
content_file: hnrss-working-and-communicating-with-japanese-engineers
fetched_at: '2026-03-08T07:25:40.669419'
original_url: https://www.tokyodev.com/articles/working-and-communicating-with-japanese-engineers
author: Alex Chen
date: '2026-03-03'
description: Working on an international tech team comes with communication challenges that go beyond just language. Here’s some practical advice I’ve gathered in my ten years of working in Japan.
tags:
- hackernews
- hnrss
---

If you’re an international developer working at a Japanese company, you’ve probably felt some communication-related pain. Whether your team primarily uses English, Japanese, or a mix of both, chances are there’s occasionally friction.

In a field where poor communication leads to wasted effort, bugs, and low team morale, what can we do? Learning technical and business Japanese is obviously useful, but that’s just one piece of a bigger puzzle.

Having worked in Japan for 10 years as a non-native Japanese speaker, communication is a subject that’s always been on my mind. This was especially true during the six years I worked atMercari, one of Japan’s first tech companies to adopt an international engineering organization composed of developers from both Japan and from abroad.

I initially joined the company as an English-Japanese interpreter, and later transitioned to a software development position. I worked with a large number of international teams in both roles, and witnessed all sorts of communication struggles firsthand. And although I provided support by interpreting between English and Japanese, I also realized that the challenges went far beyond just language.

Fortunately, I also had the privilege of seeing many of these teams gradually overcome those communication difficulties. Thanks to those experiences, I can confidently say that regardless of your Japanese level or your colleagues’ English levels, there are things you can do right now to improve understanding and confidence on both sides of the language barrier.

I advise people to:

* Make your English more understandable
* Practice technical terms in Japanese
* Create new meeting strategies
* Look beyond language

## Make your English more understandable

Being aware of your own speaking habits in English is crucial, and surprisingly easy for native speakers to forget.

Consider this: if you’re very comfortable speaking English, but your Japanese teammates are not, how do you think they feel when communicating with you? It’s probably nerve-racking and takes a lot of mental bandwidth. You can accommodate by making your English more understandable.

Making your English understandable doesnotmean ”speak extremely slowly,” and it certainly doesn’t mean “speak louder.”

Even when done with good intentions, these actions can be condescending, and the unnatural rhythm could ironically throw off the listener even more.

Instead, keep these questions in mind when you speak:

* Am I using run-on sentences?
* Am I constantly jumping from one idea to another?
* Am I using vague or difficult vocabulary?
* Am I using too much slang, idiomatic language, or “corporate speak?”
* Is my message clear and direct, or am I being too indirect?
* Am I pronouncing my words distinctly and clearly, or am I slurring them together?

### Scenario 1: A PM is talking to developers about upcoming goals.

Hey, so I was just sync-ing with the stakeholders and we’re thinking we really need to focus on user-facing touchpoints, because there’s too much sign-up friction. Like, we need to 10x the stickiness of the landing page but also keep it lean, and I saw the latest build and the UX isn’t quite there. We might need to pivot the North Star from legacy technical debt to user retention while also future-proofing scalability for the Q3 roadmap.

It’s easy to see why this doesn’t work. Words likesync,touchpoints,friction, andstickinessare not easy to understand.SynergyandNorth Starare corporate buzzwords. “Isn’t quite there” is vague. While the PM heredoeshave a message to convey, even a proficient English speaker is unlikely to understand it in one try.

How could we simplify this message? A common piece of guidance for bridging cultures and languages is to go low context: be clear and specific. Avoid implications and prefer direct statements.

I just had a meeting with the stakeholders. We noticed that the landing page’s UI is complicated, and many users don’t finish signing up. Because of that, I want to set a new goal for this week. Let’s make the sign-up process more simple, and increase user retention. I know our original plan was to remove technical debt, but I would like to prioritize the UI this week. Is that okay with everyone?

This is much better—the speaker delivers the same core message but with concrete details instead of buzzwords. For example, “The landing page’s UI is complicated” is much easier to understand than “sign-up friction.” The speaker follows by introducing the goals “Make the sign-up process more simple” and “Increase user retention,” both of which are far more clear and actionable than “Pivot the North Star to user retention.”

### Scenario 2: A developer is sharing what they are working on.

So I’ve been looking into the bug report from yesterday regarding the user profile save button. I checked the logs and it looks like the Put request is hitting a timeout in the validation layer. I thought it was a permissions thing so I updated the API policy but that didn’t work because the payload is actually missing the auth token in certain edge cases. I’m now trying to trace why the state isn’t persisting but I might have to look at the global store because the reducer might be wiping the data before the fetch completes.

The developer clearly worked hard to investigate, but is giving a “stream of consciousness” update where they assume the listener knows as much about the problem as they do. They give a detailed list of what they did, but it would be more helpful to simply summarize the issue and make an actual plan.

I’m working on the bug where users can’t save their profiles. The save button fails because the app forgets the users’ login info before it sends the update to our servers. It’s happening because the page updates too fast and clears the info. I’m going to try a fix that holds on to the data for a few extra seconds.

Summarizing the issue concisely requires a little more effort, but also makes it easier to understand for everyone, whether English is their native language or not.

### Other best practices

* Give context. Share the goal/purpose first, followed by the specific actions needed. “The goal is to roll back. Here is why: one, the server load was too high. Two, the API timed out.”
* Standardize vocabulary. Native speakers like using synonyms to avoid repetition, but this can be confusing for non-native speakers. For example,release, deploy, and shipare often used interchangeably, but it’s helpful to be consistent.
* Use clear transitions. Strong transitionsreallyhelp the listener know how to interpret the next sentence.However . . .Because of that . . .The problem is . . .First, second, finally
* However . . .
* Because of that . . .
* The problem is . . .
* First, second, finally
* Check for understanding. If you share an important message, you’ll want to make sure it was understood.But don’t just ask “Do you understand?” because it’s too easy to simply nod and say “Yes.” It also creates pressure to do so.Try asking in a way that invites the listener to get clarification, like “Is there any part I should explain again?”
* But don’t just ask “Do you understand?” because it’s too easy to simply nod and say “Yes.” It also creates pressure to do so.
* Try asking in a way that invites the listener to get clarification, like “Is there any part I should explain again?”
* Avoid passive voice. Instead of saying “The code was deployed by the engineer,” say “The engineer deployed the code.”

These best practices will help you in any situation in life, not only when working with international tech teams. Miscommunications happen all the time even between native speakers of the same language, and delivering crystal-clear messages is a skill on its own.

### The better your English, the harder it is

At Mercari, I worked with native English speakers, non-native but fluent speakers, and beginner/intermediate speakers. I noticed that native speakers of English were themostlikely to have these difficult-to-follow speaking habits, given that they could output words effortlessly and without monitoring themselves.

Similarly, native Japanese speakers often had difficult speech habits in Japanese. In addition to the points already mentioned, honorific and humble speech made things hard to understand for non-native listeners.

One major initiative that helped was theYasashii Communication Training, which taught employees to be more aware of their speaking habits and helped international team members meet each other halfway.

## Understanding technical jargon in Japanese

Even if you’re comfortable with conversational Japanese, technical vocabulary could pose a challenge. On top of that, there are very few resources out there that help software developers in Japan learn technical vocabulary.

Thankfully, companies like Mercari andWizcorphave compiled lists to help:

* Engineer Vocabulary List
* Japanese Lingo for Developers

These are excellent guides to help you gradually ramp up your Japanese vocabulary. Take it slow and just try to learn a few words a day—no need to brute force it. Combining these guides with natural input from your day-to-day work will help your brain synthesize new language skills.

### Katakana: often helpful, sometimes misleading

You’ve probably noticed that a huge amount of technical vocabulary can simply be converted into katakana and used in conversation. Words like debug (デバッグ,debaggu), release (リリース,riri-su), and merge (マージ,ma-ji), for example, are used the same way in both English and Japanese.

Remember that it isn’talwaysa perfect 1:1 conversion. For some words the English and Katakana versions have slightly different meanings. Like all languages,Japanese has many loan words and shortenings of themwhose meanings are based in the time and context they were originally imported.

Here are some examples:

Design (デザイン,dezain)

* In English, this can refer to anything, including visible UI/UX design, database design, and system design.
* In Japanese, this is used only for UI/UX design. When talking about database or system design, Japanese speakers use 設計 (sekkei) instead.

Fix (フィックス,fikkusu)

* In English, this can mean to “rectify a problem/bug” or “set the date” for a meeting/event.
* In Japanese, it is generally used only for the latter meaning. Japanese speakers use 修正 (shuusei) or 直す(naosu) to mean “repair” or “rectify.”

There are also some loanwords that have totally different meanings from what you’d expect. These are often used in the workplace, so don’t be confused if you hear them.

Batting (バッティング,battingu)

* This meansconflict, as in a meeting conflict.
* ミーティングがバッティングしている (mi-tingu ga battingu shiteiru), for example, means “The meetings are conflicting.”

Flying (フライング,furaingu)

* This isn’t about defying gravity. It refers to doing something too quickly, without having received permission or approval.
* フライングでコードをデプロイした (furaingu de ko-do wo depuroi shita) means “He deployed the code without permission.”

Claim (クレーム,kure-mu)

* This refers to a complaint from a user or customer.
* クレームが入った (kure-mu ga haitta) means “We got a complaint.” Hopefully you don’t hear this too often!

Revenge (リベンジ,ribenji)

* This isn’t as scary as it sounds. It just means to “try again.”
* If your team tried deploying something but was forced to roll back due to a bug, you might hear someone say リベンジしよう (ribenji shiyou). Don’t worry, it doesn’t mean they want to inflict harm on anyone! They’re just saying “Let’s try [deploying that] again.”

Merit (メリット,meritto) and demerit (デメリット,demeritto)

* Despite sounding a bit awkward to an English speaker, these words are very commonly used to mean “pros and cons.”
* この設計のメリットを教えてください (kono sekkei no meritto wo oshiete kudasai) means “Tell me about the advantages of this design choice.”
* この設計のデメリットを教えてください (kono sekkei no demeritto wo oshiete kudasai) is “Tell me about the disadvantages of this design choice.”

Lastly, be aware that some katakana words are commonly abbreviated differently in colloquial Japanese, often becoming unrecognizable to English speakers. Here are some examples:

* Pull request: プルリク (pururiku)
* Database: デービー (dei-bee)
* Reschedule: リスケ (risuke)
* Topic/theme (of a meeting): テーマ (te-ma)
* Response (to an email or Slack message) : レス (resu)
* Appointment/meeting with a client: アポ (apo)
* Smartphone: スマホ（sumaho)
* PC: パソコン (pasokon, derived from “personal computer”)

## Create new meeting strategies

Whenever you have a team meeting, take a few minutes to plan your communication in advance. You might think it’s overkill, but there’s absolutely nothing weird about gathering your thoughts and even lightly rehearsing beforehand.

If the meeting is in English, and you have a slightly complex topic to share with your Japanese-speaking team members, think for a minute about how you could structure your talk in a way that follows the best practices mentioned earlier. If your few minutes of preparation make the conversation easier for your team to follow, that’s a net positive.

If you’re not one hundred percent comfortable in Japanese but your meeting requires you to speak it, do the same thing! Take a few minutes to think about “How would I say ____ in Japanese?” and plan accordingly. You may realize there’s a word or concept that you aren’t sure how to express. That’s a golden opportunity to look it up, learn something new, and immediately use it in real-life application.

Lastly, regardless of your Japanese level, the most important thing to do at any meeting is check your understanding. The golden phrase to use is この認識で合っていますか (kono ninshiki de atteimasu ka) which means “Is my understanding correct?”

This is a phrase that you should not hesitate to use at every single meeting you attend. After having an important conversation, if you can summarize what you understood and double-check that it’s correct, your communication will be rock-solid.

### Fostering a culture of language learning

If you work on an international team, chances are that everyone has some desire to improve at their non-dominant language. I highly recommended fostering a culture where you all help each other learn, and no one is afraid of making mistakes.

One small but effective approach that many teams at Mercari took was to occasionally switch up meeting languages. For example, one team generally held meetings in Japanese, but every Friday was “English Day.” This gave members the chance to practice speaking English regularly without too much pressure.

If your team is up for it, I would recommend giving small experiments like this a try—just keep it fun and lighthearted to start.

## Look beyond language

Cultural differences can impact communication just as much as linguistic differences.

Keep in mind that the following are general statements and do not apply to all people from particular cultures. That being said, non-Japanese employees may have certain communication tendencies that differ from those of their Japanese coworkers.

One of those habits common to people from Western countries is being more direct and assertive. Whether it be during meetings, in casual conversation, or through text, many international developers prefer to say exactly what’s on their mind with minimal hesitation. For example, developers from the West see no problem with clearly stating their opposition to a topic and listing the reasons why they oppose it—in many ways, this is seen as good, clear communication. This style can sometimes be jarring to Japanese speakers, who generally prefer to avoid anything that could be taken as blunt or confrontational.

Another difference involveswhento speak during meetings or presentations. Japanese speakers tend to “wait their turn” to speak. During presentations, they almost always defer questions and comments until the end, when the presentation is finished. Non-Japanese employees, on the other hand, are more likely to speak up as soon as something comes to mind.

As a result, we have teams where some participants prefer a structured approach to communication, while others prefer a more freeform approach. Neither communication style is necessarily better than the other, but on an international team, it’s not hard for the non-Japanese employees to overpower their colleagues. If you have a strong preference for either style, you don’t need to force yourself to change. Just be mindful that your coworkers may have different tendencies.

It can help everyone in a team to make it clear what the expected communication style and processes are.

If you notice that certain members are very quiet at a meeting, despite seeming like they have something to say, see if you can give them an opportunity. A simple “Does anyone else have thoughts on this?” can go a long way in making sure everyone feels heard.

For a deeper dive on this topic, check out this article abouthow to improve your communication skills in Japanese.

## Final thoughts

You don’t need to be fluent in Japanese or a perfect English speaker to make a difference to your team. Start small: pick one habit from this article to work on this week. Learn three new technical Japanese words. Ask questions at your next meeting to make it more inclusive. Try switching languages at your next standup as an experiment, and see how your team handles it.

Working on an international tech team comes with unique challenges, but it’s also an incredible opportunity. Every conversation you navigate, every new phrase you learn, and every cultural nuance you pick up makes you a more valuable team member—not just in Japan, but anywhere in the world.
