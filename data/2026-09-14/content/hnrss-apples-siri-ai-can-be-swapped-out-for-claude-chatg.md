---
title: Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows - MacRumors
url: https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/
site_name: hnrss
content_file: hnrss-apples-siri-ai-can-be-swapped-out-for-claude-chatg
fetched_at: '2026-09-14T16:47:37.381675'
original_url: https://www.macrumors.com/2026/09/14/siri-can-be-swapped-out-for-chatgpt-claude/
date: '2026-09-14'
description: Code sleuth "pdfu" has uncovered iOS 27 and macOS Golden Gate private frameworks that show Apple has designed its new Siri architecture to work with third-party AI models at what appears to be a surprisingly deep level. One mechanism called Model Delegation allows Claude to appear as a Siri extension in the same way as the existing built-in ChatGPT extension.
tags:
- hackernews
- hnrss
---

# Apple's Siri AI Can Be Swapped Out for Claude, ChatGPT, Code Shows

Monday September 14, 2026 4:37 am PDT
 by 
Tim Hardwick

Code sleuth "pdfu" has uncovered iOS 27 and macOS Golden Gate private frameworks that show Apple has designed its new Siri architecture to work with third-party AI models at what appears to be a surprisingly deep level.

One mechanism called Model Delegation allows Claude to appear as a Siri extension in the same way as the existing built-in ChatGPT extension. In pdfu's video,shared on X, the macOS user brings up the "Search or Ask" bar and chooses Claude as the AI model via an "Ask..." contextual menu.

After enabling the Claude extension, the user asks Siri to "Ask Claude" to set a reminder in Apple's Reminders app. Claude then interprets the natural language reminder request and Siri subsequently creates the reminder. The implication is that if the request requires access to an Apple system feature, Claude hands the task back to Siri.

In another example, Claude can be seen in a Siri app conversation window receiving a request to create a CSV file – something Siri itself cannot handle – and successfully returning the result.

What's more intriguing is the second protocol demonstrated in the video that appears to go considerably further, and could really open up the AI landscape for Apple software requests.

An inference provider in "Model Manager Services" apparently allows Apple's own server-side Siri model to be completely replaced by another model, such as GPT-5.6. In this scenario, ChatGPT receives Apple's Siri planner prompt and tool definitions, which enables it to request system actions, receive the resulting personal data, and formulate an answer that Siri presents using its own interface and voice.

And here's an app extension replacing Siri AI's server model with GPT-5.6 Terra. It uses the Inference Providing protocol in Model Manager Services.
GPT-5.6 receives Apple's native Siri planner prompt and tool definitions. It can make tool calls that perform system actions, and...pic.twitter.com/cz88kyq3io— pdfu (@itspdfu)September 13, 2026In the demonstration video, the user asks the ChatGPT model (within the Siri app) to find emails about a specific topic, summarize their contents and action points, then send a message to a person in the user's contacts via the Messages app. The response is then shown as logged in OpenAI's platform web interface.

The European Union's Digital Markets Act may have helped shape Apple's approach here, as it requires Apple to give third parties effective access to iOS hardware and software features available to Apple's own services, and the European Commission has specifically said this principle extends to Siri.

The "Ask..." implementation is currently limited to the ChatGPT extension in the macOS 27 Golden Gate Release Candidate (which is effectively the final version of the software set to be released later today), so Claude is not yet available. Meanwhile, Apple has not yet opened up the model delegation entitlement to third parties and it isn't front-facing to users, but it at least shows how extensively Apple has engineered Siri for future model interoperability.

Related Roundups: 
iOS 27
, 
iPadOS 27
, 
macOS Golden Gate
Tags: 
ChatGPT
, 
Claude
, 
Siri Guide
, 
Siri AI
Related Forums: 
iOS 27
, 
macOS Golden Gate
[ 
66 comments
 ]

Get weekly top MacRumors stories in your inbox.

Leave this field empty

## Popular Stories

### iOS 27 Introduces New 'iPhone Handoff' Feature

Wednesday September 2, 2026 12:35 pm PDT by 
Joe Rossignol
Apple has added a new "iPhone Handoff" feature to iOS 27 that will allow you to switch between two iPhones while using the same phone number on each device.This functionality was briefly mentioned during the WWDC 2026 keynote in June, on a slide that listed hundreds of new features coming in iOS 27 and corresponding software updates, but Apple never shared any further details at the time....

### Here's When iOS 27 Rolls Out Today in Every Time Zone

Sunday September 13, 2026 3:00 am PDT by 
Eric Slivka
Apple is about to release iOS 27, which will finally deliver more advanced Siri AI capabilities as well as a variety of other refinements, improvements, and new features to iPhones. It's Apple's biggest software update of the year, and Apple announced at Wednesday's iPhone event that it will be releasing iOS 27 sometime today – Monday, September 14.iOS 27 won't be the only release today,...

### Apple Announces iOS 27 Release Date

Wednesday September 9, 2026 10:46 am PDT by 
Joe Rossignol
At its event today unveiling the iPhone 18 Pro, AirPods 5, Apple Watch Series 12, and more, Apple announced that iOS 27 will be released later this month.iOS 27 has already been available as a developer beta since June and as a public beta since July, and Apple today said that the update will be released for all users with a compatible iPhone model on Monday, September 14.iOS 27 is...

## Top Rated Comments

U
unobtainium
5 hours ago at 04:41 am
As it should be. The “walled garden” approach no longer holds when so much of our daily work and lives exists on the device. People should be able to choose which services they trust and find most useful. Thanks EU!
Score:
 19 Votes (
Like
 | 
Disagree
)
QuarterSwede
4 hours ago at 05:17 am
you are being very polite
After 15 years, Siri is still as dumb as day 1
That’s not remotely true. Siri AI is a big improvement. It’s 
conversationally and contextually aware
 which makes it a lot more useful and what people generally want when asking it questions.
While playing Dogs by Pink Floyd, I asked it, “who’s playing the guitar?” It answered correctly in about 3 seconds.
Could old Siri have done that? Absolutely not.
Here’s the actual question in the Siri app where it gave an even more detailed answer. This is from my original question, I didn’t ask it again.
Score:
 9 Votes (
Like
 | 
Disagree
)
A
Alloween
5 hours ago at 04:43 am
For me this is good news! Because less reasons for EU to complain.
Score:
 7 Votes (
Like
 | 
Disagree
)
A
aidler
5 hours ago at 05:06 am
Pretty much proves that what the EU Commission said was true from the get-go, and that Apple was once again just causing unnecessary drama.
Score:
 6 Votes (
Like
 | 
Disagree
)
klasma
5 hours ago at 04:48 am
Siri AI
Now that’s an oxymoron if I’ve ever heard one
Aspirational Intelligence
Score:
 6 Votes (
Like
 | 
Disagree
)
obviouslogic
4 hours ago at 05:20 am
Pretty much proves that what the EU Commission said was true from the get-go, and that Apple was once again just causing unnecessary drama.
Doesn’t prove anything and it is not what the EU was asking, nor is this Apple’s answer to that. The EU wants every model to have unfettered access to your device and your data… No app currently has that, even Apple’s own OS (Spotlight, Siri AI, etc.) cannot access your data inside a 3rd party app. That 3rd party app has to allow it via the App Intents and Spotlight API’s.
Score:
 5 Votes (
Like
 | 
Disagree
)
Read All Comments