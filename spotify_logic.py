import random
import spotipy
from spotipy import oauth2

SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = ('user-library-read,playlist-read-private,playlist-modify-private,playlist-modify-public,user-read-private')

def authorize_and_get_spotipy_manager(client_id, client_secret):
    sp_oauth = oauth2.SpotifyOAuth(client_id, client_secret, SPOTIPY_REDIRECT_URI, scope=SCOPE)
    # Click "Accept" in your browser when the auth window pops up
    code = sp_oauth.get_auth_response(open_browser=True)
    token = sp_oauth.get_access_token(code)
    refresh_token = token['refresh_token']
    return spotipy.Spotify(auth=token['access_token'])

def get_top_tracks_ids_for_artist_id(spotify_manager, artist_id, num_tracks_per_artist):
    top_tracks = spotify_manager.artist_top_tracks(artist_id).get('tracks')[0:num_tracks_per_artist]
    return [track.get('id') for track in top_tracks]

def get_current_user_playlists(spotify_manager):
    current_user = spotify_manager.current_user()
    playlists = spotify_manager.user_playlists(current_user.get('id'))
    return [playlist.get('name') for playlist in playlists.get('items')]

def create_coachella_playlist(artist_ids, client_id, client_secret, custom_playlist_name, num_tracks_per_artist, order):
    spotify_manager = authorize_and_get_spotipy_manager(client_id, client_secret)

    # aggregate all songs for playlist
    all_track_ids = []
    for artist_id in artist_ids:
        track_ids = get_top_tracks_ids_for_artist_id(spotify_manager, artist_id, num_tracks_per_artist)
        all_track_ids.extend(track_ids)
    if order == 'shuffle':
        random.shuffle(all_track_ids)

    # check if requested playlist name already exists
    playlist_name = custom_playlist_name or 'My Coachella 2022 Playlist'
    user_playlists = get_current_user_playlists(spotify_manager)
    unique_suffix = '1'
    while (playlist_name in user_playlists):
        playlist_name = '{playlist_name} {suffix}'.format(playlist_name=playlist_name, suffix=unique_suffix)

    # create playlist
    user = spotify_manager.current_user()
    coachella_playlist = spotify_manager.user_playlist_create(user.get('id'), name=playlist_name)
    spotify_manager.user_playlist_add_tracks(user.get('id'), coachella_playlist.get('id'), all_track_ids)
    return coachella_playlist.get('external_urls').get('spotify')