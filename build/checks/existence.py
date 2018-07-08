import re, os, sys

"""
File Existence Check

Errors:
 - Linked file does not exist
"""

rIMG    = r"<img(?:.+?)(?<!:)src=\"(.+?)\"(?:.+?)>"
rLINK   = r"<link(?:.+?)href=\"(.+?)\"(?:.+?)>"
rSCRIPT = r"<script(?:.+?)src=\"(.+?)\"(?:.+?)>"
rA      = r"<a(?:.+?)href=\"(.+?)\"(?:.+?)>"

scandir = ""
try:
    scandir = sys.argv[1]
except IndexError:
    scandir = "."

ret = 0

EXTS = ["html", "php", "inc"]

def check(root, text, regex):
    global ret
    matches = re.finditer(regex, text)
    for matchNum, match in enumerate(matches):
        matchNum = matchNum + 1
        if match.groups():
            src = match.group(1)
            if "http" not in src and not src.startswith("<?php"):
                if not os.path.isfile(src) \
                and not os.path.isfile(os.path.join(root, src)):
                    ret += 1
                    print("File not found:", os.path.join(root, src), src)

for root, dirs, files in os.walk(scandir):
    for f in files:
        if f.split('.')[-1] in EXTS:
            with open(os.path.join(root, f), encoding="utf-8") as f:
                check(root, f.read(), rIMG)
                check(root, f.read(), rLINK)
                check(root, f.read(), rSCRIPT)
                check(root, f.read(), rA)

sys.exit(ret)
