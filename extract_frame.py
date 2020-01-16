"""
python extract_frame.py <video_dir> <frame_dir>
"""
import glob, sys, os
import numpy as np
rng = np.random.RandomState(65537)
styles = ["starrynight", "lamuse", "feathers", "composition", "candy", "udnie", "mosaic"]
contents = ['sintel_ambush_1', 'sintel_bamboo_3', 'sintel_market_1', 'sintel_mountain_2', 'sintel_PERTURBED_shaman_1', 'sintel_tiger', 'sintel_temple_1', 'sintel_wall', 'sintel_cave_3', 'sintel_market_4', 'davis_man-bike', 'davis_slackline', 'davis_cats-car', 'davis_girl-dog', 'davis_helicopter', 'davis_guitar-violin', 'davis_subway', 'davis_gym', 'davis_horsejump-stick', 'davis_tandem']

rng_dic = {c:{} for c in contents}
for c in contents:
  rng_dic[c] = {s:rng.randint(0, 1000000) for s in styles}

def find_rng(name):
  for c in contents:
    if c in name: break
  for s in styles:
    if s in name: break
  return rng_dic[c][s]

in_dir, out_dir = sys.argv[1:]
files = glob.glob(in_dir + "/*.mp4")
files.sort()
# temp dir
os.system("mkdir temp")
basecmd = "ffmpeg -loglevel panic -i %s -qscale:v 2 temp/%s"
os.system("rm %s/*.jpg" % out_dir)
for f in files:
  os.system("rm temp/*.jpg")
  ind = f.rfind("/")
  name = f[ind+1:]
  video_name = name.replace(".mp4", "")
  cmd = basecmd % (f, video_name)
  cmd = cmd + "_%05d.jpg"
  print(cmd)
  os.system(cmd)
  num = len(os.listdir("temp"))
  ind = find_rng(name) % num
  print("mv temp/%s_%05d.jpg %s/" % (video_name, ind, out_dir))
  os.system("mv temp/%s_%05d.jpg %s/" % (video_name, ind, out_dir))
