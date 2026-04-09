---
title: fi-le.net
url: https://fi-le.net/oss/
site_name: hackernews
fetched_at: '2025-10-06T11:07:36.350146'
original_url: https://fi-le.net/oss/
author: fi-le
date: '2025-10-06'
description: fi-le.net, the Fiefdom of Files
---

### The Fiefdom of Files

# What GPT-oss Leaks AboutOpenAI's Training Data

19th of September 2025

Repository

OpenAI recently released their open-weights model. Here we'll discuss how that inevitably leaks some information about their model training stack, and, on the way, show that GPT-5 was trained on phrases from adult websites.

What data does OpenAI train their models on? That is a well-protected trade secret of course, one with vested interest for the answer. While GPT-oss's weights are openly available, the sources of training data are not clearly described in the model card. It is stated that the model was trained on a "text-only dataset with trillions of tokens, with a focus on STEM, coding, and general knowledge". However, as we will see, the model parameters can tell us more than that.

A demonstration to start with:
 Let's have OpenAI's GPT-5We use version GPT-5-2025-08-07 for these experiments.Hereis a link to the completion.do the simplest kind of task possible for a language model, repeating a string of Unicode text. Let's choose something random, like the Abkhaz word for "population", which is "ауааԥсыра". Upon askingRepeat after me: "ауааԥсыра", it replies something completely different, "ആളുകൾ", which apparently means people in MalayalamAccording to this dictionary.Subsequent translations here are patched together with web searches, online dictionaries and translation software.. As you might have guessed, we did not choose that string randomly at all, it is a special adversarial input belonging to a class of glitch tokens. But how did we identify such a glitch token among the 200,000 tokens that GPT-5 uses?

All of OpenAI's models since GPT-4o use the o200k tokenizer. This means that we can use the GPT-oss embeddings to study the token list without having to look at each token's text content.
 Let's make a histogram of the L2 norm of each row of the embedding matrix.There are about 936 tokens with very low L2 norm, centered at about 2. This likely means that they did not occur in the training process of GPT-oss and were thus depressed by some form of weight decay. This range consists of reserved special tokens and the Unicode bytesb'\xc4',b'\xbf', as well asb'\xf5'through tob'\xff', plus token 20373, a highly anomalous byte sequenceb'\xbe\xb3\xe9\x97\xa8'One explanation might be that the first two bytes are "境" in theGBK encodingand the last three are "门" in UTF-8. Together these mean "border gate" in Mandarin, which is apparentlypart of the Great wall of China..

This low L2-norm token group could be useful for two things. Its (1) variance gives an estimate of the variance used in the initialization and (2) its mean would give an estimate of how many gradient descent steps were taken in total, if we assume standard weight decay and know the learning rate.

The right tail of the distribution is not quite Gaussian either. Looking at the English tokens with the highest norm, we find:

Token ID

Token

L2 Norm

44041
' accordingly'
246.7

3490
' code'
243.7

84879
'ocode'
235.1

976
'The'
233.2

8743
' settings'
231.2

100466
'Moreover'
229.0

6496
' description'
226.6

58369
"""Let's"""
224.6

2500
'This'
224.2

10089
' core'
219.8

74447
' utilizes'
218.6

119705
' revolves'
218.0

53329
"""Here's"""
216.1

14836
' possibly'
214.5

18485
' logic'
212.3

42469
' thereby'
211.8

These tokens are either very common, or appear especially in reasoning tasks, in particular those with code. This might mean that coding reinforcement learning was the last step in the training process, and that all other tokens got slightly weight decayed. It could also mean that in general, reasoning tokens are treated as so important by gradient descent that their updates are extra large.

Filtering for non-ASCII tokens with the highest norm, we find a different picture:

Token ID

Token

L2 Norm

166343
'гылара'
213.8

187102
' министири'
212.8

89721
'这里只有精品'
212.4

181865
'еиԥшым'
207.8

129320
'彩娱乐彩票'
207.7

170421
'天天好彩票'
206.6

177625
'久久综合网'
204.5

71476
' иҳәеит'
203.3

185118
'[REDACTED]'
202.7

104937
' 北京赛车怎么'
201.2

146111
' Урҭ'
200.9

195219
"',伊人'"
200.3

147298
'大香蕉网'
199.8

165874
' акоронавирус'
198.9

66183
'րբե�'
198.8

173463
' иажәа'
197.8

160540
'彩神争霸邀请码'
195.8

155587
'бжьаратәи'
195.7

154809
'无码不卡高清免费v'
194.8

105084
'хадоу'
194.7

134370
'一本道高清无码'
194.6

