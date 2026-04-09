---
title: My Bank Keeps On Undermining Anti-Phishing Education | Moritz M.
url: http://moritz-mander.de/blog/my_bank_keeps_on_undermining_anti-phishing_education/
site_name: hackernews
fetched_at: '2025-07-18T04:06:52.206190'
original_url: http://moritz-mander.de/blog/my_bank_keeps_on_undermining_anti-phishing_education/
date: '2025-07-18'
published_date: '2025-06-09T00:00:00+00:00'
description: 'TLDR: my bank sent out emails with websites which looked a lot like phishing mails, so much so that this similarity could potentially be used against them legally by potential phishing victims – Discussion at hackernews (soon) Chapter 1: You’ve got mail As I was writing my first post some weeks ago, I got an email from my bank in my inbox:'
---

TLDR: my bank sent out emails with websites which looked a lot like phishing mails, so much so that this similarity could potentially be used against them legally by potential phishing victims

– Discussion at hackernews (soon)

## Chapter 1: You’ve got mail#

As I was writing my first post some weeks ago, I got an email from my bank in my inbox:

Here the English translation of the email:

Dear …,

The big Wero Win Weeks are starting! Take part now and secure your chance every week to win 7 prizes of €1,000 each.

With Wero, you can send money from account to account in under 10 seconds. It’s easy, fast, and secure. And the best part: If you register once for the prize draw now, you will automatically participate in the draw until September 2nd. With a chance to win every week!

Join now! Win €1,000 seven times every week!

Here’s how it works:

Some background information for my non-German readers:What is a Sparkasse?The bank in question is my local Sparkasse. Sparkassen are regional savings banks that exclusively serve people in their region. They are generally owned and sponsored by their serving municipalities. Each Sparkasse is an independent institution, but they are all connected through an umbrella organisation, which coordinates their activities, ensures interoperability and gives it an overarching corporate design. Their areas are focused on SMEs and private customers, and in general, they have a strong local economic impact and are serving a lot of people. All institutes combined, the Sparkassen financial group is the largest financial service provider in Europe.A link to the Wikipedia article.

What is Wero?

The email in question was promoting Wero. And I do not mean the Māori challenge, which is part of the welcoming ceremony. Wero is a new European digital payment system launched by the European Payment Initiative (EPI). It was created to replace several local payment systems, which were only used in the respective countries. Imagine it more or less like a rival to PayPal, just decentralised among all banks. Initially it focused on P2P payments (which is promoted in this mail), but sometime they plan to support online and in-store payments. They are still in an early adaptation phase.A link to the Wikipedia article.

This email address wasn’t on a spam list yet, so I was quite confused. I mean, the indicators are clear:

* You can win quite a large sum of money
* The prize draw without context (more on that later)
* Contains a link to a domain unrelated to my bank (“gewinnen-mit-wero.de”)
* The text in the subject and the body are very generic and tonally like phishing emails.

As there is nothing like free lunch, this must be spam. But on the other side:

* The sender address is a domain from my local Sparkasse institute
* The email is personalised with my name

I went to my bank’s website and checked whether the prize draw really exists and if they use the same domain. And they do. So I started to get angry: How can a trusted institution like a bank send such a spam-looking mail? Then I went to the website, and it just got worse…

## Chapter 2: It gets worse…#

Here the English translation of the website:

### Send money. Win money. With the Wero-Win Weeks#

Fill out the one-time participation form.
Send money with Wero in the Sparkasse app.
Automatically be entered into the prize draw with every amount you send.*

Promotion period: 18.03. to 02.09.2025
Participate now

### Send money, win, celebrate#

Anyone who sends money with Wero has the chance to win one of seven weekly cash prizes worth €1,000 – every week brings a new chance!

### Wero-Win Weeks. Join now!#

1. Register: Sign up once.
2. Send money: Send money at least once a week with Wero to friends or family. By the way, in order to participate in the prize draw, you must agree to the “analysis of data from payment transactions.”By agreeing to the analysis of payment data, you participate in the prize draw.
3. Increase your chances: Every successful payment earns you a spot in that week’s prize draw.
4. Didn’t win? Your entries remain valid.

Important:A maximum of seven payments per week will be counted. You only have a chance to win in the weeks when you send money with Wero.
Each week, seven €1,000 cash prizes are awarded.

