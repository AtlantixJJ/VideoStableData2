"""
Mix a few csv files
"""
import os, sys
import numpy as np
rng = np.random.RandomState(1)
csvfiles = [open(f) for f in sys.argv[1].split(",")]
lines = [f.readlines() for f in csvfiles]
header = lines[0][0]
newlines = []
for i in range(len(lines)):
  newlines.extend(lines[i][1:])
rng.shuffle(newlines)
f = open(sys.argv[2], "w")
f.write(header)
for l in newlines:
  f.write(l)
