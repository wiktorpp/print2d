from PIL import Image
import sys

monochrome = False

im = Image.open(sys.argv[1])
width, height = im.size
if monochrome:
    im = im.convert("L")
px = im.load()
try:
    trIm = Image.open(sys.argv[2])
except:
    tr = False
else:
    width, height = trIm.size
    trIm = trIm.convert("L")
    trPx = trIm.load()
    tr = True

bmp = []
for i in range(height):
    row = []
    for j in range(width):
        if monochrome:
            if px[j,i] == 255:
                row.append(1)
            else:
                row.append(0)
        elif tr and trPx[j, i] == 0:
            row.append(0)
        else:
            row.append(px[j,i])
    bmp.append(row)

try:
    from printBmp import bmpToAnsi
    output = bmpToAnsi(bmp)
    print(output)
except:
    raise Exception