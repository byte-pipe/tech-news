---
title: 'Beyond Lazarus: How North Korea Organizes Its Cyber Operations'
url: https://www.sekoia.com/blog/beyond-lazarus-organization-of-dprk-cyber-capabilities
site_name: tldr
content_file: tldr-beyond-lazarus-how-north-korea-organizes-its-cyber
fetched_at: '2026-09-09T15:29:57.946677'
original_url: https://www.sekoia.com/blog/beyond-lazarus-organization-of-dprk-cyber-capabilities
date: '2026-09-09'
description: Co-authored by Sekoia and Kudelski Security, this report maps North Korea’s cyber ecosystem, from state institutions and APT clusters to IT worker operations.
tags:
- tldr
---

Home

Blog

Beyond Lazarus: Organization of DPRK cyber capabilities
Table of contents
35 min
H2 title on one or more lines.
All categories & topics
Threat Research & Intelligence
Detection Engineering
SOC Insights & Other News
Product News
TDR Team
AI
Cloud
Integrations
Compliance
APT
Cybercrime
Phishing
Speak to a Sekoia expert

Your security challenges deserve expert answers. Get a tailored demo and discover how Sekoia helps your team detect and respond to threats faster.

Get a demo

Share

Copied !

Threat Research & Intelligence
TDR Team
APT
By
TDR Team
By
Saee V.
By
Coline C.
By
Clifford
Updated on
September 7, 2026

# Beyond Lazarus: Organization of DPRK cyber capabilities

Get the full overview of North Korea's cyber operations, from state institutions and APT clusters to IT workers units, and enablers.

## Key takeaways

The DPRK built its cyber capability as a deliberate extension of its asymmetric deterrence doctrine, treating cyber operations as a cheap, deniable "all-purpose sword" alongside nuclear weapons to ensure regime survival against better-resourced adversaries and circumvent international sanctions.

* From roughly 2014 onward, cyber operations evolved from espionage and sabotage into a load-bearing revenue stream, bank heists, ransomware, and cryptocurrency theft, financing the very weapons programmes that international sanctions were designed to constrain.
* Even as the GRIB (ex-RGB) and NIA (ex-MSS) consistently lead DPRK cyber offensive operations, the units and bureaus beneath them are subject to constant reorganization, a deliberate control mechanism that keeps agencies competing for Kim Jong-un's favor, prevents consolidation of independent power, and complicates the attribution and sanctions-designation efforts of foreign governments.
* DPRK offensive cyber operations are distributed across APT clusters, with the former Lazarus umbrella now decomposed by Sekoia and Kudelski Security into six distinct sub-clusters, nearly all of which conduct lucrative operations, whether as their primary mandate or to self-fund espionage and sabotage campaigns.
* These APT intrusion sets are complemented by thousands of IT workers operating under false identities worldwide, who serve a dual function: remitting salaries to the regime and leveraging their insider access within contracted organizations to conduct further operations, with proceeds laundered through centralized exchanges, decentralized exchanges (DEXs), and P2P platform.
* The DPRK has constructed a complex network of educational and private intermediaries to enable its cyber operations, spanning academic institutions that both train operatives and function as operational nodes. This parallel web of third-country relays often extends to allies like China and Russia, as well as countries in Africa and Southeast Asia. Front companies across these regions participate in generating revenue and providing operational cover, while criminal networks are operationalized for money laundering.

This article was co-authored by Sekoia’s TDR team and Kudelski Security as part of a joint research effort.

## Introduction

TheDemocratic People's Republic of Korea (DPRK)has established itself as one of the more prominent state actors in cyberspace. For Pyongyang, cyber operations serve as an instrument of sanctions evasion, a means of projecting reach beyond a diplomatically and economically constrained periphery, and a source of revenue for a structurally weakened economy. These capabilities are theproduct of a deliberate strategy, considerably reinforced under Kim Jong-un, which situates information warfare at the centre of contemporary geopolitical confrontation.

The consequences of that strategy are visible inthe growth of the operator base, thesuccessive reorganizationsof the institutions holding offensive cyber mandates, and theexpanding frequency and sophisticationof DPRK operations and revenue-generation activity. As the regime continues to consolidate these capabilities and project them globally, an understanding of the DPRK cyber threat has become a practical necessity for governments and private organizations alike.

This paper seeks to provide the elements required for such an understanding: the function of cyber operations within Pyongyang's wider strategic posture, the organization of offensive capabilities across DPRK institutions, and an overview of threat clusters through which that architecture manifests. The research was conducted in partnership betweenSekoiaandKudelski Security.

‍

## Strategic development of cyber capabilities

### Origin and structure of the regime

The Democratic People's Republic of Korea (DPRK) was proclaimed on 9 September 1948, a few years after Japan's 1945 surrender ended thirty-five years of colonial rule and left the peninsula divided by Soviet and American occupation zones along the 38th parallel. In the Soviet-administered north, Moscow installedKim Il-sung, a former guerrilla commander who had fought Japanese forces in Manchuria, as chairman of the provisional government. Soviet advisers helped build theKorean Workers' Party (KWP)and the nascent security apparatus that would outlast the occupation itself.

Kim Il-sung consolidated power through the Korean War (1950-1953) and subsequent purges of rival factions. Then, he built a totalitarian, Stalinist-inspired state organized aroundjuche(self-reliance)and an increasingly elaborate cult of personality that was extended, after his death in 1994, to his son Kim Jong-il and, since 2011, to his grandson Kim Jong-un.

Institutionally, the DPRK is a party-state in which theKWP, the state bureaucracy (headed by theState Affairs Commission, SAC) and the military are formally distinct but functionally fused under the Kim family's personal authority. As chairman of the SAC, supreme commander of theKorean People's Army(KPA) and chairman of the KWP's Central Military Commission, Kim Jong-un holds simultaneous command of the party, the cabinet and the armed forces.

Within this structure, intelligence and covert operations, including cyber activity, sit primarily under theReconnaissance General Bureau (RGB), formed in 2009 by merging several older intelligence organs and reporting directly to Kim rather than through the conventional military chain of command, alongside the General Staff Department of the KPA and the Ministry of State Security.

DPRK regime structure

### Strategic objectives and their evolution

