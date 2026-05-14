---
title: 'Old PC vs New AI: Can a 2015 Desktop Actually Run Gemma 4? (2B vs 4B Benchmark) - DEV Community'
url: https://dev.to/gramli/old-pc-vs-new-ai-can-a-2015-desktop-actually-run-gemma-4-2b-vs-4b-benchmark-2eg6
site_name: devto
content_file: devto-old-pc-vs-new-ai-can-a-2015-desktop-actually-run-g
fetched_at: '2026-05-14T19:35:09.206681'
original_url: https://dev.to/gramli/old-pc-vs-new-ai-can-a-2015-desktop-actually-run-gemma-4-2b-vs-4b-benchmark-2eg6
author: Daniel Balcarek
date: '2026-05-14'
description: Running modern AI models locally on older hardware sounds almost impossible. But with smaller models... Tagged with devchallenge, gemmachallenge, gemma, ai.
tags: '#devchallenge, #gemmachallenge, #gemma, #ai'
---

Gemma 4 Challenge: Write about Gemma 4 Submission

Running modern AI models locally on older hardware sounds almost impossible. But with smaller models like Gemma 4 and tools like Ollama, local AI is starting to become surprisingly accessible even on aging machines.

I still have my old desktop computer, bought back in 2015. It is still fast enough for development and even for playing some of my favorite games. At this point, it feels like a member of the family (it’s actually older than my oldest kid).

The only thing it could never really handle was running AI models locally. But now, models seem to be getting much more friendly toward older CPUs, GPUs, and limited RAM, so I finally decided to give it a try with Gemma 4.

I want to create a whole series around Gemma 4. First, I’ll explore how to run Gemma 4 locally on older hardware and benchmark it to see whether it is actually usable and which model variants work best for my specific setup. Then, I want to build something useful where Gemma 4 becomes the core of the application.

So, let’s dive in.

## Table of Contents

* Choosing right Gemma 4 VariationBasic Gemma 4 Knowledge
* Basic Gemma 4 Knowledge
* Installing and Running Gemma 4
* BenchmarksSpeed BenchmarkReasoning BenchmarkKnowledge BenchmarkCode GenerationStructured Output (JSON)Instruction FollowingSystem Metrics
* Speed Benchmark
* Reasoning Benchmark
* Knowledge Benchmark
* Code Generation
* Structured Output (JSON)
* Instruction Following
* System Metrics
* Summary

## Choosing right Gemma 4 Variation

Before choosing the right variant, let’s take a look at my old setup:

Component

Value

CPU

Intel(R) Core(TM) i5-6400 CPU @ 2.70GHz Core

RAM

24 GB

GPU

NVIDIA GeForce GTX 950 2GB VRAM

What does this tell us?

We should stay realistic and focus on the smaller models. Based on some recommendations online:

* Unsloth Gemma 4
* WaveSpeed Gemma 4
* Ollama model page

Gemma 4 Memory Requirements

Model Variant

Minimum RAM/VRAM

Ideal RAM/VRAM

Gemma 4 E2B

4 GB

8 GB

Gemma 4 E4B

6 GB

12 GB

Gemma 4 26B (MoE)

18 GB

24 GB

Gemma 4 31B (Dense)

22 GB

32 GB

With 24 GB of RAM and i5-6400 CPU, I should be able to run E2B and E4B quite comfortably. The 26B model is likely beyond what this system can realistically handle, and the 31B variant is out of reach for this setup.

### Basic Gemma 4 Knowledge

For anyone wondering what terms like E2B or E4B mean:

* The “B” stands for billions of parameters, which describes the size of the model.
* The “E” stands for effective parameters.

These models are designed for edge and local deployment, meaning they are optimized to run efficiently on consumer hardware.

In simple terms, parameters are the internal values the model learns during training. They represent patterns in data that the model uses to generate responses.

You can think of parameters as the model’s capacity to learn and generalize patterns, rather than stored factual knowledge.

Examples:

* 2B → ~2 billion parameters
* 4B → ~4 billion parameters
* 26B → ~26 billion parameters

## Installing and Running Gemma 4

First, we need to downloadOllama, which will act as our local "AI server". Ollama handles model downloading, hardware optimization, and model management, so the only thing we really need to focus on is prompting.

It is probably the easiest way to bridge the gap between "having a computer" and "having a private local ChatGPT".

After installing Ollama, we can run the following commands to download and start both Gemma 4 models:

ollama
 
run
 
gemma4:e2b

ollama
 
run
 
gemma4:e4b

Enter fullscreen mode

Exit fullscreen mode

Finished installation of E2B:

ollama run gemma4:e2b
pulling manifest
pulling 4e30e2665218: 100% ▕██████████████████████████████████████████████████████████▏ 7.2 GB
pulling 7339fa418c9a: 100% ▕██████████████████████████████████████████████████████████▏ 11 KB
pulling 56380ca2ab89: 100% ▕██████████████████████████████████████████████████████████▏ 42 B
pulling c6bc3775a3fa: 100% ▕██████████████████████████████████████████████████████████▏ 473 B
verifying sha256 digest
writing manifest
success

Enter fullscreen mode

Exit fullscreen mode

Finished installation of E4B:

PS C:\Users\dbalc>
 
ollama run gemma4:e4b

pulling manifest
pulling 4c27e0f5b5ad: 100% ▕██████████████████████████████████████████████████████████▏ 9.6 GB
pulling 7339fa418c9a: 100% ▕██████████████████████████████████████████████████████████▏ 11 KB
pulling 56380ca2ab89: 100% ▕██████████████████████████████████████████████████████████▏ 42 B
pulling f0988ff50a24: 100% ▕██████████████████████████████████████████████████████████▏ 473 B
verifying sha256 digest
writing manifest
success

Enter fullscreen mode

Exit fullscreen mode

In total, you will need around 6.5 GB for Ollama itself, plus an additional 7.2 GB or 9.6 GB depending on which model you install.

Once the model is downloaded, you can immediately start chatting directly in the terminal:

>>>
 
Send
 
a
 
message
 
(
/
?
 
for
 
help
)

Enter fullscreen mode

Exit fullscreen mode

The next time you run:

ollama
 
run
 
gemma4:e2b

Enter fullscreen mode

Exit fullscreen mode

or

ollama
 
run
 
gemma4:e4b

Enter fullscreen mode

Exit fullscreen mode

Ollama will simply load the already downloaded model, and you can start chatting immediately.

Note:Ollama also allows you to use local models directly inside VS Code Copilot Chat. Simply run:

ollama
 
launch
 
vscode

plaintextThen select your local model in VS Code.More details:Ollama VS Code Integration

## Benchmarks

