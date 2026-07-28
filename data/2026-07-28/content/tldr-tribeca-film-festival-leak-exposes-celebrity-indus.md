---
title: Tribeca Film Festival Leak Exposes Celebrity & Industry Data
url: https://www.expressvpn.com/blog/tribeca-film-festival-data-exposed/
site_name: tldr
content_file: tldr-tribeca-film-festival-leak-exposes-celebrity-indus
fetched_at: '2026-07-28T19:33:35.959045'
original_url: https://www.expressvpn.com/blog/tribeca-film-festival-data-exposed/
date: '2026-07-28'
description: A major data breach exposed 666,369 Tribeca Film Festival records — including sensitive PII and confidential documents tied to A-list talent and industry professionals.
tags:
- tldr
---

* Blog
* Research
* Tribeca Film Festival Leak Exposes Celebrity & Industry Data

# A-list directors, actors and celebrities exposed in major film festival data breach

Research

25.07.2026

7 mins

 Written by 

 Jeremiah Fowler 

Cybersecurity Researcher Jeremiah Fowler uncovered a data leak affecting a major film and cultural festival and shared his findings with
 
ExpressVPN
. We are publishing his report to help the public stay informed and protected as part of our ongoing effort to make the web a safer place.

I recently discovered a publicly accessible database that was not password-protected or encrypted and contained what appeared to be records associated with the Tribeca Film Festival.

Upon further investigation I uncovered an additionalthree separate unsecured databases: “development” (203,370 records), “staging” (224,999 records), and “production” (238,000 records).The total number of exposed records was 666,369, and timestamps ranged from 2019 to 2026. Multiple files also referenced a fourth database labeled as “CMS” (content management system) that was properly secured. While the latter was not publicly accessible, there are potential risks associated with identifying where internal data is stored.

A majority of the exposed records I saw in a limited sample were images, press kits, marketing materials, and documents (including some marked as confidential). Inside the database marked as “production,” there was a single backup .dump file that contained potentially sensitive information, including email addresses, phone numbers, IP addresses, and hashed passwords. The backup file contained a total of 295,916 records that included folders indicating 163,171 “users,” 15,488 “films contacts,” 13,535 “contacts,” and more.

Documents inside the databases and the name of the database indicated the files belonged to the Tribeca Film Festival. I immediately sent a responsible disclosure notice to multiple contacts associated with the Tribeca Film Festival, and the backup file was removed or restricted from public access the same day. The following day, I received a reply stating: “Thank you for bringing this information to our attention. We appreciate your responsible disclosure. Tribeca takes matters of data security very seriously and is actively investigating this issue.

It is not known whether the database was managed directly by the Tribeca Film Festival, Tribeca Enterprises, or by a third-party vendor, contractor, or service provider. Additionally, it is not known how long the database may have been publicly accessible before my discovery or whether anyone else may have accessed the exposed information and contact details of thousands of directors, actors, and attendees. Only an internal forensic investigation could determine whether any additional access occurred and establish the timeline of the exposure.

According toWikipedia, the Tribeca Film Festival is a major annual film, television, and cultural event based in New York City. Founded in 2002 by Robert De Niro, Jane Rosenthal, and Craig Hatkoff following the September 11 attacks, the festival was created to help revitalize Lower Manhattan and has since become one of the most prominent cultural events in the United States. Tribeca showcases feature films, documentaries, television premieres, immersive media experiences, podcasts, and discussions with creators from around the world.

This screenshot shows schema names, table names, and estimated row counts that included PII and contact information.

This image is a collage of screenshots showing individual lines containing contact details and names matching those of well-known individuals.

This screenshot shows a spreadsheet document that contained rows labeled: User ID, Unique Identifier (UID), Email Address, First Name, Last Name, Facebook Location, Address, Tribeca Cinemas Newsletter Subscription, Tribeca Film Newsletter Subscription, Film Newsletter Preference, General Newsletter Preference, Privacy Policy Acceptance, Tribeca Staff Status, Current Sign-In Date, Current Sign-In IP Address, Encrypted Password, Last Sign-In Date, and more.

This screenshot shows a spreadsheet containing email addresses alongside user-agent data, including device information, browser details, and source applications, highlighting potential risks related to user or device fingerprinting.

The document labeled “contacts” contained the names, addresses, phone numbers, and emails. The document contained names of prominent directors, producers, and filmmakers such as Martin Scorsese, Francis Ford Coppola, Guillermo del Toro, George Lucas, Ron Howard, Danny Boyle, Patty Jenkins and more. I also saw the contacts of well-known Hollywood Actors and Actresses. These included names such as Robert De Niro, Morgan Freeman, Michael Douglas, Angelina Jolie, Jennifer Lawrence, Kate Hudson, Winona Ryder, Neil Patrick Harris, Naomi Watts, Hilary Duff, Don Cheadle, Debra Messing, Rami Malek, Eva Mendes, Michael J. Fox, Sharon Stone, and many more.

While some contact fields contained information considered PII, some were blank or missing data, or contained the contacts of assistants or management that could be publicly available. It is also possible that some individuals may share the same name as known celebrities. A large number of these emails used services such as Yahoo, Gmail, Outlook, etc. indicating they could potentially be personal contacts. I am not implying or claiming that these individuals were ever at risk or that their information is part of a broader public exposure.

