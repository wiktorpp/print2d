import os
import sys
esc = chr(0x1B)

blockGraphics = {
    (False, False): " ", 
    (False, True): "▄",
    (True, False): "▀",
    (True, True): "█"
}

"""
def setColorFg(color):
    return f"{esc}[38;2;{color[0]};{color[1]};{color[2]}m"

def setColorBg(color):
    return f"{esc}[48;2;{pixelEven[0]};{pixelEven[1]};{pixelEven[2]}m"
"""

blockGraphicsColor = {
    (False, False): 
        f"{chr(0x1B)}[0m ", 
    (False, True): 
        f"{chr(0x1B)}[49m{chr(0x1B)}[38;2;{{pixels[1][0]}};{{pixels[1][1]}};{{pixels[1][2]}}m▄",
    (True, False): 
        f"{chr(0x1B)}[38;2;{{pixels[0][0]}};{{pixels[0][1]}};{{pixels[0][2]}}m{chr(0x1B)}[49m▀",
    (True, True): 
        f"{chr(0x1B)}[48;2;{{pixels[0][0]}};{{pixels[0][1]}};{{pixels[0][2]}}m{chr(0x1B)}[38;2;{{pixels[1][0]}};{{pixels[1][1]}};{{pixels[1][2]}}m▄"
}

def pixelsToAnsi(pixels=(0,0)):
    try:
        return blockGraphicsColor[pixels[0] != False, pixels[1] != False].format(pixels=pixels)
    except TypeError:
        return blockGraphics[pixels[0] != False, pixels[1] != False]

reset = f"{chr(0x1B)}[0m"

def bmpToAnsi(bmp):
    size = (
        len(bmp),
        max(map(len, bmp))
    )
    
    #print(size)

    out = ""
    for row in range(0, size[0], 2):
        for col in range(size[1]):
            #print(f"{row} {col} {row + 1} {col}")
            try:
                out += pixelsToAnsi((bmp[row][col], bmp[row + 1][col]))
            except IndexError:
                out += pixelsToAnsi((bmp[row][col], 0))
        out += f"{reset}\n"
    return out

def printBmp(bmp):
    print(bmpToAnsi(bmp))
