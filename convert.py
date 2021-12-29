from PIL import Image
import sys

monochrome = False

try: 
    imageFilename = sys.argv[1]
except:
    print("usage: ./convert.py <image> [transparency] > <output>")
    exit()

image = Image.open(imageFilename)
width, height = image.size
if monochrome:
    image = image.convert("L")
pixelmap = image.load()
try:
    transparencyImage = Image.open(sys.argv[2])
except:
    transparency = False
else:
    transparencyImage = transparencyImage.convert("L")
    transparencyPixelmap = transparencyImage.load()
    transparency = True

bmp = []
for i in range(height):
    row = []
    for j in range(width):
        if monochrome:
            if pixelmap[j,i] == 255:
                row.append(1)
            else:
                row.append(0)
        elif transparency and transparencyPixelmap[j, i] == 0:
            row.append(0)
        else:
            row.append(pixelmap[j,i])
    bmp.append(row)

from printBmp import bmpToAnsi
output = bmpToAnsi(bmp)
print(output, end="")