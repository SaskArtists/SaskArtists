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

import test

class Existence(test.Test):
    def check(self, source, text):
        for regex in [rIMG, rLINK, rSCRIPT, rA]:
            matches = re.finditer(regex, text)
            for matchNum, match in enumerate(matches):
                matchNum = matchNum + 1
                if match.groups():
                    src = match.group(1)
                    if "http" not in src and not src.startswith("<?php"):
                        if not os.path.isfile(source):
                            self.ret += 1
                            print("File not found:", os.path.join(root, src), src)

check = Existence(["html", "htm", "php", "inc"])
check.ret = 0
check.run()
sys.exit(check.ret)
