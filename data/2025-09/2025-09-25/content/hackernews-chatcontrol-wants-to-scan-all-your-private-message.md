---
title: ChatControl wants to scan all your private messages · Metalhearf's Blog
url: https://metalhearf.fr/posts/chatcontrol-wants-your-private-messages/
site_name: hackernews
fetched_at: '2025-09-25T19:07:44.950634'
original_url: https://metalhearf.fr/posts/chatcontrol-wants-your-private-messages/
author: Metalhearf
date: '2025-09-25'
published_date: '2025-09-25T00:00:00+02:00'
description: The European Union wants to require all messaging platforms to scan private communications.
---

Table of Contents


 Table of Contents


 The European Union wants to force tech companies to scan your private messages & images, even in your favorite encrypted apps.

## Introduction#

The 🇪🇺 European Union is advancing legislation that could fundamentally change how we communicate online.ChatControlwould requireallmessaging platforms to automatically scan their users’ private messages and images.

Yes, even encrypted ones likeSignal,WhatsAppandTelegram.No, you can’t opt out.

This isn’t just another privacy policy update you can ignore. If passed, this EU regulation (strongest and most binding legal instrument in EU law) would automatically apply to all member states without any wiggle room for national interpretation. It would even override constitutional protections for communication privacy and establish unprecedented mass surveillance of private communications.

The official justification? Fightingchild sexual abuse material(CSAM). Protecting children is undeniably crucial, but the proposed methods would eliminate digital privacy for 450 million Europeans and set a global precedent for mass surveillance.

This surveillance trend extends beyond Europe: 🇨🇭 Switzerland is advancing metadata retention requirements, the 🇬🇧 UK is implementing comprehensive age verification systems and now the 🇪🇺 EU proposes to scanevery private message. Each initiative is positioned as child protection policy, but the implications reach far beyond their stated goals.

## What is ChatControl#

ChatControl is what critics call the EU’s proposedRegulation to Prevent and Combat Child Sexual Abuse, also known as CSAR (Child Sexual Abuse Regulation).

The proposal builds on surveillance techniques already deployed by major tech companies. Meta analyzes all Facebook Messenger conversations and unencrypted WhatsApp data (profile photos, group descriptions). Apple announced similar scanning for iCloud content in 2021, though they later suspended the program.

This turns voluntary corporate surveillance into mandatory government-ordered scanning. A temporary 2021 EU regulation allowed platforms to scan content voluntarily for three years. That authorization expired in 2024, which is why CSAR was proposed. The temporary regulation merely permitted scanning; CSAR would make detection obligatory under certain conditions.

There’s also theRoadmap for Lawful Access to Datawhich has an even bigger goal: making all our digital data readable by authorities upon request. We’ll dive deeper into this broader surveillance agenda later.

### Scope and Coverage#

CSAR casts an extremely wide net. The regulation would apply to allinterpersonal communication service providers, not just obvious targets like Signal, WhatsApp, or Telegram, but also:

* Email providers
* Dating apps
* Gaming platforms with chat features
* Social media platforms
* File hosting services (Google Drive, iCloud, DropBox…)
* App stores
* Even small community hosting services run by associations

This means virtually any digital service that allows people to communicate or share content would fall under surveillance requirements. The scope extends far beyond what most people imagine when they hearmessaging apps.

## How it Works#

ChatControl relies onClient-Side Scanning. Your device becomes a monitoring station that analyzes your content before encryption happens.

This represents a fundamental shift away from traditional surveillance that intercepts messages during transmission. With ChatControl, every message gets automatically checked, assuming everyone is guilty until proven innocent and effectively reversing thepresumption of innocence.

### Technical Implementation#

How does Chat Control work?

The system would automatically scan for three categories of contentbeforeencryption:

1. Known illegal content: Images or videos already catalogued by authorities as CSAM. Your device createshash fingerprintsof your content and compares them against databases of known illegal material.
2. Unknown potential content: Photos or videos that might constitute CSAM but haven’t been previously identified. AI algorithms analyze visual elements (like exposed skin) to flag potentially problematic content based on statistical models.
3. Grooming behavior: Text analysis using AI to identify communication patterns that match predefined indicators of adults soliciting children. This involves scanning the actual content of your private conversations.

If something gets flagged, it automatically gets reported to authorities. No human checks it first, that would be impossible given the billions of daily messages. This would be mandatory for all messaging platforms in 🇪🇺 Europe.