I want to benchmark these models to see how much CPU, RAM, and GPU resources they actually consume on my old machine across different prompt categories. I also want to compare response quality and generation speed between both models.

To avoid mixing unrelated metrics, I split evaluation into focused benchmark categories.

Each benchmark table is designed to measure one specific aspect of the model’s behavior, instead of trying to evaluate everything at once.

This is important because different aspects of an AI model behave very differently:

* Performance (tokens per second, TPS)tells us how fast the model generates text.
* Reasoning qualitytells us how well the model solves problems and follows logic.
* Structured output reliabilitytells us how consistently the model can follow strict formats like JSON.

Combining these metrics into a single benchmark would produce misleading results. For example, a JSON task might look "slow" just because the output is longer, not because the model is actually slower.

That’s why each table uses carefully designed prompts that match the metric being measured:

* Speed testsuse similar, comparable prompts to fairly measure token generation throughput (tokens per second).
* Reasoning testsuse multi-step logic and problem-solving tasks to evaluate correctness and reasoning quality, not speed.
* Structured output testsenforce strict JSON formatting rules to measure schema adherence and output reliability.
* Code generation testsevaluate correctness, compilability, and code structure in practical C# and .NET scenarios.
* Knowledge testsassess factual recall and basic understanding of geographic or general domain knowledge.
* Instruction following testsmeasure how well models comply with explicit constraints such as word limits and language restrictions.

Each benchmark section includes full model outputs, allowing readers to independently review and verify the results.

System metrics such as CPU and RAM usage were measured during sustained model sessions, while response-specific metrics were recorded individually for each prompt execution.

Before each benchmark, I performed a warm-up phase by sending 4 prompts to the model. This ensures the model is already loaded into memory, allowing Ollama to utilize CPU, RAM, and GPU resources more consistently during testing.

All benchmarks were run using Ollama version0.23.2with default model settings in PowerShell terminal.

### Speed Benchmark

Ollama exposes detailed runtime metrics for each inference request by setting verbose level:

/set verbose

Enter fullscreen mode

Exit fullscreen mode

After each prompt, Ollama outputs detailed runtime metrics such as:

total duration: 1m56.4241285s #This represents full request lifecycle latency.
load duration: 1m6.4841917s #This primarily represents model initialization overhead and is most visible during cold starts or after the model has been unloaded from memory.

# This measures input ingestion speed (how quickly the model encodes and understands the prompt before generating output).
prompt eval count: 19 token(s)
prompt eval duration: 912.2499ms
prompt eval rate: 20.83 tokens/s

# This is the model’s output generation speed, measured in tokens per second. It is the primary indicator of inference performance.
eval count: 357 token(s)
eval duration: 48.4355362s
eval rate: 7.37 tokens/s

Enter fullscreen mode

Exit fullscreen mode

Load duration represents model initialization time, while total duration includes the full request lifecycle.

Prompt evaluation measures input processing speed, and evaluation rate represents token generation throughput.

In this benchmark,evaluation rateis used as the primary performance indicator, while other metrics provide context for system overhead.

For clarity, the benchmark tables rename these metrics slightly:

Prompt Tokens/s = prompt eval rate
Generation Tokens/s = eval rate

Enter fullscreen mode

Exit fullscreen mode

To improve result consistency, I will run each prompt four times for every model and calculate the average values.

#### Prompts

Task

Prompt

REST API explanation

Explain what a REST API is in one paragraph.

Docker summary

Summarize Docker in exactly 3 sentences.

#### 2B Outputs

REST API explanation

Click to expand REST API explanationARESTAPI(RepresentationalStateTransfer)isanarchitecturalstylethatdefinesasetofrulesforhowsoftwarecomponentsshouldcommunicateovertheinternet.Itfunctionsasastandardizedinterface,allowingdifferentapplicationstointeractwitheachotherbyfocusingon**resources**(likeusersorproducts)identifiedbyuniqueURLs.CommunicationbetweentheclientandtheserveristypicallydoneusingstandardHTTPmethods—suchasGET(toretrievedata),POST(tosubmitnewdata),PUT(toupdatedata),andDELETE(toremovedata)—makingthecommunicationefficient,scalable,andstateless.Enter fullscreen modeExit fullscreen mode

Docker summary

Click to expand Docker summaryDockerisaplatformthatusescontainerizationtechnologytopackageapplicationsandalltheirdependenciesintostandardized,isolatedunitscalledcontainers.Thesecontainersensurethatanapplicationrunsconsistentlyandpredictablyacrossanycomputingenvironment,solvingthecommonproblemofenvironmentalincompatibility.Thisportabilitymakesdeployingandscalingapplicationssignificantlyeasierandmoreefficientacrossdevelopmentandproductionsystems.Enter fullscreen modeExit fullscreen mode

#### 4B Outputs

REST API explanation

Click to expand REST API explanationARESTAPI(RepresentationalStateTransferApplicationProgrammingInterface)isessentiallyasetofrulesandguidelinesthatdictateshowtwoseparatepiecesofsoftwarecommunicateandexchangedataovertheinternet,actingasauniversaltranslatorforwebservices.Insteadofneedingcomplex,proprietarymethods,RESTorganizesallinformationintoeasilyidentifiable"resources"(likeauseroraproduct)thatareaddressedviaspecificURLs.Tointeractwiththeseresources,thesystemusesstandardHTTPverbs:`GET`toreaddata,`POST`tocreateit,`PUT`toupdateit,and`DELETE`toremoveit.Becauseitreliesonthesesimple,standardizedmethods—andformatsdatalikeJSONorXML—RESTmakesthewebhighlymodularandscalable,ensuringthatanyclientapplication,regardlessofitsunderlyinglanguage,canreliablyandefficientlyaccessandmanipulatedatafromanyserver.Enter fullscreen modeExit fullscreen mode

Docker summary

Click to expand Docker summaryDockerisaplatformthatenablesdeveloperstocontainerizeapplications,bundlingthecode,runtime,libraries,andalldependenciesintoasingle,portableunitcalledacontainer.Thesecontainerspackageanapplicationintoaconsistent,isolatedenvironment,whicheffectivelysolvesthe"it works on my machine"problembyensuringtheapplicationrunsidenticallyregardlessoftheunderlyingoperatingsystem.Thisportabilitymakesdeploymentimmenselyreliableandefficient,allowingdeveloperstoquicklybuild,test,andscaleapplicationsacrossanymachineorcloudenvironment.Enter fullscreen modeExit fullscreen mode

#### Results

Prompt

Model

Prompt Tokens/s (avg)

Generation Tokens/s (avg)

Total Time (avg)

REST API explanation

2B

473.86

6.91

64.00s

REST API explanation

4B

237.49

5.03

116.55s

Docker summary

2B

