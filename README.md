# Magnetic Swipe Card Jukebox

Fork of [https://github.com/helen/swipe-jukebox]

Changes:
* Python script jukebox.py (instead of shell jukebox.sh)
* Uses [spotify-tui](https://github.com/Rigellute/spotify-tui) instead of `mpd`.
* Format of songs.txt is space-delimited song number, then URI. Anything after URI is ignored (can be used as comment for the name of the song.)

## Steps (to be expanded)
* Set up `spotifyd` and `spotify-tui` on the Raspberry Pi
* Ensure Spotify is set up and audio is working by running `spt play --uri spotify:track:7GhIk7Il098yCjg4BQjzvb`
* Encode and label cards
* Run `curl https://raw.githubusercontent.com/mwm126/swipe-jukebox/master/jukebox.py > jukebox.py`
* [Set root to auto-login](https://www.opentechguides.com/how-to/article/raspberry-pi/5/raspberry-pi-auto-start.html) (unless you want to have to log in every time it reboots)
* [Set `/root/jukebox.py` to run after login](https://www.opentechguides.com/how-to/article/raspberry-pi/5/raspberry-pi-auto-start.html) (unless, again, you want to do this manually every time)
* Swipe card
* Enjoy!