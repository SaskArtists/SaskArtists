import os, sys

invalid_names = ["image","art","picture","pic","img"]

scandir = ""
try:
    scandir = sys.argv[1]
except:
    scandir = "."

ret = 0

for root, dirs, files in os.walk(scandir):
    path = root.split(os.sep)
    for file in files:
        if " " in file:
            ret = 1
            print "Space in filename: ",os.path.join(root,file)
        for i in invalid_names:
            if len(file.replace(i,"")) < 5 and "." in file:
                print "Undescriptive name:",os.path.join(root,file)

sys.exit(ret)
