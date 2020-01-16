import os, sys
baseurl = "https://github.com/AtlantixJJ/VideoStableData/raw/master/images"
dic = {
  "starrynight" : baseurl + "/starry_night_tr.jpg",
  "lamuse" : baseurl + "/la_muse_tr.jpg",
  "composition" : baseurl + "/composition_vii_tr.jpg",
  "feathers" : baseurl + "/feathers_tr.jpg"
}
f = open(sys.argv[1], "r")
head = f.readline()
lines = f.readlines()
f.close()
f = open(sys.argv[2], "w")
f.write(head.strip() + ",image_url\n")
for l in lines:
  for k,v in dic.items():
    if k in l:
      f.write(l.strip() + "," + v + "\n")
      break
f.close()
