---
title: 'Launch HN: Issen (YC F24) – Personal AI language tutor | Hacker News'
url: https://news.ycombinator.com/item?id=44387828
site_name: hackernews
fetched_at: '2025-06-28T01:05:53.777355'
original_url: https://news.ycombinator.com/item?id=44387828
author: mariano54
date: '2025-06-28'
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

Launch HN: Issen (YC F24) – Personal AI language tutor
292 points
 by
mariano54

1 day ago

 |
hide
 |
past
 |
favorite
 |
253 comments
Hey HN, we're Mariano and Anton from ISSEN (
https://issen.com
), a foreign language voice tutor app that adapts to your interests, goals, and needs.

Demo:https://www.loom.com/share/a78e713d46934857a2dc88aed1bb100d?...We started this company after struggling to find great tools to practice speaking Japanese and French. Having a tutor can be awesome, but there are downsides: they can be expensive (since you pay by the hour), difficult to schedule, and have a high upfront cost (finding a tutor you like often forces you to cycle through a few that you don’t).We wanted something that would talk with us — realistically, in full conversations — and actually help us improve. So we built it ourselves.
The app relies on a custom voice AI pipeline combining STT (speech-to-text), TTS (text-to-speech), LLMs, long term memory, interruptions, turn-taking, etc. Getting speech-to-text to work well for learners was one of the hardest parts — especially with accents, multi-lingual sentences, and noisy environments. We now combine Gemini Flash, Whisper, Scribe, and GPT-4o-transcribe to minimize errors and keep the conversation flowing.We didn’t want to focus too much on gamification. In our experience, that leads to users performing well in the app, achieving long streaks and so on, without actually getting fluent in the language you're wanting to learn.With ISSEN you instantly speak and immerse yourself in the language, which, while not easy, is a much more efficient way to learn.We combine this with a word bank and SRS flashcards for new words learned in the AI voice chats, which allows very rapid improvement in both vocabulary and speaking skills. We also create custom curriculums for each student based on goals, interests, and preferences, and fully customizable settings like speed, turn taking, formality, etc.App:https://issen.com(works on web, iOS, Android)
Pricing: 20 min free trial, $20–29/month (depending on duration and specific geography)We’d love your feedback — on the tech, the UX, or what you’d wish from a tool like this. Thanks!

anavat

23 hours ago

 |
next

[–]

Thanks for working on this! Language learning really needs a breakthrough.

Now, I tried the web app and chose to learn Greek as a beginner. And while I had better experience with your app than with ChatGPT or Gemini voice modes, I still got lost 5 minutes in because the AI tutor doesn't seem to have a plan for me, nor does it "see" my struggles. For example, after asking me about a hobby, it gives me a long sentence in Greek about how how it is nice to hike in mountains. Being absolute noob I cannot reply to it, nor even repeat it. And I don't even know what it is expected from me at the moment. A human tutor here would probably repeat a part of the sentence with a translation and ask me to repeat, or would explain something. The AI just sits there waiting for me to make a sound, and when I make it, it goes on on a tangental subject of beach vacations. :)Again, this is still relatively not bad, and I'm going to give it another try.

reply

drakonka

23 hours ago

 |
parent
 |
next

[–]

I had a similar feeling with Swedish just now. It isn't really much different than conversing with ChatGPT in advanced voice mode - it's up to me to drive the conversation and it all feels quite arbitrary (and I find myself instinctively falling back on topics I know how to talk about, which quite defeats the purpose). I was hoping for a more structured learning plan that strategically expands my comfort zone and skills in a guided way.

reply

mariano54

23 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks for the feedback. Yeah we need to improve the beginner experience, it's more tailored towards intermediate/advanced students at the moment.

reply

55555

22 hours ago

 |
root
 |
parent
 |
next

[–]

I'm an advanced learner but I stopped after a few moments because it's boring. It's asking me questions that you'd ask a beginner (although a beginner wouldn't understand the questions). It just asked what food I like to eat, where I like to travel, whether I like the weather, etc. I have a language tutor IRL and I have found that we run out of things to talk about too. So we often find ourselves just discussing the latest events from the news. I think you should feed fresh conversation topics daily from a data source like the news, localized to the user. There are global news APIs you can subscribe to.

reply

Velorivox

6 minutes ago

 |
root
 |
parent
 |
next

[–]

I'm not sure that would solve the problem. Ultimately this (and speaking with LLMs in general) feels a lot like filling in an adaptive form rather than talking to a human being. The LLM, for example, is never going to go on and tell you some anecdote from its life (and if it were prompted to do so it would come across as quite insincere). It's not going to say, "Oh that neighborhood is not safe," when you tell it about where you'll live when studying abroad. It's not going to recommend supplementary material.

I'm not even sure this helps with speaking practice since it's just a test of whether what you said can be transcribed by Whisper, which is not at all a test of correct pronunciation. I just tried it with the most horrid, butchered accent I could muster, and it still worked...if I practiced for months on end like that, I'd end up in a very difficult place as a language learner.

reply

drakonka

23 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Do you mean that the experience is meant to have more structure if you pick the intermediate or advanced level? (fwiw I did pick intermediate for my Swedish level in the app).

My thinking is - I can have unstructured conversations with Advanced Voice Mode or in real life here in Sweden. What I'd really appreciate is a guided learning experience taking me up from intermediate/slightly above intermediate to fluent in the most efficient possible way (as opposed to just having us 'ramble' about random topics of my own choosing).

reply

mariano54

21 hours ago

 |
root
 |
parent
 |
next

[–]

There is a structured curriculum that gets generated after the intro lesson (if you responded yes to the curriculum question).

This is available for all proficiencies. It's just much harder to talk for hours in a new language as a beginner. It's usable but requires more effort.

reply

drakonka

5 hours ago

 |
root
 |
parent
 |
next

[–]

I see it now, thank you! This looks like what I was hoping for. I wonder if there's some way to communicate very clearly that you'll need to talk for around n minutes to get a structured curriculum prepared - and maybe even show a progress bar of some sort so the user can have an idea of when they're going to get to "the good stuff"?

Another thing is that the trial period seems incongruent. To me the structured curriculum is what I really want to _try_. I want to see what the planned lessons are like, how guided they are, etc. But the trial runs out and tries to make me pay right after the unstructured more all-over-the-place feeling introductory conversation, and I'm not prepared to pay at that point since I feel like I haven't gotten to evaluate the main part of the product at all. I would suggest leaving the trial unlocked to maybe the first three structured lessons of the learning plan. Let the user really experience what they'll be paying for.

reply

Ocha

23 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

So basically if you are starting a new language from zero, then this is not for you?

reply

mariano54

22 hours ago

 |
root
 |
parent
 |
next

[–]

That's correct.

reply

candiddevmike

23 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Why wouldn't intermediate/advanced students just talk directly to ChatGPT? From what I see, I thought your value prop was for the beginners.

reply

mariano54

21 hours ago

 |
root
 |
parent
 |
next

[–]

ISSEN is designed from the ground up for this use case.

* curriculum, completely customizable, with grammar, roleplay, topics, speaking speech, transcript, dictionary, corrections, etc* prompting and AI models all chosen to be a better fit for multilingual, easy to understand, etc.* the tutor actively tries to teach you, it's not an assistant* integrated flashcards that go hand in hand with the speaking immersion

reply

cameldrv

20 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

As an intermediate German speaker I thought it was great!

reply

sotix

14 hours ago

 |
parent
 |
prev
 |
next

[–]

Language Transfer[0] will continue to be a better resource than any AI course. It’s very hard to beat a human that has put in time crafting a logical way to teach a language with the appropriate ramp ups. The Greek course on there is fantastic. And it’s free with zero ads. Best language learning tool I’ve ever used period.

[0]:https://www.languagetransfer.org/

reply

frank20022

6 hours ago

 |
root
 |
parent
 |
next

[–]

Agreed, languagetransfer is fantastic. Much better than any "AI tutor".

reply

candiddevmike

13 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

What's the best way to listen to this on your mobile in a way that will remember your location? SoundCloud app?

reply

xzel

9 hours ago

 |
root
 |
parent
 |
next

[–]

They have their own app. It’s pretty minimal but it does save your spot.

reply

sirodoht

20 hours ago

 |
parent
 |
prev
 |
next

[–]

Funnily enough I said my native language is Greek but then it responded with an error and reset my onboarding guide. Then, I lied that my native language is English, which worked. But now it calls me Anton, rather than the name I said I have!

reply

dbuxton

19 hours ago

 |
root
 |
parent
 |
next

[–]

I also got Anton. Looks like something's hard coded - or maybe a caching issue?

reply

kevmo314

22 hours ago

 |
parent
 |
prev
 |
next

[–]

I think this is a pretty big limitation of the architecture (STT->LLM->TTS) they've chosen. The intonation around struggling to speak or difficulty with certain phrases is totally lost when the text is transcribed.

reply

mattbee

22 hours ago

 |
parent
 |
prev
 |
next

[–]

I paid for Memrise to polish up French. The scripted lessons alwere great but it dropped me into an AI conversation assistant that did exactly the same. It forgot the vocab and grammar level that the scripted lessons had taught, and often broke into idiom. I haven't picked it up since.

reply

Nadya

22 hours ago

 |
root
 |
parent
 |
next

[–]

I'm a Memrise beta member w/ lifetime premium access for my contributions to the site in its early days. I cannot recommend anyone use Memrise for anything nowadays it has been so heavily enshittified. In fact, I recommend against using it in favor of Anki (Memrise's biggest strength over Anki in the early days was the community mnemonics and courses (Anki equivalent "community decks") - none of which really exist in any way today).

I tried following the modern Japanese track on Memrise and was appalled at how bad it is nowadays.

reply

koakuma-chan

22 hours ago

 |
parent
 |
prev
 |
next

[–]

I think the point here is for you to
practice
 (i.e. develop "muscle memory" for speaking), not to
learn
.

reply

thaumasiotes

18 hours ago

 |
root
 |
parent
 |
next

[–]

As far as using language goes, those aren't different things.

reply

artur_makly

4 hours ago

 |
prev
 |
next

[–]

OMG this app f'n rocks.
My convo with my Argentine mujer is soooo fluid and smooth.

I've been living in Buenos Aires for over 18 years now, so my pronunciations and accent is quite good. It's just that I never had the proper early fundamental foundations of grammar ..so I have a bunch of embarrassing holes that need filling -- this app is quite precise when it comes to focusing on those aspects.Te felicito!Ps my only nit pick so far is the UX on ios > the Settings modal > when opened there is no clear CTA to close it. Because the click-state of the settings button is 97% the same color as the non-click state.Solution :
1 - add a close X button to the top right (standard accessibility)2 - change the click-state Color of the settings button to a reverse color or accent color.Want more UX tear-downs?
Dm me artur at visualsitemaps.com

reply

masspro

15 hours ago

 |
prev
 |
next

[–]

I don't think I can trust TTS for language learning. I could be internalizing wrong pronunciation, and I wouldn't know. One time I tried Duolingo for Japanese already knowing a bit. To their credit I assumed it was recorded clips, until it read 'oyogu' as something like 'oyNHYAOgu', like it concatenated two syllable clips that don't go together. If I didn't already know, would I be trying to study and replicate that nonsense? So I don't know if I could trust TTS audio for language study regardless of what kind of tech it is. Sure mistakes can be unlearned over time spent immersing, but at much more effort than just not internalizing them in the first place.

Also Japanese specifically has this meme where it literally is a pitch-accent language but many people say it's not and teaching resources ignore it. E.g. 'ima' means either 'now' or 'living room' depending if syllable #2 is higher or lower. Clearly only applies to some languages, but is another dimension even harder to a learner to know there's a mistake. I have to imagine even other Latin languages probably have reading quirks where this could happen to me.

reply

mariano54

5 hours ago

 |
parent
 |
next

[–]

Minimax's new model is quite good. We use their voices for some of our Japanese tutors. The pitch accent is almost perfect.

There are incorrect reading or Chinese readings occasionally, but you can tell when that happens due to the furigana being different

reply

yorwba

4 hours ago

 |
