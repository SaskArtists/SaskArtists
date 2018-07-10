from difflib import SequenceMatcher
import os
import sys

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

ROOT = "./www/artists"

ret = 0

for artist in filter(lambda x: os.path.isdir(os.path.join(ROOT, x)), os.listdir(ROOT)):
    for dir in os.walk(os.path.join(ROOT, artist)):
        for file in dir[2]:
            if not file.endswith(".html"): continue
            path = os.path.join(dir[0], file)
            with open(path, encoding="utf-8") as fobj:
                data = fobj.read()
            for file in dir[2]:
                if not file.endswith(".html"): continue
                checkpath = os.path.join(dir[0], file)
                if checkpath == path: continue
                with open(checkpath, encoding="utf-8") as fobj:
                    checkdata = fobj.read()
                sim = similar(data, checkdata)
                if sim > 0.99:
                    ret += 1
                    print("{0:.3f}% similar {1} {2}".format(sim * 100.0, path, checkpath))

print("Errors:", ret)
#In the future we will enable failing this test
sys.exit(0)
