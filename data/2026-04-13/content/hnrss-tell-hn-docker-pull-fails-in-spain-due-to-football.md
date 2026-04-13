---
title: 'Tell HN: Docker pull fails in Spain due to football Cloudflare block | Hacker News'
url: https://news.ycombinator.com/item?id=47738883
site_name: hnrss
content_file: hnrss-tell-hn-docker-pull-fails-in-spain-due-to-football
fetched_at: '2026-04-13T12:02:39.251799'
original_url: https://news.ycombinator.com/item?id=47738883
date: '2026-04-12'
description: 'Tell HN: Docker pull fails in Spain due to football Cloudflare block'
tags:
- hackernews
- hnrss
---

Hacker News
new
 | 
past
 | 
comments
 | 
ask
 | 
show
 | 
jobs
 | 
submit
login
Tell HN: Docker pull fails in Spain due to football Cloudflare block
961 points
 by 
littlecranky67
 
23 hours ago
 
 | 
hide
 | 
past
 | 
favorite
 | 
353 comments
I just spent 1h+ debugging why my locally-hosted gitlab runner would fail to create pipelines. The gitlab job output would just display weird TLS errors when trying to pull a docker images. After debugging gitlab and the runner, I realized after a while I could not even run "docker pull <image>" on my machine as root:

> error pulling image configuration: download failed after attempts=6: tls: failed to verify certificate: x509: certificate is not valid for any names, but wanted to match docker-images-prod.6aa30f8b08e16409b46e0173d6de2f56.r2.cloudflarestorage.comFirst blaming tailscale, dns configuration and all other stuff. Until I just copied that above URL into my browser on my laptop, and received a website banner:> El acceso a la presente dirección IP ha sido bloqueado en cumplimiento de lo dispuesto en la Sentencia de 18 de diciembre de 2024, dictada por el Juzgado de lo Mercantil nº 6 de Barcelona en el marco del procedimiento ordinario (Materia mercantil art. 249.1.4)-1005/2024-H instado por la Liga Nacional de Fútbol Profesional y por Telefónica Audiovisual Digital, S.L.U.
https://www.laliga.com/noticias/nota-informativa-en-relacion-con-el-bloqueo-de-ips-durante-las-ultimas-jornadas-de-laliga-ea-sports-vinculadas-a-las-practicas-ilegales-de-cloudflareFor those non-spanish speakers: It means there is football match on, and during that time that specific host is blocked. This is just plain madness. I guess that means my gitlab pipelines will not run when football is on. Thank you, Spain.

 
help

danirod
 
21 hours ago
 
 | 
next
 
[–]

Heh, lucky you, at least you get a message. My ISP just drops traffic to the affected IPs. No ping, no traceroute, just a spinner in the browser until it says "page not found".

Every response and comment from LaLiga, the football organization responsible for this, has been so far that this is a minor issue that only affects a few bunch of nerds who talk about "docker images" or "github repositories" or "whatever that means".Meanwhile, there are testimonies of smart home devices like anti-theft alarms or automatic doors, that stop working whenever there is a football match, because their backends rely on Cloudflare.Last week, a woman asked for help on social media, as the GPS tracking app she uses to see where her father with dementia is, went offline during a match. It was getting late and he still wasn't back home, and she couldn't locate the tag he was wearing to find him:https://www.infobae.com/america/agencias/2026/04/05/laliga-d...It's hard to say this, because no one should experience an event like this, but as stressful as these are, it's the only way to make the mainstream people care about this censorship. "I cannot pull a docker image" will never be on nightly news, but safety and personal security is a more powerful driver for discourses.

reply

pxc
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

> Heh, lucky you, at least you get a message. My ISP just drops traffic to the affected IPs. No ping, no traceroute, just a spinner in the browser until it says "page not found".

This is generally how the GFW works in China. Instead of an overbearing nanny like a school or corporation's DNS blocker, you're left with a sense that you're on a version of the Internet that is just intermittently and somewhat mysteriously broken.And indeed, in China, a lot of things that probably aren't fully intended to be blocked are not reliably accessible. Implementation varies, so you get strange routing and peering issues. It feels like an Internet that isn't fully formed, that hasn't finished coming together yet.Nation states and corporations obviously gain some things sometimes by having Internet censorship/blocking frameworks in place. Maybe, sometimes, ordinary people even benefit, too, if it helps shut down illegal and genuinely harmful businesses.But it feels like the whole world is gradually trending towards more and more Internet censorship without realizing that we areun-buildinga miraculous thing that took enormous effort and cleverness and expense to build. I wish we could think about this not only in terms of freedom (and we absolutely should think about it in terms of freedom), but how we aredisintegrating the infrastructureof communication and computing.

reply

goodcanadian
 
10 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is generally how the GFW works in China. Instead of an overbearing nanny like a school or corporation's DNS blocker, you're left with a sense that you're on a version of the Internet that is just intermittently and somewhat mysteriously broken.

Oh boy, an excuse to share my favourite great firewall story on a visit to China. Keep in mind, this is 15 years old, so probably doesn't represent the current state of affairs. At the time, my daily news reading habit had me checking BBC and CBC (Canadian Broadcasting Corporation). The BBC site seemed to be working fine, but whenever I clicked on an article on CBC, it was blocked. A few minutes later, I went to show my wife that CBC articles were blocked, and I clicked on the same one again, and it loaded. I clicked on another: blocked. Tried it again after a few minutes and it loaded. Someone was screening the articles in real time for me. When I was done reading, I clicked on several of the weirdest headlines I could find, and after a few minutes, everything was blocked again including ones that had previously worked.

reply

RiverCrochet
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Your last paragraph: it is sad. But we had successful global networks before the Internet (the PSTN, telegraph) and we'll certainly have global networks after this at some point in human history. Perhaps in the the time between the Internet and what's next, the world will become a bit more mature about a few things.

reply

Spooky23
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Those predecessor networks weren’t problem free. Many conversations to “interesting” places were monitored.

The counter-reaction to this era will include additional communication control.

reply

jazzyjackson
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

this is teleological thinking. it's not necessarily the case that things get better over time.

reply

dingnuts
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

there's a lot of evidence things do generally get better over time, though. Jon Haidt and his ilk... I forget all involved... have done research into it

obviously it can be bumpy and maybe there's a Great Filter or you happen to live during a bad period but life is certainly much longer and less brutal than it was for 99.9% of human history

reply

mschuster91
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> But we had successful global networks before the Internet (the PSTN, telegraph)

These were ripe with espionage, wiretapping and sabotage. Access to it used to be highly restricted as well, up until the 90s for example you were only allowed to connect government-licensed modems to the German PSTN directly.

reply

RiverCrochet
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> These were ripe with espionage, wiretapping and sabotage.

Just like today's Internet. BGP spoofing, CALEA, DDoS.> Access to it used to be highly restricted as well ...And this is where the regression or "downfall" is beginning. Access to the Internet (as in ability to send/receive arbitrary data to the wider Internet) is something I bet is going to be increasingly restricted, but most people won't notice because they don't understand the difference between apps and the Internet.I'd be surprised if direct access to the Internet is possible for consumers in the next 10 years. Everything will have to be through approved apps (age assurance is going to be the catalyst) that work over registered tunnels contracted through ISPs, if there isn't an outright blurring or merger between the concepts of phone/CPE, ISP and CDN. Your non-tech layperson will not know any difference whatsoever if all they use are their phone plan, streaming/banking apps and Facebook.

reply

angry_octet
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Surely this was simply the nature of Deutsche Bundespost / Deutsche Telekom? Like, of course you had to use hardware they had approved to connect to their network.

This was the same in many places. The cost of hardware and connection time limited connections, and no one had cryptography except the government and ultra nerds.

reply

sneak
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

There was also no way for a normal person to easily and cheaply communicate with 20 million people in realtime.

reply

nrds
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> a version of the Internet that is just intermittently and somewhat mysteriously broken.

That's actually just how the Internet is. Nothing to do with the great firewall.

reply

freetanga
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

All people affected should file a complaint with your ISP and with Oficina de Atención al Usuario de Telecomunicaciones claiming financial loss for arbitrary service censorship.

reply

embedding-shape
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've been filing complaints since a year ago, told others to do the same too, nothing happens. There been moments I've meant to deploy fixes to issues but I cannot, because some tooling goes offline.

I've claimed financial loss, claimed sanity loss and everything in-between, but I'm afraid unless something reaches the European/EU courts, Spain will continue to be in the pocket of the La Liga owners.Straight up fucking censorship with wide collateral being completely accepted in a Western country in 2026, beyond comprehension how this is allowed.

reply

ryandrake
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Whenever I get a little down over how much power unelected corporations have in my country, I can at least cheer myself up a little by being thankful that something as stupid as 
football
 doesn't have enough power here to control whether or not I have internet access.

reply

necovek
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

La Liga is basically operating like an "unelected corporation" as well.

reply

embedding-shape
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Ignorance is a bliss, agree :) Sometimes we all need to force ourselves into that so we can get a bit more joy.

reply

sneak
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It would if it were bigger business in your country. Try torrenting an MCU movie and see what happens to your ISP account.

reply

bombcar
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Someone in Texas torrenting an MCU slop doesn’t disconnect me from half the Internet.

reply

voidUpdate
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

In my experience, nothing...

reply

fn-mote
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Out of curiosity, what does happen?

reply

Semaphor
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

AFAIK not much in most of the world, in Germany you get a letter from lawyers wanting ~1000 EUR

reply

SturgeonsLaw
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In Australia the court ruled that they can only sue for the cost of renting the movie, so they don't bother trying to recoup their ten bucks

reply

iamtedd
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That's interesting. Do you have further reading? I've seen AFACT v iiNet, but that doesn't look to be the source of "cost of renting", just that the ISP isn't responsible for their users.

reply

dariosalvi78
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

these things need to be brought to an international court who would require the government to act. Otherwise nothing happens, because institutions are completely corrupt.

It takes time, money and a strong legal team, but maybe IT companies maybe can put this together?

reply

drnick1
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If this is done at the DNS level, run your own DNS. If not, use a VPN. Taking this to the courts is a long term solution, but in the short term you want to act on your own to evade censorship and oppression.

reply

gschizas
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> run your own DNS

Can you expand on that? How would you go about running your own DNS that wouldn't be affected by football leagues?

reply