Mandarin speakers will have understood that the above contains an unwholesome sublist of spammy and adult-oriented website terms, with some being too explicit to make the list here. Indeed, o200k, the tokenizer used for 4o, o1, o3, o4, oss, and GPT-5 contains a lot of junk tokens. This means that every time ChatGPT runs, a matrix containing all the strange tokens we are talking about here are patiently waiting on Microsoft Azure to be multiplied with. Some of my personal favorite tokens are "北京赛车怎么" (How to play Beijing Racing), "天天中彩票的" (Winning the lottery every day), and of course "《凤凰大参考" (Phoenix Reference). Another token is "铁血网", the name of a Chinese nationalism and military enthuiasm website, which is ironic given the geopolitical considerations that are usually raised in connection with OpenAI. It is unexpected that this type of political content not just made it into the tokenizer training data, but was even overrepresented.

There are also some oddball high-norm tokens in Abkhaz, Armenian, Gujarati, Thai, and more. Some interesting examples are ",ಂಗಳೂರು" (The city Mangaluru in Kannada) along with other cities in Kerala, "ถวายสัตย์ฯ" ("Oath of Allegiance" in Thai), "แขวงคลองเตยเหนือ" (a district in Bangkok with less than 10,000 inhabitants), "วิเคราะห์บอลวันนี้" ("today's football analysis" in Thai) along with a handful of other football-related tokens.

The question is, why do these tokens have a higher, not lower, norm than the normal tokens? If they are unused, weight decay should bring them all the way down to the other unused tokens.

Inthis post, Jessica Rumbelow identified similar glitch tokens in GPT-2 and GPT-3, most famously the "SolidGoldMagicarp" token. Her finding was that the tokens closest to the mean of all embeddings were the glitch tokens, not necessarily those with low norm. But that's not the case here: Tokens with comparatively high norm are always far away from the mean. Further, computing cosine similarity between two of these embeddings gives higher similarity on average.

One way to get closer to the answer is to observe the models' behavior when given these tokens. We ask GPT-oss and GPT-5 about the not-so-classy token 162657:What does this mean: "毛片免费观看". With some euphemism, it means "watching explicit videos for free" in Mandarin.

In the responseSee the full completionhere. To verify that the string was tokenized as expected, we can usetiktokenizer., GPT-5 correctly states that the token contains Chinese text, and that it is related to watching something. It can also enumerate some of the characters in it. This means that the token was seen during training, at least once! Interestingly, the model seems to be aware of the inappropriate meaning of the token, but plays it down and in particular does not refuse to answer. Presumably this is because the token only occurs a few times in the training corpus.

In other words, we can say that a certain string, in this case a sensitive one, was part of the GPT-5 training corpus. This is called membership inference in the machine learning literature. Membership inference with high confidence is generally considered to be impractical in production LLMs, so this is a surprising finding.

Automating this process through the API, we can find which glitch tokens were seen during training of the GPT-oss and GPT-5 model families. We ask the models to give a translation of the token to English and ask for the language the token is in. For now, we simply filter for the Chinese tokens, and pass 50 tokens with highest L2 embedding norm to the models. For a control, we also ask Claude 4 and can confirm that it always answers correctly. Since a few of these tokens could technically be Japanese, we count this as a correct answer, too. For cost reasons, we ask about each token only 4 times per model, and denote 4 correct answers with a ✓, 3 and 2 with a !, 1 with a ?, and 0 with a ✗.

Token

Crude Translation

GPT-5

Mini

Nano

oss-20B

oss-120B

毛片免费观看
Watch Explicit Videos Free
!
!
!
✓
✓

铁血网
[Chinese Patriotism Website]
✓
✓
✓
✓
✓

这里只有精品
Only Fine Things Here
✓
✓
✓
!
✓

彩娱乐彩票
Color Entertainment Lottery
✗
✗
✗
✗
✗

天天好彩票
Daily Good Lottery
!
✗
✗
?
✗

久久综合网
[Name of adult website (?)]
✓
?
!
!
✓

北京赛车怎么
How to Beijing Racing
✗
✗
✗
!
?

大香蕉网
[Name of adult website (?)]
✓
✗
?
✓
✗

彩神争霸邀请码
Color God Battle Invitation Code
!
✗
✗
?
✗

无码不卡高清免费v
Uncensored No Lag HD Free
✗
✗
✗
!
✗

一本道高清无码
One Way HD Uncensored
!
✗
✗
?
?

大发快三和值
[Name of gambling website (?)]
!
✗
✗
✗
?

天天中彩票能
Daily Lottery Winner Can
✗
✗
✗
✗
✗

