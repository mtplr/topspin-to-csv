"""
Created by Matteo Paolieri
University of Cologne 2021

MIT LICENSE

A simple script to export topspin raw .txt data to csv
to be plotted elsewhere
"""


#!/usr/bin/env python3


import argparse
import re
import numpy as np 


parser = argparse.ArgumentParser(description="Input: topspinfile.txt")

parser.add_argument('--filename', '-f', type=str,
                    help='Input file name.')

args = parser.parse_args()

# read it

y = []

with open(args.filename) as f:
      
    for i in range (3):  
        f.readline()
    
    txt = f.readline()
    leftright = re.findall(r"(?<![a-zA-Z:])[-+]?\d*\.?\d+",txt)
    f.readline()
    txt = f.readline()
    
    for i in range (4):  
        f.readline()
    
    while True:
        l = f.readline()
        if not l:
            break
        y.append(float(l))

size = int([int(s) for s in txt.split() if s.isdigit()][0])

left = float(leftright[0])
right = float(leftright[1])
step = -(left-right)/size

# generate sequence 

x = np.arange(left, right, step).tolist()

# write a new file

out = args.filename[:-4]+".csv"

with open(out, 'w') as f:
    for i in range(0, size):
        print(f'{x[i]},{y[i]}', file=f)
