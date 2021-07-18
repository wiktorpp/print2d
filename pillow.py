from PIL import Image
import sys
im = Image.open(sys.argv[1])
width, height = im.size
px = im.load()

print("[", end="")
for i in range(height):
    print("[", end="")
    for j in range(width):
        print(str(px[j,i]) + ", ", end="")
    print("],")
print("]", end="")