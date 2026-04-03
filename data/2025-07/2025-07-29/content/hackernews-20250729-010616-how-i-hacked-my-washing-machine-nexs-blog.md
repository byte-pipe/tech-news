---
title: How I hacked my washing machine - Nex's Blog
url: https://nexy.blog/2025/07/27/how-i-hacked-my-washing-machine/
site_name: hackernews
fetched_at: '2025-07-29T01:06:16.820377'
original_url: https://nexy.blog/2025/07/27/how-i-hacked-my-washing-machine/
author: JadedBlueEyes
date: '2025-07-29'
description: I ran out of characters for microblogging so this is where the big words go
---

# How I hacked my washing machine¶



If you've known me for some amount of time you knew this was something that was bound to happen eventually. Yesterday (and technically today), me and a friend went on an endeavor to hack our washing machine, partially for the fun of it, and partially because there's actually a practical use for it.





Don't take this article too seriously



A lot of the response I've seen to this post has been "this was unnecessarily complicated".



Since a lot of people don't seem to be reading the whole article, especially the last part, I just want to clarify:This was done for fun and as a challenge, the sheer absurdity of connecting our washing machine to our Discord to receive notifications when our cycles finish is what put this whole thing into motion.



While there is practical use, I know it's limited, and that this could be done simply by using a smart plug or even just overestimating the time it'll take to finish the cycle. But come on, if we did that, you wouldn't be reading this hilarious article where I later explain how we reverse engineered a washing machine and further plan to "hack" our other dumber appliances.



Plus, even if this was all pointless, at least I got to get some reverse engineering practice in a practical scenario :P




## Some background¶



For context, I recently moved into a new house for uni, with some friends. This house was pre-furnished, so it came with all the appliances we needed, including a washing machine and whatnot. And, in true typical renting fashion, the washing machine is some cheap "smart" model, that features a Wi-Fi connection, and a mobile app to control it. Now, half of this house is populated by cybersecurity students, so naturally we were scoffing at the idea of putting the washing machine on the network.



And then we did it.



Turns out, this washing machine has the capability to send notifications to the mobile app whenever a load finishes. There's also some other stuff too like "self clean" or whatever, but nothing functional (the app is some cheap crappy HTML job crammed into a WebView). This was kinda funny, however, having notifications for when your "three hour" (usually like 4-5 hours) load finishes is actually really useful, especially when you're like me and forgot to... buy clothes, so have to keep the same set of clothes clean constantly. However,only one person can be connected to the washing machine at a time, so if someone else wanted notifications, you'd have to disconnect the washing machine from your app, and then let them do the whole jig. Which involves reconnecting it to the Wi-Fi network, by the way.




 The front page of the washing machine app, after logging in. The app is called "
Hoover Wizard
".




 Notifications received for when a wash cycle finishes.



### The doorbell¶



Tangentally related, this house is an incredibly old victorian house, meaning the walls, floors, and doors are super thick. There's also only one person living on the ground floor near the door, so having someone knock on the door, or a doorbell that just rings near the door isn't helpful, since nobody will hear it. Luckily, however, this doorbell has a receiver that plugs in elsewhere, and the doorbell broadcasts a signal to it when pressed. This is a 433MHz doorbell, which is a common frequency for these types of devices.



In short, my friend bought a cheap receiver that listens for these signals, and then uses that signal to send a notification in our Discord server, so that we all know when someone rang the doorbell. In future, it'll also probably be used in conjunction with a security camera, so we can see who rang the doorbell. Pretty neat, right?




 The doorbell triggering a notification in our Discord server.



This does still, in addition, ring the actual doorbell receiver, so there's still an audible notification, but this is more of a backup.



It was after seeing the success of this project that we had the bright idea - what if we could do the same thing with the washing machine? So we started plotting...



## The plan¶



Going into this, I had some experience with reverse engineering and hacking apps on my phone. I had previously done a bit of work on reverse engineering the attendance app for my university, which was fun, but ultimately didn't go anywhere because it started being more effort than fun. However, this lead me to the initial idea - see what the washing machine app connects to, and work out the API from there. This would've been simple, just install some self-signed TLS certificate on my phone, and then use a tool liketcpdumpandmitmproxyto capture DNS requests and other traffic.



However, we realised that most of the work was doneby the washing machine itself. This gave me the bright idea to just capture the traffic from the washing machine itself, and then reverse engineer that. And so, I went and grabbed anOpenWRT-compatbile router I had laying around, flashed it, and set it up to listen on 2.4GHz (since that's all the washing machine worked with), and connect to WAN via 5GHz, with my laptop in the middle connected over Ethernet.



After setting up the router, I broadcast a temporary SSID, and paired the washing machine to it. Grabbed the IP address of the washing machine, and then started capturing traffic withtcpdump. Unfortunately, I don't have any of those captures anymore.



## Who is my washing machine talking to¶



After tracing the traffic for a short while, I noticed four things:


1. The washing machine REALLY liked talking to... itself? I don't think whoever engineered their networking stack knew what a loopback interface was, because it was sending a lot of traffic from itself to its own IP address. I didn't think this was relevant, so I ignored it.
2. It really liked sending traffic to255.255.255.255every second, for some reason. Again, ignored.
3. It occasionally contactedsimplyfimgmt.candy-hoover.com. This is a CNAME to some herokudns domain, which I thought was odd, but also couldn't pull anything interesting from it. I did, however, see&encrypted=1in the URL, which I thoughtwasinteresting, since this appliance was connecting to this server overHTTP, notHTTPS.
4. The washing machine wasdirectly connectingwith the mobile app, with the app sending HTTP requests to port 80.


Of all these four things, only the last one was particularly interesting, so I started looking into it. I assume the server contactingsimplyfimgmt.candy-hoover.comwas for notifications, but I couldn't get anything useful out of it. That's when my friend suggested that we just... poll the washing machine.



What an insane sentence, by the way. Poll the washing machine?



## Reverse engineering the washing machine's API¶



So, trying to intercept notifications from the washing machine was pretty much out of the question. at least without a lot more effort. So, I started looking into how the app behaves when opened, and when I try to interact with the washing machine, etc.



It looked like the app was only contacting two endpoints:


1. /http-read.json?encrypted=1
2. /http-write.json?encrypted=1


There were possibly more, but those were the ones that stuck out to me, and were also repeatedly contacted by the app.



http-write.jsonlooked like it was used to send commands to the washing machine, such as to start a self-clean, or whatever. This was thrown aside since we didn't want to talk to the washing machine, we wanted the washing machine to talk to us.



Moving on tohttp-read.json, this looked like it was used to read the state of the washing machine, however,it was encrypted!. Your eyes do not deceive you, that?encrypted=1query parameter was actually doing something!



In the most ugly manner possible, after loading up the endpoint in my browser, I was greeted to


HTTP/1.1 200 OK

Content-Type: text/html

45D3EBF9E63886CD240D412B44973ECBCD96ADFF263D56E293C48B9F0C884D00...



That's right, the washing machine was sending encrypted data... as hex... with a HTML content type. This was incredibly infuriating, because now I had to figure out how to decrypt this data.



### Breaking the encryption¶




Couldn't you just setencrypted=0?



I thought this too, however, settingencrypted=0returned the encrypted data still,orreturn a 400 Bad Request. No idea why, but also don't care.




In March, me and my friend had visited Lancaster University for the cybersecurity conference,Hackademia 2025. While I don't remember too much of that conference (although it wasamazing, if you get the chance to go to it, I highly recommend it), I do remember one of the workshops we attended being about hacking an IoT camera, run byInterrupt Labs. Now, I didn't do very well at this - it was far lower-level than I was used to working at, so a lot of the concepts were lost on me. However, I did learn some fundamental concepts that would prove to be useful later on, namely the fact that most of these devices are insecure, have firmware just publicly available, are terrible for re-using credentials, and are pretty often poorly secured in general. I also learned that these devices will often have some incredibly simple home-grown encryption by just XORing data.



This left me with two possible ideas to get the washing machine's XOR key - either pull the machine apart, read the firmware, and put it all back together (hard), or just try to brute-force the key (easy). I only had my laptop with me at this time, so brute-forcing a key with very little information on what we were looking for seemed suboptimal. But also, taking apart a whole ass washing machine just to read a short string seemed silly, so I got to work on brute-forcing the key withCyberChef.




 CyberChef churning away at an XOR brute-force on the washing machine's encrypted response.



Unfortunately, we were fighting an uphill battle with this one. We had no idea what a known string would be inside the decrypted data, and we had no idea how long the key was. As my laptop is some thin workbook, it has 8 cores (16 threads), so brute forcing a key of length 3 or more was taking FOREVER. It was during this time that my friend was researching if anyone else had managed to do this before, and sure enough,MelvinGr/CandySimplyFi-toolexisted. This is a simple C++ program thatalready knew some known strings, and was able to brute-force the key in a matter of seconds. I was able to compile this on my laptop, and run it, and sure enough, it was able to decrypt the data in a matter of seconds.



For now, I plugged this key into CyberChef, and was able to decrypt the data.




 CyberChef decrypting the washing machine's response with the key we found.



And, luckily, subsequent requests to the machine returned the same format, so guess what, we now also had a schema! I ended up re-using some of the components ofofalvai/home-assistant-candy, which meant I didn't need to spend too long figuring out what the data meant. Now, on to the fun bit.



### Prodding the machine¶



Now came the most fun part of all of this - poking the machine to see what changes.



We started by simply just turning the washing machine on, and noting down what changed. And then turning on a cycle, letting it run for a bit, pausing it mid way, restarting it, and then letting it finish.



After a while, we'd got a pretty good idea of everything that changed, however, during our testing, we noticed a huge issue - the Wi-Fi chip in the washing machinewent to sleepif it wasn't contactedevery 30 seconds. Unless the washing machine woke it up to send a ping to the remote server, it would just stop responding to rqeuests periodically, which was incredibly annoying. My workaround for this is to just request the endpoint every three seconds.



Anyway, we noticed the following things changed:


* Prchanged whenever the program selection knob was turned, or when the washing machine was turned on. Obviously, this relates to the program selected.
* PrPhchanged during the wash cycle, so it looked like it represented the current phase of the wash cycle.
* Tempchanged whenever the program changed or when the temperature was manually set.
* SpinSpchanged whenever the spin speed was changed.
* RemTimechanged frequently during the wash cycle, and represented the remaining time of the wash in minutes.


Interestingly,RemTimewas fairly accurate, however, sometimes it would just drop to10for seemingly no reason. I still don't know for sure why this happens, but I assume it's some default value that the washing machine uses when it doesn't know how long is left. In my notification script (later), I just opted to ignore the value10. My washing machine will never be able to finish a wash in 10 minutes, only ever 9 minutes or 11.



Additionally,SpinSpwas only ever whatever the program selected dictated - not the machine's actual current spin speed. This is annoying because I really want to know when my washer is spinning at 1495 RPM instead of 1500, but whatever I guess.



## Creating the notification script¶



So, by this point, I now have


* The washing machine's API schema
* The washing machine's encryption key
* The ability to poll the washing machine
* The ability to decrypt the washing machine's responses
* The ability to read the washing machine's state


Now, I just needed to write a script that would poll the washing machine, and then ping that over to a Discord webhook.



I'll save you the details of how it works, you can read the source code here:https://git.nexy7574.co.uk/nex/washing-machine-bot



In summary, the functionality loop is as follows:


1. Poll the washing machine
2. If the response hasn't changed, sleep 3 seconds and repeat.
3. If something has changed, attempt to edit the last webhook message
4. If the webhook message doesn't exist, create a new one
5. Wait 3 seconds and repeat


In future I plan to add a way to set up personalised pings and also claim a wash cycle and whatnot, plus some fun stats tracking or something like that, but for now it does what I need it to do.




 The washing machine bot in action, showing the current state of the washing machine.



## What next?¶



Oh buddy, it doesn't stop there. We've currently got a doorbell pinging into our Discord, and the washing machine constantly updating too, but as my friend put it, we "need more smart-home bullshit". So, what next?



Well, the washing machine is the only "smart" Wi-Fi enabled appliance in the house. But, how do I know when my tumble dryer is done? Or my dishwasher? How am I going to control my TV without using the remote? It's 2025 people! I shouldn't have to use a remote to control my TV!



The plan is, in future, since we can't hack something that doesn't have a brain, to instead attach a brain to it. The dishwasher is easy, we can just whack that on a smart plug and monitor when the power use surges and drops. The dryer is a bit more difficult, since they pull a LOT of power, and smart plugs typically either don't support that much power, or are incredibly expensive. So that's likely going to be some fancy vibration sensor-based thingy, and the TV can likely be controlled by some cheap IR blaster hooked up to a control board or something. We're also probably going to rig some awful webcam cameras up to the windows at the front and back of the house, in theory for security monitoring, but in reality, just for the love of the game.




Anyway, that's all I've got for you this newsround. I hope you enjoyed the read! If you've got any questions or feedback, feel free to contact me:https://timedout.uk/contact.html. Also if you think I do cool things, I now have fee-free ways to buy me a beverage:https://timedout.uk/donate.html.






 Back to top
