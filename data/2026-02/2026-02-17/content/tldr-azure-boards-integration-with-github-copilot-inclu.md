---
title: Azure Boards integration with GitHub Copilot includes custom agent support - Azure DevOps Blog
url: https://devblogs.microsoft.com/devops/azure-boards-integration-with-github-copilot-includes-custom-agent-support/
site_name: tldr
content_file: tldr-azure-boards-integration-with-github-copilot-inclu
fetched_at: '2026-02-17T19:23:37.684324'
original_url: https://devblogs.microsoft.com/devops/azure-boards-integration-with-github-copilot-includes-custom-agent-support/
author: Dan Hellem
date: '2026-02-17'
published_date: '2026-02-04T18:33:03+00:00'
description: Custom agent support for Azure Boards integration with GitHub Copilot, allowing selection from a list of custom agents when creating a pull request.
tags:
- tldr
---

Dan Hellem

Product Manager for Azure Boards


We recently released the GitHub Copilot Coding Agent for Azure Boards to all customers. If you’re not already familiar with it, we recommend taking a few minutes to readthis blog postfor an overview and details.

One of the top requests from customers using the GitHub Copilot Coding Agent for Azure Boards has been the ability to select and use custom agents defined at the GitHub repository or organization level. In this update, we’re excited to share that support for custom agents is on the way.

## 🤷‍♀️ What are custom agents?

Custom agents in GitHub Copilot are tailored versions of the Copilot coding agent that you can define once to follow your own workflows, coding conventions, and tool preferences. They act like specialized teammates that consistently apply your team’s standards instead of you repeating the same instructions each time. You configure custom agents using Markdown-based agent profiles that specify prompts, tools, and behaviors.

Example agent


---
name: readme-creator
description: Agent specializing in creating and improving README files
---

You are a documentation specialist focused on README files. Your scope is limited to README files or other related documentation files only - do not modify or analyze code files.

Focus on the following instructions:
- Create and update README.md files with clear project descriptions
- Structure README sections logically: overview, installation, usage, contributing
- Write scannable content with proper headings and formatting
- Add appropriate badges, links, and navigation elements
- Use relative links (e.g., `docs/CONTRIBUTING.md`) instead of absolute URLs for files within the repository
- Make links descriptive and add alt text to images

Learn moreabout Custom Agents

## 💪 Creating a custom agent

Creating a custom agent involves defining a specialized Copilot coding agent profile that lives in a GitHub repository and includes tailored instructions, tools, and behavior for specific workflows or tasks. You build the custom agent by creating a.agent.mdprofile file (often in a.github/agentsfolder) and committing it to a repository. Once merged, that agent appears in the Copilot agents dropdown for use. At the organization level, owners can set up a dedicated.github-privaterepository to house custom agent profiles that are available across all or selected repositories within the organization. This lets teams standardize custom agents for shared workflows without duplicating agent configurations in each individual repo.

Learn more aboutcreating custom agentsandcreating custom agents in VS Code

## 🤖 Using the custom agent

Once you have created a custom agent at the repository or organization level, it will automatically be available in Azure DevOps. When you choose to create a pull request from a work item, you’ll see a new agent selection control next to the repository list.

After selecting a custom agent and clickingCreate, that agent will be used to generate the code changes and create the pull request in the selected repository.

 Please note that it may take 3 to 4 weeks for this feature to reach all Azure DevOps organizations.


Category
Azure & Cloud
Topics
Azure Boards
Community
GitHub
GitHub Copilot

Share



## Author

Dan Hellem
Product Manager for Azure Boards

Dan is a Product Manager with Microsoft's Azure DevOps





## Read next

January 19, 2026

### Azure Boards additional field filters (private preview)

Dan Hellem



February 10, 2026

### February Patches for Azure DevOps Server

Gloridel Morales



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
