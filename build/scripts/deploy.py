"""Deploys changed files to saskartists.ca"""

import os
import subprocess
import sys

def h(path):
    """Helper to expand the user home directory"""
    return os.path.expanduser(path)

#Get Environment Variables

COMMIT_CURR = subprocess.getoutput("git rev-parse HEAD")

if os.path.exists(h("~/deploy-info/commit")):
    with open(h("~/deploy-info/commit")) as f:
        COMMIT_PREV = f.read().strip()
else:
    os.system("scp -oStrictHostKeyChecking=no -r * saskarti@saskartists.ca:/home/saskarti/www/")
    os.system("scp -oStrictHostKeyChecking=no -r .htaccess saskarti@saskartists.ca:/home/saskarti/www/.htaccess")
    with open(h("~/deploy-info/commit"), "w") as f:
        f.write(COMMIT_CURR)
    sys.exit(0)

#Files that have been modified since the last CircleCI build
CHANGED_FILES = subprocess.getoutput("git diff --name-only {} {}".format(COMMIT_PREV, COMMIT_CURR))
CHANGED_FILES = CHANGED_FILES.split("\n")

print(CHANGED_FILES)

with open(h("~/deploy-info/commit"), "w") as f:
    f.write(COMMIT_CURR)
