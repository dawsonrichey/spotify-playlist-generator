# spotify-playlist-generator

## Requirements
[Spotify account](https://www.spotify.com/)
[spotify developer account](https://developer.spotify.com/)
[Create a web app](https://developer.spotify.com/dashboard)


### Redirect URIs
http://localhost:8888/callback

### APIs used
Web API
Web Playback SDK


This project was built using 
python version 3.11.6

Create Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

Make Credentials File
- Make a copy of .env.copy and rename it .env then enter your projects information into the provided fields.

Install
```
pip install python-dotenv spotipy
```
Run Project 
```
python3 spotifyGooglePlaylistGenerator.py
```
Running this file with trigger your browser to open a window to authorize your spotify account.

### To Do
- [X] Add a readme
- [ ] Provide links and instruction to set up a spotify developer account & app
- [X] make sure importEnv.py is not in use before removing from project
- [ ] fix to do list formatting
- [ ] add cron file and instructions
