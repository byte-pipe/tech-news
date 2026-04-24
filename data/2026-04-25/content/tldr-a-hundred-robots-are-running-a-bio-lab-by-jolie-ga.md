---
title: A Hundred Robots Are Running A Bio Lab - by Jolie Gan
url: https://www.corememory.com/p/a-hundred-robots-are-running-a-bio-medra-michelle-lee
site_name: tldr
content_file: tldr-a-hundred-robots-are-running-a-bio-lab-by-jolie-ga
fetched_at: '2026-04-25T08:21:47.515058'
original_url: https://www.corememory.com/p/a-hundred-robots-are-running-a-bio-medra-michelle-lee
author: Jolie Gan
date: '2026-04-25'
description: Meet Medra and the pharma factory for the AI age
tags:
- tldr
---

# A Hundred Robots Are Running A Bio Lab

### Meet Medra and the pharma factory for the AI age

Jolie Gan
Apr 23, 2026
39
4
Share

The small robot has brushed past me five times in the last hour.

It runs loops around the perimeter of the third floor of this bio lab, serving as a courier. The machine’s job is to visit workstations and keep other robots - arms bolted to lab benches - fed with whatever they need be it pipette holders, sealed plates or something in a labeled bag. The little bot is relentless and unconcerned about me or much else beyond its job. Out of the corner of my eye, I spot chairs still rotating slowly on their bases from where it clipped them on the last pass.

About a hundred robotic arms fill this room, each one positioned beside a different scientific tool. The arms must deal with centrifuges, incubators, chambers and tubes. They run simultaneously and continuously. The small robot links them together, ferrying consumables between stations the way a junior scientist carries things between benches. Except the benches are robots. And so is the assistant.

All of this is the brainchild of Michelle Lee, the founder and CEO of Medra. And, at this moment, she’s rather proud that one of her robots has learned to open and close a glass door with ease.

Subscribe

MEDRA TODAYformally announced the opening of its 38,000 square foot warehouse in San Francisco. The company runs what it calls “physical AI scientists”: general-purpose robot arms with cameras mounted near their grippers and nine different sensors - all governed by software that lets the arms operate lab instruments the way a trained human would.

Standard lab automation gear, the kind that has existed for two decades, comes with dated APIs and rigid interfaces. Only about five percent of the instruments sitting on a scientist’s bench fall into the “can be automated” category. The rest — centrifuges you open and balance, pipettes you grip and tilt and time — were designed for hands. Medra thinks it has technology to automate the old and the new. Its software uses computer vision and manipulation models to adapt to the instruments that labs already own. Lee says that, if successful, Medra’s physical AI scientists can bump the overall automation number for bio-tech tasks from five percent to seventy-five percent.

THE PLATFORMworks in two linked layers.

The first is physical: cameras are mounted on every arm and every lab bench with the nine sensors doing yet more monitoring. When an arm opens a centrifuge, for example, the wrist camera reads the rotor angle to balance the load. When a pipette misses a pick-up, the system catches the mistake and sends a notification. The sensor network logs the exact angle of every pipette tip, the exact depth of its insertion, the timing between reagent additions — all of it automatically. With humans in a lab, this layer of practice is tacit — an experienced scientist builds intuition for what to do over years, and once they leave or retire, their knowledge goes with them. Medra’s sensors would be among the first systems to put this information on the record. “The way science sometimes works is super subtle,” Lee says. “You vortex it thirty seconds more, shake a certain way, suddenly it starts working. How do you capture that? The robots just capture exactly what they do.”

The second layer is the AI scientist: a software agent that reads the results, identifies what’s going wrong, proposes protocol changes, and rewrites the protocol itself. It can run autonomously or hold for human approval. According to Lee, one customer ran an experiment to test whether their antibodies would bind to a target protein. The answer came back zero — meaning the antibodies weren’t sticking to anything. The AI scientist narrowed the problem to two hypotheses, designed a test to distinguish them, proposed adding a vortexing step mid-protocol, and watched binding jump from zero to more than seventy percent.

There was no automation engineer involved - just a chat interface and an arm. The doing and the thinking on one platform.

The arms are general-purpose hardware, sourced from the same manufacturer that supplies Toyota factories. The software is what makes them useful in a lab context.

“We adapt general robots for the reality we live in,” Lee says.

We’re in the midst of an AI-for-bio boom with a bottleneck problem. Companies likeChai Discoverycan now design drug candidates at a pace that would have been unthinkable five years ago. But a designed molecule is not a validated one. Every drug candidate still has to be synthesized and tested in a physical lab by physical scientists who can only run so many experiments in a day. The software has sprinted ahead of the hardware.

