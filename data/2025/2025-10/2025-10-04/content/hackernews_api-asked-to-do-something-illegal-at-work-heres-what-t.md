---
title: Asked to do something illegal at work? Here’s what these software engineers did - The Pragmatic Engineer
url: https://blog.pragmaticengineer.com/asked-to-do-something-illegal-at-work/
site_name: hackernews_api
fetched_at: '2025-10-04T19:07:54.305644'
original_url: https://blog.pragmaticengineer.com/asked-to-do-something-illegal-at-work/
author: bschne
date: '2025-10-02'
published_date: '2023-11-09T19:47:07.000Z'
description: At FTX, Frank, and Pollen, software engineers were asked to do something potentially illegal, or to go along with what looked like fraud. They obliged in two out of three cases, landed in hot water, and now face jail time. A reminder why it’s never a good idea to go along with such requests.
tags:
- hackernews
- trending
---

Update on 2 Oct 2025: back in 2021, Charlie Javice, CEO of student loan startup Frank pressured a software engineer to inflate customer numbers. She told the engineer that she did not believe that anyone would end up in an ‘orange jumpsuit’ just for this. Still, the engineer refused – and was proven right. Javice, in fact, did end up in an orange jumpsuit,sentencedto 7 years of prison in 2025 for fraud.

The below topic was sent out to full subscribers ofThe Pragmatic Engineer, three weeks ago, inThe Pulse #66. I have received several messages from people asking if they can pay to “unlock” this information for others, given how vital it is for software engineers. It is vital, and so I’m sharing this with all readers, without a paywall. In the unlikely case that you are asked to do something fishy or illegal: I hope the below will help decide how to do the right thing.

Sign up to The Pragmatic Engineerto get articles like this earlier in your inbox. It's a pretty good read, and the#1 tech publicationon Substack.

What would you do if you learned your company is up to something illegal like stealing customer funds, or you’re asked to make code changes that will enable something illegal to happen, like misleading investors, or defrauding customers? Here are three real-life cases, where what engineers and engineering managers did had serious consequences.

#### FTX: an engineering director went along with the fraud

A trial related to FTX, the cryptocurrency exchange which allegedly defrauded investors of $9B, is ongoing. Day 9 of the trial of former FTX CEO Sam Bankman-Fried trial, heard testimony from Nishad Singh, who joined the business as a software engineer, and later became an engineering director. Here is software engineer and writer Molly Whitesummarizes of his evidence:

“To hear Singh tell it, he didn’t even really realize what was going on at FTX and Alameda Research until September 2022 — only a month or two before everything came crashing down. (...) Several times throughout various testimonies, we’ve seen a document written by Sam Bankman-Fried, in which he describes his thinking that Alameda Research should be shut down. That document was, ultimately, how Singh learned in September 2022 that Alameda Research had taken billions of dollars of customer funds from FTX.This was when Gary Wang told Singh that Alameda was borrowing massive amounts of customer money from FTX — at the time, around $13 billion of it. Singh testified that he felt ‘really afraid’, and called an in-person meeting immediately. Bankman-Fried, who was sitting next to Singh at the time, ‘seemed unsurprised and made up what I understood to be a false excuse for dodging the meeting.’ Singh, Ellison, and Wang met without him, and Singh confirmed his fears: that he had not misunderstood Wang, and that Alameda had actually taken customer funds to that extent.”

Okay, so in September 2022, Singh had confirmation that something illegal was happening at the company, which he had no direct knowledge of,until then. At that point, if he wanted to avoid being an accomplice to potentially illegal activity, his options were:

1. Talk to a lawyer on how to avoid assisting a crime
2. Turn whistleblower. See thetech whistleblower guide
3. Quit the company, ensuring he did not further aid this activity

The smart thing would have been to do #1. The profitable thing could have been to do #2 because in the US, a whistleblower may receive awhistleblower rewardof between 10-30% of what the government recovers from fraudulent activities. The final choice #3 is hard, but could have meant Singh would not have had to plead guilty as he did.

Here’s what Singh did instead: he asked for a personal meeting with Bankman-Fried and confronted him about the missing funds. However, Bankman-Fried replied there not much to worry about, and that they’d repay the funds by raising more money from investors (!!) This should have been the point at which Singh quit. Instead:

“He thought about leaving the company then, he testified, but worried that his departure could cause everything to fall apart. He felt that if he stayed, maybe he could help the companies make back what they owed.”

For the next two months, Singh tried to make things better, but it was fruitless. FTX collapsed in November 2022.

Lesson #1: when you discover fraud may be happening, do not “stay around to fix it.”Any other approach would have been better for Singh; seeking legal advice, turning whistleblower, or quitting on the spot.

To be fair, Singh didn’t seentotallyclueless, and it seems he decided to profit on the developments. Days after he found about this fraud, he took a $3.7M loan from FTX (!!) to buy a house, The Vergepointed out. It’s exactly the type of thing you don’t want to do after you discover fraud.

Now, Singh is facing up to 75 years in jail thanks to his decision to aid the company after discovering the fraud. His sentence will most likely be reduced due to his plea deal, but any course of action which leads to a criminal conviction is surely a grave error of judgment.

Update in Oct 2025: in the end, Nishad Singhwas sparedfrom prison, and received 3 years of supervised release. The judgewas persuadedthat Singh’s involvement with the fraud was far more limited than that of FTX founder Sam Bankman-Fried or Caroline Ellison, the former CEO of sister hedge fund Alameda Research.

#### Frank: a software engineer refuses to fake customer data

