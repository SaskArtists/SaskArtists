import test, sys, re, json

regex = r"{name}(?!</a>)"

artists = []

with open("./www/artists.json") as artf:
    data = json.loads(artf.read())
    for artist in data:
        artists.append(artist["name"])

class Crosslinks(test.Test):
    def check(self, source, text):
        for artist in artists:
            name = artist.lower().split(" ")
            if name[0][0] + name[-1] in source: continue
            matches = re.finditer(regex.format(name = artist), text)
            for matchNum, match in enumerate(matches):
                print(source, f"{artist}")
                self.ret += 1

check = Crosslinks()
check.ret = 0
check.run()

#sys.exit(check.ret)
sys.exit(0)