import os


def createdirectory(d):
    if not os.path.exists(d):
        os.makedirs(d)

def createfile(d):
    if not os.path.exists(d):
        file = open(d,'w+')
        file.close()

def createpackmcmeta(directory):
    createdirectory(directory + "resources/META-INF")
    file = open(directory + "resources/pack.mcmeta",'w+')
    filedata = '{\n' \
               '    "pack": {\n' \
               '        "description": "mcinfini resources",\n' \
               '        "pack_format": 9,\n' \
               '        "forge:resource_pack_format": 9,\n' \
               '        "forge:data_pack_format": 10\n' \
               '    }\n' \
               '}'
    file.write(filedata)
    file.close()
    print("Created the file pack.mcmeta")

def createmodstoml(directory):
    createdirectory(directory + "resources/META-INF")
    file = open(directory + "resources/META-INF/mods.toml",'w+')
    filedata = 'modLoader="javafml"\n' \
               'loaderVersion="[41,)"\n' \
               'license="All rights reserved"\n' \
               '[[mods]]\n' \
               'modId="mcinfini"\n' \
               'version="1.0"\n' \
               'displayName="Minecraft Infinite"\n' \
               'logoFile="examplemod.png"\n' \
               'credits="Massive thank you goes to all my patreons and supporters."\n' \
               'authors="Syrup"\n' \
               "description='''\n" \
               'An infinite content mod developed by Syrup.\n' \
               "'''\n"
    file.write(filedata)
    file.close()
    print("Created the file mods.toml")

def createMcInfini(directory, items):
    filedata = 'package dev.syrup.mcinfini;\n' \
               '\n' \
               'import dev.syrup.mcinfini.init.BlockInit;\n' \
               'import dev.syrup.mcinfini.init.ItemInit;\n' \
               'import dev.syrup.mcinfini.world.feature.ConfiguredFeatures;\n' \
               'import dev.syrup.mcinfini.world.feature.PlacedFeatures;\n' \
               '\n' \
               'import net.minecraft.world.item.CreativeModeTab;\n' \
               'import net.minecraft.world.item.ItemStack;\n' \
               'import net.minecraftforge.common.MinecraftForge;\n' \
               'import net.minecraftforge.eventbus.api.IEventBus;\n' \
               'import net.minecraftforge.fml.common.Mod;\n' \
               'import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;\n' \
               '\n' \
               '@Mod(McInfini.MOD_ID)\n' \
               'public class McInfini {\n' \
               '    public static final String MOD_ID = "mcinfini";\n' \
               '    public McInfini() {\n' \
               '        IEventBus bus = FMLJavaModLoadingContext.get().getModEventBus();\n' \
               '\n' \
               '        BlockInit.BLOCKS.register(bus);\n' \
               '        ItemInit.ITEMS.register(bus);\n' \
               '\n' \
               '        ConfiguredFeatures.register(bus);\n' \
               '        PlacedFeatures.register(bus);\n' \
               '\n' \
               '        MinecraftForge.EVENT_BUS.register(this);\n' \
               '    }\n' \
               '\n' \
               '    public static final CreativeModeTab TAB = new CreativeModeTab(MOD_ID) {\n' \
               '        @Override\n' \
               '        public ItemStack makeIcon(){\n' \
               '            return ItemInit.'+items[0].upper()+'.get().getDefaultInstance();\n' \
                                                               '        }\n' \
                                                               '    };\n' \
                                                               '}'
    createdirectory(directory + "java/dev/syrup/mcinfini")
    file = open(directory + "java/dev/syrup/mcinfini/McInfini.java", 'w+')
    file.write(filedata)
    file.close()
    print("Created the file McInfini.java")

