---
title: I've Covered Robots for Years. This One Is Different | WIRED
url: https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/
site_name: hnrss
content_file: hnrss-ive-covered-robots-for-years-this-one-is-different
fetched_at: '2026-05-02T11:43:44.789431'
original_url: https://www.wired.com/story/when-robots-have-their-chatgpt-moment-remember-these-pincers/
author: Will Knight
date: '2026-04-29'
published_date: '2026-04-29T10:00:00.000Z'
description: From sorting chicken nuggets to screwing in lightbulbs, Eka’s robotic claw feels like we're approaching a ChatGPT moment for the physical world.
tags:
- hackernews
- hnrss
---

Save Story
Save this story
Save Story
Save this story

A robot’s clawhurtles toward a light bulb on a table. I wince, waiting for the crunch. But suddenly the claw decelerates. It starts gingerly pawing around the table, as if searching for its glasses on the nightstand. It gently positions the bulb between its two pincers. The bulb rolls away. The claw goes chasing it across the table. After a few nips, the bulb is back in its grasp. The robot swiftly screws the bulb into a nearby socket, illuminating its work area.

In more than a decade of writing aboutrobots, I have never seen one move so naturally. Most are ham-fisted klutzes, even when remotely controlled by a person. Of the few dozen robot arms on the market today, not one can screw in a light bulb.

I have come to visit Eka, a startup located in Kendall Square, Cambridge, Massachusetts, a short walk from MIT and a slightly longer bike ride from my home. The company’s office is a few floors above one of my favorite restaurants, called Shy Bird, a place I often come to work with my own pincers—typing out stories for WIRED.

Eka’s testing facilities in Cambridge, Massachusetts.
Photograph: Tony Luong

Eka’s office is small, and it’s packed with different robot arms, assorted grippers and hands, and tables covered with odd knicknacks of different shapes, sizes, and textures—gloves, small boxes of earplugs, hairbrushes, key rings, and so on.

I try putting a few things beneath the robot. First the earplugs box, then a hairbrush, and finally—in an attempt to trip it up—my own jumble of keys, which have a plush key ring. Each time, the robot swoops down and nips gently at the item a few times before grasping and lifting it up. When I try to take my keys back from Eka’s machine, the robot resists for just a moment, then lets go and instantly turns its attention back to the table, hunting for something else to pick up. Its dedication to picking is impressive. It is also kind of freaky.

Watching Eka’s robot in action reminds me of the first time I tried talking to ChatGPT. The robots are so fluid, so natural-seeming, that I can’t help but feel there’s something genuinely intelligent, if not quite human, behind them.

In a conference room not far from the robots, Eka’s cofounders, Pulkit Agrawal, a professor at MIT, and Tuomas Haarnoja, an ex-Google DeepMind robotics researcher, lay out their vision for the curious new machine. “A couple of years ago, we realized that dexterity can finally be cracked,” Agrawal says. Eka’s robot demos suggest that the company’s approach should enable real robot dexterity with further training. If that’s true, it could revolutionizehow robots are used—not only in factories and warehouses but also in shops, restaurants, even households. “Trillions of dollars flow through the human hand,” Agrawal says. “To me, this is the biggest problem in the world to be solved.”

The two men believe they are halfway there. Solving dexterity, they say, is now just a question of scaling up the approach.

The fastest humanscan solve a Rubik’s Cube in about three seconds. In those same three seconds, a computer with a virtual Rubik’s Cube could solvethousands of variationsof the puzzle. As the Austrian computer scientist Hans Moravec famously noted in the late 1980s, the tasks that often seem hardest to us humans are child’s play for a machine; the things a child does without thinking are often a struggle for machines. Moravec suggested that the ability to interact with the physical realm evolved so long ago that for us it’s innate, more so than “higher-level” reasoning. The question has been: Can we impart that embodied intelligence to machines?

One of Eka's newer machines with a three-point hand.
Photograph: Tony Luong

Back in October 2018, about four years before launching ChatGPT, OpenAI created Dactyl, a robotic hand that later used AI to solve a Rubik’s Cube. The company took an off-the-shelf hand from Shadow Robot and created a detailed simulation of its joints, servos, motors, and more—a virtual hand holding a virtual cube. Using reinforcement learning, which combines experimentation with positive and negative feedback, OpenAI trained an artificial neural network to manipulate the digital cube over and over. After many thousands of repetitions of wiggling its virtual fingers, Dactyl had figured out how to move the facets of the real thing.

In a press release, OpenAI suggested that Dactyl had achieved “close to human-level dexterity.” In fact, the robot lacked elements of physical intelligence that we take for granted. If the cube began to slip from its grasp, it couldn’t recover. If its hands weren’t placed at a precise angle, it couldn’t manipulate the cube at all. Even under perfect conditions, the only object it could handle was a Rubik’s Cube. And that Rubik’s Cube wasn’t even a standard one—it had sensors that tracked the movement of the squares to feed back to Dactyl.

