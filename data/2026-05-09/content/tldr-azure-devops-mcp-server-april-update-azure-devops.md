---
title: Azure DevOps MCP Server April Update - Azure DevOps Blog
url: https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/
site_name: tldr
content_file: tldr-azure-devops-mcp-server-april-update-azure-devops
fetched_at: '2026-05-09T11:49:49.070886'
original_url: https://devblogs.microsoft.com/devops/azure-devops-mcp-server-april-update/
author: Dan Hellem
date: '2026-05-09'
published_date: '2026-04-21T14:12:23+00:00'
description: Discover improvements in the Azure DevOps MCP Server Update, including Markdown default settings and new query capabilities.
tags:
- tldr
---

Dan Hellem

Product Manager for Azure Boards, Repos & Wiki
 

This update brings a set of improvements and changes across both local and remote Azure DevOps MCP Servers.

Here’s a summary of what’s changed.

## Query work items with WIQL

We’ve introduced a newwit_query_by_wiqltool that enables users to construct and run work item WIQL queries. For our remote MCP, to ensure reliability and performance, access to this tool is currently limited to users with theInsidersfeature enabled.Learn more.

As we gather usage telemetry and validate query performance, we plan to make it broadly available.

## Remote MCP Server

### Annotations

MCP Annotations are metadata tags that help LLMs understand how to safely and effectively use external tools by providing a shared vocabulary for behavior, context, and risk. We’re implementing annotations for read-only, destructive, and openWorld tools to clearly signal how each tool operates and ensure safer, more reliable interactions.

### Missing tools

There are still a few gaps between the local and remote MCP servers. We’ve recently added support forrepo_get_file_content,repo_list_directory, andrepo_vote_pull_request, and will continue closing these gaps by introducing additional tools in the coming weeks.

### Tool restructuring

One of the key challenges in building an Azure DevOps MCP Server is the sheer surface area that Azure DevOps covers. At the same time, both clients and LLMs tend to perform better with a smaller, more focused set of tools. To address this, we are beginning to consolidate related tools. With our remote MCP Server still in public preview, now is an ideal time to make these improvements. We’re starting incrementally, beginning with the wiki tools, to evaluate performance and usability before expanding further. Here is what you can expect:

 New Tool
 

 Type
 

 Actions / Scope
 

 Replaces
 

wiki

 Read-only
 

get_page
, 
list_pages
, 
list_wikis
, 
get_wiki

wiki_get_page
, 
wiki_get_page_content
, 
wiki_list_pages
, 
wiki_list_wikis
, 
wiki_get_wiki

wiki_upsert_page

 Write
 

 Single operation, no action parameter
 

wiki_create_or_update_page

search_wiki

 Search
 

search_wiki

There will be more changes to come. Keep an eye on thedocumentation for updates.

## Local MCP Server

### Personal Access Token Support

Personal access tokens are now supported for authentication, simplifying the experience for users integrating the Azure DevOps MCP Server with external services and clients such as GitHub Copilot.Learn more

### Elicitations

Elicitations are guided prompts that help ensure the correct information is provided when performing a task. For example, since most operations require a project, we’ve added elicitation support for project selection across the core, work, and work items toolsets.

While elicitations can be helpful, we haven’t yet seen strong demand from the community. As a result, we are experimenting with a limited rollout to evaluate their effectiveness. We would love your feedback. Please share your thoughts in an issue or comment and let us know if you would like to see broader support across more tools and parameters.

### MCP Apps (Experimental)

MCP Apps are an experimental feature that enables packaging and executing common workflows directly within the MCP Server environment. Rather than manually chaining multiple tools together, MCP Apps provide a more structured and repeatable way to perform tasks such as querying or updating work items.

This approach reduces setup time and helps maintain consistency across users and scenarios.

For example, you can use themcp_app_my_work_itemtool to access a self-contained work item experience that allows you to view work items assigned to you, filter results, and open and edit work items.

To try it out, use themcp-apps-pocbranch.

Then update yourmcp.jsonconfiguration to include themcp-appsdomain:

{
 "servers": {
 "ado": {
 "type": "stdio",
 "command": "mcp-server-azuredevops",
 "args": ["contsoso", "-d", "core", "work", "work-items", "mcp-apps"]
 }
 }
}

We’d love your feedback on MCP Apps. If you find them useful, let us know. Your input will help shape whether this capability is brought into the main local and remote MCP Servers.

## Feedback

Stay tuned, more updates are on the way. In the meantime, we’d love your feedback. Please leave a comment on this post orcreate an issuein the MCP Server repository.

### Category

* Azure & Cloud

### Topics

* #DevOps
* Azure Boards
* Azure DevOps
* Community
* MCP Server

### Share

 

## Author

Dan Hellem
Product Manager for Azure Boards, Repos & Wiki

Dan is a Product Manager with Microsoft's Azure DevOps

 

 

## Read next

April 22, 2026

### Public Preview: Actual Result for Manual Tests in Azure Test Plans

Panagiotis Liaros

April 22, 2026

### Optimizing Git policy management at scale

Azat Galiev

 

## Stay informed

Get notified when new posts are published.

Email 
*

 

Country/Region 
*

Select...
United States
Afghanistan
Åland Islands
Albania
Algeria
American Samoa
Andorra
Angola
Anguilla
Antarctica
Antigua and Barbuda
Argentina
Armenia
Aruba
Australia
Austria
Azerbaijan
Bahamas
Bahrain
Bangladesh
Barbados
Belarus
Belgium
Belize
Benin
Bermuda
Bhutan
Bolivia
Bonaire
Bosnia and Herzegovina
Botswana
Bouvet Island
Brazil
British Indian Ocean Territory
British Virgin Islands
Brunei
Bulgaria
Burkina Faso
Burundi
Cabo Verde
Cambodia
Cameroon
Canada
Cayman Islands
Central African Republic
Chad
Chile
China
Christmas Island
Cocos (Keeling) Islands
Colombia
Comoros
Congo
Congo (DRC)
Cook Islands
Costa Rica
Côte dIvoire
Croatia
Curaçao
Cyprus
Czechia
Denmark
Djibouti
Dominica
Dominican Republic
Ecuador
Egypt
El Salvador
Equatorial Guinea
Eritrea
Estonia
Eswatini
Ethiopia
Falkland Islands
Faroe Islands
Fiji
Finland
France
French Guiana
French Polynesia
French Southern Territories
Gabon
Gambia
Georgia
Germany
Ghana
Gibraltar
Greece
Greenland
Grenada
Guadeloupe
Guam
Guatemala
Guernsey
Guinea
Guinea-Bissau
Guyana
Haiti
Heard Island and McDonald Islands
Honduras
Hong Kong SAR
Hungary
Iceland
India
Indonesia
Iraq
Ireland
Isle of Man
Israel
Italy
Jamaica
Jan Mayen
Japan
Jersey
Jordan
Kazakhstan
Kenya
Kiribati
Korea
Kosovo
Kuwait
Kyrgyzstan
Laos
Latvia
Lebanon
Lesotho
Liberia
Libya
Liechtenstein
Lithuania
Luxembourg
Macau SAR
Madagascar
Malawi
Malaysia
Maldives
Mali
Malta
Marshall Islands
Martinique
Mauritania
Mauritius
Mayotte
Mexico
Micronesia
Moldova
Monaco
Mongolia
Montenegro
Montserrat
Morocco
Mozambique
Myanmar
Namibia
Nauru
Nepal
Netherlands
New Caledonia
New Zealand
Nicaragua
Niger
Nigeria
Niue
Norfolk Island
North Macedonia
Northern Mariana Islands
Norway
Oman
Pakistan
Palau
Palestinian Authority
Panama
Papua New Guinea
Paraguay
Peru
Philippines
Pitcairn Islands
Poland
Portugal
Puerto Rico
Qatar
Réunion
Romania
Rwanda
Saba
Saint Barthélemy
Saint Kitts and Nevis
Saint Lucia
Saint Martin
Saint Pierre and Miquelon
Saint Vincent and the Grenadines
Samoa
San Marino
São Tomé and Príncipe
Saudi Arabia
Senegal
Serbia
Seychelles
Sierra Leone
Singapore
Sint Eustatius
Sint Maarten
Slovakia
Slovenia
Solomon Islands
Somalia
South Africa
South Georgia and South Sandwich Islands
South Sudan
Spain
Sri Lanka
St Helena
Ascension
Tristan da Cunha
Suriname
Svalbard
Sweden
Switzerland
Taiwan
Tajikistan
Tanzania
Thailand
Timor-Leste
Togo
Tokelau
Tonga
Trinidad and Tobago
Tunisia
Turkey
Turkmenistan
Turks and Caicos Islands
Tuvalu
U.S. Outlying Islands
U.S. Virgin Islands
Uganda
Ukraine
United Arab Emirates
United Kingdom
Uruguay
Uzbekistan
Vanuatu
Vatican City
Venezuela
Vietnam
Wallis and Futuna
Yemen
Zambia
Zimbabwe

I would like to receive the Azure DevOps Blog Newsletter. 
Privacy Statement.

Subscribe

 

Follow this blog

Are you sure you wish to delete this
 comment?

OK

Cancel