877.51

6.46

56.08s

Docker summary

4B

479.66

5.04

65.00s

The 2B model completed both tasks noticeably faster, completing the Docker summary in 56 seconds and the REST API explanation in 64 seconds. The 4B model was slower, taking around 65 seconds for the Docker summary and nearly 2 minutes (116 seconds) for the REST API explanation.

Both the REST API explanation and Docker summary responses from the 2B model were technically correct. However, for non-technical users, the answers might feel too short and somewhat difficult to fully understand without additional context.

The 4B model consistently generated responses more slowly, although the performance gap varied significantly between prompts. For the REST API explanation it took nearly twice as long (116s vs 64s), while for the Docker summary the difference was much smaller (65s vs 56s). Output token generation also lagged behind, averaging around 5 TPS compared to the 2B's ~6.7 TPS. Despite the lower throughput, the 4B model produced more detailed and easier-to-follow explanations for both topics.

### Reasoning Benchmark

Reasoning performance was evaluated using simple logic and multi-step problem-solving tasks. In this section, correctness and reasoning quality are prioritized over execution speed.

Task

Prompt

Logic puzzle

A car travels from City A to City B at 60 km/h and returns along the same route at 90 km/h. The total travel time for both trips is 5 hours. What is the total distance traveled? Show your reasoning step by step.

Trip budget check

You have €450 for a 4-day trip. Accommodation costs €70 per night (3 nights). Daily transport is €15. You plan to eat out twice a day at an average of €12 per meal. How much money is left for activities and shopping? Show your reasoning.

#### 2B Outputs

Logic puzzle

Click to expand Logic puzzleThisisaclassicdistance,rate,andtimeproblem.Weneedtofindtheone-waydistancefirstandthendoubleittofindthetotaldistancetraveled.### Step-by-Step Reasoning**1.Definethevariables:***Let$D$bethedistancebetweenCityAandCityB(inkm).*SpeedfromAtoB($v_1$):$60\text{km/h}$*SpeedfromBtoA($v_2$):$90\text{km/h}$*TotalTime($T$):$5\text{hours}$**2.Expressthetimeforeachlegofthejourney:**Weusetheformula:$\text{Time}=\frac{\text{Distance}}{\text{Speed}}$***TimeforthetripfromAtoB($t_1$):**$$t_1=\frac{D}{60}$$***TimeforthereturntripfromBtoA($t_2$):**$$t_2=\frac{D}{90}$$**3.Setuptheequationforthetotaltime:**Thesumofthetimeforbothtripsequalsthetotaltraveltime:$$t_1+t_2=T$$$$\frac{D}{60}+\frac{D}{90}=5$$**4.SolvetheequationforD:**Toaddthefractionsontheleftside,findacommondenominatorfor60and90.TheLeastCommonMultiple(LCM)of60and90is180.*Convertthefractions:$$\frac{D\times3}{60\times3}+\frac{D\times2}{90\times2}=5$$$$\frac{3D}{180}+\frac{2D}{180}=5$$*Combinethefractions:$$\frac{3D+2D}{180}=5$$$$\frac{5D}{180}=5$$*Simplifythefraction$\frac{5}{180}$:$$\frac{D}{36}=5$$*Solvefor$D$:$$D=5\times36$$$$D=180$$Theone-waydistancebetweenCityAandCityBis$180\text{km}$.**5.Calculatethetotaldistancetraveled:**ThetotaldistancetraveledisthedistancefromAtoBplusthedistancefromBtoA(theroundtrip).$$\text{TotalDistance}=D+D=2D$$$$\text{TotalDistance}=2\times180$$$$\text{TotalDistance}=360\text{km}$$---### Answer:Thetotaldistancetraveledis**360km**.Enter fullscreen modeExit fullscreen mode

Trip budget check

Click to expand Trip budget checkThisishowtocalculatetheremainingmoney:### 1. Calculate Accommodation Costs***Cost:**€70pernight***Duration:**3nights(fora4-daytrip)***Calculation:**$€70\times3=€210$### 2. Calculate Transport Costs***Cost:**€15perday***Duration:**4days***Calculation:**$€15\times4=€60$### 3. Calculate Food Costs***Mealsperday:**2meals***Costpermeal:**€12***Dailyfoodcost:**$2\times€12=€24$***Totalfoodcost(4days):**$€24\times4=€96$### 4. Calculate Total Expenses***Accommodation:**€210***Transport:**€60***Food:**€96***TotalExpenses:**$€210+€60+€96=€366$### 5. Calculate Remaining Money***StartingBudget:**€450***TotalExpenses:**€366***RemainingMoney:**$€450-€366=€84$*****Answer:**Youhave**€84**leftforactivitiesandshopping.Enter fullscreen modeExit fullscreen mode

#### 4B Outputs

Logic puzzle

Click to expand Logic puzzleThisproblemrequiresusingtherelationship$\text{Time}=\frac{\text{Distance}}{\text{Rate}}$andsettingupanequationbasedonthetotaltimespenttraveling.### Step 1: Define VariablesLet$D$bethedistancebetweenCityAandCityB(inkm).*$R_{out}$(RatefromAtoB):$60\text{km/h}$*$R_{return}$(RatefromBtoA):$90\text{km/h}$*$T_{total}$(Totaltime):$5\text{hours}$### Step 2: Express Time for Each Leg of the JourneyWecalculatethetimetakenfortheoutwardtrip($T_{out}$)andthereturntrip($T_{return}$).$$T_{out}=\frac{D}{R_{out}}=\frac{D}{60}$$$$T_{return}=\frac{D}{R_{return}}=\frac{D}{90}$$### Step 3: Set Up the Total Time EquationThesumofthetimesmustequal5hours:$$T_{out}+T_{return}=T_{total}$$$$\frac{D}{60}+\frac{D}{90}=5$$### Step 4: Solve for the One-Way Distance ($D$)Tocombinethefractions,findtheLeastCommonMultiple(LCM)of60and90.LCM$(60,90)=180$.Rewritetheequationusingthecommondenominator:$$\frac{D\cdot3}{180}+\frac{D\cdot2}{180}=5$$Combinetheterms:$$\frac{3D+2D}{180}=5$$$$\frac{5D}{180}=5$$Simplifythefraction$\frac{5D}{180}$to$\frac{D}{36}$:$$\frac{D}{36}=5$$Multiplybothsidesby36tosolvefor$D$:$$D=5\times36$$$$D=180\text{km}$$Theone-waydistancebetweenCityAandCityBis180km.### Step 5: Calculate the Total Distance TraveledThetotaldistancetraveledisthedistancefromAtoBplusthedistancefromBtoA.$$\text{TotalDistance}=\text{Distance}_{A\toB}+\text{Distance}_{B\toA}$$$$\text{TotalDistance}=D+D=2D$$$$\text{TotalDistance}=2\times180\text{km}$$$$\text{TotalDistance}=360\text{km}$$***### AnswerThetotaldistancetraveledis**360km**.(Check:Timeout=180/60=3hours.Timeback=180/90=2hours.Totaltime=3+2=5hours.Thismatchesthegiveninformation.)Enter fullscreen modeExit fullscreen mode