martheen
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If it's purely DNS blocking (no IP redirection or blocking), your own recursive resolver (eg, unbound) shouldn't be affected, assuming the ISP doesn't also intercept unencrypted DNS queries. If there's also interception, encrypted DNS upstream might help (assuming they're not blocked entirely, repressive countries do this, so far not in EU)

I don't think any of them will help in Spain case though, I believe the ISP/court choose to block the IP range entirely, which hit Cloudflare customers. DNS hijinks won't solve those.

reply

rock_artist
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If anyone who’s capable in Spain set a petition or the relevant steps and put it on HN. I’m pretty sure any Spanish resident in HN would be more than happy to take part even if it means to send a Bizum for the cause.

(Sadly as living in Spain for about a year I’m still not in such place to raise this or understand the full steps needed)

reply

lentil_soup
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

how do you make claims, here: 
https://usuariosteleco.digital.gob.es/
? Can't find a way of doing it with Cl@ve

reply

embedding-shape
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've used this: 
https://usuariosteleco.digital.gob.es/reclamaciones/telefoni...

Used my digital certificate (which is installed in the browser), but AFAIK, you can use Cl@ve on that page above too.In the past, I've cited BOE-A-2022-10757 (https://www.boe.es/buscar/act.php?id=BOE-A-2022-10757), done a reclamació for the repeated loss of lawful access on my connection, and a denúncia about a broader overblocking practice affecting access to lawful services.Also, supposedly, we should be able to make claims to CNMC as well, but haven't figured out how. Also of course, been complaining to my ISP every time it happens too.

reply

GranPC
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I think this is it: 
https://reg.redsara.es/#login

reply

madaxe_again
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It’s football. I’m pretty sure there are a great many countries you could induce to do insane things if the populace could be made to believe that said insane things will help football.

I mean, didn’t El Salvador and Honduras go to war over football back in the 60’s? And I seem to recall there was a football match which helped precipitate the dissolution of Yugoslavia - national identities coalesced around football tribes.

reply

emptysongglass
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Because the EU as a whole is quite happy to censor and generally wield the same tricks as "non-Western" countries in their desires to combat misinformation (however our EU bureaucrats define it), child abuse materials (see Chat Control that thing is not going to go away), and hatred (oh boy).

We've never guaranteed the right to free speech and because we haven't it's a slippery slope all the way back down to the furnaces of autocracy we sprang from.The Spanish president has come out on record saying we don't deserve anonymity on the internet.

reply

megous
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Not sure why you get downvoted. EU censors quite a bit. I can't read about 10 Telegram channels that I could access just 3 years ago, and the list is growing.
All due to "vioalted laws of [my country]". (said near-east related channels have nothing to do with my country, government just doesn't want me to read them)

Some people deemed "russian assets" are not just censored, but stripped of ability to leave EU and prevented from being able to live in EU at the same time by financial sanctions, etc. Of course this doesn't happen to actual politicians in power, for whatever reason those never get sanctioned by EC, despite doing more "damage" than random blabberheads on twitter.It's a mess.

reply

loloquwowndueo
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It would be great if there was a webpage with clear instructions on how to do this, maybe fill out a few questions and get a printable pdf you can mail, or at least telling you how to file an online complaint. Making complaints very low friction will lead to more of those and perhaps more attention to the issue.

Snail mail uses up physical space so it might get more attention, it would be hilarious to see news reports of truckloads of complaint mail being dumped in front of the whatever office.

reply

embedding-shape
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> It would be great if there was a webpage with clear instructions on how to do this, maybe fill out a few questions and get a printable pdf you can mail, or at least telling you how to file an online complaint. Making complaints very low friction will lead to more of those and perhaps more attention to the issue.

This is a great idea, we definitively should make this happen! If people are curious on collaborating on something, reach out, email in profile (English or Spanish emails welcome!).

reply

bakugo
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Sadly, it won't accomplish anything. La Liga seems to have enough political power in the country to bury all of that. Probably bribing everyone involved.

reply

cluckindan
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Corruption at that level could mean organized crime. Is there a culture of betting through illegal bookies, are they fixing matches, or ¿porque no los dos?

reply

hdgvhicv
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

FIFA makes the mafia look like a bake sale committee

reply

hunterpayne
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

No, its worse than that. If you wish, learn about FIFA and how it works. At least the mafia fears the government somewhat...FIFA doesn't.

reply

embedding-shape
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Well, I think when the organized crime is registered as proper businesses and they have the judges on their side even if the law isn't, I think we just call that "for-profit capitalism" nowadays.

reply

dualvariable
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

penalti para el real madrid!

reply

pixl97
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yep, flood them with complaints.

reply

bluecalm
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's Spain man. Nothing will happen, maybe they will call their buddies in La Liga to ask what's up if the complains pile up and then will ignore all of them if they are assured everything works as expected.

reply

estebarb
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

At this point the protests should be against the matches themselves. But let's be honest: nobody cares anymore.

reply

xp84
 
7 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Who cares if she can’t find her elderly father? A small price to pay to preserve the stratospheric prices on football TV rights!!!!

reply

vasco
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The thing is it doesn't protect anything. All it does is funnel money to VPN providers

reply

the_gipsy
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It's ridiculous and wrong what LaLiga does. But it's also a weakeup call to consider ditching cloudflare's centralization.

reply

estebank
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The companies relying on cloudflare won't be in Spain. If you buy a GPS tracker by a Canadian company, developed in India, manufactured in China, they are unlikely to know, even it they cared, that a single country that accounts for a tiny percentage of their sales breaks fundamental internet infrastructure on the regular "because fútbol y dinero".

And when purchasing a product, there's no "bill of materials" telling you about the services it relies on, beyond "internet connection" at best.

reply

otabdeveloper4
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> breaks fundamental internet infrastructure

I think lots of countries block Cloudflare whole-sale.Laundering IP addresses for (or against) shady purposes is, in fact, Cloudflare's whole business. It's a wonder Cloudflare isn't being blocked more often.

reply

encom
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

>fundamental internet infrastructure

I'm not saying this situation isn't bullshit, but the bigger problem is that CloudFlare is now "fundamental internet infrastructure". This is precisely the situation that the internet was designed to prevent.Yesterday I got stuck in endless CloudFlare CAPTCHA's, trying to access theretroweb.com. I had to give up. Many such cases. I hate CloudFlare so much, it's unreal.

reply

embedding-shape
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> This is precisely the situation that the internet was designed to prevent

Right, but on the other hand, our constitution and laws are supposed to give us the rights to access a internet where the government cannot block entire companies who host websites, because a few bad websites are hosted there.Not to mention all us freelancers, contractors and just in general computing users, who sometimes want to continue working although 90% of the country is watching football, we should be able to do so even if pirates use Cloudflare for shitty stuff.I agree that Cloudflare sucks, people should avoid defaulting to putting Cloudflare in front of absolutely everything they do and I too get stuck at the CAPTCHAs sometimes. But that doesn't remove the fact that Cloudflare, just like every other lawful company, should be allowed to be visited during La Liga matches.

reply

rightofcourse
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The LaLiga post seem to accuse Cloudflare of unlawful activity directly by protecting criminals, not just the illegal streamers. At least my reading (of Google translation) is that they target Cloudflare here and it works "as expected" since Cloudflare is the bad guys.

reply

bombcar
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I’d love for a way to put all my sites behind Cloudflare 
only
 during La Liga matches.

reply

girvo
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I’d happily use anything else, but it (with CF Tunnels and its DDoS and caching systems) is what lets me self host on my little home server on today’s internet. Would gladly move to some other system (or systems)

reply

j0057
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It takes very little money to rent massive botnet capacity to perform crippling DDOS attacks. Unfortunately there are only very few CDNs capable of absorbing that kind of attack.

reply

miki123211
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The only reason this happens is because Cloudflare's centralization makes precise censorship impossible. That's bad in this particular case (as it results in over-broad censorship), but good in general, as it makes censorship harder.

Without Cloudflare, you can censor whatever you want. If you have the support of an (undemocratic) government on your side, you can even DeDoS them, making sure that information critical of you cannot see the light of day.

reply

direwolf20
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Cloudflare has nothing to do with it. Actually you should further insist on using Cloudflare in Spain to increase the collateral cost of this ridiculous government decision as much as possible. Make it so not a single website works during football, and see if the government changes their tune.

reply

cryptonym
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

If cloudflare is providing services to illegal websites, they very much are in full control of the situation. They knowingly choose to keep hosting that content, and have legal customers exposed to that risk.

You may like that the platform is open by default to everybody, but that's the obvious consequence.

reply

lukan
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Does cloudflare refuse a court order to take down a site? I don't think so.

reply

trailheadsec
 
13 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I agree with this take (that it’s a wake up call). Makes one question their entire app design and if using Cloudflare is “good enough” for managing CDN, tunnels, etc. for their apps.

reply

matheusmoreira
 
6 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> Every response and comment from LaLiga, the football organization responsible for this, has been so far that this is a minor issue that only affects a few bunch of nerds who talk about "docker images" or "github repositories" or "whatever that means".

Translation: go away kid, we're trying to make money here.

reply

tobz1000
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> there are testimonies of smart home devices like anti-theft alarms or automatic doors, that stop working whenever [...] because their backends rely on Cloudflare.

The fault here lies 100% with horribly designed IoT devices that turn into bricks when they lose internet connection.

reply

shibapuppie
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yeah the horribly designed alarm system that can't alert a central authority that something has gone wrong. Maybe we should just put huge air raid sirens on our homes instead?

reply

boredatoms
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Perhaps its time to put a VPN into all your CI jobs

reply

tryauuum
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You can't fight political issues with clever technical solutions

reply

toast0
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It depends on what the political system is trying to do.

A VPN won't help against government blanket outages, where the target is complete control of communications, and attempts to circumvent may result in extreme penalty. In this case, where the government policy is to stop unauthorized streaming, and collatoral damage is acceptable, a VPN hosted in a more favorable location is likely to work enough. Afaik, I don't think Spain has the political appetite to block VPNs and such during football matches.You can still fight the political issue with political means, but in the mean time, you can also get work done.

reply

swiftcoder
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Afaik, I don't think Spain has the political appetite to block VPNs and such during football matches

Unfortunately nobody is quite sure what appetite they have, because LaLiga is doing this all on the back of a relatively narrow judicial ruling that hasn't been reviewed in a long time

reply

peanut-walrus
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Yes you can. Fight with clever technical solutions and the politics will follow once the solution becomes common or displays its usefulness. It is in fact the most effective way to fight dumb political issues.

reply

tryauuum
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

In my country (Russia) the politics followed, now the ISPs block the OpenVPN and wireguard packets. And sometimes the white list mode is enabled, so you cannot connect, with your clever custom VPN solution, to a host outside the country

reply

necovek
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You should be able to use things like sshuttle or even tunnel through HTTPS whatever you want, right? As you can control both sides of the tunnel with encryption (comes by default), no MITM-ing unless you are forced to use solutions that install and eavesdrop on your secure traffic too.

reply

out_of_protocol
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

1) they do protocol sniffing, and any inconsistency (including statistical) gets you blocked
2) "white list mode" which engaged sometimes (poorly implemented atm), means nothing goes outside of country at all (means 99.9% of everything is broken). They really want to become North Korea soon

reply

necovek
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Are any streaming sites allowed? It should be really easy to make a VPN through HTTPS tunnel appear to have a traffic pattern exactly like you are streaming videos and/or music (depending in the bandwidth needs) by throwing discardable traffic through when no valuable traffic is needed.

Obviously, everything can be cut off, but the point is that if encrypted something is allowed, there should be a way to get anything through.

reply

bryan_w
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If they turn off the internet, that gives you more time to meet your neighbors and do "arts and crafts" and read (cook)books. He's getting so old, at some point the horse throws him off

reply

peanut-walrus
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

And eventually even a worm will turn.

reply

psychoslave
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That's actually part of rebellion modus operandi, so totally something realistic. But not within the frame of law and not in the sweet position of someone away from the "I'll die for the just cause" mindset.

reply

tryauuum
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

can you rephrase your idea please. What's realistic, fighting stupid laws or corporations with a VPN? Yes, but not for long. They are always stronger than you, they can switch from blacklisting to whitelisting and your VPN becomes useless.

What is this "sweet position" you talk about?

reply

psychoslave
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sorry for being unclear.

I was trying to refer to an actual rebel position, which is actors which use illegal practices to achieve their goals agaisnt institutions in place. Which might have the cool attitude imagery attached to it, but which is certainly not an easy one in reality.

reply

logicchains
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You totally can, that's why bittorrent still exists and works fine.

reply

fc417fc802
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

That became a popular refrain at some point but the truth of it varies. In fact many political issues are brought about by technical changes so obviously the reverse must be possible as well.

What technical solutions can't change is the underlying social dynamics.

reply

necovek
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Even that is IMO untrue: "technical solutions" have indeed changed society at large quite significantly; eg. "social media" is one very influential example, "smart phone" is another, "internet" itself, etc.

reply

fc417fc802
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Aren't you agreeing with me? None of those things changed the underlying social dynamics that humans exhibit but they nonetheless affected widespread social and political change.

reply

utrack
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

They block the whole of Cloudflare R2, I believe the Docker hub is just (heh) a collateral.

When the La Liga match starts, everything that's proxied via CF (including zero access reverse tunnels) stops working.There's even a website made for checking if the match is on:https://hayahora.futbol/You can check if your host is affected:https://hayahora.futbol/#comprobador&domain=docker-images-pr...

reply

micw
 
7 hours ago
 
 | 
parent
 | 
