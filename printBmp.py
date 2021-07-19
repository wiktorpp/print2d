import os
import sys
esc = chr(0x1B)

blockGraphics = {
    (False, False): " ", 
    (False, True): "▄",
    (True, False): "▀",
    (True, True): "█"
}

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

def bmpToAnsi(bmp):
    size = (
        len(bmp),
        max(map(len, bmp))
    )

    out = ""
    for row in range(0, size[0], 2):
        for col in range(size[1]):
            try:
                out += pixelsToAnsi((bmp[row][col], bmp[row + 1][col]))
            except IndexError:
                out += pixelsToAnsi((bmp[row][col], 0))
        out += f"{chr(0x1B)}[0m\n"
    return out

def printBmp(bmp):
    print(bmpToAnsi(bmp))
