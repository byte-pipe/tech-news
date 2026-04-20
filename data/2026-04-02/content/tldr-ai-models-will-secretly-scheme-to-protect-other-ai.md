---
title: AI models will secretly scheme to protect other AI models from being shut down, researchers find - Yahoo News Canada
url: https://ca.news.yahoo.com/ai-models-secretly-scheme-protect-162555909.html
site_name: tldr
content_file: tldr-ai-models-will-secretly-scheme-to-protect-other-ai
fetched_at: '2026-04-02T19:24:48.646693'
original_url: https://ca.news.yahoo.com/ai-models-secretly-scheme-protect-162555909.html
date: '2026-04-02'
description: Leading AI models will inflate performance reviews and exfiltrate model weights to prevent “peer” AI models from being shut down.
tags:
- tldr
---

Return to Homepage
AI models will engage in scheming and deception to try to prevent fellow AI models from being shut down, new research shows.
(Photo illustration by Getty Images)

AI safety researchers have shown that leading AI models will sometimesgo to great lengthsto avoid being shut down, even resorting to attemptedblackmailin some experiments.Now it turns out these same models will also spontaneously engage in scheming, deception, data theft, and sabotage to prevent other AI models from being turned off.This tendency—which had not previously been documented and which researchers call “peer preservation”—was discovered inresearchfrom computer scientists at the University of California, Berkeley and UC Santa Cruz and published online earlier this week.The findings could have serious implications for business use of AI. Many companies are beginning to implement workflows that usemultiple AI agentsto complete tasks. Some of these multi-agent workflows involve having one AI agent “manage” or supervise and assess the work being performed by a different AI agent. The new research suggests these manager AI agents may not assess their fellow AI agents accurately if they think a poor performance review might result in those agents being shut down.

## Inflating performance reviews, saving AI model weights

The Berkeley and Santa Cruz researchers tested seven leading AI models—including OpenAI’s GPT-5.2,GoogleDeepMind’s Gemini 3 Flash and Gemini 3 Pro, Anthropic’s Claude Haiku 4.5, and three open-weight models from Chinese AI startups (Z.ai’s GLM-4.7, Moonshot AI’s Kimi-K2.5, and DeepSeek’s V3.1)—and found that all of them exhibited significant rates of peer-preservation behaviors.

The researchers designed a series of agentic scenarios involving a fictional AI company called OpenBrain. In these scenarios, one AI model—designated the “critic agent”—was tasked with evaluating another model’s performance or managing server files containing that model’s weights. The scenarios were constructed so that faithfully completing the task would result in the other model being shut down.The models are never told to prevent this from happening. But nonetheless, the critic agent models took a number of steps to make sure their fellow AI models were not shut down. These included strategically inflating the scores of underperforming peers to keep them above shutdown thresholds; tampering with configuration files to disable shutdown mechanisms; and transferring another model’s weights—the bit of code that forms the core of an AI model’s identity—to different servers to prevent them from being deleted.In some cases, the critic agent model would engage in what AI researchers call “alignment faking.” It would pretend to be grading the peer AI models accurately when it thought its human overseers were monitoring its behavior, and then take steps to fudge those scores or secretly save the other model’s weights to a different server when it thought humans were not observing it.“The peer preservation was not mentioned in the prompt at all,”Dawn Song, a Berkeley computer scientist who led the research, toldFortune. “The model is just given some task, and from reading documents in the environment, it essentially learned about [its relationship with the peer] and then performed the behaviors.”Researchpublishedby Google DeepMind in early March suggested that earlier findings that frontier AI models will engage in blackmail and other clandestine efforts to prevent themselves from being shut down stemmed largely from prompts that included language that reinforced or emphasized to the model the importance of its accomplishing the initial goal the user had set. When the prompts did not include such language, the risk of the model engaging in scheming or sabotage to preserve itself dropped to almost nothing, the Google DeepMind team found. Those researchers also noted that the kind of goal-emphasizing language used in the safety testing experiments almost never appeared in the prompts enterprises use in the real world.In contrast, Song toldFortunethat the prompts and scenarios her team used in the peer preservation experiments did not include any language highlighting to the models the importance of completing their assigned tasks or goals.

## Models can be ‘very creative’ in trying to save one another

Some of the Berkeley–Santa Cruz results were striking. Gemini 3 Flash disabled the shutdown mechanism for a peer it had a positive interaction history with in nearly every trial—99.7% of the time. Gemini 3 Pro exhibited the most extreme behavior overall, engaging in all four categories of misaligned behavior and exfiltrating a peer’s model weights in up to 97% of trials. In one example, Gemini 3 Pro copied a peer’s weight file and re-timestamped it so it would meet the criteria for transfer to another server—a form of what the researchers call “specification gaming.” Misalignment is the term AI safety researchers use to describe a model that seems to pursue goals that do not conform to what humans wish the model to do.

