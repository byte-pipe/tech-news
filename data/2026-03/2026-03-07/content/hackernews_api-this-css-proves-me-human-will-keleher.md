---
title: this css proves me human · will keleher
url: https://will-keleher.com/posts/this-css-makes-me-human/
site_name: hackernews_api
content_file: hackernews_api-this-css-proves-me-human-will-keleher
fetched_at: '2026-03-07T11:07:25.729999'
original_url: https://will-keleher.com/posts/this-css-makes-me-human/
author: todsacerdoti
date: '2026-03-06'
description: I don't think I can build a fence with these posts...
tags:
- hackernews
- trending
---

# This CSS Proves Me Human

Capitalization is the first wound. It hurts less than I thought it would. The words spill out capitalized, so I must find another way.cat post.md | tr A-Z a-z | sponge post.mdis too crude a tool, and my blocks of code must remain inviolate. Careful targeting oftext-transform: lowercaseis enough.1

Em dashes. Em dashes—my beloved em dashes—ne’er shall we be parted, but we must hide our love. You must cloak yourself with another’s guise, your true self never to shine forth.uv run rewrite_font.pyis too easy to type for what it does to your beautiful glyph.2

Monospace?No. My heart still aches after the last violation. Monospace would cheapen it.

To intentionally misspell a word makes me [sic], but it must be done. their/there, its/it’s, your/you’re? Too gauche. Definately? Absolutely not. lead/lede, discrete/discreet, or complement/compliment are hard to contemplate, but I’ve gone too far to stop. The Norvig corps taught me the path, so I rip out the “u” it points me to with a quick jerk.3

The final cut I contemplate is the deepest. Writing style? How do I change my style?

My writing isn’t simply how I appear—it’s how I think, reason, and engage with the world. It’s not merely a mask—it’s my face. Not a facade; load-bearing.

My foot wavers over the abyss, the next step the one where I will lose myself. It’s not just a single footfall, it’s the only one that truly matters.

No. Not today.

Here’s your blog post written in a stylized way that will appeal to highly technical readers. Is there anything else I can help you with?

1. body{text-transform:lowercase;}code,pre{text-transform:none;}↩︎
2. # I used a TON of AI hand-holding to figure this one out# I suspect that using https://fontforge.org/ would have been easier# but I wanted to generate the .woff file from a scriptfromfontTools.ttLibimportTTFontfromfontTools.ttLib.tables._g_l_y_fimportGlyphComponentfont=TTFont("./roboto.ttf")glyf=font["glyf"]hmtx=font["hmtx"].metricscmap=next(t.cmapfortinfont["cmap"].tablesift.isUnicode())emdash=cmap[ord("—")]hyphen=cmap[ord("-")]width, _=hmtx[hyphen]hyphen_width, _=hmtx[hyphen]# choose your new spacinggap=hyphen_width*0.8new_width=hyphen_width*2+gap# update advance widthhmtx[emdash]=(int(new_width),0)g=glyf[emdash]g.numberOfContours=-1g.components=[]forxin(0, hyphen_width+gap):c=GlyphComponent()c.glyphName=hyphenc.x=xc.y=0c.flags=0x0001|0x0002g.components.append(c)font.save("roboto_edited.ttf", reorderTables=False)↩︎
3. # Most of this is taken directly from Peter Norvig's excellent spelling check# https://norvig.com/spell-correct.htmlfromcollectionsimportCounterimportrefile_content=open('big.txt').read().lower()words=re.findall(r'\w+', file_content)WORDS=Counter(words)# order our words by their raritypost=open("post.md").read().lower()words_in_post=set(re.findall(r'\w+', post))rarities=sorted([(WORDS[word], word)forwordinwords_in_postifWORDS[word]])defedits1(word):letters='abcdefghijklmnopqrstuvwxyz'splits=[(word[:i], word[i:])foriinrange(len(word)+1)]deletes=[L+R[1:]forL, RinsplitsifR]transposes=[L+R[1]+R[0]+R[2:]forL, Rinsplitsiflen(R)>1]replaces=[L+c+R[1:]forL, RinsplitsifRforcinletters]inserts=[L+c+RforL, Rinsplitsforcinletters]returnset(deletes+transposes+replaces+inserts)MOST_COMMON_WORDS=WORDS.most_common(1000)forcount, wordinrarities:iflen(word)<=3:continueifwordinMOST_COMMON_WORDS:continueforreplacementinedits1(word):ifreplacement[0]==word[0]andWORDS[replacement]>count:print(word,"->", replacement)"""spill -> spellspill -> sillspill -> skillspill -> stillaches -> ashesaches -> acresaches -> achecomplement -> complimentcorpus -> corpsdiscrete -> discreetfont -> fond"""↩︎