root
 |
parent
 |
next

[–]

If you have the correct furigana, you could even detect when the TTS model picked the wrong reading and regenerate.

But how do you know the furigana are correct? Unless you start out fully human-annotated text, you need some automated procedure to add furigana, which pushes the problem from "TTS AI picked the wrong reading" to "furigana AI picked the wrong reading."

reply

mariano54

3 hours ago

 |
root
 |
parent
 |
next

[–]

Yes it pushes the problem, but it's a much easier problem, and models like Gemini flash 2.5 do very well.

reply

barrell

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Yeah Japanese TTS is a lot harder than it looks. I’m also building a language learning application, and constantly ran into incorrect readings. Eleven labs, eleven labs v3, OpenAI, play.ht, azure, google, Polly — I’ve tried them all. They are all really bad (more than 1/3 the expressions had an error in them somewhere).

It _is_ fixable though. It took me about a week, but I have yet to find a mistaken reading now. This also seems to just be the case with Japanese - most tonal languages seem to have the correct tones (I’m not qualified to comment on how natural the tones sound, but I have yet to find a mismatch like in Japanese)

reply

jamager

5 hours ago

 |
parent
 |
prev
 |
next

[–]

Yes. AI transcription is great, AI
translation is OK (depending on language pair), but TTS is still pretty awful for most languages.

reply

runarberg

13 hours ago

 |
parent
 |
prev
 |
next

[–]

Also a Japanese learner here—albeit a beginner. As I understand it, the pitch accent is about stress, languages can stress a syllable with length, volume, pitch, etc. Spanish uses vowel length, Icelandic uses volume, English uses a combination of length and volume, and Swedish (just like Japanese) uses pitch. Just like in English if you put the wrong stress on the word it can range anything from sounding foreign to being incomprehensible. (Aside: I always remember trying to say the name of the band Duran Duran to an English speaker, while putting the stress on the first syllable like is normal in Icelandic, but my listener had no idea what I was saying, it took probably 30 attempts before I was corrected with the correct stress).

I think Japanese is somewhat special though for a large number of homonyms (i.e. words that are spelled the same) so speaking with the correct pitch becomes somewhat more important.

reply

glandium

11 hours ago

 |
root
 |
parent
 |
next

[–]

Somewhat more important, but as someone with decent Japanese who knows about pitch accent but can barely hear the difference in real time, and never actively learned it except for the few well known examples like bridge/chopstick, I don't think it matters all that much. Yes, you'll sound foreign. But you'll be understood nevertheless, in the vast majority of cases.

reply

runarberg

9 hours ago

 |
root
 |
parent
 |
next

[–]

Speaking of bridge/chopsticks, I created a video to try to spot the difference my self a couple of months ago:

https://imgur.com/KJXanqc

reply

glandium

4 hours ago

 |
root
 |
parent
 |
next

[–]

Here's the problem: pitch accent is easy to hear in isolation and/or in comparison. Under real life conditions, in the middle of a sentence, it's a completely different experience. But then you're saved by context. Because candy is most likely not falling from the sky. Homophones that are still ambiguous in context are possible, but a rare occurrence in my experience.

reply

thinkingtoilet

23 hours ago

 |
prev
 |
next

[–]

>We didn’t want to focus too much on gamification.

Thank you so much for this. Duolingo is literally unbearable because it's so gamified. I'll try it out later. I've seen a few of these apps, can I seamlessly go between my native language and the language I'm trying to learn? If I am trying to learn Hindi, can I ask a question in English in the middle of a conversation?

reply

vjerancrnjak

21 hours ago

 |
parent
 |
next

[–]

The app is optimized on the whole population, not on individual level. They even publish papers on global optimization.

These kinds of learning apps are destined to become mediocre over time.The learning metric is so easy to capture, the learning content so easy to produce, yet no one has an individualized loop to make learning work well.For example, I'd press "Training" on Duolingo, and would get nowhere. Same lessons all of the time. Bread and water.

reply

ChadNauseam

16 hours ago

 |
root
 |
parent
 |
next

[–]

Duolingo is laughably inefficient. I have an app I've made for myself to learn french, and it's amazing how little effort is required to make something 10x better. (I completed the french Duolingo tree and learned essentially nothing so I feel justified in saying that.) If you're learning french, let me know and I'll add you to the app.

reply

mariano54

23 hours ago

 |
parent
 |
prev
 |
next

[–]

Yes, we've spent a lot of time getting the STT and TTS to work seamlessly in multilingual, it works pretty well!

reply

thinkingtoilet

12 hours ago

 |
root
 |
parent
 |
next

[–]

I said I would use it and report back. Unfortunately, the experience was not great for me. I told it multiple times I'm a beginner and not speak in full, long sentences in my target language, and it would remember that for one response maybe, then switch right back to full sentences. I had to keep telling it I couldn't understand it and that I'm a beginner. After the 4th or 5th time I gave up.

reply

TypingOutBugs

8 hours ago

 |
parent
 |
prev
 |
next

[–]

Babbel is better than Duolingo!

reply

thinkingtoilet

2 hours ago

 |
root
 |
parent
 |
next

[–]

Unfortunately, Babbel doesn't have a Hindi course. I wish it did.

reply

iandanforth

22 hours ago

 |
prev
 |
next

[–]

Alright, having tried this with Japanese I can say it's frustrating. As a near complete beginner the tutor kept speaking in Japanese even when I said "sorry I don't understand" repeatedly and then when I asked it to start in English and then gradually transition to Japanese it lasted all of one sentence in English before switching back. I can totally see how this would be useful conversation practice if you've progressed that far, but I'd love to have something for even earlier beginners. Also since many of the models you use are natively multi modal this could readily integrate visual media for discussion and grounding.

Also, for the transcription it would be great to get pure romanji to start with!

reply

antonaf

22 hours ago

 |
parent
 |
next

[–]

Yes, I can understand and empathize with your experience. Quite honestly our current focus is more for B1+ students. That 0 -> 1 / bootstrapping of the language is much better served by traditional material that is less talking / listening-heavy.

reply

SkyBelow

1 hour ago

 |
root
 |
parent
 |
next

[–]

I think I'm around A2 in Japanese and find myself kinda scared by all these talking apps. I don't mind texting, because it gives me time to look up what I don't know and much more time to think about my response, but talking just makes me feel very anxious. Eventually I have to get over the barrier, but it is a barrier to entry and could scare people away.

I do think immersion is generally better, but it is not only harder, an AI app doesn't seem like it could do the right kind of immersion (missing body language, visual cues, seeing the mouth movements, and all sorts of other things one gets from watching a podcast, or even better, in person interaction).

reply

55555

22 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Unfortunately, I think you will soon learn that the market for advanced language learners is 1/500th the size of the market for beginner learners. But thank you very much and please keep focusing on us.

reply

iandanforth

20 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This is demonstrably false. Natural language acquisition is almost entirely listening and talking. The fastest and most consistently effective way to learn a language is immersion. The reason traditional material doesn't attempt immersive techniques is because it is
much much
 easier to print a static book than it is to produce interactive and adaptive content.

The promise and potential of LLM based language learning apps is that you can cross that gap to full immersion in a way that has never been possible before.Please be more ambitious.

reply

ookdatnog

2 hours ago

 |
root
 |
parent
 |
next

[–]

Learning primarily through listening and talking only works if you have an enormous amount of high quality data, ie, the situation you're in as a baby when you're surrounded by native speakers who are producing speech for hours every day.

If you are an adult and want to spend, say, a couple of hours each week learning a language from scratch, especially without constant access to a native speaker, your initial progress will be much faster if you study grammar and vocabulary in a traditional class from a text book, than if you just try to pick up patterns from listening to the TV or something.I can't source my claim. I attended a public lecture years ago from a researcher about exactly this misconception.

reply

jamager

5 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> Natural language acquisition is almost entirely listening and talking

Listening and reading. Talking goes last. See Steve Kaufmann, for example

reply

npinsker

19 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Your comment sparked an idea of a conversation with an agent where at any time you could ask, “what’s this word?” and it would respond with an image explaining it. I’m surprised there don't seem to be voice apps that integrate any visual content.

reply

glandium

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

> Natural language acquisition is almost entirely listening and talking.

And it's bootstrapped by 1+ year of listening before being even able to speak, let alone talk intelligibly. That's not really an appealing process to anyone beyond that age.

reply

thaumasiotes

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

> The reason traditional material doesn't attempt immersive techniques is because it is much much easier to print a static book than it is to produce interactive and adaptive content.

No, that's not correct.First off, you can provide immersion with static books. A common favorite here on HN isLingua Latina per se illustrata["the Latin tongue explained by itself"].Second off, there are two reasons that traditional material doesn't do this. The biggest one is student demand; people are afraid of immersion. The second is that the traditional approach is faster. It's lower quality, and it tops out well below the level you hope to reach, but it's faster, not slower. It takes babies a year to learn to say they're hungry. It takes an elementary school class studying a foreign language less than a day.

reply

itake

23 hours ago

 |
prev
 |
next

[–]

I'm trying to learn vietnamese, but the lessons are really really rough and borderline bad advice.

---AI: Anh mệt is good if bạn are a man speaking about yourself. You can also say, “Em mệt” if you’re a woman.this isn't correct. If you are of "older brother" age and are male, you say Anh. Em is for if you are "younger person" (does not matter the gender). Women tend to prefer being called "em" (even if they are older), because women prefer to be identified as younger than their true age... But that doesn't mean you can't call younger men em.A good tutor would know your age relative to theirs and explain this context.---It would say english phrases with a vietnamese accent.---It also would give me really complex vietnamese phrases that I am not ready for. when I prompt for an explaination or translation, it would get off track from the original thing we were learning.---Way more people in Vietnam (and the globe) speak southern Vietnamese, but the tutors seem to be from north Vietnam.---The STT also was very forgiving if I pronounced things incorrectly. Or it would confuse english and vietnamese. I would say, "Phai", but it heard "bye"---I was ready to pull out my credit card, but I can't trust it to teach me the right information. I pay $160/mo for Vietnamese tutoring ($20 per class). This would be way cheaper and I don't have to schedule my classes.

reply

mariano54

20 hours ago

 |
parent
 |
next

[–]

We are really sorry for the subpar experience. We did not test Vietnamese, and it seems like the quality is not sufficient. Thanks for pointing out the issues.

reply

true_pk

18 hours ago

 |
parent
 |
prev
 |
next

[–]

Hey, it’s great to see other people learn Vietnamese! And your feedback is on point. I’m still at the beginning and just built a tool to help me learn basic phrases. I will very much appreciate the feedback!
https://envn.app

reply

itake

18 hours ago

 |
root
 |
parent
 |
next

[–]

I haven't figured out what works for me yet when learning Vietnamese, so I'm not really sure yet was advice to give.

Trying out your tool, I'd really like to know if the sound is north or southern Vietnamese. I think your tool is southern vietnamese, but idk.. I personally prefer learning southern, but all the AI TTS tools use the north dialect. Ideally, I'd like a 'pure' southern accent and not a hybrid.For your tool, You might want to get into the way to address people (Anh, em, ba, co, etc). You seem to just use toi (which I hear vietnamese people using with each other too...) but my understanding is the (Anh/Em/Ba/etc) are more 'intimate' whereas toi is more formal/business like?One idea I haven't tried too much of yet is making flash cards that teach me a sentence structure, but introduce new vocabulary. Learning a diaspora of phrases works for short 2-3 word ones, but when I try to learn more complex sentences, my brain isn't able to draw the patterns as nothing is connected.For example, trying to learn "bạn tên là gì" and "nhà vệ sinh ở đâu" (from your website) is harder than learning "Bạn tên là gì?", "Bạn nghề là gì?", "Bạn số điện thoại là gì?"The other huge challenge I have is feeling like I am making progress. I'm definitely getting better, but its pretty disheartening to study for 40+ hours and still can't pronounce words like Can Tho properly, despite knowing how to read and write.---My email is in my profile. Feel free to reach out to me if you have more updates or want to bounce ideas.

reply

tempodox

23 hours ago

 |
parent
 |
prev
 |
next

