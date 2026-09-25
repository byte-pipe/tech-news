---
title: ambionix - Boards of Casio
url: https://www.ambionix.com/blog/boards-of-casio/
site_name: hnrss
content_file: hnrss-ambionix-boards-of-casio
fetched_at: '2026-09-25T21:59:57.857439'
original_url: https://www.ambionix.com/blog/boards-of-casio/
date: '2026-09-25'
tags:
- hackernews
- hnrss
---

Blog
About

English

Español

Français

简体中文

日本語

한국어

24th September 2026

# Boards of Casio

While working away on theCZP-1, which was at least initially an effort to create a CasioCZ-101on a web page I happened to see this YouTube video by oliveoil22:

The immediate question was “How can I make those sounds in the CZP-1?”. Luckily for me oliveoil22 had also shared their CZ-101 patch data . . .

### Boards of Casio patch data

1. Download the patch datahere.
2. Open theCZP-1and turn it on by pressing Power. (Make sure your device is not in silent mode!)
3. In the “Library” panel under “Banks” select an empty slot from drop down menu.
4. Select the(“Load bank from JSON file”) button and choose the file you downloaded, probably in your Downloads directory.
5. Now the bank program data has been replaced by the loaded Boards of Casio patches, so under “Programs” you can select one of the loaded sounds.
6. Touch the on screen keyboard, or play notes with your computer keyboard, or if you are adventurous use the MIDI facilities to connect an external keyboard.

Note the CZP-1 doesn’t include the post processing effects oliveoil22 has in their patches, and that accounts for most of the differences, but it is otherwise very close.

The CZP-1 saves the banks you have loaded in different slots in your browser so as long as you don’t use private browsing you will find it remembers them between sessions. This also operates across tabs, so all CZP-1 tabs will see the same bank data loaded, but you can select different banks and programs in different tabs.

If you want to empty a bank you unload it with the(“Remove bank”) button.

### Sharing sounds with urls

The CZP-1 doesn’t just support sharing sounds by loading and saving json files, you can also just share urls.

For examplehereis another sound.

To make these urls you just make the sound you want and in the Library under Programs hit“Share” which copies the url to your device clipboard.

The url encodes the data in itself. There is no sound data stored on the server, and you can freely send urls between devices.

Check out more in thethe introductory blog postor the full CZP-1Manual.

### Hang on, what? Again?

The twist here was how this was done. I downloaded the patch data from the Google Drive oliveoil22 links to on the YouTube video page, guessed it was probably system exclusive MIDI data from the “syx” extension, told the Claude that had done the last pass of the CZP-1 audio engine and five minutes later I had the json file of the bank containing the patch data for loading into the CZP-1.

If you tried to do this kind of thing in the before times this is mind bending stuff.

Finally. thank you to oliveoil22 who deserves the credit of anything good about that patch data. I assume you’re cool with this, if not let me know.