---
title: GPT-6 Astra Solves a WWI German Radio Cipher - prinz
url: https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio
site_name: hackernews_api
content_file: hackernews_api-gpt-6-astra-solves-a-wwi-german-radio-cipher-prinz
fetched_at: '2026-09-19T21:18:00.103104'
original_url: https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio
author: prinz
date: '2026-09-19'
description: Scienceblogs.de, a German science blogging portal, includes a relatively famous list of 50 unsolved ciphers, which range from cryptograms published by serial killers to the famous Voynich manuscript.
tags:
- hackernews
- trending
---

# GPT-6 Astra Solves a WWI German Radio Cipher

prinz
Sep 17, 2026
23
1
5
Share

Scienceblogs.de, a German science blogging portal, includes a relatively famouslist of 50 unsolved ciphers, which range fromcryptograms published by serial killersto the famousVoynich manuscript.

Among these ciphers isa set of German radio messages from World War Ithat were encoded using the ADFGVX method.

This method is illustrated by the following example using the word “HOUSE” as the key:

    A D F G V X
A   H O U S E A
D   B C D F G I
F   J K L M N P
G   Q R T V W X
V   Y Z 0 1 2 3
X   4 5 6 7 8 9

As you can see, ADFGVX is used both horizontally and vertically to give each “cell” in the table a value. For example, in this text, “AA” corresponds to the letter H, “AD” corresponds to the letter O, “DA” corresponds to the letter B, and so on. And so, the word “PRINZ” would be encoded as:

FX GD DX FV VD

Using an encryption word other than “HOUSE” would result in a completely different table.

There isa list of known keysused by the Germans to encrypt these radio.messages, and hundreds of these messageshave already been decoded, including by codebreaking expert George Lasry. Still, over a dozen have thus far eluded efforts to solve them, including (to my knowledge) this one, originally transmitted on November 27, 1918 (pg. 217):

GPT-6 Astra solved this cipher, and believes that the original message was as follows:

EIN ENGLISCHER KREUZER EINLIEG X SEWASTOPOL X S4STEN X EIN GESCHWADER DER X ALLIIERTEN FOLGT 26STEN X

Or, in English:

AN ENGLISH CRUISER ARRIVED AT SEVASTOPOL ON THE ?4TH AN ALLIED SQUADRON FOLLOWS ON THE 26TH

The model used “TRUPPENVERSCHIEBUNG” as the encryption word, as described on pgs. 214-215 of J. Rives Childs's “The History and Principles of German Military Ciphers, 1914–1918”. This encryption word yields the following table:

Before even using this table, the word “TRUPPENVERSCHIEBUNG” is required to be rearranged, so that the letters in the word are in an alphabetical order (e.g., T is 16th and R is 13th).

Then, the same “TRUPPENVERSCHIEBUNG” is written out horizontally, with letters from the encrypted message written under it, in rows of 19 (resulting in 8 rows of 19 symbols each, plus 1 row of 18 symbols, since there are 170 characters total). This also means that we have 18 columns with 9 symbols each and 1 column with 8 symbols (column “G”). From here, because T is the 16th column, it has 14 9-symbol columns before it, plus 1 8-symbol G column; 9×14 + 1×8 = 134, so “T” will correspond to the following, 135th, symbols in the message, which is “A”. Similarly, the next letter, “R”, corresponds to the letter “V” (because R is the 13th letter alphabetically and thus has 11×9 + 1×8 = 107 symbols before it; the 108th symbol in the message is “V”).

In the table above, “AV” corresponds to “E”, the first letter in “EIN”. We repeat this process until we decode the entire message.

(Wow.)

Astra's hypothesis for why this particular message was previously unsolved is that “TRUPPENVERSCHIEBUNG” was used as the key starting on December 9, 1918 - whereas, as noted above, this message was transmitted earlier, on November 27, 1918. The reason for this discrepancy is unknown.

Astra felt compelled to check its work and found that, in fact, the English cruiser HMS Canterbury arrived in Sevastopol on November 24, 1918, based onits original logs:

… and an allied squadron did follow on November 26 (see right below line 11, which says that an allied squadron arrived):

Iam not aware of this particular message having ever been decoded before, so sharing it here as a minor (but I think really cool) result and illustration of the capabilities of this model.

23
1
5
Share