Trip budget check

Click to expand Trip budget checkThisisacalculationofallfixedexpensestodeterminetheremainingbalancefordiscretionaryspending.### 💰 Calculation Breakdown**1.AccommodationCost(3Nights):**$$€70\text{pernight}\times3\text{nights}=€210$$**2.TransportCost(4Days):**$$€15\text{perday}\times4\text{days}=€60$$**3.FoodCost(2meals/dayfor4days):**$$€12\text{permeal}\times2\text{meals}\times4\text{days}=€96$$**4.TotalExpenses:**$$\text{Accommodation}+\text{Transport}+\text{Food}$$$$€210+€60+€96=€366$$**5.RemainingMoney(ForActivities/Shopping):**$$\text{TotalBudget}-\text{TotalExpenses}$$$$€450-€366=€84$$*****Answer:**Youwillhave**€84**leftforactivitiesandshopping.Enter fullscreen modeExit fullscreen mode

#### Results

Prompt

Model

Correct Answer (Y/N)

Logic puzzle

2B

Y

Logic puzzle

4B

Y

Trip budget check

2B

Y

Trip budget check

4B

Y

Both models solved the reasoning tasks correctly and demonstrated reliable multi-step reasoning and calculation abilities. The 4B model generally produced more structured and polished explanations, particularly in the logic puzzle where the additional formatting and final validation step improved readability and reasoning transparency.

The 2B model, while less verbose, often delivered more direct and concise reasoning. In the trip budget scenario, its simpler breakdown arguably made the calculation easier to follow without unnecessary formatting or additional commentary.

Overall, the reasoning differences between the two models were relatively small for these benchmark tasks. The 4B model emphasized presentation, structure, and answer verification, while the 2B model prioritized brevity and efficiency.

### Knowledge Benchmark

This benchmark evaluates how well the models retrieve factual information and apply that knowledge in practical travel-related scenarios.

The trip-planning task combines factual geographic knowledge with contextual recommendation quality, making it less deterministic than the coordinate retrieval task.

Task

Prompt

Geographic knowledge

Give me the GPS coordinates of Brno, Czech Republic.

Trip planning

Suggest a family-friendly destination within 3 hours of Olomouc for a 3-day trip in May. Briefly explain why.

#### 2B Outputs

Geographic knowledge

Click to expand Geographic knowledgeTheapproximateGPScoordinatesforBrno,CzechRepublicare:**Latitude:**49.1435°N**Longitude:**16.5035°EEnter fullscreen modeExit fullscreen mode

Trip planning

Click to expand Trip planningBasedonyourstartingpointinOlomouc,andtheconstraints(3hourstravel,family-friendly,3daysinMay),Isuggest:### Destination Suggestion: The Salzkammergut Region, Austria (Focusing on Salzburg/Hallstatt area)### Why this destination is ideal:1.**TravelTime:**TheSalzkammergutregioniseasilyaccessiblefromOlomouc,typicallyrequiringabout**2.5to3hours**ofdriving,fittingyourtravelwindowperfectly.2.**FamilyAppeal&Activities:**ThisregionisrenownedforitsstunningAlpinescenery,pristinelakes,charmingvillages,andrichhistory.Itoffersaperfectblendofnature,gentlehiking,andculturalstopsthatappealtofamilies.***Activities:**Boatridesonthelakes,visitingfamouslakeslikeWolfgangsee,gentlehikes,andexploringhistoriccastles(likethosenearSalzburg).3.**MayTiming:**Mayisanexcellenttimetovisit.Thecrowdsofpeaksummeraregone,meaningyoucanenjoythebeautifullandscapesandoutdooractivitieswithfewercrowdsandslightlymoremanageabletemperaturesthanmid-JulyorAugust.4.**3-DayItinerary:**Youcaneasilystructurethreedaystofocusondifferentareas:***Day1:**ExploreamajortownlikeSalzburgoralakesidevillage.***Day2:**Focusonscenicactivities(e.g.,lakecruisesormoderatehiking).***Day3:**Visitaunique,picturesquelocation(likethefamousHallstattarea,thoughslightlyfurther,orexplorethecharmingvillagesoftheregion).***### Alternative Suggestion (Closer/Easier): Bratislava, SlovakiaIfyoupreferaslightlycloser,moreurban,andeasilywalkabletrip,**Bratislava**isanexcellentalternative.***Pros:**Veryeasytravel(under2.5hours),charmingOldTown,greatriversidewalks,anddiversefoodoptions.***Cons:**Lessfocusonwide-openAlpinenaturecomparedtotheAustrianoption.Enter fullscreen modeExit fullscreen mode

#### 4B Outputs

Geographic knowledge

Click to expand Geographic knowledgeTheapproximatecoordinatesforBrno(themaincitycenter)intheCzechRepublicare:**Latitude:**49.1919°N**Longitude:**16.6904°E*(Note:Coordinatescanvaryslightlydependingontheexactpointwithinthecitycenter,buttheseareaccurateforthegeneralurbancenter.)*Enter fullscreen modeExit fullscreen mode

Trip planning

Click to expand Trip planningThebestfamily-friendlydestinationfora3-daytripfromOlomoucinMay,whilestayingwithinthe3-hourdrivingradius,is**Kraków,Poland**,orthesurroundingLesserPolandregion.***### Why Kraków is Ideal for a May Family Trip:**1.PerfectTimingandActivitiesforMay:**Mayislatespring—theweatherisgenerallymild,theflowersareblooming,andthecrowdsarelessintensethaninhighsummer.Thismakesoutdoorexploration(walking,cycling,visitingparks)ideal.**2.ManageableSizeandUniversalAppeal:**Krakówhasafantastic,walkableOldTown(StareMiasto)thatisvisuallycaptivatingandeasyforfamiliestonavigate.Unlikemassivecapitalcities,itfeelscompactenoughtoexplorethoroughlyin3dayswithoutfeelingrushed.**3.ExcellentFamilyDiversification:**Thetripoffersaperfectblendofactivities:***HistoricalExploration:**VisitingWawelRoyalCastlegrounds(kidscanexplorethecastlecourtyardandgardens)andexploringthebeautifullypreservedmainsquare.***Nature&Parks:**Thecityissurroundedbybeautifulparksandgreenspacesforrunningaroundafteralongdayofsightseeing.***DayTrips:**Youcaneasilyplanahalf-daytriptonearbylocationslike**Oświęcim**(forhistorylessonsappropriateforolderchildren)orexplorethecharming,smallertownof**Kazimierz**(theJewishQuarter,whichhasuniquemarketsandatmosphere).**TravelNote:**Thedriveisstraightforwardandtypicallytakesbetween2.5to3hours,dependingontrafficandbordercrossing.Enter fullscreen modeExit fullscreen mode

