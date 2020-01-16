# Write list and form csv
# args: <data_dir1> <method1> <data_dir2> <method2> <output_file>
import os
import glob
import sys
import csv
import numpy as np

lists = [[], []]
styles = ["starrynight", "lamuse", "feathers", "composition"]
base_url = "https://raw.githubusercontent.com/AtlantixJJ/VideoStableData/master/"

def get_url_list(data_dir, method):
    mp4list = glob.glob(data_dir + "/*.mp4")
    l = []
    for m in mp4list:
        if method not in m: continue
        for s in styles:
            if s in m:
                l.append(base_url + m)
    return l

lists = [
  get_url_list(sys.argv[1], sys.argv[2]),
  get_url_list(sys.argv[3], sys.argv[4])]

for l in lists: l.sort()
print(lists[0][:10], lists[1][:10])
# form pair
def add_pair_from_list(list1, list2):
    pair = []
    for l1, l2 in zip(list1, list2):
        pair.append((l1, l2))
    return pair

tot_pair = []

for i in range(len(lists[0])):
    tot_pair.append((lists[0][i], lists[1][i]))

#tot_pair.extend(add_pair_from_list(ctrl_lists[0], ctrl_lists[1]))

# swith pair
for i in range(len(tot_pair)):
    if np.random.uniform() < 0.5:
        tot_pair[i] = tot_pair[i][1], tot_pair[i][0]

# shuffle order
s = np.random.RandomState(1092411)
s.shuffle(tot_pair)

out = open(sys.argv[3], 'w')
csv_writer = csv.writer(out, dialect='excel')
header = ["video_A_url", "video_B_url"]
csv_writer.writerow(header)

for p in tot_pair:
    csv_writer.writerow(p)
