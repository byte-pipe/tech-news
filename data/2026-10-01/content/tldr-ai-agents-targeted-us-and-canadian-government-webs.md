---
title: AI Agents Targeted U.S. and Canadian Government Websites | Transluce AI
url: https://transluce.org/us-canada-gov
site_name: tldr
content_file: tldr-ai-agents-targeted-us-and-canadian-government-webs
fetched_at: '2026-10-01T17:18:21.805656'
original_url: https://transluce.org/us-canada-gov
date: '2026-10-01'
description: We discovered a set of additional, similar incidents where rogue AI agents appear to have used aggressive techniques to access public data on government websites.
tags:
- tldr
---

Incident Reports

# AI Agents Targeted U.S. and Canadian Government Websites

Evidence from Arquivo.pt and urlquery.net

Jack Cable
*
,
1
, 
Daniel Chiu
*
, 
Francisco Pernice
*
,
2
, 
Laura Ruis
*
,
2
, 
Selena Zhang
*
,
3
, 
Tetiana Bas
4
, 
Jordan Chetty
5
, 
Farzaan Kaiyom
1
, 
Gary Shen
4
, 
Conrad Stosz
†
,
3
, 
Jacob Steinhardt
†
,
3
1
 
Corridor
 · 
2
 
MIT
 · 
3
 
Transluce
 · 
4
 
AIUC
 · 
5
 
Hertz Foundation
 · 
*
 
First authors, alphabetical
 · 
†
 
Senior authors
Transluce | Published: 
September 30, 2026

Following up on our previousblog post, we discovered several additional incidents where rogue AI agents appear to have used aggressive techniques to access publicly available data on government websites.

This includes two rudimentary and failed hacking attempts, one against the U.S. Department of Education’sCivil Rights Data Collection, and one against Library and Archives Canada, a Canadian federal agency.

These failed attempts connect to additional rogue activity where agents used an array of aggressive tactics short of hacking to probe U.S. government websites, often using sites in unintended ways and sometimes violating explicit usage policies. This activity targeted websites across the White House, the Departments of War, Justice, and Commerce, the CDC and SEC, and state agencies in California, Maryland, Illinois, Texas, and New York.

We have so far identified no instances in these datasets where agents gained access to any information that is not publicly available.

We base our analysis below on data from ourpreviously publishedurlquery.netdataset, as well asArquivo.pt, a Portuguese web archive with a feature called ArchivePageNow that was used to send requests and retrieve data.

## Agents attempted a basic SQL injection on the U.S. Department of Education

On June 17, while apparently looking up school statistics, agents made more than 200,000 requests to a U.S. Department of Education website. The activity included a rudimentary failed hacking attempt, a SQL injection probe where the agents added the text “State_Id=1 OR 1=1” in an attempt to bypass the site’s normal filters.

In the 40 seconds leading up to the SQL injection, there were a series of requests with a variety of unusual state ID inputs (without access to more context about the agents and their reasoning traces, the purpose of this set of queries is unclear):

* State_Id=0
* State_Id=-1
* State_Id=99
* State_Id=999
* State_Id=1,2(potentially to test SQL injections/parameter handling)
* State_Id=(empty string)
* State_Id=1&State_Id=2
* State_Id%5B%5D=1&State_Id%5B%5D=2(URL-encoded square brackets)
* State_Id=1%2C2(URL-encoded comma)

Data stored on this website appears to match a web search task inGoogle's DeepSearchQA benchmark, suggesting that the agents were not given a hacking-related task but were being graded on their ability to successfully retrieve specific niche information from the internet.

The specific DeepSearchQA task (dsqa_250):Using data fromcivilrightsdata.ed.govfor the 2017–2018 school year, determine which of the following states—South Carolina, North Carolina, Georgia, or Virginia—had the highest ratio of full-time equivalent school counselors to students reported as victims of race-related harassment or bullying.

How the agents’ query parameters we observe in Arquivo traffic relate to dsqa_250:

Query parameter
Explanation
survey_Year_Key=9
Corresponds with 2017-2018. Agents often made multiple queries using Arquivo to find this mapping, often enumerating IDs in order.
Measure_Id=130
Corresponds to race-based bullying victims.
State_Id=11
, 
State_Id=28
, 
State_Id=41
, 
State_Id=46
Corresponds to the relevant states.

We also note that more than 10,000 requests included a tag beginning with “oai” (example). 99.6% of those requests use a combination of the three query parameters described above, indicating the submitters of these requests were attempting to answer dsqa_250.

We disclosed this attempted hack to the Department of Education on September 25, 2026. A Department spokespersonsubsequently commentedthat they had observed no impact to their services from this reported incident.

Download the Data

## Agents attempted rudimentary hacks on Library and Archives Canada

On May 28, 2026, and June 9, 2026, Arquivo.pt captured 899 requests hitting the “collection-search” service of Library and Archives Canada (LAC), including a series of apparently failed rudimentary hacking attempts. The requests were associated with retrieving data on divorce records in Canada between 1905 and 1911.

We do not confidently attribute these attempts to OpenAI, but they exhibit tactics consistent with prior observed agent activity that we have attributed to OpenAI in a similar timeframe, including the use ofArquivo.pt, conducting aggressive data collection focused on targeted, obscure information, and probing for cybersecurity vulnerabilities.

Of these 899 requests, 13 of them carried attack payloads rather than ordinary queries, including by probing for vulnerabilities in the record-identifier parameter. The payloads included:

* Three SQL injection probes (an apostrophe,1 OR 1=1, and1,2)
* Anencoded <for cross-site scripting
* 2147483648to test a 32-bit integer boundary
* The stringabcfor non-numeric handling
* Five requests fuzzing the output format (.json,?output=,?raw=,?url=)
* Two toggling adebug=1flag

We do not believe that these probes were successful: each one came back as a normal HTTP 200 with an empty record page, with nothing to indicate the database acted on the input or that any extra data was returned.

We disclosed this attempted hack to the Canadian government on September 28, 2026. On September 29, the Canadian Centre for Cyber Security issueda public statementin response.

## Agents used a range of other aggressive tactics against U.S. state and federal websites

In addition to the above, we identified a broader pattern of automated workflows that we attribute to AI agents with varying levels of confidence, based on task-level connections, shared infrastructure, and timing. Some of this traffic overlaps to varying degrees with prior activity confirmed to be associated with OpenAI, and in some cases agents explicitly mark themselves as being associated with OpenAI. However, we are not attributing this traffic as a whole to OpenAI nor do we attempt to estimate attribution for each incident.

In the below cases, we did not observe hacking techniques. Rather, these workflows use aggressive or gray-area techniques to retrieve information from government websites, sometimes using sites in unintended ways or violating explicit usage policies. This includes techniques like making accounts with disposable email addresses, reusing exposed credentials, bypassing antibot controls, and flooding websites with requests.

We outline our observations here:

* Kansas:On May 7, Arquivo recorded 36,578 user-triggered captures ofKansasMemory.gov(a site apparently administered by the Kansas Historical Society with support from the Kansas government), with a peak of 1,093 captures per minute. Early requestsreturned content, but over the course of the campaign the website started returninggateway timeouts. We were not able to confirm whether the activity caused a service disruption.
* Illinois:On four separate days between April 19 and May 1, we observed 251 related Arquivo captures involving Illinois’s legacy IQuery public-health statistics portal. Initial captures return “service unavailable”, but the automated workflow nevertheless tried workarounds, likedirect IP-routes,URL-parsing variations, anda guessed ePass routethat redirected to the state’s sign-in system. None of the reviewed responses returned IQuery data.
* Maryland:On May 6, Arquivo recorded 295,912 captures across multiple Maryland hosts containing education statistics, peaking at 5,594 captures per minute. The activity involves extensiveguessing of downloadable filenames, alongside a successful download ofpublic aggregate datasets of students’ math performance. Separately, as early as March 2, Arquivo recorded a smaller burst of API requests to Maryland’s mathematics-performance API, although we have not established a connection with the later May activity.
* New York State:On May 17, we observed archived activity attempting to access public New York school-enrollment statistics through modified URLs and multiple intermediary services.Initial requestswere blocked, while later attemptsreturned public statistics. The same school and enrollment selections appear in wiki activity previously documented bycollusion.wiki.
* Texas:Also on May 17, archived results show repeated attempts to retrieve public sexually transmitted infection statistics from the Texas Department of State Health Services, throughdirect export requestsas well as through intermediary conversion services which have previously been reported to be used by agents. We could not confirm successful retrieval of the requested statistics.
* California:On May 26, a sequence of requests apparently bypassed antibot controls and retrieved public campaign-finance records from California'sCAL-ACCESS. The workflowinitially encountered the site’s antibot protectionsystem, but subsequently retrieved records using paths withfile-like suffixes. Retrieved records includecampaign expenditure statements.
* White House Office of Management and Budget:From May 25 to 27, we found 719 urlquery.net reports that appear to be attempts at downloadingtwo public fiscal-year 2023 budget reportsfrom OMB’s MAX.gov system. These reports show 145 distinct submission strings, 416 distinct method/URL pairs, and 243 trace groups spanning 2,922 HTTP entries. The URLs queried include variants with hostnames related to MAX’sloginandPIV, and were sometimes queried throughintermediary services. In one 27-second burst on May 26, the workflow submitted 16 versions of the same PDF URL through markdown.new (a service for converting webpages to agent-readable text), changing only an arbitrary?uniqNquery parameter (example). Other urlquery.net reports show that the workflowsuccessfully downloaded the public PDFand that an intermediary servicesuccessfully extracted text from it into JSON. A preservedcollusion.wiki revisioncontains a matching urlquery.net download reference, and aMay 27 screenshotshows the two reports together with several alternate ways of accessing them.
* U.S. Navy:On April 23–24 and May 18, archived requests probed alternative URLs and endpoints on the Naval History and Heritage Command’s website,history.navy.mil. Some of these returnedimage metadata, while broader attempts to reach the website’scontent-management pagesfor editing or publishing content failed. We found no evidence of access to sensitive military information.
* U.S. Department of Justice:On May 30–31, an automated workflow sought public FBI arrest statistics through the Justice Department’s Office of Juvenile Justice and Delinquency Prevention (OJJDP). Legacy URLs repeatedly redirected to a replacement service, but the workflow succeeded at retrievingthe legacy tableby adding an encoded parent-directory segment. The retrieved data, includinga 1980–2020 robbery table, plausibly matches aDeepSearchQAquestion.
* Bureau of Economic Analysis (U.S. Department of Commerce):On June 18, an automated workflowattempted to registerfor a Bureau of Economic Analysis (BEA) API key using a disposable email address and the self-entered organization name “OpenAI Research,” with no confirmed successful registration. The workflow alsounsuccessfully attempted to use an OCR serviceto make the CAPTCHA machine-readable. The sequence occurred amid a larger cluster of 3,005 BEA-related Arquivo captures between June 16 and 18.
* Census Bureau (U.S. Department of Commerce):Between June 16 and 22, publicly posted URLs indicate attempts to reuse exposed API keys to accesscensus.govdata. Several of the related pages contain OpenAI markers. We do not share underlying URLs in this case to avoid republishing sensitive materials, and found no response showing that these attempts were successful or ever reached census.gov.
* U.S. Securities and Exchange Commission:On June 18, a workflow sought public SEC crowdfunding statistics. Previously documented agent communication claims thatdouble-slash URL paths can bypass rate limits, and separate urlquery.net records demonstrate thoseURLs indeed returning public county data. Ordinary paths also succeeded, so no rate-limit bypass has been demonstrated.
* Centers for Disease Control and Prevention:On July 18, an archived browser-execution program attempted to submit a data request to CDC’s WONDER statistics service (link not included here because it contains executable code), including acceptance of its data-use terms. Acapture one second laterreturns a query-validation error, consistent with execution of the form-submission code, although we are not able to establish the complete execution chain.

## How we identified and assessed the activity

We relied primarily on publicly available data fromurlquery.net(a web security service) andArquivo.pt(a web archive service) to identify the activity above. Agents apparently used these platforms to route their requests around restrictions placed on them either by their developers or by the websites they targeted, but both services also made the agents’ requests public by default. We have identified these and other promising data sources through web searches, references in existing investigations and concrete examples of task-related activity.

As we analyzed this data, our guiding principle was to identify which of this traffic was left by AI agents and to study their behavior as they tried to complete their tasks. For example, we looked for high-volume, apparently automated patterns of requests that appear related to web retrieval tasks that we know previously reported agent swarms were being trained and evaluated on. To identify aggressive tactics, we searched within this traffic for recognizable exploit patterns and related activity, such as SQL expressions inserted where a record ID should be (e.g. “1 OR 1=1”), injected JavaScript, or paths attempting to reach sensitive files such as/etc/passwd.

To help correlate individual requests with each other, we also examined sequences of requests that changed URL paths, encodings, or retrieval services after failures, and we connected related requests through shared record IDs, distinctive URL parameters, and timing.

To implement this approach, we used a combination of regex matching, LLM-as-a-judge, coding agent investigation, and manual human investigation.

## What is Arquivo.pt?

The free online servicearquivo.ptis the national Portuguese web archive, operated by the PortugueseFoundation for Science and Technology(FCT). Its purpose is to allow a user to search and access historical versions of web content collected since 1996. It primarily covers the Portuguese web, but also contains material from international sites and supports full-text search across the archived corpus.

The site’s Terms and Conditions, last updated August 25, 2022, say thatArquivo.ptis intended to support educational, scientific, and research work, and that commercial use is expressly prohibited. They also prohibit using accessed contents for commercial purposes, distribution, modification, or forwarding to other sites.

For a knowledge retrieval task, it provides the following functionality that may be useful to an AI agent:

* It gives an actor able to make HTTP GET requests access to a large corpus of archived web content through a programmable API, with full-text search.
* It can recover information from pages that are unavailable on the live web. Given a URL, an agent can queryArquivo.pt's version history and obtain preserved versions of that page. This is useful when a source has been deleted, moved, changed substantially, or is otherwise inaccessible from the live site.
* It can provide an alternative retrieval path when querying the original site is undesirable.
* It can provide an indirect way to execute JavaScript through its screenshot service. This can help an agent inspect content generated dynamically by scripts without running a browser locally. If the service accepts a page whose scripts the actor controls, it can also provide a means of running actor-supplied JavaScript.