The regime's overriding objective has remained its own survival against what it portrays as existential threats from Washington and Seoul. From this core goal, three broad and evolving strategic lines can be traced. First,military-first (Songun policy) deterrence, which, after the collapse of Soviet and Chinese economic patronage in the 1990s, hardened into a nuclear and missile programintended to make forced regime change too costlyto attempt. This culminated in nuclear tests from 2006 onward and, more recently, constitutional changes formally vesting command of nuclear forces in the SAC chairman.

Second, Pyongyang has aimed atasymmetric and covert capability-building, with the use of electronic warfare, cyber operations, special forces, and proliferation networks, designed to inflict cost on adversaries and generate hard currency while remaining below the threshold of open war. This doctrine has been traced to North Korea's study of the1991 Gulf Warand the2003 Iraq War, and to inspiration drawn from the concept of information warfare developed in China. It was later reinforced by Kim Jong-un's speech at the3rd Plenary Meeting of the 7th KWP Central committee in April 2018, when he announced the achievement of theByungjin policy’s objectives,which were the development of nuclear capabilities in parallel with the economy. As a new guideline, he stated that the DPRK would focus on socialist economic construction, pivoting from a doctrine of “military-first” to “economy-first”. As a result, the number of DPRK cyber operatorsdoubled that year compared to 2013and lucrative operations targeting cryptocurrency rose as the nascent global crypto market exploded.

Third,since 2024, the DPRK has formallyabandoned the unification goalthat had nominally guided its policy since 1948. Indeed, Kim Jong-un declared inter-Korean relations to be between "two hostile states," and the KWP subsequently dismantled unification-oriented institutions andrevised the constitutionin 2026 to define South Korea as foreign territory rather than a temporarily separated part of the same nation. This shift reflects both domestic legitimation needs, with Kim Jong-un increasingly grounding his authority in constitutional and popular-sovereignty language rather than purely dynastic cult of personality claims, and a geopolitical recalculation: deepening alignment with Russia since the invasion of Ukraine, and a long-standing reliance on China, have reduced Pyongyang's incentive to court Seoul or maintain ambiguity for the sake of eventual unification.

### Cyber operations as an integrated strategic tool

Cyber capability was progressively folded into this strategic architecture. Kim Jong-il began prioritizing "electronic warfare" after observing the decisive role of networked,information-enabled forces in the Gulf, Kosovo and Iraq wars, reportedly describing cyberattacks as "atomic bombs" of the information age.

His successor, Kim Jong-un, who is acomputer-science-trained leader, later called cyber operations an "all-purpose sword" alongside nuclear weapons and missiles. Because cyber operations are cheap compared to conventional weapons, deniable, and effective against wealthier and more networked states, such as South Korea and the United States, they became a natural extension of the asymmetric-deterrence line of DPRK.

Consequently, cyber operations have moved from a niche military-modernization experiment (cf.2009-2011 DDoS attacks) to a load-bearing pillar of DPRK statecraft, simultaneously anintelligence tool, asanctions-evasion mechanism, and arevenue streamfor the nuclear and missile programs that anchor the regime's core survival strategy under Kim Jong-un’s influence.

Computer networks exploitation (CNE) and attack (CNA) became a core priority, withtalented children identified in schoolto integrate elite hacking universities, the emergence offirst DPRK-led destructive cyber operations(Operation DarkSeoul 2013, Sony PIctures Hack 2014, WannaCry 2017), themultiplication of intelligence gatheringoperations, and thesystematic use of cyber campaignsfor revenue generation.

Indeed, fromroughly 2014 onward, cyber operations became an increasingly importantfinancing mechanismfor the heavily sanctioned DPRK economy, as the regime shifted from pure espionage and sabotage toward bank heists, ransomware, and large-scale cryptocurrency theft (cf. the 2016 Bangladesh Bank $101 million heist andthe 2025 Bybit$1.5 billion theft), reportedly generatinghundreds of millions to over a billion dollars annuallyto help fund weapons programs.

‍

## Institutions with offensive cyber mandates

### Mandates and operational roles

As previously mentioned, the North Korean regime relies on institutions such as theKorea Workers’ Party (KWP)and theGeneral Reconnaissance and Information Bureau (GRIB), formerly known as theRGBto facilitate its offensive cyber operations. These operations are considered to be anintegrated strategic toolor an “all-purpose sword” to achieve the economic and geopolitical objectives of the regime.

#### General Reconnaissance and Information Bureau (GRIB) 정찰정보총국, ex-RGB 정찰총국

TheGRIBisconsideredto be the Kimregime’s leading foreign intelligence agencyandmilitary reconnaissance unit. However, itsfunctionsare far broader than a traditional military intelligence agency. In addition to intelligence collection and clandestine operations, the GRIBcommands the DPRK’s most capable cyber offensive and combat units. Furthermore, The bureau has usedfront companiessuch as the UN-designated Green Pine Associated Corporation (KPe.010) to conduct illicit arms trade and procurement.

To conduct these varied operations, the GRIB (ex-RGB) isuniquely placedwithin the DPRK political and military structure. The agency is hierarchically under the North Korean State Affairs Commission (SAC) andreports directlyto the KPA Supreme Commander Kim Jong-un. Concurrently, its administrative military designation isKPA Unit 586.

Before the RGB was established, Demilitarized Zone (DMZ) infiltration operations werehandledby the KPA Reconnaissance Bureau, a long-standing unit under the KPA General Staff. In 2009, as Kim Jong-un prepared to take power, North Korea restructured this bureau into the RGB, alarge consolidated task force. The new RGB merged the former Reconnaissance Bureau's large-scale reconnaissance and infiltration functions with the KWP Operations Department and the overseas intelligence operations of KWP Office 35.

Thus, theRGBat its inception in 2009 representedstreamlined control and commandof all intelligence operations. Cyber warfare capabilities have alsogrownin their effectiveness and importance to the Kim regime more than any other operational functions, thus the reorganization allowed for better control by the Supreme Leader for command as well as political-military oversight.

#### National Intelligence Agency (NIA) 국가정보국, ex-MSS 국가안전보위성

