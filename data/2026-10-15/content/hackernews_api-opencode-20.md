---
title: OpenCode 2.0
url: https://anoma.ly/notes/opencode-2-0/
site_name: hackernews_api
content_file: hackernews_api-opencode-20
fetched_at: '2026-10-15T15:30:39.832543'
original_url: https://anoma.ly/notes/opencode-2-0/
author: gmays
date: '2026-10-14'
published_date: '2026-10-12'
description: OpenCode 2.0.
tags:
- hackernews
- trending
---

OpenCode2.0isamajoroverhaul.Itdrawsonmillionsofdailyusers'experiencetodeliverasystemthatcanflextoeverythinganagentneedstobe.Therearequitealotofnewfeatures,performanceimprovements,andbugfixesbutherearesomeofthemoreimpactfuluser-facingchanges.

## The Service

FromthebeginningOpenCodeadoptedaclient/servermodel.However,thiswasnotsomethingittookadvantageofbydefaultandwasmostlyusedbypowerusers.

In2.0thisservernowautomaticallyrunsasasinglebackgroundprocessonyourmachine.WhenyouopenupaTUI,thewebinterfaceorthedesktopappthey'realltalkingtothesamecentralprocess.

Terminal
Fix flaky test
Web
Fix flaky test
Desktop
Add dark mode
review.ts
Review changes
opencode
pid 
48213
Stopped
Starting
Running
Sessions
Fix flaky test
Add dark mode
Review changes

Ifyou'reusingtheprogrammaticclient@opencode/clienttomakeyourownscripts,theywillautodiscoverthelocalserviceandjustwork.Thisisparticularlyusefulforscheduledtasks.YoucanalsocallitviaCLIbyusingopencodeapicommands.

Youcanexposeittootherhostsandrun/pairoropencodepairtoconnectittootherapplications.Wehavenativeappsintheworksthattakeadvantageofthisflow.

## The API

TheoldAPIgrewhaphazardlyasweandtheworldcollectivelylearnedwhatagentsareandshouldbe.Itwasbad.

WestartedfromscratchandexaminedalltheweirdusecasesacrossthemillionsofuserswhouseOpenCodeeveryday.Itnowsupportsnearlyanythingyouneedtobeabletodo.

OpenCodeisalsoawareofitsownAPIandwillcallittodousefulthingslikemovingthecurrentsessionintoagitworktreewhenstartingnewwork.

Session
New session
YOU
Start
 
rate
 
limiting
 
uploads
 
in
 
a
 
new
 
worktree.
execute
{
 
code
 
}
›
opencode.
worktree_create
[name=rate-limit]
›
opencode.
session_rename
[title=Rate limit uploads]
›
opencode.
session_move
[directory=~/worktrees/rate-limit]
YOU
The
 
flaky
 
test
 
session
 
is
 
stuck.
 
Stop
 
it,
 
have
 
it
 
quarantine
 
the
 
test,
 
and
 
close
 
my
 
finished
 
tabs.
execute
{
 
code
 
}
›
opencode.
session_list
›
opencode.
session_context
[sessionID=ses_7c41e09a]
└ "Retrying uploads.test.ts again…"
execute
{
 
code
 
}
›
opencode.
session_interrupt
[sessionID=ses_7c41e09a]
›
opencode.
session_prompt
[sessionID=ses_7c41e09a, text=Quarantine uploads.test.ts]
›
opencode.
tab_close
[sessionID=ses_2f9d61b4]
Stopped
 
it,
 
told
 
it
 
to
 
quarantine
 
the
 
test,
 
closed
 
the
 
config
 
tab.
OpenCode
~/app
Fix flaky upload test
interrupted
Migrate config loader
tab closed
New session
this session
~/worktrees/rate-limit

We'vealsoshippedanewclientpackage@opencode/clientthatcontainsclientsforvanillaJavaScriptaswellasEffect.

review.ts
import
 { OpenCode } 
from
 
"@opencode/client"

import
 { Service } 
from
 
"@opencode/client/service"

const
 
endpoint
 
=
 
await
 Service.
ensure
()

const
 
client
 
=
 OpenCode.
make
({

 baseUrl: endpoint.url,

 headers: Service.
headers
(endpoint),

})

const
 
session
 
=
 
await
 client.session.
create
({

 location: { directory: process.
cwd
() },

})

await
 client.session.
prompt
({

 sessionID: session.id,

 text: 
"Review the current changes"
,

})

## Code Mode

ThemodelslovetowritecodeandOpenCode2.0takesadvantageofthatmorethananyothercodingagent.We'vebuiltaminimalJavaScriptinterpreterinthe@opencode/codemodepackage.

Session
YOU
File
 
GitHub
 
bugs
 
in
 
Linear.
execute
{
 
code
 
}
tools.github.list_issues
tools.linear.save_issue
execute
{
 
code
 
}
["OC-412", "OC-413", "OC-414"]
Code Mode
return
 [
search
({ query: 
"list github issues"
 }),
 
search
({ query: 
"create linear issue"
 })]
