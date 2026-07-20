---
title: Minecraft 26.3 Snapshot 4 | Minecraft
url: https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4
site_name: hackernews_api
content_file: hackernews_api-minecraft-263-snapshot-4-minecraft
fetched_at: '2026-07-20T11:58:03.697600'
original_url: https://www.minecraft.net/en-us/article/minecraft-26-3-snapshot-4
author: ObviouslyFlamer
date: '2026-07-19'
published_date: '2026-07-16T14:30:00Z'
description: Minecraft 26.3 Snapshot 4
tags:
- hackernews
- trending
---

News

Written By

Java Team

Published

7/16/26

# Minecraft 26.3 Snapshot 4

A Minecraft Java Snapshot

Happy Snapshot Tues... Thursday? Yes, you read that right! As we've entered peak vacation season here in Sweden, snapshots might not come out on their usual schedule.

In today's snapshot we have switched the library used for window management, input and platform integration from GLFW to SDL3.

We have also added new item components for custom furnace fuels, as well as several technical changes for signs, world generation and loot tables.

Happy mining!

## Known Issues

* Exclusive fullscreen mode on Windows may cause the game to crash in certain situations, especially when using multiple monitors
* Entering Exclusive fullscreen mode crashes the game on Wayland

## New Features

* Players in spectator mode can now interact with portals to teleport

## Changes

### Minor Tweaks to Blocks, Items and Entities

* Armadillos no longer try to roll up when submerged in liquids

### UI

* Removed the Raw Input mouse settingMouse input now always uses relative mouse mode while playing in-game
* Mouse input now always uses relative mouse mode while playing in-game
* Key bindings now use physical keys instead of keyboard-layout-specific key codes
* Borderless Fullscreen is now the default fullscreen mode
* Switching between Borderless and Exclusive Fullscreen no longer requires restarting the game
* Exclusive fullscreen mode on macOS is no longer supported
* The minimum window size is now 320 by 240 pixels
* On macOS, holding a key while entering text now displays the native accent and candidate popup
* On Linux systems, the game will now use and prefer Wayland natively if available

#### Debug Overlay

* The debug overlay now supports a separate GUI scale than the rest of the gameThis is customizable through the Debug Options screen,F3 + F6The default scale is "Auto", which tries to stay at a higher resolution than normalAnother option is "Unchanged", which matches your regular GUI scaleThe rest of the options work the same as in the normal "GUI Scale", controlling the scale directly
* This is customizable through the Debug Options screen,F3 + F6
* The default scale is "Auto", which tries to stay at a higher resolution than normal
* Another option is "Unchanged", which matches your regular GUI scale
* The rest of the options work the same as in the normal "GUI Scale", controlling the scale directly
* Added a "player_speed" debug entry that displays the speed of the player in blocks per tick.
* The debug overlay now shows the display refresh rate

### Creative Inventory

* Reordered mineral item and block ordering to have non-tiered ingredients up first, then tiered ingredients that craft into equipment lastIngredientsNon-tiered mineralsUnrefined tiered mineralsRefined tiered mineralsNuggetsIngotsBuilding BlocksNon-tiered mineral blocks and variantsRefined tiered mineral blocks and variantsCopper block familyCopper Blocks continue to be pushed to the end of the order in Building Blocks since they have a large list of content
* IngredientsNon-tiered mineralsUnrefined tiered mineralsRefined tiered mineralsNuggetsIngots
* Non-tiered minerals
* Unrefined tiered minerals
* Refined tiered mineralsNuggetsIngots
* Nuggets
* Ingots
* Building BlocksNon-tiered mineral blocks and variantsRefined tiered mineral blocks and variantsCopper block family
* Non-tiered mineral blocks and variants
* Refined tiered mineral blocks and variants
* Copper block family
* Copper Blocks continue to be pushed to the end of the order in Building Blocks since they have a large list of content
* Improved ordering of Natural Blocks tab so that all inner ordering of group content sequentially progresses from Overworld -> Nether -> End to stay consistent with other tabs

## Technical Changes

* The Data Pack version is now 111.0
* The Resource Pack version is now 92.0
* Loot table types that have a dedicated registry now support registry element and tag referencesThis means that the majority of fields of such types that previously accepted single elements will now accept either a namespaced ID or an inline value, while fields that previously accepted lists can now accept an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag IDAffected types:minecraft:advancementminecraft:item_modifierminecraft:loot_tableminecraft:number_providerminecraft:predicateminecraft:recipeminecraft:slot_sourceExistingreferencetypes for predicates, item modifiers and slot sources are now obsolete and have been removed
* This means that the majority of fields of such types that previously accepted single elements will now accept either a namespaced ID or an inline value, while fields that previously accepted lists can now accept an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID
* Affected types:minecraft:advancementminecraft:item_modifierminecraft:loot_tableminecraft:number_providerminecraft:predicateminecraft:recipeminecraft:slot_source
* minecraft:advancement
* minecraft:item_modifier
* minecraft:loot_table
* minecraft:number_provider
* minecraft:predicate
* minecraft:recipe
* minecraft:slot_source
* Existingreferencetypes for predicates, item modifiers and slot sources are now obsolete and have been removed

### Windowing and Input Backend

* Minecraft now uses SDL3 instead of GLFW for window management, input and platform integration
* Keyboard input now uses SDL scancodes for physical key positions and SDL keycodes for layout-dependent text editing shortcuts

## Data Pack Version 111.0

* Signs no longer automatically execute click events in custom text

### Commands

#### Changes tospreadplayers

* Whether a block is safe to spread a player to is now controlled by the#entities_can_teleport_toblock tag

### Environment Attributes

#### Addedminecraft:gameplay/natural_mob_spawns

