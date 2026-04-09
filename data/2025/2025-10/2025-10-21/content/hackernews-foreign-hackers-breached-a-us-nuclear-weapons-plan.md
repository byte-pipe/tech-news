---
title: Foreign hackers breached a US nuclear weapons plant via SharePoint flaws | CSO Online
url: https://www.csoonline.com/article/4074962/foreign-hackers-breached-a-us-nuclear-weapons-plant-via-sharepoint-flaws.html
site_name: hackernews
fetched_at: '2025-10-21T19:08:03.457720'
original_url: https://www.csoonline.com/article/4074962/foreign-hackers-breached-a-us-nuclear-weapons-plant-via-sharepoint-flaws.html
author: zdw
date: '2025-10-21'
description: A foreign actor infiltrated the National Nuclear Security Administration’s Kansas City National Security Campus through vulnerabilities in Microsoft’s SharePoint browser-based app, raising questions about the need to solidify further federal IT/OT security protections.
---

by
Cynthia Brumfield

Contributing Writer

# Foreign hackers breached a US nuclear weapons plant via SharePoint flaws

News Analysis

Oct 20, 2025
8 mins
Cyberattacks
Data Breach
Government IT


## A foreign actor infiltrated the National Nuclear Security Administration’s Kansas City National Security Campus through vulnerabilities in Microsoft’s SharePoint browser-based app, raising questions about the need to solidify further federal IT/OT security protections.



							Credit: 															Wirestock Creators / Shutterstock

A foreign threat actor infiltrated theKansas City National Security Campus (KCNSC), a key manufacturing site within the National Nuclear Security Administration (NNSA), exploiting unpatched Microsoft SharePoint vulnerabilities, according to a source involved in an August incident response at the facility.

The breach targeted a plant that produces the vast majority of critical non-nuclear components for US nuclear weapons under the NNSA, a semi-autonomous agency within the Department of Energy (DOE) that oversees the design, production, and maintenance of the nation’s nuclear weapons. Honeywell Federal Manufacturing & Technologies (FM&T) manages the Kansas City campus under contract to the NNSA.

The Kansas City campus, Honeywell FM&T, and the Department of Energy did not respond to repeated requests for comment throughout September, well before the current government shutdown. NSA public affairs officer Eddie Bennett did respond, saying, “We have nothing to contribute,” and referred CSO back to the DOE.

Although it is unclear whether the attackers were a Chinese nation-state actor or Russian cybercriminals — the two most likely culprits — experts say the incident drives home the importance of securing systems that protect operational technology from exploits that primarily affect IT systems.

## How the breach unfolded

The attackers exploitedtwo recently disclosed Microsoft SharePoint vulnerabilities— CVE-2025-53770, a spoofing flaw, and CVE-2025-49704, a remote code execution (RCE) bug — both affecting on-premises servers. Microsoftissued fixesfor the vulnerabilities on July 19.

On July 22, the NNSAconfirmedit was one of the organizations hit by attacks enabled by the SharePoint flaws. “On Friday, July 18th, the exploitation of a Microsoft SharePoint zero-day vulnerability began affecting the Department of Energy,” a DOE spokesperson said.

However, the DOE contended at the time, “The department was minimally impacted due to its widespread use of the Microsoft M365 cloud and very capable cybersecurity systems. A very small number of systems were impacted. All impacted systems are being restored.”

By early August, federal responders, including personnel from the NSA, were on-site at the Kansas City facility, the source tells CSO.

Located in Missouri, theKCNSC manufacturesnon-nuclear mechanical, electronic, and engineered material components used in US nuclear defense systems. It also provides specialized technical services, including metallurgical analysis, analytical chemistry, environmental testing, and simulation modeling.

Roughly 80% of the non-nuclear parts in the nation’s nuclear stockpileoriginate from KCNSC. While most design and programmatic details remain classified, the plant’s production role makes it one of the most sensitive facilities in the federal weapons complex.

## China or Russia? Conflicting attribution

Microsoftattributed the broader wave of SharePoint exploitationsto three Chinese-linked groups: Linen Typhoon, Violet Typhoon, and a third actor it tracks as Storm-2603. The company said the attackers were preparing to deploy Warlock ransomware across affected systems.

