import sys
import os
#model: sfn, adain, rnn
model = sys.argv[1]
subfix = "jpg"
mtd = ["flow","comb","diff", "none"]
basedir = "%s_%s_%s/"

# build frames
for m in mtd:
  in_dir = basedir % ("video", model, m)
  out_dir = in_dir.replace("video", "frame")
  os.system("mkdir %s" % out_dir)
  os.system("rm %s/*.jpg" % out_dir)
  cmd = "python extract_frame.py %s %s" % (in_dir, out_dir)
  print(cmd)
  os.system(cmd)

