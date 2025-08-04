import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET")
))

def get_playlist_by_emotion(emotion):
    query = emotion + " mood"
    results = sp.search(q=query, type='playlist', limit=1)
    if results['playlists']['items']:
        playlist = results['playlists']['items'][0]
        return {
            "name": playlist['name'],
            "url": playlist['external_urls']['spotify'],
            "image": playlist['images'][0]['url']
        }
    return None