def createItemInit(directory, names, rarity, refinements, items, itemtypes, itemproperties):
    filedata = 'package dev.syrup.mcinfini.init;\n' \
               'import dev.syrup.mcinfini.McInfini;\n' \
               'import dev.syrup.mcinfini.base.ModArmorMaterial;\n' \
               'import net.minecraft.sounds.SoundEvent;\n' \
               'import net.minecraft.sounds.SoundEvents;\n' \
               'import net.minecraft.world.effect.MobEffectInstance;\n' \
               'import net.minecraft.world.effect.MobEffects; \n' \
               'import net.minecraft.world.entity.EquipmentSlot;\n' \
               'import net.minecraft.world.food.FoodProperties;\n' \
               'import net.minecraft.world.item.*;\n' \
               'import net.minecraft.world.item.crafting.Ingredient;\n' \
               'import net.minecraftforge.common.ForgeTier;\n' \
               'import net.minecraftforge.registries.DeferredRegister;\n' \
               'import net.minecraftforge.registries.ForgeRegistries;\n' \
               'import net.minecraftforge.registries.RegistryObject;\n' \
               '\n' \
               'public class ItemInit {\n' \
               '    private static Item.Properties properties(){\n' \
               '        return new Item.Properties().tab(McInfini.TAB);\n' \
               '    }\n' \
               '    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, McInfini.MOD_ID);\n'
    for i in range(len(items)):
        filedata += '    public static final RegistryObject<'+itemtypes[i]+'> '+items[i].upper()+' = ITEMS.register("'+items[i]+'", () -> new '+itemtypes[i]+'('+itemproperties[i]+'properties()));\n'
    #Tool Tiers
    filedata += '\n' \
                '   public static class ToolTiers {\n' \
                '\n'

    for i in range(len(rarity)):
        filedata +='       public static final Tier TOOL'+rarity[i]+' = new ForgeTier('+str(1+i)+', '+str(64*(i+1))+', '+str((i+1)*2)+'f, '+str(i)+', '+str(5*(i+1))+', null, () -> Ingredient.of(ItemInit.'
        if refinements[i]:
            filedata += names[i].upper()+'_INGOT.get()));\n'
        else:
            filedata += names[i].upper()+'.get()));\n'
    filedata += '  }\n'
    #Armor Tiers
    filedata += '\n' \
                '   public static class ArmorTiers {\n' \
                '\n'

    for i in range(len(rarity)):
        filedata += '       public static final ArmorMaterial ARMOR'+rarity[i]+' = new ModArmorMaterial( "'+names[i]+'", '+str((i+1)*100)+', new int[] {'+str(i+1)+','+str(i+3)+','+str(i+2)+','+str(i+1)+'}, '+str(5*(i+1))+', SoundEvents.ARMOR_EQUIP_DIAMOND, 0.0f, 0.0f, () -> Ingredient.of(ItemInit.'
        if refinements[i]:
            filedata += names[i].upper()+'_INGOT.get()));\n'
        else:
            filedata += names[i].upper()+'.get()));\n'
    filedata += '  }\n}\n'

    createdirectory(directory + "java/dev/syrup/mcinfini/init")
    file = open(directory + "java/dev/syrup/mcinfini/init/ItemInit.java", 'w+')
    file.write(filedata)
    file.close()
    print("Created the file ItemInit.java")

def createBlockInit(directory, blocks, blockproperties):
    filedata = 'package dev.syrup.mcinfini.init;\n' \
               'import dev.syrup.mcinfini.McInfini;\n' \
               'import java.util.function.Function;\n' \
               'import java.util.function.Supplier;;\n' \
               'import net.minecraft.resources.ResourceLocation;\n' \
               'import net.minecraft.tags.BlockTags;\n' \
               'import net.minecraft.tags.ItemTags;\n' \
               'import net.minecraft.tags.TagKey;\n' \
               'import net.minecraft.world.item.BlockItem;\n' \
               'import net.minecraft.world.item.Item;\n' \
               'import net.minecraft.world.level.block.Block;\n' \
               'import net.minecraft.world.level.block.state.BlockBehaviour;\n' \
               'import net.minecraft.world.level.material.Material;\n' \
               'import net.minecraftforge.registries.DeferredRegister;\n' \
               'import net.minecraftforge.registries.ForgeRegistries;\n' \
               'import net.minecraftforge.registries.RegistryObject;\n' \
               '\n' \
               'public class BlockInit {\n' \
               '    private static <T extends Block> RegistryObject<T> register(String name, Supplier<T> supplier, Item.Properties properties){\n' \
               '        RegistryObject<T> block = BLOCKS.register(name, supplier);\n' \
               '        ItemInit.ITEMS.register(name, () -> new BlockItem(block.get(), properties));\n' \
               '        return block;\n' \
               '    }\n' \
               '    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, McInfini.MOD_ID);\n'

    for i in range(len(blocks)):
        filedata += '    public static final RegistryObject<Block> '+blocks[i].upper()+' = register("'+blocks[i]+'", () -> new Block(BlockBehaviour.Properties.of('+blockproperties[i]+'), new Item.Properties().tab(McInfini.TAB));\n'
    filedata += '}'
    createdirectory(directory + "java/dev/syrup/mcinfini/init")
    file = open(directory + "java/dev/syrup/mcinfini/init/BlockInit.java", 'w+')
    file.write(filedata)
    file.close()
    print("Created the file BlockInit.java")