### Why This Breaks Encryption#

Claims that
client-side scanning is compatible with encryption
 are misleading.

ChatControldoesn’t break encryption, it bypasses it entirely. While your messages still get encrypted during transmission, the system defeats the purpose of end-to-end encryption by examining your content before it gets encrypted. TrueE2EEmeans only you and your recipient can read messages: no government, no company, no algorithm should peek inside. This surveillance violates that principle by inserting monitoring at the source.

Privacy-focused companies like Protonpoint outthis approach might beworse than encryption backdoors. Backdoors give authorities access to communications you share with others. This system examines everything on your device, whether you share it or not.

Your encrypted messaging app becomes spyware. Supporters claim this protects privacy because scanning happens locally, but surveillance built into your device makes itimpossible to escape.

### Governance Structure#

Quis custodiet ipsos custodes?

The proposal would create a centralizedEU Centre on Child Sexual Abuseto receive all reports, but EU institutions wouldn’t control the scanning technology itself.

Service providers would face additional obligations beyond scanning. They would need to conductrisk assessmentsto evaluate and minimize the potential for illegal content sharing on their platforms. This requires collecting detailed information about their users (age groups, content types) that many privacy-focused services deliberately avoid gathering.

The regulation also pushes for mandatory age verification systems. No viable, privacy-respecting age verification technology currently exists. These systems would eliminate online anonymity, requiring users to prove their identity to access digital services.

Rules for thee, but not for me
: While ordinary Europeans would have all their messages scanned, the proposed legislation includes exemptions for government accounts used for “
national security purposes, maintaining law and order or military purposes
”. Convenient.

## Real-World Impact#

### Encryption Concerns#

ChatControl fits into a broader political strategy. Since the 1990scrypto wars, certain states have argued that privacy-protecting technologies, especially encryption, obstruct police investigations. These technologies are designed to do exactly that, protect everyone’s ability to control their expression and communication.

The European Commission’sRoadmap for Lawful Access to Datawants to make all digital data accessible to authorities by 2030. This involves systematically weakening encryption rather than simply bypassing it.

Edward Snowden’s revelations ten years ago led to widespread adoption of encryption and institutional consensus supporting the right to encrypted communication. But governments remain frustrated by their inability to access private communications. We’re seeing a return to authoritarian positions using terrorism, organized crime and child exploitation as justifications for undermining encryption.

🇩🇰Danish Minister of JusticePeter Hummelgaard, chief architect of the current ChatControl proposal,recently stated:“We must break with the totally erroneous perception that it is everyone’s civil liberty to communicate on encrypted messaging services.”Well, there you have it folks:encrypted communicationisn’t a civil liberty anymore. Youcypherpunkswere wrong all along. /s

Similarly in 🇫🇷 France, both Bernard Cazeneuve and Emmanuel Macron have explicitly stated their desire to control encrypted messaging, seeking to pierce the privacy of millions who use these services.

CSAR provides the perfect opportunity for member states to finally design and implement a generalized surveillance tool for monitoring population communications. Crossing this threshold means eliminating all confidentiality from communications using digital infrastructure.

### False Positives#

These scanning systems get it wrong most of the time.Studies show approximately 80% of algorithmic reports are false positives: innocent content incorrectly flagged as illegal. 🇮🇪 Irish law enforcementconfirms this: only 20.3% of 4,192 automated reports actually contained illegal material.

This is fine.

Even with hypothetical 99% accuracy (which current systems don’t achieve), scanning billions of daily messages would generate millions of false accusations. Police resources would be overwhelmed investigating innocent families sharing vacation photos while real crimes go uninvestigated.

Innocent content regularly triggers these systems: family photos, teenage conversations, educational materials and medical communications. Consider this real case:a father was automatically reported to policeafter sending photos of his child’s medical condition to their doctor. Google’s algorithms flagged this legitimate medical consultation as potential abuse, permanently closed his account and refused all appeals. His digital life was destroyed by an algorithm that couldn’t distinguish between medical care and criminal activity.

### Scientific Opposition#

For the third time in three years, over 600 cryptographers, security researchers and scientists across 35 countries haveco-signed an open letterexplaining why this mass scanning project is “technically unfeasible”, constitutes a “danger to democracy” and would “completely compromise” the security and privacy of all European citizens.

The letter emphasizes that client-side scanning cannot distinguish between legal and illegal content without fundamentally breaking encryption and creating vulnerabilities that malicious actors can exploit.

