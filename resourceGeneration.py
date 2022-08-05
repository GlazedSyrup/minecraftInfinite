import random
import os
import subprocess
import sys
import shutil

from dataManagement import fetchResource1, fetchResource2, fetchResource3
from fileGeneration import createdirectory, batchbuild
from recoloring import spriteCreator, layerSpriteCreator, oreSpriteCreator, ArmorSpriteCreator

def initAppend(l1, d1, l2, d2, l3, d3, l4, d4, l5=None, d5=None):
    l1.append(d1)
    l2.append(d2)
    l3.append(d3)
    l4.append(d4)
    if not l5 == None:
        l5.append(d5)

def langAppend(l1, d1, l2, d2):
    l1.append(d1)
    l2.append(d2)

def oreAppend(l1, d1, l2, d2, l3, d3, l4, d4, l5, d5, l6, d6):
    l1.append(d1)
    l2.append(d2)
    l3.append(d3)
    l4.append(d4)
    l5.append(d5)
    l6.append(d6)

def craftAppend(l1, d1, l2, d2, l3, d3, l4, d4, l5, d5, l6, d6, l7, d7):
    l1.append(d1)
    l2.append(d2)
    l3.append(d3)
    l4.append(d4)
    l5.append(d5)
    l6.append(d6)
    l7.append(d7)

def oreConstantsAppend(l1, d1, l2, d2, l3, d3, l4, d4):
    l1.append(d1)
    l2.append(d2)
    l3.append(d3)
    l4.append(d4)

