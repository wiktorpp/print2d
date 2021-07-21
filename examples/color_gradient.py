from printBmp import *
import colorsys

for i in range(100): 
    color = colorsys.hsv_to_rgb(i/100,1,1)
    color = (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
    print(pixelsToAnsi((color, color)), end="")
print(reset)