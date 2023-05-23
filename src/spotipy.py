# Path: main.py

# Importing libraries
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials # To access authorised Spotify data
import pandas as pd # for creating the dataframe
import os # (for loading the environment variables)
from dotenv import load_dotenv # For loading the environment variables (API keys and playlist URI's)
from tqdm import tqdm # For the progress bar

# Load the environment variables
def load_environment_variables():
    load_dotenv()
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")
    return client_id, client_secret, playlist_id

# Setting up the credentials
def setup_spotify(client_id, client_secret, playlist_id):
    # Set up client credentials
    credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=credentials_manager)
    playlist = sp.playlist(playlist_id)

    return sp, playlist


# Function to get the tracks, song URI's, genres by artists and artists names from a playlist into a panadas dataframe
def get_tracks_and_artists(playlist, sp):
    df = pd.DataFrame(columns=['artist', 'song_name', 'song_uri', 'artist_genres'])
    # Extract song titles
    song_titles = [track['track']['name'] for track in playlist['tracks']['items']]
    print('Extracting song titles...')
    for i in tqdm(range(len(song_titles))):
        artist = playlist['tracks']['items'][i]['track']['artists'][0]['name']
        song_name = playlist['tracks']['items'][i]['track']['name']
        song_uri = playlist['tracks']['items'][i]['track']['uri']
        artist_genres = sp.artist(playlist['tracks']['items'][i]['track']['artists'][0]['uri'])['genres']
        df.loc[i] = [artist, song_name, song_uri, artist_genres]
    return df

# create a list of the songs and the artists
def get_song_artist_list(df):
    songs = []
    for i in range(len(df)):
        songs.append(df['song_name'][i] + ' - ' + df['artist'][i])
    return songs