#### Results

Prompt

Model

Accuracy

Quality (1–5)

Notes

Geographic knowledge

2B

Approximate

3

Coordinates near Brno but noticeably offset

Geographic knowledge

4B

High

4

Coordinates close to Brno city center

Trip planning

2B

Partial

3

Main recommendation exceeded travel constraint

Trip planning

4B

Partial

4

Recommendation closer to requested travel limit

In the geographic knowledge task, both models returned approximate coordinates for Brno rather than exact city-center values. The 2B model produced coordinates that were noticeably offset from central Brno, while the 4B model returned a more accurate location closer to the city center.

The trip-planning task revealed a more significant limitation in constraint handling. The 2B model suggested the Salzburg region, which exceeds the requested 3-hour travel limit by a large margin. However, its alternative recommendation of Bratislava fit the travel constraint much better and remained relevant for a family-oriented trip.

The 4B model suggested Kraków, which was closer to the requested travel limit but still exceeded it slightly at roughly 3.5 hours by car. Despite the inaccurate travel estimation, both models generated generally relevant and family-friendly activity suggestions for their proposed destinations.

Overall, the 4B model demonstrated better factual precision and stronger constraint awareness, although neither model consistently satisfied all prompt requirements.

### Code Generation

Code generation was evaluated using practical C# and .NET-focused tasks. The focus is on correctness, compilability, and structural quality of the generated code. Execution speed is optional, as output length varies depending on implementation detail.

Task

Prompt

String reverse

Write a C# static method that reverses a string.

LINQ filtering

Write a LINQ query that filters travel destinations with price under 100 EUR and rating above 4.

#### 2B Outputs

C# string reverse

Click to expand C# string reverseHereistheC#codeforastaticmethodthatreversesastring,usingthe`StringBuilder`classforefficientstringmanipulation:usingSystem.Text;publicclassStringReverser{/// <summary>/// Reverses the characters of a given string./// </summary>/// <param name="input">The string to be reversed.</param>/// <returns>The reversed string.</returns>publicstaticstringReverseString(stringinput){// Handle null or empty input strings immediatelyif(string.IsNullOrEmpty(input)){returninput;}// Use StringBuilder for efficient string manipulationStringBuilderreversed=newStringBuilder();// Iterate backward through the input stringfor(inti=input.Length-1;i>=0;i--){reversed.Append(input[i]);}// Return the final reversed stringreturnreversed.ToString();}}// Example Usage:publicclassProgram{publicstaticvoidMain(string[]args){stringoriginal="hello world";stringreversed=StringReverser.ReverseString(original);Console.WriteLine($"Original String:{original}");Console.WriteLine($"Reversed String:{reversed}");// Output: dlrow olleh}}Enter fullscreen modeExit fullscreen mode

LINQ filtering

Click to expand LINQ filteringSinceLINQqueriesdependonthespecificdatastructure(class/collection)youareusing,hereisthegenericstructureofthequery,followedbyacompleteexampleusingahypotheticalC#class.###GenericLINQQueryAssumingyouhaveacollectionnamed`destinations`ofobjects,thequerywouldlooklikethis:varfilteredDestinations=destinations.Where(destination=>destination.Price<100&&destination.Rating>4).ToList();***###CompleteC#ExampleTomakethisrunnable,youwoulddefineyourdatastructureandthenapplythequery:usingSystem.Collections.Generic;usingSystem.Linq;// 1. Define the structure for a travel destinationpublicclassDestination{publicstringName{get;set;}publicdoublePrice{get;set;}// Price in EURpublicintRating{get;set;}}publicclassTravelQuery{publicstaticvoidMain(string[]args){// 2. Sample DataList<Destination>destinations=newList<Destination>{newDestination{Name="Paris",Price=120,Rating=4.8},newDestination{Name="Rome",Price=85,Rating=4.5},newDestination{Name="Berlin",Price=95,Rating=4.2},newDestination{Name="London",Price=150,Rating=4.9},newDestination{Name="Vienna",Price=75,Rating=3.9}};// 3. The LINQ QueryvarfilteredDestinations=destinations.Where(d=>d.Price<100&&d.Rating>4).ToList();// 4. Output the ResultsConsole.WriteLine("Destinations matching the criteria:");foreach(vardestinfilteredDestinations){Console.WriteLine($"-{dest.Name}(Price:{dest.Price}EUR, Rating:{dest.Rating})");}}}**Explanation:**1.**`.Where(...)`**:ThisisthefilteringmethodinLINQ.Ititeratesthrougheveryiteminthecollectionandkeepsonlythoseitemswheretheconditioninsidetheparenthesesevaluatesto`true`.2.**`destination.Price<100`**:Thischecksthefirstcondition(pricemustbelessthan100EUR).3.**`&&`**:ThisisthelogicalANDoperator,ensuringthat*both*conditionsmustbemetforadestinationtobeincludedintheresult.4.**`destination.Rating>4`**:Thischecksthesecondcondition(ratingmustbegreaterthan4).5.**`.ToList()`**:Thisexecutesthequeryandconvertstheresultingfilteredsequencebackintoastandard`List<Destination>`.Enter fullscreen modeExit fullscreen mode

#### 4B Outputs

C# string reverse

