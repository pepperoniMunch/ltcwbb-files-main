# Define a list, 'roster_list' to include some players
roster_list = ['teoscar hernandez', 'bo bichette', 'robbie "pants" ray']

# Uppercase all player names using a loop
roster_list_upper = ['', '', '']
i = 0
for player in roster_list:
    roster_list_upper[i] = player.title()
    i = i + 1

# Define a dict, 'roster_dict' to include some players and their positions
roster_dict = {
    'RF': 'teoscar hernandez',
    'SS': 'bo bichette',
    'SP': 'robbie "pants" ray'}

# Commands for 'Unpacking', i.e. assigning multiple variables at once
p, rf = ['hyun-jin ryu', 'cavan biggio']