However, the source familiar with the Kansas City incident tells CSO that a Russian threat actor, not a Chinese one, was responsible for the intrusion. Cybersecurity company Resecurity, which was monitoring the SharePoint exploitations, tells CSO that its own data pointed primarily to Chinese nation-state groups, but it does not rule out Russian involvement.

Resecurity’s researchers say that while Chinese groups appeared to have developed and deployed the initial zero-day, financially motivated Russian actors may have independently reproduced the exploit before technical details began circulating in late June.

In May, researchers at Viettel Cyber Securitydemonstrated an attack chaining two SharePoint flaws, CVE-2025-49706 and CVE-2025-49704, at Pwn2Own Berlin. Resecurity researchers tell CSO that those demonstrations likely accelerated the reverse-engineering of the vulnerabilities by multiple threat actors.

Resecurity’s analysts observed early-stage scanning and exploitation activity from infrastructure located in Taiwan, Vietnam, South Korea, and Hong Kong, a distribution pattern consistent with tactics used by Chinese advanced persistent threat (APT) groups to disguise attribution.

“The root cause of the SharePoint exploitation is closely related to misuse of the Microsoft Active Protections Program (MAPP) by China,” Resecurity researchers tell CSO. “The most probable perpetrators are Chinese nation-state actors such as Linen Typhoon and Violet Typhoon.”

Still, they say that yet another way that Russia-based threat actors could have acquired knowledge of the vulnerability early on was through underground exchanges or by analyzing network scanning data once the exploit became known. Thetransition from zero-day to N-day status, they say, opened a window for secondary actors to exploit systems that had not yet applied the patches.

## Could the attack have reached operational systems?

The breach targeted the IT side of the Kansas City campus, but the intrusion raises the question of whether attackers could have moved laterally into the facility’s operational technology (OT) systems, the manufacturing and process control environments that directly support weapons component production.

OT cybersecurity specialists interviewed by CSO say that KCNSC’s production systems are likely air-gapped or otherwise isolated from corporate IT networks, significantly reducing the risk of direct crossover. Nevertheless, they caution against assuming such isolation guarantees safety.

“We have to really consider and think through how state actors potentially exploit IT vulnerabilities to gain access to that operational technology,”Jen Sovada, general manager of public sector operations at Claroty, speaking generally and not about the specific incident, tells CSO.

“When you have a facility like the KCNSC where they do nuclear weapons lifecycle management — design, manufacturing, emergency response, decommissioning, supply chain management — there are multiple interconnected functions,” Sovada says. “If an actor can move laterally, they could impact programmable logic controllers that run robotics or precision assembly equipment for non-nuclear weapon components.”

Such access, Sovada adds, could also affect distribution control systems that oversee quality assurance, or supervisory control and data acquisition (SCADA) systems that manage utilities, power, and environmental controls. “It’s broader than just an IT vulnerability,” she says.

## IT/OT convergence and the zero-trust gap

The Kansas City incident highlights a systemic problem across the federal enterprise: the disconnect between IT and OT security practices. While the federal government has advanced its zero-trust roadmap for traditional IT networks, similar frameworks for operational environments have lagged, although recent developments point to progress on that front.

“There’s anIT fan chartthat maps all of the controls for zero trust, segmentation, authentication, and identity management,” Sovada says. “But there’s also anOT fan chartbeing developed by the Department of Defense that will define comparable controls for zero trust in operational technology. The goal is to marry the two, so that zero trust becomes comprehensive across all network types.”

That alignment, she says, is essential to preventing intrusions like the one that struck KCNSC from cascading into physical operations.

## Even non-classified data theft holds strategic value

If the source’s claim of Russian involvement is accurate, the attackers may have been financially motivated ransomware operators rather than state intelligence services. But even in that scenario, the data they accessed could still carry strategic value.

“It would make sense that if it were a ransomware actor and they got this kind of data about nuclear weapons manufacturing, they might pause and hand it off to the appropriate Russian government officials or experts,” Sovada tells CSO.

Although there is no evidence that classified information was compromised, even unclassified technical data can have significant implications. “It could be something as simple as requirements documents that may not be classified but reveal the level of precision required for components,” Sovada says. “In weapons manufacturing, a millimeter difference can change a device’s trajectory or the reliability of its arming mechanism.”

Such information could aid adversaries in understanding US weapons tolerances, supply chain dependencies, or manufacturing processes, all of which are sensitive even if not formally secret.