The National Intelligence Agency (NIA), formerly the Ministry of State Security (MSS) is the regime’sprimarycounterintelligence, and secret police agency, tasked withinternal securityand protecting the leadership fromdomestic and foreign threats. It reports directly to the State Affairs Commission under Kim Jong-un, ensuring loyalty to the ruling party. Though it is primarily an internal security body, it is also believed to coordinate with military and cyber units tosupport regime stability and strategic goals, including conducting intelligence operations targeting foreign governments, defectors, and dissident groups.

In June 2026, this Ministry wasrenamedas theNational Intelligence Agency (NIA), or the State Intelligence Agency. Originally, the MSS operated counterintelligence and counterespionage missions, conducting cyber campaigns targeting defectors and DPRK experts. Its renaming was likely as a sign of an expansion of its field of competencies, especially forforeign missionsand of a new repartition with theMinistry of Public Security (MPS), which will likely assume the role of adomestic police force.

#### Korean Workers' Party (KWP) 조선로동당

Kim Jong-un frequently signals hisprioritiesfor economic and military development in his annual addresses to the KWP plenary meetings. After these addresses, the cyber program’s units are observed toquickly shiftto new mission areas in line with Kim’s statements. Thus, the KWP is crucial to sense thepolitical directionwhich mandates cyber offensive activities.

The KWP also retains aparallelrole through bodies like theOrganization and Guidance Department (OGD), which controls senior personnel appointments across the party, military, and government and enforces the regime's internal political and censorship controls, giving the party a supervisory hand over the same personnel pipeline that feeds intelligence units. Additionally,educational programsin DPRK universities focusing on developing skills in science, technology, engineering, and math (STEM), which ultimately produce“information warriors”are also set up under the direction of the KWP.

### Institutional reorganization

Despite the existence of institutions clearly identified as housingNorth Korea’s offensive cyber capabilities, thefrequent reshufflingof responsibilities makes mapping the hierarchy of political-military entities including units, bureaus and liaison offices difficult.

According to some DPRK-watchers, North Korean intelligence agencies have continuously beenreorganizedand/or redesignated, shifting between combined and independent structures over time to align with the regime’sstrategic goals. For instance, in March 2026, the regimeremoved referencestoreunificationwith South Korea from the DPRK constitution, signaling a push for a more hostile policy toward South Korea. The push for the restructuring of theGRIB(ex-RGB) andNIA(ex-MSS) came soon after, possibly reflecting an effort to realign the intelligence apparatus with the leadership’s long‑term state‑building goals.

Moreover, splitting intelligence missions across multiple agencies creates competition among them for the Supreme Leader's favor. This allows him to keep the agencies watching one another, which strengthens regime security and longevity; akey goalof the regime being itssurvival,andresponseto global events.

By analyzing the roles of North Korean entities with cyber offensive functions, certain plausible links can be drawn between their nomenclatures and roles. It must be noted that certain discrepancies will remain and these entities are subject to frequent change.

 
 
 
 
Nomenclature
 
Role
 
 
 
 
 
Department (
부
 / 
-부
)
 
A major, publicly acknowledged pillar of the party bureaucracy
 
 
 
Bureau (
국
 / 
-국
)
 
Used at multiple levels to designate executive or operational arms; tends to be an operational command or executive body, often military or security-related, that implements rather than sets policy
 
 
 
Office (
실
/
처
)
 
Smaller, secretive units. North Korea is notorious for giving some of its most sensitive ones anonymous numbers rather than descriptive names
 
 
 
Unit (
부대
 or 
소조
)
 
A numeric cover designation applied at variable scale, from small operational cells up to entire bureaus
 
 
 
Military units (corps, brigades, etc.)
 
Conventional troop formations, unrelated to the party apparatus
 
 
 

## DPRK-nexus intrusion sets and operational clusters

Organizationally, offensive cyber operators arelargely dilutedinto various entities, inside and outside DPRK borders.

Units related to publicly tracked Advanced Persistent Threats (APTs) are intrusion sets sitting mainly within theGRIB(ex-RGB), and to a smaller extent, within theNIA(ex-MSS). Anintrusion setis a cluster of malicious cyber activity characterized by its specific victimology, a dedicated arsenal, comprising tools and malware, and key patterns in terms of infrastructure and Tactic, Techniques and Procedures (TTPs).

In addition, DPRK cyber activity is supported byfake IT workers, who are North Korean nationals and foreigners recruited to secure technical jobs, channel salaries and information back to the regime, and/or conduct operations from abroad.

In this section, we will present the DPRK-nexus threat actors conducting offensive cyber operations to support Pyongyang strategic objectives, evade sanctions and fund ballistic missiles and nuclear programmes.

An important characteristic of these activity clusters is thatthey almost all conduct lucrative operations. For some of them, it constitutes their main operational objective, while, for others, notably with a focus on cyberespionage, it can be explained by a need toself-fundtheir operations.

### DPRK-nexus APTs

Since the integration of offensive cyber capabilities in DPRK strategy, sophisticated units were implemented, often tracked asAPTs. These clusters have been mandated to conduct various types of operations, ranging fromfinancially-motivated campaigns, tocyber espionage,sabotageandinfluence.

DPRK-nexus APTs

As explained previously, these units have been regularly reorganized and renamed, making the understanding of North Korea’s cyber ecosystem complex. We categorized DPRK-nexus threat clusters depending on their TTPs and the type of operations they conduct. We notably made our clustering evolved by splitting theLazarus umbrellainto six distinct sub-clusters: TEMP.Hermit, Citrine Sleet, CryptoCore, Jade Sleet, Moonstone Sleet, and Famous Chollima.Famous Chollimadistinguished itself by representing malicious activity related to fake IT workers, which often supports the operational objectives of other cyber warfare units.

Lazarus Group sub-Clusters evolution

#### Strategic espionage

DPRK-nexus threat clustersfocusing primarilyon intelligence collection sit under theGRIB(ex-RGB). Even if their affiliation to the3rdand/or the5th Bureauis debated among the CTI community, they are the inheritage of the historicalLazarusumbrella andKimsukycluster.

We identify cyberespionage as the primary objective of the threat clusters mentioned below, as their arsenal and associated campaigns pointed out to intelligence collection capabilities. However, they also happened to conduct cybercrime activity at the margin, likely to self-fund their operations.

Similarly to the Lazarus umbrella, which is now associated with several threat clusters, likely reflecting an internal reorganization following an increase in the number of operators,Kimsukyis regardedby some DPRK expertsas a mega-cluster comprising several branches, likeTA406andTA408among others.

