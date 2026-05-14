---
title: Twin brothers wipe 96 gov't databases minutes after being fired - Ars Technica
url: https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/
site_name: hackernews_api
content_file: hackernews_api-twin-brothers-wipe-96-govt-databases-minutes-after
fetched_at: '2026-05-14T11:37:03.952098'
original_url: https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/
author: jnord
date: '2026-05-12'
published_date: '2026-05-12T19:12:07+00:00'
description: A case study in why credentials are revoked before firings.
tags:
- hackernews
- trending
---

Text
 settings

In the US, fired and laid-off workers often have their digital credentials deactivated before they learn about the loss of their jobs; indeed, the inability to log in to a corporate system may be the first an employee knows of the situation.

Although not a generous or humane approach to staff reduction, it does follow from the simple fact that a fired employee with access to company systems is a security risk.

Just ask the Akhter twin brothers,accused of wiping out 96 databaseshosting US government information in the minutes after both were fired last year from their shared employer.

## DROP DATABASE

Muneeb and Sohaib Akhter, now both 34, had been in trouble before. Back in 2015, the brothers pled guilty in Virginia to a scheme involving wire fraud and computers. Muneeb was sentenced to three years in prison, while Sohaib got two.

After their stints in jail, the brothers worked their way back into the tech world. In 2023, Muneeb got a job with a Washington, DC, firm that sold software and services to 45 federal clients; Sohaib got a job at the same company a year later.

According to the government, however, the two couldn’t stay out of trouble. For instance:

On Feb. 1, 2025, Muneeb Akhter asked Sohaib Akhter for the plaintext password of an individual who submitted a complaint to the Equal Employment Opportunity Commission’s Public Portal, which was maintained by the Akhters’ employer. Sohaib Akhter conducted a database query on the EEOC database and then provided the password to Muneeb Akhter. That password was subsequently used to access that individual’s email account without authorization.

This was not a one-off. Muneeb had been assembling usernames and passwords—5,400 of them taken from his own company’s network data. He then built custom Python scripts to try these logins against common websites; for instance, his “marriott_checker.py” application tested the logins against Marriott’s hotel chains. Muneeb managed to log in successfully hundreds of times, including to DocuSign and airline accounts. Sometimes, if victims had airline miles stored, Muneeb would book travel for himself.

The brothers’ employer appears to have learned about their criminal past at some point in February. On February 18, 2025, the brothers—who lived together in Virginia—were both called into a Microsoft Teams meeting and summarily fired.

The call took place at the end of the day, wrapping up at 4:50 pm. Five minutes later, Sohaib was already trying to access his (now former) employer’s network—but found that his VPN access and Windows account were terminated.

Muneeb’s account had been overlooked, however, and he immediately embarked on a campaign of destruction.

At 4:56 pm, Muneeb accessed a US government database that his company maintained. He “issued commands to prevent other users from connecting or making changes to the database, and then issued a command to delete the database,” the government said.

At 4:58 pm, he wiped out aDepartment of Homeland Securitydatabase using the command “DROP DATABASE dhsproddb.”

At 4:59 pm, he asked an AI tool, “How do i clear system logs from SQL servers after deleting databases?” He later asked, “How do you clear all event and application logs from Microsoft windows server 2012?”

In the space of a single hour, Muneeb deleted around 96 databases with US government information. He downloaded 1,805 files belonging to the EEOC and stashed them on a USB drive, then grabbed federal tax information for at least 450 people.

## Smart ideas

While this was going on, the brothers held a running conversation. (The government is not clear about whether this took place over text, instant message, or in person.)

“I see you cleaning out their database backups,” Sohaib said as he watched Muneeb’s work. As the database casualty list grew, Sohaib said, “Alright—if you have good plausible deniability.”

Muneeb didn’t appear to consider his actions a big deal. “Eh, they can recover from yesterday,” he said, referring to daily database backups.

“Yeah, they could,” Sohaib agreed.

