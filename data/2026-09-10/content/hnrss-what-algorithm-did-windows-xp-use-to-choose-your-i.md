---
title: What algorithm did Windows XP use to choose your initial user picture? - The Old New Thing
url: https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683
site_name: hnrss
content_file: hnrss-what-algorithm-did-windows-xp-use-to-choose-your-i
fetched_at: '2026-09-10T14:50:07.347744'
original_url: https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683
author: Raymond Chen
date: '2026-09-10'
published_date: '2026-09-09T14:00:00+00:00'
description: It's random, really.
tags:
- hackernews
- hnrss
---

Raymond Chen

I noted some time ago thatWindows XP chose your initial picture at randomfrom among the pictures in the%ALLUSERSPROFILE%\Application Data\Microsoft\User Account Pictures\Default Picturesdirectory. But it seems people want to know more.

Has anyone attempted to figure out the RNG for how Windows XP determines what profile picture is used on first account creation?

— Xeno (@XenoPanther)December 11, 2025

The random number generator is our friendRtlRandomEx, using the current value ofGetTickCount()as the initial seed.

The function uses a one-pass random selection algorithm. I can immediately think of two benefits of this decision. First, compared to the naïve two-pass algorithm of counting up all the items, then randomly picking a number from 1 ton, and then iterating a second time to find the item at that index, it’s more efficient because it reduces the amount of calls into the file system, which is where the bottleneck is. Furthermore, the one-pass algorithm avoids complications if the number of files in the directory changes while the code is running.

The one-pass algorithm is a special case ofreservoir sampling, wherekis 1. This special case permits a tailored algorithm that is much simpler.

selectRandomFromIterator(iterator)
{
 var count = 0;
 var winner = null;

 while (iterator.moveNext()) {
 ++count;
 if (uniform_random(min: 1, max: count) == count) {
 winner = iterator.current();
 }
 }

 return winner;
}

The way this algorithm works is by observing that in a collection ofnitems, the last item has a 1/nchance of being randomly selected. If it isn’t selected, then you need to select randomly from the firstn− 1 items, which you can solve recursively.

Playing the recursion forward, you start with the base case which is that if you have a list of 1 item, then your only choice is to chose that item. Otherwise, if you have a list ofnitems, first choose an item randomly from the firstn− 1, and then switch to thenth item with a 1/nprobability.

As a final safety check, the code stops after sampling 100 pictures. This avoids pathological behavior if somebody puts a million files in theDefault Picturesdirectory.

### Category

* Old New Thing

### Topics

* History

### Share

 

## Author

Raymond Chen

Raymond has been involved in the evolution of Windows for more than 30 years. In 2003, he began a Web site known as The Old New Thing which has grown in popularity far beyond his wildest imagination, a development which still gives him the heebie-jeebies. The Web site spawned a book, coincidentally also titled The Old New Thing (Addison Wesley 2007). He occasionally appears on the Windows Dev Docs Twitter account to tell stories which convey no useful information.

 

 

## Read next

September 8, 2026

### A sample use of thewinstart.batfile in Windows 95

Raymond Chen

August 25, 2026

### Why didn’t the Windows Entertainment Pack just run the MS-DOS version inside an emulator?

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