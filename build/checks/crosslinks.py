import test, sys, re, json

regex = r"{name}(?!</a>)"

artists = []

with open("./www/artists.json") as artf:
    data = json.loads(artf.read())
    for artist in data:
        artists.append({"link": artist["link"], "name": artist["name"]})

class Crosslinks(test.Test):
    def check(self, source, text):
        for artist in artists:
            link = artist["link"].lower()
            if link in source:
                continue
            matches = re.finditer(regex.format(name = artist["name"]), text)
            for _ in enumerate(matches):
                artistName = artist["name"]
                print(source, f"{artistName}")
                self.ret += 1

check = Crosslinks()
check.ret = 0
check.run()

sys.exit(check.ret)