const
 { 
issues
 } 
=
 
await
 
tools.github.
list_issues
({
 owner: 
"anomalyco"
, repo: 
"opencode"
,
 labels: [
"bug"
], state: 
"OPEN"
,
})
const
 
filed
 
=
 
await
 
Promise
.
all
(issues.
map
(({ 
title
 }) 
=>
 
tools.linear.
save_issue
({ team: 
"OC"
, title })))
return
 filed.
map
(
issue
 
=>
 issue.identifier)
MCP servers
github
linear
sentry

ThispackageingestsMCPserversorOpenAPIendpoints,convertingthemintofunctionsthattheagentcancallinascript.ItcanrunthesescriptsnativelywithoutthecomplexityofNode.jsVMsorembeddingcomplicatedsolutionslikeQuickJS.

Thisletsyouragentwritescriptsthatcandothingslikecallatool,mapovertheresultsandcallanothertool.Singleroundtripinsteadofcallingthemoneatatime.

AllMCPserversin2.0areoptedintocodemodebydefault.Thismeansyoucanaddathousandofthemwithminimalcontextbloatandyouragentwilldiscoverandcomposethemtogetthingsdone.

## Background Tasks

Thelatestbatchofmodelsareincrediblygoodatorchestrationanditisimportantforharnessestoletthemexpressthefullextentofthatcapability.

Session
YOU
Spawn
 
a
 
background
 
fable
 
subagent
 
to
 
review
 
this
 
code.
subagent
review
 
this
 
code
fable
background
2 comments
$
shell
bun
 
test
background
148 passed
edit
src/retry.ts
+12
$
$
shell
bun
 
run
 
build
background
done
Press
 
ctrl
b
 
to move running work to the background
YOU
Update
 
the
 
changelog
 
too.
edit
CHANGELOG.md
+3
All
 
done.
 
The
 
review
 
left
 
2
 
comments,
 
148
 
tests
 
passed,
 
the
 
build
 
succeeded
 
and
 
the
 
changelog
 
is
 
updated.
Background
review this code
fable
$
bun test
$
bun run build
ctrl
b

First,we'veaddedbackgroundsubagents.Thisallowstheprimaryagenttokickoffsomeworktoanotheronewhileitcontinues.

Thishappensautomaticallybutyoucanalsotriggeritmanually-evenwithadifferentmodel.Itletsyoudothingslike“spawnabackgroundfablesubagenttoreviewthiscode”whileyoukeepprompting.

Second,we'veaddedbackgroundshellcommands.Theshelltoolcanbeinvokedasynchronouslysolong-runningworkdoesnothavetoblocktheprimaryagent.It'llbenotifiedwhenthingsarecomplete.

Ifanyforegroundshellcommandorsubagenttakeslongerthanyouexpect,youcanhitahotkeytomovethemtothebackgroundsoyoucankeepprompting.

## Plugins

AlthoughOpenCode1.0hadapluginsystem,itnevergottheattentionitneeded.Tocorrectthat,weforcedourselvestoimplementnearlyeveryOpenCode2.0featureasaninternalpluginandtherearenow80+ofthem.ThisguaranteesthatthePluginAPIstayswellmaintained.

We'vealsopromotedTUIpluginsfromexperimentaltostable.SinceitisallpoweredbyOpenTUI,youcanbuildnearlyanything.Hereisanexampleofsomethinguseless.

WealsospentquitealotoftimeensuringeverythinginOpenCode2.0canbehot-reloaded.Soitcanwriteapluginforitselfmid-sessionanduseitrightaway-wecoveredthedesignofthisinaprevious blogpost.

YoucanaskOpenCodetobuildwhateverpluginyouwantanditknowshowto.Butifyoudowanttoreadthedocs,theyareavailablehere.

## The SDK

OpenCodecanalsonowbeusedasalibrarywiththe@opencode/sdkpackage.ThisistheexactsamecodethatpowersourCLI.

ThismeansyoucanstripitdownandmakeyourownflavorofOpenCodethatrunsonaserverorinspecializedenvironmentslikeDurableObjects.AndthenyoucanconnecttoitfromanyOpenCodeclientsinceitspeaksthestandardOpenCodeserverprotocol.

ItalsohasanoptionalEffect-basedAPI.

Thisoneisstillindevelopmentasthingsareshiftingbutyoucanalready use it.

## Upgrading

ToupgradetheCLI,makesureyou'reonthelatest1.xrelease,thenrunopencodeupgrade--major.

Toupgradeyourdesktopapp,downloadthelatesthere.

Therearesomebreakingchanges.

1.0pluginswillnotworkin2.0

ServerAPIiscompletelydifferent

tui.jsonconfigismovedtojson

Therearealotofotherchangesbuttheyarebackwardscompatible.ItisworthpointingOpenCodeatthis docsoitcanmigratethingsforyou.