---
title: 'Fedware: 13 Government Apps That Spy Harder Than the Apps They Ban'
url: https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/
site_name: hackernews_api
content_file: hackernews_api-fedware-13-government-apps-that-spy-harder-than-th
fetched_at: '2026-03-31T11:22:20.099142'
original_url: https://www.sambent.com/the-white-house-app-has-huawei-spyware-and-an-ice-tip-line/
author: speckx
date: '2026-03-30'
published_date: '2026-03-28T18:17:42.000Z'
description: The White House app ships with a sanctioned Chinese tracking SDK, the FBI app serves ads, and FEMA wants 28 permissions to show you weather alerts.
tags:
- hackernews
- trending
---

White House App

3 Trackers, GPS + Biometrics

 Version 47.0.1 requests precise GPS, fingerprint access, storage modification, auto-start at boot, draw over apps, and Wi-Fi scanning for a news app.
 

FBI Dashboard

4 Trackers + AdMob Ads

 The FBI's official app has 12 permissions, 4 trackers including Google AdMob. It serves targeted ads while reading your phone identity.
 

FEMA App

28 Permissions

 28 permissions for an app that shows weather alerts. AP News delivers the same disaster coverage with a fraction of the permissions.
 

CBP Passport Control

7 Dangerous Permissions

 Background location tracking, camera, biometrics, full storage access. Faceprints retained for up to 75 years across DHS, ICE, and FBI.
 

Mobile Fortify

200M+ Face Database

 ICE field agents carry this facial recognition app. Pulls from 200M+ DHS/FBI/State images plus 50B Clearview AI scraped images via $9.2M contract.
 

SmartLINK

$2.2B ICE Monitor

 Collects geolocation, facial images, voice prints, pregnancy data. ICE contract gives them "unlimited rights to use, dispose of, or disclose" all data.
 

Venntel / Data Brokers

15B Location Points/Day

 DHS, FBI, DOD, and DEA buy location data from 250M+ devices without warrants, bypassing the Supreme Court's Carpenter ruling entirely.
 

IRS-ICE Data Deal

1.28M Names Shared

 IRS shared tax data with ICE, erroneously included thousands who should never have been on the list. The acting IRS Commissioner resigned in protest.
 

GAO Oversight Failure

60% Ignored Since 2010

 Nearly 60% of 236 GAO privacy and security recommendations from 2010 onward remain unimplemented. Congress was told twice to pass privacy law. It has done neither.
 

The federal government released an app yesterday, March 27th, and it's spyware.

Listen to this article

0:00

--:--

1x

Failed to load audio

