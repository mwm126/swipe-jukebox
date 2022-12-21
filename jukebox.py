#!/usr/bin/python3

""" Python script to run Spotify Jukebox with spotify-tui """

from pathlib import Path
from subprocess import run

DEVICE = "raspotify"
SONG_URL = "https://raw.githubusercontent.com/mwm126/swipe-jukebox/master/songs.txt"
SONGS_TXT = Path(__file__).parent / "songs.txt"

print("Updating song list...")
song_list = run(["curl", "-s", "-S", SONG_URL, "-o", SONGS_TXT.as_posix()], check=False)
if song_list.returncode:
    print("Could not update songlist.")
else:
    print("Got latest songlist.")

print("Jukebox started!")

while True:
    swipe = input("Swipe: ")
    tracks = swipe.split("?")
    if not tracks:
        print("Could not parse card: ", swipe)
        continue
    SWIPE_NUM = "".join([char for char in track[0] if char.isdigit()])

    if not SWIPE_NUM:
        print("no swipe_num")
        continue

    if SWIPE_NUM == "999":
        print("toggle")
        # run(["spt", "playback", "--toggle", "--device", DEVICE], check=False)
        continue

    with open(SONGS_TXT, encoding="utf8") as songs:
        for line in songs:
            fields = line.split()
            if len(fields) < 2:
                continue
            song_num, uri, *rest = fields
            desc = " ".join(rest)
            if song_num == SWIPE_NUM:
                print("Playing: song #", SWIPE_NUM, " ", desc)
                break
        else:
            print("Not found: song #", SWIPE_NUM)
            continue

    # run(["spt", "play", "--device", DEVICE, "--uri", uri], check=False)
