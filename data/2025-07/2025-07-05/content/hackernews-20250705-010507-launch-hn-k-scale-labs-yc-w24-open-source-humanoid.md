---
title: 'Launch HN: K-Scale Labs (YC W24) – Open-Source Humanoid Robots | Hacker News'
url: https://news.ycombinator.com/item?id=44456904
site_name: hackernews
fetched_at: '2025-07-05T01:05:07.944940'
original_url: https://news.ycombinator.com/item?id=44456904
author: codekansas
date: '2025-07-05'
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
Launch HN: K-Scale Labs (YC W24) – Open-Source Humanoid Robots
206 points
 by
codekansas

22 hours ago

 |
hide
 |
past
 |
favorite
 |
88 comments
Hi HN, I'm Ben, from K-Scale Labs (
https://kscale.dev
). We're building open-source humanoid robots.

Hardware video:https://www.youtube.com/watch?v=qhZi9rtdEKgSoftware video:https://www.youtube.com/watch?v=hXi3b3xXJFwDocs:https://docs.kscale.devGithub:https://github.com/kscalelabsHN thread from back in May:https://news.ycombinator.com/item?id=44023680I started K-Scale because I really wanted a humanoid robot to hack on, so I knew that if I built one, I would have at least one customer. It was before the Unitree G1 came out so the cheapest option at the time costed over $50k, but I figured I could build one for about $10k using COTS (Commercial Off-the-Shelf) components, which would be a much better price point for indie hackers and developers.We built the first version using some 3D printers and parts that I bought off of Amazon and Alibaba. It was not great, but it let us build out the full pipeline, from designing and building the hardware to training control policies in simulation. We actually did most of this in about two months, and had a standing, waving robot by YC Demo Day (although it wasn't good for much else!).Since then, our focus has been on figuring out how to go from a hobby-grade robot to a consumer-grade robot, without inflating our BOM (Bill of Materials, i.e. cost of all the parts) or having to set up our own factories. This is surprisingly difficult. A lot of the supply chain for robotics components currently goes through China, but tariffs have made it difficult to rely on Chinese suppliers for components. Also, even a $10k price point is pretty expensive for most customers, for a humanoid robot that has fairly limited capabilities.Our solution to this is to open-source our hardware and software. This makes it easier for us to navigate tariffs and manufacturing challenges. By making our reference design public, our suppliers have a much easier time figuring out how to offer us competitive solutions, and our manufacturing partners are able to more easily adjust our design for their production processes.On the demand side, the basic problem with humanoid robots is that they're mostly useless right now, and it will probably be a long and fairly capital-intensive journey to make them useful. My expectation was that there is a large pool of latent interest from people like me who are interested in hacking on humanoids, and that this customer segment is a much better customer segment to sell into than more traditional business-focused robotics applications. As someone in this customer segment myself, I felt that open-source software and hardware would be a strong value proposition, particularly for developers exploring bringing humanoids into their own business verticals.More philosophically, I think it is important that there is a good, open-source humanoid robot. I think the technology is likely to mature much more rapidly than many people currently expect, and the idea of armies of humanoids owned by some single company walking around is pretty dystopian.Right now, we're selling our base humanoid robot, K-Bot, for $8999. The main reason we're selling it now, instead of waiting to do more R&D, is because we're trying to negotiate volume prices with our own suppliers before we do final DfM (Design for Manufacturing). For example, we are able to negotiate better volume pricing for actuators and end effectors than what the average indie developer would be able to get for low-volume orders.However, a lot of the people who want to buy a humanoid robot today do so because they want a completely autonomous robot to do all their chores, which is a pretty hard (although exciting) thing to build. To square this circle, we're offering a "Full Autonomy" option - it is the same robot hardware, but we will provide free hardware and software upgrades until we are able to make the robot fully autonomous. This way, we can have some extra cash upfront to kickstart development, and start to build a core group of people who are aligned with helping us improve the robot's capabilities across a diverse set of environments. From our customers' perspective, it's a way to de-risk buying a first-generation product from a young hardware company, and to have a bigger influence on how the technology unfolds.The best part about building open source software and hardware is getting torn apart by people smarter than us, so we'd love your feedback!

BrandiATMuhkuh

20 hours ago

 |
next

[–]

Congratulations on the launch! This is really cool.

