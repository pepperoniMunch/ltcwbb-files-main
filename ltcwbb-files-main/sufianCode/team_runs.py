blue_jays_runs = 6
yankees_runs = 5

blue_jays_won = (blue_jays_runs > yankees_runs)
yankees_won = (yankees_runs > blue_jays_runs)

teams_tied = (blue_jays_runs == yankees_runs)
no_tie = (blue_jays_runs != yankees_runs)

# print(max(blue_jays_runs, yankees_runs))

winner = max(blue_jays_runs, yankees_runs)
loser = min(blue_jays_runs, yankees_runs)

# print(winner)
# print(loser)

if blue_jays_won:
    message = "Nice job Blue Jays!"
elif yankees_won:
    message = "Nice job Yankees!"
else:
    message = "Tie game!"

print(message)