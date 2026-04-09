---
title: Try This One Weird Trick Russian Hackers Hate – Krebs on Security
url: https://krebsonsecurity.com/2021/05/try-this-one-weird-trick-russian-hackers-hate/
site_name: hackernews
fetched_at: '2025-06-30T13:31:51.990457'
original_url: https://krebsonsecurity.com/2021/05/try-this-one-weird-trick-russian-hackers-hate/
author: air7
date: '2025-06-30'
---

In aTwitterdiscussion last week on ransomware attacks, KrebsOnSecuritynotedthat virtually all ransomware strains have a built-in failsafe designed to cover the backsides of the malware purveyors: They simply will not install on aMicrosoft Windowscomputer that already has one of many types of virtual keyboards installed — such as Russian or Ukrainian. So many readers had questions in response to the tweet that I thought it was worth a blog post exploring this one weird cyber defense trick.

The Commonwealth of Independent States (CIS) more or less matches the exclusion list on an awful lot of malware coming out of Eastern Europe.

The Twitter thread came up in a discussion onthe ransomware attack against Colonial Pipeline, which earlier this month shut down 5,500 miles of fuel pipe for nearly a week, causing fuel station supply shortages throughout the country and driving up prices. TheFBI saidthe attack was the work ofDarkSide, a new-ish ransomware-as-a-service offering that says it targets only large corporations.

DarkSide and other Russian-language affiliate moneymaking programs have long barred their criminal associates from installing malicious software on computers in a host of Eastern European countries, including Ukraine and Russia. This prohibition dates back to the earliest days of organized cybercrime, and it is intended to minimize scrutiny and interference from local authorities.

In Russia, for example, authorities there generally will not initiate a cybercrime investigation against one of their own unless a company or individual within the country’s borders files an official complaint as a victim. Ensuring that no affiliates can produce victims in their own countries is the easiest way for these criminals to stay off the radar of domestic law enforcement agencies.

Possibly feeling the heat from beingreferencedinPresident Biden’s Executive Order on cybersecuritythis past week, the DarkSide group sought to distance itself from their attack against Colonial Pipeline. In a message posted to its victim shaming blog, DarkSide tried to say it was “apolitical” and that it didn’t wish to participate in geopolitics.

“Our goal is to make money, and not creating problems for society,” the DarkSide criminals wrote last week. “From today we introduce moderation and check each company that our partners want to encrypt to avoid social consequences in the future.”

But here’s the thing:Digital extortion gangs like DarkSide take great care to make their entire platforms geopolitical, because their malware is engineered to work only in certain parts of the world.

DarkSide, like a great many other malware strains, has a hard-coded do-not-install list of countries which are the principal members of the Commonwealth of Independent States (CIS) — former Soviet satellites that mostly have favorable relations with the Kremlin. The full exclusion list in DarkSide (published byCybereason) is below:

Image: Cybereason.

Simply put, countless malware strains will check for the presence of one of these languages on the system, and if they’re detected the malware will exit and fail to install.

[Side note. Many security experts have pointed to connections between the DarkSide and REvil (a.k.a. “Sodinokibi”) ransomware groups. REvil was previously known asGandCrab, and one of the many things GandCrab had in common with REvil was thatboth programs barred affiliates from infecting victims in Syria.As we can see from the chart above, Syria is also exempted from infections by DarkSide ransomware. And DarkSide itself proved their connection to REvil this past weekwhen it announced it was closing up shop after its servers and bitcoin funds were seized.]

## CAVEAT EMPTOR

Will installing one of these languages keep your Windows computer safe from all malware? Absolutely not. There is plenty of malware that doesn’t care where in the world you are. And there is no substitute for adopting a defense-in-depth posture, and avoiding risky behaviors online.

But is there really a downside to taking this simple, free, prophylactic approach? None that I can see, other than perhaps a sinking feeling of capitulation. The worst that could happen is that you accidentally toggle the language settings and all your menu options are in Russian.

If this happens (and the first time it does the experience may be a bit jarring) hit the Windows key and the space bar at the same time; if you have more than one language installed you will see the ability to quickly toggle from one to the other. The little box that pops up when one hits that keyboard combo looks like this:

Cybercriminals are notoriously responsive to defenses which cut into their profitability, so why wouldn’t the bad guys just change things up and start ignoring the language check? Well, they certainly can and maybe even will do that (a recent version of DarkSide analyzed by Mandiantdidnotperform the system language check).

But doing so increases the risk to their personal safety and fortunes by some non-trivial amount, saidAllison Nixon, chief research officer at New York City-based cyber investigations firmUnit221B.

Nixon said because of Russia’s unique legal culture, criminal hackers in that country employ these checks to ensure they are only attacking victims outside of the country.

“This is for their legal protection,” Nixon said. “Installing a Cyrillic keyboard, or changing a specific registry entry to say ‘RU’, and so forth, might be enough to convince malware that you are Russian and off limits. This can technically be used as a ‘vaccine’ against Russian malware.”

Nixon said if enough people do this in large numbers, it may in the short term protect some people, but more importantly in the long term it forces Russian hackers to make a choice: Risk losing legal protections, or risk losing income.

“Essentially, Russian hackers will end up facing the same difficulty that defenders in the West must face — the fact that it is very difficult to tell the difference between a domestic machine and a foreign machine masquerading as a domestic one,” she said.

KrebsOnSecurity asked Nixon’s colleague at Unit221B — founderLance James— what he thought about the efficacy of another anti-malware approach suggested by Twitter followers who chimed in on last week’s discussion: Adding entries to the Windows registry that specify the system is running as a virtual machine (VM). In a bid to stymie analysis by antivirus and security firms, some malware authors have traditionally configured their malware to quit installing if it detects it is running in a virtual environment.

But James said this prohibition is no longer quite so common, particularly since so many organizations have transitioned to virtual environments for everyday use.

“Being a virtual machine doesn’t stop malware like it used to,” James said. “In fact, a lot of the ransomware we’re seeing now is running on VMs.”

But James says he loves the idea of everyone adding a language from the CIS country list so much he’s produced his ownclickable two-line Windows batch scriptthat adds a Russian language reference in the specific Windows registry keys that are checked by malware. The script effectively allows one’s Windows PC to look like it has a Russian keyboard installed without actually downloading the added script libraries from Microsoft.

To install a different keyboard language on a Windows 10 computer the old fashioned way, hit the Windows key and X at the same time, then select Settings, and then select “Time and Language.” Select Language, and then scroll down and you should see an option to install another character set. Pick one, and the language should be installed the next time you reboot. Again, if for some reason you need to toggle between languages, Windows+Spacebar is your friend.
