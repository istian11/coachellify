DAY_1_ARTISTS = {
    'Harry Styles': '6KImCVD70vtIoJWnq6nGn3',
    'Daniel Caesar': '20wkVLutqVOYrc0kxFs7rA',
    'Madeon': '4pb4rqWSoGUgxm63xmJ8xc',
    'NIKI': '2kxP07DLgs4xlWz8YHlvfh',
}

DAY_2_ARTISTS = {
    'Billie Eilish': '6qqNVTkY8uBg9cP3Jd7DAH',
    'Megan Thee Stallion': '181bsRPaVXVlUKXrxwZfHK',
    'Disclosure': '6nS5roXSAGhTGr34W6n7Et',
    'Japanese Breakfast': '7MoIc5s9KXolCBH1fy9kkw',
}

DAY_3_ARTISTS = {
    'Kanye West': '5K4W6rqBFWDnAN6FQUkS6x',
    'Doja Cat': '5cj0lLjcoR7YOSnhnX0Po5',
    'Joji': '3MZsBdqDrRTJihTHQrO6Dq',
    'Vince Staples': '68kEuyFKyqrdQQLLsmiatm',
}

def get_all_artists_map():
    all_artists_map = {}
    all_artists_map.update(DAY_1_ARTISTS)
    all_artists_map.update(DAY_2_ARTISTS)
    all_artists_map.update(DAY_3_ARTISTS)
    return all_artists_map
