from consts import get_all_artists_map

def sanitize_artist_list(parsed_artists):
    # This function removes artists not performing at Coachella 2022 and sanitizes names
    # for misspellings.
    all_artists_map = get_all_artists_map()
    all_artists = list(all_artists_map.keys())

    all_artists_lowercased = [artist.lower() for artist in all_artists]
    sanitized_list = []
    for parsed_artist in parsed_artists:
        if parsed_artist.lower() in all_artists_lowercased:
            artist_index = all_artists_lowercased.index(parsed_artist.lower())
            sanitized_list.append(all_artists[artist_index])

    return sanitized_list

def get_artist_ids_for_artists(artists):
    all_artists_map = get_all_artists_map()
    return [all_artists_map.get(artist) for artist in artists]

def parse_artists_from_file(filename):
    with open(filename, 'r') as f:
        artists = f.read().splitlines()

    artists = sanitize_artist_list(artists)
    return artists