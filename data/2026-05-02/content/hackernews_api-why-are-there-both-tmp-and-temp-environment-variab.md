---
title: Why are there both TMP and TEMP environment variables, and which one is right? - The Old New Thing
url: https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213
site_name: hackernews_api
content_file: hackernews_api-why-are-there-both-tmp-and-temp-environment-variab
fetched_at: '2026-05-02T19:55:14.777447'
original_url: https://devblogs.microsoft.com/oldnewthing/20150417-00/?p=44213
author: Raymond Chen
date: '2026-05-02'
published_date: '2015-04-17T21:00:00+00:00'
description: Why are there both TMP and TEMP environment variables? (2015)
tags:
- hackernews
- trending
---

Raymond Chen

If you snoop around your environment variables, you may notice that there are two variables that propose to specify the location of temporary files. There is one calledTMPand another calledTEMP. Why two? And if they disagree, then who’s right?

Rewind to 1973. The operating system common on microcomputers was CP/M. The CP/M operating system had no environment variables. That sounds like a strange place to start a discussion of environment variables, but it’s actually important. Since it had no environment variables, there was consequently neither aTMPnor aTEMPenvironment variable. If you wanted to configure a program to specify where to put its temporary files, you needed to do some sort of program-specific configuration, like patching a byte in the executable to indicate the drive letter where temporary files should be stored.

(My recollection is that most CP/M programs were configured via patching. At least that’s how I configured them. I remember my WordStar manual coming with details about which bytes to patch to do what. There was also a few dozen bytes of patch space set aside for you to write your own subroutines, in case you needed to add custom support for your printer. I did this to add an “Is printer ready to accept another character?” function, which allowed for smoother background printing.)

Move forward to 1981. The 8086 processor and the MS-DOS operating system arrived on the scene. The design ofboth the 8086 processorandthe MS-DOS operating systemwere strongly inspired by CP/M, so much so thatit was the primary design goal that it be possible to take your CP/M program written for the 8080 processor and machine-translate it into an MS-DOS program written for the 8086 processor. Mind you, the translator assumed that you didn’t play any sneaky tricks like self-modifying code, jumping into the middle of an instruction, or using code as data, but if you played honest, the translator would convert your program.

(The goal of allowing machine-translation of code written for the 8080 processor into code written for the 8086 processor helps to explain some of the quirks of the 8086 instruction set. For example, the H and L registers on the 8080 map to the BH and BL registers on the 8086, and on the 8080, the only register that you could use to access a computed address was HL. This is why of the four basic registers AX, BX, CX, and DX on the 8086, the only one that you can use to access memory is BX.)

One of the things that MS-DOS added beyond compatibility with CP/M was environment variables. Since no existing CP/M programs used environment variables, none of the first batch of programs for MS-DOS used them either, since the first programs for MS-DOS were all ported from CP/M. Sure, you could set aTEMPorTMPenvironment variable, but nobody would pay attention to it.

Over time, programs were written with MS-DOS as their primary target, and they started to realize that they could use environment variables as a way to store configuration data. In the ensuing chaos of the marketplace, two environment variables emerged as the front-runners for specifying where temporary files should go:TEMPandTMP.

MS-DOS 2.0 introduced the ability to pipe the output of one program as the input of another. Since MS-DOS was a single-tasking operating system, this was simulated by redirecting the first program’s output to a temporary file and running it to completion, then running the second program with its input redirected from that temporary file. Now all of a sudden, MS-DOS needed a location to create temporary files! For whatever reason, the authors of MS-DOS chose to use theTEMPvariable to control where these temporary files were created.

Mind you, the fact thatCOMMAND.COMchose to go withTEMPdidn’t affect the fact that other programs could use eitherTEMPorTMP, depending on the mood of their original author. Many programs tried to appease both sides of the conflict by checking for both, and it was up to the mood of the original author which one it checked first. For example, the oldDISKCOPYandEDITprograms would look forTEMPbefore looking forTMP.

Windows went through a similar exercise, but for whatever reason, the original authors of theGet­Temp­File­Namefunction chose to look forTMPbefore looking forTEMP.

The result of all this is that the directory used for temporary files by any particular program is at the discretion of that program, Windows programs are likely to use theGet­Temp­File­Namefunction to create their temporary files, in which case they will prefer to useTMP.

When you go to the Environment Variables configuration dialog, you’ll still see both variables there,TMPandTEMP, still duking it out for your attention. It’s like Adidas versus Puma, geek version.

### Category

* Old New Thing

### Topics

* History

### Share

 

## Author

Raymond Chen

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.

 

 

## Read next

April 21, 2015

### What was the starting point for the Panther Win32 kernel?

Raymond Chen

April 23, 2015

### How did the scopes for the CryptProtectMemory function end up in a strange order?

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