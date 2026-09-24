---
title: Two-Tier Encryption in the UK
url: https://macanorak.com/two-tier-encryption-in-the-uk/
site_name: hackernews_api
content_file: hackernews_api-two-tier-encryption-in-the-uk
fetched_at: '2026-09-24T21:57:38.731135'
original_url: https://macanorak.com/two-tier-encryption-in-the-uk/
author: ReturnoftheHack
date: '2026-09-24'
published_date: '2026-09-21T08:25:25.000Z'
description: Alice and Bill have identical iPhones. Only one gets Apple’s strongest iCloud protection.
tags:
- hackernews
- trending
---

Here's something odd. Alice and Bill both live in the UK. Both have identical iPhones. Both use iCloud. Both pay Apple for the same services. Alice hasAdvanced Data Protectionswitched on, protecting the majority of her iCloud data. Bill doesn’t, and can’t switch it on. Alice enabled it before Apple withdrew the feature for new UK users in February 2025. Bill missed the window.

To understand how this happened, we need to go back over a decade to the aftermath of theSnowden/NSA revelationssurroundingPRISM. In January 2014, Tim Cook was interviewed byDavid Muir for ABC News. Cook said,“We have a gag order on us right now,”but clarified,“there is no back door. The government doesn't have access to our servers. They would have to cart us out in a box for that… we feel that strongly about it."

Nearly two years later, on the 2nd of December 2015,Syed Rizwan Farook and Tashfeen Malikcarried out theSan Bernardino terrorist attack, killing 14 people and wounding 22. The FBI obtained the iPhone 5C that had been used by Farook. They had a warrant to search the iPhone, but they didn't know the passcode.The FBI obtained a court orderto compel Apple to help them into the device. They wanted Apple to create a version of iOS that would remove or circumvent the iPhone's security protections (in particular the limits on passcode attempts). Apple demurred. In anopen letterby Tim Cook, he said that the government was asking for something the company simply didn't have, and something it considered"too dangerous to create."

In another interview with ABC's David Muir, Cook gave an impassioned and at times angrydefence of Apple's position, describing the requested software as the"equivalent of cancer."He argued that such a tool would function as a “master key” capable of unlocking hundreds of millions of devices, and that once built, there would be no way to guarantee it was only used against that one phone.

Ina separate interviewfor CBS’ 60 minutes, Cook reiterated the underlying principle:"If you put a back door in, then that back door is for everybody. For good guys and bad guys.”James Comey, then Director of the FBI, told 60 Minutes that whilst he was committed to protecting the privacy of Americans,“the notion that we would market devices that would allow someone to place themselves beyond the law troubles me a lot.”

The FBI eventually obtained access using a third party (widely reported to be Cellebrite[1]) andwithdrew its legal actionagainst Apple.

Skip forward almost a decade, and on the 7th of February 2025,The Washington Postexclusively revealed that the UK government had ordered Apple to provide access to data protected by its strongest level of iCloud encryption. The UK has powers to make such requests under theInvestigatory Powers Act 2016— the centrepiece of the UK’s modern surveillance law.[2]

One of the mechanisms available under that legislation is called aTechnical Capability Notice(a sanitised, bureaucratic euphemism if ever there was one). A Technical Capability Notice (TCN) is a legal instruction that requires a communications / technology provider to maintain or develop the capability to comply with certain requirements (the notice itself doesn’t authorise access to anyone’s data — it just ensures the capability exists for when a specific warrant or authorisation does). Before issuing a TCN, the government is obliged to consider things such as technical feasibility, cost, likely benefits and the number of users affected. A TCN requires approval from a Judicial Comissioner, and the recipient of a TCN is generally gagged from revealing its existence or contents without the UK Secretary of State's permission (the Home Office says it will generally neither confirm nor deny whether a particular TCN exists).

The Postreported that UK security officials had issued such a TCN, in secret, in January 2025, requesting that Apple create a way to access encrypted iCloud data belonging not just to UK users, but to Apple usersworldwide. The chutzpah of it all was astonishing.