Frank was a student loan startup founded by Charlie Javice in 2016. In 2019, Javice was featured on the Forbes “30 under 30”finance list, suggesting she was a high-flying founder:

How Charlie Javice appeared on the Forbes 30 under 30 list in 2019. We now know the 300,000 user number was fake. Source: Forbes

It certainly seemed like Charlie Javice was a standout founder; in 2021, JP Morgan purchased Frank for $175M. However, things turned sour quickly. JP Morgan thought it bought a startup with 5 million customers, which worked with 6,000 schools. But after the purchase, this data was found to be mostly fake.

Let’s get to a software engineer’s involvement. This April, founder Charlie Javice was arrested, and a lawsuit is ongoing between her, former Chief Growth Officer Olivier Amar, and JP Morgan. From to this lawsuit, we get an inside look at how events unfolded inside Frank.

In 2021, an engineer was asked to produce fake data for 4.2M non-existent customers.As acquisition talks were ongoing, JP Morgan wanted to validate that Frank had the nearly 5M customers it claimed. In reality, Frank had 293,000 customers, so the CEO asked an engineer to fake the data and turn this list into 4.2M members. Here’s what happened next – fromthe lawsuit:

“[In 2021] Javice [CEO], Amar [Chief Growth Officer] and the Director of Engineering then had a Zoom meeting during which Javice and Amar asked the Director of Engineering to help them create a synthetic list of customer data. She asked the Director of Engineering if he could help take a known set of FAFSA application data and use it to artificially augment a much larger set of anonymous data tht her systems had collected over time.The Director of Engineering questioned whether creating and using such a data set was legal, but Javice tried to assure the engineer by claiming that this was perfectly acceptable in an investment situation and she did not believe that anyone would end up in an ‘orange jumpsuit’ over this project.”

Lesson #2: when your manager claims they don’t believe anyone would end up in an “orange jumpsuit,” assume that someone definitely could.The engineering director’s next step? They refused:

“The Director of Engineering was not persuaded and told Javice and Amar that he would not perform the task, and only would send them the file containing Frank’s actual users, which amounted to approximately 293,000 individuals at the time.”

And this engineering director played it right, as the people who are likely to go to jail and end up in orange jumpsuits are the other two people on the call, who knowingly went along with the illegal.

#### Pollen: an engineer told to double charge customers by the CEO

Last year, I published my first – and to date only– investigative article onhow events tech startup Pollen raised $200M and then collapsed, owing months of wages to staff. In the investigation, I focused on an unusual detail: $3.2M worth of funds taken months early from customers. The incident was described internally by Pollen as a mistake, and an incident reviewshouldhave followed. Even more confusing, the company blamed the payments processor Stripe for the incident.

The reality was that this was a very deliberate double charge. I could not share this fact at the time – as the company threatened me with libel after I informed them of this detail – but the BBC has now produced a documentaryrevealing detailsabout this deliberate double charge that was covered up as an outage. Fromthe documentary:

[Narrator] “Pollen initially told some customers that the problem was with their payments provider. Later, Callum [the CEO] addressed his staff who were demanding to know what happened.”

[CEO of Pollen talking] “All that happened was that a couple millions of dollars of payment plans that were due to be paid at a later month were then paid earlier. It’s being investigated. We’ve committed already that once that investigation is done, it will be shared with the company so that people understand what happened.”

[Narrator] “With over 1,500 customers impacted, rumors began to circulate about the causes of the incident.”

[Dan Taylor, managing editor at Tech.eu] “From my understanding, there was a creative code ‘malfunction’ that all of the sudden, double charged customers. But that double charge magically happened to meet Pollen’s payroll, that month. Hmm! Odd, don’t you think?”

[Narrator] “The internal investigation due to be shared with the company was never completed, but a group of Pollen staff did their own, unofficial digging. (...) The code contained in the report confirms that the customer's monthly payment plans had been manually altered, which meant that double or triple charges will take place on a single day, without the customer’s authorization.”

The engineer making this change even did a test run the day before, to ensure that this code change “correctly” double charges customers! A former Pollen software engineer appearing in the documentary also makes the point that any code changing production code in payments needs to go through code review, so whoever made this change could have not been acting alone.

Two days after the incident, a senior engineering team member sent an internal chat message to 3 colleagues, where they admit that they had run the script at the request of the CEO. Here is what this message said:

“Also want to come clean that it was me who ran a bad script - in hindsight I wasn’t knowledgeable enough to alter a subset of payment plans for Balvin [one of the events organized by Pollen]. I did this as a special request from Callum and didn’t want to raise on call to handle. It’s been a long week and I displayed a very poor form of judgement.”

In the video, a Pollen software engineer is shown the message, and he says: “I’m not sure I buy this. It seems a bit fishy.”

Lesson #3: if the CEO asks you to do something potentially illegal – document it, and consider not doing it.We don’t know what happened with the senior engineering member who carried out the code changes, following a request from the CEO. This person could have said no, like the engineering director at Frank did. The message sent a few days ago already said that this person regretted doing so, and it’s unlikely that this action was worth the risk it carried.

Update in Oct 2025: no criminal charges that I am aware of have been made related to this double charging at Pollen.

If you take one lesson from this, it’s that you can always say no.In these three stories, the only engineer who’s legally safe is the former engineering director at Frank who point blank refused to assist what could be an illegal request. The engineering director at FTX who stayed after he confirmed fraud was occurring is now facing jail time, while the senior engineering member at Pollen is at the mercy of the UK police, and how they deal with what could be a potential wire fraud case.

Subscribe to my weekly newsletterto get articles like this in your inbox. It's a pretty good read - and the#1 tech newsletteron Substack.
