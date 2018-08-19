"""Deploys changed files to saskartists.ca"""

import os
import subprocess
import sys

#Get Environment Variables

COMMIT_CURR = subprocess.getoutput("git rev-parse HEAD")
print("COMMIT_CURR {}".format(COMMIT_CURR))

if os.path.exists("./deploy-info/commit"):
    with open("./deploy-info/commit") as f:
        COMMIT_PREV = f.read().strip()
        print("COMMIT_PREV {}".format(COMMIT_PREV))
else:
    os.system("scp -oStrictHostKeyChecking=no -r www/* saskarti@saskartists.ca:/home/saskarti/www/")
    os.system("scp -oStrictHostKeyChecking=no -r www/.htaccess saskarti@saskartists.ca:/home/saskarti/www/.htaccess")
    with open("./deploy-info/commit", "w") as f:
        f.write(COMMIT_CURR)
    sys.exit(0)

#Files that have been modified since the last CircleCI build
CHANGED_FILES = subprocess.getoutput("git diff --name-only {} {}".format(COMMIT_PREV, COMMIT_CURR))
CHANGED_FILES = CHANGED_FILES.split("\n")

print(CHANGED_FILES)

with open("./deploy-info/commit", "w") as f:
    f.write(COMMIT_CURR)
