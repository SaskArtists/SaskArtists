"""Reads info.json for each artist and generates a single file"""

import json
import os
import sys

FAIL_ON_MISSING = False

ROOT = "./www/artists"

DEFAULT_ARTIST = {
    "hidden": False,
    "featured": False
}

ATTRIBUTES = {
    "name": {
        "type": type("Wayne Tunison")
    },
    "location": {
        "type": type("Regina")
    },
    "changelog": {
        "type": type([
            "Created by Ryan Aird: 2016",
            "Updated by Brett Mayson: 2018"
        ])
    },
    "hidden": {
        "type": type(False)
    },
    "featured": {
        "type": type(False)
    }
}

fail = False

artists = []

for artist in filter(lambda x: os.path.isdir(os.path.join(ROOT, x)), os.listdir(ROOT)):
    if os.path.exists(os.path.join(ROOT, artist, "artist.json")):
        artists.append(artist)
    elif FAIL_ON_MISSING:
        fail = True
        print("Missing artist.json from {}".format(artist))
    else:
        print("Missing artist.json from {}".format(artist))

if fail:
    sys.exit(1)

output = []

for artist in artists:
    with open(os.path.join(ROOT, artist, "artist.json")) as info:
        data = DEFAULT_ARTIST.copy()
        data.update(json.load(info))
        data["link"] = artist
        for att, props in ATTRIBUTES.items():
            if att not in data:
                fail = True
                print("{} is missing required field {}".format(artist, att))
            elif type(data[att]) != props["type"]:
                fail = True
                print("{} has invalid property type for {}".format(artist, att))
        if data["hidden"]:
            continue
        output.append(data)

if fail:
    sys.exit(1)
else:
    with open("./www/artists.json", "w") as out:
        json.dump(output, out)
    print("artists.json generated")
