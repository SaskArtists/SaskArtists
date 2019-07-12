import os, sys

invalid_names = ["image","art","picture","pic","img"]
invalid_characters = ["(",")","'","\"","%","&","^","=","+","?",","]
invalid_end_char = ["_","."]

scandir = ""
try:
    scandir = sys.argv[1]
except:
    scandir = "."

ret = 0

for root, dirs, files in os.walk(scandir):
    path = root.split(os.sep)
    for file in files:
        #Reginabellringers.ca exception
        if  "reginabellringers.ca" in os.path.join(root, file) \
            or ".git" in os.path.join(root, file) \
            or os.path.join(root, file) == "./README.md":
            break
        if "test.py" in file:
            continue
        if " " in file:
            ret += 1
            print("Space in filename: ", os.path.join(root, file))
        if file.lower() != file:
            ret += 1
            print("Capital letter in filename: ", os.path.join(root, file))
        for i in invalid_characters:
            if i in file:
                print("Invalid Character "+i+":", os.path.join(root, file))
                ret += 1
        for i in invalid_end_char:
            if file[-1] == i:
                print("Invalid Ending "+i+":", os.path.join(root, file))
                ret += 1
        for i in invalid_names:
            if len(file.replace(i, "")) < 8 and "." in file:
                print("Undescriptive name:", os.path.join(root, file))
                ret += 1
                break

sys.exit(ret)