def createModArmorMaterial(directory):
    filedata = 'package dev.syrup.mcinfini.base;\n' \
               'import dev.syrup.mcinfini.McInfini;\n' \
               'import net.minecraft.sounds.SoundEvent;\n' \
               'import net.minecraft.world.entity.EquipmentSlot;\n' \
               'import net.minecraft.world.item.ArmorMaterial;\n' \
               'import net.minecraft.world.item.crafting.Ingredient;\n' \
               '\n' \
               'import java.util.function.Supplier;\n' \
               '\n' \
               'public record ModArmorMaterial(String name, int durability, int[] protection, int enchantability, SoundEvent equipSound, float toughness, float knockbackResistance, Supplier<Ingredient> repairMaterial) implements ArmorMaterial {\n' \
               '    private static final int[] DURABILITY_PER_SLOT = new int[] {13, 15, 16, 11};\n' \
               '\n' \
               '    @Override\n' \
               '    public int getDurabilityForSlot(EquipmentSlot slot) { return DURABILITY_PER_SLOT[slot.getIndex()] * this.durability; }\n' \
               '\n' \
               '    @Override\n' \
               '    public int getDefenseForSlot(EquipmentSlot slot) { return this.protection[slot.getIndex()]; }' \
               '\n' \
               '    @Override\n' \
               '    public int getEnchantmentValue() { return this.enchantability; }' \
               '\n' \
               '    @Override\n' \
               '    public SoundEvent getEquipSound() { return this.equipSound; }' \
               '\n' \
               '    @Override\n' \
               '    public Ingredient getRepairIngredient() { return this.repairMaterial.get(); }' \
               '\n' \
               '    @Override\n' \
               '    public String getName() { return McInfini.MOD_ID + ":" + this.name; }' \
               '\n' \
               '    @Override\n' \
               '    public float getToughness() { return this.toughness; }' \
               '\n' \
               '    @Override\n' \
               '    public float getKnockbackResistance() { return this.knockbackResistance; }' \
               '}'
    createdirectory(directory + "java/dev/syrup/mcinfini/base")
    file = open(directory + "java/dev/syrup/mcinfini/base/ModArmorMaterial.java", 'w+')
    file.write(filedata)
    file.close()
    print("Created the file ModArmorMaterial.java")

def createblockstates(directory, blocks):
    createdirectory(directory + "resources/assets/mcinfini/blockstates")
    for i in range(len(blocks)):
        filedata = '{\n  "variants": {\n    "": {\n      "model": "mcinfini:block/'+blocks[i]+'"\n    }\n  }\n}'
        file = open(directory + "resources/assets/mcinfini/blockstates/"+blocks[i]+".json",'w')
        file.write(filedata)
        file.close()
    print("created "+blocks[i]+".json")

def createlang(directory, obj, tags): #Creates a file
    createdirectory(directory + "resources/assets/mcinfini/lang")
    filedata = '{\n  "itemGroup.mcinfini": "Mod Tab"'
    for i in range(len(obj)):
        name = obj[i].replace("_", " ")
        filedata += ',\n  "'+tags[i]+'.mcinfini.'+obj[i]+'": "'+name.title()+'"'
    filedata += '\n}'
    file = open(directory + "resources/assets/mcinfini/lang/en_us.json",'w+')
    file.write(filedata)
    file.close()
    print("Created the file en_us.json")

def createmodelblock(directory, all, name): #Creates a file
    createdirectory(directory + "resources/assets/mcinfini/models/block")
    if all:
        all = "cube_all"
    else:
        all = "cube_side" #IDK??????    WHAT IS IT??

    filedata = '{\n  "parent": "minecraft:block/'+all+'",\n  "textures": {\n    '
    filedata += '"all": "mcinfini:blocks/'+name+'"\n  }\n}'
    file = open(directory + "resources/assets/mcinfini/models/block/"+name+".json",'w')
    file.write(filedata)
    file.close()
    print("Created the file "+name+".json")

