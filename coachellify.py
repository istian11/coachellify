import argparse
from parse_logic import parse_artists_from_file
from parse_logic import get_artist_ids_for_artists
from spotify_logic import create_coachella_playlist

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--textfile', help='Path to .txt file of artists')
    parser.add_argument('-c', '--clientid', help='Spotify client ID')
    parser.add_argument('-s', '--secret', help='Spotify client secret')
    parser.add_argument('-p', '--playlistname', default='', help='Name of custom playlist')
    parser.add_argument('-n', '--numtracks', default=5, help='Number of tracks to select per artist')
    args = parser.parse_args()

    if not args.textfile or not args.clientid or not args.secret:
        print('You need to provide a .txt file param as well as a Spotify client ID and secret.')
    else:
        artists = parse_artists_from_file(args.textfile)
        artist_ids = get_artist_ids_for_artists(artists)
        playlist_url = create_coachella_playlist(artist_ids, args.clientid, args.secret, args.playlistname, args.numtracks)
        print('Created your Coachella playlist! {url}'.format(url=playlist_url))
