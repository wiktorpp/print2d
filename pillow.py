from PIL import Image
import sys
im = Image.open(sys.argv[1])
width, height = im.size
px = im.load()
if len(sys.argv) == 3:
    trIm = Image.open(sys.argv[2])
    width, height = trIm.size
    trIm = trIm.convert("L")
    trPx = trIm.load()
    tr = True
else:
    tr = False

print("[", end="")
for i in range(height):
    print("[", end="")
    for j in range(width):
        if tr and trPx[j, i] == 0:
            print("0, ", end="")
        else:
            print(str(px[j,i]) + ", ", end="")
    print("],")
print("]", end="")
#import pdb; pdb.set_trace()