I'm not super active in the humanoid robot space anymore, however I did my PhD about 9 years ago in HRI.
That was the time of Boston Dynamics, DARPA robotics challenge, and Aldebaran's Pepper and Nao robots.You mentioned you are building everything open source. What happened with ROS and related projects? Do you build on top of that, or is that all super outdated that a reboot was needed?Another question I have is: why are you choosing a two-legged human over a four-legged one?My experiments with two legged robots were mostly bad. Not only did they fall basically all the time but they also had a big drift. So far, I have not seen any large improvements. But again, I might be very outdated.I always said to my colleagues. The main point stopping robots from picking up is a stable platform. And with the platform I mean walking.

reply

codekansas

20 hours ago

 |
parent
 |
next

[–]

Eh. I think we got a bit nerd-sniped on some things and we ended up trying to build most of our stack ourselves. The control loop is just a pretty simple Rust loop for running ML models. ROS is kind of annoying to work with and the control loop is pretty simple so we just wrote it ourselves.

For two legged - I think it will eventually be quite a bit cheaper, it's mostly a software problem to get them to be stable. RL based control has gotten much, much better. For example, I was talking to Trevor Blackwell a few weeks ago, and he was saying the IMU on the original Anybots robot was over $2k, whereas if you throw a noisy IMU into sim, you can get away with something basically from a cellphone. So yea, personally I'm a big believer in needing to solve the robotics intelligence problem, and once you solve that, humanoids will make the most sense as a form factor.

reply

chrsw

21 hours ago

 |
prev
 |
next

[–]

I have some technical questions about feet.

Human feet have metatarsophalangeal joints connecting the toes to the rest of the foot. But humanoid robots don't have these (at least, the vast majority don't). Why? These joints are very useful.Also, the bottom of the human foot is soft and has thousands of nerve endings. Can we really expect robots to get anywhere near human mobility performance without this level of compliance and sensory sophistication?

reply

cpgxiii

21 hours ago

 |
parent
 |
next

[–]

Feet/ankles on humanoids are really hard mechanically. In many ways the kinematic requirements for the ankle are similar to a wrist, but while the wrist of a robot arm is the least-heavily-loaded, the ankle area can be the most heavily loaded. Humans get away with it by having most of the highly-stressed actuators in the lower leg, not the ankle itself, whereas many humanoid robots end up putting more of the actuators in the ankle assembly itself.

In general, I think the best way to think about the differences between human muscles and robot actuators is that human muscles are simultaneously incredible in terms of strength and power density, and also incredibly fragile. Robot actuators are fairly robust, but comparatively poor. Humans are essentially falling apart at all times, but the repair mechanisms in the body do a good enough job that it doesn't matter (although you probably know someone with a "career-disruptive/ending" sports-related injury that shows these mechanisms have limits). Robotics is a long way away from making actuators that can be fixed online in such a process. Even cable stretching in cable-driven mechanisms remains hard to handle effectively, and that's one of the simplest types of mechanism wear.

reply

bbertelsen

20 hours ago

 |
root
 |
parent
 |
next

[–]

These are the kinds of comments that make comments worth reading. Thank you!

reply

codekansas

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

This is a much better answer than mine

reply

codekansas

21 hours ago

 |
parent
 |
prev
 |
next

[–]

So, most humanoids you see that are relatively cost-effective are just "humanoid" in that they look like humans, but there are significant mechanical differences between them and real humans. It's almost always driven by the cost of manufacturing different components. A good example is the lead screw you see in the knee and ankle on Optimus - while it is more human-centric to have tendon-like actuation, it drives the price up quite a bit. Put differently, humans have a lot of specialization which is not great if you want to mass manufacture something.

For walking, the most important thing is that the robot can be simulated well, so in our case, we tried to model the foot contact with the ground in simulation quite accurately. In fact, we found that force sensors in the foot probably help but they're not necessary in simulation, and we wanted to shave off anything that wasn't necessary. I am not sure how close we will get to human mobility - it's definitely a learning process - but you can get much further in simulation than you'd expect.

reply

pj_mukh

21 hours ago

 |
prev
 |
next

[–]

Pretty sweet! Don’t have the time (or budget) to directly invest in the hardware but do you have a list of open source “open” software problems you are looking to solve?

reply

codekansas

21 hours ago

 |
parent
 |
next

[–]

We do!
https://bounties.kscale.dev/

We haven't updated it much but it's a good starter point

reply

pj_mukh

21 hours ago

 |
root
 |
parent
 |
next

[–]

Amazing, pretty nice list! Two quick suggestions:

a) some of these definitely look they could be done without hardware or with light hardware support from a staff member?b) if you do a) and are open source completely I bet you don’t even need to do bounties. The increased participation could mean some great community generated solutions quick.

reply

codekansas

21 hours ago

 |
root
 |
parent
 |
next

[–]

I think it's tricky to manage an open source community effectively while still being opinionated on the product. I don't want to get too sucked into coordinating adhoc contributors - we do have a strong core team of people, and we all live together, which is pretty important. But yea, still figuring out what the right dynamic here will look like. Thanks for the suggestions!

reply

pj_mukh

20 hours ago

 |
root
 |
parent
 |
next

[–]

That's fair, especially around firmware and things like OTA updates and lower level controls/safety you'd want to keep that closer to team.

But on the long-tail of autonomy options? Implementing the latest papers, trying cutting edge solutions, I bet a thriving open-source community could be very helpful ala PR2, given that the hardware is already open-source.Nothing stopping you from picking and choosing from the various implementations to build into a streamlined product offering on the front end.

reply

codekansas

20 hours ago

 |
root
 |
parent
 |
next

[–]

Yep I definitely agree. Our team is pretty small and bandwidth limited

I basically think our goal is to solve all the boring stuff and make it work reliably, so that other can people can try out the cool ML stuff more easily

reply

randomNumber7

16 hours ago

 |
prev
 |
next

[–]

What ML algorithms do you intend for full autonomy? Multi Modal LLMs for planning that control the robot by generating s.th. like code? Or s.th. that requires more learning from the environment?

When I click "get in touch" on your github I just land on the website where I can buy the robot. Building the hardware for an autonomous robot is orders of magnitudes easier than the control. Do you think anyone with the capability do develop an autonomus robot will buy this and then just give you the code because its open source?

reply

codekansas

15 hours ago

 |
parent
 |
next

[–]

My overall plan is basic joystick control -> VLA with RL -> self-supervised embodied representation -> end-to-end RL -> end-to-end control. I suspect there will be some very good multi modal models coming out in the next few years which we might use as base models, although more likely, we will adapt their techniques to work on data from our own robot.

I agree that the hardware is easier than the software - I am a software guy, personally, but I felt that it was important to do the hardware first so at least we can have a baseline product which we can offer to people. I would personally like to work on this software problem (or rather, build a company to work on this problem), and this seems like the right way to go about funding working on this problem.

reply

randomNumber7

15 hours ago

 |
root
 |
parent
 |
next

[–]

I like the K-Sim Gym. Im looking forward to fiddle with it a bit when I have more time. I could see that you get something usefull out of people competing on your leaderboard xD

It's my hot take that the next big ML breakthrough needs s.th. that learns from its own actions in an environment, so this goes in the right direction imo.On the other hand a lot of big companies struggle with self driving cars even though they predicted to build this years ago. Also probably all big AI companies work on AI for autonomous robots. Where do you intend to do s.th. different to get a shot at competing with them (when they have so much more capital)?

reply

codekansas

12 hours ago

 |
root
 |
parent
 |
next

[–]

I really do think that building through the open source community is the best way to compete with the big players, even without having a lot of capital. Of course, it doesn't mean we can't execute well, but I do think it's a good way to make a lot of progress without spending a lot of money.

reply

srameshc

21 hours ago

 |
prev
 |
next

[–]

I love the idea of humaniod robot and commercially available. I like to think of such expensive things as an investment rather than a toy if I have to buy. Question is what are some good use cases that can be solved with such a humanoid robot ?

reply

codekansas

21 hours ago

 |
parent
 |
next

[–]

To be honest, I don't know that there are many applications today which humanoids are the best form factor to solve. I would view it more as a form factor that is likely to get much more useful over the next few years, and having the hardware in your home lets you try out new techniques as they come online.

Personally, I think the first real use cases will mostly be entertainment. Humanoids have a high "coolness" factor. Also, I think there's a long tail of random problems which you don't want to buy a new robot to solve, but which, if you have a robot lying around that isn't perfect but is "good enough", might be possible to solve imperfectly. For example, I just had a newborn baby, and I was thinking it would be nice if I had a static arm that could hold his bottle for me. There's a lot of tail end problems like that in your day to day life. But I think the really interesting capabilities will come once there's very good end-to-end models running on-device.

reply

srameshc

20 hours ago

 |
root
 |
parent
 |
next

[–]