Meanwhile, the Commission has provided no serious studies demonstrating the effectiveness, reliability or appropriateness of these intrusive measures for actually protecting children. Industry claims appear to have taken precedence over evidence-based policy-making.

Genuine security emerges through thoughtful design where security measures and civil liberties function as complementary forces, not opposing ones.

### Easily Defeated#

The fundamental flaw in ChatControl becomes clear when examining how easily determined actors can circumvent these scanning systems. Criminals don’t need sophisticated techniques to bypass client-side scanning; they use well-documented public knowledge already employed by malicious actors.

Layered EncryptionEncrypt files with standard tools likeGPGbefore messaging. Hell, even a basicCaesar cipherwould be sufficient to bypass detection. Since client-side scanning occurs after user encryption but before transport encryption, pre-encrypted content looks like random data to detection algorithms. Recipients decrypt locally with shared keys.

External Platform BypassUpload content to any third-party platform (Dropbox, OneDrive, anonymous file hosts, or obscure hosting services) and share links instead of files. The scanner sees innocent text containing a URL while the actual content sits untouched on external servers.

Custom Messaging ClientsOpen-source protocols likeXMPPandMatrixallow custom client development. Modified clients can automatically implement cloud storage and encryption workflows transparently. Users experience normal messaging while completely evading surveillance infrastructure.

Digital SteganographySteganographic techniquesembed data within innocent images. Family photos can carry hidden payloads invisible to both human operators and AI systems. Tools likeOpenStegomake this accessible to average users.

Platform MigrationCriminal networks can shift to decentralized platforms, peer-to-peer networks or services outside EU jurisdiction. Tor-based messaging, blockchain communications or servers in non-compliant countries remain beyond ChatControl’s reach.

ChatControl catches only amateur criminals who directly attach problematic content to messages. Professional networks already employ these evasion techniques as standard practice. EU legislation won’t make them forget how computers work.

The system fails at protecting children while succeeding at mass civilian monitoring.It’s not a bug, it’s a feature.

## Business Interests#

### Industry Players#

The child protection narrative masks concerning business interests. The European Commission based its CSAR proposal primarily on claims from industry players rather than independent research.

Commercial surveillance companies would manage the technology with guaranteed access to the European market. Organizations likeThorn(co-founded by actorAshton Kutcher), Microsoft’sPhotoDNAand other tech companies develop these detection systems while simultaneously lobbying for regulations that would require their adoption across Europe.

These companies develop the detection technologies and lobby for laws mandating their adoption, creating a profitable feedback loop. The proposal would secure privileged market positions for surveillance companies across hundreds of millions of European users. Pretty nice, isn’t it?

These systems would be:

* Proprietary: Built on closed-source code with methods hidden from public view
* Unverifiable: Operating without meaningful external examination or accountability
* Legally powerful: Capable of starting criminal proceedings through algorithmic decisions

### Rhetorical Tactics#

Corporate media offers control of internet speech wrapped in protect kids packaging.

CommissionerYlva Johanssonconsistently emphasizes this narrative in her communications:

“[Privacy defenders make a lot of noise], but someone has to speak for the children.”

Won’t somebody please think of the children? - The Simpsons

“Think of the children” is a well-documented political rhetoric technique that appeals to emotion rather than evidence. While child protection is genuinely important, this approach frames any opposition as being against child welfare, making nuanced discussion more difficult.

This creates a false choice. Privacy isn’t a luxury for troublemakers, it’s afundamental rightthat protects journalists, whistleblowers, activists and ordinary people from unwarranted intrusion.

Critics aren’t opposing child protection. We’re questioning whether undermining privacy rights for 450 million 🇪🇺 Europeans is the most effective approach when targeted alternatives exist that preserve rights.

## EU Country Positions#

Understanding how 🇪🇺 EU member states position themselves on this legislation is crucial, as their votes will determine whether ChatControl becomes reality.

### Vote Breakdown#

Countries that support ChatControl (12):🇧🇬 Bulgaria • 🇭🇷 Croatia • 🇨🇾 Cyprus • 🇩🇰 Denmark • 🇫🇷 France • 🇭🇺 Hungary • 🇮🇪 Ireland • 🇱🇹 Lithuania • 🇲🇹 Malta • 🇵🇹 Portugal • 🇷🇴 Romania • 🇪🇸 Spain