next
 
[–]

Who exactly is blocking and on what legal base? If it's Spanish ISPs and they are massively over blocking, why are there no legal actions against them? (E.g. for not fulfilling their contracts)

reply

dariosalvi78
 
1 hour ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

it's institutional corruption at all levels, legislative, executive and judicial. A systemic failure that favour abnormous private profits over basic rights of the citizens.

The effort required to change the situation is massive.

reply

Parodper
 
2 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

ISP are blocking, because of a district judge's ruling.

reply

nikanj
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

On the one hand, you have money and famous footballers. On the other hand, you have a bunch of nerds whining about the internet being broken. The average voter (and politician) is out watching the soccer match, and doesn't care about the internet.

reply

eazel7
 
2 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

then I think we should move all possible services to cloudflare
maybe when nothing works for them they start to care

reply

Moldoteck
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Football lobby is strong in Spanish political system. It's legal

reply

mr_mitm
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Why do they do that? Sorry, I don't speak Spanish.

reply

michaelt
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The football league would rather not have pirates livestream their ~90 minute games.

Pirates would rather not be blocked, so they create a new, disposable website for every game. Any blocking must happen fast.Cloudflare would rather not block websites without a court order specifying the sites to be blocked.The courts would rather not create a special fast lane through the courts, just to resolve a squabble between two huge corporations.

reply

n6242
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> The football league would rather not have pirates livestream their ~90 minute games.

Funny enough, I work in IT and I've had to use a VPN to be able to do my job when soccer is on, but my two non-tech-savy family members that do watch soccer using pirate livestreams say that they've never had any issues with blocked streams.

reply

KAMSPioneer
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I work in IT and have found that the issue impacts my work but not my ability to stream sports from sites of questionable legality. Of course, I don't pirate La Liga matches but that's primarily because I don't give a shit about soccer.

But the point is that the measure does more to block legitimate use than illegitimate (in my experience). And next they want to go after VPNs. Wonderful.

reply

fc417fc802
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

But think of the children ... and futbol!

reply

miohtama
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Think of all political donations

reply

spwa4
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

But you must realize, the alternative to this is that some very wealthy Spanish companies ... lose a small amount of money.

Surely you understand now. Go about your business, poor person.

reply

ryandrake
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They don't even "lose a small amount of money." They simply gain less money than usual for a short period of time. Think of how rough that is for them.

reply

necovek
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I think it's even that they "gain less money than they could if everyone watching illegally 
would pay
 for it when they could not watch illegally" (that's usually how companies crying "piracy" calculate "losses" — "let's assume everyone watching illegally would certainly still watch it and pay the full price").

reply

shiroiuma
 
3 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

This isn't quite right either. It's "they gain less money than they might 
potentially
 gain if piracy weren't physically possible". If the piracy avenues didn't exist, how many people would actually pay full price to the legitimate sources, and how many people would simply go without?

reply

joquarky
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I once remember reading an article about shareholders selling off a stock because the rate of increase in profit had slowed.

reply

fireant
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

There is nothing wrong with that. Stock price is based on perceived future value , not current company profits.

reply

array_key_first
 
9 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Arguably they even gain more money in the long run, because more people have access to their entertainment and they have more opportunities to form life long connections with consumers.

reply

hunterpayne
 
11 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

In all fairness, the Spanish economy is a mine, a farm and a soccer league in a trenchcoat. Better than Ireland which is 2 tax shelters in a trenchcoat, but not by much. Not surprisingly, they are the 2 most left leaning countries in Europe. To be fair, they had an actual fascist government in Spain for several decades and there were atrocities committed.

reply

cool_dude85
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ireland, the country with 2 center right parties that differ with regards to patronage networks and political history from 1940, is one of the most left-wing leaning countries in Europe?

reply

lentil_soup
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> Cloudflare would rather not block websites without a court order specifying the sites to be blocked.

why would they?> squabble between two huge corporationsI think this is just LaLiga using it's cultural and economical power, don't think Cloudflare or the courts should be making exceptions just so they can control how people watch football

reply

mlyle
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> why would they?

Well, in this case, the alternative is all of Spain intermittently blocking lots of Cloudflare.But if Cloudflare bows to Spain in this case, every jurisdiction will want to pile up lots of special case rules for Cloudflare to try and implement.

reply

pxc
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

LaLiga isn't Cloudflare's customer. They have no relationship. So why would Cloudflare rework their infrastructure just to instrument rapid blocking at their own expense as a favor to LaLiga? And if they don't, ISPs just break the Internet for each soccer match? This is a kind of coercion that makes no sense. Cloudflare has no obligation like this to LaLiga (and neither would a Spanish domestic CDN!).

reply

mlyle
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The reason why entities comply with the wishes of courts is because there's consequences if they don't. Consequences like being filtered.

reply

pxc
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Cloudflare has not in fact refused to comply with any court orders! The very thing at issue is that LaLiga wants Cloudflare to do censorship on their behalf that Cloudflare, who has no contractual relationship with LaLiga, is not required to do by any legal framework in Spain or the US.

Cloudflare literally wasn't even a party to the ruling by which LaLiga has been compelling Spanish ISPs to do the IP-level blocking. They're just an affected third-party because the blocking scheme the courts have allowed LaLiga to impose onISPsis on a per-IP basis.Spainhasn't asked Cloudflare to do anything. Only LaLiga has acted like Cloudflare owes them a huge, expensive rework of their CDN's architecture for the purpose of censoring things for LaLiga purely as a favor to LaLiga. What LaLiga has over Cloudflare isn't a court order. It's a protection racket, or maybe a hostage situation, where court orders involvingother partiesare the gun held to the hostage's head.

reply

mlyle
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Cloudflare has not in fact refused to comply with any court orders!

Nor did I say they did.The question was asked, "why would they [without an explicit order]" The answer is they probably shouldn't, but there's still an obvious incentive here.

reply

forty
 
4 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm not sure why it shouldn't be cloudflare job to make sure they don't host illegal content. If my super market keeps distributing illegal goods, even if they remove it after a court order, they will end up having to close the whole market.

Either they should police the content they serve themselves or they accept the right holders to do it (which sucks for everyone).Also they certainly willing take all their customers as hostage, as they could certainly split their network into legitimate customers and shaddy ones so the blocking is not so impactful, but I guess they prefer to make it as impactful as possible to be able to complain.

reply

gruez
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

>why would they?

Plenty of companies proactively take action against shady users, even if not 100% required under law. Youtube has content id, social media companies have "community guidelines", and ISPs have AUPs.

reply

teaearlgraycold
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The US is captured by the Israeli lobby. Spain is captured by the football lobby.

reply

Pay08
 
17 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

So what, do they just block a range of IP addresses and are then done with it?

reply

swiftcoder
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

technically, LaLiga themselves doesn't even do the blocking. They have a court order from some years ago that allows them to compel all the individual ISPs to block any IP addresses they specify, with no oversight or review

reply

bartread
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This must negatively impact a huge number of businesses. Is there no move for them to all get together to take legal action against LaLiga to stop them doing this?

reply

hunterpayne
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is the country that takes a 2 hour nap every day. They also have a sleeping contest every year with a winner and everything. And Spain isn't hot like Mexico where folks take 2 hours off in the topically heat and make it up for it in the evening because that's more efficient.

reply

doetoe
 
5 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Have you ever spoken to a person from Spain?

reply

swiftcoder
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

or been to the south of Spain in summertime - it may not be Mexico-hot, but it's no picnic

reply

miohtama
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Think of the all political donations this would lose

reply

quadrifoliate
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Here's a good English-language article about it, with a timeline: 
https://daniel.es/blog/cloudflare-vs-la-liga/

Looks like same old regulatory capture.

reply

maest
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Also, a classic tweet from the Cloudflare CEO re their fight with Italians authorities re censorship:

https://xcancel.com/eastdakota/status/2009654937303896492Everyone looks bad in this conflict.

reply

post-it
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

How does this make Matthew look bad?

reply

encom
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Matt acting like he's a free speech absolutist. Hilarious.

reply

petcat
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Italy and Spain are the bad actors here. Not cloudflare.

reply

nslsm
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

HN in 2026: free speech is hilarious.

reply

encom
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You have it backwards. I'm the free speech absolutist. Cloudflare is not.

reply

bethekidyouwant
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

On a scale of oppression he certainly leans towards free.

reply

prmoustache
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Because LaLiga and football in general is what is governing Spain really.

reply

lentil_soup
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

to stop people pirating football streams while matches are on. Insanity

reply

bakugo
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

The website has a language selector on the right just below the initial screen, just FYI.

reply

ShowalkKama
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

to """"""""""prevent piracy""""""""""

reply

sva_
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Ah man, that shader in the background is like a rite of passage for people including a shader on their website.

https://www.shadertoy.com/view/lscczl

reply

aftbit
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Ah the irony, I'm blocked from viewing that page by Cloudflare

Performing security verificationThis website uses a security service to protect against malicious bots. This page is displayed while the website verifies you are not a bot.
Incompatible browser extension or network configuration

reply

jojobas
 
4 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Great, time to proxy through AWS, Azure and GCP so that these muppets block Spain from everything.

reply

isodev
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Very good example as to why using a single, centralised proxy globally by all services is a bad idea. Docker would never have a reason to block anything if they were simply running their own.

For everyone else, small and big, this is the weekly reminder to not use Cloudflare for user-facing access to anything.

reply

pajamasam
 
48 minutes ago
 
 | 
parent
 | 
next
 
[–]

There are multiple good reasons to use a CDN though. What’s your suggestion for an alternative?

reply

madbo1
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Reading this from India, where stuff like this is pretty much Tuesday business. But that’s not the problem; the problem is precisely the one hour of your life spent trying to figure out whether the issue is your DNS, your VPN, your configuration, or your programming. “The government in the country I’m accessing this from just decided to shut down my IP for the next two hours” rarely crosses your mind.

India has consistently been at the top of the number of Internet blackouts anywhere in the world for years (Access Now keeps track of this through its KeepItOn project). These tend to be brief and localized, triggered by something as mundane as an exam or protest or local incident. It’s such a routine occurrence here that there’s even a reflexive response: mobile data works differently from other connectivity types, so go with that, try new DNS settings, rely on Telegram instead of WhatsApp when the latter fails you, and always have a list of mirrors.What’s fascinating about this case is that it’s identical except for who is pressing the button LaLiga, a privately owned entity, in place of the government.

reply

teitoklien
 
39 minutes ago
 
 | 
parent
 | 
next
 
[–]

Bullshit,say one site that regularly causes this ?

Telegram always works, Whatsapp always works, Cloudflare Always works 
Only time any of those 3 have been down, is when the service is down globally itself.India mostly does blackouts in small town/district level regions or in provinces/states where mass-infighting is ongoing atm and they need to curb misinformation spread while Law Enforcement brings the fights down.In any major Indian city, regardless of what ISP you use, almost all major service providers always work , all the time.This issue is more prominant in rural towns or tier-2 cities with exams ongoingNot in any major Indian metro city

reply

mrvaibh
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

This is a great example of why blanket IP blocking is such a terrible enforcement mechanism. Cloudflare hosts hundreds of thousands of services behind shared IP ranges — blocking one IP to stop a piracy stream
 takes out everything else on that IP, including Docker registries, API endpoints, and CDNs that have nothing to do with football.

The real fix on your end until Spain sorts this out: set up a pull-through registry cache (e.g. registry:2 with proxy.remoteurl) on a VPS outside Spain, and point your Docker daemon's mirror config at it. Your
 GitLab runner pulls from the cache, the cache pulls from Docker Hub via a non-blocked IP. Also insulates you from Docker Hub rate limits.

 But yeah, the fact that a court order about football streaming can break docker pull for an entire country is genuinely absurd.

reply

embedding-shape
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

> This is a great example of why blanket IP blocking is such a terrible enforcement mechanism

