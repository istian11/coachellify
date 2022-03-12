import argparse
from consts import ALL_ARTISTS


def sanitize_artist_list(parsed_artists):
    # This function removes artists not performing at Coachella 2022 and sanitizes names
    # for misspellings.
    all_artists_lowercased = [artist.lower() for artist in ALL_ARTISTS]
    sanitized_list = []
    for parsed_artist in parsed_artists:
        if parsed_artist.lower() in all_artists_lowercased:
            artist_index = all_artists_lowercased.index(parsed_artist.lower())
            sanitized_list.append(ALL_ARTISTS[artist_index])

    return sanitized_list

def parse_artists_from_file(filename):
    with open(filename, 'r') as f:
        artists = f.read().splitlines()

    artists = sanitize_artist_list(artists)
    return artists

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--textfile', help='Provide .txt file of artists')
    args = parser.parse_args()

    if not args.textfile:
        print('You need to provide a .txt file param.')
    else:
        artists = parse_artists_from_file(args.textfile)
        print('Artists: {parsed_artists}'.format(parsed_artists=artists))
