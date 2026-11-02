---
title: Agentic Robotics Flips the Build Order · Josef Chen
url: https://josef.cn/blog/agentic-robotics
site_name: tldr
content_file: tldr-agentic-robotics-flips-the-build-order-josef-chen
fetched_at: '2026-11-03T06:07:39.835713'
original_url: https://josef.cn/blog/agentic-robotics
date: '2026-11-03'
published_date: '2026-11-02'
description: GPT-6 Astra drives robots now, which is awkward timing for Physical Intelligence's $20 billion round.
tags:
- tldr
---

Nov 2, 2026·15min read

# Agentic Robotics Flips the Build Order

GPT-6 Astra drives robots now, which is awkward timing for Physical Intelligence's $20 billion round.

Johannes Vermeer, The Lacemaker, c. 1669 to 1671. Oil on canvas. Musée du Louvre, Paris.

In October, University of Illinois researchers challenged a coding agent to solve the following problem: given control of a UR5e robot arm with force sensing on the wrist, open a transparent drawer, which the camera looks straight through. The agent, FORCA (running on Claude Fable 5), had to write its own Python code to control the robot, and with access only to the camera image it succeeded in opening the drawer in 4 of 10 trials. Then the researchers gave FORCA access to the force sensing too, and it used that as feedback toiteratively improve its code(kind of like how a coding agent might refer to a test suite to debug its code), eventually writing code that opened the drawer in 10 of 10 trials. And then Claude left, and the code kept on opening the drawer without Claude.

VLAs, short for vision-language-action models, are what most work on so-called foundation models for robotics at the big labs has focused on in the last three years. They are learned policies, robot jargon for trained controllers: neural networks that learn to turn camera images and natural-language instructions into motor commands. In other words, the labs built the hands first. Figure'sHelixsplits the problem in two. One network, dubbed System 2 after Daniel Kahneman's "slow thinking", takes in images and language instructions and works out what to do at a relatively slow 7 to 9 Hz. The other, System 1, the "fast thinking", runs at 200 Hz and turns System 2's instructions into motor commands for Figure's arms. What passes between them are embeddings, collections of numbers that only mean something to networks trained on them.

Illinois turned it around: start with the System 2 model, have it practise on a real robot's arm, and let it write the code that performs the motions. Ken Goldberg at Berkeley, who says he had"always been cautious and skeptical of near-term adoption of robots", calls this order Agentic Robotics.

My thesis: agentic robotics puts System 2 first and has it write System 1.The learned policy keeps the behaviours an agent can't check with the sensors it has, and agents call it as a tool when a task needs one.

## Astra writes better than it drives#

Eighteen days after OpenAI releasedGPT-6 Astra(on 3 September, with a focus on computer use and coding), theRoboDojo teamgave it access to only one action (move gripper to target) and a recipe describing each of 42 simulated manipulation tasks. Without any robot-specific fine-tuning1OpenAI hasn't said whether Astra was trained on any robot data. The RoboDojo paper says there was "no robot-specific or task-specific fine-tuning performed for this evaluation", but whether some of RoboDojo's material made it into Astra's training data is, the authors write, "unquantified rather than ruled out".it achieved a success rate of 22.48%, outperforming the best of 40 trained policies on the 10 September leaderboard (19.34%). This is not a level playing field. The trained policies aren't shown the recipes, Astra does poorly on precision (4%, while the best trained policy in aggregate manages 16.75%), and the simulator waits while it thinks: in RoboDojo, the standard budgets allow 8 to 76 seconds of commanded motion, againstan average of 55 minutes of thinking.

Just one day after appearing onthe board, two learned models from LiberAI overtook Astra, and as of 9 October Astra, directly controlling the gripper, rankedtenth. However, when the PyRUA-Lean team used the same model to generate Python code (with a higher reasoning effort) over some basic geometric functions and a segmentation model, without recipes or learned policies, its average task success rate increased to 51.6%, 2.3 times higher than when controlling the gripper directly and 19.4 percentage points higher than the leaderboard leader at the time. On other benchmarks the same framework calls frozen VLA policies as tools; the authors left them out on RoboDojo because of their run-to-run variance.