Whether Medra is the company that closes the gap is another question. Lab automation and versions of “AI scientists” have been overpromised for two decades. But somebody has to build the throughput. A hundred arms running in San Francisco is a worthy attempt.

Medra’s old lab was 4,000 square feet and had a handful of robots in training. This new building has three floors of weight-bearing concrete and 38,000 square feet of space. Back in November, Medra had 15 employees. Now, it’s up to 45. Five customers have experiments scheduled to run across the robot army inside of the only autonomous lab in the city.

Customization is Medra’s moat. A new customer describes their protocol: instruments, throughput, consumables. An agent asks questions, builds a simulation from a JSON file, optimizes the layout, and runs the protocol virtually before the first arm moves. More than eighty-five percent of customers arrive with a request Medra has never fulfilled before. Because the software and hardware layer is consistent across protocols, reconfiguring from one setup to a hundred doesn’t require massive rebuilding. Over the last three months, Medra went from none of these systems in the building existing to a hundred arms running antibody binding.

Share

Medra’s customers own their experimental data: the sequences, the targets, the candidates. What Medra retains is process knowledge – the pipette angle that produced good results, the vortex duration, the timing between reagent additions. The data edge compounds the more protocols the company runs.

One gap, though, remains. The system can detect a missing plate, catch a dropped tip, and read a centrifuge rotor. It cannot distinguish one colorless liquid from another. Humans still open boxes and load the consumables. For now, there’s no way around it.

LEE GREWup in Taiwan and came to America at fourteen. Her family worked in chemical engineering, and so, as one does, she studied chemical engineering, built a go-kart in undergrad, won a grant for an iPhone, and spent 2015 interning at SpaceX. You can hear traces of her time at SpaceX - and remnants of Elon Musk’s unwavering commitment to speed and infrastructure — in the conviction in her voice. Just ten years ago, everyone she knew at Google was praising Project Loon – Starlink seemed like insanity.

Now, she tells me, “Starlink feels inevitable.”

Lee was supposed to become a professor at NYU. Then, in 2021, AlphaFold 2 was released, and she started thinking through why it worked. Protein folding was solvable because fifty years of structural data existed to train on. Data for problems like drug target validation, antibody design and gene function is still limited, and the only way to get more data is to run more experiments. Labs can run only as many experiments as they have scientists, and scientists, like all humans, have limited working hours and, when they leave, take their technique with them.

From 2022 to 2024, Lee tried to build standardized cell culture boxes – something she could sell to multiple customers. She quickly learned that every lab wanted the work done differently and ended all the pilots in 2024. Then she rebuilt the hardware and software, this time designed to be reconfigured for each customer instead of sold as a fixed product.

The first Medra customer signed a six-figure contract on the basis of a PowerPoint and photographs of a robotic arm (the arm hadn’t even been hers — she had borrowed it from a friend with access to a lab.) The team had exactly one employee: Lee.

THE MODELshe uses to explain Medra is TSMC. TSMC manufactures the chips that make it possible for chip designers to exist. Medra wants to be what makes it possible for a drug discovery company to run experiments without building its own lab.

She grew up watching semiconductor manufacturing transform Taiwan into a geopolitical asset. Then realized early on that the infrastructure had to exist domestically.“Science is so critical to the United States’ — any nation’s — prosperity and also national security,” she notes. “If all our antibiotics come from abroad, what happens when there’s a national security crisis?” There’s urgency in her voice. “We need to move fast.”

The Chinese pharmaceutical industry has been moving fast for decades. Novo Nordisk, Eli Lilly, and most major American pharmaceutical companies manufacture extensively in China, where Chinese scientists, technicians, and — you guessed it — robots have been accumulating process knowledge at a volume no American lab has matched. As with more traditional manufacturing, the U.S. has fallen behind, which is not ideal as we head toward a century possibly full of bio-tech breakthroughs.

Medra offers the hope that the U.S. could play off its AI and software strengths and find a way to compete.

The arms are still running when you leave the third floor, and will still be running as you head to bed tonight. The small robot is still on its circuit – tip rack here, plate there – moving through the room on a schedule that doesn’t stop at five or take weekends. The jobs queue and clear. The arms complete their protocols. The chairs spin slowly in the corners.

“If we could cure cancer, Alzheimer’s, infectious disease – we have the ability to do that,” Lee says. “We just don’t have the throughput.”

The bot makes another pass.

Subscribe
39
4
Share
Previous
Next