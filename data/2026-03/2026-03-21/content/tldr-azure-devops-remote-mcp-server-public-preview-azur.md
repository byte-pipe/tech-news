---
title: Azure DevOps Remote MCP Server (public preview) - Azure DevOps Blog
url: https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview/
site_name: tldr
content_file: tldr-azure-devops-remote-mcp-server-public-preview-azur
fetched_at: '2026-03-21T19:10:30.024120'
original_url: https://devblogs.microsoft.com/devops/azure-devops-remote-mcp-server-public-preview/
author: Dan Hellem
date: '2026-03-21'
published_date: '2026-03-17T13:52:29+00:00'
description: Get started with the Azure DevOps Remote MCP Server public preview to connect Azure DevOps data to client tools and agent builders.
tags:
- tldr
---

Dan Hellem

Product Manager for Azure Boards, Repos & Wiki
 

When we released thelocal Azure DevOps MCP Server, it gave customers a way to connect Azure DevOps data with tools like Visual Studio and Visual Studio Code through GitHub Copilot Chat. The next step was to make this experience easier to get started with and to enable it for services that support only remote MCP servers.

The Remote MCP Server is a hosted version of the Azure DevOps MCP Server that uses streamable HTTP transport. It supports the same core scenarios as the local server but removes the need for additional setup and installation.

TheRemote Azure DevOps MCP Serverpreview is available now. We are excited to see how teams use it and will continue investing in the experience as we expand support and improve the MCP Server tools.

# 👟 Getting Started

Getting started in simple. Depending on the tools that you are using, you only need to add the following server information to yourmcp.json.

{
 "servers": {
 "ado-remote-mcp": {
 "url": "https://mcp.dev.azure.com/{organization}",
 "type": "http"
 }
 },
 "inputs": []
}

There are additional configuration options available, and you can read more in ourofficial documentation.

Your browser does not support the video tag.

## ⚙️ Supported Clients and Services

The Remote MCP Server is hosted on the Azure DevOps service and uses Microsoft Entra for authentication. As a result, it follows the authentication rules and constraints that come with Entra. This also means your Azure DevOps organization must be backed by Entra. Standalone organizations, sometimes referred to as MSAs, are not supported by the Remote MCP Server.

The following clients are supported today with no additional onboarding required:

* Visual Studio with GitHub Copilot
* Visual Studio Code with GitHub Copilot

## ⌛ Coming Soon

Additional client tools such as GitHub Copilot CLI, Claude Desktop, Claude Code, and ChatGPT require dynamic registration of an OAuth Client ID in Entra before they can be used with the MCP server. We are working closely with the Entra team to enable this capability. For now, only Visual Studio and Visual Studio Code are supported.

Support for other services, including Azure AI Foundry, Microsoft 365 Copilot, and Copilot Studio, is not yet available. We will share a separate blog post when these services become available with the Azure DevOps MCP Server.

## 📌 Local MCP Server

You can continue using thelocal MCP Serverfor the time being. However, we plan to eventually archive that repository and focus our investments on the Remote MCP Server. We do not have a specific archive date yet, but it will align with the Remote MCP Server reaching general availability.

Now is a great time to try the Remote MCP Server and begin moving your workloads over to it instead of relying on the local MCP Server.

## 🆘 Support

During the public preview, you can submit any issues or questions through thelocal Azure DevOps MCP Server repository. This allows our team to quickly review and respond to any problems or feedback you may have.

Category
Azure & Cloud
Topics
#DevOps
Azure DevOps
Community
MCP Server

Share

 

## Author

Dan Hellem
Product Manager for Azure Boards, Repos & Wiki

Dan is a Product Manager with Microsoft's Azure DevOps

 

 

## Read next

March 18, 2026

### Authentication Tokens Are Not a Data Contract

Angel Wong

March 19, 2026

### Remote MCP Server preview in Microsoft Foundry

Dan Hellem

 

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