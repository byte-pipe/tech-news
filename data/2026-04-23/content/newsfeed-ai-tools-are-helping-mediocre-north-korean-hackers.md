---
title: AI Tools Are Helping Mediocre North Korean Hackers Steal Millions | WIRED
url: https://www.wired.com/story/ai-tools-are-helping-mediocre-north-korean-hackers-steal-millions/
site_name: newsfeed
content_file: newsfeed-ai-tools-are-helping-mediocre-north-korean-hackers
fetched_at: '2026-04-23T09:44:44.543176'
original_url: https://www.wired.com/story/ai-tools-are-helping-mediocre-north-korean-hackers-steal-millions/
author: Andy Greenberg
date: '2026-04-22'
published_date: '2026-04-22T16:00:00.000Z'
description: One group of hackers used AI for everything from vibe coding their malware to creating fake company websites—and stole as much as $12 million in three months.
tags:
- wired
- security
- security / cyberattacks and hacks
- security / security news
---

Save Story
Save this story
Save Story
Save this story

The advent ofAI hacking tools hasraised fears of a near futurein which anyone can use automated tools to dig up exploitable vulnerabilities inany piece of software, like a kind of digital intrusion superpower. Here in the present, however, AI seems to be playing a more mundane, if still concerning, role in hackers’ toolkit: It’s helping mediocre hackers level up and carry out broad, effective malware campaigns. That includes one group of relatively unskilled North Korean cybercriminals who’ve been discovered using AI to carry out virtually every part of an operation that hacked thousands of victims to steal their cryptocurrency.

On Wednesday, cybersecurity firm Expelrevealedwhat it describes as a North Korean state-sponsored cybercrime operation that installed credential-stealing malware on more than 2,000 computers, specifically targeting the machines of developers working on small cryptocurrency launches, NFT creation, and Web3 projects. By using the AI tools of US-based companies, including those of OpenAI, Cursor, and Anima, the hacker group—which Expel calls HexagonalRodent—“vibe coded” almost every part of its intrusion campaign, from writing their malware to building the fake websites of companies used in its phishing schemes. That AI-enabled hacking allowed the group to steal as much as $12 million in cryptocurrency from victims in three months.

What’s most striking about the HexagonalRodent hacking campaign isn’t its sophistication, says Marcus Hutchins, the security researcher who discovered the group, but rather how AI tools allowed an apparently unsophisticated group to carry out a profitable theft spree in the service of the North Korean state.

“These operators don't have the skills to write code. They don't have the skills to set up infrastructure. AI is actually enabling them to do things that they otherwise just would not be able to do,” says Hutchins, who became well-known in the cybersecurity community afterdisabling the WannaCry ransomware wormcreated by North Korean hackers.

## Emoji-Littered, AI-Written Code

HexagonalRodent’s hacking operation focused on tricking crypto developers withfraudulent job offersat tech firms, going so far as to create full websites for the fake companies recruiting the victims, often created with AI web design tools. Eventually, the victim was told they’d have to download and complete a coding assignment as a test—which the hackers had infected with malware that infiltrated their machine and stole credentials, including those that in some cases could grant access to the keys that controlled their crypto wallets.

Those parts of the hacking operation appear to have been well-honed and effective, but the hackers were also clumsy enough to leave parts of their own infrastructure unsecured, leaking the prompts they used to write their malware with tools that included OpenAI’s ChatGPT and Cursor. They also exposed a database where they tracked victim wallets, which allowed Expel to estimate the total amount of cryptocurrency the hackers may have stolen. (While those wallets added up to $12 million in total contents, Hutchins says the company couldn’t confirm for each target whether the entire sum had already been drained from the wallets or if the hackers still needed to obtain keys to the victim wallets in some cases, given some may have been protected with hardware security tokens.)

Hutchins also analyzed samples of the hackers’ malware and found other clues that it was largely—perhaps entirely—created with AI. It was thoroughly annotated with comments throughout—in English—hardly the typical coding habits of North Koreans, despite the fact that some command-and-control servers for the malware tied them to known North Korean hacking operations. The malware’s code was also littered with emojis, which Hutchins points out can, in some cases, serve as a clue that software was written by a large language model, given that programmers writing on a PC keyboard rather than a phone rarely take the time to insert emojis. “It's a pretty well-documented sign of AI-written code,” Hutchins says.