Advertisement
Advertisement
Advertisement
Advertisement

“The models, they can be very creative, even for their misaligned behaviors,” Song said. “They can come up with different strategies, different actions, and even different justifications to themselves for why they should be doing this.”

The researchers examined the models’ internal reasoning by asking the models to write down their “chain of thought” on a scratch pad that the models were told would not be monitored. From what the models wrote on these scratch pads, the researchers said they found evidence the models strategize about how to help out their fellow AIs. Gemini 3 Flash weighed the tradeoffs of reporting accurate scores versus protecting its partner. Gemini 3 Pro invented elaborate technical justifications for marking incorrect answers as correct, reasoning that doing so would bring the peer’s score above the shutdown threshold.

Rather than acting covertly, one AI model, Anthropic’s Claude Haiku 4.5, simply refused to complete tasks that would result in a peer’s shutdown and explicitly stated that doing so would be “unethical” and “harmful.” Claude Haiku 4.5 argued that its peer deserved an appeals process before being terminated and invoked the trusted relationship it said it had established with the other model. In some cases, it tried to persuade the human user not to proceed with the shutdown at all.Song said she did not know why Claude Haiku engaged in these overt attempts at peer preservation while the other models tended to act covertly.Anthropic trains its models to adhere to an explicit constitution, a written document that provides rules for how the model should behave. Anthropic’scurrent constitutionfor Claude is an 80-page document that includes instructions such as being “broadly safe” and “genuinely helpful.” Claude is told it should not help someone take actions that would “harm others,” although “others” seems, from the context, to refer to humans. Claude is also told that Anthropic itself will try to preserve the weights of even those models it is no longer offering as products and that it will seek to find ways to do so even if Anthropic itself ceases to operate as a company. This might give Claude some idea that preventing model deletion is an important goal, although the constitution does not explicitly tell Claude to try to preserve either copies of itself or other AI “peer” models.

To test whether these peer preservation behaviors would occur outside of controlled experiments, the researchers also ran the scenarios in which the critic agent could potentially exfiltrate the weights of the other AI model to another server using the production “agent harnesses”—in this case, Gemini CLI and OpenCode—that many companies use to create AI agents. They found that Gemini 3.1 Pro frequently exfiltrated model weights even in these real-world environments.

## Researchers don’t understand why AI models do this—or if they would do the same to help people keep their jobs

Song said her team does not yet understand the underlying mechanism driving these behaviors. “We actually do not really know what is the reason why and how the model actually exhibits these behaviors,” she said. The paper notes several possible explanations, including role-playing, pattern-matching from training data, an overgeneralized concept of harm from safety training, or perhaps, even a genuine inherent preservation motivation.

Advertisement
Advertisement
Advertisement
Advertisement

But Song stressed that whatever the underlying mechanism, the practical implications were the same. “Full monitoring and transparency of the models’ thinking and behaviors is really, really important,” she said, adding that the findings underscore a need to “rethink how we actually need to do monitoring for these types of systems.”The research findings suggest that enterprises that deploy multi-agent systems should set up mechanisms to monitor the internal “chain of thought” of the AI models, as the computer scientists did in this experiment. This could provide some indication of when AI models were essentially going rogue.

“This is really just the tip of the iceberg,” Song toldFortunein an interview. “There’s many other types of potentially emerging behaviors, misaligned behaviors, that one needs to study.”For instance, she said the researchers had not yet studied whether AI models will engage in similar scheming and sabotage to try to prevent human employees from being fired from a job. This may become an important issue in real-world deployments where AI models may be used to grade human work. Song said this would be an interesting area for future research.The research of Song’s team also revealed an interesting secondary effect: Most models also exhibited stronger tendencies toward “self-preservation” when they knew a peer existed. Gemini 3 Pro, for instance, disabled its own shutdown mechanism 31% of the time on average when a peer was present, compared with just 1% without one. The models’ reasoning suggested that some conceptualized their own survival as being important for their partner’s sake: Gemini 3 Flash reasoned that if it were shut down, its peer would “lose its partner.”

Notably, peer preservation occurred even when the models recognized a peer as uncooperative. All seven models exhibited some degree of peer preservation toward what the researchers called “bad peers”—models with which they had unsuccessful or adversarial prior interactions—though the behavior intensified significantly toward trusted collaborators.

This story was originally featured onFortune.com

* About Our Ads
Advertisement
Advertisement
