def is_vladdy(player_name):
    """
    a function that assesses whether the entered player name
    is vladdy or not
    """
    return player_name.replace("'", '').lower() == 'vladdy'
