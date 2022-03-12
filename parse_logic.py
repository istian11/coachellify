from consts import ARTISTS_TO_IDS
from consts import get_all_artists

def sanitize_artist_list(parsed_artists):
    # This function removes artists not performing at Coachella 2022 and sanitizes names
    # for misspellings.
    all_artists = get_all_artists()

    parsed_artists_lowercased = [artist.lower() for artist in parsed_artists]
    sanitized_list = []
    for artist in all_artists:
        if artist.lower() in parsed_artists_lowercased:
            sanitized_list.append(artist)
    return sanitized_list

def get_artist_ids_for_artists(artists, order):
    artist_ids = [ARTISTS_TO_IDS.get(artist) for artist in artists]
    if order == 'reverse':
        artist_ids.reverse()
    return artist_ids

def parse_artists_from_file(filename):
    with open(filename, 'r') as f:
        artists = f.read().splitlines()

    artists = sanitize_artist_list(artists)
    return artists