Espionage-oriented threat clusters

Historically, DPRK-nexus threat clusters associated with cyberespionage campaigns also conductedsabotageoperations leveraging wipers. Well-known cases are theOperation Dark Seoul(2013), and theOperation Blockbuster(Sony Picture Hack) (2014) attributed toLazarus.Kimsukywas also observed using wiper components during theKorea Hydro and Nuclear Power breachin 2014. However, no investigations pointed out the use of wipers in recent campaigns, likely due to refocus on stealthy espionage operations. The most recent case wasAPT38, now considered as splitted between CryptoCore and Jade Sleet, which was a financially-motivated threat cluster, which leveraged disk-wipe techniques (KillDisk) as an anti-forensics measure in 2017.

#### Dual-mandate: Espionage and revenue generation

Characteristic of Pyongyang’s strategy, a set of DPRK-nexus threat clusters conductboth financially-motivated campaigns and cyberespionage, likely to support the development and thefundingof the nuclear and ballistic missiles programs.

Of note,Andarielis particular as it used custom ransomware (Maui and H0lyGh0st) for financial theft, as well as ransomware-as-a-service (RaaS) developed by an operator of the Russian cybercrime ecosystem. It was notablyobservedcollaborating withPlayin 2024. Another DPRK cluster,Moonstone Sleet,acted similarly by deploying its custom malwareFakePennyin 2024, but also theQilinRaaSin 2025. It is interesting to note that the two clusters integrated RaaS in their campaigns within two months of each other.

Lucrative and espionage-oriented threat clusters

#### Revenue generation

In atransition phaseduring which the Lazarus umbrella likely reorganized internally, the group was divided into sub-clusters, likely specializing their activity between financial gain and espionage. This evolution happened between2018 and 2023, in the context of an expansion of the cryptocurrency market globally.

As a result, the sub-clusterAPT38was identified and associated with financially-motivated operations likely conducted by the110th Research Instituteunder the GRIB (ex-RGB). It focused on the targeting of the cryptocurrency industry, Web3 and blockchain technologies.

Currently, APT38 has likely splitted in two sub-clusters that we associate withCryptoCoreandJade Sleetas a result of our research. These two clusters are characterized by focusing exclusively on financially-motivated campaigns, likely to generate revenue for the regime.

Lucrative-oriented threat clusters

#### Surveillance and internal repression

In line with theNIA(ex-MSS) mandate, the related threat clusterReaperfocuses on DPRK defectors, South Korean DPRK-focus activists and NGOs, acting as a secret police with cyber means.This new ministry nameimplemented in 2026 likely confirmed the wide range of sectors, mainly in South Korea, targeted by Reaper for espionage. Indeed, it is likely as a sign of an expansion of MSS competencies and of a new repartition with theMinistry of Public Security (MPS),which will likely assume the role of a police force focused on internal affairs.

Reaper also likely increased in 2024, with the dismantlement of theUnited Front Department.According toanalysts, cyber operators from the United Front Department were transferred notably to the GRIB (ex-RGB) and to the NIA (ex-MSS).

Repression-oriented threats

### IT worker operations

Beyond the operations of APTs intrusion sets, the DPRK's offensive cyber capabilities are complemented by the activities ofIT workers. They are skilled individuals, predominantly DPRK nationals and in some cases supported by foreign facilitators recruited online, tasked withgenerating revenuefor the regime in order to circumvent international sanctions and finance the country's ballistic missile and nuclear programmes.

The IT-worker programmeadapts an established practicerather than inaugurating a new one: the dispatch of North Korean labor abroad to earn foreign currency dates to the 1960s and 1970s, beginning with logging in the Soviet Far East before broadening into construction, textiles and restaurant services across Russia, China, the Gulf and Africa. The shift into the IT sector is documented publicly from at least 2018, when theUS Treasury designatedYanbian Silverstar and Volasys Silverstar as IT-worker front companies, and was set out systematically in the2022 joint advisoryof the US Departments of State and the Treasury and the FBI.

Their number isestimated in the thousands, operating both within and beyond the DPRK's borders and systematically obfuscating their location and identity in order tosecure contracts in the IT sector. Such employment serves as leverage in two respects: it enables theremittance of salariesto the regime, and it affords privileged access from which toconduct operationsfor financial gain or espionage.

Cross-referencingopen-source reportingwithstealer logssurfaced the profiles of IT workers themselves, indicating that they draw on the same infrastructure as the operators conducting intrusions.Infiltration appears in part opportunistic rather than target-driven. In the cases observed, workers queried internal corporate documentation while nominally engaged as employees, and reproduced the same behavior within client organizations where they can be deployed as remote consultants. This placement model allows them to extendtheir reachbeyond the entity that contracted them.

DPRK IT workers units identified in stealer logs and leaks

The workers are organized into units embedded across aheterogeneous range of host entities: DPRK military and state institutions, state-owned enterprises, front companies, legitimate businesses abroad, and universities. Although the units from which they operate are not concentrated within a limited set of characteristic organizations, it can nonetheless be monitored through theirmeans of communication, which are considerably more constrained. Three channels can be distinguished:

* Chat platforms, mainlySlackandIP Messenger(IPmsg);
* Machines designatedPC-call;
* A proxy operated byRyonbongand marked as "RB".

An interesting inflection point in these communications can be situated around October 2022. Internal exchanges, previously conducted in Korean and in a markedly formal register, thereaftershifted to English, a change assessed to follow a directive, and consistent with aligning working practices to international norms while reducing the distinctiveness of the workers' online presence.

Internal policy on internet access likewise appearsconsiderably more permissivethan for the ordinary DPRK citizen: identified users adopt working pseudonyms drawn from Western, South Korean and Japanese popular culture (G-Dragon, Superman, James Bond, Harry Potter, Olaf, Kisame). The practice presupposes a degree of cultural exposure, and a latitude in displaying it, unavailable to the general population.

Recruitment into IT workers roles follows aformalized selection process, notably documented by theKorea Institute for National Unification, which indicates that access to the function is far from open to the general population. Candidates must first satisfy vetting on political and social background, both their own (songbun) and that of their family (todae), before they can be considered for overseas deployment. Individuals with relatives resident abroad are excluded from selection outright, and a substantial proportion of those eventually dispatched have prior employment in Pyongyang or other major cities. At the final stage, candidates seeking a particular destination are expected to pay for it, the scale of the bribe varying with the nature of the mission to which they are assigned.