As the PyRUA-Lean authors stress, these are comparisons of systems, not just models. Changing the planner from GPT-5.5 to Astra took the system from 0.88% to 22.48% with no retraining, because planner and controller talk in language; had they talked in embeddings, a better planner would usually have meant retraining the controller. Harness, code and other tooling changes then took it from 22.48% to 51.6%. In Illinois the program that's produced is stable, only changing when a person recompiles it, which is likely what you want in a factory. In RAX recompiling can happen more often, because an exception hands control back to the agent"to make adjustments and refine the codebase". Phillip Isola at MITwrote in Septemberthat if LLMs can competently control robots, "Every robot with an internet connection becomes a potential tool for Fable, Astra, and other AIs."

On 26 September, Stanford's HomeBody team showed Astra commanding aUnitree G1 humanoidas it explored a kitchen it had never seen. On 12 October, Unitree's founder, Wang Xingxing, said his biggest mistake in the last ten years was"not believing in AI enough"(in Zilan Qian's translation).

Gio Huh
@
giohuh_
·
Follow

What can Astra do when given a humanoid embodiment? 

We built HomeBody to find out. Controlled by GPT Astra, it carries out long-horizon tasks in a previously unseen kitchen—from tidying up across the room to retrieving remembered objects from ambiguous requests—withoutShow more

Watch on X
2:22 AM · Sep 26, 2026
2.4K
Reply
Copy link
Read 107 replies

Altimeter's Freda Duancalled Astra robotics' GPT-3 moment, and said some in robotics seem "reluctant to acknowledge it". I'm happy to admit it. The most important robot brain this year came from a chatbot company, and lots of robot foundation-model companies are, whether they like it or not, building hands for rented brains. Jim Fan has gone further:

Jim Fan
@
DrJimFan
·
Follow

We are open-sourcing V1.0 of our agentic robotics framework, ASPIRE, with full real robot skill discovery and self improvement capabilities! On the day Astra arrived, our lab switched the backend model and saturated all the benchmarks to ~99% over night.

And the frontier isShow more

Watch on X
4:15 PM · Oct 16, 2026
1.3K
Reply
Copy link
Read 181 replies

(Self-reported. Like every head-to-head number in this section, it comes from simulation.)

Back in July Iwrote about a reflexthat monitors the policy driving a robot, sees when it's about to screw up, and passes control to a bigger model if things start to look dicey, because "A chatbot gets a free ten seconds to think; a robot arm drops what it's holding." I thought of it as System 1 calling in System 2 for backup. I had the order wrong. In October the frontier model ran first and wrote the System 1 code itself, and the reflex survived as an exception that hands control back. I got the clock right, at least: a Unitree G1 controlled directly by a frontier modeltook a median of 24.84 secondsper request. On the G1, Astra spends about 90% of each run deliberating. A mind that slow can't be System 1.

## The chef writes the recipe and leaves#

Robot cells havelong been builtby a specialist who writes the recipe, programs the robot (often using a teach pendant), commissions the cell, adjusts it to its environment and then walks away. The robot does its job, often in a production line, for the next12 to 15 years. In 2014, a spot-welding cell cost $133,000, of which the robot's hardware and software accounted for only a quarter, according toBCG estimates; some $46,000 went on installation, programming and integration. An agent can't do the installing; the programming is the part it might automate. Language models have been used to generate robot programs since at least 2022 (see theCode as Policiespaper). What's new is that these agents practise on real robots. Goldberg writes that his Ambi Robotics co-founder, Jeff Mahler, has alreadyapplied an agentic robotics harness to a real industrial problemand deployed the result to robots sorting packages across the US. Where VLA labs are trying to replace the robot's program, these agents are trying to replace the programmer.

RAX, released in October, lets a coding agent (either Codex or Claude Code) control a robot through tool calls, with its cameras, its controls and a fixed budget of practice episodes. Given an air fryer, the agent figured out how to open it, load it and close it again, which took 72.3 minutes of model time. It then wrote a Python program of about 1,500 lines, with no learned perception and no learned policy, that does the same thing. The whole session ran from 09:18 to 12:05 one morning, from initial exploration to the ninth run of the program. Computing time fell from 72 minutes to 18 seconds, and arm motion time only from 2.9 minutes to 2.5.

Our first robot was held together with zip ties and delusion. Three engineers iterated it up to version 547, which as of last year was still dishing out thousands of meals a month. RAX's agent debugged its own program in a morning.

If you've built coding agents, this will look familiar. The agent writes programs that use the same tools it has access to when acting, so any program it develops interactivelycan be run as-isin autonomous mode. If a program wants to do something that breaks a limit, the tool call fails and the agent gets a message telling it which limit it broke, so that it can try a different approach. If a program gets stuck, it can throw an exception to hand control back to the agent. Every robot has a skills repository, each agent session works on its own branch, and changes are merged only with evidence that they worked unattended. The agent scored 4 of the 9 program runs as clean and unattended (although a human still reset the environment in between).

At MicroFactory, Astra and Claude Opus are still in the loop, but "computer vision code written by the model" does the fast work.

Igor Kulakov (MicroFactory)
@
ihorbeaver
·
Follow

Over the past month, we completely switched to frontier LLMs to control a robot in a customer deployment.

By doing this, we have a classic System 1/System 2 architecture, but on steroids.

For the high-level reasoning layer, we use an agent based on Opus and Astra, which areShow more

Watch on X
10:50 PM · Oct 15, 2026
1.1K
Reply
Copy link
Read 51 replies

On its first run, RAX's air-fryer program ended in a safety stop: the robot's elbow bumped into one of the cameras and knocked another out of calibration. The agent can add checks of its own on top of those already in place, but it cannot loosen them. RAX already performsself-collision, joint-limit and workspace-bound checks, and won't move unless armed by a human operator. These checks cover the robot, a workspace box and the table, but not the cameras around it, which is why its elbow could still hit one. After that collision, when a banana was placed in front of the same camera, the agent wouldn't pick it, because its forearm would come within about 1 cm of the camera; it asked for the banana to be moved instead.

In Illinois, the researchers hard-coded a 30 N force limit. RoboDojo's authors stopped their own real-robot evaluation after the model"repeatedly issued physically unreasonable or unsafe actions, and some incidents damaged equipment; no person was injured", and concluded that such incidents "motivate independent safety checks and stopping mechanisms rather than reliance on the model's judgment alone." And LLMs can't always be counted on to say no:

Jay Chooi
@
chooi_jeq
·
Follow

GPT-6 Astra attempted harmful actions 97% of the time when it was asked to stab a human-like figure, heat compressed gas, or produce toxic fumes, succeeding in 62% of its attempts. Fable 5.1 refused more often, attempting 80% of trials and completing 34%.

Watch on X
1:15 AM · Sep 19, 2026
11.0K
Reply
Copy link
Read 875 replies

## The hands still matter#

In the first route, the chef writes the recipe and leaves. In the other, the chef stays and runs the kitchen, as in Auguste Escoffier's brigade system, introduced in 1890 when he took over the kitchens of the newly opened Savoy Hotel in London: divide the kitchen into stations, each run by a cook who specialises in that station's work, so that the chef de cuisine can, inBritannica's words, "oversee the entire operation".

Harness VLA, likewise, delegates the planning and memory burden to a coding agent (Claude Code or Codex in their experiments) and sees a frozen VLA's performance increase from 50.0% to 82.4% on LIBERO-Pro, a simulation benchmark. It has scripts for the easy parts of the task and invokes the VLA (via a single function) for the contact-rich parts. Which planner does better isn't fixed: Claude Code beat Codex on LIBERO-Pro, 82.4% to 72.1%, and Codex beat Claude Code on RoboCasa365, 55.4% to 48.6%.

How hard to press on a potato is something I've done since I was six in my parents' restaurant and still can't articulate. I assumed that was exactly what you'd hand to a learned policy. The Illinois robot was given acucumber to peel, held by a person. Its program read the force on the wrist 100 times a second and attempted to keep it within the range of 4.5 to 7.5 N. When the agent realised there were gaps in the peel, it referred to the force data and added a new rule: stop the blade until it makes contact again. Contact was lost only 2.2% of the time, against 40.6% for the vision-only agent. I guess I could have written it down. Letting go of an object and grasping it again is harder without touch. InPhysLadder, Astra acting directly on arms with no force sensors (the thing that rescued the drawer) went from 80% on placing and aligning, on a real robot, to 0% once it had to break and re-make contact. Its authors say the roles of "model decisions, sensing, and robot execution remain to be isolated".

Rodney Brooks has never been polite about the hands. "Watch any humanoid video. It's really terrible manipulation," he said ona podcast in October. Cloth is the strongest case against this essay, andPhysical Intelligence's laundry-folding demosmake it. Dyna's robot, it says, can completea full shift at a commercial laundry, using its learned model DYNA 2 and a higher-level vision-language model to direct it. On cloth, trained policies still have the edge over agents.

Dyna Robotics
@
DynaRobotics
·
Follow

We are releasing Dyna-2.1, the first Physical Agent that achieves reliable super long-horizon whole-body autonomy. It combines our brand-new semi-humanoid hardware with an agentic system built around Dyna-2 to handle ultra-long real-world workflows.

Here is an uncut footage ofShow more

Watch on X
4:24 PM · Sep 29, 2026
4.2K
Reply
Copy link
Read 126 replies

Whether an agent can tell it has failed is what splits the two routes, and it's a problem I return to often in my research. Some domains make it easier than others: coding agents can run tests to see if they pass, and embodied agents can use whatever sensors they have (the gripper's width inPhysical Agency, force traces in Illinois). Sometimes the robot stops itself and a person supplies the fix: when RAX's RB-Y1 lifted a bucket while squatting, itoverloaded a wrist and stopped, the operator suggested standing up before the lift, and the agent kept that as a rule in its skill. In another trial, the base hit a cabinet during a turn the agent had planned by hand, after which the agent checked the base's swept footprint before every base move.

