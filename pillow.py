from PIL import Image
import sys

monochrome = False

im = Image.open(sys.argv[1])
width, height = im.size
if monochrome:
    im = im.convert("L")
px = im.load()
if len(sys.argv) == 3:
    trIm = Image.open(sys.argv[2])
    width, height = trIm.size
    trIm = trIm.convert("L")
    trPx = trIm.load()
    tr = True
else:
    tr = False

out = ""
out += "["
for i in range(height):
    out += "["
    for j in range(width):
        if monochrome:
            if px[j,i] == 255:
                out += "1, "
            else:
                out += "0, "
        elif tr and trPx[j, i] == 0:
            out += "0, "
        else:
            out += str(px[j,i]) + ", "
    out += "],\n"
out += "]"
print(out)
#import pdb; pdb.set_trace()