[–]

This sounds very much like the kinds of mistakes that LLMs typically make. It's a pity, I would love a good language learning platform.

reply

Velorivox

20 hours ago

 |
root
 |
parent
 |
next

[–]

A fundamental problem with language learning built around an LLM is that the
one
 thing you can guarantee is that no two people will have a consistent experience, nor is there ever going to be a 100% freedom-from-error. That makes it very hard to predict and therefore market what or how people will learn.

I think this company will end up pivoting into a B2B context before long. Hopefully they will still stick to the mission, but who knows (and I wouldn't fault them if they don't – survival comes first).

reply

jamager

5 hours ago

 |
root
 |
parent
 |
next

[–]

> nor is there ever going to be a 100% freedom-from-error

That is not a problem. Language is messy, you don't need 100% accuracy to learn. The problem is that LLM errors are fundamentally different from human errors, and you won't even know how to recognize them.Your interlocutors can work around human errors, because they tend to follow the same patterns in same language. But they will freak out with LLM errors.

reply

itake

20 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

The trend I've seen in these AI tech companies is they launch their MVP using base models (or in this case fine tuning gpt4). This gives them enough traction for a seed round, but 2+ years later, they don't have the talent to actually improve the product beyond this.

If OpenAI puts resources to language learning, they could build a great product. But 3rd party devs relying on someone's tech hasn't proven to be a good strategy.

reply

vunderba

22 hours ago

 |
prev
 |
next

[–]

The ChatGPT mobile app in hands-free voice conversation mode works quite well for language practice with one important call-out: you have to give it a topic at the beginning otherwise it won't be able to drive the conversation forward and will stick to banal pleasantries.

What I usually do is pick a random blurb in the news and paste the entire thing along with the Reuters link at the beginning and inform ChatGPT that we'll be carrying on language practice specifically over that topic of discussion.I've used this to carry an hour long foreign language practice in Spanish while walking my husky. Just put the phone in my pocket and go. If you're an intermediate/advanced learner, it's a pretty decent solution.In fact, you can actually instruct ChatGPT that you are going to speak in your native language, but ChatGPT is only allowed to respond in the target language if you just want to focus on practicing listening comprehension.I'd be interested in hearing how significantly improved Issen is over this.

reply

mariano54

21 hours ago

 |
parent
 |
next

[–]

Yeah, agreed, we started with a similar observation. These voice models are getting better quickly.

You do need an app to create a holistic learning experience just for language learning. Customized curriculum, tons of prompting, AI models chosen for transcription accuracy, flashcards/dictionary, etc.We also support hands free mode, and many other things are customizable like slang, speaking speed, target language usage, etc.

reply

dbuxton

19 hours ago

 |
prev
 |
next

[–]

For me this is great for practice (I tried Russian). However the big missing piece for all these language learning apps is the lack of support for spotting and correcting errors in your pronunciation - as long as you say the word more or less right, the transcription gives you a pass.

I am very excited for the whole STT/TTS to go away and for us to have models that really "hear" exactly what you said.Sometimes this is about accent but a lot of the time, the AI won't spot areas where you e.g. fudge a case ending or the stress on a word. Yes, you can get some of that pronunciation right by the AI repeating back with the correct stress or clear case, but you never really get the confidence that you would get from an actual human.Another product suggestion - turn off transcription (at least for the tutor side of the conversation; I'd suggest both). Personally I find it distracting at best for languages I already speak well and a crutch for those I don't.Finally, I find it really very hard to enjoy having a random conversation that's not very directed ("What interests you most about artificial intelligence?"). I'd suggest that there are ways of making it more goal focused without being explicitly gamified - maybe something like, here's a position and you have to persuade me (AI debate club!), or something that brings out an actual opinion or relates to a concrete experience ("what's your main goal in your job this year").Overall though this is the first product I've seen in this space that I might actually use, so well done.

reply

mariano54

18 hours ago

 |
parent
 |
next

[–]

The persuasion lesson sounds like a great idea, we haven't thought of that. Yeah voice to voice models will be amazing. There is significant progress from openai/gemini, and we plan to use them when they are ready.

reply

0bi1A4xvXtQCO

1 hour ago

 |
prev
 |
next

[–]

I created an account just to provide feedback. I would consider myself the core audiance and would be definitly be willing to pay for it. I am learning Japanese with, but, since I am living outside of Japan, struggle to find good opportunities to output on a regular basis.
An AI-based language tutor would make my life much easier.

A few comments from the 20min trial I had:- About the positive aspects: There were definitly parts of the conversation where I was genuinely suprised with the naturalness. Overall, I felt that the demo already helped me practice my output a bit. From this, I definitely believe that AI-based language tutors might become quite widespread soon as they could becomereallygood language exchange partners. In my case, I still have low speaking skills (~Japanese N4, A2), so just having any chance to practice verb conjugations etc is already immensily helpful.- I also like that there is no gamification aspect. I prefer apps where users can decide how they use them. A lot of Japanese learners, people already use anki for vocab, etc., so forcing extra vocab practice would me definitly quit the app.Some feedback for improvement:- Due to my still low speaking skills, I often need mid-sentence pauses which are at least 1-2 seconds long. When I pause, the sentence is already half-transcribed, sometimes in another language. I think I had moments where then the sentence is cut-off entirely. At least, it makes me pressured to finish the sentence in a fluent manner without much pauses.- I know you want to have multilingual transriptions, but maybe you could add some language bias in transcribing the speech?- About the cutting off: If you have some sort of VAD frontend: Maybe you could adjust its parameters based on estimated language skills of the users (beginners have longer pauses)- I saw that my sentences were rated. But they were rated only in text, even though I said that my mistakes should be corrected right away (The speech-based AI partner just kept on talking about the topics). Maybe I have overlooked something, but is there some overview of my mistakes besides the text-based corrections?

reply

mariano54

52 minutes ago

 |
parent
 |
next

[–]

Thanks for the feedback.

1. The response latency / patience can be configured in the quick settings (tap the gear during the call).2. There already is a bias in transcription. It's something we're actively improving, multilingual transcription isn't a solved problem yet3. It is supposed to correct you actively if you have corrections enabled (check the settings). But we received feedback that it's not enough, so we will ramp it up soon

reply

TuringNYC

18 hours ago

 |
prev
 |
next

[–]

Congrats on your app and love it so far! Already sent it to over a dozen family members. Curious about a couple of things

- I see only two employees on LinkedIn -- how were you able to QA all these different languages with just two people?!- I tried Urdu and the app did quite well. But curious why you have two female voices and not any male voice?- I realize Sesame is a much bigger team, but curious what you think they are doing that makes their voices feel so real and seamless. I dont think they do multiple languages so I think you have a harder problem of course.

reply

mariano54

18 hours ago

 |
parent
 |
next

[–]

Thank you so much for that!

We focused on testing and tweaking the most popular ones, we have not tested some of the niche ones. We have removed languages that users have told us have major issues, but there are still some left.The voices are due to the quality of the TTS services that we use. Openi, 11labs, minimax. Some services don't have many or even 1 good voice. We will add more over timeSesame also passes in the users voice into the TTS model so that it can vibe well with the users tone and mood, whereas we are just using raw TTS. Their latency is also very low, but this is not quite suitable for language learning.In the future we hope to move to full voice to voice models, once those become mature and intelligent enough.

reply

leonidasv

20 hours ago

 |
prev
 |
next

[–]

Question: ChatGPT voice mode seems to have too much tolerance for mispronouncing. Sometimes, it understands you even you mispronounce something in a phrase, and it's not aware enough to correct you - it even says your pronunciation is correct if asked. It's good at grammar, though.

It makes me think the audio goes through a kind of voice-to-text model before the answer, so nuance is lost; or the model wasn't trained to distinguish between correct and incorrect pronunciations.Does Issen have this issue too? Pronunciation vices are common when you're learning a new language.

reply

konovalov-nk

20 hours ago

 |
parent
 |
next

[–]

In general there aren't really models that can understand nuances of your speech yet. Gemini 2.5 voice mode changed that only recently and I think it can understand emotions but I'm not sure if it can detect things like accent and mispronouncing. The problem is data, we need a large corpus of data labeled how exactly the audio sample is mispronouncing the word, so the model can cluster those. Maybe self-learning techniques without human feedback can do it somehow. Other than that I'm not seeing how this is even possible to train such model with what's currently available.

reply

mariano54

20 hours ago

 |
parent
 |
prev
 |
next

[–]

Yes we do have this issue, but it's improved a bit over chatgpt due to using multiple transcribers.

The models are improving though, and they are at a very good place for English at the moment. I expect by next year we will switch over to full voice to voice models.

reply

harles

20 hours ago

 |
root
 |
parent
 |
next

[–]

This reply seems to miss the question, or at least doesn’t answer it clearly. Is this service overly tolerant of mispronunciations? Foundational models are becoming more tolerant, not less, over time which is the opposite of what I’d want in this case.

reply

mariano54

20 hours ago

 |
root
 |
parent
 |
next

[–]

It's less tolerant of mispronunciations. There is custom promting to explicitly leave in mistakes and to not fix them. It's still not perfect and it (the speech to text module) sometimes corrects the user's pronunciation mistakes.

reply

BrandiATMuhkuh

16 hours ago

 |
prev
 |
next

[–]

Congratulations on the launch.

I wish you great success.Focusing on speaking first, and not writing makes so much sense. As a father I could first hand experience how my child learned 3 languages (German, English, Arabic) without reading/writing first.The hardest part for you will likely be the "curriculum". It's "easy" to make something that works for a couple of weeks. But language learning takes years.Btw, if you are up for it, I would enjoy chatting with you. -> I co-founded an AI math tutoring company, and focused my PhD on how to influence human language with AI. Hint: Social connections between humans and AI.What you are trying to solve is something I dreamed about for years.

reply

mtalantikite

23 hours ago

 |
prev
 |
next

[–]

This looks great, congrats! As someone that has gone through Assimil courses and done lots of comprehensible input for various languages, language production is typically the weak point that isn't covered well. I've done plenty of lessons on iTalki, but I've been wanting something more structured and this seems like it could cover it. Definitely going to give it a shot!

The feature request I make for all language course makers: please consider Bengali support in the future! It's wild to me that the 7th most spoken language in the world, with a deep culture around literature and poetry [1], gets zero attention from language course makers. I can buy an Assimil course on Breton, spoken by 200k people, and not Bangla, spoken by 284 million.[1]https://en.wikipedia.org/wiki/Charyapada

reply

xmodem

16 hours ago

 |
prev
 |
next

[–]

I’m at a roughly A2 - B1 level at the language I’m learning and I picked up a whole lot of pretty basic grammar errors in the first conversation.

The app also used a bunch of constructions I’m not familiar with even though I specified I’m a beginner.If I hired a human tutor and had this experience, I would ask for my money back.

reply

mariano54

16 hours ago

 |
parent
 |
next

[–]

I'm sorry about that. May I ask what language you tried?

reply

xmodem

16 hours ago

 |
root
 |
parent
 |
next

[–]

Swedish

reply

clbrmbr

21 hours ago

 |
prev
 |
next

[–]

Nice! I’ve wanted this for years.

Suggestion: you may be able to integrate SRS into the conversation. —- you could encourage the model to use certain words, and more importantly you can track the student’s active use of words that are on the review list, basically acting as if it were an SRS step. — this could totally eliminate the need for flashcards.

reply

mariano54

21 hours ago

 |
parent
 |
next

[–]

Yeah this is a really great idea, perhaps you can sample tokens based on some kind of SRS and I+1 sentence system. Kind of like a graded reader but for speaking. Will definitely look into this in the future

reply

shazron

10 hours ago

 |
prev
 |
next

[–]

The beginner experience (like others mentioned) is not there, at all. It's as if I was dropped into a foreign country, and forced to talk. Sure, I'm going to flail around, and maybe get frustrated, and maybe with some hand gestures get my point across in real life.

But this is not real life - I tried to "flag" the tutor with sentences that I don't understand, and I am way over my head, and it just chugs along, with long sentences, totally unaware.The service should not advertise itself as having a beginner level at all, in my opinion.

