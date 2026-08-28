---
title: 'I''m 12. A senior dev broke my app. Then he became User #001 - DEV Community'
url: https://dev.to/koda2026/im-12-a-senior-dev-broke-my-app-then-he-became-my-first-user-meh
site_name: devto
content_file: devto-im-12-a-senior-dev-broke-my-app-then-he-became-use
fetched_at: '2026-08-28T12:25:20.285776'
original_url: https://dev.to/koda2026/im-12-a-senior-dev-broke-my-app-then-he-became-my-first-user-meh
author: Harun - solo dev
date: '2026-08-27'
description: Two days ago, my Dev.to post went viral. I gained 400 followers in a single night. And then the... Tagged with ai, buildinpublic, webdev, beginners.
tags: '#ai, #buildinpublic, #webdev, #beginners'
---

Two days ago, my Dev.to post went viral. I gained 400 followers in a single night.

And then the worst thing a solo founder can experience happened:My signup page threw a 500 error to every single person who tried to join.

I was at a family wedding. Eating biryani. Dancing. When I checked my phone, there was a notification from a senior developer named@nyaomaru:

"I tried your interesting app, but I couldn't make an account. POST https://... 500 Internal Server Error. Please check your netlify server log. 👍"

My heart stopped. 💔

The most humiliating thing for a 12-year-old solo dev? Having a senior engineer publicly point out that your production database is broken while hundreds of people are watching.

## 🕵️‍♂️ The 48 Hours That Changed Everything

Instead of laughing at me, the Dev.to communityrallied.

@publiflow(a SaaS founder) was already deep in my comments debatingvisibilitychangestate management and optimistic UI patterns. He treated me like an equal, not a kid.

@sanukhandev(a Tech Lead with 13 years of experience) wrote:

"Good Luck and keep building — Live Young Live FREE!! feel free to connect if you need any help fellow developer"

He called me"fellow developer."I almost cried. 🥹

So I opened Supabase on my POCO C55, in the middle of the wedding reception, and started debugging production SQL triggers between slices of cake.

### The Bug That Almost Broke Me

Turns out I had THREE layers of bugs stacked on top of each other:

1. ❌ A missingis_championcolumn (I forgot to add it when I built the Code Jam feature).
2. ❌ A hidden leftover trigger onauth.usersfrom an older build.
3. ❌ A type-mismatch bug in my referral trigger (text <> uuid— Postgres refused to compare them).

Senior engineers get paid serious money to find bugs like #3. I found it at 12 years old, on a 6.5-inch Android screen.

I ran the nuclear SQL fix to build an "un-killable" trigger:

create
 
or
 
replace
 
function
 
public
.
handle_new_user
()

returns
 
trigger

language
 
plpgsql

security
 
definer

as
 
$$

begin

 
insert
 
into
 
public
.
profiles
 
(
id
,
 
username
,
 
referral_count
,
 
is_ambassador
,
 
is_champion
)

 
values
 
(
new
.
id
,
 
coalesce
(
new
.
raw_user_meta_data
->>
'username'
,
 
split_part
(
new
.
email
,
 
'@'
,
 
1
)),
 
0
,
 
false
,
 
false
)

 
on
 
conflict
 
(
id
)
 
do
 
nothing
;

 
return
 
new
;

exception
 
when
 
others
 
then

 
raise
 
warning
 
'PROFILE CREATION FAILED: %'
,
 
sqlerrm
;

 
return
 
new
;

end
;

$$
;

Enter fullscreen mode

Exit fullscreen mode

I deployed. I messaged nyaomaru:"Please try again!"

## 🎯 The Plot Twist

A few minutes later, nyaomaru replied:

"I checked that I can make account! Well done 👍 Happy coding! 😸"

Then I opened my Supabaseprofilestable and saw it:username: nyaonyao0725

The senior dev who found my bug, tested my app in Incognito, and gave me UX advice became KODA User #001.😭 He reacted to my post with 💖 and 🦄. That was the moment I realized: the Dev.to community isn't just an audience. It's a family.

## 👀 The "Guest Mode" Epiphany

While I was fixing that 500 error, I realized something even bigger was wrong with my app:The Login Wall.

Think about it from a stranger's perspective. You click a link, and a 12-year-old is asking for your email and password.Are you going to sign up? Probably not.

So, I builtGuest Mode.

Now, anyone can click "👀 Try KODA as Guest" and immediately start chatting with the AI. No email. No password. Zero friction. They get to experience the magic instantly.

But here is the growth hack: After they send 3 messages, the AI gently nudges them:

"You are in Guest Mode! I don't save chats for guests. Create a FREE account to save your history, join the Code Jam, and unlock the full Dojo! 🏆"

I learned a massive SaaS lesson that day:Let them taste the magic before you ask for their email.

## 🏰 The Database Logs Told Me A Story

After the bug was dead, I checked mychatstable to see what real humans were asking my AI mentor. What I saw broke me in the best way possible:

* 🇮A Tamil-speaking userasked:"Vanakam da mapla"and"Tamil pesuvaya". My AI replied in flawless Tamil. I built a multilingual mentor just by adding one line to my system prompt:"ALWAYS reply in the SAME language the user writes in."
* 🎮A user asked:"Me want to create a app"and"Which app to create a game". My AI acted like a Product Manager, giving them a decision matrix and a full 5-session game-dev lesson plan.
* 📚Another user asked:"teach me git"then"Explain simply like I am 5". My AI gave them the "Magic Notebook" analogy.

9 strangers from around the world are actively learning to code inside an app I built on my Android phone. That is not a metric. That is a mission.

## 🎉 The 1,000 Follower Moment

This morning, while eating ice cream at the wedding reception, my follower count ticked from 999 to1,006.

I didn't tell my parents. To them, I'm just their 12-year-old son at a wedding. They don't know what Supabase is. They don't know what a Dev.to algorithm is. And that's okay.

But 1,006 developers from Brazil, Dubai, Japan, and the US know. They clicked follow because they saw a kid with a POCO C55 and a dream, and they said:"I'm watching this one."

## 🏆 The Gift (Still Running!)

To celebrate, I launched theFirst-Ever KODA Code Jam. It's a 7-day global coding event:

* The Mission:Build a single-page website for a niche market.
* The Rule:At least 50% of your code must be co-written with KODA.
* The Prize:Champion Status forever + featured interview on Dev.to.
* Timeline:Aug 27 – Sept 2.

👉Read the full announcement & join the Code Jam here

Every legendary founder has a "scar." Mark Zuckerberg's was the server crashing when Harvard flooded Facebook.My scar is the Supabaseon_auth_user_createdtrigger.

It means I didn't just build a toy project. I built a real product, put it in front of real people, the real world broke it, and this community helped me fix it.

Thank you to@nyaomaru,@publiflow,@sanukhandev, and the 1,006 of you who believed in me.

Let's build. 🏗️

— Harun, solo dev, age 12

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse