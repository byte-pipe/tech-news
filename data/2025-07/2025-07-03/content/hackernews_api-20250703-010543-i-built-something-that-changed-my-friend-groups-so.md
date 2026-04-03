---
title: I built something that changed my friend group's social fabric
url: https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/
site_name: hackernews_api
fetched_at: '2025-07-03T01:05:43.791702'
original_url: https://blog.danpetrolito.xyz/i-built-something-that-changed-my-friend-gro-social-fabric/
author: dandano
date: '2025-06-28'
published_date: '2025-06-28T05:16:52.000Z'
description: I built something that changed my friend group's social fabric
tags:
- hackernews
- trending
---

This is a story that started back in 2022, but I think its a perfect time to reflect on the impact that it has had on my friend group still to this day.

A year or so before COVID, our friend group dispersed across the world - I moved to Vancouver, one friend moved to the UK and another one moved to the United States. The rest of them still lived in Melbourne.

Once COVID hit, like many others, we looked to find a way to keep in contact and still hang out. We have always been a big gaming group (both board game & video games) so moving online seemed like a logical choice. We had always used Discord so we started to ramp up our time there.

### The problem

Over the next year, our group chat (in Signal) was drowning in notifications. A mix of general chit chat, talks on the ever changing news of COVID and the most important - when can people play games and chat. It really annoyed me when people would post on "hey anyone wanna play [game] in 15 mins?", for it to be buried in another 5 messages. The message would have to be constantly bumped in Signal before we eventually jumped in a voice chat in our Discord server. My friends were also annoyed that they didn't know we were playing a certain game tonight, for us to go "we talked about it on Signal!". Something had to change.

### The solution

I thought, rather than people typing in Signal that they want to play a game in Discord, it would be better for Discord to notify us when someone has joined a voice channel in our server. Now you're probably thinking "Daniel, wouldn't this just be another notification that people would miss?" - you would be right to be skeptical, but I thought that since it was a distinct notification from Discord rather than Signal it would be better.

I went to Discord to find a setting to send a notification to the server when someone joined a voice channel, and I came up with crickets. There was no such thing. Eventually I found that you can write a Discord bot to leverage theon_voice_state_updatefromdiscord.py, a Discord API wrapper. So I spun up a new git repo and got to work writing a simple Discord bot. Here is main guts of the bot.

Sinceon_voice_state_updatetriggers on when a member joins or leaves a voice channel and if the member muted or deafened - we must check that thebeforechannel is null and theafterchannel is not null to signify that they have joined a voice channel.

We then get the first text channel of the server so that our bot can send the message to the server. Then we actually send the message to the text channel. I added thedelete_afteroption so that the text channel is not clogged up with all the messages sent from the bot. All we care about is receiving the notification. Finally, I add a record into a postgres table (hosted onSupabase) of the Discord server (guild), the member id and member display name along with a timestamp of when they joined. All this juicy data will come in handy later.

I originally hosted the bot on fly.io. But I've been on a mission to learn more about self-hosting, so I bought a server from Hetzner and it runs on same server as this blog usingCoolify.

I added the bot to the server with the appropriate permissions and we are live! Here's what it looks like.

Notification on discord desktop client
Notification on iPhone

### The reaction

My friends had mixed views when I initially told them. It was a 50/50 split between 'that sounds useful', to 'that sounds dumb and I won't use it'. The hardest part was convincing people to download the Discord app on their phone as most of us didn't have it downloaded.

Only a few months later, I had moved back to Melbourne and was with my friends on a sunny afternoon at a pub. My friend, Jack, who was initially in the 'I wont use it' camp, completely changed his tune. He said that it encourages him to jump into Discord not even to play games but just to have a quick chat with everyone and to socialize.

The batsignal of our group

I quickly realized that this has not just reduced the amount of messages around organizing to play games, it acted as a Batsignal for our friends to hang out. I estimated that over 60% of the time when people join Discord, it's just to have a chin-wag about our day and not to play a game.

## The results

Since I had been keeping a record of each time someone joined Discord, I now had years worth of data to see some trends (as of 27th June 2025).

Year

Times joined

Days joined

2022

2374

318

2023

3181

345

2024

3503

352

2025

1378

171

Even I am staggered on how much we use Discord. Our sessions varies a lot from 5-30 mins to nights of multi-hour gaming sessions. All of my friends are in their 30s and with a few of us being first-time Dads. Being one of those Dad's - it was a life savior when my little one was a newborn to jump onto Discord for even 5 minutes to chat with my friends, watch someone play a game and then log off for another diaper change. Our group has gone from primarily text-based chat to chatting on Discord most nights - it's reminiscent of picking up the landline back in the 90s and calling your friends.

This is how I feel when I join Discord with my friends

Every year we have an annual Christmas party for our friends and since last year I've been doing a 'Discord Wrapped' (cross with the Dundies from the Office) - where I announce who has joined Discord the most as well as providing each person with stats around their year on Discord. It's been such a fun way to recap the year and see trends of our activity.

My stats for 2024
The leaderboard for 2024

### Conclusion & what's next

I didn't realize the impact this would have on our group, but I'm very grateful I had a few hours to spare one Sunday to quickly whip this Discord bot up.

I plan to add achievements based on who you hung out on Discord and some other fun ideas, as well as tracking when you left Discord to get those juicyhours spentstats.

I also had this idea to turn this into an IoT device that has 5 RGB lights and sits on your desk. It would light up when each friend you have delegated joins your Discord voice channel and you could customize the colour for each friend. If I get some traction I might turn it into a real product, so email me at my email address in my about page if that seems something you'd like.