TheWhite House appmarkets itself as a way to get "unparalleled access" to the Trump administration, with press releases, livestreams, and policy updates. The kind of content that every RSS feed on the planet delivers with one permission: network access. But the White House app, version 47.0.1 (because subtlety died a long time ago), requestsprecise GPS location, biometric fingerprint access, storage modification, the ability to run at startup, draw over other apps, view your Wi-Fi connections, and read badge notifications. It also ships with3 embedded trackersincluding Huawei Mobile Services Core (yes, the Chinese company the US government sanctioned, shipping tracking infrastructure inside the sitting president's official app), and it has an ICE tip line button that redirects straight to ICE's reporting page.

This thing also has a "Text the President" button that auto-fills your message with "Greatest President Ever!" and then collects your name and phone number. There's no specific privacy policy for the app, just a generic whitehouse.gov policy that doesn't address any of the app's tracking capabilities.

The White House app might actually be one of the milder ones. I've been going through every federal agency app I can find on Google Play, pulling their permissions fromExodus Privacy(which audits Android APKs for trackers and permissions), and what I found deserves its own term. I'm calling it Fedware.

Ok so let me walk you through what the federal government is running on your phone.

The FBI's app,myFBI Dashboard, requests 12 permissions including storage modification, Wi-Fi scanning, account discovery (it can see what accounts are on your device), phone state reading, and auto-start at boot. It also contains4 trackers, one of which is Google AdMob, which means the FBI's official app ships with an ad-serving SDK while also reading your phone identity. From what I found, the FBI's news app has more trackers embedded than most weather apps.

The FEMA app requests28 permissionsincluding precise and approximate location, and has gone from 4 trackers in older versions down to 1 in v3.0.14. Twenty-eight permissions for an app whose primary function is showing you weather alerts and shelter locations. To put that in context, the AP News app delivers the same kind of disaster coverage with a fraction of the permissions.

IRS2Go has3 trackers and 10 permissionsin its latest version, and according to aTIGTA audit, the IRS released this app to the public before the required Privacy Impact Assessment was even signed, which violated OMB Circular A-130. The app shares device IDs, app activity, and crash logs with third parties, and TIGTA found that the IRS never confirmed that filing status and refund amounts were masked and encrypted in the app interface.

Permission Audit: Federal Apps vs. Civilian

Source: Exodus Privacy

Application

Permissions Requested

Count

Trackers

Federal Government Apps

FEMA

0

1

White House

0

3

CBP Passport

0

0

myFBI Dashboard

0

4

IRS2Go

0

3

MyTSA

0

1

Civilian News / RSS Apps

Feedly

0

0

AP News

0

2

Sorted by permission count descending

Hatched = dangerous permissions

MyTSA comes in lighter with9 permissions and 1 tracker, but still requests precise and approximate location. The TSA's ownPrivacy Impact Assessmentsays the app stores location locally and claims it never transmits GPS data to TSA. I'll give them credit for documenting that, because most of these apps have privacy policies that read like ransom notes.

CBP Mobile Passport Control is where things get genuinely alarming. This one requests14 permissions including 7 classified as "dangerous": background location tracking (it follows you even when the app is closed), camera access, biometric authentication, and full external storage read/write. And the whole CBP ecosystem, from CBP One to CBP Home to Mobile Passport Control, feeds data into a network that retains your faceprints forup to 75 yearsand shares it across DHS, ICE, and the FBI.

The government also built a facial recognition app calledMobile Fortifythat ICE agents carry in the field. It draws fromhundreds of millions of imagesacross DHS, FBI, and State Department databases. ICE Homeland Security Investigations signed a$9.2 million contract with Clearview AIin September 2025, giving agents access to over 50 billion facial images scraped from the internet. DHS's own internal documents admit Mobile Fortify can be used to amass biographical information of"individuals regardless of citizenship or immigration status", and CBP confirmed it will"retain all photographs"including those of U.S. citizens, for 15 years.

Photos submitted through CBP Home, biometric scans from Mobile Passport Control, and faces captured by Mobile Fortify all feed this system. And the EFF found that ICEdoes not allow people to opt out of being scanned, and agents can use a facial recognition match to determine your immigration status even when other evidence contradicts it. A U.S.-born citizen was told he could be deported based on a biometric match alone.

SmartLINKis the ICE electronic monitoring app, built by BI Incorporated, a subsidiary of the GEO Group (a private prison company that profits directly from how many people ICE monitors), under a $2.2 billion contract. The app collects geolocation, facial images, voice prints, medical information including pregnancy data, and phone numbers of your contacts. ICE's contract gives them"unlimited rights to use, dispose of, or disclose"all data collected. The app's former terms of service allowed sharing "virtually any information collected through the application, even beyond the scope of the monitoring plan." SmartLINK went from 6,000 users in 2019 to over 230,000 by 2022, and in 2019, ICE used GPS data from these monitors to coordinate one of the largest immigration raids in history, arresting around 700 people across six cities in Mississippi.

And if you think your location data is safe because you use regular apps and avoid government ones, the federal government is buying that data too. Companies likeVenntel collect 15 billion location points from over 250 million devices every daythrough SDKs embedded in over 80,000 apps (weather, navigation, coupons, games). DHS, FBI, DOD, and the DEApurchase this data without warrants, creating a constitutional loophole around the Supreme Court's 2018 Carpenter v. United States ruling that requires a warrant for cellphone location history. The Defense Department evenpurchased location data from prayer apps to monitor Muslim communities. Police departments used similar data to track racial justice protesters.

And then there's theIRS-ICE data sharing deal from April 2025. The IRS and ICE signed a Memorandum of Understanding allowing ICE to receive names, addresses, and tax data for people with removal orders. ICE submitted 1.28 million names. The IRSerroneously shared the data of thousands of people who should never have been included. The acting IRS Commissioner, Melanie Krause,resigned in protest. The chief privacy officer quit. One person leaving changes nothing about the institution, and the data was already out the door. A federal judge blocked further sharing in November 2025, ruling it likely violates IRS confidentiality protections, but by then the IRS was already building an automated system to give ICE bulk access to home addresses with minimal human oversight. The court order is a speed bump, and they'll find another route.

The apps, the databases, and the data broker contracts all feed the same pipeline, and no single agency controls it because they all share it.

Surveillance Data Pipeline

Federal App → Enforcement

 Data Source

 Processing

 Enforcement

TheGAO reported in 2023that nearly 60% of 236 privacy and security recommendations issued since 2010 had still not been implemented. Congress has been told twice, in 2013 and 2019, to pass comprehensive internet privacy legislation. It has done neither. And it won't, because the surveillance apparatus serves the people who run it, and the people who run it write the laws. Oversight is theater. The GAO issues a report, Congress holds a hearing, everyone performs concern for the cameras, and then the contracts get renewed and the data keeps flowing. It's working exactly as designed.

The federal government publishes content available through standard web protocols and RSS feeds, then wraps that content in applications that demand access to your location, biometrics, storage, contacts, and device identity. They embed advertising trackers in FBI apps. They sell the line that you need their app to receive their propaganda while the app quietly collects data that flows into the same surveillance pipeline feeding ICE raids and warrantless location tracking. Every single one of these apps could be replaced by a web page, and they know that. The app exists because a web page can't read your fingerprint, track your GPS in the background, or inventory the other accounts on your device.

You don't need their app. You don't need their permission to access public information. You already have a browser, an RSS reader, and the ability to decide for yourself what runs on your own hardware. Use them.

Fedware Knowledge Check

Test what you learned about US government app surveillance

Progress

0/10 answered

Question 1

How many embedded trackers does the White House app contain?

0

1

3

7

Question 2

Which Chinese company's tracking SDK is embedded in the White House app?

Tencent

Huawei

ByteDance

Xiaomi

Question 3

Which FBI app tracker is used for serving targeted advertisements?

Google Firebase Analytics

Google AdMob

Facebook SDK

OneSignal

Question 4

How many permissions does the FEMA app request?

9

14

28

42

Question 5

How long does DHS retain faceprints collected through CBP apps?

5 years

15 years

Up to 75 years

Indefinitely

Question 6

How much is CBP's contract with Clearview AI worth?

$1.5 million

$9.2 million

$22 million

$2.2 billion

Question 7

How many location data points does Venntel collect per day?

500 million

3 billion

15 billion

100 billion

Question 8

What private prison company's subsidiary built SmartLINK for ICE?

CoreCivic

GEO Group

Palantir

Northrop Grumman

Question 9

What Supreme Court case ruled that warrants are required for cellphone location history?

Riley v. California

Carpenter v. United States

Katz v. United States

Smith v. Maryland

Question 10

What percentage of GAO privacy recommendations from 2010 onward have still not been implemented?

25%

40%

Nearly 60%

80%

Submit Quiz

0/10

Your Score

0

Correct

0

Incorrect

0

Unanswered

Retake Quiz