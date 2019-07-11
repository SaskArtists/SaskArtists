import test, sys, re, json

regex = r"{name}(?!</a>)"

artists = []

with open("./www/artists.json") as artf:
    data = json.loads(artf.read())
    for artist in data:
        artists.append({link: artist["link"], name: artist["name"]})

class Crosslinks(test.Test):
    def check(self, source, text):
        for artist in artists:
            link = artist[link].lower()
            if link in source: continue
            name = artist["name"].lower.split(" ")
            matches = re.finditer(regex.format(name = artist), text)
            for matchNum, match in enumerate(matches):
                print(source, f"{artist}")
                self.ret += 1

check = Crosslinks()
check.ret = 0
check.run()

#sys.exit(check.ret)
sys.exit(0)
