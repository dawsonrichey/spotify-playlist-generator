import spotipy
import spotipy.util as util
import datetime
import os
import createPlaylistTitle
from dotenv import load_dotenv

load_dotenv()

SPOTIPY_USERNAME = os.getenv('SPOTIPY_USERNAME')
SPOTIPY_SOURCE_PLAYLIST_ID = os.getenv('SPOTIPY_SOURCE_PLAYLIST_ID')
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')


def copy_playlist(SPOTIPY_USERNAME, SPOTIPY_SOURCE_PLAYLIST_ID, new_playlist_name):
    # Authentication
    scope = 'playlist-modify-public playlist-modify-private'  # Permissions needed
    token = util.prompt_for_user_token(SPOTIPY_USERNAME, scope)

    if token:
        sp = spotipy.Spotify(auth=token)

        # Get tracks from the source playlist
        results = sp.playlist_items(SPOTIPY_SOURCE_PLAYLIST_ID)
        track_ids = [track['track']['id'] for track in results['items']]

        # Create new playlist
        new_playlist = sp.user_playlist_create(SPOTIPY_USERNAME, new_playlist_name, public=True)
        new_playlist_id = new_playlist['id']

        # Add tracks to the new playlist (API has limits, might need multiple calls)
        sp.playlist_add_items(new_playlist_id, track_ids) 

    else:
        print("Can't get token for", SPOTIPY_USERNAME)



# Example usage
# Get the current date
today = datetime.date.today()
date_string = today.strftime("%Y-%m-%d")

createPlaylistTitle.create_playlist_title()

copy_playlist(SPOTIPY_USERNAME, SPOTIPY_SOURCE_PLAYLIST_ID, createPlaylistTitle.create_playlist_title())