Hypothetically, publicly exposed internal data could provide criminals with a detailed view of non-public festival operations, potentially including information about participants, filmmakers, media assets, communications, and much more. This type of information could create privacy and security risks by revealing personal contact information that could be used for phishing, social engineering, identity correlation, impersonation attempts, or further reconnaissance of internal storage systems.

The passwords I saw were stored as what appeared to be Bcrypt cryptographic hashes, not encrypted passwords. Bcrypt hashing is a one-way process that transforms data into a fixed-value hash that cannot be reversed, whereas encryption is a two-way process that scrambles data using a key so it can later be decrypted back to its original form. Bcrypt is considered a secure method for storing passwords. Researchshowsthat its effectiveness can also depend on users and administrators creating strong, hard-to-guess passwords. As an ethical researcher, I never attempt to decrypt passwords or test the strength of exposed credentials.

Anyone who believes their information may have been involved in a data exposure should be aware of the common tactics criminals use in social engineering and phishing attempts. These can include unexpected emails, phone calls, or text messages that may even reference non-public information. Criminals often use details from data incidents to establish credibility and attempt to persuade individuals to disclose additional personal or financial information.

Always be suspicious of unexpected communications and requests for information. I recommend independently verifying that a person or organization is who they claim to be and only communicating through official channels. Avoid clicking unsolicited links or opening files that may contain malicious code or scripts. If it is identified that criminals are using the name of an individual or organization, it is important to report it so they can notify partners, customers, or others who may be targeted. I am not implying that there is an imminent risk of phishing, social engineering, or any type of fraud. I am only providing educational guidance regarding hypothetical real-world threat scenarios.

In my experience as a cybersecurity researcher, I often see that backup files are among the most overlooked assets when it comes to data security. Many organizations focus on protecting production systems while giving less priority to backups, exports, archives, or development environments. It is important to remember that backup files can sometimes contain complete copies of production data or include sensitive internal information. Backup files can become a single point of exposure if improperly secured. I recommend encrypting backup files and restricting access through authentication controls. Monitoring and logging can also help identify suspicious activity and unauthorized access.

In the U.S., the Federal Trade Commission (FTC) issued awarningabout the growing trend of scammers impersonating celebrities on social media. In 2025, FTC consumer protection datareportedthat financial losses linked to impersonation scams have risen fourfold among adults aged 60 and older over the previous several years.

The report states that losses exceeding $100,000 increased substantially, with total reported losses growing from approximately $55 million in 2020 to roughly $445 million in 2024. Although individuals of all ages have fallen victim to these schemes, older adults were significantly more likely to experience the largest financial impacts.

These scams are not unique to the U.S., and there have been numerous well-publicized cases from around the world. It is my personal opinion that the rise of deepfake technology will only increase the problem of impersonation.

I imply no wrongdoing by the Tribeca Film Festival, Tribeca Enterprises, or any affiliated organizations, contractors, vendors, partners, or service providers. I do not claim that any internal, employee, partner, attendee, or other user information was misused, accessed by unauthorized parties, or at imminent risk. Any hypothetical risk scenarios described in this report are presented solely for educational and awareness purposes and should not be interpreted as evidence of an actual compromise or malicious activity.

As an ethical security researcher, I do not download the data I discover. In my research, I review a limited number of records to verify and responsibly report on the nature of an exposure, as well as to document any publicly exposed information. My goal is to responsibly notify relevant parties and raise awareness about the importance of protecting potentially sensitive data.

Explore the web with greater privacy

 Get ExpressVPN 

Sign up today to enjoy our latest offers

 

Jeremiah Fowler

Jeremiah Fowler is an experienced cybersecurity researcher, journalist, and privacy advocate. With over a decade in the field, he has uncovered and responsibly reported some of the largest data breaches and has helped protect the personal data of millions of individuals, companies, and governmental organizations worldwide. His commitment to privacy, transparency, and data protection are reflected in his reporting and offering real world examples of why data privacy is important and how companies and individuals can be aware of potential risks.

* 0
* 0
 

* RELATED POST
* MORE FROM THE AUTHOR

20 best expat destinations for each life stage

ExpressVPN

11.06.2026

73 mins

Celebrities’ and influencers’ private communications exposed in stalkerware data breach

Jeremiah Fowler

30.04.2026

8 mins

Digital safety resources every activist should know about

ExpressVPN

14.04.2026

27 mins

How to help kids outsmart social media algorithms

ExpressVPN

03.04.2026

33 mins

Department stores and online retailers exposed in AI chatbot logs and audio recordings data leak

Jeremiah Fowler

17.03.2026

6 mins

 

Why your favourite football team could be your biggest cybersecurity threat

Jeremiah Fowler

23.06.2026

10 mins

Celebrities’ and influencers’ private communications exposed in stalkerware data breach

Jeremiah Fowler

30.04.2026

8 mins

Department stores and online retailers exposed in AI chatbot logs and audio recordings data leak

Jeremiah Fowler

17.03.2026

6 mins

Password security: What changed from 2015 to 2025

Jeremiah Fowler

06.03.2026

9 mins

149M Logins and Passwords Exposed Online Including Financial Accounts, Instagram, Facebook, Roblox, Dating Sites, and More.

Jeremiah Fowler

23.01.2026

9 mins

Popular AI Generator Exposed Over One Million Images Including DeepFakes and Nudify Face Swaps

Jeremiah Fowler

05.12.2025

7 mins

 

## ExpressVPN is proudly supporting

 

## Subscribe to the blog newsletter

Get the latest in privacy news, tips, tricks, and security guides to level-up your digital security.

Submit