reply

999900000999

22 hours ago

 |
prev
 |
next

[–]

It would probably be better to pick one or two languages, actually work with native speakers to make sure it's right.

These "we cover every single language" tools get it like 75% right at best.

reply

55555

21 hours ago

 |
parent
 |
next

[–]

I disagree because of how AI is progressing and because there's tons of neglected language markets they can pick up. Obviously your approach can work too, perhaps better. But 95% of language learning tools don't support Thai (my target language) for example so I am an eager user for that reason alone. I think they'll be able to make a generalized curriculum and have the AI use it in all languages.

reply

adastra22

18 hours ago

 |
root
 |
parent
 |
next

[–]

Most of the generalized curriculum stuff out there is crap because languages differ from each other in substantial ways. LLMs in principle should help here as they can use their knowledge of the structure of the language to modify, but we're just not there with context windows and thinking capabilities. They will need at least a per-language (ideally per language pair) system prompt that contains a rough outline of the curriculum.

reply

55555

8 hours ago

 |
root
 |
parent
 |
next

[–]

I think the curriculum areas you're referring to are for learners in the beginning and intermediate stages. In which case, fair enough, although I still think you could get pretty far by just prompting an LLM, as the LLM has read hundreds of books teaching how to learn each language. But that's not really my point; my point is that once you're an advanced learner (they claim this is their target market) who knows about 12,000 words, I think you know almost all of the grammar, and the remaining bits will get picked up along the way effortlessly via immersion. What you need help with in this stage is slogging through the next 10,000 vocab words you need to learn to get to extreme fluency or the next 25,000 you need to learn to become plausibly native-level, as well as the speaking and reading practice to make your reading faster (if it's a different character set to your native language) and make your speaking effortless.

reply

adastra22

7 hours ago

 |
root
 |
parent
 |
next

[–]

At that point why engage with an LLM? Just go read a book.

reply

55555

6 hours ago

 |
root
 |
parent
 |
next

[–]

Probably too long of an answer, but: averaged out over the months, I spend 30 minutes every weekday doing flashcards, 45 minutes with a tutor, and spend another 1.25 hours watching TV or reading books in my target language. With 2.5 hours every weekday on average and without life immersion (at your home or office) it's possible to get to reading/writing/speaking/understanding fluency (including in terms of speed) in a difficult language in about 3-4 years and near-native in another 2 years. It's very difficult as an English native to learn a language like Chinese, Japanese, or Thai. It's not like learning Spanish or French (which I have also studied). To answer your question directly, surprisingly, reading a book does very little to help your speaking or understanding abilities. The skills of understanding accents/pronunciations quickly enough and the skill of structuring sentences when speaking quickly enough are completely different skills. Writing/reading/speaking/understanding are four remarkably unrelated skills that must be trained separately. Actually, typing on a keyboard and writing by hand are also different. Because thai actually has a different keyboard on desktop vs phone, since it became good enough, I decided to simply use speech to text for the rest of my life. I'm remarkably fluent in comprehension and have read quite a few adult books and yet if you give me a pencil and paper my brain can't figure out how to spell a word that I can easily say or type. And why use an LLM instead of a tutor? To save $2,700 a year.

reply

999900000999

21 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Would you rather have a tool that teaches you accurate conversational Spanish ?

Or something that tries to teach 60 languages but does so poorly ?

reply

Alex-Programs

21 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

My tool supports Thai, if you'd like to try it -
https://nuenki.app
 . I added it at the request of a user, who seems to be happy with it.

It's a browser extension that finds English sentences in webpages, and translates the ones at your difficulty level into the language you're learning.

reply

55555

8 hours ago

 |
root
 |
parent
 |
next

[–]

Thank you, I will try it, although I'd prefer to translate entire sentences into Thai randomly. Perhaps you can add this advanced mode. Actually, I saw your app before while looking for an alternative to Toucan that supported Thai, but at that point in time you hadn't added support yet. Thanks for doing so.

reply

55555

6 hours ago

 |
root
 |
parent
 |
next

[–]

Okay I installed it and this is pretty great. Although I think your extension doesn't work for Thai the way you think it does. Because there's spaces between sentences instead of between words in Thai, it's translating entire sentences even with the "words only" setting enabled. This is what I want anyways, but will be too difficult for most learners. I have written misc Thai learning softwares and just so you know you should use an LLM to do word-splitting, not a software library. If you do use a library, you need to split words while looking for the largest possible word, but it won't work well. Basically you can't tell without a brain whether it's a lot of small words next to one another or a smaller number of compound words. IME only an LLM or a human will do a good job of this.

reply

Alex-Programs

3 hours ago

 |
root
 |
parent
 |
next

[–]

Translating entire sentences is the idea - I'm not sure what setting you mean with "words only"? I really ought to make the settings clearer, but it's hard to do when you know what they "ought" to express.

"Translate Isolated Words"allowsit to translate "sentences" of only one word, but it doesn't disable full sentences.And yeah, atm it word splits by spaces for the dictionary. I hadn't thought to do it with LLMs, though that's a good idea. There's a somewhat related problem when doing Furigana, where it has a hashmap of strings-to-pronunciations, and it starts with a 4-character sliding window looking for matches, then a 3 character, etc.

reply

adastra22

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

That's a pretty sick idea. Unfortunately I presume it involves sending your browsing data (e.g. page contents) to the server?

reply

Alex-Programs

16 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, though I've added lots of privacy protections to at least partially mitigate that:

- There's a global blacklist of sites, as well as phrases in the title/URL (e.g. "bank")- You can blacklist sites yourself- Each sentence is run against filters checking for medical/legal/etc info, as well as checks for addresses, card/social security numbers, etc. All the checks are done client side- There are also some special implementations, e.g. it looks at the source code of websites to work out if they're an instance of an American health portal that I've forgotten the name of - each doctor's surgery self-hosts it.- Websites can add `nuenki-ignore=true` on their end, if they'd like to disable it.And of course it doesn't log anything, though there is an anonymous cache in order to make it economical.

reply

adastra22

14 hours ago

 |
root
 |
parent
 |
next

[–]

What about a whitelist? I might just be interested in only having certain sites, like this one or Reddit, translated into my target language. That way I can be certain it is only turned on for sites that I am OK with sharing browsing history and not be concerned that I might have missed adding something to the blacklist.

reply

Alex-Programs

3 hours ago

 |
root
 |
parent
 |
next

[–]

That's a good point. At some point I ought to make a UBlock-origin style list of customisable rules.

At the moment I'm focused on translation quality, but I intend to add that.

reply

adastra22

32 minutes ago

 |
root
 |
parent
 |
next

[–]

Thanks!

reply

55555

8 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

This is a great idea. Specifically, I want this enabled when I'm wasting time but not when I'm working. So I'd like it to be enabled only on X.com. This whitelist+blocklist functionality could be a user-side setting like with Adblockers.

reply

psychoslave

9 hours ago

 |
prev
 |
next

[–]

Looks like a really great job, congratulations.

I'll try to give it a chance later today if I can find some room for it.My main fear of anticipated deception is that it won't give me feedback on how out of the track my pronunciation can be deemed and lake tips on how to give a nicer moment to a native listening to me. That's really the thing I would like to be able to experiment more than anything else regarding foreign language acquisition. And giving IPA transcription of expected CS actual and possibly some links to video explaining each phonem that went wrong would be top notch.Regarding engagement, after having try a bunch of online things, to my mind the best formula is to give insights on cultural and social matter: what are the regions of the country¹ and their specificities, what people love as food, drink, music, dance, literature, what have been the historical struggle of the linguistic community, who are the people prised in this community? Well at least for my profile it drives more interest than anything else.¹ languages are not one to one bound to a single specific country of course, but you get the idea.

reply

dataviz1000

23 hours ago

 |
prev
 |
next

[–]

Luis von Ahn spoke in the early 2010s—probably around 2014—at The LAB in Wynwood, Miami. He recounted how his fascination with crowd-sourcing led first to reCAPTCHA and then to his latest venture, Duolingo. He made it clear that his real passion wasn’t language per se, but building a crowd-sourced human translation service as a business model. At that point, Duolingo had roughly 24 employees—and, much to his surprise, only two were focused on the crowd-sourcing engine. He explained how they’d enlisted some of the world’s leading language-education researchers as consultants. Their very first question: “Which part of speech should learners tackle first?” The experts confessed they didn’t know, so the team gathered the data and used A/B testing coupled with statistical analysis to pinpoint the answer.