Countries that oppose ChatControl (7):🇦🇹 Austria • 🇨🇿 Czech Republic • 🇪🇪 Estonia • 🇫🇮 Finland • 🇱🇺 Luxembourg • 🇳🇱 Netherlands • 🇵🇱 Poland

Countries still undecided (8):🇧🇪 Belgium • 🇩🇪 Germany • 🇬🇷 Greece • 🇮🇹 Italy • 🇱🇻 Latvia • 🇸🇰 Slovakia • 🇸🇮 Slovenia • 🇸🇪 Sweden

### National Stances#

💪 Strong opposition (the good guys)
 (click to expand)

* 🇦🇹Austria: Constitutional and privacy concerns.
* 🇨🇿Czech Republic: Prime Minister explicitly rejects proposals that would allow widespread monitoring of citizens’ private digital communications.
* 🇪🇪Estonia: Acknowledges sincere concerns about child exploitation, but opposes undermining end-to-end encryption and forcing mass surveillance.
* 🇫🇮Finland: Cannot support the latest compromise proposal because it contains a constitutionally problematic identification order.
* 🇱🇺Luxembourg: Rejects broad surveillance measures like client-side scanning and insists that EU regulation must ensure proportional, targeted detection to protect citizens’ fundamental rights.
* 🇳🇱Netherlands: Strong privacy protection stance.
* 🇵🇱Poland: Opposition to mass surveillance measures.

🤷 Undecided positions
 (click to expand)

* 🇧🇪Belgium: The N-VA party calls ChatControl a“monster that invades your privacy and cannot be tamed”. Despite this, Belgium backed Denmark’s compromise during September meetings. Mixed signals from Brussels.
* 🇩🇪Germany: Won’t break encryption but wants to find middle ground. They’re trying to craft their own compromise instead of rejecting ChatControl outright. Germany’s fence-sitting could be decisive.
* 🇬🇷Greece: Still figuring out the technical details. No clear stance yet.
* 🇮🇹Italy: Has concerns about expanding the scope to cover new CSAM detection. Rome seems hesitant about how far this thing could reach.
* 🇱🇻Latvia: The government likes what they see on paper but worries about political backlash after summer attention. Classic politicians hedging their bets.
* 🇸🇰Slovakia: Playing the wait-and-see game. No commitment either way.
* 🇸🇮Slovenia: Dealing with constitutional headaches around privacy. Another country wrestling with legal implications.
* 🇸🇪Sweden: Stockholm is still reading the fine print. Taking their time to decide.

### Current Status#

Current situation: Country positions continue shifting regularly since September 12. With 12 countries supporting, 7 opposing, and 8 undecided, ChatControl supporters still fall short of the 65% EU population threshold needed for a qualified majority. The opposition maintains enough demographic weight to block the proposal for now, but the situation remains fluid as the interim regulation approaches expiration.

📅 Timeline of Events
 (click to expand)

## ChatControl Proposal Introduced### May 11, 2022#### European CommissionThe European Commission unveils the original ChatControl proposal, requiring all email and messaging providers to scan communications for child sexual abuse material.## Danish Presidency Takes Charge### Jul 1, 2025#### EU Council Presidency🇩🇰 Denmark assumes the EU Council Presidency and immediately reintroduces ChatControl as a top legislative priority, targeting October 14, 2025 for adoption.## Support Momentum Builds### Jul 28, 2025#### 15 Member StatesFifteen EU member states back the ChatControl proposal, reversing earlier resistance. 🇫🇷 France has shifted its position and now supports the proposal. 🇩🇪 Germany remains the crucial undecided vote.## Opposition Wave Begins### Aug 26, 2025#### Czech Republic🇨🇿 Czech Prime Minister Petr Fiala announces total opposition on behalf of the entire coalition government.## Constitutional Concerns### Aug 29, 2025#### Finland🇫🇮 Finland rejects the compromise proposal due to constitutionally problematic detection requirements.## Blocking Minority Secured### Sep 10, 2025#### Germany, Luxembourg, Slovakia🇩🇪 Germany, 🇱🇺 Luxembourg, and 🇸🇰 Slovakia officially oppose breaking encryption. This creates the blocking minority needed to stop the proposal.## Estonia Joins Opposition### Sep 14, 2025#### Privacy Protection🇪🇪 Estonia acknowledges child exploitation concerns but opposes undermining end-to-end encryption and mass surveillance.## Germany Wavers### Sep 16, 2025#### Position Unclear🇩🇪 Germany refrains from taking a definitive stance during the LEWP meeting, despite previous encryption concerns. Position becomes uncertain.## Three Countries Flip### Sep 23, 2025#### Belgium, Latvia, Italy🇧🇪 Belgium, 🇱🇻 Latvia, and 🇮🇹 Italy have moved away from supporting the proposal and are now undecided. Country positions continue changing regularly since September 12.Source.