IT workers' recruitment process

Stealer logs indicate that selection is followed by astructured onboarding phase. The material recovered covers the workers' assigned objectives, prescribed means of communication, the platforms to be used in conducting fraudulent activity, and a body of development-related reference questions. The presence of such material suggests that workers enter the programme with little or no direct exposure to the outside world, and that the requisite operational and cultural knowledge is supplied at induction rather than presupposed.

DPRK Fake IT worker onboarding

The primary function of DPRK IT workers is thegeneration of revenuefor the regime, directed towards circumventing international sanctions and financing its ballistic missile and nuclear programmes. The restrictions on DPRK labor abroad were introduced incrementally by the United Nationsthrough 2017:decision UNSCR 2371capped worker numbers at existing levels;the decision UNSCR 2375barred the issuance of new work authorisations ; andthe decision UNSCR 2397required the repatriation of all DPRK nationals earning income in member states' territories by 22 December 2019.

The cumulative effect was to remove any lawful basis for employing DPRK labor abroad. However, aseach obligation is linked to nationality, concealing this fact at the time of recruitment places the transaction outside the scope of the ban, at least from the employer’s perspective. The IT workers model therefore relies on theuse of a false identityduring recruitment, and on thelaundering of the resulting profits. Documented conversion methodsinclude:

* Converting stolen assetsvia centralized exchanges or OTC trades, using proxy accounts run by local facilitators to bypass Know Your Customer (KYC) checks;
* Exploitingdecentralized exchangeswith weak ID verification to swap stolen assets for other cryptocurrencies, followed by cashing out to fiat;
* Conducting crypto-to-cash trades onpeer-to-peer (P2P) platforms, splitting large amounts into smaller, staggered transactions to avoid detection.

Alongside APT groups, DPRKIT workersare alsofoundto be engaging in cryptocurrency thefts. Some documented instances includeOnyxDAO($3.8 million),Munchables($62.5 million) and Exclusible Penthouse ($827,000). It is interesting to note that in one of the theft operations in (Munchables 2024), funds stolen by probable IT workers were ultimately returneddue to operational challengesfaced in the laundering process.

‍

## Enabling ecosystem: Indirect and supporting entities

As a heavily sanctioned country, the DPRK has constructed a complex network of intermediaries, whethereducational, entrepreneurial, or criminal, toenableits cyber offensive operations. These intermediaries fall into two broad categories.

The first is educational institutions, which serve adual purpose.They train the DPRK's cyber operatives, and, in the later stages of education, they function asoperational nodesfor offensive activity, particularly when located in allied countries such as China or Russia.

The second is a web of third-country relays and enterprises. These help the DPRK overcome domestic technical constraints related to infrastructure and networks, enable plausible deniability, and serve as financial relays to circumvent sanctions.

### Educational institutions

#### North Korean educational institutions

North Korean Institutes are the first stepping stone in the training of cyber operators, starting as early as primary school. The brightest students, aged 11 to 17, arefunneledthrough elite, specialized educational institutions likeKumsong Middle Schoolslocated in the capital, before advancing toKim Il-sung University and Kim Chaek University of Technologyto begin their training as “cyber warriors”. Other colleges likeHamhungandMoranbongfocus on cyber engineering, giving students roughlyten yearsof training by graduation.

In exchange, families getperkslike Pyongyang relocation and extra rations. At university, top performers are chosen for advanced hacking training, thencommissionedinto the KPA'sGRIB(ex-RGB) or placed in IT units under theMunitions Industry Department (MID)orMinistry of National Defense (MND). This process can be observed in the following talent pipeline.

DPRK talent pipeline

Beyond this internal talent recruitment process, the DPRK also relies on exchanges with foreign universities to train its operators. These exchanges also serve asoperational channelsthanks to the close ties between the DPRK and the host country. This is particularly evident in the cases of China and Russia.

#### Academic exchanges between North Korea and the PRC

North Korea and China have historically maintained close-relations, owing to asharedhistory of communist movements. Today, China remains one of North Korea’s closest allies despite atumultuousrelationship. Thus, it is not surprising that formal training and access to resources for DPRK cyber talent is also provided througha network of universitiesin China.

During our investigation, we found mentions of several Chinese universities in stealer logs of DPRK IT workers, includingShanghai University of Electric Power,Chongqing UniversityandBeijing Institute of Technology.The complete list of universities can be found in Annex 1. According to official diplomaticcommunications,“DPRK students at institutions such as Jilin University and Yanbian University gain insights from China’s reform and opening-up, and advancements in science and technology, which they bring back to their country”.

However, these universities are known to host DPRK-nexus malicious actors, for instance injoint researchcentre facilities, and offer them operational stability.

North Korea has also replicated this strategic model in Russia to expand its operational footprint, especially as Beijing increasingly seeks todistance itselffrom North Korea to avoid Western sanctions.

#### Academic exchanges between North Korea and Russia

Alongside thestrengtheningof long-existing ties between Russia and North Korea, educational exchanges between these two countries alsoexpanded quicklysince the former’s 2022 invasion of Ukraine. This is highlighted by mandatory Russian language schooling in the DPRK, increased university scholarships, and high-level academicdelegationvisits.

Indeed, Russian is now acompulsory subjectin DPRK schools from the 4th grade onward. According to Alexander Kozlov, co-chair of theintergovernmental commission of the Russian Federation and North Korea, 96 North Korean citizens were accepted to Russian universities. Furthermore, Russiagrantedover 36,000 entry visas to North Koreans in 2025 (a fourfold increase from 2024) among which over 98% were for education. Thesecloser tieswith Moscow are likely used to uplift Kim Jong un’s domestic image as a strong leader.

We observe that a key difference between the DPRK's exchanges with Russia and China lies invisa transparency: As of August 2026, Russia haspublicly discloseddetailed data on visas issued to North Korean nationals, while China has not. This asymmetry might reflect, in part, China'stactical ambiguity, which aims toavoidbeing drawn into the conflict the DPRK faces with the West.

