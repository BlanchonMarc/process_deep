#! /usr/bin/env python3

import numpy as np
import os
import glob
import argparse
import re


def sorted_alphanumeric(data):
    def convert(text): return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key): return [convert(c)
                                   for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


gt_path = ""
pred_path = ""
visualize = False
save = False
colorMap =

parser = argparse.ArgumentParser(description="Process Images Post Deep")
parser.add_argument('-g', '--gt_path', default=gt_path)
parser.add_argument('-p', '--pred_path', default=pred_path)
parser.add_argument('-v', '--visualize', action='store_true')
parser.add_argument('-s', '--save', action='store_true')
args = parser.parse_args()

gt_path = str(args.gt_path)
pred_path = str(args.pred_path)
visualize = args.visualize
save = args.save

if visualize:
    import matplotlib.pyplot as plt
    plt.close('all')

list_gt = os.listdir(gt_path)
list_pred = os.listdir(pred_path)

assert len(list_gt) == len(list_pred)

for gt, pred in zip(sorted_alphanumeric(list_gt), sorted_alphanumeric(list_pred)):
    pass