## Consequences#

The effects of these proposals go beyond individual privacy concerns.

Cybersecurity gets compromisedAdding deliberate vulnerabilities to encryption creates weaknesses that everyone can exploit. Any backdoor for authorized access becomes a potential entry point for criminals and foreign intelligence services. In February 2024, the 🇪🇺 European Court of Human Rightsalready determinedthat mandating weakened encryption “cannot be regarded as necessary in a democratic society”.

Innovation suffers🇪🇺 European cybersecurity companies would face an impossible situation in global markets. How could they credibly sell security solutions when regulations require them to build in access mechanisms that undermine those very protections?

“Buy our ultra-secure encrypted stuff!” (Terms and conditions apply, government backdoors included)."

Tech companies will leave EuropePrivacy-focused services that moved to 🇪🇺 Europe after the Snowden revelations are already signaling they might leave. Signal has explicitly said it would stop operating in 🇪🇺 Europe rather than compromise its security.

Even 🇨🇭 Switzerland, traditionally seen as a privacy haven, is facing severe legislative pressures that are forcing tech companies to relocate. Proton has confirmed it hasbegun moving some of its physical infrastructure out of Switzerlanddue to “legal uncertainty” over the proposed surveillance law amendments. Lumo, their AI chatbot, became the first productto relocate, moving to Germany instead of Switzerland specifically because of these legislative concerns.

The SwissOSCPT(Ordinance on the Surveillance of Correspondence by Post and Telecommunications) revision would require VPNs and messaging apps to identify users and retain data for up to six months, plus decrypt communications upon authority request. As Proton’s CEOAndy Yenexplained, these are proposals that “have been outlawed in the EU” but could soon become reality in Switzerland.

Other privacy-focused providers like Tuta haveexpressedsimilar concerns and contingency plans to leave 🇨🇭 Switzerland if the surveillance laws pass.

Europe might become dependent on US surveillanceI’m not so sure on this one, but by outsourcing surveillance technology to American companies, 🇪🇺 Europe may create dangerous dependencies. These companies operate under 🇺🇸 US jurisdiction and theCLOUD Act, potentially allowing 🇺🇸 Washington to access data collected on 🇪🇺 European citizens. Under the pretense of child protection, the 🇪🇺 EU risks handing surveillance keys to foreign powers.

Social behavior changesWhen people know they’re being watched, they change how they communicate. People start self-censoring, avoiding certain topics and carefully choosing their words even in private conversations.

This is called thechilling effect. Rights don’t disappear overnight: they erode gradually as people change their behavior to avoid potential problems.

## Take Action#

Here’s how you can contribute to defending our digital freedoms:

1. Share this article and educate your network: Use hashtags like#ChatControlor#StopScanningMe. Forward resources to friends, family and colleagues.
2. Sign the petition: against ChatControl atchange.org.
3. Stay informed and follow updates:@[email protected],x.com/nonchatcontrol,patrick-breyer.deandfightchatcontrol.eu.
4. Contact your national representativesto convince your country to oppose ChatControl, if it’s not already the case.
5. Join campaigns and support organizations:stopscanningme.eufor local actions,EFFandEDRifor digital rights advocacy.
6. Adopt privacy tools and infrastructure: Use Signal and other privacy-respecting alternatives. Host your own services or support privacy-focused providers.

## Conclusion#

The irony is kinda painful: the continent that builtGDPRto protect digital privacy now designs ChatControl to dismantle it systematically. What was once a fundamental right could become mandatory surveillance.

ChatControl represents a historic choice for 🇪🇺 Europe. Either we become the first democracy to normalize mass surveillance of private communications or we defend the digital rights that made Europe a global privacy leader.

You were the chosen one! - Star Wars

This decision deserves close attention: authoritarian regimes worldwide are watching, ready to justify their own programs with: “Eh, if Europe does it, why shouldn’t we?”

The next chapter unfolds on October 14, 2025. 😉

 Author


 Metalhearf


IT Architect, Hacker & Passionate Tinkerer

 ↑