* Defines mob spawns in an Environment Attribute Source
* During worldgen placement, only Dimensions and Biomes will apply this Environment Attribute
* Format: object with fields:spawns_by_category- map of spawn category to weighted list of spawn dataSpawn data format: object with fields:type- entity type, the entity to spawncount- int provider, amount to spawnspawn_costs- map of entity type to object with fields:energy_budget- float, energy change allowed per spawncharge- float, how much existing mobs will attract or repulse other charged mobs
* spawns_by_category- map of spawn category to weighted list of spawn dataSpawn data format: object with fields:type- entity type, the entity to spawncount- int provider, amount to spawn
* Spawn data format: object with fields:type- entity type, the entity to spawncount- int provider, amount to spawn
* type- entity type, the entity to spawn
* count- int provider, amount to spawn
* spawn_costs- map of entity type to object with fields:energy_budget- float, energy change allowed per spawncharge- float, how much existing mobs will attract or repulse other charged mobs
* energy_budget- float, energy change allowed per spawn
* charge- float, how much existing mobs will attract or repulse other charged mobs
* Available attribute modifiers:overlayFor each mob category, overrides the lower layer's spawn settings with the higher layer's, unless the category is not includedMerges each layer's spawn costs together, overriding the lower layer's spawn costs with the higher layer's if both define the same entity type
* overlayFor each mob category, overrides the lower layer's spawn settings with the higher layer's, unless the category is not includedMerges each layer's spawn costs together, overriding the lower layer's spawn costs with the higher layer's if both define the same entity type
* For each mob category, overrides the lower layer's spawn settings with the higher layer's, unless the category is not included
* Merges each layer's spawn costs together, overriding the lower layer's spawn costs with the higher layer's if both define the same entity type
* Default: Empty

#### Addedminecraft:gameplay/creature_world_gen_spawn_probability

* Sets the probability to run an iteration in which mobs defined to spawn in thecreaturemob category will spawn during world generation
* Only Dimensions and Biomes will apply this Environment Attribute
* Format: float with range[0,1)
* Default:0.1

#### Changedminecraft:visual/ambient_particles

* Now supports interpolation between Timeline keyframes (probabilities will be crossfaded)
* Introduced support for new modifier:appendUnlikeoverridewhich totally replaces the particle list, this modifier concatenates all elements with the layers below
* Unlikeoverridewhich totally replaces the particle list, this modifier concatenates all elements with the layers below

### Data Components

#### Addedminecraft:cooking_fuel

* Describes an item that can be used as fuel for a Furnace, Smoker or Blast Furnace
* Format: object with fieldsburn_time- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the time, in ticks, for which this fuel will burnspeed_multiplier- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the speed of the cooking/smelting
* burn_time- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the time, in ticks, for which this fuel will burn
* speed_multiplier- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the speed of the cooking/smelting

#### Addedminecraft:brewing_fuel

* Describes an item that can be used as fuel for a Brewing Stand
* Format: object with fieldsuses- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the number of times this fuel will brew before being consumedspeed_multiplier- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the speed of the brewing
* uses- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the number of times this fuel will brew before being consumed
* speed_multiplier- namespaced ID pointing to an element ofminecraft:number_providerregistry representing the speed of the brewing
* Note: the#brewing_fuelitem tag has been removed and will no longer function to register new brewing fuels

#### Addedminecraft:sign_text_frontandminecraft:sign_text_back

* Two identical components that represent text in front and back of a sign
* Contents will be displayed in item tooltip
* The format is the same asfront_textandback_textfields onminecraft:signandminecraft:hanging_signblock entities, i.e.messages- a list of text componentsfiltered_messages- an optional list of text components, if omitted, it will be set to the same value asmessagesmessagesandfiltered_messagesmust have same entry countcolor- optional dye color, default:blackhas_glowing_text- optional boolean, default:false
* messages- a list of text components
* filtered_messages- an optional list of text components, if omitted, it will be set to the same value asmessagesmessagesandfiltered_messagesmust have same entry count
* messagesandfiltered_messagesmust have same entry count
* color- optional dye color, default:black
* has_glowing_text- optional boolean, default:false

#### Addedminecraft:waxed

* A marker for blocks with contents that are waxed
* No fields

#### Addedminecraft:cushion/color

* Applied to Cushion entities when they get placed using an item
* Format: one of 16 dye colors

#### Addedminecraft:villager_food

Represents items that Villagers can eat. Villagers will pick up items with this component in addition to items in the#villager_picks_uptag.

* Format: object with fieldsnutrition- positive integer, how much hunger the item satiates in the Villager once eaten
* nutrition- positive integer, how much hunger the item satiates in the Villager once eaten

#### Addedminecraft:mob_visibility

Represents the visibility percentage provided by an item with the appropriateminecraft:equippablecomponent, modifying the range at which mobs are able to detect an entity

* Format: object with fieldstargeting_entity- an entity ID, a list of namespaced entity IDs, or a hash-prefixed entity tag to matchvisibility- float (between 0.0 and 10.0), with 0.0 reducing the range at which mobs detects the entity to 2 blocks while 10.0 increases the detection range tenfoldWhile multiple items with this component stack, the maximum vision will still never exceed 10.0
* targeting_entity- an entity ID, a list of namespaced entity IDs, or a hash-prefixed entity tag to match
* visibility- float (between 0.0 and 10.0), with 0.0 reducing the range at which mobs detects the entity to 2 blocks while 10.0 increases the detection range tenfoldWhile multiple items with this component stack, the maximum vision will still never exceed 10.0
* While multiple items with this component stack, the maximum vision will still never exceed 10.0

### Block Entity Data

#### Changedminecraft:signandminecraft:hanging_sign