Finally, it is crucial to note that while these exchanges likely include some training and knowledge-sharing with partners who have well-developed cyber offensive ecosystems, such as China and Russia, theirprimary aimis togain access to third-country networksin order to conduct cyber offensive operations.

### Front companies and money laundering hubs

North Korea often obscures itsoperational originsby leveragingoverseas intermediaries, particularlyphysical relay networksas channels for conducting cyber operationsandcriminal enterprisesfor laundering illicit funds.

Firstly, this allows the regime tocompensate for its limited domestic internet infrastructure(2 325 IPS and 1 ASNin the DPRK, compared to 344 902 269 IPs and 6 656 ASNsin China)by rerouting attacks throughrelay networksin allied countries like China and Russia. Secondly, it allows for a web of state-sponsored, private and criminal actors tocooperateandgenerate revenuefor the regime while evading sanctions.

#### Physical relay networks

Physical relay networks have not only served as a financial and infrastructuralchannel, but also as aphysical basefor DPRK cyber operations. In this context, physical relay network refers to overseas hubs, such as offices, hotels, or front companies staffed or frequented by DPRK operatives, that provide a base outside North Korea for conducting operations and generating revenue.

These operational networks are notably located in China, Russia, Southeast Asia, and certain African countries. Among them, China stands out, given its status as a historical partner of Pyongyang. These intermediaries can be bothfrontsorlegitimate businesseswith operators working for North Korea abroad.  For instance, amemberof the Lazarus Group was associated withChosun Expo, which is a North Koreanfront companybased in China. Additionally, operatives from Bureau 121, allegedly responsible for the 2014 Sony hack, were speculated to beworkingfromChilbosan Hotel in Shenyang, Chinaduring the operation. These methods were likely used to enable North Korea to plausibly deny its cyber operations.

Yet another example isChinyong Information Technology Cooperation Company (Chinyong), a sanctioned North Korean enterprise subordinated to the Ministry of People's Armed Forces (KPe.054), active since at least 2016. The enterprise isinvolvedin theemployment of DPRK IT workersoverseas and the generation ofillicit revenueabroad. Chinyong’s teams are primarily known tooperateout of China, Laos, and Russia, where they engage in “traditional” freelance IT work, as well as in cryptocurrency theft using their insider access to blockchain projects.

In the African continent, DPRKfront companiessuch asJunggongchon Trading Corporationare known to deploy IT worker teams in countries likeTanzania. According to theChollima group, DPRK operatives are also likely deployed inGuineaandNigeriathrough similar fronts.

At times, this physical infrastructure extends into the target countries themselves. In the United States, there were documented cases of “laptop farms”, which are third-party proxies used by DPRK IT workers to receive company-issued laptops, allowing them to appear as though they are working from within the US while operating from abroad.

Of note, physical relay networks are not only used by rank-and-file IT workers who are deployed abroad, but also byAPT operators.For instance, Kudelski Securityobservedthat fake IT workers and offensive teams often share the same VPN exit nodes. It is thus plausible that these operators either conduct cyber operations alongside their ostensible day-to-day work or, in the case of front companies, do so on afull-time basis, coordinating with counterparts based inside the DPRK.

#### Criminal enterprises

The DPRK hashistoricallyexploitedunderground criminal systemsto support state-building activities. Until the late 2010s, the most lucrative state-sponsored criminal operations included the smuggling of cigarettes and the creation of counterfeit money. Following the DPRK's pivot toward cyber operations as a source of illicit revenue, DPRK-nexus intrusion sets have applied a similar playbook to launder the proceeds of their operations.

These actors launder funds through criminal networks notably across Southeast Asia byactively exploitingthe region’s vulnerable and weakly-regulated financial environment linked to local illicit actors. In particular, casinos and cryptocurrency exchanges withhigh-volume cash conversion channelsinMyanmar, Thailand, Laos, and Cambodiahave served as key operational nodes formoney laundering.

Cambodia, in particular, has emerged as a laundering hub due to its less regulated financial and gambling sectors, with an estimated$37.6 millionin North Korea-linked cryptocurrency laundered between 2021 and 2025 through the Cambodia-basedHuione Group, whoseexecutiveshave shown indications of direct ties to North Korean actors. Huione's infrastructure, including technical tools that facilitate scams andstablecoinsthat cannot be frozen, has allowed North Korea to bypass regulations, convert illicit proceeds into ostensibly legitimate assets, andsustain revenue generationfrom its cyber operations.

## Conclusion

The DPRK's offensive cyber apparatus is not an adjunct to the regime's strategy but a constituent part of it. Most states maintain cyber capabilities for intelligence collection and military contingency, Pyongyang has additionally constituted them as a source of state revenue, notably to fund its nuclear and ballistic missile programmes, and that model has proven durable under sustained international pressure. The intrusion sets examined in this paper and the IT worker programme operating alongside them both serve this dual purpose.

Several conclusions can be drawn. First, the institutional map isunstable. Mandates are redistributed between bureaus, organs are periodically reorganized, and certain entities operate transversally rather than within the hierarchy. Ryonbong is a great example: its formal position within the defense-industrial structure does not necessarily translate its operational responsibility in IT workers’ campaigns.

Second, the IT worker programme fits awkwardly within conventional threat intelligence frameworks. It works like acriminal enterprise: the units are dispersed across a heterogeneous range of host entities, with the end goal of making profit. They use cyber means, but also fake identities, fraud schemes and lures to channel foreign currencies to the regime.

Third, the distinction between espionage and revenue generation is less firm than it appears. Access acquired for financial purposes has been turned to collection, and the same infrastructure appears to serve both. On the other hand, intelligence units self-fund their operations, conducting lucrative campaigns at the margin.

Aliases proliferate, clusters are divided and consolidated differently across vendors. However, what endures is the understanding of how the DPRK operates. Indeed, the history of these clusters and following their successive reconfigurations, alongside their characteristic tradecraft and motivations can help defenders to better monitor and anticipate the threat posed by Pyongyang operators. This paper is intended to support that approach.

DPRK Cyber Capabilities Organization

‍

# Annexes

### Annex 1 - North Korean university acronyms found on stealer logs and leaks

 
 
 
 
North Korean university's acronym or nickname
 
Meaning and affiliation
 
Confidence level of the meaning
 
 
 
 
 
