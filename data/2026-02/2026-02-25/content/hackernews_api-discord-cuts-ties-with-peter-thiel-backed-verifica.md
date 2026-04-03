---
title: Discord cuts ties with Peter Thiel-backed verification software after code found in US surveillance | Fortune
url: https://fortune.com/2026/02/24/discord-peter-thiel-backed-persona-identity-verification-breach/
site_name: hackernews_api
content_file: hackernews_api-discord-cuts-ties-with-peter-thiel-backed-verifica
fetched_at: '2026-02-25T06:00:16.165756'
original_url: https://fortune.com/2026/02/24/discord-peter-thiel-backed-persona-identity-verification-breach/
author: Catherina Gioino
date: '2026-02-24'
description: Discord cut ties with its age-verification partner after exposed code fueled federal-reporting concerns, months after a breach hit 70,000 users.
tags:
- hackernews
- trending
---

Cybersecurity
Social Media

# Discord cuts ties with Peter Thiel–backed verification software after its code was found tied to U.S. surveillance efforts

By

Catherina Gioino
Catherina Gioino
Down Arrow Button Icon
By

Catherina Gioino
Catherina Gioino
Down Arrow Button Icon
February 24, 2026, 3:02 AM ET
Add us on
Persona, partially funded by Peter Thiel’s venture firm Founders Fund, continues to provide age verification services for OpenAI, Lime, and Roblox.
Eva Marie Uzcategui/Bloomberg via Getty Images

Communication platform Discord is under fire after its identity verification software, Persona Identities, was found to have front-end code accessible on the open internet and on government servers.

Recommended Video

Nearly 2,500 accessible files were found sitting on a U.S. government-authorized endpoint,researchers pointed out on X. The files showed Persona conducted facial recognition checks against watchlists and screened users against lists of politically exposed persons.

In addition to verifying a user’s age, researchers found Persona performs 269 distinct verification checks, including screening for “adverse media” across 14 different categories such as terrorism and espionage. It then assigns risk and similarity scores to user information.

And the information was openly available. “We didn’t even have to write or perform a single exploit, the entire architecture was just on the doorstep,” wrote the researchers in their blog, adding they found 53 megabytes of data on a Federal Risk and Authorization Management Program (FedRAMP) government endpoint that also “tags reports with codenames from active intelligence programs.”

Discord has since announced it is cutting ties with Persona. The AI software, partially funded by Palantir cofounder Peter Thiel’s venture firm Founders Fund, continues to provide age verification services for OpenAI, Lime, andRoblox.

Both Persona and Discord confirmed toFortunetheir partnership lasted for less than a month and has since dissolved. According to Discord, only a small number of users were part of this test, in which any information submitted could be stored for up to seven days before it would be deleted.

## Discord’s safety overhaul missteps

This isn’t the first time a third-party vendor has come under scrutiny for mishandling sensitive user information for Discord, which is popular among gamers, students, influencers, tech professionals, and other communities.

Last year, hackers accessed the government IDs of more than 70,000 who had complied with its age-verification requirements.

In astatementfrom Oct. 9, 2025, the company said the attack was “not a breach of Discord, but rather a breach of a third party service provider, 5CA.” Discord stated the breach affected only users who communicated with the company’s Customer Support or Trust and Safety teams.

“At Discord, protecting the privacy and security of our users is a top priority. That’s why it’s important to us that we’re transparent with them about events that impact their personal information,” the statement added. Affected users received an email if their government IDs, IP addresses, or limited billing and corporate data were leaked.

And earlier this month, Discord faced almost immediate backlash afterannouncingit would default all accounts to teen-safety settings. Users seeking access to additional features would be required to verify their age using Persona.

“Rolling out teen-by-default settings globally builds on Discord’s existing safety architecture,” Discord’s head of product policy Savannah Badalich said in the statement. The company “will continue working with safety experts, policymakers, and Discord users to support meaningful, long-term wellbeing.”

But after users quickly pointed out the October data hack, Discord amended the statement the following day to clarify that age verification would remain optional unless users wished to access age-restricted servers and channels.

