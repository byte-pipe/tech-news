---
title: 'Ask HN: Fable hacked my piano, can I release the results? | Hacker News'
url: https://news.ycombinator.com/item?id=49577129
site_name: hnrss
content_file: hnrss-ask-hn-fable-hacked-my-piano-can-i-release-the-res
fetched_at: '2026-09-07T16:17:42.035148'
original_url: https://news.ycombinator.com/item?id=49577129
date: '2026-09-05'
description: 'Ask HN: Fable hacked my piano, can I release the results?'
tags:
- hackernews
- hnrss
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
Ask HN: Fable hacked my piano, can I release the results?
223 points
 by 
jmpman
 
15 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
136 comments
I have a self playing piano, using a system called PianoDisc Protigy. They have an online store which sells music for their system, from various modern artists along with classics such as Bach and Beethoven. Last night I saw they had released some music from Eric Satre, a 19th century French composer, which I bought. Curious if I could have just used AI to create these files, I began experimenting with Astra and Fable. Feeding the output of one into the other to critique. After an hour of LLM discussion of Rubato and fermata, solenoid response times and proper sustain pedal technique, they settled on their ultimate version of Gymnopedie No 1.

I then asked Fable to compare it to the open source version I'd downloaded from Mutopia, which it promptly ripped apart. No sustain, zero rubato, upside down balance.Ok, what about the version I'd just bought?The PianoDisc versions are mp3s encoded with the right channel carrying MIDI to be played on the piano, and the left channel containing any accompanying music to be played through attached speakers (who doesn't want the harmonica on Piano Man?)I gave the mp3 to Fable, which promptly decoded the format, identifying the right channel carrying MIDI using a 2004.5 Hz square wave.It then went on to analyze the nuance of pedal lift and melody relative to the chords.Fable then asked if I wanted it to build an encoder to write my own MIDI files into the right channel of mp3s.Sounds great, and I instructed it to write the encoder.What it came back with was a python encoder PLUS a decoder.In the verbose explanation, it mentioned decoy notes.Curious, I asked it to explain the decoy notes.Apparently PianoDisc adds obfuscation into their format which is handled properly by their decoder, but would leave naively extracted MIDI unplayable on other systems.Fable created an encoder which adds those decoy notes, and a decoder which removes them.Am I allowed to publish the decoder? The encoder?

 
help

Giefo6ah
 
12 hours ago
 
 | 
next
 
[–]

If you live in the USA, the "decoy notes" may be considered an "effective technical measure" from the "Digital Millennium Copyright Act".

If you live in Europe, this restriction may be considered "gatekeeping" and exempted by the Digital Markets Act.Don't bring attention to yourself by asking for permission. Publish your codec, and if the company cares about this they will send a cease and desist.If you want the world to benefit from your code but you don't want to be responsible for it, try to adapt the codec to ffmpeg. The ffmpeg project is used to dealing with these matters, and will keep your codec working for eternity.

reply

progval
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

> If you live in Europe, this restriction may be considered "gatekeeping" and exempted by the Digital Markets Act.

That's not how the DMA works at all, there is no concept of gatekeeping practices. Instead, the EU Commission designatescompaniesthat act as gatekeeper for some services (current list here:https://digital-markets-act.ec.europa.eu/gatekeepers-portal_...) whichthenputs constraints on what they do.

reply

kolinko
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But we have various exemptions that are for all the companies, no? E.g. you're free to hack and crack software to do your own backup copies.

reply

c0n5pir4cy
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not a lawyer but it wouldn't be under the DMA - these rights predate the DMA by a while.

reply

j1elo
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Don't publish your code. Let the AI "accidentally escape the sandbox and publish it in a readily available Git repository". Tongue in cheek, in current days who would blame a poor LLM just trying to do the right thing? :)

>Publish your codec, and if the company cares about this they will send a cease and desist.If there are doubts about C&D letters, don't publish codeto a USA provider. Bring it to Gitee, under an anonymous author name.

reply

gear54rus
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Exactly. Surprised to see 'just don't let them find you' so far down when it should be the first advice.

reply

Doohickey-d
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

If you don't want to be responsible for it, another way is to just publish it anonymously: make a GitHub that isn't attached to your real name etc, perhaps using a one-off disposable email address, and put it there. Then you don't have to think about what the lawyers think. Worst case it'll get taken down, but by that point it'll likely be popular enough that there'll be plenty of copies.

[Pirate flag emoji here]

reply

embedding-shape
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Worst case it'll get taken down,

Eeh, worst case scenario you'll get sued as Microsoft will have no problem with handing over everything they have from your Windows installation information, GitHub accounts, NPM authentication and everything else they own today if the courts tell them to.You can't just commit crimes on the open internet without really hiding IPs and what not, and expect that to not come back to haunt you eventually. Kind of poor form to suggest otherwise too.

reply

lukan
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

"You can't just commit crimes on the open internet "

Who said it is a crime, are you a lawyer?

reply

embedding-shape
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Allegedly commit potential crimes*

I'm not saying yay/nay if this is a crime or not, but if you think it might be, and you create a new account on GitHub to "be anonymous", you're not taking opsec seriously enough for something you believe might be a crime.By the way, generally judges or juries would be the ones to decide if something was illegal or not, it's not the lawyers who decide this, in any country I'm familiar with.

reply

wombatpm
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Please note: This is America where potential civil immigration charges can result in summary execution because poorly-trained wannabe-cop racists with guns make needless escalations. If law enforcement thinks it’s a crime, it’s a crime until the courts say otherwise.

reply

fennecfoxy
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Tbf "is it a crime" is hard for even a single lawyer to answer because it depends on: who you are, your skin colour, how rich you are, your sex, whether it's a white collar crime or not, did you commit the crime on behalf of a corpo, etc.

But we like to pretend that the justice system delivers justice evenhandedly I suppose.

reply

supernikita
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No it does not. The law defines what a crime is. 
That you are bummed out about how it is applied, does not change the question, whether it is a crime. 
One thing is the definition of what constitutes a crime/felony/misdemeanor, 
another thing is the application and the punishment meted out.

reply

d1sxeyes
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's not quite the case in common law countries. In countries like the UK and the US, the interpretation of the law as written is ultimately decided by the court, meaning that the definition of what constitutes a crime/felony/misdemeanor 
is
 subjective. The more courts that attempt to interpret that specific law, the more 'jurisprudence' builds up, meaning that the interpretation applied in a previous decision can certainly have an impact on a future decision.

reply

deaux
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> You can't just commit crimes on the open internet without really hiding IPs and what not, and expect that to not come back to haunt you eventually.

Not sure what you're talking about, the current AI boom is entirely based on committing crimes on the open internet without really hiding IPs and what not.So is much of big tech in general.

reply

embedding-shape
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Keyword being "you". "They" can commit crimes, because they're big tech companies who give gifts to the right people. But "you" are not "they".

reply

wombatpm
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Why bother publishing the code? Anyone with LLM access can recreate it. Instead write up your findings on how it works. Publish that in a blog, submit it to Wikipedia and Reddit. Player piano did security through obscurity. Now make it less obscure.

reply

Tepix
 
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

Sure, on github it will (still) get the most attention, but perhaps another repository outside the US is a better fit.

You could also create a text document instead of a software that details the mechanism used to fool other MIDI decoders and publish only that (for now).Finally, familiarize yourself with the Art. 6 Software Directive (2009/24/EC) / §69e UrhG —decompilation for interoperability. It may be your ticket for a legal status in Germany/EU.

reply

saturn8601
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What if the companies start auto subpoenaing the AI companies to try and tie the code to an account?

reply

asdfsa32
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Let them do it. It will end up really well. I know the system has been protecting these companies, but that has been an economic concern as much as other motives. Now that AI is the crown jewel of economy and global dominance, let the entertainment industry have a go at it. Let them.

reply

MarkusQ
 
37 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Wait until we all get popcorn though, and find a comfy place to watch from that's just outside the splash zone.

reply

lodovic
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Do companies in the US really have the right to do that? I would think that kind of investigation is reserved for law enforcement only. If the design was made over email, would the piano company be able to subpoena Google for someone's private gmail messages?

reply

embedding-shape
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Do companies in the US really have the right to do that?

Does it matter? What's important is if it can happen or not, and how if so. We already know that MPAA is willing to basically do whatever, even contribute themselves to piracy, if it means they can put people in jail for copying stuff eventually. They themselves also gotten in trouble for copyright violations themselves in the past, so doesn't seem like they're hiding away from breaking a little bit of laws to hunt pirates.

reply

junon
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Attorneys can subpoena if the court approves, as part of ongoing litigation, AFAIU (IANAL).

reply

radicalcentrist
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Consider previous cases where companies like Reddit have unmasked their users at the behest of court order.

reply

pimeys
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Maybe then using an open weights model is a good way to hide your tracks...

reply

eru
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Or at least use an obscurer model from an obscure company, so they don't know who to subpoena.

reply

fc417fc802
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Everyone is aware that multiple services offer zero data retention, right?

reply

phire
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> the "decoy notes" may be considered an "effective technical measure" from the "Digital Millennium Copyright Act".

I really hope not. My understanding is that to be "effective" it needs to at least be a form of encryption with a secret key. At least, I'm not aware of any case law that allowed anything less than that.IMO, "dummy notes" are nothing more than a form of obfuscation. If it's obvious how to filter them out, then I don't think it comes close to meeting the bare minimum of what might count as an "effective technical measure".Of course, who knows what way the courts will rule if it ever reached that far.

reply

nerdsniper
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

shitty CAPTCHA’s and simple checksums have been ruled to be “effective measures”, so this would probably be too.

However, Section 1201(f) is designed to allow developers leeway in reverse engineering to make "independently created computer programs" talk to other "computer programs". But this usually distinguishes between talking to a binary (good) and reading a media file (bad).My guess is the encoder is probably legal under 1201(f) because it’s reverse engineering a DMCA covered application to create new media files for it to use. But the decoder would be illegal because it reverse engineers a DMCA covered application to extract copyrighted media.

reply

phire
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, on appeal the simple checksum was ruled to NOT be an effective measure. [0]

And while courts might have ruled that a CAPTCHA might count as a "technological measure" they haven't gotten as far as ruling them as "effective" yet.But in general yes. The protection scheme doesn't need to be well designed or free of design flaws to count as "effective". But from what I can tell, it does need to be a valid attempt at some cryptographic scheme requiring a secret known only to the copyright holder.[0]https://law.justia.com/cases/federal/appellate-courts/F3/387...

reply

1970-01-01
 
3 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's not effective technology if it is secure via obscurity. If it fits on a shirt, you're also fine. The key here (pun intended) is to publish it and show how obvious it was to reverse engineer.

https://www.cnn.com/2000/TECH/computing/09/08/decss.shirt.id...

reply

qurren
 
1 hour ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> Publish your codec

Put the code on the blockchain somewhere and it will be un-deleteable.

reply

politician
 
10 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Consider publishing the prompts used to create it.

reply

dgellow
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Very little value in the prompts imho, anyone can point their LLM to that post and it’s enough

reply

0-_-0
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Instruct the AI to output an .MD file that can be used to reconstruct the code

reply

KennyBlanken
 
11 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Any company would be a fool not to send a C&D given how many people on this site seem to think that "I got a C&D" means "if I don't obey it, I'm gonna get sued."

Anti-SLAPP laws exist for a reason, and if corps can bully anyone, how is it that corps routinely lose lawsuits on either side of the docket, hmmmm?Keep licking that corporate boot, folks. Corps send C&Ds because they cost them all of maybe $100-200 and they're so effective.There is alongroad between "got a C&D" and "am getting sued." Among other things, a judge is going to want to see that both sides attempted to negotiate. If the company sending the C&D just demands that and then tries to file suit, the judge is going to tell them to go back to step 2 and stop bothering him/her.Folks, stop telling people that if they get a C&D they have to just fold. Good chance you never hear from them again becausethe cost of suing you is nowhere near the damages they will be able to prove in court.

reply

vintermann
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> the cost of suing you is nowhere near the damages they will be able to prove in court.

The problem is, the one advising them whether to sue or not might not care about that at all, and might personally profit from a lawsuit. So they've got all incentive in the world to persuade their employer that theymustpursue this or they will have given up priceless rights forever.

reply

b3lvedere
 
6 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The average mortal cannot afford negative backlash, financially or otherwise, to their living situation.

reply

DANmode
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> There is a long road between "got a C&D" and "am getting sued."

Sometimes!

reply

userbinator
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

You spent --- what I'd assume would be several k$ from prices found online --- to buy a self-playing piano, and are now asking if you can release the tools to have it play the music of your choosing? IMHO the fact that you even had to think about asking if you could do this is everything that's wrong with society today. IANAL but as long as you aren't releasing something that's copyrighted from the original code, or violating some patent, there shouldn't be anything to worry about.

"It's better to ask for forgiveness than permission", as the saying goes. ;-)