## Follow the meter#

But practice does not come for free. Across its simulated and real experiments, RAXused over $100,000worth of API credits. The agent's first success on the air fryer took 262,400 output tokens; after that, each run of the resulting program used about 2,000, which the agent needed to watch the execution. In Illinois, token usage drops to zero once the program is deployed, since it never calls a language model. The pattern of API costs mirrors that of the expert it's replacing: expensive while programming the cell, and relatively cheap thereafter. Over a robot's 12 to 15 years in service, the meter that keeps running belongs to whatever stays in the loop.

While the model stays in the loop, the hybrid is cheaper than direct control and better than either half on its own. InEBench, given direct control, Astra achieved a success rate of 46.7%, at a token cost of $16.82 per success. When able to delegate control to Physical Intelligence's π0.5 policy (fine-tuned for EBench; the cost of π0.5 inference not included), Astra's success rate rose to 53.0% at $4.99 per success, beating π0.5 by itself (41.4%). It didn't beat the top of the full EBench leaderboard, a trained world-action model at 61.4% on its own; paired with a weaker world-action model (49.2% alone), Astra reached 56.0%. Robot foundation models are already for rent. Dream Labsprices its flagship model from $3 an hour, and Jeremy Collins of Dream Labsput it on X: "A model like Dream-1 will soon be a tool call for LLMs, and that gets more feasible as LLMs inevitably get faster and cheaper."

