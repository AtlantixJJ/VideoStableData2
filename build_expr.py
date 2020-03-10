import listop
import os
types = ["video", "frame"]

# sfn flow v.s. diff, diff v.s. none, flow v.s. none
model = "sfn"
losses = ["flow", "diff", "none"]
styles = ["starrynight", "lamuse", "feathers", "composition"]
for t in types:
  dirs = [f"{t}_{model}_{loss}" for loss in losses]
  listop.build_list(dirs, styles, True)

# sfn comb v.s. pixel
model = "sfn"
losses = ["comb", "diff"]
styles = ["starrynight", "lamuse", "feathers", "composition"]
for t in types:
  dirs = [f"{t}_{model}_{loss}" for loss in losses]
  listop.build_list(dirs, styles)

# sfn comb v.s. none
model = "sfn"
losses = ["comb", "none"]
styles = ["starrynight", "lamuse", "feathers", "composition"]
for t in types:
  dirs = [f"{t}_{model}_{loss}" for loss in losses]
  listop.build_list(dirs, styles)

# sfn comb v.s. osn 
styles = ["lamuse", "candy", "udnie", "mosaic"]
for t in types:
  dirs = [f"{t}_sfn_comb", f"{t}_msra"]
  listop.build_list(dirs, styles)

# rnn flow v.s. comb v.s. none
model = "rnn"
losses = ["flow", "comb", "none"]
styles = ["starrynight", "lamuse", "feathers", "composition"]
for t in types:
  dirs = [f"{t}_{model}_{loss}" for loss in losses]
  listop.build_list(dirs, styles, True)
os.system("rm expr/*rnn_flow_none*") 