Apple's position (privately, since they were prohibited from commenting publicly on the reported TCN) showed fidelity to its previous stance: deliberately weakening end-to-end encryption, for whatever purpose or for whomever the intended beneficiary, would make every user less secure. So the dispute became the UK government saying it needed access, Apple saying it couldn't decrypt the data, and the UK effectively replying: then change the system so that you can.

It's important to get into the technicalities here. All iCloud data is encrypted. But there's a difference between encrypted and end-to-end encrypted (E2EE) data. iCloud already protects sensitive categories of data (like Passwords, Health data, Messages in iCloud, etc) with end-to-end encryption by default. For everything else, Apple retains the ability to decrypt the data when necessary, and can be ordered to hand this data over by law enforcement. WithAdvanced Data Protection(ADP), several more categories of iCloud data become end-to-end encrypted (iCloud Backup, Photos, Notes, and others). Apple itself doesn't possess the keys needed to decrypt that protected data. It's not something Apple can unlock just because a government asks for the contents.

There was a heartening backlash to what the UK government had asked Apple to do. The Investigatory Powers Tribunal (IPT)became involved(the independent UK body that hears complaints about unlawful surveillance or human rights breaches by public authorities).Privacy Internationaland other groups argued that the government shouldn't be able to secretly compel technology companies to weaken encryption without adequate public scrutiny. Apple itself effectively confirmed the underlying confrontation with the UK government, without directly acknowledging the existence of the reported TCN: on the 21st of February it announced that Advanced Data Protection wouldno longer be available to new UK users, stating that"we have never built a backdoor or master key to any of our products or services and we never will".[3]

To be clear, the reported TCN itself didn’t order Apple to withdraw ADP. It ordered Apple to maintain thetechnical capabilityto make ADP-protected data accessible when a warrant required it. If Applehadcomplied with the reported TCN, they would have needed to create a mechanism capable of unlocking private information that could potentially be exploited by hackers, hostile governments, and others. It would also, I believe, have set a dangerous precedent — the "good guys" might not actually be good, and even if they were, a future government might not be, and might want to use that access for bad ends. Apple was the canary in the coal mine in this case.[4]Such a precedent would also affect WhatsApp, Signal[5], cloud-storage companies, password managers, banks, and essentially any service relying on genuine end-to-end encryption.

Faced with a legal order that would have required it to change the security architecture on which ADP depended, Apple found a third option:stop offering the feature that made this dilemma exist in the first place. It reverted affected UK iCloud data to Standard Data Protection, where Apple does hold the keys and can respond to lawful legal procress (except the baseline categories that stay end-to-end encrypted either way). This satisfied the underlying legal requirement without ever building a ‘backdoor’.

Apple said the decision to withdraw ADP in the UK left them“gravely disappointed”. There was, however, an important disclaimer. Apple only stopped allowingnewUK users to turn on Advanced Data Protection. It said it could not automatically disable ADP for existing users who had already turned it on. Why couldn’t Apple just switch ADP off for everyone in the UK? Because Apple deliberately designed ADP so that the setting can only be changed by the user’s trusted devices. Apple’ssecurity documentationsays its servers can’t modify the ADP setting, or roll it back on a user’s behalf.

This has effectively led to a "two-tier" level of encryption for Apple customers in the UK. People like myself, who were fortunate to have enabled the feature before it was pulled, are still protected by Advanced Data Protection.Apple says“users will be given a period of time to disable the feature themselves to keep using their iCloud account”(the company hasn’t published a deadline for when existing UK users must do this). People who didn't have ADP turned on prior to the decision, or became Apple customers after the company pulled the feature, can’t turn ADP on.

This is what I still see on my iPhone:

To bring this into sharper focus: Alice enabled ADP on her iPhone in 2024. Bill can't turn the feature on. Both are UK residents. Both use iCloud. Both are subject to the same UK legal regime. Yet Alice has the stronger end-to-end encryption for the additional ADP-protected categories, while Bill does not.

