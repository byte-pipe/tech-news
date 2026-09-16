---
title: America's Driver's License Breach Is a National Security Disaster | Lawfare
url: https://www.lawfaremedia.org/article/america%27s-drivers-licence-breach-is-a-national-security-disaster
site_name: hackernews_api
content_file: hackernews_api-americas-drivers-license-breach-is-a-national-secu
fetched_at: '2026-09-16T10:38:14.098672'
original_url: https://www.lawfaremedia.org/article/america%27s-drivers-licence-breach-is-a-national-security-disaster
author: hn_acker
date: '2026-09-16'
description: The latest edition of the Seriously Risky Business cybersecurity newsletter, now on Lawfare.
tags:
- hackernews
- trending
---

* ## Tom Uren

Meet The Authors

Subscribe to Lawfare

America's Driver's License Breach is a National Security Disaster

Last week, Krebs on Securitybroke the story ofa newly launched dark web service calling itself Nexus that was selling access to identity documents, including 3 million travel documents and 153 million driver's licenses from U.S. and Canadian citizens. This is a huge breach that not only will be used for run-of-the-mill cybercrime but also will feed the intelligence machines of America's adversaries.

Nexus claimed that it had gained unauthorized access to a major identity verification company and had spent more than a year "continuously" exfiltrating new data into a private database. Krebs on Securitynoted that in a single day the number of licenses in the database increased by nearly 400,000, suggesting regular ingestion of new data.

Krebs on Security was able to verify that the driver's licenses held by the service were genuine. In addition to Krebs’s own, it contained licenses from nine of his friends and family members. Secretary of War Pete Hegseth, an assistant director at the FBI and other high-ranking U.S. government officials also had licenses in the mix.

Based on a variety of circumstantial evidence, Krebs linked the incident to identity verification service IDScan.The service's websitesays it helps to reduce fraud by confirming that an ID is authentic and being presented by its legitimate owner and by detecting fraudulent documents.

TheFBI is looking into the incident, and IDScan hasconfirmed it is investigatinga data breach. The Nexus service also disappeared from the dark web shortly after Krebs published his story, although the people responsible for the hack do not claim to have deleted the data. Presumably they are lying low till the publicity dies down.

Licenses and identity documents can be used to facilitate identity theft and phishing attacks, but because the data can be used to inform intelligence operations, an incident like this also has national security implications.

For the intelligence world, licenses are particularly valuable because they're key identity documents and license numbers are often used in other databases. These databases, whether hacked or purchased, become much more valuable when records can be linked directly to a particular person with home address and photo included.

And it's not a theoretical threat.

In the mid-2010s, Chinese cyber espionage actors stole complementary data from a variety of sources that, together, would be useful for analyzing the U.S. intelligence apparatus. Various Chinese APT groups stole information from thehealth insurance company Anthem, creditreporting company Equifax,Marriott hotels,United Airlines, and, perhaps most significantly, security clearance information from theOffice of Personnel Management.

The U.S. intelligence community is certain that stolen data was used to counter American intelligence efforts against China, asdescribedinthis seriesofForeign Policy articlesby Zach Dorfman.

Of course, China itself isn't known for releasing detailed reports describing how it exploits its stolen data, but investigative research outfit Bellingcat has shown exactly how similar data can be used to uncover covert government activity.

In 2022,a hacked databaseprovided a key piece of travel information thathelped Bellingcat identifya deep coverGRU agent(Russian military intelligence) trying to infiltrate a NATO command post in Naples, Italy. And in another striking example,thesethreeBellingcatreportsfrom 2018 identified suspects in theattempted assassination of Sergei Skripalwith the Novichok nerve agent.

Clearly, leaked and hacked databases are incredibly useful for Bellingcat's Russia-related investigations. In 2020,it saidit had "acquired dozens of leaked databases over the past few years, giving us a large number of data points to cross-reference and verify any new data we acquire."

If a small investigative outfit is hoovering up Russian data when it is leaked, you can bet your bottom yuan that China's intelligence services are doing the same for any American data that pops up.

The IDScan breach is big. The number of U.S. licenses in the database is roughly 63 percent of thecountry's total licenses. But breaches from identity verification companies occur depressingly frequently. In the past two years, breaches have occurredat AU10TIX, at Discord'sage verification service provider 5CA, and atNational Public Data.

Identity verification services are necessary to help to prevent fraud but are also a point of vulnerability when security is poorly done. The sheer volume of sensitive data these services handle means they should be subject to strict regulation and oversight.

We're realists here at Seriously Risky Business, though, and recognize that there is no chance of swift government action. In the short term, we can only hope that significant financial consequences will help encourage these firms to shore up their security. Law firms are alreadylining up class-action suitsagainst IDScan, but a little federal government attention from the Federal Trade Commission wouldn't be unwelcome either.

The U.S. Military's Ad-Tracking Fig Leaf

Back in June, Reutersreported thatcommercial location data was being used to target U.S. military personnel in the Middle East. At the time,we wrotethat the Department of Defense's existing policies regarding the issue, which already included disabling advertising identifiers on military-owned devices, did "not fill us with confidence." They simply weren't comprehensive enough.

It turns out that these policies weren't even being well implemented.

This week, Reutersreportedthat some branches of the U.S. military have finally gotten around to disabling some advertising identifiers on military-owned devices.

The U.S. Air Force said it disabled Windows and Android advertising identifiers in late July, although they were already disabled on Apple devices. The Army told Reuters it disabled advertising identifiers on Android and Apple devices by default in February. And U.S. Special Operations Command said that identifiers on Windows computers were "recently" disabled.

Turning off these advertising identifiers is a fundamental mitigation that should have been implemented years ago. The U.S. militarywas first briefedin 2016 about the potential for commercial location data to be used to track its people to sensitive locations. In a striking 2018 example, an Australian Twitter userpointed outthat Strava's global heat map could be used toidentify U.S. military basesand even service members' jogging routes.

Disabling advertising identifiers on military devices is also an incomplete solution. It makes it harder to track them, but not impossible. And as it happens, many U.S. service members also use personal devices. Having a locked-down work phone is step one, but having good policies for personal devices is equally important.

Disabling advertising identifiers by default is the simplest short-term measure that might improve operational security (OPSEC), but it is impossible to know if it will make much of a difference without assessing the U.S. military's OPSEC posture holistically. Does disabling advertising identifiers on government devices reduce risk to an acceptable level? Probably not.

It's good that the U.S. military is finally disabling advertising identifiers by default. But we’re concerned the military has no idea how effective it will be.

"White Hats" Are Kidding Themselves

Over the weekend, self-proclaimed white-hat hackers stole$320 million worth of Bitcoinfrom the Liquid Network cryptocurrency platform. By Wednesday, the hackers had returned 85 percent of the funds, but kept around $47 million.

In recent years, there has been a regular drumbeat of steal-first-claim-reward-later hacks. We begrudgingly categorize several of these as successes as the perpetrators have not (yet) been arrested or jailed.

In 2021, a hackerstole $610 million worthof cryptocurrency from Poly Network. This waseventually returned in full, minus the  company's offer of $500,000 for the attacker it referred to as Mr White Hat.

Hacks ofMultichain (2022),Huobi (2023), andTender.fi (2023)had similar outcomes: Millions were stolen and returned, with the hackers taking a cut of tens or hundreds of thousands in cryptocurrency as a "reward" or "bug bounty."

The standout example is the 2022 hack of Mango Markets, in which a hacker extracted $110 million from the decentralized exchange. The individual responsible, Avraham Eisenberg,described his actions at the timeas a "highly profitable trading strategy." He claimed all his actions were legal and he used the protocol as designed, "even if the development team did not fully anticipate all the consequences of setting parameters the way they are."

Eisenberg returned $67 million to Mango Markets to recapitalize it, and the Mango community voted to give him a cool $47 million for his time. Eisenberg wasconvicted of fraud in a 2024 jury trial, but those convictions wereoverturnedby a U.S. judge last year.

In our view, the perpetrators of these hacks are deceiving themselves. By returningmostof the money, they're deluding themselves into thinking they're acting responsibly. As for consequences, the law won't chase me down if I return the majority and the victim says it's fine … right?

In Eisenberg's case, it did turn out to be right. But the FBI has been clear that victims cannot guarantee that perpetrators will not be prosecuted.

One wrinkle in the Liquid Network case is, as far as we can tell, the company never agreed toallowthe hacker to keep a 15 percent cut.

It feels possible that this self-proclaimed good guy might have to spend some of that $47 million on a good lawyer.

Three Reasons to Be Cheerful This Week:

1. More options for trusted defenders:Last week, Googlelaunchedthe Fairwind Program, its version of equivalentAnthropic's Project GlasswingandOpenAI's Trusted Accessinitiatives to limit more advanced AI cyber capabilities to vetted cyber defenders. On the same day,it launchedGemini 3.8 Flash Cyber, a cyber-specific version of its latest model that will be available through its Fairwind Program. Google says the model delivers "frontier-level" performance in vulnerability detection and patching but is far cheaper than competitor models.
2. Sality botnet takedown:Last week,the U.S. Department of JusticeandEuropol announcedthat an international operation had disrupted the Sality botnet. The botnet was first detected way back in 2003, and its peer-to-peer architecture meant there was no single point of failure that authorities could attack. CrowdStrike'sblog on the takedownsays that for the past eight years the botnet's primary payload, known as EggJagger, monitored the compromised host's clipboard for cryptocurrency wallet addresses and replaced them with addresses controlled by the malware operator.
3. U.S., U.K. to collaborate on scam networks:British and American authoritieshave signeda memorandum of understanding to collaborate on efforts to tackle scam compounds.

Risky Biz Talks

In ourlatest "Between Two Nerds" discussion, Tom Uren andThe Grugqtalk about whether AI will help cyber defense in critical infrastructure and organizations that are below the cyber poverty line.

FromRisky Bulletin:

Ukraine's top prosecutor resigns amid scam call center scandal:Ukraine's top prosecutor, Ruslan Kravchenko, resigned on Monday over allegations that individuals in his office were taking bribes to protect scam call centers operating across the country.

His resignation comes after investigators from Ukraine's main anti-corruption body, the National Anti-Corruption Bureau (NABU),arrestedSerhiy Kropyva, the deputy head of the Department of International Cooperation, a top lieutenant in Kravchenko's Office of the Prosecutor General.

In areportlast week, NABU claimed it uncovered a major scheme in Kravchenko's office, where one of his department heads was taking bribes to look the other way when it came to a network of call centers that was calling Ukrainians and foreigners and luring them into fake investment platforms that stole their money.

[moreon Risky Bulletin]

BEC campaign steals 35 million euros from French notaries:Hackers have stolen more than 35 million euro from French notaries in a massive business email compromise campaign over the past four years.

The attackers breached companies via phishing, took over their networks, and slowly and silently modified transaction details to hijack wired payments.

According to French newspaperLe Monde, the campaign hit more than 500 victims, or about 7 percent of all French notary offices.

[moreon Risky Bulletin]

Russia tells data centers to deploy drone defenses:The Russian government has instructed data center operators to deploy protections against drone strikes and other physical threats as part of a national effort to boost defenses at critical infrastructure organizations.

Companies that fail to follow the Kremlin's instructions risk having their operations put under the state's administration.

Russian President Vladimir Putin signed apresidential decreelast month allowing the state to temporarily take over the operations of critical infrastructure operators who fail to protect against Ukrainian hacks and drone strikes, or who take too long to repair damage.

[moreon Risky Bulletin]

Topics:

Cybersecurity & Tech


 Back to Top
 

### Tom Uren


 Read More
 


 Tom Uren writes Seriously Risky Business, a big-picture, policy-focused cyber security newsletter. He also co-hosts the Seriously Risky Business and Between Two Nerds podcasts that appear on the Risky Business News feed. He was formerly a Senior Analyst in the Australian Strategic Policy Institute's (ASPI) Cyber Policy Centre where he contributed to various projects including on offensive cyber capabilities, information operations, the Huawei debate in Australia and end-to-end encryption.
 









}


## More Articles

* ### Why We Opted Not to Work at the AI LabsBharat ChandarKevin FrazierSep 15, 2026As AI labs draw professors and students away from universities, society risks losing the expertise to govern what those labs build.
* ### The Global Data Center Boom Is a Gift to SpiesSara ShahTal FeldmanSep 10, 2026A Chinese company doesn’t need to hack Silicon Valley; it can simply rent the server next door.
* ### GPS and the Limits of ControlIsobel PorteousMatt KaplanSep 9, 2026What AI can learn from Selective Availability, the governance technology once used to pace GPS.

## Other Topics

* Armed Conflict
* Congress
* Courts & Litigation
* Criminal Justice & Rule of Law
* Cybersecurity & Tech
* Democracy & Elections
* Executive Branch
* Foreign Relations & International Law
* Intelligence
* States & Localities
* Surveillance & Privacy
* Terrorism & Extremism

## Subscribe to Lawfare

Email Address 
*
 

First Name 

Last Name 

Newsletters 

* Today on Lawfare
* The Week That Was

Bot Input

 Subscribe