import cv2
import numpy as np

from dataManagement import fetchResource1


# spriteCreator("////////textures/blocks", "diamond", "_ore", "block_sprites", 20, 5, raw
def spriteCreator(dir, name, database, hue, id):
    rgba = recolor(hue, database, "image", id)
    print("generated: " + name + ".png")

    cv2.imwrite(dir + name + ".png", rgba)
    return rgba
def oreSpriteCreator(dir, name, hue, oreid, baseid):
    ore = recolor(hue, "block_sprites", "image", oreid)
    block = np.array(fetchResource1("block_sprites", "image", "id", "=", baseid)[0][0], dtype='uint8')
    rgba = np.empty((16, 16, 4), dtype=int)
    for i in range(16):
        for j in range(16):
            if ore[i][j][3] == 0:
                rgba[i][j] = block[i][j]
            else:
                rgba[i][j] = ore[i][j]
    print("generated: " + name + "_ore.png")

    cv2.imwrite(dir+name+"_ore.png", rgba)
    return rgba
def layerSpriteCreator(dir, name, hue, id):
    layer1 = recolor(hue, "item_sprites", "image", id)
    layer2 = np.array(fetchResource1("item_sprites", "imagelayer1", "id", "=", id)[0][0], dtype='uint8')
    rgba = np.empty((16, 16, 4), dtype=int)
    for i in range(16):
        for j in range(16):
            if layer1[i][j][3] == 0:
                rgba[i][j] = layer2[i][j]
            else:
                rgba[i][j] = layer1[i][j]
    print("generated: " + name + ".png")

    cv2.imwrite(dir+name+".png", rgba)
    return rgba
def ArmorSpriteCreator(dir, name, hue, id, id2, id3, id4):
    layer1 = recolor(hue, "item_sprites", "imagelayer1", id)  #helmet
    layer2 = recolor(hue, "item_sprites", "imagelayer1", id2) #chestplate
    layer3 = recolor(hue, "item_sprites", "imagelayer1", id3) #leggings #solo
    layer4 = recolor(hue, "item_sprites", "imagelayer1", id4) #boots
    rgba = np.empty((32, 64, 4), dtype=int)
    for i in range(32):
        for j in range(64):
            if layer1[i][j][3] == 0:
                if layer2[i][j][3] == 0:
                    rgba[i][j] = layer4[i][j]
                else:
                    rgba[i][j] = layer2[i][j]
            else:
                rgba[i][j] = layer1[i][j]

    print("generated: " + name + "_layer_1.png")
    cv2.imwrite(dir+name+"_layer_1.png", rgba)
    print("generated: " + name + "_layer_2.png")
    cv2.imwrite(dir+name+"_layer_2.png", layer3)

def recolor(hue, database, column, id):
    """

    :param hue: the color change of the sprite
    :param id: The id image used for recoloring (?)
    """

    image = np.array(fetchResource1(database, column, "id", "=", id)[0][0], dtype='uint8')

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    hsv[:, :, 0] = hue
    hsv[:, :, 1] = 250

    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR_FULL)
    #prevents transparent pixels from going black
    if image[0][0].shape[0] == 4:
        rgba = np.empty((image.shape[0], image[0].shape[0], 4), dtype='uint8')
        for i in range(image.shape[0]):
            for j in range(image[0].shape[0]):
                if image[i][j][3] == 0:
                    rgba[i][j] = np.append(rgb[i][j], 0)
                else:
                    rgba[i][j] = np.append(rgb[i][j], image[i][j][3])
        #    fileN = "D:\\Coding\\PersonalCode\\MC\\GeneratedSprites\\a_trial.png"
        #    cv2.imwrite(fileN, rgba)
        return rgba
    else:
        return rgb



#HUE RED  ORANGE YELLOW   LIME  GREEN   TEAL   CYAN   BLUE   DEEP BLUE DEEPERBLUEple  PURPLE   MAGENTA   PINK   REDDERPINK
#     0     20     40      60     80    100     120    140      160         180        190       200      220        240