Whether the intruders were Chinese state actors or Russian cybercriminals, the Kansas City breach exposes the fragile intersection of IT and operational security across critical defense infrastructure. As Sovada stresses, “We can’t just think of zero trust as an IT concept anymore. It has to extend into the physical systems that underpin national defense.”

Update: The Department of Energy (DOE)confirmedthat it is furloughing the vast major of the NNSA’s workers. DOE spokesperson said, “Since its creation in 2000, NNSA has never before furloughed federal workers during funding lapses. We are left with no choice this time. We’ve extended funding as long as we could.”





				SUBSCRIBE TO OUR NEWSLETTER

### From our editors straight to your inbox

				Get started by entering your email address below.



Please enter a valid email address

Subscribe

														by

																Cynthia Brumfield

Contributing Writer

Cynthia Brumfield is a veteran communications and technology analyst who is currently focused on cybersecurity. She runs a cybersecurity news destination site,Metacurity.com, consults with companies through her firm DCT-Associates, and is the author of the book published by Wiley,Cybersecurity Risk Management: Mastering the Fundamentals Using the NIST Cybersecurity Framework.Cynthia holds a Master of Planning Degree from the University of Virginia and a Bachelor’s degree from The George Washington University. She has won multiple AZBEE awards for her work on CSO, including two in 2025.

## More from this author

* news### AI-enabled ransomware attacks: CISO’s top security concern — with good reasonOct 21, 20255 mins
* news analysis### Government shutdown deepens US cyber risk, exposing networks to threat actorsOct 1, 20256 mins
* news analysis### CISA 2015 cyber threat info-sharing law lapses amid government shutdownOct 1, 20257 mins
* news analysis### Qantas cutting CEO pay signals new era of cyber accountabilitySep 26, 20256 mins
* news### CrowdStrike bets big on agentic AI with new offerings after $290M Onum buySep 16, 20258 mins
* news analysis### Whistleblower: DOGE put Social Security database covering 300 million Americans on insecure cloudAug 27, 20259 mins
* news### Storm-0501 debuts a brutal hybrid ransomware attack chainAug 27, 20255 mins
* feature### Behind the Coinbase breach: Bribery emerges as enterprise threatAug 26, 20259 mins


## Show me more

Popular
Articles
Podcasts
Videos

news



### Google kills its cookie killer


By Maxwell Cooter
Oct 21, 2025
4 mins

Browser Security
Endpoint Protection
Marketing and Advertising Industry

news



### Security patch or self-inflicted DDoS? Microsoft update knocks out key enterprise functions


By Taryn Plumb
Oct 21, 2025
6 mins

Data and Information Security
Encryption
Windows Security

feature



### CISOs’ security priorities reveal an augmented cyber agenda


By Esther Shein
Oct 21, 2025
11 mins

C-Suite
CSO and CISO
IT Strategy

podcast



### CSO Executive Sessions: Leading the Charge on Cyber Agility for Southeast Asia’s Digital Future


By Estelle Quek
Oct 2, 2025
21 mins

Cloud Security
Cyberattacks
Threat and Vulnerability Management

podcast



### CSO Executive Session ASEAN: Navigating the Cyber Battleground, Strengthening Southeast Asia’s Digital Defense


By Estelle Quek
Sep 23, 2025
41 mins

Cyberattacks
Cybercrime
Threat and Vulnerability Management

podcast



### CSO Executive Session ASEAN: Navigating sophisticated cyberthreats in Southeast Asia region


By Estelle Quek
Sep 16, 2025
48 mins

Cybercrime
Ransomware

video



### CSO Executive Sessions: Leading the Charge on Cyber Agility for Southeast Asia’s Digital Future


By Estelle Quek
Oct 2, 2025
21 mins

Cloud Security
Cyberattacks
Threat and Vulnerability Management

video



### CSO Executive Session ASEAN: Navigating the Cyber Battleground, Strengthening Southeast Asia’s Digital Defense


By Estelle Quek
Sep 23, 2025
41 mins

Cyberattacks
Threat and Vulnerability Management
Zero Trust

video



### CSO Executive Session ASEAN: Navigating sophisticated cyberthreats in the Southeast Asia region


By Estelle Quek
Sep 15, 2025
48 mins

Cybercrime
Ransomware
