---
title: A hotel check-in system left a million passports and driver's licenses open for anyone to see | TechCrunch
url: https://techcrunch.com/2026/05/15/a-hotel-check-in-system-left-a-million-passports-and-drivers-licenses-open-for-anyone-to-see/
site_name: newsfeed
content_file: newsfeed-a-hotel-check-in-system-left-a-million-passports-a
fetched_at: '2026-05-15T19:34:12.329602'
original_url: https://techcrunch.com/2026/05/15/a-hotel-check-in-system-left-a-million-passports-and-drivers-licenses-open-for-anyone-to-see/
author: Zack Whittaker
date: '2026-05-15'
published_date: '2026-05-15T18:51:33+00:00'
description: The tech company that maintains the hotel check-in system set its cloud storage to public, allowing anyone to access customers' data without a password.
tags:
- techcrunch
- security
- age verification
- cybersecurity
---

A hotel check-in system left more than one million customer passports, driver’s licenses, and selfie verification photos to the open web after a security lapse. The data is now offline after TechCrunch alerted the company responsible.

The hotel check-in system,called Tabiq, is maintained by the Japan-based tech startupReqrea. According to its website, Tabiq is used in several hotels across Japan and relies on facial recognition and document scanning to check guests in.

Independent security researcherAnurag Sencontacted TechCrunch earlier this week after discovering that the system was leaking the sensitive documents of hotel guests from around the world. Sen said this was because the startup set one of its Amazon cloud-hosted storage buckets, which the check-in system uses to store customer data, to be publicly accessible. The data inside could be viewed by anyone using a web browser, without needing a password, by knowing only the bucket name: “tabiq.”

Sen alerted TechCrunch in an effort to help in notifying the company. Reqrea locked down the storage bucket after TechCrunch reached out to both the company and Japan’s cybersecurity coordination team,JPCERT.

This latest lapse underscores a recurring problem of companies exposing or spilling their customers’ personal information and sensitive documents — not through sophisticated attacks, but by failing to follow basic cybersecurity practices. Aside from arecent buzzof AI-discovered vulnerabilities andnew cybersecurity capabilities, oftentimes sizable security incidents stem from human error, misconfigurations, or failing to adhere to cybersecurity best practices.

In an email acknowledging the exposure, Reqrea director Masataka Hashimoto told TechCrunch: “We are conducting a thorough review with the support of external legal counsel and other advisors to determine the full scope of exposure.”

Reqrea said it does not know how the storage bucket became public. By default, Amazon’s cloud storage buckets are private. After a spate of exposed customer storage buckets a few years ago, Amazon added several warning prompts to customers before data can be made public, making this kind of lapse increasingly hard to do accidentally.

Hashimoto told TechCrunch that the company plans to notify affected individuals once it has completed its investigation.

It remains unclear whether anyone other than Sen accessed the exposed data before it was secured. Hashimoto said the company is reviewing its logs to determine if there had been any authorized access prior to securing the bucket.

Details of the exposed bucket were also captured byGrayHatWarfare, a searchable database that indexes publicly visible cloud storage. The bucket listing contains files dating back to early 2020 up to as recently as this month, and included identity documents of visitors from countries around the world.

The hotel check-in system lapse follows other incidents involving sensitive government-issued documents. Earlier this year, TechCrunch reported on the exposure of driver’s licenses, passports, and other identity documents uploaded by customers ofmoney transfer service Duc App. Adata breach at car rental service Hertz last yearsaw hackers make off with driver’s license information belonging to at least 100,000 customers.

These incidents come at a time when governments are increasingly rolling out age verification laws and private businesses are using “know your customer” checks to verify a person’s identity. Both rely on adults uploading sensitive documents, often to a third-party company, for verification, despite criticisms from cybersecurity experts. Data lapses can put people whose information was taken at greater risk of identity fraud or having their likeness misused as age verification requirementstake hold around the world.

Topics

age verification
, 
cybersecurity
, 
data exposure
, 
Exclusive
, 
Security
 

When you purchase through links in our articles,we may earn a small commission. This doesn’t affect our editorial independence.

			Zack Whittaker	

Security Editor

Zack Whittaker is the security editor at TechCrunch. He also authors the weekly cybersecurity newsletter,this week in security.

He can be reached via encrypted message at zackwhittaker.1337 on Signal. You can also contact him by email, or to verify outreach, atzack.whittaker@techcrunch.com.

 

View Bio