AFAIK, they're not doing "blanket IP blocking", they're intercepting requests based on DNS and IP, and try to serve their own certificates and their own content. Obviously, in most cases it fails, as the certificate doesn't match the site, so the browser rejects it, but as far as I can see and tell, there is no "blanket IP blocks", more like "DNS and IP interception".The difference doesn't really matter in practice, sucks regardless, but I thought I'd clarify for the ones who are not experiencing these blocks themselves at least.

reply

tom1337
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

just wait until they block Azure as well so the official La Liga site also stops working

reply

jacquesm
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Hmmm. Don't they have a reporting form or something like that? Down with those filthy Azure pirates on IP 52.166.113.188.

reply

hunterpayne
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Starting a new business I see...this actually seems like the best form of protest here so good luck to you.

reply

mcintyre1994
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Dumb question but why don’t the pirate sites all host on Azure if Cloudflare is blocked and Azure isn’t?

reply

fireant
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Besides the reasons already listed, Cloudflare is free, Azure is not. As a pirate site owner I imagine you don't want you payment information with your name associated with your pirate site. You can pay for hosting and dns with crypto.

reply

tom1337
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

i have no data to back this up but in the past cloudflare was much more lax with piracy sites and I can imagine that Azure is stricter with blocking them

reply

kjs3
 
15 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I would imagine they do. The people running the pirate sites know what they are doing. Noone who really wants to stream pirated games is stopped. Blocking CF is performative, not effective.

reply

littlecranky67
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I wondered how they actually managed to have their own business to be unencumbered by that. At a certain corporate level, you have to have some piece of tech in your portfolio that relies on cloudflare. I hope one day there companion or "2nd screen" apps stops working during a game, because using cloudflare.

reply

joquarky
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Sounds like the answer here is to host alt streams on Azure.

reply

jjcm
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Barring an Internet giant suing them in court, it really feels like this is unlikely to change as most just don’t understand the why or the effect.

Someone needs to write a heist movie set in Spain where a key part of the plan is they steal something while La Liga is blocking some key security route.

reply

evilmonkey19
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Last weekend happened as well :/

https://news.ycombinator.com/item?id=47480926The situation every weekend is getting worse and worse. Honestly, I cannot understand how any goverment who wants freedom for its citizens can allow to block internet access to a whole country only because a private football company asks for it. I guess LaLiga is the 4th statement in Spain...A probably will get even worse the situation with Fastly entering the equation:https://www.fastly.com/press/press-releases/fastly-and-lalig...

reply

jcalvinowens
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

This is the moral equivalent of shutting the water off for a whole city because one dude's house has a leak. The harms to society clearly and obviously outweigh any possible benefits to society. But if that one dude has the power to shut it all off, and doesn't care...

reply

spwa4
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

If you think that's even remotely close to the worst the Spanish government has done, don't look up "Catalunya".

https://int.assemblea.cat/civil-and-human-rights-abuses/tool...

reply

Ikatza
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Just so everyone here has the full picture: the source linked — Assemblea Nacional Catalana — is not a human rights watchdog, an international observer, or a journalistic outlet. It is the main pro-independence criminal activist organization in Catalonia. Citing them as evidence of Spanish human rights abuses is a bit like citing the murderer's wife as an impartial witness.

For context, Spain is a full constitutional democracy, subject to the jurisdiction of the European Court of Human Rights, with a free(ish) press, independent judiciary, and regular elections — none of which Assemblea itself disputes, because it participates in all of them. The events OP is referencing (the 2017 independence referendum aftermath) were reviewed by European courts, and the outcomes were, shall we say, not quite the narrative Assemblea sells on its website.If there are genuine, documented human rights concerns, I'd welcome impartial sources from the Supreme Court or the ECHR.What I'd push back on is treating a political lobby's own press releases as neutral reporting. You should do better than that here, OP.

reply

hggh
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Such democracy, so constitutional

https://www.ohchr.org/en/press-releases/2022/08/spain-violat...

reply

spwa4
 
5 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Or to put it another way: Catalunya (Barcelona and surroundings) is one of 3 Spanish regions that want to break away from Spain, not counting overseas territories. And yes, the population really wants this: there was a referendum and the outcome was: 92% want out of Spain. 
https://en.wikipedia.org/wiki/2017_Catalan_independence_refe...

(why? Let's be honest: Catalunya would benefit enormously from independence, but when the economy goes well, as it did from 2001-2007, they're fine. After that the situation worsened again. The situation is simple: Catalunya has a much better economy than Spain and could maintain government spending, whereas being part of Spain, they need to cut social spending)The Spanish government has violently repressed this, attacked the people, arrested politicians, tried to threaten other EU nations with invasion (yes, seriously, the current government has a few "rough edges", even if I would agree if someone said that any other party would be worse) unless they arrest Catalunya politicians (then did nothing when they told them to go f themselves), and this mostly with the agreement of regular Spaniards.Given what is happening in the EU (10+ years of slowly but unrelentingly worsening economy) the situation is slowly worsening again.

reply

buildfocus
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That referendum result is quite debatable, since the legal situation meant most people against it simply didn't vote. While in the past it was close, nowadays polls strongly suggest a comfortable majority against independence: 
https://www.democrata.es/politica/39-catalanes-apoya-indepen...

I agree the Rajoy government's handling of this was very problematic, but the rest of this isn't really accurate. And the morals of the economy argument is terrible - the rest of the country needs us, so we should cut them off? The same argument would apply for Barcelona cutting off the rest of Catalunya. It's not a good direction.

reply

ErneX
 
53 minutes ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You forgot to mention that some of the people behind the catalonian independence movement met with Russians who even offered military support if they went ahead with a proclamation of independency. I think we should all move on from that bizarre situation.

reply

egeres
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

