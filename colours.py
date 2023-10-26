BLACK   = (   0,   0,   0)
GREY    = ( 127, 127, 127)
WHITE   = ( 255, 255, 255)
RED     = ( 255,   0,   0)
GREEN   = (   0, 255,   0)
BLUE    = (   0,   0, 255)
YELLOW  = ( 255, 255,   0)
AQUA    = (   0, 255, 255)
PURPLE  = ( 255,   0, 255)

LIGHT_RED   = (255, 179, 179)
DARK_RED    = (139,   0,   0)

LIGHT_PAPER = ( 248, 236, 194)
PAPER       = ( 228, 216, 174)
DARK_PAPER  = ( 208, 196, 154)

##def colourCorrection(rgb):      # Removes numbers >255 & <0 from rbg colour arrays
##    newRBG = [rgb[0],rgb[1],rgb[2]]
##    if newRBG[0] < 0:
##        newRBG[0] = 0
##    elif newRBG[0] > 255:
##        newRBG[0] = 255
##    if newRBG[1] < 0:
##        newRBG[1] = 0
##    elif newRBG[1] > 255:
##        newRBG[1] = 255
##    if newRBG[2] < 0:
##        newRBG[2] = 0
##    elif newRBG[2] > 255:
##        newRBG[2] = 255
##    return newRBG
##
##def colourChanger(rgb, x):       # Alters all values from rbg colour arrays by a set amount
##    newR = rgb[0] + x
##    newG = rgb[1] + x
##    newB = rgb[2] + x
##    newRBG = colourCorrection([newR,newG,newB])
##    return newRBG
##
##def light(rbg):
##    return colourChanger(rbg, 127)
