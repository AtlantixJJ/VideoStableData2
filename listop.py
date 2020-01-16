# Write list and form csv
# args: <data_dir1> <data_dir2> 
import os
import glob
import sys
import csv
import numpy as np

base_url = "https://raw.githubusercontent.com/AtlantixJJ/VideoStableData/master/"
#base_url = "static/"

def get_model(s):
    models = ["sfn", "adain", "rnn"] # msra is compared within loss content
    for m in models:
        if m in s:
            return m
    return 0

def get_loss(s):
    losses = ["msra", "diff", "flow", "comb", "none"]
    for m in losses:
        if m in s:
            return m
    return 0

def get_ref_image(url):
    image_url = base_url + "image/"
    if "starrynight" in url:
        image_url += "starry_night.jpg"
    elif "lamuse" in url:
        image_url += "la_muse.jpg"
    elif "feathers" in url:
        image_url += "feathers.jpg"
    elif "composition" in url:
        image_url += "composition_vii.jpg"
    return image_url

def get_url_list(data_dir, styles):
    subfix = "mp4" if "video" in data_dir else "jpg"
    filelist = glob.glob(data_dir + "/*." + subfix)
    l = []
    for m in filelist:
        for s in styles:
            if s in m:
                l.append(base_url + m)
    l.sort()
    return l

def get_compare_list(dir1, dir2, styles):
    rng = np.random.RandomState(131071)
    list1 = get_url_list(dir1, styles)
    list2 = get_url_list(dir2, styles)
    print("=> Found %d files in %s" % (len(list1), dir1))
    print("=> Found %d files in %s" % (len(list2), dir2))
    # form list
    l = []
    if "video" in dir1:
        l = [[A,B] for A,B in zip(list1, list2)]
    elif "frame" in dir1:
        list_style = [get_ref_image(x) for x in list1]
        l = [[A,B,S] for A,B,S in zip(list1, list2, list_style)]
    # switch left and right
    for i in range(len(l)):
        if rng.uniform() < 0.5:
            l[i][0], l[i][1] = l[i][1], l[i][0]
    rng.shuffle(l)     
    return l

def get_csv_name(dirs):
    expr_type = "video_stability" if "video" in dirs[0] else "frame_quality"
    model = get_model(dirs[0]) # msra shouldn't be the first model
    losses = [get_loss(d) for d in dirs] 
    losses.sort()
    s = "_".join(losses)
    name = f"expr/{expr_type}_{model}_{s}.csv"
    return name

def write_list(dirs, l):
    fname = get_csv_name(dirs)
    csv_writer = csv.writer(open(fname, 'w'), dialect='excel')
    header = []
    if "video" in dirs[0]:
        header = ["A_url", "B_url"]
    elif "frame" in dirs[0]:
        header = ["A_url", "B_url", "image_url"]
    csv_writer.writerow(header)
    for p in l:
        csv_writer.writerow(p)

def get_full_compare_list(dirs, styles):
    rng = np.random.RandomState(65537)
    n = len(dirs)
    l = []
    for i in range(n):
        for j in range(i + 1, n):
            l.extend(get_compare_list(dirs[i], dirs[j], styles))
    rng.shuffle(l)
    return l

def build_list(dirs, styles):
    print("=> build %s" % ",".join(dirs))
    print("=> style %s" % ",".join(styles))
    write_list(dirs, get_full_compare_list(dirs, styles))

if __name__ == "__main__":
    styles = ["starrynight", "lamuse", "feathers", "composition"]
    dirs = sys.argv[1:]
    l = get_full_compare_list(dirs, styles)
    write_list(dirs, l)