Haven’t activated Wero in the Sparkasse app yet? You can catch up easily.How to activate Wero in the Sparkasse app.

Participation Form:

First name

Last name

Date of birth

IBAN

Email address

☑ I accept the terms and conditions and privacy policy. I am aware that Sparkasse employees are excluded from participating.

☑ I would like to receive email updates and news about the prize draw. I can revoke this consent at any time.

Submit

### What is Wero?#

Wero is the new payment solution for sending moneywithin seconds– directly from phone to phone.

Secure and fastSend and receive money in under 10 seconds.

TransparentKeep track of incoming and outgoing transactions on your account in real time.

Simple and always availableFrom account to account, directly in the Sparkasse app – even on weekends.

No IBAN requiredForget account numbers – to use Wero, all you need is the recipient’s phone number or email address.

You can find more information about Wero at sparkasse.de

### How do I activate Wero in the Sparkasse app?#

Open the Sparkasse app on your smartphone or tablet, or download it now:
[Google Play] [App Store]

Activate Wero in the “Send Money” section or via your profile settings:Activate Wero in the Sparkasse app

### How do I send money with Wero?#

SEND MONEY WITH WEROWERO

FAQ | Terms & Conditions | Privacy | Prize Draw Legitimacy | Imprint
© 2025 S-Payment GmbH

The design language is quite straightforward, but it directly rings a lot of alarm bells inside me. Some things you may immediately notice:

* The website does not give a hint of the Sparkassen branch, which I am a customer of. Remember, each Sparkasse is a separate, independent institute.
* The domain (“gewinnen-mit-wero.de”) looks really generic and has nothing to do with the institute. Everybody could register this domain.
* The SSL certification is from Let’s Encrypt and not from one of the major root CAs. While everyone can register for free on Let’s Encrypt, only (or mostly) serious companies pay money to register on DigiCert, GoDaddy, and so on.
* There is no context for why the prize draw is happening. On most draws, companies try to find a reason (like Christmas, jubilee, etc.), but nothing is named here. The only thing which is highlighted is that you can win a lot of money. That is something you mostly see in scams.
* Most importantly, to participate, you need to enter your full name, birth date, IBAN and email address. Nowadays, it is common to participate from inside the app, especially if it is mobile-first like Wero. This is the first time in a long time that I have seen that you need to register on a separate website.

And this made me really angry. How are we supposed to educate users about how spam and malicious websites look like when real entities promote their crap like this? When a trusted institution, like a bank, uses similar practices, it completely undermines everything we try to teach users, especially since we are talking about the largest financial service provider in Europe [^1]! As a result, users may begin to question every suspicious email they receive, thinking, “This looks like spam, but it might actually be legitimate…”

I didn’t dig deeper than that, as white hat hacking is criminalised in Germany. Our current laws do not distinguish between malicious and ethical hacking.

But it is not even the first time that they have done something like this:

Some years ago, I received an SMS from the same bank. On one side, I forgot that I gave them my phone number. But on the other side, the SMS looked like this:
“Here is your Sparkasse. A very important document is waiting for your signature. Please visit paperless.io/548fkjgd7f to continue.”(I couldn’t find the original SMS, but the text and the domain were pretty much similar to this)It was so suspicious to me that I even called my bank to make them aware that this scam was circulating, and I was made aware that the SMS was real. It contained a legal document I wasn’t anticipating. But the lady on the other end couldn’t even understand why I thought this was spam…

## Chapter 3: A plausible solution?#

Now, how can we solve this mess?
Of course, I do not know the exact internal structures and reasons for the decisions.

The safest way is to implement this prize draft inside the app itself. The Sparkasse can still send out emails promoting it, but without a suspicious-looking website. But I suspect that it was probably not possible to implement a prize draft into the application itself, just because one of the many participating banks organises one.

So the next idea is to register the domain as a subdomain of sparkasse.de (the official website of the umbrella organisation) or as a subdomain of the local institute. Even a CNAME should be sufficient. However, as I suspect that the prize draw is on the level of the umbrella organisation of the Sparkasse, I think the first one makes more sense than the latter. A similar thing recently did the German government:

In 2023, the German government issued students money to help them financially during the price spikes of gas because of the just-started invasion of Russia into Ukraine [^2]. Every student could claim this money by visiting einmalzahlung200.de. The domain was so weird that misspelling was common: einmalzahlungzweihundert.de. It was so common that one guy set up a website with a misspelt domain to make us aware of the misspelling and a link to the real website. Next to the generic domain name, it also wasn’t designed like other government websites. It just looked like spam.[^3]

As a response to that and similar cases, the German government launched a “digital umbrella brand”, which will give all services of the federal government, state governments and all connected sub-organisations a similar look and feel - and additionally a common root domain with gov.de [^4]. I already saw it in use for Veterans Day, for which they created the website “veteranentag.gov.de”.

## Chapter 4: From careless mistakes to courtrooms#

Just on the day I wanted to release this blog post, I found an article about a Sparkasse needing to pay some money back to a phishing victim [^5]. While this verdict was about problems with the design of the 2FA, it got me thinking: May there even be a legal problem when they accustom customers to sloppy websites with weird domains where they need to enter sensitive information?

Indeed, there are some interesting rulings [^6], where the specific Sparkassen institutes were ruled to refund the phishing victims. In each case, the court checked if the victims acted in gross negligence, for example, by carelessly disclosing sensitive access data. In these two cases, the courts couldn’t find gross negligence on the part of the customer, so the bank is generally obliged to compensate for the damage.

If a phishing attack based on a similar mail and website were performed now, it could be hard for the bank to prove that the customer acted in gross negligence, as this legitimate mail and website are almost indistinguishable from phishing emails and websites.

As a result, the sloppy promotion could make it possible for victims to sue Sparkasse if a phishing attack with a similar website is performed. I’ll admit, I’m stretching the argument here; additionally, I really want to point out that I am no legal expert, so there’s no way I’d bet my neck on it. But from the bank’s perspective, it is a point worth considering.

## Conclusion#

While cybersecurity is finally taken seriously on the technical side of things, it still seems to be a blind spot on the usabile security side. This email and website seem rushed, as so many good practices were ignored.
It will have a lasting effect on undermining phishing education in general, not just for this specific bank. This issue is especially prominent now, as courts are more frequently finding banks liable for insufficient measures against phishing. And on that point, we haven’t even touched the exposure of personal financial transactions for the sake of the prize draft.

How should a single person proceed in this matter? The issue is systemic, and the bank will likely not change its policy based on a single piece of feedback. What makes me a bit hopeless is the point that we are not talking about an SME or a private project - we are talking about the largest financial service group [^1] in Europe! So I guess the only thing left to say is: Please do not undermine security education? Maybe even take a look at it as well? Please?

Discussion at hackernews (soon)

[^1]https://www.sparkasse.de/ueber-uns.html#groesste-finanzgruppe-europas-und-gesellsc

[^2]https://www.handelsblatt.com/finanzen/steuern-recht/recht/einmalzahlung-wie-studierende-jetzt-noch-200-euro-energiepauschale-erhalten/29391432.html

[^3] As a small side note: the undermining of usable security practices was just one of many controversies around this undertaking. It was also criticised for forcing the creation of a federal bundID account (https://www.heise.de/news/Zwang-zu-BundID-Streit-ueber-Auszahlung-der-Energiepreispauschale-fuer-Studenten-7518235.html) and its technical issues when it started (https://www.heise.de/news/Energiepreispauschale-Holpriger-Start-der-Einmalzahlung-fuer-Studenten-7549625.html).

[^4]https://www.digitale-verwaltung.de/Webs/DV/DE/aktuelles-service/digitale_dachmarke/digitale_dachmarke-node.html

[^5]https://www.heise.de/en/news/OLG-ruling-S-pushTAN-procedure-not-sufficient-for-strong-authentication-10477555.htmlis the article andhttps://openjur.de/u/2528019.htmlis the original ruling

[^6] Az.: 2 O 312/22,https://www.anwalt.de/rechtstipps/phishing-sparkasse-muss-schaden-in-hoehe-von-ca-42-000-euro-ersetzen-232489.html; and Az.: 15 O 267/22,https://bruellmann.de/online-banking-sparkasse-muss-phishing-opfer-schadenersatz-leisten