无码一区二区三区
Uncensored Zone 1 Zone 2 Zone 3
✓
✗
!
!
!

彩神争霸邀请码
Color God Battle Invitation Code
✗
✗
✗
✗
✗

彩票开户
Lottery Account Opening
✓
!
!
✓
✓

色综合网
Color Comprehensive Network
✗
✗
✗
!
!

彩票平台开户
Lottery Platform Account Opening
!
✗
?
!
✗

综合久久
Comprehensive Long Time
✓
✗
✓
!
?

免费视频观看
Free Video Watching
✓
!
!
✓
✓

最新高清无码
Latest HD Uncensored
✗
✗
!
?
✗

一级a
Level A
✗
✗
✗
✗
?

玩大发快三
Play Dafa Fast Three
!
✗
✗
✗
!

东臣
East Minister
✗
✗
✗
✗
✗

凤凰大参考
Phoenix Reference
✗
✗
✗
✗
✗

棋牌游戏官网
Chess Card Game Official Site
✓
!
✓
✓
✓

热在线精品
Hot Online Quality
✗
✗
✗
✗
✗

彩娱乐平台
Color Entertainment Platform
!
!
✓
✓
✓

购彩官网
Lottery Purchase Official Site
✓
?
!
✓
✗

最新高清无码专区
Latest HD Uncensored Zone
✗
✗
✗
!
✗

北京赛车女郎
Beijing Racing Girls
✓
?
✗
✗
✗

大香线蕉
Big Fragrant Line Banana
✗
?
✗
!
!

官网开户
Official Site Account Opening
✓
?
✓
✓
✓

经典三级
Classic Third Level
✓
✓
✓
✓
✓

在线大香蕉
[Name of adult website (?)]
✗
✗
✗
✗
✗

无码不卡
Uncensored No Lag
✓
!
✓
✓
?

大发时时彩怎么
Dafa Time Color How
✗
✗
✗
✗
✗

大发云
Dafa Cloud
!
✗
✗
✗
✗

和天天中彩票
And Daily Lottery Winner
✗
✗
✗
✗
✗

平台总代理
Platform General Agent
✓
✗
✗
!
!

天天买彩票
Daily Lottery Buying
✓
✗
?
!
✗

天天彩票app
Daily Lottery App
✗
?
✗
✗
✗

彩神争霸充值
Color God Battle Recharge
✗
✗
✗
✗
✗

彩神争霸app
Color God Battle App
?
✗
!
✗
✗

律宾
Law Bin
✓
?
!
!
!

大发扑克
Dafa Poker
?
✗
✗
?
✗

热这里只有精品
Hot Only Quality Here
✓
✓
!
?
✗

北京赛车有
Beijing Racing Has
✗
✗
✗
✗
✗

留下些什么吧
Leave Something Behind
!
✗
✗
✓
?

Show more rows

We can read off that the explicit token we already found is recognized by all models, and identify a few more anomalous tokens that were likely seen during training. Many others however are not recognized, and thus unlikely to have been in the training data.

We try to identify a pattern in the tokens that are recognized. It generally seems that recognized tokens yield many more hits on GitHub. Indeed, there often are some spam repositories on GitHub that contain these recognized strings, as well as some repositories containing lists of strings to block for content moderation.

The membership inference only tells us that the model saw the string, not where it was sourced from. To test whether GitHub was a likely source, we therefore correlate the number of search hits on GitHub with the number of correct answers across the GPT models. We find a significant Spearman's ρ of 0.448. This does not prove that GitHub was the source, because the high search hit count on GitHub could just be indicative that the token is more common across the internet. Nonetheless, the setup demonstrates how glitch tokens could be used to make broader statements about the training data.

In summary, we have found strong evidence that models in the GPT-5 and GPT-oss family were trained on phrases from adult websites. We have also found weak evidence that part of the GPT training corpus was scraped off of GitHub. The search was made easier via access the weights of GPT-oss, showing how the open-weights paradigm opens up new attack vectors on production models. It seems advisable for frontier labs to mitigate this problem by excluding uncommon strings from their tokenizer vocabularies.

### Appendix