def createmodelitem(directory, tag, name): #Creates a file
    createdirectory(directory + "resources/assets/mcinfini/models/item")
    if tag == "block":
        filedata = '{\n  "parent": "mcinfini:block/'+name+'"\n}'
    else:
        filedata = '{\n  "parent": "minecraft:item/'+tag+'",\n  "textures": {\n    '
        filedata += '"layer0": "mcinfini:items/'+name+'"\n  }\n}'
    file = open(directory + "resources/assets/mcinfini/models/item/"+name+".json",'w')
    file.write(filedata)
    file.close()
    print("Created the file "+name+".json")

def createloottable(directory, refinement, tag, name):
    createdirectory(directory + "resources/data/mcinfini/loot_tables/blocks")
    if tag == "block":
        if name[-3:] == "ore":
            if refinement:
                filedata = '{\n  "type": "minecraft:block",\n  "pools": [\n    {\n      "rolls": 1,\n      "bonus_rolls": 0,\n      "entries": ['
                filedata += '\n        {\n          "type": "minecraft:item",\n          "name": "mcinfini:raw_'+name[:-4]+'"\n        }\n      ]\n    }\n  ]\n}'
            else:
                filedata = '{\n  "type": "minecraft:block",\n  "pools": [\n    {\n      "rolls": 1,\n      "bonus_rolls": 0,\n      "entries": ['
                filedata += '\n        {\n          "type": "minecraft:item",\n          "name": "mcinfini:'+name[:-4]+'"\n        }\n      ]\n    }\n  ]\n}'
        else:
            filedata = '{\n  "type": "minecraft:block",\n  "pools": [\n    {\n      "rolls": 1,\n      "bonus_rolls": 0,\n      "entries": ['
            filedata += '\n        {\n          "type": "minecraft:item",\n          "name": "mcinfini:'+name+'"\n        }\n      ]\n    }\n  ]\n}'

    else:
        print("not a block")
    file = open(directory + "resources/data/mcinfini/loot_tables/blocks/"+name+".json",'w')
    file.write(filedata)
    file.close()
    print("Created the file "+name+".json")

def createrecipes(directory, count, group, type, input, output, filename, grid):
    createdirectory(directory + "resources/data/mcinfini/recipes")
    if "crafting_shaped" == type:
        unique_key = []
        for i in range(len(grid)):
            if grid[i] not in unique_key and not "" == grid[i] and not " " == grid[i]:
                unique_key.append(grid[i])
        filedata = '{\n' \
                   '  "type": "minecraft:crafting_shaped",\n'
        if not None == group:
            filedata += '  "group": "'+group+'",\n'
        filedata +='  "pattern": [\n'
        if not "" == grid[0]+grid[1]+grid[2]:
            filedata += '    "'+grid[0]+grid[1]+grid[2]+'"'
        if not "" == grid[3]+grid[4]+grid[5]:
            filedata += ',\n    "'+grid[3]+grid[4]+grid[5]+'"'
        if not "" == grid[6]+grid[7]+grid[8]:
            filedata += ',\n    "'+grid[6]+grid[7]+grid[8]+'"'
        filedata +='\n  ],\n' \
                   '  "key": {\n'
        for i in range(len(unique_key)):
            filedata +='    "'+unique_key[i]+'": {\n' \
                                             '      "item": "'+input[i]+'"\n' \
                                                                        '    },\n'
        filedata = filedata[:-2]
        filedata +='\n  },\n' \
                   '' \
                   '  "result": {\n' \
                   '    "item": "mcinfini:'+ output +'",\n' \
                                                     '    "count": ' + str(count) + '\n' \
                                                                                    '  }\n' \
                                                                                    '}\n'
    elif "crafting_shapeless" == type:
        filedata = '{\n' \
                   '  "type": "minecraft:crafting_shapeless",\n'
        if not None == group:
            filedata += '  "group": "'+group+'",\n'
        filedata +='  "ingredients": [\n'
        for item in input:
            filedata +='    {\n' \
                       '      "item": "'+item+'"\n' \
                                              '    }\n'
        filedata +='  ],\n' \
                   '  "result": {\n' \
                   '    "item": "mcinfini:'+ output +'",\n' \
                                                     '      "count": ' + str(count) + '\n' \
                                                                                      '  }\n' \
                                                                                      '}\n'
    elif "smelting" == type:
        filedata = '{\n' \
                   '  "type": "minecraft:smelting",\n'
        if not None == group:
            filedata += '  "group": "'+group+'",\n'
        filedata +='  "ingredient": {\n' \
                   '    "item": "'+input[0]+'"\n' \
                                            '  },\n' \
                                            '  "result": "mcinfini:'+ output +'",\n' \
                                                                              '  "experience": 0.7,\n' \
                                                                              '  "cookingtime": 200\n' \
                                                                              '}\n'
    else:
        print("RECIPE ERROR!!")
    file = open(directory + "resources/data/mcinfini/recipes/"+filename+".json",'w')
    file.write(filedata)
    file.close()
    print("Created the file "+filename+".json")