Today, it’s not only easier than ever to launch a platform to challenge Duolingo, but its core product—its crowd-sourced human translation service—has been distrupted.This morning, I found myself thinking about how all those decade-old learning platforms—like Coursera, as reflected in its ever-falling stock price—are being distrupted.Your product looks awesome and I hope you distrupt all the language learning platforms. Thank you for sharing.(I had ChatGPT fix my grammatical errors and now this comment doesn't sound like me, sorry.)

reply

b3orn

20 hours ago

 |
parent
 |
next

[–]

> (I had ChatGPT fix my grammatical errors and now this comment doesn't sound like me, sorry.)

And it didn't correct "distrupted" to disrupted?

reply

dataviz1000

18 hours ago

 |
root
 |
parent
 |
next

[–]

Nope

https://imgur.com/a/m3svUky

reply

thaumasiotes

17 hours ago

 |
root
 |
parent
 |
next

[–]

>
https://imgur.com/a/m3svUky

That's an image of text. Is it supposed to provide more evidentiary value than the word "Nope" above it would by itself?I'll bet you I can show you a screenshot where "ChatGPT" says whatever your heart desires.

reply

dataviz1000

14 hours ago

 |
root
 |
parent
 |
next

[–]

I started using o3 yesterday. Turns out it has sycophancy behavior. That is good to know. Regardless, I'm beginning to enjoy my errors because it reminds me of my humanity.

reply

brcmthrowaway

20 hours ago

 |
parent
 |
prev
 |
next

[–]

Coursera is failing because its platforms are infested with Big tech cert slop.

And mid 2010s view was MOOCs were supposed to disrupt University education!Add it to the pile.

reply

famahar

5 hours ago

 |
prev
 |
next

[–]

This looks similar to Speak. I took part in their Japanese language beta and enjoyed it. It's an interesting use of AI and I did learn a lot fast. My biggest problem with these are that they feel like magic until it suddenly doesn't. Weird pronunciation and strange replies. It comes nowhere close to replacing a tutor or speaking partner yet. I am optimistic as the tech improves fast.

reply

johncole

23 hours ago

 |
prev
 |
next

[–]

I appreciate your comment about gamification. I’ve kept a streak alive on other apps for no other reason than keeping a streak alive. Not learning a thing.

reply

antonaf

22 hours ago

 |
parent
 |
next

[–]

Yeah, this is the biggest gripe we hear about much of the existing language learning landscape. That they're effectively gaming apps masked as language learning apps.

reply

55555

21 hours ago

 |
root
 |
parent
 |
next

[–]

You should still gamify it. Gamification is orthogonal to whether the tool actually works and positively correlated with whether the user actually uses it.

reply

Velorivox

20 hours ago

 |
root
 |
parent
 |
next

[–]

I would argue that games are a great analogue to language learning as well. Contrary to our ideals, people do like to enjoy themselves and are more likely to pick an activity they enjoy than one they don't. Games and puzzles are able to present frustration as enjoyment (provided there is appropriate reward and perceived growth) making them great tools for learning.

However, gamification can only do so much and I'm afraid language learning is a lot like learning to code: many people want to want it but few actually want it. In that case, presenting as a "want it" when you are a "want to want it" is social proof and largely unrelated to whether you are actually learning (as long as the pretense is kept up) — hence the success of Duolingo despite the relatively poor real-world outcomes. In Duolingo's case the streaks are even explicitly considered to be social proof.

reply

ianbicking

16 hours ago

 |
prev
 |
next

[–]

I've been thinking and playing slightly with this concept myself. A few thoughts:

1. Using a standard transcription service is pretty tricky because it's going to correct the user's speech. Or make it incorrect! Standard transcription is predicated on the speaker saying things correctly.2. I've tried sending the audio directly to OpenAI to address this issue. I can't say if it works or not. It's very hard to test or understand a system without a transcript as a source of truth!3. I'd like to learn a new language as a beginner, and all of these AI systems work poorly for this. It's great to immerse the learner in the language, but if you know NOTHING then it's not that helpful.4. Language learning needs to be MUCH more multimodal than a standard chat. Especially as a beginner.5. The AI should be generating translations and explanations alongside its responses. I'd like to be able to inspect everything the AI says (in the language I'm learning) to understand it.6. Emoji would be another easy way to annotate the text.7. I think giving the user/AI a subject to talk about would be helpful. Again, a subject that is not language-based would be great, like an image or something.8. As a very new learner I would like an experience where I respond in my native language and then I'm told how to translate this to the language I'm learning. This should include a pronunciation guide. Then I should repeat the phrase I'm given.9. I should still be able to ask questions in my native language and probably get a response in my native language. But with some prompting the AI should be able to distinguish these two cases.10. For low latency it's nice if you produce the spoken text quickly, but you still have the opportunity to get the LLM to produce _more_ material immediately after. This is where things like translations can be produced.11. You probably don't have timestamps on your TTS, but if you did and could highlight words as they were spoken that would be _great_. Probably worth choosing a TTS provider with that in mind.

reply

AndyKelley

19 hours ago

 |
prev
 |
next

[–]

It's very cool, I'm enjoying playing with it.

Feedback: The tutor pronounces some obvious things wrong that contradicts the words. Two examples: 気滅の刃 - it pronounced 刃 wrong despite the furigana being correct. It also kept pronouncing は as "ha" even when used as topic particle in more complex sentences. Edit: also observed 使い方 pronounced "saifou" - no idea what's going on there. It was in a mixed english-japanese message.I think I would pay for this if I wasn't worried about learning mispronunciations or errors.Oh, more feedback: focus the app on the conversation with the tutor and leave the memorization to Anki - just let us export those words we struggle with to CSV or something so we can import into existing vocab workflows.

reply

mariano54

18 hours ago

 |
parent
 |
next

[–]

May I ask which tutor you were using? The TTSs have different strengths and weaknesses.

Good idea on the export, will add that to our to-do list.

reply

AndyKelley

18 hours ago

 |
root
 |
parent
 |
next

[–]

Aoi (it was 1st in the list)

reply

accidentalrebel

22 hours ago

 |
prev
 |
next

[–]

Thank you for sharing this.

I've been learning Arabic, and I noticed that the app uses Arabic script right from the start. This can be quite challenging for beginners who haven't learned how to read it yet. May I suggest adding an Englishized (romanized) version of the Arabic text to help ease the learning curve?It also seems to not listen to me when I asked to give me shorter sentences. It seems to not care that I'm struggling despite my pleading.I later switched to Spanish, which was a better experience. This one seems to listen to me better. I can ask the tutor to repeat what they said in English and give me shorter sentences, and thankfully, it does.Interacting with the tutors does feel I have to drive the conversation which is taxing. Compared to a human tutor, where I feel assured that I can be guided properly.Still an interesting app. Would love to try Spanish some more, in the future.

reply

runarberg

20 hours ago

 |
parent
 |
next

[–]

A Japanese learner here (not commenting on this platform). I do recommend start using your target language script as soon as possible, maybe even earlier. The only exception are ideograms where you have to learn like 2000 unique characters, and even then you should learn the most common ones and start using them immediately.

Reading in a non-familiar script becomes much easier the more you do it, and the longer you put off learning it, the more opportunities you miss for using it.I think you should only be using the latinized scripts in the absolute beginning where you are learning the most basic words and phrases like: “hello”, “yes”, and “no”, and “what is your name?”. This should only be for your first couple of weeks. After that you should have learned to read new words in the new script (albeit slowly). Learning the script makes everything much easier afterwards.

reply

Kosirich

3 hours ago

 |
prev
 |
next

[–]

Can it be used in a car? Is looking at the screen required?

reply

mariano54

3 hours ago

 |
parent
 |
next

[–]

The mobile app can be used in a car (not the Web app). Looking at the screen is not required.

reply

brilee

22 hours ago

 |
prev
 |
next

[–]

I'm a second-gen Korean-American; my korean is weak but conversational. I am intrigued by the reasoning model that analyzes my speech and points out various mistakes I'm making. It's a good first attempt at separating the 2 tracks of actual conversation vs mistake-correcting.

I think showing the raw reasoning text is not quite the right UI; maybe highlighting the specific text in red and showing a suggested correction would work better?It's also a little awkward that the conversation is live; I don't really have any breathing room to read the reasoning traces on what mistakes I made / could have done better. I hung up the first time I tried to figure out how to pause.

reply

mariano54

20 hours ago

 |
parent
 |
next

[–]

Thanks for the feedback. You might want to try manual mode, where you press enter or say "send" to trigger a response

reply

jlarks32

23 hours ago

 |
prev
 |
next

[–]

Yeah great work with this. Seems like a real opportunity given how hard Duolingo is dropping the ball.

reply

noleary

23 hours ago

 |
prev
 |
next

[–]

I can't wait to try this! I studied a few languages in school and have lost any semblance of proficiency -- mainly because I never have a real occasion to use anything other than English. I've been waiting for someone to build something like this

reply

visarga

9 hours ago

 |
prev
 |
next

[–]

I would exercise a new vocabulary by generating many different phrases based on a limited number of known words, like the Pimsleur method. This teaches words in context, not isolated.

reply

lawrencechen

23 hours ago

 |
prev
 |
next

[–]

Congrats on the launch!

I tried the Japanese track. I'm a total beginner and the first lesson wasn't helpful at all. The AI asked about maybe mixing up Japanese<>English, but it didn't actually follow through. It either spoke fully in Japanese or fully in English. Maybe this is a standard practice for language lessons? I remember going to the first day of French class in a community college, and the teacher only spoke French, which was extremely overwhelming. Perhaps it's the standard way of teaching? Even if it is, I'm not sure if it works when compressed down to the shorter times I see myself opening the app.

reply

dgs_sgd

19 hours ago

 |
prev
 |
next

[–]

I learned Spanish to an advanced level (B2) many years ago with a combo of Duolingo, Anki flashcards, and real tutors. One of my biggest regrets is focusing too much on the grammar and vocabulary and not enough on having conversations with natives. I'm convinced it would have taken me half the time to reach B2 if I had focused more on conversations. I think this app is going to be really effective. Congrats to you guys on the launch!

reply

kwkrass

8 hours ago

 |
prev
 |
next

[–]

Well done! I have built a side project in the same space given that i wanted to learn Spanish (my wife is Colombian) and also wasnt happy with existing offerings. I have used the OpenAI realtime API to fully focus on audio conversations. You can check it out (for free) here:
http://lucas.alldone.app/

reply

deanc

21 hours ago

 |
prev
 |
next

[–]

I built a basic version of this for myself with a prompt in chat gpt in an afternoon. It's great that you've built this yourself, but where's the magic? If it's your prompt it can probably be extracted in a few minutes by those who know how to do so.

reply

M4R5H4LL

21 hours ago

 |
parent
 |
next

[–]

Why not finish, publish it to the store and get income if it was that straightforward? There's a long way to go between a toy application to demonstrate a product, and something on shelves actually selling. In other words, you can most often quickly tackle the concept or trivial parts of an app, but it's much harder to get a real product out, even if the implementation looks straightforward on surface.

reply

deadbabe

20 hours ago

 |
root
 |
parent
 |
next

[–]

This is like the story of the businessman and the fisherman.

Why on earth are you going to build out a whole product: doing marketing, security, incorporation, customer support, etc… just so you can finally arrive at the end result of… teaching yourself a language?The toy app is 100% of the value. You don’t need all that other shit, you just need a really good prompt. It’s exactly how you don’t need to search websites anymore, just ask AI for the answer and get it immediately. You don’t need a full app, just ask AI exactly what you want.

reply

owebmaster

18 hours ago

 |
root
 |
parent
 |
next

[–]

you think a chat UI is the apex UX? Most of us don't agree with that. On top of that, ChatGPT, Claude, Gemini apps all sucks.

reply

deadbabe

16 hours ago

 |
root
 |
parent
 |
next

[–]

You don’t get it, you can just tell an AI to build you a UI as some html page and use that.

reply

owebmaster

14 hours ago

 |
root
 |
parent
 |
next

[–]

I do get it and you don't get that AI just can't do UX better than humans, and probably will take many, many years to catch up, if they do. I dare to say that UX is probably one of the few things humans will always do better.

reply

deadbabe

13 hours ago

 |
root
 |
parent
 |
next

[–]

You’re still thinking about mass market UX.

A UX someone builds for themselves and makes sense to them is going to be way better than something a designer puts together for the masses. That’s the promise of AI, totally custom software down to the individual user level.

reply

owebmaster

13 hours ago

 |
root
 |
parent
 |
next

[–]

I will still bet that great apps with much better UX than your average vibecoder will still continue to make people rich.

reply

deadbabe

2 hours ago

 |
root
 |
parent
 |
next

[–]

UX won’t make you rich anymore in a world where people want their own custom versions of apps.

reply

deanc

21 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

That's exactly my point. This is at best a toy application driven by a prompt that many people will be able to extract and recreate. Putting the pieces together is easy and letting someone talk to an AI is not a particularly difficult problem. Creating magic and making people come back to learn the language is entirely different and I don't see anything magical here.

reply

owebmaster

18 hours ago

 |
root
 |
parent
 |
next

[–]

> Putting the pieces together is easy and letting someone talk to an AI is not a particularly difficult problem

Exactly! Not difficult, right? Making and selling a product out of it is called marketing. It is not rocket science, but many engineers can't grasp it.GPT Wrappers are the new CRUD. There is no innovation in Trello, Jira and any other SaaS, they are just marketed products that thousands of people here in HN could code better, but they don't, because they are wasting their time pointing that other people's products are not a difficult problem to solve.

reply

TypingOutBugs

8 hours ago

 |
root
 |
parent
 |
next

[–]

Be honest though, what’s the difference between this and a good system prompt in Claude to be a language tutor?

I worked for an Edtech startup before that had a novel approach to mastery (as opposed to Anki) and it’s not something you can put in a prompt.

reply

vimy

16 hours ago

 |
parent
 |
prev
 |
next

[–]

> We wanted something that would talk with us — realistically, in full conversations — and actually help us improve. So we built it ourselves. The app relies on a custom voice AI pipeline combining STT (speech-to-text), TTS (text-to-speech), LLMs, long term memory, interruptions, turn-taking, etc. Getting speech-to-text to work well for learners was one of the hardest parts — especially with accents, multi-lingual sentences, and noisy environments. We now combine Gemini Flash, Whisper, Scribe, and GPT-4o-transcribe to minimize errors and keep the conversation flowing.

Your prompt can't do this. I know because I've been trying to build something similar and a prompt just isn't enough. You need multiple LLMs and custom code working together to achieve realistic conversations.

reply

haiku2077

20 hours ago

 |
parent
 |
prev
 |
next

[2 more]

[flagged]
deanc

19 hours ago

 |
root
 |
parent
 |
next

[–]

I knew this would be a reply. Dropbox was magical and just worked and took a huge amount of pain points away from a complicated protocol. Building an LLM wrapper doesn't make a product in 2025.

reply

chrischen

23 hours ago

 |
prev
 |
next

[–]

Speaking of translation with LLMs I've been looking for a solution to quickly open a bi-directional translation context without having to prompt ChatGPT or any other LLM every time. iOS lets you set the action button to use the default translation app quickly, but the translation it provides is vastly inferior to LLMs.

Even some basic app that can pre-load the prompt doesn't seem to exist?

reply

Brajeshwar

23 hours ago

 |
prev
 |
next

[–]

I tried the Web Version. Started, then tried to create an account, but it kept looping, informing me that my email address does not exist in your system. Well, the “Create New Account” got kicked off and gets me in a loop of “Do not Exist”. I just went through the whole process again, and I'm back to the beginning.

I’m going to assume this works better on the App.

reply

antonaf

22 hours ago

 |
parent
 |
next

[–]

Unclear what issue you hit, we'll look into it. Thanks for sharing.

reply

Brajeshwar

14 hours ago

 |
root
 |
parent
 |
next

[–]

Played around > tried creating an account > says email not in system > can neither create nor sign in. So, I don't have an account even if I wanted to create one.

reply

raymondgh

21 hours ago

 |
prev
 |
next

[–]

Thanks for sharing! I tried using it for Thai language coming from English and found that the app understands me well! But I couldn’t understand it at all. It replied to my turns with very long messages (20+ syllables) in pure Thai and spoke with an unnatural rhythm which made it hard to pick out words or phrases. The foreign alphabet made it really difficult too. I tried changing some settings in the bottom left menu and it started speaking English to me too, but I found it unbearably slow. At one point it asked me if I wanted it to speak in pure Thai or a mix and then ignored my answer. Ultimately as a beginner I don’t think Issen will work for me very well as-is. Happy to check back in the future!

reply

lennertjansen

6 hours ago

 |
prev
 |
next

[–]

this is the future of language learning. love that you guys are working on this. gonna try it out for Indonesian this weekend :)

