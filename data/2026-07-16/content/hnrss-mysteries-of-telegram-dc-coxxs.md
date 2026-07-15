---
title: Mysteries of Telegram DC - Coxxs
url: https://dev.moe/en/3025
site_name: hnrss
content_file: hnrss-mysteries-of-telegram-dc-coxxs
fetched_at: '2026-07-16T03:37:13.565041'
original_url: https://dev.moe/en/3025
author: Coxxs
date: '2026-07-15'
published_date: '2022-05-09T20:33:00+00:00'
description: Mysteries of Telegram Data Centers
tags:
- hackernews
- hnrss
---

Telegram claims to have 5 data centers (DCs), referred to as DC1~5 in Telegram’s code and documentation. Among them, DC1 and DC3 are located in Miami, USA; DC2 and DC4 are in Amsterdam, Netherlands; and DC5 is in Singapore.

Telegram’s 
operation status

Each account is associated with a DC upon registration anddoes not changewith the user’s phone number or geographic location. Users cannot freely choose a DC—if connected to the wrong DC, the server returns an error message, requiring the client to connect to the correct DC associated with the account.

## Starting with the Frequently Down DC5

Among the 5 DCs, DC5 is particularly well-known in the Chinese Telegram community—not because it quietly serves a large number of Chinese users, but because it frequently goes down.

When DC5 is down, users on DC5 cannot use Telegram, and the topic in Telegram circles often becomes, “Why is DC5 down again?” DC5 users can only wait for their constantly “reconnecting” clients to recover, then join group chats with users from other DCs to criticize DC5.

## The Mystery of DC2 and DC3

To satisfy the curiosity of group members, someone created a bot to query the DC a user is on. So, group members started checking their DCs:

* Users registered with a +86 phone number found themselves on DC5 (Singapore), about to experience the next downtime.
* Users registered with a +1 phone number were on DC1 (Miami, USA), enjoying both connection speed and stability.
* Users registered with European phone numbers found themselves on DC4 (Amsterdam, Netherlands), becoming the rarest in the Chinese Telegram community.

Huh? Wait… Doesn’t Telegram claim to have 5 DCs? What about DC2 and DC3?

By searching the bot’s messages, there were 360 users on DC1, 50 on DC4, and 390 on DC5. DC2 and DC3 had 0.

Through “big data queries” of the bot’s messages, it seems there are indeed no users from DC2 or DC3.

Thus, somespeculatedthat DC2 and DC3 have no users, while othersanalyzed and speculatedthat DC2 and DC3 are subordinate DCs to DC1 and DC4, respectively, accepting user registrations when their parent DCs are busy.

Is that really the case?

## Telegram DC Allocation Rules (2022-05)

TL;DR:

* DC1, DC2, DC4, and DC5 are allocated based on thecountry codeof the phone number providedat registration. These 4 DCs accept new user registrations at any time and have a large number of existing users.
* DC3 once had users, but around 2020, DC3’s existing usersmay have been transferred toDC1. DC3 currently likely has no users and no longer accepts new registrations.

In other words, DC2 actually has a large number of users, and like other DCs,as long as the country code of the phone number at registration falls within DC2’s range (e.g., +49 Germany), the user will definitely be assigned to DC2. Meanwhile, DC3, though still operational, likely has no associated users.

Since there are many users on DC2, why did the bot above never detect any DC2 users?

This is because the bot’s method of retrieving DCs is flawed.

## Which DC Am I Actually On?

There are currently 3 common methods to determine a DC. Below, we will register a new DC2 account and try these 3 methods.

### Method 1 (Login Method)

Using a phone number that would be assigned toDC2, we connect toDC1via Telegram’sMTProto protocol(the same protocol used by the official client), call theauth.sendCodeinterface, and attempt to send a verification code to register an account.

At this point, the server returns aPHONE_MIGRATE_2error, indicating that the client should connect to DC2 (if the same operation is performed after connecting to DC2, the verification code is sent directly).

This way, we know this account is a DC2 account.This method also works for already registered accounts, but it requires knowing the user’s phone number, making it difficult to query group members’ DCs.