def createmineable(directory, tag, name): #Creates a file
    createdirectory(directory + "resources/data/minecraft/tags/blocks/mineable")
    createfile(directory + "resources/data/minecraft/tags/blocks/mineable/"+tag+".json")
    file = open(directory + "resources/data/minecraft/tags/blocks/mineable/"+tag+".json",'r')
    filedata = file.read()
    file.close()
    if filedata == "":
        filedata = '{\n  "replace": false,\n  "values": [\n    "mcinfini:'+name+'"\n  ]\n}'
    else:
        filedata = filedata[:-7]
        filedata += '",\n    "mcinfini:'+name+'"\n  ]\n}'

    file = open(directory + "resources/data/minecraft/tags/blocks/mineable/"+tag+".json",'w')
    file.write(filedata)
    file.close()
    print("Created the file "+tag+".json")

def createneedtool(directory, req, name): #Creates a file
    if not req == None:
        createdirectory(directory + "resources/data/minecraft/tags/blocks")
        createfile(directory + "resources/data/minecraft/tags/blocks/needs_"+req+"_tool.json")
        file = open(directory + "resources/data/minecraft/tags/blocks/needs_"+req+"_tool.json",'r')
        filedata = file.read()
        file.close()
        if filedata == "":
            filedata = '{\n  "replace": false,\n  "values": [\n    "mcinfini:'+name+'"\n  ]\n}'
        else:
            filedata = filedata[:-7]
            filedata += '",\n    "mcinfini:'+name+'"\n  ]\n}'

        file = open(directory + "resources/data/minecraft/tags/blocks/needs_"+req+"_tool.json",'w')
        file.write(filedata)
        file.close()
        print("Created the file needs_"+req+"_tool.json")

