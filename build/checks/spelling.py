import os
import subprocess
import sys

ROOT = "./www/artists"

ret = 0

#with open("./build/spelling_allowed.txt") as fobj:
#    allowed = fobj.read().split("\n")

most = {}

for artist in filter(lambda x: os.path.isdir(os.path.join(ROOT, x)), os.listdir(ROOT)):
    print(artist)
    for dir in os.walk(os.path.join(ROOT, artist)):
        for file in dir[2]:
            if not file.endswith(".html"): continue
            path = os.path.join(dir[0], file)
            print(path)
            errors = subprocess.getoutput("cat {} | aspell -a -H".format(path)).split("\n")[1:]
            for line in errors:
                print(line)
                if line.strip() in ["*", ""]: continue
                word = line.strip().split(" ")[1]
                if word in allowed: continue
                print(path, line.split(":")[0])
                ret += 1
                if word in most:
                    most[word] += 1
                else:
                    most[word] = 1

for spelling in sorted(most.items(), key=lambda x: x[1]):
    print(spelling)

#In the future we will enable failing
print("Errors:", ret)
sys.exit(ret>0)