A few years later, OpenAI gave up on its robotics work to focus on large language models and chatbots. (The company has since restarted work on robotics.) Agrawal, who has remained in touch with a couple members of the Dactyl team, says the project’s simulation approach was considered a dead end because of the so-called sim-to-real gap. But both he and Haarnoja, working at separate labs, remained convinced that they could close that gap by making the sim closer to the real.

At Google DeepMind, Haarnoja was on a project that used virtual reinforcement learning to train small humanoid robots to play soccer. (If this sounds more complicated than training a robotic hand to screw in a light bulb, consider that the soccer field doesn’t roll around beneath the players’ feet.) At MIT, Agrawal was researching how to train a robotic hand to grasp objects from above, not just hold them in its palm. Where Dactyl had simply moved its unfeeling pincers until the sensors in the Rubik’s cube showed its squares shifting to the desired state, Agrawal’s system would need to know what its fingers were doing and how the cube was reacting at any given moment—while accounting for the pull of gravity. When he told someone who used to work on Dactyl about the project, he says, “I got a one-hour lecture from them saying, ‘This will never work.’”

Eka cofounders Pulkit Agrawal (left) and Tuomas Haarnoja at the startup’s office in Cambridge.
Photograph: Tony Luong

Agrawal persevered. “Pulkit is a very creative thinker,” says Ken Goldberg, a professor at UC Berkeley who has known Agrawal since his student days and is currently an adviser to his company. “He's always pushing in a direction that other people aren't.” (I first met him in 2017 at a big AI conference in Long Beach, California. Then a graduate student, he had just published a paper outlining a new way for computers to learn to play video games.)

By late 2021, Agrawal had created a virtual hand capable of manipulating 2,000 objects upside down. Yet simulation was continuing to lose favor among roboticists, and ChatGPT fever was taking hold. If vast amounts of human-written text could yield a remarkably general linguistic intelligence, then perhaps showing robots enough examples of humans using their hands could give themphysical intelligence, too.

Eka uses objects of varying sizes, shapes, and weights to test its robots.
Photograph: Tony Luong

A handful of well-funded startups are pursuing this vision, training what are called vision-language-action (VLA) models. To build one, you show the model videos of, say, humans folding T-shirts, or humans controlling T-shirt-folding robots. The hope is that with enough data, new robotic skills will emerge. Plenty of video is already available online, but a small industry has now emerged to generate more of this data. Companies pay people to spend hours doing routine tasks with their hands while wearing cameras and motion-capture gloves.

Agrawal and Haarnoja, who originally met as graduate students at UC Berkeley, teamed up to pursue a different approach with Eka. Rather than having humans provide training data, the company wants robots to learn how to do things for themselves. They spend thousands of computer hours practicing movements inside simulated worlds and inventing their own solutions. In this sense, Eka’s bot is more like AlphaZero, the Google DeepMind program that learned to play different board games with superhuman skill, and which discovered, for itself, entirely new strategies in games like chess.

Eka’s founders say their robots can transfer learning from a simulator to the real world more reliably than anyone else’s—though they won’t say exactly how. Agrawal seems optimistic that their approach could lead to greater and greater capabilities. “Some people want robots to be human-level,” Agrawal says. “For us the goal is superhuman.”

Engineers look on as a robot screws in a light bulb.
Photograph: Tony Luong

Agrawal and Haarnoja declined to give details of how they train their robots since this is their commercial edge. But they reveal that they have created custom robot grippers that incorporate a sense of touch. Agrawal and Haarnoja also say they have developed a new kind of AI algorithm called a vision-force-action model. This model learns from a simulation that incorporates not just realistic joints and motors but principles of physics like mass and inertia. It learns both how moving affects the pixels on a screen and how the weight and speed of its movement interact with the objects in its grasp.

Perhaps the mostinteresting Eka demo involves chicken nuggets.

The company’s engineers have set up a station where chicken nuggets are strewn across a table. A conveyor belt carries plastic containers along one side. Eka’s robot has to grab the nuggets and place them into the boxes. It does this with not only impressive speed but also human-like improvisation, sometimes placing nuggets carefully, but other times—if a container is moving out of reach—almost tossing them in from a short distance.

An Eka robot practices placing chicken nuggets into take-out containers.
Photograph: Tony Luong

Food handling is an area of work that still relies heavily on humans. Fruit, vegetables, meat, and other foods need to be handled quickly but gently. It is also hard to automate because no two pieces of fruit, vegetables, or chicken nuggets look exactly the same.

Eka’s demos suggest that the company may be onto something big. I found myself mentally comparing their robots to GPT-1, OpenAI’s first large language model, developed four years before ChatGPT. GPT-1 was often incoherent but showed glimmers of general linguistic intelligence.