def createconfiguredfeatures(directory, opv, loc, ore, block, block2=None, loc2=None): #Creates a file
    for i in range(len(loc)):
        loc[i] = loc[i].upper()
        ore[i] = ore[i].upper()
        block[i] = block[i].upper()
    #        block2[i] = block2[i].upper()

    createdirectory(directory + "java/dev/syrup/mcinfini/world/feature/")
    file = open(directory + "java/dev/syrup/mcinfini/world/feature/ConfiguredFeatures.java",'w+')
    filedata = 'package dev.syrup.mcinfini.world.feature;\n' \
               '\n' \
               'import dev.syrup.mcinfini.McInfini;\n' \
               'import dev.syrup.mcinfini.init.BlockInit;\n' \
               '\n' \
               'import com.google.common.base.Supplier;\n' \
               'import com.google.common.base.Suppliers;\n' \
               'import net.minecraft.core.Registry;\n' \
               'import net.minecraft.data.worldgen.features.OreFeatures;\n' \
               'import net.minecraft.world.level.block.Blocks;\n' \
               'import net.minecraft.world.level.levelgen.feature.ConfiguredFeature;\n' \
               'import net.minecraft.world.level.levelgen.feature.Feature;\n' \
               'import net.minecraft.world.level.levelgen.feature.configurations.OreConfiguration;\n' \
               'import net.minecraft.world.level.levelgen.structure.templatesystem.BlockMatchTest;\n' \
               'import net.minecraftforge.eventbus.api.IEventBus;\n' \
               'import net.minecraftforge.registries.DeferredRegister;\n' \
               'import net.minecraftforge.registries.RegistryObject;\n' \
               '\n' \
               'import java.util.List;\n' \
               '\n' \
               'public class ConfiguredFeatures {\n' \
               '    public static void register(IEventBus eventBus) { CONFIGURED_FEATURES.register(eventBus); }\n' \
               '\n' \
               '    public static final DeferredRegister<ConfiguredFeature<?, ?>> CONFIGURED_FEATURES =\n' \
               '            DeferredRegister.create(Registry.CONFIGURED_FEATURE_REGISTRY, McInfini.MOD_ID);\n' \
               '\n'

    for i in range(len(ore)):
        filedata += '    public static final Supplier<List<OreConfiguration.TargetBlockState>> '+loc[i]+'_'+ore[i]+' = Suppliers.memoize(() -> List.of(\n' \
                                                                                                                   '            OreConfiguration.target(new BlockMatchTest(Blocks.'+block[i]+'), BlockInit.'+ore[i]+'.get().defaultBlockState())));\n'
        #    if block2[i] != None:
        #        filedata += '            OreConfiguration.target(OreFeatures.'+block2[i]+'_ORE_REPLACEABLES, BlockInit.'+ore[i]+'.get().defaultBlockState())));\n' \
        #                '            OreConfiguration.target(new BlockMatchTest(Blocks.'+loc2[i]+'), BlockInit.'+loc2[i]+'_'+ore[i]+'.get().defaultBlockState())));'
        #
        filedata +='\n' \
                   '    public static final RegistryObject<ConfiguredFeature<?, ?>> '+ore[i]+' = CONFIGURED_FEATURES.register("'+ore[i].lower()+'",\n' \
                                                                                                                                                '            () -> new ConfiguredFeature<>(Feature.ORE, new OreConfiguration('+loc[i]+'_'+ore[i]+'.get(),'+str(opv[i])+')));//BlocksPerVein\n' \
                                                                                                                                                                                                                                                                       '\n'
    filedata +='}\n'
    file.write(filedata)
    file.close()
    print("Created the file ConfiguredFeatures.java")

def createplacedfeatures(directory, vpc, ore, loc2): #Creates a file
    for i in range(len(ore)):
        ore[i] = ore[i].upper()

    createdirectory(directory + "java/dev/syrup/mcinfini/world/feature/")
    file = open(directory + "java/dev/syrup/mcinfini/world/feature/PlacedFeatures.java",'w+')
    filedata = 'package dev.syrup.mcinfini.world.feature;\n' \
               '\n' \
               'import dev.syrup.mcinfini.McInfini;\n' \
               '\n' \
               'import net.minecraft.core.Registry;\n' \
               'import net.minecraft.world.level.levelgen.VerticalAnchor;\n' \
               'import net.minecraft.world.level.levelgen.placement.*;\n' \
               'import net.minecraftforge.eventbus.api.IEventBus;\n' \
               'import net.minecraftforge.registries.DeferredRegister;\n' \
               'import net.minecraftforge.registries.RegistryObject;\n' \
               '\n' \
               'import java.util.List;\n' \
               '\n' \
               'public class PlacedFeatures {\n' \
               '\n' \
               '    public static final DeferredRegister<PlacedFeature> PLACED_FEATURES =\n' \
               '            DeferredRegister.create(Registry.PLACED_FEATURE_REGISTRY, McInfini.MOD_ID);\n' \
               '\n' \
               '    public static List<PlacementModifier> orePlacement(PlacementModifier p_195347_, PlacementModifier p_195348_) {\n' \
               '        return List.of(p_195347_, InSquarePlacement.spread(), p_195348_, BiomeFilter.biome());\n' \
               '    }\n' \
               '\n' \
               '    public static List<PlacementModifier> commonOrePlacement(int p_195344_, PlacementModifier p_195345_) {\n' \
               '        return orePlacement(CountPlacement.of(p_195344_), p_195345_);\n' \
               '    }\n' \
               '\n' \
               '    public static List<PlacementModifier> rareOrePlacement(int p_195350_, PlacementModifier p_195351_) {\n' \
               '        return orePlacement(RarityFilter.onAverageOnceEvery(p_195350_), p_195351_);\n' \
               '    }\n' \
               '\n' \
               '    public static void register(IEventBus eventBus) {\n' \
               '        PLACED_FEATURES.register(eventBus);\n' \
               '    }\n' \
               '\n'
    for i in range(len(ore)):
        filedata += '    public static final RegistryObject<PlacedFeature> '+ore[i]+'_PLACED = PLACED_FEATURES.register("'+ore[i].lower()+'_placed",\n' \
                                                                                                                                          '            () -> new PlacedFeature(ConfiguredFeatures.'+ore[i]+'.getHolder().get(),\n' \
                                                                                                                                                                                                           '                    commonOrePlacement('+str(vpc[i])+', // VeinsPerChunk\n' \
                                                                                                                                                                                                                                                                 '                            HeightRangePlacement.triangle(VerticalAnchor.absolute('+str(loc2[i]-20)+'), VerticalAnchor.absolute('+str(loc2[i]+20)+')))));\n'
    filedata +='}\n'
    file.write(filedata)  #vpc[i]
    file.close()
    print("Created the file PlacedFeatures.java")