I wasn't able to pull some images and I lost 1h trying to diagnose network problems in my setup, but it didn't occur to me that "la liga" was the root cause . My workaround was to add "registry-mirrors": ["
https://mirror.gcr.io
"] in my /etc/docker/daemon.json

reply

chaz6
 
30 minutes ago
 
 | 
parent
 | 
next
 
[–]

This is the correct answer.

Something that confused me for a while was the path "docker.io" used for pulling containers. There is not actually a container registry at "docker.io" - rather docker and podman are hard coded to convert it to either "registry-1.docker.io" or "index.docker.io".

reply

Self-Perfection
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

This is far from the first time that I see on HN indignation on LaLiga blockings. Sadly all this rage does not seem to lead to any change.

I'd like to suggest some steps that might/should be followed, which I will not pursue personally but in my defense - I do not live in Spain and not affected.1) (first! low-effort) Somebody should create any space on the internet, where such anecdotes might shared and probably people with common goals of fixing internet access in Spain will meet. E.g. telegram group, discord channel, subreddit...2) probably create wiki with related research: legal framework and possible actions etc3) Raise public awareness. Create a resource/website with schedule of past and future "semi-blackouts", simple explanation of possible effects a layman may notice etc4) Explore legal actions that might be taken. How this issue might be forced to be discussed by politicians? For instance I know that Portugal has official mechanism to put forward petitions, that will be discussed in parliament if get enough votes [1]Space of possible demands in such petitions is vast. For instance:- Make LaLiga compensate partly price of internet access- Force LaLiga to include education notice in the beginning and the of translation with title like "Start of reduced internet connectivity" / "End of reduced internet connectivity"[1]https://participacao.parlamento.pt/initiatives/

reply

redbell
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

This behavior of blocking some domains and IP ranges during LaLiga games has become a routine by now. You might also want to check these similar submissions:

My game's server is blocked in Spain whenever there's a football match on:https://news.ycombinator.com/item?id=45358433Spain’s LaLiga has blocked access to freedom.gov:https://news.ycombinator.com/item?id=47114235

reply

flobosg
 
1 hour ago
 
 | 
parent
 | 
next
 
[–]

See 
https://hn.algolia.com/?dateRange=all&page=0&prefix=false&qu...
 as well.

reply

panstromek
 
5 hours ago
 
 | 
prev
 | 
next
 
[–]

Yea, when there's a match, our app stops playing videos in Spain and we get some bad reviews. It's pretty annoying.

reply

jeroenhd
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

At some point apps should just start pointing the finger at the cause of these problems. Linking users with Spanish IPs to a page explaining soccer internet censorship won't stop the bad reviews entirely but at least it'll be more useful than doing nothing.

reply

torben-friis
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

As a Spaniard, I would be very happy it cloudflare stops serving Spain. The situation is beyond stupid and I know without international pressure and shaming we're not getting rid of this abuse.

reply

littlecranky67
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

They should at least do a single "awareness day" during which they block the same IPs and sites they are ordered by court, as if there was a football match on. Ideally with a 7 days public notice announcement. Probably won't happen though, as their contractual obligation won't allow for voluntary suspension of services.

reply

pier25
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

As a Spaniard I couldn't agree more. This situation is just absolutely ridiculous.

reply

rmonvfer
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

As a Spaniard, this also happens to me. You can either use a VPN or just switch DNS servers to one that doesn’t have anycast nodes in Spain.

Cloudflare’s authoritative DNS uses EDNS Client Subnet (ECS) to return different IP pools based on where the query originates. Spanish resolvers get IPs from a range that La Liga blocks. If your recursive resolver is physically outside Spain (or you use DoH/DoT to tunnel to one), Cloudflare returns a different, unblocked pool.AdGuard DNS works well for this.

reply

samgranieri
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

This is inexcusable. Just because sports right holders are worried about piracy doesn’t give them license to break normal internet operations. Spain, get your act together and put your equivalent of the content cartel in the penalty box.

reply

pjc50
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

This is why technology businesses and professionals need to take a little bit of an active role in local politics. Otherwise you get nonsense.

reply

dabinat
 
11 hours ago
 
 | 
parent
 | 
next
 
[–]

We also need more tech-savvy politicians in office. There are a lot of politicians who are expected to legislate on important technology issues that barely know how to use a cellphone.

reply

otabdeveloper4
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Probably not, the tech-savvy politicians know about things like "DPI" and "traffic signatures".

reply

DocTomoe
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

That's an interesting euphenism for 'spend a massive amount of money on ~~corruption~~ lobbying',

reply

lentil_soup
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

not necesarilly, any government will make decisions, if there's no one to speak up and inform them why the decision is stupid, like the one from LaLiga, then we end up in this situation

reply

afh1
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

This is incredibly naive.

reply

lentil_soup
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

ok, then what do you suggest? we don't get involved and decisions at the government level are made for us? I might be naive, but let's not be restrained by the cynicism of any involment in politics and governance is corruption

reply

embedding-shape
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What? This is how governance and public opinion happen, at least in Spain. Government does something bad? Everyone out on the streets to complain, and calling politicians to change their mind.

Sometimes it works, sometimes it does not, but doing nothing is never an option if you disagree with what they're doing. To think that doing nothing is better than something, that's incredibly naive.

reply

ryandrake
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Doing nothing can't be better, but it's entirely possible that doing nothing has exactly the equal effect as doing something.

reply

embedding-shape
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> but it's entirely possible

You're right, it possibly has the same effect. How could we figure out what's the actual answer in practice?

reply

swiftcoder
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Hah. I have had to use a US-based VPN to access GitHub pretty much every weekend lately. La Liga's efforts to curb pirate TV streams are basically undermining the internet itself at this point.

This is also not new behaviour - Theo posted a YouTube about it nearly a year ago[1].[1]:https://www.youtube.com/watch?v=1-geGEYEw7g

reply

schnitzelstoat
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

The government really needs to step in, it's surprising that the PSOE and Sumar have allowed private companies to block so much of the internet.

reply

Self-Perfection
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

[Meta comment]

Humankind is not doing well with implementing new policies. We should really strive for each new policy (like in this case - blocking access to some parts of internet during soccer games):- Consider running policy in small scale scenario (e.g. testing blocking in small parts of Spain before whole country rollout)- Implement channels to gather info from those who are faced with results of policy implementation (in this case: the op got webpage with description why the page is blocked - a bit of sanity! It would be better if it was served with HTTP code 451)- Policy instructions- When deciding on policy put a date at which policy should be reconsidered and revised using data collected during the time when it was in effect- ... and some more I have not thought about.Let's strive to cultivate this principles in all life areas where we can affect how new policies are implemented.(edit: linebreaks)

reply

yangm97
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Maybe it’s time to reflect upon the reliance on centralized services?
Not long ago docker hub started rate limiting access and we all turned to blanket solutions like the GitLab registry cache.
I wonder if the IPFS distributed docker registry thing still exists/works.

reply

tabwidth
 
13 hours ago
 
 | 
parent
 | 
next
 
[–]

This isn't really about centralization. ISPs are blocking at the IP level, not Docker Hub specifically. You could self-host a registry behind Cloudflare and still run into the same thing.

reply

yangm97
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Self-hosting a registry is objectively “less bad” than relying entirely on docker hub but, unless all your Dockerfiles start with `FROM scratch` you’ll still need access to Docker Hub to pull the base images and their updates, and that’s true regardless of how many people are running their own registries.
If instead of relying on a centralized registry, which just so happens to also depend on a centralized CDN, you could instead pull images using something like IPFS or even torrent, not only ISP IP banlists wouldn’t be an issue but you would also eliminate a whole bunch of failure modes from the system.

reply

rrr_oh_man
 
8 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

"Behind Cloudflare" is the centralisation part

reply

pfortuny
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

> instado por la Liga Nacional de Fútbol Profesional y por Telefónica Audiovisual Digital,

(The trial was initiated by LaLiga and Telefonica...)."Telefonica" is the (exclusive) distributor for the rights of streaming the matches, and is only (of course?) the main consumer (and business) Telco in Spain: they are in a game they cannot lose. This is such an abuse and no government (this, past, whichever) has done anything about it.

reply

swiftcoder
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

It is also educational to look up the overlap between Telefonica directors, LaLiga directors, and the government officials who granted the defacto monopoly

reply

ordersofmag
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Interesting alternative. Cloudflare (market cap $58B) buys La liga (market value $5 billion), drops suit.

reply

manquer
 
12 hours ago
 
 | 
parent
 | 
next
 
[–]

Real Madrid alone is more than $5B ? Maybe you mean to say league association is worth 5B ? That seems too high the association does not have lot of margins they pass through most of their revenue to the clubs .

The last domestic TV deal they signed recently was worth $6B for 5 seasons or so, which is what you are proposing they buy.In enterprise value terms that $1B/year growing 6 %YoY is worth a lot more than $5B.In contrast Cloudflare has a $2.5B revenue albeit growing much faster but also has much smaller earnings or free cash flow, I.e. money they are not spending to make their current revenue.

reply

hunterpayne
 
11 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Here are RMs financials...
https://www.realmadrid.com/en-US/news/club/latest-news/notic...

They make about $25m a year in profit. Cloudflair actually looses a small amount of money on 2.5x the revenue. However, Cloudflairs market cap is about 100x that of RM's and that's because they have a growing business, in a growing industry and can easily become profitable when needed. That's probably not possible for RM and their very pricey lineup of players.

reply

manquer
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It is not the comparison to make, which is why I focused on the league’s tv revenue which is what is relevant , i only bought up Madrid’s valuation to ask where is Laliga ‘s $5B coming from.

Real Madrid owns the Bernabeu a valuable piece of real estate in the heart of Madrid and many other assets the Real Madrid brand is very monetizable .Sports team have been consistently growing businesses in every major sport in both Europe and US. Comparing a sports team and SaaS company is hardly going to be apples to apples with different asset , revenue, brand and monopoly and strategic profiles.——The risk to the league due to piracy is the value of the television deal. The buyer paying $1B/yr (DAZN) is the reason for this enforcement.If Cloudflare wants to buy this problem away that is what they need — The $1B deal growing 5-6% YoY and get into the streaming business .Prime alone is expected to spend $4B on live sports rights this year. It is very expensive space with everyone from Apple to Google and Netflix to sovereign funds going deeper every year .The streaming revenues otherwise aren’t expected to be massively grow so this is the content play that is least risk - compared to investing in say 4-5 blockbuster movies or tv series this is far more predictable and consistent revenue stream.

reply

msully4321
 
14 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I'm not sure where that number comes from but I don't think it's right, and I don't think that's how La Liga is structured anyway. It's governed by an association of all of the teams in the top two flights of spanish football.

reply

ordersofmag
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Right. The number is the result of Claude adding up the public information about the aggregate value of all those clubs plus the association. So it would mean buying all the clubs; or at least enough to have a controlling interest in the association. Clearly there are big challenges to that (e.g. clubs not being for sale for one). But I thought it was an interesting thought experiment. Of course if you're just trying to play the money = power card then it'd probably be cheaper to purchase the influence of some government officials.

reply

duckmysick
 
4 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Did Claude point out that under this proposal the Spanish clubs would be bared from entering European competitions? Since the clubs under the same ownership (more than 30%) can't enter the same UEFA club competitions.

reply

lokar
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Set an example. Buy them, fire everyone, shut it down and liquidate the property.

reply

outside2344
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Less headaches, free futbol matches!

reply

gchamonlive
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Here in Brazil sometimes my ISP goes into a weird state where I can't SSH into a remote machune. Got two ISP links here and still sometimes I need to resort to Mullvad to get stable internet

reply

Chrisszz
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

LOL this is so hilarious, blocking a portion of a web infra for a football match

reply

sva_
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

It is somewhat funny until you realize the amount of power some copyright mafia knuckleheads have over the (local) internet.

It isn't even an authoritative regime censoring something, but much more silly.

reply

amarant
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

I had to Google why this happens, blocking cloudflare during football games seems.. Arbitrary, to say the least. Maybe something to do with hooligans trashing entire cities when their team loses? I could almost get behind that, if I thought it would work..

But no, it's apparently to stop piracy!? Turning off half the internet, and mostly the legitimate parts at that (since when do pirates use cloudflare?) seems like probably the worst method to go about it.Someone ought to start streaming those games illegally without using cloudflare just to demonstrate how stupid this policy is

reply

swiftcoder
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

> Someone ought to start streaming those games illegally without using cloudflare just to demonstrate how stupid this policy is

Oh, the icing on the cake is that they already do. While my whole dev stack gets shut off every weekend, my neighbour watches pirate futbol streams just fine - not only is it a stupid policy, it's an ineffective one, and the pirates bypassed the bans ages ago

reply

amarant
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Makes you wonder why they keep the ban up? Are more people watching more football now that everything else stops working during matches?

Talk about unfair business practices!

reply

HDThoreaun
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Pirates use cloudflare because it solves their biggest problem, DOS attacks. Rights owners figured out that they can shut down these sites by DDOSing them which bypasses the courts and can be done instantly, so the pirates put their sites behind cloudflare ddos protection.

reply

Parodper
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

According to the court, the real reason is because ECH would make it impossible to block through DPI.

reply

Kamshak
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

I'm in Spain as well and it sucks a lot. What I do now is I go thorough Cloudflare 1.1.1.1 VPN (set up on my router). Fixes the issue and there is practically no latency or bandwidth impact.

reply

baobabKoodaa
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

You mean 1.1.1.1. DNS? Or do they also serve a VPN through that IP?

reply

Kamshak
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They also have a wireguard VPN service called 1.1.1.1 (with WARP). My understanding is you basically VPN into a cloudflare datacenter so you don't have issues with cloudflare IPs being blocked

reply

drnick1
 
10 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's probably just DNS (port 53). It's the way Europeans tend to implement their censorship, with the ISPs as executors. It's trivial to bypass, but most non-technical users don't know how, so it's good enough to comply.

reply

christkv
 
1 hour ago
 
 | 
prev
 | 
next
 
[–]

Companies should start suing La Liga for danaged please

reply

vaylian
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

This is a know issue and it is completely fucked up:

https://www.techradar.com/vpn/vpn-privacy-security/cloudflar...

What Spain does is basically censorship and it's very poorly executed. The docker image registry is only one out of the many collateral victims of this stupid law.

reply

embedding-shape
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

> What Spain does is basically censorship and it's very poorly executed

Basically? It is censorship, with huge collateral damage and regardless of how much we complain or share evidence that the blocks are actually financially harming us, no one seems to care as long as La Liga gets to freely block whatever hoster of websites as they wish.

reply

ryandrake
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

It's just like the Great Firewall of China, except in service of 
football profits
 instead of political ideology. I don't know which one is dumber and more disgraceful.

reply

embedding-shape
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wouldn't say "instead of", just "also", these "football blocks" are not the first cases of censorship of the internet in Spain.

womenonweb.org for example was inaccessible for years, just unblocked some years ago. During the latest Catalan independence referendum, the Spanish government blocked a bunch of websites, not the very least the official website of the referendum itself.This is just one of the most recent cases, and so far the one with widest regular impact.

reply

Jare
 
20 hours ago
 
 | 
prev
 | 
next
 
[–]

It's a disgrace, but apparently all relevant forces still consider soccer the most important thing in the country.

reply

znnajdla
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

How timely. I was just moving off Github to self-hosted docker registries.

reply

TiredOfLife
 
3 hours ago
 
 | 
parent
 | 
next
 
[–]

Bad bot.

reply

dlahoda
 
8 hours ago
 
 | 
prev
 | 
next
 
[–]

Just use Nix.

1. If nix fails to pull anything, it builds (up to and including Linux kernel and compiler).2. Nix has several ways to build OCI images, some even faster to assemble and slimmer output of official Docker tooling.3. It is allowed several providers for same artefact to resolve pull.

reply

TheDong
 
8 hours ago
 
 | 
parent
 | 
next
 
[–]

> 1. If nix fails to pull anything, it builds (up to and including Linux kernel and compiler).

If nix fails to pull things from its binary cache, it will download the "sources" of the derivations, which are hosted in various places and so it's even more likely an overly broad block impacts one of them.This football block very well could also cover GitHub, cdn.kernel.org, and so on, so nix building things could fail just as easily.The solution isn't to use something else which can download source code from 100s of sites across the internet to compile as a fallback, it's to not use internet which sporadically blocks sites hosting developer assets.The solution is not technical, it's political.

reply

dlahoda
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

1. We are more on OCI images? Assuming source available, run nix build and docker load of result.

2. Even if kernel.org or GitHub.com will be blocked, it likely than not it already was cached by nixos org cache or community cache or cachix or by your CI or by you workstation.

reply

postepowanieadm
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Why are you working instead of watching the match?

reply

userbinator
 
14 hours ago
 
 | 
parent
 | 
next
 
[–]

That's what crossed my mind too: It's like a nationally-mandated break to watch football.

reply

aftbit
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

What's the current state of the art for VPN'ing through deep packet inspection firewalls? I have imagined building something around TLS and Websockets that connects to a popular cloud provider which is "too big to block". Of course, if they'll block Cloudflare, or all connections outside of the country, maybe _nothing_ is too big to block. I remember some solutions to this in the 2010s, like obfsproxy and shadowsocks, but are there any newer or better options?

reply

krick
 
7 hours ago
 
 | 
prev
 | 
next
 
[–]

Is it exclusively football or do they try to fight piracy this way for some other major streaming events? I am just curious, because it's just comical to go this far over some dumb ball-game.

reply

sammy2255
 
5 hours ago
 
 | 
parent
 | 
next
 
[–]

It's just football. Once the game is over they revert the block

reply

snickerer
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

The Internet was originally designed to survive a nuclear war. Now we downgraded it deliberately to not survive a football game.

Decentralised infrastructure: goodCentralised infrastructure: badGood and bad for you, of course. For the big companies selling and controlling this stuff, it's vice versa.Just stay alert and don't chain yourself with big tech dependencies. The reason Git is great is its decentralised nature. If you got so far, why cripple yourself by running your traffic through a single American company like Cloudflare?

reply

giorgioz
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

POSSIBLE FIX:

I think changing your default DNS servers to Google 8.8.8.8 or Cloudflare 1.1.1.1
might bypass the spanish sunday ban on Cloudlflare.macOS + Cloudlfare 1.1.1.1https://developers.cloudflare.com/1.1.1.1/setup/macos/Google 8.8.8.8https://developers.google.com/speed/public-dns/docs/using

reply

echoangle
 
18 hours ago
 
 | 
parent
 | 
next
 
[–]

I don’t think it’s a DNS ban, it looks like they actually ban connections to the IP range.

But you can just use a VPN.

reply

LtdJorge
 
18 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Nope, it’s IP ban. At least for Vodafone and Telefónica.

reply

jesuslop
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Just to confirm it is true. This is LaLiga bringing down essential country-wide infrastructure on soccer hours if your internet access is through main ISPs.

reply

zeafoamrun
 
13 hours ago
 
 | 
prev
 | 
next
 
[–]

I don't even like televised sport but this makes me want to figure out how to pirate it at scale

reply

rcarmo
 
15 hours ago
 
 | 
prev
 | 
next
 
[–]

Ah, so that's why my site is "down" there:

https://hayahora.futbol/#sobre-los-bloqueos&domain=taoofmac....They're blocking the CDN too, not just R2.

reply

Robdel12
 
10 hours ago
 
 | 
prev
 | 
next
 
[–]

How is this cloudflares problem? This is on LaLiga.

reply

danpalmer
 
10 hours ago
 
 | 
parent
 | 
next
 
[–]

It might not be Cloudflare's fault, but it is their problem. If their customers can't use their products sporadically, it doesn't really matter why. Cloudflare taking a principled approach hurts their users in the short term, so they have to make a business trade-off between pragmatism and principle. Currently they're choosing principle, so it's reasonable to be angry at them for the short term issues that causes.

reply

sigio
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Time to use a VPN in your docker pipelines ;) Or run your systems outside of Spain.

Or can this be avoided by using an alternate DNS?

reply

darkwater
 
22 hours ago
 
 | 
parent
 | 
next
 
[–]

They are planning to also block VPN providers during football matches, see 
https://www.techradar.com/vpn/vpn-privacy-security/la-liga-w...

reply

Mordisquitos
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They are not "planning" to block VPNs. A technologically illiterate judge has ordered it, but there are no plans nor mechanisms to enforce it.

reply

darkwater
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The exact same stupid mechanism they are already using. Forcing ISPs to blackhole whole subnets if they belong to the VPN provider ASN(s).

reply

chrismustcode
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

If they can block IPs of cloudflare what extra mechanisms would be needed to block VPN IPs?

reply

chmod775
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The only viable way to even get most of them is to shut down internet access entirely. It's not a realistic solution, unlike blocking a few well known IP ranges belonging to a large corp like Cloudflare.

And even if you managed to get them all beforehand, some VPN providers will adapt and keep some servers in reserve, putting them online just as you managed to block the previous ones. Getting around internet censorship is a large chunk of their business, and some arereallygood at it.

reply

echoangle
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You don’t really need to block all, you just need to annoy the users enough that paying is easier. And I think there are enough games to use up the IP reserve pretty quickly and getting new ones every time is pretty annoying.

reply

chmod775
 
15 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I can provision a new VPS in about 5s of active work. I'd probably fully automate spinning up new servers and failing over because automatically detecting which got blocked is trivial. Bonus points if you use providers that let you attach multiple IPs to each VPS for cheap. Use some censorship resistant decentralized protocols to provide the next couple IPs to your client software and you're good.

And then they still need to monitor hundreds of VPN providers for whether they have new IPs, which is not neccssarily as easy as just grabbing a list of them. Once they have some, they then need to forward them to the ISPs and ask for them to be blocked. Their process is significantly less friendly to automation.No country ever won this fight short of total shutdown/disconnects.

reply

pxc
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> No country ever won this fight short of total shutdown/disconnects.

Some countries also throttle pretty effectively. So you can connect but if you're trying to do more than read Hacker News it's not very usable.

reply

mr-wendel
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It's a game. The VPN marketplace is huge so it's wack-a-mole.

Big companies don't hide their VPN ASNs. Obscure, for sure, but getting a good list isn't hard. Usually they get blocked.Smaller companies may pass under the radar, and have higher tolerance for risky strategies.The fringe providers are the problem. They aggressively change IP ranges, front-vs-obscure ownership, and play dirty. Shady folks will resell residential ranges. End-users often get tainted goods.... and you still have the collateral damage game when VPNs host infra with big cloud providers vs colofarms vs self-host, etc.

reply

prmoustache
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

When talking about VPNs, it doesn't have to mean "third party VPN". You can host your own on any VPN service outside of Spain.

reply

darkwater
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, but that's not something many can do easily. Also already having to use a VPN is not the "right" solution. The right so solution is to beat some sense inside some politician's head, and force them to write and approve laws that don't let stupid (or conniving) judges pass orders like this one we are talking about.

reply

prmoustache
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I agree it is not the right solution.

But anyone who is pulling docker images in a sunday afternoon while the rest of the country is glued to their screen to watch a football game or enjoying a sunny sunday outside having beers and tapas and what not should be capable of setting up wireguard.

reply

marginalia_nu
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Given the context of the HN audience, it's probably something you can do.

reply

darkwater
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wasn't strictly speaking about HNers. Using NordVPN and the likes is already done by slightly savvier users. Just look at where those products are advertised.

Spinning up and provision a VPS to act as a VPN exit node in some other country raises the bar 10x or more.

reply

msh
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It takes very light technical skills to deploy algo

reply

ufocia
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

"A _Sanish_ Court has ordered NordVPN and Proton VPN to block IPs transmitting illegal football streams" [emphasis added], that is inspain.

reply

skgsergio
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Alternate DNS doesn't help, they block at IP level.

Yes, they block IPs belonging to CDNs (CF including R2, BunnyCDN, CDN77, Fastly, Alibaba, Akamai even)...

reply

gred
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

> run your systems outside of Spain

So much for digital sovereignty :-)

reply

littlecranky67
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

It is not a DNS based block, but on the IP level. Once I knew what caused the issue, I figured I use one of my Hetzner vServers as an exit node in tailscale.

But come on, this can't be true. I wonder how many other people in IT wasted hours on issues and tickets to find out it is due to a football match taking place. Admittedly, chances are low, as football matches are usually outside of office hours.

reply

ethin
 
9 hours ago
 
 | 
prev
 | 
next
 
[–]

This is exactly why random corporations need to be gone from government. Or copyright needs to be abolished, one of the two. No corporation (no matter how beloved) should ever have this kind of power. IMO the more powerful an organization becomes, the deeper the scrutiny should be.

reply

archon810
 
12 hours ago
 
 | 
prev
 | 
next
 
[–]

I found out about this a month ago when a confused Spanish user showed me all downloads on 
https://apkmirror.com
 (powered by Cloudflare R2) are blocked in Spain during LaLiga soccer matches 
https://x.com/i/status/2030361569691898237
. It was so idiotic, I couldn't believe it. Glad it's getting more attention now.

reply

Dibby053
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Going to play devil's advocate here but I suspect if Cloudflare had been more cooperative about taking down illegal content, LaLiga would not have resorted to blanket blocking individual IPs.

I would really like to understand more about the process that they should follow but didn't / followed but didn't satisfy them / doesn't exist, in order to remove infringing websites quickly from CloudFlare.

reply

integralid
 
15 hours ago
 
 | 
parent
 | 
next
 
[–]

I work with actually malicious content (things that make people lose their life savings) and Cloudflare abuse is relatively helpful (compared to most ISPs who just don't care).

They just refuse to take down random things that some media company representatives send their way, without a court order or any oversight. And this is a good thing.

reply

Dibby053
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Can you qualify "relatively helpful"? If you send them a ransomware site, a person looks at it, and still demand a court order... A company like them should know the scale at which these things are run, and that courts can't keep up with the speed.

>And this is a good thing.Disagree. Demanding a court order for every single clear-cut case of infringement reported by the rightful owner of ephemeral content that is a infringed upon hundreds of times every day, causing nearly a billion dollar of losses per year... This is what the ISPs were trying to do and LaLiga successfully sued them, creating the modern fast-lane that CloudFlare complains about. Furthermore, unlike CloudFlare, the ISPs were not even profiting from the illegal content! This is a huge difference in the Spanish legal system. This will not end up good for them or for the open Internet they claim to defend (presumably as an excuse for taking their cut from cybercrime.)

reply

JoshTriplett
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> for every single clear-cut case of infringement

Clear-cut by whose judgement? Surely not the plaintiff, who has demonstrated no care for collateral damage. Witness the many, many fraudulent DMCA takedowns that are regularly sent, for a demonstration of what happens when prospective plaintiffs are given a power of "guilty until proven innocent".> causing nearly a billion dollar of lossesI thought we were long past people believing the funny-money fake numbers claiming every download is a lost sale.

reply

JoshTriplett
 
16 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

LaLiga wanted the right to tell Cloudflare to block specific sites without going through a court.

Cloudflare, rightfully, said that was ridiculous and unreasonable.A Spanish court, wrongfully, decided to let LaLiga block all of Cloudflare.

reply

Dibby053
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I assume the problem is Cloudflare wants a court order that mentions the specific infringing domain name. The problem is: what's faster, spinning up a new frontend for a livestream or getting an order from a court?

Courts orders are, rightfully, slow. A court order is a serious thing and we shouldn't be wasting judges' time and resources to determine if hundreds of domains in CloudFlare, during every single match, are infringing on LaLiga. This is why the Spanish ISPs have a fast-lane with LaLiga to block infringing websites quickly. Why is it ridiculous and unreasonable? If LaLiga starts abusing this power to attack competitors or do anything malicious they will lose that power instantly.Fastly understood the problem and will start running detection software to ban infringing livestreams in real time.https://www.laliga.com/en-GB/news/fastly-and-laliga-team-up-...What's CF's solution?

reply

JoshTriplett
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> If LaLiga starts abusing this power to attack competitors or do anything malicious they will lose that power instantly.

Because everything demonstrated so far has suggested that LaLiga is reasonable and measured? Courts exist for many reasons, among them that we do not trust plaintiffs to always be right or reasonable.By way of demonstrating that such power is unacceptable, it sounds like LaLiga isalsotrying to get Spanish ISPs toblock all VPNs whenever a game is on.This is not an entity that can be trusted with power. This is an entity thatrightfullyshould take its whining to a court who can keep its abuses in check. (Unfortunately, the Spanish courtsalsodon't seem willing to keep its abuses in check, which brings us back to the collateral damage problem.)> Fastly understood the problemNo, Fastly accepted the blackmail that Cloudflare refused.

reply

Dibby053
 
7 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>By way of demonstrating that such power is unacceptable, it sounds like LaLiga is also trying to get Spanish ISPs to block all VPNs whenever a game is on.

What LaLiga did was get some VPN providers (NordVPN and ProtonVPN) to start blocking pirate streaming websites. They're not trying to block VPNs themselves unless there's other news I didn't find.

reply

JoshTriplett
 
6 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And, presumably, if they don't comply with that unreasonable order, they'll next try to get local ISPs to block the entire VPN provider, just as they did with Cloudflare. Repeat as long as there are usable VPN providers.

https://news.ycombinator.com/item?id=47739695It is not the job of an intermediary ISP or VPN to help construct a country-wide firewall. If a company wants to go after streaming sites, go take down the streaming site. If the streaming site is out of its jurisdiction, talk to the other jurisdiction. If the that jurisdiction does not care,give up and lose.

reply

lokar
 
17 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

They will take down anything you get a judge to agree with.

reply

lloydatkinson
 
3 hours ago
 
 | 
prev
 | 
next
 
[–]

Probably the only even slightly relevant thread I’ll ever find for this so here goes. There is a certain visitor in the “Madrid Autonomous Community” (whatever that is) which frequently requests just my homepage, no other page on my site, over and over again.

It comes in waves, and it’s not enough to affect anything, but it’s very weird because when I did some digging by looking at the ASN there was actually only one active IP address and if I browse to it I get someone’s Synology NAS login page.Why would someone setup their NAS to randomly keep pinging my homepage?

reply

blurb4969
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Welcome to the club, buddies! Here, in Russia, the government doesn't care about collateral damage at all when shutting down whole Internet in cities. They turn on white list mode, when only approved sites and IPs work. Businesses stop working and start losing money? They don't care. Important IT systems stop working? They don't care. People can't communicate with each other? Don't care.
And seems like it will happen everywhere else. Sad to see the whole world goes down apart.

reply

fc417fc802
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

I think perhaps there's a difference in expectations between wartime versus a country at peace going after pirates.

reply

blurb4969
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wanted to say that Internet freedom dismantlement is a global trend.

reply

fc417fc802
 
16 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Fair enough, I completely agree. However in the case of Russia specifically, I understand that at one point Ukrainian drones were making routine use of mobile internet within the county. Temporary internet whitelists seem like a reasonable alternative to complete blackouts in that scenario. There are plenty of historic examples of malware using just about any communication platform for the C&C transport.

reply

sschueller
 
2 hours ago
 
 | 
prev
 | 
next
 
[–]

Just wait until a bank moves their 2FA to CF...

Netblock do not work and will never work.

reply

jimaek
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Off topic but I wonder when Cloudflare is going to launch their own Docker registry as a product.

reply

ImJasonH
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

It's pretty easy to write your own. I made this one a while ago: 
https://github.com/chainguard-dev/crow-registry

reply

ai_slop_hater
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

https://github.com/cloudflare/serverless-registry

reply

jimaek
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I've seen it but it's buggy and lacking in features. Feels like an afterthought instead of a real product

reply

wqtz
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Well, Cloudflare does not launch anything. They acquire to build products. Look into all their recent product launches. They acquired a relatively small company and converted the founding team to a product team.

So, if you want them to build stuff, ask yourself, are there any "Docker Registry" startups out there. If jsdelivr/globalping is not keeping you busy enough... there is an idea

reply

a_t48
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Yes, actually, there are. I've built 
https://clipper.dev
. I'm somewhat focused on robotics/edge device use cases right now (handling large images in bandwidth constrained environments), but my storage costs are also 1/7th of DockerHub. It also enables device to device content sharing much easier than base Docker, will be much easier to do antivirus/vuln scans, some other side benefits.

If there's something you'd want out of a registry that you think the market would want, I'm all ears.

reply

jimaek
 
21 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Honestly I would build it if I knew how to properly market it to quickly get users.

Globalping and jsDelivr took years to gain a meaningful user base

reply

wqtz
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I do not think that is the issue. The recent acquisitions from all these big tech companies did not have any "meaningful" user base to begin with.

I think your name alone carries significant weight in the industry and you have built a very large community.If you even vibe code something with, you will get a stupid amount of money thrown at you and a contract that bounds your existing projects and the next 3-5 years to a particular company as project lead.Here is a list of acquisitions Cloudflare made recently:https://blog.cloudflare.com/tag/acquisitions/Most of these companies did not have a half dozen paying customer or even a fully fleshed-out product before they were acquired.

reply

jimaek
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

I wish I had as much faith in myself as you have in me :)

reply

a_t48
 
12 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

What would you build that would make it different/better than the existing registries out there?

reply

vaylian
 
22 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

What would the business case be?

reply

jimaek
 
22 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Capture developers and funnel them to the Workers platform

reply

maxlin
 
4 hours ago
 
 | 
prev
 | 
next
 
[–]

sportsball more importanter than your nerd stuff.

regards: spanish authorities (who are watching the sportsball and so are better spaniards than you!)

reply

Magnets
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

BT used to block the entire streamable.com site during football matches

reply

LtdJorge
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Thankfully, Adamo hasn’t implemented the blockade yet (if ever).

reply

thomasjudge
 
16 hours ago
 
 | 
prev
 | 
next
 
[–]

Could you bypass this with a VPN?

reply

tossandthrow
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

Yes, and all of Spain is learning how to use VPNs

reply

dmitrygr
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

The last sentence of this submission makes no sense. You are in Spain. Allegedly, the country has a representative government. That means that you should have a way to influence the government to fix this idiocy. If, in fact, you don’t, then it is not a representative government and …ahem… further steps may be warranted to remind the government whom they work for.

reply

ahachete
 
22 hours ago
 
 | 
prev
 | 
next
 
[–]

Yeah, I know. Welcome to the club :(

https://x.com/ahachete/status/2035783292549755228

reply

anthk
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

CF could just sue LaLiga and the judge as interrupting and intercepting telecomms it's a really serious crime in Spain. Call the AEPD too because of consumers' right against both ISP and LaLiga's snooping. Another huge fine.

This is not an issue under the civil code (civilian issues), but something to be dealt under penal (criminal) code.In Spanishhttps://www.fiscal.es/memorias/memoria2020/FISCALIA_SITE/rec...Oh, and BTW, LaLiga has just partnered with a CF rival.Now CF can just sue both like hell because of unfair competition:https://nitter.tiekoetter.com/xataka/status/2042658662850724...

reply

quadrifoliate
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

Looks like they already tried to appeal the block, and lost:

https://x.com/jaumepons/status/1904906677335245294

reply

buzer
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They could potentially file the suit against Spain in European Court of Human Rights if they have exhausted national remedies. ECtHR has previously ruled some blocks to be illegal, but generally in the context where country sought the ban. Of course in both cases Court is the one that actually orders the ban.

One relevant would be Yildirim v. Turkey where court ordered blocking access to all Google sites because there was one that where someone insulted the memory of Atatürk. This was due to request from Telecommunications Directorate. This then caused the appellant's website to get blocked as well.Another one would be Vladimir Kharitonov v. Russia.

reply

prmoustache
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I think they are doing it already.

reply

anthk
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Yea, La Liga it's crapping out as always.
Docker needs either some I2P gateway, or a Tor service.

reply

fc417fc802
 
16 hours ago
 
 | 
parent
 | 
next
 
[–]

The pirate streams need an I2P service that way LaLiga might give up.

reply

Myzel394
 
18 hours ago
 
 | 
prev
 | 
next
 
[–]

Just use a VPN

reply

genericacct
 
14 hours ago
 
 | 
prev
 | 
next
 
[–]

same thing happens in italy

reply

mschuster91
 
17 hours ago
 
 | 
prev
 | 
next
 
[–]

Cloudflare 
could
 resolve this without negatively impacting fundamental services... just place all newly registered sites (e.g. <30 days) on a dedicated block of IP addresses. That way, Spain's government-ordered censorship could be limited to (mostly) pirate sites. Or they could invest money in vetting customers properly.

But of course, Cloudflare rather prefers to hold their actual large customers (who don't have much of an alternative to CF) and everyday Spaniard users hostage.

reply

fc417fc802
 
17 hours ago
 
 | 
parent
 | 
next
 
[–]

What would prevent a pirate site operator from registering a domain a few months in advance and sitting on it in the meantime?

How do you propose customers ought to be vetted? Why should a host be expected to take on the duties of a hall monitor? Isn't that the judiciary's job?I think it is actually Spain using their residents as hostages in an attempt to extort Cloudflare and other large providers. The current situation is best described as blatantly corrupt regulatory capture.

reply

mschuster91
 
14 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> What would prevent a pirate site operator from registering a domain a few months in advance and sitting on it in the meantime?

It's driving up the cost and expenses. Operators of legitimate sites don't have to worry during that probation time about anything with the exception of customers in Spain during LL match hours.LL has ~10 matches / weekend (Fri/Sat/Sun/Mon), that means pirates have to have about 40 domains/CF integrations per month plus more in standby - and more, for longer probation periods.> How do you propose customers ought to be vetted?I dunno... stuff like basic KYC measures would be a good start. Copies of ID cards. Government business licenses. Private entities (credit bureaus). Even phone number verification is a serious hurdle for malicious actors, and it ties activities to real world identities that can be held accountable.Dangerous stuff (e.g. streaming) could only be made available upon a security deposit.> Why should a host be expected to take on the duties of a hall monitor? Isn't that the judiciary's job?No, and that we let ISPs get away with ignoring abuse@ emails is part of why the Internet is such a nasty place these days. You need a license to drive a car on public roads, you need an expensive license to fly a small plane, and you need a goddamn massively expensive license to fly a widebody aircraft. So why shouldn't you need to pass some set of verification before you get access to inarguably the Internet's most powerful data pipes?

reply

fc417fc802
 
12 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> It's driving up the cost and expenses.

That's an interesting point. Are their margins so slim that they can't afford less than ~$50 per domain? I'm not familiar with their revenue model.This is the sort of thing that could be done via the legislature if Spain were serious and playing by the rules. They could require ISPs to do DNS filtering based on domain age during matches. If they really wanted to do service level filtering they could require hosts such as CF to perform geoblocking in a similar manner during matches.> Dangerous stuff (e.g. streaming) could only be made available upon a security deposit.Let's set aside for a moment that I think this suggestion is completely absurd. Are these sites using some prepackaged streaming solution? Do you not realize that I can stream video from any machine using software I control? To an approximation the only thing required to scale streaming up to lots of customers is raw bandwidth. If you don't accommodate seeking you can potentially serve thousands of simultaneous streams with a single cheap VPS (in practice this won't work because a cheap VPS won't have a 100 Gbit pipe).> So why shouldn't you need to pass some set of verificationSince when have you needed a license or verification to publish? You're acting as though a global impressum requirement is the natural state of affairs. Your demand is an affront to free society.> we let ISPs get away with ignoring abuse@ emailsThat seems like an entirely separate matter, if it's even true at all.> NoAh yes, a rousing argument. Obviously you must be correct.You've failed to make a convincing case as to why deciding what is and isn't permissible isn't the job of the judiciary. If Spain wants to change that then they need to pass laws to that effect but in practice those won't have global reach. Thus they might (for example) engage in international lobbying efforts to incorporate a DMCA equivalent for illegal streaming into the global copyright regime.Failing the above it is Spain that is in the wrong here and I'm happy to see that CF isn't going along with their overbearing and entirely unreasonable nonsense.

reply

mschuster91
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> Are their margins so slim that they can't afford less than ~$50 per domain?

It's not (just) about driving up the financial cost, that works out decently to combat "normal" spam. The thing is, it drives up the organizational effort - you need to acquire and maintain a constant fresh stream of fake identities, payment credentials and the likes.> Let's set aside for a moment that I think this suggestion is completely absurd. Are these sites using some prepackaged streaming solution? Do you not realize that I can stream video from any machine using software I control?At the moment, the pirates are streaming through Cloudflare, which is why CF is being targeted with the mass bans in the first place.And yes, Cloudflare could go and say "we block everything looking like m3u8 HLS, DASH or other forms of video streaming for young accounts". Cloudflare has enough AI to dynamically detect and ban abusive clients - you can't seriously assume they could not detect someone running video streams on the server side.> Since when have you needed a license or verification to publish? You're acting as though a global impressum requirement is the natural state of affairs. Your demand is an affront to free society.One man's freedom ends where another man's freedom begins, society cannot survive without an "immune system" to ward off abuse, and Cloudflare are an accomplice to a whole lot of abusive behavior that is worthy to call out and confront.> That seems like an entirely separate matter, if it's even true at all.Have you ever heard about the term "bullet-proof hosting"?

reply

fc417fc802
 
18 minutes ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> you need to acquire and maintain a constant fresh stream of fake identities, payment credentials and the likes.

Domains aren't free to begin with so I'm not sure what your point is. You claimed a small hike would price them out so I asked about their revenue model.> And yes, Cloudflare could go and say "we block everything looking like m3u8 HLS, DASH or other forms of video streaming for young accounts".Yes, they could start doing DPI and arbitrarily censoring things similar to the Chinese. As I previously stated your position is an affront to free society. You ought to be ashamed to advocate such viewpoints.Also it would not go as smoothly as you seem to think. Without access to the plaintext stream they would be guessing using heuristics and there would be at least some false positives.> One man's freedom ends where another man's freedom beginsA vacuous rebuttal seeing as violating IP law doesn't infringe on anyone else's freedoms. By the same logic an impressum for printed works could be justified on the basis of people who publish "harmful" viewpoints such as those that might lead to social discord.

reply

breppp
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Vote early, vote often

reply

richwater
 
21 hours ago
 
 | 
prev
 | 
next
 
[–]

Spain is a failing country. Their economy is in shambles and the government has ceded internet control to a private corporation who runs football games.

reply

gruez
 
20 hours ago
 
 | 
parent
 | 
next
 
[–]

>Their economy is in shambles

But it's among the fastest growing in the EU? Granted, part of this is starting from a low base, but it's hardly "in shambles"https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG?locat...

reply

nslsm
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

They are doing this by artificially inflating the numbers, destroying the country forever: 
https://i.imgur.com/0MAeFaF.jpg

reply

gruez
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

>total population change in EU countries

The figures I cited are for GDP per capita, which accounts for population growth. Moreover immigration should have the opposite effect of depressing per-capita GDP, because immigrants typically take lower skilled jobs, dragging overall productivity down. So if anything, the figures are artificially depressed, not inflated.

reply

hunterpayne
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You should read down that table a bit. Sure the Spanish economy had higher growth rates the last couple of years. The way they managed to have a higher rate was to have the economy shrink by 8% in 2023. So according to my math, the estimated size of the Spanish economy in 2026 is about the same as the 2023 Spanish economy (within 1%). Hard to claim that as a win.

Technically you can say that they have been in a depression for the last 4 years and counting as their functional growth rate (accounting for inflation of the Euro) is negative over that period (down about 10% inflation adjusted).

reply

gruez
 
9 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> So according to my math, the estimated size of the Spanish economy in 2026 is about the same as the 2023 Spanish economy (within 1%). Hard to claim that as a win.

That conclusion does not seem to check out just by eyeballing the charts.https://data.worldbank.org/indicator/NY.GDP.PCAP.KD?location...It shows a divergence from the EU back in the 2010s, but afterwards is recovering at the same pace or even faster than the EU. Could be better, but not "in shambles" either.

reply

embedding-shape
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Spain isn't a perfect country, I don't think any is. But the economy isn't in shambles, only someone who doesn't know what they're talking about would say anything like that. It does suck that La Liga can wield so much power, agree, but this is not related to the economy at all...

reply

hunterpayne
 
10 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Sorry, but this isn't true. The Spanish economy shrank by 8% in 2023. So all those gains in the last couple of years are just catching up to 2023 and not actual growth. Add in inflation and the average Spaniard has lost 10% of their income over that period (2023-now). The median citizen losing 10% of their income in real economic terms does qualify for the vaunted "shambles" title.

reply

chrz
 
15 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Are you spanish and never went to another country? I only heard such things from never-stop complaining locals that never traveled anywhere. Yeah La Liga is a religion here, but Spain is one of the worlds top of life quality mate

reply

schnitzelstoat
 
2 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

The salaries and unemployment are pretty awful though. As are the working conditions in many jobs (jornada partida, paying less than legally required into social security etc.)

I think most people care more about these things than the GDP statistics tbh.

reply

fabianmg
 
1 hour ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

You most likely are arguing with a right winger from Spain. They compare the president with a dictator in their right wing media, and they basically talk about Spain like is Venezuela at every opportunity.

reply

estebank
 
20 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

To note that this isn't the executive or legislative but the judiciary doing the bidding.

reply

renewiltord
 
19 hours ago
 
 | 
prev
 | 
next
 
[7 more]

[flagged]
post-it
 
19 hours ago
 
 | 
parent
 | 
next
 
[–]

It's not just docker and tech. Plenty of people depend on tools that use Cloudflare.

reply

renewiltord
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

And when you are on your deathbed you will say “I wish I had spent more time on Cloudflare-based products”? I doubt it. No peer-reviewed research has shown people say that.

reply

embedding-shape
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Telling someone what to do is even more American, let people do whatever they want, at the times they want, as long as they don't hurt others, this is the Spanish way.

reply

renewiltord
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Touché. Or should I say “me has tocado señor”. Probably not but it would be funny.

reply

Synthetic7346
 
19 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

This comment has some "you should smile more" energy

reply

renewiltord
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Smile more. Touch grease. Roll coal.

reply

lofaszvanitt
 
19 hours ago
 
 | 
prev
 | 
next
 
[–]

Good. Cloudflare is the next evil entity on the internet.

reply

mathfailure
 
21 hours ago
 
 | 
prev
 
[–]

Cloudflare is cancer. And the tumor is now too big.

reply

Cpoll
 
21 hours ago
 
 | 
parent
 | 
next
 
[–]

You've got it backwards. Spain's ISPs are blocking Cloudflare and other CDNs because of LaLiga/football piracy. CloudFlare isn't doing anything here.

reply

sph
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You are correct, but Cloudflare is still a cancer on the Internet.

reply

petcat
 
21 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Rampant bot traffic and scrapers are the real cancer. Until that goes away everyone is going to need cloudflare or some other bot firewall service.

reply

adrian_b
 
20 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Perhaps that is true, but the Cloudflare anti-bot protection is too stupid and annoying.

They should have used a cookie or something else that does not require asking me every few minutes to prove once more that I am not a bot.There was a time when Cloudflare had become less intrusive, but for the last months it has begun again to intervene almost each time when opening some pages.There is no doubt that anti-bot protection can be implemented in a better way than Cloudflare does, but presumably the alternatives would consume more resources on their servers, so probably they choose whatever minimizes their costs, regardless if that ensures maximum discomfort for Internet users.

reply

post-it
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You're getting frequent verification requests because you're behaving like a bot. Are you modifying your user agent string or using a VPN?

reply

encom
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Who knows what upsets ClownFlare? I'm using Vivaldi on Linux on IPv6 in Denmark with every uBlock filter enabled and Cookie Auto-delete. That seems to confuse and anger CloudFlare and I get CAPTCHA tarpitted constantly.

reply

post-it
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> They should have used a cookie or something else that does not require asking me every few minutes to prove once more that I am not a bot.

> every uBlock filter enabled and Cookie Auto-deleteHmm

reply

bethekidyouwant
 
18 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

So you know why.

reply

encom
 
18 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

No, it could be any, or other, totally normal and reasonable factors. Or maybe I posted too much Cloudflare hate on HN and they singled me out.

They're in the walls!NO CARRIER
 +CREG: 0,0

reply

fc417fc802
 
16 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

Those are easy enough to dissuade with readily available PoW solutions. People use CF & co. out of convenience, the exact same reason that most websites load resources from 
at least
 half a dozen third parties instead of self hosting.

reply

Duwensatzaj
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

It won’t. Some people are perfectly happy to destroy and destroy as long as they get some small portion as profit for themselves.

reply

sph
 
19 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

That, ironically, includes Cloudflare. Without rampant bots making the internet worse for everybody, they wouldn't have as much work. And their portion of profit is anything but small.

reply

otterley
 
19 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

I know this is an unpopular opinion among freedom maximalists, but:

It’s precisely because CloudFlare isn’t responding like other CDNs to reasonable demands to cut off pirate origin sites that this mess exists. If they reacted quickly to remove configurations that are obviously facilitating copyright infringement, Spain wouldn’t resort to full scale ASN blocking.How do we know it’s CloudFlare? Because other CDNs like CloudFront, Akamai, Fastly, etc. respond to takedown demands and aren’t being blocked. (Those also cost money and require customer identification.)In an escalating war between the state and a corporation, the state will always prevail if they have the public’s backing. In Spain it’s clear that most people are happy to watch the match through legitimate channels even at the cost of blocking CloudFlare.

reply

FireBeyond
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

> It’s precisely because CloudFlare isn’t responding like other CDNs to reasonable demands to cut off pirate origin sites that this mess exists. If they reacted quickly to remove configurations that are obviously facilitating copyright infringement, Spain wouldn’t resort to full scale ASN blocking.

Apropos of anything else, CF is (reasonably) requiring a court order to remove offending material rather than just "well, company said so, so eh, just do as they say". La Liga complains that "oh, that's too slow for what we want" and just got a blanket ruling.I am not a fan of CF but your argument seems to be "CF should just roll over any time someone says "hey, delete this", because, obviously, everyoneknowsit's problematic, right? Right?".

reply

otterley
 
17 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

At least the DMCA in the U.S. has guardrails: not just anyone can send a takedown demand for everything. The requester has identify the works and declare under penalty of perjury that they are operating on the behalf of the owner. I imagine the equivalent EU law has similar requirements.

CloudFlare uses legal chicanery to try to subvert the DMCA by claiming that because they’re not the origin server, they’re not subject to takedown demands. So far no court has told them to knock it off. I expect that day will eventually come. Every lawsuit against them to date has ended in a settlement because CloudFlare would rather pay up than get an unfavorable ruling on the books.CloudFlare has consistently treated loss of DMCA safe harbor protection as a material business risk; it’s been cited in every SEC filing from the 2019 IPO S-1 through the FY2025 10-K.

reply

willdr
 
13 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Nobody cares about the DMCA guardrails and they are never meaningfully enforced. Case in point, Anthropic DMCAing thousands of repositories that simply mentioned the word "claude".

reply

FireBeyond
 
14 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

> At least the DMCA in the U.S. has guardrails: not just anyone can send a takedown demand for everything. The requester has identify the works and declare under penalty of perjury that they are operating on the behalf of the owner.

You'd think so, but no.DMCA came into effect 28 years ago. All those decades, all those billions of takedowns, and you don't even need the fingers of one hand to count those who've been hit with perjury for a false takedown request, because the number is ... zero.

reply

otterley
 
8 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

You might misunderstand what the law requires. The person making the complaint (demand) only has to declare under penalty of perjury 
that they represent the copyright holder
. It does not require them, under penalty of perjury, to be correct about the underlying facts.

See 17 U.S.C. 512(c)(3)(A):"(A) To be effective under this subsection, a notification of claimed infringement must be a written communication provided to the designated agent of a service provider that includes substantially the following: ..."(vi) A statement that the information in the notification is accurate, and under penalty of perjury,that the complaining party is authorized to act on behalf of the owner of an exclusive right that is allegedly infringed."In other words: someone issuing a notice of infringement relating to a Disney work must declare under penalty of perjury that they represent Disney. They don't have to declare under penalty of perjury that the work is in fact a Disney work, that the title is correct, that the use in question is not fair use, etc.This would explain why you're not seeing what you expect to see.

reply

jbxntuehineoh
 
20 hours ago
 
 | 
root
 | 
parent
 | 
prev
 | 
next
 
[–]

cf is failing to comply with Spanish law and as a result is being blocked in Spain

reply

skgsergio
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

I can agree on how much power on the global traffic they have, but this blocks affect many other CDNs like Fastly, Akamai, CDN77, BunnyCDN, Alibaba...

reply

petcat
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

Spain is mandating their ISPs block cloudflare to stop people from illegally streaming soccer games. Cloudflare isn't the one doing the blocking.

reply

imcritic
 
3 hours ago
 
 | 
root
 | 
parent
 | 
next
 
[–]

Isn't the ONLY one doing blocking.

I'm not from Spain and instead of Spanish ISP I get a block from CloudFlare.Now take a wild guess: which one is bigger - some Spanish ISP or CF?

reply

StrLght
 
21 hours ago
 
 | 
parent
 | 
prev
 | 
next
 
[–]

You made a few typos in "LaLiga"

reply

ufocia
 
21 hours ago
 
 | 
parent
 | 
prev
 
[–]

How so?

reply

Guidelines
 | 
FAQ
 | 
Lists
 | 
API
 | 
Security
 | 
Legal
 | 
Apply to YC
 | 
Contact

Search: