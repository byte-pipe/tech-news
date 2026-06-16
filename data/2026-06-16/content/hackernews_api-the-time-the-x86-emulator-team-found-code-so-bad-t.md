---
title: The time the x86 emulator team found code so bad that they fixed it during emulation - The Old New Thing
url: https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419
site_name: hackernews_api
content_file: hackernews_api-the-time-the-x86-emulator-team-found-code-so-bad-t
fetched_at: '2026-06-16T12:37:11.820858'
original_url: https://devblogs.microsoft.com/oldnewthing/20260615-00/?p=112419
author: Raymond Chen
date: '2026-06-16'
published_date: '2026-06-15T14:00:00+00:00'
description: Offensive content in the eyes of a software engineer.
tags:
- hackernews
- trending
---

Raymond Chen

During an exchange of war stories, a colleague of mine told one from back in the days when Windows included a processor emulator for x86-32 on systems that natively ran some other processor. (This has happened many times. And no, I don’t know which processor this particular story applied to.)

This particular emulator employed binary translation, generating native code to perform the equivalent operations of the original x86-32 code. This offered a significant performance improvement over emulation via interpreter. You can imagine that x86-32 is just a bytecode, and the emulator is a JIT compiler.

Anyway, my colleague found that there was one program that needed to allocate around 64KB of memory on the stack and initialize it. The standard way of doing this is toperform a stack probe to ensure that 64KB of memory is available, then subtracting 65536 from the stack pointer, and then initializing the memory in a small, tight loop.

But using a loop to initialize the memory was too mundane for whatever compiler was used to compile this code. Instead of generating a loop to initialize each byte of the buffer, the compiler “optimized” the code by unrolling the loop into 65,536 individual “write byte to memory” instructions, each 4 bytes long.

All in all, it took this program 256 kilobytes of code to initialize 64 kilobytes of data.

This offended the team so much that they added special code to the translator to detect this horrible function and replace it with the equivalent tight loop.

### Category

* Old New Thing

### Topics

* History

### Share

 

## Author

Raymond Chen

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.

 

 

## Read next

June 9, 2026

### The Microsoft Company Party where everybody played name tag swap

Raymond Chen

June 1, 2026

### The placeholder name for the Windows 8 experience was “modern”

Raymond Chen

 

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

I would like to receive the The Old New Thing Newsletter. 
Privacy Statement.

Subscribe

 

Follow this blog

Are you sure you wish to delete this
 comment?

OK

Cancel