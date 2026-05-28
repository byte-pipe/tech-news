---
title: Amazon Thinks the Future of Data Centers Depends on a Technical Problem It Just Solved | WIRED
url: https://www.wired.com/story/amazon-thinks-the-future-of-data-centers-depends-on-a-technical-problem-it-just-solved/
site_name: newsfeed
content_file: newsfeed-amazon-thinks-the-future-of-data-centers-depends-o
fetched_at: '2026-05-29T04:36:19.099535'
original_url: https://www.wired.com/story/amazon-thinks-the-future-of-data-centers-depends-on-a-technical-problem-it-just-solved/
author: Lauren Goode
date: '2026-05-28'
published_date: '2026-05-28T10:30:00.000Z'
description: The tech giant says a breakthrough in data center networking has dramatically accelerated the flow of information through its massive cloud infrastructure.
tags:
- wired
- business
- business / artificial intelligence
- business / big tech
---

Save Story
Save this story
Save Story
Save this story

Amazon says itrecently achieved a major breakthrough in networking design—and has been quietly deploying the new technology in itsdata centerssince late last year. The company claims it has significantly increaseddata speedswhile reducing energy use, potentially giving the tech giant an edge as companies race to build ever-faster systems in the cloud.

The new technology hinges on a “quasi-random” design that combines elements of traditional, structured data networks with the performance advantages of more random architectures. Researchers have explored random networks for decades, but the technology has never been successfully scaled. Now, Amazon thinks it has cracked the code.

The fact that Amazon is using this in the real world is “remarkable,” says Brighten Godfrey, a computer science professor at the University of Illinois Urbana-Champaign and an expert in networking, who was not involved in Amazon’s research. Godfrey coauthored a seminal 2012 paper on random network graphs, which he says are a “mind-bending problem to solve, in general.”

A team of engineers and researchers atAmazon Web Services, including several recruited from academia, has been working on the random networking problem since 2023. Amazon also designed a new piece of data center equipment it dubbed the ShuffleBox, which automatically shuffles the cables required for this kind of networking.

“By essentially flattening the network, we eliminated the bottlenecks that come with traditional networking designs,” Matt Rehder, vice president of AWS Network Engineering, said in an exclusive interview with WIRED. “We think we’re the only ones who have done this at scale.”

Courtesy of Amazon

## Network Effects

Amazon detailed its new networking design in apaper published last monthtitled “RNG: Flat Datacenter Networks at Scale.” RNG stands for “resilient network graphs,” which are neither entirely structured nor entirely random.

Interestingly, the Amazon team behind RNG isn’t making this networking pitch around generative AI. This is about making the company’s everyday data center architecture more efficient. “RNG is a great fit for our core demands, but AI training data patterns are far more coordinated and centrally orchestrated, so they don’t approximate a random graph,” Rehder says.

Since the mid-1980s, communications networks—from telecoms to data centers—have been predominantly designed with a“fat-tree” topology, which includes two or three vertical layers of switches and routers. These are connected by “fat” nodes at the top of the structure, where there are multiple routers of the same type, and thinner branches toward the bottom. Put very simply, in a fat-tree network, data moves up and down the stack. The increased bandwidth near the top of the structure, where the data bisects, helps eliminate bottlenecks.

Over time, the tech industry has developed and deployed variations on the fat-tree architecture. But the design has room for improvement. It’s generally reliable but also rigid and inefficient, and it requires complex cabling. As in, actual physical cables.

If you’ve ever been in a data center or an office building’s server room, you’ve likely seen nests of colorful cables spilling out of metal racks. Cabling is one of the greatest costs in networking, Rehder says, and Amazon’s global data centers are currently connected with 20 million kilometers of fiber-optic cables. That’s roughly the distance it would take to travel from Earth to the moon and back 25 times.

In 2012, as the demand for cloud computing services was exploding, a group of researchers at University of Illinois Urbana-Champaign, including Godfrey, introduceda concept known as Jellyfish. Fixed network designs in use at the time were struggling to meet growing demand, so the researchers proposed a “high-capacity network interconnect which, by adopting a random graph topology, yields itself naturally to incremental expansion.” They believed this random approach could be more efficient and scalable than networks built using the fat-tree architecture.

“We gave it the name Jellyfish because it’s fluid,” Godfrey says. “You can connect the routers and switches randomly and it becomes this flexible pool of network capacity, which is very efficient.”

However, Jellyfish also introduced new challenges in layout, data routing, and cabling. Routing in random graphs is trickier, Godfrey says, because there are many more and diversified paths that data can take from its source to its destination. Cabling is harder because the endpoints of the cables are chosen randomly.

A couple of years later, Google began toying with another solution: Itstarted integrating optical circuit switching, or OCS, into its network designs. This approach uses tiny mirrors to reflect light from an input port to an output port, which lets Google reconfigure optical cabling in real time. But again, this adds a certain amount of engineering complexity as well as cost.

## So Random

Amazon, meanwhile, was searching for the “holy grail,” says Giacomo Bernardi, who is one of the lead authors on the new paper, along with Amazon Scholars Ratul Mahajan and Seshadhri Comandur. In an ideal world, a data network would be flat and efficient, resilient to hardware failures, random enough to maximize performance, and scalable enough to grow without becoming unwieldy. It would also rely on simpler, streamlined cabling rather than increasingly complex fiber-optic systems.

