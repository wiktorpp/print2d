from printBmp import *
import colorsys
import time
import signal

try:
    while True:
        for i in range(100): 
            time.sleep(0.03)
            color = colorsys.hsv_to_rgb(i/100,1,1)
            color = (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
            print(f"{esc}[D" + pixelsToAnsi((color, color)), end="", flush=True)
except:
    print(reset)