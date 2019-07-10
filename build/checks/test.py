import os, sys

ROOT = "./www/artists"

class Test:
    def __init__(self, extensions=["html","htm"]):
        self.extensions = extensions

    def run(self):
        for artist in filter(lambda x: os.path.isdir(os.path.join(ROOT, x)), os.listdir(ROOT)):
            if artist == "reginabellringers.ca": continue
            for dir in os.walk(os.path.join(ROOT, artist)):
                for f in dir[2]:
                    if f.split('.')[-1] in self.extensions:
                        name = os.path.join(dir[0], f)
                        with open(name, encoding="utf-8") as fobj:
                            try:
                                self.check(name, fobj.read())
                            except UnicodeDecodeError:
                                print(f"Invalid unicode {name}")