HUCE
 
Hamhung Chemical Industry University
Contain a Fake IT worker cell
 
HIGH
 
 
 
PUCR
 
Pyongyang University of computer science
Contain a Fake IT worker cell
 
LOW
 
 
 
PUCS
 
Pyongyang University of computer science Information Exchange Company.
Contain a Fake IT worker cell
 
HIGH
 
 
 
UOS
 
University of Science
Contain a Fake IT worker cell
 
MEDIUM
 
 
 
Trans Univ
 
Pyongyang University of Transport - Contain a Fake IT worker cell
 
MEDIUM
 
 
 
KUT
 
Kim Chaek University of Technology
Contain a Fake IT worker cell
 
HIGH
 
 
 
PUG
 
Unknown - Likely contain an attack infrastructure
 
Unknown
 
 
 
HUT
 
Huichon University of Telecommunications
Contain a Fake IT worker cell
 
LOW
 
 
 
PAU
 
Pyongyang University of Automation
Contain a Fake IT worker cell
 
MEDIUM
 
 
 
Univ JN
 
Jinung Institute of IT Development - Kim Il Sung university
Contain a Fake IT worker cell
 
HIGH
 
 
 
Print University
 
Pyongyang University of Printing Engineering
Contain a Fake IT worker cell
 
MEDIUM
 
 
 
Nampho Ship
 
University of Nampo ship
Contain a Fake IT worker cell
 
HIGH
 
 
 
PYITC
 
Pyongyang Information Technology Center
 
MEDIUM
 
 
 

‍

### Annex 2 - Overlap between fake IT workers and DPRK offensive campaigns

Annex 2. Overlap between fake IT workers and DPRK offensive campaigns

IP exit node used by DPRK fake IT workers

Campaign and cluster source

Source

23[.]237[.]102[.]130

37[.]120[.]154[.]98

38[.]75[.]137[.]97

45[.]86[.]208[.]162

50[.]7[.]159[.]34

91[.]239[.]130[.]102

103[.]214[.]44[.]138

167[.]88[.]61[.]117

185[.]135[.]76[.]89

188[.]43[.]33[.]252

211[.]21[.]6[.]181

 Contagious Interview

(Recorded Future)

Recorded Future

45[.]86[.]208[.]162

70[.]32[.]3[.]15

 Contagious Interview

(SentinelOne)

SentinelOne

66[.]118[.]255[.]35

 Bybit attack

(Silent Push)

Silent Push

## External references

The Reconnaissance General Bureau: The Kim Regime’s “Precious Treasured Sword” – The Committee for Human Rights in North Korea, February 2026 –https://www.hrnk.org/documentations/the-reconnaissance-general-bureau-the-kim-regimes-precious-treasured-sword/

The All-Purpose Sword: North Korea’s Cyber Operations and Strategies – IEEE, May 2019 –https://ieeexplore.ieee.org/document/8756954/

White Paper on Human Rights in North Korea 2023 –  Korea Institute for National Unification) –https://www.kinu.or.kr/eng/module/report/view.do?idx=125351&nav_code=eng1674806000

Hidden Enablers: Third Countries in North Korea’s Cyber Playbook – July 2025 –https://www.csis.org/analysis/hidden-enablers-third-countries-north-koreas-cyber-playbook

North Korea’s Constitutional Amendments Cement the Regime’s Strategic Posture – Institute for the Study of War, June 2026 –https://understandingwar.org/research/china-taiwan/north-koreas-constitutional-amendments-cement-the-regimes-strategic-posture/

North Korea’s Economic Policy in 2018 and Beyond: Reforms Inevitable, Delays Possible - 38 North: Informed Analysis of North Korea – 38 North, August 2018 –https://www.38north.org/2018/08/rfrank080818/

Quick Take: The Leader Gets a Strong Constitution - 38 North: Informed Analysis of North Korea – 38 North, May 2026 –https://www.38north.org/2026/05/quick-take-the-leader-gets-a-strong-constitution/

Youth as torchbearers of China-North Korea relations –https://asianews.network/youth-as-torchbearers-of-china-north-korea-relations/

North Korea-Russia People-to-People Exchanges as a Tool for Sustained Dialogue - 38 North: Informed Analysis of North Korea – 38 North, June 2025 –https://www.38north.org/2025/06/north-korea-russia-people-to-people-exchanges-as-a-tool-for-sustained-dialogue/

2025 Crypto Theft Reaches $3.4 Billion – Chainalysis, December 2025 –https://www.chainalysis.com/blog/crypto-hacking-stolen-funds-2026/

Analysis of DPRK-Linked Money Laundering Infrastructure –https://s2w.inc/en/resource/detail/1090

How DPRK’s Contagious Interview Campaign Targets Developers - Kudelski Security Research Center –https://kudelskisecurity.com/research/how-dprks-contagious-interview-campaign-targets-developers

How North Korea’s Hackers Became Dangerously Good - WSJ –https://www.wsj.com/articles/how-north-koreas-hackers-became-dangerously-good-1524150416

Internal Security and IC Changes | North Korea Leadership Watch –https://www.nkleadershipwatch.org/2026/06/05/internal-security-and-ic-changes/

KillDisk now targeting Linux: Demands $250K ransom, but can’t decrypt –https://www.welivesecurity.com/2017/01/05/killdisk-now-targeting-linux-demands-250k-ransom-cant-decrypt/

Organization Guidance Department and WMD Program | North Korea Leadership Watch –https://www.nkleadershipwatch.org/the-party/organization-guidance-department-and-wmd-program/

Thread on exfiltrated North Korean payment server data – @zachxbt, April 2026https://x.com/zachxbt/status/2041873508180095032

S/RES/2371 2017 | Security Council –https://main.un.org/securitycouncil/en/s/res/2371-%282017%29

S/RES/2397 2017 | Security Council –https://main.un.org/securitycouncil/en/s/res/2397-%282017%29

South Korean researchers uncover another cyber-espionage campaign from the North –https://therecord.media/apt37-scarcruft-cyber-espionage-campaign-south-korea

The DPRK’s Violation and Evasion of UN Sanctions through Cyber and Information Technology Worker Activities –https://msmt.info/Publications/detail/MSMT%20Report/4221