Thanks for an honest response. I did some google search and I see that even a simple Robotic arm costs over $15, so K-Bot is at a good price point . If I have to invest purely for learning and trying to integrate with something like Gemini Robotics SDK, do you think it will work ?

reply

codekansas

20 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah, this is exactly the kind of use case we intend to support. Basically, we want our robot to be the best mass-produced robot for this kind of experimentation.

reply

999900000999

9 hours ago

 |
prev
 |
next

[–]

Cool.

But this looks like an expensive toy.The stuff of nightmares is this being adapted by the DoD. I can almost imagine your website as a scene in the prologue of a terminator like movie.Nightmare 2 is this becomes a companion of some sort. Detroit Become Human goes into this. You have a theme of the robots basically wanting freedom. Which throws out a moral conundrum, if someone buys an AGI enabled bot just to be mean to it, have they done anything wrong.I like technology , but this feels like step one to a whole lot of weird stuff.

reply

bravesoul2

2 hours ago

 |
parent
 |
next

[–]

DoD has Boston Dynamics? I think this is like the Llama. Give everyone else a play.

reply

codekansas

8 hours ago

 |
parent
 |
prev
 |
next

[–]

I suspect that these kinds of things will happen with or without my involvement. Assuming that they do, I would rather that a good open source option exists

reply

Ey7NFZ3P0nzAe

3 hours ago

 |
root
 |
parent
 |
next

[–]

Aren't there ways to legally forbid reusing anything you made for war like purposes?

reply

swyx

18 hours ago

 |
prev
 |
next

[–]

congrats! just sharing also the behind the scenes talk that one of your engineers did at AIE:
https://www.youtube.com/watch?v=BS92RdBvI90

reply

v5v3

18 hours ago

 |
prev
 |
next

[–]

>However, a lot of the people who want to buy a humanoid robot today do so because they want a completely autonomous robot to do all their chores,

Not sure your research has been through.The ones that get the most attention from what I've seen are the ones that look female. And the first comment is always about how easy to clean...All those lonely men spending thousands on the billion dollar revenue generating onlyfans and webcam sites seem to be the immediate consumer market.

reply

codekansas

18 hours ago

 |
parent
 |
next

[–]

Yes, we are aware of this customer segment. I don't think they have thoroughly considered the implications of what high torque actuators can do to the human body

reply

beau_g

18 hours ago

 |
root
 |
parent
 |
next

[–]

Every technological leap has it's Chuck Yeagers and Yuri Gagarins that will put it all on the line with early tech for humanity to take that next step - we have to accept the inevitable and hope that luck is on these brave soul's side

reply

idiotsecant

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

You might have a significant portion of those customers that are into that

reply

nativeit

12 hours ago

 |
root
 |
parent
 |
next

[–]

Castration via motorized actuator? Pretty niche kink, I'd say.

reply

voidUpdate

4 minutes ago

 |
root
 |
parent
 |
next

[–]

cheaper than getting bottom surgery

reply

deepdarkforest

22 hours ago

 |
prev
 |
next

[–]

>
the demand side, the basic problem with humanoid robots is that they're mostly useless right now ... ... to square this circle, ... we will provide free hardware and software upgrades until we are able to make the robot fully autonomous...This way, we can have some extra cash upfront to kickstart development

Congratulations guys! The technical stuff is above my paygrade, but you have a cracked team and with open source you will have a great chance to be close or at SOTA level at your price point.However, it looks to me that your core thesis is yes, when the autonomous robots get good enough, even at a medium family car price range they will sell like candies. Sure. But since you also want to have the cash now, to who exactly are you selling? Yes you promise that you will support the full autonomy option, but this sounds weirdly similar to Tesla selling cars promising the FSD, which we all know how that story went.I'm not saying you won't deliver, I'm just saying you might need to a bit more careful in your story selling/narrative for this. For example, i would be super interested to get one for like 2k if it's not useful now, but paying 10k for essentially promises and possible upgrades is a bit iffy. Hence i would like to at least see some plug in and playcurrentusecases? Even if they are just for fun.

reply

codekansas

21 hours ago

 |
parent
 |
next

[–]

I spent two years on Tesla's FSD team, and I think from a cash flow perspective for funding R&D this model did make a lot of sense - basically, it takes cash upfront for training models, but there's zero marginal cost for distributing the models once you've developed them.