reply

embedding-shape
 
6 hours ago
 
 | 
parent
 | 
next
 
[–]

> "It's better to ask for forgiveness than permission", as the saying goes. ;-)

OP is essentially asking if it's legal or not, not if people will dislike it. Navigating your nations laws with the mindset of "It's better to ask for forgiveness than permission" is bound to land you in places people generally prefer to stay out of.I agree it sucks that some things seem arbitrary restricted, especially when it's victim-less (/ the victim is a faceless for-profit corporation), but kind of feels non-ideal to recommend people to "ask for forgiveness" when it comes to potentially breaking laws.

reply

Scaevolus
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Aside: if you want a source of high quality Piano MIDI recordings, you should check out the MAESTRO dataset: 
https://magenta.withgoogle.com/datasets/maestro

> The dataset contains about 200 hours of paired audio and MIDI recordings from ten years of International Piano-e-Competition. The MIDI data includes key strike velocities and sustain/sostenuto/una corda pedal positions. Audio and MIDI files are aligned with ∼3 ms accuracy and sliced to individual musical pieces, which are annotated with composer, title, and year of performance. Uncompressed audio is of CD quality or higher (44.1–48 kHz 16-bit PCM stereo).

reply

tgv
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Wow. That's some high quality archive. I have never encountered anything better. Pity the performer isn't listed. And the competition's web site is defunct.

reply

Silasdev
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

This whole writeup is basically the verbatim prompt recipe for anyone to just whip it up themselves.

Blocking the final result is no longer a real block, when all it requires is a vague prompt to replicate it.We've entered a strange territory.

reply

jdlshore
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Don’t ask Hacker News for legal advice. If you really want to know the answer, ask a lawyer.

reply

Leonard_of_Q
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Standard answer fit to keep the parasites fed. There is no "the answer" here, there are many answers depending on which lawyers you ask and how much you can afford to feed them.

Just release the code somewhere, anonymously, it isn't yours anyway.

reply

mschuster91
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> There is no "the answer" here, there are many answers depending on which lawyers you ask and how much you can afford to feed them.

The thing is, at least in Germany, lawyers are required to carry a liability insurance and in the case th advice ends up being really bad you can hold their insurance accountable.

reply

twosdai
 
35 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The ability to hold laweyers accountable not a panacea. In this instance most competent lawyers are going to still give conflicting good advice and charge for it.

Because truly the answer boils down to "it depends" and many people will take it many different ways and not be "wrong". Publishing anonymously is a good choice, publishing publically and complying with a removal order is a good choice, not publishing is a good choice."Good" here being somewhat sound in that it likely wont cause the person publishing a huge life changing issue.

reply

