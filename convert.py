from PIL import Image
import sys

monochrome = False

try: 
    imageFilename = sys.argv[1]
except:
    print("usage: ./convert.py <image> [transparency] [raw|python|hex|base64|bz2|...] > [output]")
    exit()

image = Image.open(imageFilename)
width, height = image.size
if monochrome:
    image = image.convert("L")
pixelmap = image.load()
try:
    transparencyImage = Image.open(sys.argv[2])
except IndexError:
    transparency = False
except FileNotFoundError:
    transparency = False
    sys.stderr.write("Invalid transparency layer, ignoring.\n")
    sys.stderr.flush()
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
try: encoding = sys.argv[3]
except IndexError:
    print(output, end="")
else:
    if encoding == "raw":
        print(output, end="")
    elif encoding == "python":
        from codecs import encode
        sys.stdout.buffer.write(encode(output, "unicode_escape")+b"\n")
    else:
        from codecs import encode
        try:
            output = encode(output.encode('utf-8'), encoding)
        except TypeError:
            output = encode(output, encoding)
        sys.stdout.buffer.write(output)