There are two ways Bill might have ended up here. Maybe he bought his iPhone after Apple pulled the option for new UK users entirely. Or maybe he bought it before the cutoff, like Alice, but didn't know that ADP was anopt-infeature — he had toactively turn it on, and he didn’t. Whichever version of Bill you imagine, the same fact now applies to both: it's too late for him to do anything about it.

Tough luck, Bill.

#### Where things stand now, and why the secrecy matters.

The UK government’s original reported demand was global. It was replaced in late 2025 by anarrower notice affecting only UK citizens, after the Trump administrationapplied pressureover concerns about the implications for American users.

In July 2026, Apple lodged afresh complaintat the Investigatory Powers Tribunal, which became public the following month. Then, on the 11th of September 2026, U.S. Senator Ron Wyden[6](a Democrat) and Republican Congressman Warren Davidson called on the UK's Investigatory Powers Tribunal to open up its proceedings concerning Apple's encrypted-data dispute. In theirletter to the tribunal, they argued that the UK's demand for secrecy undermines democratic governance on both sides of the pond, warning that Congress cannot fulfil its oversight duties if"foreign non-disclosure orders are weaponized"to stop US companies answering to elected lawmakers.

On the 17th of SeptemberThe Daily Telegraphreported that Apple had asked the Investigatory Powers Tribunal to remove restrictions that gag them from confirming the existence of the reported TCN. Daniel Beard KC, representing Apple, told the tribunal this would allow“facts to be deployed in the open”. Lawyers for two human-rights organisations — Liberty and Privacy International — argued that maintaining the gag order is“farcical”, because everyone knows about it anyway; Ben Jaffey KC compared the secrecy order to the“emperor’s new clothes… and brings the administration of justice into disrepute”.

And this is the most troubling aspect of this whole sorry affair — the secrecy. Technical Capability Notices can be issued by the UK government in secret, and the recipient of the notice is restricted in law about what it can publicly say about it.

In a 1961speech to the American Newspaper Publishers Association[7], John F. Kennedy warned that"the very word 'secrecy' is repugnant in a free and open society,"specifically highlighting“secret societies… secret oaths and… secret proceedings”. He argued that a free society shouldn't automatically accept secrecy just because the government invokes security. He cautioned that any announced need for increased security risked being exploited by those seeking to expand it into full-blown censorship and concealment.

I want to be fair to the UK government here, so let me try the most charitable explanation first: maybe this isn't malice, just plain ignorance — technological illiteracy on behalf of UK government ministers. But this explanation is too simple, too comforting. It's difficult to believe the UK government isn’t aware that encryption is not like a physical safe where the manufacturer holds a master key that a government can subpoena. The cryptographic design meansthere is no master key.You can't obtain information just by ordering the manufacturer to hand it over. The only way to do it is to change the system. And ignorance becomes even harder to credit once you consider who would likely be involved in issuing a TCN — not just ministers, but security and intelligence agencies, lawyers and technical advisors, all operating within the statutory framework of the Investigatory Powers Act.

The government might argue this situation is nothing like the FBI's 2016 demand for a master key: it's a legal mechanism, subject to independent judicial oversight, targeted at serious crimes. But, to my mind, judicial oversight doesn’t solve the underlying technical problem — any mechanism that lets an authorised party in, is a mechanism an unauthorised party could potentially discover and exploit too. The UK government (and this behaviour concerns successive UK governments, of different political flavours, Labour and Conservative alike) seems to believe the national security benefits outweigh any cybersecurity cost. I do understand the position: serious criminals use encryption, therefore law enforcement needs a way of accessing encrypted material when legally authorised. But we are at a stalemate. Apple doesn’t have the decryption keys. It can't give the government what it wants. So, in the context of this particular dispute, the UK government only really has two options: force Apple to change the system so that someone other than the user’s trusted devices can ultimately gain access — call it a backdoor, a technical capability, whatever euphemism suits — or accept that some data will stay permanently out of reach, inaccessible, as part of the trade-off of living in a free society.

