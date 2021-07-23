import os
import sys

class ansi:
    esc = chr(0x1B)
    fg = f"{esc}[38;2;{{r}};{{g}};{{b}}m"
    bg = f"{esc}[48;2;{{r}};{{g}};{{b}}m"
    def setFg(r, g, b): return ansi.fg.format(r=r, g=g, b=b)
    def setBg(r, g, b): return ansi.bg.format(r=r, g=g, b=b)
    reset = f"{esc}[0m"
    resetFg = f"{esc}[39m"
    resetBg = f"{esc}[49m"

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
        f"{chr(0x1B)}[49m{chr(0x1B)}[38;2;{{pixelPair[1][0]}};{{pixelPair[1][1]}};{{pixelPair[1][2]}}m▄",
    (True, False): 
        f"{chr(0x1B)}[38;2;{{pixelPair[0][0]}};{{pixelPair[0][1]}};{{pixelPair[0][2]}}m{chr(0x1B)}[49m▀",
    (True, True): 
        f"{chr(0x1B)}[48;2;{{pixelPair[0][0]}};{{pixelPair[0][1]}};{{pixelPair[0][2]}}m{chr(0x1B)}[38;2;{{pixelPair[1][0]}};{{pixelPair[1][1]}};{{pixelPair[1][2]}}m▄"
}

def pixelsToAnsi(pixelPair=(0,0)):
    #pixelPairVisibility
    try:
        return blockGraphicsColor[pixelPair[0] != False, pixelPair[1] != False].format(pixelPair=pixelPair)
    except TypeError:
        return blockGraphics[pixelPair[0] != False, pixelPair[1] != False]

def bmpToAnsi(bmp, returnList=False):
    size = (
        len(bmp),
        max(map(len, bmp))
    )

    out = []
    for rowIndex in range(0, size[0], 2):
        row = []
        for colIndex in range(size[1]):
            try:
                row.append(pixelsToAnsi((bmp[rowIndex][colIndex], bmp[rowIndex + 1][colIndex])))
            except IndexError:
                row.append(pixelsToAnsi((bmp[rowIndex][colIndex], 0)))
        row.append(f"{chr(0x1B)}[0m\n")
        out.append(row)

    if returnList:
        return out
    else:
        return "".join(sum(out, []))

def printBmp(bmp):
    print(bmpToAnsi(bmp))