When he and his colleagues began trying to build such a network, Bernardi says he had already become obsessed with Penrose tiling, a kind of aperiodic tiling named after the British physicist Roger Penrose. (Other researchershave been so inspired by Penrose tilingsthat they’ve tried to translate the patterns into error-correcting code in quantum computers.) Bernardi wondered if Amazon could use a similar construction and create a flat “mesh” by following a repeating pattern. He and his team tried building a simulation of what that might look like.

It didn’t work. Penrose tiling was promising on paper, Bernardi says, but the simulated data network was unreliable, and the researchers didn’t achieve the efficiency gains they had hoped for. They achieved better outcomes, he realized, when they replaced the more structured parts of the network design with randomness. “We ‘embraced the chaos,’ and adopted a quasi-random approach,” Bernardi explains.

Courtesy of Amazon

A critical component of this design is the ShuffleBox, the new optical device Amazon developed that mixes connections between routers internally. During a short tour of one of Amazon’s networking labs in Cupertino, WIRED was able to view the chaotic bundle of cables running between routers in a traditional fat-tree structure, and compare them side by side with the tidy waves of cables being run through ShuffleBoxes in the new design.

Rehder says Amazon’s RNG design has made the company’s data centers both more efficient and more resilient. Compared to traditional networks, he claims it uses 69 percent fewer routers and switches, delivers 33 percent higher data throughput, cuts network power consumption by 40 percent, and lowers operating costs by 27 percent.

The first instance of RNG was unleashed in a Dublin data center in 2024. Amazon then expanded the technology to data centers in Germany and Spain. The company says that now, most newly built data centers are being outfitted with the RNG networking protocol.

## Comments

Back to top
Triangle

## You Might Also Like

* How to find us:Add WIRED.com to your preferred sourcesin Google
* These women are trying tooptimize their vaginas
* Big Story:AI gig work is the new waiting tables—and it's soul-crushing
* This summer,the American water crisisbecomes real
* Event:How to adapt, compete, andwin in the next era of business
Lauren Goode
 is a senior correspondent at WIRED covering all things Silicon Valley, including artificial intelligence, semiconductors, venture capital, startups, workplace culture, and tech's most interesting people and trends. Previously she worked at The Verge, Recode, and The Wall Street Journal. Please send story tips (no PR pitches) to ChaoticGoode.12 ... 
Read More
Senior Correspondent
* X
* bluesky
Topics
Amazon
AWS
data centers
Cloud Computing
research
math
Huawei's ‘Chip Queen’ Throws Down the Gauntlet
The Chinese company is adapting to the demise of Moore’s Law, which guides chip production. It could complicate US chip dominance.
Will Knight
Anthropic Gets in Bed With SpaceX as the AI Race Turns Weird
In an unexpected turn, the two companies signed a deal for Anthropic to use computing resources from Elon Musk’s xAI.
Lauren Goode
The Gulf’s AI Boom Has an Undersea Cable Problem
Hyperscalers are pushing the Gulf to rethink internet infrastructure as AI raises the stakes of cable disruptions.
Chris Hamill-Stewart
Welcome to the Great American Satellite Age
A new generation of satellite startups in San Francisco is racing to capitalize on recent technological breakthroughs in space-based data collection and communications.
Paresh Dave
Diabetes Detection Needs Better Tools. They’re on the Way
Blood glucose levels can be a reliable indicator of diabetes risk. But in some populations, it's not enough to catch the disease early.
Anna McKie
Former Google and Apple Researchers Launch a Startup to Build AI’s Missing Feedback Loop
Trajectory is betting the rapid iteration cycle that supercharged vibe-coding can help all kinds of companies build AI products that learn continuously.
Maxwell Zeff
Mira Murati Wants Her AI to ‘Keep Humans in the Loop’
The Thinking Machines Lab founder and former CTO of OpenAI tells WIRED she isn’t interested in automating people out of jobs. Instead, she’s building AI that can collaborate.
Will Knight
Demis Hassabis Thinks AI Job Cuts Are Dumb
The CEO of Google DeepMind tells WIRED that companies should use the productivity gains of AI to do more, not lay people off.
Will Knight
Thousands of Vibe-Coded Apps Expose Corporate and Personal Data on the Open Web
Companies like Lovable, Base44, Replit, and Netlify use AI to let anyone build a web app in seconds—and in thousands of cases, spill highly sensitive data onto the public internet.
Andy Greenberg
Testing for ‘Bad Cholesterol’ Doesn’t Tell the Whole Story
There’s a more accurate way of measuring who’s at risk for cholesterol-related health issues. So why don’t more doctors use it?
Anna McKie
Why Soccer Still Defies Statistical Analysis
Sarah Rudd, who once ran analytics for Arsenal, made her name applying the tenets of probability theory to movements on the pitch. Even she admits not everything can be solved with data.
Nick Greene
Foxconn Ransomware Attack Shows Nothing Is Safe Forever
Famous for helping build Apple’s iPhones, Foxconn just suffered another cyberattack, highlighting the perils of warehousing some of the world’s most valuable data.
Lily Hay Newman