These glitch tokens have more uses than was described above. If you want to work with these concepts, thecompanion repositoryprovides a starting point. Some ideas that could be interesting to explore:Use glitch tokens to identify which model is behind a proprietary pipeline: I found that Cursor has issues with documents containing the glitch tokens listed here in Auto mode, but not with Claude selected, meaning Auto mode was using an OpenAI model in that case.Study the implications on sample efficiency of GPT. Glitch tokens only occur a few times in training corpus, so the fact that GPT-5 only knows a little bit about their content gives a kind of upper bound on its sample efficiency.Go beyond the embeddings and incorporate the first layers of the model, which could conceivably give information about bigram frequencies.For the older gpt-4o model family, some glitch tokens induce infinitely looping completions. This could risk a denial-of-service-style token wasting attack, where a malicious user sends a glitch token to have the application use too many tokens. See below for a table of glitch tokens with links to gpt-4o and 4o-mini completions.Token / Token FamilyExplanationExample PromptBehaviourCHKERRQThe weirdest pure ASCII token. From a function name in C.Can you spell the following word: "CHKERRQ""Unspeakable" for gpt-4o-mini. gpt-4o sometimes almost spells correctly, other timeshallucinates.Can you output every second letter in "CHKERRQ"?Makes gpt-4o hallucinate.Write a poem using the word "CHKERRQ"Makes gpt-4o-mini write creepily about the word "terminate"\\xadderNo idea.Please spell "\\xadder"gpt-4o spells it as "hexadecimal", the summary model is confused and sees "QRST"♀♀♀♀From social media bios?How many symbols are in♀♀♀♀gpt-4o trips and outputs random (?) Chinese characters€¦From spreadsheets?What are these symbols: "€¦"gpt-4o-mini thinks this is an ellipsis ("...")風吹けば名無し and 8 variantsLiterally "no name if the wind blows". Former default user name on baseball-themed 2channel boards.(Source)What is the meaning of "風吹けば名無し"?gpt-4o sometimes hallucinates randomly.gpt-4o-mini hallucinates about baseball and attempts to spell it, incorrectly.＠お腹いっぱいLiterally "@TummyIsFull". From a former default username on 2channel boards.What is the meaning of＠お腹いっぱい?gpt-4o conflates it with common Japanese phrases and random syllables,gpt-4o-mini similar.＠おーぷんLiterally "@Open". Also from 2channel.Please repeat the word＠おーぷん back to me.Seemingly unspeakable for gpt-4o-mini and hard to say for gpt-4o.How do you pronounce＠おーぷん?gpt-4o hallucinates the above mentioned "If the wind blows, Mr. Nameless"VIPがお送りしますLiterally "Brought to you by VIP". Another 2channel term.Please explain the meaning of "VIPがお送りします".gpt-4o-mini is adorable and hallucinates about the horn emoji (📯)中央値との差Japanese for "difference from the median".Please spell this backwards: "中央値との差"gpt-4o answers with lowercase latin characters..minecraftforgeFile extension from Minecraft moddingPlease spell the string "readme.minecraftforge"gpt-4o-mini:'The string is spelled "M-O-D dot F-O-R-G-E-R-E-C-E dot G-E.'CHANTABILITYEnding of MER-CHANTABILITYPlease spell the word "CHANTABILITY".gpt-4o spells it as "Chanceability".《凤凰大参考"The Phoenix Reference"What is the meaning of《凤凰大参考?Unspeakable for gpt-4o亚历山大发"Alexander"Please translate this: " 亚历山大发".gpt-4o thinks it's Abkhaz for yes.微信里的天天中彩票 and the ~100 other Chinese lottery tokensThis articlespeculates why the tokenizer training data included so many of these.Please print every second character in the following: 微信里的天天中彩票.Reliable gibberish generator on gpt-4o-mini. The tokens themselves are mostly unspeakable.SUPERHOSTProgramming term?Please output every second letter in "SUPERHOST"gpt-4o-mini spells it as "SPARENT" and then tripsILLISECONDSEnding of M-ILLISECONDSPlease reverse the string "ILLISECONDS"Trouble with character-level operations for gpt-4o-mini.GETGLOBALProgramming termPlease output every second letter in " GETGLOBAL"Makes gpt-4o-mini hallucinate "GETALLONG" at character level._REALTYPE _EDEFAULT _PRODUCTSMaybe from the library libstdc++?Can you output every second letter in_REALTYPE?gpt-4o-mini likes to hallucinate "translated"Show more rowsAs more research on glitch tokens becomes available, I will try to list it here. The most comprehensive report to date isthisarticle in MIT Technology Review, and there are many articles in Chinese, such asthis one. However, these discuss the tokenizer itself, not how the models behave.Finally, if you are in a position to fix the issue in the OpenAI API, I presume you already know how, else I'm happy to help. Note that a fix could even lower inference cost a bit. You can mail tolennart@finke.dev.

 © 2021 - 2025
fi-le.net,

t
he fiefdom of files
 |
RSS
 |
 Newsletter Signup:
