---
title: Advancing conflict research and response through satellite-derived data | Nature
url: https://www.nature.com/articles/s41586-026-11004-6
site_name: newsfeed
content_file: newsfeed-advancing-conflict-research-and-response-through-s
fetched_at: '2026-09-09T21:31:06.423025'
original_url: https://www.nature.com/articles/s41586-026-11004-6
date: '2026-09-09'
description: 'With armed conflicts at a historic high and attacks on civilians rising1, understanding the evolving nature of conflict is a critical research priority. The current paradigm in conflict research relies heavily on text-based data, using fatalities as the primary—and often sole—proxy for violence intensity. Although these data have expanded our ability to study armed conflict, they exhibit inherent limitations due to uneven human reporting2–6. War damage assessments based on satellite data7–13 offer a complementary perspective. Satellite-derived data have their own limitations, but these arise from different mechanisms, creating distinct, complementary strengths that can be leveraged through data integration. Here we propose three concrete approaches to integration: improvement, enrichment and fusion. Each bridges a different gap in the underlying data sources. We use case studies from Ukraine and Myanmar to illustrate how integration can be implemented in practice and the novel
  analytical insights that emerge. Prioritizing data integration enables a paradigm shift away from fatality-centric research towards a broader spectrum of violence, revealing the complexity of conflict dynamics. Integrating satellite-derived war-damage data with text-based fatality records&nbsp;through improvement, enrichment and fusion mitigates&nbsp;limitations inherent in each source, revealing complex violence dynamics beyond fatality-centric paradigms, as case studies from Ukraine and Myanmar&nbsp;illustrate.'
tags:
- nature
---

Advancing conflict research and response through satellite-derived data
 

Download PDF

Download PDF

## Abstract

With armed conflicts at a historic high and attacks on civilians rising1, understanding the evolving nature of conflict is a critical research priority. The current paradigm in conflict research relies heavily on text-based data, using fatalities as the primary—and often sole—proxy for violence intensity. Although these data have expanded our ability to study armed conflict, they exhibit inherent limitations due to uneven human reporting2,3,4,5,6. War damage assessments based on satellite data7,8,9,10,11,12,13offer a complementary perspective. Satellite-derived data have their own limitations, but these arise from different mechanisms, creating distinct, complementary strengths that can be leveraged through data integration. Here we propose three concrete approaches to integration: improvement, enrichment and fusion. Each bridges a different gap in the underlying data sources. We use case studies from Ukraine and Myanmar to illustrate how integration can be implemented in practice and the novel analytical insights that emerge. Prioritizing data integration enables a paradigm shift away from fatality-centric research towards a broader spectrum of violence, revealing the complexity of conflict dynamics.

### Explore related subjects

Discover the latest articles and news in related subjects.

* Computer science
* Environmental social sciences
* Interdisciplinary studies
* Politics

## Main

We are witnessing a record number of armed conflicts, and attacks on civilians are increasing in number1. In conflicts such as those in Gaza, Ukraine, Sudan and Myanmar, the use of heavy weaponry, drone warfare and arson has caused widespread death, destruction and displacement, leaving lasting scars on entire countries. This makes understanding the evolving nature of armed conflicts and developing strategies to reduce violence a critical research priority.

Despite the urgency of studying armed conflict, there are important limitations in the available data. Over the past 15 years, conflict research has made substantial progress with the emergence of detailed conflict event datasets based primarily on media sources14,15,16. However, these datasets exhibit well-documented limitations and biases that reflect the uneven availability of human reporting2,3,4,5,6. Most notably, because media reporting is attention-driven, there is a lack of reliable data from places and periods that receive little media coverage, and from types of event that often go unreported or are reported only in unspecific terms17,18, such as the destruction of dwellings and crops or the displacement of populations. Accordingly, quantitative studies of conflict-related violence focus predominantly on fatalities and often leave other aspects of violence and their social and environmental effects unaddressed.

We propose an approach to broaden this focus through the integration of text-based conflict event data with satellite-derived data. Here we use the term satellite-derived data to refer to information generated through the analysis of satellite data (see Supplementary Information, sectionB). Advances in automated satellite analysis7,8,9,10,19,20,21,22and increasingly available open-access satellite data make this a pivotal moment for such data integration. Prior work has highlighted the potential of satellite data for humanitarian action23,24,25and provided remote-sensing-based perspectives on specific conflicts9,10,26,27,28,29. In this Analysis, we demonstrate how the fundamentally different data generation processes of text-based and satellite-derived data lead to unique strengths and limitations that can be overcome only through data integration. We propose three approaches to integration—improvement, enrichment and fusion—and use empirical examples from Ukraine and Myanmar to illustrate their feasibility and the novel empirical insights that they provide. We advocate for prioritizing this integration to enable a paradigm shift away from fatality-centric research towards a broader spectrum of violence, to reveal the complex, interactive dynamics that shape conflict landscapes.

## Expanding our view on violence

To reduce impact on civilians and the long-term consequences of war, we must understand when and where conflict actors use violence to advance their military or political aims. This makes data on conflict-related violence central to many research efforts. Although approaches such as fieldwork and surveys offer invaluable insights into various conflict dynamics, large-scale analyses across time and space require techniques for systematic, retrospective data collection. The current paradigm in conflict research relies almost exclusively on data derived from human reporting. Yet uneven reporting means that we currently focus primarily on a relatively narrow, although highly important, spectrum of conflict-related violence. Emerging approaches that automatically analyse satellite data offer a complementary perspective and promise to expand both the scope and depth of conflict research. To realize this potential, we must understand what each data source captures, how the data are generated, and how the generation process shapes what we observe and with what precision.

### Text-based data

Disaggregated conflict event data based on human reporting, which we refer to as text-based data, form the empirical backbone of most quantitative-comparative studies of conflict dynamics. Figure1ashows how such data are typically produced. Most studies rely on manually coded data14,15,16(Fig.1a, left). Human coders record individual instances of violence based primarily on news articles and reports from sources on the ground30, documenting event location and date, involved actors and resulting fatalities. Advances in natural language processing and large language models have enabled automated approaches to detecting conflict events from text31,32,33,34(Fig.1a, right). These approaches are faster and scalable, and draw on sources in multiple languages, but introduce new challenges, most notably reduced corroboration and validation of events4(Supplementary Information, sectionC).

Fig. 1: Data generation processes and associated limitations.
Full size image

a, Text-based data.b, Satellite-derived data. Outlines indicate strengths (green), current challenges and limitations that may be mitigated through technical, conceptual or organizational progress (orange), and challenges and limitations inherent to each data generation process (red). Although specific steps vary across methodologies, the primary limitations remain the same.

Coverage varies across geography and time, shaped by factors such as regime openness, media presence and access to communication technologies2,3,4,6,17,35. Because reporting is attention-driven, these biases are particularly pronounced for non-lethal violence14,17,18, which often goes unreported or is reported only at aggregate level. As a result, datasets that aim to include events beyond fatalities15,31,34,36,37tend to severely undercount them14,17,18. One core provider of disaggregated conflict data records only events that involve fatalities, precisely because of this bias1,14.

Neither manual nor automated advances can resolve these core limitations of text-based data, which arise from the uneven availability of human reporting. Professionalized coding procedures, source selection and transparency inform engagement with these biases4but cannot overcome the underlying constraints38. Triangulating across event datasets only highlights varied blind spots in overall coverage39. Emerging approaches, such as crowd-sourced reporting platforms and digital fieldwork infrastructures40,41, bypass media intermediaries and may improve coverage of underreported forms of violence, such as sexual violence. However, these too depend on eyewitnesses being present, willing and able to share information.

### Satellite-derived data

We see promise in complementing existing conflict data with data derived from satellite imagery (Fig.1b). Satellites collect data during conflicts independently of physical access or perceived newsworthiness. Images are acquired at known times and georeferenced, tying each pixel to an exact time and location. This enables data collection in areas where information has been difficult to access, with spatial precision beyond text-based sources, and on events that often go unreported, particularly violence against material targets.

In theory, satellites can capture a wide range of information related to violence: actors and instruments of violence, such as troop movements or weapons systems; direct effects of violence, such as destruction of the built-up and natural environment; and indirect effects, such as degradation of agricultural activity or decline in market activity (Supplementary Information, sectionA). However, automated detection of actors and their instruments at fine-grained spatial and temporal resolution carries a high risk of dual use24, and we do not advocate for public research in this area. Given its direct relevance to conflict research and response, and its complementarity to text-based fatality data, we focus on data capturing the direct effects of violence on the built-up and natural environment, which we term war damage. Capturing such damage matters because, although lives lost are among the most tragic consequences of war, they are neither the only nor always the most relevant indicator of violence severity. The torching of homes and destruction of livelihoods may produce few direct deaths if populations have fled, yet they reshape realities on the ground, with long-term societal consequences, and often contribute to large numbers of indirect conflict-related fatalities42,43.

Traditionally, war damage data were collected through manual annotation of very high-resolution satellite images (Fig.1b, left), a costly and labour-intensive approach that limited the scope of such data collections. Progress in the automated analysis of multi-temporal satellite data7,8,9,10,19,20,21,22now makes large-scale, long-term data collections feasible (Fig.1b, right), even  though the field is still in its early stages. One area that has emerged as a strong field in its own right is the detection of building damage8,9,10,11,12,13. Other work examines violence targeting the natural environment, including deforestation to deny cover to armed groups and attacks on cropland and water resources to disrupt rural livelihoods26,44,45,46,47. Studies document vegetation damage from rocket fire and munitions detonations48,49,50, fires set to trees and crops26,51, and direct vegetation clearance52(Supplementary Information, sectionB).

Satellite-derived data also face important constraints. Whereas a decade of scrutiny has produced a clear understanding of the limitations of text-based conflict data2,3,4,5,6, satellite-derived data have been less systematically analysed, given the recency of the field. We see three main types of limitation.

The first type arises from limited reference data to train and validate war damage detection. As a result, approaches are fine-tuned for only a small number of conflicts, and we lack methods and analysis-ready data for information-poor settings, precisely where satellite-derived data would be most valuable. The availability of reference data is linked to international attention, but we can deliberately expand reference data and invest in approaches that generalize to underrepresented conflicts. Moreover, satellite archives span decades, meaning that even when events go undetected or patterns are overlooked, satellite data provide a record of the effects of armed conflict that can be analysed retrospectively as methods improve.

The second type arises because events are not equally detectable across forms of violence and settings. For example, in peripheral areas, buildings are often more isolated, smaller and surrounded by vegetation, making it more difficult to identify destruction. For automated building damage assessments based on moderate resolution data, this results in an urban bias that mirrors that of text-based data, even though it arises from a different mechanism. Technical improvements such as multi-modal approaches or higher-resolution open-access imagery can mitigate this limitation over time. For now, researchers must account for these biases, especially when they correlate with those of text-based data.

The third type differs from the first two in that it is inherent to the source and cannot be overcome through technical, conceptual or organizational innovation. Satellites can only capture phenomena that have a physical presence or visible effect on the Earth’s surface, and they cannot provide contextual narrative information. Similar to the inherent limitations of text-based data, which arise from the uneven availability of human reporting, this third type of limitation reflects the nature of the source itself rather than the methods of analysis. The implication is clear: advancing the field rests on our ability to leverage the strengths and mitigate the limitations of each data type through data integration.

## Data integration

The inherent limitations of single-source data motivate different forms of integration. Prior research on data integration in conflict research39,53has focused on combining text-based event datasets, emphasizing their complementary coverage and use for cross-validation and enrichment across sources. Focusing on integration at scale, we propose three main approaches for combining text-based and satellite-derived data; the choice depends on the gap that needs to be bridged. Improvement addresses cases in which one data type covers the violence of interest but lacks a specific feature, such as the spatial precision missing from text-based data or the contextual narrative information that is absent from satellite-derived data. Enrichment is needed when no single source captures the full scope of relevant violence, as in campaigns that combine killings, destruction and displacement. Fusion, the deepest level of integration, jointly models text and satellite data to infer phenomena that neither source captures directly.

We illustrate these approaches in two contrasting contexts: Ukraine, an information-rich setting where automated war damage data are available, and Myanmar, an information-poor setting where we rely primarily on manually annotated data. Integration adds value in both contexts, although the gaps that it bridges differ. In information-poor environments, where text-based data are sparse, satellite-derived data carry more of the analytical weight. Conversely, some integration applications require fine-grained text-based data and are most feasible in information-rich settings.

### Improvement

The inherent limitations of single-source data (Fig.1) mean that even when we focus on a specific form of violence, such as lethal violence or the targeting of livelihoods, reliance on one data type can yield biased results or preclude certain research questions. For example, analysing neighbourhood-level diffusion of violence or identifying targeting patterns requires spatial precision that text-based fatality data typically lack. Improvement addresses such cases by using one data type to add the missing feature to another, enabling new forms of analysis.

A key opportunity is to use satellite-derived data to improve the spatial precision of text-based data (for a related approach, see the literature on dasymetric mapping54,55). In many contexts, armed actors pursue specific objectives rather than engaging in violence at random; knowing where they fight is central to understanding the logic of violence. Because satellite-derived data are spatially explicit, we can use them to refine the locations of text-based data, provided that the form of violence captured in the text-based data co-occurs with the form captured in the satellite-derived data (Supplementary Information, sectionC)—for example, killings that take place alongside dwelling destruction. We illustrate this with examples from violence against the Rohingya people in Myanmar at the local (Fig.2a–e) and more aggregate (Fig.2f–h) levels. Our local-level example focuses on Chut Pyin in Rakhine State, where several hundred people were killed in a large-scale massacre; Extended Data Figs.1and2provide two additional village-level examples.

Fig. 2: Spatial violence attribution in Rakhine State.
Full size image

a–e, Chut Pyin, Rakhine State.a, Pre-event optical imagery (27 December 2016).b, Post-event optical imagery (19 April 2019) showing selective destruction.c, Spatial distribution of reported fatalities at the settlement level.d, Satellite-detected destruction footprints.e, Refined fatality locations (red) derived from intersecting reported events with destruction data, excluding unaffected areas (green).f–h, Rakhine State.f, Fatalities recorded only at the Admin 1 (state) level.g, Thermal anomalies detected between 25 August and 9 September 2017 based on National Aeronautics and Space Administration (NASA) Fire Information for Resource Management System (FIRMS) data.h, Improved attribution of state-level fatalities to specific sub-districts on the basis of thermal anomalies.aandbreproduced from Google Earth, CNES/Airbus and Maxar Technologies (2025).c–e, Basemap adapted from OpenStreetMap contributors, ODbL (https://opendatacommons.org/licenses/odbl/1-0/). Data sources: refs.1,14,70,71,72.

Text-based data14,15form the backbone of our understanding of this violence and the actors involved, but are spatially imprecise. The best available fatality data are reported at the settlement level (Fig.2c, red raster footprint). Because violence during this period involved coordinated attacks—killing civilians and destroying their homes in the same operation—we use satellite-derived war damage data (Fig.2d) to indicate where fatalities are likely to have occurred. This enables attribution of fatalities to specific neighbourhoods (Fig.2e). In this case, the divided spatial pattern, revealed only through improved spatial precision, points to ethnic targeting, indicating that Rohingya civilians were killed, whereas ethnic Rakhine residents in the same settlement were probably spared56. This process can be done at scale, contingent on the availability of satellite-derived data on destruction (Supplementary Information, sectionD). Because text-based data are typically limited to settlement level, local-level improvement opens up within-settlement variation analysis across information environments.

Figure2f–hillustrates an approach to improving the spatial precision of text-based data at a more aggregate level. During the peak of lethal violence in Rakhine State, a substantial share (13%) of reported fatalities was coded only at the state level (Fig.2f), forcing researchers to analyse at coarse spatial scales—where results are less meaningful—or to exclude these events, risking biased inference. Because most killings in this period occurred alongside the burning of Rohingya houses56, we use satellite-derived fire data to narrow down the area where these events are likely to have taken place. In this case, fire data (Fig.2g) point only to the three sub-districts already identified through spatially precise data. We can infer that the imprecisely coded events took place in the same areas (Fig.2h). This type of aggregate-level refinement is particularly valuable in information-poor settings, where a larger share of reported events is likely to be coded at coarse spatial units. The refinement enables analysis at smaller geographic units, allowing researchers and policymakers to identify where violence is actually unfolding rather than where it is reported.

Conversely, text-based data can enhance satellite-derived analysis by capturing contextual information. Details about perpetrators, victims or the context of an event can be drawn only from text-based data. In information-rich settings where fine-grained text-based data are available, this enables insights that are not possible with satellite-derived data alone. We demonstrate this through an analysis of building destruction in Ukraine during the frontline war (Fig.3; see Extended Data Fig.3for full time series and Extended Data Fig.4for disaggregation of Russian gains into operational phases). Although satellite-derived war damage data reveal the spatio-temporal distribution of building destruction, only the integration of text-based territorial control data exposes asymmetries in targeting patterns between Russian and Ukrainian forces. During Ukraine’s 2022 counteroffensive, for example, the absolute number of newly destroyed buildings remained high (Extended Data Fig.5). Comparing first stable transitions during the frontline war (Methods), our analysis shows that populated areas gained by Russian forces experienced building damage more often than those retaken by Ukrainian forces. In the month of territorial transition, 70.5% of populated areas gained by Russia exhibited newly damaged buildings, compared with 43.9% of populated areas regained by Ukraine (χ2(1) = 16.5,P< 0.001,φ= 0.26; full results for the 5-month window are in Extended Data Table1). Where damage occurred, it was also more severe: among the subset of areas that sustained damage, Russian gains experienced more building destruction than Ukrainian gains, from two months before to one month after the control change (Fig.3b; statistical analysis in Extended Data Table2). These patterns remain hidden without text-based data on territorial control. Such integrated analyses, which single-source data cannot support, provide an empirical basis for assessing how different forces wage war and reveal differences that have systematic consequences for the scale of destruction endured by civilians.

Fig. 3: Building damage associated with territorial gains in Ukraine, frontline war.
Full size image

a, Areas with at least one change in territorial control (February 2022 to October 2023), overlaid with the first stable transitions occurring during frontline war (May 2022 to October 2023;Methods).b, Box plots of newly damaged buildings per 1,000 intact buildings (start of month) across populated areas, in a five-month window centred on the month of control change, stratified by Russian (blue) and Ukrainian (purple) gains (May 2022–October 2023). Centre line shows median, box spans interquartile range and whiskers extend to the most extreme observation lying within 1.5 × IQR of the nearest edge of the box. These include only areas containing mapped building footprints with first stable transitions and radar-detected damage (Methods). The asymmetry is statistically significant from two months before (m−2) to one month after (m+1) control change and converges by two months after control change (m+2) (Kolmogorov–Smirnov, two-sided,m−2:D= 0.313,P= 0.008;m−1:D= 0.372,P< 0.001;m0:D= 0.237,P= 0.039;m+1:D= 0.275,P= 0.007;m+2:D= 0.151,P= 0.367). A Mann–Whitney test confirms the same pattern; full results in Extended Data Table2, spatial autocorrelation analysis and its interpretation in Supplementary Table1. The full time series is shown in Extended Data Fig.3, and phase-specific analyses associated with Russian gains are presented in Extended Data Fig.4. Data sources: refs.9,73,74.

### Data enrichment

Our second level of integration—enrichment—enables researchers to examine how different forms of violence relate to and capture spatio-temporal dynamics that cannot be observed from one data type in isolation. Unlike improvement, where one primary data source is supplemented by an auxiliary one, enrichment links text-based and satellite-derived data by a common time and location while keeping them analytically distinct.

A policy-relevant example is ethnic cleansing: actors target individuals from ethnic or religious groups through killings, rape and intimidation while simultaneously razing cultural or religious buildings and destroying homes. As people are attacked and livelihoods are destroyed, people are forced to flee, which subsequently reduces fatalities and violence against persons more broadly. Only data integration can capture these complex relationships.

Figure4illustrates how integrating fatality and war damage data changes our understanding of the ethnic cleansing campaign against the Rohingya population in Myanmar. Figure4a,bshows that all reported killings in the two most affected townships occurred during the first week of the campaign (third-most affected township in Extended Data Fig.6; same pattern using alternative conflict event data in Extended Data Fig.7). Relying on fatality data alone would suggest that violence quickly subsided. Satellite-derived war damage data (Fig.4c,d), however, reveal that violence continued for at least six months after the killing apparently subsided, albeit with a clear shift in form and intensity. As hundreds of thousands fled amid reports of violence and massacres, the government proceeded to remake Rakhine State by bulldozing the remains of burned villages, clearing trees and other vegetation, and in some cases constructing new security bases or villages reserved for other Rakhine communities56. This phase of the campaign is consequential for the surviving Rohingya population, as it hinders their return and continued existence in Rakhine State. Viewed through fatality data alone, the campaign appears as a week of violence; integrated analysis reveals a months-long process of permanent displacement. In information-poor environments, satellite-derived data carry more of the analytical weight, and even more so when violence itself decreases reporting as populations are killed and flee.

Fig. 4: Killings and settlement destruction in Rakhine State.
Full size image

a,b, Reported fatalities (25 August 2017 to 18 March 2018; Uppsala Conflict Data Program (UCDP) Georeferenced Event Dataset (GED)) in Maungdaw township (a) and Buthidaung township (b).c,d, Settlement destruction (25 August 2017 to 18 March 2018; UNOSAT) in Maungdaw township (c) and Buthidaung township (d). Reproducing these panels with Armed Conflict Location and Event Data (ACLED) rather than UCDP GED data confirms the patterns (Extended Data Fig.7). Note thaty-axis scales differ across townships to accommodate varying absolute levels of violence. The campaign exhibited higher levels of violence in Maungdaw than in Buthidaung. Data sources: refs.1,14,71,72.

Our second enrichment example, from Ukraine (Fig.5; see Extended Data Fig.8for alternative estimates of fatalities), illustrates how, without data integration, we miss not only temporal but also spatial variation. The analysis compares text-based fatality data (Fig.5a,b) and satellite-derived war damage data (Fig.5c,d) for two large Ukrainian cities: Mariupol and Sievierodonetsk. Although both cities were devastated by Russian bombing and shelling, clear differences emerge, owing in part to the speed and timing of Russian advances. Mariupol was almost fully encircled within a week of the full-scale invasion, which hindered evacuation efforts and contributed to high casualties early on. By contrast, the Russian ground assault on Sievierodonetsk began in late May 2022, leaving more time to prepare evacuations. By the time violence peaked, only 10–15% of the pre-war population remained. Considering satellite-derived war damage data alone would obscure key differences in levels of lethal violence, whereas relying only on fatality data would miss much of the non-lethal violence endured by residents of Sievierodonetsk, including extensive destruction and sustained suffering by civilians who remained. The implications extend from research—such as understanding when destruction translates into mass casualties—to post-conflict planning. Both cities face massive reconstruction needs, but the populations who will return, and the trauma that they carry, differ profoundly.

Fig. 5: Scope of fatalities and building damage in Mariupol and Sievierodonetsk.
Full size image

a,b, Cumulative deaths in Mariupol (a) and Sievierodonetsk (b) as a percentage of the respective pre-war populations (data from February 2022 to October 2023). Solid lines include only events coded at settlement-level spatial precision; dotted lines additionally include events coded within 25 km. Both use UCDP GED best estimates. See Extended Data Fig.8for the same analysis with best and high estimates.c,d, Cumulative building damage in Mariupol (c) and Sievierodonetsk (d) as a percentage of the total number of buildings in each city (data from March 2022 to October 2023). Solid lines show detected damage and dotted lines show estimates adjusting for true positive rates (seeMethods). Data sources: refs.1,9,14.

Enrichment requires careful spatial and temporal aggregation or disaggregation, which involves consequential assumptions57(Methods). Where conceptually meaningful, however, enrichment enables researchers to capture relationships between forms of violence that would remain invisible in single-source analyses.

### Cross-modal data fusion

Data fusion, our deepest level of integration, jointly models text and satellite data to infer an underlying phenomenon, such as violence in general, or specific manifestations such as civilian targeting. Whereas improvement and enrichment occur at the data output level (text-based and satellite-derived data), fusion occurs at the source level (text and satellite data), enabling the synthesis of insights across heterogeneous sources at scale. This makes fusion especially promising for information-poor settings, where patterns learned in data-rich contexts can support inference where direct evidence is sparse.

Although traditional data fusion has proven effective in other domains, the most promising path for conflict research lies in emerging vision–language foundation models (VLFMs)58,59, which generalize earlier fusion paradigms. Traditional fusion models combine input data sources (modalities) for specific tasks, relying on fixed, task-specific designs. By contrast, modern vision–language foundation models map different data types into a joint representation space (embeddings) using per-source encoders, learning relationships between concepts, space and time from co-located pairs (Fig.6a). These general-purpose vision–language representations can be transferred to specific downstream tasks with minimal fine-tuning, enabling us to detect, classify, localize, and eventually understand conflict processes (Fig.6b).

Fig. 6: Vision–language pre-training and supervised fine-tuning under uneven data coverage.
Full size image

a, Pre-training learns vision and language encoders by aligning large-scale image–text pairs in a joint embedding space, bringing matched pairs closer and pushing mismatched pairs apart.b, Under supervised fine-tuning, pre-trained encoders are adapted to conflict-specific tasks using (1) text only, (2) image only or (3) paired image–text data, and connected to downstream task-specific heads to produce conflict-related outputs. Example imagery is derived from Copernicus Sentinel-2 data.

For example, campaigns of ethnic cleansing manifest through multiple tactics—killings, destruction and displacement—each of which leaves traces in different data sources. General-purpose joint modelling of these signals could enable fusion models to infer such campaigns even when individual indicators are sparse. Fusion approaches may also learn associations between textual descriptions and visual patterns that elude human analysts. In Myanmar, for instance, Rohingya and Rakhine communities typically construct distinct housing types56. After fine-tuning, a VLFM could learn associations between ethnicity, building typologies and targeting patterns. Spatially clustered destruction of one structure type may indicate group-based targeting, whereas destruction of individual buildings could signal selective violence60. Identifying such patterns at scale could advance long-standing debates about indiscriminate versus selective violence and inform policies to protect civilians under different targeting logics.

VLFMs are an emerging area and have not yet been applied to conflict research. The most mature applications are in medicine, where models trained on medical image–text data are fine-tuned to jointly interpret medical imaging and clinical text to detect disease processes61,62,63. In remote sensing, emerging approaches in areas such as ecology64,65,66typically treat text as auxiliary to satellite imagery, rather than jointly modelling both as independent evidence of a latent phenomenon.

One challenge in adapting VLFMs for conflict research is that data vary widely in spatial and temporal resolution and exhibit uneven coverage across modalities, requiring careful spatio-temporal alignment67. Given the scarcity of conflict-specific aligned image–text pairs, training VLFMs from scratch on conflict data is unrealistic. The most promising path is to adapt pre-trained vision and language encoders67through supervised fine-tuning with conflict-relevant data (Fig.6). Such fine-tuning connects pre-trained vision and language encoders to task-specific downstream model blocks (heads) using conflict-relevant supervision, such as labels for detection, classification or localization. As shown in Fig.6, encoders can be fine-tuned independently using text-only or image-only data when paired data are lacking, or jointly when aligned image–text annotations exist. This flexibility enables pre-trained representations to be tailored to conflict-relevant analytical objectives despite uneven data coverage. When image–text pairs are available, models learn cross-modal associations, combining the contextual richness of text reports and the localization of satellite images. Improvement and enrichment thus also help generate the aligned annotations needed for paired supervised fine-tuning.

Given its novelty and rapid development, fusion is likely to remain a methodological research frontier before it can be reliably deployed in conflict research or humanitarian applications. Beyond challenges of domain transfer, key concerns include explainability and trustworthiness68, as fusion may amplify biases in non-transparent ways69. Careful conceptualization of the target phenomenon is essential for data curation, model design and validation, especially where multiple processes co-occur (for example, natural hazard disasters and violence). Yet such settings may be where fusion adds most value, combining textual context with imagery to disentangle complex situations that single sources cannot.

Although foundation models for conflict research promise to be transformative, their development raises difficult ethical questions. With more narrow applications, researchers can control training data and impose targeted limitations. The versatile nature of foundation models, however, means that the same approaches used to understand conflicts and support populations in need could be repurposed to target vulnerable populations or identify military assets. Moreover, advances in generative AI now make it possible to create realistic synthetic satellite imagery. Although the risk to researchers using official providers remains low, this potential for forgery could erode public trust in satellite evidence and underscores the need for future authenticity certification. Addressing these risks requires careful ethical assessment, technical safeguards, and robust governance structures, which are likely to include gated release and access restrictions, particularly in early stages when risks remain poorly understood.

## Way forward

Given the strengths and inherent limitations of text-based and satellite-derived data, data integration is central to developing a more complete understanding of armed conflict. For now, integration at the output level—through improvement and enrichment—is the most feasible path, while data fusion promises even greater insights, especially in information-poor environments. Our aim of enabling large-scale analysis based on text and satellite data leads to two central priorities: expanding what automated approaches can capture across conflict settings and integrating satellite-derived data effectively with text-based data.

First, research with satellite data must prioritize approaches that generalize across forms of violence and conflict settings. Choices about which events and locations are used to train models directly shape what is detectable, and where. Current research focuses heavily on a few locations, such as Ukraine and Gaza, leaving many of the world’s conflicts overlooked. Although models are more difficult to train and validate in areas with limited reference data and informal settlements, ensuring that methods generalize is essential for systematic data collection and for humanitarian actors to respond to the needs of vulnerable populations.

Second, because the most fundamental limits of both data types are inherent to the source and cannot be overcome through innovation, researchers must pursue deeper interdisciplinary collaboration to establish the technical and conceptual foundations for data integration. Both technical expertise and social science insights are essential for adapting techniques to new settings and violence types, and understanding what the data represent. Once we pursue data integration, conceptual clarity becomes even more critical, because the deeper the integration, the richer the data become—but the more potential sources of error and misinterpretation we introduce, for example, when assumptions about spatial or temporal co-occurrence do not hold. Ultimately, broad and genuinely interdisciplinary perspectives are required to navigate the ethical challenges that this work inevitably raises and to ensure that data and code are developed, released and governed in responsible ways that protect vulnerable populations.

By pursuing this agenda across disciplinary boundaries, we can adopt a multi-modal, multi-dimensional approach that moves quantitative conflict research towards a fuller picture of violence in armed conflict—one that enables more effective protection of civilians and more informed policy responses.

## Methods

### Ukraine data collection

For our analyses of building destruction during the Ukraine war, we draw on three existing datasets.

#### War damage data

We use war-related damage data from ref.9, which identifies probable damage across Ukrainian human settlements between March 2022 and October 2023. This dataset was generated using a coherent change detection framework applied to Sentinel-1 SAR data75.

#### Building footprints

Building footprint data were sourced from Overture Maps, providing a comprehensive dataset of 26,714,652 building footprints in Ukraine. The primary sources for these footprints include Microsoft ML Building Footprints (72.8% of buildings) and OpenStreetMap (27.2% of buildings).

#### Tessellated geometries

The unit of analysis is tessellated geometries around populated places. We use the polygons provided by the VIINA dataset73, which are based on the GeoNames gazetteer and include 33,141 tessellated geometries in Ukraine.

#### Boundaries

Spatial data on admin1 and admin2 boundaries, and settlement boundaries for Mariupol and Sievierodonetsk, are from State Scientific Production Enterprise ‘Kartographia’, as provided by the Humanitarian Data Exchange platform74.

#### Areas of control

For areas of control, we used the daily data provided by Violent Incident Information from News Articles (VIINA)73, which draws on four sources: VIINA event reports, DeepStateMap, the Institute for the Study of War, and Wikipedia.

#### Pre-war population data

Pre-war population statistics for Mariupol and Sievierodonetsk are taken from the State Statistics Service of Ukraine (2021, Number of Present Population of Ukraine).

#### Conflict event data

Information on fatalities is taken from the UCDP GED v25.11,14.

### Ukraine data analysis

#### Building-level damage data

We disaggregate damage data based on ref.9to the building level using Overture Maps data. The original damage data are provided as 10-m projected pixel grids corresponding to built-up area identified by Global Human Settlement Layer76. We attribute damage to Overture building footprint data if a building footprint fully (\( > \)99%) overlaps with pixel-wise damage data. This resulted in 246,777 likely damaged Overture Maps building footprints.

#### Improvement section

To examine differences in building destruction before and after territorial control changes between Russian and Ukrainian gains (Fig.3), we first identify changes in control at the level of tessellated geometries and then link these to the war damage data for the corresponding month–geometry combinations.

We aggregate control patterns to a monthly timestep to align with the monthly timestep of damage data. We classify a given month as under full control by one actor if that actor maintained control throughout the entire month; as transitioning from actor A to actor B if A controlled the territory on the first day of the month and B on the last day; and as ‘other’ for all remaining patterns, including contested status at the beginning or end of the month, or control by actor A at both the beginning and end but back and forth in control in between. This yields 569,606 month–geometry combinations under full Ukrainian control, 107,094 under full Russian control, 5,731 for Russian gains, 4,372 for Ukrainian gains, and 19,261 for contested or mixed control during the period of analysis (February 2022 to October 2023).

Next, we identify first stable transitions, defined as the first instance in which a territory transitions from Ukraine to Russia (Russian gains) or from Russia back to Ukraine (Ukrainian gains). A transition is considered stable if it was followed (and for Ukraine regaining territory, also preceded) by stable control. For Ukrainian gains, the territory had to be under full Russian control for at least two months before and under full Ukrainian control for at least two months after the transition. For Russian gains, we require at least two months of full Russian control following the transition. We do not require Russian gains to be preceded by two months of full Ukrainian control because the VIINA control data are only available from February 2022 onward. We are confident that Russian gains in the analysis had been under Ukrainian control prior to the transition because, by construction, month–geometry combinations for Russian gains must begin with Ukrainian control, which excludes territories already under Russian control in February 2022. To control for any buildings damaged prior to our analysis window, we only assess newly damaged buildings across the comparison window and further normalize per 1,000 undamaged buildings at the start of each month.

By focusing on clear and stable transitions, excluding areas that fluctuated between the two sides, and controlling for earlier building damage, we can more confidently attribute damage before and after control changes to Russian and Ukrainian gains separately. A total of 2,438 transitions meet our criteria for first stable Russian gains, of which 2,130 occurred in the initial phase of the invasion (February and March 2022), 108 in April 2022, and 200 between May 2022 and October 2023. For Ukraine, we identify 967 first stable transitions that meet our criteria, all of which fall in the period between May 2022 and October 2023. For the box plots in Fig.3band Extended Data Figs.3and4, and the statistical analyses presented in Extended Data Tables1and2and Supplementary Table1inSupplementary Information, we restrict the analyses to populated areas, removing geometries with no buildings in our building layer. For Russian gains, this leaves 273 populated areas in February and March 2022, 29 in April 2022, and 95 between May 2022 and October 2023. For Ukraine, it leaves 148 populated areas between May 2022 and October 2023.

For the map of territorial control change (Fig.3a), we visualize all first stable transitions that occurred during the frontline war (May 2022 to October 2023). In addition, we also visualize all tessellated areas that experienced at least one monthly change in territorial control during the study period. For the latter, we include areas that were (1) not under full Russian control in February 2022 but were under full Russian control for at least one month between March 2022 and October 2023, or (2) under full Russian control in February 2022 but were under full Ukrainian control for at least one month between March 2022 and October 2023.

To visualize the distribution of damage, we normalize the timelines by assigning month 0 to the month of the control change (first stable transition), with a five-month window spanning two months before to two months after (m−2tom+2). Using the tessellated month–geometry combinations with normalized timelines, we attribute damage to Russian versus Ukrainian gains and visualize the distributions using box plots (Fig.3b). Each box aggregates the newly damaged-building counts across the cells with at least one newly damaged building in that specific relative month. Cells with zero new damage in a given month do not contribute to that month’s box but may contribute to others.

To assess the difference in targeting patterns, we conduct a two-step statistical analysis. First, we compare, at each relative month in the five-month window (m−2tom+2), the proportion of populated areas that experienced damage around control change between areas gained by Russia and those retaken by Ukraine (two-sided Pearson chi-squared test, results reported in the main text and Extended Data Table1). Second, we conduct two-sided Kolmogorov–Smirnov and Mann–Whitney tests to compare levels of damage associated with Russian and Ukrainian gains, conditional on at least one newly damaged building in monthm(reported in Fig.3and Extended Data Table2). The results of the two-step analysis show that, in the months around the transition, Russian territorial gains are more often associated with building damage than Ukrainian gains (Extended Data Table1), and the median number of newly damaged buildings per 1,000 intact buildings is roughly twice as high for Russian gains, a significant difference (Extended Data Table2). To check the independence assumption underlying the per-month tests, we compute Moran’sIon log1p(newly damaged buildings) using a spatio-temporal weights matrix (full results and interpretation in Supplementary Information, sectionE).

The war damage data are available from March 2022 to October 2023. For the main analysis, we include only control changes from May 2022 onward, which is approximately when the frontline war began. Many sources date the beginning of the ‘Battle of Donbas’ to 18 April 2022; however, because our war damage data are at monthly resolution, we use May 2022 as the starting point. This approach has two advantages: it aligns with the temporal resolution of our damage data, and it ensures that damage data for the two months preceding control changes are available (as the damage data only extend back to March 2022). In the extended data, we present the same analysis for the full period covered by the war damage data (Extended Data Fig.3) and further disaggregate Russian gains into three phases: the initial multi-front invasion, the reorientation phase and the frontline war (Extended Data Fig.4).

#### Enrichment section

For the enrichment analysis presented in Fig.5, we use the month-settlement unit as the common unit of analysis to compare fatalities and war damage over time. To identify relevant conflict events, we perform a spatial intersection between the UCDP GED event coordinates and the settlement boundaries. While the majority of fatalities were recorded with a temporal precision of one month or finer, some events involving high fatality counts were recorded with a lower temporal precision level (level 5), indicating a range exceeding one month. Excluding these data points would have distorted the overall level of fatalities, particularly in Mariupol. To maintain the month-settlement unit, we disaggregate these entries by distributing fatalities uniformly across the days within the reported date range.

Regarding spatial precision, our primary estimates include only events coded at the settlement level (the highest precision level). Given the documented urban bias in conflict event data, we are confident that most events occurring within Mariupol and Sievierodonetsk are captured at this level. However, to account for events occurring within settlement boundaries that may have been coded with lower spatial precision, we also provide a broader estimate using spatial precision level 2 (event occurred within 25 km), represented by a dotted line. All fatality figures are based on the UCDP GED ‘best’ estimates. In the Extended Data Fig.8, we also provide ‘high’ estimates reported by UCDP GED (events coded at settlement-level precision only), which show even more pronounced contrasts in fatality levels between the two cities. To facilitate comparison between cities of different size, we report cumulative fatalities as a percentage of pre-war inhabitants, using 2021 population baselines.

The war damage data, originally reported at monthly intervals, required only spatial aggregation via intersection with the settlement boundaries. We report these results as the percentage of the total buildings affected, providing both detected damage and adjusted estimates based on reported true positive rates9, capped at 100%.

### Myanmar data collection

For our analyses of civilian targeting of the Rohingya population in Myanmar, we draw on five existing datasets.

#### Conflict event data

Information on violent events, including involved actors and reported fatalities, is sourced from the UCDP Georeferenced Event Dataset (GED) v25.11,14. In Extended Data Fig.7we replicate our enrichment analyses using ACLED15.

#### War damage

To capture building destruction, we rely on damage assessment data produced by United Nations Institute for Training and Research (UNITAR)–United Nations Satellite Centre (UNOSAT), which record satellite-detected destroyed and damaged settlements in the Buthidaung, Maungdaw and Rathedaung townships of Rakhine State71. These data are based on a manual analysis of satellite imagery collected on multiple dates between 31 August and 11 October 2017.

#### Thermal anomalies

To identify thermal anomalies, we used data from the near-real time VIIRS 375 m Active Fire product (VNP14IMGT)77.

#### Populated areas

To distinguish populated from unpopulated areas, we use raster data from WorldPop70, drawing on the constrained estimates of total population per grid square at 3 arcsec resolution (approximately 100 m at the equator), R2025A v1. We use estimates for 2016—the year preceding the 2017 violent campaign—because violence in Rakhine State led to large-scale population displacement. To select thermal anomalies detected in or near populated areas, we also use village point locations from the Myanmar Information Management Unit (MIMU) v9.678.

#### Administrative units

Spatial data on the administrative boundaries of Myanmar are taken from MIMU v01, via the Humanitarian Data Exchange platform72. We use administrative levels one (state), two (district) and three (township).

### Myanmar data analysis

#### Improvement section, settlement level

We conduct local analyses at the level of individual settlements (villages or towns) across multiple locations in northern Rakhine State. In a first step, we use text-based conflict event data (UCDP GED) to identify settlements in which government violence against civilians involving killings was reported during the initial phase of the 2017 campaign. The majority of lethal conflict events occurred between 25 August and 9 September 2017. Our analysis focuses on the window of 25 August to 16 September 2017, representing the narrowest temporal interval that captures the peak violence while also aligning with the capture dates of satellite-derived war damage data. We restrict the conflict event data to observations with the highest level of spatial precision—that is, events for which the affected settlement was recorded.

For each settlement, we define a settlement-specific spatial window based on the visually interpreted settlement extent. We then integrate gridded population data at 100 m resolution from WorldPop, clipped to each settlement’s spatial window, to delineate inhabited space prior to violence. Population cells with zero values are excluded, and the remaining cells are converted to polygons to enable spatial intersection with satellite-derived damage assessments. Prior to this intersection with the more spatially precise satellite-derived damage data, the entire populated polygon is assumed to be affected by violence.

To further refine this area, we incorporate UNITAR-UNOSAT damage polygons and restrict these data to observations dated on or before the second available satellite image acquisition date (16 September 2017). We spatially intersect the damage polygons with each settlement’s populated polygon to classify each populated image pixel within the spatial window as damaged or undamaged. This enables us to distinguish between settlements that experienced physical damage and those that did not within a tightly bounded local context, thereby refining the spatial footprint implied by settlement-level conflict event reporting.

The article presents the results of this analysis for one such settlement, Chut Pyin (Fig.2), where a large-scale massacre occurred during the analysis period56. In Extended Data Figs.1and2, we present the same analyses for additional settlements, and in Supplementary Information, sectionDwe discuss how they can be conducted at scale. Study locations were selected based on the availability of satellite-derived damage assessments in an otherwise information-poor conflict environment.

#### Improvement section, state level

To illustrate how satellite-derived data can be used to improve spatial precision in cases where reported events are located at coarse administrative levels, we again focus on the 2017 violence in Rakhine State, Myanmar.

We restrict the UCDP GED conflict event data to events recorded in Rakhine State. Of the 54 events reported in 2017, 42 (78%) occurred within a two-week period between 25 August and 9 September 2017; we therefore limited our analysis to this time frame.

For approximately half of these events, we know within which village or town they occurred. All these events with high spatial precision occurred in Maungdaw and Sittwe districts in the northern part of Rakhine State. For an additional third of events, the district is known; in all cases, this is Maungdaw district. The remaining events—accounting for 281 reported fatalities (best estimate)—are recorded as occurring in Rakhine State without any sub-state location information.

To narrow down the areas likely affected by the violent campaign, we analysed active fire detections from the NRT VIIRS 375 m product (VNP14IMGT) between 25 August and 9 September 2017. These detections are point features, which we restricted to the Rakhine State boundary using administrative level-one shapefiles. We further intersected the fire detections with a 500-m radial buffer around settlement locations to differentiate potential village burning from wildfires. To further distinguish these events from non-conflict-related events, such as agricultural burning or industrial heat emissions, we conducted visual verification using publicly available historical very high-resolution imagery available through Google Earth and optical imagery from the Copernicus Sentinel-2 mission79. Fires were positively attributed to the campaign only when thermal detections co-occurred with visible evidence of settlement destruction, such as scorch marks, burned structures, or collapsed roofs.

We then aggregated confirmed thermal anomalies to townships by intersecting detections with third-level administrative polygons. We constructed a binary indicator for each township denoting whether it contained at least one confirmed thermal anomaly during the analysis period. This produced a state-wide map of administrative units with physical evidence consistent with widespread settlement burning. We detected thermal anomalies exclusively in the townships in which spatially precisely coded killings took place. No thermal anomalies were detected elsewhere in Rakhine State during the period under investigation.

Using this exclusion-based logic, we infer that the imprecisely coded conflict events are likely to have occurred in the same northern part of the state as the precisely located events, rather than elsewhere in Rakhine. Importantly, this process does not reassign individual events to specific locations. Rather, it demonstrates how satellite-derived data can be used to narrow the plausible geography of coarse event locations for descriptive and statistical downstream analyses in cases where lethal violence and the burning of structures spatially and temporally co-occur. Because VIIRS detections capture thermal activity rather than violence per se, and because fires may go undetected due to cloud cover or timing, the absence of detections should not be interpreted as definitive evidence of the absence of violence.

#### Enrichment section

For the enrichment analyses presented in Fig.4and Extended Data Fig.6, we integrate text-based conflict event data from UCDP GED with satellite-derived damage data from UNITAR-UNOSAT into a single tabular dataset. The spatial unit of analysis is the township. We focus on three townships in northern Rakhine State—Maungdaw, Buthidaung and Rathedaung—for which UNOSAT data are available.

To compare fatalities and war damage over time, we first align the damage data and the conflict event data temporally. Damage assessments are tied to specific image acquisition dates, which are irregular over time. Conflict event data, by contrast, are temporally more fine-grained and, in the large majority of cases, report the exact date of an event. Because the UNOSAT data have the coarser temporal resolution, they define the temporal unit of analysis. In our case, the UNOSAT data contained 22 distinct acquisition dates, with intervals between acquisitions ranging from 1 to 35 days. For interpretability of the time series, we collapse closely spaced acquisition dates, resulting in 17 analysis periods with intervals between 5 and 35 days. These periods constitute the temporal unit of analysis used throughout the enrichment example.

To aggregate the conflict event data to these periods, we first subset the data to events that are known to have occurred in Rakhine State. For approximately 80% of events, the precise date on which they occurred is reported (temporal precision 1). The rest of events are recorded with lower temporal precision and information about the period within which they occurred. To allow alignment with the UNOSAT periods, we distribute fatalities uniformly across the days within the reported date range—a common procedure in conflict research for temporally disaggregating event data80. After constructing the daily conflict event data, we restrict the sample to the period of UNOSAT damage data availability (ending 18 March 2018). Although the violent campaign began on 25 August 2017, the first UNOSAT image was not acquired until 31 August 2017. Consequently, damage detected between the first two image acquisitions is attributed to the full period from the campaign’s onset to the date of the second image. We assign each daily observation to the corresponding UNOSAT acquisition period, enabling direct aggregation of fatalities to the satellite-defined temporal units.

Next, we spatially intersect UNOSAT damage polygons with township boundaries (administrative level 3) to assign each observation to a specific administrative unit. In instances where a single damage polygon spanned multiple townships, we retain only the fragment with the largest overlap to ensure unique assignment. We apply a similar filtering process to the UCDP GED conflict data, restricting the sample to events with spatial precision levels 1 (exact location) and 2 (known location within a 25 km radius). Events at precision level 3 (second-level unit known) are excluded as they are too spatially imprecise for our township-level analysis. This results in the exclusion of over half of the recorded events, underscoring how improvements in spatial precision (such as those demonstrated in Fig.2) facilitate more advanced forms of data integration.

We then aggregate both datasets to a common township-period unit of analysis. For the damage data, we calculate the total destroyed or damaged area in m2and convert to km2. For the conflict event data, we compute the sum of the best-estimate fatalities. To enable consistent comparisons over time, we complete both panels by explicitly adding missing township–period combinations and setting damaged area and fatalities to zero where no observations were recorded for a given township-period.

Finally, we merge the two datasets into a single township-by-period panel, which forms the basis for the township-level time series shown in Fig.4and Extended Data Figs.6and7. Given the highly skewed distribution of both variables, we visualize both series using a log10(x+ 1) transformation. This approach preserves zero values while facilitating comparison across periods of varying magnitudes. The main text presents the comparative plots for Maungdaw and Buthidaung townships. In Extended Data Fig.6, we present the corresponding visualizations for Rathedaung, and in Extended Data Fig.7the fatality counts using ACLED data instead of UCDP GED.

### Reporting summary

Further information on research design is available in theNature Portfolio Reporting Summarylinked to this article.

## Data availability

All data necessary to reproduce results and figures are available athttps://doi.org/10.5281/zenodo.21809900(ref.81).

## Code availability

All scripts and information necessary to reproduce results and figures are available athttps://doi.org/10.5281/zenodo.21809900(ref.81).

## References

1. Davies, S., Pettersson, T., Sollenberg, M. & Oberg, M. Organized violence 1989–2024, and the challenges of identifying civilian victims.J. Peace Res.62, 1223–1240 (2025).ArticleGoogle Scholar
2. Dawkins, S. The problem of the missing dead.J. Peace Res.58, 1098–1116 (2021).ArticleGoogle Scholar
3. Dietrich, N. & Eck, K. Known unknowns: media bias in the reporting of political violence.Int. Interact.46, 1043–1060 (2020).ArticleGoogle Scholar
4. Miller, E., Kishi, R., Raleigh, C. & Dowd, C. An agenda for addressing bias in conflict data.Sci. Data9, 593 (2022).ArticlePubMedPubMed CentralGoogle Scholar
5. Weidmann, N. B. A closer look at reporting bias in conflict event data.Am. J. Polit. Sci.60, 206–218 (2016).ArticleGoogle Scholar
6. Weidmann, N. B. On the accuracy of media-based conflict event data.J. Confl. Resolut.59, 1129–1149 (2015).ArticleGoogle Scholar
7. Mueller, H., Groeger, A., Hersh, J., Matranga, A. & Serrat, J. Monitoring war destruction from space using machine learning.Proc. Natl Acad. Sci. USA118, e2025400118 (2021).ArticleCASPubMedPubMed CentralGoogle Scholar
8. Hou, Z. et al. War city profiles drawn from satellite images.Nat. Cities1, 359–369 (2024).ArticleGoogle Scholar
9. Scher, C. & Van Den Hoek, J. Nationwide conflict damage mapping with interferometric synthetic aperture radar: a study of the 2022 Russia–Ukraine conflict.Sci. Remote Sens.11, 100217 (2025).ArticleGoogle Scholar
10. Dietrich, O. et al. An open-source tool for mapping war destruction at scale in Ukraine using Sentinel-1 time series.Commun. Earth Environ.6, 215 (2025).ArticleADSGoogle Scholar
11. Racek, D., Zhang, Q., Thurner, P. W., Zhu, X. X. & Kauermann, G. Unsupervised detection of building destruction during war from publicly available radar satellite imagery.PNAS Nexus4, pgaf367 (2025).ArticlePubMedPubMed CentralGoogle Scholar
12. Scher, C. & Van Den Hoek, J. Active InSAR monitoring of building damage in Gaza during the Israel–Hamas War. Preprint athttps://doi.org/10.48550/arXiv.2506.14730(2025).
13. Karwowska, K., Slesinski, J., Sekrecka, A., Smiarowski, M. & Metsoja, K. Integrating optical and radar satellite data for conflict-related change detection in Ukraine.Sci. Rep.16, 12557 (2026).ArticleADSCASPubMedPubMed CentralGoogle Scholar
14. Sundberg, R. & Melander, E. Introducing the UCDP Georeferenced Event Dataset.J. Peace Res.50, 523–532 (2013).ArticleGoogle Scholar
15. Raleigh, C., Kishi, R. & Linke, A. Political instability patterns are obscured by conflict dataset scope conditions, sources, and coding choices.Humanit. Soc. Sci. Commun.10, 74 (2023).ArticleGoogle Scholar
16. LaFree, G. & Dugan, L. Introducing the global terrorism database.Terror. Polit. Violen.19, 181–204 (2007).ArticleGoogle Scholar
17. Croicu, M. & Eck, K. Reporting of non-fatal conflict events.Int. Interact.48, 450–470 (2022).ArticleGoogle Scholar
18. Öberg, M. & Yilmaz, M. C. Measurement issues in conflict event data: addressing some misconceptions about what drives differences between human-coded event datasets.Res. Polit.12, 20531680251362440 (2025).ArticleGoogle Scholar
19. Jean, N. et al. Combining satellite imagery and machine learning to predict poverty.Science353, 790–794 (2016).ArticleADSCASPubMedGoogle Scholar
20. Tuia, D. et al. Artificial intelligence to advance earth observation: a review of models, recent trends, and pathways forward.IEEE Geosci. Remote Sens. Mag.13, 2–25 (2025).ArticleGoogle Scholar
21. Coluzzi, R. et al. Rapid landslide detection from free optical satellite imagery using a robust change detection technique.Sci. Rep.15, 4697 (2025).ArticleADSCASPubMedPubMed CentralGoogle Scholar
22. Rußwurm, M., Venkatesa, S. J. & Tuia, D. Large-scale detection of marine debris in coastal areas with Sentinel-2.iScience26, 108402 (2023).ArticleADSPubMedPubMed CentralGoogle Scholar
23. Bennett, M. M., Van Den Hoek, J., Zhao, B. & Prishchepov, A. V. Improving satellite monitoring of armed conflicts.Earths Future10, e2022EF002904 (2022).ArticleADSGoogle Scholar
24. Sticher, V., Wegner, J. D. & Pfeifle, B. Toward the remote monitoring of armed conflicts.PNAS Nexus2, pgad181 (2023).ArticlePubMedPubMed CentralGoogle Scholar
25. Avtar, R. et al. Remote sensing for international peace and security: its role and implications.Remote Sens.13, 439 (2021).ArticleADSGoogle Scholar
26. Jaafar, H., Sujud, L. & Woertz, E. Scorched earth tactics of the “Islamic State” after its loss of territory: intentional burning of farmland in Iraq and Syria.Reg. Environ. Change22, 120 (2022).ArticleGoogle Scholar
27. Kussul, N. et al. Assessment of war-induced agricultural land use changes in Ukraine using machine learning applied to Sentinel satellite data.Int. J. Appl. Earth Obs. Geoinf.140, 104551 (2025).Google Scholar
28. Asi, Y. et al. Nowhere and no one is safe’: spatial analysis of damage to critical civilian infrastructure in the Gaza Strip during the first phase of the Israeli military campaign, 7 October to 22 November 2023.Confl. Health18, 24 (2024).ArticlePubMedPubMed CentralGoogle Scholar
29. Yu, Y., Liu, S., Li, Y. & Shi, K. Satellite remotely sensed nighttime lights reveal spatiotemporal dynamics of the Ukrainian-Russian conflict.IEEE Geosci. Remote Sens. Lett.20, 1–5 (2023).CASGoogle Scholar
30. Croicu, M.Forecasting Battles: New Machine Learning Methods for Predicting Armed Conflict. PhD thesis, Uppsala Univ. (2025).
31. Zhukov, Y. Near-real time analysis of war and economic activity during Russia’s invasion of Ukraine.J. Comp. Econ.51, 1232–1243 (2023).ArticleGoogle Scholar
32. Braun, L. & Oswald, C. Automated information extraction from text variables in event datasets with large language models. Preprint athttps://doi.org/10.31235/osf.io/yxp8k_v3(2025).
33. Simon, É. et al. Abstractive event analysis of armed conflicts: introducing the UCDP-AEC dataset. InProc. 21st Conference on Natural Language Processing Workshops(eds Wartena, C. & Heid, U.) 104–119 (2025).
34. GDELT: Global Database of Events, Language and Tone.The GDELT Projecthttps://www.gdeltproject.org/(accessed 13 May 2026).
35. Eck, K. In data we trust? A comparison of UCDP GED and ACLED conflict events datasets.Coop. Confl.47, 124–141 (2012).ArticleGoogle Scholar
36. Grace, I. et al. POLECAT Weekly Datahttps://doi.org/10.7910/dvn/ajgvit(2023).
37. Boschee, E. et al. ICEWS Coded Event Datahttps://doi.org/10.7910/dvn/28075(2015).
38. Althaus, S., Peyton, B. & Shalmon, D. A total error approach for validating event data.Am. Behav. Sci.66, 603–624 (2022).ArticleGoogle Scholar
39. Donnay, K., Dunford, E. T., McGrath, E. C., Backer, D. & Cunningham, D. E. Integrating conflict event data.J. Confl. Resolut.63, 1337–1364 (2019).ArticleGoogle Scholar
40. Limonier, K. & Audinet, M. From restricted to digital fieldwork: a renewed methodological framework for Russian studies after the full-scale invasion of Ukraine.Communist Post Communist Stud.https://doi.org/10.1525/cpcs.2025.2474792(2025).ArticleGoogle Scholar
41. Van der Windt, P. & Humphreys, M. Crowdseeding in eastern Congo: using cell phones to collect conflict events data in real time.J. Confl. Resolut.60, 748–781 (2016).ArticleGoogle Scholar
42. Gates, S., Hegre, H., Nygård, H. M. & Strand, H. Development consequences of armed conflict.World Dev.40, 1713–1722 (2012).ArticleGoogle Scholar
43. Ghobarah, H. A., Huth, P. & Russett, B. Civil wars kill and maim people—long after the shooting stops.Am. Polit. Sci. Rev.97, 189–202 (2003).ArticleGoogle Scholar
44. Negash, E. et al. Remote sensing reveals how armed conflict regressed woody vegetation cover and ecosystem restoration efforts in Tigray (Ethiopia).Sci. Remote Sens.8, 100108 (2023).ArticleGoogle Scholar
45. Krampe, F., Kreutz, J. & Ide, T. Armed conflict causes long-lasting environmental harms.Environ. Secur.https://doi.org/10.1177/27538796251323739(2025).
46. Weinthal, E. & Sowers, J. Targeting infrastructure and livelihoods in the West Bank and Gaza.Int. Affairs95, 319–340 (2019).ArticleGoogle Scholar
47. Feuer, A. Environmental warfare tactics in irregular conflicts.Perspect. Polit.21, 533–549 (2023).ArticleGoogle Scholar
48. Naghizadeh, M. H. The uses for fire data and satellite images in monitoring, detecting, and documenting collective political violence.Res. Polit.https://doi.org/10.1177/20531680241261769(2024).
49. Duncan, E. C., Skakun, S., Kariryaa, A. & Prishchepov, A. V. Detection and mapping of artillery craters with very high spatial resolution satellite imagery and deep learning.Sci. Remote Sens.7, 100092 (2023).ArticleGoogle Scholar
50. Feizizadeh, B. et al. An integrated object-based-deep learning approach applied for mapping armed conflict impacts and land scars.Sci. Remote Sens.12, 100257 (2025).ArticleGoogle Scholar
51. Eklund, L. & Dinc, P. Fires as collateral or means of war: challenges of environmental peacebuilding in the Kurdistan Region of Iraq.Ecol. Soc.29, 25 (2024).ArticleGoogle Scholar
52. Yin, H., Eklund, L., Habash, D., Qumsiyeh, M. B. & Van Den Hoek, J. Evaluating war-induced damage to agricultural land in the Gaza Strip since October 2023 using PlanetScope and SkySat imagery.Sci. Remote Sens.11, 100199 (2025).ArticleGoogle Scholar
53. Zhukov, Y. M., Byers, J. S., Davidson, M. A. & Kollman, K. Integrating data across misaligned spatial units.Polit. Anal.32, 17–33 (2023).ArticleGoogle Scholar
54. Eicher, C. L. & Brewer, C. A. Dasymetric mapping and areal interpolation: implementation and evaluation.Cartogr. Geogr. Inf. Sci.28, 125–138 (2001).ArticleGoogle Scholar
55. Mennis, J. Generating surface models of population using dasymetric mapping.Prof. Geogr.55, 31–42 (2003).ArticleGoogle Scholar
56. Myanmar: “We Will Destroy Everything”: Military Responsibility for Crimes Against Humanity in Rakhine State.Amnesty Internationalhttps://reliefweb.int/report/myanmar/myanmar-we-will-destroy-everything-military-responsibility-crimes-against-humanity(2018).
57. Schutte, S. & Kelling, C. A Monte Carlo analysis of false inference in spatial conflict event studies.PLoS ONE17, e0266010 (2022).ArticleCASPubMedPubMed CentralGoogle Scholar
58. Radford, A. et al. Learning transferable visual models from natural language supervision. InPMLR139, 8748–8763 (2021).
59. Yang, J. et al. Vision-language pre-training with triple contrastive learning. InProc. IEEE/CVF Conference on Computer Vision and Pattern Recognition15671–15680 (2022)
60. Kalyvas, S. N.The Logic of Violence in Civil War, 1st edn (Cambridge Univ. Press, 2006).
61. Wenckstern, J. et al. AI-powered virtual tissues from spatial proteomics for clinical diagnostics and biomedical discovery. InICLR 2025 Workshop on Machine Learning for Genomics Explorationshttps://iclr.cc/virtual/2025/37004(2025).
62. Xiang, J. et al. A vision–language foundation model for precision oncology.Nature638, 769–778 (2025).ArticleADSCASPubMedPubMed CentralGoogle Scholar
63. Lu, Y. & Wang, A. Integrating language into medical visual recognition and reasoning: a survey.Med. Image Anal.102, 103514 (2025).ArticlePubMedGoogle Scholar
64. Zermatten, V., Castillo-Navarro, J., Marcos, D. & Tuia, D. Learning transferable land cover semantics for open vocabulary interactions with remote sensing images.ISPRS J. Photogramm. Remote Sens.220, 621–636 (2025).ArticleADSGoogle Scholar
65. Daroya, R., Cole, E., Mac Aodha, O., van Horn, G. & Maji, S. Wildsat: learning satellite image representations from wildlife observations. InProc. International Conference on Computer Visionhttps://doi.org/10.1109/ICCV51701.2025.00580(2025).
66. Liu, W., Wu, G., Wang, H. & Ren, F. Cross-modal data fusion via vision-language model for crop disease recognition.Sensors25, 4096 (2025).ArticleADSPubMedPubMed CentralGoogle Scholar
67. Yang, L. et al. Survey of multimodal geospatial foundation models: techniques, applications, and challenges. Preprint athttps://doi.org/10.48550/arXiv.2510.22964(2025).
68. Karpatne, A. et al. AI-enabled scientific revolution in the age of generative AI: second NSF workshop report.npj Artif. Intell.1, 18 (2025).ArticleGoogle Scholar
69. Acosta, J. N., Falcone, G. J., Rajpurkar, P. & Topol, E. J. Multimodal biomedical AI.Nat. Med.28, 1773–1784 (2022).ArticleCASPubMedGoogle Scholar
70. Tatem, A. J. WorldPop, open data for spatial demography.Sci. Data4, 170004 (2017).ArticlePubMedPubMed CentralGoogle Scholar
71. UNOSAT.Destroyed Areas in Buthidaung, Maungdaw, and Rathedaung Townships of Rakhine State in Myanmar(UN Institute for Training and Research, 2018).
72. Myanmar Information Management Unit (MIMU).Myanmar - Subnational Administrative Boundarieshttps://data.humdata.org/dataset/cod-ab-mmr(OCHA, 2025).
73. Zhukov, Y. & Ayers, N. VIINA 2.0: violent incident information from news articles on the 2022 Russian invasion of Ukraine. Version 2.0https://github.com/zhukovyuri/VIINA(2023).
74. State Scientific Production Enterprise “Kartographia”.Ukraine - Subnational Administrative Boundarieshttps://data.humdata.org/dataset/cod-ab-ukr(OCHA, 2022).
75. Copernicus Sentinel-1 mission.European Space Agencyhttps://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1(accessed 26 January 2026).
76. Pesaresi, M. GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel2 composite and Landsat, multitemporal (1975-2030).JRC Data Cataloguehttps://doi.org/10.2905/JRC.939FACR(European Commission, 2023).
77. NASA VIIRS Land Science Team.VIIRS (S-NPP) I Band 375 m Active Fire Product NRT (Vector Data)https://doi.org/10.5067/FIRMS/VIIRS/VNP14IMGT_NRT.002(NASA, 2020).
78. Myanmar Information Management Unit.Village Points Rakhine State PCode v9.6https://data.humdata.org/dataset/mimu-geonode-village-points-rakhine-state-pcode(OCHA, 2026).
79. Copernicus Sentinel-2 Mission.European Space Agencyhttps://dataspace.copernicus.eu/data-collections/copernicus-sentinel-missions/sentinel-2(accessed 26 January 2026).
80. Bara, C. & Schumann, M. P. Who, what, and where? Linking violence to civil wars.Res. Polit.https://doi.org/10.1177/20531680251328885(2025).
81. Sticher, V. et al. Replication package for: Advancing conflict research and response through satellite-derived data.Zenodohttps://doi.org/10.5281/zenodo.21809900(2026).
82. Myanmar: Remaking Rakhine State(Amnesty International, 2018).

Download references

## Acknowledgements

We thank T. Ton-That Whelan, M. E. Paquette, J. Kissling, N. Cadorin, L. Dasen, M. D. Cavelty, M. Gilli, K. Rickard, L. Schmidt, P. Tasche and members of the Conflict Colloquium of the International Conflict Research group at ETH Zurich for comments and feedback on earlier versions of this manuscript.

## Funding

This work was supported by the Engineering for Humanitarian Action initiative (Humanitarian Crisis Detection With Nightlight, Remote Monitoring of Armed Conflicts), the Swiss innovation agency Innosuisse (grant 116.740 IP-ICT), and the National Aeronautics and Space Administration (grant 80NSSC25K7001). Open access funding provided by Swiss Federal Institute of Technology Zurich.

## Author information

### Authors and Affiliations

1. Center for Security Studies, ETH Zurich, Zurich, SwitzerlandValerie Sticher, Corinne Bara & Jenniina Kotajoki
2. Department of Political Science, University of Zurich, Zurich, SwitzerlandValerie Sticher & Karsten Donnay
3. United Nations Satellite Centre (UNOSAT), Geneva, SwitzerlandLars Bromley & Manuel Fiol
4. World Food Programme (WFP), Rome, ItalyThierry Crevoisier
5. Environmental Computational Science and Earth Observation Laboratory, EPFL, Sion, SwitzerlandEmanuele Dalsasso, Filip Dorm & Devis Tuia
6. Université Grenoble Alpes, Inria, CNRS, Grenoble INP, LJK, Grenoble, FranceEmanuele Dalsasso
7. Photogrammetry and Remote Sensing, ETH Zurich, Zurich, SwitzerlandOlivier Dietrich & Konrad Schindler
8. Digital Society Initiative, University of Zurich, Zurich, SwitzerlandKarsten Donnay
9. State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University, Wuhan, ChinaXi Li
10. German Institute of Global and Area Studies, Hamburg, GermanyMikael Hiberg Naghizadeh
11. College of Earth, Ocean, and Atmospheric Sciences, Oregon State University, Corvallis, OR, USACorey Scher & Jamon Van Den Hoek
12. EcoVision Lab, Department of Mathematical Modeling and Machine Learning, University of Zurich, Zurich, SwitzerlandJan Dirk Wegner
Authors
1. Valerie SticherView author publicationsSearch author on:PubMedGoogle Scholar
2. Corinne BaraView author publicationsSearch author on:PubMedGoogle Scholar
3. Jenniina KotajokiView author publicationsSearch author on:PubMedGoogle Scholar
4. Lars BromleyView author publicationsSearch author on:PubMedGoogle Scholar
5. Thierry CrevoisierView author publicationsSearch author on:PubMedGoogle Scholar
6. Emanuele DalsassoView author publicationsSearch author on:PubMedGoogle Scholar
7. Olivier DietrichView author publicationsSearch author on:PubMedGoogle Scholar
8. Karsten DonnayView author publicationsSearch author on:PubMedGoogle Scholar
9. Filip DormView author publicationsSearch author on:PubMedGoogle Scholar
10. Manuel FiolView author publicationsSearch author on:PubMedGoogle Scholar
11. Xi LiView author publicationsSearch author on:PubMedGoogle Scholar
12. Mikael Hiberg NaghizadehView author publicationsSearch author on:PubMedGoogle Scholar
13. Corey ScherView author publicationsSearch author on:PubMedGoogle Scholar
14. Jamon Van Den HoekView author publicationsSearch author on:PubMedGoogle Scholar
15. Konrad SchindlerView author publicationsSearch author on:PubMedGoogle Scholar
16. Devis TuiaView author publicationsSearch author on:PubMedGoogle Scholar
17. Jan Dirk WegnerView author publicationsSearch author on:PubMedGoogle Scholar

### Contributions

V.S.: conceptualization (lead), project administration (lead), writing—original draft (lead), revisions and editing (lead), data curation, analysis (Ukraine enrichment: lead; Ukraine improvement), methodology (lead), visualizations (lead), literature review, funding acquisition and supervision. C.B.: conceptualization, writing—original draft, revisions and editing, data curation, analysis (Myanmar improvement and enrichment: lead), methodology, visualizations, literature review, funding acquisition and supervision. J.K.: writing—original draft, revisions and editing, methodology and literature review (lead). L.B., T.C. and M.F.: practical examples, literature review and writing—review and editing; E.D. and F.D.: visualizations, literature review and writing—original draft, review and editing. O.D., K.D. and X.L.: visualizations, literature review and writing—review and editing. M.H.N.: analysis (Myanmar improvement), literature review and writing—review and editing. C.S.: data curation, analysis (Ukraine improvement: lead), methodology and writing—review and editing. J.V.D.H.: analysis (Ukraine improvement), literature review, methodology, supervision and writing—review and editing. K.S.: funding acquisition, supervision and writing—review and editing. D.T.: visualizations, funding acquisition, supervision and writing—original draft, review and editing. J.D.W.: conceptualization, funding acquisition, methodology, supervision and writing—review and editing.

### Corresponding authors

Correspondence toValerie SticherorCorinne Bara.

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Peer review

### Peer review information

Naturethanks Hannes Mueller and the other, anonymous, reviewers for their contribution to the peer review of this work.Peer reviewer reportsare available.

## Additional information

Publisher’s noteSpringer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Extended data figures and tables

### Extended Data Fig. 1 Local-level spatial violence attribution in Inn Din, Rakhine State.

a, Pre-event optical imagery (27 December 2016) of Inn Din, a mixed-ethnicity village.b, Post-event optical imagery (1 October 2020) showing selective destruction. The entirely destroyed areas are Rohingya areas within the village, while the ethnic Rakhine area in the North of the village is left completely intact56.c, Spatial distribution of reported fatalities at the settlement level: all populated cells are presumed affected.d, Satellite-detected destruction footprints.e, Refined fatality locations (red) derived from intersecting reported events with destruction data, excluding unaffected areas (green). Images: Google ©2025 CNES/Airbus. Basemap: © OpenStreetMap contributors, ODbL. Data sources:1,14,70,71,72.

### Extended Data Fig. 2 Local-level spatial violence attribution in Gu Dar Pyin, Rakhine State.

Gu Dar Pyin was the site of a mass killing involving several hundred casualties1,14.a, Pre-event optical imagery of the north end of the village (27 December 2016), showing traditional dwellings in irregular spatial arrangements and partly covered by vegetation.b, Post-event optical imagery of the north end of the village (26 November 2019) showing newly constructed houses with highly uniform designs arranged in a regular pattern, suggesting coordinated planning.c, Spatial distribution of reported fatalities at the settlement level: all populated cells are presumed affected.d, Satellite-detected destruction footprints.e, Refined fatality locations (red) derived from intersecting reported events with destruction data, excluding unaffected areas (green). In this case, the spatial data show the almost complete destruction of the village. The before-after images show the subsequent transformation of the village in a pattern that is consistent with reports of coordinated resettlements of ethnic Rakhine populations following the displacement of the original inhabitants82. Images: Google ©2025 CNES/Airbus. Basemap: © OpenStreetMap contributors, ODbL. Data sources:1,14,70,71,72.

### Extended Data Fig. 3 Building damage associated with territorial gains in Ukraine, full time series.

Box plots of newly damaged buildings per 1,000 intact buildings (start of month) across populated areas, in a five-month window centered on the month of control change, stratified by Russian (blue) and Ukrainian (purple) gains from February 2022 to October 2023. Includes only populated areas with first stable transitions and damage; seeMethods. Data sources:9,73. Centre line shows median, box spans interquartile range and whiskers extend to the most extreme observation lying within 1.5 × IQR of the nearest edge of the box.

### Extended Data Fig. 4 Building damage associated with Russian territorial gains in Ukraine, by operational phases.

Box plots of newly damaged buildings associated with Russian territorial gains, per 1,000 intact buildings (start of month) across populated areas, in a five-month window centered on the month of control change, disaggregated across three distinct operational phases: the initial invasion (February–March 2022), Russia’s strategic reorientation toward the Donbas around April 2022, and subsequent frontline war (May 2022–October 2023). These phases reveal substantial variation in destruction intensity associated with Russian advances. Note that our damage data begin in March 2022. The absence of pre-invasion observations is unlikely to substantially affect these patterns, as the full-scale invasion represented an abrupt military escalation in most captured territories. Includes only populated areas with first stable transitions and damage; seeMethods. Data sources:9,73. Centre line shows median, box spans interquartile range and whiskers extend to the most extreme observation lying within 1.5 × IQR of the nearest edge of the box.

### Extended Data Fig. 5 Timeline of building damage in Ukraine.

Total detected newly damaged buildings per month (March 2022 to October 2023). Data sources:9.

### Extended Data Fig. 6 Killings and settlement destruction in Rathedaung township.

a, Reported fatalities (25 August 2017 to 18 March 2018).b, Settlement destruction (25 August 2017–18 March 2018). Data sources:1,14,71,72.

### Extended Data Fig. 7 Fatalities in Maungdaw, Buthidaung, and Rathedaung townships with ACLED data.

a, Maungdaw.b, Buthidaung.c, Rathedaung. All panels show reported fatalities between 25 August 2017 and 18 March 2018. Patterns closely mirror those in Fig.4and Extended Data Fig.6, suggesting that results are robust across the two principal conflict event datasets. Grey dots indicate months with reports of property destruction in ACLED. Data sources:15,72.

### Extended Data Fig. 8 Cumulative fatalities in Mariupol and Sievierodonetsk, best and high estimates.

a, Mariupol.b, Sievierodonetsk. Panels show cumulative deaths as a percentage of the pre-war population, including best and high estimates, for the period February 2022–October 2023. Only events coded at the settlement level are included. Data source:1,14.

Extended Data Table 1 Statistical differences in the proportion of populated areas experiencing destruction between Russian and Ukrainian gains
Full size table
Extended Data Table 2 Statistical differences in levels of destruction between Russian and Ukrainian gains
Full size table

## Supplementary information

### Supplementary Information (download PDF)

This file contains five sections: (A) Data on three aspects of violence; (B) War damage and human toll of conflict; (C) Data generation processes and limitations; (D) Automated spatial improvement; and (E) Spatial autocorrelation analysis (including Supplementary Table 1).

### Reporting Summary (download PDF)

### Peer Review file (download PDF)

## Rights and permissions

Open AccessThis article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visithttp://creativecommons.org/licenses/by/4.0/.

Reprints and permissions

## About this article

### Cite this article

Sticher, V., Bara, C., Kotajoki, J.et al.Advancing conflict research and response through satellite-derived data.Nature(2026). https://doi.org/10.1038/s41586-026-11004-6

Download citation

* Received:19 May 2025
* Accepted:07 August 2026
* Published:09 September 2026
* Version of record:09 September 2026
* DOI:https://doi.org/10.1038/s41586-026-11004-6

### Share this article

Anyone you share the following link with will be able to read this content:

Get shareable link

Sorry, a shareable link is not currently available for this article.

Copy shareable link to clipboard

Provided by the Springer Nature SharedIt content-sharing initiative