### Method 2 (Profile Picture/File Method)

After registering the DC2 account (referred to as the new account below), we use a third-party client (Plus Messenger) that displays a user’s DC,log in with another account, and check the new account’s DC. However, the client cannot display the DC until we upload a profile picture for the new account, after which it shows the new account is on DC2.

This is because the third-party client retrieves the user’s DC from thedc_idfield in theuserProfilePhotostructure of the MTProto protocol when downloading the user’s profile picture.

This method determines the user’s DC based on the DC where the user’s uploaded files are stored.

If you log into a third-party client with the new account to check your own DC, it may use Method 1 to determine the DC, as the client knows which server it is connected to.

### Method 3 (Web CDN Method)

Finally, we use the bot mentioned earlier to query the new account’s DC.

The bot says the account is on data center DC4 (Amsterdam, Netherlands).

Huh? Isn’t this new account on DC2? Why does the bot say it’s DC4?

It turns out the bot determines the user’s DC via Telegram’s Web CDN. If we open https://t.me/dctest** and check the source code, we find that the new account’s profile picture domain starts with cdn4, causing the bot to identify it as DC4.

Since DC2 and DC3 “borrow” the domains of DC4 and DC1 in the same location to provide Web CDN services, the bot cannot identify any DC2 users—they are all mistaken for DC4 users.

Another type of bot requires users to send an image/file to determine their DC. This is similar to Method 2 and can accurately identify a user’s DC.

## The Disappearance of DC3

After correctly determining users’ DCs using Method 2, we found that globally (especially in overseas groups), DC2 users are not uncommon, but DC3 users are extremely rare. After extensive searching, we found two users on DC3:@urie**and@flowinglig**.

However, further analysis reveals they may not actually be on DC3. For example, callingphotos.GetUserPhotosto view the profile picture list shows that@urie**uploaded 7 profile pictures, only two of which are on DC3, with newly uploaded pictures on DC1.

Similarly, checking the images in the message history of both users shows only a few old images stored on DC3, with new images stored on DC1. In contrast, users on other DCs have their images stored on their respective DCs.

Additionally,@urie**sent a file to a DC identification bot (File Method) in 2021 for testing, and the result was also DC1.

Unfortunately, since we cannot access their phone numbers, we cannot accurately test using Method 1 (Login Method). We can only infer through Method 2 (Profile Picture/File Method) that they were transferred from DC3 to DC1.

To further confirm that DC3 no longer accepts new users, we generated over 10,000 phone numbers from various global regions and tested Telegram’s DC allocation rules using Method 1 (Login Method). The results are as follows:

During testing, we ensured each number connected to the wrong DC whenever possible—to understand the actual DC corresponding to the number via the returnedPHONE_MIGRATE_Xerror and to avoid generating excessive spam SMS, causing harassment or bankruptingPavel Durovwith SMS fees.

After testing, we filtered out numbers confirmed to be on DC4, then reconnected the remaining numbers to DC4 to ensure no numbers assigned to DC3 were missed.

Based on the above analysis, we can conclude that DC3 indeed no longer accepts new users, and existing users have likely all been transferred to DC1.

Although we couldn’t find the missing DC3, if you want to become a user on a specific DC, avoid DC5’s downtime risks, or test whether a bot is reliable, you can now refer to the previous image and register with a phone number from a specific country code.

Since Telegram’s server and some operational mechanisms are not open-source, many conclusions in this article are based on speculation. If you find errors in the article or have additional clues, please feel free to comment.

The following projects and content were referenced during the writing of this article, and I would like to express my gratitude:

* Telegram DC Analysis Reportby Hertz
* Which DC is My Telegram Account On?(Web CDN Method) by oott123
* GramJS
* Plus Messenger (Profile Picture Method)
* @WooMaiBot (Web CDN Method)
* @where_is_my_dc_bot (File Method)

Coxxs

This article (https://dev.moe/en/3025) is an original work by Coxxs. Please credit the original link when reposting.