Discord said it could determine the ages of most users using the “information we already have.” Most users would not have to upload government IDs and instead could opt for video selfies.

“We offer multiple privacy-forward options through trusted partners,” the addendum stated, adding “facial scans never leave your device. Discord and our vendor partners never receive it.”

Any identifying documents uploaded to Discord would be submitted to the platform’s third-party vendors and deleted quickly. “In most cases, immediately after age confirmation,” read the statement.

“IDs are used to get your age only and then deleted,” it continued. “Discord only receives your age—that’s it. Your identity is never associated with your account.”

However, a since-deleted version of Discord’s FAQ on age verification policies appears to contradict the company’s claims about how long government IDs are stored by the third-party vendor, in this case, Persona.

“Important: If you’re located in the UK, you may be part of an experiment where your information will be processed by an age-assurance vendor, Persona,” anarchivedversion of the site reads. “The information you submit will be temporarily stored for up to 7 days, then deleted. For ID document verification, all details are blurred except your photo and date of birth, so only what’s truly needed for age verification is used.”

## Persona gets personal

Persona CEO and cofounder Rick Song toldFortunethat the files were not a vulnerability, but instead, publicly accessible front-end information. “What was found was uncompressed files of a front end that’s already on every single person’s device,” he said, adding the information is available on the company’s help center and API documentation. “I don’t think having uncompressed files online is good,” Song went on, but added the information found by the researcher is the uncompressed version of a company’s compressed source map online.

“I think this is one of these in which the contents of it seems scarier, but…internally, we didn’t consider this even a major vulnerability.”

Song still considers the partnership between Persona and Discord to be a success. “I think the performance of the product did incredibly well,” the CEO toldFortune. “The reason why we were able to say that all data was redacted immediately is because the data was redacted; it had already been redacted upon processing. It’s not like it was due to the termination of the contract that we delete the data. It’s deleted immediately after a verification of the individual.”

Song denied any ties to Palantir, ICE, or the government, but said the company is going through FedRAMP authorization. “We are trying to get FedRAMP and the goal of that is we do a lot of work for workforce security,” which uses a whole other set of information to confirm an employee is who they say they are, as compared to a user on a social media platform verifying their age.

In response to the 269 kinds of verification checks, these are all options Persona offers, said Song, but it does not necessarily mean a client would need all of them. In essence, the needs of a social media platform for age verification would not be the same as an employer conducting a background check.

Over the weekend, Song denied that Persona—which also offers know your customer (KYC) and anti-money laundering (AML) solutions—links facial biometrics to financial records or law enforcement databases. Song posted screenshots of an email exchange with the researcher “Celeste” onX, stating the researcher’s implication of some connection between Persona, Palantir, and ICE has led to threats against members of the company.

“We have no relationship whatsoever with ICE, Palantir,” Song’s screenshot of the email exchange read. The CEO added that some of the members of the company who have received backlash are new grads or people who have recently signed on. “I don’t think these people are the ones that the public’s ire should be directed at, and if anyone, it should be directed at me.”

Song was also attacked for his lack of personally identifiable information online. A user onXposted a screenshot of the CEO’sLinkedInprofile showing Song with a verified badge but lacking a profile photo. Persona handles LinkedIn’s identity verification requests.

In response, Songwrote, “I am verified. That’s the entire point. It’s dystopian that we want people to facedox themselves to everyone to be real online. It’s ironic that folks posting about privacy want me to facedox to everyone.”

Join us at the Fortune Workplace Innovation Summit
May 19–20, 2026, in Atlanta. The next era of workplace innovation is here—and the old playbook is being rewritten. At this exclusive, high-energy event, the world’s most innovative leaders will convene to explore how AI, humanity, and strategy converge to redefine, again, the future of work.
Register now
.
About the Author
By
Catherina Gioino
See full bio
Right Arrow Button Icon
Latest in Cybersecurity
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Most Popular
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
Finance
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
By Fortune Editors
October 20, 2025