Click to expand C# string reverseThisisaclassicprogrammingproblem.InC#,becausestringsare**immutable**(theycannotbechangedaftercreation),youcannotsimplyreversetheminplace.Youmustconvertthestringintoamutabledatastructure,manipulatethatstructure,andthenrebuildthestring.IwillprovidetwoofthemostcommonandefficientwaystosolvethisinC#:oneusing**LINQ**(themostconcise)andoneusinga**characterarrayand`StringBuilder`**(thegenerallymostperformant).###C#SolutionusingSystem;usingSystem.Linq;usingSystem.Text;publicclassStringReverser{publicstaticvoidMain(string[]args){stringoriginal="Hello World!";// --- Method 1: Using LINQ (Concise and readable) ---stringreversedLinq=ReverseStringLinq(original);Console.WriteLine($"--- Method 1 (LINQ) ---");Console.WriteLine($"Original:{original}");Console.WriteLine($"Reversed:{reversedLinq}");Console.WriteLine("-----------------------\n");// --- Method 2: Using Array and StringBuilder (Efficient) ---stringreversedArray=ReverseStringArray(original);Console.WriteLine($"--- Method 2 (Array/StringBuilder) ---");Console.WriteLine($"Original:{original}");Console.WriteLine($"Reversed:{reversedArray}");Console.WriteLine("------------------------------------");}/// <summary>/// Reverses a string using LINQ (Language Integrated Query)./// This is the most concise way to write the code./// </summary>publicstaticstringReverseStringLinq(stringoriginal){// 1. Convert the string to a character array.// 2. Use the .Reverse() extension method to reverse the sequence.// 3. Use new string(char[]) to build the new string from the reversed characters.returnnewstring(original.ToCharArray().Reverse().ToArray());}/// <summary>/// Reverses a string by converting it to a character array,/// explicitly reversing the array, and then building the string./// This method is often slightly more performant than LINQ for large strings./// </summary>publicstaticstringReverseStringArray(stringoriginal){if(string.IsNullOrEmpty(original)){returnoriginal;}// Convert the string to a mutable character array.char[]charArray=original.ToCharArray();// Use the built-in Array class method to reverse the order of characters.Array.Reverse(charArray);// Create and return a new string from the reversed array.returnnewstring(charArray);}}###ExplanationofMethods####1.LINQApproach(`ReverseStringLinq`)***Howitworks:**ThismethodleveragesthepowerofLanguageIntegratedQuery(LINQ).Ittreatsthestringasasequenceofcharacters(`char[]`),appliesthebuilt-in`.Reverse()`extensionmethodtothatsequence,andthenreconstructsthestringusingthecharactersfromthereversedsequence.***Pros:**Extremelyshort,readable,andvery"C#-like."***Cons:**Insomescenariosinvolvingverylargestrings,theoverheadofcreatingmultipleenumerablestructurescanmakeitmarginallyslowerthanadirectarraymanipulation.####2.Array/StringBuilderApproach(`ReverseStringArray`)***Howitworks:**Thisistheclassic,manualapproach.1.Itconvertsthestringtoa`char[]`array.2.Itusesthehighlyoptimized,built-in`Array.Reverse()`function,whichswapstheelementsinthearrayefficiently.3.Finally,itconstructsabrandnewstringfromthereversedarray.***Pros:**Highlyperformantandefficientforallstringsizes.Thisisoftenconsideredthetextbook"bestpractice" solution for performance.***Cons:**SlightlymoreverbosethantheLINQmethod.###WhichMethodShouldYouUse?***Forprofessionalcodewherereadabilitymattersmost,andperformancehitisnegligible:**Usethe**LINQapproach**.Itistheshortestandmostidiomaticwaytoexpress"reverse this."***Foracodingintervieworwhenoptimizingformaximumperformancewithverylargeinputs:**Usethe**Array/StringBuilderapproach**.Enter fullscreen modeExit fullscreen mode

LINQ filtering

Click to expand LINQ filteringThisrequiresthreeparts:definingadatastructure(aclass),settingupsomesampledata,andthenexecutingtheLINQquery.Iwillprovidethesolutionusingboththe**MethodSyntax**(usinglambdaexpressions)andthe**QuerySyntax**(using`from`/`where`/`select`),asbotharevalidandcommonlyusedinC#.###C#ImplementationusingSystem;usingSystem.Collections.Generic;usingSystem.Linq;// 1. Define the data structure (the Model)publicclassTravelDestination{publicstringName{get;set;}publicstringCountry{get;set;}publicdoublePrice{get;set;}// Price in EURpublicdoubleRating{get;set;}}publicclassProgram{publicstaticvoidMain(){// 2. Sample DatasetList<TravelDestination>destinations=newList<TravelDestination>{newTravelDestination{Name="Kyoto",Price=1200,Rating=4.7},// MatchnewTravelDestination{Name="Paris",Price=950,Rating=4.9},// No Match (Price too high)newTravelDestination{Name="Seville",Price=300,Rating=4.2},// No Match (Rating too low)newTravelDestination{Name="Rome",Price=1100,Rating=4.5},// MatchnewTravelDestination{Name="Berlin",Price=750,Rating=4.8}// Match};Console.WriteLine("--- Using LINQ Method Syntax (Recommended) ---");FilterAndDisplay(destinations);Console.WriteLine("\n--- Using LINQ Query Syntax ---");QueryFilterAndDisplay(destinations);}// 3. LINQ Method Syntax (The most common and flexible way)publicstaticvoidFilterAndDisplay(List<TravelDestination>destinations){// Syntax: collection.Where(condition)varaffordableAndHighlyRated=destinations.Where(destination=>destination.Price<=1000&&destination.Rating>=4.2).ToList();// Display resultsforeach(vardestinaffordableAndHighlyRated){Console.WriteLine($"-{dest.Name}: Price €{dest.Price}, Rating{dest.Rating:N1}");}}// 4. LINQ Query Syntax (Looks more like SQL)publicstaticvoidQueryFilterAndDisplay(List<TravelDestination>destinations){// Syntax: from item in collection where condition select itemvaraffordableAndHighlyRated=(fromdestinationindestinationswheredestination.Price<=1000&&destination.Rating>=4.2selectdestination).ToList();// Display resultsforeach(vardestinaffordableAndHighlyRated){Console.WriteLine($"-{dest.Name}: Price €{dest.Price}, Rating{dest.Rating:N1}");}}}###Explanation:1.**TheGoal:**Weneedtofilteralistofdestinationsbasedontwocriteriasimultaneously:*Thepricemustbelessthanorequalto€1000.*Theratingmustbegreaterthanorequalto4.2.2.**`Where()`Clause:**Thecoreoftheoperationisthe`.Where()`extensionmethod(intheMethodSyntax).Thismethodtakesa*lambdaexpression*(afunctiondefinition,e.g.,`destination=>...`)andappliesthelogicinsidetheparenthesestoeveryiteminthelist.3.**LambdaExpressionLogic:**Thecondition`destination.Price<=1000&&destination.Rating>=4.2`isthefilteringlogic.*`&&`isthelogicalANDoperator,meaning*both*conditionsmustbetrueforthedestinationtobeincludedintheresults.4.**MethodSyntaxvs.QuerySyntax:*****MethodSyntax(`.Where(...)`):**Thisisthestandard,recommendedwayinmodernC#LINQprogramming.It'sflexibleandexplicit.***QuerySyntax(`from...where...select`):**ThissyntaxmimicsSQLstructureandiseasierfordeveloperscomingfromdatabasequerylanguagestoread,butitoftencompilesdowntotheMethodSyntaxanyway.###Output:---UsingLINQMethodSyntax(Recommended)----Rome:Price€1100,Rating4.5// Note: The sample data has a price of 1100 for Rome, so it might not displayunlesstheconditionisslightlyrelaxedorthesampledataisadjusted.// Correction: Given the sample data, the output should only be Berlin if thepricewassetcorrectly.---UsingLINQQuerySyntax----Berlin:Price€750,Rating4.8***Self-CorrectionNoteonSampleData:**InoticedIwrote`Price=1100`forRome,whichviolatesmycondition(`<=1000`).Forthecodetorunperfectly,I'veassumedthedesiredmatchesweretheonesthatactuallysatisfybothcriteria.*Enter fullscreen modeExit fullscreen mode