The robots I saw seem to have a similar kind of nascent physical intelligence. When I watched a video of one reaching for a set of keys in slow motion, I noticed it did something that seemed remarkably human: It touched the tips of its grippers to the table and slid them along the surface before making contact with the keys and securing them between its digits. Eka’s algorithms seem to know instinctively how to recover from a fumble. This kind of thing is difficult for other robots to learn, unless the humans training them deliberately make a wide range of mistakes.

Unlike with any other robot I can think of, it’s almost possible to imagine what the world is like for the robot. Its sensors seem to feel the weight of its arm, the inertia as it sweeps toward the keys and slows down. Once it has the keys in its grasp, it seems to sense the weight of them dangling from its claw.

I don’t know if Eka’s approach really is the route to a ChatGPT-like breakthrough in robotics. Some very smart experts believe that mixing human demonstration with simulation will yield better results than simulation alone. Maybe some combination of the two approaches will ultimately be necessary? But it does seem clear that robots will eventually need to have the kind of tactile, physical intelligence that Eka is working on if they are to obtain humanlike dexterity.

Agrawal tells me that the same general approach should work for finer manipulation. The fiddly dexterity required to build an iPhone, for instance, could be achieved by building different actuators and sensors and practicing the task in simulation.

After spending a few hours at Eka, I decide to stop by the restaurant downstairs. I watch from the counter as the staff prepare food and make coffee. A descendant of the machine upstairs may be able to do these things just as well, if not better. But given how much I enjoy chatting with the people who work there, I think I would pay extra to keep humans around. Unless, that is, my hands get automated away too.

What Say You?Let us know what you think about this article in the comments below. Alternatively, you can submit a letter to the editor at[email protected].

## Comments

Back to top
Triangle

## You Might Also Like

* In your inbox:Upgrade your life withWIRED-tested gear
* Palantir employeeswonder if they’re the bad guys
* Big Story:They builta legendary privacy tool—now they’re sworn enemies
* These AI modelstried to scam me—some of them were scary good
* Event:How to adapt, compete, andwin in the next era of business
Will Knight
 is a senior writer for WIRED, covering artificial intelligence. He writes the 
AI Lab
 newsletter
, a weekly dispatch from beyond the cutting edge of AI—
sign up here
. He was previously a senior editor at MIT Technology Review, where he wrote about fundamental advances in AI and China’s AI ... 
Read More
Senior Writer
* X
Topics
longreads
robots
artificial intelligence
machine learning
This Beanie Is Designed to Read Your Thoughts
California-based startup Sabi is developing a thought-to-text wearable that could usher in the cyborg future.
Emily Mullin
Cursor Launches a New AI Agent Experience to Take On Claude Code and Codex
As Cursor launches the next generation of its product, the AI coding startup has to compete with OpenAI and Anthropic more directly than ever.
Maxwell Zeff
AI Could Democratize One of Tech's Most Valuable Resources
AI is making it easier to design chips and optimize software for different silicon. Some startups envision a revolution in chipmaking.
Will Knight
They Built the ‘Cursor for Hardware.’ Now, Anthropic Wants In
Schematik is a program that aims to help people vibe code for physical devices. Hopefully, it won’t blow anything up.
Boone Ashworth
5 AI Models Tried to Scam Me. Some of Them Were Scary Good
The cyber capabilities of AI models have experts rattled. AI’s social skills may be just as dangerous.
Will Knight
Ace the Ping-Pong Robot Can Whup Your Ass
Ace can read the trajectory of a ball, adjust the racket angle, and respond with strokes that keep the exchange alive with real players.
Marta Musso
Sanctioned Chinese AI Firm SenseTime Releases Image Model Built for Speed
With US restrictions limiting its access to advanced tech, SenseTime is doubling down on open source with a new model optimized to run on Chinese-made chips.
Zeyi Yang
This Startup Wants You to Pay Up to Talk With AI Versions of Human Experts
Onix is launching a “Substack of bots,” where digital twins of health and wellness influencers dispense advice 24/7. And maybe hawk their products.
Steven Levy
Gazing Into Sam Altman’s Orb Now Proves You’re Human on Tinder
Honestly, what’s hotter than a real person?
Maxwell Zeff
AI Agents Are Coming for Your Dating Life
The developers of Pixel Societies are using AI agents to simulate social interactions. It's an attempt optimize the process of choosing new colleagues, friends, and even romantic partners.
Joel Khalili
‘It’s Undignified’: Hundreds of Workers Training Meta’s AI Could Be Laid Off
More than 700 people working for a Meta contractor in Ireland are at risk of losing their jobs, documents show.
Joel Khalili
The 70-Person AI Image Startup Taking on Silicon Valley's Giants
Black Forest Labs has long punched above its weight in the AI image generation space. Its next move? Powering physical AI.
Maxwell Zeff