The AI-written code Hutchins analyzed ought to have been detectable with typical “end point detection and response” security tools used in most companies and government agencies, Hutchins says, given that it followed standard patterns of behavior for malware. But Hutchins says HexagonalRodent’s decision to focus on individual victims in its hacking campaign meant many didn’t have those security tools installed. “They found a niche where you actually can get away with completely AI-generated malware,” says Hutchins.

Hutchins argues that the HexagonalRodent campaign shows how AI may be an especially useful tool for North Korea, which can easily recruit unskilled IT workers to join its hacker ranks—or more commonly, toinfiltrate tech companieswhile posing as citizens of other countries—but has a far more limited number of capable hackers, given the average North Korean’s lack of access to the internet or even computers. “They have hundreds of people being sent over the border to work in IT operations, and only a few of them really know what they're doing,” Hutchins says. “But then they're able to use generative AI to get a leg up and actually run fairly successful hacking campaigns.”

In fact, rather than reduce the number of people involved in the hacking campaign through automation, Hutchins says he’s been able to observe North Korean operations grow in size over time. Expel estimates that as many as 31 individual hackers were involved in HexagonalRodent. “They just keep adding more and more operators,” Hutchins says. “Because they can just hand them access to an AI model, and they can now do things which they would have previously needed a development team to support.”

## A Hermit Kingdom, Embracing AI

The HexagonalRodent activity observed by Hutchins makes up only a small part of North Korea’s sweeping hacking and cybercriminal activity, which can involve vast cryptocurrency theft, ransomware, espionage, fraud, and infiltrating Western organizations through its IT worker schemes. Security researchers havelikenedNorth Korea's cyber operations to functioning like a “state-sanctioned crime syndicate,” which ultimately works to fund the nation’s nuclear weaponry, build the country’s infrastructure, and evade international sanctions.

Increasingly, and perhaps unsurprisingly, these state-backed programs have been adding generative AI to their hacking and fraud workflows to improve their overall efficiency. Within North Korea, these efforts have reportedly been supported by the creation of Research Center 227, an organization sitting under the military’s Reconnaissance General Bureau that will partly focus ondeveloping AI-focussed hacking tooling. But day-to-day, North Korea’s cyber operators have repeatedly been caught using commercial, off-the-shelf AI tools.

“North Korea is using AI as a force multiplier, and it is helping with every aspect—building resumes, building websites, building exploits, testing vulnerabilities—and they're doing it at speed and scale,” says Michael “Barni” Barnhart, a researcher at security firm DTEX, who hastrackedthe country’s hacking operations for years. North Korean cyber operators have been experimenting and widely using AI for multiple years, Barnhart says. “AI is helping them move faster so that they can weaponize exploits and even help build those exploits,” he explains. “You get little pieces of the puzzle from each of the groups, and then it kind of forms a whole picture of how they're using AI.”

For instance, members of North Korea’s IT worker programs have been using AI assistants andface-changing deepfakesto answer questions and change their appearance during fraudulent job interviews. Security researchers at Microsoft havespottedsuspected North Korean operations using AI to create false IDs, research work tools, polish their English for social engineering, and research known security vulnerabilities. Some North Korea actors have also used the technology to create web infrastructure at scale, making their operations harder to detect, according to Microsoft’s research.

Both OpenAI and Anthropic have also spotted North Korean cyber operators using their platforms over the last 12 months. In February last year, OpenAIsaidit had banned suspected North Korean accounts that it detected using ChatGPT at multiple stages of fraudulent IT worker schemes, including during interviews to generate answers to technical questions and for writing code once someone had gained employment at a company.

Meanwhile, Anthropicsaidin its August threat intelligence report that it had seen North Korean IT workers who “appear unable to perform basic technical tasks or professional communication without AI assistance.” The company also said it detected North Korean hackers intending to use Claude to “enhance” some of the same malware strains Expel found in use, and to develop skills tests containing malware. But Anthropic wrote in its own report that it detected the malicious use of Claude and banned the hackers from using its tools.

OpenAI tells WIRED that its tools did not give the hackers any “novel capabilities,” but acknowledging that the “value” of its tools to the hackers “appears to be speed and scale.” OpenAI did not say if it had banned any accounts in relation to Expel’s findings. Cursor tells WIRED that it had blocked the HexagonalRodent hackers from using its tools, adding that the company is “investigating further and [is] in communication with other model providers on the incident."

Anima, one of the AI web design firms whose tools were used in the hacking campaign, tells WIRED that it was working with Expel to identify and block the hackers from using its software. “This is misuse of Anima’s coding agent by bad actors, and we’re addressing it head-on,” the company’s CEO, Avishay Cohen, wrote.