reply

I_am_tiberius

23 hours ago

 |
prev
 |
next

[–]

Do you store conversations? And what's the general privacy philosophy behind the app?

reply

mariano54

23 hours ago

 |
parent
 |
next

[–]

We store the messages, but not the audio. We also store session summaries and a "user facts" summary that gets regenerated after every session, based on all session summaries, everything in our AWS DB.

You can delete your account at any time to fully wipe all your data, but there is no way to delete sessions ATM.

reply

juandsc

2 hours ago

 |
prev
 |
next

[–]

I really like the idea and I'm a potential customer, but I don't think this is ready yet. I've been learning Chinese for a while and decided to give this a shot and at my level (somewhere between HSK 2 and 3) it's very frustrating:

When I babble (as someone at my level does) and say "eh... a bit of sentence eh... a bit more of sentence" half the times it cuts me off in the first eh... or the second one. This is extremely frustrating, in fact I didn't even finish the free 20 minutes trial because of this.Another issue is that like all LLMs it's bad at maintaining context of a conversation. I tried speaking about cars with it, as it's a topic I like so I thought it'd be cool and all of a sudden it's asking me what's my favourite ice cream. Don't get me wrong, I'm 100% certain I said something about ice cream but any human would understand I didn't want to say that.Also I tried it with Spanish as I'm a native speaker. The speech recognition is bad, I don't know what sort of processing this does but it has a lot of mistakes, however it's very rare that chatGPT ever fails to transcript. I'd say well over 20% of sentences were misunderstood.The idea is cool, but I wouldn't recommend this to anyone who wants to learn Spanish.

reply

serjester

22 hours ago

 |
prev
 |
next

[–]

Cool stuff! Probably one of the less popular languages, but I noticed that the transcription with Russian is often quite poor.

Part of me loves this—no judgement, endless convenience, cheap. But another part mourns, sensing it strips away the grit, the stumbles, the soul of language learning. The kind that only comes from fumbling through conversations with another human.When I was learning Spanish, I used italki extensively and found having a live Columbian tutor invaluable and very affordable for most Westerners. It would genuinely make me sad if those excellent tutors start losing work to this kind of AI.

reply

jasonthorsness

23 hours ago

 |
prev
 |
next

[–]

Can't wait to try it; my kids need to learn French in school and I've been trying to keep up with them with Duolingo; but something is missing there.

For me a key feature will be a family plan; Duolingo is great in that regard.

reply

zygy

20 hours ago

 |
prev
 |
next

[–]

Glad you're working on this. Duolingo is garbage and I've been hopeful that AI can help accelerate language learning in a way that is actually effective.

reply

swairshah

22 hours ago

 |
prev
 |
next

[–]

Just used it for French right now. The Design is excellent! but the LLM task orientedness needs some work. The tutor needs to follow the curriculum well. This has the same issue that I have in my day job i.e. keeping the LLM on topic. Its not
strict
. i.e. after asking it to make sure to remind me to reply in french it very easily forgets to do so. Its not following a structured approach or even in casual conversation isn't correcting my mistakes unless I ask.

reply

cpursley

21 hours ago

 |
prev
 |
next

[–]

This is the language app I've always wanted to exist. Will try it out - really hoping it can create custom lessons for specific scenarios that I need to study for.

reply

mariano54

20 hours ago

 |
parent
 |
next

[–]

You should try re-generating a custom curriculum from the settings, and there you can prompt it to create specific lesson types.

reply

cpursley

16 hours ago

 |
root
 |
parent
 |
next

[–]

Which specific settings should I modify?

reply

TuringNYC

18 hours ago

 |
prev
 |
next

[–]

Also I noticed your app doesn't work without a network connection, so i'm assuming you're doing all the TTS and STT server-side. Curious how practical that is w/r/t latency? Any plans to doing it all on-phone?