I think this kind of "promise the future, pay now" model does alienates some people, especially when the tech is not ready today. That's why we're open sourcing everything, to avoid the feeling of overpromising on what is ready today. The core idea is that the people who bought FSD early on were very invested in it's success, and that feedback loop is very important for improving machine learning models at scale. The problem happens when actually delivering on the tech takes a long time, but I think we have a fairly clear technical roadmap to make our robot useful. At least, I think there are a lot more intermediate benchmarks for driving value for a humanoid robot than there are for self-driving cars, so I think people who buy it will have a stronger feeling that it is constantly improving.

reply

deepdarkforest

21 hours ago

 |
root
 |
parent
 |
next

[–]

From a cash flow perspective of course it makes sense to sell the future before you have it as working product. It just needs a great salesman or narrative to keep it going, im not arguing that.

>that feedback loop is very important for improving machine learning models at scaleOh will you have your own feedback loop with let's say user's data? Or you meant as an example?> * That's why we're open sourcing everything, to avoid the feeling of overpromising on what is ready today*I agree here, it helps the today, but I dont think it helps the feeling of overpromising on what is ready today, its more like, even if it's open source , it does not increase the chances of it being ready/autonomous in the future. (im just playing devils advocate here)I also agree with the intermediate benchmarks for sure, this is more to what i was referring to, it would be nice to see some more short term usecases/fun applications that are realistic to hit today or in the nearer future, that would drive a lot of sales value, at least for me, rather than go from now to full autonomy. Good luck!

reply

codekansas

21 hours ago

 |
root
 |
parent
 |
next

[–]

> Oh will you have your own feedback loop with let's say user's data? Or you meant as an example?

That's more or less the idea - obviously since it's open source we wouldn't scrape peoples' data without their consent, but I would hope that people would contribute to the project in some form. Like, the core idea of the open source ethos is that building something like this collaboratively is a better / cheaper way to scale data collection / experience than us trying to collect all the data ourselves.> it does not increase the chances of it being ready/autonomous in the future.Yea that's true. At the end of the day it's just technical execution, so it's pretty risky. I just prefer that if people sign up for something risky, it's pretty transparent what exactly it is they're signing up for :)

reply

timhigins

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

> we're open sourcing everything

Does/will this include the training data, hyperparams, and weights for the models?People will be reluctant to buy an "open source" robot if the key ML magic to make it work is closed off, e.g. if you charge a subscription for it.

reply

codekansas

20 hours ago

 |
root
 |
parent
 |
next

[–]

Yeah of course. That's kind of the whole point - I don't think you can really trust a humanoid robot in your house around your family if it is not clear what it's running. Basically, for myself, I would not want to buy a closed sourced humanoid, and I view myself as relatively representative of the early adopter mentality. So personally I think this is the right way to build a great product.

I basically believe that in a world where humanoid robots are actually useful, we will not have any trouble monetizing. Probably we will verticalize manufacturing at some point in the future. I think the bigger risks for our business model are not from people copying us or something, but from not making progress fast enough.

reply

a_t48

17 hours ago

 |
root
 |
parent
 |
next

[–]

Love it. It's tough to balance keeping the ship afloat vs giving back to the community, I think you've got a good thing going.

reply

timhigins

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

Great to hear, thanks for the response!

reply

markisus

17 hours ago

 |
prev
 |
next

[–]

Congrats on the launch!

Your current market seems to be "niche toys for rich tech people" and the future market seems very uncertain. I am impressed that you were able to get funding for this idea. How do you get around the "solution in search of a problem (SISP)" objection from VCs? In fact, your founding story indicates that you just liked the technology meaning you had to work backwards to find the business case.I'm asking because I think many of us would like to get funding for ventures in areas of technology that we are passionate about, but for which the future market potential remains extremely speculative. How do you do it?

reply

codekansas

16 hours ago

 |
parent
 |
next

[–]

I have a pretty bad mental model of how most VCs think, but I think good VCs will fund smart people who demonstrate extreme conviction, regardless of how they initially size the market. The opportunity cost for me doing K-Scale is making quite a bit of money at Tesla or Meta, so assuming I am not acting irrationally, either I have extreme conviction or I am a masochist. In my experience, VCs are pretty bad at telling the difference.

reply

lachyg

22 hours ago

 |
prev
 |
next

[–]

Congratulations! This looks really great. What've you found to be the best hands / end effectors these days? When do you think we'll have good, reliable 5 finger hands that are ~reasonably priced?

reply

codekansas

22 hours ago

 |
parent
 |
next

[–]