* By default, commands and other click events contained in Sign text are no longer executed when the block is clickedAdditionally, text components on newly placed Signs are no longer resolved by defaultNew boolean field calledallow_op_features(defaults tofalse) has been added to restore previous behaviorPlaced Signs and items with theminecraft:block_entity_datacomponent containing Sign data stored in worlds saved before this version will haveallow_op_featuresset totrueAny newly created Sign will need to have that field set explicitly
* Additionally, text components on newly placed Signs are no longer resolved by default
* New boolean field calledallow_op_features(defaults tofalse) has been added to restore previous behavior
* Placed Signs and items with theminecraft:block_entity_datacomponent containing Sign data stored in worlds saved before this version will haveallow_op_featuresset totrue
* Any newly created Sign will need to have that field set explicitly
* Changed the rules for opening the Sign edit screen after a block is placed:Previously, the screen would open unlessminecraft:block_entity_datawas applied successfullyNow, the screen will open only if it could be opened normally by clicking the block (i.e. it's not waxed and only has editable text on the front side)
* Previously, the screen would open unlessminecraft:block_entity_datawas applied successfully
* Now, the screen will open only if it could be opened normally by clicking the block (i.e. it's not waxed and only has editable text on the front side)
* Signs will now accept and return theminecraft:sign_text_front,minecraft:sign_text_backandminecraft:waxedcomponents

#### Changedminecraft:brewing_stand

The following fields are now stored as integers rather than shorts:

* Changed theBrewTimefield from a short to an integer, this is the amount of time that the current brewing process has taken so far
* Changed theFuelfield from a byte to an integer, this is the amount of fuel remaining

The following new fields have been added:

* Added thetotal_brew_timeinteger field, this is the total amount of time the current brewing process will take
* Added thetotal_fuelinteger field, this represents the amount of fuel that was added in the last refuel
* Added thespeed_multiplierfloat field, this will be used to speed up or slow down the next brewing process

#### Changedminecraft:furnace,minecraft:smokerandminecraft:blast_furnace

The following fields are now stored as integers rather than shorts:

* Changed thecooking_time_spentfield from a short to an integer, this is the amount of time that the current cooking process has taken so far
* Changed thecooking_total_timefield from a short to an integer, this is the total amount of time the current cooking process will take
* Changed thelit_time_remainingfield from a short to an integer, this is the amount of burn time remaining
* Changed thelit_total_timefield from a short to an integer, this is the total amount of burn time that was added in the last refuel

The following new fields have been added:

* Added thespeed_multiplierfloat field, this will be used to speed up or slow down the next brewing process

### Advancements

#### Rewards

* Thelootsub-field in therewardsfield now accepts an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:loot_tabletype

#### Triggers

* Multiple fields that accepted a list of loot conditions are now stricter:Previous functionality of a list of conditions was equivalent to a singleminecraft:all_ofcondition has been removedAdditionally,typefield is mandatory (previously it defaulted tominecraft:entity_properties)
* Previous functionality of a list of conditions was equivalent to a singleminecraft:all_ofcondition has been removed
* Additionally,typefield is mandatory (previously it defaulted tominecraft:entity_properties)
* Some fields that previously accepted only inline loot conditions now also accept a namespaced ID of aminecraft:predicate
* Theplayerfield, available on all triggers exceptminecraft:impossible, now accepts an inline value or a namespaced ID of aminecraft:predicatetypeTo avoid duplication, this field is not mentioned in entries below
* To avoid duplication, this field is not mentioned in entries below

##### Changedminecraft:any_block_usetrigger

* Thelocationfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:bee_nest_destroyed

* Theblockfield has been renamed toblocksand now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:blocktype
* Added fieldstatethat matches block state properties (same format asminecraft:enter_block)

##### Changedminecraft:bred_animalstrigger

* child,parent, andpartnerfields now accept an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:brewed_potiontrigger

* Thepotionfield now acceptsminecraft:potion_contentsdata component predicate

##### Changedminecraft:cured_zombie_villagertrigger

* villagerandzombiefields now accept an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:default_block_usetrigger

* Thelocationfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:effects_changedtrigger

* Thesourcefield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:enter_block

* Theblockfield has been renamed toblocksand now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:blocktype

##### Changedminecraft:fall_after_explosiontrigger

* Thecausefield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:fishing_rod_hookedtrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:placed_blocktrigger

* Thelocationfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:item_used_on_blocktrigger

* Thelocationfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:allay_drop_item_on_blocktrigger

* Thelocationfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:player_killed_entitytrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype
* Thekilling_blow.tags.idfield now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:damage_typetype

##### Changedminecraft:entity_killed_playertrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype
* Thekilling_blow.tags.idfield now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:damage_typetype

##### Changedminecraft:kill_mob_near_sculk_catalysttrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype
* Thekilling_blow.tags.idfield now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:damage_typetype

##### Changedminecraft:lightning_striketrigger

* bystanderandlightningfields now accept an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:player_generates_container_loottrigger

* Theloot_tablefield has been renamed toloot_tablesand now accepts a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:loot_tabletypeIf a tag or a list is used, trigger will run when any listed loot table is generated
* If a tag or a list is used, trigger will run when any listed loot table is generated

##### Changedminecraft:thrown_item_picked_up_by_playertrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:thrown_item_picked_up_by_entitytrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:player_hurt_entitytrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype
* Thedamage.type.tags.idfield now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:damage_typetype

##### Changedminecraft:entity_hurt_playertrigger

* Thedamage.type.tags.idfield now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:damage_typetype

##### Changedminecraft:player_interacted_with_entitytrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:player_sheared_equipmenttrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:crafter_recipe_craftedtrigger

* Therecipe_idfield has been renamed torecipesand now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:recipetypeIf a tag or a list is used, trigger will run when any listed recipe is used
* If a tag or a list is used, trigger will run when any listed recipe is used

##### Changedminecraft:recipe_craftedtrigger

* Therecipe_idfield has been renamed torecipesand now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:recipetypeIf a tag or a list is used, trigger will run when any listed recipe is used
* If a tag or a list is used, trigger will run when any listed recipe is used

##### Changedminecraft:recipe_unlockedtrigger

* Therecipefield has been renamed torecipesand now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:recipetypeIf a tag or a list is used, trigger will run when any listed recipe is unlocked
* If a tag or a list is used, trigger will run when any listed recipe is unlocked

##### Changedminecraft:slide_down_block

* Theblockfield has been renamed toblocksand now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:blocktype

##### Changedminecraft:summoned_entitytrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:tame_animaltrigger

* Theentityfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:target_hittrigger

* Theprojectilefield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

##### Changedminecraft:villager_tradetrigger

* Thevillagerfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

### Slot Sources

#### Changedminecraft:group

* Thetermsfield now accepts an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:slot_sourcetype
* Inline format ofminecraft:group(previously only a list of inline slot source) can now also accept a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:slot_sourcetypeThis format is now available consistenly available for all fields of slot source
* This format is now available consistenly available for all fields of slot source

#### Changedminecraft:filtered

* Theslot_sourcefield now accepts an inline value or a namespaced ID of aminecraft:slot_sourcetype

#### Changedminecraft:contents

* Theslot_sourcefield now accepts an inline value or a namespaced ID of aminecraft:slot_sourcetype

#### Changedminecraft:limit_slots

* Theslot_sourcefield now accepts an inline value or a namespaced ID of aminecraft:slot_sourcetype

#### Removedminecraft:reference

* This slot source has become obsolete, as any field that takes slot source now accepts (among other fields) a namespaced ID of aminecraft:slot_sourcetype

### Loot Tables

* Therollsandbonus_rollsfields now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Loot Table Types

##### Addedminecraft:container_processloot table type

* Currently used to evaluate cooking and brewing fuel values
* It takes the following parameters:container, the container or inventory being evaluatedblock_entity, the block entity being fueledblock_state, the current state of the block being fueledorigin, the location of the block being fueled
* container, the container or inventory being evaluated
* block_entity, the block entity being fueled
* block_state, the current state of the block being fueled
* origin, the location of the block being fueled

##### Changedminecraft:advancement_location

* Block entities are now available in context and can be matched by conditions likeminecraft:match_block

#### Loot Pool Entries

* Theconditionsfield in loot pool entries has been renamed toconditionand now accepts an inline value or a namespaced ID of aminecraft:predicatetype
* Thefunctionsfield in loot pool entries has been renamed tomodifierand now accepts an inline value (including list as a short form ofminecraft:sequence) or a namespaced ID of aminecraft:item_modifiertypeThis field is now present on all loot entries, including previously omittedminecraft:alternatives,minecraft:sequenceandminecraft:group
* This field is now present on all loot entries, including previously omittedminecraft:alternatives,minecraft:sequenceandminecraft:group

##### Changedminecraft:tagloot pool entry

* Thenamefield has been renamed toitemsand now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:itemtype

##### Changedminecraft:loot_tableloot pool entry

* Thevaluefield now accepts a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:loot_tabletype
* Addedexpandfield, working the same as inminecraft:tagpool entry:iftrue, each entry inside tag will be added to outer pool, with weights equal to weight of this entryiffalse, this pool entry will operate as a single entry in outer pool. If this entry gets selected, it will return all items from all referenced loot tables
* iftrue, each entry inside tag will be added to outer pool, with weights equal to weight of this entry
* iffalse, this pool entry will operate as a single entry in outer pool. If this entry gets selected, it will return all items from all referenced loot tables

### Loot Functions

* Theconditionsfield is now available in all loot functions and has been renamed toconditionIt now also accepts an inline value or a namespaced ID, but no longer an inline list of conditionsFunctionality of old condition list format can be achieved by explicitly usingminecraft:all_ofloot condition type
* It now also accepts an inline value or a namespaced ID, but no longer an inline list of conditions
* Functionality of old condition list format can be achieved by explicitly usingminecraft:all_ofloot condition type
* Thefunctionfield (describing function type) has been renamed totype

#### Changedminecraft:sequence

* Thefunctionsfield now accepts an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:item_modifiertype
* Added optionalconditionfield which accepts an inline value or a namespaced ID of aminecraft:predicatetype
* Inline format ofminecraft:sequence(previously only a list of inline functions) can now also accept a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:item_modifiertypeThis format is now consistenly available for all fields of loot function type, which means that every such field can accept an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:item_modifiertype
* This format is now consistenly available for all fields of loot function type, which means that every such field can accept an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:item_modifiertype

#### Changedminecraft:modify_contents

* Themodifierfield now accepts an inline value or a namespaced ID of aminecraft:item_modifiertype

#### Changedminecraft:set_attributes

* Number providers inamountsub-fields ofmodifierslist now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:enchanted_count_increase

* Thecountfield now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:enchant_with_levels

* Thelevelsfield now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_custom_model_data

* Elements infloatsandcolorslists can now be an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_enchantments

* Values inenchantmentsmap can now be an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_count

* Thecountfield now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:limit_count

* Theminandmaxfields insidelimitstructure now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_damage

* Thecountfield now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_ominous_bottle_amplifier

* Theamplifierfield now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_random_dyes

* Thenumber_of_dyesfield now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_stew_effect

* Thedurationfield in elements ofeffectslist now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:set_loot_table

* Thenamefield has been renamed totag

#### Changedminecraft:exploration_map

* Thedestinationfield is no longer optional and now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:structuretype

#### Removedminecraft:reference

* This function has become obsolete, as any field that takes a function now accepts (among other things) a namespaced ID to other functions

### Predicates

* Theconditionfield (describing predicate type) has been renamed totype

#### Changedminecraft:all_of

* Thetermsfield now accepts an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:predicatetype
* Note: values of this type can no longer be shortened to a single list, a full object with typeminecraft:all_ofneeds to be used explicitly

#### Changedminecraft:any_of

* Thetermsfield now accepts an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:predicatetype

#### Changedminecraft:inverted

* Thetermfield now accepts an inline value or a namespaced ID of aminecraft:predicatetype

#### Changedminecraft:random_chance

* Thechancefield now accepts an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:value_check

* Thevaluefield now accepts an inline value or a namespaced ID of aminecraft:number_providertype
* Theminandmaxfields insiderangestructure now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:time_check

* Theminandmaxfields insidevaluestructure now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:entity_scores

* Theminandmaxfields inside values ofscoresmap now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:damage_source_properties

* Thepredicate.tags.idfield now accepts a single namespaced ID, a list of namespaced IDs, or a hash-prefixed tag ID of aminecraft:damage_typetype

#### Removedminecraft:reference

* This condition has become obsolete, as any field that takes a loot condition now accepts (among other things) a namespaced ID to other conditions

#### Added vanilla predicates

* minecraft:block/fast_cooking

#### Addedminecraft:match_blockcondition type

Matches block state and optionally block entity data and components (if present)

Fields (same as elements ofminecraft:can_place_oncomponents):

* blocks- optional block id, list of namespaced block IDs, or hash-prefixed block tag to match
* state: optional map of block state property keys to values to match
* nbt: optional block entity NBT to match
* match will fail if this field is present, but block entity is not available in context
* components- optional map of exact components to match
* match will fail if this field is present, but block entity is not available in context
* predicates- optional map of component predicates to match
* match will fail if this field is present, but block entity is not available in context

#### Removedminecraft:block_state_propertycondition type

* This has been fully replaced byminecraft:match_block

### Number Providers

* Thetypefield always needs to be specified explicitly when using an inline number provider (it was previously defaulting tominecraft:uniform)

#### Added vanilla number providers

* minecraft:cooking/time_bambooReturns the burn time in ticks for bamboo and scaffolding
* Returns the burn time in ticks for bamboo and scaffolding
* minecraft:cooking/time_blaze_rodReturns the burn time in ticks for blaze rods
* Returns the burn time in ticks for blaze rods
* minecraft:cooking/time_boatsReturns the burn time in ticks for boats
* Returns the burn time in ticks for boats
* minecraft:cooking/time_coalReturns the burn time in ticks for coal
* Returns the burn time in ticks for coal
* minecraft:cooking/time_coal_blockReturns the burn time in ticks for coal blocks
* Returns the burn time in ticks for coal blocks
* minecraft:cooking/time_dried_kelp_blockReturns the burn time in ticks for dried kelp blocks
* Returns the burn time in ticks for dried kelp blocks
* minecraft:cooking/time_dry_plantsReturns the burn time in ticks for various dry plants
* Returns the burn time in ticks for various dry plants
* minecraft:cooking/time_hanging_signsReturns the burn time in ticks for hanging signs
* Returns the burn time in ticks for hanging signs
* minecraft:cooking/time_lava_bucketReturns the burn time in tickss for lava buckets
* Returns the burn time in tickss for lava buckets
* minecraft:cooking/time_rootsReturns the burn time in ticks for mangrove roots
* Returns the burn time in ticks for mangrove roots
* minecraft:cooking/time_wood_blocksReturns the burn time in ticks for wood blocks
* Returns the burn time in ticks for wood blocks
* minecraft:cooking/time_wood_items_extra_smallReturns the burn time in ticks for very small wood items such as buttons
* Returns the burn time in ticks for very small wood items such as buttons
* minecraft:cooking/time_wood_items_largeReturns the burn time in ticks for large wood items such as doors
* Returns the burn time in ticks for large wood items such as doors
* minecraft:cooking/time_wood_items_smallReturns the burn time in ticks for small wood items such as bows
* Returns the burn time in ticks for small wood items such as bows
* minecraft:cooking/time_wood_slabsReturns the burn time in ticks for wood slabs
* Returns the burn time in ticks for wood slabs
* minecraft:cooking/time_woolReturns the burn time in ticks for most wool blocks
* Returns the burn time in ticks for most wool blocks
* minecraft:cooking/time_wool_carpetsReturns the burn time in ticks for wool carpets
* Returns the burn time in ticks for wool carpets
* minecraft:cooking/time_wool_slabsReturns the burn time in ticks for wool slabs and cushions
* Returns the burn time in ticks for wool slabs and cushions
* minecraft:cooking/speed_defaultReturns the default speed multiplier for cooking fuel
* Returns the default speed multiplier for cooking fuel
* minecraft:brewing/speed_defaultReturns the default speed multiplier for brewing fuel
* Returns the default speed multiplier for brewing fuel
* minecraft:brewing/uses_defaultReturns the default number of brews provided by brewing fuel
* Returns the default number of brews provided by brewing fuel

#### Changedminecraft:number_dispatcher

* Fields:cases- a list of cases in the order that the dispatcher will try to execute themFields:condition- an inline value or a namespaced ID of aminecraft:predicatetypenumber_provider- an inline value or a namespaced ID of aminecraft:number_providertype which is executed if the condition is fulfilleddefault- an optional inline value or a namespaced ID of aminecraft:number_providertypeDefaults to a constant0if omitted
* cases- a list of cases in the order that the dispatcher will try to execute themFields:condition- an inline value or a namespaced ID of aminecraft:predicatetypenumber_provider- an inline value or a namespaced ID of aminecraft:number_providertype which is executed if the condition is fulfilled
* Fields:condition- an inline value or a namespaced ID of aminecraft:predicatetypenumber_provider- an inline value or a namespaced ID of aminecraft:number_providertype which is executed if the condition is fulfilled
* condition- an inline value or a namespaced ID of aminecraft:predicatetype
* number_provider- an inline value or a namespaced ID of aminecraft:number_providertype which is executed if the condition is fulfilled
* default- an optional inline value or a namespaced ID of aminecraft:number_providertypeDefaults to a constant0if omitted
* Defaults to a constant0if omitted

#### Changedminecraft:conditional_value

* Fields:conditions- an inline value or a namespaced ID of aminecraft:predicatetypeon_true- an inline value or a namespaced ID of aminecraft:number_providertype which is executed if its condition is fulfilledon_false- an optional inline value or a namespaced ID of aminecraft:number_providertypeDefaults to a constant0if omitted
* conditions- an inline value or a namespaced ID of aminecraft:predicatetype
* on_true- an inline value or a namespaced ID of aminecraft:number_providertype which is executed if its condition is fulfilled
* on_false- an optional inline value or a namespaced ID of aminecraft:number_providertypeDefaults to a constant0if omitted
* Defaults to a constant0if omitted

#### Changedminecraft:weighted_list

* Fields:distribution- a list of objects with the following fieldsFields:data- an inline value or a namespaced ID of aminecraft:number_providertypeweight- a positive integer
* distribution- a list of objects with the following fieldsFields:data- an inline value or a namespaced ID of aminecraft:number_providertypeweight- a positive integer
* Fields:data- an inline value or a namespaced ID of aminecraft:number_providertypeweight- a positive integer
* data- an inline value or a namespaced ID of aminecraft:number_providertype
* weight- a positive integer

#### Changedminecraft:uniform

* Theminandmaxfields now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:binomial

* Thenandpfields now accept an inline value or a namespaced ID of aminecraft:number_providertype

#### Changedminecraft:sum

* Thesummandsfield now accepts an inline value, a single namespaced ID, a list of namespaced IDs, a list of inline values, or a hash-prefixed tag ID of aminecraft:number_providertype

### Recipes

#### Smoker and Blast Furnace Recipes

The recipes for Smokers and Blast Furnaces now use the same cooking time in their data definition as their Furnace counterparts.

The cooking time speedup is now done through theminecraft:cooking/speed_defaultNumber Provider used by the furnace fuel components.

### World Generation

#### Biomes

* Removed thespawners,spawn_costs, andcreature_spawn_probabilityfieldsThese values have been moved to the new Environment Attributes
* These values have been moved to the new Environment Attributes

#### Features

* Removed feature types:minecraft:nether_forest_vegetationminecraft:twisting_vinesminecraft:weeping_vines
* minecraft:nether_forest_vegetation
* minecraft:twisting_vines
* minecraft:weeping_vines

#### Noise Settings

* Thefinal_densityfield no longer has thebeardifierDensity Function implicitly added to the final result
* Theaquifers_enabledfield has been replaced by an optionalaquifersobject:If not present, no aquifers will be generatedFields:barrier- Density Function, moved fromnoise_router.barrierfluid_level_floodedness- Density Function, moved fromnoise_router.fluid_level_floodednessfluid_level_spread- Density Function, moved fromnoise_router.fluid_level_spreadlava- Density Function, moved fromnoise_router.lavasurface_level- Density Function, duplicated fromnoise_router.preliminary_surface_levelexclusion- Density Function, any aquifer cell where this value is positive will have no fluid
* If not present, no aquifers will be generated
* Fields:barrier- Density Function, moved fromnoise_router.barrierfluid_level_floodedness- Density Function, moved fromnoise_router.fluid_level_floodednessfluid_level_spread- Density Function, moved fromnoise_router.fluid_level_spreadlava- Density Function, moved fromnoise_router.lavasurface_level- Density Function, duplicated fromnoise_router.preliminary_surface_levelexclusion- Density Function, any aquifer cell where this value is positive will have no fluid
* barrier- Density Function, moved fromnoise_router.barrier
* fluid_level_floodedness- Density Function, moved fromnoise_router.fluid_level_floodedness
* fluid_level_spread- Density Function, moved fromnoise_router.fluid_level_spread
* lava- Density Function, moved fromnoise_router.lava
* surface_level- Density Function, duplicated fromnoise_router.preliminary_surface_level
* exclusion- Density Function, any aquifer cell where this value is positive will have no fluid
* Theore_veins_enabledfield has been replaced by an optional list ofore_veinsobjects:If not present, no ore veins will be generatedFields:ore_block- Block State, the ore block to placeraw_ore_block- Block State, the raw ore block to placefiller_block- Block State, the filler block to placeraw_ore_chance- float between 0 and 1, the probability for araw_ore_blockto be placed instead of anore_blockdensity- Density Function, the probability between 0 and 1 for the ore vein to replace a blockIf0or lower, no block will be replacedrichness- Density Function, the probability between 0 and 1 forore_blockorraw_ore_blockto be placed (as opposed tofiller_block)If0or lower, all blocks will befiller_blockIf1or greater, no blocks will befiller_blockfiller_gap- Density Function, acts as an override torichness: if positive,filler_blockwill always be placed
* If not present, no ore veins will be generated
* Fields:ore_block- Block State, the ore block to placeraw_ore_block- Block State, the raw ore block to placefiller_block- Block State, the filler block to placeraw_ore_chance- float between 0 and 1, the probability for araw_ore_blockto be placed instead of anore_blockdensity- Density Function, the probability between 0 and 1 for the ore vein to replace a blockIf0or lower, no block will be replacedrichness- Density Function, the probability between 0 and 1 forore_blockorraw_ore_blockto be placed (as opposed tofiller_block)If0or lower, all blocks will befiller_blockIf1or greater, no blocks will befiller_blockfiller_gap- Density Function, acts as an override torichness: if positive,filler_blockwill always be placed
* ore_block- Block State, the ore block to place
* raw_ore_block- Block State, the raw ore block to place
* filler_block- Block State, the filler block to place
* raw_ore_chance- float between 0 and 1, the probability for araw_ore_blockto be placed instead of anore_block
* density- Density Function, the probability between 0 and 1 for the ore vein to replace a blockIf0or lower, no block will be replaced
* If0or lower, no block will be replaced
* richness- Density Function, the probability between 0 and 1 forore_blockorraw_ore_blockto be placed (as opposed tofiller_block)If0or lower, all blocks will befiller_blockIf1or greater, no blocks will befiller_block
* If0or lower, all blocks will befiller_block
* If1or greater, no blocks will befiller_block
* filler_gap- Density Function, acts as an override torichness: if positive,filler_blockwill always be placed
* The following fields fromnoise_routerhave been moved:barrier,fluid_level_floodedness,fluid_level_spread,lava- moved intoaquifersfieldvein_toggle,vein_ridged,vein_gap- moved intoore_veinsfield
* barrier,fluid_level_floodedness,fluid_level_spread,lava- moved intoaquifersfield
* vein_toggle,vein_ridged,vein_gap- moved intoore_veinsfield

#### Density Functions

##### Updatedconstant

* argumenthas been renamed tovalue

##### Updatedadd,mul,min, andmax

* argument1has been renamed toleft
* argument2has been renamed toright

##### Updatedabs,square,cube,half_negative,quarter_negative,squeeze,interpolated,flat_cache,cache_2d,cache_once,cache_all_in_cell, andblend_densityDensity Functions

* argumenthas been renamed toinput

##### Updatedshift_a,shift_b, andshift

* argumenthas been renamed tonoise

##### Addedsub

Performs subtraction between two arguments. Format: object with fields:

* left- Density Function, the left-hand side of the operation
* right- Density Function, the right-hand side of the operation

##### Addeddiv

Performs division between two arguments. Format: object with fields:

* left- Density Function, the left-hand side of the operation
* right- Density Function, the right-hand side of the operation

##### Updatedreciprocal

* Renamed frominvert

##### Addednegate

Negates the input. Format: object with fields:

* input- Density Function, the function to negate

##### Addedlerp

Performs (unclamped) linear interpolation between two arguments based on an alpha. Format: object with fields:

* alpha- Density Function, the interpolation factor (0=first,1=second)Any value outside of[0; 1]will extrapolate
* Any value outside of[0; 1]will extrapolate
* first- Density Function, the value atalpha=0
* second- Density Function, the value atalpha=1

##### Addedfloor,round,ceil, andtruncate

Rounds the input value to an integer multiple of a given function in a type-dependent direction:

* floor: rounds towards negative infinity
* round: rounds towards the nearest integer (ties round up)
* ceil: rounds towards positive infinity
* truncate: rounds towards 0

Format: object with fields:

* input- Density Function, the input to round
* multiple- Density Function, the output will be rounded to an integer multiple of this valueIf not specified, defaults to constant1(i.e. rounding to integer)
* If not specified, defaults to constant1(i.e. rounding to integer)

##### Addedbeardifier

Outputs the structure bearding density. Generally summed together with the base terrain density to produce ground below, carve air around, or bury structures.

Format: no fields

### Villager Trades

* Thegiven_item_modifiersfield has been renamed togiven_item_modifierNote: unlike other fields of typeminecraft:item_modifierthis field does not support namespaced element or tag IDs
* Note: unlike other fields of typeminecraft:item_modifierthis field does not support namespaced element or tag IDs

### Tags

#### Block Tags

* Added#cushion_uses_collision_shape- Blocks where Cushion placement raycasts against collision shape instead of interaction shapeDefault entries: all blocks in#cauldrons, plushopperandcomposter
* Default entries: all blocks in#cauldrons, plushopperandcomposter

#### Item Tags

* Removed#brewing_fuel- thebrewing_fuelitem component is now used to identify brewing fuels

## Resource Pack Version 92.0

### Shaders & Post-process Effects

* Added new shaders to support order-independent transparency:core/oit_depth_bounds_cull.fsh
* core/oit_depth_bounds_cull.fsh
* Updated core shaders to support order-independent transparencyIntroduced new defines:OIT_ALWAYS_WRITE_DEPTH- A boolean indicating that the OIT algorithm should always write depth for the executing pipeline during the depth bounds stage
* Introduced new defines:OIT_ALWAYS_WRITE_DEPTH- A boolean indicating that the OIT algorithm should always write depth for the executing pipeline during the depth bounds stage
* OIT_ALWAYS_WRITE_DEPTH- A boolean indicating that the OIT algorithm should always write depth for the executing pipeline during the depth bounds stage

#### New Core Shaders

* core/integrate_depth.fshwas added and is used to integrate the "3d hud" and always-on-top gizmo depth buffers into the main depth buffer

## Fixed bugs in 26.3 Snapshot 4

* MC-2157- Particles emitted from dragon eggs when teleporting do not point in the correct direction
* MC-46421- You cannot use nether portals, end portals, and end gateways while in Spectator mode
* MC-58061- Endermen can teleport onto signs
* MC-110989- /spreadplayers considers signs to be a valid block to be spread onto
* MC-116286- /spreadplayers can spread entities on structure void
* MC-121278- Keybindings (e.g. Ctrl+A) are being mapped to the US keyboard layout even if you're using another layout
* MC-133407- Keybinds switch when upgrading to 1.13 if not using a QWERTY keyboard
* MC-148541- /spreadplayers can spread players to seagrass near the surface of the water
* MC-212671- Loot table tag entry with "expand": true does not apply functions
* MC-252934- Placing structures with item frames, paintings, or cushions logsBlock-attached entity at invalid position: [BlockPosition]
* MC-263708- Keybinds menu renders Keypad keys the same as regular keys
* MC-266429- Holding shift on macOS causes hotbar scroll direction to reverse (mouse only)
* MC-268521- The game window doesn't have a minimal width and height
* MC-269968- Can't scroll while holding shift on macOS (except in the hotbar) (mouse only)
* MC-299019- Using a Bed while riding a rideable mob causes the player to sleep either on the ground, or on top of the mob
* MC-303493- Theapply_impulseentity effect does not apply components of the impulse that would cause the affected entity to hit a solid block when used with atickorlocation_changedadvancement trigger
* MC-303789- Looking directly up with anapply_impulseenchantment entity effect will limit the impulse's effect on the X and Z axes to only apply on one of the two horizontal axes
* MC-306619- Cannot jump while sneaking while using a Chinese input method
* MC-308127- The "Friends Screen" key bind overrides debug hotkeys using the same key
* MC-308222- Worldgen heightmaps do not persist properly through chunk saving/loading
* MC-308469- Hitting the ender dragon's head hitbox no longer causes the ender dragon to take more damage
* MC-308804- The input method does not switch to the corresponding CJK mode in the Create New World screen
* MC-309166- Block breaking is delayed after hitting an entity in Survival/Adventure mode
* MC-309394- The game crashes when trying to render the item texture of a filled map in the world with the "Improved Transparency" option enabled
* MC-309474- Block displays do not display glass blocks when the "Improved Transparency" setting is enabled
* MC-309475- Shelf mushrooms held in the off hand are rotated incorrectly
* MC-309506- Blocks z-fight with the world border with the "Improved Transparency" option enabled
* MC-309513- The top texture of stripped poplar logs uses a different color from the middle of the top texture of poplar logs
* MC-309521- The texture of poplar hanging signs uses a recolored version of the texture of stripped pale oak instead of stripped poplar
* MC-309522- Translucent objects can be seen through glass block elements when the "Improved Transparency" option is enabled
* MC-309524- Drowned that are outside of water continue to aim their trident at players within 3 blocks of them
* MC-309656- Cushions can be placed on top of fire
* MC-309659- Cushions cannot be placed on the highest edge of a lectern
* MC-309685- Sleeping on the head part of a straw bed teleports the player to Y=-Infinity
* MC-309686- The game crashes when shooting some projectiles outside the vertical limits of the world
* MC-309693- The ender dragon appears to fly backwards until perching
* MC-309695- You can place cushions at any height inside cauldrons, composters, and hoppers
* MC-309697- The texture of the top half of poplar doors has a miscolored pixel on the hinge
* MC-309703- Breaking a cushion causes it to lose its custom name
* MC-309707- The texture of straw beds does not align with the texture of hay bales
* MC-309718- Mob positions permanently desync after tick sprinting
* MC-309771- Themaintarget's depth buffer only contains the player's arm when fetched from post effects
* MC-309790- You can sleep while on a cushion
* MC-309809- Waxing a sign or a hanging sign doesn't play any sound
* MC-309832- Placed cushions do not respect thecolortag in theentity_datacomponent of the item used to place them
* MC-309891- Thechat_restriction.disabled_by_launcherstring lacks a period, unlike similar strings
* MC-309893- Thegamerule.minecraft.fire_spread_radius_around_player.descriptionstring lacks a period, unlike similar strings
* MC-309897- Thegui.report_to_serverstring is improperly capitalized
* MC-309898- TheeditGamerule.inGame.discardChanges.titlestring is improperly capitalized
* MC-309901- Thestructure_block.position.xstring is improperly capitalized
* MC-309902- Some strings contain stray spaces adjacent to line breaks
* MC-309903- The "Isn't It Iron Pick" advancement name is missing a question mark
* MC-309907- The word "whoosh" is mispelled as "woosh" in thesubtitles.block.bubble_column.upwards_insidestring
* MC-309908- Thesubtitles.entity.copper_golem.no_item_getstring is missing an article before the word "item"
* MC-309911- The words "blocks" and "seconds" in thecommands.worldborder.set.growstring are always pluralized
* MC-309914- Thecommands.op.failedstring has awkward and inconsistent adverb placement, unlike similar strings
* MC-309915- Thecommands.kick.owner.failedstring is missing articles before the words "server" and "LAN"
* MC-309916- Some /stopwatch strings incorrectly capitalize the word "Stopwatch" mid-sentence, which is inconsistent with other commands
* MC-309918- Thecommands.perf.startedstring is missing a hyphen between the words "10" and "second" and an article before the word "10"
* MC-309919- Themco.errorMessage.6002string is improperly capitalized
* MC-309920- Themco.configure.world.close.question.line1string is improperly capitalized
* MC-309921- Themco.snapshot.subscription.infostring uses the "to" preposition instead of "with"
* MC-309922- TheadvMode.trackOutputstring is improperly capitalized
* MC-309923- Thegamerule.minecraft.entity_drops.descriptionstring is improperly capitalized
* MC-309924- Theargument.enum.invalidstring surrounds the placeholder with double quotes instead of single quotes, unlike every other command
* MC-309925- Themount.onboardstring is improperly capitalized
* MC-309926- TheselectWorld.edit.backupSizestring is improperly capitalized
* MC-309927- Thegui.friends.error.unauthorizedstring lacks a period, unlike similar strings
* MC-309928- Themultiplayer.confirm_command.signature_requiredstring lacks a period
* MC-309937- Theargument.pos.outofboundsstring ends with a period, unlike similar strings
* MC-309938- Thequickplay.error.invalid_identifierstring is missing an article before the word "world"
* MC-309940- ThedatapackFailure.safeMode.failed.titlestring ends with a period, unlike similar title strings
* MC-309980- Cushions last longer as fuel than in Bedrock Edition
* MC-310045- Opaque particles turn translucent when seen through experience orbs with the "Improved Transparency" option enabled
* MC-310075- The game crashes when placing a bee nest or beehive at the lowest height of the world

## Get the Snapshot

Snapshots are available for Minecraft: Java Edition. To install the Snapshot, open up theMinecraft Launcherand enable snapshots in the "Installations" tab.

Testing versions can corrupt your world, so please backup and/or run them in a different folder from your main worlds.

Cross-platform server jar:

* Minecraft server jar

Report bugs here:

* Minecraft issue tracker!

Want to give feedback?

* For any feedback and suggestions, head over to theFeedback site. If you're feeling chatty, join us over at theofficial Minecraft Discord.

## Share this story

## Newest News

 
 
 Catch up on the latest Minecraft news & game updates!