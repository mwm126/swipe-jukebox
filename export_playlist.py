import os
import re

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")

# change for your target playlist
PLAYLIST_LINK = (
    "https://open.spotify.com/playlist/23Q8kLlDOrOtUnEfzffo3p?si=j3TMxDokQzqL_c34H0t0Ow"
)

client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
session = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", PLAYLIST_LINK):
    playlist_uri = match.groups()[0]
else:
    raise ValueError("Expected format: https://open.spotify.com/playlist/...")

tracks = session.playlist_tracks(playlist_uri)["items"]
for song_num, track in enumerate(tracks):
    uri = track["track"]["uri"]
    name = track["track"]["name"]
    ARTISTS = ", ".join([artist["name"] for artist in track["track"]["artists"]])
    print(f"{song_num+1:03d}   {uri}   {name} ({ARTISTS})")
