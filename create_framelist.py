import os
import sys
model = sys.argv[1]
comtype = sys.argv[2]
if comtype == "frame":
  mid = "compare_framequality_%s_%s_%s.csv"
  fin = "compare_framequality_%s_%s_%s_%s.csv"
  subfix = "jpg"
elif comtype == "video":
  mid = "compare_videostability_%s_%s_%s.csv"
  fin = "compare_videostability_%s_%s_%s_%s.csv"
  subfix = "mp4"
mtd = ["flow","comb","none"]
basedir = "data/%s_%s_%s/"
basecmd = "python compare2dir_wl.py %s %s %s %s"
for pm, cm in zip(mtd[:-1],mtd[1:]):
  pd = basedir % (comtype, model, pm)
  cd = basedir % (comtype, model, cm)
  cmd = basecmd % (pd, cd, mid % (model, pm, cm), comtype)
  print(cmd)
  os.system(cmd)
basecmd = "python mixrows.py %s,%s %s"
cmd = basecmd % (mid % (model, mtd[0], mtd[1]), mid % (model, mtd[1], mtd[2]), fin % (model, mtd[0], mtd[1], mtd[2]))
print(cmd)
os.system(cmd)