(probably a more fringe request, but i'm asking because I do all my language learning on the commuter trains w/o a good connection.)

reply

mariano54

18 hours ago

 |
parent
 |
next

[–]

Exactly, it's all server side. There are no plans for this. The main issue I see with doing it in device is the LLM piece. Even with some large models like llama 4 maverick, the tutor just struggles to properly teach and understand the student, it's not viable IMO.

Intelligence is super key here, especially as the context size gets larger (due to memory) and intelligence degrades.Another major issue is TTS voice quality, but this seems to be improving a lot for small local models.EDIT: You're right, latency is also a big deal. You need to get each piece under a second, and the LLM part would be especially slow on mobile devices.

reply

0b01

20 hours ago

 |
prev
 |
next

[–]

Portuguese should have the flag of Brazil.

Don’t dim screen on iPhone during conversation.The tutor should terminate the lesson when its goals are achieved and do a warm handoff.Overall it’s quite good.

reply

55555

22 hours ago

 |
prev
 |
next

[–]

I'm glad someone is building this! I was using this in Thai. I expected it to be awful. But it's actually very good. I only used it for a few minutes but will try to use it more later. It's possibly good enough for me to stop paying my tutor. However, please use a different Text to Speech model because the current Thai one sounds robotic, like the old (current?) Google Translate. This seems like a great product.

reply

antonaf

22 hours ago

 |
parent
 |
next

[–]

Ok, thanks for the feedback. Who was your tutor for Thai, Supatra or Malee?

reply

55555

8 hours ago

 |
root
 |
parent
 |
next

[–]

I'm sure it was the bangkok one, which I believe is the former.

reply

xmodem

23 hours ago

 |
prev
 |
next

[–]

This actually looks pretty neat. How have you been able to achieve such broad language support so quickly?

How widely have you tested your supported languages on native-speakers and learners?

reply

mariano54

23 hours ago

 |
parent
 |
next

[–]

The STT and LLM support many languages out of the box. For TTS we use multiple providers based on their strengths and weaknesses (for example minimax is great for Chinese)

We've done a lot of testing on Spanish, English, Italian, Japanese, and French, but much less on the others and none at all for some of the niche ones.The language support is based on the intersection of the languages that have low word errors rates in the transcribers, as well as officially supported by LLM/TTS (like gpt4.1, eleven labs etc).We've seen the models' quality improve consistently over the last 6 months, in all languages we tested, and now the error rates are getting really low.

reply

xmodem

23 hours ago

 |
root
 |
parent
 |
next

[–]

Right - I think it would be appreciated by your users if you at the very least made it clear from the outset how well different languages are supported and what degree of testing you have done.

Certainly if your product were to mis-teach me important details, and I were to then find out that you had spent less time testing than I had spent learning, I would be quite angry.

reply

akshayKMR

23 hours ago

 |
prev
 |
next

[–]

Why not use the Gemini flash voice-api directly instead? Cost?
I ask because from the demo, the tutor's voice seems mechanical.
I've played with the gemini voice api and it's quite impressive for conversation with low latency, I'd say perfect for your use case. It even switches languages if I say "Okay, let's talk in $foo language".

The vocabulary tooling looks neat and well thought out.

reply

mariano54

23 hours ago

 |
parent
 |
next

[–]

Multiple reasons (which also apply to openAIs realtime API):
- it's less intelligent than the non voice apis
- intelligence degrades even further with lots of context
- more expensive
- latency is not a free lunch, it comes at the cost of more interruptions from the tutor, which is a really bad UX. We prefer to interrupt less and have higher latency

Also, we prefer the eleven labs voices, but there is definitely varying quality. I'm guessing later this year or next, the voice to voice models will become good enough, and we will switch over.

reply

guilhermesfc

23 hours ago

 |
prev
 |
next

[–]

Looks great. I have been looking for something like this

reply

tanushv

17 hours ago

 |
prev
 |
next

[–]

This might be the most obvious question regarding this, but how are you planning on competing with the entrenched competition for mindshare, namely Duolingo. This is probably technically superior, but from a user standpoint, it might not be so. Happy to be proven wrong

reply

AndyKelley

17 hours ago

 |
parent
 |
next

[–]

Every serious language learner already considers Duolingo to be trash. It's not real competition.

reply

mariano54

17 hours ago

 |
parent
 |
prev
 |
next

[–]

Our market is different - ISSEN is more focused on intermediate and advanced students, and especially those that are willing to use a more difficult app in order to learn faster.

Also, having the AI voice tutor as our main feature allows us to iterate quickly, and be well positioned for future improvements in AI models.As for marketing and GTM, we're in the super early stages, and there is definitely a lot of competition out there, it won't be easy.

reply

srameshc

23 hours ago

 |
prev
 |
next

[–]

I like this
https://labs.google/lll/en
 from Google

reply

fode

18 hours ago

 |
prev
 |
next

[–]

Ok, in over a decade on HN I've never commented on a product but this one is awesome! I just signed up!

I currently pay $99 a month to learn Spanish from a live tutor 30 mins a day, and this is far superior if you ask me.The element that stands out to me is that the AI Tutor is consistent and concise!

reply

anonu

19 hours ago

 |
prev
 |
next

[–]

The conversation flows nicely. Certainly nicely built.

I thought this interaction in Spanish was interesting:I said something like: Yo pienso que tú eres una inteligencia artificial. Es muy interesante.Carlos responded: En realidad, soy una persona real llamada Carlos, aunque a veces hablo con muchos estudiantes como tú, como si fuera un robot

reply

mariano54

19 hours ago

 |
parent
 |
next

[–]

Ouch it looks like all the personality promoting has made it confused about its identity.. thanks for pointing it out

reply

farai89

14 hours ago

 |
prev
 |
next

[–]

I have tried the app. I was previously using chatgpt only to learn Spanish. I have found the app to be a much better and flowy experience - will continue using and provide feedback.

reply

hahamaster

18 hours ago

 |
prev
 |
next

[–]

Tried it is Safari, frustrating, confusing, spent some time figuring it out and closed the tab. I didn't say anything but the app kept "recognizing" some random words and "answering" tutor's questions... looks like pre-alpha version.

reply

tmaly

21 hours ago

 |
prev
 |
next

[–]

I want to build some AI tutors at home to help my kids with some of their school subjects and interests. I help them with subjects I know, but for other subjects I often do not have enough background. What are you best tips/ideas/design patterns you learned when making this app?

reply

mariano54

21 hours ago

 |
parent
 |
next

[–]

Some random tips which could help you

- Don't go over 10k tokens in the prompts as the intelligence and memory degrades- Summarize sessions and save the summaries, potentially summarize the summaries as well- use VAPI or realtime api if you want to build fast. Building the full pipeline takes a while- try out different models and see how personality varies. Our favorite is gpt4.1 with temperature 1.- goal system. The promot should always contain the current goal, and the next goal. Evaluate goals with another LLM, and dynamically change the prompt

reply

heeton

23 hours ago

 |
prev
 |
next

[–]

I had a go and it failed at the first hurdle I’m afraid. It was hallucinating my responses and inserting phrases that I wasn’t saying.

The teacher kept switching into an American accent when I was trying to learn French and the responses were getting very slow bitty.Hopefully this is just an initial load of issues because the concept is great.

reply

shellfishgene

18 hours ago

 |
parent
 |
next

[–]

Yes, this is weird. I said something like "I want to learn Spanisch to go shopping" and it just added "That's great" to my sentence.

Also for the flash cards the audio that says the word starts at the same time with the audio for the example sentence.

reply

n0tbl0nd3

18 hours ago

 |
prev
 |
next

[–]

The website is a bit buggy (Safari). The session should start with a 'hi!' from the tutor ?? I got confused whether my mic was working, refreshed a couple of times until I prompted it myself.
I tried it in my native language, Romanian: the speech to text is bad for Romanian and I got a random non-Romanian word within the first 30 seconds of using it (I assume it was meant to say "hello!") and gave up.
For German, which I am learning: I agree with others it is too unstructured. Also the transcription for my speech was wrong, it didn't correct me on it and I got frustrated again.

reply

aizk

20 hours ago

 |
prev
 |
next

[–]

Nice! I'm curious if your software can pick up really subtle details - like for instance, pitch accent in Japanese (which is basically NEVER covered in a beginner level course) but is useful to just be aware of as a language learner.

reply

mariano54

20 hours ago

 |
parent
 |
next

[–]

Thanks!
No, it cannot do this yet, as it's using a pipeline of voice to text to voice. I think models are heading in that direction, and voice to voice models are getting better.

For pitch accent, shadowing is a great way to improve. You can pause and repeat the tutors messages for example, or read out the word when doing flashcard reviews (copying the flashcard audio).

reply

iandanforth

23 hours ago

 |
prev
 |
next

[–]

Which spaced repetition algorithm are you using? I recently learned that there is a much improved one that has been adopted by Anki. (
https://domenic.me/fsrs/
) Have you adopted that as well?

reply

rahimnathwani

22 hours ago

 |
parent
 |
next

[–]

Jarrett Ye, the creator of FSRS, is a big fan of Math Academy. He records some of his sessions and posts them to YouTube.

https://x.com/JarrettYe

reply

mariano54

22 hours ago

 |
parent
 |
prev
 |
next

[–]

Yes we're using FSRS

reply

gngoo

12 hours ago

 |
prev
 |
next

[–]

I tried it, but I got stuck. I am trying to learn this Language, and I know very little of it. So we are having a conversation, and I just get totally lost. Would be cool if it switches back to English and then actually teaches me what all the words and sentences mean. Now I just closed the app, and going back to my usual language learning curriculum - generally, I would uninstall the app. But now I might just try it again in a few weeks from now.

reply

logsr

9 hours ago

 |
prev
 |
next

[–]

Love this. I have been looking for an app that does this. Congrats on the launch.

reply

iNic

21 hours ago

 |
prev
 |
next

[–]

Very impressive, but still has the same problem that seemingly all voice modes that I have tried have which is that the Cantonese voice has a Mandarin accent, and sometimes just straight up uses Mandarin pronunciations.

reply

gwintrob

20 hours ago

 |
parent
 |
next

[–]

I have this complaint too! I was impressed that they included Cantonese but it's frustrating that I don't know when it's pronunciation/accent is off. Have you found any other tools that work well for learning Cantonese as an English speaker?

reply

iNic

19 hours ago

 |
root
 |
parent
 |
next

[–]

Sadly there isn't one perfect resource. I find Hambaanglaang kinda useful. The complete cantonese books are good. And I have just started making flash cards. But, I am still just a beginner so take it with a huge grain of salt!

reply

gwintrob

14 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks. I'll check that out. Glossika has some good sentences you can use as flashcards.

reply

andy_ppp

19 hours ago

 |
prev
 |
next

[–]

Hey! Can you add a feature that can record my lessons with a real human and then build a way for me to practice all the things we covered in the lesson? Would pay for this feature if it worked well!

reply

OsrsNeedsf2P

16 hours ago

 |
prev
 |
next

[–]

Gave it a shot, but mostly found it unable to keep up an interesting conversation. There's a lot of similar apps and they all have the same issue.

reply

qmmmur

22 hours ago

 |
prev
 |
next

[–]

Is all this capital, energy and opportunity cost really worth displacing tutors who are already pretty cheap and demonstrably effective? I put AI language apps somewhere near fad diets, in that they appeal to the convenience mindset.

reply

forkerenok

19 hours ago

 |
prev
 |
next

[–]

I see some rough edges typical to LLM-powered products, but this is still a fantastic tool!

I think it needs push-to-talk mode, because it's picking up every surrounding noise.

reply

ghostpepper

19 hours ago

 |
prev
 |
next

[–]

I also use chatGPT to translate phrases idiomatically and to ask questions about etymology, synonyms, homophones etc. I'm not sure I would want the entire language-learning process to be driven by talking with an AI so maybe I'm not the target audience for this app but these are the places where I think an AI can be uniquely useful in language learning.

I recently discovered www.lingq.com and it's by far the best language learning tool I've tried. The concept is that each learner brings the content they personally want to engage with - so it allows you to import articles, podcasts, and videos and then read them in your target language but translate words you don't recognize on the fly. It tracks the words you know and the ones you are learning automatically, and allows you to test yourself with flashcards based on the words in the content you care about.This is great because if you just want to read eg. French articles about cybersecurity, you will quickly start to pick up the domain-specific words.The problem is that the site is quite buggy, and needs a lot of UX/UI polish. I get the sense it's a small team, but they've been around for over a decade and it's still not polished.I don't want to use an inferior clone of Anki, I just want deep integration with Anki. I want importing content to be as painless as possible, including subscribing to podcasts.My ideal language-learning tool would be something like LingQ with all the bugs fixed and features implemented, and with AI integrated in the places it makes sense, not as the primary means of engagement with the app.

reply

Alex-Programs

17 hours ago

 |
parent
 |
next

[–]

You might like my tool. It has the same general principle as LingQ - learning from content you actually want to read - except it applies it to all web browsing. It's a browser extension that finds sentences in webpages, scores them by difficulty, then translates the ones that are right at the edge of your knowledge.

https://nuenki.appI haven't added Anki integration, though. A few people have asked for it, but it's a big time investment for something relatively niche.

reply

tietjens

18 hours ago

 |
prev
 |
next

[–]

I would like something like this particularly for learning specific styles of programming. For example, in order to grasp functional programing.

reply

madmod

23 hours ago

 |
prev
 |
next

[–]

Edit: Never mind it seems to be an issue on my device.

The faq wont expand on tap for me on android firefox. Dm me if you need more info.Looks like a great app and I can't wait to try it for Japanese!Can the cards be exported to anki?

reply

antonaf

22 hours ago

 |
parent
 |
next

[–]

Exporting to Anki is something we're currently discussing, as various users have already requested this feature!

reply

vibranium

17 hours ago

 |
prev
 |
next

[–]

I’ve tried Greek (Athena voice) and the accent is terrible. It sounds like an English or American person speaking Greek!

reply

mariano54

17 hours ago

 |
parent
 |
next

[–]

Thanks for pointing that out. Did you try the other ones by any chance?

reply

Twey

19 hours ago

 |
prev
 |
next

[–]

I put in my name but it insists I am called Anton.

reply

adastra22

21 hours ago

 |
prev
 |
next

[–]

I haven't tried it out yet. I will. But I just want to say that I have wanted this to exist since I first used ChatGPT in 2022. Thank you for building it.

reply

stronglikedan

23 hours ago

 |
prev
 |
next

[–]

I'll try it, but that seems pricy compared to a Duolingo subscription. And while
I
 understand that they are different, will
your
 average lead know that?

reply

vlan121

22 hours ago

 |
prev
 |
next

[–]

Awesome, I was going back and forth with LLMs trying to keep a conversation up. You guys managed to channel those process, I think I will love this app!

reply

icanhasjonas

7 hours ago

 |
prev
 |
next

[–]

I love it!

Q: how do I change my name in the app?

reply

mariano54

1 minute ago

 |
parent
 |
next

[–]

You can do this in the web app:
https://app.issen.com/manage-account

reply

panarchy

23 hours ago

 |
prev
 |
next

[–]

Hopefully people that use these AI language tutors don't end up being clowned on by native speakers because they sound like robots.

reply

4b11b4

23 hours ago

 |
prev
 |
next

[–]

Those FAQ boxes on the main page don't expand?

reply

mariano54

23 hours ago

 |
parent
 |
next

[–]

What device and browser?

reply

zuminator

23 hours ago

 |
root
 |
parent
 |
next

[–]

Same for me, Google browser, Android.

reply

b0a04gl

23 hours ago

 |
prev
 |
next

[–]

how're you handling latency on turn overlaps : buffered stream with early intent cutoff or full duplex with partial decoding?

reply

mariano54

23 hours ago

 |
parent
 |
next

[–]

We transcribe after 400ms of silence in 200ms chunks. 3 voice chunks (VAD) automatically interrupts, unless it's a back channel like "yeah" or "right" or something like that.

Whisper can transcribe in <100ms.
We then wait for the turn detection model, LLM, and tts to trigger a streamed response back to eh client.

reply

chris_engel

22 hours ago

 |
prev
 |
next

[–]

Sorry but the approach is too naive and the tech isnt there yet.

You can't make up a couple of conversation topics and expect the LLMs to do the rest by just switching languages. People approach the same topics completely different in different languages. The app looks like someone picked a couple of topics and the rest is "just" ChatGPT advanced voice mode.And the worst thing is that the LLMs in TTS do not sound native and cannot teach you pronounciation and learning to listen and understand (which is the whole point in having spoken conversation).And the other way around, the STT will not notice pronounciation mistakes made by the student - so the app cannot tell you: oh, its pronounced like this.

reply

kenan089

14 hours ago

 |
prev
 |
next

[–]

Congratulations on a successful launch.
Wishing you success.

reply

plorntus

21 hours ago

 |
prev
 |
next

[–]

Honestly tried it out, I wanted to like it but in its current form I found myself frustrated enough to just end the 'call' and close the app. Been learning Spanish for quite some time now so wasn't put off by the 'it always talks in X language' thing people are talking about.

The thing that put me off was the speech recognition. I am not in a loud environment and I wasn't even talking and it was picking up responses and responding to it before I even opened my mouth. It blazed through the 'preferences' set up itself making up responses. Then when I did get to talk it just simply got my answers wrong. It would often interject too at random during my sentences.

reply

hahamaster

18 hours ago

 |
parent
 |
next

[–]

Me too. Complete silence, headphones but recognized random words before I had a chance to say anything.

reply

skor

15 hours ago

 |
prev
 |
next

[–]

You have Catalan and Galician but not Basque

reply

Jimmyjohn619

23 hours ago

 |
prev
 |
next

[–]

This s super interesting! i have been wanting to learn other languages, but it i have been unsatisfied with most mainstream solutions. From what i have seen and for the price, i could see myself giving this a shot!

reply

jphelan

22 hours ago

 |
prev
 |
next

[–]

I tried the app. I love that you’re tackling this and I’m rooting for you. I’ll tell you about myself, my experience, and my thoughts.

I’m currently learning French as a beginner and I’ve learned other languages in the past. I’ve trued Duolingo as well as italki and frantasic as well as just ChatGPT. I am very familiar with Anki and I think it’s critical to make your own flashcards by choosing images and sounds. I don’t want auto cards.My experience with Issen:* it’s frustrating when the conversation partner doesn’t remember what it just said - it means I can’t get a chance to ask que c’est que ça veut dire.* it’s frustrating (just like with ChatGPT) that the conversation partner tends to interrupt and jump in while I’m thinking. I think many learners speak slowly and spend extra time thinking. ChatGPT allows you to hold the glowing circle and it won’t interrupt while you do.I’d love to see the chat bubbles have more in depth features like:* much clearer indicator of hover or click words for translation, and more features like example sentences or click to pronounce* an option to ask for an explanation of some or all the text* for my own text I’d love to see feedback with more UI native elements about how accurately I pronounced each word and any grammatical mistakes I made. The text summary is a great startI found myself ignoring the features of the chat bubbles and only in writing this feedback did I notice them! They could maybe use more contrast and clear UI emphasis. Duolingo does a good job of making their UI very clear with this kind of feedback.I think it’s important to build features that augment the app to work around LLM limitations. My guess is a lot of the settings change the prompt and that’s great but I think it leaves too much room for hallucinations to nosedive the experience.I’d also love to see some way to have a hold to talk or something similar.I’m very conscious at this point about the cost of these lessons and I have a hard time finding the price. Frantastic is absurdly expensive and it made me switch to italki where human conversation is literally cheaper. Without differentiating more from ChatGPT I would have a hard time justifying an additional subscription to my wife!Edit: I found the pricing and it’s a tough sell! ChatGPT is cheaper.I think you can both differentiate further from ChatGPT and keep cost down. I’d recommend to try to get more value out of each API call, so learners are more aligned with the cost per interaction- like make it so I’m enticed to spend a little longer reviewing the chat bubbles. My suggestions are mostly about how I want more engagement with each utterance anyway. Right now it’s very tempting to just keep making more and more utterances and IMHO that drives up costs while being frustrating for me.I’d be happy to discuss!
I wish you success.

reply

mel0n_

21 hours ago

 |
parent
 |
next

[–]

Have have you found to be the most helpful services/resources when learning French? I'm starting this journey

reply

jphelan

20 hours ago

 |
root
 |
parent
 |
next

[–]

Congrats! I'm happy to suggest some ideas. This is near and dear to me so I've got a lot to say lol.
I think when beginning French the most helpful services for beginners relate to pronunciation and language comprehension because that is the "secret trick". Seriously, I recommend giving pronunciation/comprehension a lot of attention at first. There are only like 10-20 new sounds (plenty of resources to find the list if you search IPA French
https://www.frenchcourses-paris.com/french-lessons-in-paris/...
 find one that clicks for you) so don't worry that it's too much even though I know it's hard and looks cryptic at first. I think most people end up mis-learning to read French like it's funny English then they will never have a good experience and certainly won't be able to have a conversation. I had the same experience with Chinese where if you don't learn tones at the start then it will always be miserable. For example in Chinese you can ask for dumplings and people literally just hear you saying sleep unless you add the right inflection (like the way we make a statement a question vs a demand).

In terms of the exact resources for pronunciation - The Fluent Forever guy has a good anki deck for $12 (I bought it and I'd recommend it - just have patience and know he tends to over explain IMHO but the cards are linked in there and they're great)https://blog.fluent-forever.com/chapter3/and I'd recommend finding your own favorite YouTube videos to explain how to pronounce the French R and nasal sounds. I would try watching some YouTube in French just to wet your beak. Know that it's frustrating to not yet have good comprehension but keep at pronunciation/comprehension and you'll get there.I recommend making Anki cards for like the top 100 and then the top 500 words, and include images and sounds (Anki strengths).I'd suggest to have a goal of understanding some rewarding things like children's T.V. (Bob l'éponge) or language learning YouTube (Easy French) - really fun. Then after you master some early words and feel like you have a "French ear" jump in and do some "early reader" kinds of book (https://www.barnesandnoble.com/w/short-stories-in-french-for...) because that will be really rewarding and reenforcing.I also recommend jumping in to italki probably earlier than you feel comfortable (or this app, as it continues to improve!) and doing some community conversations in just an unstructured way. Just be ready to try a couple people and find someone you like. If you can travel to France I think that is probably best, too! You'll be very happy that you've got a good "R" at this point.I think at that point you're ready to look at the A1/A2/B1/B2 test content and learn it on your own pretty easily or work with a structured tutor. It should be chill and not too challenging at that point.

reply

clarkalistair

22 hours ago

 |
prev
 |
next

[–]

I've been waiting for someone to build this! Trying it out now

reply

clarkalistair

21 hours ago

 |
parent
 |
next

[–]

Ok, so feedback from me.

It asks me for my level; I'm half way through this audiobook (https://www.amazon.co.uk/Next-Steps-Spanish-Paul-Noble/dp/B0...), and have listened to the book before it a number of times, so I'd say I'm between beginner and intermediate. I think you could do better than a "what level are you, pick from 3 options" and throw you straight into a chat - ask some basic Spanish questions, and then try and figure out where the user is from there.Next I chose Blanca from Barcelona, and she said an awful lot of words and I understood very little of them, so I think I'm not ready. Half the grammar lessons have both a Spanish and English explanation, and half don't.I'll keep the feedback coming, but I'm on a train now and the questionable internet is not good enough for an actual conversation.(not at all relevant but I work for Devyce, from the YC S22 batch!)

reply

dinkblam

20 hours ago

 |
prev
 |
next

[–]

tried it in Safari, didn't hear anything of the intro sentence after choosing a voice and then i got

"Error An unknown error has occurred."has this been tested on Safari?

reply

personjerry

22 hours ago

 |
prev
 |
next

[–]

Loom embeddings work in HN posts? Is that new?

reply

55555

21 hours ago

 |
parent
 |
next

[–]

You must have the Loom chrome extension installed?

reply

vibranium

17 hours ago

 |
prev
 |
next

[–]

How does this compare to Langua?

reply

mariano54

17 hours ago

 |
parent
 |
next

[–]

Langua is a nice app with more features than ISSEN. We focus on the voice chats, and I think our tech is better (intelligence, latency, realtime flow, voices, etc), especially for non english/spanish.

We are aiming to create a long term companion/tutor that gets to know you more and more, and can create customized curriculums, lessons, etc.

reply

QuadmasterXLII

19 hours ago

 |
prev
 |
next

[–]

Someday someone will release a good AI based language learning app, because it’s the obvious use of the technology.

That person will have a hellish time marketing it because projects like this will have so thoroughly primed us to assume its slop.

reply

titusaj92

22 hours ago

 |
prev
 |
next

[–]

THIS IS AMAZING!

reply

golergka

21 hours ago

 |
prev
 |
next

[–]

Great work! I'm learning Spanish in Argentina, and most of the apps that offer it just have Mexican or Spain variants of the language. I think it's the first time I see a selection of different virtual tutors with regional dialects.

reply

jmyeet

21 hours ago

 |
prev
 |
next

[–]

So this is the AI gold rush and of course this isn't the first AI language product I've seen of course. No hate to you or your product but I have a question.

If AI succeeds, will we evenneedlanguage learning? Language learning is notoriously difficult and time-consuming. We're rapidly approaching a future like Star Trek of universal translators.If so, what is the realistic future for AI language learning products?

reply

mariano54

20 hours ago

 |
parent
 |
next

[–]

I think so. Language learning is not just about practicality, it's about knowledge, culture, respect, and connection between people of different countries. If people have more free time and travel more, I expect language learning to grow.

Plus, you can't do auto translation for languages like Japanese where the grammar is reversed. Auto translation has fundamental limitations.

reply

kiririn7

12 hours ago

 |
root
 |
parent
 |
next

[–]

you cant create a machine that thinks like a human. machines have fundemental limitations

reply

joshtucholski

19 hours ago

 |
prev
 |
next

[–]

feels like i should be asked to tell it my name, not type it

reply

mariano54

18 hours ago

 |
parent
 |
next

[–]

The issue with that is people with less common names will get the wrong transcription, and there's nothing worse that seeing your name spelled wrong over and over

reply

faustocarva

19 hours ago

 |
prev
 |
next

[–]

Pretty cool, tested it!

reply

TeeMassive

17 hours ago

 |
prev
 |
next

[–]

Very interesting, but 20 minutes seems very low to fully try a language learning app. would you consider extending to a few hours?

reply

runarberg

19 hours ago

 |
prev
 |
next

[–]

I tried a 20 minute conversation, as a beginner Japanese learner (mid-to-high A1).

My first problem was setting my native language truthfully to Icelandic which seemed to confuse both me and the AI tutor. We spoke together in Japanese but asking how to say a word in Japanese but giving the Icelandic word didn’t quite work, giving the word in English worked much better.Now as a beginner I don’t think this service is right for me. It is very hard to have a conversation—even a basic one—at my level and I didn’t actually learn that much as I wasn’t able to say anything. I did however learn that I need to practice creating sentences on my own, and I need to practice speaking, but honestly I would much rather do that via structured exercises from a textbook then from an AI tutor (or a human tutor for that matter). I have been skipping those exercises in the textbook that I use, so I guess having that 20 min conversation did indeed help me realize what I need to focus on. So I guess thanks for that.A more useful feedback from a beginner’s perspective. Taking your time between sentences is something you can do with an AI tutor which you can‘t do with a human tutor, so I recommend you add stuff like dictionaries and grammar keys which beginners can look up before starting the next sentence.I would also like to see some basic note-taking, or even message drafting, such that you can type in a draft before you start speaking your next sentence. I don’t think intermediate speakers would need these as they can just ask the AI tutor during the conversation, but for beginners it is nice to have some written materials as you practice.

reply

carstenhag

20 hours ago

 |
prev

[–]

Haven't tested the functionality yet, but some feedback:

- the name is bad. Issen? I (German, Spanish speaker) don't know how to pronounce it.- use correct flags. Catalan speakers will be rightfully pissed when you use the Spanish flag for their language.- in a language learning focused app, it is not acceptable to have a badly translated app. I'm using it in German and while the intro does not have typos, I can tell it's all just AI blubber- For German specifically, I'd recommend you to use "du" and not "Sie" ("Wie heißen Sie?") across the app. If your tool isn't aimed at 60+ year old BMW drivers, use "du".

reply

mpeg

19 hours ago

 |
parent
 |
next

[–]

Catalan, the language, does not have a flag. As a native speaker (of a dialect) who is not from Catalonia I would much rather the language be represented by the Spanish national flag. Although people from Andorra might also not love that.

Languages and flags don't mix well.

reply

celebdor

19 hours ago

 |
root
 |
parent
 |
next

[–]

All the areas where Catalan is spoken as a mothertongue:

-https://en.wikipedia.org/wiki/Alghero-https://en.wikipedia.org/wiki/Andorra-https://en.wikipedia.org/wiki/Balearic_Islands-https://en.wikipedia.org/wiki/Pyr%C3%A9n%C3%A9es-Orientales-https://en.wikipedia.org/wiki/Catalonia-https://en.wikipedia.org/wiki/Valencian_Community-https://en.wikipedia.org/wiki/AragonAll of them share the coat of arms of the crown of Aragon:https://en.wikipedia.org/wiki/Coat_of_arms_of_the_Crown_of_A.... Thus using the "four red pallets on a gold background" represents all the speakers in different European countries.

reply

carstenhag

19 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I am not sure if I got you, are you aware of the cultural/political issues around it? There's no flag for the language (as it's used at many places), but almost everyone will be happy with a commonly known flag they can identify with. A Valencian will be fine with a Catalunya flag :)

