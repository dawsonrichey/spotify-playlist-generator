# spotify-playlist-generator
The spotify-playlist-generator project is a Python-based tool designed to automate the creation of Spotify playlists. At its core, the createPlaylistTitle.py file contains a function that generates a standardized title for these playlists.

<!-- The create_playlist_title() function in createPlaylistTitle.py dynamically creates a playlist title based on the current date. It formats the title as "Discover [YEAR] - w[WEEK_NUMBER]", where YEAR is the current year and WEEK_NUMBER is the week number of the year. This naming convention allows for consistent and chronological organization of playlists.


 -->



The spotify-playlist-generator project is a Python-based tool that interacts with the Spotify Web API to create personalized playlists. At the core of this project is the createPlaylistTitle.py file, which generates dynamic titles for playlists based on the current date or a specified date.

createPlaylistTitle.py contains a function that creates a playlist title in the format "Discover YYYY - wWW", where YYYY represents the year and WW represents the week number. This naming convention allows for easy tracking and organization of playlists over time.

The project likely utilizes various Spotify Web API endpoints to fetch user data, search for tracks, and create playlists. It may include features such as:

Authentication and authorization using Spotify's OAuth 2.0 flow
Retrieving user's listening history and preferences
Generating personalized track recommendations
Creating and populating playlists with selected tracks
Managing playlist metadata and settings

By leveraging the Spotify Web API, this project offers users a way to automatically generate curated playlists tailored to their musical tastes, potentially on a weekly basis. This can enhance the music discovery experience and provide a convenient way for users to explore new tracks aligned with their preferences.




## Requirements
[Spotify Account](https://www.spotify.com/)

[Spotify Developer Account](https://developer.spotify.com/)

[Create a Web App](https://developer.spotify.com/dashboard)


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



Clone the repository:

git clone https://github.com/your-username/spotify-playlist-generator.git
cd spotify-playlist-generator


Set up a virtual environment (optional but recommended):
```   
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required dependencies:

```pip install -r requirements.txt```


Set up Spotify API credentials:

Go to the Spotify Developer Dashboard (https://developer.spotify.com/dashboard/)

Create a new application
Note down the Client ID and Client Secret
Configure your environment variables:

Create a .env file in the project root
Add your Spotify API credentials:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

Run the script:

```python main.py```


Now you're all set to use the spotify-playlist-generator! The script will use the createPlaylistTitle.py module to generate playlist titles and interact with the Spotify Web API to create your personalized playlists.