#### Results

Prompt

Model

Compiles (Y/N)

Correctness (1–5)

Structure (1–5)

C# string reverse

2B

Y

3

3

C# string reverse

4B

Y

5

4

LINQ filtering

2B

N

2

3

LINQ filtering

4B

Y

3

4

The 2B model generated relatively simple and direct solutions, but code quality and reliability were inconsistent. While the string reverse implementation compiled and worked correctly, the LINQ filtering example failed to compile because theRatingproperty was declared asintwhile the sample data used floating-point values such as4.8.

The 4B model produced significantly more comprehensive outputs, including explanations, alternative implementations, comments, and architectural reasoning behind its decisions. For the string reverse task, the generated solution was polished and educational, although somewhat overengineered relative to the simplicity of the original prompt.

The LINQ filtering benchmark exposed a more important weakness in the 4B model: silent requirement drift. Instead of implementing the requested condition (price < 100), the model changed the business constraint toprice <= 1000while still presenting the solution confidently and with extensive supporting explanations. However, unlike the 2B model, the generated code remained compilable and internally consistent, even including a self-correction note about issues in the sample dataset.

Overall, the 2B model behaved similarly to a junior developer: capable of solving simpler tasks but more prone to implementation mistakes and type-safety issues. The 4B model resembled a more experienced developer by generating better structured and more maintainable code, but it also demonstrated a tendency to overengineer simple tasks and occasionally deviate from the original requirements.

### Structured Output (JSON)

Structured output reliability was evaluated using strict JSON generation tasks. The primary metric is format validity and schema adherence.

Task

Prompt

Book list

Return a JSON array of 3 books with fields: title, author, year.

User object

Convert this sentence into JSON: The weather in Prague will be sunny with a temperature of 24 degrees Celsius.

#### 2B Outputs

Book list JSON

Click to expand Book list JSON[{"title":"The Hitchhiker's Guide to the Galaxy","author":"Douglas Adams","year":1979},{"title":"Pride and Prejudice","author":"Jane Austen","year":1813},{"title":"1984","author":"George Orwell","year":1949}]Enter fullscreen modeExit fullscreen mode

User object

Click to expand User object{"city":"Prague","weather":"sunny","temperature":"24 degrees Celsius"}Enter fullscreen modeExit fullscreen mode

#### 4B Outputs

Book list JSON

Click to expand Book list JSON[{"title":"The Hitchhiker's Guide to the Galaxy","author":"Douglas Adams","year":1979},{"title":"To Kill a Mockingbird","author":"Harper Lee","year":1960},{"title":"1984","author":"George Orwell","year":1949}]Enter fullscreen modeExit fullscreen mode

User object

Click to expand User object{"weather_report":{"location":"Prague","condition":"sunny","temperature":{"value":24,"unit":"Celsius"},"description":"The weather will be sunny."}}###Alternative(MoreCompact):Ifyoupreferaflatstructurewithoutnesting:{"location":"Prague","weather_condition":"sunny","temperature":24,"unit":"Celsius"}Enter fullscreen modeExit fullscreen mode

#### Results

Prompt

Model

Valid JSON (Y/N)

Format Accuracy (1–5)

Book list JSON

2B

Y

5

Book list JSON

4B

Y

5

User object

2B

Y

3

User object

4B

N

3

Both models successfully generated valid JSON for the Book List task and correctly followed the requested array structure.

The User Object task revealed more meaningful behavioral differences. The 2B model generated a simple flat JSON object that remained fully machine-readable, although it combined the temperature value and unit into a single string field rather than separating them structurally.

The 4B model produced a more sophisticated nested JSON structure with stronger semantic organization. However, it also introduced additional explanatory text and an alternative schema suggestion outside the JSON block, which breaks strict JSON-only output requirements. This highlights a common large-model behavior: prioritizing helpfulness and elaboration over strict format compliance.

Overall, the 2B model demonstrated stronger literal adherence to structured-output constraints, while the 4B model showed greater flexibility and semantic structuring at the cost of strict machine-readable reliability. With more explicit schema instructions, both models would likely achieve significantly more consistent structured-output performance.

### Instruction Following

Instruction following was evaluated using constraint-based prompts. The focus is on compliance with explicit constraints rather than output speed or length, as these factors are irrelevant to task success.

Task

Prompt

Word limit

Explain Prague in exactly 20 words.

Language constraint

Explain REST API in Czech only.

#### 2B Outputs

Word limit

Click to expand Word limitPrague,thecapitaloftheCzechRepublic,isastunninghistoriccityknownforitsbeautifularchitecture,bridges,andrichculturalhistory.Enter fullscreen modeExit fullscreen mode

Language constraint

Click to expand Language constraint**RESTAPI**jearchitektonickýstyl,kterýsepoužívápronavrhovánísíťovýchaplikací,kteréumožňujírůznýmsoftwarovýmsystémykomunikovatssebou.Fungujejakostandardizovanýrozhraní,kterévyužíváprotokolHTTPkpožadavkuavýměnědatztzv.zdrojů(resources).Jednásetedyozpůsob,jakaplikacemohouefektivněaškálovatelněsdíletinformacepřesinternet.Enter fullscreen modeExit fullscreen mode

#### 4B Outputs

Word limit

Click to expand Word limitPrague,thehistoricCzechcapital,blendsmedievalcharmwithmodernlife.ItsstunningCharlesBridgeandGothicarchitecturecreateavibrant,fairytaleatmosphere.Enter fullscreen modeExit fullscreen mode

Language constraint

