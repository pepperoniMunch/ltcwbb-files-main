# Define a list, 'roster_list' to include some players
roster_list = ['teoscar hernandez', 'bo bichette', 'robbie "pants" ray']

# Uppercase all player names using a for loop (which are iterable)
roster_list_upper = ['', '', '']
i = 0
for player in roster_list:
    roster_list_upper[i] = player.title()
    i = i + 1

# Uppercase all player names using a comprehension
roster_list_proper = [x.title() for x in roster_list]

# Split first name from last name using a comprehension (this won't work for
# Robbie Ray because Ray is the [3] index in the string 'Robbie "Pants" Ray'
roster_last_names = [full_name.split(' ')[1] for full_name in roster_list]

# Filter a comprehension to include only certain items from the list.
# For example, here we will query only last names that start with 'b'
roster_b_only = [x.title() for x in roster_list if x.startswith('b')]

# Define a dict, 'roster_dict' to include some players and their positions. Note that dicts are also iterable.
roster_dict = {
    'RF': 'teoscar hernandez',
    'SS': 'bo bichette',
    'SP': 'robbie "pants" ray'}

# Accessing the keys of a dict
for x in roster_dict:
    print(f"position: {x}")

# Accessing the values of a dict
for x in roster_dict:
    print(f"Position: {x}")
    print(f"Player: {roster_dict[x]}")

# Alternate route to accessing values of a dict
for x, y in roster_dict.items():
    print(f"Position: {x}")
    print(f"Player: {y}")

# Commands for 'Unpacking', i.e. assigning multiple variables at once
p, rf = ['hyun-jin ryu', 'cavan biggio']

# Dict comprehensions are wrapped in curly brackets rather than square brackets
salary_per_player = {
    'hyun-jin ryu': 31000000,
    'bo bichette': 27000000,
    'teoscar hernandez': 11500000}

salary_m_per_upper_player = {
    name.upper(): salary/1000000 for name, salary, in salary_per_player.items()
}

sum([salary for _, salary in salary_per_player.items()])
