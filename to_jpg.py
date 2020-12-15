import os
import sys
from PIL import Image

#A simple script that takes an image as an input and convert it into ".jpg"

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        img = Image.open(sys.argv[1])
        img_name = sys.argv[1] + ".jpg"
        rgb_img = img.convert('RGB')
        rgb_img.save(img_name)
        print("Saved as " + img_name)
    else:
        print(sys.argv[1] + " is not found")
else:
    print("Write: to_jpg.py _filename_")