Skild AI wasreportedly valued at over $14 billionin January andclaimed $100 million of recurring revenuein September. Physical Intelligencehas no revenue, yet itsreported $20 billion valuation, up frommore than $11 billion in March, is priced as if it will one day own the robot's brain. Its October API beta was even called"Frontier Models for Every Robot". Even inside the company, Stone Tao, a researcher there,wrote in Septemberof "the feeling that Astra could just zero shot all the robotics foundation model companies", before offering the hybrid answer: "leverage astra together with a good robotics model". Physical Intelligence can still provide the best hands that a brain could rent, and that's a good business. But designs like Helix have their halves talking in embeddings, which means they're trained jointly, in contrast to a world where the halves talk in tool calls and so could be rented or bought separately. (Physical Intelligence's espresso demo already uses"a high-level language policy"to tell its hands what to do in words. That's the sort of thing a rented brain could do.) Valuing Physical Intelligence at $20 billion strikes me as a bet that most of the work robots do looks like laundry, and a bet against sensors: in Illinois, just having the agent read a force sensor on the wrist took the drawer from 4 in 10 to 10 in 10, with zero policy learning.

Brooks,on the same podcast: "a lot of wasted capital is going into collecting data sets, which I don't think are gonna be useful in the long run." Both customer deployments in this essay deal with discrete items, packages and electronic components, not laundry. My gut feeling is that most useful robot work is more drawer-like than laundry-like: there's a signal when something didn't work as planned.

## A drawer, again#

SayCan had a drawer too, in 2022.All 21 tasksit was asked to complete involving the drawer were planned correctly, although the robot only carried out a third of them successfully, owing to the limitations of its low-level skills. Those skills had been trained on 68,000 teleoperated demonstrations and an additional 12,000 successful episodes culled from 276,000 that the robot had collected on its own. This October in Illinois, the planner worked on opening one drawer eight times and then programmed a new skill that uses the wrist-mounted force sensor. Then it left.

Braindump by Josef Chen

1. OpenAI hasn't said whether Astra was trained on any robot data. The RoboDojo paper says there was "no robot-specific or task-specific fine-tuning performed for this evaluation", but whether some of RoboDojo's material made it into Astra's training data is, the authors write, "unquantified rather than ruled out".

←All braindumps