reply

mpeg

17 hours ago

 |
root
 |
parent
 |
next

[–]

The cultural/political issues are deeper than you'd think, there are some within Catalonia that would claim all of us Catalan speakers as part of the same cultural umbrella, negating our own cultural background as derivative.

That's why I say that I personally (as a Mallorcan) would much prefer the language to be associated with a Spanish flag than a Catalan flag. Some people would agree and some would disagree – ultimately the best thing is to not link flags to languages anyway.To give you another example from Issen, they're also using the American flag for English which is probably even more controversial :)

reply

diggan

18 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

Academically, maybe it doesn't have a flag. But the de facto flag is the Senyera and I don't think a lot of people
wouldn't
 recognize it as such in Spain.

reply

magackame

17 hours ago

 |
root
 |
parent
 |
prev
 |
next

[–]

I wonder if anyone ever came up with logos or at least emoji codes for languages?

reply

npinsker

20 hours ago

 |
parent
 |
prev
 |
next

[–]

The English intro feels non-native too, and does have a typo (“You’ll be truly amazed of how polished […]”), which makes me think it
wasn’t
 AI.

reply

Twey

19 hours ago

 |
parent
 |
prev

[–]

Also on the controversial flags side: using the British flag to represent Welsh

reply

cpursley

3 hours ago

 |
root
 |
parent

[–]

Or American ;)

reply

Consider applying for YC's Fall 2025 batch! Applications are open till Aug 4

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