Chinyong Information Technology Cooperation Company – OpenSanctions.org, May 2023 –https://www.opensanctions.org/entities/NK-37t8mDJBBsxKzZxfhW8Qo2/

Third Bureau of the Reconnaissance General Bureau – OpenSanctions.org, August 2023 –https://www.opensanctions.org/entities/kprusi-3d6e2f6255ea677c2f68d1508bd161d2a3645db8/

Munchables hacker returns $62.8M Ether without ransom – Cointelegraph, March 2024 –https://cointelegraph.com/news/munchables-hacker-returns-ether-without-ransom

Onyx protocol exploited a second time for $3.8M via known bug – TradingView, September 2024 –https://www.tradingview.com/news/cointelegraph:5ca7f0869094b:0-onyx-protocol-exploited-a-second-time-for-3-8m-via-known-bug/

FinCEN Finds Cambodia-Based Huione Group to be of Primary Money Laundering Concern, Proposes a Rule to Combat Cyber Scams and Heists | FinCEN.gov – May 2025 –https://www.fincen.gov/news/news-releases/fincen-finds-cambodia-based-huione-group-be-primary-money-laundering-concern

North Korea makes Russian mandatory in schools – POLITICO, November 2025 –https://www.politico.eu/article/north-korea-russia-mandatory-school-mgimo/

Treasury Sanctions Clandestine IT Worker Network Funding the DPRK’s Weapons Programs – U.S. Department of the Treasury, June 2026 –https://home.treasury.gov/news/press-releases/sb0205

Treasury Sanctions DPRK Bankers and Institutions Involved in Laundering Cybercrime Proceeds and IT Worker Funds – U.S. Department of the Treasury, June 2026 –https://home.treasury.gov/news/press-releases/sb0302

Treasury Targets DPRK Malicious Cyber and Illicit IT Worker Activities – U.S. Department of the Treasury, June 2026 –https://home.treasury.gov/news/press-releases/jy1498

Treasury Targets IT Worker Network Generating Revenue for DPRK Weapons Programs – U.S. Department of the Treasury, June 2026 –https://home.treasury.gov/news/press-releases/jy2790

DEF CON 33 - Blurred Lines: Evolving Tactics of North Korean Cyber Threat Actors - Seongsu Park – October 2025 –https://www.youtube.com/watch?v=j5gxdWd5sMg

Kim Jong Un labels South Korea as ‘No. 1 hostile country’ – The Chosun Daily, January 2024 –https://www.chosun.com/english/north-korea-en/2024/01/16/NZ2TGZIDRJDG3MYB6Z5ZUXFDYM/

‘As close as lips and teeth’: The highs and lows of China-North Korea ties – Al Jazeera –https://www.aljazeera.com/news/2026/6/9/as-close-as-lips-and-teeth-the-highs-and-lows-of-china-north-korea-ties

Inter-Korean Rivalry in the Cyber Domain: The North Korean Cyber Threat in the “Sŏn’gun” Era – Georgetown University Press, 2016 –https://www.jstor.org/stable/26395976

APT38 | New North Korean Regime-Backed Threat Group | Google Cloud Blog –https://cloud.google.com/blog/topics/threat-intelligence/apt38-details-on-new-north-korean-regime-backed-threat-group?hl=en

At North Korean hub in China, uncertainty looms for Pyongyang-backed businesses | Reuters –https://www.reuters.com/article/world/at-north-korean-hub-in-china-uncertainty-looms-for-pyongyang-backed-businesses-idUSKBN1DV3S1/

DPRK Fake IT Workers: Inside Their Evolving Network Infrastructure - Kudelski Security Research Center –July 2026–https://kudelskisecurity.com/research/dprk-fake-it-workers-inside-their-evolving-network-infrastructure

Russia issued over 36K visas to North Koreans in 2025, almost all for education | NK News –April 2026 –https://www.nknews.org/2026/04/russia-issued-over-36k-visas-to-north-koreans-in-2025-almost-all-for-education/

S/RES/2375 2017 | Security Council –https://main.un.org/securitycouncil/en/s/res/2375-%282017%29

The Incredible Rise of North Korea’s Hacking Army | The New Yorker –April 2021 –https://web.archive.org/web/20210903030018/https://www.newyorker.com/magazine/2021/04/26/the-incredible-rise-of-north-koreas-hacking-army

The Strategic Partnership Agreement between Russia and North Korea - Georgian Foundation for Strategic and International Studies (Rondeli Foundation)  –https://gfsis.org/en/the-strategic-partnership-agreement-between-russia-and-north-korea/

국정원 “DDoS 공격 비상대응체제 가동중” - 정책뉴스 | 뉴스 | 대한민국 정책브리핑 –https://www.korea.kr/news/policyNewsView.do?newsId=148673043

Russia–North Korea Military Cooperation in Response to China’s Tactical Ambiguity | Asia Society – June 2026 –https://asiasociety.org/policy-institute/russia-north-korea-military-cooperation-response-chinas-tactical-ambiguity

Thread on the leak of North Korean IT workers’ email addresses – @SttyK, August 2025https://x.com/SttyK/status/1956180410104471917

The Lazarus Constellation – Lexfo, February 2020https://blog.lexfo.fr/ressources/Lexfo-WhitePaper-The_Lazarus_Constellation.pdf

Hudson Rock – Infostealer Intelligence Solutionshttps://www.hudsonrock.com/

## Read our latest blog articles

AI
SOC Insights & Other News
Product News
August 31, 2026

### AI SOC agents are only as good as the context they can see

AI SOC agents need more than an alert to investigate threats. See how telemetry, asset data, identities and threat intelligence help explain each verdict.

By
David Greenwood
View more

Threat Research & Intelligence
TDR Team
APT
September 7, 2026

### Beyond Lazarus: Organization of DPRK cyber capabilities

Get the full overview of North Korea's cyber operations, from state institutions and APT clusters to IT workers units, and enablers.

By
TDR Team
By
Saee V.
By
Coline C.
By
Clifford
View more

AI
Product News
SOC Insights & Other News
August 27, 2026

### AI transparency in cybersecurity: How Sekoia handles customer data

Security teams are being asked to trust AI with work that used to belong to experienced analysts. So how can they decide if it’s earned its place there?

By
Antoine Heuzé
By
Charles Ngor
View more