I'm not convinced that 5 finger hands are necessary right now, but there is a really long tail of hand suppliers that we've been exploring to help get the price down.

I think at volume the price for a good set of hands should settle somewhere around $300-500. Most of it comes down to meeting suppliers where they're at and negotiating mutually beneficial deals. It's not magic but it does require having a good understanding of the hardware in order to negotiate well.

reply

mhb_eng

21 hours ago

 |
root
 |
parent
 |
next

[–]

Have you identified any limitations in current grippers based on lack of tactile sensing solutions to unlock truly dextrous manipulation?

reply

codekansas

20 hours ago

 |
root
 |
parent
 |
next

[–]

Actually yea, the benefit of our parallel gripper is that we get some proprioceptive feedback which we can't get from the current 5 finger hand. I'm not sure how important this will be long term - I think vision can eventually mostly compensate if the ML models are good enough

reply

dbmikus

18 hours ago

 |
prev
 |
next

[–]

This is awesome! How much of your team's time goes into working on the physical hardware, versus RL simulation environments, versus managing all the training data from the real robot and the simulations?

I'm super interested in learning more about the training process of world and robotics model and the data challenges there.

reply

codekansas

18 hours ago

 |
parent
 |
next

[–]

Thanks!

We're all pretty cross-stack - there are some hardware people and some software people, but the product is quite integrated. Personally, my time has been mostly focused on the RL stack recently, and after there are more robots in the wild, I suspect my time will transition to working on building this data feedback loop.I try to answer questions pretty actively on our Discord so happy to chat there about whatever you like

reply

dbmikus

18 hours ago

 |
root
 |
parent
 |
next

[–]

I'll hop in there!

reply

rkagerer

13 hours ago

 |
prev
 |
next

[–]

I appreciate the humility in your videos, good luck with the launch!

reply

ZeroCool2u

17 hours ago

 |
prev
 |
next

[–]

My friend and I are so excited about this bot that we're actively looking for AI grants to apply to for funding the purchase! The price is incredible for what you get, but we both work in the public sector :/

reply

codekansas

16 hours ago

 |
parent
 |
next

[–]

We're exploring some options - maybe a rental option in the future. Would like to make it accessible to everyone

reply

Joel_Mckay

16 hours ago

 |
parent
 |
prev
 |
next

[–]

Consider the ROS simulators first, and look at the platforms used in RoboCup events. There are better platforms than Talos or HECTOR around.

It can take years to get a basic bipedal platform operational, and in general it takes 3 times as long to tune the software/firmware. Unless you see actual proof of platform operation for more than a minute, than take any claims as marketing hype.Could also try a cheap servo hexapod or turtle-bot kit first, as stable well-studied platforms are easier to code on. =3

reply

nativeit

12 hours ago

 |
prev
 |
next

[–]

I give you a lot of credit for your communication and openness. I am afraid full-autonomy is a fairy tale to rationalize the ungodly expense of LLMs, I personally would find taking money on spec for something like fully autonomous robotics to be a little shaky, ethically speaking. But then, I don't believe this is an unsolved problem, I believe this is an unsolvable problem, so more of a philosophical difference than an empirical position at this point.

reply

codekansas

12 hours ago

 |
parent
 |
next

[–]

I think it's a very hard problem, but I would like to align our company's incentives towards solving it

reply

smaudet

11 hours ago

 |
root
 |
parent
 |
next

[–]

Great. Another problem for us to solve, how defend ourselves from your robots.

Just because you can, doesn't mean you should.

reply

fragmede

21 hours ago

 |
prev
 |
next

[–]

https://lite.berkeley-humanoid.org/
 is only $5000. What's the extra $3000 get me?

reply

codekansas

21 hours ago

 |
parent
 |
next

[–]

Yeah, really like that project. The main difference is that it's much shorter than ours, and shorter robots are cheaper. The downside is that it can't really reach normal human spaces. Actually, we made another robot called Zeroth Bot which you can build for $350 if you want:
https://docs.kscale.dev/docs/zeroth-01

We are planning to release a similar-size robot later this year (calling it M-Bot) that will be closer in height and price, but our current focus has been on launching the full-size humanoid.Mechanically, I think Berkeley Humanoid Lite is pretty similar to the 3D printed one we made last year. Our main focus with the K-Bot redesign was to make it not break so much. 3D printed components break a lot and repair time can be quite long. Also, having the wiring routed internally makes a huge, huge difference. So there are some benefits to doing QA on a manufacturing line in terms of quality and consistency.

reply

fragmede

21 hours ago

 |
root
 |
parent
 |
next

[–]

How far away from robot hands/manipulators that are dexterous enough to repair other robots?

reply

codekansas

21 hours ago

 |
root
 |
parent
 |
next

[–]

That is a good question. I think mechanically we're probably there today, but on the intelligence level, who knows... If I had to guess, probably 1-3 years

reply

fragmede

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

obviously there's more to the kinematics than making the legs longer, but can't they just make the legs longer for it to be taller?

reply

codekansas

21 hours ago

 |
root
 |
parent
 |
next

[–]

Longer legs means more inertia on the actuators, which means bigger actuators + bigger battery, which means heavier robot, which means...

reply

fragmede

21 hours ago

 |
root
 |
parent
 |
next

[–]

right? thanks!

reply

accurrent

15 hours ago

 |
prev
 |
next

[–]

How do you plan on competing with existing Chinese manufacturers. Unitree for instance sells there robots at a reasonable price and already has walking working.

reply

codekansas

12 hours ago

 |
parent
 |
next

[–]

Well, I believe the competition up until now has mostly been on hardware, but moving forward it will mostly be in software. I don't think we will be outcompeted by Unitree on software. And I hope to capitalize on our engagement with the open source community in a way that Unitree has not.

reply

ecesena

13 hours ago

 |
prev
 |
next

[–]

Is there any doc on
the hand? It looks surprisingly cheap.

reply

codekansas

12 hours ago

 |
parent
 |
next

[–]

We try to sell it for a fair price while still making money. Actually I think there will be comparably priced humanoids coming out from other companies soon

reply

ecesena

11 hours ago

 |
root
 |
parent
 |
next

[–]

Sorry maybe I should have been more specific. I had Unitree in mind, last time I checked the humanoid with no hands was $20k and each hand was an extra $20k. Yours seems to ship with 2 hands for extra $1k (surprisingly cheap, which is great of course!). I was curious to read more about what the hands are capable of doing.

reply

codekansas

10 hours ago

 |
root
 |
parent
 |
next

[–]

Oh I see. Yes, we're currently exploring a few different five finger hand options - we will choose whichever option provides the best value. I actually quite like the Inspire hands and we might be able to get a volume discount

reply

dan344

16 hours ago

 |
prev
 |
next

[–]

So the non full autonomy would mean little software upgrades? More do it yourself?

Also, what’s the different bt the computes: like what’s the onboard computer running (the 2 options)?Thanks.

reply

codekansas

15 hours ago

 |
parent
 |
next

[–]

Yeah, the basic robot is just a robot, albeit with open-source software and hardware

For compute - we're exploring a few boards right now, but the base model will be something from Amlogic and the higher end model will be something from Nvidia

reply

dan344

15 hours ago

 |
root
 |
parent
 |
next

[–]

nice! For manipulation taskes, is kscale planning to train in sim mostly and transferring to real, or is some imitation learning used, like with gloves and such? maybe both?

Appreciate it

reply

codekansas

12 hours ago

 |
root
 |
parent
 |
next

[–]

I think we will just focus on making really great, low-cost hardware and a nice SDK, and let other people experiment with different approaches on the intelligence layer.

reply

lucubratory

16 hours ago

 |
prev
 |
next

[–]

Hey, just chiming in to say that I think this project is really cool even though it's outside the price range of what I can spend on a cool hobby.