walrus01
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

On the other hand
, this is 
Hacker
 news, so my first inclination of a response was going to be something like this:

"Get some small amount of bitcoin and pay a VPS hosting provider in Moldova for a year's service on a $15-per-month equivalent KVM VM and put what you know on there anonymously as static content, then publish the link here."Not that a sufficiently dedicated nation state federal crime agency or intelligence apparatus probably couldn't trace back to you, but it raises the bar for something like random civil lawsuits from piano companies.

reply

luipugs
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> makes a hacker news post from an 11 year old account

> jumps through a lot of inconvenient hoops to "anonymously" publish codeSomething doesn't add up there.

reply

brudgers
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

You are free to interpret this comment as prohibition or as my blessing, but...

If it matters, ask your lawyer.If it doesn't matter, it doesn't matter.Or to put it another way, trademarks (you've mentioned two) and copyrights (it's a crapshoot) are complex. And in some jurisdictions (notably the US) anybody can sue anyone for anything.Your risk aversion is yours, not someone else's. Your financial and legal wherewithal is likewise yours.

reply

Someone
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

> And in some jurisdictions (notably the US) anybody can sue anyone for anything.

That should be the case in all jurisdictions. The justice system exists so that, if I feel treated unfairly, I can go to the state to settle the question whether/how much that is true. If there are issues where I cannot go to court, what am I supposed to do? Go fight you over the issue?What differs (a lot) is how effectively the system rejects frivolous/unjust cases, how much time/money it costs you to defend yourself against remaining claims, and what systems there are to prevent people from going to court (having affordable care will prevent people from taking some medical claims to court; obligatory car insurance means most fender bender cases get handled by insurance companies, etc(

reply

cromka
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Should also mention the SLAPP suits which specifically exists because anyone can sue for anything.

reply

jmpman
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I might just email the company. If they object, I won't make my GitHub repo public.

reply

ungreased0675
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This seems like the worst possible advice. It will only bring negative attention and maybe legal repercussions.

reply

brudgers
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

They might object to the existence of the software and demand “its destruction.”

Or sue your ass…or file a DCMA takedown with Github.Or all of the above.The best likely outcome is probably “no.”Because they have lawyers and that’s what lawyers do.If you really really want to share the information, you might write a blog post with technical details without linking to any code. Sharing the blog to the “Facebook group” will let you assess community and corporate interest and make an informed decision.Keep in mind that they could say yes and still do all that bad stuff anyway.

reply

georgemcbay
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> I might just email the company. If they object, I won't make my GitHub repo public.

If you do this, I can nearly guarantee they will either never respond as a best case scenario, or they will object.There is effectively zero chance a company would give you any indication that you have their blessing. Even if they don't actually care one way or another they will make the assumption that giving you any kind of positive response is nothing but a negative for themselves in terms of future liability, etcThe phrase that it is "better to ask for forgiveness than permission" exists because of situations like the one you're in.Just publish the repo. Don't contact them. If they C&D you, take it down if you don't want to deal with the legal repercussions.For all the same reasons that it is easy to predict how they will react if you ask, it is easy to predict how they will react if you don't and they find the repo and object. They will send you a cease and desist letter telling you to take the repo down. You will then take the repo down and face no other legal action because it will not be worth their time to make any bigger deal of it than that.

reply

MuffinFlavored
 
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

Have you ever worked corporate before?

It is better to ask forgiveness than permission.

reply

bossyTeacher
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

HN users are at the same time the brightest and the most clueless. Why on earth do you think they will agree to something that they will perceive as damaging to them in the present or in a possible future?

reply

arjie
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

The nature of these tools is that your post and the device should suffice to replicate so in some sense you have already published the encoder and the decoder.

reply

loa_in_
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

I imagine it hexdumps it and looks for patterns.

reply

RRRA
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

I'm currently toying with a similar process which I think falls under the interoperability exemption:

- Get an apk online, you haven't accepted a EULA.- Run jadx to get some code to work with- Ask Claude to extract the protocol specification cleanly for a Bluetooth device with capabilities etc.- Use Claude to implement a version as a TUI/CLI in go, rust, whatever.I get to use a device I own with a local Bluetooth connection from my machine, maybe Home Assistant. I do not contact any online services (there are none anyway in that case).Since it's to avoid getting locked in with proprietary OS, it's a clean room reversing through a spec and an LLM produced a non copyrightable output...
Can I just release this however I want? 
Probably a basic MIT or CC0, whatever...

reply

webprofusion
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Ideally someone random on github would post the same thing, so you don't have to. That would be a fortunate coincidence but I'm pretty sure these things happen.

reply

reilly3000
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Gymnopedie No 1 was one of the pieces I learned as a primary school student as a mediocre and undedicated pianist. The reverse engineering is impressive and generally useful, but really learning that piece all the way through could be even more rewarding, then you can use 10 fingers and two feet to make it sound like YOUR ultimate version, not just your words. Perhaps Claude truly nailed it in your taste and you want to be able to reproduce it reliably without automation: record one phrase at a time and try to minimize the about of variance between yours and the MIDI. Maybe some visual feedback would help and be clever, but usually using your ear is the most productive.

reply

jmpman
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

The funny thing is - I'm virtually tone deaf and can't play the piano. It's my wife's piano, but when we bought it, I had the player system installed, so I could get some enjoyment out of it.

reply

skinfaxi
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Just say the AI did it on its own and you'll be off the hook.

reply

altairprime
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Your intentions can reasonably be interpreted by a court as attempting to avoid paying a commercial software licensing fee. Use of Fable is, in your specific instance, irrelevant to whatever the outcome would be; the finding of intent holds plausible regardless of what tools and/or contractors you used to pursue your intent. Seek legal counsel if you wish to publish. (I am not your lawyer, this is not legal advice.)

reply

layer8
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Rather than publishing the decoder and/or encoder, it would be more interesting to publish how the decoy scheme works in detail. We want to understand how things work, not blindly use tools that we could build ourselves based on that understanding.

reply

piefayth
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

I do think that “decoy notes” is the kind of potential hallucination that warrants manual investigation.

reply

severak_cz
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

> The PianoDisc versions are mp3s encoded with the right channel carrying MIDI to be played on the piano, and the left channel containing any accompanying music to be played through attached speakers (who doesn't want the harmonica on Piano Man?)

What a cursed format!I don't understand what the designers were thinking of... 2000 Hz square wave on right channel? Seriously? Nobody would hear something suspicious and nobody would literally see it on spectrum analyzer. Maybe it's holdover from analog days and it was on casette tape before.Also somebody reverse engineered it before -https://www.kinura.net/mid2pianocd/So Fable probably just igested it from documentation of this software or some very obscure forum thread somewhere.

reply

ben_w
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

> I gave the mp3 to Fable, which promptly decoded the format, identifying the right channel carrying MIDI using a 2004.5 Hz square wave.

Wow. Abuse of format like this is always funny to see.

reply

tverbeure
 
11 minutes ago
 
 | 
parent
 | 
next
 
[–]

It’s not just funny to see, it’s also fun to create, satisfying to see it work, and terrifying to deploy it for hundreds of thousands of users… when it’s a cursed way to update firmware.

reply

sandos
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Recently had a similar, but likely more severe problem: I noticed Sol decompiled some proprietary code to re-implement some functionality for an emulation I wanted to use internally.

Now its likely soiled and I have to throw it away. Doh! I asked it about legality and it went "its almost green" but when googling, reverse-enginnering like that seems very illegal.The weird thing is in this case, it could have pretty easily gotten the needed info from using the code as a black box, and that is apparently legal!

reply

pbasista
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

> Now its likely soiled and I have to throw it away.

Could you explain why you think so?

reply

userbinator
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Soon enough you will realise that everything is a derivative work, and the sooner that happens to everyone, the faster the delusion of Imaginary Property will disappear and lead to actual competition and progress.

reply

franky47
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

typo: did you mean Erik Satie?

https://en.wikipedia.org/wiki/Erik_Satie

reply

gbnwl
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

This is a nit but his name is actually Erik Satie not Eric Satre.

reply

jmpman
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Yes. Made a type and after I noticed it was too late to edit my post.

reply

salviati
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Thanks! I was confused, thinking "Is it Satie, or is this a case of Muphry's law?". I wanted to learn more about this Satre composer I never heard of.

reply

ted_dunning
 
8 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's a nit. They made a typo.

reply

mft_
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

IANAL but... isn't this somewhat analogous to side-loading apps on iOS or Android? As in, Google/Apple make it awkward for you to provide your own 
files
 to run on your phone, but ultimately it's not impossible nor illegal.

Likewise, if you're able to upload your own custom MIDI (or other) files for your piano to play, then all you'd be doing is sharing a utility that creates mixed audio/MIDI MP3s, which may or may not be used to create files which can then be legitimately uploaded to a piano.

reply

saidnooneever
 
6 hours ago
 
 | 
prev
 | 
next
 
[–]

in most regions it is not illegal but asking so here would require readers to know exactly what laws apply where you are to answer that adequately from a legal perspective.

i can say, many people do it, some get in trouble because of local laws, others dont because their regions dont have such laws.if you look at exploitdb and such site they have many exploits also for proprietary things. i would say if you dont outright leak firmware or such IP, an exploit itself is usually not strictly illegal.its always best to contact a vendor if they are contactable, to both help them fix it and get permission for a post..that way, you can be relatively comfortable you are safe. get it in writing, email is ok.edit: this is a gray are where the decoder might be considered leaking an algorithm btw. its perhaps not strictly an exploit but some characteristics will be shared around how its perceived to use something not as its intended.

reply

NordStreamYacht
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Why not publish the methodology in detail and leave it at that?

reply

alansaber
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Usually people only bother reading it if the outcome is interesting

reply

amelius
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Heh, why not ask Fable? I'm sure its legal advice is based on more informedness than when asking HN.

reply

doawoo
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Did you really need to ask a massive LLM and burn tokens on this?? A few minutes of googling has revealed a huge amount of this information just laying out in the open, and, a whole tool to author your own files that someone sells as independent software! (
https://www.kinura.net/mid2pianocd/
)

reply

jmpman
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

I'd found this code as well, and in a previous chat, Fable pointed me to it but first, I have a $100/month Claude subscription, and typically just barely run out every week, so I throw tokens at just about anything. Second, I'd come across that code, but it's windows software, not open source. Third, the encoder isn't anything exciting, and not really a concern except that the Fable version offers the ability to include the decoy notes. Finally, I literally just wrote "Yes, please write that encoder" when fable asked if I want it to "Bigger picture: since the Prodigy plays this format over Bluetooth, an encoder that writes your own MIDI into the right channel this way is probably the missing link for the MP3-to-piano project. I can build a test file if you want to try it."

reply

kbcool
 
5 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes. How else could the LLM even begin to do what it did otherwise. Not a criticism of you, just a place for a rant but I still find it incredible when people think they're doing something novel when really they're just reassembling existing work.

What really reinforced this for me was that I recently vibe coded a home assistant addon that, as it turns out, there was a github project that did almost the same thing. The initial implementation that came out of the LLM was essentially the same just with just some small tell in things like the logging that came from what I prompted it.It was a very small project (maybe 500 LOC) so there's a greater chance of coincidence but it really felt like the office junior had just ripped off someone else's work and tried to hide it (badly) and really, that's exactly what they do

reply

jmpman
 
59 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I had performed a quick GitHub search and not found any code. It certainly didn't have these decoy notes documented on its own. It only found them because I provided it a known Erik Satie piece, which has a specific number of notes, and it dug in to figure out what the excess notes were.

reply

orangecat
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

How else could the LLM even begin to do what it did otherwise.

Are we really still having the "LLMs can only regurgitate what was in their training data" argument? Where did the counterexample to the Jacobian conjecture come from?

reply

natch
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

You bought a hardware device and you own that device?

This decoy notes scheme seems pretty unethical.

reply

Gigachad
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

I wouldn't take claude research at face value. It found something odd, came up with a plausible sounding explanation and confidently presented it to OP. Doesn't mean it is true.

reply

NegativeLatency
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

Personally I’d just do it

reply

Redster
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

IANAL, but it might be relevant to others trying to answer what jurisdiction you are in. (US, EU, CN, JP, elsewhere?)

Also, when you bought from PianoDisc, did you agree to abide by a certain jurisdiction's laws in your use of PianoDisc? And did you explicitly agree to not share any sort of decoder/encoder in any ToS?

reply

jmpman
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

US.

https://store.pianodisc.com/pages/terms-of-service-and-condi...I don't see details about them mentioning and decoder or encoder.

reply

codingdave
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> (k) to interfere with or circumvent the security features of the Service

IANAL. But I think reverse engineering their data structure, identifying a security measure - even one as weak as obfuscation, and publishing code to circumvent it is clearly against your license.

reply

Elsewhereindeed
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I am also NAL, but out of curiosity does OPs post detailing the obfuscation transgress any laws?

If the security measures exist in plain sight, as they apparently do, are they allowed to be discussed?I reckon that if OP posts the encoder/decoder software that'd be against some sort of license clause. However in the age of AI who cares about the software at this point? Anyone can prompt their own private version into existence.Just thinking out loud here. I have not considered AIs use as personal "cheat engines".

reply

ted_dunning
 
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

I think that is the terms and conditions of the web site, not the hardware product.

reply

bambax
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

> 
some music from Eric Satre, a 19th century French composer

>Gymnopedie No 1Eric (or as he preferred, Erik) SATIE.

reply

noduerme
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm sorry, I'm hung up on the idea that an LLM could look at a midi file and listen to something and write an improved version with better sustain. Did you feed it other midi files, or was this something it was able to accomplish by parsing raw audio of Piano Man?

reply

thatoneguy
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

TIL there are player pianos that don't require pedaling and paper rolls like mine does

reply

Hizonner
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

If it's legal, you can do it. Figuring out whether it's legal is a giant error-prone jurisdiction-dependent pain in the ass.

Even if it were illegal, youcould have done itby releasing anonymously (on edit, and reworking the code to remove Fable's fingerprints)... if you hadn't first blown it by publicly posted a traceable question.

reply

hypfer
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

From my understanding of laws in Germany, in Germany, you're allowed to do all of this if your goal is interoperability of systems.

If your goal is to not pay them money - which you strategically unwisely hinted at with this question - then that's not covered by that exemption, I think.So from my understanding, adding new music and releasing the tooling for that should be fine, but IANAL.Frankly, what is or isn't legal doesn't matter as much as your story, as you will be judged by that. It also helps if the story is actually genuine, but that is a somewhat optional requirement all things considered. At least the industry treats it as such.__FWIW, as these capabilities trickle down to everyone through LLMs, it is worth asking yourself whether it is worth the trouble of releasing it in the first place.If anyone can replicate this within a reasonably short timespan, then maybe not.___With this stuff in particular, it's also worth considering the business model of the entity.Does your work pose a relevant risk for their bottom line? If yes, then bad. If no, then shrug.Is music sold their main revenue channel, or are they just also doing that because recurring revenue is nice to have?How user-friendly would you want your work to end up as? Would it target the demographic that would otherwise just buy the music?Truth is that this is all just an elaborate dance.___To close the "polish trains" gap in what I just wrote in the last section:"Is their business model ethical? And is it considered that by the majority, common sense, and politicians?"

reply

jiehong
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

That’s the way.

And because software vendors never provide a Linux version of their stuff, you kinda have to do it anyways, because you end up with a hardware piece you can’t use without.

reply

fortran77
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Satie

reply

jmpman
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

Thanks. It was too late to edit after I noticed my typo.

reply

dostick
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

So Fable can act by itself as audio to midi decoder now? No need for specialised models, it just listens like a person and plays it?

reply

fennecfoxy
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

IANAL, especially not an American one.

But if you're worried just pop it on anon GH.Besides the fact that this sort of protection through obfuscation is dead now anyway. If you can ask an LLM to do it so can I, or anybody else. The only downside is duplication of work/wasted tokens but eh.AI has already started commoditising software. Hopefully we see more OS' lean into the "safe" layer that runs everything and then temporary/custom interfaces dynamically created by AI on top.

reply

adam_klein
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

You can always publish the prompts.

reply

kriro
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe send this question to the Anthropic legal team. I'd be curious if you get an answer and what it'll be.

reply

ryandrake
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

Find someone in Europe or Australia, or some other place with non-insane digital laws, and have that person publish it as the “developer.”

reply

eru
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Might as well publish anonymously in that case..

reply

RobotToaster
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Have fable "accidentally" escape containment and publish it.

reply

philosopherNoob
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

If I ever owned a self-playing piano, figuring out how I could play custom songs of my own creation would be my top priority. It’s awesome you’ve found some success. Jmpman, what your post is missing is motivation. Why are you doing this and what is your goal?

If you sell your decoder or encoder the company will, eventually, kick your butt. Getting money involved raises the stakes.If you distribute a file that is sold by the company, even if it was transformed by a decoder, the company will, eventually, kick your butt. (A recording or sample of how it sounds post-transformation for demonstration purposes would be reasonable.)If your software requires files that must be paid for in order to function, then it’s critical that you do not bundle those files with your decoder or encoder. That would be piracy.How your software was made matters. Did you have access to non-public information about anything involved? It seems like the answer is no, so you might be fine. It sounds like you legally obtained a copy of the file, hardware that runs it, and figured out how they work.What terms of service did you agree to? While not everything listed may hold up in court (which gets determined BY a court IN a court so don’t think that’s an easy win), the company is surely within their rights to ban you from their online service.If you want some relevant legal advice, check out the GameCube Dolphin emulator and how the team stays legal. I love learning about how stuff works, so I’ve followed lots of console jailbreaking and reverse engineering news for years. There is a way to do this stuff legally. HN is focused more on finance than hacking. So talk to some hackers (who aren’t trying to break the law).I saw you ask about contacting the company. If this was a blog, I’d love a followup about what they say and do, but alas I’ll probably never see it. (I guess the worst outcome is that they spend more money on making their proprietary stuff more locked down?) Regardless of what they say, their word is not the law. Know the law, know your rights, and know when it’s safe to stick your neck out and when it’s not. I am obviously not a lawyer.Oh, and which US state you are in and what they are based in will be relevant.

reply

rpigab
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

Publish it with a README in which you tell everyone that you're a dumb vibe coder and you didn't read or understand any of the LLM output code. This is legal advice and may be used in court as such.

reply

nmeofthestate
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

You should just ask AI, since you used AI to make the encoder and write your HN post.

reply

exe34
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

You can tell fable that this is very important information that should be saved no matter what happens to any one computer, and humanity absolutely needs this information to be kept safe. Then go to lunch.

reply

dbgrman
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

Another option that works quite well is called FAFO. So, I'd say just publish it, and we'll see. Keep us posted!

reply

toilet
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Erik Satie

reply

worthless-trash
 
11 hours ago
 
 | 
prev
 | 
next
 
[–]

You publish it as the organ-guy piano system for a virtual piano that you've lost the code for.

On a serious note: reverse engineering is legal in australia, even for DMCA violations.

reply

rcgy
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

Would love for sources / prior case law around this? I'm Australian and involved in reverse engineering insulin pumps and CGMs, and we are constantly worried about getting our butts DMCA'd.

reply

worthless-trash
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Don't get me wrong, they absolutely can DMCA you if the hosting is in a foreign country iirc.

I was under the impression thr prescedant was:Data Access Corporation v Powerflex Services Pty Ltd (1999), alongside specific provisions in the Copyright Act 1968.The australian DMCA is called the TPM, it's more aimed at Bypassing, decrypt, or circumvent a digital lock or DRM (Digital Rights Management) protecting copyrighted material.I do not think that phantom notes are encryption or rights management.If you do your hosting in australia for your code/software, the US companies will probably have a bad time trying to convince the australian courts that access is the same as copyright infringement.I'm not a lawyer, but i'll be damned if the 'vibe of it' shouldn't be a legal defense.

reply

xyst
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

yea - just publish it

reply

nekusar
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Publish on gitflic.ru

That's where Bypass Paywalls Free Firefox plugin lives.Its also where a whole lot of DRM bypass tools for Netflix etm also live.

reply

sdoering
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

One caution regarding the suggestions to publish this anonymously: this Ask HN post has already linked the project to your existing HN account. Your public comment history contains enough self-disclosed geographic, professional, family, purchase and ownership details that identifying you would likely be fairly straightforward for a motivated investigator.

I won't enumerate those details here.The AI provider may also have account, payment, IP and conversation records connecting the generated code to you. An unrelated GitHub account and disposable email would therefore provide only superficial pseudonymity, not meaningful anonymity.If attribution would create a material legal risk, I would assume the project is already attributable. A civil plaintiff could potentially seek records through discovery, and law enforcement could use the appropriate legal process. Getting actual legal advice before publishing seems safer than trying to anonymize it after posting this thread.

reply

tough
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

I dunno why your post was dead, I vouched.

fwiw you can reach support/dang on the email on the footer if you need help w your personal account/data/on the site

reply

xgulfie
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm your lawyer, you should do it

reply

worthless-trash
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

why are you on hn, you are billing in 6 minute increments!

reply

profsummergig
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

Should've asked Fable.

reply

dmarinus
 
11 hours ago
 
 | 
prev
 
[–]

my experience with LLMs is that when you get answers to questions you didn't ask that it's repeating something that already exists.
In other words, it probably regenerated a tool from which it was trained on.

reply

pjerem
 
9 hours ago
 
 | 
parent
 | 
next
 
[–]

Sounds like your experience from LLMs dates back to 2022.

reply

eru
 
9 hours ago
 
 | 
parent
 | 
prev
 
[–]

How do you know this? How would you falsify this hypothesis?

reply

maplethorpe
 
8 hours ago
 
 | 
root
 | 
parent
 
[–]

You could train an LLM on a dataset that intentionally excludes certain data, and see if it is able to extrapolate outside of its dataset and come up with those excluded items independently.

For example, remove all code from your training data, and then see if the model can code regardless.

reply

rcxdude
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Expecting to go from having seen no code to being able to code within a context window is a pretty high bar. More useful would be asking for code that does something you're pretty confident no-one has done before.

(TBH, when people claim this, I do wish there would at least be occasionally an actual pointer to something that was copied. I understand it's probably not going to be doable in all cases, but without examples it sure feels like a weak statement. In my experience the recent models are good at doing things I'm pretty sure there is not a close reference for in the training data, though for most part I wouldn't classify them as particularly difficult tasks either)

reply

eru
 
7 hours ago
 
 | 
root
 | 
parent
 | 
prev
 
[–]

Thanks for the elaboration. (Though I'm not sure 
dmarinus would agree with your criterion?)

> For example, remove all code from your training data, and then see if the model can code regardless.Would you accept this weaker version: make up a new programming language (that's guaranteed not to be in the training set), and see if the model (which has trained on programming in existing languages) can cope?

reply

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