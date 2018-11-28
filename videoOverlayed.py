#! /usr/bin/env python3

import numpy as np
import os
import glob
import argparse
import re
import matplotlib.pyplot as plt
import cv2


def sorted_alphanumeric(data):
    def convert(text): return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


imgray = ""
imcolor = ""
output = ""

parser = argparse.ArgumentParser(description="Process Images Post Deep")
parser.add_argument('-g', '--imgray', default=imgray)
parser.add_argument('-c', '--imcolor', default=imcolor)
parser.add_argument('-o', '--output', default=output)
args = parser.parse_args()

imgray = str(args.imgray)
imcolor = str(args.imcolor)
output = str(args.output)

list_gray = os.listdir(imgray)
list_color = os.listdir(imcolor)

# assert len(list_gray) == len(list_color)

for i, (gray, color) in enumerate(zip(sorted_alphanumeric(list_gray), sorted_alphanumeric(list_color))):
    path_gray = imgray + gray
    path_color = imcolor + color
    image_gray = cv2.imread(path_gray)
    image_color = cv2.imread(path_color)
    sizes = image_gray.shape
    image_color = cv2.resize(image_color, dsize=(sizes[1], sizes[0]),
                             interpolation=cv2.INTER_CUBIC)
    output_image = cv2.addWeighted(image_gray, 1.0, image_color, 0.4, 0.0)

    cv2.imwrite(os.path.join(output, 'img_'+str(i)+'.png'), output_image)
