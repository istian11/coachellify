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
    parser.add_argument('-n', '--numtracks', default=5, type=int, help='Number of tracks to select per artist')
    parser.add_argument('-o', '--order', default='poster', help='How to order artists in the playlist. Can be "reverse" or "shuffle", set to "poster" by default.')
    args = parser.parse_args()

    if not args.textfile or not args.clientid or not args.secret:
        print('You must provide a .txt file as well as a Spotify client ID and secret.')
    else:
        artists = parse_artists_from_file(args.textfile)
        artist_ids = get_artist_ids_for_artists(artists, args.order)
        playlist_url = create_coachella_playlist(artist_ids, args.clientid, args.secret, args.playlistname, args.numtracks, args.order)
        print('Created your Coachella playlist! {url}'.format(url=playlist_url))