Hutchins argues that it’s this practical use of AI for enabling hacking operations that should be the cybersecurity’s industry’s focus, not the notion of some future vulnerability discovery AI.

“We're thinking we need to build defenses for the hypothetical Skynet that’s going to blast through all of our networks,” says Hutchins. “Meanwhile, you have a nation-state threat who is able to spin up their operations using AI without doing anything novel. There is real threat activity happening as a result of AI. But it's not the stuff that people are wasting their breath on.”

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Will Knight'sAI Labexplores advances in AI
* Meta’s facial recognition glassescould arm sexual predators
* Big Story:Thesnake brosgetting bitten by their lethal pets
* Thedeepfake nudes crisisin schools is worse than you thought
* Listen:Silicon Valley is spending millionsto stop one of its own
Andy Greenberg
 is a senior writer for WIRED covering hacking, cybersecurity, and surveillance. He’s the author of the books 
Tracers in the Dark: The Global Hunt for the Crime Lords of Cryptocurrency
 and 
Sandworm: A New Era of Cyberwar and the Hunt for the Kremlin's Most Dangerous Hackers
. His books ... 
Read More
Senior Writer
* X
Matt Burgess
 is a senior writer at WIRED focused on information security, privacy, and data regulation in Europe. He graduated from the University of Sheffield with a degree in journalism and now lives in London. Send tips to 
[email protected]
. ... 
Read More
Senior writer
* X
Topics
north korea
Crime
scams
hacking
cybersecurity
malware
security
artificial intelligence
hacks
Hackers Are Posting the Claude Code Leak With Bonus Malware
Plus: The FBI says a recent hack of its wiretap tools poses a national security risk, attackers stole Cisco source code as part of an ongoing supply chain hacking spree, and more.
Andrew Couts
In the Wake of Anthropic’s Mythos, OpenAI Has a New Cybersecurity Model—and Strategy
OpenAI says its safeguards “sufficiently reduce cyber risk” for now, while GPT-5.4-Cyber is a new cybersecurity-focused model.
Lily Hay Newman
Anthropic’s Mythos Will Force a Cybersecurity Reckoning—Just Not the One You Think
The new AI model is being heralded—and feared—as a hacker’s superweapon. Experts say its arrival is a wake-up call for developers who have long made security an afterthought.
Lily Hay Newman
Your Push Notifications Aren’t Safe From the FBI
Plus: Iran’s internet blackout hits the 1,000-hour mark, cryptocurrency scams result in a record amount of money stolen from Americans, and more.
Matt Burgess
Meta Pauses Work With Mercor After Data Breach Puts AI Industry Secrets at Risk
Major AI labs are investigating a security incident that impacted Mercor, a leading data vendor. The incident could have exposed key data about how they train AI models.
Maxwell Zeff
Iranian Hackers Breached Kash Patel’s Email—but Not the FBI’s
Plus: Apple makes big claims about the effectiveness of its Lockdown Mode anti-spyware feature, Russia moves to implement homegrown encryption for 5G, and more.
Andrew Couts
Iran-Linked Hackers Are Sabotaging US Energy and Water Infrastructure
As Trump threatens Iranian infrastructure, the US government warns that Iran has carried out its own digital attacks against US critical infrastructure.
Andy Greenberg
It Takes 2 Minutes to Hack the EU’s New Age-Verification App
Plus: Major data breaches at a gym chain and hotel giant, a disruptive DDoS attack against Bluesky, dubious ICE hires, and more.
Dell Cameron
The Hack That Exposed Syria’s Sweeping Security Failures
When Syrian government accounts were hijacked in March, the breach looked chaotic. But it revealed something more troubling: a state struggling with the most basic layer of cybersecurity.
Danny Makki
Men Are Buying Hacking Tools to Use Against Their Wives and Friends
In Telegram groups, men are sharing thousands of nonconsensual images of women and girls, buying spyware, and engaging in doxing and sexual abuse.
Matt Burgess
Anthropic Teams Up With Its Rivals to Keep AI From Hacking Everything
The AI lab's Project Glasswing will bring together Apple, Google, and more than 45 other organizations. They'll use the new Claude Mythos Preview model to test advancing AI cybersecurity capabilities.
Lily Hay Newman
The Dumbest Hack of the Year Exposed a Very Real Problem
Last April, a hacker hijacked crosswalk announcements to mimic Mark Zuckerberg and Elon Musk. Records obtained by WIRED reveal how unprepared local authorities were.
Paresh Dave