def newResource(directory, num, names, hues, effects, refinements):
    #file creation vars
    textureDirectory = directory + "resources/assets/mcinfini/textures/"
    createdirectory(textureDirectory + "blocks/")
    createdirectory(textureDirectory + "items/")
    createdirectory(textureDirectory + "models/armor/")

    previous_ore = None





    #blockinit
    blocks = []
    blockproperties = []
    mineable = []
    mineabletool = []

    #iteminit
    items = []
    itemtypes = []
    modeltypes = []
    itemproperties = []

    #lang
    langtags = []
    blockitems = []

    #oregen
    ore = []
    orebase = []
    opv = []
    vpc = []
    loc = []
    loc2 = []

    #crafting
    count = []
    group = []
    type = []
    grid = []
    input = []
    output = []
    filename = []

    #onevalueperore
    rarity = []
    toolvalues = []

    for i in range(num):
        print("i", i)
        raritytemp = "TIER"+str(i+1)
        rarity.append(raritytemp)
        toolvaluestemp = ","+str(i)+",3.5f"
        toolvalues.append(toolvaluestemp)

        name = names[i]
        hue = hues[i]
        effect = effects[i]
        refinement = refinements[i]

        dark = False
        light = False

        dec = False

        if refinement:
            suffix = "_ingot"
            prefix = "raw_"
        else:
            suffix = ""
            prefix = ""



        #Generate The Ore Block
        baseid = random.choice(fetchResource1("block_sprites", "id", "tag", "=", "'orebase'"))[0]
        oreid = random.choice(fetchResource3("block_sprites", "id", "tag", "=", "'orelayer'", "dark", "=", dark, "light", "=", light))[0]
        yvals = random.choice(fetchResource1("block_sprites", "yvalues", "id", "=", baseid))[0]
        dimension = random.choice(fetchResource1("block_sprites", "dimension", "id", "=", baseid))[0]
        base = fetchResource1("block_sprites", "name", "id", "=", baseid)[0][0]
        oreSpriteCreator(textureDirectory+"blocks/", name, hue, oreid, baseid)

        #dimension = fetchResource1("block_sprites", "dimension", "id", "=", baseid)[0][0] #NEED TO ADD COLUMNS TO DATABASE AND RE ENTER VALUES
        #max = fetchResource1("block_sprites", "max_y", "id", "=", baseid)[0][0] #NEED TO ADD COLUMNS TO DATABASE AND RE ENTER VALUES
        #min = fetchResource1("block_sprites", "min_y", "id", "=", baseid)[0][0] #NEED TO ADD COLUMNS TO DATABASE AND RE ENTER VALUES
        #mid = random.randint(min, max)
        if fetchResource1("block_sprites", "stone", "id", "=", baseid)[0][0]:
            temp = "pickaxe"
            temp2 = "Material.STONE).strength(3f).requiresCorrectToolForDrops()"
        elif fetchResource1("block_sprites", "soil", "id", "=", baseid)[0][0]:
            temp = "shovel"
            temp2 = "Material.DIRT).strength(1f)"
        else:
            temp = "axe"
            temp2 = "Material.WOOD).strength(2f)"

        initAppend(blocks, name+"_ore", blockproperties, temp2, mineable, temp, mineabletool, previous_ore, modeltypes, "block")
        langAppend(langtags, "block", blockitems, name+"_ore")
        oreAppend(ore, name+"_ore", orebase, base, opv, random.randint(4, 10), vpc, random.randint(40, 80), loc, dimension, loc2, random.randint(yvals[0], yvals[1]))


        if refinement:
            #Generate The Raw Block
            choice = random.choice(fetchResource3("block_sprites", "id", "tag", "=", "'raw'", "dark", "=", dark, "light", "=", light))[0]
            spriteCreator(textureDirectory+"blocks/", "raw_"+name+"_block", "block_sprites", hue, choice)

            initAppend(blocks, "raw_"+name+"_block", blockproperties, "Material.METAL).strength(3f).requiresCorrectToolForDrops()", mineable, "pickaxe", mineabletool, previous_ore, modeltypes, "block")
            langAppend(langtags, "block", blockitems, "raw_"+name+"_block")
            craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", "#", "#", "#", "#", "#", "#", "#", "#"], input, ["mcinfini:raw_"+name], output, "raw_"+name+"_block", filename, "raw_"+name+"_block")

            #Generate The Raw Ingot
            choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'raw'", "dark", "=", dark, "light", "=", light))[0]
            spriteCreator(textureDirectory+"items/", "raw_"+name, "item_sprites", hue, choice)

            initAppend(items, "raw_"+name, itemproperties, "", itemtypes, "Item", modeltypes, "generated")
            langAppend(langtags, "item", blockitems, "raw_"+name)
            craftAppend(count, 9, group, None, type, "crafting_shapeless", grid, None, input, ["mcinfini:raw_"+name+"_block"], output, "raw_"+name, filename, "raw_"+name)

            #Generate The Ingot
            choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'ingot'", "dark", "=", dark, "light", "=", light))[0]
            spriteCreator(textureDirectory+"items/", name+"_ingot", "item_sprites", hue, choice)

            initAppend(items, name+"_ingot", itemproperties, "", itemtypes, "Item", modeltypes, "generated")
            langAppend(langtags, "item", blockitems, name+"_ingot")
            craftAppend(count, 9, group, None, type, "crafting_shapeless", grid, None, input, ["mcinfini:"+name+"_block"], output, name+"_ingot", filename, name+"_ingot_from_"+name+"_block")
            craftAppend(count, 1, group, name+"_ingot", type, "crafting_shaped", grid, ["#", "#", "#", "#", "#", "#", "#", "#", "#"], input, ["mcinfini:"+name+"_nugget"], output, name+"_ingot", filename, name+"_ingot_from_"+name+"_nugget")
            craftAppend(count, 1, group, name+"_ingot", type, "smelting", grid, None, input, ["mcinfini:raw_"+name], output, name+"_ingot", filename, name+"_ingot_from_smelting_raw_"+name)

            #Generate The Nugget


        else:
            #Generate The Gem
            choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'gem'", "dark", "=", dark, "light", "=", light))[0]
            spriteCreator(textureDirectory+"items/", name, "item_sprites", hue, choice)

            initAppend(items, name, itemproperties, "", itemtypes, "Item", modeltypes, "generated")
            langAppend(langtags, "item", blockitems, name)
            craftAppend(count, 9, group, None, type, "crafting_shapeless", grid, None, input, ["mcinfini:"+name+"_block"], output, name, filename, name)

        #Generate The Gem Block
        choice = random.choice(fetchResource3("block_sprites", "id", "tag", "=", "'gem'", "dark", "=", dark, "light", "=", light))[0]
        spriteCreator(textureDirectory+"blocks/", name+"_block", "block_sprites", hue, choice)

        initAppend(blocks, name+"_block", blockproperties, "Material.HEAVY_METAL).strength(3f).requiresCorrectToolForDrops()", mineable, "pickaxe", mineabletool, previous_ore, modeltypes, "block")
        langAppend(langtags, "block", blockitems, name+"_block")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", "#", "#", "#", "#", "#", "#", "#", "#"], input, ["mcinfini:"+name+suffix], output, name+"_block", filename, name+"_block")


        #Generate The Tools
        #Generate The Axe
        choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'axe'", "dark", "=", dark, "light", "=", light))[0]
        layerSpriteCreator(textureDirectory+"items/", name+"_axe", hue, choice)

        initAppend(items, name+"_axe", itemproperties, "ToolTiers.TOOL"+raritytemp+toolvaluestemp+",", itemtypes, "AxeItem", modeltypes, "handheld")
        langAppend(langtags, "item", blockitems, name+"_axe")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", "#", "", "#", "X", "", " ", "X", ""], input, ["mcinfini:"+name+suffix, "minecraft:stick"], output, name+"_axe", filename, name+"_axe")

        #Generate The Pickaxe
        choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'pickaxe'", "dark", "=", dark, "light", "=", light))[0]
        layerSpriteCreator(textureDirectory+"items/", name+"_pickaxe", hue, choice)

        initAppend(items, name+"_pickaxe", itemproperties, "ToolTiers.TOOL"+raritytemp+toolvaluestemp+",", itemtypes, "PickaxeItem", modeltypes, "handheld")
        langAppend(langtags, "item", blockitems, name+"_pickaxe")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", "#", "#", " ", "X", " ", " ", "X", " "], input, ["mcinfini:"+name+suffix, "minecraft:stick"], output, name+"_pickaxe", filename, name+"_pickaxe")

        #Generate The Sword
        choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'sword'", "dark", "=", dark, "light", "=", light))[0]
        layerSpriteCreator(textureDirectory+"items/", name+"_sword", hue, choice)

        initAppend(items, name+"_sword", itemproperties, "ToolTiers.TOOL"+raritytemp+toolvaluestemp+",", itemtypes, "SwordItem", modeltypes, "handheld")
        langAppend(langtags, "item", blockitems, name+"_sword")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["", "#", "", "", "#", "", "", "X", ""], input, ["mcinfini:"+name+suffix, "minecraft:stick"], output, name+"_sword", filename, name+"_sword")

        #Generate The Shovel
        choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'shovel'", "dark", "=", dark, "light", "=", light))[0]
        layerSpriteCreator(textureDirectory+"items/", name+"_shovel", hue, choice)

        initAppend(items, name+"_shovel", itemproperties, "ToolTiers.TOOL"+raritytemp+toolvaluestemp+",", itemtypes, "ShovelItem", modeltypes, "handheld")
        langAppend(langtags, "item", blockitems, name+"_shovel")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["", "#", "", "", "X", "", "", "X", ""], input, ["mcinfini:"+name+suffix, "minecraft:stick"], output, name+"_shovel", filename, name+"_shovel")

        #Generate The Hoe
        choice = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'hoe'", "dark", "=", dark, "light", "=", light))[0]
        layerSpriteCreator(textureDirectory+"items/", name+"_hoe", hue, choice)

        initAppend(items, name+"_hoe", itemproperties, "ToolTiers.TOOL"+raritytemp+toolvaluestemp+",", itemtypes, "HoeItem", modeltypes, "handheld")
        langAppend(langtags, "item", blockitems, name+"_hoe")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", "#", "", " ", "X", "", " ", "X", ""], input, ["mcinfini:"+name+suffix, "minecraft:stick"], output, name+"_hoe", filename, name+"_hoe")

        #Generate Armor
        #Generate The Helmet
        id1 = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'helmet'", "dark", "=", dark, "light", "=", light))[0]
        spriteCreator(textureDirectory+"items/", name+"_helmet", "item_sprites", hue, id1)

        initAppend(items, name+"_helmet", itemproperties, "ArmorTiers.ARMOR"+raritytemp+", EquipmentSlot.HEAD,", itemtypes, "ArmorItem", modeltypes, "generated")
        langAppend(langtags, "item", blockitems, name+"_helmet")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", "#", "#", "#", " ", "#", "", "", ""], input, ["mcinfini:"+name+suffix], output, name+"_helmet", filename, name+"_helmet")

        #Generate The Chestplate
        id2 =random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'chestplate'", "dark", "=", dark, "light", "=", light))[0]
        spriteCreator(textureDirectory+"items/", name+"_chestplate", "item_sprites", hue, id2)

        initAppend(items, name+"_chestplate", itemproperties, "ArmorTiers.ARMOR"+raritytemp+", EquipmentSlot.CHEST,", itemtypes, "ArmorItem", modeltypes, "generated")
        langAppend(langtags, "item", blockitems, name+"_chestplate")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", " ", "#", "#", "#", "#", "#", "#", "#"], input, ["mcinfini:"+name+suffix], output, name+"_chestplate", filename, name+"_chestplate")

        #Generate The Leggings
        id3 =random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'leggings'", "dark", "=", dark, "light", "=", light))[0]
        spriteCreator(textureDirectory+"items/", name+"_leggings", "item_sprites", hue, id3)

        initAppend(items, name+"_leggings", itemproperties, "ArmorTiers.ARMOR"+raritytemp+", EquipmentSlot.LEGS,", itemtypes, "ArmorItem", modeltypes, "generated")
        langAppend(langtags, "item", blockitems, name+"_leggings")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", "#", "#", "#", " ", "#", "#", " ", "#"], input, ["mcinfini:"+name+suffix], output, name+"_leggings", filename, name+"_leggings")

        #Generate The Boots
        id4 = random.choice(fetchResource3("item_sprites", "id", "tag", "=", "'boots'", "dark", "=", dark, "light", "=", light))[0]
        spriteCreator(textureDirectory+"items/", name+"_boots", "item_sprites", hue, id4)
        initAppend(items, name+"_boots", itemproperties, "ArmorTiers.ARMOR"+raritytemp+", EquipmentSlot.FEET,", itemtypes, "ArmorItem", modeltypes, "generated")
        langAppend(langtags, "item", blockitems, name+"_boots")
        craftAppend(count, 1, group, None, type, "crafting_shaped", grid, ["#", " ", "#", "#", " ", "#", "", "", ""], input, ["mcinfini:"+name+suffix], output, name+"_boots", filename, name+"_boots")

        ArmorSpriteCreator(textureDirectory+"models/armor/", name, hue, id1, id2, id3, id4)




    iteminit = [items, itemtypes, modeltypes, itemproperties]
    blockinit = [blocks, blockproperties, mineable, mineabletool]
    language = [langtags, blockitems]
    oregeneration = [ore, orebase, opv, vpc, loc, loc2]
    crafting = [count, group, type, grid, input, filename, output]

    batchbuild(directory, names, rarity, refinement, refinements, iteminit, blockinit, language, oregeneration, crafting)
    previous_ore = name

directory = "automatedMod/src/main/"

#newResource(directory, num, names, hues, effects, refinements)

#delete main directory and subdirectorie and files
try:
    shutil.rmtree(directory)
except OSError as e:
    #print("Error: %s - %s." % (e.filename, e.strerror))
    print("")
#create main directory and everything else
#newResource(directory, 6, ["oblium", "sublite", "rogline", "dawhil", "ospite", "truonor"], [150, 10, 90, 170, 70, 210], [None, None, None, None, None, None], [False, False, True, True, False, True])
newResource(directory, 1, ["oblium"], [150], [None], [False])

#build the mod
subprocess.run("D:/Coding/PersonalCode/MC/minecraftModAutomation/automatedMod/build.bat")
#copy the mod to a main folder.
shutil.copyfile('D:/Coding/PersonalCode/MC/minecraftModAutomation/automatedMod/build/libs/mcinfini-1.0.jar', 'D:/Coding/PersonalCode/MC/minecraftModAutomation/modExtracted/mcinfini.jar')