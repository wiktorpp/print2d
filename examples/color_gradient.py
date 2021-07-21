from printBmp import *
import colorsys
import os
terminal_size = os.get_terminal_size()
print(terminal_size.columns)
for i in range(terminal_size.lines):
    for i in range(os.get_terminal_size().columns): 
        color = colorsys.hsv_to_rgb(i/100,1,1)
        color = (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
        print(pixelsToAnsi((color, color)), end="")
    print(reset)