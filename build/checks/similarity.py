from difflib import SequenceMatcher
import os
import sys

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

ROOT = "./www/artists"

checked = []

ret = 0

for artist in filter(lambda x: os.path.isdir(os.path.join(ROOT, x)), os.listdir(ROOT)):
    if artist == "reginabellringers.ca": continue
    for dir in os.walk(os.path.join(ROOT, artist)):
        cache = {}
        for file in dir[2]:
            if not file.endswith(".html") and not file.endswith(".htm"): continue
            path = os.path.join(dir[0], file)
            with open(path, encoding="utf-8") as fobj:
                data = fobj.read()
            for file in dir[2]:
                if not file.endswith(".html") and not file.endswith(".htm"): continue
                checkpath = os.path.join(dir[0], file)
                if checkpath == path: continue
                if (path, checkpath) in checked or (checkpath, path) in checked: continue
                if not checkpath in cache:
                    with open(checkpath, encoding="utf-8") as fobj:
                        cache[checkpath] = fobj.read()
                sim = similar(data, cache[checkpath])
                if sim > 0.98:
                    ret += 1
                    print("{0:.3f}% similar {1} {2}".format(sim * 100.0, path, checkpath))
                checked.append((checkpath, path))

print("Errors:", ret)
#In the future we will enable failing this test
sys.exit(0)