I sometimes wonder what would have happened if Apple had acquiesced to the FBI's requests in 2015. No matter what one thinks of Tim Cook's (likely calculated)appeasement of Trump[8], it's worth looking back at his fidelity to one unequivocal position after the San Bernardino terrorist attack, when he and his company came under significant fire, not just from the FBI and the wider apparatus of government, but from large sections of the public too. It remains one of the most prominent examples of a private American company publicly resisting government overreach on behalf of its users.[9]

Over on this side of the pond, Apple chose to resist the UK government’s original demand by withdrawing ADP from new UK users, ironically depriving them of end-to-end encryption for categories of iCloud data that ADP previously protected. It wouldn’t be fair to treat the resultant two-tier outcome as something Apple did to Bill. Apple was handed an extraordinarily difficult choice and picked the least-bad option available. In my view, the unfairness belongs with the government decision that created this impossible order in the first place.

Note:I wrote to the Home Secretary and other relevant ministers ahead of publishing this piece; none had responded by the time it went live.

1. Researchers at the University of Toronto'sCitizen Labhave documented Cellebrite’s extraction devices being used against human rights activists and journalists in Russia, Serbia, and elsewhere, sometimes even after the company claimed to have cut off the country in question.↩︎
2. The roots of the Investigatory Powers Act go back to the 2012‘Snooper's Charter’, an attempt to expand government access to communications data, and to earlier legislation such as theRegulation of Investigatory Powers Act 2000. After the 2012 proposals stalled, the Government returned with theInvestigatory Powers Bill in 2015. It became law in November 2016 and came into force the following year.↩︎
3. Withdrawing ADP in the UK did not affect the 14 iCloud categories that were already end-to-end encrypted by default, including iCloud Keychain and Health. ADP increases the total from 14 to 23 categories. For UK users without ADP, the additional categories (iCloud Backup, Photos, Notes, iCloud Drive and so on) revert to Standard Data Protection.↩︎
4. Canaries sing constantly, and fall silent at the first hint of gas.Miners learned to listen for the silence.This isn't the only warning system built around birdsong. Some 17th-century Japanese castles (Kyoto's Nijō Castle, for example) have floors said to chirp like anightingalewith each footstep, which is popularly believed to have alerted guards to anyone creeping through the corridors (the castle's signage. however, says:“The singing sound is not actually intentional, stemming rather from the movement of nails against clumps in the floor caused by wear and tear over the years").↩︎
5. Signal Foundation’s presidentMeredith Whittakerhas said,“We would leave the U.K. or any jurisdiction if it came down to the choice between backdooring our encryption and betraying the people who count on us for privacy, or leaving."↩︎
6. This is not a new fight for Wyden — he's been one of theloudest anti-backdoor voicesin the U.S. Senate for the best part of a decade, introducing the Secure Data Act inDecember 2014to ban the government from forcing companies to weaken encryption.↩︎
7. Kennedy gave this speech about a week after the failedBay of Pigs invasion. He argued simultaneously for “far greater public information” and “far greater official secrecy”, reflecting the tension between press freedom and national security during the Cold War.↩︎
8. Tim Cook presented Trump with acustom 24-karat gold-based glass plaquein the Oval Office in August 2025, alongside a $100 billion manufacturing investment announcement.↩︎
9. A couple of other notable examples:Lavabitshut itself down entirely rather than hand the FBI its SSL keys, after being threatened with a $5,000-a-day fine;Yahoofought a secret FISA court order demanding it hand over user data for the NSA's PRISM program, and was threatened with fines of $250,000 a day for refusing.↩︎

#### Read next

Apple's new Audio Intelligence features protect your privacy. What about everyone else’s?

 

Apple keeps building the future, then losing its nerve to finish it.

 

Why I think Apple needs to get back on stage.