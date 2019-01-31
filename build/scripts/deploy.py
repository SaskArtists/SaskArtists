"""Deploys changed files to saskartists.ca"""

import os
import subprocess
import sys
import urllib.request

DIR = "/tmp/project/workspace/build-output/deploy-info/"
COMMIT_FILE = DIR + "commit"

WEB = "saskartists.ca"
ENDPOINT = f"saskarti@{WEB}"
DEST = f"{ENDPOINT}:/home/saskarti"

COMMIT_CURR = subprocess.getoutput("git rev-parse HEAD")
print(f"COMMIT_CURR {COMMIT_CURR}")

def run(cmd):
    os.system(f"{cmd} > /dev/null")

def save():
    if not os.path.exists(DIR):
        os.makedirs(DIR)
    with open(COMMIT_FILE, "w") as out:
        out.write(COMMIT_CURR)
    run(f"scp -oStrictHostKeyChecking=no -r {COMMIT_FILE} {DEST}/www/commit")

try:
    response = urllib.request.urlopen(f"https://{WEB}/commit")
    COMMIT_PREV = response.read().decode("utf8").strip()
    print(f"COMMIT_PREV {COMMIT_PREV}")
except Exception as e:
    print(str(e))
    print("Unable to read commit file from remote, sending all")
    run(f"scp -oStrictHostKeyChecking=no -r www/* {DEST}/www")
    run(f"scp -oStrictHostKeyChecking=no -r www/.htaccess {DEST}/www/.htaccess")
    save()
    sys.exit(0)

#Files that have been modified since the last CircleCI build
CHANGED_FILES = subprocess.getoutput(f"git diff --name-only {COMMIT_PREV} {COMMIT_CURR}")
CHANGED_FILES = CHANGED_FILES.split("\n")

print("Processing Changed Files")

for FILE in CHANGED_FILES:
    if not FILE.startswith("www/"):
        print(f"SKIPPING: {FILE}")
        continue
    if not os.path.exists(FILE):
        print(f"FILE DELETED: {FILE}")
        run(f"ssh {ENDPOINT} \"rm -f {DEST}/{FILE}\"")
    else:
        print(f"SENDING FILE: {FILE}")
        run(f"scp -oStrictHostKeyChecking=no -r {FILE} {DEST}/{FILE}")

save()
