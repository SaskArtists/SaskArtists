"""Deploys changed files to saskartists.ca"""

import os
import subprocess
import sys

DIR = "/tmp/project/workspace/build-output/deploy-info/"
COMMIT_FILE = DIR + "commit"

DEST = "saskarti@saskartists.ca:/home/saskarti/www"

COMMIT_CURR = subprocess.getoutput("git rev-parse HEAD")
print(f"COMMIT_CURR {COMMIT_CURR}")

def run(cmd):
    os.system(f"{cmd} > /dev/null")

def save():
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    with open(COMMIT_FILE, "w") as out:
        out.write(COMMIT_CURR)

if os.path.exists(COMMIT_FILE):
    with open(COMMIT_FILE) as f:
        COMMIT_PREV = f.read().strip()
        print(f"COMMIT_PREV {COMMIT_PREV}")
else:
    print("no previous commit, sending all")
    run(f"scp -oStrictHostKeyChecking=no -r www/* {DEST}")
    run(f"scp -oStrictHostKeyChecking=no -r www/.htaccess {DEST}/.htaccess")
    save()
    sys.exit(0)

#Files that have been modified since the last CircleCI build
CHANGED_FILES = subprocess.getoutput(f"git diff --name-only {COMMIT_PREV} {COMMIT_CURR}")
CHANGED_FILES = CHANGED_FILES.split("\n")

print(CHANGED_FILES)

save()
