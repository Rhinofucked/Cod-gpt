import random

def assign_teams(users, players_per_team):
    random.shuffle(users)
    return [users[i:i + players_per_team] for i in range(0, len(users), players_per_team)]