I'm disabled, and one thing I'm really interested in long-term for humanoid robots is disability support work. Disability support work involves a huge variety of individual tasks, as many as a typical person will do in their life, so it's a good fit for an extremely general platform like a humanoid robot. Motorised wheelchairs and dishwashers exist, but a support worker might need to push a wheelchair, do sensitive dishes, do laundry, accurately open and place medications without destroying them, weigh & dose powders, help someone with going to the toilet, cook meals, drive a car, control pets, manage the level of noise/light/smells in the environment to stop someone from being overwhelmed, sanitise surfaces including themselves, navigate confusing interfaces on a phone or computer, help someone drink from a bottle, remember what sort of activities helped a disabled person in the past to be able to do them in the future, help someone with physical fitness activities like punching or kicking a pad, talk to people for someone, carry someone safely in the event of an emergency, make coffee in the morning, monitor intake of various drugs/nutrients/macronutrients, be able to reach and catch someone before they hit the floor if they pass out, help someone walk if they're unsteady on their feet, etc etc. It makes sense to me that it would be cost effective to have one platform which can do all of that with similar performance to a human, rather than automating many of those tasks individually in ways that might not be accessible to some disabled people.In terms of TAM, absolutely huge amounts of money are spent on disability care (keeping in mind that elder care is also disability care), by both governments and private citizens, and this number is forecasted to continue growing as more people become disabled by COVID-19 and demographic changes increase the elderly population relative to working age adults. As well, there are constantly scandals about how bad conditions are in some area of disability care, almost always due to underpaid, untrained, or unmonitored staff, so there's a lot of demand for both more reliable quality & lower prices; that demand is only going to grow with time. Various government bodies are very large sources of funding that are very concerned with value for money and would pursue any option that could do the job without costing as much - in my country (Australia), there's the NDIS, National Disability Insurance Scheme. They are always looking for ways to consolidate care for less money.I strongly suspect that any humanoid robot which was good enough to do disability support work would be in extremely high demand in the general population for obvious reasons, as well as being useful as a platform for labour automation, but those are much more speculative. Disability support work is a lot of money for incredibly varied tasks being spent right now. Something to think about.

reply

codekansas

16 hours ago

 |
parent
 |
next

[–]

This is really interesting to read about. To be honest, I know very little about this space, but it's something a few people have approached me about tackling.

I do think that this is a great application of a general purpose robot. I'm not sure what the technical timeline will be, but it would certainly be cool for my parents to have such a robot when they are elderly.

reply

lucubratory

15 hours ago

 |
root
 |
parent
 |
next

[–]

I spend a lot of time thinking about it day-to-day because of my disability and reliance on multiple disability support workers, as well as living with my husband who is also disabled, so if you ever wanted to talk to someone with disability support workers feel free to ask.

reply

andrewrn

16 hours ago

 |
parent
 |
prev
 |
next

[–]

This, to me, is the most compelling and humane application of humanoids. Often I think people jump to humanoids taking jobs, but wow, it would be so incredible for elderly folks to have a humanoid that can help them.

reply

dchuk

18 hours ago

 |
prev
 |
next

[–]

Your build guide link is a 404

reply

codekansas

18 hours ago

 |
parent
 |
next

[–]

Which link? I can fix

reply

bbor

21 hours ago

 |
prev
 |
next

[–]

Looks very cool! $9K is well outside my budget, but very reasonable for even small startups -- props.

Small note:https://www.kscale.dev/whyis a 404

reply

codekansas

21 hours ago

 |
parent
 |
next

[–]

Oh thank you! Will fix

reply

alexnewman

13 hours ago

 |
prev
 |
next

[–]

I'm so glad I sent them a check asap. Super proud that there's georgia (as in 404) in the founder crew

reply

codekansas

12 hours ago

 |
parent
 |
next

[–]

Really appreciate it :)

reply

hmmmmmmmstve

21 hours ago

 |
prev
 |
next

[–]

Seems like the thing is entirely manufactured and mostly designed by a Chinese company?

https://mp.weixin.qq.com/s/V_WVFSJg3cTPq0Y4gK4cHw

reply

amacneil

20 hours ago

 |
parent
 |
next

[–]

That post says "manufactured", why would you assume "mostly designed"?

Any robotics company that is not thinking about manufacturing from day 1 is not a serious robotics company.

reply

codekansas

20 hours ago

 |
parent
 |
prev
 |
next

[–]

Tao Motors reached out to us about a month ago after our soft launch because they just bought a big factory in Texas to manufacture golf karts, and the supply chain for golf karts and humanoids is actually pretty similar. Their subsidiary invested some money in our company recently and we are partnering with them to scale manufacturing. I discussed this in our launch video.

reply

harhargange

20 hours ago

 |
prev

[–]

Nothing against the company but I'm waiting for the tech to get backlash. I have a feeling people are going to want to end the techno autocracy and so-calledb advancements that go on to become weapons while people continue to go back to old ways and learn old skills that prove to more useful.

reply

codekansas

20 hours ago

 |
parent

[–]

Yeah I think humanoids are a pretty fraught area. There's definitely been some backlash but overall I have really appreciated the responses we've got from people. Like, I just want people to care about what we're doing - if positive that's great, if negative then we can learn how to do better. As long as people have an opinion one way or the other, I'm happy :)

reply

Consider applying for YC's Fall 2025 batch! Applications are open till Aug 4

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
