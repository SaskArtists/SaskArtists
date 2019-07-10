import os
import subprocess
import sys

ROOT = "./www/artists"

ret = 0

with open("./build/spelling_allowed.txt") as fobj:
    allowed = fobj.read().split("\n")

import test

class Spelling(test.Test):
    def check(self, source, text):
        if source == "./www/artists/ahasiw/sake.htm": return
        errors = subprocess.getoutput("cat {} | aspell -a -H --master=en_US --extra-dicts=en_GB".format(source)).split("\n")[1:]
        for line in errors:
            if line.strip() in ["*", ""]: return
            self.word = line.strip().split(" ")[1]
            if self.word in allowed: return
            print(path, line.split(":")[0])
            self.ret += 1
            if self.word in self.most:
                self.most[self.word] += 1
            else:
                self.most[self.word] = 1

check = Spelling()
check.most = {}
check.ret = 0
check.run()

for spelling in sorted(check.most.items(), key=lambda x: x[1]):
    print(spelling)

#In the future we will enable failing
print("Errors:", ret)
sys.exit(ret>0)