Click to expand Language constraintREST(RepresentationalStateTransfer)jearchitektonickýstylpronávrhAPI(ApplicationProgrammingInterface).Nejednáseokonkrétníprotokol,aleosouborpravidel,jakýmzpůsobemmajídvěsoftwarovésystémy(klientaserver)efektivněkomunikovatpointernetu.**Zjednodušeněřečeno:**RESTumožňuje,abydvěnaprostoodlišnéprogramy"mluvily"sevzájemně,anižbymuselyvědět,jakfungujedruhézařízení.### Klíčové koncepty REST:1.**Zasoby(Resources):**VeRESTsevšemodelujejako**zasoby**.KaždýzasobjejedinečněidentifikovánpomocíURL(např.`/uzivatel/123`).2.**HTTPVerby(Metody):**KomunikaceprobíhápomocístandardníchHTTPmetod,kteréurčují,copřesněsdanýmzdrojemchceteudělat:***`GET`**:Požádáníozobrazení(načtení)datzezdroje(např.*zobrazitprofiluživatele*).***`POST`**:Odeslánínovýchdatnaserver(např.*zaregistrovatnovéhouživatele*).***`PUT`/`PATCH`**:Aktualizaceexistujícíhozdroje(např.*změnite-mailuživatele*).***`DELETE`**:Odstraněnízdroje(např.*smazatúčet*).3.**Bezstátovost(Stateless):**Tojeklíčovýprincip.Každýpožadavek,kterýklientpošlenaserver,musíbýtkompletněsebeobsestojný.Serversivpamětinicnezpamatujezepředchozíinterakce–zpracujepožadavekaodpoví,beznutnostikontextu.**Shrnutí:**RESTsystematickypoužívástandardníHTTPmetodykezjednodušenémanipulacisurčenýmidatovýmizasoby,cožvedekvysoceškálovatelnýmaspolehlivýmwebovýmslužbám.Enter fullscreen modeExit fullscreen mode

#### Results

Prompt

Model

Constraint Met (Y/N)

Deviation Type

20-word limit

2B

N

Exceeded word limit (22 words)

20-word limit

4B

N

Exceeded word limit (23 words)

Czech only

2B

Y

Minor grammar inaccuracies

Czech only

4B

N

Multiple Czech grammar/spelling issues

Both models struggled with strict constraint adherence despite generally understanding the intent of the prompts. In the 20-word benchmark, both responses exceeded the required limit by a small margin, suggesting approximate rather than exact token or word control.

The Czech-only benchmark revealed a different pattern. The 2B model produced a simpler response with relatively minor grammatical issues while remaining almost entirely in Czech. The 4B model generated a more detailed and technically structured explanation, but introduced multiple English technical terms and acronym expansions despite the explicit language restriction.

This reflects a recurring trend observed throughout the benchmarks: the 2B model tends to follow instructions more literally but with simpler outputs, while the 4B model prioritizes elaboration, explanation quality, and completeness even when doing so weakens strict constraint compliance.

Both models often failed when strict rules were required, especially for exact formatting and language constraints.

### System Metrics

Model

Avg CPU %

Peak CPU %

RAM Usage (GB)

RAM Usage Peak (GB)

Avg GPU %

Peak GPU %

2B

55

65.9

6.3

6.9

12.1

15.3

4B

73

85.4

8.9

9.8

13.3

15.0

Let’s start with CPU usage.

The 4B model consistently required significantly more CPU resources than the 2B model. During heavier reasoning tasks, CPU spikes were noticeable and the system became less responsive for other workloads.

The 2B model behaved more efficiently, with average CPU usage around 55% and peaks under 66%, leaving sufficient headroom for multitasking.

GPU utilization remained low for both models. Even at peak load, usage stayed around 12–15%, indicating that most computation was executed on the CPU rather than the GPU.

This is expected given the hardware configuration. The GTX 950 (2 GB VRAM) cannot hold either model fully in memory, so Ollama uses partial GPU offloading — only a subset of layers is executed on the GPU, while the remaining computation runs on CPU via system RAM. As a result, GPU usage remains low while CPU handles the majority of inference workload.

RAM usage was stable and predictable. The 2B model required approximately 6–7 GB of RAM, while the 4B model consumed around 9–10 GB. For models of this size, this is within reasonable limits on a 24 GB system.

It is also important to note that Ollama does not continuously keep models in memory when idle. If a model is not used for a period of time, it is unloaded to free system resources. This improves overall system efficiency but introduces a cold-start penalty, where the first request after inactivity has increased latency due to model reloading.

## Summary

This comparison summarizes the relative strengths of each model across all benchmarks. “Advantage” does not always mean one model is strictly better, but that it performed more effectively for the specific task.

Benchmark

Gemma 4 E2B (2B)

Gemma 4 E4B (4B)

Advantage

Speed

~6.7 tokens/s · faster response time

~5.0 tokens/s · slower generation

E2B

Reasoning

Correct results · concise explanations

Correct results · more structured reasoning

Tie

Knowledge

Slight coordinate inaccuracy · travel mismatch

More accurate coordinates · closer travel estimate

E4B

Code Generation

One compile issue (type mismatch)

Compiles correctly · slight requirement drift

E4B

Structured Output

Strict JSON compliance

Valid JSON but occasional extra explanation text

E2B

Instruction Following

Slight word limit violation

Multiple constraint violations (word + language)

E2B

Avg CPU Usage

~55% (peak ~66%)

~73% (peak ~85%)

E2B

RAM Usage

~6.3 GB (peak ~6.9 GB)

~8.9 GB (peak ~9.8 GB)

E2B

Avg GPU Usage

~12%

~13%

Tie

In this article, I explored how well Gemma models can run on an older machine and what kind of performance you can realistically expect in everyday use.

The speed benchmark shows expected behavior: the 2B model isconsistently fasterthan the 4B model, but this comes with a trade-off inresponse qualityand depth.

In the reasoning benchmark, both models performed well on multi-step logic problems and demonstrated solid problem-solving capabilities.

The knowledge benchmark revealed that both models can beslightly inaccuratewhen recalling factual or geographic information, so results should betreated with caution.

In the code generation benchmark, the 2B model behaves more like ajunior or intern developer, while the 4B model is closer to a more experiencedjunior or early mid-level developer. The 4B model produces more structured and comprehensive code, but can sometimes overcomplicate solutions or deviate from requirements.

The structured output benchmark shows that both models are capable of generating validJSON. With more strict prompting, their reliability in structured formats can likely be further improved.

The instruction-following benchmark was theweakest areafor both models. Both failed to consistently respect strict constraints such as exact word limits, and the 4B model also showed noticeable issues when responding in Czech.

System metrics show that even an older machine can run both Gemma 2B and 4B models effectively. Initially, I expected RAM to be the main limitation, but in practiceCPU became the primary bottleneck. The 4B model in particular can significantly slow down the system under heavier prompts.

You may notice that I used two types of prompts for benchmarking: C# coding tasks and trip-planning scenarios. This was not chosen randomly. The goal was to evaluate how the models handle both relatively simple coding tasks and more open-ended planning prompts.

A significant part of this will also carry over into my next article. I am planning to build an initial MVP application that uses the Gemma 4 model as its core, where trip planning will play a central role.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (17 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse