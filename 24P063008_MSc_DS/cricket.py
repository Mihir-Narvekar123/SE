from abc import ABC, abstractmethod
import random

# --- Role classes ---
class Role(ABC):
    @abstractmethod
    def role(self):
        pass

class Batsman(Role):
    def role(self):
        return "Batsman"

class Bowler(Role):
    def role(self):
        return "Bowler"

class WicketKeeper(Role):
    def role(self):
        return "WicketKeeper"

class Captain(Role):
    def role(self):
        return "Captain"

class Fielder(Role):
    def role(self):
        return "Fielder"

# --- Player class ---
class Player:
    def __init__(self, name):
        self.name = name
        self.roles = []

    def add_role(self, role_instance: Role):
        self.roles.append(role_instance)

    def role(self):
        base_role = ["Player"]
        other_roles = [r.role() for r in self.roles]
        return ", ".join(base_role + other_roles)

# --- Team setup ---
def create_team(team_name, players_info):
    team = []
    for info in players_info:
        player = Player(info["name"])
        for role_class in info["roles"]:
            player.add_role(role_class())
        team.append(player)
    return team

# --- India Squad ---
india_players_info = [
    {"name": "Rohit Sharma", "roles": [Captain, Batsman, Fielder]},
    {"name": "Virat Kohli", "roles": [Batsman, Fielder]},
    {"name": "Shubman Gill", "roles": [Batsman, Fielder]},
    {"name": "KL Rahul", "roles": [Batsman, WicketKeeper]},
    {"name": "Hardik Pandya", "roles": [Batsman, Bowler, Fielder]},
    {"name": "Ravindra Jadeja", "roles": [Bowler, Batsman, Fielder]},
    {"name": "Kuldeep Yadav", "roles": [Bowler, Fielder]},
    {"name": "Jasprit Bumrah", "roles": [Bowler, Fielder]},
    {"name": "Mohammed Shami", "roles": [Bowler, Fielder]},
    {"name": "Suryakumar Yadav", "roles": [Batsman, Fielder]},
    {"name": "Rishabh Pant", "roles": [Batsman, WicketKeeper]}
]

# --- Australia Squad ---
australia_players_info = [
    {"name": "Pat Cummins", "roles": [Captain, Bowler, Fielder]},
    {"name": "David Warner", "roles": [Batsman, Fielder]},
    {"name": "Steve Smith", "roles": [Batsman, Fielder]},
    {"name": "Marnus Labuschagne", "roles": [Batsman, Fielder]},
    {"name": "Alex Carey", "roles": [WicketKeeper, Batsman]},
    {"name": "Cameron Green", "roles": [Bowler, Batsman, Fielder]},
    {"name": "Mitchell Marsh", "roles": [Batsman, Fielder]},
    {"name": "Josh Hazlewood", "roles": [Bowler, Fielder]},
    {"name": "Mitchell Starc", "roles": [Bowler, Fielder]},
    {"name": "Glenn Maxwell", "roles": [Batsman, Bowler, Fielder]},
    {"name": "Travis Head", "roles": [Batsman, Fielder]}
]

# Create teams
india_team = create_team("India", india_players_info)
australia_team = create_team("Australia", australia_players_info)

# --- Display teams ---
print("\n🏏 Team India:")
for player in india_team:
    print(f"{player.name} - Roles: {player.role()}")

print("\n🏏 Team Australia:")
for player in australia_team:
    print(f"{player.name} - Roles: {player.role()}")

# --- Match Start ---
print("\n🎉 The match begins between India and Australia!\n")

# Simulate toss
teams = ["India", "Australia"]
toss_winner = random.choice(teams)
toss_decision = random.choice(["bat", "bowl"])

print(f"🪙 {toss_winner} have won the toss and elected to {toss_decision} first.\n")
