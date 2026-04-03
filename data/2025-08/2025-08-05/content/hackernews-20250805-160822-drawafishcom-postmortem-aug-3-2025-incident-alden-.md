---
title: DrawAFish.com Postmortem — Aug 3, 2025 Incident - Alden Hallak
url: https://aldenhallak.com/blog/posts/draw-a-fish-postmortem.html
site_name: hackernews
fetched_at: '2025-08-05T16:08:22.263417'
original_url: https://aldenhallak.com/blog/posts/draw-a-fish-postmortem.html
author: Alden Hallak
date: '2025-08-05'
description: A blameful postmortem of the DrawAFish.com security incident - lessons learned from vibe coding gone wrong.
---

DrawAFish.com

## TL;DR:

* Incident Duration:~6 hours (2AM–8AM EST)
* Impact:Username vandalism (slurs)Offensive fish approved / safe fish removed
* Username vandalism (slurs)
* Offensive fish approved / safe fish removed
* Root Causes:Legacy 6-digit admin password exposed in past data breachUsername update API lacked authenticationJWT not tied to specific user
* Legacy 6-digit admin password exposed in past data breach
* Username update API lacked authentication
* JWT not tied to specific user
* Mitigation:Manual reversal of mod actions, fixed authorization logic, backups reviewed
* Takeaway:hwoopsy daisy 🙂

Did you see? Did you see it? What it says? What it says on top of the website?

If you were on HackerNews onAug 1 2025, you may have seenDrawAFish.com.
 Because it was in the number 1 spot. You also may have seen it if you follow me oninstagram. You also probably saw
 that I was in the #1 spot on Hackernews there too. Because I posted about it a lot. And also if you
 talked to me in person you probably heard about it. And then you probably heard a lot of quotes fromThe Social Network(2010) where I replaced various words with "Fish."

 "A million fish isn't cool. You know what's cool?
A billion fish
."


If you read the post on Hackernews, you saw that the website was an exercise in
 vibe-coding. I used Copilot to implement features, and I used it to implement featuresfast.

In my career,[0]I have learned the art of "Blameless
 Postmortems." The problem with a Blameless
 Postmortem is that it doesn't really work when you're the sole contributor. So this is a blameful
 postmortem. And I blame me. (Not the LLM, sorry).

If you saw the website only on August 1, you probably do not understand why I need to write a postmortem
 at
 all. Everything went swimmingly (ha, ha). But if you had the displeasure of viewing my website between
 the hours of 2AM (20 minutes after I went to sleep) and 8AM (when I woke up)[1]EST on Aug 3, then you would have seen chaos. Every single username was
 transformed to a heinous slur, many unsavory fish had made it into the fishtank, and many beautiful fish
 were gone. How did this happen?

## The Vulnerabilities

This is not what they changed my username to. I'll let you use your
 imagination.

1. Legacy admin password exposed in data breach:When creating the website, I used
 my childhood username and my childhood 6-digit password for testing. I think the first time it
 leaked was on Neopets.com.[2]I then set up
 Google Auth. From then on, I only logged in with Google Auth. But the password remained. I
 simply forgot. This allowed some of the most intelligent and brilliant minds on the internet to
 find my password on the Neopets data leak paste, log in as an admin, and approve and disapprove
 some really disgusting and horrible fish.On the plus side, the brilliant minds (while attempting to ban every single user) managed to
 accidentally ban themselves. So that vulnerability was only an active issue for an hour or so.
2. Username update API lacked authentication:I vibe coded the profile backend,
 which allows users to modify their username. I added this feature last minute, figured I'd
 review it later, and then didn't. The username modification did not perform any auth logic
 whatsoever. whoopsy
3. JWT not tied to specific user:There was another security vulnerability - I
 used the JWT to authorize login, but never confirmed that the JWT token belonged to the userId /
 email associated with it in the admin actions. So you could log in with my username and password,
 grab the JWT, and then send that along with your request. While this was a mistake, it ended up
 saving me. Fortunately, hackernews user @iceweaselfan44used this vulnerability to authorize as an admin and
 delete the really bad fish. He was awake, on the other side of the world, removing fish and
 helping out.[3]

## The Recovery

Moderation logs. There are so many of these.

I woke up at around 7:45 am, saw a couple pings and messages, and immediately rushed to my desktop.[4]Fortunately, I had set up firebase backups.
 Unfortunately, I had set them up wrong. I spent a good hour or so diagnosing the errors and then quickly
 pushed changes to require authentication.

I had a mod log set up, so undoing the changes was as simple as writing an annoying script that just
 undid all the mod actions. Did I learn my lesson about vibe coding? Maybe. I vibe coded the script,
 looked over the code, and did a dry run first.

I banned the other mod account ran by IceWeasel[5]and
 patched the JWT bug - at which point he reached out to me and explained how he created it. We then
 hopped on a call and he took a look at the codebase, where he expertly suggested a refactor that would
 be more idiomatic with current security practices. And then when I blindly pushed it and it broke
 everything, he expertly committed some more changes that fixed it.

## Reflection

At this point, you're probably thinking: geeze man. Wow. youve gotta be stupid.

And I'd like to get on my hands and knees and beg for your suspension of belief when I say: yes I am but
 not when it comes to my job. It is really fun to just have high velocity, and it is really fun to not do
 code reviews and to just push stuff. Sometimes it feels like all I do at work is review code and write
 docs - and the code I write at work is lately deeply within legacy systems and makes my brain hurt
 sometimes. I have good reviews! Just ask my coworkers! The ones that hate me hate me because I leave TOO
 many comments and am TOO thorough (or they are jealous of my handsome good looks and devilish charm).

So when I decided to learn how to build on GCP and vibe code a small app that I figured a handful of
 people would see, I took it easy on the code reviews. I let Copilot do all the work, I wrote no tests,
 and instead of writing TODOs and Documentation I simply said "I'll remember to change my password / add
 auth / understand this code later." And then I didn't do that. Whoops!

It would be very nice for my ego to blame the LLM here. But LLMs are a tool. They let you generate a lot
 of code really fast, and sometimes that is good. Sometimes it is not. And it is up to you to review it,
 and decide what code gets committed.

I am selling these stickers for 100 dollars each. Please reach out to purchase
 them.

[0]Nearly 5 years at the same company.↩

[1]I usually try to sleep more than this. I want to sleep more than
 this. But my fancy "smart" ikea roller blinds that keep it dark at night and bright when I wake up
 fell down because I taped them to the wall very poorly.↩

[2]I remember being a kid and forgetting my password and thinking "wow
 it's nice how they just email you your password, instead of resetting it. More websites should do
 that."↩

[3]The JWT token issue was the only vuln that really required knowing
 how anything worked. I don't think it's a coincidence that there was a correlation between being a
 studious / diligent person and actively being a helpful force.↩

[4]Which is next to my bed. I live in New York.[4a][4a]You may have heard differently, especially if you saw mydoxxing[4b]on the unsavory website. Fortunately, my publicly listed
 information appears to be a little out of date.The first time I
 was doxxedwas much scarier.↩[4b]To be fair, I deserved the doxxing for removing the weird and
 offensive fish and slurs.↩↩

[5]Only because it had no identifying information at all - just didn't
 know who this person was. He reached out later and we chatted over discord and now we're cool.↩