def createaddore(directory,ore,loc,mod="minecraft"):
    #ore should be like so: "iron_ore"
    #loc should be one of the following "overworld", "nether", "end"
    createdirectory(directory + "resources/data/mcinfini/forge/biome_modifier")
    file = open(directory + "resources/data/mcinfini/forge/biome_modifier/add_"+ore.lower()+".json",'w+')
    filedata = '{\n' \
               '  "type": "forge:add_features",\n' \
               '  "biomes": "#'+mod.lower()+':is_'+loc.lower()+'",\n' \
                                                               '  "features": "mcinfini:'+ore.lower()+'_placed",\n' \
                                                                                                      '  "step": "underground_ores"\n' \
                                                                                                      '}'
    file.write(filedata)
    file.close()
    print("Created the file add_"+ore.lower()+".json")



def batchbuild(directory, names, rarity, refinement, refinements, iteminit, blockinit, language, oregeneration, crafting):

    items, itemtypes, modeltypes, itemproperties = iteminit[0], iteminit[1], iteminit[2], iteminit[3]
    blocks, blockproperties, mineable, mineabletool = blockinit[0], blockinit[1], blockinit[2], blockinit[3]
    langtags, blockitems = language[0], language[1]
    ore, orebase, opv, vpc, loc, loc2 = oregeneration[0], oregeneration[1], oregeneration[2], oregeneration[3], oregeneration[4], oregeneration[5]
    count, group, type, grid, input, filename, output = crafting[0], crafting[1], crafting[2], crafting[3], crafting[4], crafting[5], crafting[6]




    #create mods.toml
    createmodstoml(directory)

    #create pack.mcmeta
    createpackmcmeta(directory)

    #create McInfini.java
    createMcInfini(directory, items)

    #create ItemInit.java
    print("create ItemInit.java")
    createItemInit(directory, names, rarity, refinements, items, itemtypes, itemproperties)

    #create BlockInit.java
    print("create BlockInit.java")
    createBlockInit(directory, blocks, blockproperties)

    #create ModArmorMaterial.java
    print("create ModArmorMaterial.java")
    createModArmorMaterial(directory)

    #create ConfiguredFeatures.java
    print("create ConfiguredFeatures.java")
    createconfiguredfeatures(directory, opv, loc, ore, orebase)

    #create PlacedFeatures.java
    print("create PlacedFeatures.java")
    createplacedfeatures(directory, vpc, ore, loc2)

    #create blockstates
    createblockstates(directory, blocks)

    #create lang
    createlang(directory, blockitems, langtags)

    #create models block
    for i in blocks:
        createmodelblock(directory, True, i)

    #create models item
    for i in range(len(blockitems)):
        createmodelitem(directory, modeltypes[i], blockitems[i])

    #create loot_tables
    for i in blocks:
        createloottable(directory, refinement, "block", i)

    #create recipes
    for i in range(len(count)):
        createrecipes(directory, count[i], group[i], type[i], input[i], output[i], filename[i], grid[i])

    #create tool.json
    for i in range(len(mineable)):
        createmineable(directory, mineable[i], blocks[i])

    #create needs_blank_tool.json
    for i in range(len(mineabletool)):
        createneedtool(directory, mineabletool[i], blocks[i])

    #create add_ore.json
    for i in range(len(ore)):
        createaddore(directory,ore[i],loc[i])