Muneeb noted that an employee they knew would “have some work to do” when the destruction was revealed.

Sohaib fed Muneeb more suggestions.

“Delete their filesystem as well?” he said.

“Smart idea,” said Muneeb.

Sohaib then wondered if they had been too hasty. Perhaps, he said, “You shoulda had a kill script. Like, blackmailing them for some money would have been—”

“No, you do not do that, that’s proof of guilt, man,” Muneeb said.

“No, but the thing was, you always have your opinion,” Sohaib complained, and the two then bickered about whether they might try to blackmail their company’s customers instead.

As the data destruction went on, Sohaib said, “They’re gonna probably raid this place.”

“I’ll clean this shit up,” Muneeb said.

After wiping out the databases and event logs, the brothers reinstalled the operating systems on their corporate laptops with the help of an unnamed co-conspirator.

## God guide my words

Sohaib was right—the feds did raid them. It just took three weeks.

On March 12, 2025, a search warrant was executed at Sohaib’s home in Alexandria. Agents grabbed plenty of tech gear but also turned up seven firearms and 370 rounds of .30 caliber ammunition. Given his former crimes, Sohaib should have had none of this.

The brothers remained free for another nine months as the investigation proceeded, but both were eventually arrested on December 3 and indicted for a host of crimes (you can read the indictment here).

Muneebsigned a plea dealon April 15, 2026, admitting to the major allegations in the indictment.

Sohaib took his case to trial. He lost. On May 7, 2026, a jury found him guilty of conspiracy to commit computer fraud, password trafficking, and possession of a firearm by a prohibited person. He will be sentenced in September.

The cases would seem to be basically over, except that Muneeb has begun filing handwritten petitions from jail, arguing that hislawyer has been ineffective. More recently, the filings have taken aim at his signed guilty plea.

 One of Muneeb’s letters from prison.
 

 One of Muneeb’s letters from prison.

 

“God guide my words,” he wrote in aone-paragraph letterto the judge on April 27. “I am uncomfortable with my plea and the pace with which the government expected it signed during pretrial motion deadlines limiting my ability to challenge the evidence against me… I stand with my brother in his innocence.” (As mentioned above, Sohaib was found guilty several days later.)

Anotherbrief handwritten letter, filed on May 5, claims that Muneeb is innocent of count 10, “since accessing DocuSign account does not grant anything of value nor did he obtain or intend to obtain anything of value from it.” It says nothing about deleting the 96 databases.

A third letter, also filed on May 5, asks for permission to proceedpro se—that is, with Muneeb functioning as his own lawyer. This is generally the “kiss of death” for federal cases. Still, like many intelligent-but-overconfident defendants with plenty of time on their hands, Muneeb wants to give it a shot. It may well turn out to be one more of his “smart ideas.”

Update: The company that employed the brothers went unnamed in court documents but was identified in the press asOpexus. An eagle-eyed Ars reader points out that, back in December, the company gave a series of quotes toCyberscoopabout the entire incident. Though Opexus did background checks, the company admitted that “additional diligence should have been applied,” it acknowledged that “the terminations were not handled in an appropriate manner,” and it said that “the individuals responsible for hiring the twins are no longer employed by Opexus.” Clearly, the failure here was all-encompassing.

 Nate Anderson
 

Deputy Editor

 Nate Anderson
 

Deputy Editor

 Nate is the deputy editor at Ars Technica. His most recent book is 
In Emergency, Break Glass: What Nietzsche Can Teach Us About Joyful Living in a Tech-Saturated World
, which is much funnier than it sounds.
 

1. 1.Twin brothers wipe 96 gov't databases minutes after being fired
2. 2.Altman forced to confront claims at OpenAI trial that he's a prolific liar
3. 3.The newest AI boom pitch: Host a mini data center at your home
4. 4.Amazon employees are "tokenmaxxing" due to pressure to use AI tools
5. 5.Solar drone with jumbo jet wingspan broke a flight record—then it crashed

Customize